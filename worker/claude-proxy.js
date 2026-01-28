/**
 * CLOUDFLARE WORKER - Proxy para Claude API
 * English Tutor B1 - UNED
 *
 * INSTRUCCIONES DE DESPLIEGUE:
 * 1. Ve a https://dash.cloudflare.com
 * 2. Workers & Pages > Create Application > Create Worker
 * 3. Nombra el worker: "english-tutor"
 * 4. Pega este código
 * 5. Settings > Variables > Add Variable:
 *    - Name: ANTHROPIC_API_KEY
 *    - Value: tu-api-key-de-anthropic
 *    - Encrypt: Yes
 * 6. Guarda y despliega
 * 7. Copia la URL del worker y actualiza API.workerUrl en api.js
 */

export default {
  async fetch(request, env) {
    // CORS headers
    const corsHeaders = {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type',
    };

    // Handle CORS preflight
    if (request.method === 'OPTIONS') {
      return new Response(null, { headers: corsHeaders });
    }

    // Only allow POST
    if (request.method !== 'POST') {
      return new Response(JSON.stringify({ error: 'Method not allowed' }), {
        status: 405,
        headers: { ...corsHeaders, 'Content-Type': 'application/json' },
      });
    }

    try {
      // Parse request body
      const body = await request.json();
      const { system, messages } = body;

      if (!messages || !Array.isArray(messages)) {
        return new Response(JSON.stringify({ error: 'Invalid messages format' }), {
          status: 400,
          headers: { ...corsHeaders, 'Content-Type': 'application/json' },
        });
      }

      // Call Claude API
      const anthropicResponse = await fetch('https://api.anthropic.com/v1/messages', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'x-api-key': env.ANTHROPIC_API_KEY,
          'anthropic-version': '2023-06-01',
        },
        body: JSON.stringify({
          model: 'claude-sonnet-4-20250514',
          max_tokens: 1024,
          system: system || 'You are a helpful English tutor.',
          messages: messages,
        }),
      });

      if (!anthropicResponse.ok) {
        const errorText = await anthropicResponse.text();
        console.error('Anthropic API error:', errorText);
        return new Response(JSON.stringify({ error: 'API error', details: errorText }), {
          status: anthropicResponse.status,
          headers: { ...corsHeaders, 'Content-Type': 'application/json' },
        });
      }

      const data = await anthropicResponse.json();

      // Extract text content
      const content = data.content?.[0]?.text || 'No response generated.';

      return new Response(JSON.stringify({ content }), {
        status: 200,
        headers: { ...corsHeaders, 'Content-Type': 'application/json' },
      });

    } catch (error) {
      console.error('Worker error:', error);
      return new Response(JSON.stringify({ error: 'Internal error', message: error.message }), {
        status: 500,
        headers: { ...corsHeaders, 'Content-Type': 'application/json' },
      });
    }
  },
};
