---
title: "wimlib-imagex-apply(1)"
name: "wimlib-imagex-apply"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wimlib-imagex-apply/"
description: "wimlib-imagex-apply – Extract one image, or all images, from a WIM archive"
---

<h2>NAME</h2>
<p> wimlib-imagex-apply &#8211; Extract one image, or all images, from a WIM archive</p>
<h2>SYNOPSIS</h2>
<p> <code>wimlib-imagex apply</code> <i>WIMFILE</i> [<i>IMAGE</i>] <i>TARGET</i> [<i>OPTION</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>wimlib-imagex apply</code> extracts an image, or all images, from the Windows Imaging (WIM) file <i>WIMFILE</i>. This command is also available as simply <code>wimapply</code> if the appropriate hard link or batch file has been installed. </p>
<p> This command is designed to extract, or &quot;apply&quot;, one or more full WIM images. If you instead want to extract only certain files or directories contained in a WIM image, consider using <code>wimlib-imagex extract</code> or <code>wimlib-imagex mount</code> instead. (<code>wimlib-imagex mount</code> is not supported on Windows.) </p>
<p> <i>IMAGE</i> specifies the WIM image in <i>WIMFILE</i> to extract. It may be a 1-based index of an image in <i>WIMFILE</i>, the name of an image in <i>WIMFILE</i>, or the keyword &quot;all&quot; to indicate that all images in <i>WIMFILE</i> are to be extracted. Use the <code>wimlib-imagex info</code> (1) command to show what images a WIM file contains. <i>IMAGE</i> may be omitted if <i>WIMFILE</i> contains only one image. </p>
<p> <i>TARGET</i> specifies where to extract the WIM image to. If <i>TARGET</i> specifies a directory, the WIM image is extracted to that directory (see <code>DIRECTORY EXTRACTION (UNIX)</code> or <code>DIRECTORY EXTRACTION (WINDOWS)</code>). Similarly, if <i>TARGET</i> specifies a non-existent file, a directory is created in that location and the WIM image is extracted to that directory. </p>
<p> If <i>IMAGE</i> is specified as &quot;all&quot;, then all the images in <i>WIMFILE</i> are actually extracted into subdirectories of <i>TARGET</i>, each of which is given the name of the corresponding image, falling back to the image index in the case of an image with no name or a name not valid as a filename. </p>
<p> Alternatively, on UNIX-like systems only, if <i>TARGET</i> specifies a regular file or block device, it is interpreted as an NTFS volume to which the WIM image is to be extracted (see <code>NTFS VOLUME EXTRACTION (UNIX)</code>). Only a single image can be extracted in this mode, and only extracting to the root of the NTFS volume (not a subdirectory thereof) is supported. </p>
<p> <i>WIMFILE</i> may be &quot;-&quot; to read the WIM from standard input rather than from a file, but see <code>PIPABLE WIMS</code> for more information. </p>
<p> <code>wimlib-imagex apply</code> supports applying images from stand-alone WIMs as well as split WIMs. See <code>SPLIT WIMS</code>.</p>
<h2>DIRECTORY EXTRACTION (UNIX)</h2>
<p> This section documents how <code>wimlib-imagex apply</code> (and also <code>wimlib-imagex extract</code>) extract a WIM image (or a possibly a subset thereof, in the case of <code>wimlib-imagex extract</code>) to a directory on UNIX-like systems. See <code>DIRECTORY EXTRACTION (WINDOWS)</code> for the corresponding documentation for Windows. </p>
<p> As mentioned, a WIM image can be applied to a directory on a UNIX-like system by providing a <i>TARGET</i> directory. However, it is important to keep in mind that the WIM format was designed for Windows, and as a result WIM files can contain data or metadata that cannot be represented on UNIX-like systems. The main information that <code>wimlib-imagex</code> will <i>not</i> be able to extract on UNIX-like systems is the following:</p>
<dl>
<dt>&bull;</p>
<dd> Windows security descriptors (which include the file owner, group, and ACLs).</p>
<dt>&bull;</p>
<dd> Named data streams.</p>
<dt>&bull;</p>
<dd> Reparse points other than symbolic links and junction points.</p>
<dt>&bull;</p>
<dd> Certain file attributes such as compression, encryption, and sparseness.</p>
<dt>&bull;</p>
<dd> Short (DOS) names for files.</p>
<dt>&bull;</p>
<dd> File creation timestamps.</dl>
<p> Notes: Unsupported data and metadata is simply not extracted, but <code>wimlib-imagex</code> will attempt to warn you when the contents of the WIM image can&#8217;t be exactly represented when extracted. Last access and last modification timestamps are specified to 100 nanosecond granularity in the WIM file, but will only be extracted to the highest precision supported by the underlying operating system, C library, and filesystem. Compressed files will be extracted as uncompressed, while encrypted files will not be extracted at all.</p>
<h2>NTFS VOLUME EXTRACTION (UNIX)</h2>
<p> This section documents how <code>wimlib-imagex apply</code> extracts a WIM image directly to an NTFS volume image on UNIX-like systems. </p>
<p> As mentioned, <code>wimlib-imagex</code> running on a UNIX-like system can apply a WIM image directly to an NTFS volume by specifying <i>TARGET</i> as a regular file or block device containing an NTFS filesystem. The NTFS filesystem need not be empty, although it&#8217;s expected that it be empty for the intended use cases. A new NTFS filesystem can be created using the <code><a href="/docs/linux/man/8-mkntfs/">mkntfs</a></code>(8) command provided with <code>ntfs-3g</code>. </p>
<p> In this NTFS volume extraction mode, the WIM image is extracted to the root of the NTFS volume in a way preserves almost all information contained in the WIM image. It therefore does not suffer from the limitations described in <code>DIRECTORY EXTRACTION (UNIX)</code>. This support relies on libntfs-3g to write to the NTFS volume and handle NTFS-specific and Windows-specific data. </p>
<p> Please note that this NTFS volume extraction mode is <i>not</i> entered if <i>TARGET</i> is a directory, even if an NTFS filesystem is mounted on <i>TARGET</i>. You must specify the NTFS volume itself (and it must be unmounted, and you must have permission to write to it). </p>
<p> This NTFS volume extraction mode attempts to extract as much information as possible, including:</p>
<dl>
<dt>&bull;</p>
<dd> All data streams of all files except encrypted files, including the unnamed data stream as well as all named data streams.</p>
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
<p> However, there are also several known limitations of the NTFS volume extraction mode:</p>
<dl>
<dt>&bull;</p>
<dd> Encrypted files will not be extracted.</p>
<dt>&bull;</p>
<dd> Sparse file attributes will not be extracted.</dl>
<p> Regardless, since almost all information from the WIM image is restored in this mode, it is possible (and fully supported) to restore an image of an actual Windows installation using <code>wimlib-imagex</code> on UNIX-like systems as an alternative to using <code>wimlib-imagex</code> on Windows. In the examples at the end of this manual page, there is an example of applying an image from the &quot;install.wim&quot; file contained in the installation media for Windows (Vista or later) in the &quot;sources&quot; directory. </p>
<p> Note that to actually boot Windows (Vista or later) from an applied &quot;install.wim&quot; image, you also need to mark the partition as &quot;bootable&quot; and set up various boot files, such as \BOOTMGR and \BOOT\BCD. The latter task is most easily accomplished by running the &quot;bcdboot.exe&quot; program from a live Windows system (such as Windows PE), but there are other options as well.</p>
<h2>DIRECTORY EXTRACTION (WINDOWS)</h2>
<p> On Windows, <code>wimlib-imagex apply</code> and <code>wimlib-imagex extract</code> natively support Windows-specific and NTFS-specific data. For best results, the target directory should be located on an NTFS volume and <code>wimlib-imagex</code> should be run with Administrator privileges; however, non-NTFS filesystems and running without Administrator privileges are also supported. </p>
<p> On Windows, <code>wimlib-imagex apply</code> and <code>wimlib-imagex extract</code> try to extract as much data and metadata as possible, including:</p>
<dl>
<dt>&bull;</p>
<dd> All data streams of all files. This includes the default file contents, as well as named data streams if supported by the target volume.</p>
<dt>&bull;</p>
<dd> Reparse points, including symbolic links, junction points, and other reparse points, if supported by the target volume. (Note: see <code>&#8211;rpfix</code> and <code>&#8211;norpfix</code> for documentation on exactly how absolute symbolic links and junctions are extracted.) However, as per the default security settings of Windows, it is impossible to create a symbolic link or junction point without Administrator privileges; therefore, you must run <code>wimlib-imagex</code> as the Administrator if you wish to fully restore an image containing symbolic links and/or junction points. (Otherwise, merely a warning will be issued when a symbolic link or junction point cannot be extracted due to insufficient privileges.)</p>
<dt>&bull;</p>
<dd> File and directory creation, access, and modification timestamps, to the highest resolution supported by the target volume.</p>
<dt>&bull;</p>
<dd> Security descriptors, if supported by the filesystem and <code>&#8211;no-acls</code> is not specified. Furthermore, unless <code>&#8211;strict-acls</code> is specified, the security descriptors for individual files or directories may be omitted or only partially set if the user does not have permission to set them, which can be a problem if <code>wimlib-imagex</code> is run as a non-Administrator.</p>
<dt>&bull;</p>
<dd> File attributes, including hidden, compressed, encrypted, etc, when supported by the filesystem.</p>
<dt>&bull;</p>
<dd> DOS names (8.3) names of files; however, the failure to set them is not considered an error condition.</p>
<dt>&bull;</p>
<dd> Hard links, if supported by the target filesystem.</p>
<dt>&bull;</p>
<dd> Object IDs, if supported by the target filesystem.</dl>
<p> Additional notes about extracting files on Windows:</p>
<dl>
<dt>&bull;</p>
<dd> <code>wimlib-imagex</code> will issue a warning when it is unable to extract the exact metadata and data of the WIM image, for example due to features mentioned above not being supported by the target filesystem.</p>
<dt>&bull;</p>
<dd> Sparse file attributes will not be extracted.</p>
<dt>&bull;</p>
<dd> Since encrypted files (with FILE_ATTRIBUTE_ENCRYPTED) are not stored in plaintext in the WIM image, <code>wimlib-imagex</code> cannot restore encrypted files to filesystems not supporting encryption. Therefore, on such filesystems, encrypted files will not be extracted. Furthermore, even if encrypted files are restored to a filesystem that supports encryption, they will only be decryptable if the decryption key is available.</p>
<dt>&bull;</p>
<dd> Files with names that cannot be represented on Windows will not be extracted by default; see <code>&#8211;include-invalid-names</code>.</p>
<dt>&bull;</p>
<dd> Files with full paths over 260 characters (the so-called MAX_PATH) will be extracted, but beware that such files will be inaccessible to most Windows software and may not be able to be deleted easily.</p>
<dt>&bull;</p>
<dd> On Windows, unless the <code>&#8211;no-acls</code> option is specified, wimlib will attempt to restore files&#8217; security descriptors exactly as they are provided in the WIM image. Beware that typical Windows installations contain files whose security descriptors do not allow the Administrator to delete them. Therefore, such files will not be able to be deleted, or in some cases even read, after extracting, unless processed with a specialized program that knows to acquire the SE_RESTORE_NAME and/or SE_BACKUP_NAME privileges which allow overriding access control lists. This is not a bug in wimlib, which works as designed to correctly restore the data that was archived, but rather a problem with the access rights Windows uses on certain files. But if you just want the file data and don&#8217;t care about security descriptors, use <code>&#8211;no-acls</code> to skip restoring all security descriptors.</p>
<dt>&bull;</p>
<dd> A similar caveat to the above applies to file attributes such as Readonly, Hidden, and System. By design, on Windows wimlib will restore such file attributes; therefore, extracted files may have those attributes. If this is not what you want, use the <code>&#8211;no-attributes</code> option.</dl>
<h2>SPLIT WIMS</h2>
<p> You may use <code>wimlib-imagex apply</code> to apply images from a split WIM. The <i>WIMFILE</i> argument must specify the first part of the split WIM, while the additional parts of the split WIM must be specified in one or more <code>&#8211;ref</code>=&quot;<i>GLOB</i>&quot; options. Since globbing is built into the <code>&#8211;ref</code> option, typically only one <code>&#8211;ref</code> option is necessary. For example, the names for the split WIM parts usually go something like:</p>
<dl>
<dt>
<dd>
<pre>
mywim.swm
mywim2.swm
mywim3.swm
mywim4.swm
mywim5.swm
</dl>
</pre>
<p> To apply the first image of this split WIM to the directory &quot;dir&quot;, run: </p>
<dl>
<dt>
<dd> wimlib-imagex apply mywim.swm 1 dir &#8211;ref=&quot;mywim*.swm&quot;</dl>
<p> As a special case, if you are applying an image from standard input from a split WIM that is also pipable (as described in <code>PIPABLE WIMS</code>), the <code>&#8211;ref</code> option is unneeded; instead you must ensure that all the split WIM parts are concatenated together on standard input. They can be provided in any order, with the exception of the first part, which must be first.</p>
<h2>PIPABLE WIMS</h2>
<p> Since wimlib v1.5.0, <code>wimlib-imagex apply</code> supports applying a WIM from a nonseekable file, such as a pipe, provided that the WIM was captured with <code>&#8211;pipable</code> (see <code>wimlib-imagex <a href="/docs/linux/man/1-capture/">capture</a></code>(1)). To use standard input as the WIM, specify &quot;-&quot; as <i>WIMFILE</i>. A useful use of this ability is to apply an image from a WIM while streaming it from a server. For example, to apply the first image from a WIM file available on a HTTP server to an NTFS volume on /dev/sda1, run something like: </p>
<dl>
<dt>
<dd> wget -O &#8211; <a rel="nofollow" href="http://myserver/mywim.wim">http://myserver/mywim.wim</a> | wimapply &#8211; 1 /dev/sda1</dl>
<p> (The above also used the <code>wimapply</code> abbreviation for <code>wimlib-imagex apply</code>.) Note: WIM files are <i>not</i> pipable by default; you have to explicitly capture them with <code>&#8211;pipable</code>, and they are <i>not</i> compatible with Microsoft&#8217;s software. See <code>wimlib-imagex <a href="/docs/linux/man/1-capture/">capture</a></code>(1) for more information. </p>
<p> It is possible to apply an image from a pipable WIM split into multiple parts; see <code>SPLIT WIMS</code>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;check</code></p>
<dd> When reading <i>WIMFILE</i>, verify its integrity if the integrity table is present.</p>
<dt><code>&#8211;ref</code>=&quot;<i>GLOB</i>&quot;</p>
<dd> File glob of additional WIMs or split WIM parts to reference resources from. See <code>SPLIT_WIMS</code>. This option can be specified multiple times. Note: <i>GLOB</i> is listed in quotes because it is interpreted by <code>wimlib-imagex</code> and may need to be quoted to protect against shell expansion.</p>
<dt><code>&#8211;rpfix</code>, <code>&#8211;norpfix</code></p>
<dd> Set whether to fix targets of absolute symbolic links (reparse points in Windows terminology) or not. When enabled (<code>&#8211;rpfix</code>), extracted absolute symbolic links that are marked in the WIM image as being fixed are assumed to have absolute targets relative to the image root, and therefore <code>wimlib-imagex apply</code> prepends the absolute path to the extraction target directory to their targets. The intention is that you can apply an image containing absolute symbolic links and still have them be valid after it has been applied to any location.</p>
<dt>
<dd> The default behavior is <code>&#8211;rpfix</code> if any images in <i>WIMFILE</i> have been captured with reparse-point fixups done. Otherwise, it is <code>&#8211;norpfix</code>.</p>
<dt>
<dd> Reparse point fixups are never done in the NTFS volume extraction mode on UNIX-like systems.</p>
<dt><code>&#8211;unix-data</code></p>
<dd> (UNIX-like systems only) Restore UNIX owners, groups, modes, and device IDs (major and minor numbers) that were captured by <code>wimlib-imagex capture</code> with the <code>&#8211;unix-data</code> option. Since wimlib v1.7.0, you can backup and restore not only the standard UNIX file permission information, but also character device nodes, block device nodes, named pipes (FIFOs), and UNIX domain sockets.</p>
<dt><code>&#8211;no-acls</code></p>
<dd> Do not restore security descriptors on extracted files and directories.</p>
<dt><code>&#8211;strict-acls</code></p>
<dd> Fail immediately if the full security descriptor of any file or directory cannot be set exactly as specified in the WIM file. If this option is not specified, when <code>wimlib-imagex</code> on Windows does not have permission to set a security descriptor on an extracted file, it falls back to setting it only partially (e.g. with SACL omitted), and in the worst case omits it entirely. However, this should only be a problem when running <code>wimlib-imagex</code> without Administrator rights. Also, on UNIX-like systems, this flag can also be combined with <code>&#8211;unix-data</code> to cause <code>wimlib-imagex</code> to fail immediately if the UNIX owner, group, or mode on an extracted file cannot be set for any reason.</p>
<dt><code>&#8211;no-attributes</code></p>
<dd> Do not restore Windows file attributes such as readonly, hidden, etc.</p>
<dt><code>&#8211;include-invalid-names</code></p>
<dd> Extract files and directories with invalid names by replacing characters and appending a suffix rather than ignoring them. Exactly what is considered an &quot;invalid&quot; name is platform-dependent.</p>
<dt>
<dd> On POSIX-compliant systems, filenames are case-sensitive and may contain any byte except &#8216;
