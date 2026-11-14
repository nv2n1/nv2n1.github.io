---
title: "register_trace_handler(3)"
name: "register_trace_handler"
section: "3"
letter: "r"
url: "/docs/linux/man/3-register_trace_handler/"
description: "register_trace_handler – Registers a custom handler for trace output. Allegro game programming library."
---

<p>register_trace_handler &#8211; Registers a custom handler for trace output. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void register_trace_handler(int (*handler)(const char *msg));</code></pre>
<h2>Description</h2>
<p>Supplies a custom handler function for dealing with trace output. Your callback will be passed a formatted error message in ASCII, and should return non-zero if it has processed the message, or zero to continue with the default actions. You could use this to ignore trace output, or to display the messages on a second monochrome monitor, etc. You can call this function even when Allegro has not been initialised. Example: </p>
<pre><code>int network_broadcaster(const char *text)
{
    int f;

      for (int f = 0; f
         send_msg_to_client(client[f], text);

      return 0; /* Let normal tracing occur. */
}
... register_trace_handler(network_broadcaster);
TRACE(&quot;Networked tracing activated
&quot;);
</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-al_trace/">al_trace</a></code>(3), <code><a href="/docs/linux/man/3-trace/">TRACE</a></code>(3), <code><a href="/docs/linux/man/3-register_assert_handler/">register_assert_handler</a></code>(3) </p>
