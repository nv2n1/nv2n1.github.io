---
title: "virt-diff(1)"
name: "virt-diff"
section: "1"
letter: "v"
url: "/docs/linux/man/1-virt-diff/"
description: "virt-diff – Differences between files in two virtual machines"
---

<h2 class="name">NAME</h2>
<p> virt-diff &#8211; Differences between files in two virtual machines </p>
<h2>SYNOPSIS</h2>
<pre><code>
virt - diff[--options] - d domain1 - D domain2 virt - diff[--options] - a disk1.img[-a...] - A disk2.img[-A...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> <tt>&quot;virt-diff&quot;</tt> lists the differences between files in two virtual machines or disk images. The usual use case is to show the changes in a <font SIZE="-1">VM</font> after it has been running for a while, by taking a snapshot, running the <font SIZE="-1">VM,</font> and then using this tool to show what changed between the new <font SIZE="-1">VM</font> state and the old snapshot. </p>
<p> This tool will find differences in filenames, file sizes, checksums, extended attributes, file content and more from a virtual machine or disk image. However it <code>does not</code> look at the boot loader, unused space between partitions or within filesystems, &#8220;hidden&#8221; sectors and so on. In other words, it is not a security or forensics tool. </p>
<p> To specify two guests, you have to use the <i>-a</i> or <i>-d</i> option(s) for the first guest, and the <i>-A</i> or <i>-D</i> option(s) for the second guest. The common case is: </p>
<pre>
 virt-diff -a old.img -A new.img
</pre>
<p> or using names known to libvirt: </p>
<pre>
 virt-diff -d oldguest -D newguest
</pre>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Display brief help.</p>
<dt><code>-a</code> file</p>
<dd>
<dt><code>&#8211;add</code> file</p>
<dd> Add <i>file</i> which should be a disk image from the first virtual machine. If the virtual machine has multiple block devices, you must supply all of them with separate <i>-a</i> options. </p>
<p> The format of the disk image is auto-detected. To override this and force a particular format use the <i>&#8211;format=..</i> option.</p>
<dt><code>-a</code> <font SIZE="-1">URI</font></p>
<dd>
<dt><code>&#8211;add</code> <font SIZE="-1">URI</font></p>
<dd> Add a remote disk. See &#8220;<font SIZE="-1">ADDING REMOTE STORAGE&#8221;</font> in <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1).</p>
<dt><code>&#8211;all</code></p>
<dd> Same as <i>&#8211;extra-stats</i> <i>&#8211;times</i> <i>&#8211;uids</i> <i>&#8211;xattrs</i>.</p>
<dt><code>&#8211;atime</code></p>
<dd> The default is to ignore changes in file access times, since those are unlikely to be interesting. Using this flag shows atime differences as well.</p>
<dt><code>-A</code> file</p>
<dd>
<dt><code>-A</code> <font SIZE="-1">URI</font></p>
<dd> Add a disk image from the second virtual machine.</p>
<dt><code>&#8211;checksum</code></p>
<dd>
<dt><code>&#8211;checksum=crc|md5|sha1|sha224|sha256|sha384|sha512</code></p>
<dd> Use a checksum over file contents to detect when regular files have changed content. </p>
<p> With no argument, this defaults to using <i>md5</i>. Using an argument, you can select the checksum type to use. If the flag is omitted then file times and size are used to determine if a file has changed.</p>
<dt><code>-c</code> <font SIZE="-1">URI</font></p>
<dd>
<dt><code>&#8211;connect</code> <font SIZE="-1">URI</font></p>
<dd> If using libvirt, connect to the given <i></i><font SIZE="-1"><i>URI</i></font><i></i>. If omitted, then we connect to the default libvirt hypervisor. </p>
<p> If you specify guest block devices directly (<i>-a</i>), then libvirt is not used at all.</p>
<dt><code>&#8211;csv</code></p>
<dd> Write out the results in <font SIZE="-1">CSV</font> format (comma-separated values). This format can be imported easily into databases and spreadsheets, but read &#8220;<font SIZE="-1">NOTE ABOUT CSV FORMAT&#8221;</font> below.</p>
<dt><code>&#8211;dir-links</code></p>
<dd> The default is to ignore changed in the number of links in directory entries, since those are unlikely to be interesting. Using this flag shows changes to the nlink field of directories.</p>
<dt><code>&#8211;dir-times</code></p>
<dd> The default is to ignore changed times on directory entries, since those are unlikely to be interesting. Using this flag shows changes to the time fields of directories.</p>
<dt><code>-d</code> guest</p>
<dd>
<dt><code>&#8211;domain</code> guest</p>
<dd> Add all the disks from the named libvirt guest, as the first guest. Domain UUIDs can be used instead of names.</p>
<dt><code>-D</code> guest</p>
<dd> Add all the disks from the named libvirt guest, as the second guest. Domain UUIDs can be used instead of names.</p>
<dt><code>&#8211;echo-keys</code></p>
<dd> When prompting for keys and passphrases, virt-diff normally turns echoing off so you cannot see what you are typing. If you are not worried about Tempest attacks and there is no one else in the room you can specify this flag to see what you are typing.</p>
<dt><code>&#8211;extra-stats</code></p>
<dd> Display extra stats.</p>
<dt><code>&#8211;format=raw|qcow2|..</code></p>
<dd>
<dt><code>&#8211;format</code></p>
<dd> The default for the <i>-a</i>/<i>-A</i> option is to auto-detect the format of the disk image. Using this forces the disk format for <i>-a</i>/<i>-A</i> options which follow on the command line. Using <i>&#8211;format</i> with no argument switches back to auto-detection for subsequent <i>-a</i>/<i>-A</i> options. </p>
<p> For example: </p>
<pre>
 virt-diff --format=raw -a disk.img [...]
</pre>
<p> forces raw format (no auto-detection) for <i>disk.img</i>. </p>
<pre><code>
virt - diff-- format = raw - a disk.img-- format - a another.img[...]
</code></pre>
<p> forces raw format (no auto-detection) for <i>disk.img</i> and reverts to auto-detection for <i>another.img</i>. </p>
<p> If you have untrusted raw-format guest disk images, you should use this option to specify the disk format. This avoids a possible security problem with malicious guests (<font SIZE="-1">CVE-2010-3851</font>).</p>
<dt><code>-h</code></p>
<dd>
<dt><code>&#8211;human-readable</code></p>
<dd> Display file sizes in human-readable format.</p>
<dt><code>&#8211;keys-from-stdin</code></p>
<dd> Read key or passphrase parameters from stdin. The default is to try to read passphrases from the user by opening <i>/dev/tty</i>.</p>
<dt><code>&#8211;times</code></p>
<dd> Display time fields.</p>
<dt><code>&#8211;time-days</code></p>
<dd> Display time fields as days before now (negative if in the future). </p>
<p> Note that <tt>0</tt> in output means &#8220;up to 1 day before now&#8221;, or that the age of the file is between 0 and 86399 seconds.</p>
<dt><code>&#8211;time-relative</code></p>
<dd> Display time fields as seconds before now (negative if in the future).</p>
<dt><code>&#8211;time-t</code></p>
<dd> Display time fields as seconds since the Unix epoch.</p>
<dt><code>&#8211;uids</code></p>
<dd> Display <font SIZE="-1">UID</font> and <font SIZE="-1">GID</font> fields.</p>
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
<dt><code>&#8211;xattrs</code></p>
<dd> Display extended attributes.</dl>
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
<p> <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3), <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1), <i><a href="/docs/linux/man/1-virt-cat/">virt-cat</a></i>(1), <i><a href="/docs/linux/man/1-virt-copy-out/">virt-copy-out</a></i>(1), <i><a href="/docs/linux/man/1-virt-ls/">virt-ls</a></i>(1), <i><a href="/docs/linux/man/1-virt-tar-out/">virt-tar-out</a></i>(1), <a rel="nofollow" href="http://libguestfs.org/.">http://libguestfs.org/.</a></p>
<h2>AUTHOR</h2>
<p> Richard W.M. Jones <a rel="nofollow" href="http://people.redhat.com/~rjones/">http://people.redhat.com/~rjones/</a></p>
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
