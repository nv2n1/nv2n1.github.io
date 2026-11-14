---
title: "xzdec(1)"
name: "xzdec"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xzdec/"
description: "xzdec, lzmadec – Small .xz and .lzma decompressors"
---

<h2>NAME</h2>
<p> xzdec, lzmadec &#8211; Small .xz and .lzma decompressors</p>
<h2>SYNOPSIS</h2>
<p> <code>xzdec</code> [<i>option&#8230;</i>] [<i>file&#8230;</i>]<br />
 <code>lzmadec</code> [<i>option&#8230;</i>] [<i>file&#8230;</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>xzdec</code> is a liblzma-based decompression-only tool for <code>.xz</code> (and only <code>.xz</code>) files. <code>xzdec</code> is intended to work as a drop-in replacement for <code><a href="/docs/linux/man/1-xz/">xz</a></code>(1) in the most common situations where a script has been written to use <code>xz &#8211;decompress &#8211;stdout</code> (and possibly a few other commonly used options) to decompress <code>.xz</code> files. <code>lzmadec</code> is identical to <code>xzdec</code> except that <code>lzmadec</code> supports <code>.lzma</code> files instead of <code>.xz</code> files. </p>
<p> To reduce the size of the executable, <code>xzdec</code> doesn&#8217;t support multithreading or localization, and doesn&#8217;t read options from <code>XZ_DEFAULTS</code> and <code>XZ_OPT</code> environment variables. <code>xzdec</code> doesn&#8217;t support displaying intermediate progress information: sending <code>SIGINFO</code> to <code>xzdec</code> does nothing, but sending <code>SIGUSR1</code> terminates the process instead of displaying progress information.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code>, <code>&#8211;decompress</code>, <code>&#8211;uncompress</code></p>
<dd> Ignored for <code><a href="/docs/linux/man/1-xz/">xz</a></code>(1) compatibility. <code>xzdec</code> supports only decompression.</p>
<dt><code>-k</code>, <code>&#8211;keep</code></p>
<dd> Ignored for <code><a href="/docs/linux/man/1-xz/">xz</a></code>(1) compatibility. <code>xzdec</code> never creates or removes any files.</p>
<dt><code>-c</code>, <code>&#8211;stdout</code>, <code>&#8211;to-stdout</code></p>
<dd> Ignored for <code><a href="/docs/linux/man/1-xz/">xz</a></code>(1) compatibility. <code>xzdec</code> always writes the decompressed data to standard output.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> Specifying this once does nothing since <code>xzdec</code> never displays any warnings or notices. Specify this twice to suppress errors.</p>
<dt><code>-Q</code>, <code>&#8211;no-warn</code></p>
<dd> Ignored for <code><a href="/docs/linux/man/1-xz/">xz</a></code>(1) compatibility. <code>xzdec</code> never uses the exit status 2.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Display a help message and exit successfully.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Display the version number of <code>xzdec</code> and liblzma.</dl>
<h2>EXIT STATUS</h2>
<dl>
<dt><code>0</code></p>
<dd> All was good.</p>
<dt><code>1</code></p>
<dd> An error occurred.</dl>
<p> <code>xzdec</code> doesn&#8217;t have any warning messages like <code><a href="/docs/linux/man/1-xz/">xz</a></code>(1) has, thus the exit status 2 is not used by <code>xzdec</code>.</p>
<h2>NOTES</h2>
<p> Use <code><a href="/docs/linux/man/1-xz/">xz</a></code>(1) instead of <code>xzdec</code> or <code>lzmadec</code> for normal everyday use. <code>xzdec</code> or <code>lzmadec</code> are meant only for situations where it is important to have a smaller decompressor than the full-featured <code><a href="/docs/linux/man/1-xz/">xz</a></code>(1). </p>
<p> <code>xzdec</code> and <code>lzmadec</code> are not really that small. The size can be reduced further by dropping features from liblzma at compile time, but that shouldn&#8217;t usually be done for executables distributed in typical non-embedded operating system distributions. If you need a truly small <code>.xz</code> decompressor, consider using XZ Embedded.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-xz/">xz</a></code>(1) </p>
<p> XZ Embedded: &lt;<a rel="nofollow" href="http://tukaani.org/xz/embedded.html">http://tukaani.org/xz/embedded.html</a>&gt; </p>
<h2>Index</h2>
