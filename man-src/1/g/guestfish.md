---
title: "guestfish(1)"
name: "guestfish"
section: "1"
letter: "g"
url: "/docs/linux/man/1-guestfish/"
description: "guestfish – the guest filesystem shell"
---

<h2 class="name">NAME</h2>
<p> guestfish &#8211; the guest filesystem shell </p>
<h2>SYNOPSIS</h2>
<pre><code>
guestfish[--options][commands] guestfish
        guestfish[--ro | --rw] -
    a disk.img
        guestfish[--ro | --rw] -
    a disk.img - m dev[:mountpoint] guestfish - d libvirt - domain guestfish[--ro | --rw] - a disk.img - i guestfish - d libvirt - domain - i
</code></pre>
<h2>WARNING</h2>
<p> Using <tt>&quot;guestfish&quot;</tt> in write mode on live virtual machines, or concurrently with other disk editing tools, can be dangerous, potentially causing disk corruption. The virtual machine must be shut down before you use this command, and disk images must not be edited concurrently. </p>
<p> Use the <i>&#8211;ro</i> (read-only) option to use <tt>&quot;guestfish&quot;</tt> safely if the disk image or virtual machine might be live. You may see strange or inconsistent results if running concurrently with other changes, but with this option you won&#8217;t risk disk corruption.</p>
<h2>DESCRIPTION</h2>
<p> Guestfish is a shell and command-line tool for examining and modifying virtual machine filesystems. It uses libguestfs and exposes all of the functionality of the guestfs <font SIZE="-1">API,</font> see <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3). </p>
<p> Guestfish gives you structured access to the libguestfs <font SIZE="-1">API,</font> from shell scripts or the command line or interactively. If you want to rescue a broken virtual machine image, you should look at the <i><a href="/docs/linux/man/1-virt-rescue/">virt-rescue</a></i>(1) command.</p>
<h2>EXAMPLES</h2>
<h3>As an interactive shell</h3>
<p> $ guestfish</p>
<p> Welcome to guestfish, the guest filesystem shell for<br />
 editing virtual machine filesystems.</p>
<p> Type: &#8216;help&#8217; for a list of commands<br />
       &#8216;man&#8217; to read the manual<br />
       &#8216;quit&#8217; to quit the shell</p>
<p> &gt;&lt;fs&gt; add-ro disk.img<br />
 &gt;&lt;fs&gt; run<br />
 &gt;&lt;fs&gt; list-filesystems<br />
 /dev/sda1: ext4<br />
 /dev/vg_guest/lv_root: ext4<br />
 /dev/vg_guest/lv_swap: swap<br />
 &gt;&lt;fs&gt; mount /dev/vg_guest/lv_root /<br />
 &gt;&lt;fs&gt; cat /etc/fstab<br />
