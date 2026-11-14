---
title: "md5sum-textutils(1)"
name: "md5sum-textutils"
section: "1"
letter: "m"
url: "/docs/linux/man/1-md5sum-textutils/"
description: "md5sum – compute and check MD5 message digest"
---

<p>md5sum &#8211; compute and check MD5 message digest </p>
<h2>Synopsis</h2>
<p><code>md5sum</code> [<i>,OPTION/</i>]&#8230; [<i>,FILE/</i>]&#8230;</p>
<h2>Description</h2>
<p>Print or check MD5 (128-bit) checksums. </p>
<p> With no FILE, or when FILE is -, read standard input.</p>
<dl COMPACT>
<dt><code>-b</code>, <code>&#8211;binary</code></p>
<dd>read in binary mode</p>
<dt><code>-c</code>, <code>&#8211;check</code></p>
<dd>read MD5 sums from the FILEs and check them</p>
<dt><code>&#8211;tag</code></p>
<dd>create a BSD-style checksum</p>
<dt><code>-t</code>, <code>&#8211;text</code></p>
<dd>read in text mode (default)</p>
<dt><code>-z</code>, <code>&#8211;zero</code></p>
<dd>end each output line with NUL, not newline, and disable file name escaping</dl>
<h3>The following five options are useful only when verifying checksums:</h3>
<dl COMPACT>
<dt><code>&#8211;ignore-missing</code></p>
<dd>don&#8217;t fail or report status for missing files</p>
<dt><code>&#8211;quiet</code></p>
<dd>don&#8217;t print OK for each successfully verified file</p>
<dt><code>&#8211;status</code></p>
<dd>don&#8217;t output anything, status code shows success</p>
<dt><code>&#8211;strict</code></p>
<dd>exit non-zero for improperly formatted checksum lines</p>
<dt><code>-w</code>, <code>&#8211;warn</code></p>
<dd>warn about improperly formatted checksum lines</p>
<dt><code>&#8211;help</code></p>
<dd>display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd>output version information and exit</dl>
<p> The sums are computed as described in RFC 1321. When checking, the input should be a former output of this program. The default mode is to print a line with checksum, a space, a character indicating input mode (&#8216;*&#8217; for binary, &#8216; &#8216; for text or where binary is insignificant), and name for each FILE. </p>
<p> Note: There is no difference between binary mode and text mode on GNU systems.</p>
<h2>Bugs</h2>
<p>Do not use the MD5 algorithm for security related purposes. Instead, use an SHA-2 algorithm, implemented in the programs <a href="/docs/linux/man/1-sha224sum/">sha224sum</a>(1), <a href="/docs/linux/man/1-sha256sum/">sha256sum</a>(1), <a href="/docs/linux/man/1-sha384sum/">sha384sum</a>(1), <a href="/docs/linux/man/1-sha512sum/">sha512sum</a>(1), or the BLAKE2 algorithm, implemented in <a href="/docs/linux/man/1-b2sum/">b2sum</a>(1)</p>
<h2>Author</h2>
<p>Written by Ulrich Drepper, Scott Miller, and David Madore.</p>
<h2>Reporting Bugs</h2>
<p>GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>See Also</h2>
<p>Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/md5sum">https://www.gnu.org/software/coreutils/md5sum</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) md5sum invocation&#8217;</p>
