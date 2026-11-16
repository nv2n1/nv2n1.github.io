---
title: "partprobe(8)"
name: "partprobe"
section: "8"
letter: "p"
url: "/docs/linux/man/8-partprobe/"
description: "partprobe – inform the OS of partition table changes"
---

<p>partprobe &#8211; inform the OS of partition table changes</p>
<h2>Synopsis</h2>
<p><code>partprobe</code> [<i>-d</i>] [<i>-s</i>] [<i>devices&#8230;</i>]</p>
<h2>Description</h2>
<p>This manual page documents briefly the <code>partprobe</code> command. </p>
<p> <code>partprobe</code> is a program that informs the operating system kernel of partition table changes.</p>
<h2>Options</h2>
<p>This program uses short UNIX style options.</p>
<dl>
<dt><code>-d, &#8211;dry-run</code></dt>
<dd>Don&#8217;t update the kernel.</dd>
<dt><code>-s, &#8211;summary</code></dt>
<dd>Show a summary of devices and their partitions.</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd>Show summary of options.</dd>
<dt><code>-v, &#8211;version</code></dt>
<dd>Show version of program.</dd></dl>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;bug-parted [at] gnu.org&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-parted/">parted</a></code>(8).</p>
<h2>Author</h2>
<p>This manual page was written by Timshel Knoll &lt;timshel [at] debian.org&gt;, for the Debian GNU/Linux system (but may be used by others).</p>
