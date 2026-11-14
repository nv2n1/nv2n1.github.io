---
title: "virt-filesystems(1)"
name: "virt-filesystems"
section: "1"
letter: "v"
url: "/docs/linux/man/1-virt-filesystems/"
description: "virt-filesystems – List filesystems, partitions, block devices, LVM in a virtual machine or disk image"
---

<h2 class="name">NAME</h2>
<p> virt-filesystems &#8211; List filesystems, partitions, block devices, LVM in a virtual machine or disk image </p>
<h2>SYNOPSIS</h2>
<pre><code>
virt - filesystems[--options] - d domname virt - filesystems[--options] - a disk.img[-a disk.img...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> This tool allows you to discover filesystems, partitions, logical volumes, and their sizes in a disk image or virtual machine. It is a replacement for <i><a href="/docs/linux/man/1-virt-list-filesystems/">virt-list-filesystems</a></i>(1) and <i><a href="/docs/linux/man/1-virt-list-partitions/">virt-list-partitions</a></i>(1). </p>
<p> One use for this tool is from shell scripts to iterate over all filesystems from a disk image: </p>
<pre>
 for fs in $(virt-filesystems -a disk.img); do
   # ...
 done
</pre>
<p> Another use is to list partitions before using another tool to modify those partitions (such as <i><a href="/docs/linux/man/1-virt-resize/">virt-resize</a></i>(1)). If you are curious about what an unknown disk image contains, use this tool along with <i><a href="/docs/linux/man/1-virt-inspector/">virt-inspector</a></i>(1). </p>
<p> Various command line options control what this program displays. You need to give either <i>-a</i> or <i>-d</i> options to specify the disk image or libvirt guest respectively. If you just specify that then the program shows filesystems found, one per line, like this: </p>
<pre>
 $ virt-filesystems -a disk.img
 /dev/sda1
 /dev/vg_guest/lv_root
</pre>
<p> If you add <i>-l</i> or <i>&#8211;long</i> then the output includes extra information: </p>
<pre>
 $ virt-filesystems -a disk.img -l
 Name                   Type         VFS   Label  Size
 /dev/sda1              filesystem   ext4  boot   524288000
 /dev/vg_guest/lv_root  filesystem   ext4  root   10212081664
</pre>
<p> If you add <i>&#8211;extra</i> then non-mountable (swap, unknown) filesystems are shown as well: </p>
<pre>
 $ virt-filesystems -a disk.img --extra
 /dev/sda1
 /dev/vg_guest/lv_root
 /dev/vg_guest/lv_swap
 /dev/vg_guest/lv_data
</pre>
<p> If you add <i>&#8211;partitions</i> then partitions are shown instead of filesystems: </p>
<pre>
 $ virt-filesystems -a disk.img --partitions
 /dev/sda1
 /dev/sda2
</pre>
<p> Similarly you can use <i>&#8211;logical-volumes</i>, <i>&#8211;volume-groups</i>, <i>&#8211;physical-volumes</i>, <i>&#8211;block-devices</i> to list those items. </p>
<p> You can use these options in combination as well (if you want a combination including filesystems, you have to add <i>&#8211;filesystems</i>). Notice that some items fall into several categories (eg. <i>/dev/sda1</i> might be both a partition and a filesystem). These items are listed several times. To get a list which includes absolutely everything that virt-filesystems knows about, use the <i>&#8211;all</i> option. </p>
<p> UUIDs (because they are quite long) are not shown by default. Add the <i>&#8211;uuid</i> option to display device and filesystem UUIDs in the long output. </p>
<p> <i>&#8211;all &#8211;long &#8211;uuid</i> is a useful combination to display all possible information about everything. </p>
<pre><code>
$ virt - filesystems - a win.img-- all-- long --uuid - h Name Type VFS Label Size Parent UUID / dev / sda1 filesystem ntfs System Reserved 100M - F81C92571C92112C / dev / sda2 filesystem ntfs - 20G - F2E8996AE8992E3B / dev / sda1 partition - -100M / dev / sda -
    / dev / sda2 partition - -20G / dev / sda -
    / dev / sda device - -20G - -
</code></pre>
<p> For machine-readable output, use <i>&#8211;csv</i> to get Comma-Separated Values.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Display brief help.</p>
<dt><code>-a</code> file</p>
<dd>
<dt><code>&#8211;add</code> file</p>
<dd> Add <i>file</i> which should be a disk image from a virtual machine. If the virtual machine has multiple block devices, you must supply all of them with separate <i>-a</i> options. </p>
<p> The format of the disk image is auto-detected. To override this and force a particular format use the <i>&#8211;format=..</i> option.</p>
<dt><code>-a </code><font SIZE="-1"><code>URI</code></font></p>
<dd>
<dt><code>&#8211;add </code><font SIZE="-1"><code>URI</code></font></p>
<dd> Add a remote disk. See &#8220;<font SIZE="-1">ADDING REMOTE STORAGE&#8221;</font> in <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1).</p>
<dt><code>&#8211;all</code></p>
<dd> Display everything. This is currently the same as specifying these options: <i>&#8211;filesystems</i>, <i>&#8211;extra</i>, <i>&#8211;partitions</i>, <i>&#8211;block-devices</i>, <i>&#8211;logical-volumes</i>, <i>&#8211;volume-groups</i>, <i>&#8211;physical-volumes</i>. (More may be added to this list in future). </p>
<p> See also <i>&#8211;long</i>.</p>
<dt><code>&#8211;blkdevs</code></p>
<dd>
<dt><code>&#8211;block-devices</code></p>
<dd> Display block devices.</p>
<dt><code>-c</code> <font SIZE="-1">URI</font></p>
<dd>
<dt><code>&#8211;connect</code> <font SIZE="-1">URI</font></p>
<dd> If using libvirt, connect to the given <i></i><font SIZE="-1"><i>URI</i></font><i></i>. If omitted, then we connect to the default libvirt hypervisor. </p>
<p> If you specify guest block devices directly (<i>-a</i>), then libvirt is not used at all.</p>
<dt><code>&#8211;csv</code></p>
<dd> Write out the results in <font SIZE="-1">CSV</font> format (comma-separated values). This format can be imported easily into databases and spreadsheets, but read &#8220;<font SIZE="-1">NOTE ABOUT CSV FORMAT&#8221;</font> below.</p>
<dt><code>-d</code> guest</p>
<dd>
<dt><code>&#8211;domain</code> guest</p>
<dd> Add all the disks from the named libvirt guest. Domain UUIDs can be used instead of names.</p>
<dt><code>&#8211;echo-keys</code></p>
<dd> When prompting for keys and passphrases, virt-filesystems normally turns echoing off so you cannot see what you are typing. If you are not worried about Tempest attacks and there is no one else in the room you can specify this flag to see what you are typing.</p>
<dt><code>&#8211;extra</code></p>
<dd> This causes filesystems that are not ordinary, mountable filesystems to be displayed. This category includes swapspace, and filesystems that are empty or contain unknown data. </p>
<p> This option implies <i>&#8211;filesystems</i>.</p>
<dt><code>&#8211;filesystems</code></p>
<dd> Display mountable filesystems. If no display option was selected then this option is implied. </p>
<p> With <i>&#8211;extra</i>, non-mountable filesystems are shown too.</p>
<dt><code>&#8211;format=raw|qcow2|..</code></p>
<dd>
<dt><code>&#8211;format</code></p>
<dd> The default for the <i>-a</i> option is to auto-detect the format of the disk image. Using this forces the disk format for <i>-a</i> options which follow on the command line. Using <i>&#8211;format</i> with no argument switches back to auto-detection for subsequent <i>-a</i> options. </p>
<p> For example: </p>
<pre>
 virt-filesystems --format=raw -a disk.img
</pre>
<p> forces raw format (no auto-detection) for <i>disk.img</i>. </p>
<pre>
 virt-filesystems --format=raw -a disk.img --format -a another.img
</pre>
<p> forces raw format (no auto-detection) for <i>disk.img</i> and reverts to auto-detection for <i>another.img</i>. </p>
<p> If you have untrusted raw-format guest disk images, you should use this option to specify the disk format. This avoids a possible security problem with malicious guests (<font SIZE="-1">CVE-2010-3851</font>).</p>
<dt><code>-h</code></p>
<dd>
<dt><code>&#8211;human-readable</code></p>
<dd> In <i>&#8211;long</i> mode, display sizes in human-readable format.</p>
<dt><code>&#8211;keys-from-stdin</code></p>
<dd> Read key or passphrase parameters from stdin. The default is to try to read passphrases from the user by opening <i>/dev/tty</i>.</p>
<dt><code>-l</code></p>
<dd>
<dt><code>&#8211;long</code></p>
<dd> Display extra columns of data (&#8220;long format&#8221;). </p>
<p> A title row is added unless you also specify <i>&#8211;no-title</i>. </p>
<p> The extra columns displayed depend on what output you select, and the ordering of columns may change in future versions. Use the title row, <i>&#8211;csv</i> output and/or <i><a href="/docs/linux/man/1-csvtool/">csvtool</a></i>(1) to match columns to data in external programs. </p>
<p> Use <i>-h</i> if you want sizes to be displayed in human-readable format. The default is to show raw numbers of <i>bytes</i>. </p>
<p> Use <i>&#8211;uuid</i> to display UUIDs too.</p>
<dt><code>&#8211;lvs</code></p>
<dd>
<dt><code>&#8211;logvols</code></p>
<dd>
<dt><code>&#8211;logical-volumes</code></p>
<dd> Display <font SIZE="-1">LVM</font> logical volumes. In this mode, these are displayed irrespective of whether the LVs contain filesystems.</p>
<dt><code>&#8211;no-title</code></p>
<dd> In <i>&#8211;long</i> mode, don&#8217;t add a title row. </p>
<p> Note that the order of the columns is not fixed, and may change in future versions of virt-filesystems, so using this option may give you unexpected surprises.</p>
<dt><code>&#8211;parts</code></p>
<dd>
<dt><code>&#8211;partitions</code></p>
<dd> Display partitions. In this mode, these are displayed irrespective of whether the partitions contain filesystems.</p>
<dt><code>&#8211;pvs</code></p>
<dd>
<dt><code>&#8211;physvols</code></p>
<dd>
<dt><code>&#8211;physical-volumes</code></p>
<dd> Display <font SIZE="-1">LVM</font> physical volumes.</p>
<dt><code>&#8211;uuid</code></p>
<dd>
<dt><code>&#8211;uuids</code></p>
<dd> In <i>&#8211;long</i> mode, display UUIDs as well.</p>
<dt><code>-v</code></p>
<dd>
<dt><code>&#8211;verbose</code></p>
<dd> Enable verbose messages for debugging.</p>
<dt><code>-V</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd> Display version number and exit.</p>
<dt><code>&#8211;vgs</code></p>
<dd>
<dt><code>&#8211;volgroups</code></p>
<dd>
<dt><code>&#8211;volume-groups</code></p>
<dd> Display <font SIZE="-1">LVM</font> volume groups.</p>
<dt><code>-x</code></p>
<dd> Enable tracing of libguestfs <font SIZE="-1">API</font> calls.</dl>
<h2>COLUMNS</h2>
<p> Note that columns in the output are subject to reordering and change in future versions of this tool.</p>
<dl>
<dt><code>Name</code></p>
<dd> The filesystem, partition, block device or <font SIZE="-1">LVM</font> name. </p>
<p> For device and partition names these are displayed as canonical libguestfs names, so that for example <i>/dev/sda2</i> is the second partition on the first device. </p>
<p> If the <i>&#8211;long</i> option is <code>not</code> specified, then only the name column is shown in the output.</p>
<dt><code>Type</code></p>
<dd> The object type, for example <tt>&quot;filesystem&quot;</tt>, <tt>&quot;lv&quot;</tt>, <tt>&quot;device&quot;</tt> etc.</p>
<dt><font SIZE="-1"><code>VFS</code></font></p>
<dd> If there is a filesystem, then this column displays the filesystem type if one could be detected, eg. <tt>&quot;ext4&quot;</tt>.</p>
<dt><code>Label</code></p>
<dd> If the object has a label (used for identifying and mounting filesystems) then this column contains the label.</p>
<dt><font SIZE="-1"><code>MBR</code></font></p>
<dd> The partition type byte, displayed as a two digit hexadecimal number. A comprehensive list of partition types can be found here: <a rel="nofollow" href="http://www.win.tue.nl/~aeb/partitions/partition_types-1.html">http://www.win.tue.nl/~aeb/partitions/partition_types-1.html</a> </p>
<p> This is only applicable for <font SIZE="-1">DOS </font>(<font SIZE="-1">MBR</font>) partitions.</p>
<dt><code>Size</code></p>
<dd> The size of the object in bytes. If the <i>&#8211;human</i> option is used then the size is displayed in a human-readable form.</p>
<dt><code>Parent</code></p>
<dd> The parent column records the parent relationship between objects. </p>
<p> For example, if the object is a partition, then this column contains the name of the containing device. If the object is a logical volume, then this column is the name of the volume group. </p>
<p> If there is more than one parent, then this column is (internal to the column) a comma-separated list, eg. <tt>&quot;/dev/sda,/dev/sdb&quot;</tt>.</p>
<dt><font SIZE="-1"><code>UUID</code></font></p>
<dd> If the object has a <font SIZE="-1">UUID </font>(used for identifying and mounting filesystems and block devices) then this column contains the <font SIZE="-1">UUID</font> as a string. </p>
<p> The <font SIZE="-1">UUID</font> is only displayed if the <i>&#8211;uuid</i> option is given.</dl>
<h2>NOTE ABOUT CSV FORMAT</h2>
<p> Comma-separated values (<font SIZE="-1">CSV</font>) is a deceptive format. It <i>seems</i> like it should be easy to parse, but it is definitely not easy to parse. </p>
<p> Myth: Just split fields at commas. Reality: This does <i>not</i> work reliably. This example has two columns: </p>
<pre>
 &quot;foo,bar&quot;,baz
</pre>
<p> Myth: Read the file one line at a time. Reality: This does <i>not</i> work reliably. This example has one row: </p>
<pre>
 &quot;foo
 bar&quot;,baz
</pre>
<p> For shell scripts, use <tt>&quot;csvtool&quot;</tt> (<a rel="nofollow" href="https://github.com/Chris00/ocaml-csv">https://github.com/Chris00/ocaml-csv</a> also packaged in major Linux distributions). </p>
<p> For other languages, use a <font SIZE="-1">CSV</font> processing library (eg. <tt>&quot;Text::CSV&quot;</tt> for Perl or Python&#8217;s built-in csv library). </p>
<p> Most spreadsheets and databases can import <font SIZE="-1">CSV</font> directly.</p>
<h2>EXIT STATUS</h2>
<p> This program returns 0 if successful, or non-zero if there was an error.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3), <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1), <i><a href="/docs/linux/man/1-virt-cat/">virt-cat</a></i>(1), <i><a href="/docs/linux/man/1-virt-df/">virt-df</a></i>(1), <i><a href="/docs/linux/man/1-virt-list-filesystems/">virt-list-filesystems</a></i>(1), <i><a href="/docs/linux/man/1-virt-list-partitions/">virt-list-partitions</a></i>(1), <i><a href="/docs/linux/man/1-csvtool/">csvtool</a></i>(1), <a rel="nofollow" href="http://libguestfs.org/.">http://libguestfs.org/.</a></p>
<h2>AUTHOR</h2>
<p> Richard W.M. Jones <a rel="nofollow" href="http://people.redhat.com/~rjones/">http://people.redhat.com/~rjones/</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2010-2012 Red Hat Inc.</p>
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
