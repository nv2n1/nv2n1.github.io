---
title: "fedora-ksplice-create(8)"
name: "fedora-ksplice-create"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fedora-ksplice-create/"
description: "fedora-ksplice-create – Create a set of kernel modulesfor a rebootless kernel update"
---

<p>fedora-ksplice-create &#8211; Create a set of kernel modulesfor a rebootless kernel update</p>
<h2>Synopsis</h2>
<p><code>fedora-ksplice-create</code> [<i>OPTIONS</i>] [<i>KERNELVERSION</i>] [<i>PATCH</i>]</p>
<h2>Description</h2>
<p>Fedora-ksplice-create allow to patch a kernel without the need to reboot the system to activate the patched kernel. </p>
<p> If you specified the <i>KERNELVERSION</i> argument, fedora-ksplice-create may be use the downloaded kernel sources for the specified kernel version. </p>
<p> Please keep in mind, that you must boot the system with this specified kernel version, if you want to apply the generated kernel patch via Ksplice-apply.</p>
<h2>Options</h2>
<dl>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Verbose output</p>
<dt><code>-c</code>, <code>&#8211;config </code><i>CONFIGFILE</i></p>
<dd>Define configure file for ksplice</p>
<dt><code>&#8211;id </code><i>BUILDID</i></p>
<dd>Specifies a uniue value that will be used as the identifier of the Ksplice update. This identifier will be, for example, apper in the name of the update tarball. By default, a random 8-character ID be be generated.</p>
<dt><code>&#8211;patch-opt </code><i>OPTIONS</i></p>
<dd>Can be used to pass options to the <i><a href="/docs/linux/man/1-patch/">patch</a></i>(1). if this option is NOT specified, then <code>-p1</code> is passed to <code>patch</code>. If this option is specified, then only the specified options will be passed to <code>patch</code>.</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-ksplice-create/">ksplice-create</a></i>(8), <i><a href="/docs/linux/man/8-ksplice-apply/">ksplice-apply</a></i>(8)</p>
<h2>Author</h2>
<p>Written by Jochen Schmitt</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to to &lt;Jochen [at] herr-schmitt.de&gt;</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2008 Jochen Schmitt License GPLv3+ GNU GPL version 3 or later &lt;<a rel="nofollow" href="http://www.gnu.org/license/gpl.html">http://www.gnu.org/license/gpl.html</a>&gt;<br />
 Tnis is free software: you are free to chage and redistribute it. There is NO WARRENTY, to the extent permitted by law.</p>
