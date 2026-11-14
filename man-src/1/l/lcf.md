---
title: "lcf(1)"
name: "lcf"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lcf/"
description: "lcf – Determine which of the historical versions of a config is installed"
---

<h2 class="name">NAME</h2>
<p> lcf &#8211; Determine which of the historical versions of a config is installed </p>
<h2>SYNOPSIS</h2>
<p> <code>lcf</code> <i>[options]</i> <i>&lt;Destination File Name&gt;</i> <i>&lt;Historical MD5SUM source directory&gt;</i></p>
<h2>DESCRIPTION</h2>
<p> This script, given a destination file name, and a directory containing md5sums of historical versions of the file, attempts to determine if the installed version corresponds to a historical version. lcf uses the same algorithm that ucf uses, and should exhibit the same behaviour. </p>
<p> The source directory is the place where historical md5sums are expected to live. Specifically, the historical md5sums are looked for in either the file <i>${filename}.md5sum, </i> or the subdirectory <i>${filename}.md5sum.d/</i></p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Print a short usage message</p>
<dt><code>-n, &#8211;no-action</code></p>
<dd> Dry run. Print the actions that would be taken if the script is invoked, but take no action.</p>
<dt><code>-d [n], &#8211;debug [n]</code></p>
<dd> Set the debug level to the (optional) level <i>n </i> (n defaults to 1). This turns on copious debugging information.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Make the script be very verbose about setting internal variables.</dl>
<h2>FILES</h2>
<p> <i>/var/lib/ucf/hashfile,</i> <i>/etc/ucf.conf</i></p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-ucf/">ucf</a>(1) <a href="/docs/linux/man/5-ucf-conf/">ucf.conf</a>(5).</p>
<h2>BUGS</h2>
<p> There are no bugs. Any resemblance thereof is delirium. Really.</p>
<h2>AUTHOR</h2>
<p> This manual page was written Manoj Srivastava &lt;srivasta [at] debian.org&gt;, for the Debian GNU/Linux system. </p>
<h2>Index</h2>
