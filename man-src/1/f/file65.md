---

title: "file65(1)"
name: "file65"
section: "1"
letter: "f"
url: "/docs/linux/man/1-file65/"
description: "file65 – print information for o65 object files"
---

<p> file65 &#8211; print information for o65 object files</p>
<h2>SYNOPSIS</h2>
<p> <code>file65</code> [<i>OPTION</i>]&#8230; <i>FILE</i>&#8230; </p>
<h2>DESCRIPTION</h2>
<p> <code>file65</code> prints file information for files in the o65 object format. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-V</code></dt>
<dd> Print undefined and global labels.</dd>
<dt><code>-P</code></dt>
<dd> Print the segment end addresses (suitable for the <code><a href="/docs/linux/man/1-xa/">xa</a></code>(1) command line parameter <code>-b</code>).</dd>
<dt><code>-a offset</code></dt>
<dd> Print <code><a href="/docs/linux/man/1-xa/">xa</a></code>(1) &quot;ROMmable&quot; parameter for another file behind this one in the same ROM, located at the specified offset.</dd>
<dt><code>-A offset</code></dt>
<dd> Does the same thing as <code>-a</code> but only prints the starting address of the next file in the ROM.</dd>
<dt><code>&#8211;help</code></dt>
<dd> Show summary of options.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Show version of program. </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ldo65/">ldo65</a></code>(1), <code><a href="/docs/linux/man/1-printcbm/">printcbm</a></code>(1), <code><a href="/docs/linux/man/1-reloc65/">reloc65</a></code>(1), <code><a href="/docs/linux/man/1-uncpk/">uncpk</a></code>(1), <code><a href="/docs/linux/man/1-xa/">xa</a></code>(1), <code>dxa</code>(1) </p>
<h2>AUTHOR</h2>
<p> This manual page was written by David Weinehall &lt;tao [at] acc.umu.se&gt; and Cameron Kaiser &lt;ckaiser [at] floodgap.com&gt;. Original xa package (C)1989-1997 Andre Fachat. Additional changes (C)1989-2006 Andre Fachat, Jolse Maginnis, David Weinehall and Cameron Kaiser. The current maintainer is Cameron Kaiser. </p>
<h2>WEBSITE</h2>
<p> <a rel="nofollow" href="http://www.floodgap.com/retrotech/xa/">http://www.floodgap.com/retrotech/xa/</a> </p>
