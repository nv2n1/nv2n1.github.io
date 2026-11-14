---
title: "floppy(8)"
name: "floppy"
section: "8"
letter: "f"
url: "/docs/linux/man/8-floppy/"
description: "floppy – format floppy disks"
---

<p>floppy &#8211; format floppy disks</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>floppy</code> [[&#8211;createrc&nbsp;<wbr>&gt;/etc/floppy] | [&#8211;format&nbsp;<wbr><i>/dev/fdo</i>] | [&#8211;format&nbsp;<wbr><i>A:</i>]]</p>
<dt> <code>floppygtk</code></dl>
<h2>Description</h2>
<dd>The <code>floppy</code> utility does low-level formatting of floppy disks. <code>floppy</code> uses a simple interface for formatting disks in floppy controller drives and in ATAPI IDE floppy drives, such as LS-120 &quot;Superdisk&quot; drives. ATAPI IDE support requires a patch to the Linux kernel. Without a patched kernel <code>floppy</code> can only format disks in floppy controller drives.</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 Use caution in formatting anything other than standard 3.5&quot; 1.4MB floppy disks in ATAPI IDE floppy drives. Most LS-120 drives, for example, accept a request to format 120MB high density disks, but most 120MB disks are not designed to be formatted. Low-level formatting will ruin them permanently.  <code>floppygtk</code> is a GTK interface to the floppy utility. If started from an X terminal window, <code>floppy</code> automatically runs <code>floppygtk</code>.</p>
<h2>Options</h2>
<p>FC&#8211;probe, -pF[]</p>
<dl>
<dd>Probe for available floppy drives. <code>floppy</code> creates and displays a list of all detected floppy drives.</dl>
<p> FC&#8211;createrc, -rF[]</p>
<dl>
<dd>Print a configuration file. <code>floppy</code> prints on standard output the results of the FC&#8211;probeF[] option in a configuration file format. This configuration file should be saved as FC/etc/floppyF[].</dl>
<p> FC&#8211;showrcF[]</p>
<dl>
<dd>List floppy drives configured in FC/etc/floppyF[].</dl>
<p> FC&#8211;capacity, -cF[]</p>
<dl>
<dd>Show the available format capacities of the floppy drive. Most floppy drives can format disks of different capacities. FC&#8211;capacityF[] lists each available format capacity as FCCxBxSF[] where: C &#8211; number of cylinders, B &#8211; blocks per cylinder, S &#8211; block size, in bytes. FC&#8211;capacityF[] also calculates how much that is, in kilobytes ormegabytes.</dl>
<p> FC&#8211;format, -fF[]</p>
<dl>
<dd>Format the disk in the floppy drive.</dl>
<p> FC&#8211;size=CxBxS, -s=CxBxSF[]</p>
<dl>
<dd>Specify the size of the disk to format. FC&#8211;formatF[] uses the first format capacity reported by FC&#8211;capacityF[] if the FC&#8211;sizeF[] option is not specified.</dl>
<p> FC&#8211;ext2F[], or FC&#8211;ext3F[]</p>
<dl>
<dd>Create an ext2 or an ext3 (Linux) filesystem on the formatted floppy. This option requires the e2fsprogs package to be installed. This option runs <code>mke2fs</code> after formatting the floppy disk.</dl>
<p> FC&#8211;fatF[]</p>
<dl>
<dd>Create a FAT (DOS) filesystem on the formatted floppy. This option requires the dosfstools package to be installed. This option runs <code>mkdosfs</code> after formatting the floppy disk.</dl>
<p> FC&#8211;noprompt, -nF[]</p>
<dl>
<dd>Suppress verbose output produced by FC&#8211;capacityF[] and FC&#8211;formatF[]. Use a raw output format that can be used by a front-end wrapper that runs <code>floppy</code> on the back-end.</dl>
<p> FC&#8211;ejectF[]</p>
<dl>
<dd>Eject the floppy from the drive (IDE floppy drives with an electronic eject mechanism).</dl>
<h3>Probing For Available Floppy Drives</h3>
<dl>
<dd><font SIZE="-1"> </font></p>
<pre>floppy --probe</pre>
<p><font SIZE="+1"></dl>
<p> This command probes the hardware and reports on the available floppy drives. A typical output from FC&#8211;probeF[] would be: </p>
<dl>
<dd></font> </p>
<pre>floppy 0.18 Copyright 2001-2003, Double Precision, Inc.
floppy /dev/fd0: 3.5&quot; HD
idefloppy /dev/hda: LS-120 VER5 00 UHD Floppy
 Revision: F523M5A9
 Serial number: 9803M9A03464</pre>
