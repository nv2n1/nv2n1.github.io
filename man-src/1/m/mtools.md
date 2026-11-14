---
title: "mtools(1)"
name: "mtools"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mtools/"
description: "mtools – utilities to access DOS disks in Unix."
---

<h2>Name</h2>
<p> mtools &#8211; utilities to access DOS disks in Unix. </p>
<h2>Introduction</h2>
<p> Mtools is a collection of tools to allow Unix systems to manipulate MS-DOS files: read, write, and move around files on an MS-DOS file system (typically a floppy disk). Where reasonable, each program attempts to emulate the MS-DOS equivalent command. However, unnecessary restrictions and oddities of DOS are not emulated. For instance, it is possible to move subdirectories from one subdirectory to another. </p>
<p> Mtools is sufficient to give access to MS-DOS file systems. For instance, commands such as <tt>mdir a:</tt> work on the <tt>a:</tt> floppy without any preliminary mounting or initialization (assuming the default <tt>&infin;/etc/mtools.confIntegral</tt> works on your machine). With mtools, one can change floppies too without unmounting and mounting. </p>
<h2>Where to get mtools</h2>
<p> Mtools can be found at the following places (and their mirrors):<br />
&nbsp; </p>
<pre>
<code><a rel="nofollow" href="http://ftp.gnu.org/gnu/mtools/mtools-4.0.24.tar.gz">http://ftp.gnu.org/gnu/mtools/mtools-4.0.24.tar.gz</a>
<a rel="nofollow" href="http://mtools.linux.lu/mtools-4.0.24.tar.gz">http://mtools.linux.lu/mtools-4.0.24.tar.gz</a>
<a href="ftp://www.tux.org/pub/knaff/mtools/mtools-4.0.24.tar.gz">ftp://www.tux.org/pub/knaff/mtools/mtools-4.0.24.tar.gz</a>
<a href="ftp://ibiblio.unc.edu/pub/Linux/utils/disk-management/mtools-4.0.24.tar.gz">ftp://ibiblio.unc.edu/pub/Linux/utils/disk-management/mtools-4.0.24.tar.gz</a>
</code></pre>
<p>&nbsp; </p>
<p> Before reporting a bug, make sure that it has not yet been fixed in the Alpha patches which can be found at:<br />
&nbsp; </p>
<pre>
<code><a rel="nofollow" href="http://ftp.gnu.org/gnu/mtools/">http://ftp.gnu.org/gnu/mtools/</a>
<a rel="nofollow" href="http://mtools.linux.lu/">http://mtools.linux.lu/</a>
<a href="ftp://www.tux.org/pub/knaff/mtools">ftp://www.tux.org/pub/knaff/mtools</a>
</code></pre>
<p>&nbsp; </p>
<p> These patches are named <tt>mtools-</tt><i>version</i><tt>-</tt><i>ddmm</i><tt>.taz</tt>, where version stands for the base version, <i>dd</i> for the day and <i>mm</i> for the month. Due to a lack of space, I usually leave only the most recent patch. </p>
<p> There is an mtools mailing list at mtools @ tux.org . Please send all bug reports to this list. You may subscribe to the list by sending a message with &#8216;subscribe mtools @ tux.org&#8217; in its body to majordomo @ tux.org . (N.B. Please remove the spaces around the &quot;@&quot; both times. I left them there in order to fool spambots.) Announcements of new mtools versions will also be sent to the list, in addition to the Linux announce newsgroups. The mailing list is archived at <a rel="nofollow" href="http://lists.gnu.org/pipermail/info-mtools/">http://lists.gnu.org/pipermail/info-mtools/</a> </p>
<h2>Common features of all mtools commands</h2>
<h3>Options and filenames</h3>
<p> MS-DOS filenames are composed of a drive letter followed by a colon, a subdirectory, and a filename. Only the filename part is mandatory, the drive letter and the subdirectory are optional. Filenames without a drive letter refer to Unix files. Subdirectory names can use either the &#8216;<tt>/</tt>&#8216; or &#8216;<tt>\</tt>&#8216; separator. The use of the &#8216;<tt>\</tt>&#8216; separator or wildcards requires the names to be enclosed in quotes to protect them from the shell. However, wildcards in Unix filenames should not be enclosed in quotes, because here we <code>want</code> the shell to expand them. </p>
<p> The regular expression &quot;pattern matching&quot; routines follow the Unix-style rules. For example, `<tt>*</tt>&#8216; matches all MS-DOS files in lieu of `<tt>*.*</tt>&#8216;. The archive, hidden, read-only and system attribute bits are ignored during pattern matching. </p>
<p> All options use the <tt>-</tt> (minus) as their first character, not <tt>/</tt> as you&#8217;d expect in MS-DOS. </p>
<p> Most mtools commands allow multiple filename parameters, which doesn&#8217;t follow MS-DOS conventions, but which is more user-friendly. </p>
<p> Most mtools commands allow options that instruct them how to handle file name clashes. See section name clashes, for more details on these. All commands accept the <tt>-V</tt> flags which prints the version, and most accept the <tt>-v</tt> flag, which switches on verbose mode. In verbose mode, these commands print out the name of the MS-DOS files upon which they act, unless stated otherwise. See section Commands, for a description of the options which are specific to each command. </p>
<h3>Drive letters</h3>
<p> The meaning of the drive letters depends on the target architectures. However, on most target architectures, drive A is the first floppy drive, drive B is the second floppy drive (if available), drive J is a Jaz drive (if available), and drive Z is a Zip drive (if available). On those systems where the device name is derived from the SCSI id, the Jaz drive is assumed to be at SCSI target 4, and the Zip at SCSI target 5 (factory default settings). On Linux, both drives are assumed to be the second drive on the SCSI bus (/dev/sdb). The default settings can be changes using a configuration file (see section Configuration). </p>
<p> The drive letter : (colon) has a special meaning. It is used to access image files which are directly specified on the command line using the <tt>-i</tt> options. </p>
<p> Example:<br />
&nbsp; </p>
<pre>
<code> mcopy -i my-image-file.bin ::file1 ::file2 .
</code></pre>
<p>&nbsp; </p>
<p> This copies <tt>file1</tt> and <tt>file2</tt> from the image file (<tt>my-image-file.bin</tt>) to the <tt>/tmp</tt> directory. </p>
<p> You can also supply an offset within the image file by including <tt>@@</tt><i>offset</i> into the file name. </p>
<p> Example:<br />
&nbsp; </p>
<pre>
<code> mcopy -i my-image-file.bin@@1M ::file1 ::file2 .
</code></pre>
<p>&nbsp; </p>
<p> This looks for the image at the offset of 1M in the file, rather than at its beginning. </p>
<h3>Current working directory</h3>
<p> The <tt>mcd</tt> command (&infin;mcdIntegral) is used to establish the device and the current working directory (relative to the MS-DOS file system), otherwise the default is assumed to be <tt>A:/</tt>. However, unlike MS-DOS, there is only one working directory for all drives, and not one per drive. </p>
<h3>VFAT-style long file names</h3>
<p> This version of mtools supports VFAT style long filenames. If a Unix filename is too long to fit in a short DOS name, it is stored as a VFAT long name, and a companion short name is generated. This short name is what you see when you examine the disk with a pre-7.0 version of DOS.<br />
&nbsp;The following table shows some examples of short names: </p>
<p>&nbsp; </p>
<pre><code>
Long name       MS-DOS name     Reason for the change
---------       ----------      ---------------------
thisisatest     THISIS~1        filename too long
alain.knaff     ALAIN~1.KNA     extension too long
prn.txt         PRN~1.TXT       PRN is a device name
.abc            ABC~1           null filename
hot+cold        HOT_CO~1        illegal character
</code></pre>
<p>&nbsp; </p>
<p>&nbsp;As you see, the following transformations happen to derive a short name:</p>
<dl>
<dt>* &nbsp;<wbr>&nbsp;</p>
<dd> Illegal characters are replaced by underscores. The illegal characters are <tt>;+=[]',\&quot;*\&lt;&gt;/?:|</tt>.</p>
<dt>* &nbsp;<wbr>&nbsp;</p>
<dd> Extra dots, which cannot be interpreted as a main name/extension separator are removed</p>
<dt>* &nbsp;<wbr>&nbsp;</p>
<dd> A <tt>~</tt><i>n</i> number is generated,</p>
<dt>* &nbsp;<wbr>&nbsp;</p>
<dd> The name is shortened so as to fit in the 8+3 limitation</dl>
<p>&nbsp;The initial Unix-style file name&nbsp;(whether long or short)&nbsp;is also called the <i>primary</i> name, and the derived short name is also called the <i>secondary</i> name. </p>
<p>&nbsp;Example:<br />
&nbsp; </p>
<pre>
<code> mcopy /etc/motd a:Reallylongname
</code></pre>
<p>&nbsp; Mtools creates a VFAT entry for Reallylongname, and uses REALLYLO as a short name. Reallylongname is the primary name, and REALLYLO is the secondary name.<br />
&nbsp; </p>
<pre>
<code> mcopy /etc/motd a:motd
</code></pre>
<p>&nbsp; Motd fits into the DOS filename limits. Mtools doesn&#8217;t need to derivate another name. Motd is the primary name, and there is no secondary name. </p>
<p>&nbsp;In a nutshell: The primary name is the long name, if one exists, or the short name if there is no long name. </p>
<p>&nbsp;Although VFAT is much more flexible than FAT, there are still names that are not acceptable, even in VFAT. There are still some illegal characters left (<tt>\&quot;*\&lt;&gt;/?:|</tt>), and device names are still reserved. </p>
<p>&nbsp; </p>
<pre><code>
Unix name       Long name       Reason for the change
---------       ----------      ---------------------
prn             prn-1           PRN is a device name
ab:c            ab_c-1          illegal character
</code></pre>
<p>&nbsp; </p>
<p>&nbsp;As you see, the following transformations happen if a long name is illegal:</p>
<dl>
<dt>* &nbsp;<wbr>&nbsp;</p>
<dd> Illegal characters are replaces by underscores,</p>
<dt>* &nbsp;<wbr>&nbsp;</p>
<dd> A <tt>-</tt><i>n</i> number is generated,</dl>
<h3>Name clashes</h3>
<p> When writing a file to disk, its long name or short name may collide with an already existing file or directory. This may happen for all commands which create new directory entries, such as <tt>mcopy</tt>, <tt>mmd</tt>, <tt>mren</tt>, <tt>mmove</tt>. When a name clash happens, mtools asks you what it should do. It offers several choices:</p>
<dl>
<dt><tt>overwrite</tt>&nbsp;</p>
<dd> Overwrites the existing file. It is not possible to overwrite a directory with a file.</p>
<dt><tt>rename</tt>&nbsp;</p>
<dd> Renames the newly created file. Mtools prompts for the new filename</p>
<dt><tt>autorename</tt>&nbsp;</p>
<dd> Renames the newly created file. Mtools chooses a name by itself, without prompting</p>
<dt><tt>skip</tt>&nbsp;</p>
<dd> Gives up on this file, and moves on to the next (if any)</dl>
<p> To chose one of these actions, type its first letter at the prompt. If you use a lower case letter, the action only applies for this file only, if you use an upper case letter, the action applies to all files, and you won&#8217;t be prompted again. </p>
<p> You may also chose actions (for all files) on the command line, when invoking mtools:</p>
<dl>
<dt><tt>-D o</tt>&nbsp;</p>
<dd> Overwrites primary names by default.</p>
<dt><tt>-D O</tt>&nbsp;</p>
<dd> Overwrites secondary names by default.</p>
<dt><tt>-D r</tt>&nbsp;</p>
<dd> Renames primary name by default.</p>
<dt><tt>-D R</tt>&nbsp;</p>
<dd> Renames secondary name by default.</p>
<dt><tt>-D a</tt>&nbsp;</p>
<dd> Autorenames primary name by default.</p>
<dt><tt>-D A</tt>&nbsp;</p>
<dd> Autorenames secondary name by default.</p>
<dt><tt>-D s</tt>&nbsp;</p>
<dd> Skip primary name by default.</p>
<dt><tt>-D S</tt>&nbsp;</p>
<dd> Skip secondary name by default.</p>
<dt><tt>-D m</tt>&nbsp;</p>
<dd> Ask user what to do with primary name.</p>
<dt><tt>-D M</tt>&nbsp;</p>
<dd> Ask user what to do with secondary name.</dl>
<p> Note that for command line switches lower/upper differentiates between primary/secondary name whereas for interactive choices, lower/upper differentiates between just-this-time/always. </p>
<p> The primary name is the name as displayed in Windows 95 or Windows NT: i.e. the long name if it exists, and the short name otherwise. The secondary name is the &quot;hidden&quot; name, i.e. the short name if a long name exists. </p>
<p> By default, the user is prompted if the primary name clashes, and the secondary name is autorenamed. </p>
<p> If a name clash occurs in a Unix directory, mtools only asks whether to overwrite the file, or to skip it. </p>
<h3>Case sensitivity of the VFAT file system</h3>
<p> The VFAT file system is able to remember the case of the filenames. However, filenames which differ only in case are not allowed to coexist in the same directory. For example if you store a file called LongFileName on a VFAT file system, mdir shows this file as LongFileName, and not as Longfilename. However, if you then try to add LongFilename to the same directory, it is refused, because case is ignored for clash checks. </p>
<p> The VFAT file system allows you to store the case of a filename in the attribute byte, if all letters of the filename are the same case, and if all letters of the extension are the same case too. Mtools uses this information when displaying the files, and also to generate the Unix filename when mcopying to a Unix directory. This may have unexpected results when applied to files written using an pre-7.0 version of DOS: Indeed, the old style filenames map to all upper case. This is different from the behavior of the old version of mtools which used to generate lower case Unix filenames. </p>
<h3>high capacity formats</h3>
<p> Mtools supports a number of formats which allow storage of more data on disk than usual. Due to different operating system abilities, these formats are not supported on all operating systems. Mtools recognizes these formats transparently where supported. </p>
<p> In order to format these disks, you need to use an operating system specific tool. For Linux, suitable floppy tools can be found in the <tt>fdutils</tt> package at the following locations~:<br />
&nbsp; </p>
<pre>
<tt><a href="ftp://www.tux.org/pub/knaff/fdutils/.">ftp://www.tux.org/pub/knaff/fdutils/.</a>
</tt><tt><a href="ftp://ibiblio.unc.edu/pub/Linux/utils/disk-management/fdutils-*">ftp://ibiblio.unc.edu/pub/Linux/utils/disk-management/fdutils-*</a>
</tt></pre>
<p>&nbsp; </p>
<p> See the manual pages included in that package for further detail: Use <tt>superformat</tt> to format all formats except XDF, and use <tt>xdfcopy</tt> to format XDF. </p>
<h3>&nbsp;<wbr>&nbsp;More sectors</h3>
<p> The oldest method of fitting more data on a disk is to use more sectors and more cylinders. Although the standard format uses 80 cylinders and 18 sectors (on a 3 1/2 high density disk), it is possible to use up to 83 cylinders (on most drives) and up to 21 sectors. This method allows to store up to 1743K on a 3 1/2 HD disk. However, 21 sector disks are twice as slow as the standard 18 sector disks because the sectors are packed so close together that we need to interleave them. This problem doesn&#8217;t exist for 20 sector formats. </p>
<p> These formats are supported by numerous DOS shareware utilities such as <tt>fdformat</tt> and <tt>vgacopy</tt>. In his infinite hubris, Bill Gate$ believed that he invented this, and called it <tt>&infin;DMF disksIntegral</tt>, or <tt>&infin;Windows formatted disksIntegral</tt>. But in reality, it has already existed years before! Mtools supports these formats on Linux, on SunOS and on the DELL Unix PC. </p>
<h3>&nbsp;<wbr>&nbsp;Bigger sectors</h3>
<p> By using bigger sectors it is possible to go beyond the capacity which can be obtained by the standard 512-byte sectors. This is because of the sector header. The sector header has the same size, regardless of how many data bytes are in the sector. Thus, we save some space by using <i>fewer</i>, but bigger sectors. For example, 1 sector of 4K only takes up header space once, whereas 8 sectors of 512 bytes have also 8 headers, for the same amount of useful data. </p>
<p> This method permits storage of up to 1992K on a 3 1/2 HD disk. </p>
<p> Mtools supports these formats only on Linux. </p>
<h3>&nbsp;<wbr>&nbsp;2m</h3>
<p> The 2m format was originally invented by Ciriaco Garcia de Celis. It also uses bigger sectors than usual in order to fit more data on the disk. However, it uses the standard format (18 sectors of 512 bytes each) on the first cylinder, in order to make these disks easier to handle by DOS. Indeed this method allows you to have a standard sized boot sector, which contains a description of how the rest of the disk should be read. </p>
<p> However, the drawback of this is that the first cylinder can hold less data than the others. Unfortunately, DOS can only handle disks where each track contains the same amount of data. Thus 2m hides the fact that the first track contains less data by using a <i>shadow FAT</i>. (Usually, DOS stores the FAT in two identical copies, for additional safety. XDF stores only one copy, but tells DOS that it stores two. Thus the space that would be taken up by the second FAT copy is saved.) This also means that you should <code>never use a 2m disk to store anything else than a DOS file system</code>. </p>
<p> Mtools supports these formats only on Linux. </p>
<h3>&nbsp;<wbr>&nbsp;XDF</h3>
<p> XDF is a high capacity format used by OS/2. It can hold 1840 K per disk. That&#8217;s lower than the best 2m formats, but its main advantage is that it is fast: 600 milliseconds per track. That&#8217;s faster than the 21 sector format, and almost as fast as the standard 18 sector format. In order to access these disks, make sure mtools has been compiled with XDF support, and set the <tt>use_xdf</tt> variable for the drive in the configuration file. See section Compiling mtools, and &infin;miscellaneous variablesIntegral, for details on how to do this. Fast XDF access is only available for Linux kernels which are more recent than 1.1.34. </p>
<p> Mtools supports this format only on Linux. </p>
<p> <code>Caution / Attention distributors</code>: If mtools is compiled on a Linux kernel more recent than 1.3.34, it won&#8217;t run on an older kernel. However, if it has been compiled on an older kernel, it still runs on a newer kernel, except that XDF access is slower. It is recommended that distribution authors only include mtools binaries compiled on kernels older than 1.3.34 until 2.0 comes out. When 2.0 will be out, mtools binaries compiled on newer kernels may (and should) be distributed. Mtools binaries compiled on kernels older than 1.3.34 won&#8217;t run on any 2.1 kernel or later. </p>
<h3>Exit codes</h3>
<p> All the Mtools commands return 0 on success, 1 on utter failure, or 2 on partial failure. All the Mtools commands perform a few sanity checks before going ahead, to make sure that the disk is indeed an MS-DOS disk (as opposed to, say an ext2 or MINIX disk). These checks may reject partially corrupted disks, which might otherwise still be readable. To avoid these checks, set the MTOOLS_SKIP_CHECK environmental variable or the corresponding configuration file variable (see section global variables)</p>
<h3>Bugs</h3>
<p> An unfortunate side effect of not guessing the proper device (when multiple disk capacities are supported) is an occasional error message from the device driver. These can be safely ignored. </p>
<p> The fat checking code chokes on 1.72 Mb disks mformatted with pre-2.0.7 mtools. Set the environmental variable MTOOLS_FAT_COMPATIBILITY (or the corresponding configuration file variable, &infin;global variablesIntegral) to bypass the fat checking. </p>
<h2>See also</h2>
<p> floppyd_installtest mattrib mbadblocks mcd mclasserase mcopy mdel mdeltree mdir mdu mformat minfo mkmanifest mlabel mmd mmount mmove mrd mren mshortname mshowfat mtoolstest mtype </p>
<h2>Index</h2>
<dt><a href="#lbAS">See also</a></p>
<dd></dl>
