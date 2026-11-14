---
title: "bglmco(1)"
name: "bglmco"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bglmco/"
description: "bglmco – produces module checksum object files."
---

<h2 class="name">NAME</h2>
<p> bglmco &#8211; produces module checksum object files.</p>
<h2>SYNOPSIS</h2>
<p> <code>bglmco</code> [ options ] [ sourcefile ] </p>
<h2>DESCRIPTION</h2>
<p> <code>bglmco</code> reads <i>sourcefile</i> and produces a module checksum object file. This bglmco file is used to ensure modules coherence in Bigloo Makefiles. </p>
<h2>OPTIONS</h2>
<dl>
<dt>
<dt><code>-v</code></p>
<dd>
<dd> Verbose mode </p>
<dt><code>-v</code></p>
<dd> Verbose mode. </p>
<dt><code>-s</code></p>
<dd> Silent mode. </p>
<dt><code>-o &lt;file&gt;</code></p>
<dd> The name of the <i>bglmco</i> file to be generated. </p>
</dl>
<h2>EXAMPLE</h2>
<p> An bglmco is created by &#8220;bglmco foo.scm -o foo.mco&#8221;. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-bigloo/">bigloo</a>(1), <a href="/docs/linux/man/1-bglafile/">bglafile</a>(1), <a href="/docs/linux/man/1-bglmake/">bglmake</a>(1), <a href="/docs/linux/man/1-bgltags/">bgltags</a>(1), <a href="/docs/linux/man/1-makedepend/">makedepend</a>(1), <a href="/docs/linux/man/1-make/">make</a>(1) </p>
<h2>AUTHOR</h2>
<p> Manuel SERRANO, Manuel.Serrano [at] inria.fr </p>
<h2>Index</h2>
