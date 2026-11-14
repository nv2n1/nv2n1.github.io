---
title: "readproc(3)"
name: "readproc"
section: "3"
letter: "r"
url: "/docs/linux/man/3-readproc/"
description: "readproc, freeproc – read information from next /proc/## entry"
---

<p>readproc, freeproc &#8211; read information from next /proc/## entry</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;proc/readproc.h&gt;</code></pre>
<p> <code>proc_t* readproc(PROCTAB *</code><i>PT</i><code>, proc_t *</code><i>return_buf</i><code>);</code><br />
 <code>void freeproc(proc_t *</code><i>p</i><code>);</code> </p>
<h2>Description</h2>
<p><code>readproc</code> reads the information for the next process matching the criteria specified in <i>PT</i> and fills them into a <i>proc_t</i> structure. If <i>return_buf</i> is not NULL, it will use the struct pointed at by <i>return_buf</i>. Otherwise it will allocate a new <i>proc_t</i> structure and return a pointer to it. Note that (if so specified in <i>PT</i>) readproc always allocates memory if it fills in the <i>environ</i> or <i>cmdline</i> parts of <i>proc_t</i>. <code>freeproc</code> frees all memory allocated for the <i>proc_t</i> struct <i>*p</i>. The <i>proc_t</i> structure is defined in <i>&lt;proc/readproc.h&gt;</i>, please look there for a definition of all fields. </p>
<h2>Return Value</h2>
<p><code>readproc</code> returns a pointer to the next <i>proc_t</i> or NULL if there are no more processes left. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-openproc/">openproc</a></code>(3), <code><a href="/docs/linux/man/3-readproctab/">readproctab</a></code>(3), <code>/usr/include/proc/readproc.h</code>, <code>/proc/#pid/</code>,</p>
<h2>Reporting Bugs</h2>
<p>Please send bug reports to</p>
