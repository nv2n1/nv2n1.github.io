---
title: "virt-copy-out(1)"
name: "virt-copy-out"
section: "1"
letter: "v"
url: "/docs/linux/man/1-virt-copy-out/"
description: "virt-copy-out – Copy files and directories out of a virtual machine disk image."
---

<h2 class="name">NAME</h2>
<p> virt-copy-out &#8211; Copy files and directories out of a virtual machine disk image. </p>
<h2>SYNOPSIS</h2>
<pre><code>
virt - copy - out - a disk.img / file | dir[/ file | dir...] localdir virt - copy - out - d domain / file | dir[/ file | dir...] localdir
</code></pre>
<h2>DESCRIPTION</h2>
<p> <tt>&quot;virt-copy-out&quot;</tt> copies files and directories out of a virtual machine disk image or named libvirt domain. </p>
<p> You can give one of more filenames and directories on the command line. Directories are copied out recursively.</p>
<h2>EXAMPLES</h2>
<p> Download the home directories from a virtual machine: </p>
<pre>
 mkdir homes
 virt-copy-out -d MyGuest /home homes
</pre>
<h2>JUST A SHELL SCRIPT WRAPPER AROUND GUESTFISH</h2>
<p> This command is just a simple shell script wrapper around the <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1) <tt>&quot;copy-out&quot;</tt> command. For anything more complex than a trivial copy, you are probably better off using guestfish directly.</p>
<h2>OPTIONS</h2>
<p> Since the shell script just passes options straight to guestfish, read <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1) to see the full list of options.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1), <i><a href="/docs/linux/man/1-virt-cat/">virt-cat</a></i>(1), <i><a href="/docs/linux/man/1-virt-copy-in/">virt-copy-in</a></i>(1), <i><a href="/docs/linux/man/1-virt-edit/">virt-edit</a></i>(1), <i><a href="/docs/linux/man/1-virt-tar-in/">virt-tar-in</a></i>(1), <i><a href="/docs/linux/man/1-virt-tar-out/">virt-tar-out</a></i>(1), <a rel="nofollow" href="http://libguestfs.org/.">http://libguestfs.org/.</a></p>
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
