---
title: "whirlpoolsum(1)"
name: "whirlpoolsum"
section: "1"
letter: "w"
url: "/docs/linux/man/1-whirlpoolsum/"
description: "whirlpoolsum – compute and check WHIRLPOOL message digest"
---

<h2>NAME</h2>
<p> whirlpoolsum &#8211; compute and check WHIRLPOOL message digest</p>
<h2>SYNOPSIS</h2>
<p> <code>whirlpoolsum</code> [<i>OPTION</i>]&#8230; [<i>FILE</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Print or check WHIRLPOOL (512-bit) checksums. With no FILE, or when FILE is -, read standard input.</p>
<dl>
<dt><code>-b</code>, <code>&#8211;binary</code></p>
<dd> read in binary mode</p>
<dt><code>-c</code>, <code>&#8211;check</code></p>
<dd> read WHIRLPOOL sums from the FILEs and check them</p>
<dt><code>&#8211;tag</code></p>
<dd> create a BSD-style checksum, always in binary mode</p>
<dt><code>-t</code>, <code>&#8211;text</code></p>
<dd> read in text mode (default)</p>
<dt>
<dd> Note: There is no difference between binary and text mode option on GNU system.</dl>
<h3>The following three options are useful only when verifying checksums:</h3>
<dl>
<dt><code>&#8211;quiet</code></p>
<dd> don&#8217;t print OK for each successfully verified file</p>
<dt><code>&#8211;status</code></p>
<dd> don&#8217;t output anything, status code shows success</p>
<dt><code>-w</code>, <code>&#8211;warn</code></p>
<dd> warn about improperly formatted checksum lines</p>
<dt><code>&#8211;strict</code></p>
<dd> with <code>&#8211;check</code>, exit non-zero for any invalid input</p>
<dt><code>&#8211;test</code></p>
<dd> invoke Whirlpool API test function and exit</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<p> The sums are computed as described in the official WHIRLPOOL specs. When checking, the input should be a former output of this program. The default mode is to print a line with checksum, a character indicating input mode (&#8216;*&#8217; for binary, space for text), and name for each FILE. </p>
<h2>AUTHOR</h2>
<p> Written by Denis Fateyev. Based on WHIRLPOOL algorithm implementation by Paulo S.L.M. Barreto and Vincent Rijmen, and various improvements by Avar Arnfjörð Bjarmason.</p>
<h2>REPORTING BUGS</h2>
<p> Report whirlpoolsum bugs to &#8216;denis [at] fateyev.com&#8217;<br />
 Libwhirlpool home page: &lt;<a rel="nofollow" href="https://github.com/dfateyev/libwhirlpool">https://github.com/dfateyev/libwhirlpool</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> This is free and unencumbered software released into the public domain. Anyone is free to copy, modify, publish, use, compile, sell, or distribute this software, either in source code form or as a compiled binary, for any purpose, commercial or non-commercial, and by any means.<br />
 THE SOFTWARE IS PROVIDED &quot;AS IS&quot;, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-sha256sum/">sha256sum</a></code>(1), <code><a href="/docs/linux/man/1-sha384sum/">sha384sum</a></code>(1), <code><a href="/docs/linux/man/1-sha512sum/">sha512sum</a></code>(1). </p>
<h2>Index</h2>
