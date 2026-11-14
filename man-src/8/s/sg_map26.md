---
title: "sg_map26(8)"
name: "sg_map26"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sg_map26/"
description: "sg_map26 – map SCSI generic (sg) device to corresponding device names"
---

<p>sg_map26 &#8211; map SCSI generic (sg) device to corresponding device names</p>
<h2>Synopsis</h2>
<p><code>sg_map26</code> [<i>&#8211;dev_dir=DIR</i>] [<i>&#8211;given_is=</i>0|1] [<i>&#8211;help</i>] [<i>&#8211;result=</i>0|1|2|3] [<i>&#8211;symlink</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] <i>DEVICE</i></p>
<h2>Description</h2>
<p>Maps a special file (block or char) associated with a SCSI device to the corresponding SCSI generic (sg) device, or vice versa. Can also be given a sysfs file, for example &#8216;/sys/block/sda&#8217; or &#8216;/sys/block/sda/dev&#8217;. </p>
<p> Rather than map to or from a sg device, the sysfs file name matching a given device special file (or vice versa) can be requested. This is done with &#8216;&#8211;result=2&#8217; and &#8216;&#8211;result=3&#8217;. This feature works on ATA devices (e.g. &#8216;dev/hdc&#8217;) as well as SCSI devices. </p>
<p> In this utility, &quot;mapped&quot; refers to finding the relationship between a SCSI generic (sg) node and the higher level SCSI device name; or vice versa. For example &#8216;/dev/sg0&#8217; may &quot;map&quot; to &#8216;/dev/sda&#8217;. Mappings may not exist, if a relevant module is not loaded, for example. Also there are SCSI devices that can only be accessed via a sg node (e.g. SAF-TE and some SES devices). </p>
<p> In this utility, &quot;matching&quot; refers to different representations of the same device accessed via the same driver. For example, &#8216;/dev/hdc&#8217; and &#8216;/sys/block/hdc&#8217; usually refer to the same device and thus would be considered matching. A related example is that &#8216;/dev/cdrom&#8217; and &#8216;/dev/hdc&#8217; are also considered matching if &#8216;/dev/cdrom&#8217; is a symlink to &#8216;/dev/hdc&#8217;.</p>
<h2>Options</h2>
<p>Arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-d</code>, <code>&#8211;dev_dir</code>=<i>DIR</i></p>
<dd>where <i>DIR</i> is the directory to search for resultant device special files in (or symlinks to same). Only active when &#8216;&#8211;result=0&#8217; (the default) or &#8216;&#8211;result=2&#8217;. If this option is not given and <i>DEVICE</i> is a device special file then the directory part of <i>DEVICE</i> is assumed. If this option is not given and <i>DEVICE</i> is a sysfs name, then if necessary &#8216;/dev&#8217; is assumed as the directory.</p>
<dt><code>-g</code>, <code>&#8211;given_is</code>=0 | 1</p>
<dd>specifies the <i>DEVICE</i> is either a device special file (when the argument is 0), or a sysfs &#8216;dev&#8217; file (when the argument is 1). The parent directory of a sysfs &#8216;dev&#8217; file is also accepted (e.g. either &#8216;/sys/block/sda/dev&#8217; or &#8216;/sys/block/sda&#8217; are accepted). Usually there is no need to give this option since this utility first checks for special files (or symlinks to special files) and if not, assumes it has been given a sysfs &#8216;dev&#8217; file (or its parent). Generates an error if given and disagrees with variety of <i>DEVICE</i>.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>output the usage message then exit.</p>
<dt><code>-r</code>, <code>&#8211;result</code>=0 | 1 | 2 | 3</p>
<dd>specifies what variety of file (or files) that this utility tries to find. The default is a &quot;mapped&quot; device special file, when the argument is 0. When the argument is 1, this utility tries to find the &quot;mapped&quot; sysfs node name. When the argument is 2, this utility tries to find the &quot;matching&quot; device special file. When the argument is 3, this utility tries to find the &quot;matching&quot; sysfs node name.</p>
<dt><code>-s</code>, <code>&#8211;symlink</code></p>
<dd>when a device special file is being sought (i.e. when &#8216;&#8211;result=0&#8217; (the default) or &#8216;&#8211;result=2&#8217;) then also look for symlinks to that device special file in the same directory.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase the level of verbosity, (i.e. debug output).</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print the version string and then exit.</dl>
<h2>Notes</h2>
<p>This utility is designed for the Linux 2.6 (and later) kernel series. It uses special file major and minor numbers (and whether the special is block or character) together with sysfs to do its mapping or matching. In the absence of any other information, device special files are assumed to be in the &#8216;/dev&#8217; directory while sysfs is assumed to be mounted at &#8216;/sys&#8217;. Device names in sysfs are predictable, given the corresponding major and minor number of the device. However, due to udev rules, the name of device special files can be anything the user desires (e.g. &#8216;/dev/sda&#8217; could be named &#8216;/dev/my_boot_disk&#8217;). When trying to find a resultant device special file, this utility uses the major and minor numbers (and whether a block or char device is sought) to search the device directory. </p>
<p> This utility only shows one relationship at a time. To get an overview of all SCSI devices, with special file names and optionally the &quot;mapped&quot; sg device name, see the lsscsi utility.</p>
<h2>Examples</h2>
<p>Assume sg2 maps to sdb while dvd, cdrom and hdc are all matching.<br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>sg_map26&nbsp;<wbr>/dev/sg2 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>/dev/sdb<br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>sg_map26&nbsp;<wbr>/dev/sdb </p>
<p>&nbsp;<wbr>&nbsp;<wbr>/dev/sg2 </p>
<pre><code># sg_map26 --result=0 /dev/sdb

/dev/sg2
# sg_map26 --result=3 /dev/sdb

/sys/block/sda
# sg_map26 --result=1 /dev/sdb

/sys/class/scsi_generic/sg0</code></pre>
<p> Now look at &#8216;/dev/hdc&#8217; and friends<br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>sg_map26&nbsp;<wbr>/dev/hdc </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&lt;error: a hd device does not map to a sg device&gt; </p>
<pre><code># sg_map26 --result=3 /dev/hdc

/sys/block/hdc
# sg_map26 --result=2 /dev/hdc

/dev/hdc
# sg_map26 --result=2 --symlink /dev/hdc

/dev/cdrom

/dev/dvd

/dev/hdc
# sg_map26 --result=2 --symlink /sys/block/hdc

/dev/cdrom

/dev/dvd

/dev/hdc</code></pre>
<h2>Exit Status</h2>
<p>The exit status of sg_map26 is 0 when it is successful. Otherwise see the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page.</p>
<h2>Authors</h2>
<p>Written by Douglas Gilbert.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2005-2012 Douglas Gilbert<br />
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-udev/">udev</a>(7), lsscsi(lsscsi)</code> </p>
