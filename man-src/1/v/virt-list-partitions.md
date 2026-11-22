---

title: "virt-list-partitions(1)"
name: "virt-list-partitions"
section: "1"
letter: "v"
url: "/docs/linux/man/1-virt-list-partitions/"
description: "virt-list-partitions – List partitions in a virtual machine or disk image"
---

<p> virt-list-partitions &#8211; List partitions in a virtual machine or disk image </p>
<h2>SYNOPSIS</h2>
<pre><code>
virt - list - partitions[--options] domname virt - list - partitions[--options] disk.img[disk.img...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> <tt>&quot;virt-list-partitions&quot;</tt> is a command line tool to list the partitions that are contained in a virtual machine or disk image. It is mainly useful as a first step to using <i><a href="/docs/linux/man/1-virt-resize/">virt-resize</a></i>(1). </p>
<p> <tt>&quot;virt-list-partitions&quot;</tt> is just a simple wrapper around <i>libguestfs</i>(3) functionality. For more complex cases you should look at the <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1) tool.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></dt>
<dd> Display brief help.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Display version number and exit.</dd>
<dt><code>&#8211;connect </code><code>URI</code> | <code>-c </code><code>URI</code></dt>
<dd> If using libvirt, connect to the given <i></i><i>URI</i><i></i>. If omitted, then we connect to the default libvirt hypervisor. </dd>
<p> If you specify guest block devices directly, then libvirt is not used at all.</p>
<dt><code>-l</code> | <code>&#8211;long</code></dt>
<dd> With this option, <tt>&quot;virt-list-partitions&quot;</tt> displays the type and size of each partition too (where &#8220;type&#8221; means <tt>&quot;ext3&quot;</tt>, <tt>&quot;pv&quot;</tt> etc.)</dd>
<dt><code>-h</code> | <code>&#8211;human-readable</code></dt>
<dd> Show sizes in human-readable form (eg. &#8220;1G&#8221;).</dd></dl>
<h2>SEE ALSO</h2>
<p> <i>guestfs</i>(3), <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1), <i><a href="/docs/linux/man/1-virt-list-filesystems/">virt-list-filesystems</a></i>(1), <i><a href="/docs/linux/man/1-virt-resize/">virt-resize</a></i>(1), <i>Sys::Guestfs</i>(3), <i>Sys::Guestfs::Lib</i>(3), <i>Sys::Virt</i>(3), &lt;<a rel="nofollow" href="http://libguestfs.org/">http://libguestfs.org/</a>&gt;.</p>
<h2>AUTHOR</h2>
<p> Richard W.M. Jones &lt;<a rel="nofollow" href="http://people.redhat.com/~rjones/">http://people.redhat.com/~rjones/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2009-2010 Red Hat Inc. </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA. </p>
