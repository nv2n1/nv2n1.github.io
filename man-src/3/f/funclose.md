---
title: "funclose(3)"
name: "funclose"
section: "3"
letter: "f"
url: "/docs/linux/man/3-funclose/"
description: "FunClose – close a Funtools data file"
---

<h2>NAME</h2>
<p> <code>FunClose &#8211; close a Funtools data file</code></p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;funtools.h&gt;
</code></pre>
<pre>
  void FunClose(Fun fun)
</pre>
<h2>DESCRIPTION</h2>
<p> The FunClose() routine closes a previously-opened Funtools data file, freeing control structures. If a Funtools reference handle was passed to the <i>FunOpen()</i> call for this file, and if copy mode also was specified for that file, then <i>FunClose()</i> also will copy the remaining extensions from the input file to the output file (if the input file still is open). Thus, we recommend always closing the output Funtools file <code>before</code> the input file. (Alternatively, you can call <i>FunFlush()</i> explicitly).</p>
<h2>SEE ALSO</h2>
<p> See <a href="/docs/linux/man/n-funtools/">funtools</a>(n) for a list of Funtools help pages </p>
<h2>Index</h2>
