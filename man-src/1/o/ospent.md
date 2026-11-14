---
title: "ospent(1)"
name: "ospent"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ospent/"
description: "ospent – Concatenates entities in an SGML/XML document"
---

<h2 class="name">NAME</h2>
<p> ospent &#8211; Concatenates entities in an SGML/XML document </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>ospent</code> [<code>-ChnrRv</code>] [<code>-b</code><i>bctf</i>] [<code>-c</code><i>sysid</i>] [<code>-f</code><i>file</i>] [<code>-D</code><i>directory</i>] [<i>sysid</i>&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>ospent</code> (OpenSP print entity) prints the concatenation of the entities with system identifiers</p>
<dl>
<dt>
<dd>on the standard output.</dl>
<p> The following options are available: </p>
<p> <code>-b</code><i>bctf</i>, <code>&#8211;bctf=</code><i>bctf</i></p>
<dl>
<dt>
<dd> Use the BCTF with name <i>bctf</i> for output.</dl>
<p> <code>-c</code><i>sysid</i>, <code>&#8211;catalog=</code><i>sysid</i></p>
<dl>
<dt>
<dd> Map public identifiers and entity names to system identifiers using the catalog entry file whose system identifier is <i>sysid</i>.</dl>
<p> <code>-C</code>, <code>&#8211;catalogs</code></p>
<dl>
<dt>
<dd> This has the same effect as in <code><a href="/docs/linux/man/1-onsgmls/">onsgmls</a>(1)</code>.</dl>
<p> <code>-D</code><i>directory</i>, <code>&#8211;directory=</code><i>directory</i></p>
<dl>
<dt>
<dd> Search directory for files specified in system identifiers. This has the same effect as in <code><a href="/docs/linux/man/1-onsgmls/">onsgmls</a>(1)</code>.</dl>
<p> <code>-f</code><i>file</i>, <code>&#8211;error-file=</code><i>file</i></p>
<dl>
<dt>
<dd> Redirect error messages to <i>file</i>.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display a help text and exit.</dl>
<p> <code>-n</code>, <code>&#8211;non-sgml</code></p>
<dl>
<dt>
<dd> The entity is a non-SGML data entity. This option forces the octets in the storage objects comprising the entity to be copied exactly without any of the conversions that are done for text entities. Implies <code>-r</code>.</dl>
<p> <code>-r</code>, <code>&#8211;raw</code></p>
<dl>
<dt>
<dd> Raw output. Don&#8217;t perform any conversion on RSs and REs when printing the entity. The entity would typically have the storage manager attribute records=asis.</dl>
<p> <code>-R</code>, <code>&#8211;restricted</code></p>
<dl>
<dt>
<dd> This has the same effect as in <code><a href="/docs/linux/man/1-onsgmls/">onsgmls</a>(1)</code>.</dl>
<p> <code>-v</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print the version number.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-onsgmls/">onsgmls</a>(1)</code>, <code><a href="/docs/linux/man/1-ospam/">ospam</a>(1)</code>, <code><a href="/docs/linux/man/1-onsgmlnorm/">onsgmlnorm</a>(1)</code>, <code><a href="/docs/linux/man/1-osx/">osx</a>(1)</code></p>
<h2>AUTHORS</h2>
<p> <code>James Clark</code></p>
<dl>
<dt>
<dd> Author.</dl>
<p> <code>Ian Castle</code> &lt;ian.castle [at] openjade.org&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<h2>COPYRIGHT</h2>
<h2>Index</h2>
