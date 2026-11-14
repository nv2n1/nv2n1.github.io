---
title: "lzfgrep(1)"
name: "lzfgrep"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lzfgrep/"
description: "xzgrep – search compressed files for a regular expression"
---

<h2 class="name">NAME</h2>
<p> xzgrep &#8211; search compressed files for a regular expression </p>
<h2>SYNOPSIS</h2>
<p> <code>xzgrep</code> [<i>grep_options</i>] [<code>-e</code>] <i>pattern</i> <i>file</i>&#8230;<br />
 <code>xzegrep</code> &#8230;<br />
 <code>xzfgrep</code> &#8230;<br />
 <code>lzgrep</code> &#8230;<br />
 <code>lzegrep</code> &#8230;<br />
 <code>lzfgrep</code> &#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>xzgrep</code> invokes <code><a href="/docs/linux/man/1-grep/">grep</a></code>(1) on <i>files</i> which may be either uncompressed or compressed with <code><a href="/docs/linux/man/1-xz/">xz</a></code>(1), <code><a href="/docs/linux/man/1-lzma/">lzma</a></code>(1), <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1), <code><a href="/docs/linux/man/1-bzip2/">bzip2</a></code>(1), <code><a href="/docs/linux/man/1-lzop/">lzop</a></code>(1), or <code><a href="/docs/linux/man/1-zstd/">zstd</a></code>(1). All options specified are passed directly to <code><a href="/docs/linux/man/1-grep/">grep</a></code>(1). </p>
<p> If no <i>file</i> is specified, then standard input is decompressed if necessary and fed to <code><a href="/docs/linux/man/1-grep/">grep</a></code>(1). When reading from standard input, <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1), <code><a href="/docs/linux/man/1-bzip2/">bzip2</a></code>(1), <code><a href="/docs/linux/man/1-lzop/">lzop</a></code>(1), and <code><a href="/docs/linux/man/1-zstd/">zstd</a></code>(1) compressed files are not supported. </p>
<p> If <code>xzgrep</code> is invoked as <code>xzegrep</code> or <code>xzfgrep</code> then <code><a href="/docs/linux/man/1-egrep/">egrep</a></code>(1) or <code><a href="/docs/linux/man/1-fgrep/">fgrep</a></code>(1) is used instead of <code><a href="/docs/linux/man/1-grep/">grep</a></code>(1). The same applies to names <code>lzgrep</code>, <code>lzegrep</code>, and <code>lzfgrep</code>, which are provided for backward compatibility with LZMA Utils. </p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>GREP</code></p>
<dd> If the <code>GREP</code> environment variable is set, <code>xzgrep</code> uses it instead of <code><a href="/docs/linux/man/1-grep/">grep</a></code>(1), <code><a href="/docs/linux/man/1-egrep/">egrep</a></code>(1), or <code><a href="/docs/linux/man/1-fgrep/">fgrep</a></code>(1).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-grep/">grep</a></code>(1), <code><a href="/docs/linux/man/1-xz/">xz</a></code>(1), <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1), <code><a href="/docs/linux/man/1-bzip2/">bzip2</a></code>(1), <code><a href="/docs/linux/man/1-lzop/">lzop</a></code>(1), <code><a href="/docs/linux/man/1-zstd/">zstd</a></code>(1), <code><a href="/docs/linux/man/1-zgrep/">zgrep</a></code>(1) </p>
<h2>Index</h2>
