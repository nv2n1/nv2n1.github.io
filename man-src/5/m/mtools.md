---
title: "mtools(5)"
name: "mtools"
section: "5"
letter: "m"
url: "/docs/linux/man/5-mtools/"
description: "mtools.conf – mtools configuration files"
---

<p>mtools.conf &#8211; mtools configuration files </p>
<h2>Description</h2>
<p>This manual page describes the configuration files for mtools. They are called <tt>&infin;/etc/mtools.confIntegral</tt> and <tt>&infin;~/.mtoolsrcIntegral</tt>. If the environmental variable <tt>MTOOLSRC</tt> is set, its contents is used as the filename for a third configuration file. These configuration files describe the following items:</p>
<dl>
<dt>* &nbsp;Global configuration flags and variables&nbsp;</p>
<dd>
<dt>* &nbsp;Per drive flags and variables&nbsp;</p>
<dd></dl>
<h3>Location of the configuration files</h3>
<p><tt>&infin;/etc/mtools.confIntegral</tt> is the system-wide configuration file, and <tt>&infin;~/.mtoolsrcIntegral</tt> is the user&#8217;s private configuration file. On some systems, the system-wide configuration file is called <tt>&infin;/etc/default/mtools.confIntegral</tt> instead.</p>
<h3>&nbsp;<wbr>&nbsp;General configuration file syntax</h3>
<p>The configuration files is made up of sections. Each section starts with a keyword identifying the section followed by a colon. Then follow variable assignments and flags. Variable assignments take the following form: <i> </i></p>
<pre>name=value</pre>
<p>&nbsp; Flags are lone keywords without an equal sign and value following them. A section either ends at the end of the file or where the next section begins. Lines starting with a hash (<tt>#</tt>) are comments. Newline characters are equivalent to whitespace (except where ending a comment). The configuration file is case insensitive, except for item enclosed in quotes (such as filenames).</p>
<h3>Default values</h3>
<p>For most platforms, mtools contains reasonable compiled-in defaults for physical floppy drives. Thus, you usually don&#8217;t need to bother with the configuration file, if all you want to do with mtools is to access your floppy drives. On the other hand, the configuration file is needed if you also want to use mtools to access your hard disk partitions and DOSEMU image files.</p>
<h3>Global variables</h3>
<p>Global flags may be set to 1 or to 0. The following global flags are recognized:</p>
<dl>
<dt><tt>MTOOLS_SKIP_CHECK</tt>&nbsp;</p>
<dd>If this is set to 1, mtools skips most of its sanity checks. This is needed to read some Atari disks which have been made with the earlier ROMs, and which would not be recognized otherwise.</p>
<dt><tt>MTOOLS_FAT_COMPATIBILITY</tt>&nbsp;</p>
<dd>If this is set to 1, mtools skips the fat size checks. Some disks have a bigger FAT than they really need to. These are rejected if this option is not set.</p>
<dt><tt>MTOOLS_LOWER_CASE</tt>&nbsp;</p>
<dd>If this is set to 1, mtools displays all-upper-case short filenames as lowercase. This has been done to allow a behavior which is consistent with older versions of mtools which didn&#8217;t know about the case bits.</p>
<dt><tt>MTOOLS_NO_VFAT</tt>&nbsp;</p>
<dd>If this is set to 1, mtools won&#8217;t generate VFAT entries for filenames which are mixed-case, but otherwise legal dos filenames. This is useful when working with DOS versions which can&#8217;t grok VFAT long names, such as FreeDOS.</p>
<dt><tt>MTOOLS_DOTTED_DIR</tt>&nbsp;</p>
<dd>In a wide directory, prints the short name with a dot instead of spaces separating the basename and the extension.</p>
<dt><tt>MTOOLS_NAME_NUMERIC_TAIL</tt>&nbsp;</p>
<dd>If this is set to one (default), generate numeric tails for all long names (~1). If set to zero, only generate numeric tails if otherwise a clash would have happened.</p>
<dt><tt>MTOOLS_TWENTY_FOUR_HOUR_CLOCK</tt>&nbsp;</p>
<dd>If 1, uses the European notation for times (twenty four hour clock), else uses the UK/US notation (am/pm)</p>
<dt><tt>MTOOLS_LOCK_TIMEOUT</tt>&nbsp;</p>
<dd>How long, in seconds, to wait for a locked device to become free. Defaults to 30.</dl>
<p> Example: Inserting the following line into your configuration file instructs mtools to skip the sanity checks:<br />
&nbsp; </p>
<pre><code> MTOOLS_SKIP_CHECK=1
</code></pre>
<p> Global variables may also be set via the environment:<br />
&nbsp; </p>
<pre><code> export MTOOLS_SKIP_CHECK=1
</code></pre>
<p> Global string variables may be set to any value:</p>
<dl>
<dt><tt>MTOOLS_DATE_STRING</tt>&nbsp;</p>
<dd>The format used for printing dates of files. By default, is dd-mm-yyyy.</dl>
<h3>Per drive flags and variables</h3>
<h3>&nbsp;<wbr>&nbsp;General information</h3>
<p>Per drive flags and values may be described in a drive section. A drive section starts with <tt>drive</tt> &quot;<i>driveletter</i>&quot; : Then follow variable-value pairs and flags. This is a sample drive description:<br />
&nbsp; </p>
<pre><code> drive a:
 file=&quot;/dev/fd0&quot; use_xdf=1
</code></pre>
<h3>&nbsp;<wbr>&nbsp;Location information</h3>
<p>For each drive, you need to describe where its data is physically stored (image file, physical device, partition, offset).</p>
<dl>
<dt><tt>file</tt>&nbsp;</p>
<dd>The name of the file or device holding the disk image. This is mandatory. The file name should be enclosed in quotes.</p>
<dt><tt>partition</tt>&nbsp;</p>
<dd>Tells mtools to treat the drive as a partitioned device, and to use the given partition. Only primary partitions are accessible using this method, and they are numbered from 1 to 4. For logical partitions, use the more general <tt>offset</tt> variable. The <tt>partition</tt> variable is intended for removable media such as Syquest disks, ZIP drives, and magneto-optical disks. Although traditional DOS sees Syquest disks and magneto-optical disks as <tt>&infin;giant floppy disksIntegral</tt> which are unpartitioned, OS/2 and Windows NT treat them like hard disks, i.e. partitioned devices. The <tt>partition</tt> flag is also useful DOSEMU hdimages. It is not recommended for hard disks for which direct access to partitions is available through mounting.</p>
<dt><tt>offset</tt>&nbsp;</p>
<dd>Describes where in the file the MS-DOS file system starts. This is useful for logical partitions in DOSEMU hdimages, and for ATARI ram disks. By default, this is zero, meaning that the file system starts right at the beginning of the device or file.</dl>
<h3>&nbsp;<wbr>&nbsp;Disk Geometry Configuration</h3>
<p>Geometry information describes the physical characteristics about the disk. Its has three purposes:</p>
<dl>
<dt>formatting&nbsp;</p>
<dd>The geometry information is written into the boot sector of the newly made disk. However, you may also describe the geometry information on the command line. See section mformat, for details.</p>
<dt>filtering&nbsp;</p>
<dd>On some Unixes there are device nodes which only support one physical geometry. For instance, you might need a different node to access a disk as high density or as low density. The geometry is compared to the actual geometry stored on the boot sector to make sure that this device node is able to correctly read the disk. If the geometry doesn&#8217;t match, this drive entry fails, and the next drive entry bearing the same drive letter is tried. See section multiple descriptions, for more details on supplying several descriptions for one drive letter.</p>
<dd>If no geometry information is supplied in the configuration file, all disks are accepted. On Linux (and on SPARC) there exist device nodes with configurable geometry (<tt>&infin;/dev/fd0Integral</tt>, <tt>&infin;/dev/fd1Integral</tt> etc), and thus filtering is not needed (and ignored) for disk drives. (Mtools still does do filtering on plain files (disk images) in Linux: this is mainly intended for test purposes, as I don&#8217;t have access to a Unix which would actually need filtering).</p>
<dd>If you do not need filtering, but want still a default geometry for mformatting, you may switch off filtering using the <tt>mformat_only</tt> flag.</p>
<dd>If you want filtering, you should supply the <tt>filter</tt> flag. If you supply a geometry, you must supply one of both flags.</p>
<dt>initial geometry&nbsp;</p>
<dd>On devices that support it (usually floppy devices), the geometry information is also used to set the initial geometry. This initial geometry is applied while reading the boot sector, which contains the real geometry. If no geometry information is supplied in the configuration file, or if the <tt>mformat_only</tt> flag is supplied, no initial configuration is done.</p>
<dd>On Linux, initial geometry is not really needed, as the configurable devices are able to auto-detect the disk type accurately enough (for most common formats) to read the boot sector.</dl>
<p> Wrong geometry information may lead to very bizarre errors. That&#8217;s why I strongly recommend that you add the <tt>mformat_only</tt> flag to your drive description, unless you really need filtering or initial geometry. The following geometry related variables are available:</p>
<dl>
<dt><tt>cylinders</tt>&nbsp;</p>
<dd>
<dt> <tt>tracks</tt></p>
<dd>The number of cylinders. (<tt>cylinders</tt> is the preferred form, <tt>tracks</tt> is considered obsolete)</p>
<dt><tt>heads</tt>&nbsp;</p>
<dd>The number of heads (sides).</p>
<dt><tt>sectors</tt>&nbsp;</p>
<dd>The number of sectors per track.</dl>
<p> Example: the following drive section describes a 1.44M drive:  The following shorthand geometry descriptions are available:</p>
<dl>
<dt><tt>1.44m</tt>&nbsp;</p>
<dd>high density 3 1/2 disk. Equivalent to: <tt>fat_bits=12 cylinders=80 heads=2 sectors=18</tt></p>
<dt><tt>1.2m</tt>&nbsp;</p>
<dd>high density 5 1/4 disk. Equivalent to: <tt>fat_bits=12 cylinders=80 heads=2 sectors=15</tt></p>
<dt><tt>720k</tt>&nbsp;</p>
<dd>double density 3 1/2 disk. Equivalent to: <tt>fat_bits=12 cylinders=80 heads=2 sectors=9</tt></p>
<dt><tt>360k</tt>&nbsp;</p>
<dd>double density 5 1/4 disk. Equivalent to: <tt>fat_bits=12 cylinders=40 heads=2 sectors=9</tt></dl>
<p> The shorthand format descriptions may be amended. For example, <tt>360k sectors=8</tt> describes a 320k disk and is equivalent to: <tt>fat_bits=12 cylinders=40 heads=2 sectors=8</tt></p>
<h3>&nbsp;<wbr>&nbsp;Open Flags</h3>
<p>Moreover, the following flags are available:</p>
<dl>
<dt><tt>sync</tt>&nbsp;</p>
<dd>All i/o operations are done synchronously</p>
<dt><tt>nodelay</tt>&nbsp;</p>
<dd>The device or file is opened with the O_NDELAY flag. This is needed on some non-Linux architectures.</p>
<dt><tt>exclusive</tt>&nbsp;</p>
<dd>The device or file is opened with the O_EXCL flag. On Linux, this ensures exclusive access to the floppy drive. On most other architectures, and for plain files it has no effect at all.</dl>
<h3>&nbsp;<wbr>&nbsp;General Purpose Drive Variables</h3>
<p>The following general purpose drive variables are available. Depending to their type, these variables can be set to a string (precmd) or an integer (all others)</p>
<dl>
<dt><tt>fat_bits</tt>&nbsp;</p>
<dd>The number of FAT bits. This may be 12 or 16. This is very rarely needed, as it can almost always be deduced from information in the boot sector. On the contrary, describing the number of fat bits may actually be harmful if you get it wrong. You should only use it if mtools gets the auto-detected number of fat bits wrong, or if you want to mformat a disk with a weird number of fat bits.</p>
<dt><tt>codepage</tt>&nbsp;</p>
<dd>Describes the DOS code page used for short filenames. This is a number between 1 and 999. By default, code page 850 is used. The reason for this is because this code page contains most of the characters that are also available in ISO-Latin-1. You may also specify a global code page for all drives by using the global <tt>default_codepage</tt> parameter (outside of any drive description). This parameters exists starting at version 4.0.0</p>
<dt><tt>precmd</tt>&nbsp;</p>
<dd>On some variants of Solaris, it is necessary to call &#8216;volcheck -v&#8217; before opening a floppy device, in order for the system to notice that there is indeed a disk in the drive. <tt>precmd=&quot;volcheck -v&quot;</tt> in the drive clause establishes the desired behavior.</p>
<dt><tt>blocksize</tt>&nbsp;</p>
<dd>This parameter represents a default block size to be always used on this device. All I/O is done with multiples of this block size, independently of the sector size registered in the file system&#8217;s boot sector. This is useful for character devices whose sector size is not 512, such as for example CD-ROM drives on Solaris.</dl>
<p> Only the <tt>file</tt> variable is mandatory. The other parameters may be left out. In that case a default value or an auto-detected value is used.</p>
<h3>&nbsp;<wbr>&nbsp;General Purpose Drive Flags</h3>
<p>A flag can either be set to 1 (enabled) or 0 (disabled). If the value is omitted, it is enabled. For example, <tt>scsi</tt> is equivalent to <tt>scsi=1</tt></p>
<dl>
<dt><tt>nolock</tt>&nbsp;</p>
<dd>Instruct mtools to not use locking on this drive. This is needed on systems with buggy locking semantics. However, enabling this makes operation less safe in cases where several users may access the same drive at the same time.</p>
<dt><tt>scsi</tt>&nbsp;</p>
<dd>When set to 1, this option tells mtools to use raw SCSI I/O instead of the standard read/write calls to access the device. Currently, this is supported on HP-UX, Solaris and SunOS. This is needed because on some architectures, such as SunOS or Solaris, PC media can&#8217;t be accessed using the <tt>read</tt> and <tt>write</tt> system calls, because the OS expects them to contain a Sun specific &quot;disk label&quot;.</p>
<dd>As raw SCSI access always uses the whole device, you need to specify the &quot;partition&quot; flag in addition</p>
<dd>On some architectures, such as Solaris, mtools needs root privileges to be able to use the <tt>scsi</tt> option. Thus mtools should be installed setuid root on Solaris if you want to access Zip/Jaz drives. Thus, if the <tt>scsi</tt> flag is given, <tt>privileged</tt> is automatically implied, unless explicitly disabled by <tt>privileged=0</tt></p>
<dd>Mtools uses its root privileges to open the device, and to issue the actual SCSI I/O calls. Moreover, root privileges are only used for drives described in a system-wide configuration file such as <tt>&infin;/etc/mtools.confIntegral</tt>, and not for those described in <tt>&infin;~/.mtoolsrcIntegral</tt> or <tt>&infin;$MTOOLSRCIntegral</tt>.</p>
<dt><tt>privileged</tt>&nbsp;</p>
<dd>When set to 1, this instructs mtools to use its setuid and setgid privileges for opening the given drive. This option is only valid for drives described in the system-wide configuration files (such as <tt>&infin;/etc/mtools.confIntegral</tt>, not <tt>&infin;~/.mtoolsrcIntegral</tt> or <tt>&infin;$MTOOLSRCIntegral</tt>). Obviously, this option is also a no op if mtools is not installed setuid or setgid. This option is implied by &#8216;scsi=1&#8217;, but again only for drives defined in system-wide configuration files. Privileged may also be set explicitly to 0, in order to tell mtools not to use its privileges for a given drive even if <tt>scsi=1</tt> is set.</p>
<dd>Mtools only needs to be installed setuid if you use the <tt>privileged</tt> or <tt>scsi</tt> drive variables. If you do not use these options, mtools works perfectly well even when not installed setuid root.</p>
<dt><tt>vold</tt>&nbsp;</p>
<dd>
<dd>Instructs mtools to interpret the device name as a vold identifier rather than as a filename. The vold identifier is translated into a real filename using the <tt>media_findname()</tt> and <tt>media_oldaliases()</tt> functions of the <tt>volmgt</tt> library. This flag is only available if you configured mtools with the <tt>--enable-new-vold</tt> option before compilation.</p>
<dt><tt>swap</tt>&nbsp;</p>
<dd>
<dd>Consider the media as a word-swapped Atari disk.</p>
<dt><tt>use_xdf</tt>&nbsp;</p>
<dd>If this is set to a non-zero value, mtools also tries to access this disk as an XDF disk. XDF is a high capacity format used by OS/2. This is off by default. See section XDF, for more details.</p>
<dt><tt>mformat_only</tt>&nbsp;</p>
<dd>Tells mtools to use the geometry for this drive only for mformatting and not for filtering.</p>
<dt><tt>filter</tt>&nbsp;</p>
<dd>Tells mtools to use the geometry for this drive both for mformatting and filtering.</p>
<dt><tt>remote</tt>&nbsp;</p>
<dd>Tells mtools to connect to floppyd (see section floppyd).</dl>
<h3>&nbsp;<wbr>&nbsp;Supplying multiple descriptions for a drive</h3>
<p>It is possible to supply multiple descriptions for a drive. In that case, the descriptions are tried in order until one is found that fits. Descriptions may fail for several reasons:</p>
<dl>
<dt>1.&nbsp;</p>
<dd>because the geometry is not appropriate,</p>
<dt>2.&nbsp;</p>
<dd>because there is no disk in the drive,</p>
<dt>3.&nbsp;</p>
<dd>or because of other problems.</dl>
<p> Multiple definitions are useful when using physical devices which are only able to support one single disk geometry. Example:<br />
&nbsp; </p>
<pre><code> drive a: file=&quot;/dev/fd0H1440&quot; 1.44m
 drive a: file=&quot;/dev/fd0H720&quot; 720k
</code></pre>
<p> This instructs mtools to use /dev/fd0H1440 for 1.44m (high density) disks and /dev/fd0H720 for 720k (double density) disks. On Linux, this feature is not really needed, as the /dev/fd0 device is able to handle any geometry. You may also use multiple drive descriptions to access both of your physical drives through one drive letter:  With this description, <tt>mdir z:</tt> accesses your first physical drive if it contains a disk. If the first drive doesn&#8217;t contain a disk, mtools checks the second drive. When using multiple configuration files, drive descriptions in the files parsed last override descriptions for the same drive in earlier files. In order to avoid this, use the <tt>drive+</tt> or <tt>+drive</tt> keywords instead of <tt>drive</tt>. The first adds a description to the end of the list (i.e. it will be tried last), and the first adds it to the start of the list.</p>
<h3>Location of configuration files and parsing order</h3>
<p>The configuration files are parsed in the following order:</p>
<dl>
<dt>1.&nbsp;</p>
<dd>compiled-in defaults</p>
<dt>2.&nbsp;</p>
<dd><tt>&infin;/etc/mtools.confIntegral</tt></p>
<dt>3.&nbsp;</p>
<dd><tt>&infin;~/.mtoolsrcIntegral</tt>.</p>
<dt>4.&nbsp;</p>
<dd><tt>&infin;$MTOOLSRCIntegral</tt> (file pointed by the <tt>MTOOLSRC</tt> environmental variable)</dl>
<p> Options described in the later files override those described in the earlier files. Drives defined in earlier files persist if they are not overridden in the later files. For instance, drives A and B may be defined in <tt>&infin;/etc/mtools.confIntegral</tt> and drives C and D may be defined in <tt>&infin;~/.mtoolsrcIntegral</tt> However, if <tt>&infin;~/.mtoolsrcIntegral</tt> also defines drive A, this new description would override the description of drive A in <tt>&infin;/etc/mtools.confIntegral</tt> instead of adding to it. If you want to add a new description to a drive already described in an earlier file, you need to use either the <tt>+drive</tt> or <tt>drive+</tt> keyword.</p>
<h3>Backwards compatibility with old configuration file syntax</h3>
<p>The syntax described herein is new for version <tt>mtools-3.0</tt>. The old line-oriented syntax is still supported. Each line beginning with a single letter is considered to be a drive description using the old syntax. Old style and new style drive sections may be mixed within the same configuration file, in order to make upgrading easier. Support for the old syntax will be phased out eventually, and in order to discourage its use, I purposefully omit its description here. </p>
<h2>See also</h2>
<p>mtools </p>