<p><font SIZE="+1"></dl>
<p> Here, <code>floppy</code> detected a high density floppy drive on FC/dev/fd0F[], and an IDE floppy drive on FC/dev/hdaF[]. </font></p>
<h3>Creating A Configuration File</h3>
<p>A configuration file, FC/etc/floppyF[] must be created before <code>floppy</code> can format floppy disks. This configuration file can be created automatically by the FC&#8211;creatercF[] option. Each line in the configuration file contains the following information: FCtype&lt;TAB&gt;label&lt;TAB&gt;deviceF[]. &quot;&lt;TAB&gt;&quot; is a single ASCII TAB character. &quot;<i>device</i>&quot; is the device entry for the floppy drive. <code>floppy</code> requires that all requests for formatting floppies must use only the devices that appear in this configuration file. &quot;<i>label</i>&quot; is an alias for this device. <code>floppy</code> accepts &quot;<i>label:</i>&quot; instead of the actual device entry, for example: &quot;<code>floppy &#8211;format A:</code>&quot;. &quot;<i>type</i>&quot; is either &quot;FCfloppyF[]&quot; or &quot;FCidefloppyF[]&quot;. </p>
<p> The FC&#8211;creatercF[] option sets &quot;FCAF[]&quot; as the label for the first floppy drive, and &quot;FCBF[]&quot; for the second floppy drive. If FC&#8211;creatercF[] finds more than two floppy drives, FC&#8211;creatercF[] will use &quot;FCFAF[]&quot;, &quot;FCFBF[]&quot;, &quot;FCFCF[]&quot;, and so on.</p>
<h3>Determining Available Format Capacities</h3>
<p>Most floppy drives can format disks of different capacities. The FC&#8211;capacityF[] option shows possible format capacities on the specified floppy device. A typical IDE floppy drive may report the following capacities: </p>
<dl>
<dd><font SIZE="-1"> </font></p>
<pre>$ floppy --capacity B:
Formattable capacities for /dev/hda:
 80x36x512 (1.40 Mb)
 80x30x512 (1.17 Mb)
 56x22x1024 (1.20 Mb)</pre>
<p><font SIZE="+1"></dl>
<p> A standard floppy drive attached to the floppy controller may report the following capacities: </p>
<dl>
<dd></font> </p>
<pre>$ floppy --capacity A:
Formattable capacities for /dev/fd0:
 80x36x512 (/dev/fd0H1440, 1.40 Mb)
 80x18x512 (/dev/fd0D720, 720 Kb)
 80x48x512 (/dev/fd0u1920, 1.87 Mb)
 80x28x512 (/dev/fd0u1120, 1.09 Mb)
 80x40x512 (/dev/fd0u1660, 1.56 Mb)
 80x26x512 (/dev/fd0u1040, 1.01 Mb)
 80x46x512 (/dev/fd0u1840, 1.79 Mb)
 80x42x512 (/dev/fd0u1680, 1.64 Mb)</pre>
