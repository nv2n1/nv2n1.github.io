---
title: "rpms2solv(1)"
name: "rpms2solv"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rpms2solv/"
description: "rpms2solv – convert one or more rpms into a solv file"
---

<h2 class="name">NAME</h2>
<p> rpms2solv &#8211; convert one or more rpms into a solv file </p>
<h2>SYNOPSIS</h2>
<p> <code>rpms2solv</code> [<i>OPTIONS</i>] <i>RPM1.rpm</i> &#8230;</p>
<h2>DESCRIPTION</h2>
<p> The rpms2solv tool converts the header data from one or more rpms into the solv file written to standard output. </p>
<p> <code>-m</code> <i>MANIFESTFILE</i></p>
<dl>
<dt>
<dd> Read the rpm file names from the specified <i>MANIFESTFILE</i>. You can use <code>&#8211;</code> to read the manifest from standard input.</dl>
<p> <code>-0</code></p>
<dl>
<dt>
<dd> Use a null byte as line terminator for manifest files instead of a newline. This is useful if the file names can contain newlines. See also the <code>-print0</code> option in <code>find</code>.</dl>
<p> <code>-F</code></p>
<dl>
<dt>
<dd> Do not put all files from the headers into the file list, but instead use the filtering also found in <code>createrepo</code>.</dl>
<p> <code>-k</code></p>
<dl>
<dt>
<dd> Read pubkeys instead of rpms.</dl>
<p> <code>-K</code></p>
<dl>
<dt>
<dd> Read pubkey keyrings instead of rpms.</dl>
<p> <code>-X</code></p>
<dl>
<dt>
<dd> Autoexpand SUSE pattern and product provides into packages.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-rpmdb2solv/">rpmdb2solv</a>(1)</p>
<h2>AUTHOR</h2>
<p> Michael Schroeder &lt;mls [at] suse.de&gt; </p>
<h2>Index</h2>
