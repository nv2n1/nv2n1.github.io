---
title: "trace(3)"
name: "trace"
section: "3"
letter: "t"
url: "/docs/linux/man/3-trace/"
description: "TRACE – Debugging helper macro to trace messages. Allegro game programming library."
---

<p>TRACE &#8211; Debugging helper macro to trace messages. Allegro game programming library.</p>
<h2>Synopsis</h2>
<p><code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void TRACE(char *msg, &#8230;);</code></p>
<h2>Description</h2>
<p>Debugging helper macro. Normally compiles away to nothing, but if you defined the preprocessor symbol DEBUGMODE before including Allegro headers, it passes the supplied message given in ASCII format to al_trace(). Example: </p>
<pre> #define DEBUGMODE
 #include 
 ...
 void my_blitter(BITMAP *source, int flags)
 {
 static int count_call = 0;
 TRACE(&quot;my_blitter() called %d times.
&quot;, count_call++);
 ...
 }</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-al_trace/">al_trace</a></code>(3), <code><a href="/docs/linux/man/3-assert/">ASSERT</a></code>(3), <code><a href="/docs/linux/man/3-register_trace_handler/">register_trace_handler</a></code>(3)</p>
