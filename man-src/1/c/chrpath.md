---

title: "chrpath(1)"
name: "chrpath"
section: "1"
letter: "c"
url: "/docs/linux/man/1-chrpath/"
description: "chrpath – change the rpath or runpath in binaries"
---

<p> chrpath &#8211; change the rpath or runpath in binaries</p>
<h2>SYNOPSIS</h2>
<p> <code>chrpath</code> [ <code>-v</code> | <code>&#8211;version</code> ] [ <code>-d</code> | <code>&#8211;delete</code> ] [ <code>-r</code> <i>&lt;path&gt;</i> |&nbsp;<wbr> <code>&#8211;replace</code> <i>&lt;path&gt;</i> ] [ <code>-c</code> | <code>&#8211;convert</code> ] [ <code>-l</code> | <code>&#8211;list</code> ] [ <code>-h</code> | <code>&#8211;help</code> ] <i>&lt;program&gt;</i> [ <i>&lt;program&gt;</i> &#8230; ]</p>
<h2>DESCRIPTION</h2>
<p> <code>chrpath</code> changes, lists or removes the rpath or runpath setting in a binary. The rpath, or runpath if it is present, is where the runtime linker should look for the libraries needed for a program.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v</code>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;version</code></dt>
<dd> Display program version number</dd>
<dt><code>-d</code>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;delete</code></dt>
<dd> Delete current rpath or runpath setting</dd>
<dt><code>-c</code>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;convert</code></dt>
<dd> Convert the rpath setting into a runpath setting</dd>
<dt><code>-r&nbsp;<wbr></code><i>&lt;path&gt;</i>&nbsp;<wbr>| &#8211;replace&nbsp;<wbr><i>&lt;path&gt;</i></dt>
<dd> Replace current rpath or runpath setting with the path given</dd>
<dt><code>-k</code>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;keepgoing</code></dt>
<dd> Do not fail on first error, but process all arguments before returning the error.</dd>
<dt><code>-l</code>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;list</code></dt>
<dd> List the current rpath or runpath (default)</dd>
<dt><code>-h</code>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;help</code></dt>
<dd> Show usage information.</dd></dl>
<h2>EXIT STATUS</h2>
<dl>
<dt><code>0</code></dt>
<dd> If all operations were successful</dd>
<dt><code>&gt;</code>0</dt>
<dd> if one of the operations failed. A failing operation terminates the program unless -k is specified. </dd>
</dl>
<h2>AUTHOR</h2>
<p> The chrpath program was written by Petter Reinholdtsen &lt;pere [at] hungry.com&gt;, based on works by Geoffrey Keating &lt;geoffk [at] ozemail.com.au&gt; and Peeter Joot &lt;peeterj [at] ca.ibm.com&gt;. </p>
<p> This manual page was originally written by Tollef Fog Heen &lt;tfheen [at] debian.org&gt;, for the Debian GNU/Linux system (but may be used by others). </p>
