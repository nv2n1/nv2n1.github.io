---
title: "virt-tar-in(1)"
name: "virt-tar-in"
section: "1"
letter: "v"
url: "/docs/linux/man/1-virt-tar-in/"
description: "virt-tar-in – Unpack a tarball into a virtual machine disk image."
---

<h2 class="name">NAME</h2>
<p> virt-tar-in &#8211; Unpack a tarball into a virtual machine disk image. </p>
<h2>SYNOPSIS</h2>
<pre>
 virt-tar-in -a disk.img data.tar /destination
 virt-tar-in -d domain data.tar /destination
 zcat data.tar.gz | virt-tar-in -d domain - /destination
</pre>
<h2>WARNING</h2>
<p> Using <tt>&quot;virt-tar-in&quot;</tt> on live virtual machines, or concurrently with other disk editing tools, can be dangerous, potentially causing disk corruption. The virtual machine must be shut down before you use this command, and disk images must not be edited concurrently.</p>
<h2>DESCRIPTION</h2>
<p> <tt>&quot;virt-tar-in&quot;</tt> unpacks an uncompressed tarball into a virtual machine disk image or named libvirt domain. </p>
<p> The first parameter is the tar file. Use <tt>&quot;-&quot;</tt> to read the tar file from standard input. The second parameter is the absolute target directory to unpack into.</p>
<h2>EXAMPLES</h2>
<p> Upload a home directory to a guest: </p>
<pre>
 virt-tar-in -d MyGuest homes.tar /home
</pre>
<h2>JUST A SHELL SCRIPT WRAPPER AROUND GUESTFISH</h2>
<p> This command is just a simple shell script wrapper around the <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1) <tt>&quot;tar-in&quot;</tt> command. For anything more complex than a trivial copy, you are probably better off using guestfish directly.</p>
<h2>OPTIONS</h2>
<p> Since the shell script just passes options straight to guestfish, read <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1) to see the full list of options.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1), <i><a href="/docs/linux/man/1-virt-cat/">virt-cat</a></i>(1), <i><a href="/docs/linux/man/1-virt-copy-in/">virt-copy-in</a></i>(1), <i><a href="/docs/linux/man/1-virt-copy-out/">virt-copy-out</a></i>(1), <i><a href="/docs/linux/man/1-virt-edit/">virt-edit</a></i>(1), <i><a href="/docs/linux/man/1-virt-make-fs/">virt-make-fs</a></i>(1), <i><a href="/docs/linux/man/1-virt-tar-out/">virt-tar-out</a></i>(1), <a rel="nofollow" href="http://libguestfs.org/.">http://libguestfs.org/.</a></p>
<h2>AUTHORS</h2>
<p> Richard W.M. Jones (<tt>&quot;rjones at redhat dot com&quot;</tt>)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2011-2012 Red Hat Inc.</p>
<h2>LICENSE</h2>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE. </font> See the <font SIZE="-1">GNU</font> General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, <font SIZE="-1">MA 02110-1301 USA.</font></p>
<h2>BUGS</h2>
<p> To get a list of bugs against libguestfs, use this link: <a rel="nofollow" href="https://bugzilla.redhat.com/buglist.cgi?component=libguestfs">https://bugzilla.redhat.com/buglist.cgi?component=libguestfs</a>&amp;product=Virtualization+Tools </p>
<p> To report a new bug against libguestfs, use this link: <a rel="nofollow" href="https://bugzilla.redhat.com/enter_bug.cgi?component=libguestfs">https://bugzilla.redhat.com/enter_bug.cgi?component=libguestfs</a>&amp;product=Virtualization+Tools </p>
<p> When reporting a bug, please supply:</p>
<dl>
<dt>&bull;</p>
<dd> The version of libguestfs.</p>
<dt>&bull;</p>
<dd> Where you got libguestfs (eg. which Linux distro, compiled from source, etc)</p>
<dt>&bull;</p>
<dd> Describe the bug accurately and give a way to reproduce it.</p>
<dt>&bull;</p>
<dd> Run <i><a href="/docs/linux/man/1-libguestfs-test-tool/">libguestfs-test-tool</a></i>(1) and paste the <code>complete, unedited</code> output into the bug report. </p>
</dl>
<h2>Index</h2>
