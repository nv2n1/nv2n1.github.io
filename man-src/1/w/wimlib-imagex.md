---
title: "wimlib-imagex(1)"
name: "wimlib-imagex"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wimlib-imagex/"
description: "wimlib-imagex – Extract, create, modify, or mount a WIM (Windows Imaging Format) archive"
---

<h2>NAME</h2>
<p> wimlib-imagex &#8211; Extract, create, modify, or mount a WIM (Windows Imaging Format) archive</p>
<h2>SYNOPSIS</h2>
<p> <code>wimlib-imagex append</code> <i>arguments&#8230;</i><br />
 <code>wimlib-imagex apply</code> <i>arguments&#8230;</i><br />
 <code>wimlib-imagex capture</code> <i>arguments&#8230;</i><br />
 <code>wimlib-imagex delete</code> <i>arguments&#8230;</i><br />
 <code>wimlib-imagex dir</code> <i>arguments&#8230;</i><br />
 <code>wimlib-imagex export</code> <i>arguments&#8230;</i><br />
 <code>wimlib-imagex extract</code> <i>arguments&#8230;</i><br />
 <code>wimlib-imagex info</code> <i>arguments&#8230;</i><br />
 <code>wimlib-imagex join</code> <i>arguments&#8230;</i><br />
 <code>wimlib-imagex mount</code> <i>arguments&#8230;</i><br />
 <code>wimlib-imagex mountrw</code> <i>arguments&#8230;</i><br />
 <code>wimlib-imagex optimize</code> <i>arguments&#8230;</i><br />
 <code>wimlib-imagex split</code> <i>arguments&#8230;</i><br />
 <code>wimlib-imagex unmount</code> <i>arguments&#8230;</i><br />
 <code>wimlib-imagex update</code> <i>arguments&#8230;</i><br />
 <code>wimlib-imagex verify</code> <i>arguments&#8230;</i></p>
