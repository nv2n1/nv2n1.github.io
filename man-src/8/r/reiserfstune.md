---
title: "reiserfstune(8)"
name: "reiserfstune"
section: "8"
letter: "r"
url: "/docs/linux/man/8-reiserfstune/"
description: "reiserfstune – The tunning tool for the ReiserFS filesystem."
---

<p>reiserfstune &#8211; The tunning tool for the ReiserFS filesystem.</p>
<h2>Synopsis</h2>
<p><code>reiserfstune</code> [ <code>-f</code> ] [ <code>-h</code> | <code>&#8211;help</code> ] [ <code>-j</code> | <code>&#8211;journal-device</code> <i>FILE</i> ] [ <code>&#8211;no-journal-available</code> ] [ <code>&#8211;journal-new-device</code> <i>FILE</i> ] [ <code>&#8211;make-journal-standard</code> ] [ <code>-s</code> | <code>&#8211;journal-new-size</code> <i>N</i> ] [ <code>-o</code> | <code>&#8211;journal-new-offset</code> <i>N</i> ] [ <code>-t</code> | <code>&#8211;max-transaction-size</code> <i>N</i> ] [ <code>-b</code> | <code>&#8211;add-badblocks</code> <i>file</i> ] [ <code>-B</code> | <code>&#8211;badblocks</code> <i>file</i> ] [ <code>-u</code> | <code>&#8211;uuid </code><i>UUID</i> ] [ <code>-l</code> | <code>&#8211;label </code><i>LABEL</i> ] [ <code>-c</code> | <code>&#8211;check-interval </code><i>interval-in-days</i> ] [ <code>-C</code> | <code>&#8211;time-last-checked </code><i>timestamp</i> ] [ <code>-m</code> | <code>&#8211;max-mnt-count </code><i>count</i> ] [ <code>-M</code> | <code>&#8211;mnt-count </code><i>count</i> ] <i>device</i></p>
<h2>Description</h2>
<p><code>reiserfstune</code> is used for tuning the ReiserFS. It can change two journal parameters (the journal size and the maximum transaction size), and it can move the journal&#8217;s location to a new specified block device. (The old ReiserFS&#8217;s journal may be kept unused, or discarded at the user&#8217;s option.) Besides that <code>reiserfstune</code> can store the bad block list to the ReiserFS and set UUID and LABEL. Note: At the time of writing the relocated journal was implemented for a special release of ReiserFS, and was not expected to be put into the mainstream kernel until approximately Linux 2.5. This means that if you have the stock kernel you must apply a special patch. Without this patch the kernel will refuse to mount the newly modified file system. We will charge $25 to explain this to you if you ask us why it doesn&#8217;t work. </p>
<p> Perhaps the most interesting application of this code is to put the journal on a solid state disk.</p>
<dl>
<dt><i>device</p>
<dd>is the special file corresponding to the newly specified block device (e.g /dev/hdXX for IDE disk partition or /dev/sdXX for the SCSI disk partition).</dl>
<p> </i></p>
<h2>Options</h2>
<dl>
<dt><code>-h</code> | <code>&#8211;help</code></p>
<dd>Print usage information and exit.</p>
<dt><code>-j</code> | <code>&#8211;journal-device</code> <i>FILE</p>
<dd>FILE</i> is the file name of the block device the file system has the current journal (the one prior to running reiserfstune) on. This option is required when the journal is already on a separate device from the main data device (although it can be avoided with <code>&#8211;no-journal-available</code>). If you don&#8217;t specify journal device by this option, reiserfstune suppose that journal is on main device.</p>
<dt><code>&#8211;no-journal-available</p>
<dd>allows reiserfstune</code> to continue when the current journal&#8217;s block device is no longer available. This might happen if a disk goes bad and you remove it (and run fsck).</p>
<dt><code>&#8211;journal-new-device </code><i>FILE</p>
<dd>FILE</i> is the file name of the block device which will contain the new journal for the file system. If you don&#8217;t specify this, reiserfstune supposes that journal device remains the same.<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt></p>
<dt><code> -s</code> | <code>&#8211;journal-new-size </code><i>N</p>
<dd>N</i> is the size parameter for the new journal. When journal is to be on a separate device &#8211; its size defaults to number of blocks that device has. When journal is to be on the same device as the filesytem &#8211; its size defaults to amount of blocks allocated for journal by <i>mkreiserfs</i> when it created the filesystem. Minimum is 513 for both cases.</p>
<dt><code> -o</code> | <code>&#8211;journal-new-offset </code><i>N</p>
<dd>N</i> is an offset in blocks where journal will starts from when journal is to be on a separate device. Default is 0. Has no effect when journal is to be on the same device as the filesystem. Most users have no need to use this feature. It can be used when you want the journals from multiple filesystems to reside on the same device, and you don&#8217;t want to or cannot partition that device.</p>
<dt><code> -t</code> | <code>&#8211;maximal-transaction-size </code><i>N</p>
<dd>N</i> is the maximum transaction size parameter for the new journal. The default, and max possible, value is 1024 blocks. It should be less than half the size of the journal. If specifed incorrectly, it will be adjusted.</p>
<dt><code> -b</code> | <code>&#8211;add-badblocks</code> <i>file</i></p>
<dd><i>File</i> is the file name of the file that contains the list of blocks to be marked as bad on the fs. The list is added to the fs list of bad blocks.</p>
<dt><code> -B</code> | <code>&#8211;badblocks</code> <i>file</i></p>
<dd><i>File</i> is the file name of the file that contains the list of blocks to be marked as bad on the fs. The bad block list on the fs is cleared before the list specified in the <i>File</i> is added to the fs.</p>
<dt><code>-f</code> | <code>&#8211;force</code></p>
<dd>Normally <code>reiserfstune</code> will refuse to change a journal of a file system that was created before this journal relocation code. This is because if you change the journal, you cannot go back (without special option <code>&#8211;make-journal-standard</code>) to an old kernel that lacks this feature and be able to use your filesytem. This option forces it to do that. Specified more than once it allows to avoid asking for confirmation.</p>
<dt><code>&#8211;make-journal-standard</code></p>
<dd>As it was mentioned above, if your file system has non-standard journal, it can not be mounted on the kernel without journal relocation code. The thing can be changed, the only condition is that there is reserved area on main device of the standard journal size 8193 blocks (it will be so for instance if you convert standard journal to non-standard). Just specify this option when you relocate journal back, or without relocation if you already have it on main device.</p>
<dt><code>-u</code> | <code>&#8211;uuid </code><i>UUID</i></p>
<dd>Set the universally unique identifier (<code> UUID </code>) of the filesystem to <i>UUID</i> (see also <code><a href="/docs/linux/man/8-uuidgen/">uuidgen</a>(8)</code>). The format of the UUID is a series of hex digits separated by hypthens, like this: &quot;c1b9d5a2-f162-11cf-9ece-0020afc76f16&quot;.</p>
<dt><code>-l</code> | <code>&#8211;label </code><i>LABEL</i></p>
<dd>Set the volume label of the filesystem. <i>LABEL</i> can be at most 16 characters long; if it is longer than 16 characters, reiserfstune will truncate it.</p>
<dt><code>-c</code> | <code>&#8211;check-interval </code><i>interval-in-days</i></p>
<dd>Adjust the maximal time between two filesystem checks. A value of &quot;disable&quot; will disable the time-dependent checking. A value of &quot;default&quot; will restore the compile-time default. </p>
<p> It is strongly recommended that either <code>-m</code> (mount-count dependent) or <code>-c</code> (time-dependent) checking be enabled to force periodic full <code><a href="/docs/linux/man/8-fsck-reiserfs/">fsck.reiserfs</a>(8)</code> checking of the filesystem. Failure to do so may lead to filesystem corruption (due to bad disks, cables, memory, or kernel bugs) going unnoticed, ultimately resulting in data loss or corruption.</p>
<dt><code>-C</code> | <code>&#8211;time-last-checked </code><i>timestamp</i></p>
<dd>Set the time the filesystem was last checked using fsck.reiserfs. This can be useful in scripts which use a Logical Volume Manager to make a consistent snapshot of a filesystem, and then check the filesystem during off hours to make sure it hasn&#8217;t been corrupted due to hardware problems, etc. If the filesystem was clean, then this option can be used to set the last checked time on the original filesystem. The format of time-last-checked is the international date format, with an optional time specifier, i.e. YYYYMMDD[HH[MM[SS]]]. The keyword <code>now</code> is also accepted, in which case the last checked time will be set to the current time.</p>
<dt><code>-m</code> | <code>&#8211;max-mnt-count </code><i>max-mount-count</i></p>
<dd>Adjust the number of mounts after which the filesystem will be checked by <code><a href="/docs/linux/man/8-fsck-reiserfs/">fsck.reiserfs</a>(8).</code> If max-mount-count is &quot;disable&quot;, the number of times the filesystem is mounted will be disregarded by <code><a href="/docs/linux/man/8-fsck-reiserfs/">fsck.reiserfs</a>(8)</code> and the kernel. A value of &quot;default&quot; will restore the compile-time default. </p>
<p> Staggering the mount-counts at which filesystems are forcibly checked will avoid all filesystems being checked at one time when using journaled filesystems. </p>
<p> You should strongly consider the consequences of disabling mount-count-dependent checking entirely. Bad disk drives, cables, memory, and kernel bugs could all corrupt a filesystem without marking the filesystem dirty or in error. If you are using journaling on your filesystem, your filesystem will never be marked dirty, so it will not normally be checked. A filesys‐ tem error detected by the kernel will still force an fsck on the next reboot, but it may already be too late to prevent data loss at that point. </p>
<p> This option requires a kernel which supports incrementing the count on each mount. This feature has not been incorporated into kernel versions older than 2.6.25. </p>
<p> See also the <code>-c</code> option for time-dependent checking.</p>
<dt><code>-M</code> | <code>&#8211;mnt-count </code><i>count</i></p>
<dd>Set the number of times the filesystem has been mounted. If set to a greater value than the max-mount-counts parameter set by the <code>-m</code> option, <code><a href="/docs/linux/man/8-fsck-reiserfs/">fsck.reiserfs</a>(8)</code> will check the filesystem at the next reboot.</dl>
<h2>Possible Scenarios Of Using Reiserfstune:</h2>
<p>1. You have ReiserFS on /dev/hda1, and you wish to have it working with its journal on the device /dev/journal </p>
<pre><dl><dt><dd>boot kernel patched with special &quot;relocatable journal support&quot; patch
reiserfstune /dev/hda1 --journal-new-device /dev/journal -f
mount /dev/hda1 and use.
You would like to change max transaction size to 512 blocks
reiserfstune -t 512 /dev/hda1
You would like to use your file system on another kernel that doesn't 
contain relocatable journal support.
umount /dev/hda1
reiserfstune /dev/hda1 -j /dev/journal --journal-new-device /dev/hda1 --make-journal-standard
mount /dev/hda1 and use.
</dl>
2. You would like to have ReiserFS on /dev/hda1 and to be able to
switch between different journals including journal located on the
device containing the filesystem.
<dl><dt><dd>boot kernel patched with special &quot;relocatable journal support&quot; patch
mkreiserfs /dev/hda1
you got solid state disk (perhaps /dev/sda, they typically look like scsi disks)
reiserfstune --journal-new-device /dev/sda1 -f /dev/hda1
Your scsi device dies, it is three in the morning, you have an extra IDE device
lying around
reiserfsck --no-journal-available /dev/hda1
or
reiserfsck --rebuild-tree --no-journal-available /dev/hda1
reiserfstune --no-journal-available --journal-new-device /dev/hda1 /dev/hda1
using /dev/hda1 under patched kernel
</dl></pre>
<h2>Author</h2>
<p>This version of <code>reiserfstune</code> has been written by Vladimir Demidov &lt;vova [at] namesys.com&gt; and Edward Shishkin &lt;edward [at] namesys.com&gt;.</p>
<h2>Bugs</h2>
<p>Please report bugs to the ReiserFS developers &lt;reiserfs-devel [at] vger.kerne.org&gt;, providing as much information as possible&#8211;your hardware, kernel, patches, settings, all printed messages; check the syslog file for any related information.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-reiserfsck/">reiserfsck</a></code>(8), <code><a href="/docs/linux/man/8-debugreiserfs/">debugreiserfs</a></code>(8), <code><a href="/docs/linux/man/8-mkreiserfs/">mkreiserfs</a></code>(8) </p>
