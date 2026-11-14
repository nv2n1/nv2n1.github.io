---
title: "readproctab(3)"
name: "readproctab"
section: "3"
letter: "r"
url: "/docs/linux/man/3-readproctab/"
description: "readproctab, freeproctab – read information for all current processes at once"
---

<p>readproctab, freeproctab &#8211; read information for all current processes at once</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;proc/readproc.h&gt;</code></pre>
<p> <code>proc_t** readproctab(int </code><i>flags</i><code>, &#8230; );</code><br />
 <code>void freeproctab(proc_t **</code><i>p</i><code>);</code> </p>
<h2>Description</h2>
<p><code>readproctab</code> reads information on all processes matching the criteria from <i>flags</i>, allocating memory for everything as needed. It returns a NULL-terminated list of <i>proc_t</i> pointers. For more information on the arguments of <code>readproctab</code>, see <code><a href="/docs/linux/man/3-openproc/">openproc</a></code>(3). <code>freeproctab</code> frees all memory allocated by <code>readproctab</code>. The <i>proc_t</i> structure is defined in <i>&lt;proc/readproc.h&gt;</i>, please look there for a definition of all fields. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-openproc/">openproc</a></code>(3), <code><a href="/docs/linux/man/3-readproc/">readproc</a></code>(3), <code>/proc/</code>, <code>/usr/include/proc/readproc.h</code>.</p>
<h2>Reporting Bugs</h2>
<p>Please send bug reports to</p>
