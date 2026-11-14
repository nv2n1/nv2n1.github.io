---
title: "virt-list-filesystems(1)"
name: "virt-list-filesystems"
section: "1"
letter: "v"
url: "/docs/linux/man/1-virt-list-filesystems/"
description: "virt-list-filesystems – List filesystems in a virtual machine or disk image"
---

<h2 class="name">NAME</h2>
<p> virt-list-filesystems &#8211; List filesystems in a virtual machine or disk image </p>
<h2>SYNOPSIS</h2>
<pre><code>
virt - list - filesystems[--options] domname virt - list - filesystems[--options] disk.img[disk.img...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> <tt>&quot;virt-list-filesystems&quot;</tt> is a command line tool to list the filesystems that are contained in a virtual machine or disk image. </p>
<p> <tt>&quot;virt-list-filesystems&quot;</tt> is just a simple wrapper around <i><a href="/docs/linux/man/3-libguestfs/">libguestfs</a></i>(3) functionality. For more complex cases you should look at the <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1) tool.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Display brief help.</p>
<dt><code>&#8211;version</code></p>
<dd> Display version number and exit.</p>
<dt><code>&#8211;connect </code><font SIZE="-1"><code>URI</code></font> | <code>-c </code><font SIZE="-1"><code>URI</code></font></p>
<dd> If using libvirt, connect to the given <i></i><font SIZE="-1"><i>URI</i></font><i></i>. If omitted, then we connect to the default libvirt hypervisor. </p>
<p> If you specify guest block devices directly, then libvirt is not used at all.</p>
<dt><code>-l</code> | <code>&#8211;long</code></p>
<dd> With this option, <tt>&quot;virt-list-filesystems&quot;</tt> displays the type of each filesystem too (where &#8220;type&#8221; means <tt>&quot;ext3&quot;</tt>, <tt>&quot;xfs&quot;</tt> etc.)</p>
<dt><code>-a</code> | <code>&#8211;all</code></p>
<dd> Normally we only show mountable filesystems. If this option is given then swap devices are shown too.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3), <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1), <i><a href="/docs/linux/man/1-virt-cat/">virt-cat</a></i>(1), <i><a href="/docs/linux/man/1-virt-tar/">virt-tar</a></i>(1), <i><a href="/docs/linux/man/1-virt-list-partitions/">virt-list-partitions</a></i>(1), <i><a href="/docs/linux/man/3-sys--guestfs/">Sys::Guestfs</a></i>(3), <i><a href="/docs/linux/man/3-sys--guestfs--lib/">Sys::Guestfs::Lib</a></i>(3), <i><a href="/docs/linux/man/3-sys--virt/">Sys::Virt</a></i>(3), &lt;<a rel="nofollow" href="http://libguestfs.org/">http://libguestfs.org/</a>&gt;.</p>
<h2>AUTHOR</h2>
<p> Richard W.M. Jones &lt;<a rel="nofollow" href="http://people.redhat.com/~rjones/">http://people.redhat.com/~rjones/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2009 Red Hat Inc. </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT</font> <font SIZE="-1">ANY</font> <font SIZE="-1">WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS</font> <font SIZE="-1">FOR</font> A <font SIZE="-1">PARTICULAR</font> <font SIZE="-1">PURPOSE</font>. See the <font SIZE="-1">GNU</font> General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, <font SIZE="-1">MA</font> 02139, <font SIZE="-1">USA</font>. </p>
<h2>Index</h2>
