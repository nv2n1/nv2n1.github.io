---
title: "ustrerror(3)"
name: "ustrerror"
section: "3"
letter: "u"
url: "/docs/linux/man/3-ustrerror/"
description: "ustrerror – Returns a string describing errno. Allegro game programming library."
---

<p>ustrerror &#8211; Returns a string describing errno. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

const char *ustrerror(int err);</code></pre>
<h2>Description</h2>
<p>This function returns a string that describes the error code `err&#8217;, which normally comes from the variable `errno&#8217;. Example: </p>
<pre><code>PACKFILE *input_file = pack_fopen(&quot;badname&quot;, &quot;r&quot;);
if (input_file == NULL)
    allegro_message(&quot;%s
Sorry!
&quot;, ustrerror(errno));</code></pre>
<h2>Return Value</h2>
<p>Returns a pointer to a static string that should not be modified or freed. If you make subsequent calls to ustrerror(), the string will be overwritten. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-uconvert/">uconvert</a></code>(3), <code><a href="/docs/linux/man/3-allegro_error/">allegro_error</a></code>(3) </p>
