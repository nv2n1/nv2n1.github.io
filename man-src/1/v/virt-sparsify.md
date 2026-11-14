---
title: "virt-sparsify(1)"
name: "virt-sparsify"
section: "1"
letter: "v"
url: "/docs/linux/man/1-virt-sparsify/"
description: "virt-sparsify – Make a virtual machine disk sparse"
---

<h2 class="name">NAME</h2>
<p> virt-sparsify &#8211; Make a virtual machine disk sparse </p>
<h2>SYNOPSIS</h2>
<pre><code>
virt - sparsify[--options] indisk outdisk virt - sparsify[--options]-- in - place disk
</code></pre>
<h2>WARNING</h2>
<p> Using <tt>&quot;virt-sparsify&quot;</tt> on live virtual machines, or concurrently with other disk editing tools, can be dangerous, potentially causing disk corruption. The virtual machine must be shut down before you use this command, and disk images must not be edited concurrently.</p>
<h2>DESCRIPTION</h2>
<p> Virt-sparsify is a tool which can make a virtual machine disk (or any disk image) sparse a.k.a. thin-provisioned. This means that free space within the disk image can be converted back to free space on the host. </p>
<p> Virt-sparsify can locate and sparsify free space in most filesystems (eg. ext2/3/4, btrfs, <font SIZE="-1">NTFS,</font> etc.), and also in <font SIZE="-1">LVM</font> physical volumes. </p>
<p> Virt-sparsify can also convert between some disk formats, for example converting a raw disk image to a thin-provisioned qcow2 image. </p>
<p> Virt-sparsify can operate on any disk image, not just ones from virtual machines. However if a virtual machine has multiple disks and uses volume management, then virt-sparsify will work but not be very effective (<a rel="nofollow" href="http://bugzilla.redhat.com/887826">http://bugzilla.redhat.com/887826</a>).</p>
<h3><font SIZE="-1">IMPORTANT NOTE ABOUT SPARSE OUTPUT IMAGES</font></h3>
<p> If the input is raw, then the default output is raw sparse. <code>You must check the output size using a tool that understands sparseness</code> such as <tt>&quot;du -sh&quot;</tt>. It can make a huge difference: </p>
<pre>
 $ ls -lh test1.img
 -rw-rw-r--. 1 rjones rjones 100M Aug  8 08:08 test1.img
 $ du -sh test1.img
 3.6M   test1.img
</pre>
<p> (Compare the apparent size <code>100M</code> vs the actual size <code>3.6M</code>)</p>
<h3><font SIZE="-1">IMPORTANT LIMITATIONS</font></h3>
<dl>
<dt>&bull;</p>
<dd> The virtual machine <i>must be shut down</i> before using this tool.</p>
<dt>&bull;</p>
<dd> Virt-sparsify may require up to 2x the virtual size of the source disk image (1 temporary copy + 1 destination image). This is in the worst case and usually much less space is required. </p>
<p> If you are using the <i>&#8211;in-place</i> option, then large amounts of temporary space are <code>not</code> required.</p>
<dt>&bull;</p>
<dd> Virt-sparsify cannot resize disk images. To do that, use <i><a href="/docs/linux/man/1-virt-resize/">virt-resize</a></i>(1).</p>
<dt>&bull;</p>
<dd> Virt-sparsify cannot handle encrypted disks. Libguestfs supports encrypted disks, but encrypted disks themselves cannot be sparsified.</p>
<dt>&bull;</p>
<dd> Virt-sparsify cannot yet sparsify the space between partitions. Note that this space is often used for critical items like bootloaders so it&#8217;s not really unused.</p>
<dt>&bull;</p>
<dd> In copy mode, qcow2 internal snapshots are not copied over to the destination image.</dl>
<p> You may also want to read the manual pages for the associated tools <i><a href="/docs/linux/man/1-virt-filesystems/">virt-filesystems</a></i>(1) and <i><a href="/docs/linux/man/1-virt-df/">virt-df</a></i>(1) before starting.</p>
<h2>EXAMPLES</h2>
<p> Typical usage is: </p>
<pre>
 virt-sparsify indisk outdisk
</pre>
<p> which copies <tt>&quot;indisk&quot;</tt> to <tt>&quot;outdisk&quot;</tt>, making the output sparse. <tt>&quot;outdisk&quot;</tt> is created, or overwritten if it already exists. The format of the input disk is detected (eg. qcow2) and the same format is used for the output disk. </p>
<p> To convert between formats, use the <i>&#8211;convert</i> option: </p>
<pre>
 virt-sparsify disk.raw --convert qcow2 disk.qcow2
</pre>
<p> Virt-sparsify tries to zero and sparsify free space on every filesystem it can find within the source disk image. You can get it to ignore (don&#8217;t zero free space on) certain filesystems by doing: </p>
<pre>
 virt-sparsify --ignore /dev/sda1 indisk outdisk
</pre>
<p> See <i><a href="/docs/linux/man/1-virt-filesystems/">virt-filesystems</a></i>(1) to get a list of filesystems within a disk image. </p>
<p> Since virt-sparsify ≥ 1.26, you can now sparsify a disk image in place by doing: </p>
<pre>
 virt-sparsify --in-place disk.img
</pre>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Display help.</p>
<dt><code>&#8211;check-tmpdir ignore</code></p>
<dd>
<dt><code>&#8211;check-tmpdir continue</code></p>
<dd>
<dt><code>&#8211;check-tmpdir warn</code></p>
<dd>
<dt><code>&#8211;check-tmpdir fail</code></p>
<dd> Check if &#8220;<font SIZE="-1">TMPDIR&#8221;</font> or <i>&#8211;tmp</i> directory has enough space to complete the operation. This is just an estimate. </p>
<p> If the check indicates a problem, then you can either:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <code>ignore</code> it,</p>
<dt>&bull;</p>
<dd> print a warning and <code>continue</code>,</p>
<dt>&bull;</p>
<dd> <code>warn</code> and wait for the user to press the Return key (this is the default), or:</p>
<dt>&bull;</p>
<dd> <code>fail</code> and exit.</dl>
</dl>
<dl>
<dt>
<dd>
<p> You cannot use this option and <i>&#8211;in-place</i> together.</dl>
<dt><code>&#8211;colors</code></p>
<dd>
<dt><code>&#8211;colours</code></p>
<dd> Use <font SIZE="-1">ANSI</font> colour sequences to colourize messages. This is the default when the output is a tty. If the output of the program is redirected to a file, <font SIZE="-1">ANSI</font> colour sequences are disabled unless you use this option.</p>
<dt><code>&#8211;compress</code></p>
<dd> Compress the output file. This <i>only</i> works if the output format is <tt>&quot;qcow2&quot;</tt>. </p>
<p> You cannot use this option and <i>&#8211;in-place</i> together.</p>
<dt><code>&#8211;convert</code> raw</p>
<dd>
<dt><code>&#8211;convert</code> qcow2</p>
<dd>
<dt><code>&#8211;convert</code> [other formats]</p>
<dd> Use <tt>&quot;output-format&quot;</tt> as the format for the destination image. If this is not specified, then the input format is used. </p>
<p> Supported and known-working output formats are: <tt>&quot;raw&quot;</tt>, <tt>&quot;qcow2&quot;</tt>, <tt>&quot;vdi&quot;</tt>. </p>
<p> You can also use any format supported by the <i><a href="/docs/linux/man/1-qemu-img/">qemu-img</a></i>(1) program, eg. <tt>&quot;vmdk&quot;</tt>, but support for other formats is reliant on qemu. </p>
<p> Specifying the <i>&#8211;convert</i> option is usually a good idea, because then virt-sparsify doesn&#8217;t need to try to guess the input format. </p>
<p> For fine-tuning the output format, see: <i>&#8211;compress</i>, <i>-o</i>. </p>
<p> You cannot use this option and <i>&#8211;in-place</i> together.</p>
<dt><code>&#8211;debug-gc</code></p>
<dd> Debug garbage collection and memory allocation. This is only useful when debugging memory problems in virt-sparsify or the OCaml libguestfs bindings.</p>
<dt><code>&#8211;format</code> raw</p>
<dd>
<dt><code>&#8211;format</code> qcow2</p>
<dd> Specify the format of the input disk image. If this flag is not given then it is auto-detected from the image itself. </p>
<p> If working with untrusted raw-format guest disk images, you should ensure the format is always specified.</p>
<dt><code>&#8211;ignore</code> filesystem</p>
<dd>
<dt><code>&#8211;ignore</code> volgroup</p>
<dd> Ignore the named filesystem. </p>
<p> When not using <i>&#8211;in-place</i>: Free space on the filesystem will not be zeroed, but existing blocks of zeroes will still be sparsified. </p>
<p> When using <i>&#8211;in-place</i>, the filesystem is ignored completely. </p>
<p> In the second form, this ignores the named volume group. Use the volume group name without the <i>/dev/</i> prefix, eg. <i>&#8211;ignore vg_foo</i> </p>
<p> You can give this option multiple times.</p>
<dt><code>&#8211;in-place</code></p>
<dd> Do in-place sparsification instead of copying sparsification. See &#8220;IN-PLACE <font SIZE="-1">SPARSIFICATION&#8221;</font> below.</p>
<dt><code>&#8211;machine-readable</code></p>
<dd> This option is used to make the output more machine friendly when being parsed by other programs. See &#8220;<font SIZE="-1">MACHINE READABLE OUTPUT&#8221;</font> below.</p>
<dt><code>-o</code> option[,option,&#8230;]</p>
<dd> Pass <i>-o</i> option(s) to the <i><a href="/docs/linux/man/1-qemu-img/">qemu-img</a></i>(1) command to fine-tune the output format. Options available depend on the output format (see <i>&#8211;convert</i>) and the installed version of the qemu-img program. </p>
<p> You should use <i>-o</i> at most once. To pass multiple options, separate them with commas, eg: </p>
<pre>
 virt-sparsify --convert qcow2 \
   -o cluster_size=512,preallocation=metadata ...
</pre>
<p> You cannot use this option and <i>&#8211;in-place</i> together.</p>
<dt><code>-q</code></p>
<dd>
<dt><code>&#8211;quiet</code></p>
<dd> This disables progress bars and other unnecessary output.</p>
<dt><code>&#8211;tmp</code> block_device</p>
<dd>
<dt><code>&#8211;tmp</code> dir</p>
<dd> In copying mode only, use the named device or directory as the location of the temporary overlay (see also &#8220;<font SIZE="-1">TMPDIR&#8221;</font> below). </p>
<p> If the parameter given is a block device, then the block device is written to directly. <code>Note this erases the existing contents of the block device</code>. </p>
<p> If the parameter is a directory, then this is the same as setting the &#8220;<font SIZE="-1">TMPDIR&#8221;</font> environment variable. </p>
<p> You cannot use this option and <i>&#8211;in-place</i> together.</p>
<dt><code>&#8211;tmp</code> prebuilt:file</p>
<dd> In copying mode only, the specialized option <i>&#8211;tmp prebuilt:file</i> (where <tt>&quot;prebuilt:&quot;</tt> is a literal string) causes virt-sparsify to use the qcow2 <tt>&quot;file&quot;</tt> as temporary space.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> The file <code>must</code> be freshly formatted as qcow2, with indisk as the backing file.</p>
<dt>&bull;</p>
<dd> If you rerun virt-sparsify, you <code>must</code> recreate the file before each run.</p>
<dt>&bull;</p>
<dd> Virt-sparsify does not delete the file.</dl>
</dl>
<dl>
<dt>
<dd>
<p> This option is used by oVirt which requires a specially formatted temporary file.</dl>
<dt><code>-v</code></p>
<dd>
<dt><code>&#8211;verbose</code></p>
<dd> Enable verbose messages for debugging.</p>
<dt><code>-V</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd> Display version number and exit.</p>
<dt><code>-x</code></p>
<dd> Enable tracing of libguestfs <font SIZE="-1">API</font> calls.</p>
<dt><code>&#8211;zero</code> partition</p>
<dd>
<dt><code>&#8211;zero</code> logvol</p>
<dd> Zero the contents of the named partition or logical volume in the guest. All data on the device is lost, but sparsification is excellent! You can give this option multiple times.</dl>
<h2>IN-PLACE SPARSIFICATION</h2>
<p> Since virt-sparsify ≥ 1.26, the tool is able to do in-place sparsification (instead of copying from an input disk to an output disk). This is more efficient. It is not able to recover quite as much space as copying sparsification. </p>
<p> To use this mode, specify a disk image which will be modified in place: </p>
<pre>
 virt-sparsify --in-place disk.img
</pre>
<p> Some options are not compatible with this mode: <i>&#8211;convert</i>, <i>&#8211;compress</i> and <i>-o</i> because they require wholesale disk format changes; <i>&#8211;check-tmpdir</i> because large amounts of temporary space are not required. </p>
<p> In-place sparsification works using discard (a.k.a trim or unmap) support.</p>
<h2>MACHINE READABLE OUTPUT</h2>
<p> The <i>&#8211;machine-readable</i> option can be used to make the output more machine friendly, which is useful when calling virt-sparsify from other programs, GUIs etc. </p>
<p> There are two ways to use this option. </p>
<p> Firstly use the option on its own to query the capabilities of the virt-sparsify binary. Typical output looks like this: </p>
<pre>
 $ virt-sparsify --machine-readable
 virt-sparsify
 ntfs
 btrfs
</pre>
<p> A list of features is printed, one per line, and the program exits with status 0. </p>
<p> Secondly use the option in conjunction with other options to make the regular program output more machine friendly. </p>
<p> At the moment this means:</p>
<dl>
<dt>1.</p>
<dd> Progress bar messages can be parsed from stdout by looking for this regular expression: </p>
<pre><code>
^[0 - 9] + / [0 - 9] + $
</code></pre>
<dt>2.</p>
<dd> The calling program should treat messages sent to stdout (except for progress bar messages) as status messages. They can be logged and/or displayed to the user.</p>
<dt>3.</p>
<dd> The calling program should treat messages sent to stderr as error messages. In addition, virt-sparsify exits with a non-zero status code if there was a fatal error.</dl>
<p> All versions of virt-sparsify have supported the <i>&#8211;machine-readable</i> option.</p>
<h2>WINDOWS 8</h2>
<p> Windows 8 &#8220;fast startup&#8221; can prevent virt-sparsify from working. See &#8220;<font SIZE="-1">WINDOWS HIBERNATION AND WINDOWS 8 FAST STARTUP&#8221;</font> in <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3).</p>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><font SIZE="-1">TMPDIR</font></p>
<dd> Location of the temporary directory used for the potentially large temporary overlay file. </p>
<p> In virt-sparsify ≥ 1.28, you can override this environment variable using the <i>&#8211;tmp</i> option. </p>
<p> You should ensure there is enough free space in the worst case for a full copy of the source disk (<i>virtual</i> size), or else set <tt>$TMPDIR</tt> to point to another directory that has enough space. </p>
<p> This defaults to <i>/tmp</i>. </p>
<p> Note that if <tt>$TMPDIR</tt> is a tmpfs (eg. if <i>/tmp</i> is on tmpfs, or if you use <tt>&quot;TMPDIR=/dev/shm&quot;</tt>), tmpfs defaults to a maximum size of <i>half</i> of physical <font SIZE="-1">RAM. </font> If virt-sparsify exceeds this, it will hang. The solution is either to use a real disk, or to increase the maximum size of the tmpfs mountpoint, eg: </p>
<pre>
 mount -o remount,size=10G /tmp
</pre>
<p> If you are using the <i>&#8211;in-place</i> option, then large amounts of temporary space are <code>not</code> required.</dl>
<p> For other environment variables, see &#8220;<font SIZE="-1">ENVIRONMENT VARIABLES&#8221;</font> in <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3).</p>
<h2>EXIT STATUS</h2>
<p> This program returns 0 if the operation completed without errors. (This doesn&#8217;t necessarily mean that space could be freed up.) </p>
<p> A non-zero exit code indicates an error. </p>
<p> If the exit code is <tt>3</tt> and the <i>&#8211;in-place</i> option was used, that indicates that discard support is not available in libguestfs, so copying mode must be used instead.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-virt-df/">virt-df</a></i>(1), <i><a href="/docs/linux/man/1-virt-filesystems/">virt-filesystems</a></i>(1), <i><a href="/docs/linux/man/1-virt-resize/">virt-resize</a></i>(1), <i><a href="/docs/linux/man/1-virt-rescue/">virt-rescue</a></i>(1), <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3), <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1), <i><a href="/docs/linux/man/1-truncate/">truncate</a></i>(1), <i><a href="/docs/linux/man/1-fallocate/">fallocate</a></i>(1), <i><a href="/docs/linux/man/1-qemu-img/">qemu-img</a></i>(1), <a rel="nofollow" href="http://libguestfs.org/.">http://libguestfs.org/.</a></p>
<h2>AUTHOR</h2>
<p> Richard W.M. Jones <a rel="nofollow" href="http://people.redhat.com/~rjones/">http://people.redhat.com/~rjones/</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2011-2016 Red Hat Inc.</p>
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
<dt><a href="#lbAH">EXAMPLES</a></p>
<dd>
<dt><a href="#lbAI">OPTIONS</a></p>
<dd>
<dt><a href="#lbAJ">IN-PLACE SPARSIFICATION</a></p>
<dd>
<dt><a href="#lbAK">MACHINE READABLE OUTPUT</a></p>
<dd>
<dt><a href="#lbAL">WINDOWS 8</a></p>
<dd>
<dt><a href="#lbAM">ENVIRONMENT VARIABLES</a></p>
<dd>
<dt><a href="#lbAN">EXIT STATUS</a></p>
<dd>
<dt><a href="#lbAO">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAP">AUTHOR</a></p>
<dd>
<dt><a href="#lbAQ">COPYRIGHT</a></p>
<dd>
<dt><a href="#lbAR">LICENSE</a></p>
<dd>
<dt><a href="#lbAS">BUGS</a></p>
<dd></dl>
