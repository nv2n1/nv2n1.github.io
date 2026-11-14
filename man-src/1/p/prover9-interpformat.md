---
title: "prover9-interpformat(1)"
name: "prover9-interpformat"
section: "1"
letter: "p"
url: "/docs/linux/man/1-prover9-interpformat/"
description: "interpformat – tool for transforming mace4(1) models"
---

<h2>NAME</h2>
<p> interpformat &#8211; tool for transforming <code><a href="/docs/linux/man/1-mace4/">mace4</a></code>(1) models</p>
<h2>SYNOPSIS</h2>
<p> <code>interpformat</code> [<i>options</i>] &lt;<i>transformation</i>&gt; -f <i>input-file</i> &gt; <i>output-file</i><br />
 <code>interpformat</code> [<i>options</i>] &lt;<i>transformation</i>&gt; &lt; <i>input-file</i> &gt; <i>output-file</i></p>
<h2>DESCRIPTION</h2>
<p> The models (structures) in <code><a href="/docs/linux/man/1-mace4/">mace4</a></code>(1) output files can be transformed in various ways with the program <code>interpformat</code>.</p>
<h2>TRANSFORMATIONS</h2>
<p> The transformations are listed here.</p>
<dl>
<dt><code>standard</code></p>
<dd> one line per operation</p>
<dt><code>standard2</code></p>
<dd> standard, with binary operations in a square (default)</p>
<dt><code>portable</code></p>
<dd> list of lists, suitable for parsing by Python, GAP, etc.</p>
<dt><code>tabular</code></p>
<dd> as nice tables</p>
<dt><code>raw</code></p>
<dd> similar to standard, but without punctuation</p>
<dt><code>cooked</code></p>
<dd> as terms, e.g., f(0,1)=2</p>
<dt><code>tex</code></p>
<dd> formatted for LaTeX</p>
<dt><code>xml</code></p>
<dd> XML</dl>
<h2>OPTIONS</h2>
<p> A summary of options is included below.</p>
<dl>
<dt><code>output </code><i>&lt;operations&gt;</i></p>
<dd> Output only the listed <i>operations</i>.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mace4/">mace4</a></code>(1).<br />
 Full documentation for <code>interpformat</code> is found in the <code>prover9</code> manual, available on Debian systems in the <i>prover9-doc</i> package at <i>/usr/share/doc/prover9-doc/manual/index.html</i>.</p>
<h2>AUTHOR</h2>
<p> <code>interpformat</code> was written by William McCune &lt;mccune [at] cs.unm.edu&gt; </p>
<p> This manual page was written by Peter Collingbourne &lt;pcc03 [at] doc.ic.ac.uk&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
