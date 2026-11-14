---
title: "febootstrap-to-initramfs(8)"
name: "febootstrap-to-initramfs"
section: "8"
letter: "f"
url: "/docs/linux/man/8-febootstrap-to-initramfs/"
description: "febootstrap-to-initramfs – Convert febootstrap root to initramfs (cpio) file."
---

<p>febootstrap-to-initramfs &#8211; Convert febootstrap root to initramfs (cpio) file.</p>
<h2>Synopsis</h2>
<pre> febootstrap-to-initramfs [--files=filelist] DIR &gt; initrd.img</pre>
<h2>Description</h2>
<p><i>febootstrap-to-initramfs</i> converts the filesystem created by <i><a href="/docs/linux/man/8-febootstrap/">febootstrap</a></i>(8) into an initramfs image. This allows the new system to be booted on real hardware or inside a QEMU-based virtual machine. </p>
<p> An initramfs image is just a compressed cpio file, so you could uncompress it with <i><a href="/docs/linux/man/1-gunzip/">gunzip</a></i>(1) and use <i><a href="/docs/linux/man/1-cpio/">cpio</a></i>(1) to convert it into other formats. </p>
<p> The permissions inside the initrd image are corrected automatically (see the discussion of fakeroot logfile in the <i><a href="/docs/linux/man/8-febootstrap/">febootstrap</a></i>(8) page). You do <i>not</i> need to run this command as root.</p>
<h2>Options</h2>
<dl>
<dt>&#8211;files=filelist</p>
<dd><tt>&quot;filelist&quot;</tt> should be a file containing a list of the files to be added to the initramfs (one per line). Only those files are added and any others are ignored. </p>
<p> When the <tt>&quot;--files&quot;</tt> option is not given, all files in <tt>&quot;DIR&quot;</tt> are added to the initramfs image.</p>
<dt>&#8211;nocompress</p>
<dd>This prevents the initramfs image from being compressed. </p>
<p> Linux can boot from uncompressed initramfs images (in fact, faster), but they take up a lot more space on disk.</dl>
<h2>/init</h2>
<p>Normal initramfs images start by executing the program or script called <tt>&quot;/init&quot;</tt>. febootstrap does not create this script, so you may wish to, particularly for very minimal bootstraps that don&#8217;t have the normal SysVinit/upstart machinery. It&#8217;s also required if the kernel cannot find a &#8220;real&#8221; root filesystem (the root filesystem that we built and placed in an initramfs doesn&#8217;t count). </p>
<p> Linux will try to run the following commands in turn, unless you override it using the <tt>&quot;init=</tt>cmd<tt>&quot;</tt> kernel option:</p>
<dl>
<dt>*</p>
<dd>/init</p>
<dt>*</p>
<dd>/sbin/init</p>
<dt>*</p>
<dd>/etc/init</p>
<dt>*</p>
<dd>/bin/init</p>
<dt>*</p>
<dd>/bin/sh</dl>
<h2>Memory Requirements</h2>
<p>Initramfs images are uncompressed by the kernel into memory. When booting the new system you will need at least enough free <font SIZE="-1">RAM</font> to store the <code>uncompressed</code> filesystem plus extra to run any programs. Bear this in mind when creating very large filesystems.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-febootstrap/">febootstrap</a></i>(8), <i><a href="/docs/linux/man/1-cpio/">cpio</a></i>(1).</p>
<h2>Authors</h2>
<p>Richard W.M. Jones &lt;rjones @ redhat . com&gt;</p>
<h2>Copyright</h2>
<p>(C) Copyright 2009 Red Hat Inc., &lt;<a rel="nofollow" href="http://et.redhat.com/~rjones/febootstrap">http://et.redhat.com/~rjones/febootstrap</a>&gt;. </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT</font> <font SIZE="-1">ANY</font> <font SIZE="-1">WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS</font> <font SIZE="-1">FOR</font> A <font SIZE="-1">PARTICULAR</font> <font SIZE="-1">PURPOSE</font>. See the <font SIZE="-1">GNU</font> General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, <font SIZE="-1">MA</font> 02139, <font SIZE="-1">USA</font>.</p>
