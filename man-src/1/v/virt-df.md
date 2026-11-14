---
title: "virt-df(1)"
name: "virt-df"
section: "1"
letter: "v"
url: "/docs/linux/man/1-virt-df/"
description: "virt-df – Display free space on virtual filesystems"
---

<h2 class="name">NAME</h2>
<p> virt-df &#8211; Display free space on virtual filesystems </p>
<h2>SYNOPSIS</h2>
<p> All guests: </p>
<pre>
 virt-df [--options]
</pre>
<p> Single guest: </p>
<pre><code>
virt - df[--options] - d domname virt - df[--options] - a disk.img[-a disk.img...]
</code></pre>
<p> Old style: </p>
<p>virt &#8211; df[&#8211;options] domname virt &#8211; df[&#8211;options] disk.img[disk.img&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <tt>&quot;virt-df&quot;</tt> is a command line tool to display free space on virtual machine filesystems. Unlike other tools, it doesn&#8217;t just display the size of disk allocated to a virtual machine, but can look inside disk images to see how much space is really being used. </p>
<p> If used without any <i>-a</i> or <i>-d</i> arguments, <tt>&quot;virt-df&quot;</tt> checks with libvirt to get a list of all active and inactive guests, and performs a <tt>&quot;df&quot;</tt>-type operation on each one in turn, printing out the results. </p>
<p> If any <i>-a</i> or <i>-d</i> arguments are specified, <tt>&quot;virt-df&quot;</tt> performs a <tt>&quot;df&quot;</tt>-type operation on either the single named libvirt domain, or on the disk image(s) listed on the command line (which must all belong to a single <font SIZE="-1">VM</font>). <code>In this mode (with arguments), </code>&quot;virt-df&quot;<code> will only work for a single guest</code>. If you want to run on multiple guests, then you have to invoke <tt>&quot;virt-df&quot;</tt> multiple times. </p>
<p> Use the <i>&#8211;csv</i> option to get a format which can be easily parsed by other programs. Other options are similar to the standard <i><a href="/docs/linux/man/1-df/">df</a></i>(1) command.</p>
<h2>EXAMPLES</h2>
<p> Show disk usage for a single libvirt guest called <tt>&quot;F14x64&quot;</tt>. Make the output human-readable: </p>
<pre>
 # virt-df -d F14x64 -h
 Filesystem                       Size     Used  Available  Use%
 F14x64:/dev/sda1                 484M      66M       393M   14%
 F14x64:/dev/vg_f13x64/lv_root    7.4G     3.4G       4.0G   46%
</pre>
<p> Show disk usage for a disk image file called <i>test.img</i>: </p>
<pre>
 $ virt-df -a test1.img
 Filesystem                  1K-blocks     Used  Available  Use%
 test1.img:/dev/sda1             99099     1551      92432    2%
</pre>
<p> If a single guest has multiple disks, use the <i>-a</i> option repeatedly. A plus sign (<tt>&quot;+&quot;</tt>) is displayed for each additional disk. <code>Note: Do not do this with unrelated guest disks.</code> </p>
<pre>
 $ virt-df -a Win7x32TwoDisks-a -a Win7x32TwoDisks-b 
 Filesystem                   1K-blocks    Used  Available  Use%
 Win7x32TwoDisks-a+:/dev/sda1    102396   24712      77684   25%
 Win7x32TwoDisks-a+:/dev/sda2  12478460 7403416    5075044   60%
 Win7x32TwoDisks-a+:/dev/sdb1    521212   55728     465484   11%
</pre>
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
<dt><code>&#8211;format=raw|qcow2|..</code></p>
<dd>
<dt><code>&#8211;format</code></p>
<dd> The default for the <i>-a</i> option is to auto-detect the format of the disk image. Using this forces the disk format for <i>-a</i> options which follow on the command line. Using <i>&#8211;format</i> with no argument switches back to auto-detection for subsequent <i>-a</i> options. </p>
<p> For example: </p>
<pre>
 virt-df --format=raw -a disk.img
</pre>
<p> forces raw format (no auto-detection) for <i>disk.img</i>. </p>
<pre>
 virt-df --format=raw -a disk.img --format -a another.img
</pre>
<p> forces raw format (no auto-detection) for <i>disk.img</i> and reverts to auto-detection for <i>another.img</i>. </p>
<p> If you have untrusted raw-format guest disk images, you should use this option to specify the disk format. This avoids a possible security problem with malicious guests (<font SIZE="-1">CVE-2010-3851</font>).</p>
<dt><code>-h</code></p>
<dd>
<dt><code>&#8211;human-readable</code></p>
<dd> Print sizes in human-readable format. </p>
<p> You are not allowed to use <i>-h</i> and <i>&#8211;csv</i> at the same time.</p>
<dt><code>-i</code></p>
<dd>
<dt><code>&#8211;inodes</code></p>
<dd> Print inodes instead of blocks.</p>
<dt><code>&#8211;one-per-guest</code></p>
<dd> Since libguestfs 1.22, this is the default. This option does nothing and is left here for backwards compatibility with older scripts.</p>
<dt><code>-P</code> nr_threads</p>
<dd> Since libguestfs 1.22, virt-df is multithreaded and examines guests in parallel. By default the number of threads to use is chosen based on the amount of free memory available at the time that virt-df is started. You can force virt-df to use at most <tt>&quot;nr_threads&quot;</tt> by using the <i>-P</i> option. </p>
<p> Note that <i>-P 0</i> means to autodetect, and <i>-P 1</i> means to use a single thread.</p>
<dt><code>&#8211;uuid</code></p>
<dd> Print UUIDs instead of names. This is useful for following a guest even when the guest is migrated or renamed, or when two guests happen to have the same name. </p>
<p> Note that only domains that we fetch from libvirt come with UUIDs. For disk images, we still print the disk image name even when this option is specified.</p>
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
<h2>STATVFS NUMBERS</h2>
<p> <tt>&quot;virt-df&quot;</tt> (and <i><a href="/docs/linux/man/1-df/">df</a></i>(1)) get information by issuing a <i><a href="/docs/linux/man/3-statvfs/">statvfs</a></i>(3) system call. You can get the same information directly, either from the host (using libguestfs) or inside the guest:</p>
<dl>
<dt>From the host</p>
<dd> Run this command: </p>
<pre>
 guestfish --ro -d GuestName -i statvfs /
</pre>
<p> (change <i>/</i> to see stats for other filesystems).</p>
<dt>From inside the guest</p>
<dd> Run this command: </p>
<pre><code>
python - c 'import os; s = os.statvfs ("/"); print s'
</code></pre>
<p> (change <i>/</i> to see stats for other filesystems).</dl>
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
<p> <i><a href="/docs/linux/man/1-df/">df</a></i>(1), <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3), <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1), <i><a href="/docs/linux/man/1-virt-filesystems/">virt-filesystems</a></i>(1), <a rel="nofollow" href="http://libguestfs.org/.">http://libguestfs.org/.</a></p>
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
