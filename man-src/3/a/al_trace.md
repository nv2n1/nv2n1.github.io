---
title: "al_trace(3)"
name: "al_trace"
section: "3"
letter: "a"
url: "/docs/linux/man/3-al_trace/"
description: "al_trace – Outputs a debugging trace message. Allegro game programming library."
---

<h2>NAME</h2>
<p> al_trace &#8211; Outputs a debugging trace message. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void al_trace(const char *msg, &#8230;);</code></p>
<h2>DESCRIPTION</h2>
<p> Outputs a debugging trace message, using a printf() format string given in ASCII. If you have installed a custom trace handler it uses that, or if the environment variable ALLEGRO_TRACE is set it writes into the file specified by the environment, otherwise it writes the message to &quot;allegro.log&quot; in the current directory. You will usually want to use the TRACE() macro instead of calling this function directly. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-trace/">TRACE</a></code>(3), <code><a href="/docs/linux/man/3-al_assert/">al_assert</a></code>(3), <code><a href="/docs/linux/man/3-register_trace_handler/">register_trace_handler</a></code>(3) </p>
<h2>Index</h2>
