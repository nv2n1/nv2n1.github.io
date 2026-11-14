---
title: "wimappend(1)"
name: "wimappend"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wimappend/"
description: "wimlib-imagex-capture, wimlib-imagex-append – Create or append a WIM image"
---

<h2>NAME</h2>
<p> wimlib-imagex-capture, wimlib-imagex-append &#8211; Create or append a WIM image</p>
<h2>SYNOPSIS</h2>
<p> <code>wimlib-imagex capture</code> <i>SOURCE</i> <i>WIMFILE</i> [<i>IMAGE_NAME</i> [<i>IMAGE_DESCRIPTION</i>]] [<i>OPTION</i>&#8230;]<br />
 <code>wimlib-imagex append</code> <i>SOURCE</i> <i>WIMFILE</i> [<i>IMAGE_NAME</i> [<i>IMAGE_DESCRIPTION</i>]] [<i>OPTION</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> The <code>wimlib-imagex capture</code> and <code>wimlib-imagex append</code> commands create a Windows Imaging (WIM) image from a directory tree. The <code>wimlib-imagex capture</code> command creates a new WIM file containing the captured image, while the <code>wimlib-imagex append</code> command appends the captured image to an existing WIM file. These commands are also available as simply <code>wimcapture</code> and <code>wimappend</code> if the appropriate hard links or batch files are installed. </p>
<p> Background information: A WIM image is an independent directory tree in a WIM file. A WIM file may contain any number of separate images. WIM files are single-instancing with regards to file data, so a file is stored only one time in the entire WIM, regardless of how many images the file appears in. </p>
<p> <i>SOURCE</i> specifies the location of the files to create the new WIM image from. If <i>SOURCE</i> is a directory, the WIM image is captured from that directory (see <code>DIRECTORY CAPTURE (UNIX)</code> or <code>DIRECTORY CAPTURE (WINDOWS)</code>). Alternatively, if the <code>&#8211;source-list</code> option is specified, <i>SOURCE</i> is interpreted as a file that itself provides a list of files and directories to include in the new WIM image. Still alternatively, only on UNIX-like systems, if <i>SOURCE</i> is a regular file or block device, it is interpreted as an NTFS volume from which a WIM image is to be captured using libntfs-3g (see <code>NTFS VOLUME CAPTURE (UNIX)</code>). </p>
<p> <i>IMAGE_NAME</i> and <i>IMAGE_DESCRIPTION</i> specify the name and description to give the new WIM image. If <i>IMAGE_NAME</i> is not specified, it defaults to the base name (excluding path to parent directory) of <i>SOURCE</i>, but if this name already exists in <i>WIMFILE</i>, a unique suffix is added. Otherwise, <i>IMAGE_NAME</i> must be either a name that does not already exist as an image in <i>WIMFILE</i>, or the empty string to create an image with no name. If <i>IMAGE_DESCRIPTION</i> is not specified, no description is given to the new image. </p>
<p> As a special case, if <i>WIMFILE</i> is &quot;-&quot;, the <code>&#8211;pipable</code> option is assumed and the WIM file is written to standard output in a special pipable format. See the documentation for <code>&#8211;pipable</code> for more details.</p>
<h2>DIRECTORY CAPTURE (UNIX)</h2>
<p> This section documents how <code>wimlib-imagex</code> captures files from a directory tree on UNIX-like systems. See <code>DIRECTORY CAPTURE (WINDOWS)</code> for the corresponding documentation for Windows. </p>
<p> On UNIX-like systems, when <i>SOURCE</i> specifies a directory or a symbolic link to a directory, the WIM image will be captured from the directory tree rooted at this directory. This directory can be on any type of filesystem, and mountpoints are followed recursively. In this mode, wimlib will store the following types of information:</p>
<dl>
<dt>&bull;</p>
<dd> Directories and regular files, and the contents of regular files</p>
<dt>&bull;</p>
<dd> Hard links</p>
<dt>&bull;</p>
<dd> Symbolic links (translated losslessly to Windows reparse points)</p>
<dt>&bull;</p>
<dd> Last modification times (mtime) and last access times (atime) with 100 nanosecond granularity</p>
<dt>&bull;</p>
<dd> With <code>&#8211;unix-data</code>: UNIX owners, groups, and modes</p>
<dt>&bull;</p>
<dd> With <code>&#8211;unix-data</code>: device nodes, FIFOs, and UNIX domain sockets</dl>
<p> There is no support for storing extended attributes (e.g. SELinux security labels and POSIX ACLs). Also note that last status change times (ctime) are not stored. </p>
<p> Pedantic note: A limitation of the WIM format prevents the unusual case where a single symbolic link file itself has multiple names (hard links); in this unlikely case, each symbolic link is stored as an independent file.</p>
<h2>NTFS VOLUME CAPTURE (UNIX)</h2>
<p> This section documents how <code>wimlib-imagex</code> captures files directly from an NTFS volume image on UNIX-like systems. </p>
<p> On UNIX-like systems, a special image capture mode is entered when <i>SOURCE</i> is a regular file or block device. In this mode, <i>SOURCE</i> is assumed to be an NTFS volume or volume image, and <code>wimlib-imagex</code> will capture a WIM image containing the full contents of the NTFS volume, including NTFS-specific data. This is done using libntfs-3g. </p>
<p> Note that the NTFS volume capture mode is <i>not</i> entered if <i>SOURCE</i> is a directory, even if an NTFS filesystem is mounted on <i>SOURCE</i> using ntfs-3g. You must specify the NTFS volume itself (and it must be unmounted, and you must have permission to read from it). </p>
<p> The NTFS volume capture mode attempts to capture as much data and metadata as possible, including:</p>
<dl>
<dt>&bull;</p>
<dd> All data streams of all unencrypted files, including the unnamed data stream as well as all named data streams.</p>
<dt>&bull;</p>
<dd> Reparse points, including symbolic links, junction points, and other reparse points.</p>
<dt>&bull;</p>
<dd> File and directory creation, access, and modification timestamps, using the native NTFS resolution of 100 nanoseconds.</p>
<dt>&bull;</p>
<dd> Windows security descriptors, including all components (owner, group, DACL, and SACL).</p>
<dt>&bull;</p>
<dd> DOS/Windows file attribute flags.</p>
<dt>&bull;</p>
<dd> All names of all files, including names in the Win32 namespace, DOS namespace, Win32+DOS namespace, and POSIX namespace. This includes hard links.</p>
<dt>&bull;</p>
<dd> Object IDs.</dl>
<p> However, the main limitations of this NTFS volume capture mode are:</p>
<dl>
<dt>&bull;</p>
<dd> Encrypted files are excluded by default. Although libntfs-3g can read their data, they need to be stored in the WIM file in a special format that wimlib does not yet support (except on Windows, where wimlib can treat the data as opaque and hand it off to the appropriate API function).</p>
<dt>&bull;</p>
<dd> The sparse attribute on sparse files will be saved, but the data stored will be the full data of the file rather than the &quot;sparse&quot; data. (The data is, however, subject to the WIM format&#8217;s compression.)</dl>
<h2>DIRECTORY CAPTURE (WINDOWS)</h2>
<p> On Windows, <code>wimlib-imagex capture</code> and <code>wimlib-imagex append</code> natively support Windows-specific and NTFS-specific data. They therefore act similarly to the corresponding commands of Microsoft&#8217;s ImageX or DISM. For best results, the directory being captured should be on an NTFS volume and <code>wimlib-imagex</code> should be run with Administrator privileges; however, non-NTFS filesystems and running without Administrator privileges are also supported. </p>
<p> On Windows, <code>wimlib-imagex capture</code> and <code>wimlib-imagex append</code> try to archive as much data and metadata as possible, including:</p>
<dl>
<dt>&bull;</p>
<dd> All data streams of all files.</p>
<dt>&bull;</p>
<dd> Reparse points, including symbolic links, junction points, and other reparse points, if supported by the source filesystem. (Note: see <code>&#8211;rpfix</code> and <code>&#8211;norpfix</code> for documentation on exactly how absolute symbolic links and junctions are captured.)</p>
<dt>&bull;</p>
<dd> File and directory creation, access, and modification timestamps. These are stored with Windows NT&#8217;s native timestamp resolution of 100 nanoseconds.</p>
<dt>&bull;</p>
<dd> Security descriptors, if supported by the source filesystem and <code>&#8211;no-acls</code> is not specified. However, beware that unless <code>&#8211;strict-acls</code> is specified, the security descriptors for individual files or directories may be omitted or only partially captured if the user does not have permission to read them, which can be a problem if <code>wimlib-imagex</code> is run as a non-Administrator.</p>
<dt>&bull;</p>
<dd> File attributes, including hidden, sparse, compressed, encrypted, etc. Encrypted files will be stored in encrypted form rather than in plain text. Transparently compressed files will be read as uncompressed and stored subject to the WIM&#8217;s own compression. There is no special handling for storing sparse files, but they are likely to compress to a small size.</p>
<dt>&bull;</p>
<dd> DOS names (8.3) names of files; however, the failure to read them is not considered an error condition.</p>
<dt>&bull;</p>
<dd> Hard links, if supported by the source filesystem.</p>
<dt>&bull;</p>
<dd> Object IDs, if supported by the source filesystem.</dl>
<p> There is no support for storing NTFS extended attributes. </p>
<p> The capture process is reversible, since when <code>wimlib-imagex apply</code> (on Windows) extracts the captured WIM image, it will extract all of the above information, at least to the extent supported by the destination filesystem. </p>
<p> Pedantic note: since Windows is not fully compatible with its own filesystem (NTFS), on Windows wimlib cannot archive certain files that may exist on a valid NTFS filesystem but are inaccessible to the Windows API, for example two files with names differing only in case in the same directory, or a file whose name contains certain characters considered invalid by Windows. If you run into problems archiving such files consider using the <code>NTFS VOLUME CAPTURE (UNIX)</code> mode from Linux.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;boot</code></p>
<dd> Specifies that the new image is to be made the bootable image of the WIM archive.</p>
<dt><code>&#8211;check</code></p>
<dd> For <code>wimlib-imagex append</code>, before performing the append operation, check the integrity of <i>WIMFILE</i> if an integrity table is present. Furthermore, include an integrity table in the new WIM file (<code>wimlib-imagex capture</code>) or the modified WIM file (<code>wimlib-imagex append</code>). If this option is not specified, no integrity table is included in a WIM file created with <code>wimlib-imagex capture</code>, while a WIM file updated with <code>wimlib-imagex append</code> will be written with an integrity table if and only if one was present before.</p>
<dt><code>&#8211;compress</code>=<i>TYPE</i>[:<i>LEVEL</i>]</p>
<dd> Specifies the compression format for the new WIM file. <i>TYPE</i> may be &quot;none&quot;, &quot;XPRESS&quot; (alias: &quot;fast&quot;), &quot;LZX&quot; (alias: &quot;maximum&quot;), or &quot;LZMS&quot; (alias: &quot;recovery&quot;). <i>TYPE</i> is matched case-insensitively. The default is &quot;LZX&quot;.</p>
<dt>
<dd> You can optionally also specify an integer compression <i>LEVEL</i>. The compression level specifies how hard the compression algorithm for the specified compression <i>TYPE</i> will work to compress the data. The values are scaled so that 20 is quick compression, 50 is medium compression, and 100 is high compression. However, you can choose any value, and not just these particular values. The default is 50.</p>
<dt>
<dd> This option only affects the compression type used in non-solid WIM resources. If you are creating a solid WIM (using the <code>&#8211;solid</code> option), then you probably want <code>&#8211;solid-compress</code> instead.</p>
<dt>
<dd> Be careful if you choose LZMS compression. It is not compatible with wimlib before v1.6.0, WIMGAPI before Windows 8, DISM before Windows 8.1, and 7-Zip before v15.12.</p>
<dt>
<dd> Also note that choosing LZMS compression does not automatically imply solid-mode compression, as it does with DISM. Use <code>&#8211;solid</code> if you want to create a solid WIM, or &quot;ESD file&quot;.</p>
<dt><code>&#8211;chunk-size</code>=<i>SIZE</i></p>
<dd> Set the compression chunk size to <i>SIZE</i> bytes. A larger compression chunk size results in a better compression ratio. wimlib supports different chunk sizes depending on the compression type:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> XPRESS: 4K, 8K, 16K, 32K, 64K</p>
<dt>&bull;</p>
<dd> LZX: 32K, 64K, 128K, 256K, 512K, 1M, 2M</p>
<dt>&bull;</p>
<dd> LZMS: 32K, 64K, 128K, 256K, 512K, 1M, 2M, 4M, 8M, 16M, 32M, 64M, 128M, 256M, 512M, 1G</dl>
</dl>
<dt>
<dd> You can provide the full number (e.g. 32768), or you can use one of the K, M, or G suffixes. KiB, MiB, and GiB are also accepted.</p>
<dt>
<dd> This option only affects the chunk size used in non-solid WIM resources. If you are creating a solid WIM (using the <code>&#8211;solid</code> option), then you probably want <code>&#8211;solid-chunk-size</code> instead.</p>
<dt>
<dd> Use this option with caution if compatibility with Microsoft&#8217;s implementation is desired, since their implementation has limited support for non-default chunk sizes.</p>
<dt><code>&#8211;solid</code></p>
<dd> Create a &quot;solid&quot; WIM file that compresses files together rather than independently. This results in a significantly better compression ratio, but it comes at the cost of various tradeoffs, including: slow compression with very high memory usage; slow random access to the resulting WIM file; and reduced compatibility.</p>
<dt>
<dd> Compatibility-wise, the first version of Microsoft&#8217;s WIMGAPI to support solid WIM files was released with Windows 8, and the first version of DISM to do so was released with Windows 8.1.</p>
<dt>
<dd> If you want to create an &quot;ESD file&quot;, then use this option. An (unencrypted) &quot;ESD file&quot; is a solid WIM file.</p>
<dt>
<dd> By default, this option has an effect equivalent to DISM&#8217;s option <code>/compress:recovery</code>. The options for wimlib-imagex are different because they try not to conflate the compression type (e.g. LZX or LZMS) with solid-mode compression, as these are two different things.</p>
<dt><code>&#8211;solid-chunk-size</code>=<i>SIZE</i></p>
<dd> Like <code>&#8211;chunk-size</code>, but set the chunk size used in solid resources. The default, assuming LZMS compression, is 64MiB (67108864); this requires about 640MiB of memory per thread. This option only has an effect when <code>&#8211;solid</code> is also specified. Note: Microsoft&#8217;s implementation is not compatible with LZMS chunk sizes larger than 64MiB.</p>
<dt><code>&#8211;solid-compress</code>=<i>TYPE</i>[:<i>LEVEL</i>]</p>
<dd> Like <code>&#8211;compress</code>, but set the compression type used in solid resources. The default is LZMS compression. This option only has an effect when <code>&#8211;solid</code> is also specified.</p>
<dt><code>&#8211;threads</code>=<i>NUM_THREADS</i></p>
<dd> Number of threads to use for compressing data. Default: autodetect (number of available CPUs).</p>
<dt><code>&#8211;rebuild</code></p>
<dd> For <code>wimlib-imagex append</code>: rebuild the entire WIM rather than appending the new data to the end of it. Rebuilding the WIM is slower, but will save a little bit of space that would otherwise be left as a hole in the WIM. Also see <code>wimlib-imagex <a href="/docs/linux/man/1-optimize/">optimize</a></code>(1).</p>
<dt><code>&#8211;flags</code>=<i>EDITIONID</i></p>
<dd> Specify a string to use in the &lt;FLAGS&gt; element of the XML data for the new image.</p>
<dt><code>&#8211;image-property</code> <i>NAME</i>=<i>VALUE</i></p>
<dd> Specify an arbitrary per-image property to set in the XML document of the WIM file. <i>VALUE</i> is the string to set as the property value. <i>NAME</i> is the name of the image property, for example &quot;NAME&quot;, &quot;DESCRIPTION&quot;, or &quot;TOTALBYTES&quot;. The name can contain forward slashes to indicate a nested XML element; for example, &quot;WINDOWS/VERSION/BUILD&quot; indicates the BUILD element nested within the VERSION element nested within the WINDOWS element. A bracketed number can be used to indicate one of several identically-named elements; for example, &quot;WINDOWS/LANGUAGES/LANGUAGE[2]&quot; indicates the second &quot;LANGUAGE&quot; element nested within the &quot;WINDOWS/LANGUAGES&quot; element. When adding a list of elements in this way, they must be specified in sequential order. Note that element names are case-sensitive. This option may be specified multiple times.</p>
<dt><code>&#8211;dereference</code></p>
<dd> (UNIX-like systems only) Follow symbolic links and archive the files they point to, rather than archiving the links themselves.</p>
<dt><code>&#8211;config</code>=<i>FILE</i></p>
<dd> Specifies a configuration file (UTF-8 or UTF-16LE encoded; plain ASCII also works) for capturing the new image. The configuration file specifies files that are to be treated specially during the image capture.</p>
<dt>
<dd> The format of the configuration file is INI-style; that is, it is arranged in bracketed sections. Currently, the following sections are recognized:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> [ExclusionList] &#8212; contains a list of path globs to exclude from capture. If a directory is matched, both the directory and its contents are excluded.</p>
<dt>&bull;</p>
<dd> [ExclusionException] &#8212; contains a list of path globs to include in the capture, even when the file or directory also matches a glob in [ExclusionList].</p>
<dt>&bull;</p>
<dd> [PrepopulateList] &#8212; this does not affect capture, but if the image is applied later with <code>&#8211;wimboot</code>, these are globs of files that shall be extracted normally, not as WIMBoot &quot;pointer files&quot;. If a directory is matched, all files and subdirectories are also matched recursively.</dl>
</dl>
<dt>
<dd> Path globs may contain the &#8216;*&#8217; and &#8216;?&#8217; meta-characters. Relative globs (e.g. *.mp3) match against a filename in any directory. Absolute globs (e.g. /dir/file), are treated as paths starting at the main directory being captured, or the root of the NTFS volume for NTFS volume capture mode. Do not use drive letters in the paths; they will be ignored. Path separators may be either forwards slashes or backwards slashes.</p>
<dt>
<dd> Lines beginning with the &#8216;#&#8217; or &#8216;;&#8217; characters are treated as comments and ignored. Globs with whitespace in them need not be quoted; however, if they are, both double and single quotes are accepted.</p>
<dt>
<dd> If this option is not specified the following default configuration file is used:</p>
<dt>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
[ExclusionList]
\$ntfs.log
\hiberfil.sys
\pagefile.sys
\swapfile.sys
\System Volume Information
\RECYCLER
\Windows\CSC
</dl>
</dl>
</pre>
<dt>
<dd> However, special behavior applies if <code>&#8211;wimboot</code> is also specified. By default, with <code>&#8211;wimboot</code> specified, the file Windows/System32/WimBootCompress.ini in the directory being captured will be used as the configuration file. However, this can be overridden using <code>&#8211;config</code>; and this also causes the specified configuration file to be saved in the WIM image as Windows/System32/WimBootCompress.ini, overriding any that may be present on the filesystem.</p>
<dt><code>&#8211;unix-data</code></p>
<dd> (UNIX-like systems only) Store the UNIX owner, group, mode, and device ID (major and minor number) of each captured file. Since wimlib v1.7.0, you can backup and restore not only the standard UNIX file permission information, but also character device nodes, block device nodes, named pipes (FIFOs), and UNIX domain sockets.</p>
<dt>
<dd> wimlib stores UNIX data by adding a special tagged metadata item to each directory entry of each file that contains this information. This extra information is ignored by the Microsoft implementation. Note: UNIX data stored by wimlib before v1.7.0 used a different format that is no longer supported. If you have old WIM files with UNIX data, apply them with v1.6.2 and recapture them with v1.7.0 or later.</p>
<dt><code>&#8211;no-acls</code></p>
<dd> Do not capture files&#8217; security descriptors.</p>
<dt><code>&#8211;strict-acls</code></p>
<dd> Fail immediately if the full security descriptor of any file cannot be read. On Windows, the default behavior without this option is to first try omitting the SACL from the security descriptor, then to try omitting the security descriptor entirely. The purpose of this is to capture as much data as possible without always requiring Administrator privileges. However, if you desire that all security descriptors be captured exactly, you may wish to provide this option, although the Administrator should have permission to read everything anyway.</p>
<dt><code>&#8211;rpfix</code>, <code>&#8211;norpfix</code></p>
<dd> Set whether to fix targets of absolute symbolic links (reparse points in Windows terminology) or not. When enabled (<code>&#8211;rpfix</code>), absolute symbolic links that point inside the directory tree being captured will be adjusted to be absolute relative to the root of the directory tree being captured. When disabled (<code>&#8211;norpfix</code>), absolute symbolic links will be captured exactly as is.</p>
<dt>
<dd> The default behavior for <code>wimlib-imagex capture</code> is equivalent to <code>&#8211;rpfix</code>. The default behavior for <code>wimlib-imagex append</code> will be <code>&#8211;rpfix</code> if reparse point fixups have previously been done on <i>WIMFILE</i>, otherwise <code>&#8211;norpfix</code>.</p>
<dt>
<dd> In the case of a multi-source capture, (<code>&#8211;source-list</code> specified), passing <code>&#8211;norpfix</code> is recommended. Otherwise, reparse point fixups will be disabled on all capture sources destined for non-root locations in the WIM image, while capture sources destined for the WIM root will get the default behavior from the previous paragraph.</p>
<dt><code>&#8211;source-list</code></p>
<dd> <code>wimlib-imagex capture</code> and <code>wimlib-imagex append</code> support creating a WIM image from multiple separate files or directories. When <code>&#8211;source-list</code> is specified, the <i>SOURCE</i> argument specifies the name of a text file, each line of which is either 1 or 2 whitespace separated file paths. The first file path, the source, specifies the path to a file or directory to capture into the WIM image. It may be either absolute or relative to the current working directory. The second file path, if provided, is the target and specifies the path in the WIM image that this file or directory will be saved as. Leading and trailing slashes in the target are ignored, except if it consists entirely of slashes (e.g. &quot;/&quot;), which indicates that the directory is to become the root of the WIM image. If omitted, the target string defaults to the same as the source string.</p>
<dt>
<dd> An example source list file is as follows:</p>
<dt>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
# Make the WIM image from the 'winpe' directory
winpe   /
# Send the 'overlay' directory to '/overlay' in the WIM image
overlay /overlay
# Overlay a separate directory directly on the root of the WIM image.
/data/stuff     /
</dl>
</dl>
</pre>
<dt>
<dd> Subdirectories in the WIM are created as needed. Multiple source directories may share the same target, which implies an overlay. In the event that this results a nondirectory file being added to the WIM image multiple times, the last version (as listed in the source list file) overrides any earlier version.</p>
<dt>
<dd> File paths containing whitespace may be quoted with either single quotes or double quotes. Quotes may not be escaped.</p>
<dt>
<dd> Lines consisting only of whitespace and lines beginning with &#8216;#&#8217; preceded by optional whitespace are ignored.</p>
<dt>
<dd> As a special case, if <i>SOURCE</i> is &quot;-&quot;, the source list is read from standard input rather than an external file.</p>
<dt>
<dd> The NTFS volume capture mode on UNIX-like systems cannot be used with <code>&#8211;source-list</code>, as only capturing a full NTFS volume is supported.</p>
<dt><code>&#8211;pipable</code></p>
<dd> Create a &quot;pipable&quot; WIM, which can be applied fully sequentially, including from a pipe. An image in the resulting WIM can be applied with <code>wimlib-imagex apply</code>, either normally by specifying the WIM file name, or with <code>wimlib-imagex apply &#8211;</code> to read the WIM from standard input. See <code>wimlib-imagex <a href="/docs/linux/man/1-apply/">apply</a></code>(1) for more details.</p>
<dt>
<dd> For append operations, this option will result in a full rebuild of the WIM to make it pipable. For capture operations, the captured WIM is simply created as pipable. Beware that the more images you add to a pipable WIM, the less efficient piping it will be, since more unneeded data will be sent through the pipe.</p>
<dt>
<dd> When wimlib creates a pipable WIM, it carefully re-arranges the components of the WIM so that they can be read sequentially and also makes several other modifications. As a result, these &quot;pipable&quot; WIMs are <i>not compatible with Microsoft&#8217;s software</i>, so keep this in mind if you&#8217;re going to use them. If desired, you can use <code>wimlib-imagex optimize &#8211;not-pipable</code> to re-write a pipable WIM as a regular WIM. (<code>wimlib-imagex export</code> also provides the capability to export images from a pipable WIM into a non-pipable WIM, or vice versa.)</p>
<dt>
<dd> For the most part, wimlib operates on pipable WIMs transparently. You can modify them, add or delete images, export images, and even create split pipable WIMs. The main disadvantages are that appending is (currently) less efficient (<code>&#8211;rebuild</code> is always implied), and also they aren&#8217;t compatible with Microsoft&#8217;s software.</p>
<dt>
<dd> <code>wimlib-imagex capture</code> and <code>wimlib-imagex append</code> can both write a pipable WIM directly to standard output; this is done automatically if <i>WIMFILE</i> is specified as &quot;-&quot;. (In that case, <code>&#8211;pipable</code> is assumed.)</p>
<dt><code>&#8211;not-pipable</code></p>
<dd> Ensure the resulting WIM is in the normal, non-pipable WIM format. This is the default for <code>wimlib-imagex capture</code>, except when writing to standard output (<i>WIMFILE</i> specified as &quot;-&quot;), and also for <code>wimlib-imagex append</code>, except when appending to a WIM that is already pipable.</p>
<dt><code>&#8211;update-of</code>=[<i>WIMFILE</i>:]<i>IMAGE</i></p>
<dd> Declares that the image being captured or appended from <i>SOURCE</i> is mostly the same as the existing image <i>IMAGE</i> in <i>WIMFILE</i>, but captured at a later point in time, possibly with some modifications in the intervening time. This is designed to be used in incremental backups of the same filesystem or directory tree. <i>IMAGE</i> can be a 1-based index or name of an existing image in <i>WIMFILE</i>. It can also be a negative integer to index backwards into the images (e.g. -1 means the last existing image in <i>WIMFILE</i>).</p>
<dt>
<dd> When this option is provided, the capture or append of the new image will be optimized by not reading files that, based on metadata such as timestamps, appear not to have been modified since they were archived in the existing <i>IMAGE</i>. Barring manipulation of timestamps, this option only affects performance and does not change the resulting WIM image (but see note below).</p>
<dt>
<dd> As shown, the full syntax for the argument to this option is to specify the WIM file, a colon, and the image; for example, &quot;&#8211;update-of mywim.wim:1&quot;. However, the WIM file and colon may be omitted, in which case the WIM file will default to the WIM file being appended to for append operations, or the WIM file from which a delta is being taken (only if <code>&#8211;delta-from</code> is specified exactly once) for capture operations.</p>
<dt>
<dd> Note: in the Windows version of wimlib, it has been observed that <code>&#8211;update-of</code> mode is not completely reliable at detecting changes in file contents, sometimes causing the old contents of a few files to be archived rather than the current contents. The cause of this problem is that Windows does not immediately update a file&#8217;s last modification timestamp after every write to that file. Unfortunately, there is no known way for applications like wimlib to automatically work around this bug. Manual workarounds are possible; theoretically, taking any action that causes the problematic files to be closed, such as restarting applications or the computer itself, should cause the files&#8217; last modification timestamps to be updated. Also note that wimlib compares file sizes as well as timestamps in determining whether a file has changed, which helps make the problem less likely to occur; and the problem does not occur on other operating systems such as Linux which maintain files&#8217; last modification timestamps correctly.</p>
<dt><code>&#8211;delta-from</code>=<i>WIMFILE</i></p>
<dd> For <code>wimlib-imagex capture</code> only: capture the new WIM as a &quot;delta&quot; from <i>WIMFILE</i>. Any streams that would ordinarily need to be archived in the new WIM are omitted if they are already present in the <i>WIMFILE</i> on which the delta is being based. The new WIM will still contain a full copy of the image metadata, but this is typically only a small fraction of a WIM&#8217;s total size.</p>
<dt>
<dd> This option can be specified multiple times, in which case the resulting delta WIM will only contain streams not present in any of the specified base WIMs.</p>
<dt>
<dd> To operate on the resulting delta WIM using other commands such as <code>wimlib-imagex apply</code>, you must specify the delta WIM as the WIM file to operate on, but also reference the base WIM(s) using the <code>&#8211;ref</code> option. Beware: to retain the proper functioning of the delta WIM, you can only add, not delete, files and images to the base WIM(s) following the capture of a delta from it.</p>
<dt>
<dd> <code>&#8211;delta-from</code> may be combined with <code>&#8211;update-of</code> to increase the speed of capturing a delta WIM.</p>
<dt>
<dd> As an example, consider the following backup and restore sequence:</p>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
(initial backup)
$ wimcapture /some/directory bkup-base.wim
(some days later, create second backup as delta from first)
$ wimcapture /some/directory bkup-2013-08-20.dwm \
        --update-of bkup-base.wim:-1 --delta-from bkup-base.wim
(restoring the second backup)
$ wimapply bkup-2013-08-20.dwm --ref=bkup-base.wim 1 \
        /some/directory
</dl>
</pre>
<dt>
<dd> However, note that as an alternative to the above sequence that used a delta WIM, the second backup could have simply been appended to the WIM as new image using <code>wimlib-imagex append</code>. Delta WIMs should be used only if it&#8217;s desired to base the backups or images on a separate, large file that is rarely modified.</p>
<dt>
<dd> Note: unlike &quot;pipable&quot; WIMs (created with the <code>&#8211;pipable</code> option), &quot;delta&quot; WIMs (created with the <code>&#8211;delta-from</code> option) are compatible with Microsoft&#8217;s software. For example, you can use the /ref option of ImageX to reference the base WIM(s), similar to above.</p>
<dt>
<dd> Additional note: <code>wimlib-imagex</code> is generalized enough that you can in fact combine <code>&#8211;pipable</code> and <code>&#8211;delta-from</code> to create pipable delta WIMs. In such cases, the base WIM(s) must be captured as pipable as well as the delta WIM, and when applying an image, the base WIM(s) must be sent over the pipe after the delta WIM.</p>
<dt><code>&#8211;wimboot</code></p>
<dd> Mark the image as WIMBoot-compatible. See Microsoft&#8217;s documentation for more information about WIMBoot. This option will, by default, set the compression type to XPRESS and the chunk size to 4096 bytes; these can, however, still be overridden through the <code>&#8211;compress</code> and <code>&#8211;chunk-size</code> parameters, respectively. In addition, this option will, by default, set the configuration file to <i>SOURCE</i>\Windows\System32\WimBootCompress.ini if present and accessible; however, this may still be overridden through the <code>&#8211;config</code> parameter.</p>
<dt><code>&#8211;unsafe-compact</code></p>
<dd> For <code>wimlib-imagex append</code>: compact the WIM archive in-place and append any new data, eliminating &quot;holes&quot;. In general, this option should <i>not</i> be used because a failed or interrupted compaction will corrupt the WIM archive. For more information, see the documentation for this option in <code>wimlib-imagex-optimize</code> (1).</p>
<dt><code>&#8211;snapshot</code></p>
<dd> Create a temporary filesystem snapshot of the source directory and capture the files from it. Currently, this option is only supported on Windows, where it uses the Volume Shadow Copy Service (VSS). Using this option, you can create a consistent backup of the system volume of a running Windows system without running into problems with locked files. For the VSS snapshot to be successfully created, <code>wimlib-imagex</code> must be run as an Administrator, and it cannot be run in WoW64 mode (i.e. if Windows is 64-bit, then <code>wimlib-imagex</code> must be 64-bit as well).</dl>
<h2>NOTES</h2>
<p> <code>wimlib-imagex append</code> does not support appending an image to a split WIM. </p>
<p> Except when using <code>&#8211;unsafe-compact</code>, it is safe to abort a <code>wimlib-imagex append</code> command partway through; however, after doing this, it is recommended to run <code>wimlib-imagex optimize</code> to remove any data that was appended to the physical WIM file but not yet incorporated into the structure of the WIM, unless the WIM was being fully rebuilt (e.g. with <code>&#8211;rebuild</code>), in which case you should delete the temporary file left over. </p>
<p> <code>wimlib-imagex</code> creates WIMs compatible with Microsoft&#8217;s software (WIMGAPI, ImageX, DISM), with some caveats:</p>
<dl>
<dt>&bull;</p>
<dd> With <code>wimlib-imagex</code> on UNIX-like systems, it is possible to create a WIM image containing files with names differing only in case, or files with names containing the characters &#8216;:&#8217;, &#8216;*&#8217;, &#8216;?&#8217;, &#8216;&quot;&#8217;, &#8216;&lt;&#8216;, &#8216;&gt;&#8217;, &#8216;|&#8217;, or &#8216;\&#8217;, which are valid on POSIX-compliant filesystems but not Windows. Be warned that such files will not be extracted by default by the Windows version of <code>wimlib-imagex</code>, and (even worse) Microsoft&#8217;s ImageX can be confused by such names and quit extracting the image partway through. (It perhaps is worth pointing out that Windows&#8217; own default filesystem, NTFS, supports these characters, although Windows does not!)</p>
<dt>&bull;</p>
<dd> Pipable WIMs are incompatible with Microsoft&#8217;s software. Pipable WIMs are created only if <i>WIMFILE</i> was specified as &quot;-&quot; (standard output) or if the <code>&#8211;pipable</code> flag was specified.</p>
<dt>&bull;</p>
<dd> WIMs captured with a non-default chunk size (with the <code>&#8211;chunk-size</code> option) or as solid archives (with the <code>&#8211;solid</code> option) or with LZMS compression (with <code>&#8211;compress</code>=LZMS or <code>&#8211;compress</code>=recovery) have varying levels of compatibility with Microsoft&#8217;s software. Generally, more recent versions of Microsoft&#8217;s software are more compatible.</dl>
<h2>EXAMPLES</h2>
<p> First example: Create a new WIM &#8216;mywim.wim&#8217; with LZX (&quot;maximum&quot;) compression that will contain a captured image of the directory tree &#8216;somedir&#8217;. Note that the image name need not be specified and will default to &#8216;somedir&#8217;:</p>
<dl>
<dt>
<dd>
<p> wimlib-imagex capture somedir mywim.wim</dl>
<p> or, if the <code>wimcapture</code> hard link or batch file has been installed, the abbreviated form can be used:</p>
<dl>
<dt>
<dd>
<p> wimcapture somedir mywim.wim</dl>
<p> The remaining examples will use the long form, however. Next, append the image of a different directory tree to the WIM created above:</p>
<dl>
<dt>
<dd>
<p> wimlib-imagex append anotherdir mywim.wim</dl>
<p> Easy enough, and the above examples of imaging directory trees work on both UNIX-like systems and Windows. Next, capture a WIM with several non-default options, including XPRESS (&quot;fast&quot;) compression, an integrity table, no messing with absolute symbolic links, and an image name and description:</p>
<dl>
<dt>
<dd>
<p> wimlib-imagex capture somedir mywim.wim &#8211;compress=fast \</p>
<dl>
<dt>
<dd> &#8211;check &#8211;norpfix &quot;Some Name&quot; &quot;Some Description&quot;</dl>
</dl>
<p> Capture an entire NTFS volume into a new WIM file and name the image &quot;Windows 7&quot;. On UNIX-like systems, this requires using the special mode described in <code>NTFS VOLUME CAPTURE (UNIX)</code> where <i>SOURCE</i> is a file or block device containing an NTFS filesystem:</p>
<dl>
<dt>
<dd>
<p> wimlib-imagex capture /dev/sda2 windows7.wim &quot;Windows 7&quot;</dl>
<p> or, on Windows, to capture a full NTFS volume you instead need to specify the root directory of the mounted volume, for example:</p>
<dl>
<dt>
<dd>
<p> wimlib-imagex capture E:\ windows7.wim &quot;Windows 7&quot;</dl>
<p> Same as above example with capturing an NTFS volume from <code>wimlib-imagex</code> running on a UNIX-like system, but capture the WIM in the wimlib-specific &quot;pipable&quot; format that can be piped to <code>wimlib-imagex apply</code>:</p>
<dl>
<dt>
<dd>
<p> wimlib-imagex capture /dev/sda2 windows7.wim &quot;Windows 7&quot; \ </p>
<dl>
<dt>
<dd> &#8211;pipable</dl>
</dl>
<p> Same as above, but instead of writing the pipable WIM to the file &quot;windows7.wim&quot;, write it directly to standard output through a pipe into some other program &quot;someprog&quot;, which could, for example, be a program or script that streams the data to a server. Note that <code>&#8211;pipable</code> need not be explicitly specified when using standard output as the WIM &quot;file&quot;:</p>
<dl>
<dt>
<dd>
<p> wimlib-imagex capture /dev/sda2 &#8211; &quot;Windows 7&quot; | someprog</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-wimlib-imagex/">wimlib-imagex</a></code>(1), <code><a href="/docs/linux/man/1-wimlib-imagex-apply/">wimlib-imagex-apply</a></code>(1) </p>
<h2>Index</h2>
