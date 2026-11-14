---
title: "mkisofs(1)"
name: "mkisofs"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mkisofs/"
description: "genisoimage – create ISO9660/Joliet/HFS filesystem with optional Rock Ridge attributes"
---

<h2 class="name">NAME</h2>
<p> genisoimage &#8211; create ISO9660/Joliet/HFS filesystem with optional Rock Ridge attributes </p>
<h2>SYNOPSIS</h2>
<p> <code>genisoimage</code> [<i>options</i>] [<code>-o</code> <i>filename</i>] <i>pathspec</i> [<i>pathspec &#8230;</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>genisoimage</code> is a pre-mastering program to generate ISO9660/Joliet/HFS hybrid filesystems. </p>
<p> <code>genisoimage</code> is capable of generating the <code>System Use Sharing Protocol records (SUSP)</code> specified by the <code>Rock Ridge Interchange Protocol</code>. This is used to further describe the files in the ISO9660 filesystem to a Unix host, and provides information such as long filenames, UID/GID, POSIX permissions, symbolic links, and block and character device files. </p>
<p> If Joliet or HFS hybrid command line options are specified, <code>genisoimage</code> will create the additional filesystem metadata needed for Joliet or HFS. Otherwise <code>genisoimage</code> will generate a pure ISO9660 filesystem. </p>
<p> <code>genisoimage</code> can generate a <i>true</i> (or <i>shared</i>) HFS hybrid filesystem. The same files are seen as HFS files when accessed from a Macintosh and as ISO9660 files when accessed from other machines. HFS stands for <i>Hierarchical File System</i> and is the native filesystem used on Macintosh computers. </p>
<p> As an alternative, <code>genisoimage</code> can generate the <i>Apple Extensions to ISO9660</i> for each file. These extensions provide each file with CREATOR, TYPE and certain Finder flags when accessed from a Macintosh. See the <code>HFS MACINTOSH FILE FORMATS</code> section below. </p>
<p> <code>genisoimage</code> takes a snapshot of a given directory tree, and generates a binary image which will correspond to an ISO9660 and/or HFS filesystem when written to a block device. </p>
<p> Each file written to the ISO9660 filesystem must have a filename in the 8.3 format (up to 8 characters, period, up to 3 characters, all uppercase), even if Rock Ridge is in use. This filename is used on systems that are not able to make use of the Rock Ridge extensions (such as MS-DOS), and each filename in each directory must be different from the other filenames in the same directory. <code>genisoimage</code> generally tries to form correct names by forcing the Unix filename to uppercase and truncating as required, but often this yields unsatisfactory results when the truncated names are not all unique. <code>genisoimage</code> assigns weightings to each filename, and if two names that are otherwise the same are found, the name with the lower priority is renamed to include a 3-digit number (guaranteed to be unique). For example, the two files <i>foo.bar</i> and <i>foo.bar.~1~</i> could be rendered as <i>FOO.BAR;1</i> and <i>FOO000.BAR;1</i>. </p>
<p> When used with various HFS options, <code>genisoimage</code> will attempt to recognise files stored in a number of Apple/Unix file formats and will copy the data and resource forks as well as any relevant Finder information. See the <code>HFS MACINTOSH FILE FORMATS</code> section below for more about formats <code>genisoimage</code> supports. </p>
<p> Note that <code>genisoimage</code> is not designed to communicate with the writer directly. Most writers have proprietary command sets which vary from one manufacturer to another, and you need a specialized tool to actually burn the disc. <code>wodim</code> is one such tool. The latest version of <code>wodim</code> is available from <i><a rel="nofollow" href="http://www.cdrkit.org/">http://www.cdrkit.org/</a></i>. </p>
<p> <code>pathspec</code> is the path of the directory tree to be copied into the ISO9660 filesystem. Multiple paths can be specified, and <code>genisoimage</code> will merge the files found in all of the specified path components to form the filesystem image. </p>
<p> If the option <code>-graft-points</code> has been specified, it is possible to graft the paths at points other than the root directory, and it is possible to graft files or directories onto the cdrom image with names different than what they have in the source filesystem. This is easiest to illustrate with a couple of examples. Let&#8217;s start by assuming that a local file <i>../old.lis</i> exists, and you wish to include it in the cdrom image.</p>
<dl>
<dt>
<dd> foo/bar/=../old.lis</dl>
<p> will include <i>old.lis</i> in the cdrom image at <i>/foo/bar/old.lis</i>, while</p>
<dl>
<dt>
<dd> foo/bar/xxx=../old.lis</dl>
<p> will include <i>old.lis</i> in the cdrom image at <i>/foo/bar/xxx</i>. The same sort of syntax can be used with directories as well. <code>genisoimage</code> will create any directories required such that the graft points exist on the cdrom image &#8212; the directories do not need to appear in one of the paths. By default, any directories that are created on the fly like this will have permissions 0555 and appear to be owned by the person running <code>genisoimage</code>. If you wish other permissions or owners of the intermediate directories, see <code>-uid</code>, <code>-gid</code>, <code>-dir-mode</code>, <code>-file-mode</code> and <code>-new-dir-mode</code>. </p>
<p> <code>genisoimage</code> will also run on Windows machines when compiled with Cygnus&#8217; cygwin (available from <i><a rel="nofollow" href="http://www.cygwin.com/">http://www.cygwin.com/</a></i>). Therefore most references in this man page to <i>Unix</i> can be replaced with <i>Win32</i>.</p>
<h2>OPTIONS</h2>
<p> Several options can be specified as defaults in a <i>.genisoimagerc</i> configuration file, as well as on the command line. If a parameter is specified in both places, the setting from the command line is used. For details on the format and possible locations of this file, see <code><a href="/docs/linux/man/5-genisoimagerc/">genisoimagerc</a></code>(5).</p>
<dl>
<dt><code>-abstract</code><i> file</i></p>
<dd> Specifies the abstract filename. There is space for 37 characters. Equivalent to <code>ABST</code> in the <i>.genisoimagerc</i> file.</p>
<dt><code>-A</code><i> application_id</i></p>
<dd> Specifies a text string that will be written into the volume header. This should describe the application that will be on the disc. There is space for 128 characters. Equivalent to <code>APPI</code> in the <i>.genisoimagerc</i> file.</p>
<dt><code>-allow-limited-size</code></p>
<dd> When processing files larger than 2GiB which cannot be easily represented in ISO9660, add them with a shrunk visible file size to ISO9660 and with the correct visible file size to the UDF system. The result is an inconsistent filesystem and users need to make sure that they really use UDF rather than ISO9660 driver to read a such disk. Implies enabling <code>-udf.</code></p>
<dt><code>-allow-leading-dots</code></p>
<dd>
<dt><code>-ldots</code></p>
<dd> Allow ISO9660 filenames to begin with a period. Usually, a leading dot is replaced with an underscore in order to maintain MS-DOS compatibility.<br />
 This violates the ISO9660 standard, but it happens to work on many systems. Use with caution.</p>
<dt><code>-allow-lowercase</code></p>
<dd> This options allows lowercase characters to appear in ISO9660 filenames.<br />
 This violates the ISO9660 standard, but it happens to work on some systems. Use with caution.</p>
<dt><code>-allow-multidot</code></p>
<dd> This options allows more than one dot to appear in ISO9660 filenames. A leading dot is not affected by this option, it may be allowed separately using <code>-allow-leading-dots</code>.<br />
 This violates the ISO9660 standard, but it happens to work on many systems. Use with caution.</p>
<dt><code>-biblio</code><i> file</i></p>
<dd> Specifies the bibliographic filename. There is space for 37 characters. Equivalent to <code>BIBL</code> in the <i>.genisoimagerc</i> file.</p>
<dt><code>-cache-inodes</code></p>
<dd>
<dt><code>-no-cache-inodes</code></p>
<dd> Enable or disable caching inode and device numbers to find hard links to files. If <code>genisoimage</code> finds a hard link (a file with multiple names), the file will also be hard-linked on the CD, so the file contents only appear once. This helps to save space. <code>-cache-inodes</code> is default on Unix-like operating systems, but <code>-no-cache-inodes</code> is default on some other systems such as Cygwin, because it is not safe to assume that inode numbers are unique on those systems. (Some versions of Cygwin create fake inode numbers using a weak hashing algorithm, which may produce duplicates.) If two files have the same inode number but are not hard links to the same file, <code>genisoimage -cache-inodes</code> will not behave correctly. <code>-no-cache-inodes</code> is safe in all situations, but in that case <code>genisoimage</code> cannot detect hard links, so the resulting CD image may be larger than necessary.</p>
<dt><code>-alpha-boot</code><i> alpha_boot_image</i></p>
<dd> Specifies the path and filename of the boot image to be used when making an Alpha/SRM bootable CD. The pathname must be relative to the source path specified to <code>genisoimage</code>.</p>
<dt><code>-hppa-bootloader</code><i> hppa_bootloader_image</i></p>
<dd> Specifies the path and filename of the boot image to be used when making an HPPA bootable CD. The pathname must be relative to the source path specified to <code>genisoimage</code>. Other options are required, at the very least a kernel filename and a boot command line. See the <code>HPPA NOTES</code> section below for more information.</p>
<dt><code>-hppa-cmdline</code><i> hppa_boot_command_line</i></p>
<dd> Specifies the command line to be passed to the HPPA boot loader when making a bootable CD. Separate the parameters with spaces or commas. More options must be passed to <code>genisoimage,</code> at the very least a kernel filename and the boot loader filename. See the <code>HPPA NOTES</code> section below for more information.</p>
<dt><code>-hppa-kernel-32</code><i> hppa_kernel_32</i></p>
<dd>
<dt><code>-hppa-kernel-64</code><i> hppa_kernel_64</i></p>
<dd> Specifies the path and filename of the 32-bit and/or 64-bit kernel images to be used when making an HPPA bootable CD. The pathnames must be relative to the source path specified to <code>genisoimage</code>. Other options are required, at the very least the boot loader filename and the boot command line. See the <code>HPPA NOTES</code> section below for more information.</p>
<dt><code>-hppa-ramdisk</code><i> hppa_ramdisk_image</i></p>
<dd> Specifies the path and filename of the ramdisk image to be used when making an HPPA bootable CD. The pathname must be relative to the source path specified to <code>genisoimage</code>. This parameter is optional. Other options are required, at the very least a kernel filename and the boot command line. See the <code>HPPA NOTES</code> section below for more information.</p>
<dt><code>-mips-boot</code><i> mips_boot_image</i></p>
<dd> Specifies the path and filename of the boot image to be used when making an SGI/big-endian MIPS bootable CD. The pathname must be relative to the source path specified to <code>genisoimage</code>. This option may be specified several times, to store up to 15 boot images.</p>
<dt><code>-mipsel-boot</code><i> mipsel_boot_image</i></p>
<dd> Specifies the path and filename of the boot image to be used when making an DEC/little-endian MIPS bootable CD. The pathname must be relative to the source path specified to <code>genisoimage</code>.</p>
<dt><code>-B</code><i> img_sun4,img_sun4c,img_sun4m,img_sun4d,img_sun4e</i></p>
<dd>
<dt><code>-sparc-boot</code><i> img_sun4,img_sun4c,img_sun4m,img_sun4d,img_sun4e</i></p>
<dd> Specifies a comma-separated list of boot images that are needed to make a bootable CD for SPARC systems. Partition 0 is used for the ISO9660 image, the first image file is mapped to partition 1. The comma-separated list may have up to 7 fields, including empty fields. This option is required to make a bootable CD for Sun SPARC systems. If <code>-B</code> or <code>-sparc-boot</code> has been specified, the first sector of the resulting image will contain a Sun disk label. This disk label specifies slice 0 for the ISO9660 image and slices 1 to 7 for the boot images that have been specified with this option. Byte offsets 512 to 8191 within each of the additional boot images must contain a primary boot that works for the appropriate SPARC architecture. The rest of each of the images usually contains a UFS filesystem used for the primary kernel boot stage.</p>
<dt>
<dd> The implemented boot method is the one found with SunOS 4.x and SunOS 5.x. However, it does not depend on SunOS internals but only on properties of the Open Boot prom, so it should be usable for any OS for SPARC systems. For more information also see the <code>NOTES</code> section below.</p>
<dt>
<dd> If the special filename <code>&#8230;</code> is used, the actual and all following boot partitions are mapped to the previous partition. If <code>genisoimage</code> is called with <code>-G</code><i> image </i><code>-B</code><i> &#8230;</i> all boot partitions are mapped to the partition that contains the ISO9660 filesystem image and the generic boot image that is located in the first 16 sectors of the disc is used for all architectures.</p>
<dt><code>-G</code><i> generic_boot_image</i></p>
<dd> Specifies the path and filename of the generic boot image to be used when making a generic bootable CD. The boot image will be placed on the first 16 sectors of the CD, before the ISO9660 primary volume descriptor. If this option is used together with <code>-sparc-boot</code>, the Sun disk label will overlay the first 512 bytes of the generic boot image.</p>
<dt><code>-b</code><i> eltorito_boot_image</i></p>
<dd> Specifies the path and filename of the boot image to be used when making an El Torito bootable CD for x86 PCs. The pathname must be relative to the source path specified to <code>genisoimage</code>. This option is required to make an El Torito bootable CD. The boot image must be exactly 1200 kB, 1440 kB or 2880 kB, and <code>genisoimage</code> will use this size when creating the output ISO9660 filesystem. The PC BIOS will use the image to emulate a floppy disk, so the first 512-byte sector should contain PC boot code. This will work, for example, if the boot image is a LILO-based boot floppy.</p>
<dt>
<dd> If the boot image is not an image of a floppy, you need to add either <code>-hard-disk-boot</code> or <code>-no-emul-boot</code>. If the system should not boot off the emulated disk, use <code>-no-boot</code>.</p>
<dt>
<dd> If <code>-sort</code> has not been specified, the boot images are sorted with low priority (+2) to the beginning of the medium. If you don&#8217;t like this, you need to specify a sort weight of 0 for the boot images.</p>
<dt><code>-eltorito-alt-boot</code></p>
<dd> Start with a new set of El Torito boot parameters. Up to 63 El Torito boot entries may be stored on a single CD.</p>
<dt><code>-hard-disk-boot</code></p>
<dd> Specifies that the boot image used to create El Torito bootable CDs is a hard disk image. The image must begin with a master boot record that contains a single partition.</p>
<dt><code>-no-emul-boot</code></p>
<dd> Specifies that the boot image used to create El Torito bootable CDs is a &quot;no emulation&quot; image. The system will load and execute this image without performing any disk emulation.</p>
<dt><code>-no-boot</code></p>
<dd> Specifies that the created El Torito CD should be marked as not bootable. The system will provide an emulated drive for the image, but will boot off a standard boot device.</p>
<dt><code>-boot-load-seg</code><i> segment_address</i></p>
<dd> Specifies the load segment address of the boot image for no-emulation El Torito CDs.</p>
<dt><code>-boot-load-size</code><i> load_sectors</i></p>
<dd> Specifies the number of &quot;virtual&quot; (512-byte) sectors to load in no-emulation mode. The default is to load the entire boot file. Some BIOSes may have problems if this is not a multiple of 4.</p>
<dt><code>-boot-info-table</code></p>
<dd> Specifies that a 56-byte table with information of the CD-ROM layout will be patched in at offset 8 in the boot file. If this option is given, the boot file is <i>modified in the source filesystem</i>, so make a copy of this file if it cannot be easily regenerated! See the <code>EL TORITO BOOT INFO TABLE</code> section for a description of this table.</p>
<dt><code>-C</code><i> last_sess_start,next_sess_start</i></p>
<dd> This option is needed to create a CD Extra or the image of a second session or a higher-level session for a multisession disc. <code>-C</code> takes two numbers separated by a comma. The first is the first sector in the last session of the disc that should be appended to. The second number is the starting sector number of the new session. The correct numbers may be retrieved by calling <code>wodim -msinfo &#8230;</code> If <code>-C</code> is used in conjunction with <code>-M</code>, <code>genisoimage</code> will create a filesystem image that is intended to be a continuation of the previous session. If <code>-C</code> is used without <code>-M</code>, <code>genisoimage</code> will create a filesystem image that is intended to be used for a second session on a CD Extra. This is a multisession CD that holds audio data in the first session and an ISO9660 filesystem in the second session.</p>
<dt><code>-c</code><i> boot_catalog</i></p>
<dd> Specifies the path and filename of the boot catalog, which is required for an El Torito bootable CD. The pathname must be relative to the source path specified to <code>genisoimage</code>. This file will be inserted into the output tree and not created in the source filesystem, so be sure the specified filename does not conflict with an existing file, or it will be excluded. Usually a name like <i>boot.catalog</i> is chosen.</p>
<dt>
<dd> If <code>-sort</code> has not been specified, the boot catalog sorted with low priority (+1) to the beginning of the medium. If you don&#8217;t like this, you need to specify a sort weight of 0 for the boot catalog.</p>
<dt><code>-check-oldnames</code></p>
<dd> Check all filenames imported from the old session for compliance with the ISO9660 file naming rules. Without this option, only names longer than 31 characters are checked, as these files are a serious violation of the ISO9660 standard.</p>
<dt><code>-check-session</code><i> file</i></p>
<dd> Check all old sessions for compliance with actual <code>genisoimage </code> ISO9660 file naming rules. This is a high-level option that combines <code>-M</code> <i>file</i> <code>-C 0,0 -check-oldnames</code>. For the parameter <i>file</i>, see the description of <code>-M</code>.</p>
<dt><code>-copyright</code><i> file</i></p>
<dd> Specifies copyright information, typically a filename on the disc. There is space for 37 characters. Equivalent to <code>COPY</code> in the <i>.genisoimagerc</i> file.</p>
<dt><code>-d</code></p>
<dd> Do not append a period to files that do not have one.<br />
 This violates the ISO9660 standard, but it happens to work on many systems. Use with caution.</p>
<dt><code>-D</code></p>
<dd> Do not use deep directory relocation, and instead just pack them in the way we see them.<br />
 If ISO9660:1999 has not been selected, this violates the ISO9660 standard, but it happens to work on many systems. Use with caution.</p>
<dt><code>-dir-mode</code><i> mode</i></p>
<dd> Overrides the mode of directories used to create the image to <i>mode</i>, specified as 4 digits of permission bits as in <code><a href="/docs/linux/man/1-chmod/">chmod</a></code>(1). This option automatically enables Rock Ridge extensions.</p>
<dt><code>-dvd-video</code></p>
<dd> Generate a DVD-Video compliant UDF filesystem. This is done by sorting the order of the content of the appropriate files and by adding padding between the files if needed. Note that the sorting only works if the DVD-Video filenames include uppercase characters only.</p>
<dt>
<dd> Note that in order to get a DVD-Video compliant filesystem image, you need to prepare a DVD-Video compliant directory tree. This requires a directory <code>VIDEO_TS</code> (all caps) in the root directory of the resulting DVD, and usually another directory <code>AUDIO_TS</code>. <code>VIDEO_TS</code> needs to include all needed files (filenames must be all caps) for a compliant DVD-Video filesystem.</p>
<dt><code>-f</code></p>
<dd> Follow symbolic links when generating the filesystem. When this option is not in use, symbolic links will be entered using Rock Ridge if enabled, otherwise they will be ignored.</p>
<dt><code>-file-mode</code><i> mode</i></p>
<dd> Overrides the mode of regular files used to create the image to <i>mode</i>, specified as 4 digits of permission bits as in <code><a href="/docs/linux/man/1-chmod/">chmod</a></code>(1). This option automatically enables Rock Ridge extensions.</p>
<dt><code>-gid</code><i> gid</i></p>
<dd> Overrides the group ID read from the source files to the value of <i>gid</i>. Specifying this option automatically enables Rock Ridge extensions.</p>
<dt><code>-gui</code></p>
<dd> Switch the behaviour for a GUI. This currently makes the output more verbose but may have other effects in the future.</p>
<dt><code>-graft-points</code></p>
<dd> Allow use of graft points for filenames. If this option is used, all filenames are checked for graft points. The filename is divided at the first unescaped equal sign. All occurrences of `\&#8217; and `=&#8217; characters must be escaped with `\&#8217; if <code>-graft-points</code> has been specified.</p>
<dt><code>-hide</code><i> glob</i></p>
<dd> Hide any files matching <i>glob</i>, a shell wildcard pattern, from being seen in the ISO9660 or Rock Ridge directory. <i>glob</i> may match any part of the filename or path. If <i>glob</i> matches a directory, the contents of that directory will be hidden. In order to match a directory name, make sure the pathname does not include a trailing `/&#8217; character. All the hidden files will still be written to the output CD image file. See also <code>-hide-joliet</code>, and <i>README.hide</i>. This option may be used multiple times.</p>
<dt><code>-hide-list</code><i> file</i></p>
<dd> A file containing a list of shell wildcards to be hidden. See <code>-hide</code>.</p>
<dt><code>-hidden</code><i> glob</i></p>
<dd> Add the hidden (existence) ISO9660 directory attribute for files and directories matching <i>glob</i>, a shell wildcard pattern. This attribute will prevent the files from being shown by some MS-DOS and Windows commands. <i>glob</i> may match any part of the filename or path. In order to match a directory name, make sure the pathname does not include a trailing `/&#8217; character. This option may be used multiple times.</p>
<dt><code>-hidden-list</code><i> file</i></p>
<dd> A file containing a list of shell wildcards to get the hidden attribute. See <code>-hidden</code>.</p>
<dt><code>-hide-joliet</code><i> glob</i></p>
<dd> Hide files and directories matching <i>glob</i>, a shell wildcard pattern, from being seen in the Joliet directory. <i>glob</i> may match any part of the filename or path. If <i>glob</i> matches a directory, the contents of that directory will be hidden. In order to match a directory name, make sure the pathname does not include a trailing `/&#8217; character. All the hidden files will still be written to the output CD image file. This option is usually used with <code>-hide</code>. See also <i>README.hide</i>. This option may be used multiple times.</p>
<dt><code>-hide-joliet-list</code><i> file</i></p>
<dd> A file containing a list of shell wildcards to be hidden from the Joliet tree. See <code>-hide-joliet</code>.</p>
<dt><code>-hide-joliet-trans-tbl</code></p>
<dd> Hide the <i>TRANS.TBL</i> files from the Joliet tree. These files usually don&#8217;t make sense in the Joliet world as they list the real name and the ISO9660 name which may both be different from the Joliet name.</p>
<dt><code>-hide-rr-moved</code></p>
<dd> Rename the directory <i>RR_MOVED</i> to <i>.rr_moved</i> in the Rock Ridge tree. It seems to be impossible to completely hide the <i>RR_MOVED</i> directory from the Rock Ridge tree. This option only makes the visible tree less confusing for people who don&#8217;t know what this directory is for. If you need to have no <i>RR_MOVED</i> directory at all, you should use <code>-D</code>. Note that if <code>-D</code> has been specified, the resulting filesystem is not ISO9660 level-1 compliant and will not be readable on MS-DOS. See also the <code>NOTES</code> section.</p>
<dt><code>-input-charset</code><i> charset</i></p>
<dd> Input charset that defines the characters used in local filenames. To get a list of valid charset names, call <code>genisoimage -input-charset help</code>. To get a 1:1 mapping, you may use <code>default</code> as charset name. The default initial values are <i>cp437</i> on DOS-based systems and <i>iso8859-1</i> on all other systems. See the <code>CHARACTER SETS</code> section below for more details.</p>
<dt><code>-output-charset</code><i> charset</i></p>
<dd> Output charset that defines the characters that will be used in Rock Ridge filenames. Defaults to the input charset. See <code>CHARACTER SETS</code> section below for more details.</p>
<dt><code>-iso-level</code><i> level</i></p>
<dd> Set the ISO9660 conformance level. Valid numbers are 1 to 4.</p>
<dt>
<dd> With level 1, files may only consist of one section and filenames are restricted to 8.3 characters.</p>
<dt>
<dd> With level 2, files may only consist of one section.</p>
<dt>
<dd> With level 3, no restrictions (other than ISO-9660:1988) do apply.</p>
<dt>
<dd> With all ISO9660 levels from 1 to 3, all filenames are restricted to uppercase letters, numbers and underscores (_). Filenames are limited to 31 characters, directory nesting is limited to 8 levels, and pathnames are limited to 255 characters.</p>
<dt>
<dd> Level 4 officially does not exist but <code>genisoimage</code> maps it to ISO-9660:1999, which is ISO9660 version 2.</p>
<dt>
<dd> With level 4, an enhanced volume descriptor with version number and file structure version number set to 2 is emitted. Directory nesting is not limited to 8 levels, there is no need for a file to contain a dot and the dot has no special meaning, filenames do not have version numbers, and filenames can be up to 207 characters long, or 197 characters if Rock Ridge is used.</p>
<dt>
<dd> When creating Version 2 images, <code>genisoimage</code> emits an enhanced volume descriptor, similar but not identical to a primary volume descriptor. Be careful not to use broken software to make ISO9660 images bootable by assuming a second PVD copy and patching this putative PVD copy into an El Torito VD.</p>
<dt><code>-J</code></p>
<dd> Generate Joliet directory records in addition to regular ISO9660 filenames. This is primarily useful when the discs are to be used on Windows machines. Joliet filenames are specified in Unicode and each path component can be up to 64 Unicode characters long. Note that Joliet is not a standard &#8212; only Microsoft Windows and Linux systems can read Joliet extensions. For greater portability, consider using both Joliet and Rock Ridge extensions.</p>
<dt><code>-joliet-long</code></p>
<dd> Allow Joliet filenames to be up to 103 Unicode characters, instead of 64. This breaks the Joliet specification, but appears to work. Use with caution.</p>
<dt><code>-jcharset</code><i> charset</i></p>
<dd> A combination of <code>-J -input-charset</code> <i>charset</i>. See the <code>CHARACTER SETS</code> section below for more details.</p>
<dt><code>-l</code></p>
<dd> Allow full 31-character filenames. Normally the ISO9660 filename will be in an 8.3 format which is compatible with MS-DOS, even though the ISO9660 standard allows filenames of up to 31 characters. If you use this option, the disc may be difficult to use on a MS-DOS system, but will work on most other systems. Use with caution.</p>
<dt><code>-L</code></p>
<dd> Outdated option; use <code>-allow-leading-dots</code> instead.</p>
<dt><code>-jigdo-jigdo</code><i> jigdo_file</i></p>
<dd> Produce a <code>jigdo</code> <i>.jigdo</i> metadata file as well as the filesystem image. See the <code>JIGDO NOTES</code> section below for more information.</p>
<dt><code>-jigdo-template</code><i> template_file</i></p>
<dd> Produce a <code>jigdo</code> <i>.template</i> file as well as the filesystem image. See the <code>JIGDO NOTES</code> section below for more information.</p>
<dt><code>-jigdo-min-file-size</code><i> size</i></p>
<dd> Specify the minimum size for a file to be listed in the <i>.jigdo</i> file. Default (and minimum allowed) is 1KB. See the <code>JIGDO NOTES</code> section below for more information.</p>
<dt><code>-jigdo-force-md5</code><i> path</i></p>
<dd> Specify a file pattern where files <i>must</i> be contained in the externally-supplied MD5 list as supplied by <code>-md5-list</code>. See the <code>JIGDO NOTES</code> section below for more information.</p>
<dt><code>-jigdo-exclude</code><i> path</i></p>
<dd> Specify a file pattern where files will not be listed in the <i>.jigdo</i> file. See the <code>JIGDO NOTES</code> section below for more information.</p>
<dt><code>-jigdo-map</code><i> path</i></p>
<dd> Specify a pattern mapping for the jigdo file (e.g. <i>Debian=/mirror/debian</i>). See the <code>JIGDO NOTES</code> section below for more information.</p>
<dt><code>-md5-list</code><i> md5_file</i></p>
<dd> Specify a file containing the MD5sums, sizes and pathnames of the files to be included in the <i>.jigdo</i> file. See the <code>JIGDO NOTES</code> section below for more information.</p>
<dt><code>-jigdo-template-compress</code><i> algorithm</i></p>
<dd> Specify a compression algorithm to use for template date. gzip and bzip2 are currently supported, and gzip is the default. See the <code>JIGDO NOTES</code> section below for more information.</p>
<dt><code>-log-file</code><i> log_file</i></p>
<dd> Redirect all error, warning and informational messages to <i>log_file</i> instead of the standard error.</p>
<dt><code>-m</code><i> glob</i></p>
<dd> Exclude files matching <i>glob</i>, a shell wildcard pattern, from being written to CD-ROM. <i>glob</i> may match either the filename component or the full pathname. This option may be used multiple times. For example: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;genisoimage -o rom -m&nbsp;&#8216;*.o&#8217;&nbsp;-m core -m foobar </p>
<p> would exclude all files ending in `.o&#8217;, or called <i>core</i> or <i>foobar</i> from the image. Note that if you had a directory called <i>foobar</i>, it too (and of course all its descendants) would be excluded.</p>
<dt><code>-exclude-list</code><i> file</i></p>
<dd> A file containing a list of shell wildcards to be excluded. See <code>-m</code>.</p>
<dt><code>-max-iso9660-filenames</code></p>
<dd> Allow ISO9660 filenames to be up to 37 characters long. This option enables <code>-N</code> as the extra name space is taken from the space reserved for file version numbers.<br />
 This violates the ISO9660 standard, but it happens to work on many systems. Although a conforming application needs to provide a buffer space of at least 37 characters, discs created with this option may cause a buffer overflow in the reading operating system. Use with extreme care.</p>
<dt><code>-M</code><i> path</i></p>
<dd>
<dt><code>-M</code><i> device</i></p>
<dd>
<dt><code>-dev</code><i> device</i></p>
<dd> Specifies path to existing ISO9660 image to be merged. The alternate form takes a SCSI device specifier that uses the same syntax as the <code>dev=</code> parameter of <code>wodim</code>. The output of <code>genisoimage</code> will be a new session which should get written to the end of the image specified in <code>-M</code>. Typically this requires multisession capability for the CD recorder used to write the image. This option may only be used in conjunction with <code>-C</code>.</p>
<dt><code>-N</code></p>
<dd> Omit version numbers from ISO9660 filenames.<br />
 This violates the ISO9660 standard, but no one really uses the version numbers anyway. Use with caution.</p>
<dt><code>-new-dir-mode</code><i> mode</i></p>
<dd> Specify the mode, a 4-digit number as used in <code><a href="/docs/linux/man/1-chmod/">chmod</a></code>(1), to use when creating new directories in the filesystem image. The default is 0555.</p>
<dt><code>-nobak</code></p>
<dd>
<dt><code>-no-bak</code></p>
<dd> Exclude backup files files on the ISO9660 filesystem; that is, filenames that contain the characters `~&#8217; or `#&#8217; or end in <i>.bak</i>. These are typically backup files for Unix text editors.</p>
<dt><code>-force-rr</code></p>
<dd> Do not use the automatic Rock Ridge attributes recognition for previous sessions. This can work around problems with images created by, e.g., NERO Burning ROM.</p>
<dt><code>-no-rr</code></p>
<dd> Do not use the Rock Ridge attributes from previous sessions. This may help to avoid problems when <code>genisoimage</code> finds illegal Rock Ridge signatures on an old session.</p>
<dt><code>-no-split-symlink-components</code></p>
<dd> Don&#8217;t split the symlink components, but begin a new Continuation Area (CE) instead. This may waste some space, but the SunOS 4.1.4 cdrom driver has a bug in reading split symlink components.</p>
<dt>
<dd> It is questionable whether this option is useful nowadays.</p>
<dt><code>-no-split-symlink-fields</code></p>
<dd> Don&#8217;t split the symlink fields, but begin a new Continuation Area (CE) instead. This may waste some space, but the SunOS 4.1.4 and Solaris 2.5.1 cdrom driver have a bug in reading split symlink fields (a `/&#8217; can be dropped).</p>
<dt>
<dd> It is questionable whether this option is useful nowadays.</p>
<dt><code>-o</code><i> filename</i></p>
<dd> Specify the output file for the the ISO9660 filesystem image. This can be a disk file, a tape drive, or it can correspond directly to the device name of the optical disc writer. If not specified, stdout is used. Note that the output can also be a block device for a regular disk partition, in which case the ISO9660 filesystem can be mounted normally to verify that it was generated correctly.</p>
<dt><code>-pad</code></p>
<dd> Pad the end of the whole image by 150 sectors (300 kB). This option is enabled by default. If used in combination with <code>-B</code>, padding is inserted between the ISO9660 partition and the boot partitions, such that the first boot partition starts on a sector number that is a multiple of 16.</p>
<dt>
<dd> The padding is needed as many operating systems (e.g. Linux) implement read-ahead bugs in their filesystem I/O. These bugs result in read errors on files that are located near the end of a track, particularly if the disc is written in Track At Once mode, or where a CD audio track follows the data track.</p>
<dt><code>-no-pad</code></p>
<dd> Do not pad the end by 150 sectors (300 kB) and do not make the the boot partitions start on a multiple of 16 sectors.</p>
<dt><code>-path-list</code><i> file</i></p>
<dd> A file containing a list of <i>pathspec</i> directories and filenames to be added to the ISO9660 filesystem. This list of pathspecs are processed after any that appear on the command line. If the argument is <i>&#8211;</i>, the list is read from the standard input.</p>
<dt><code>-P</code></p>
<dd> Outdated option; use <code>-publisher</code> instead.</p>
<dt><code>-publisher</code><i> publisher_id</i></p>
<dd> Specifies a text string that will be written into the volume header. This should describe the publisher of the CD-ROM, usually with a mailing address and phone number. There is space for 128 characters. Equivalent to <code>PUBL</code> in the <i>.genisoimagerc</i> file.</p>
<dt><code>-p</code><i> preparer_id</i></p>
<dd> Specifies a text string that will be written into the volume header. This should describe the preparer of the CD-ROM, usually with a mailing address and phone number. There is space for 128 characters. Equivalent to <code>PREP</code> in the <i>.genisoimagerc</i> file.</p>
<dt><code>-print-size</code></p>
<dd> Print estimated filesystem size in multiples of the sector size (2048 bytes) and exit. This option is needed for Disk At Once mode and with some CD-R drives when piping directly into <code>wodim</code>, cases where <code>wodim</code> needs to know the size of the filesystem image in advance. Old versions of <code>mkisofs</code> wrote this information (among other information) to <i>stderr</i>. As this turns out to be hard to parse, the number without any other information is now printed on <i>stdout</i> too. If you like to write a simple shell script, redirect <i>stderr</i> and catch the number from <i>stdout</i>. This may be done with: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cdblocks=`&nbsp;genisoimage -print-size -quiet &#8230;&nbsp;` </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;genisoimage &#8230; | wodim &#8230; tsize=${cdblocks}s &#8211;</p>
<dt><code>-quiet</code></p>
<dd> This makes <code>genisoimage</code> even less verbose. No progress output will be provided.</p>
<dt><code>-R</code></p>
<dd> Generate SUSP and RR records using the Rock Ridge protocol to further describe the files on the ISO9660 filesystem.</p>
<dt><code>-r</code></p>
<dd> This is like the -R option, but file ownership and modes are set to more useful values. The uid and gid are set to zero, because they are usually only useful on the author&#8217;s system, and not useful to the client. All the file read bits are set true, so that files and directories are globally readable on the client. If any execute bit is set for a file, set all of the execute bits, so that executables are globally executable on the client. If any search bit is set for a directory, set all of the search bits, so that directories are globally searchable on the client. All write bits are cleared, because the filesystem will be mounted read-only in any case. If any of the special mode bits are set, clear them, because file locks are not useful on a read-only filesystem, and set-id bits are not desirable for uid 0 or gid 0. When used on Win32, the execute bit is set on <i>all</i> files. This is a result of the lack of file permissions on Win32 and the Cygwin POSIX emulation layer. See also <code>-uid</code>, <code>-gid</code>, <code>-dir-mode</code>, <code>-file-mode</code> and <code>-new-dir-mode</code>.</p>
<dt><code>-relaxed-filenames</code></p>
<dd> Allows ISO9660 filenames to include all 7-bit ASCII characters except lowercase letters.<br />
 This violates the ISO9660 standard, but it happens to work on many systems. Use with caution.</p>
<dt><code>-root</code><i> dir</i></p>
<dd> Moves all files and directories into <i>dir</i> in the image. This is essentially the same as using <code>-graft-points</code> and adding <i>dir</i> in front of every pathspec, but is easier to use. <i>dir</i> may actually be several levels deep. It is created with the same permissions as other graft points.</p>
<dt><code>-old-root</code><i> dir</i></p>
<dd> This option is necessary when writing a multisession image and the previous (or even older) session was written with <code>-root</code> <i>dir</i>. Using a directory name not found in the previous session causes <code>genisoimage</code> to abort with an error. Without this option, <code>genisoimage</code> would not be able to find unmodified files and would be forced to write their data into the image once more. <code>-root</code> and <code>-old-root</code> are meant to be used together to do incremental backups. The initial session would e.g. use: <code>genisoimage -root backup_1</code> <i>dirs</i>. The next incremental backup with <code>genisoimage -root backup_2 -old-root backup_1</code> <i>dirs</i> would take another snapshot of these directories. The first snapshot would be found in <code>backup_1</code>, the second one in <code>backup_2</code>, but only modified or new files need to be written into the second session. Without these options, new files would be added and old ones would be preserved. But old ones would be overwritten if the file was modified. Recovering the files by copying the whole directory back from CD would also restore files that were deleted intentionally. Accessing several older versions of a file requires support by the operating system to choose which sessions are to be mounted.</p>
<dt><code>-sort</code><i> sort_file</i></p>
<dd> Sort file locations on the media. Sorting is controlled by a file that contains pairs of filenames and sorting offset weighting. If the weighting is higher, the file will be located closer to the beginning of the media, if the weighting is lower, the file will be located closer to the end of the media. There must be only one space or tabs character between the filename and the weight and the weight must be the last characters on a line. The filename is taken to include all the characters up to, but not including the last space or tab character on a line. This is to allow for space characters to be in, or at the end of a filename. This option does <code>not</code> sort the order of the filenames that appear in the ISO9660 directory. It sorts the order in which the file data is written to the CD image, which is useful in order to optimize the data layout on a CD. See <code>README.sort</code> for more details.</p>
<dt><code>-sparc-boot</code><i> img_sun4,img_sun4c,img_sun4m,img_sun4d,img_sun4e</i></p>
<dd> See <code>-B</code> above.</p>
<dt><code>-sparc-label</code><i> label</i></p>
<dd> Set the Sun disk label name for the Sun disk label that is created with <code>-sparc-boot</code>.</p>
<dt><code>-split-output</code></p>
<dd> Split the output image into several files of approximately 1 GB each. This helps to create DVD-sized ISO9660 images on operating systems without large file support. <code>wodim</code> will concatenate more than one file into a single track if writing to a DVD. To make <code>-split-output</code> work, <code>-o</code><i> filename</i> must be specified. The resulting output images will be named: <i>filename_00</i>, <i>filename_01</i>, <i>filename_02</i>&#8230;.</p>
<dt><code>-stream-media-size</code><i> #</i></p>
<dd> Select streaming operation and set the media size to # sectors. This allows you to pipe the output of the <code><a href="/docs/linux/man/1-tar/">tar</a></code>(1) program into <code>genisoimage</code> and to create an ISO9660 filesystem without the need of an intermediate tar archive file. If this option has been specified, <code>genisoimage</code> reads from <i>stdin </i> and creates a file with the name <i>STREAM.IMG</i>. The maximum size of the file (with padding) is 200 sectors less than the specified media size. If <code>-no-pad</code> has been specified, the file size is 50 sectors less than the specified media size. If the file is smaller, <code>genisoimage</code> will write padding. This may take awhile.</p>
<dt>
<dd> The option <code>-stream-media-size</code> creates simple ISO9660 filesystems only and may not used together with multisession or hybrid filesystem options.</p>
<dt><code>-stream-file-name</code><i> name</i></p>
<dd> Reserved for future use.</p>
<dt><code>-sunx86-boot</code><i> UFS_img,,,AUX1_img</i></p>
<dd> Specifies a comma-separated list of filesystem images that are needed to make a bootable CD for Solaris x86 systems.</p>
<dt>
<dd> Note that partition 1 is used for the ISO9660 image and that partition 2 is the whole disk, so partition 1 and 2 may not be used by external partition data. The first image file is mapped to partition 0. There may be empty fields in the comma-separated list, and list entries for partition 1 and 2 must be empty. The maximum number of supported partitions is 8 (although the Solaris x86 partition table could support up to 16 partitions), so it is impossible to specify more than 6 partition images. This option is required to make a bootable CD for Solaris x86 systems.</p>
<dt>
<dd> If <code>-sunx86-boot</code> has been specified, the first sector of the resulting image will contain a PC fdisk label with a Solaris type 0x82 fdisk partition that starts at offset 512 and spans the whole CD. In addition, for the Solaris type 0x82 fdisk partition, there is a SVr4 disk label at offset 1024 in the first sector of the CD. This disk label specifies slice 0 for the first (usually UFS type) filesystem image that is used to boot the PC and slice 1 for the ISO9660 image. Slice 2 spans the whole CD slice 3 &#8230; slice 7 may be used for additional filesystem images that have been specified with this option.</p>
<dt>
<dd> A Solaris x86 boot CD uses a 1024 byte sized primary boot that uses the <code>El-Torito no-emulation</code> boot mode and a secondary generic boot that is in CD sectors 1..15. For this reason, both <code>-b </code><i>bootimage</i><code> -no-emul-boot</code> and <code>-G</code><i> genboot</i> must be specified.</p>
<dt><code>-sunx86-label</code><i> label</i></p>
<dd> Set the SVr4 disk label name for the SVr4 disk label that is created with <code>-sunx86-boot</code>.</p>
<dt><code>-sysid</code><i> ID</i></p>
<dd> Specifies the system ID. There is space for 32 characters. Equivalent to <code>SYSI</code> in the <i>.genisoimagerc</i> file.</p>
<dt><code>-T</code></p>
<dd> Generate a file <i>TRANS.TBL</i> in each directory on the CD-ROM, which can be used on non-Rock Ridge-capable systems to help establish the correct filenames. There is also information present in the file that indicates the major and minor numbers for block and character devices, and each symlink has the name of the link file given.</p>
<dt><code>-table-name</code><i> table_name</i></p>
<dd> Alternative translation table filename (see above). Implies <code>-T</code>. If you are creating a multisession image you must use the same name as in the previous session.</p>
<dt><code>-ucs-level</code><i> level</i></p>
<dd> Set Unicode conformance level in the Joliet SVD. The default level is 3. It may be set to 1..3 using this option.</p>
<dt><code>-udf</code></p>
<dd> Include UDF filesystem support in the generated filesystem image. UDF support is currently in alpha status and for this reason, it is not possible to create UDF-only images. UDF data structures are currently coupled to the Joliet structures, so there are many pitfalls with the current implementation. There is no UID/GID support, there is no POSIX permission support, there is no support for symlinks. Note that UDF wastes the space from sector ~20 to sector 256 at the beginning of the disc in addition to the space needed for real UDF data structures.</p>
<dt><code>-uid</code><i> uid</i></p>
<dd> Overrides the uid read from the source files to the value of <i>uid</i>. Specifying this option automatically enables Rock Ridge extensions.</p>
<dt><code>-use-fileversion</code></p>
<dd> The option <code>-use-fileversion</code> allows <code>genisoimage</code> to use file version numbers from the filesystem. If the option is not specified, <code>genisoimage</code> creates a version number of 1 for all files. File versions are strings in the range <i>;1</i> to <i>;32767</i> This option is the default on VMS.</p>
<dt><code>-U</code></p>
<dd> Allows &quot;untranslated&quot; filenames, completely violating the ISO9660 standards described above. Enables the following flags: <code>-d -l -N -allow-leading-dots -relaxed-filenames</code> <code>-allow-lowercase -allow-multidot -no-iso-translate</code>. Allows more than one `.&#8217; character in the filename, as well as mixed-case filenames. This is useful on HP-UX, where the built-in <i>cdfs</i> filesystem does not recognize any extensions. Use with extreme caution.</p>
<dt><code>-no-iso-translate</code></p>
<dd> Do not translate the characters `#&#8217; and `~&#8217; which are invalid for ISO9660 filenames. Although invalid, these characters are often used by Microsoft systems.<br />
 This violates the ISO9660 standard, but it happens to work on many systems. Use with caution.</p>
<dt><code>-V</code><i> volid</i></p>
<dd> Specifies the volume ID (volume name or label) to be written into the master block. There is space for 32 characters. Equivalent to <code>VOLI</code> in the <i>.genisoimagerc</i> file. The volume ID is used as the mount point by the Solaris volume manager and as a label assigned to a disc on various other platforms such as Windows and Apple Mac OS.</p>
<dt><code>-volset</code><i> ID</i></p>
<dd> Specifies the volume set ID. There is space for 128 characters. Equivalent to <code>VOLS</code> in the <i>.genisoimagerc</i> file.</p>
<dt><code>-volset-size</code><i> #</i></p>
<dd> Sets the volume set size to #. The volume set size is the number of CDs that are in a CD volume set. A volume set is a collection of one or more volumes, on which a set of files is recorded.</p>
<dt>
<dd> Volume Sets are not intended to be used to create a set numbered CDs that are part of e.g. a Operation System installation set of CDs. Volume Sets are rather used to record a big directory tree that would not fit on a single volume. Each volume of a Volume Set contains a description of all the directories and files that are recorded on the volumes where the sequence numbers are less than, or equal to, the assigned Volume Set Size of the current volume.</p>
<dt>
<dd> <code>genisoimage</code> currently does not support a <code>-volset-size</code> that is larger than 1.</p>
<dt>
<dd> The option <code>-volset-size</code> must be specified before <code>-volset-seqno</code> on each command line.</p>
<dt><code>-volset-seqno</code><i> #</i></p>
<dd> Sets the volume set sequence number to #. The volume set sequence number is the index number of the current CD in a CD set. The option <code>-volset-size</code> must be specified before <code>-volset-seqno</code> on each command line.</p>
<dt><code>-v</code></p>
<dd> Verbose execution. If given twice on the command line, extra debug information will be printed.</p>
<dt><code>-x</code><i> glob</i></p>
<dd> Identical to <code>-m</code> <i>glob</i>.</p>
<dt><code>-z</code></p>
<dd> Generate special <i>RRIP</i> records for transparently compressed files. This is only of use and interest for hosts that support transparent decompression, such as Linux 2.4.14 or later. You must specify <code>-R</code> or <code>-r</code> to enable Rock Ridge, and generate compressed files using the <code>mkzftree</code> utility before running <code>genisoimage</code>. Note that transparent compression is a nonstandard Rock Ridge extension. The resulting disks are only transparently readable if used on Linux. On other operating systems you will need to call <code>mkzftree</code> by hand to decompress the files.</dl>
<h2>HFS OPTIONS</h2>
<dl>
<dt><code>-hfs</code></p>
<dd> Create an ISO9660/HFS hybrid CD. This option should be used in conjunction with the <code>-map</code>, <code>-magic</code> and/or the various <i>double dash</i> options given below.</p>
<dt><code>-apple</code></p>
<dd> Create an ISO9660 CD with Apple&#8217;s extensions. Similar to <code>-hfs</code>, except that the Apple Extensions to ISO9660 are added instead of creating an HFS hybrid volume. Former <code>genisoimage</code> versions did include Rock Ridge attributes by default if <code>-apple</code> was specified. This versions of <code>genisoimage</code> does not do this anymore. If you like to have Rock Ridge attributes, you need to specify this separately.</p>
<dt><code>-map</code><i> mapping_file</i></p>
<dd> Use the <i>mapping_file</i> to set the CREATOR and TYPE information for a file based on the filename&#8217;s extension. A filename is mapped only if it is not one of the know Apple/Unix file formats. See the <code>HFS CREATOR/TYPE</code> section below.</p>
<dt><code>-magic</code><i> magic_file</i></p>
<dd> The CREATOR and TYPE information is set by using a file&#8217;s <i>magic number</i> (usually the first few bytes of a file). The <i>magic_file</i> is only used if a file is not one of the known Apple/Unix file formats, or the filename extension has not been mapped using <code>-map</code>. See the <code>HFS CREATOR/TYPE</code> section below for more details.</p>
<dt><code>-hfs-creator</code><i> creator</i></p>
<dd> Set the default CREATOR for all files. Must be exactly 4 characters. See the <code>HFS CREATOR/TYPE</code> section below for more details.</p>
<dt><code>-hfs-type</code><i> type</i></p>
<dd> Set the default TYPE for all files. Must be exactly 4 characters. See the <code>HFS CREATOR/TYPE</code> section below for more details.</p>
<dt><code>-probe</code></p>
<dd> Search the contents of files for all the known Apple/Unix file formats. See the <code>HFS MACINTOSH FILE FORMATS</code> section below for more about these formats. However, the only way to check for <i>MacBinary</i> and <i>AppleSingle</i> files is to open and read them, so this option may increase processing time. It is better to use one or more <i>double dash</i> options given below if the Apple/Unix formats in use are known.</p>
<dt><code>-no-desktop</code></p>
<dd> Do not create (empty) Desktop files. New HFS Desktop files will be created when the CD is used on a Macintosh (and stored in the System Folder). By default, empty Desktop files are added to the HFS volume.</p>
<dt><code>-mac-name</code></p>
<dd> Use the HFS filename as the starting point for the ISO9660, Joliet and Rock Ridge filenames. See the <code>HFS MACINTOSH FILENAMES</code> section below for more information.</p>
<dt><code>-boot-hfs-file</code><i> driver_file</i></p>
<dd> Installs the <i>driver_file</i> that <i>may</i> make the CD bootable on a Macintosh. See the <code>HFS BOOT DRIVER</code> section below. (Alpha).</p>
<dt><code>-part</code></p>
<dd> Generate an HFS partition table. By default, no partition table is generated, but some older Macintosh CD-ROM drivers need an HFS partition table on the CD-ROM to be able to recognize a hybrid CD-ROM.</p>
<dt><code>-auto</code><i> AutoStart_file</i></p>
<dd> Make the HFS CD use the QuickTime 2.0 Autostart feature to launch an application or document. The given filename must be the name of a document or application located at the top level of the CD. The filename must be less than 12 characters. (Alpha).</p>
<dt><code>-cluster-size</code><i> size</i></p>
<dd> Set the size in bytes of the cluster or allocation units of PC Exchange files. Implies <code>&#8211;exchange</code>. See the <code>HFS MACINTOSH FILE FORMATS</code> section below.</p>
<dt><code>-hide-hfs</code><i> glob</i></p>
<dd> Hide <i>glob</i>, a shell wildcard pattern, from the HFS volume. The file or directory will still exist in the ISO9660 and/or Joliet directory. <i>glob</i> may match any part of the filename. Multiple globs may be excluded. Example: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;genisoimage -o rom -hfs -hide-hfs&nbsp;&#8216;*.o&#8217;&nbsp;-hide-hfs foobar </p>
<p> would exclude all files ending in `.o&#8217; or called <i>foobar</i> from the HFS volume. Note that if you had a directory called <i>foobar</i>, it too (and of course all its descendants) would be excluded. The <i>glob</i> can also be a path name relative to the source directories given on the command line. Example: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;genisoimage -o rom -hfs -hide-hfs src/html src </p>
<p> would exclude just the file or directory called <i>html</i> from the <i>src</i> directory. Any other file or directory called <i>html</i> in the tree will not be excluded. Should be used with <code>-hide</code> and/or <code>-hide-joliet</code>. In order to match a directory name, make sure the pattern does not include a trailing `/&#8217; character. See <i>README.hide</i> for more details.</p>
<dt><code>-hide-hfs-list</code><i> file</i></p>
<dd> Specify a file containing a list of wildcard patterns to be hidden as in <code>-hide-hfs</code>.</p>
<dt><code>-hfs-volid</code><i> hfs_volid</i></p>
<dd> Volume name for the HFS partition. This is the name that is assigned to the disc on a Macintosh and replaces the <i>volid</i> used with <code>-V</code>.</p>
<dt><code>-icon-position</code></p>
<dd> Use the icon position information, if it exists, from the Apple/Unix file. The icons will appear in the same position as they would on a Macintosh desktop. Folder location and size on screen, its scroll positions, folder View (view as Icons, Small Icons, etc.) are also preserved. (Alpha).</p>
<dt><code>-root-info</code><i> file</i></p>
<dd> Set the location, size on screen, scroll positions, folder View etc. for the root folder of an HFS volume. See <i>README.rootinfo</i> for more information. (Alpha)</p>
<dt><code>-prep-boot</code><i> file</i></p>
<dd> PReP boot image file. Up to 4 are allowed. See <i>README.prep_boot</i> for more information. (Alpha)</p>
<dt><code>-chrp-boot</code></p>
<dd> Add CHRP boot header.</p>
<dt><code>-input-hfs-charset</code><i> charset</i></p>
<dd> Input charset that defines the characters used in HFS filenames when used with <code>-mac-name</code>. The default charset is <i>cp10000</i> (Mac Roman). See the <code>CHARACTER SETS</code> and <code>HFS MACINTOSH FILENAMES</code> sections below for more details.</p>
<dt><code>-output-hfs-charset</code><i> charset</i></p>
<dd> Output charset that defines the characters that will be used in the HFS filenames. Defaults to the input charset. See the <code>CHARACTER SETS</code> section below for more details.</p>
<dt><code>-hfs-unlock</code></p>
<dd> By default, <code>genisoimage</code> will create an HFS volume that is locked. This option leaves the volume unlocked so that other applications (e.g. <code>hfsutils</code>) can modify the volume. See the <code>HFS PROBLEMS/LIMITATIONS</code> section below for warnings about using this option.</p>
<dt><code>-hfs-bless</code><i> folder_name</i></p>
<dd> &quot;Bless&quot; the given directory (folder). This is usually the <i>System Folder</i> and is used in creating HFS bootable CDs. The name of the directory must be the whole path name as <code>genisoimage</code> sees it. E.g., if the given pathspec is <i>./cddata</i> and the required folder is called <i>System Folder</i>, the whole path name is <i>&quot;/cddata/System Folder&quot;</i> (remember to use quotes if the name contains spaces).</p>
<dt><code>-hfs-parms</code><i> parameters</i></p>
<dd> Override certain parameters used to create the HFS filesystem. Unlikely to be used in normal circumstances. See the <i>libhfs_iso/hybrid.h</i> source file for details.</p>
<dt><code>&#8211;cap</code></p>
<dd> Look for AUFS CAP Macintosh files. Search for CAP Apple/Unix file formats only. Searching for the other possible Apple/Unix file formats is disabled, unless other <i>double dash</i> options are given.</p>
<dt><code>&#8211;netatalk</code></p>
<dd> Look for NETATALK Macintosh files</p>
<dt><code>&#8211;double</code></p>
<dd> Look for AppleDouble Macintosh files</p>
<dt><code>&#8211;ethershare</code></p>
<dd> Look for Helios EtherShare Macintosh files</p>
<dt><code>&#8211;ushare</code></p>
<dd> Look for IPT UShare Macintosh files</p>
<dt><code>&#8211;exchange</code></p>
<dd> Look for PC Exchange Macintosh files</p>
<dt><code>&#8211;sgi</code></p>
<dd> Look for SGI Macintosh files</p>
<dt><code>&#8211;xinet</code></p>
<dd> Look for XINET Macintosh files</p>
<dt><code>&#8211;macbin</code></p>
<dd> Look for MacBinary Macintosh files</p>
<dt><code>&#8211;single</code></p>
<dd> Look for AppleSingle Macintosh files</p>
<dt><code>&#8211;dave</code></p>
<dd> Look for Thursby Software Systems DAVE Macintosh files</p>
<dt><code>&#8211;sfm</code></p>
<dd> Look for Microsoft&#8217;s Services for Macintosh files (NT only) (Alpha)</p>
<dt><code>&#8211;osx-double</code></p>
<dd> Look for Mac OS X AppleDouble Macintosh files</p>
<dt><code>&#8211;osx-hfs</code></p>
<dd> Look for Mac OS X HFS Macintosh files</dl>
<h2>CHARACTER SETS</h2>
<p> <code>genisoimage</code> processes filenames in a POSIX-compliant way as strings of 8-bit characters. To represent all codings for all languages, 8-bit characters are not sufficient. Unicode or ISO-10646 define character codings that need at least 21 bits to represent all known languages. They may be represented with <i>UTF-32</i>, <i>UTF-16</i> or <i>UTF-8</i> coding. UTF-32 uses a plain 32-bit coding but seems to be uncommon. UTF-16 is used by Microsoft with Win32 with the disadvantage that 16-bit characters are not compliant with the POSIX filesystem interface. </p>
<p> Modern Unix operating systems may use UTF-8 coding for filenames. Each 32-bit character is represented by one or more 8-bit characters. If a character is coded in <i>ISO-8859-1</i> (used in Central Europe and North America) is maps 1:1 to a UTF-32 or UTF-16 coded Unicode character. If a character is coded in <i>7-Bit ASCII</i> (used in USA and other countries with limited character set) is maps 1:1 to a UTF-32, UTF-16 or UTF-8 coded Unicode character. Character codes that cannot be represented as a single byte in UTF-8 (if the value is &gt; 0x7F) use escape sequences that map to more than one 8-bit character. </p>
<p> If all operating systems used UTF-8, <code>genisoimage</code> would not need to recode characters in filenames. Unfortunately, Apple uses completely nonstandard codings and Microsoft uses a Unicode coding that is not compatible with the POSIX filename interface. </p>
<p> For all non-UTF-8-coded operating systems, the actual character that each byte represents depends on the <i>character set</i> or <i>codepage</i> (the name used by Microsoft) used by the local operating system &#8212; the characters in a character set will reflect the region or natural language set by the user. </p>
<p> Usually character codes 0x00-0x1f are control characters, codes 0x20-0x7f are the 7-bit ASCII characters and (on PCs and Macs) 0x80-0xff are used for other characters. </p>
<p> As there are a lot more than 256 characters/symbols in use, only a small subset are represented in a character set. Therefore the same character code may represent a different character in different character sets. So a filename generated, say in central Europe, may not display the same character when viewed on a machine in, say eastern Europe. </p>
<p> To make matters more complicated, different operating systems use different character sets for the region or language. For example, the character code for `&eacute;&#8217; (small e with acute accent) may be character code 0x82 on a PC, code 0x8e on a Macintosh, code 0xe9 on a Unix system in western Europe, and code 0x000e9 in Unicode. </p>
<p> As long as not all operating systems and applications use the same character set as the basis for filenames, it may be necessary to specify which character set your filenames use in and which character set the filenames should appear on the CD. </p>
<p> There are four options to specify the character sets you want to use:</p>
<dl>
<dt><code>-input-charset</code></p>
<dd> Defines the local character set you are using on your host machine. Any character set conversions that take place will use this character set as the starting point. The default input character sets are <i>cp437</i> on MS-DOS-based systems and <i>iso8859-1</i> on all other systems. If <code>-J</code> is given, the Unicode equivalents of the input character set will be used in the Joliet directory. <code>-jcharset</code> is the same as <code>-input-charset -J</code>.</p>
<dt><code>-output-charset</code></p>
<dd> Defines the character set that will be used with for the Rock Ridge names on the CD. Defaults to the input character set.</p>
<dt><code>-input-hfs-charset</code></p>
<dd> Defines the HFS character set used for HFS filenames decoded from any of the various Apple/Unix file formats. Only useful when used with <code>-mac-name</code>. See the <code>HFS MACINTOSH FILENAMES</code> for more information. Defaults to <i>cp10000</i> (Mac Roman).</p>
<dt><code>-output-hfs-charset</code></p>
<dd> Defines the HFS character set used to create HFS filenames from the input character set in use. In most cases this will be from the character set given with <code>-input-charset</code>. Defaults to the input HFS character set.</dl>
<p> There are a number of character sets built in to <code>genisoimage</code>. To get a listing, use <code>-input-charset help</code>. This list doesn&#8217;t include the charset derived from the current locale, if <code>genisoimage</code> is built with <i>iconv</i> support. </p>
<p> Additional character sets can be read from file for any of the character set options by giving a filename as the argument to the options. The given file will only be read if its name does not match one of the built-in character sets. </p>
<p> The format of the character set files is the same as the mapping files available from <i><a rel="nofollow" href="http://www.unicode.org/Public/MAPPINGS">http://www.unicode.org/Public/MAPPINGS</a></i>. This format is:</p>
<dl>
<dt>
<dd> Column #1 is the input byte code (in hex as 0xXX)<br />
 Column #2 is the Unicode (in hex as 0xXXXX)<br />
 The rest of the line is ignored.</dl>
<p> Any blank line, line without two (or more) columns in the above format or comments lines (starting with the # character) are ignored without any warnings. Any missing input code is mapped to Unicode character 0x0000. </p>
<p> Note that, while UTF-8 is supported, other Unicode encodings such as UCS-2/UTF-16 and UCS-4/UTF-32 are not, as POSIX operating systems cannot handle them natively. </p>
<p> A 1:1 character set mapping can be defined by using the keyword <i>default</i> as the argument to any of the character set options. This is the behaviour of old versions of <code>mkisofs</code>. </p>
<p> The ISO9660 filenames generated from the input filenames are not converted from the input character set. The ISO9660 character set is a very limited subset of the ASCII characters, so any conversion would be pointless. </p>
<p> Any character that <code>genisoimage</code> cannot convert will be replaced with a `_&#8217; character.</p>
<h2>HFS CREATOR/TYPE</h2>
<p> A Macintosh file has two properties associated with it which define which application created the file, the <i>CREATOR</i> and what data the file contains, the <i>TYPE</i>. Both are (exactly) 4 letter strings. Usually this allows a Macintosh user to double-click on a file and launch the correct application etc. The CREATOR and TYPE of a particular file can be found by using something like ResEdit (or similar) on a Macintosh. </p>
<p> The CREATOR and TYPE information is stored in all the various Apple/Unix encoded files. For other files it is possible to base the CREATOR and TYPE on the filename&#8217;s extension using a <i>mapping</i> file (with <code>-map</code>) and/or using the <i>magic number</i> (usually a <i>signature</i> in the first few bytes) of a file (with <code>-magic</code>). If both these options are given, their order on the command line is significant. If <code>-map</code> is given first, a filename extension match is attempted before a magic number match. However, if <code>-magic</code> is given first, a magic number match is attempted before a filename extension match. </p>
<p> If a mapping or magic file is not used, or no match is found, the default CREATOR and TYPE for all regular files can be set by using entries in the <i>.genisoimagerc</i> file or using <code>-hfs-creator</code> and/or <code>-hfs-type</code>, otherwise the default CREATOR and TYPE are <i>Unix</i> and <i>TEXT</i>. </p>
<p> The format of the <i>mapping</i> file is the same <i>afpfile</i> format as used by <code>aufs</code>. This file has five columns for the <i>extension</i>, <i>file translation</i>, <i>CREATOR</i>, <i>TYPE</i> and <i>Comment</i>. Lines starting with the `#&#8217; character are comment lines and are ignored. An example file would be like: </p>
<table>
<tr VALIGN=top>
<td COLSPAN=5># Example filename mapping file
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>#
</td>
</tr>
<tr VALIGN=top>
<td># EXTN</td>
<td>XLate</td>
<td>CREATOR</td>
<td>TYPE</td>
<td>Comment
</td>
</tr>
<tr VALIGN=top>
<td>.tif</td>
<td>Raw</td>
<td>&#8216;8BIM&#8217;</td>
<td>&#8216;TIFF&#8217;</td>
<td>&quot;Photoshop TIFF image&quot;
</td>
</tr>
<tr VALIGN=top>
<td>.hqx</td>
<td>Ascii</td>
<td>&#8216;BnHq&#8217;</td>
<td>&#8216;TEXT&#8217;</td>
<td>&quot;BinHex file&quot;
</td>
</tr>
<tr VALIGN=top>
<td>.doc</td>
<td>Raw</td>
<td>&#8216;MSWD&#8217;</td>
<td>&#8216;WDBN&#8217;</td>
<td>&quot;Word file&quot;
</td>
</tr>
<tr VALIGN=top>
<td>.mov</td>
<td>Raw</td>
<td>&#8216;TVOD&#8217;</td>
<td>&#8216;MooV&#8217;</td>
<td>&quot;QuickTime Movie&quot;
</td>
</tr>
<tr VALIGN=top>
<td>*</td>
<td>Ascii</td>
<td>&#8216;ttxt&#8217;</td>
<td>&#8216;TEXT&#8217;</td>
<td>&quot;Text file&quot;
</td>
</tr>
</table>
<p> Where:</p>
<dl>
<dt>
<dd> The first column <i>EXTN</i> defines the Unix filename extension to be mapped. The default mapping for any filename extension that doesn&#8217;t match is defined with the `*&#8217; character.</p>
<dt>
<dd> The <i>Xlate</i> column defines the type of text translation between the Unix and Macintosh file it is ignored by <code>genisoimage</code>, but is kept to be compatible with <code><a href="/docs/linux/man/1-aufs/">aufs</a></code>(1). Although <code>genisoimage</code> does not alter the contents of a file, if a binary file has its TYPE set as <i>TEXT</i>, it <i>may</i> be read incorrectly on a Macintosh. Therefore a better choice for the default TYPE may be <i>????</i>.</p>
<dt>
<dd> The <i>CREATOR</i> and <i>TYPE</i> keywords must be 4 characters long and enclosed in single quotes.</p>
<dt>
<dd> The comment field is enclosed in double quotes &#8212; it is ignored by <code>genisoimage</code>, but is kept to be compatible with <code>aufs</code>.</dl>
<p> The format of the <i>magic</i> file is almost identical to the <code><a href="/docs/linux/man/5-magic/">magic</a></code>(5) file used by the <code><a href="/docs/linux/man/1-file/">file</a></code>(1) command. </p>
<p> This file has four tab-separated columns for the <i>byte offset</i>, <i>type</i>, <i>test</i> and <i>message</i>. Lines starting with the `#&#8217; character are comment lines and are ignored. An example file would be like: </p>
<table>
<tr VALIGN=top>
<td COLSPAN=4># Example magic file
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>#
</td>
</tr>
<tr VALIGN=top>
<td># off</td>
<td>type</td>
<td>test</td>
<td>message
</td>
</tr>
<tr VALIGN=top>
<td>0</td>
<td>string</td>
<td>GIF8</td>
<td>8BIM GIFf GIF image
</td>
</tr>
<tr VALIGN=top>
<td>0</td>
<td>beshort</td>
<td>0xffd8</td>
<td>8BIM JPEG image data
</td>
</tr>
<tr VALIGN=top>
<td>0</td>
<td>string</td>
<td>SIT!</td>
<td>SIT! SIT! StuffIt Archive
</td>
</tr>
<tr VALIGN=top>
<td>0</td>
<td>string</td>
<td>\235</td>
<td>LZIV ZIVU standard Unix compress
</td>
</tr>
<tr VALIGN=top>
<td>0</td>
<td>string</td>
<td>\213</td>
<td>GNUz ZIVU gzip compressed data
</td>
</tr>
<tr VALIGN=top>
<td>0</td>
<td>string</td>
<td>%!</td>
<td>ASPS TEXT Postscript
</td>
</tr>
<tr VALIGN=top>
<td>0</td>
<td>string</td>
<td>%!</td>
<td>ASPS TEXT PC Postscript with a ^D to start
</td>
</tr>
<tr VALIGN=top>
<td>4</td>
<td>string</td>
<td>moov</td>
<td>txtt MooV QuickTime movie file (moov)
</td>
</tr>
<tr VALIGN=top>
<td>4</td>
<td>string</td>
<td>mdat</td>
<td>txtt MooV QuickTime movie file (mdat)
</td>
</tr>
</table>
<p> The format of the file is described in <code><a href="/docs/linux/man/5-magic/">magic</a></code>(5). The only difference here is that for each entry in the magic file, the <i>message</i> for the initial offset must be be 4 characters for the CREATOR followed by 4 characters for the TYPE &#8212; white space is optional between them. Any other characters on this line are ignored. Continuation lines (starting with a `&gt;&#8217;) are also ignored, i.e., only the initial offset lines are used. </p>
<p> Using <code>-magic</code> may significantly increase processing time as each file has to opened and read to find its magic number. </p>
<p> In summary, for all files, the default CREATOR is <i>Unix</i> and the default TYPE is <i>TEXT</i>. These can be changed by using entries in the <i>.genisoimagerc</i> file or by using <code>-hfs-creator</code> and/or <code>-hfs-type</code>. </p>
<p> If the a file is in one of the known Apple/Unix formats (and the format has been selected), the CREATOR and TYPE are taken from the values stored in the Apple/Unix file. </p>
<p> Other files can have their CREATOR and TYPE set from their filename extension (with <code>-map</code>), or their magic number (with <code>-magic</code>). If the default match is used in the <i>mapping</i> file, these values override the default CREATOR and TYPE. </p>
<p> A full CREATOR/TYPE database can be found at <i><a rel="nofollow" href="http://www.angelfire.com/il/szekely/">http://www.angelfire.com/il/szekely/</a></i>.</p>
<h2>HFS MACINTOSH FILE FORMATS</h2>
<p> Macintosh files have two parts called the <i>Data</i> and <i>Resource fork</i>. Either may be empty. Unix (and many other OSs) can only cope with files having one part (or fork). To add to this, Macintosh files have a number of attributes associated with them &#8212; probably the most important are the TYPE and CREATOR. Again, Unix has no concept of these types of attributes. </p>
<p> E.g., a Macintosh file may be a JPEG image where the image is stored in the Data fork and a desktop thumbnail stored in the Resource fork. It is usually the information in the data fork that is useful across platforms. </p>
<p> Therefore to store a Macintosh file on a Unix filesystem, a way has to be found to cope with the two forks and the extra attributes (which are referred to as the <i>Finder info</i>). Unfortunately, it seems that every software package that stores Macintosh files on Unix has chosen a completely different storage method. </p>
<p> The Apple/Unix formats that <code>genisoimage</code> (partially) supports are:</p>
<dl>
<dt>CAP AUFS format</p>
<dd> Data fork stored in a file. Resource fork in subdirectory <i>.resource</i> with same filename as data fork. Finder info in subdirectory <i>.finderinfo</i> with same filename.</p>
<dt>AppleDouble/Netatalk</p>
<dd> Data fork stored in a file. Resource fork stored in a file with same name prefixed with `%&#8217;. Finder info also stored in same `%&#8217; file. Netatalk uses the same format, but the resource fork/Finder info stored in subdirectory <i>.AppleDouble</i> with same filename as data fork.</p>
<dt>AppleSingle</p>
<dd> Data structures similar to above, except both forks and Finder info are stored in one file.</p>
<dt>Helios EtherShare</p>
<dd> Data fork stored in a file. Resource fork and Finder info together in subdirectory <i>.rsrc</i> with same filename as data fork.</p>
<dt>IPT UShare</p>
<dd> Like the EtherShare format, but the Finder info is stored slightly differently.</p>
<dt>MacBinary</p>
<dd> Both forks and Finder info stored in one file.</p>
<dt>Apple PC Exchange</p>
<dd> Used by Macintoshes to store Apple files on DOS (FAT) disks. Data fork stored in a file. Resource fork in subdirectory <i>resource.frk</i> (or <i>RESOURCE.FRK</i>). Finder info as one record in file <i>finder.dat</i> (or <i>FINDER.DAT</i>). Separate <i>finder.dat</i> for each data fork directory.</p>
<dt>
<dd> Note: <code>genisoimage</code> needs to know the native FAT cluster size of the disk that the PC Exchange files are on (or have been copied from). This size is given by <code>-cluster-size</code>. The cluster or allocation size can be found by using the DOS utility <code>chkdsk</code>.</p>
<dt>
<dd> May not work with PC Exchange v2.2 or higher files (available with MacOS 8.1). DOS media containing PC Exchange files should be mounted as type <i>msdos</i> (not <i>vfat</i>) when using Linux.</p>
<dt>SGI/XINET</p>
<dd> Used by SGI machines when they mount HFS disks. Data fork stored in a file. Resource fork in subdirectory <i>.HSResource</i> with same filename. Finder info as one record in file <i>.HSancillary</i>. Separate <i>.HSancillary</i> for each data fork directory.</p>
<dt>Thursby Software Systems DAVE</p>
<dd> Allows Macintoshes to store Apple files on SMB servers. Data fork stored in a file. Resource fork in subdirectory <i>resource.frk</i>. Uses the AppleDouble format to store resource fork.</p>
<dt>Services for Macintosh</p>
<dd> Format of files stored by NT Servers on NTFS filesystems. Data fork is stored as <i>filename</i>. Resource fork stored as a NTFS stream called <i>filename:AFP_Resource</i>. The Finder info is stored as a NTFS stream called <i>filename:Afp_AfpInfo</i>. NTFS streams are normally invisible to the user.</p>
<dt>
<dd> Warning: <code>genisoimage</code> only partially supports the SFM format. If an HFS file or folder stored on the NT server contains an illegal NT character in its name, NT converts these characters to <i>Private Use Unicode</i> characters. The characters are: &quot; * / &lt; &gt; ? \ | and a space or period if it is the last character of the filename, character codes 0x01 to 0x1f (control characters) and Apple&#8217;s apple logo.</p>
<dt>
<dd> Unfortunately, these private Unicode characters are not readable by the <code>genisoimage</code> NT executable. Therefore any file or directory name containing these characters will be ignored &#8212; including the contents of any such directory.</p>
<dt>Mac OS X AppleDouble</p>
<dd> When HFS/HFS+ files are copied or saved by Mac OS X on to a non-HFS filesystem (e.g. UFS, NFS etc.), the files are stored in AppleDouble format. Data fork stored in a file. Resource fork stored in a file with same name prefixed with `._&#8217;. Finder info also stored in same `._&#8217; file.</p>
<dt>Mac OS X HFS (Alpha)</p>
<dd> Not really an Apple/Unix encoding, but actual HFS/HFS+ files on a Mac OS X system. Data fork stored in a file. Resource fork stored in a pseudo file with the same name with the suffix <i>/rsrc</i>. The Finder info is only available via a Mac OS X library call.</p>
<dt>
<dd> See also <i>README.macosx</i>.</p>
<dt>
<dd> Only works when used on Mac OS X.</p>
<dt>
<dd> If a file is found with a zero length resource fork and empty finderinfo, it is assumed not to have any Apple/Unix encoding &#8212; therefore a TYPE and CREATOR can be set using other methods.</dl>
<p> <code>genisoimage</code> will attempt to set the CREATOR, TYPE, date and possibly other flags from the finder info. Additionally, if it exists, the Macintosh filename is set from the finder info, otherwise the Macintosh name is based on the Unix filename &#8212; see the <code>HFS MACINTOSH FILENAMES</code> section below. </p>
<p> When using <code>-apple</code>, the TYPE and CREATOR are stored in the optional System Use or <i>SUSP</i> field in the ISO9660 Directory Record &#8212; in much the same way as the Rock Ridge attributes are. In fact to make life easy, the Apple extensions are added at the beginning of the existing Rock Ridge attributes (i.e., to get the Apple extensions you get the Rock Ridge extensions as well). </p>
<p> The Apple extensions require the resource fork to be stored as an ISO9660 <i>associated</i> file. This is just like any normal file stored in the ISO9660 filesystem except that the associated file flag is set in the Directory Record (bit 2). This file has the same name as the data fork (the file seen by non-Apple machines). Associated files are normally ignored by other OSs </p>
<p> When using <code>-hfs</code>, the TYPE and CREATOR plus other finder info, are stored in a separate HFS directory, not visible on the ISO9660 volume. The HFS directory references the same data and resource fork files described above. </p>
<p> In most cases, it is better to use <code>-hfs</code> instead of <code>-apple</code>, as the latter imposes the limited ISO9660 characters allowed in filenames. However, the Apple extensions do give the advantage that the files are packed on the disk more efficiently and it may be possible to fit more files on a CD.</p>
<h2>HFS MACINTOSH FILENAMES</h2>
<p> Where possible, the HFS filename that is stored with an Apple/Unix file is used for the HFS part of the CD. However, not all the Apple/Unix encodings store the HFS filename with the finderinfo. In these cases, the Unix filename is used &#8212; with escaped special characters. Special characters include `/&#8217; and characters with codes over 127. </p>
<p> AUFS escapes these characters by using `:&#8217; followed by the character code as two hex digits. Netatalk and EtherShare have a similar scheme, but uses `%&#8217; instead of a `:&#8217;. </p>
<p> If <code>genisoimage</code> cannot find an HFS filename, it uses the Unix name, with any <i>%xx</i> or <i>:xx</i> characters (<i>xx</i> are two hex digits) converted to a single character code. If <i>xx</i> are not hex digits ([0-9a-fA-F]), they are left alone &#8212; although any remaining `:&#8217; is converted to `%&#8217;, as `:&#8217; is the HFS directory separator. Care must be taken, as an ordinary Unix file with <i>%xx</i> or <i>:xx</i> will also be converted. e.g. </p>
<table>
<tr VALIGN=top>
<td>This:2fFile</td>
<td>converted to This/File
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
</td>
</tr>
<tr VALIGN=top>
<td>This:File</td>
<td>converted to This%File
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
</td>
</tr>
<tr VALIGN=top>
<td>This:t7File</td>
<td>converted to This%t7File
</td>
</tr>
</table>
<p> Although HFS filenames appear to support uppercase and lowercase letters, the filesystem is case-insensitive, i.e., the filenames <i>aBc</i> and <i>AbC</i> are the same. If a file is found in a directory with the same HFS name, <code>genisoimage</code> will attempt to make a unique name by adding `_&#8217; characters to one of the filenames. </p>
<p> If an HFS filename exists for a file, <code>genisoimage</code> can use this name as the starting point for the ISO9660, Joliet and Rock Ridge filenames using <code>-mac-name</code>. Normal Unix files without an HFS name will still use their Unix name. e.g. </p>
<p> If a MacBinary (or PC Exchange) file is stored as <i>someimage.gif.bin</i> on the Unix filesystem, but contains a HFS file called <i>someimage.gif</i>, this is the name that would appear on the HFS part of the CD. However, as <code>genisoimage</code> uses the Unix name as the starting point for the other names, the ISO9660 name generated will probably be <i>SOMEIMAG.BIN</i> and the Joliet/Rock Ridge would be <i>someimage.gif.bin</i>. This option will use the HFS filename as the starting point and the ISO9660 name will probably be <i>SOMEIMAG.GIF</i> and the Joliet/Rock Ridge would be <i>someimage.gif</i>. </p>
<p> <code>-mac-name</code> will not currently work with <code>-T</code> &#8212; the Unix name will be used in the <i>TRANS.TBL</i> file, not the Macintosh name. </p>
<p> The character set used to convert any HFS filename to a Joliet/Rock Ridge filename defaults to <i>cp10000</i> (Mac Roman). The character set used can be specified using <code>-input-hfs-charset</code>. Other built-in HFS character sets are: <i>cp10006</i> (MacGreek), <i>cp10007</i> (MacCyrillic), <i>cp10029</i> (MacLatin2), <i>cp10079</i> (MacIcelandandic) and <i>cp10081</i> (MacTurkish). </p>
<p> Note: the character codes used by HFS filenames taken from the various Apple/Unix formats will not be converted as they are assumed to be in the correct Apple character set. Only the Joliet/Rock Ridge names derived from the HFS filenames will be converted. </p>
<p> The existing <code>genisoimage</code> code will filter out any illegal characters for the ISO9660 and Joliet filenames, but as <code>genisoimage</code> expects to be dealing directly with Unix names, it leaves the Rock Ridge names as is. But as `/&#8217; is a legal HFS filename character, <code>-mac-name</code> converts `/&#8217; to a `_&#8217; in Rock Ridge filenames. </p>
<p> If the Apple extensions are used, only the ISO9660 filenames will appear on the Macintosh. However, as the Macintosh ISO9660 drivers can use <i>Level 2</i> filenames, you can use options like <code>-allow-multidot</code> without problems on a Macintosh &#8212; still take care over the names, for example <i>this.file.name</i> will be converted to <i>THIS.FILE</i> i.e. only have one `.&#8217;, also filename <i>abcdefgh</i> will be seen as <i>ABCDEFGH</i> but <i>abcdefghi</i> will be seen as <i>ABCDEFGHI.</i> i.e. with a `.&#8217; at the end &#8212; don&#8217;t know if this is a Macintosh problem or a <code>genisoimage</code>/<code>mkhybrid</code> problem. All filenames will be in uppercase when viewed on a Macintosh. Of course, DOS/Win3.X machines will not be able to see Level 2 filenames&#8230;</p>
<h2>HFS CUSTOM VOLUME/FOLDER ICONS</h2>
<p> To give a HFS CD a custom icon, make sure the root (top level) folder includes a standard Macintosh volume icon file. To give a volume a custom icon on a Macintosh, an icon has to be pasted over the volume&#8217;s icon in the &quot;Get Info&quot; box of the volume. This creates an invisible file called <i>Icon</i> (`&#8217; is the carriage return character) in the root folder. </p>
<p> A custom folder icon is very similar &#8212; an invisible file called <i>Icon</i> exists in the folder itself. </p>
<p> Probably the easiest way to create a custom icon that <code>genisoimage</code> can use is to format a blank HFS floppy disk on a Mac and paste an icon to its &quot;Get Info&quot; box. If using Linux with the HFS module installed, mount the floppy:</p>
<dl>
<dt>
<dd> mount -t hfs /dev/fd0 /mnt/floppy</dl>
<p> The floppy will be mounted as a CAP filesystem by default. Then run <code>genisoimage</code> using something like:</p>
<dl>
<dt>
<dd> genisoimage &#8211;cap -o output source_dir /mnt/floppy</dl>
<p> If you are not using Linux, you can use <code>hfsutils</code> to copy the icon file from the floppy. However, care has to be taken, as the icon file contains a control character. For example:</p>
<dl>
<dt>
<dd> hmount /dev/fd0<br />
 hdir -a<br />
 hcopy -m Icon^V^M icon_dir/icon</dl>
<p> Where `^V^M&#8217; is control-V followed by control-M. Then run <code>genisoimage</code> by using something like:</p>
<dl>
<dt>
<dd> genisoimage &#8211;macbin -o output source_dir icon_dir</dl>
<p> The procedure for creating/using custom folder icons is very similar &#8212; paste an icon to folder&#8217;s &quot;Get Info&quot; box and transfer the resulting <i>Icon</i> file to the relevant directory in the <code>genisoimage</code> source tree. </p>
<p> You may want to hide the icon files from the ISO9660 and Joliet trees. </p>
<p> To give a custom icon to a Joliet CD, follow the instructions found at <i><a rel="nofollow" href="http://www.cdrfaq.org/faq03.html#S3-21-1">http://www.cdrfaq.org/faq03.html#S3-21-1</a></i>.</p>
<h2>HFS BOOT DRIVER</h2>
<p> It <i>may</i> be possible to make the hybrid CD bootable on a Macintosh. </p>
<p> A bootable HFS CD requires an Apple CD-ROM (or compatible) driver, a bootable HFS partition and the necessary System, Finder, etc. files. </p>
<p> A driver can be obtained from any other Macintosh bootable CD-ROM using the <code>apple_driver</code> utility. This file can then be used with <code>-boot-hfs-file</code>. </p>
<p> The HFS partition (i.e. the hybrid disk in our case) must contain a suitable System Folder, again from another CD-ROM or disk. </p>
<p> For a partition to be bootable, it must have its <i>boot block</i> set. The boot block is in the first two blocks of a partition. For a non-bootable partition the boot block is full of zeros. Normally, when a System file is copied to partition on a Macintosh disk, the boot block is filled with a number of required settings &#8212; unfortunately I don&#8217;t know the full spec for the boot block, so I&#8217;m guessing that the following will work. </p>
<p> Therefore, the utility <code>apple_driver</code> also extracts the boot block from the first HFS partition it finds on the given CD-ROM and this is used for the HFS partition created by <code>genisoimage</code>. </p>
<p> <i>Please note:</i> By using a driver from an Apple CD and copying Apple software to your CD, you become liable to obey Apple Computer, Inc. Software License Agreements.</p>
<h2>EL TORITO BOOT INFORMATION TABLE</h2>
<p> When <code>-boot-info-table</code> is given, <code>genisoimage</code> will modify the boot file specified by <code>-b</code> by inserting a 56-byte <i>boot information table</i> at offset 8 in the file. This modification is done in the source filesystem, so make sure you use a copy if this file is not easily recreated! This file contains pointers which may not be easily or reliably obtained at boot time. </p>
<p> The format of this table is as follows; all integers are in section 7.3.1 (&quot;little endian&quot;) format. </p>
<dl>
<dt>
<dd>
<pre>
Offset    Name           Size      Meaning
 8        bi_pvd         4 bytes   LBA of primary volume descriptor
12        bi_file        4 bytes   LBA of boot file
16        bi_length      4 bytes   Boot file length in bytes
20        bi_csum        4 bytes   32-bit checksum
24        bi_reserved    40 bytes  Reserved
</pre>
</dl>
<dl>
<dt>
<dd> The 32-bit checksum is the sum of all the 32-bit words in the boot file starting at byte offset 64. All linear block addresses (LBAs) are given in CD sectors (normally 2048 bytes).</dl>
<h2>HPPA NOTES</h2>
<p> To make a bootable CD for HPPA, at the very least a boot loader file (<code>-hppa-bootloader</code>), a kernel image file (32-bit, 64-bit, or both, depending on hardware) and a boot command line (<code>-hppa-cmdline</code>) must be specified. Some systems can boot either a 32- or a 64-bit kernel, and the firmware will choose one if both are present. Optionally, a ramdisk can be used for the root filesystem using <code>-hppa-cmdline</code>.</p>
<h2>JIGDO NOTES</h2>
<p> Jigdo is a tool to help in the distribution of large files like CD and DVD images; see <i><a rel="nofollow" href="http://atterer.org/jigdo/">http://atterer.org/jigdo/</a></i> for more details. Debian CDs and DVD ISO images are published on the web in jigdo format to allow end users to download them more efficiently. </p>
<p> To create jigdo and template files alongside the ISO image from <code>genisoimage</code>, you must first generate a list of the files that will be used, in the following format: </p>
<dl>
<dt>
<dd>
<pre>
MD5sum   File size  Path
32 chars 12 chars   to end of line
</pre>
</dl>
<dl>
<dt>
<dd></dl>
<p> The MD5sum must be written in standard hexadecimal notation, the file size must list the size of the file in bytes, and the path must list the absolute path to the file. For example: </p>
<pre>
00006dcd58ff0756c36d2efae21be376         14736  /mirror/debian/file1
000635c69b254a1be8badcec3a8d05c1        211822  /mirror/debian/file2
00083436a3899a09633fc1026ef1e66e         22762  /mirror/debian/file3
</pre>
<p> Once you have this file, call <code>genisoimage</code> with all of your normal command-line parameters. Specify the output filenames for the jigdo and template files using <code>-jigdo-jigdo</code> and <code>-jigdo-template</code>, and pass in the location of your MD5 list with <code>-md5-list</code>. </p>
<p> If there are files that you do NOT want to be added into the jigdo file (e.g. if they are likely to change often), specify them using -jigdo-exclude. If you want to verify some of the files as they are written into the image, specify them using -jigdo-force-md5. If any files don&#8217;t match, <code>genisoimage</code> will then abort. Both of these options take regular expressions as input. It is possible to restrict the set of files that will be used further based on size &#8212; use the -jigdo-min-file-size option. </p>
<p> Finally, the jigdo code needs to know how to map the files it is given onto a mirror-style configuration. Specify how to map paths using <code>-jigdo-map</code>. Using <i>Debian=/mirror/debian</i> will cause all paths starting with <i>/mirror/debian</i> to be mapped to <i>Debian:&lt;file&gt;</i> in the output jigdo file.</p>
<h2>EXAMPLES</h2>
<p> To create a vanilla ISO9660 filesystem image in the file <i>cd.iso</i>, where the directory <i>cd_dir</i> will become the root directory of the CD, call:</p>
<dl>
<dt>
<dd> % genisoimage -o cd.iso cd_dir</dl>
<p> To create a CD with Rock Ridge extensions of the source directory <i>cd_dir</i>:</p>
<dl>
<dt>
<dd> % genisoimage -o cd.iso -R cd_dir</dl>
<p> To create a CD with Rock Ridge extensions of the source directory <i>cd_dir</i> where all files have at least read permission and all files are owned by <i>root</i>, call:</p>
<dl>
<dt>
<dd> % genisoimage -o cd.iso -r cd_dir</dl>
<p> To write a tar archive directly to a CD that will later contain a simple ISO9660 filesystem with the tar archive call:</p>
<dl>
<dt>
<dd> % tar cf &#8211; . | genisoimage -stream-media-size 333000 | \ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;wodim dev=b,t,l -dao tsize=333000s &#8211;</dl>
<p> To create a HFS hybrid CD with the Joliet and Rock Ridge extensions of the source directory <i>cd_dir</i>:</p>
<dl>
<dt>
<dd> % genisoimage -o cd.iso -R -J -hfs cd_dir</dl>
<p> To create a HFS hybrid CD from the source directory <i>cd_dir</i> that contains Netatalk Apple/Unix files:</p>
<dl>
<dt>
<dd> % genisoimage -o cd.iso &#8211;netatalk cd_dir</dl>
<p> To create a HFS hybrid CD from the source directory <i>cd_dir</i>, giving all files CREATOR and TYPES based on just their filename extensions listed in the file &quot;mapping&quot;.:</p>
<dl>
<dt>
<dd> % genisoimage -o cd.iso -map mapping cd_dir</dl>
<p> To create a CD with the Apple Extensions to ISO9660, from the source directories <i>cd_dir</i> and <i>another_dir</i>. Files in all the known Apple/Unix format are decoded and any other files are given CREATOR and TYPE based on their magic number given in the file <i>magic</i>:</p>
<dl>
<dt>
<dd> % genisoimage -o cd.iso -apple -magic magic -probe \ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cd_dir another_dir</dl>
<p> The following example puts different files on the CD that all have the name README, but have different contents when seen as a ISO9660/Rock Ridge, Joliet or HFS CD. </p>
<p> Current directory contains:</p>
<dl>
<dt>
<dd> % ls -F<br />
 README.hfs README.joliet README.Unix cd_dir/</dl>
<p> The following command puts the contents of the directory <i>cd_dir</i> on the CD along with the three README files &#8212; but only one will be seen from each of the three filesystems:</p>
<dl>
<dt>
<dd> % genisoimage -o cd.iso -hfs -J -r -graft-points \ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;-hide README.hfs -hide README.joliet&nbsp;\ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;-hide-joliet README.hfs -hide-joliet README.Unix&nbsp;\ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;-hide-hfs README.joliet -hide-hfs README.Unix&nbsp;\ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;README=README.hfs README=README.joliet&nbsp;\ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;README=README.Unix cd_dir</dl>
<p> i.e. the file README.hfs will be seen as README on the HFS CD and the other two README files will be hidden. Similarly for the Joliet and ISO9660/Rock Ridge CD. </p>
<p> There are probably all sorts of strange results possible with combinations of the hide options &#8230;</p>
<h2>NOTES</h2>
<p> <code>genisoimage</code> may safely be installed suid root. This may be needed to allow <code>genisoimage</code> to read the previous session when creating a multisession image. </p>
<p> If <code>genisoimage </code> is creating a filesystem image with Rock Ridge attributes and the directory nesting level of the source directory tree is too much for ISO9660, <code>genisoimage </code> will do deep directory relocation. This results in a directory called <code>RR_MOVED</code> in the root directory of the CD. You cannot avoid this directory. </p>
<p> Many boot code options for different platforms are mutualy exclusive because the boot blocks cannot coexist, ie. different platforms share the same data locations in the image. See <a rel="nofollow" href="http://lists.debian.org/debian-cd/2006/12/msg00109.html">http://lists.debian.org/debian-cd/2006/12/msg00109.html</a> for details.</p>
<h2>BUGS</h2>
<p> Any files that have hard links to files not in the tree being copied to the ISO9660 filesystem will have an incorrect file reference count. </p>
<p> Does not check for SUSP record(s) in `.&#8217; entry of the root directory to verify the existence of Rock Ridge enhancements. This problem is present when reading old sessions while adding data in multisession mode. </p>
<p> Does not properly read relocated directories in multisession mode when adding data. Any relocated deep directory is lost if the new session does not include the deep directory. </p>
<p> Does not re-use <i>RR_MOVED</i> when doing multisession from <i>TRANS.TBL</i>. </p>
<p> Does not create whole_name entry for <i>RR_MOVED</i> in multisession mode. </p>
<p> There may be other bugs. Please, report them to the maintainers.</p>
<h2>HFS PROBLEMS/LIMITATIONS</h2>
<p> I have had to make several assumptions on how I expect the modified libhfs routines to work, however there may be situations that either I haven&#8217;t thought of, or come across when these assumptions fail. Therefore I can&#8217;t guarantee that <code>genisoimage</code> will work as expected (although I haven&#8217;t had a major problem yet). Most of the HFS features work fine, but some are not fully tested. These are marked as <i>Alpha</i> above. </p>
<p> Although HFS filenames appear to support uppercase and lowercase letters, the filesystem is case-insensitive, i.e., the filenames <i>aBc</i> and AbC are the same. If a file is found in a directory with the same HFS name, <code>genisoimage</code> will attempt to make a unique name by adding `_&#8217; characters to one of the filenames. </p>
<p> HFS file/directory names that share the first 31 characters have `_N&#8217; (a decimal number) substituted for the last few characters to generate unique names. </p>
<p> Care must be taken when &quot;grafting&quot; Apple/Unix files or directories (see above for the method and syntax involved). It is not possible to use a new name for an Apple/Unix encoded file/directory. e.g. If a Apple/Unix encoded file called <i>oldname</i> is to added to the CD, you cannot use the command line:</p>
<dl>
<dt>
<dd> genisoimage -o output.raw -hfs -graft-points newname=oldname cd_dir</dl>
<p> <code>genisoimage</code> will be unable to decode <i>oldname</i>. However, you can graft Apple/Unix encoded files or directories as long as you do not attempt to give them new names as above. </p>
<p> When creating an HFS volume with the multisession options, <code>-M</code> and <code>-C</code>, only files in the last session will be in the HFS volume. i.e. <code>genisoimage</code> cannot <i>add</i> existing files from previous sessions to the HFS volume. </p>
<p> However, if each session is created with <code>-part</code>, each session will appear as separate volumes when mounted on a Mac. In this case, it is worth using <code>-V</code> or <code>-hfs-volid</code> to give each session a unique volume name, otherwise each &quot;volume&quot; will appear on the Desktop with the same name. </p>
<p> Symbolic links (as with all other non-regular files) are not added to the HFS directory. </p>
<p> Hybrid volumes may be larger than pure ISO9660 volumes containing the same data. In some cases (e.g. DVD sized volumes) the difference can be significant. As an HFS volume gets bigger, so does the allocation block size (the smallest amount of space a file can occupy). For a 650MB CD, the allocation block is 10kB, for a 4.7GB DVD it will be about 70kB. </p>
<p> The maximum number of files in an HFS volume is about 65500 &#8212; although the real limit will be somewhat less than this. </p>
<p> The resulting hybrid volume can be accessed on a Unix machine by using the hfsutils routines. However, no changes can be made to the volume as it is set as <code>locked.</code> The option <code>-hfs-unlock</code> will create an output image that is unlocked &#8212; however no changes should be made to the contents of the volume (unless you really know what you are doing) as it&#8217;s not a &quot;real&quot; HFS volume. </p>
<p> <code>-mac-name</code> will not currently work with <code>-T</code> &#8212; the Unix name will be used in the <i>TRANS.TBL</i> file, not the Macintosh name. </p>
<p> Although <code>genisoimage</code> does not alter the contents of a file, if a binary file has its TYPE set as <i>TEXT</i>, it <i>may</i> be read incorrectly on a Macintosh. Therefore a better choice for the default TYPE may be <i>????</i>. </p>
<p> <code>-mac-boot-file</code> may not work at all&#8230; </p>
<p> May not work with PC Exchange v2.2 or higher files (available with MacOS 8.1). DOS media containing PC Exchange files should be mounted as type <code>msdos</code> (not <code>vfat</code>) when using Linux. </p>
<p> The SFM format is only partially supported &#8212; see <code>HFS MACINTOSH FILE FORMATS</code> section above. </p>
<p> It is not possible to use <code>-sparc-boot</code> or <code>-generic-boot</code> with <code>-boot-hfs-file</code> or <code>-prep-boot</code>. </p>
<p> <code>genisoimage</code> should be able to create HFS hybrid images over 4Gb, although this has not been fully tested.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-genisoimagerc/">genisoimagerc</a></code>(5), <code><a href="/docs/linux/man/1-wodim/">wodim</a></code>(1), <code><a href="/docs/linux/man/8-mkzftree/">mkzftree</a></code>(8), <code><a href="/docs/linux/man/5-magic/">magic</a></code>(5).</p>
<h2>AUTHORS</h2>
<p> <code>genisoimage</code> is derived from <code>mkisofs</code> from the <code>cdrtools 2.01.01a08</code> package from May 2006 (with few updates extracted from cdrtools 2.01.01a24 from March 2007) from .IR <a rel="nofollow" href="http://cdrecord.berlios.de/">http://cdrecord.berlios.de/</a> , but is now part of the <code>cdrkit</code> suite, maintained by Joerg Jaspert, Eduard Bloch, Steve McIntyre, Peter Samuelson, Christian Fromme, Ben Hutchings, and other contributors. The maintainers can be contacted at <i>debburn-devel [at] lists.alioth.debian.org</i>, or see the <code>cdrkit</code> project web site at <i><a rel="nofollow" href="http://www.cdrkit.org/">http://www.cdrkit.org/</a></i>. </p>
<p> Eric Youngdale wrote the first versions (1993-1998) of <code>mkisofs</code>. J&ouml;rg Schilling wrote the SCSI transport library and its interface, and has maintained <code>mkisofs</code> since 1999. James Pearson wrote the HFS hybrid code, using <i>libhfs</i> by Robert Leslie. Pearson, Schilling, Jungshik Shin and Jaakko Heinonen contributed to the character set conversion code. The <code>cdrkit</code> maintainers have maintained <code>genisoimage</code> since 2006. </p>
<pre>
Copyright 1993-1998 by Yggdrasil Computing, Inc.
Copyright 1996-1997 by Robert Leslie
Copyright 1997-2001 by James Pearson
Copyright 1999-2006 by J&ouml;rg Schilling
Copyright 2007 by J&ouml;rg Schilling (originating few updates)
Copyright 2002-2003 by Jungshik Shin
Copyright 2003 by Jaakko Heinonen
Copyright 2006 by the Cdrkit maintainers
</pre>
<p> If you want to take part in the development of <code>genisoimage</code>, you may join the <code>cdrkit</code> developer mailing list by following the instructions on <i><a rel="nofollow" href="http://alioth.debian.org/mail/?group_id=31006">http://alioth.debian.org/mail/?group_id=31006</a></i>. The email address of the list is <i>debburn-devel [at] lists.alioth.debian.org</i>. This is also the address for user support questions. Note that <code>cdrkit</code> and <code>cdrtools</code> are not affiliated. </p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> UNIX is a registered trademark of The Open Group in the US and other countries. </p>
<h2>Index</h2>
