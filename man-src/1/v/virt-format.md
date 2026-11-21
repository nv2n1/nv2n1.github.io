---

title: "virt-format(1)"
name: "virt-format"
section: "1"
letter: "v"
url: "/docs/linux/man/1-virt-format/"
description: "virt-format – Erase and make a blank disk"
---

<pre><code>
virt - format[--options] - a disk.img[-a disk.img...]
</code></pre>
<h2>WARNING</h2>
<p> Using <tt>&quot;virt-format&quot;</tt> on live virtual machines, or concurrently with other disk editing tools, can be dangerous, potentially causing disk corruption. The virtual machine must be shut down before you use this command, and disk images must not be edited concurrently.</p>
<p> Virt-format takes an existing disk file (or it can be a host partition, <font SIZE="-1">LV</font> etc), <code>erases all data on it</code>, and formats it as a blank disk. It can optionally create partition tables, empty filesystems, logical volumes and more. </p>
<p> To create a disk containing data, you may be better to use <i><a href="/docs/linux/man/1-virt-make-fs/">virt-make-fs</a></i>(1). If you are creating a blank disk to use in <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1), you should instead use the guestfish <i>-N</i> option. </p>
<p> Normal usage would be something like this: </p>
<pre>
 virt-format -a disk.qcow
</pre>
<p> or this: </p>
<pre>
 virt-format -a /dev/VG/LV
</pre>
<p> <i>disk.qcow</i> or <i>/dev/VG/LV</i> must exist already. <code>Any data on these disks will be erased by these commands</code>. These commands will create a single empty partition covering the whole disk, with no filesystem inside it. </p>
<p> Additional parameters can be used to control the creation of partitions, filesystems, etc. The most commonly used options are:</p>
<dl>
<dt><i>&#8211;filesystem=[ext3|ntfs|vfat|&#8230;]</i></dt>
<dd> Create an empty filesystem (<tt>&quot;ext3&quot;</tt>, <tt>&quot;ntfs&quot;</tt> etc) inside the partition.</dd>
<dt><i>&#8211;lvm[=/dev/VG/LV]</i></dt>
<dd> Create a Linux <font SIZE="-1">LVM2</font> logical volume on the disk. When used with <i>&#8211;filesystem</i>, the filesystem is created inside the <font SIZE="-1">LV.</font></dd></dl>
<p> For more information about these and other options, see &#8220;<font SIZE="-1">OPTIONS&#8221;</font> below. </p>
<p> The format of the disk is normally auto-detected, but you can also force it by using the <i>&#8211;format</i> option (q.v.). In situations where you do not trust the existing content of the disk, then it is advisable to use this option to avoid possible exploits.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></dt>
<dd> Display brief help.</dd>
<dt><code>-a</code> file</dt>
<dd>
</dd><dt><code>&#8211;add</code> file</dt>
<dd> Add <i>file</i>, a disk image, host partition, <font SIZE="-1">LV,</font> external <font SIZE="-1">USB</font> disk, etc. </dd>
<p> The format of the disk image is auto-detected. To override this and force a particular format use the <i>&#8211;format=..</i> option. </p>
<p> <code>Any existing data on the disk is erased.</code></p>
<dt><code>-a </code><font SIZE="-1"><code>URI</code></font></dt>
<dd>
</dd><dt><code>&#8211;add </code><font SIZE="-1"><code>URI</code></font></dt>
<dd> Add a remote disk. See &#8220;<font SIZE="-1">ADDING REMOTE STORAGE&#8221;</font> in <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1).</dd>
<dt><code>&#8211;filesystem=ext3|ntfs|vfat|&#8230;</code></dt>
<dd> Create an empty filesystem of the specified type. Many filesystem types are supported by libguestfs.</dd>
<dt><code>&#8211;filesystem=none</code></dt>
<dd> Create no filesystem. This is the default.</dd>
<dt><code>&#8211;format=raw|qcow2|..</code></dt>
<dd>
</dd><dt><code>&#8211;format</code></dt>
<dd> The default for the <i>-a</i> option is to auto-detect the format of the disk image. Using this forces the disk format for <i>-a</i> options which follow on the command line. Using <i>&#8211;format</i> with no argument switches back to auto-detection for subsequent <i>-a</i> options. </dd>
<p> For example: </p>
<pre>
 virt-format --format=raw -a disk.img
</pre>
<p> forces raw format (no auto-detection) for <i>disk.img</i>. </p>
<pre>
 virt-format --format=raw -a disk.img --format -a another.img
