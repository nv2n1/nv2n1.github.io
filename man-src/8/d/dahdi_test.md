---
title: "dahdi_test(8)"
name: "dahdi_test"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dahdi_test/"
description: "dahdi_test — Test if the DAHDI timer provides timely response"
---

<p>dahdi_test &#8212; Test if the DAHDI timer provides timely response</p>
<h2>Synopsis</h2>
<p><code>dahdi_test </code> <i>[ -v ]</i> </p>
<h2>Description</h2>
<p><code>dahdi_test</code> dahdi_test runs a timing test in a loop and prints the result of each loop. The test is as follows: It reads 8192 bytes from the DAHDI timer device (<i>/dev/dahdi/pseudo</i>). This should take exactly 8000 ms . It uses calls to <i><a href="/docs/linux/man/2-gettimeofday/">gettimeofday</a>(2) </i> before and after that read to check that indeed exactly 8000ms have passed. Values of 100% and 99.99% Are normally considered a definite <i>pass.</i> Values of 99.98% and 99.97% are probably OK as well. </p>
<h2>Options</h2>
<p><code>-v</code></p>
<dl>
<dd>Be more verbose: print one line per test.</dl>
<p> <code>-c </code> <i>count</i></p>
<dl>
<dd>Run for <i>count</i> times instead of running forever.</dl>
<h2>Files</h2>
<p><code>/dev/dahdi/pseudo</code></p>
<dl>
<dd></dl>
<p> The device file used to access the DAHDI timer.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-dahdi_tool/">dahdi_tool</a>(8), <a href="/docs/linux/man/8-dahdi_cfg/">dahdi_cfg</a>(8), <a href="/docs/linux/man/8-asterisk/">asterisk</a>(8). <a href="/docs/linux/man/2-gettimeofday/">gettimeofday</a>(2) </p>
<h2>Author</h2>
<p>This manual page was written by Tzafrir Cohen &lt;tzafrir.cohen [at] xorcom.com&gt; Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 any later version published by the Free Software Foundation.</p>
