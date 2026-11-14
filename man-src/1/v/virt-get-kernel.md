---
title: "virt-get-kernel(1)"
name: "virt-get-kernel"
section: "1"
letter: "v"
url: "/docs/linux/man/1-virt-get-kernel/"
description: "virt-get-kernel – Extract kernel and ramdisk from guests"
---

<h2 class="name">NAME</h2>
<p> virt-get-kernel &#8211; Extract kernel and ramdisk from guests </p>
<h2>SYNOPSIS</h2>
<pre><code>
virt - get - kernel[--options] - d domname virt - get - kernel[--options] - a disk.img
</code></pre>
<h2>DESCRIPTION</h2>
<p> This option extracts the kernel and initramfs from a guest. </p>
<p> The format of the disk image is automatically detected unless you specify it by using the <i>&#8211;format</i> option. </p>
<p> In the case where the guest contains multiple kernels, the one with the highest version number is chosen. To extract arbitrary kernels from the disk image, see <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1). To extract the entire <tt>&quot;/boot&quot;</tt> directory of a guest, see <i><a href="/docs/linux/man/1-virt-copy-out/">virt-copy-out</a></i>(1).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Display help.</p>
<dt><code>-a</code> file</p>
<dd>
<dt><code>&#8211;add</code> file</p>
<dd> Add <i>file</i> which should be a disk image from a virtual machine. </p>
<p> The format of the disk image is auto-detected. To override this and force a particular format use the <i>&#8211;format</i> option.</p>
<dt><code>-a</code> <font SIZE="-1">URI</font></p>
<dd>
<dt><code>&#8211;add</code> <font SIZE="-1">URI</font></p>
<dd> Add a remote disk. The <font SIZE="-1">URI</font> format is compatible with guestfish. See &#8220;<font SIZE="-1">ADDING REMOTE STORAGE&#8221;</font> in <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1).</p>
<dt><code>&#8211;colors</code></p>
<dd>
<dt><code>&#8211;colours</code></p>
<dd> Use <font SIZE="-1">ANSI</font> colour sequences to colourize messages. This is the default when the output is a tty. If the output of the program is redirected to a file, <font SIZE="-1">ANSI</font> colour sequences are disabled unless you use this option.</p>
<dt><code>-c</code> <font SIZE="-1">URI</font></p>
<dd>
<dt><code>&#8211;connect</code> <font SIZE="-1">URI</font></p>
<dd> If using libvirt, connect to the given <i></i><font SIZE="-1"><i>URI</i></font><i></i>. If omitted, then we connect to the default libvirt hypervisor. </p>
<p> If you specify guest block devices directly (<i>-a</i>), then libvirt is not used at all.</p>
<dt><code>-d</code> guest</p>
<dd>
<dt><code>&#8211;domain</code> guest</p>
<dd> Add all the disks from the named libvirt guest. Domain UUIDs can be used instead of names.</p>
<dt><code>&#8211;format</code> raw|qcow2|..</p>
<dd>
<dt><code>&#8211;format</code> auto</p>
<dd> The default for the <i>-a</i> option is to auto-detect the format of the disk image. Using this forces the disk format for the <i>-a</i> option on the command line. </p>
<p> If you have untrusted raw-format guest disk images, you should use this option to specify the disk format. This avoids a possible security problem with malicious guests (<font SIZE="-1">CVE-2010-3851</font>).</p>
<dt><code>&#8211;machine-readable</code></p>
<dd> This option is used to make the output more machine friendly when being parsed by other programs. See &#8220;<font SIZE="-1">MACHINE READABLE OUTPUT&#8221;</font> below.</p>
<dt><code>-o</code> directory</p>
<dd>
<dt><code>&#8211;output</code> directory</p>
<dd> This option specifies the output directory where kernel and initramfs from the guest are written. </p>
<p> If not specified, the default output is the current directory.</p>
<dt><code>&#8211;prefix</code> prefix</p>
<dd> This option specifies a prefix for the extracted files. </p>
<p> If a prefix is specified, then there will be a dash (<tt>&quot;-&quot;</tt>) after the prefix and before the rest of the file name; for example, a kernel in the guest like <tt>&quot;vmlinuz-3.19.0-20-generic&quot;</tt> is saved as <tt>&quot;mydistro-vmlinuz-3.19.0-20-generic&quot;</tt> when the prefix is <tt>&quot;mydistro&quot;</tt>. </p>
<p> See also <i>&#8211;unversioned-names</i>.</p>
<dt><code>-q</code></p>
<dd>
<dt><code>&#8211;quiet</code></p>
<dd> Don&#8217;t print ordinary progress messages.</p>
<dt><code>&#8211;unversioned-names</code></p>
<dd> This option affects the destination file name of extracted files. </p>
<p> If enabled, files will be saved locally just with the base name; for example, kernel and ramdisk in the guest like <tt>&quot;vmlinuz-3.19.0-20-generic&quot;</tt> and <tt>&quot;initrd.img-3.19.0-20-generic&quot;</tt> are saved respectively as <tt>&quot;vmlinuz&quot;</tt> and <tt>&quot;initrd.img&quot;</tt>. </p>
<p> See also <i>&#8211;prefix</i>.</p>
<dt><code>-v</code></p>
<dd>
<dt><code>&#8211;verbose</code></p>
<dd> Enable verbose messages for debugging.</p>
<dt><code>-V</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd> Display version number and exit.</p>
<dt><code>-x</code></p>
<dd> Enable tracing of libguestfs <font SIZE="-1">API</font> calls.</dl>
<h2>MACHINE READABLE OUTPUT</h2>
<p> The <i>&#8211;machine-readable</i> option can be used to make the output more machine friendly, which is useful when calling virt-get-kernel from other programs, GUIs etc. </p>
<p> Use the option on its own to query the capabilities of the virt-get-kernel binary. Typical output looks like this: </p>
<pre>
 $ virt-get-kernel --machine-readable
 virt-get-kernel
</pre>
<p> A list of features is printed, one per line, and the program exits with status 0.</p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> For other environment variables which affect all libguestfs programs, see &#8220;<font SIZE="-1">ENVIRONMENT VARIABLES&#8221;</font> in <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3).</p>
<h2>EXIT STATUS</h2>
<p> This program returns 0 if successful, or non-zero if there was an error.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3), <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1), <i><a href="/docs/linux/man/1-guestmount/">guestmount</a></i>(1), <i><a href="/docs/linux/man/1-virt-copy-out/">virt-copy-out</a></i>(1), <a rel="nofollow" href="http://libguestfs.org/.">http://libguestfs.org/.</a></p>
<h2>AUTHOR</h2>
<p> Richard W.M. Jones <a rel="nofollow" href="http://people.redhat.com/~rjones/">http://people.redhat.com/~rjones/</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2013-2016 Red Hat Inc.</p>
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
