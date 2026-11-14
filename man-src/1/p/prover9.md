---
title: "prover9(1)"
name: "prover9"
section: "1"
letter: "p"
url: "/docs/linux/man/1-prover9/"
description: "prover9 – resolution/paramodulation theorem prover"
---

<h2>NAME</h2>
<p> prover9 &#8211; resolution/paramodulation theorem prover</p>
<h2>SYNOPSIS</h2>
<p> <code>prover9</code> [<i>options</i>] &lt; <i>input-file</i> &gt; <i>output-file</i><br />
 <code>prover9</code> [<i>options</i>] -f <i>input-file</i> &gt; <i>output-file</i></p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>prover9</code> command. </p>
<p> <code>prover9</code> is an automated theorem prover for first-order and equational logic. It is a successor of the <code><a href="/docs/linux/man/1-otter/">otter</a></code>(1) prover. <code>prover9</code> uses the inference techniques of ordered resolution and paramodulation with literal selection.</p>
<h2>OPTIONS</h2>
<p> A summary of options is included below.</p>
<dl>
<dt><code>-h</code></p>
<dd> View a list of command-line options.</p>
<dt><code>-x</code></p>
<dd> Enables an experimental enhanced auto-mode. For more information consult the <code>prover9</code> manual.</p>
<dt><code>-p</code></p>
<dd> Fully parenthesize output.</p>
<dt><code>-t </code><i>n</i></p>
<dd> Constrain the search to last about <i>n</i> seconds. For UNIX-like systems, the `user CPU&#8217; time is used.</p>
<dt><code>-f </code><i>file</i></p>
<dd> Take input from <i>file</i> instead of from standard input.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mace4/">mace4</a></code>(1), <code><a href="/docs/linux/man/1-otter/">otter</a></code>(1).<br />
 On Debian systems, the manual is found in the <i>prover9-doc</i> package, at <i>/usr/share/doc/prover9-doc/manual/index.html</i>.</p>
<h2>AUTHOR</h2>
<p> <code>prover9</code> was written by William McCune &lt;mccune [at] cs.unm.edu&gt; </p>
<p> This manual page was written by Peter Collingbourne &lt;pcc03 [at] doc.ic.ac.uk&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
