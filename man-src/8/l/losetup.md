---
title: "losetup(8)"
name: "losetup"
section: "8"
letter: "l"
url: "/docs/linux/man/8-losetup/"
description: "losetup – set up and control loop devices"
---

<p>losetup &#8211; set up and control loop devices</p>
<h2>Synopsis</h2>
<p>Get info: </p>
<p> <code>losetup</code> [<i>loopdev</i>] </p>
<p> <code>losetup</code> <code>-l</code> [<code>-a</code>] </p>
<p> <code>losetup</code> <code>-j</code> <i>file</i> [<code>-o</code> <i>offset</i>] </p>
<p> Detach a loop device: </p>
<p> <code>losetup</code> <code>-d</code> <i>loopdev</i> &#8230; </p>
<p> Detach all associated loop devices: </p>
<p> <code>losetup</code> <code>-D</code> </p>
<p> Set up a loop device: </p>
<p> <code>losetup</code> [<code>-o</code> <i>offset</i>] [<code>&#8211;sizelimit</code> <i>size</i>] [<code>&#8211;sector-size</code> <i>size</i>] [<code>-Pr</code>] [<code>&#8211;show</code>] <code>-f</code> <i>loopdev file</i> </p>
<p> Resize a loop device: </p>
<p> <code>losetup</code> <code>-c</code> <i>loopdev</i></p>
<h2>Description</h2>
<p><code>losetup</code> is used to associate loop devices with regular files or block devices, to detach loop devices, and to query the status of a loop device. If only the <i>loopdev</i> argument is given, the status of the corresponding loop device is shown. If no option is given, all loop devices are shown. </p>
<p> Note that the old output format (i.e., <code>losetup -a</code>) with comma-delimited strings is deprecated in favour of the <code>&#8211;list</code> output format. </p>
<p> It&#8217;s possible to create more independent loop devices for the same backing file. <code>This setup may be dangerous, can cause data loss, corruption and overwrites.</code> Use <code>&#8211;nooverlap</code> with <code>&#8211;find</code> during setup to avoid this problem. </p>
<p> The loop device setup is not an atomic operation when used with <code>&#8211;find</code>, and <code>losetup</code> does not protect this operation by any lock. The number of attempts is internally restricted to a maximum of 16. It is recommended to use for example flock1 to avoid a collision in heavily parallel use cases.</p>
<h2>Options</h2>
<p>The <i>size</i> and <i>offset</i> arguments may be followed by the multiplicative suffixes KiB (=1024), MiB (=1024*1024), and so on for GiB, TiB, PiB, EiB, ZiB and YiB (the &quot;iB&quot; is optional, e.g., &quot;K&quot; has the same meaning as &quot;KiB&quot;) or the suffixes KB (=1000), MB (=1000*1000), and so on for GB, TB, PB, EB, ZB and YB. </p>
<p> <code>-a</code>, <code>&#8211;all</code></p>
<dl>
<dd>Show the status of all loop devices. Note that not all information is accessible for non-root users. See also <code>&#8211;list</code>. The old output format (as printed without <code>&#8211;list)</code> is deprecated.</dl>
<p> <code>-d</code>, <code>&#8211;detach</code> <i>loopdev</i>&#8230;</p>
<dl>
<dd>Detach the file or device associated with the specified loop device(s). Note that since Linux v3.7 kernel uses &quot;lazy device destruction&quot;. The detach operation does not return <code>EBUSY</code> error anymore if device is actively used by system, but it is marked by autoclear flag and destroyed later.</dl>
<p> <code>-D</code>, <code>&#8211;detach-all</code></p>
<dl>
<dd>Detach all associated loop devices.</dl>
<p> <code>-f</code>, <code>&#8211;find</code> [<i>file</i>]</p>
<dl>
<dd>Find the first unused loop device. If a <i>file</i> argument is present, use the found device as loop device. Otherwise, just print its name.</dl>
<p> <code>&#8211;show</code></p>
<dl>
<dd>Display the name of the assigned loop device if the <code>-f</code> option and a <i>file</i> argument are present.</dl>
<p> <code>-L</code>, <code>&#8211;nooverlap</code></p>
<dl>
<dd>Check for conflicts between loop devices to avoid situation when the same backing file is shared between more loop devices. If the file is already used by another device then re-use the device rather than a new one. The option makes sense only with <code>&#8211;find</code>.</dl>
<p> <code>-j</code>, <code>&#8211;associated</code> <i>file</i> [<code>-o</code> <i>offset</i>]</p>
<dl>
<dd>Show the status of all loop devices associated with the given <i>file</i>.</dl>
<p> <code>-o</code>, <code>&#8211;offset</code> <i>offset</i></p>
<dl>
<dd>The data start is moved <i>offset</i> bytes into the specified file or device. The <i>offset</i> may be followed by the multiplicative suffixes; see above.</dl>
<p> <code>&#8211;sizelimit</code> <i>size</i></p>
<dl>
<dd>The data end is set to no more than <i>size</i> bytes after the data start. The <i>size</i> may be followed by the multiplicative suffixes; see above.</dl>
<p> <code>-b</code>, <code>&#8211;sector-size</code> <i>size</i></p>
<dl>
<dd>Set the logical sector size of the loop device in bytes (since Linux 4.14). The option may be used when create a new loop device as well as stand-alone command to modify sector size of the already existing loop device.</dl>
<p> <code>-c</code>, <code>&#8211;set-capacity</code> <i>loopdev</i></p>
<dl>
<dd>Force the loop driver to reread the size of the file associated with the specified loop device.</dl>
<p> <code>-P</code>, <code>&#8211;partscan</code></p>
<dl>
<dd>Force the kernel to scan the partition table on a newly created loop device. Note that the partition table parsing depends on sector sizes. The default is sector size is 512 bytes, otherwise you need to use the option <code>&#8211;sector-size</code> together with <code>&#8211;partscan</code>.</dl>
<p> <code>-r</code>, <code>&#8211;read-only</code></p>
<dl>
<dd>Set up a read-only loop device.</dl>
<p> <code>&#8211;direct-io</code>[<code>=on</code>|<code>off</code>]</p>
<dl>
<dd>Enable or disable direct I/O for the backing file. The optional argument can be either <code>on</code> or <code>off</code>. If the argument is omitted, it defaults to <code>off</code>.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dd>Verbose mode.</dl>
<p> <code>-l</code>, <code>&#8211;list</code></p>
<dl>
<dd>If a loop device or the <code>-a</code> option is specified, print the default columns for either the specified loop device or all loop devices; the default is to print info about all devices. See also <code>&#8211;output</code>, <code>&#8211;noheadings</code>, <code>&#8211;raw</code>, and <code>&#8211;json</code>.</dl>
<p> <code>-O</code>, <code>&#8211;output</code> <i>column</i>[,<i>column</i>]&#8230;</p>
<dl>
<dd>Specify the columns that are to be printed for the <code>&#8211;list</code> output. Use <code>&#8211;help</code> to get a list of all supported columns.</dl>
<p> <code>&#8211;output-all</code></p>
<dl>
<dd>Output all available columns.</dl>
<p> <code>-n</code>, <code>&#8211;noheadings</code></p>
<dl>
<dd>Don&#8217;t print headings for <code>&#8211;list</code> output format.</dl>
<p> <code>&#8211;raw</code></p>
<dl>
<dd>Use the raw <code>&#8211;list</code> output format.</dl>
<p> <code>-J</code>, <code>&#8211;json</code></p>
<dl>
<dd>Use JSON format for <code>&#8211;list</code> output.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dd>Display version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display help text and exit.</dl>
<h2>Encryption</h2>
<p><code>Cryptoloop is no longer supported in favor of dm-crypt.</code> For more details see <code><a href="/docs/linux/man/8-cryptsetup/">cryptsetup</a></code>(8).</p>
<h2>Exit Status</h2>
<p><code>losetup</code> returns 0 on success, nonzero on failure. When <code>losetup</code> displays the status of a loop device, it returns 1 if the device is not configured and 2 if an error occurred which prevented determining the status of the device.</p>
<h2>Notes</h2>
<p>Since version 2.37 <code>losetup</code> uses <code>LOOP_CONFIGURE</code> ioctl to setup a new loop device by one ioctl call. The old versions use <code>LOOP_SET_FD</code> and <code>LOOP_SET_STATUS64</code> ioctls to do the same.</p>
<h2>Environment</h2>
<p>LOOPDEV_DEBUG=all</p>
<dl>
<dd>enables debug output.</dl>
<h2>Files</h2>
<p><i>/dev/loop[0..N]</i></p>
<dl>
<dd>loop block devices</dl>
<p> <i>/dev/loop-control</i></p>
<dl>
<dd>loop control device</dl>
<h2>Example</h2>
<p>The following commands can be used as an example of using the loop device. </p>
<dl>
<dd>
<pre># dd if=/dev/zero of=~/file.img bs=1024k count=10
# losetup --find --show ~/file.img
/dev/loop0
# mkfs -t ext2 /dev/loop0
# mount /dev/loop0 /mnt
...
# umount /dev/loop0
# losetup --detach /dev/loop0</pre>
</dl>
<h2>Authors</h2>
<p>based on the original version from</p>
<h2>Reporting Bugs</h2>
<p>For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>Availability</h2>
<p>The <code>losetup</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;.</p>
