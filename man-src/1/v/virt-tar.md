---
title: "virt-tar(1)"
name: "virt-tar"
section: "1"
letter: "v"
url: "/docs/linux/man/1-virt-tar/"
description: "virt-tar – Extract or upload files to a virtual machine"
---

<h2 class="name">NAME</h2>
<p> virt-tar &#8211; Extract or upload files to a virtual machine </p>
<h2>SYNOPSIS</h2>
<pre><code>
virt - tar[--options] - x domname directory tarball virt - tar[--options] - u domname tarball directory virt - tar[--options] disk.img[disk.img...] - x directory tarball virt - tar[--options] disk.img[disk.img...] - u tarball directory
</code></pre>
<h2>EXAMPLES</h2>
<p> Download <tt>&quot;/home&quot;</tt> from the <font SIZE="-1">VM</font> into a local tarball: </p>
<pre>
 virt-tar -x domname /home home.tar
 virt-tar -zx domname /home home.tar.gz
</pre>
<p> Upload a local tarball and unpack it inside <tt>&quot;/tmp&quot;</tt> in the <font SIZE="-1">VM:</font> </p>
<pre>
 virt-tar -u domname uploadstuff.tar /tmp
 virt-tar -zu domname uploadstuff.tar.gz /tmp
</pre>
<h2>WARNING</h2>
<p> You must <i>not</i> use <tt>&quot;virt-tar&quot;</tt> with the <tt>&quot;-u&quot;</tt> option (upload) on live virtual machines. If you do this, you risk disk corruption in the <font SIZE="-1">VM</font>. <tt>&quot;virt-tar&quot;</tt> tries to stop you from doing this, but doesn&#8217;t catch all cases. </p>
<p> You can use <tt>&quot;-x&quot;</tt> (extract) on live virtual machines, but you might get inconsistent results or errors if there is filesystem activity inside the <font SIZE="-1">VM</font>. If the live <font SIZE="-1">VM</font> is synched and quiescent, then <tt>&quot;virt-tar&quot;</tt> will usually work, but the only way to guarantee consistent results is if the virtual machine is shut down.</p>
<h2>DESCRIPTION</h2>
<p> <tt>&quot;virt-tar&quot;</tt> is a general purpose archive tool for downloading and uploading parts of a guest filesystem. There are many possibilities: making backups, uploading data files, snooping on guest activity, fixing or customizing guests, etc. </p>
<p> If you want to just view a single file, use <i><a href="/docs/linux/man/1-virt-cat/">virt-cat</a></i>(1). If you just want to edit a single file, use <i><a href="/docs/linux/man/1-virt-edit/">virt-edit</a></i>(1). For more complex cases you should look at the <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1) tool. </p>
<p> There are two modes of operation: <tt>&quot;-x&quot;</tt> (eXtract) downloads a directory and its contents (recursively) from the virtual machine into a local tarball. <tt>&quot;-u&quot;</tt> uploads from a local tarball, unpacking it into a directory inside the virtual machine. You cannot use these two options together. </p>
<p> In addition, you may need to use the <tt>&quot;-z&quot;</tt> (gZip) option to enable compression. When uploading, you have to specify <tt>&quot;-z&quot;</tt> if the upload file is compressed because virt-tar won&#8217;t detect this on its own. </p>
<p> <tt>&quot;virt-tar&quot;</tt> can only handle tar (optionally gzipped) format tarballs. For example it cannot do PKZip files or bzip2 compression. If you want that then you&#8217;ll have to rebuild the tarballs yourself. (This is a limitation of the <i><a href="/docs/linux/man/3-libguestfs/">libguestfs</a></i>(3) <font SIZE="-1">API</font>).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Display brief help.</p>
<dt><code>&#8211;version</code></p>
<dd> Display version number and exit.</p>
<dt><code>&#8211;connect </code><font SIZE="-1"><code>URI</code></font> | <code>-c </code><font SIZE="-1"><code>URI</code></font></p>
<dd> If using libvirt, connect to the given <i></i><font SIZE="-1"><i>URI</i></font><i></i>. If omitted, then we connect to the default libvirt hypervisor. </p>
<p> If you specify guest block devices directly, then libvirt is not used at all.</p>
<dt><code>-x</code> | <code>&#8211;extract</code> | <code>&#8211;download</code></p>
<dd>
<dt><code>-u</code> | <code>&#8211;upload</code></p>
<dd> Use <tt>&quot;-x&quot;</tt> to extract (download) a directory from a virtual machine to a local tarball. </p>
<p> Use <tt>&quot;-u&quot;</tt> to upload and unpack from a local tarball into a virtual machine. Please read the &#8220;<font SIZE="-1">WARNING</font>&#8221; section above before using this option. </p>
<p> You must specify exactly one of these options.</p>
<dt><code>-z</code> | <code>&#8211;gzip</code></p>
<dd> Specify that the input or output tarball is gzip-compressed.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3), <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1), <i><a href="/docs/linux/man/1-virt-cat/">virt-cat</a></i>(1), <i><a href="/docs/linux/man/1-virt-edit/">virt-edit</a></i>(1), <i><a href="/docs/linux/man/3-sys--guestfs/">Sys::Guestfs</a></i>(3), <i><a href="/docs/linux/man/3-sys--guestfs--lib/">Sys::Guestfs::Lib</a></i>(3), <i><a href="/docs/linux/man/3-sys--virt/">Sys::Virt</a></i>(3), &lt;<a rel="nofollow" href="http://libguestfs.org/">http://libguestfs.org/</a>&gt;.</p>
<h2>AUTHOR</h2>
<p> Richard W.M. Jones &lt;<a rel="nofollow" href="http://people.redhat.com/~rjones/">http://people.redhat.com/~rjones/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2009 Red Hat Inc. </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT</font> <font SIZE="-1">ANY</font> <font SIZE="-1">WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS</font> <font SIZE="-1">FOR</font> A <font SIZE="-1">PARTICULAR</font> <font SIZE="-1">PURPOSE</font>. See the <font SIZE="-1">GNU</font> General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, <font SIZE="-1">MA</font> 02139, <font SIZE="-1">USA</font>. </p>
<h2>Index</h2>
