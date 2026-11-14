---
title: "fsck-hfsplus(8)"
name: "fsck-hfsplus"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fsck-hfsplus/"
description: "fsck.hfsplus – HFS file system consistency check"
---

<p><code>fsck.hfsplus</code> &#8211; HFS file system consistency check</p>
<h2>Synopsis</h2>
<p><code>fsck.hfsplus</code> &#8211;<code>q</code> [-<code>df</code> ] <i>special &#8230;</i><br />
<code>fsck.hfsplus</code> &#8211;<code>p</code> [-<code>df</code> ] <i>special &#8230;</i><br />
<code>fsck.hfsplus</code> [-<code>n | y | r</code> ] [-<code>dfgxlE</code> ] [-<code>D </code><i>flags</i> ] [-<code>b </code><i>size</i> ] [-<code>B </code><i>path</i> ] [-<code>m </code><i>mode</i> ] [-<code>c </code><i>size</i> ] [-<code>R </code><i>flags</i> ] <i>special &#8230;</i></p>
<h2>Description</h2>
<p>The <code>fsck.hfsplus</code> utility verifies and repairs standard HFS and HFS+ file systems. </p>
<p> The first form of <code>fsck.hfsplus</code> quickly checks the specified file systems to determine whether they were cleanly unmounted. </p>
<p> The second form of <code>fsck.hfsplus</code> preens the specified file systems. It is normally started by <a href="/docs/linux/man/8-fsck/">fsck</a>(8) run from /etc/rc.boot during automatic reboot, when a HFS file system is detected. When preening file systems, <code>fsck.hfsplus</code> will fix common inconsistencies for file systems that were not unmounted cleanly. If more serious problems are found, <code>fsck.hfsplus</code> does not try to fix them, indicates that it was not successful, and exits. </p>
<p> The third form of <code>fsck.hfsplus</code> checks the specified file systems and tries to repair all detected inconsistencies. </p>
<p> If no options are specified <code>fsck.hfsplus</code> will always check and attempt to fix the specified file systems. </p>
<p> The options are as follows:</p>
<dl>
<dt><code>-c </code><i>size</i></p>
<dd>Specify the <i>size </i> of the cache used by <code>fsck.hfsplus</code> internally. Bigger <i>size </i> can result in better performance but can result in deadlock when used with &#8211;<code>l </code> option. Size can be specified as a decimal, octal, or hexadecimal number. If the number ends with a &#8220;k&#8221;, &#8220;m&#8221;, or &#8220;g&#8221;, the number is multiplied by 1024 (1K), 1048576 (1M), or 1073741824 (1G), respectively.</p>
<dt><code>-d</code></p>
<dd>Display debugging information. This option may provide useful information when <code>fsck.hfsplus</code> cannot repair a damaged file system.</p>
<dt><code>-D </code><i>flags</i></p>
<dd>Print extra debugging information. The <i>flags</i> are a bitmap that control which kind of debug information is printed. The following values are currently implemented:</p>
<dl>
<dt><code>0x0001</code></p>
<dd>Informational messages</p>
<dt><code>0x0002</code></p>
<dd>Error messages</p>
<dt><code>0x0010</code></p>
<dd>Extended attributes related messages</p>
<dt><code>0x0020</code></p>
<dd>Overlapped extents related messages</dl>
<dt><code>-b </code><i>size</i></p>
<dd>Specify the size, in bytes, of the physical blocks used by the &#8211;<code>B</code> option.</p>
<dt><code>-B </code><i>path</i></p>
<dd>Print the files containing the physical blocks listed in the file <i>path</i> The file should contain one or more decimal, octal (with leading 0) or hexadecimal (with leading 0x) numbers separated by white space. The physical block numbers are relative to the start of the partition, so if you have block numbers relative to the start of the device, you will have to subtract the block number of the start of the partition. The size of a physical block is given with the &#8211;<code>b</code> option; the default is 512 bytes per block.</p>
<dt><code>-f</code></p>
<dd>When used with the &#8211;<code>p</code> option, force <code>fsck.hfsplus</code> to check `clean&#8217; file systems, otherwise it means force <code>fsck.hfsplus</code> to check and repair journaled HFS+ file systems.</p>
<dt><code>-g</code></p>
<dd>Causes <code>fsck.hfsplus</code> to generate its output strings in GUI format. This option is used when another application with a graphical user interface (like Mac OS X Disk Utility) is invoking the <code>fsck.hfsplus</code> tool.</p>
<dt><code>-x</code></p>
<dd>Causes <code>fsck.hfsplus</code> to generate its output strings in XML (plist) format. This option implies the &#8211;<code>g</code> option.</p>
<dt><code>-l</code></p>
<dd>Lock down the file system and perform a test-only check. This makes it possible to check a file system that is currently mounted, although no repairs can be made.</p>
<dt><code>-m </code><i>mode</i></p>
<dd>Mode is an octal number that will be used to set the permissions for the lost+found directory when it is created. The lost+found directory is only created when a volume is repaired and orphaned files or directories are detected. <code>fsck.hfsplus</code> places orphaned files and directories into the lost+found directory (located at the root of the volume). The default mode is 01777.</p>
<dt><code>-p</code></p>
<dd>Preen the specified file systems.</p>
<dt><code>-q</code></p>
<dd>Causes <code>fsck.hfsplus</code> to quickly check whether the volume was unmounted cleanly. If the volume was unmounted cleanly, then the exit status is 0. If the volume was not unmounted cleanly, then the exit status will be non-zero. In either case, a message is printed to standard output describing whether the volume was clean or dirty.</p>
<dt><code>-y</code></p>
<dd>Always attempt to repair any damage that is found.</p>
<dt><code>-n</code></p>
<dd>Never attempt to repair any damage that is found.</p>
<dt><code>-E</code></p>
<dd>Cause <code>fsck.hfsplus</code> to exit (with a value of 47) if it encounters any major errors. A &#8220;major error&#8221; is considered one which would impact using the volume in normal usage; an inconsistency which would not impact such use is considered &#8220;minor&#8221; for this option. Only valid with the &#8211;<code>n</code> option.</p>
<dt><code>-R </code><i>flags</i></p>
<dd>Rebuilds the requested btree. The following flags are supported:</p>
<dl>
<dt><code>a</code></p>
<dd>Attribute btree</p>
<dt><code>c</code></p>
<dd>Catalog btree</p>
<dt><code>e</code></p>
<dd>Extents overflow btree</dl>
<p> Rebuilding a btree will only work if there is enough free space on the file system for the new btree file, and if <code>fsck.hfsplus</code> is able to traverse each of the nodes in the requested btree successfully. Rebuilding btrees is not supported on HFS Standard volumes.</p>
<dt><code>-r</code></p>
<dd>Rebuild the catalog btree. This is synonymous with &#8211;<code>Rc </code></dl>
<p> Because of inconsistencies between the block device and the buffer cache, the raw device should always be used.</p>
<h2>Exit Values</h2>
<p><code>fsck.hfsplus</code> indicates some status by exit value. The current list of exit status results is:</p>
<dl>
<dt><code>0</code></p>
<dd>No errors found, or successfully repaired.</p>
<dt><code>3</code></p>
<dd>A quick-check (the &#8211;<code>n</code> option) found a dirty filesystem; no repairs were made.</p>
<dt><code>4</code></p>
<dd>During boot, the root filesystem was found to be dirty; repairs were made, and the filesystem was remounted. The system should be rebooted.</p>
<dt><code>8</code></p>
<dd>A corrupt filesystem was found during a check, or repairs did not succeed.</p>
<dt><code>47</code></p>
<dd>A major error was found with &#8211;<code>E</code></dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-fsck/">fsck</a>(8)</p>
<h2>Bugs</h2>
<p><code>fsck.hfsplus</code> is not able to fix some inconsistencies that it detects.</p>
<h2>History</h2>
<p>The <code>fsck.hfsplus</code> command appeared in Mac OS X Server 1.0 .</p>