#/ etc / fstab<br />
#Created by anaconda<br />
 [&#8230;]<br />
 &gt;&lt;fs&gt; exit</p>
<h3>From shell scripts</h3>
<p> Create a new <i>/etc/motd</i> file in a guest or disk image: </p>
<pre>
 guestfish &lt;&lt;_EOF_
 add disk.img
 run
 mount /dev/vg_guest/lv_root /
 write /etc/motd &quot;Welcome, new users&quot;
 _EOF_
</pre>
<p> List the <font SIZE="-1">LVM</font> logical volumes in a disk image: </p>
<pre>
 guestfish -a disk.img --ro &lt;&lt;_EOF_
 run
 lvs
 _EOF_
</pre>
<p> List all the filesystems in a disk image: </p>
<pre>
 guestfish -a disk.img --ro &lt;&lt;_EOF_
 run
 list-filesystems
 _EOF_
</pre>
<h3>On one command line</h3>
<p> Update <i>/etc/resolv.conf</i> in a guest: </p>
<pre>
 guestfish \
   add disk.img : run : mount /dev/vg_guest/lv_root / : \
   write /etc/resolv.conf &quot;nameserver 1.2.3.4&quot;
</pre>
<p> Edit <i>/boot/grub/grub.conf</i> interactively: </p>
<p>guestfish&#8211; rw&#8211; add disk.img&#8211; mount / dev / vg_guest / lv_root&#8211; mount / dev / sda1 : / boot edit / boot / grub / grub.conf</p>
<h3>Mount disks automatically</h3>
<p> Use the <i>-i</i> option to automatically mount the disks from a virtual machine: </p>
<pre>
 guestfish --ro -a disk.img -i cat /etc/group
 guestfish --ro -d libvirt-domain -i cat /etc/group
</pre>
<p> Another way to edit <i>/boot/grub/grub.conf</i> interactively is: </p>
<pre>
 guestfish --rw -a disk.img -i edit /boot/grub/grub.conf
</pre>
<h3>As a script interpreter</h3>
<p> Create a 100MB disk containing an ext2-formatted partition: </p>
<pre>
 #!/usr/bin/guestfish -f
 sparse test1.img 100M
 run
 part-disk /dev/sda mbr
 mkfs ext2 /dev/sda1
</pre>
<h3>Start with a prepared disk</h3>
<p> An alternate way to create a 100MB disk called <i>test1.img</i> containing a single ext2-formatted partition: </p>
<pre>
 guestfish -N fs
</pre>
<p> To list what is available do: </p>
<pre>
 guestfish -N help | less
</pre>
<h3>Remote drives</h3>
<p> Access a remote disk using <font SIZE="-1">NBD:</font> </p>
<pre>
 guestfish -a <a href="nbd://example.com">nbd://example.com</a>
</pre>
<h3>Remote control</h3>
<p>eval &#8220;`guestfish &#8211;listen`&#8221; guestfish&#8211; remote add &#8211; ro disk.img<br />
                                                         guestfish&#8211; remote run<br />
                                                             guestfish&#8211; remote lvs</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Displays general help on options.</p>
<dt><code>-h</code></p>
<dd>
<dt><code>&#8211;cmd-help</code></p>
<dd> Lists all available guestfish commands.</p>
<dt><code>-h cmd</code></p>
<dd>
<dt><code>&#8211;cmd-help cmd</code></p>
<dd> Displays detailed help on a single command <tt>&quot;cmd&quot;</tt>.</p>
<dt><code>-a image</code></p>
<dd>
<dt><code>&#8211;add image</code></p>
<dd> Add a block device or virtual machine image to the shell. </p>
<p> The format of the disk image is auto-detected. To override this and force a particular format use the <i>&#8211;format=..</i> option. </p>
<p> Using this flag is mostly equivalent to using the <tt>&quot;add&quot;</tt> command, with <tt>&quot;readonly:true&quot;</tt> if the <i>&#8211;ro</i> flag was given, and with <tt>&quot;format:...&quot;</tt> if the <i>&#8211;format=&#8230;</i> flag was given.</p>
<dt><code>-a </code><font SIZE="-1"><code>URI</code></font></p>
<dd>
<dt><code>&#8211;add </code><font SIZE="-1"><code>URI</code></font></p>
<dd> Add a remote disk. See &#8220;<font SIZE="-1">ADDING REMOTE STORAGE&#8221;</font>.</p>
<dt><code>-c </code><font SIZE="-1"><code>URI</code></font></p>
<dd>
<dt><code>&#8211;connect </code><font SIZE="-1"><code>URI</code></font></p>
<dd> When used in conjunction with the <i>-d</i> option, this specifies the libvirt <font SIZE="-1">URI</font> to use. The default is to use the default libvirt connection.</p>
<dt><code>&#8211;csh</code></p>
<dd> If using the <i>&#8211;listen</i> option and a csh-like shell, use this option. See section &#8220;<font SIZE="-1">REMOTE CONTROL AND CSH&#8221;</font> below.</p>
<dt><code>-d libvirt-domain</code></p>
<dd>
<dt><code>&#8211;domain libvirt-domain</code></p>
<dd> Add disks from the named libvirt domain. If the <i>&#8211;ro</i> option is also used, then any libvirt domain can be used. However in write mode, only libvirt domains which are shut down can be named here. </p>
<p> Domain UUIDs can be used instead of names. </p>
<p> Using this flag is mostly equivalent to using the <tt>&quot;add-domain&quot;</tt> command, with <tt>&quot;readonly:true&quot;</tt> if the <i>&#8211;ro</i> flag was given, and with <tt>&quot;format:...&quot;</tt> if the <i>&#8211;format=&#8230;</i> flag was given.</p>
<dt><code>&#8211;echo-keys</code></p>
<dd> When prompting for keys and passphrases, guestfish normally turns echoing off so you cannot see what you are typing. If you are not worried about Tempest attacks and there is no one else in the room you can specify this flag to see what you are typing.</p>
<dt><code>-f file</code></p>
<dd>
<dt><code>&#8211;file file</code></p>
<dd> Read commands from <tt>&quot;file&quot;</tt>. To write pure guestfish scripts, use: </p>
<pre>
 #!/usr/bin/guestfish -f
</pre>
<dt><code>&#8211;format=raw|qcow2|..</code></p>
<dd>
<dt><code>&#8211;format</code></p>
<dd> The default for the <i>-a</i> option is to auto-detect the format of the disk image. Using this forces the disk format for <i>-a</i> options which follow on the command line. Using <i>&#8211;format</i> with no argument switches back to auto-detection for subsequent <i>-a</i> options. </p>
<p> For example: </p>
<pre>
 guestfish --format=raw -a disk.img
</pre>
<p> forces raw format (no auto-detection) for <i>disk.img</i>. </p>
<pre>
 guestfish --format=raw -a disk.img --format -a another.img
</pre>
<p> forces raw format (no auto-detection) for <i>disk.img</i> and reverts to auto-detection for <i>another.img</i>. </p>
<p> If you have untrusted raw-format guest disk images, you should use this option to specify the disk format. This avoids a possible security problem with malicious guests (<font SIZE="-1">CVE-2010-3851</font>). See also &#8220;add&#8221;.</p>
<dt><code>-i</code></p>
<dd>
<dt><code>&#8211;inspector</code></p>
<dd> Using <i><a href="/docs/linux/man/1-virt-inspector/">virt-inspector</a></i>(1) code, inspect the disks looking for an operating system and mount filesystems as they would be mounted on the real virtual machine. </p>
<p> Typical usage is either: </p>
<pre>
 guestfish -d myguest -i
</pre>
<p> (for an inactive libvirt domain called <i>myguest</i>), or: </p>
<pre>
 guestfish --ro -d myguest -i
</pre>
<p> (for active domains, readonly), or specify the block device directly: </p>
<pre>
 guestfish --rw -a /dev/Guests/MyGuest -i
</pre>
<p> Note that the command line syntax changed slightly over older versions of guestfish. You can still use the old syntax: </p>
<p>guestfish[&#8211;ro] &#8211; i disk.img guestfish[&#8211;ro] &#8211; i libvirt &#8211; domain</p>
<p> Using this flag is mostly equivalent to using the <tt>&quot;inspect-os&quot;</tt> command and then using other commands to mount the filesystems that were found.</p>
<dt><code>&#8211;keys-from-stdin</code></p>
<dd> Read key or passphrase parameters from stdin. The default is to try to read passphrases from the user by opening <i>/dev/tty</i>.</p>
<dt><code>&#8211;listen</code></p>
<dd> Fork into the background and listen for remote commands. See section &#8220;<font SIZE="-1">REMOTE CONTROL GUESTFISH OVER A SOCKET&#8221;</font> below.</p>
<dt><code>&#8211;live</code></p>
<dd> Connect to a live virtual machine. (Experimental, see &#8220;<font SIZE="-1">ATTACHING TO RUNNING DAEMONS&#8221;</font> in <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3)).</p>
<dt><code>-m dev[:mountpoint[:options[:fstype]]]</code></p>
<dd>
<dt><code>&#8211;mount dev[:mountpoint[:options[:fstype]]]</code></p>
<dd> Mount the named partition or logical volume on the given mountpoint. </p>
<p> If the mountpoint is omitted, it defaults to <i>/</i>. </p>
<p> You have to mount something on <i>/</i> before most commands will work. </p>
<p> If any <i>-m</i> or <i>&#8211;mount</i> options are given, the guest is automatically launched. </p>
<p> If you don&#8217;t know what filesystems a disk image contains, you can either run guestfish without this option, then list the partitions, filesystems and LVs available (see &#8220;list-partitions&#8221;, &#8220;list-filesystems&#8221; and &#8220;lvs&#8221; commands), or you can use the <i><a href="/docs/linux/man/1-virt-filesystems/">virt-filesystems</a></i>(1) program. </p>
<p> The third (and rarely used) part of the mount parameter is the list of mount options used to mount the underlying filesystem. If this is not given, then the mount options are either the empty string or <tt>&quot;ro&quot;</tt> (the latter if the <i>&#8211;ro</i> flag is used). By specifying the mount options, you override this default choice. Probably the only time you would use this is to enable ACLs and/or extended attributes if the filesystem can support them: </p>
<pre>
 -m /dev/sda1:/:acl,user_xattr
</pre>
<p> Using this flag is equivalent to using the <tt>&quot;mount-options&quot;</tt> command. </p>
<p> The fourth part of the parameter is the filesystem driver to use, such as <tt>&quot;ext3&quot;</tt> or <tt>&quot;ntfs&quot;</tt>. This is rarely needed, but can be useful if multiple drivers are valid for a filesystem (eg: <tt>&quot;ext2&quot;</tt> and <tt>&quot;ext3&quot;</tt>), or if libguestfs misidentifies a filesystem.</p>
<dt><code>&#8211;network</code></p>
<dd> Enable <font SIZE="-1">QEMU</font> user networking in the guest.</p>
<dt><code>-N [filename=]type</code></p>
<dd>
<dt><code>&#8211;new [filename=]type</code></p>
<dd>
<dt><code>-N help</code></p>
<dd> Prepare a fresh disk image formatted as &#8220;type&#8221;. This is an alternative to the <i>-a</i> option: whereas <i>-a</i> adds an existing disk, <i>-N</i> creates a preformatted disk with a filesystem and adds it. See &#8220;<font SIZE="-1">PREPARED DISK IMAGES&#8221;</font> below.</p>
<dt><code>-n</code></p>
<dd>
<dt><code>&#8211;no-sync</code></p>
<dd> Disable autosync. This is enabled by default. See the discussion of autosync in the <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3) manpage.</p>
<dt><code>&#8211;no-dest-paths</code></p>
<dd> Don&#8217;t tab-complete paths on the guest filesystem. It is useful to be able to hit the tab key to complete paths on the guest filesystem, but this causes extra &#8220;hidden&#8221; guestfs calls to be made, so this option is here to allow this feature to be disabled.</p>
<dt><code>&#8211;pipe-error</code></p>
<dd> If writes fail to pipe commands (see &#8220;<font SIZE="-1">PIPES&#8221;</font> below), then the command returns an error. </p>
<p> The default (also for historical reasons) is to ignore such errors so that: </p>
<pre>
 &gt;&lt;fs&gt; command_with_lots_of_output | head
</pre>
<p> doesn&#8217;t give an error.</p>
<dt><code>&#8211;progress-bars</code></p>
<dd> Enable progress bars, even when guestfish is used non-interactively. </p>
<p> Progress bars are enabled by default when guestfish is used as an interactive shell.</p>
<dt><code>&#8211;no-progress-bars</code></p>
<dd> Disable progress bars.</p>
<dt><code>&#8211;remote[=pid]</code></p>
<dd> Send remote commands to <tt>$GUESTFISH_PID</tt> or <tt>&quot;pid&quot;</tt>. See section &#8220;<font SIZE="-1">REMOTE CONTROL GUESTFISH OVER A SOCKET&#8221;</font> below.</p>
<dt><code>-r</code></p>
<dd>
<dt><code>&#8211;ro</code></p>
<dd> This changes the <i>-a</i>, <i>-d</i> and <i>-m</i> options so that disks are added and mounts are done read-only. </p>
<p> The option must always be used if the disk image or virtual machine might be running, and is generally recommended in cases where you don&#8217;t need write access to the disk. </p>
<p> Note that prepared disk images created with <i>-N</i> are not affected by this option. Also commands like <tt>&quot;add&quot;</tt> are not affected &#8211; you have to specify the <tt>&quot;readonly:true&quot;</tt> option explicitly if you need it. </p>
<p> See also &#8220;<font SIZE="-1">OPENING DISKS FOR READ AND WRITE&#8221;</font> below.</p>
<dt><code>&#8211;selinux</code></p>
<dd> This option is provided for backwards compatibility and does nothing.</p>
<dt><code>-v</code></p>
<dd>
<dt><code>&#8211;verbose</code></p>
<dd> Enable very verbose messages. This is particularly useful if you find a bug.</p>
<dt><code>-V</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd> Display the guestfish / libguestfs version number and exit.</p>
<dt><code>-w</code></p>
<dd>
<dt><code>&#8211;rw</code></p>
<dd> This changes the <i>-a</i>, <i>-d</i> and <i>-m</i> options so that disks are added and mounts are done read-write. </p>
<p> See &#8220;<font SIZE="-1">OPENING DISKS FOR READ AND WRITE&#8221;</font> below.</p>
<dt><code>-x</code></p>
<dd> Echo each command before executing it.</dl>
<h2>COMMANDS ON COMMAND LINE</h2>
<p> Any additional (non-option) arguments are treated as commands to execute. </p>
<p> Commands to execute should be separated by a colon (<tt>&quot;:&quot;</tt>), where the colon is a separate parameter. Thus: </p>
<p>guestfish cmd[args&#8230;] : cmd[args&#8230;] : cmd[args&#8230;]&#8230;</p>
<p> If there are no additional arguments, then we enter a shell, either an interactive shell with a prompt (if the input is a terminal) or a non-interactive shell. </p>
<p> In either command line mode or non-interactive shell, the first command that gives an error causes the whole shell to exit. In interactive mode (with a prompt) if a command fails, you can continue to enter commands.</p>
<h2>USING launch (OR run)</h2>
<p> As with <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3), you must first configure your guest by adding disks, then launch it, then mount any disks you need, and finally issue actions/commands. So the general order of the day is:</p>
<dl>
<dt>&bull;</p>
<dd> add or -a/&#8211;add</p>
<dt>&bull;</p>
<dd> launch (aka run)</p>
<dt>&bull;</p>
<dd> mount or -m/&#8211;mount</p>
<dt>&bull;</p>
<dd> any other commands</dl>
<p> <tt>&quot;run&quot;</tt> is a synonym for <tt>&quot;launch&quot;</tt>. You must <tt>&quot;launch&quot;</tt> (or <tt>&quot;run&quot;</tt>) your guest before mounting or performing any other commands. </p>
<p> The only exception is that if any of the <i>-i</i>, <i>-m</i>, <i>&#8211;mount</i>, <i>-N</i> or <i>&#8211;new</i> options were given then <tt>&quot;run&quot;</tt> is done automatically, simply because guestfish can&#8217;t perform the action you asked for without doing this.</p>
<h2>OPENING DISKS FOR READ AND WRITE</h2>
<p> The guestfish, <i><a href="/docs/linux/man/1-guestmount/">guestmount</a></i>(1) and <i><a href="/docs/linux/man/1-virt-rescue/">virt-rescue</a></i>(1) options <i>&#8211;ro</i> and <i>&#8211;rw</i> affect whether the other command line options <i>-a</i>, <i>-c</i>, <i>-d</i>, <i>-i</i> and <i>-m</i> open disk images read-only or for writing. </p>
<p> In libguestfs ≤ 1.10, guestfish, guestmount and virt-rescue defaulted to opening disk images supplied on the command line for write. To open a disk image read-only you have to do <i>-a image &#8211;ro</i>. </p>
<p> This matters: If you accidentally open a live <font SIZE="-1">VM</font> disk image writable then you will cause irreversible disk corruption. </p>
<p> In a future libguestfs we intend to change the default the other way. Disk images will be opened read-only. You will have to either specify <i>guestfish &#8211;rw</i>, <i>guestmount &#8211;rw</i>, <i>virt-rescue &#8211;rw</i>, or change the configuration file in order to get write access for disk images specified by those other command line options. </p>
<p> This version of guestfish, guestmount and virt-rescue has a <i>&#8211;rw</i> option which does nothing (it is already the default). However it is highly recommended that you use this option to indicate that you need write access, and prepare your scripts for the day when this option will be required for write access. </p>
<p> <code>Note:</code> This does <i>not</i> affect commands like &#8220;add&#8221; and &#8220;mount&#8221;, or any other libguestfs program apart from guestfish and guestmount.</p>
<h2>QUOTING</h2>
<p> You can quote ordinary parameters using either single or double quotes. For example: </p>
<pre>
 add &quot;file with a space.img&quot;
 rm '/file name'
 rm '/&quot;'
</pre>
<p> A few commands require a list of strings to be passed. For these, use a whitespace-separated list, enclosed in quotes. Strings containing whitespace to be passed through must be enclosed in single quotes. A literal single quote must be escaped with a backslash. </p>
<pre>
 vgcreate VG &quot;/dev/sda1 /dev/sdb1&quot;
 command &quot;/bin/echo 'foo      bar'&quot;
 command &quot;/bin/echo \'foo\'&quot;
</pre>
<h3><font SIZE="-1">ESCAPE SEQUENCES IN DOUBLE QUOTED ARGUMENTS</font></h3>
<p> In double-quoted arguments (only) use backslash to insert special characters:</p>
<dl>
<dt>&quot;&quot;</p>
<dd> Alert (bell) character.</p>
<dt>&quot;&quot;</p>
<dd> Backspace character.</p>
<dt>&quot;&quot;</p>
<dd> Form feed character.</p>
<dt>&quot;
&quot;</p>
<dd> Newline character.</p>
<dt>&quot;&quot;</p>
<dd> Carriage return character.</p>
<dt>&quot;	&quot;</p>
<dd> Horizontal tab character.</p>
<dt>&quot;&quot;</p>
<dd> Vertical tab character.</p>
<dt>&quot;\&quot;&quot;</p>
<dd> A literal double quote character.</p>
<dt>&quot;\ooo&quot;</p>
<dd> A character with octal value <i>ooo</i>. There must be precisely 3 octal digits (unlike C).</p>
<dt>&quot;
