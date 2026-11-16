---
title: "virt-log(1)"
name: "virt-log"
section: "1"
letter: "v"
url: "/docs/linux/man/1-virt-log/"
description: "virt-log – Display log files from a virtual machine"
---

<h2 class="name">NAME</h2>
<p> virt-log &#8211; Display log files from a virtual machine </p>
<h2>SYNOPSIS</h2>
<pre><code>
virt - log[--options] - d domname virt - log[--options] - a disk.img[-a disk.img...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> <tt>&quot;virt-log&quot;</tt> is a command line tool to display the log files from the named virtual machine (or disk image). </p>
<p> This tool understands and displays both plain text log files (eg. <i>/var/log/messages</i>) and binary formats such as the systemd journal. </p>
<p> To display other types of files, use <i><a href="/docs/linux/man/1-virt-cat/">virt-cat</a></i>(1). To copy files out of a virtual machine, use <i><a href="/docs/linux/man/1-virt-copy-out/">virt-copy-out</a></i>(1). To display the contents of the Windows Registry, use <i><a href="/docs/linux/man/1-virt-win-reg/">virt-win-reg</a></i>(1).</p>
<h2>EXAMPLES</h2>
<p> Display the complete logs from a guest: </p>
<pre>
 virt-log -d mydomain | less
</pre>
<p> Find out what <font SIZE="-1">DHCP IP</font> address a <font SIZE="-1">VM</font> acquired: </p>
<pre>
 virt-log -d mydomain | grep 'dhclient.*bound to'
</pre>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></dt>
<dd> Display brief help.</dd>
<dt><code>-a</code> file</dt>
<dd>
</dd><dt><code>&#8211;add</code> file</dt>
<dd> Add <i>file</i> which should be a disk image from a virtual machine. If the virtual machine has multiple block devices, you must supply all of them with separate <i>-a</i> options. </dd>
<p> The format of the disk image is auto-detected. To override this and force a particular format use the <i>&#8211;format=..</i> option.</p>
<dt><code>-a </code><font SIZE="-1"><code>URI</code></font></dt>
<dd>
</dd><dt><code>&#8211;add </code><font SIZE="-1"><code>URI</code></font></dt>
<dd> Add a remote disk. See &#8220;<font SIZE="-1">ADDING REMOTE STORAGE&#8221;</font> in <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1).</dd>
<dt><code>-c</code> <font SIZE="-1">URI</font></dt>
<dd>
</dd><dt><code>&#8211;connect</code> <font SIZE="-1">URI</font></dt>
<dd> If using libvirt, connect to the given <i></i><font SIZE="-1"><i>URI</i></font><i></i>. If omitted, then we connect to the default libvirt hypervisor. </dd>
<p> If you specify guest block devices directly (<i>-a</i>), then libvirt is not used at all.</p>
<dt><code>-d</code> guest</dt>
<dd>
</dd><dt><code>&#8211;domain</code> guest</dt>
<dd> Add all the disks from the named libvirt guest. Domain UUIDs can be used instead of names.</dd>
<dt><code>&#8211;echo-keys</code></dt>
<dd> When prompting for keys and passphrases, virt-log normally turns echoing off so you cannot see what you are typing. If you are not worried about Tempest attacks and there is no one else in the room you can specify this flag to see what you are typing.</dd>
<dt><code>&#8211;format=raw|qcow2|..</code></dt>
<dd>
</dd><dt><code>&#8211;format</code></dt>
<dd> The default for the <i>-a</i> option is to auto-detect the format of the disk image. Using this forces the disk format for <i>-a</i> options which follow on the command line. Using <i>&#8211;format</i> with no argument switches back to auto-detection for subsequent <i>-a</i> options. </dd>
<p> For example: </p>
<pre>
 virt-log --format=raw -a disk.img
</pre>
<p> forces raw format (no auto-detection) for <i>disk.img</i>. </p>
<pre>
 virt-log --format=raw -a disk.img --format -a another.img
</pre>
<p> forces raw format (no auto-detection) for <i>disk.img</i> and reverts to auto-detection for <i>another.img</i>. </p>
<p> If you have untrusted raw-format guest disk images, you should use this option to specify the disk format. This avoids a possible security problem with malicious guests (<font SIZE="-1">CVE-2010-3851</font>).</p>
<dt><code>&#8211;keys-from-stdin</code></dt>
<dd> Read key or passphrase parameters from stdin. The default is to try to read passphrases from the user by opening <i>/dev/tty</i>.</dd>
<dt><code>-v</code></dt>
<dd>
</dd><dt><code>&#8211;verbose</code></dt>
<dd> Enable verbose messages for debugging.</dd>
<dt><code>-V</code></dt>
<dd>
</dd><dt><code>&#8211;version</code></dt>
<dd> Display version number and exit.</dd>
<dt><code>-x</code></dt>
<dd> Enable tracing of libguestfs <font SIZE="-1">API</font> calls.</dd></dl>
<h2>EXIT STATUS</h2>
<p> This program returns 0 if successful, or non-zero if there was an error.</p>
<h2>SEE ALSO</h2>
<p> <i>guestfs</i>(3), <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1), <i><a href="/docs/linux/man/1-virt-cat/">virt-cat</a></i>(1), <i><a href="/docs/linux/man/1-virt-copy-out/">virt-copy-out</a></i>(1), <i><a href="/docs/linux/man/1-virt-tar-out/">virt-tar-out</a></i>(1), <i><a href="/docs/linux/man/1-virt-win-reg/">virt-win-reg</a></i>(1), <a rel="nofollow" href="http://libguestfs.org/.">http://libguestfs.org/.</a></p>
<h2>AUTHOR</h2>
<p> Richard W.M. Jones <a rel="nofollow" href="http://people.redhat.com/~rjones/">http://people.redhat.com/~rjones/</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2010-2016 Red Hat Inc.</p>
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
<h2>Index</h2>
