---
title: "guestmount(1)"
name: "guestmount"
section: "1"
letter: "g"
url: "/docs/linux/man/1-guestmount/"
description: "guestmount – Mount a guest filesystem on the host using FUSE and libguestfs"
---

<h2 class="name">NAME</h2>
<p> guestmount &#8211; Mount a guest filesystem on the host using FUSE and libguestfs </p>
<h2>SYNOPSIS</h2>
<pre><code>
guestmount[--options] - a disk.img - m device[--ro] mountpoint guestmount[--options] - a disk.img - i[--ro] mountpoint guestmount[--options] - d Guest - i[--ro] mountpoint
</code></pre>
<h2>WARNING</h2>
<p> Using <tt>&quot;guestmount&quot;</tt> in write mode on live virtual machines, or concurrently with other disk editing tools, can be dangerous, potentially causing disk corruption. The virtual machine must be shut down before you use this command, and disk images must not be edited concurrently. </p>
<p> Use the <i>&#8211;ro</i> (read-only) option to use <tt>&quot;guestmount&quot;</tt> safely if the disk image or virtual machine might be live. You may see strange or inconsistent results if running concurrently with other changes, but with this option you won&#8217;t risk disk corruption.</p>
<h2>DESCRIPTION</h2>
<p> The guestmount program can be used to mount virtual machine filesystems and other disk images on the host. It uses libguestfs for access to the guest filesystem, and <font SIZE="-1">FUSE </font>(the &#8220;filesystem in userspace&#8221;) to make it appear as a mountable device. </p>
<p> Along with other options, you have to give at least one device (<i>-a</i> option) or libvirt domain (<i>-d</i> option), and at least one mountpoint (<i>-m</i> option) or use the <i>-i</i> inspection option or the <i>&#8211;live</i> option. How this works is better explained in the <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1) manual page, or by looking at the examples below. </p>
<p> <font SIZE="-1">FUSE</font> lets you mount filesystems as non-root. The mountpoint must be owned by you, and the filesystem will not be visible to any other users unless you make certain global configuration changes to <i>/etc/fuse.conf</i>. To unmount the filesystem, use the <i><a href="/docs/linux/man/1-guestunmount/">guestunmount</a></i>(1) command.</p>
<h2>EXAMPLES</h2>
<p> For a typical Windows guest which has its main filesystem on the first partition: </p>
<pre>
 guestmount -a windows.img -m /dev/sda1 --ro /mnt
</pre>
<p> For a typical Linux guest which has a /boot filesystem on the first partition, and the root filesystem on a logical volume: </p>
<pre>
 guestmount -a linux.img -m /dev/VG/LV -m /dev/sda1:/boot --ro /mnt
</pre>
<p> To get libguestfs to detect guest mountpoints for you: </p>
<pre>
 guestmount -a guest.img -i --ro /mnt
</pre>
<p> For a libvirt guest called &#8220;Guest&#8221; you could do: </p>
<pre>
 guestmount -d Guest -i --ro /mnt
</pre>
<p> If you don&#8217;t know what filesystems are contained in a guest or disk image, use <i><a href="/docs/linux/man/1-virt-filesystems/">virt-filesystems</a></i>(1) first: </p>
<pre>
 virt-filesystems -d MyGuest
</pre>
<p> If you want to trace the libguestfs calls but without excessive debugging information, we recommend: </p>
<pre>
 guestmount [...] --trace /mnt
</pre>
<p> If you want to debug the program, we recommend: </p>
<p>guestmount[&#8230;]&#8211; trace&#8211; verbose / mnt</p>
<p> To unmount the filesystem after using it: </p>
<pre>
 guestunmount /mnt
</pre>
<h2>NOTES</h2>
<h3>Other users cannot see the filesystem by default</h3>
<p> If you mount a filesystem as one user (eg. root), then other users will not be able to see it by default. The fix is to add the <font SIZE="-1">FUSE </font><tt>&quot;allow_other&quot;</tt> option when mounting: </p>
<pre>
 sudo guestmount [...] -o allow_other /mnt
</pre>
<h3>Enabling <font SIZE="-1">FUSE</font></h3>
<p> On some distros, you may need to add yourself to a special group (eg. <tt>&quot;fuse&quot;</tt>) before you can use any <font SIZE="-1">FUSE</font> filesystem. This is necessary on Debian and derivatives. </p>
<p> On other distros, no special group is required. It is not necessary on Fedora or Red Hat Enterprise Linux.</p>
<h3>fusermount error: Device or resource busy</h3>
<p> You can see this error when another process on the system jumps into the mountpoint you have just created, holding it open and preventing you from unmounting it. The usual culprits are various <font SIZE="-1">GUI </font>&#8220;indexing&#8221; programs. </p>
<p> The popular workaround for this problem is to retry the <tt>&quot;fusermount -u&quot;</tt> command a few times until it works (<i><a href="/docs/linux/man/1-guestunmount/">guestunmount</a></i>(1) does this for you). Unfortunately this isn&#8217;t a reliable fix if (for example) the mounted filesystem is particularly large and the intruding program particularly persistent. </p>
<p> A proper fix is to use a private mountpoint by creating a new mount namespace using the Linux-specific <i><a href="/docs/linux/man/2-clone/">clone</a></i>(2)/<i><a href="/docs/linux/man/2-unshare/">unshare</a></i>(2) flag <tt>&quot;CLONE_NEWNS&quot;</tt>. Unfortunately at the moment this requires root and we would also probably need to add it as a feature to guestmount.</p>
<h3>Race conditions possible when shutting down the connection</h3>
<p> When <i><a href="/docs/linux/man/1-guestunmount/">guestunmount</a></i>(1)/<i><a href="/docs/linux/man/1-fusermount/">fusermount</a></i>(1) exits, guestmount may still be running and cleaning up the mountpoint. The disk image will not be fully finalized. </p>
<p> This means that scripts like the following have a nasty race condition: </p>
<pre>
 guestmount -a disk.img -i /mnt
 # copy things into /mnt
 guestunmount /mnt
 # immediately try to use 'disk.img' ** UNSAFE **
</pre>
<p> The solution is to use the <i>&#8211;pid-file</i> option to write the guestmount <font SIZE="-1">PID</font> to a file, then after guestunmount spin waiting for this <font SIZE="-1">PID</font> to exit. </p>
<pre><code>
guestmount - a disk.img - i-- pid - file guestmount.pid / mnt

#...
#...

#Save the PID of guestmount *before *calling guestunmount.
                                                              pid = "$(cat guestmount.pid)"

#Unmount the filesystem.
                                                                    guestunmount /
                                                                    mnt

                                                                        timeout = 10

    count = $timeout while kill - 0 "$pid" 2 &gt; / dev / null &amp;&amp; [$count - gt 0];
do
    sleep 1((count--))
        done
        if[$count - eq 0];
then
    echo "$0: wait for guestmount to exit failed after $timeout seconds" exit 1 fi

#Now it is safe to use the disk image.
</code></pre>
<p> Note that if you use the <tt>&quot;guestfs_mount_local&quot;</tt> <font SIZE="-1">API</font> directly (see &#8220;<font SIZE="-1">MOUNT LOCAL&#8221;</font> in <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3)) then it is much easier to write a safe, race-free program.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a image</code></p>
<dd>
<dt><code>&#8211;add image</code></p>
<dd> Add a block device or virtual machine image. </p>
<p> The format of the disk image is auto-detected. To override this and force a particular format use the <i>&#8211;format=..</i> option.</p>
<dt><code>-a </code><font SIZE="-1"><code>URI</code></font></p>
<dd>
<dt><code>&#8211;add </code><font SIZE="-1"><code>URI</code></font></p>
<dd> Add a remote disk. See &#8220;<font SIZE="-1">ADDING REMOTE STORAGE&#8221;</font> in <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1).</p>
<dt><code>-c </code><font SIZE="-1"><code>URI</code></font></p>
<dd>
<dt><code>&#8211;connect </code><font SIZE="-1"><code>URI</code></font></p>
<dd> When used in conjunction with the <i>-d</i> option, this specifies the libvirt <font SIZE="-1">URI</font> to use. The default is to use the default libvirt connection.</p>
<dt><code>-d libvirt-domain</code></p>
<dd>
<dt><code>&#8211;domain libvirt-domain</code></p>
<dd> Add disks from the named libvirt domain. If the <i>&#8211;ro</i> option is also used, then any libvirt domain can be used. However in write mode, only libvirt domains which are shut down can be named here. </p>
<p> Domain UUIDs can be used instead of names.</p>
<dt><code>&#8211;dir-cache-timeout N</code></p>
<dd> Set the readdir cache timeout to <i>N</i> seconds, the default being 60 seconds. The readdir cache [actually, there are several semi-independent caches] is populated after a <i><a href="/docs/linux/man/2-readdir/">readdir</a></i>(2) call with the stat and extended attributes of the files in the directory, in anticipation that they will be requested soon after. </p>
<p> There is also a different attribute cache implemented by <font SIZE="-1">FUSE </font>(see the <font SIZE="-1">FUSE</font> option <i>-o attr_timeout</i>), but the <font SIZE="-1">FUSE</font> cache does not anticipate future requests, only cache existing ones.</p>
<dt><code>&#8211;echo-keys</code></p>
<dd> When prompting for keys and passphrases, guestfish normally turns echoing off so you cannot see what you are typing. If you are not worried about Tempest attacks and there is no one else in the room you can specify this flag to see what you are typing.</p>
<dt><code>&#8211;fd=FD</code></p>
<dd> Specify a pipe or eventfd file descriptor. When the mountpoint is ready to be used, guestmount writes a single byte to this file descriptor. This can be used in conjunction with <i>&#8211;no-fork</i> in order to run guestmount captive under another process.</p>
<dt><code>&#8211;format=raw|qcow2|..</code></p>
<dd>
<dt><code>&#8211;format</code></p>
<dd> The default for the <i>-a</i> option is to auto-detect the format of the disk image. Using this forces the disk format for <i>-a</i> options which follow on the command line. Using <i>&#8211;format</i> with no argument switches back to auto-detection for subsequent <i>-a</i> options. </p>
<p> If you have untrusted raw-format guest disk images, you should use this option to specify the disk format. This avoids a possible security problem with malicious guests (<font SIZE="-1">CVE-2010-3851</font>). See also &#8220;guestfs_add_drive_opts&#8221; in <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3).</p>
<dt><code>&#8211;fuse-help</code></p>
<dd> Display help on special <font SIZE="-1">FUSE</font> options (see <i>-o</i> below).</p>
<dt><code>&#8211;help</code></p>
<dd> Display brief help and exit.</p>
<dt><code>-i</code></p>
<dd>
<dt><code>&#8211;inspector</code></p>
<dd> Using <i><a href="/docs/linux/man/1-virt-inspector/">virt-inspector</a></i>(1) code, inspect the disks looking for an operating system and mount filesystems as they would be mounted on the real virtual machine.</p>
<dt><code>&#8211;keys-from-stdin</code></p>
<dd> Read key or passphrase parameters from stdin. The default is to try to read passphrases from the user by opening <i>/dev/tty</i>.</p>
<dt><code>&#8211;live</code></p>
<dd> Connect to a live virtual machine. (Experimental, see &#8220;<font SIZE="-1">ATTACHING TO RUNNING DAEMONS&#8221;</font> in <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3)).</p>
<dt><code>-m dev[:mountpoint[:options[:fstype]]</code></p>
<dd>
<dt><code>&#8211;mount dev[:mountpoint[:options[:fstype]]]</code></p>
<dd> Mount the named partition or logical volume on the given mountpoint <code>in the guest</code> (this has nothing to do with mountpoints in the host). </p>
<p> If the mountpoint is omitted, it defaults to <i>/</i>. You have to mount something on <i>/</i>. </p>
<p> The third (and rarely used) part of the mount parameter is the list of mount options used to mount the underlying filesystem. If this is not given, then the mount options are either the empty string or <tt>&quot;ro&quot;</tt> (the latter if the <i>&#8211;ro</i> flag is used). By specifying the mount options, you override this default choice. Probably the only time you would use this is to enable ACLs and/or extended attributes if the filesystem can support them: </p>
<pre>
 -m /dev/sda1:/:acl,user_xattr
</pre>
<p> The fourth part of the parameter is the filesystem driver to use, such as <tt>&quot;ext3&quot;</tt> or <tt>&quot;ntfs&quot;</tt>. This is rarely needed, but can be useful if multiple drivers are valid for a filesystem (eg: <tt>&quot;ext2&quot;</tt> and <tt>&quot;ext3&quot;</tt>), or if libguestfs misidentifies a filesystem.</p>
<dt><code>&#8211;no-fork</code></p>
<dd> Don&#8217;t daemonize (or fork into the background).</p>
<dt><code>-n</code></p>
<dd>
<dt><code>&#8211;no-sync</code></p>
<dd> By default, we attempt to sync the guest disk when the <font SIZE="-1">FUSE</font> mountpoint is unmounted. If you specify this option, then we don&#8217;t attempt to sync the disk. See the discussion of autosync in the <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3) manpage.</p>
<dt><code>-o option</code></p>
<dd>
<dt><code>&#8211;option option</code></p>
<dd> Pass extra options to <font SIZE="-1">FUSE.</font> </p>
<p> To get a list of all the extra options supported by <font SIZE="-1">FUSE,</font> use the command below. Note that only the <font SIZE="-1">FUSE </font><i>-o</i> options can be passed, and only some of them are a good idea. </p>
<pre>
 guestmount --fuse-help
</pre>
<p> Some potentially useful <font SIZE="-1">FUSE</font> options:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-o allow_other</code></p>
<dd> Allow other users to see the filesystem.</p>
<dt><code>-o attr_timeout=N</code></p>
<dd> Enable attribute caching by <font SIZE="-1">FUSE,</font> and set the timeout to <i>N</i> seconds.</p>
<dt><code>-o kernel_cache</code></p>
<dd> Allow the kernel to cache files (reduces the number of reads that have to go through the <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3) <font SIZE="-1">API</font>). This is generally a good idea if you can afford the extra memory usage.</p>
<dt><code>-o uid=N</code> <code>-o gid=N</code></p>
<dd> Use these options to map all UIDs and GIDs inside the guest filesystem to the chosen values.</p>
<dt><code>-o use_ino</code></p>
<dd> Preserve inode numbers from the underlying filesystem. </p>
<p> Without this option, <font SIZE="-1">FUSE</font> makes up its own inode numbers. The inode numbers you see in <i><a href="/docs/linux/man/2-stat/">stat</a></i>(2), <tt>&quot;ls -i&quot;</tt> etc aren&#8217;t the inode numbers of the underlying filesystem. </p>
<p> <code>Note</code> this option is potentially dangerous if the underlying filesystem consists of multiple mountpoints, as you may see duplicate inode numbers appearing through <font SIZE="-1">FUSE. </font> Use of this option can confuse some software.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;pid-file filename</code></p>
<dd> Write the <font SIZE="-1">PID</font> of the guestmount worker process to <tt>&quot;filename&quot;</tt>.</p>
<dt><code>-r</code></p>
<dd>
<dt><code>&#8211;ro</code></p>
<dd> Add devices and mount everything read-only. Also disallow writes and make the disk appear read-only to <font SIZE="-1">FUSE.</font> </p>
<p> This is highly recommended if you are not going to edit the guest disk. If the guest is running and this option is <i>not</i> supplied, then there is a strong risk of disk corruption in the guest. We try to prevent this from happening, but it is not always possible. </p>
<p> See also &#8220;<font SIZE="-1">OPENING DISKS FOR READ AND WRITE&#8221;</font> in <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1).</p>
<dt><code>&#8211;selinux</code></p>
<dd> This option is provided for backwards compatibility and does nothing.</p>
<dt><code>-v</code></p>
<dd>
<dt><code>&#8211;verbose</code></p>
<dd> Enable verbose messages from underlying libguestfs.</p>
<dt><code>-V</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd> Display the program version and exit.</p>
<dt><code>-w</code></p>
<dd>
<dt><code>&#8211;rw</code></p>
<dd> This changes the <i>-a</i>, <i>-d</i> and <i>-m</i> options so that disks are added and mounts are done read-write. </p>
<p> See &#8220;<font SIZE="-1">OPENING DISKS FOR READ AND WRITE&#8221;</font> in <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1).</p>
<dt><code>-x</code></p>
<dd>
<dt><code>&#8211;trace</code></p>
<dd> Trace libguestfs calls and entry into each <font SIZE="-1">FUSE</font> function. </p>
<p> This also stops the daemon from forking into the background (see <i>&#8211;no-fork</i>).</dl>
<h2>FILES</h2>
<dl>
<dt>$XDG_CONFIG_HOME/libguestfs/libguestfs-tools.conf</p>
<dd>
<dt>$HOME/.libguestfs-tools.rc</p>
<dd>
<dt>$XDG_CONFIG_DIRS/libguestfs/libguestfs-tools.conf</p>
<dd>
<dt>/etc/libguestfs-tools.conf</p>
<dd> This configuration file controls the default read-only or read-write mode (<i>&#8211;ro</i> or <i>&#8211;rw</i>). </p>
<p> See <i><a href="/docs/linux/man/5-libguestfs-tools-conf/">libguestfs-tools.conf</a></i>(5).</dl>
<h2>EXIT STATUS</h2>
<p> This program returns 0 if successful, or non-zero if there was an error.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-guestunmount/">guestunmount</a></i>(1), <i><a href="/docs/linux/man/1-fusermount/">fusermount</a></i>(1), <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1), <i><a href="/docs/linux/man/1-virt-inspector/">virt-inspector</a></i>(1), <i><a href="/docs/linux/man/1-virt-cat/">virt-cat</a></i>(1), <i><a href="/docs/linux/man/1-virt-edit/">virt-edit</a></i>(1), <i><a href="/docs/linux/man/1-virt-tar/">virt-tar</a></i>(1), <i><a href="/docs/linux/man/5-libguestfs-tools-conf/">libguestfs-tools.conf</a></i>(5), &#8220;<font SIZE="-1">MOUNT LOCAL&#8221;</font> in <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3), <a rel="nofollow" href="http://libguestfs.org/,">http://libguestfs.org/,</a> <a rel="nofollow" href="http://fuse.sf.net/.">http://fuse.sf.net/.</a></p>
<h2>AUTHORS</h2>
<p> Richard W.M. Jones (<tt>&quot;rjones at redhat dot com&quot;</tt>)</p>
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
<dt><a href="#lbAL">OPTIONS</a></p>
<dd>
<dt><a href="#lbAM">FILES</a></p>
<dd>
<dt><a href="#lbAN">EXIT STATUS</a></p>
<dd>
<dt><a href="#lbAO">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAP">AUTHORS</a></p>
<dd>
<dt><a href="#lbAQ">COPYRIGHT</a></p>
<dd>
<dt><a href="#lbAR">LICENSE</a></p>
<dd>
<dt><a href="#lbAS">BUGS</a></p>
<dd></dl>
