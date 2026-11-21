---
title: "virt-ls(1)"
name: "virt-ls"
section: "1"
letter: "v"
url: "/docs/linux/man/1-virt-ls/"
description: "virt-ls – List files in a virtual machine"
---

<h2 class="name">NAME</h2>
<p> virt-ls &#8211; List files in a virtual machine </p>
<h2>SYNOPSIS</h2>
<pre><code>
virt - ls[--options] - d domname directory[directory...] virt - ls[--options] - a disk.img[-a disk.img...] directory[directory...]
</code></pre>
<p> Old style: </p>
<pre><code>
virt - ls[--options] domname directory virt - ls[--options] disk.img[disk.img...] directory
</code></pre>
<h2>DESCRIPTION</h2>
<p> <tt>&quot;virt-ls&quot;</tt> lists filenames, file sizes, checksums, extended attributes and more from a virtual machine or disk image. </p>
<p> Multiple directory names can be given, in which case the output from each is concatenated. </p>
<p> To list directories from a libvirt guest use the <i>-d</i> option to specify the name of the guest. For a disk image, use the <i>-a</i> option. </p>
<p> <tt>&quot;virt-ls&quot;</tt> can do many simple file listings. For more complicated cases you may need to use <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1), or write a program directly to the <i>guestfs</i>(3) <font SIZE="-1">API.</font></p>
<h2>EXAMPLES</h2>
<p> Get a list of all files and directories in a virtual machine: </p>
<pre>
 virt-ls -R -d guest /
</pre>
<p> List all setuid or setgid programs in a Linux virtual machine: </p>
<pre>
 virt-ls -lR -d guest / | grep '^- [42]'
</pre>
<p> List all public-writable directories in a Linux virtual machine: </p>
<pre>
 virt-ls -lR -d guest / | grep '^d ...7'
</pre>
<p> List all Unix domain sockets in a Linux virtual machine: </p>
<pre>
 virt-ls -lR -d guest / | grep '^s'
</pre>
<p> List all regular files with filenames ending in &#8216;.png&#8217;: </p>
<pre>
 virt-ls -lR -d guest / | grep -i '^-.*\.png$'
</pre>
<p> To display files larger than 10MB in home directories: </p>
<pre>
 virt-ls -lR -d guest /home | awk '$3 &gt; 10*1024*1024'
</pre>
<p> Find everything modified in the last 7 days: </p>
<pre>
 virt-ls -lR -d guest --time-days / | awk '$6 &lt;= 7'
</pre>
<p> Find regular files modified in the last 24 hours: </p>
<pre>
 virt-ls -lR -d guest --time-days / | grep '^-' | awk '$6 &lt; 1'
</pre>
<h3><font SIZE="-1">DIFFERENCES IN SNAPSHOTS AND BACKING FILES</font></h3>
<p> Although it is possible to use virt-ls to look for differences, since libguestfs ≥ 1.26 a new tool is available called <i><a href="/docs/linux/man/1-virt-diff/">virt-diff</a></i>(1).</p>
<h2>OUTPUT MODES</h2>
<p> <tt>&quot;virt-ls&quot;</tt> has four output modes, controlled by different combinations of the <i>-l</i> and <i>-R</i> options.</p>
<h3><font SIZE="-1">SIMPLE LISTING</font></h3>
<p> A simple listing is like the ordinary <i><a href="/docs/linux/man/1-ls/">ls</a></i>(1) command: </p>
<pre>
 $ virt-ls -d guest /
 bin
 boot
 [etc.]
