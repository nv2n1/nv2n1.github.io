---
title: "reiserfsck(8)"
name: "reiserfsck"
section: "8"
letter: "r"
url: "/docs/linux/man/8-reiserfsck/"
description: "reiserfsck – The checking tool for the ReiserFS filesystem."
---

<p>reiserfsck &#8211; The checking tool for the ReiserFS filesystem.</p>
<h2>Synopsis</h2>
<p><code>reiserfsck </code> [ <code>-aprVy</code> ] [ <code>&#8211;rebuild-sb</code> | <code>&#8211;check</code> | <code>&#8211;fix-fixable</code> | <code>&#8211;rebuild-tree</code> | <code>&#8211;clean-attributes</code> ] [ <code>-j</code> | <code>&#8211;journal</code> <i>device</i> ] [ <code>-z</code> | <code>&#8211;adjust-size</code> ] [ <code>-n</code> | <code>&#8211;nolog</code> ] [ <code>-B</code> | <code>&#8211;badblocks </code><i>file</i> ] [ <code>-l</code> | <code>&#8211;logfile </code><i>file</i> ] [ <code>-q</code> | <code>&#8211;quiet</code> ] [ <code>-y</code> | <code>&#8211;yes</code> ] [ <code>-f</code> | <code>&#8211;force</code> ] [ <code>-S</code> | <code>&#8211;scan-whole-partition</code> ] [ <code>&#8211;no-journal-available</code> ] <i>device</i></p>
<h2>Description</h2>
<p><code>Reiserfsck</code> searches for a Reiserfs filesystem on a device, replays any necessary transactions, and either checks or repairs the file system.</p>
<dl>
<dt><i>device</i></p>
<dd>is the special file corresponding to a device or to a partition (e.g /dev/hdXX for an IDE disk partition or /dev/sdXX for a SCSI disk partition).</dl>
<h2>Options</h2>
<dl>
<dt><code>&#8211;rebuild-sb</code></p>
<dd>This option recovers the superblock on a Reiserfs partition. Normally you only need this option if mount reports &quot;read_super_block: can&#8217;t find a reiserfs file system&quot; and you are sure that a Reiserfs file system is there. But remember that if you have used some partition editor program and now you cannot find a filesystem, probably something has gone wrong while repartitioning and the start of the partition has been changed. If so, instead of rebuilding the super block on a wrong place you should find the correct start of the partition first.</p>
<dt><code>&#8211;check</code></p>
<dd>This default action checks filesystem consistency and reports, but does not repair any corruption that it finds. This option may be used on a read-only file system mount.</p>
<dt><code>&#8211;fix-fixable</code></p>
<dd>This option recovers certain kinds of corruption that do not require rebuilding the entire file system tree (<code>&#8211;rebuild-tree</code>). Normally you only need this option if the <code>&#8211;check</code> option reports &quot;corruption that can be fixed with <code>&#8211;fix-fixable</code>&quot;. This includes: zeroing invalid data-block pointers, correcting st_size and st_blocks for directories, and deleting invalid directory entries.</p>
<dt><code>&#8211;rebuild-tree</code></p>
<dd>This option rebuilds the entire filesystem tree using leaf nodes found on the device. Normally you only need this option if the <code>reiserfsck &#8211;check</code> reports &quot;Running with <code>&#8211;rebuild-tree</code> is required&quot;. You are strongly encouraged to make a backup copy of the whole partition before attempting the <code>&#8211;rebuild-tree</code> option. Once <code>reiserfsck &#8211;rebuild-tree</code> is started it must finish its work (and you should not interrupt it), otherwise the filesystem will be left in the unmountable state to avoid subsequent data corruptions.</p>
<dt><code>&#8211;clean-attributes</code></p>
<dd>This option cleans reserved fields of Stat-Data items. There were days when there were no extended attributes in reiserfs. When they were implemented old partitions needed to be cleaned first &#8212; reiserfs code in the kernel did not care about not used fields in its strutures. Thus if you have used one of the old (pre-attrbutes) kernels with a ReiserFS filesystem and you want to use extented attribues there, you should clean the filesystem first.</p>
<dt><code>&#8211;journal </code><i>device </i>, <code>-j </code><i>device </i></p>
<dd>This option supplies the device name of the current file system journal. This option is required when the journal resides on a separate device from the main data device (although it can be avoided with the expert option <code>&#8211;no-journal-available</code>).</p>
<dd><code>&#8211;adjust-size, -z</code> This option causes <code>reiserfsck</code> to correct file sizes that are larger than the offset of the last discovered byte. This implies that holes at the end of a file will be removed. File sizes that are smaller than the offset of the last discovered byte are corrected by <code>&#8211;fix-fixable</code>.</p>
<dt><code>&#8211;badblocks </code><i>file</i>, <code>-B </code><i> file</i></p>
<dd>This option sets the badblock list to be the list of blocks specified in the given `file`. The filesystem badblock list is cleared before the new list is added. It can be used with <code>&#8211;fix-fixable</code> to fix the list of badblocks (see <code>debugreiserfs -B</code>). If the device has bad blocks, every time it must be given with the <code>&#8211;rebuild-tree</code> option.</p>
<dt><code>&#8211;logfile </code><i>file</i>, <code>-l </code><i> file</i></p>
<dd>This option causes <code>reiserfsck</code> to report any corruption it finds to the specified log file rather than to stderr.</p>
<dt><code>&#8211;nolog, -n</code></p>
<dd>This option prevents <code>reiserfsck</code> from reporting any kinds of corruption.</p>
<dt><code>&#8211;quiet, -q</code></p>
<dd>This option prevents <code>reiserfsck</code> from reporting its rate of progress.</p>
<dt><code>&#8211;yes, -y</code></p>
<dd>This option inhibits <code>reiserfsck</code> from asking you for confirmation after telling you what it is going to do. It will assuem you confirm. For safety, it does not work with the <code>&#8211;rebuild-tree</code> option.</p>
<dt><code>-a</code>, <code>-p</code></p>
<dd>These options are usually passed by fsck -A during the automatic checking of those partitions listed in /etc/fstab. These options cause <code>reiserfsck</code> to print some information about the specified filesystem, to check if error flags in the superblock are set and to do some light-weight checks. If these checks reveal a corruption or the flag indicating a (possibly fixable) corruption is found set in the superblock, then <code>reiserfsck</code> switches to the fix-fixable mode. If the flag indicating a fatal corruption is found set in the superblock, then <code>reiserfsck</code> finishes with an error.</p>
<dt><code>&#8211;force, -f</code></p>
<dd>Force checking even if the file system seems clean.</p>
<dt><code>-V</code></p>
<dd>This option prints the reiserfsprogs version and then exit.</p>
<dt><code>-r</code></p>
<dd>This option does nothing at all; it is provided only for backwards compatibility.</dl>
<h2>Expert Options</h2>
<p>DO NOT USE THESE OPTIONS UNLESS YOU KNOW WHAT YOU ARE DOING. WE ARE NOT RESPONSIBLE IF YOU LOSE DATA AS A RESULT OF THESE OPTIONS.</p>
<dl>
<dt><code>&#8211;no-journal-available</code></p>
<dd>This option allows <code>reiserfsck</code> to proceed when the journal device is not available. This option has no effect when the journal is located on the main data device. NOTE: after this operation you must use <code>reiserfstune</code> to specify a new journal device.</p>
<dt><code>&#8211;scan-whole-partition, -S</code></p>
<dd>This option causes <code>&#8211;rebuild-tree</code> to scan the whole partition but not only the used space on the partition.</dl>
<h2>AN EXAMPLE OF USING reiserfsck</h2>
<p>1. You think something may be wrong with a reiserfs partition on /dev/hda1 or you would just like to perform a periodic disk check. </p>
<p> 2. Run <code>reiserfsck &#8211;check &#8211;logfile check.log /dev/hda1</code>. If <code>reiserfsck &#8211;check</code> exits with status 0 it means no errors were discovered. </p>
<p> 3. If <code>reiserfsck &#8211;check</code> exits with status 1 (and reports about fixable corruptions) it means that you should run <code>reiserfsck &#8211;fix-fixable &#8211;logfile fixable.log /dev/hda1</code>. </p>
<p> 4. If <code>reiserfsck &#8211;check</code> exits with status 2 (and reports about fatal corruptions) it means that you need to run <code>reiserfsck &#8211;rebuild-tree</code>. If <code>reiserfsck &#8211;check</code> fails in some way you should also run <code>reiserfsck &#8211;rebuild-tree</code>, but we also encourage you to submit this as a bug report. </p>
<p> 5. Before running <code>reiserfsck &#8211;rebuild-tree</code>, please make a backup of the whole partition before proceeding. Then run <code>reiserfsck &#8211;rebuild-tree &#8211;logfile rebuild.log /dev/hda1</code>. </p>
<p> 6. If the <code>reiserfsck &#8211;rebuild-tree</code> step fails or does not recover what you expected, please submit this as a bug report. Try to provide as much information as possible including your platform and Linux kernel version. We will try to help solve the problem.</p>
<h2>Exit Codes</h2>
<p><code>reiserfsck</code> uses the following exit codes:<br />
 &nbsp; <i>0</i> &#8211; No errors.<br />
 &nbsp; <i>1</i> &#8211; File system errors corrected.<br />
 &nbsp; <i>2</i> &#8211; Reboot is needed.<br />
 &nbsp; <i>4</i> &#8211; File system fatal errors left uncorrected,<br />
 <code>reiserfsck &#8211;rebuild-tree</code> needs to be launched.<br />
 &nbsp; <i>6</i> &#8211; File system fixable errors left uncorrected,<br />
 <code>reiserfsck &#8211;fix-fixable</code> needs to be launched.<br />
 &nbsp; <i>8</i> &#8211; Operational error.<br />
 &nbsp; <i>16</i> &#8211; Usage or syntax error.</p>
<h2>Author</h2>
<p>This version of <code>reiserfsck</code> has been written by Vitaly Fertman &lt;vitaly [at] namesys.com&gt;.</p>
<h2>Bugs</h2>
<p>Please report bugs to the ReiserFS developers &lt;reiserfs-devel [at] vger.kernel.org&gt;, providing as much information as possible&#8211;your hardware, kernel, patches, settings, all printed messages, the logfile; check the syslog file for any related information.</p>
<h2>Todo</h2>
<p>Faster recovering, signal handling.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mkreiserfs/">mkreiserfs</a></code>(8), <code><a href="/docs/linux/man/8-reiserfstune/">reiserfstune</a></code>(8) <code><a href="/docs/linux/man/8-resize_reiserfs/">resize_reiserfs</a></code>(8), <code><a href="/docs/linux/man/8-debugreiserfs/">debugreiserfs</a></code>(8), </p>
