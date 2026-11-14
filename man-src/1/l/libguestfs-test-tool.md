---
title: "libguestfs-test-tool(1)"
name: "libguestfs-test-tool"
section: "1"
letter: "l"
url: "/docs/linux/man/1-libguestfs-test-tool/"
description: "libguestfs-test-tool – Diagnostics for libguestfs"
---

<h2 class="name">NAME</h2>
<p> libguestfs-test-tool &#8211; Diagnostics for libguestfs </p>
<h2>SYNOPSIS</h2>
<pre>
 libguestfs-test-tool [--options]
</pre>
<h2>DESCRIPTION</h2>
<p> libguestfs-test-tool is a test program shipped with libguestfs to allow you to check basic libguestfs functionality is working. This is needed because libguestfs occasionally breaks for reasons beyond our control: usually because of changes in the underlying qemu or kernel packages, or the host environment. </p>
<p> If you suspect a problem in libguestfs, then just run: </p>
<pre>
 libguestfs-test-tool
</pre>
<p> It will print lots of diagnostic messages. </p>
<p> If it runs to completion successfully, you will see this near the end: </p>
<pre><code>
== == = TEST FINISHED OK == == =
</code></pre>
<p> and the test tool will exit with code 0. </p>
<p> If it fails (and/or exits with non-zero error code), please paste the <i>complete, unedited</i> output of the test tool into a bug report. More information about reporting bugs can be found on the <a rel="nofollow" href="http://libguestfs.org/">http://libguestfs.org/</a> website.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Display short usage information and exit.</p>
<dt><code>&#8211;qemu qemu_binary</code></p>
<dd> If you have downloaded another qemu binary, point this option at the full path of the binary to try it.</p>
<dt><code>&#8211;qemudir qemu_source_dir</code></p>
<dd> If you have compiled qemu from source, point this option at the source directory to try it.</p>
<dt><code>-t N</code></p>
<dd>
<dt><code>&#8211;timeout N</code></p>
<dd> Set the launch timeout to <tt>&quot;N&quot;</tt> seconds. The default is 600 seconds (10 minutes) which does not usually need to be adjusted.</p>
<dt><code>-V</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd> Display the libguestfs version number and exit.</dl>
<h2>TRYING OUT A DIFFERENT VERSION OF QEMU</h2>
<p> If you have compiled another version of qemu from source and would like to try that, then you can use the <i>&#8211;qemudir</i> option to point to the qemu source directory. </p>
<p> If you have downloaded a qemu binary from somewhere, use the <i>&#8211;qemu</i> option to point to the binary. </p>
<p> Note when using these options, you can ignore the business of qemu wrapper scripts (&#8220;<font SIZE="-1">QEMU WRAPPERS&#8221;</font> in <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3)), since libguestfs-test-tool writes a wrapper script for you if one is needed.</p>
<h2>TRYING OUT A DIFFERENT KERNEL</h2>
<p> You can tell supermin to try a different kernel. You do this by setting the environment variables <tt>&quot;SUPERMIN_KERNEL&quot;</tt>, <tt>&quot;SUPERMIN_KERNEL_VERSION&quot;</tt> and/or <tt>&quot;SUPERMIN_MODULES&quot;</tt>. </p>
<p> Refer to &#8220;<font SIZE="-1">ENVIRONMENT VARIABLES&#8221;</font> in <i><a href="/docs/linux/man/1-supermin/">supermin</a></i>(1) for further information.</p>
<h2>TRYING OUT A DIFFERENT VERSION OF LIBVIRT</h2>
<p> To find out which backend is the default in your libguestfs package, do: </p>
<pre>
 unset LIBGUESTFS_BACKEND
 guestfish get-backend
</pre>
<p> If you are using the libvirt backend, then you can try out a different (eg. upstream) version of libvirt by running these commands (<i>not</i> as root): </p>
<pre>
 killall libvirtd lt-libvirtd
 ~/path/to/libvirt/run libguestfs-test-tool
</pre>
<p> The first command kills any session <tt>&quot;libvirtd&quot;</tt> process(es) that may be running on the machine. The second command uses libvirt&#8217;s <tt>&quot;run&quot;</tt> script (in the top-level libvirt build directory) to set some environment variables so that the alternate version of libvirt is used to run the program.</p>
<h2>TRYING OUT WITH / WITHOUT LIBVIRT</h2>
<p> To find out which backend is the default in your libguestfs package, do: </p>
<pre>
 unset LIBGUESTFS_BACKEND
 guestfish get-backend
</pre>
<p> If you are using the libvirt backend, you can try without (ie. libguestfs directly launching qemu) by doing: </p>
<pre>
 export LIBGUESTFS_BACKEND=direct
</pre>
<p> Or if you are using the default (direct) backend, then you can try libvirt: </p>
<pre>
 export LIBGUESTFS_BACKEND=libvirt
</pre>
<p> or with libvirt and a specific libvirt <font SIZE="-1">URI</font>: </p>
<pre>
 export LIBGUESTFS_BACKEND=libvirt:<a href="qemu:///session">qemu:///session</a>
</pre>
<h2>TRYING OUT DIFFERENT SELINUX SETTINGS</h2>
<p> To find out which backend is the default in your libguestfs package, do: </p>
<pre>
 unset LIBGUESTFS_BACKEND
 guestfish get-backend
</pre>
<p> To find out if SELinux is being used, do: </p>
<pre>
 getenforce
</pre>
<p> If you are using libvirt, SELinux and sVirt, then you can try to see if changing SELinux to &#8220;permissive&#8221; mode makes any difference. Use this command as root: </p>
<pre>
 setenforce Permissive
</pre>
<p> If this makes a difference, look in the audit logs for recent failures (&#8220;AVCs&#8221;): </p>
<pre>
 ausearch -m avc -ts recent
</pre>
<p> You can convert AVCs into suggested SELinux policy rules using tools like <i><a href="/docs/linux/man/1-audit2allow/">audit2allow</a></i>(1). For more information, see the &#8220;Security Enhanced Linux User Guide&#8221;. </p>
<p> To reenable SELinux and sVirt, do: </p>
<pre>
 setenforce Enforcing
</pre>
<h2>SELF-DIAGNOSIS</h2>
<p> Refer to &#8220;<font SIZE="-1">APPLIANCE BOOT PROCESS&#8221;</font> in <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3) to understand the messages produced by libguestfs-test-tool and/or possible errors.</p>
<h2>EXIT STATUS</h2>
<p> libguestfs-test-tool returns <i>0</i> if the tests completed without error, or <i>1</i> if there was an error.</p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> For the full list of environment variables which may affect libguestfs, please see the <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3) manual page.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3), <a rel="nofollow" href="http://libguestfs.org/,">http://libguestfs.org/,</a> <a rel="nofollow" href="http://qemu.org/.">http://qemu.org/.</a></p>
<h2>AUTHORS</h2>
<p> Richard W.M. Jones (<tt>&quot;rjones at redhat dot com&quot;</tt>)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2009-2016 Red Hat Inc.</p>
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