</pre>
<h3><font SIZE="-1">LONG LISTING</font></h3>
<p> With the <i>-l</i> (<i>&#8211;long</i>) option, the output is like the <tt>&quot;ls -l&quot;</tt> command (more specifically, like the <tt>&quot;guestfs_ll&quot;</tt> function). </p>
<pre>
 $ virt-ls -l -d guest /
 total 204
 dr-xr-xr-x.   2 root root   4096 2009-08-25 19:06 bin
 dr-xr-xr-x.   5 root root   3072 2009-08-25 19:06 boot
 [etc.]
</pre>
<p> Note that while this is useful for displaying a directory, do not try parsing this output in another program. Use &#8220;<font SIZE="-1">RECURSIVE LONG LISTING&#8221;</font> instead.</p>
<h3><font SIZE="-1">RECURSIVE LISTING</font></h3>
<p> With the <i>-R</i> (<i>&#8211;recursive</i>) option, <tt>&quot;virt-ls&quot;</tt> lists the names of files and directories recursively: </p>
<pre>
 $ virt-ls -R -d guest /tmp
 foo
 foo/bar
 [etc.]
</pre>
<p> To generate this output, <tt>&quot;virt-ls&quot;</tt> runs the <tt>&quot;guestfs_find0&quot;</tt> function and converts <tt>&quot;</tt>\0&quot;</code> characters to <code>&quot;\n&quot;</code>.  </p>
<font SIZE="-1"></font><h3>RECURSIVE LONG LISTING</h3>
<p> Using <i>-lR</i> options together changes the output to display directories recursively, with file stats, and optionally other features such as checksums and extended attributes. </p>
<p> Most of the interesting features of <code>&quot;virt-ls&quot;</code> are only available when using <i>-lR</i> mode. </p>
<p> The fields are normally space-separated. Filenames are <code>not</code> quoted, so you cannot use the output in another program (because filenames can contain spaces and other unsafe characters). If the guest was untrusted and someone knew you were using <code>&quot;virt-ls&quot;</code> to analyze the guest, they could play tricks on you by creating filenames with embedded newline characters. To <code>safely</code> parse the output in another program, use the <i>--csv</i> (Comma-Separated Values) option. </p>
<p> Note that this output format is completely unrelated to the <code>&quot;ls -lR&quot;</code> command. </p>
<pre><code> $ virt-ls -lR -d guest /bin
 d 0555 4096 /bin
 - 0755 123 /bin/alsaunmute
 - 0755 28328 /bin/arch
 l 0777 4 /bin/awk -&gt; gawk
 - 0755 27216 /bin/basename
 - 0755 943360 /bin/bash
 [etc.]
</code></pre>
<p> These basic fields are always shown: </p>
<dl>
<dt>type</dt>
<dd> <p> The file type, one of: <code>&quot;-&quot;</code> (regular file), <code>&quot;d&quot;</code> (directory), <code>&quot;c&quot;</code> (character device), <code>&quot;b&quot;</code> (block device), <code>&quot;p&quot;</code> (named pipe), <code>&quot;l&quot;</code> (symbolic link), <code>&quot;s&quot;</code> (socket) or <code>&quot;u&quot;</code> (unknown). </p>
 </dd>
<dt>permissions</dt>
<dd> <p> The Unix permissions, displayed as a 4 digit octal number. </p>
 </dd>
<dt>size</dt>
<dd> <p> The size of the file. This is shown in bytes unless <i>-h</i> or <i>--human-readable</i> option is given, in which case this is shown as a human-readable number. </p>
 </dd>
<dt>path</dt>
<dd> <p> The full path of the file or directory. </p>
 </dd>
<dt>link</dt>
<dd> <p> For symbolic links only, the link target. </p>
 </dd></dl>
<p> In <i>-lR</i> mode, additional command line options enable the display of more fields. </p>
<p> With the <i>--uids</i> flag, these additional fields are displayed before the path: </p>
<dl>
<dt>uid</dt>
<dd>  </dd>
<dt>gid</dt>
<dd> <p> The <font SIZE="-1">UID</font> and <font SIZE="-1">GID</font> of the owner of the file (displayed numerically). Note these only make sense in the context of a Unix-like guest. </p>
 </dd></dl>
<p> With the <i>--times</i> flag, these additional fields are displayed: </p>
<dl>
<dt>atime</dt>
<dd> <p> The time of last access. </p>
 </dd>
<dt>mtime</dt>
<dd> <p> The time of last modification. </p>
 </dd>
<dt>ctime</dt>
<dd> <p> The time of last status change. </p>
 </dd></dl>
<p> The time fields are displayed as string dates and times, unless one of the <i>--time-t</i>, <i>--time-relative</i> or <i>--time-days</i> flags is given. </p>
<p> With the <i>--extra-stats</i> flag, these additional fields are displayed: </p>
<dl>
<dt>device</dt>
<dd> <p> The device containing the file (displayed as major:minor). This may not match devices as known to the guest. </p>
 </dd>
<dt>inode</dt>
<dd> <p> The inode number. </p>
 </dd>
<dt>nlink</dt>
<dd> <p> The number of hard links. </p>
 </dd>
<dt>rdev</dt>
<dd> <p> For block and char special files, the device (displayed as major:minor). </p>
 </dd>
<dt>blocks</dt>
<dd> <p> The number of 512 byte blocks allocated to the file. </p>
 </dd></dl>
<p> With the <i>--checksum</i> flag, the checksum of the file contents is shown (only for regular files). Computing file checksums can take a considerable amount of time.  </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>--help</code></dt>
<dd> <p> Display brief help. </p>
 </dd>
<dt><code>-a</code> file</dt>
<dd>  </dd>
<dt><code>--add</code> file</dt>
<dd> <p> Add <i>file</i> which should be a disk image from a virtual machine. If the virtual machine has multiple block devices, you must supply all of them with separate <i>-a</i> options. </p>
<p> The format of the disk image is auto-detected. To override this and force a particular format use the <i>--format=..</i> option. </p>
 </dd>
<dt><code>-a </code><font SIZE="-1"><code>URI</code></font></dt>
<dd>  </dd>
<dt><code>--add </code><font SIZE="-1"><code>URI</code></font></dt>
<dd> <p> Add a remote disk. See ``<font SIZE="-1">ADDING REMOTE STORAGE&#8217;&#8216;</font> in <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1). </p>
 </dd>
<dt><code>--checksum</code></dt>
<dd>  </dd>
<dt><code>--checksum=crc|md5|sha1|sha224|sha256|sha384|sha512</code></dt>
<dd> <p> Display checksum over file contents for regular files. With no argument, this defaults to using <i>md5</i>. Using an argument, you can select the checksum type to use. </p>
<p> This option only has effect in <i>-lR</i> output mode. See ``<font SIZE="-1">RECURSIVE LONG LISTING&#8217;&#8216;</font> above. </p>
 </dd>
<dt><code>-c</code><font SIZE="-1">URI</font></dt>
<dd>  </dd>
<dt><code>--connect</code><font SIZE="-1">URI</font></dt>
<dd> <p> If using libvirt, connect to the given <i></i><font SIZE="-1"><i>URI</i></font><i></i>. If omitted, then we connect to the default libvirt hypervisor. </p>
<p> If you specify guest block devices directly (<i>-a</i>), then libvirt is not used at all. </p>
 </dd>
<dt><code>--csv</code></dt>
<dd> <p> Write out the results in <font SIZE="-1">CSV</font> format (comma-separated values). This format can be imported easily into databases and spreadsheets, but read ``<font SIZE="-1">NOTE ABOUT CSV FORMAT&#8217;&#8216;</font> below. </p>
 </dd>
<dt><code>-d</code> guest</dt>
<dd>  </dd>
<dt><code>--domain</code> guest</dt>
<dd> <p> Add all the disks from the named libvirt guest. Domain UUIDs can be used instead of names. </p>
 </dd>
<dt><code>--echo-keys</code></dt>
<dd> <p> When prompting for keys and passphrases, virt-ls normally turns echoing off so you cannot see what you are typing. If you are not worried about Tempest attacks and there is no one else in the room you can specify this flag to see what you are typing. </p>
 </dd>
<dt><code>--extra-stats</code></dt>
<dd> <p> Display extra stats. </p>
<p> This option only has effect in <i>-lR</i> output mode. See ``<font SIZE="-1">RECURSIVE LONG LISTING&#8217;&#8216;</font> above. </p>
 </dd>
<dt><code>--format=raw|qcow2|..</code></dt>
<dd>  </dd>
<dt><code>--format</code></dt>
<dd> <p> The default for the <i>-a</i> option is to auto-detect the format of the disk image. Using this forces the disk format for <i>-a</i> options which follow on the command line. Using <i>--format</i> with no argument switches back to auto-detection for subsequent <i>-a</i> options. </p>
<p> For example: </p>
<pre><code> virt-ls --format=raw -a disk.img /dir
</code></pre>
<p> forces raw format (no auto-detection) for <i>disk.img</i>. </p>
<pre><code> virt-ls --format=raw -a disk.img --format -a another.img /dir
</code></pre>
<p> forces raw format (no auto-detection) for <i>disk.img</i> and reverts to auto-detection for <i>another.img</i>. </p>
<p> If you have untrusted raw-format guest disk images, you should use this option to specify the disk format. This avoids a possible security problem with malicious guests (<font SIZE="-1">CVE-2010-3851</font>). </p>
 </dd>
<dt><code>-h</code></dt>
<dd>  </dd>
<dt><code>--human-readable</code></dt>
<dd> <p> Display file sizes in human-readable format. </p>
<p> This option only has effect in <i>-lR</i> output mode. See ``<font SIZE="-1">RECURSIVE LONG LISTING&#8217;&#8216;</font> above. </p>
 </dd>
<dt><code>--keys-from-stdin</code></dt>
<dd> <p> Read key or passphrase parameters from stdin. The default is to try to read passphrases from the user by opening <i>/dev/tty</i>. </p>
 </dd>
<dt><code>-m dev[:mountpoint[:options[:fstype]]]</code></dt>
<dd>  </dd>
<dt><code>--mount dev[:mountpoint[:options[:fstype]]]</code></dt>
<dd> <p> Mount the named partition or logical volume on the given mountpoint. </p>
<p> If the mountpoint is omitted, it defaults to <i>/</i>. </p>
<p> Specifying any mountpoint disables the inspection of the guest and the mount of its root and all of its mountpoints, so make sure to mount all the mountpoints needed to work with the filenames given as arguments. </p>
<p> If you don&#8217;t know what filesystems a disk image contains, you can either run guestfish without this option, then list the partitions, filesystems and LVs available (see ``list-partitions&#8217;&#8216;, ``list-filesystems&#8217;&#8216; and ``lvs&#8217;&#8216; commands), or you can use the <i><a href="/docs/linux/man/1-virt-filesystems/">virt-filesystems</a></i>(1) program. </p>
<p> The third (and rarely used) part of the mount parameter is the list of mount options used to mount the underlying filesystem. If this is not given, then the mount options are either the empty string or <code>&quot;ro&quot;</code> (the latter if the <i>--ro</i> flag is used). By specifying the mount options, you override this default choice. Probably the only time you would use this is to enable ACLs and/or extended attributes if the filesystem can support them: </p>
<pre><code> -m /dev/sda1:/:acl,user_xattr
</code></pre>
<p> Using this flag is equivalent to using the <code>&quot;mount-options&quot;</code> command. </p>
<p> The fourth part of the parameter is the filesystem driver to use, such as <code>&quot;ext3&quot;</code> or <code>&quot;ntfs&quot;</code>. This is rarely needed, but can be useful if multiple drivers are valid for a filesystem (eg: <code>&quot;ext2&quot;</code> and <code>&quot;ext3&quot;</code>), or if libguestfs misidentifies a filesystem. </p>
 </dd>
<dt><code>-l</code></dt>
<dd>  </dd>
<dt><code>--long</code></dt>
<dd>  </dd>
<dt><code>-R</code></dt>
<dd>  </dd>
<dt><code>--recursive</code></dt>
<dd> <p> Select the mode. With neither of these options, <code>&quot;virt-ls&quot;</code> produces a simple, flat list of the files in the named directory. See ``<font SIZE="-1">SIMPLE LISTING&#8217;&#8216;</font>. </p>
<p> <code>&quot;virt-ls -l&quot;</code> produces a ``long listing&#8217;&#8216;, which shows more detail. See ``<font SIZE="-1">LONG LISTING&#8217;&#8216;</font>. </p>
<p> <code>&quot;virt-ls -R&quot;</code> produces a recursive list of files starting at the named directory. See ``<font SIZE="-1">RECURSIVE LISTING&#8217;&#8216;</font>. </p>
<p> <code>&quot;virt-ls -lR&quot;</code> produces a recursive long listing which can be more easily parsed. See ``<font SIZE="-1">RECURSIVE LONG LISTING&#8217;&#8216;</font>. </p>
 </dd>
<dt><code>--times</code></dt>
<dd> <p> Display time fields. </p>
<p> This option only has effect in <i>-lR</i> output mode. See ``<font SIZE="-1">RECURSIVE LONG LISTING&#8217;&#8216;</font> above. </p>
 </dd>
<dt><code>--time-days</code></dt>
<dd> <p> Display time fields as days before now (negative if in the future). </p>
<p> Note that <code>0</code> in output means ``up to 1 day before now&#8217;&#8216;, or that the age of the file is between 0 and 86399 seconds. </p>
<p> This option only has effect in <i>-lR</i> output mode. See ``<font SIZE="-1">RECURSIVE LONG LISTING&#8217;&#8216;</font> above. </p>
 </dd>
<dt><code>--time-relative</code></dt>
<dd> <p> Display time fields as seconds before now (negative if in the future). </p>
<p> This option only has effect in <i>-lR</i> output mode. See ``<font SIZE="-1">RECURSIVE LONG LISTING&#8217;&#8216;</font> above. </p>
 </dd>
<dt><code>--time-t</code></dt>
<dd> <p> Display time fields as seconds since the Unix epoch. </p>
<p> This option only has effect in <i>-lR</i> output mode. See ``<font SIZE="-1">RECURSIVE LONG LISTING&#8217;&#8216;</font> above. </p>
 </dd>
<dt><code>--uids</code></dt>
<dd> <p> Display <font SIZE="-1">UID</font> and <font SIZE="-1">GID</font> fields. </p>
<p> This option only has effect in <i>-lR</i> output mode. See ``<font SIZE="-1">RECURSIVE LONG LISTING&#8217;&#8216;</font> above. </p>
 </dd>
<dt><code>-v</code></dt>
<dd>  </dd>
<dt><code>--verbose</code></dt>
<dd> <p> Enable verbose messages for debugging. </p>
 </dd>
<dt><code>-V</code></dt>
<dd>  </dd>
<dt><code>--version</code></dt>
<dd> <p> Display version number and exit. </p>
 </dd>
<dt><code>-x</code></dt>
<dd> <p> Enable tracing of libguestfs <font SIZE="-1">API</font> calls. </p>
 </dd></dl>
<h2>OLD-STYLE COMMAND LINE ARGUMENTS</h2>
<p> Previous versions of virt-ls allowed you to write either: </p>
<pre><code> virt-ls disk.img [disk.img ...] /dir
</code></pre>
<p> or </p>
<pre><code> virt-ls guestname /dir
</code></pre>
<p> whereas in this version you should use <i>-a</i> or <i>-d</i> respectively to avoid the confusing case where a disk image might have the same name as a guest. </p>
<p> For compatibility the old style is still supported.  </p>
<h2>NOTE ABOUT CSV FORMAT</h2>
<p> Comma-separated values (<font SIZE="-1">CSV</font>) is a deceptive format. It <i>seems</i> like it should be easy to parse, but it is definitely not easy to parse. </p>
<p> Myth: Just split fields at commas. Reality: This does <i>not</i> work reliably. This example has two columns: </p>
<pre><code> &quot;foo,bar&quot;,baz
</code></pre>
<p> Myth: Read the file one line at a time. Reality: This does <i>not</i> work reliably. This example has one row: </p>
<pre><code> &quot;foo
 bar&quot;,baz
</code></pre>
<p> For shell scripts, use <code>&quot;csvtool&quot;</code> (<a rel="nofollow" href="https://github.com/Chris00/ocaml-csv">https://github.com/Chris00/ocaml-csv</a> also packaged in major Linux distributions). </p>
<p> For other languages, use a <font SIZE="-1">CSV</font> processing library (eg. <code>&quot;Text::CSV&quot;</code> for Perl or Python&#8217;s built-in csv library). </p>
<p> Most spreadsheets and databases can import <font SIZE="-1">CSV</font> directly.  </p>
<h2>EXIT STATUS</h2>
<p> This program returns 0 if successful, or non-zero if there was an error.  </p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3), <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1), <i><a href="/docs/linux/man/1-virt-cat/">virt-cat</a></i>(1), <i><a href="/docs/linux/man/1-virt-copy-out/">virt-copy-out</a></i>(1), <i><a href="/docs/linux/man/1-virt-diff/">virt-diff</a></i>(1), <i><a href="/docs/linux/man/1-virt-tar-out/">virt-tar-out</a></i>(1), <a rel="nofollow" href="http://libguestfs.org/.">http://libguestfs.org/.</a>  </p>
<h2>AUTHOR</h2>
<p> Richard W.M. Jones <a rel="nofollow" href="http://people.redhat.com/~rjones/">http://people.redhat.com/~rjones/</a>  </p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2009-2016 Red Hat Inc.  </p>
<h2>LICENSE</h2>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE. </font> See the <font SIZE="-1">GNU</font> General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, <font SIZE="-1">MA 02110-1301 USA.</font>  </p>
<h2>BUGS</h2>
<p> To get a list of bugs against libguestfs, use this link: <a rel="nofollow" href="https://bugzilla.redhat.com/buglist.cgi?component=libguestfs">https://bugzilla.redhat.com/buglist.cgi?component=libguestfs</a>&amp;product=Virtualization+Tools </p>
<p> To report a new bug against libguestfs, use this link: <a rel="nofollow" href="https://bugzilla.redhat.com/enter_bug.cgi?component=libguestfs">https://bugzilla.redhat.com/enter_bug.cgi?component=libguestfs</a>&amp;product=Virtualization+Tools </p>
<p> When reporting a bug, please supply: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The version of libguestfs. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Where you got libguestfs (eg. which Linux distro, compiled from source, etc) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Describe the bug accurately and give a way to reproduce it. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Run <i><a href="/docs/linux/man/1-libguestfs-test-tool/">libguestfs-test-tool</a></i>(1) and paste the <code>complete, unedited</code> output into the bug report. </p>
 </dd></dl>
