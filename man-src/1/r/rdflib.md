---

title: "rdflib(1)"
name: "rdflib"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rdflib/"
description: "rdflib – manage a library file for use with ldrdf(1)"
---

<h2>NAME</h2>
<p> rdflib &#8211; manage a library file for use with <a href="/docs/linux/man/1-ldrdf/">ldrdf</a>(1)</p>
<p> <code>rdflib</code> <i>command</i> <i>arguments</i></p>
<p> <code>rdflib</code> manages a library file which can be used by <code><a href="/docs/linux/man/1-ldrdf/">ldrdf</a></code>(1). It is supplied with a shell script <code>makelib</code> which should probably be used to create libraries.</p>
<h2>COMMANDS</h2>
<dl>
<dt><code>c</code><i> library-file</i></dt>
<dd> Create (or truncate) a library.</dd>
<dt><code>a</code><i> library-file object-file module</i></dt>
<dd> Add the <i>object-file</i> to the library under the name <i>module</i>.</dd>
<dt><code>x</code><i> library-file module object-file</i></dt>
<dd> Extract a <i>module</i> from the library to the file <i>object-file</i>.</dd>
<dt><code>t library-file</code></dt>
<dd> Display a list of modules in the library.</dd></dl>
<h2>NOTES</h2>
<p> A remove command will be added soon.</p>
<h2>AUTHORS</h2>
<p> Julian Hall &lt;jules [at] earthcorp.com&gt;. </p>
<p> This manual page was written by Matej Vela &lt;vela [at] debian.org&gt;. </p>
