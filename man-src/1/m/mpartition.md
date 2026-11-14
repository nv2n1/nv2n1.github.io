---
title: "mpartition(1)"
name: "mpartition"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mpartition/"
description: "mpartition – partition an MSDOS hard disk"
---

<h2>Name</h2>
<p> mpartition &#8211; partition an MSDOS hard disk </p>
<h2>Note of warning</h2>
<p> This manpage has been automatically generated from mtools&#8217;s texinfo documentation, and may not be entirely accurate or complete. See the end of this man page for details. </p>
<h2>Description</h2>
<p> The <tt>mpartition</tt> command is used to create MS-DOS file systems as partitions. This is intended to be used on non-Linux systems, i.e. systems where fdisk and easy access to SCSI devices are not available. This command only works on drives whose partition variable is set. </p>
<p> <i> </i></p>
<pre><code>
mpartition -p drive
mpartition -r drive
mpartition -I [-B bootSector] drive 
mpartition -a drive
mpartition -d drive
mpartition -c [-s sectors] [-h heads]
[-t cylinders] [-v [-T type] [-b
begin] [-l length] [-f]
</code></pre>
<p>&nbsp; </p>
<p> Mpartition supports the following operations:</p>
<dl>
<dt><tt>p</tt>&nbsp;</p>
<dd> Prints a command line to recreate the partition for the drive. Nothing is printed if the partition for the drive is not defined, or an inconsistency has been detected. If verbose (<tt>-v</tt>) is also set, prints the current partition table.</p>
<dt><tt>r</tt>&nbsp;</p>
<dd> Removes the partition described by <i>drive</i>.</p>
<dt><tt>I</tt>&nbsp;</p>
<dd> Initializes the partition table, and removes all partitions.</p>
<dt><tt>c</tt>&nbsp;</p>
<dd> Creates the partition described by <i>drive</i>.</p>
<dt><tt>a</tt>&nbsp;</p>
<dd> &quot;Activates&quot; the partition, i.e. makes it bootable. Only one partition can be bootable at a time.</p>
<dt><tt>d</tt>&nbsp;</p>
<dd> &quot;Deactivates&quot; the partition, i.e. makes it unbootable.</dl>
<p> If no operation is given, the current settings are printed. </p>
<p> For partition creations, the following options are available:</p>
<dl>
<dt><tt>s&nbsp;</tt><i>sectors</i><tt></tt>&nbsp;</p>
<dd> The number of sectors per track of the partition (which is also the number of sectors per track for the whole drive).</p>
<dt><tt>h&nbsp;</tt><i>heads</i><tt></tt>&nbsp;</p>
<dd> The number of heads of the partition (which is also the number of heads for the whole drive). By default, the geometry information (number of sectors and heads) is figured out from neighboring partition table entries, or guessed from the size.</p>
<dt><tt>t&nbsp;</tt><i>cylinders</i><tt></tt>&nbsp;</p>
<dd> The number of cylinders of the partition (not the number of cylinders of the whole drive.</p>
<dt><tt>b&nbsp;</tt><i>begin</i><tt></tt>&nbsp;</p>
<dd> The starting offset of the partition, expressed in sectors. If begin is not given, mpartition lets the partition begin at the start of the disk (partition number 1), or immediately after the end of the previous partition.</p>
<dt><tt>l&nbsp;</tt><i>length</i><tt></tt>&nbsp;</p>
<dd> The size (length) of the partition, expressed in sectors. If end is not given, mpartition figures out the size from the number of sectors, heads and cylinders. If these are not given either, it gives the partition the biggest possible size, considering disk size and start of the next partition.</dl>
<p> The following option is available for all operation which modify the partition table:</p>
<dl>
<dt><tt>f</tt>&nbsp;</p>
<dd> Usually, before writing back any changes to the partition, mpartition performs certain consistency checks, such as checking for overlaps and proper alignment of the partitions. If any of these checks fails, the partition table is not changes. The <tt>-f</tt> allows you to override these safeguards.</dl>
<p> The following options are available for all operations:</p>
<dl>
<dt><tt>v</tt>&nbsp;</p>
<dd> Together with <tt>-p</tt> prints the partition table as it is now (no change operation), or as it is after it is modified.</p>
<dt><tt>vv</tt>&nbsp;</p>
<dd> If the verbosity flag is given twice, mpartition will print out a hexdump of the partition table when reading it from and writing it to the device.</dl>
<p> The following option is available for partition table initialization:</p>
<dl>
<dt><tt>B&nbsp;</tt><i>bootSector</i><tt></tt>&nbsp;</p>
<dd> Reads the template master boot record from file <i>bootSector</i>.</dl>
<h2>Choice of partition type</h2>
<p> Mpartition proceeds as follows to pick a type for the partition:</p>
<dl>
<dt>&#8211;&nbsp;<wbr>&nbsp;</p>
<dd> FAT32 partitions are assigned type 0x0C (&#8220;<tt>Win95 FAT32, LBA</tt>&#8221;)</p>
<dt>&#8211;&nbsp;<wbr>&nbsp;</p>
<dd> For all others, if the partition fits entirely within the 65536 sector of the disk, assign 0x01 (&#8220;<tt>DOS FAT12, CHS</tt>&#8221;) for FAT12 partition and 0x04 (&#8220;<tt>DOS FAT16, CHS</tt>&#8221;) for FAT16 partitions</p>
<dt>&#8211;&nbsp;<wbr>&nbsp;</p>
<dd> If not covered by the above, assign 0x06 (&#8220;<tt>DOS BIG FAT16 CHS</tt>&#8221;) if partition fits entirely within the first 1024 cylinders (CHS mode)</p>
<dt>&#8211;&nbsp;<wbr>&nbsp;</p>
<dd> All remaining cases get 0x0E (&#8220;<tt>Win95 BIG FAT16, LBA</tt>&#8221;)</dl>
<p> If number of fat bits is not known (not specified in drive&#8217;s definition), then FAT12 is assumed for all drives with less than 4096 sectors, and FAT16 for those with more than 4096 sectors. </p>
<p> This corresponds more or less to the definitions outlined at <tt><a rel="nofollow" href="https://en.wikipedia.org/wiki/Partition_type#List_of_partition_IDs">https://en.wikipedia.org/wiki/Partition_type#List_of_partition_IDs</a></tt> and <tt><a rel="nofollow" href="https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/cc977219(v=technet.10)">https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/cc977219(v=technet.10)</a></tt>, with two notable differences:</p>
<dl>
<dt>&#8211;&nbsp;<wbr>&nbsp;</p>
<dd> If fat bits are unknown, the reference documents consider drives with less than 32680 sectors to be FAT12. Mtools uses 4096 sectors as the cutoff point, as older versions of DOS only support FAT12 on disks with less than 4096 sectors (and these older versions are the ones which would be most likely to use FAT12 in the first place).</p>
<dt>&#8211;&nbsp;<wbr>&nbsp;</p>
<dd> The reference documents use a 8GB (wikipedia) or a 4GB (Microsoft) cutoff between 0x06 (<tt>DOS BIG FAT16 CHS</tt>) and 0x0E. Mtools uses 1024 cylinders. This is because any partition beyond 1024 cylinders must be LBA and cannot be CHS. 8GB works out to be the biggest capacity which can be represented as CHS (63 sectors, 255 heads and 1024 cylinders). 4GB is the capacity limit for windows 2000, so it makes sense that a documentation for windows 2000 would specify this as the upper limit for any partition type.</dl>
<h2>See Also</h2>
<p> Mtools&#8217; texinfo doc</p>
<h2>Viewing the texi doc</h2>
<p> This manpage has been automatically generated from mtools&#8217;s texinfo documentation. However, this process is only approximative, and some items, such as crossreferences, footnotes and indices are lost in this translation process. Indeed, these items have no appropriate representation in the manpage format. Moreover, not all information has been translated into the manpage version. Thus I strongly advise you to use the original texinfo doc. See the end of this manpage for instructions how to view the texinfo doc.</p>
<dl>
<dt>* &nbsp;<wbr>&nbsp;</p>
<dd> To generate a printable copy from the texinfo doc, run the following commands:<br />
&nbsp; </p>
<pre>
<code>    ./configure; make dvi; dvips mtools.dvi
</code></pre>
</dl>
<p>&nbsp;</p>
<dl>
<dt>* &nbsp;<wbr>&nbsp;</p>
<dd> To generate a html copy, run:<br />
&nbsp; </p>
<pre>
<code>    ./configure; make html
</code></pre>
</dl>
<p>&nbsp; A premade html can be found at <tt>&infin;<a rel="nofollow" href="http://www.gnu.org/software/mtools/manual/mtools.htmlIntegral">http://www.gnu.org/software/mtools/manual/mtools.htmlIntegral</a></tt></p>
<dl>
<dt>* &nbsp;<wbr>&nbsp;</p>
<dd> To generate an info copy (browsable using emacs&#8217; info mode), run:<br />
&nbsp; </p>
<pre>
<code>    ./configure; make info
</code></pre>
</dl>
<p>&nbsp; </p>
<p> The texinfo doc looks most pretty when printed or as html. Indeed, in the info version certain examples are difficult to read due to the quoting conventions used in info. </p>
<h2>Index</h2>
