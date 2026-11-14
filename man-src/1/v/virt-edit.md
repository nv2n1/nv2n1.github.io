---
title: "virt-edit(1)"
name: "virt-edit"
section: "1"
letter: "v"
url: "/docs/linux/man/1-virt-edit/"
description: "virt-edit – Edit a file in a virtual machine"
---

<h2 class="name">NAME</h2>
<p> virt-edit &#8211; Edit a file in a virtual machine </p>
<h2>SYNOPSIS</h2>
<pre><code>
virt - edit[--options] - d domname file[file...] virt - edit[--options] - a disk.img[-a disk.img...] file[file...] virt - edit[-d domname | -a disk.img] file - e 'expr'
</code></pre>
<p> Old-style: </p>
<pre>
 virt-edit domname file
 virt-edit disk.img [disk.img ...] file
</pre>
<h2>WARNING</h2>
<p> Using <tt>&quot;virt-edit&quot;</tt> on live virtual machines, or concurrently with other disk editing tools, can be dangerous, potentially causing disk corruption. The virtual machine must be shut down before you use this command, and disk images must not be edited concurrently.</p>
<h2>DESCRIPTION</h2>
<p> <tt>&quot;virt-edit&quot;</tt> is a command line tool to edit <tt>&quot;file&quot;</tt> where each <tt>&quot;file&quot;</tt> exists in the named virtual machine (or disk image). </p>
<p> Multiple filenames can be given, in which case they are each edited in turn. Each filename must be a full path, starting at the root directory (starting with &#8216;/&#8217;). </p>
<p> If you want to just view a file, use <i><a href="/docs/linux/man/1-virt-cat/">virt-cat</a></i>(1). </p>
<p> For more complex cases you should look at the <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1) tool (see &#8220;<font SIZE="-1">USING GUESTFISH&#8221;</font> below). </p>
<p> <tt>&quot;virt-edit&quot;</tt> cannot be used to create a new file. <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1) can do that and much more.</p>
<h2>EXAMPLES</h2>
<p> Edit the named files interactively: </p>
<pre>
 virt-edit -d mydomain /boot/grub/grub.conf
 virt-edit -d mydomain /etc/passwd
</pre>
<p> For Windows guests, some Windows paths are understood: </p>
<pre>
 virt-edit -d mywindomain 'c:utoexec.bat'