<p><font SIZE="+1"></dl>
<p> The FC&#8211;capacityF[] option reports each available format capacity as &quot;cylinders x blocks-per-cylinder x block size&quot;. IDE floppy drive only return a total block count, and FC&#8211;capacityF[] tries some common blocks-per-cylinder geometries, until it finds one that fits. Format capacities of standard floppy drives are obtained from the floppy device driver. </p>
<dl>
<dd></font><font SIZE="+2"> <code>Note</code> </font><font SIZE="+1"> </p>
<p> IDE floppy drives may report format capacities only after a disk is inserted. Without a floppy disk, IDE floppy drives may not report any available format capacities, or they may report the primary format capacity that they are designed to format. For example, most LS-120 drives default to reporting 120mb when there is no disk inserted in the drive: </p>
<dl>
<dd></font> </p>
<pre>$ floppy --capacity A:
Formattable capacities for /dev/hda:
 6848x36x512 (120.37 Mb)</pre>
<p><font SIZE="+1"></dl>
</dl>
<dl>
<dd></font><font SIZE="+2"> <code>Warning</code> </font><font SIZE="+1"> </p>
<p> Do not attempt to format 120Mb media in LS-120 drives. Most LS-120 disks are not user-formattable. They are factory-formatted, and attempts to format them in LS-120 drives will render them unusable (to be sure, check the label on the floppy itself). The <code>floppy</code> utility does not prevent one from trying to use any format capacity the IDE floppy drive claims to support. If the drive claims it can format a disk of the given capacity, <code>floppy</code> will oblige. </p>
</dl>
<p> </font></p>
<h3>Formatting</h3>
<p>The FC&#8211;formatF[] option does a low-level format on the floppy. </p>
<dl>
<dd><font SIZE="-1"> </font></p>
<pre>$ ./floppy --format --size=80x36x512 A:
Formatting 1.40 Mb... 0%</pre>
<p><font SIZE="+1"></dl>
<p> FC&#8211;sizeF[] must specify a geometry returned by FC&#8211;capacityF[]. If FC&#8211;sizeF[] is absent, the first geometry is selected. </p>
<p> For floppy controller drives, the status counter will go from 0% to 100%. With most IDE floppy drives the counter will remain at 0% until the format finishes. Some IDE floppy drives are capable of reporting format progress status, which will would allow FC&#8211;formatF[] to count up from 0% to 100%. </p>
<dl>
<dd></font> </p>
<pre>$ ./floppy --format --verify A:</pre>
<p><font SIZE="+1"></dl>
<p> The FC&#8211;verifyF[] option verifies the low-level format. For floppy controller drives, the floppy disk is read from start to finish, after the low-level format concludes. For IDE floppy drives, the format request to the drive sets a flag that that requests low-level format verification. </p>
<dl>
<dd></font><font SIZE="+2"> <code>Note</code> </font><font SIZE="+1"> </p>
<p> Some IDE floppy drives ignore the verify request, or always verify low-level formats, whether or not it was requested. </p>
</dl>
<dl>
<dd></font> </p>
<pre>$ ./floppy --format -V A:</pre>
<p><font SIZE="+1"></dl>
<p> The FC-VF[] option is like FC&#8211;verifyF[] except that IDE floppy drive formats are verified manually &#8211; like floppy controller drive formats &#8211; by reading the floppy disk from start to finish. </font></p>
<h2>Files</h2>
<p>FC/etc/floppyF[]</p>
<dl>
<dd>The configuration file.</dl>
<p> FC/dev/fd[0-7]F[]</p>
<dl>
<dd>Floppy controller drives.</dl>
<p> FC/dev/hd[a-h]F[]</p>
<dl>
<dd>ATAPI IDE floppy drives.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/4-fd/">fd</a></code>(4), <code><a href="/docs/linux/man/8-mkdosfs/">mkdosfs</a></code>(8), <code><a href="/docs/linux/man/8-mke2fs/">mke2fs</a></code>(8).</p>
<h2>Authors</h2>
<p><code>Double Precision, Inc.</code></p>
