---
title: "virt-cat(1)"
name: "virt-cat"
section: "1"
letter: "v"
url: "/docs/linux/man/1-virt-cat/"
description: "virt-cat – Display files in a virtual machine"
---

<h2 class="name">NAME</h2>
<p> virt-cat &#8211; Display files in a virtual machine </p>
<h2>SYNOPSIS</h2>
<pre><code>
virt - cat[--options] - d domname file[file...] virt - cat[--options] - a disk.img[-a disk.img...] file[file...]
</code></pre>
<p> Old-style: </p>
<pre>
 virt-cat domname file
 virt-cat disk.img file
</pre>
<h2>DESCRIPTION</h2>
<p> <tt>&quot;virt-cat&quot;</tt> is a command line tool to display the contents of <tt>&quot;file&quot;</tt> where <tt>&quot;file&quot;</tt> exists in the named virtual machine (or disk image). </p>
<p> Multiple filenames can be given, in which case they are concatenated together. Each filename must be a full path, starting at the root directory (starting with &#8216;/&#8217;). </p>
<p> <tt>&quot;virt-cat&quot;</tt> can be used to quickly view a file. To edit a file, use <tt>&quot;virt-edit&quot;</tt>. For more complex cases you should look at the <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1) tool (see &#8220;<font SIZE="-1">USING GUESTFISH&#8221;</font> below).</p>
<h2>EXAMPLES</h2>
<p> Display <i>/etc/fstab</i> file from inside the libvirt <font SIZE="-1">VM</font> called <tt>&quot;mydomain&quot;</tt>: </p>
<pre>
 virt-cat -d mydomain /etc/fstab
</pre>
<p> Find out what packages were recently installed: </p>
<pre>
 virt-cat -d mydomain /var/log/yum.log | tail
</pre>
<p> Find out who is logged on inside a virtual machine: </p>
<pre>
 virt-cat -d mydomain /var/run/utmp &gt; /tmp/utmp
 who /tmp/utmp
</pre>
<p> or who was logged on: </p>
<pre>
 virt-cat -d mydomain /var/log/wtmp &gt; /tmp/wtmp
 last -f /tmp/wtmp
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
<dt><code>-d</code> guest</p>
<dd>
<dt><code>&#8211;domain</code> guest</p>
<dd> Add all the disks from the named libvirt guest. Domain UUIDs can be used instead of names.</p>
<dt><code>&#8211;echo-keys</code></p>
<dd> When prompting for keys and passphrases, virt-cat normally turns echoing off so you cannot see what you are typing. If you are not worried about Tempest attacks and there is no one else in the room you can specify this flag to see what you are typing.</p>
<dt><code>&#8211;format=raw|qcow2|..</code></p>
<dd>
<dt><code>&#8211;format</code></p>
<dd> The default for the <i>-a</i> option is to auto-detect the format of the disk image. Using this forces the disk format for <i>-a</i> options which follow on the command line. Using <i>&#8211;format</i> with no argument switches back to auto-detection for subsequent <i>-a</i> options. </p>
<p> For example: </p>
<pre>
 virt-cat --format=raw -a disk.img file
</pre>
<p> forces raw format (no auto-detection) for <i>disk.img</i>. </p>
<pre>
 virt-cat --format=raw -a disk.img --format -a another.img file
</pre>
<p> forces raw format (no auto-detection) for <i>disk.img</i> and reverts to auto-detection for <i>another.img</i>. </p>
<p> If you have untrusted raw-format guest disk images, you should use this option to specify the disk format. This avoids a possible security problem with malicious guests (<font SIZE="-1">CVE-2010-3851</font>).</p>
<dt><code>&#8211;keys-from-stdin</code></p>
<dd> Read key or passphrase parameters from stdin. The default is to try to read passphrases from the user by opening <i>/dev/tty</i>.</p>
<dt><code>-m dev[:mountpoint[:options[:fstype]]]</code></p>
<dd>
<dt><code>&#8211;mount dev[:mountpoint[:options[:fstype]]]</code></p>
<dd> Mount the named partition or logical volume on the given mountpoint. </p>
<p> If the mountpoint is omitted, it defaults to <i>/</i>. </p>
<p> Specifying any mountpoint disables the inspection of the guest and the mount of its root and all of its mountpoints, so make sure to mount all the mountpoints needed to work with the filenames given as arguments. </p>
<p> If you don&#8217;t know what filesystems a disk image contains, you can either run guestfish without this option, then list the partitions, filesystems and LVs available (see &#8220;list-partitions&#8221;, &#8220;list-filesystems&#8221; and &#8220;lvs&#8221; commands), or you can use the <i><a href="/docs/linux/man/1-virt-filesystems/">virt-filesystems</a></i>(1) program. </p>
<p> The third (and rarely used) part of the mount parameter is the list of mount options used to mount the underlying filesystem. If this is not given, then the mount options are either the empty string or <tt>&quot;ro&quot;</tt> (the latter if the <i>&#8211;ro</i> flag is used). By specifying the mount options, you override this default choice. Probably the only time you would use this is to enable ACLs and/or extended attributes if the filesystem can support them: </p>
<pre>
 -m /dev/sda1:/:acl,user_xattr
</pre>
<p> Using this flag is equivalent to using the <tt>&quot;mount-options&quot;</tt> command. </p>
<p> The fourth part of the parameter is the filesystem driver to use, such as <tt>&quot;ext3&quot;</tt> or <tt>&quot;ntfs&quot;</tt>. This is rarely needed, but can be useful if multiple drivers are valid for a filesystem (eg: <tt>&quot;ext2&quot;</tt> and <tt>&quot;ext3&quot;</tt>), or if libguestfs misidentifies a filesystem.</p>
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
<h2>OLD-STYLE COMMAND LINE ARGUMENTS</h2>
<p> Previous versions of virt-cat allowed you to write either: </p>
<pre>
 virt-cat disk.img [disk.img ...] file
</pre>
<p> or </p>
<pre>
 virt-cat guestname file
</pre>
<p> whereas in this version you should use <i>-a</i> or <i>-d</i> respectively to avoid the confusing case where a disk image might have the same name as a guest. </p>
<p> For compatibility the old style is still supported.</p>
<h2>LOG FILES</h2>
<p> To list out the log files from guests, see the related tool <i><a href="/docs/linux/man/1-virt-log/">virt-log</a></i>(1). It understands binary log formats such as the systemd journal.</p>
<h2>WINDOWS PATHS</h2>
<p> <tt>&quot;virt-cat&quot;</tt> has a limited ability to understand Windows drive letters and paths (eg. <i>E:ooar.txt</i>). </p>
<p> If and only if the guest is running Windows then:</p>
<dl>
<dt>&bull;</p>
<dd> Drive letter prefixes like <tt>&quot;C:&quot;</tt> are resolved against the Windows Registry to the correct filesystem.</p>
<dt>&bull;</p>
<dd> Any backslash (<tt>&quot;\&quot;</tt>) characters in the path are replaced with forward slashes so that libguestfs can process it.</p>
<dt>&bull;</p>
<dd> The path is resolved case insensitively to locate the file that should be displayed.</dl>
<p> There are some known shortcomings:</p>
<dl>
<dt>&bull;</p>
<dd> Some <font SIZE="-1">NTFS</font> symbolic links may not be followed correctly.</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">NTFS</font> junction points that cross filesystems are not followed.</dl>
<h2>USING GUESTFISH</h2>
<p> <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1) is a more powerful, lower level tool which you can use when <tt>&quot;virt-cat&quot;</tt> doesn&#8217;t work. </p>
<p> Using <tt>&quot;virt-cat&quot;</tt> is approximately equivalent to doing: </p>
<pre>
 guestfish --ro -i -d domname download file -
</pre>
<p> where <tt>&quot;domname&quot;</tt> is the name of the libvirt guest, and <tt>&quot;file&quot;</tt> is the full path to the file. Note the final <tt>&quot;-&quot;</tt> (meaning &#8220;output to stdout&#8221;). </p>
<p> The command above uses libguestfs&#8217;s guest inspection feature and so does not work on guests that libguestfs cannot inspect, or on things like arbitrary disk images that don&#8217;t contain guests. To display a file from a disk image directly, use: </p>
<pre>
 guestfish --ro -a disk.img -m /dev/sda1 download file -
</pre>
<p> where <i>disk.img</i> is the disk image, <i>/dev/sda1</i> is the filesystem within the disk image, and <tt>&quot;file&quot;</tt> is the full path to the file.</p>
<h2>EXIT STATUS</h2>
<p> This program returns 0 if successful, or non-zero if there was an error.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3), <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1), <i><a href="/docs/linux/man/1-virt-copy-out/">virt-copy-out</a></i>(1), <i><a href="/docs/linux/man/1-virt-edit/">virt-edit</a></i>(1), <i><a href="/docs/linux/man/1-virt-log/">virt-log</a></i>(1), <i><a href="/docs/linux/man/1-virt-tar-out/">virt-tar-out</a></i>(1), <a rel="nofollow" href="http://libguestfs.org/.">http://libguestfs.org/.</a></p>
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