</pre>
<p> If Perl is installed, you can also edit files non-interactively (see &#8220;NON-INTERACTIVE <font SIZE="-1">EDITING&#8221;</font> below). To change the init default level to 5: </p>
<pre>
 virt-edit -d mydomain /etc/inittab -e 's/^id:.*/id:5:initdefault:/'
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
<dt><code>-b</code> extension</p>
<dd>
<dt><code>&#8211;backup</code> extension</p>
<dd> Create a backup of the original file <i>in the guest disk image</i>. The backup has the original filename with <tt>&quot;extension&quot;</tt> added. </p>
<p> Usually the first character of <tt>&quot;extension&quot;</tt> would be a dot <tt>&quot;.&quot;</tt> so you would write: </p>
<pre>
 virt-edit -b .orig [etc]
</pre>
<p> By default, no backup file is made.</p>
<dt><code>-c </code><font SIZE="-1"><code>URI</code></font></p>
<dd>
<dt><code>&#8211;connect </code><font SIZE="-1"><code>URI</code></font></p>
<dd> If using libvirt, connect to the given <i></i><font SIZE="-1"><i>URI</i></font><i></i>. If omitted, then we connect to the default libvirt hypervisor. </p>
<p> If you specify guest block devices directly, then libvirt is not used at all.</p>
<dt><code>-d</code> guest</p>
<dd>
<dt><code>&#8211;domain</code> guest</p>
<dd> Add all the disks from the named libvirt guest. Domain UUIDs can be used instead of names.</p>
<dt><code>&#8211;echo-keys</code></p>
<dd> When prompting for keys and passphrases, virt-edit normally turns echoing off so you cannot see what you are typing. If you are not worried about Tempest attacks and there is no one else in the room you can specify this flag to see what you are typing.</p>
<dt><code>-e</code> <font SIZE="-1">EXPR</font></p>
<dd>
<dt><code>&#8211;edit</code> <font SIZE="-1">EXPR</font></p>
<dd>
<dt><code>&#8211;expr</code> <font SIZE="-1">EXPR</font></p>
<dd> Instead of launching the external editor, non-interactively apply the Perl expression <tt>&quot;EXPR&quot;</tt> to each line in the file. See &#8220;NON-INTERACTIVE <font SIZE="-1">EDITING&#8221;</font> below. </p>
<p> Be careful to properly quote the expression to prevent it from being altered by the shell. </p>
<p> Note that this option is only available when Perl 5 is installed.</p>
<dt><code>&#8211;format=raw|qcow2|..</code></p>
<dd>
<dt><code>&#8211;format</code></p>
<dd> The default for the <i>-a</i> option is to auto-detect the format of the disk image. Using this forces the disk format for <i>-a</i> options which follow on the command line. Using <i>&#8211;format</i> with no argument switches back to auto-detection for subsequent <i>-a</i> options. </p>
<p> For example: </p>
<pre>
 virt-edit --format=raw -a disk.img file
</pre>
<p> forces raw format (no auto-detection) for <i>disk.img</i>. </p>
<pre>
 virt-edit --format=raw -a disk.img --format -a another.img file
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
<p> Previous versions of virt-edit allowed you to write either: </p>
<pre>
 virt-edit disk.img [disk.img ...] file
</pre>
<p> or </p>
<pre>
 virt-edit guestname file
</pre>
<p> whereas in this version you should use <i>-a</i> or <i>-d</i> respectively to avoid the confusing case where a disk image might have the same name as a guest. </p>
<p> For compatibility the old style is still supported.</p>
<h2>NON-INTERACTIVE EDITING</h2>
<p> <tt>&quot;virt-edit&quot;</tt> normally calls out to <tt>$EDITOR</tt> (or vi) so the system administrator can interactively edit the file. </p>
<p> There are two ways also to use <tt>&quot;virt-edit&quot;</tt> from scripts in order to make automated edits to files. (Note that although you <i>can</i> use <tt>&quot;virt-edit&quot;</tt> like this, it&#8217;s less error-prone to write scripts directly using the libguestfs <font SIZE="-1">API</font> and Augeas for configuration file editing.) </p>
<p> The first method is to temporarily set <tt>$EDITOR</tt> to any script or program you want to run. The script is invoked as <tt>&quot;$EDITOR tmpfile&quot;</tt> and it should update <tt>&quot;tmpfile&quot;</tt> in place however it likes. </p>
<p> The second method is to use the <i>-e</i> parameter of <tt>&quot;virt-edit&quot;</tt> to run a short Perl snippet in the style of <i><a href="/docs/linux/man/1-sed/">sed</a></i>(1). For example to replace all instances of <tt>&quot;foo&quot;</tt> with <tt>&quot;bar&quot;</tt> in a file: </p>
<pre>
 virt-edit -d domname filename -e 's/foo/bar/'
</pre>
<p> The full power of Perl regular expressions can be used (see <i><a href="/docs/linux/man/1-perlre/">perlre</a></i>(1)). For example to delete root&#8217;s password you could do: </p>
<pre>
 virt-edit -d domname /etc/passwd -e 's/^root:.*?:/root::/'
</pre>
<p> What really happens is that the snippet is evaluated as a Perl expression for each line of the file. The line, including the final <tt>&quot;
&quot;</tt>, is passed in <tt>$_</tt> and the expression should update <tt>$_</tt> or leave it unchanged. </p>
<p> To delete a line, set <tt>$_</tt> to the empty string. For example, to delete the <tt>&quot;apache&quot;</tt> user account from the password file you can do: </p>
<pre>
 virt-edit -d mydomain /etc/passwd -e '$_ = &quot;&quot; if /^apache:/'
</pre>
<p> To insert a line, prepend or append it to <tt>$_</tt>. However appending lines to the end of the file is rather difficult this way since there is no concept of &#8220;last line of the file&#8221; &#8211; your expression just doesn&#8217;t get called again. You might want to use the first method (setting <tt>$EDITOR</tt>) if you want to do this. </p>
<p> The variable <tt>$lineno</tt> contains the current line number. As is traditional, the first line in the file is number <tt>1</tt>. </p>
<p> The return value from the expression is ignored, but the expression may call <tt>&quot;die&quot;</tt> in order to abort the whole program, leaving the original file untouched. </p>
<p> Remember when matching the end of a line that <tt>$_</tt> may contain the final <tt>&quot;
&quot;</tt>, or (for <font SIZE="-1">DOS</font> files) <tt>&quot;
&quot;</tt>, or if the file does not end with a newline then neither of these. Thus to match or substitute some text at the end of a line, use this regular expression: </p>
<pre>
 /some text(?
)?$/
</pre>
<p> Alternately, use the perl <tt>&quot;chomp&quot;</tt> function, being careful not to chomp <tt>$_</tt> itself (since that would remove all newlines from the file): </p>
<pre>
 my $m = $_; chomp $m; $m =~ /some text$/
</pre>
<h2>WINDOWS PATHS</h2>
<p> <tt>&quot;virt-edit&quot;</tt> has a limited ability to understand Windows drive letters and paths (eg. <i>E:ooar.txt</i>). </p>
<p> If and only if the guest is running Windows then:</p>
<dl>
<dt>&bull;</p>
<dd> Drive letter prefixes like <tt>&quot;C:&quot;</tt> are resolved against the Windows Registry to the correct filesystem.</p>
<dt>&bull;</p>
<dd> Any backslash (<tt>&quot;\&quot;</tt>) characters in the path are replaced with forward slashes so that libguestfs can process it.</p>
<dt>&bull;</p>
<dd> The path is resolved case insensitively to locate the file that should be edited.</dl>
<p> There are some known shortcomings:</p>
<dl>
<dt>&bull;</p>
<dd> Some <font SIZE="-1">NTFS</font> symbolic links may not be followed correctly.</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">NTFS</font> junction points that cross filesystems are not followed.</dl>
<h2>USING GUESTFISH</h2>
<p> <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1) is a more powerful, lower level tool which you can use when <tt>&quot;virt-edit&quot;</tt> doesn&#8217;t work. </p>
<p> Using <tt>&quot;virt-edit&quot;</tt> is approximately equivalent to doing: </p>
<pre>
 guestfish --rw -i -d domname edit /file
</pre>
<p> where <tt>&quot;domname&quot;</tt> is the name of the libvirt guest, and <i>/file</i> is the full path to the file. </p>
<p> The command above uses libguestfs&#8217;s guest inspection feature and so does not work on guests that libguestfs cannot inspect, or on things like arbitrary disk images that don&#8217;t contain guests. To edit a file on a disk image directly, use: </p>
<pre>
 guestfish --rw -a disk.img -m /dev/sda1 edit /file
</pre>
<p> where <i>disk.img</i> is the disk image, <i>/dev/sda1</i> is the filesystem within the disk image to edit, and <i>/file</i> is the full path to the file. </p>
<p> <tt>&quot;virt-edit&quot;</tt> cannot create new files. Use the guestfish commands <tt>&quot;touch&quot;</tt>, <tt>&quot;write&quot;</tt> or <tt>&quot;upload&quot;</tt> instead: </p>
<pre>
 guestfish --rw -i -d domname touch /newfile
 guestfish --rw -i -d domname write /newfile &quot;new content&quot;
 guestfish --rw -i -d domname upload localfile /newfile
</pre>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt>&quot;EDITOR&quot;</p>
<dd> If set, this string is used as the editor. It may contain arguments, eg. <tt>&quot;emacs -nw&quot;</tt> </p>
<p> If not set, <tt>&quot;vi&quot;</tt> is used.</dl>
<h2>EXIT STATUS</h2>
<p> This program returns 0 if successful, or non-zero if there was an error.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3), <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1), <i><a href="/docs/linux/man/1-virt-cat/">virt-cat</a></i>(1), <i><a href="/docs/linux/man/1-virt-copy-in/">virt-copy-in</a></i>(1), <i><a href="/docs/linux/man/1-virt-tar-in/">virt-tar-in</a></i>(1), <a rel="nofollow" href="http://libguestfs.org/,">http://libguestfs.org/,</a> <i><a href="/docs/linux/man/1-perl/">perl</a></i>(1), <i><a href="/docs/linux/man/1-perlre/">perlre</a></i>(1).</p>
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
