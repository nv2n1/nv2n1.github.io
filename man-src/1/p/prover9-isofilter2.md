---

title: "prover9-isofilter2(1)"
name: "prover9-isofilter2"
section: "1"
letter: "p"
url: "/docs/linux/man/1-prover9-isofilter2/"
description: "isofilter – removes isomorphic structures from mace4(1) models"
---

<p> isofilter &#8211; removes isomorphic structures from <code><a href="/docs/linux/man/1-mace4/">mace4</a></code>(1) models</p>
<h2>SYNOPSIS</h2>
<p> <code>isofilter</code> [<i>options</i>] &lt; <i>input-file</i> &gt; <i>output-file</i><br />
 <code>isofilter0</code> [<i>options</i>] &lt; <i>input-file</i> &gt; <i>output-file</i><br />
 <code>isofilter2</code> [<i>options</i>] &lt; <i>input-file</i> &gt; <i>output-file</i></p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>isofilter</code>, <code>isofilter0</code> and <code>isofilter2</code> commands. </p>
<p> If <code><a href="/docs/linux/man/1-mace4/">mace4</a></code>(1) produces more than one structure, some of them are very likely to be isomorphic to others. The program <code>isofilter</code> can be used to remove isomorphic structures.</p>
<h2>ALGORITHM</h2>
<p> There are multiple <code>isofilter</code> variants providing alternative algorithms.</p>
<dl>
<dt><code>isofilter</code></dt>
<dd> Uses Occurrence Profiles algorithm.</dd>
<dt><code>isofilter2</code></dt>
<dd> Uses Canonical Forms algorithm.</dd></dl>
<h2>OPTIONS</h2>
<p> A summary of options is included below.</p>
<dl>
<dt><code>ignore_constants</code></dt>
<dd> Ignore all constants during the isomorphism tests.</dd>
<dt><code>check </code><i>&lt;operations&gt;</i></dt>
<dd> Consider only the listed <i>operations</i> in the isomorphism tests.</dd>
<dt><code>output </code><i>&lt;operations&gt;</i></dt>
<dd> Output only the listed <i>operations</i>.</dd>
<dt><code>wrap</code></dt>
<dd> Enclose the resulting structures in <code>list(interpretations). &#8230; end_of_list.</code></dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mace4/">mace4</a></code>(1).<br />
 Full documentation for <code>isofilter</code> is found in the <code>prover9</code> manual, available on Debian systems in the <i>prover9-doc</i> package at <i>/usr/share/doc/prover9-doc/manual/index.html</i>.</p>
<h2>AUTHOR</h2>
<p> <code>isofilter</code> was written by William McCune &lt;mccune [at] cs.unm.edu&gt; </p>
<p> This manual page was written by Peter Collingbourne &lt;pcc03 [at] doc.ic.ac.uk&gt;, for the Debian project (but may be used by others). </p>
