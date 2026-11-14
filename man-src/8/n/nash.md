---
title: "nash(8)"
name: "nash"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nash/"
description: "nash – script interpretor to interpret linuxrc images"
---

<p>nash &#8211; script interpretor to interpret linuxrc images</p>
<h2>Synopsis</h2>
<p><code>nash</code> [&#8211;quiet] [&#8211;force] <i>script</i> </p>
<h2>Description</h2>
<p><code>nash</code> is a very simple script interpretor designed to be as small as possible. It is primarily designed to run simple linuxrc scripts on an initrd image. Arguments to commands may be enclosed in either single or double quotes to allow spaces to be included in the arguments. Spaces outside of quotations always delineate arguments, and no backslash escaping is supported. Additionally, if nash is invoked as <code>modprobe</code>, it will immediately exit with a return code of zero. This is to allow initrd&#8217;s to prevent some extraneous kernel error messages during startup. There are two types of commands, built in and external. External commands are run from the filesystem via execve(). If commands names are given without a path, nash will search it&#8217;s builtin PATH, which is /usr/bin, /bin, /sbin, /usr/sbin. Currently, <code>nash</code> supports the following built in commands.</p>
<dl>
<dt><code>access -[r][w][x][f] </code><i>path</i></p>
<dd>Tells whether the current user has sufficient permissions to read, write, or execture <i>path</i>, or if the file exists (see <code><a href="/docs/linux/man/2-access/">access</a>(2)</code> for more information).</p>
<dt><code>echo [item]* [&gt; </code><i>filename</i>]</p>
<dd>Echos the text strings given to a file, with a space in between each item. The output may be optionally redirected to a file. <code>exec</code> <i>&lt;command&gt;</i> The command given is execed, overlaying the nash process.</p>
<dt><code>find </code><i>dir</i> -name <i>name</i></p>
<dd>Display the path to files named <i>name</i> in or below directory <i>dir</i>. This is a <code>very</code> limited implementation of <a href="/docs/linux/man/1-find/">find</a>(1).</p>
<dt><code>losetup </code><i>/dev/loopdev</i> <i>file</i></p>
<dd>Binds <i>file</i> to the loopback device <i>/dev/loopdev</i>. See <code><a href="/docs/linux/man/8-losetup/">losetup</a>(8)</code> for information on loopback devices.</p>
<dt><code>mkdevices</code> <i>path</i></p>
<dd>Creates device files for all of the block devices listed in <code>/proc/partitions</code> in the directory specfied by <i>path</i>.</p>
<dt><code>mkdir</code> <i>[-p]</i> <i>path</i></p>
<dd>Creates the directory <i>path</i>. If <i>-p</i> is specified, this command will not complain if the directory exists. Note this is a subset of the standard <code>mkdir</code> <i>-p</i> behavior.</p>
<dt><code>mknod</code> <i>path</i> <i>[c|b]</i> <i>major</i> <i>minor</i></p>
<dd>Creates a device inode for <i>path</i>. This is identical to <code><a href="/docs/linux/man/1-mkdev/">mkdev</a></code>(1) which the exceptions that it will not create named pipes and if the directories in <i>path</i> do not exist they will be automatically created.</p>
<dt><code>mkdmnod</code></p>
<dd>Creates a device inode for the device mapper control inode as <i>/dev/mapper/control</i>. If it already exists with the correct major/minor, it will not be recreated.</p>
<dt><code>mkrootdev </code><i>path</i></p>
<dd>Makes <i>path</i> a block inode for the device which should be mounted as root. To determine this device nash uses the device suggested by the root= kernel command line argument (if root=LABEL is used devices are probed to find one with that label). If no root= argument is available, /proc/sys/kernel/real-root-dev provides the device number.</p>
<dt><code>mount </code><i>[&#8211;ro]</i> -o <i>opts</i> -t <i>type</i> <i>device</i> <i>mntpoint</i></p>
<dd>Mounts a filesystem. It does not support NFS, and it must be used in the form given above (arguments must go first). If <i>device</i> is of the form <code>LABEL=</code><i>foo</i> the devices listed in /fB/proc/partitions will be searched, and the first device with a volume label of <i>foo</i> will be mounted. Normal <code><a href="/docs/linux/man/2-mount/">mount</a></code>(2) options are supported, and <code>&#8211;ro</code> will mount the filesystem read only for compatibility with older versions of nash. The <code>defaults</code> mount option is silently ignored.</p>
<dt><code>pivot_root </code><i>newrootpath</i> <i>oldrootpath</i></p>
<dd>Makes the filesystem mounted at <i>newrootpath</i> the new root filesystem, and mounts the current root filesystem as <i>oldrootpath</i>.</p>
<dt><code>readlink </code><i>path</i></p>
<dd>Displays the value of the symbolic link <i>path</i>.</p>
<dt><code>raidautorun </code><i>mddevice</i></p>
<dd>Runs raid autodetection on all raid-typed partitions. <i>mddevice</i> must be a raid device (any will do).</p>
<dt><code>setquiet</code></p>
<dd>Cause any later echos in this script to not be displayed.</p>
<dt><code>showlabels</code></p>
<dd>Display a table of devices, their filesystem labels, and their uuids.</p>
<dt><code>sleep </code><i>num</i></p>
<dd>Sleep for <i>num</i> seconds</p>
<dt><code>switchroot </code><i>newrootpath</i></p>
<dd>Makes the filesystem mounted at <i>newrootpath</i> the new root filesystem by moving the mountpoint. This will only work in 2.6 or later kernels.</p>
<dt><code>umount </code><i>path</i></p>
<dd>Unmounts the filesystem mounted at <i>path</i>. </p>
<h2>Return Value</h2>
<p>Returns 0 is the last command succeeded or 1 if it failed. </p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;force</code></p>
<dd>Allows <code>force</code> really execute the script, even though <code>nash</code> doesn&#8217;t appear to be running from an initrd image. </p>
</dl>
<h2>Bugs</h2>
<p>Probably many. <code>nash</code> is not a shell, and it shouldn&#8217;t be thought of as one. It isn&#8217;t entirely different from a shell, but that&#8217;s mostly by accident. </p>
