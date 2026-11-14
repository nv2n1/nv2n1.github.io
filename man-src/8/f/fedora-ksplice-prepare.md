---
title: "fedora-ksplice-prepare(8)"
name: "fedora-ksplice-prepare"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fedora-ksplice-prepare/"
description: "fedora-ksplice-prepare – Prepare kernel sources for KSplice"
---

<p>fedora-ksplice-prepare &#8211; Prepare kernel sources for KSplice</p>
<h2>Synopsis</h2>
<p><code>fedora-ksplice-prepare</code> [<i>OPTIONS</i>] [<i>KERNELVERSION</i>]</p>
<h2>Description</h2>
<p>Download the source rpm of the currently installed kernel and prepare the kernel for applying a patch with ksplice. </p>
<p> If you specified the <i>KERNELVERSION</i> argument, the sources for the specified kernel version will be downloaded.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;clean</code></p>
<dd>Clean up the directory in which the kernel source RPMs are downloaded</p>
<dt><code>&#8211;enablerepo</code> <i>&lt;repository&gt;</i></p>
<dd>Enable repository &lt;repository&gt;</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-ksplice-create/">ksplice-create</a></i>(8)</p>
<h2>Author</h2>
<p>Written by Jochen Schmitt</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to to &lt;Jochen [at] herr-schmitt.de&gt;</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2008 Jochen Schmitt License GPLv3+ GNU GPL version 3 or later &lt;<a rel="nofollow" href="http://www.gnu.org/license/gpl.html">http://www.gnu.org/license/gpl.html</a>&gt;<br />
 Tnis is free software: you are free to chage and redistribute it. There is NO WARRENTY, to the extent permitted by law.</p>
