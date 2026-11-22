---

title: "ptaskset(1)"
name: "ptaskset"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ptaskset/"
description: "ptaskset (python-schedutils) – set or get the affinity of a process"
---

<p> <code>ptaskset (python-schedutils) &#8211; set or get the affinity of a process</code></p>
<h2>SYNOPSIS</h2>
<p> ptaskset [options] [mask | cpu-list] [pid | cmd [args&#8230;]]</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-p, &#8211;pid</code></dt>
<dd> operate on existing given pid</dd>
<dt><code>-c, &#8211;cpu-list</code></dt>
<dd> display and specify cpus in list format</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd> display help</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-taskset/">taskset</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> ptaskset was written by Arnaldo Carvalho de Melo &lt;acme [at] redhat.com&gt;<br/>
 as part of python-schedutils </p>
<p> This manual page was written by John Kacur &lt;jkacur [at] redhat.com&gt; </p>
<p> Report bugs and send patches to &lt;tuna-devel [at] lists.fedorahosted.org&gt; </p>