</pre>
<p> forces raw format (no auto-detection) for <i>disk.img</i> and reverts to auto-detection for <i>another.img</i>. </p>
<p> If you have untrusted raw-format guest disk images, you should use this option to specify the disk format. This avoids a possible security problem with malicious guests (<font SIZE="-1">CVE-2010-3851</font>).</p>
<dt><code>&#8211;label=LABEL</code></dt>
<dd> Set the filesystem label.</dd>
<dt><code>&#8211;lvm=/dev/</code><font SIZE="-1">VG</font><code>/</code><font SIZE="-1">LV</font></dt>
<dd> Create a Linux <font SIZE="-1">LVM2</font> logical volume called <i>/dev/</i><font SIZE="-1"><i>VG</i></font><i>/</i><font SIZE="-1"><i>LV</i></font><i></i>. You can change the name of the volume group and logical volume.</dd>
<dt><code>&#8211;lvm</code></dt>
<dd> Create a Linux <font SIZE="-1">LVM2</font> logical volume with the default name (<i>/dev/VG/LV</i>).</dd>
<dt><code>&#8211;lvm=none</code></dt>
<dd> Create no logical volume. This is the default.</dd>
<dt><code>&#8211;partition</code></dt>
<dd> Create either an <font SIZE="-1">MBR</font> or <font SIZE="-1">GPT</font> partition covering the whole disk. <font SIZE="-1">MBR</font> is chosen if the disk size is &lt; 2 <font SIZE="-1">TB, GPT</font> if ≥ 2 <font SIZE="-1">TB.</font> </dd>
<p> This is the default.</p>
<dt><code>&#8211;partition=gpt</code></dt>
<dd> Create a <font SIZE="-1">GPT</font> partition.</dd>
<dt><code>&#8211;partition=mbr</code></dt>
<dd> Create an <font SIZE="-1">MBR</font> partition.</dd>
<dt><code>&#8211;partition=none</code></dt>
<dd> Create no partition table. Note that Windows may not be able to see these disks.</dd>
<dt><code>-v</code></dt>
<dd>
</dd><dt><code>&#8211;verbose</code></dt>
<dd> Enable verbose messages for debugging.</dd>
<dt><code>-V</code></dt>
<dd>
</dd><dt><code>&#8211;version</code></dt>
<dd> Display version number and exit.</dd>
<dt><code>&#8211;wipe</code></dt>
<dd> Normally virt-format does not wipe data from the disk (because that takes a long time). Thus if there is data on the disk, it is only hidden and partially overwritten by virt-format, and it might be recovered by disk editing tools. </dd>
<p> If you use this option, virt-format writes zeroes over the whole disk so that previous data is not recoverable.</p>
<dt><code>-x</code></dt>
<dd> Enable tracing of libguestfs <font SIZE="-1">API</font> calls.</dd></dl>
<h2>EXIT STATUS</h2>
<p> This program returns <tt>0</tt> on success, or <tt>1</tt> on failure.</p>
<h2>SEE ALSO</h2>
<p> <i>guestfs</i>(3), <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1), <i><a href="/docs/linux/man/1-virt-filesystems/">virt-filesystems</a></i>(1), <i><a href="/docs/linux/man/1-virt-make-fs/">virt-make-fs</a></i>(1), <i><a href="/docs/linux/man/1-virt-rescue/">virt-rescue</a></i>(1), <i><a href="/docs/linux/man/1-virt-resize/">virt-resize</a></i>(1), <a rel="nofollow" href="http://libguestfs.org/.">http://libguestfs.org/.</a></p>
<h2>AUTHOR</h2>
<p> Richard W.M. Jones <a rel="nofollow" href="http://people.redhat.com/~rjones/">http://people.redhat.com/~rjones/</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2012 Red Hat Inc.</p>
<h2>LICENSE</h2>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE. </font> See the <font SIZE="-1">GNU</font> General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, <font SIZE="-1">MA 02110-1301 USA.</font></p>
<h2>BUGS</h2>
<p> To get a list of bugs against libguestfs, use this link: <a rel="nofollow" href="https://bugzilla.redhat.com/buglist.cgi?component=libguestfs">https://bugzilla.redhat.com/buglist.cgi?component=libguestfs</a>&amp;product=Virtualization+Tools </p>
<p> To report a new bug against libguestfs, use this link: <a rel="nofollow" href="https://bugzilla.redhat.com/enter_bug.cgi?component=libguestfs">https://bugzilla.redhat.com/enter_bug.cgi?component=libguestfs</a>&amp;product=Virtualization+Tools </p>
<p> When reporting a bug, please supply:</p>
<dl>
<dt>&bull;</dt>
<dd> The version of libguestfs.</dd>
<dt>&bull;</dt>
<dd> Where you got libguestfs (eg. which Linux distro, compiled from source, etc)</dd>
<dt>&bull;</dt>
<dd> Describe the bug accurately and give a way to reproduce it.</dd>
<dt>&bull;</dt>
<dd> Run <i><a href="/docs/linux/man/1-libguestfs-test-tool/">libguestfs-test-tool</a></i>(1) and paste the <code>complete, unedited</code> output into the bug report. </dd>
</dl>