<h2>DESCRIPTION</h2>
<p> <code>wimlib-imagex</code> deals with archives in the Windows Imaging Format (WIM). Its interface is similar to Microsoft&#8217;s ImageX, but <code>wimlib-imagex</code> is cross-platform and has useful improvements and extensions. </p>
<p> To do its work, <code>wimlib-imagex</code> uses <code>wimlib</code>, an open source C library that provides interfaces for manipulating WIM archives. wimlib is completely independent from the equivalent Microsoft implementation (WIMGAPI, or wimgapi.dll). You can use wimlib in your own programs, although for command-line use <code>wimlib-imagex</code> already provides access to most of wimlib&#8217;s functionality.</p>
<h2>BACKGROUND INFORMATION</h2>
<p> The Windows Imaging Format (WIM) was designed by Microsoft primarily for archiving Windows filesystems, such as NTFS. However, it can be used on other platforms as well, with some limitations. A WIM archive contains one or more images, each of which is a logically independent directory tree. Images are indexed starting from 1, and each may also have a name. File data is stored as content-addressable &quot;blobs&quot; that are deduplicated across the entire archive. Data may be compressed using one of several compression algorithms. </p>
<p> An update of the WIM format released with Windows 8 features solid compression using the LZMS compression algorithm. Such files are also called &quot;ESD files&quot; and may carry the extension .esd instead of .wim. <code>wimlib-imagex</code> v1.6.0 and later supports these new files, unless they are encrypted.</p>
<h2>COMMANDS</h2>
<p> <code>wimlib-imagex</code> accepts one of a number of commands (listed above in <code>SYNOPSYS</code>), and additional arguments depending on the specific command. Although <code>wimlib-imagex</code> will print usage information with <code>&#8211;help</code> or if you invoke it incorrectly, the full documentation for each <code>wimlib-imagex</code> command can be found in the appropriate manual page. </p>
<p> Note: to save typing, if appropriate hard links or batch files have been installed, a command <code>wimlib-imagex </code><i>COMMAND</i> can also be accessed as simply <code>wim</code><i>COMMAND</i>; for example, <code>wimapply</code> for <code>wimlib-imagex apply</code>.</p>
<h2>GENERAL FEATURES</h2>
<p> The following are some of the general features, or use cases, currently supported by <code>wimlib-imagex</code>, and pointers to the relevant commands:</p>
<dl>
<dt>&bull;</p>
<dd> Display information about a WIM file<br />
&nbsp;<wbr>(<code>wimlib-imagex info</code>)</p>
<dt>&bull;</p>
<dd> List the files in a WIM image<br />
&nbsp;<wbr>(<code>wimlib-imagex dir</code>)</p>
<dt>&bull;</p>
<dd> Extract, or &quot;apply&quot;, a full WIM image<br />
&nbsp;<wbr>(<code>wimlib-imagex apply</code>)</p>
<dt>&bull;</p>
<dd> Extract files or directories from a WIM image<br />
&nbsp;<wbr>(<code>wimlib-imagex extract</code>)</p>
<dt>&bull;</p>
<dd> Capture a WIM image and save it to a new WIM file<br />
&nbsp;<wbr>(<code>wimlib-imagex capture</code>)</p>
<dt>&bull;</p>
<dd> Capture a WIM image and append it to an existing WIM file<br />
&nbsp;<wbr>(<code>wimlib-imagex append</code>)</p>
<dt>&bull;</p>
<dd> Modify a WIM image by adding, deleting, or renaming files<br />
&nbsp;<wbr>(<code>wimlib-imagex update</code>)</p>
<dt>&bull;</p>
<dd> (Linux only) Mount a WIM image read-only<br />
&nbsp;<wbr>(<code>wimlib-imagex mount</code>)</p>
<dt>&bull;</p>
<dd> (Linux only) Mount a WIM image read-write<br />
&nbsp;<wbr>(<code>wimlib-imagex mountrw</code>)</p>
<dt>&bull;</p>
<dd> Delete an image from a WIM file<br />
&nbsp;<wbr>(<code>wimlib-imagex delete</code>)</p>
<dt>&bull;</p>
<dd> Export image(s) from a WIM file<br />
&nbsp;<wbr>(<code>wimlib-imagex export</code>)</p>
<dt>&bull;</p>
<dd> Change the name or description of a WIM image<br />
&nbsp;<wbr>(<code>wimlib-imagex info</code>)</p>
<dt>&bull;</p>
<dd> Change the bootable image index of a WIM file<br />
&nbsp;<wbr>(<code>wimlib-imagex info</code>)</p>
<dt>&bull;</p>
<dd> Rebuild, and optionally recompress, a WIM file<br />
&nbsp;<wbr>(<code>wimlib-imagex optimize</code>)</p>
<dt>&bull;</p>
<dd> Split a WIM file into multiple parts<br />
&nbsp;<wbr>(<code>wimlib-imagex split</code>)</p>
<dt>&bull;</p>
<dd> Join a split WIM<br />
&nbsp;<wbr>(<code>wimlib-imagex join</code>)</p>
<dt>&bull;</p>
<dd> Verify a WIM file<br />
&nbsp;<wbr>(<code>wimlib-imagex verify</code>)</dl>
<h2>DETAILED FEATURES</h2>
<p> This section presents some of the interesting features of <code>wimlib-imagex</code> in more detail.</p>
<dl>
<dt>&bull;</p>
<dd> Multi-platform support. <code>wimlib-imagex</code> is supported on both UNIX-like systems (mainly Linux, but also FreeBSD, Mac OS X, etc.) and Windows, and most code is shared among all platforms. However, platform-specific features are supported when possible.</p>
<dt>&bull;</p>
<dd> On UNIX-like systems, integration with libntfs-3g allows capturing a WIM image directly from a block device containing an NTFS volume, or applying a WIM image directly to a block device containing an NTFS volume. This allows saving and restoring NTFS-specific data, such as security descriptors and named data streams, which would otherwise only be supported on Windows.</p>
<dt>&bull;</p>
<dd> Long path support on Windows. <code>wimlib-imagex</code> can capture and apply files with paths exceeding the MAX_PATH (260 character) limitation of the Win32 subsystem.</p>
<dt>&bull;</p>
<dd> Non-Administrator support on Windows. You can run <code>wimlib-imagex</code> without Administrator rights, subject to some limitations.</p>
<dt>&bull;</p>
<dd> Support for WIM integrity tables. An integrity table is a list of SHA-1 message digests appended to the end of a WIM file which gives checksums over the WIM file itself. The <code>&#8211;check</code> option to several <code>wimlib-imagex</code> commands can be used to verify or add integrity tables.</p>
<dt>&bull;</p>
<dd> On UNIX-like systems, support for saving and restoring UNIX uids (user IDs), gids (group IDs), and modes to/from WIM images. This is a wimlib extension, but the Microsoft implementation ignores this extra metadata.</p>
<dt>&bull;</p>
<dd> Multithreaded compression. By default, data compression is multithreaded and will use all available processors.</p>
<dt>&bull;</p>
<dd> XPRESS, LZX, and LZMS decompression and compression. wimlib contains independent implementations of all these compression algorithms. Sometimes they can do better than the equivalent Microsoft implementations.</p>
<dt>&bull;</p>
<dd> &quot;ESD file&quot; support. As mentioned in <code>BACKGROUND INFORMATION</code>, &quot;ESD files&quot; use a new WIM format that features solid resources and LZMS compression. This support was first present in wimlib v1.6.0, but v1.7.0 and later have improved compatibility.</p>
<dt>&bull;</p>
<dd> On Linux, support for mounting WIM images with FUSE (Filesystem in UserSpacE).</p>
<dt>&bull;</p>
<dd> &quot;Pipable&quot; WIMs. This is a wimlib extension and is not compatible with the Microsoft implementation. A pipable WIM, created with <code>wimcapture</code> with the <code>&#8211;pipable</code> option, can be written to standard output or read from standard input. This can be used to pipe images to or from a server over the network to implement fast filesystem imaging and restore.</p>
<dt>&bull;</p>
<dd> Split WIMs. A split WIM is a WIM archive split into multiple parts. <code>wimsplit</code> can create a split WIM from a standalone WIM, and <code>wimjoin</code> can create a standalone WIM from a split WIM.</p>
<dt>&bull;</p>
<dd> Delta WIMs. A delta WIM contains image metadata but excludes file data already present in another WIM file. A delta WIM can be created using <code>wimcapture</code> with the <code>&#8211;delta-from</code> option.</p>
<dt>&bull;</p>
<dd> Fast incremental backups. Using the <code>&#8211;update-of</code> option of <code>wimcapture</code> or <code>wimappend</code>, you can optimize an image capture so that files that are unmodified based on timestamps are not be read from disk. But even without this option, since the WIM format features single-instance files, a file identical to any already present in the WIM archive (in any image) will not be written, but rather a reference to the stored file will be used.</p>
<dt>&bull;</p>
<dd> Windows-specific image metadata support. When capturing an image of a Windows operating system, wimlib will automatically populate XML metadata fields such as the Windows OS version details by scanning well-known system files.</p>
<dt>&bull;</p>
<dd> WIMBoot support. On Windows 8.1 and later, files can be &quot;externally backed&quot; by a WIM archive with the help of Microsoft&#8217;s Windows Overlay Filesystem filter driver (WOF). With the <code>&#8211;wimboot</code> option, <code>wimapply</code> will extract &quot;pointer files&quot; to the WIM archive rather than the files themselves.</p>
<dt>&bull;</p>
<dd> VSS snapshot support. On Windows, <code>wimcapture</code> or <code>wimappend</code> with the <code>&#8211;snapshot</code> option will automatically create a temporary VSS snapshot and capture the image from it. This can be used to image a &quot;live&quot; Windows system.</dl>
<h2>LOCALES AND CHARACTER ENCODINGS</h2>
<p> WIM files themselves store file and stream names using Windows native &quot;wide character strings&quot;, which are UTF-16. On Windows, wimlib works using these same strings, so conversions are usually not necessary and there should be no problems with character encodings. </p>
<p> On UNIX-like systems, wimlib works primarily in the locale-dependent multibyte encoding, which you are strongly recommended to set to UTF-8 to avoid any problems. You can alternatively set the environmental variable <code>WIMLIB_IMAGEX_USE_UTF8</code> to force <code>wimlib-imagex</code> to use UTF-8 internally, even if the current locale is not UTF-8 compatible.</p>
<h2>CASE SENSITIVITY</h2>
<p> By default, the case sensitivity of <code>wimlib-imagex</code> differs somewhat between UNIX-like systems and Windows. WIM images may (but usually do not) have multiple files with the same case-insensitive name. Internally, wimlib stores filenames as case-sensitive, but on Windows paths actually provided by the user for use in a WIM image (e.g. for extracting, adding, renaming, or deleting files) will by default be treated as case-insensitive in order to get the &quot;expected&quot; behavior. This differs from the default behavior on UNIX-like systems, where such paths will be treated as case-sensitive. </p>
<p> Note that with case insensitivity, a path component may in general be ambiguous due to multiple files or directories having the same case-insensitive name. In such cases, if there is a file or directory with an exactly matching name, it is chosen; otherwise, one of the case-insensitively matching file or directories is chosen arbitrarily. </p>
<p> The default case sensitivity of <code>wimlib-imagex</code> can be overridden by explicitly setting the environmental variable <code>WIMLIB_IMAGEX_IGNORE_CASE</code> to 1, in which case such paths will be treated case insensitively, or 0, in which such paths will be treated case sensitively. </p>
<p> Regardless of these settings, options and non-path arguments must be specified in lower case.</p>
<h2>LICENSE</h2>
<p> wimlib-imagex may be redistributed and/or modified under the terms of the GNU General Public License; either version 3 of the License, or (at your option) any later version. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to ebiggers3 [at] gmail.com. Feedback and suggestions are also welcome.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-wimlib-imagex-append/">wimlib-imagex-append</a></code>(1), <code><a href="/docs/linux/man/1-wimlib-imagex-apply/">wimlib-imagex-apply</a></code>(1), <code><a href="/docs/linux/man/1-wimlib-imagex-capture/">wimlib-imagex-capture</a></code>(1), <code><a href="/docs/linux/man/1-wimlib-imagex-delete/">wimlib-imagex-delete</a></code>(1), <code><a href="/docs/linux/man/1-wimlib-imagex-dir/">wimlib-imagex-dir</a></code>(1), <code><a href="/docs/linux/man/1-wimlib-imagex-export/">wimlib-imagex-export</a></code>(1), <code><a href="/docs/linux/man/1-wimlib-imagex-extract/">wimlib-imagex-extract</a></code>(1), <code><a href="/docs/linux/man/1-wimlib-imagex-info/">wimlib-imagex-info</a></code>(1), <code><a href="/docs/linux/man/1-wimlib-imagex-join/">wimlib-imagex-join</a></code>(1), <code><a href="/docs/linux/man/1-wimlib-imagex-mount/">wimlib-imagex-mount</a></code>(1), <code><a href="/docs/linux/man/1-wimlib-imagex-mountrw/">wimlib-imagex-mountrw</a></code>(1), <code><a href="/docs/linux/man/1-wimlib-imagex-optimize/">wimlib-imagex-optimize</a></code>(1), <code><a href="/docs/linux/man/1-wimlib-imagex-split/">wimlib-imagex-split</a></code>(1), <code><a href="/docs/linux/man/1-wimlib-imagex-unmount/">wimlib-imagex-unmount</a></code>(1), <code><a href="/docs/linux/man/1-wimlib-imagex-update/">wimlib-imagex-update</a></code>(1), <code><a href="/docs/linux/man/1-wimlib-imagex-verify/">wimlib-imagex-verify</a></code>(1), </p>
<h2>Index</h2>
