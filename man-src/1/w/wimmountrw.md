---
title: "wimmountrw(1)"
name: "wimmountrw"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wimmountrw/"
description: "wimlib-imagex-mount, wimlib-imagex-mountrw, wimlib-imagex-unmount – Mount and unmount an image from a WIM archive"
---

<h2>NAME</h2>
<p> wimlib-imagex-mount, wimlib-imagex-mountrw, wimlib-imagex-unmount &#8211; Mount and unmount an image from a WIM archive</p>
<h2>SYNOPSIS</h2>
<p> <code>wimlib-imagex mount</code> <i>WIMFILE</i> [<i>IMAGE</i>] <i>DIRECTORY</i> [<i>OPTION</i>&#8230;]<br />
 <code>wimlib-imagex mountrw</code> <i>WIMFILE</i> [<i>IMAGE</i>] <i>DIRECTORY</i> [<i>OPTION</i>&#8230;]<br />
 <code>wimlib-imagex unmount</code> <i>DIRECTORY</i> [<i>OPTION</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> On Linux-based systems, the <code>wimlib-imagex mount</code> and <code>wimlib-imagex mountrw</code> commands will mount the image in the Windows Imaging (WIM) file <i>WIMFILE</i> specified by <i>IMAGE</i> on the directory <i>DIRECTORY</i> using FUSE (Filesystem in Userspace). <code>wimlib-imagex mount</code> will mount the image read-only, while <code>wimlib-imagex mountrw</code> will mount the image read-write. These commands are also available as simply <code>wimmount</code>, <code>wimmountrw</code>, and <code>wimunmount</code> if the appropriate hard links are installed. </p>
<p> <i>IMAGE</i> may be a 1-based index of the image in the WIM to mount, or it may be the name of an image in the WIM. Use the <code>wimlib-imagex info</code> (1) command to see the available images in the WIM. <i>IMAGE</i> may be omitted if <i>WIMFILE</i> contains only one image. </p>
<p> The WIM image can be unmounted using the <code>wimlib-imagex unmount</code> command. Changes made to a WIM mounted read-write will be discarded unless the <code>&#8211;commit</code> flag is provided to <code>wimlib-imagex unmount</code>.</p>
<h2>DATA AND METADATA SUPPORT</h2>
<p> This section documents which WIM features are exposed via the mount support and which are not. </p>
<p> The following features are <i>supported</i> (read/write unless otherwise specified):</p>
<dl>
<dt>&bull;</p>
<dd> Hard links</p>
<dt>&bull;</p>
<dd> Symbolic links. Native Windows symbolic links and junctions in a mounted WIM image will automatically be translated into UNIX symbolic links, potentially with their targets fixed to be valid given the actual mountpoint directory. UNIX symbolic links created in a read-write mounted WIM image will automatically be translated into native Windows symbolic links.</p>
<dt>&bull;</p>
<dd> Named data streams (mostly). See the <code>&#8211;streams-interface</code> option.</p>
<dt>&bull;</p>
<dd> Standard UNIX permission bits and UNIX special files are supported if the <code>&#8211;unix-data</code> option is used.</dl>
<p> The following features are <i>unsupported</i>:</p>
<dl>
<dt>&bull;</p>
<dd> Windows security descriptors. These are not exposed in the mounted filesystem, although existing values will be preserved on commit. New files are not given security descriptors.</p>
<dt>&bull;</p>
<dd> DOS names (8.3 names) (short names). These are not exposed in the mounted filesystem, although existing values will be preserved on commit. New files are not given DOS names.</p>
<dt>&bull;</p>
<dd> Windows file attributes. These are not exposed in the mounted filesystem, although existing values will be preserved on commit. New files are assigned default attributes based on the UNIX file mode bits.</p>
<dt>&bull;</p>
<dd> Object IDs. These are not exposed in the mounted filesystem, although existing values will be preserved on commit. New files are not given object IDs.</p>
<dt>&bull;</p>
<dd> EFS-encrypted files. The files themselves will be visible in mounted WIM images but their data will not be available.</dl>
<h2>SPLIT WIMS</h2>
<p> You may use <code>wimlib-imagex mount</code> to mount an image from a split WIM read-only. However, you may not mount an image from a split WIM read-write. </p>
<p> The <i>WIMFILE</i> argument must specify the first part of the split WIM, while the additional parts of the split WIM must be specified in one or more <code>&#8211;ref</code>=&quot;<i>GLOB</i>&quot; options. Since globbing is built into the <code>&#8211;ref</code> option, typically only one <code>&#8211;ref</code> option is necessary. For example, the names for the split WIM parts usually go something like: </p>
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
To mount the first image of this split WIM to the directory &quot;dir&quot;, run:
<dl><dt><dd>wimlib-imagex mount mywim.swm 1 dir --ref=&quot;mywim*.swm&quot;
</dl>
</pre>
<h2>NOTES</h2>
<p> <i>Availablity</i>: Mounting WIM images is only supported on Linux-based systems. These commands will not work on other platforms. Furthermore, the library cannot have been configured <code>&#8211;without-fuse</code>. </p>
<p> <i>Multiple mounts</i>: You are free to mount many WIM images at the same time, provided that there are not two images mounted read-write from the same file at the same time. </p>
<p> <i>Appends vs. rebuilds</i>: By default, changes to a read-write WIM are made in-place by appending to the WIM. This is nice for big WIM files, since the entire file doesn&#8217;t have to be rebuilt to make a small change. But, if you are making many changes to a read-write mounted WIM, especially deleting large files, it is suggested to provide the <code>&#8211;rebuild</code> option to <code>wimlib-imagex unmount</code> to force the WIM to be rebuilt, or else run <code>wimlib-imagex optimize</code> on the WIM afterwards. </p>
<p> <i>ESD files (solid WIMs)</i>: You can mount version 3584 WIMs, which usually contain LZMS-compressed solid resources and may carry the <i>.esd</i> file extension rather than <i>.wim</i>. However, such files are not designed for random access, so reading data from them when mounted may be very slow. In addition, <i>.esd</i> files downloaded directly by the Windows 8 web downloader have encrypted segments, and wimlib cannot mount such files until they are first decrypted.</p>
<h2>MOUNT OPTIONS</h2>
<dl>
<dt><code>&#8211;check</code></p>
<dd> When reading the WIM, verify its integrity if it contains an integrity table.</p>
<dt><code>&#8211;streams-interface</code>=<i>INTERFACE</i></p>
<dd> This option is inspired by the ntfs-3g filesystem driver (see <code>ntfs-3g</code> (8)). It controls how alternate data streams, or named data streams, in WIM files are made available.</p>
<dt>
<dd> If &quot;none&quot;, it will be impossible to read or write the named data streams.</p>
<dt>
<dd> If &quot;xattr&quot; (default), named data streams will be accessible through extended file attributes, unless this support was disabled when compiling wimlib. The named data streams may be accessed through extended attributes named &quot;user.*&quot;, where the * is the name of the named data stream. See <code>setfattr</code> (1) and <code>getfattr</code> (1). Note that this is not an ideal interface, since named data streams may be larger than the maximum allowed extended attribute size.</p>
<dt>
<dd> If &quot;windows&quot;, the named data streams will be accessible by specifying the filename, then a colon, then the name of the named data stream; for example, &quot;myfile:mystream&quot;.</p>
<dt>
<dd> Please note that named data streams are a somewhat obscure NTFS feature that aren&#8217;t actually used much, even though they complicate the WIM file format considerably. Normally, all you care about is the default or &quot;unnamed&quot; data stream.</p>
<dt><code>&#8211;debug</code></p>
<dd> Turn on debugging information printed by the FUSE library, and do not fork into the background.</p>
<dt><code>&#8211;ref</code>=&quot;<i>GLOB</i>&quot;</p>
<dd> File glob of additional WIMs or split WIM parts to reference resources from. See <code>SPLIT_WIMS</code>. This option can be specified multiple times. Note: <i>GLOB</i> is listed in quotes because it is interpreted by <code>wimlib-imagex</code> and may need to be quoted to protect against shell expansion.</p>
<dt><code>&#8211;staging-dir</code>=<i>DIR</i></p>
<dd> Store temporary staging files in a subdirectory of the directory <i>DIR</i>. Only valid for <code>wimlib-imagex mountrw</code>.</p>
<dt><code>&#8211;unix-data</code></p>
<dd> Honor UNIX-specific metadata that was captured by <code>wimlib-imagex capture</code> with the <code>&#8211;unix-data option</code>. By default, <code>wimlib-imagex mount</code> and <code>wimlib-imagex mountrw</code> will ignore both Windows-style security descriptors (which may have been set either from Windows or by <code>wimlib-imagex capture</code> from an NTFS-volume) and UNIX-specific metadata. In this default mode, all files will simply be owned by the user running <code>wimlib-imagex</code> and will have mode 0777. (Note: they will still not be accessible to other users unless you also specify <code>&#8211;allow-other</code>.) If you instead provide the <code>&#8211;unix-data</code> option, these default permissions will be overridden on a per-file basis with the UNIX-specific data when available, and in the case of <code>wimlib-imagex mountrw</code> it will be possible to change the UNIX permissions using the standard UNIX tools and functions. In addition, with wimlib v1.7.0 and later, you can create device nodes, named pipes, and sockets on the mounted filesystem and have them stored in the WIM image.</p>
<dt><code>&#8211;allow-other</code></p>
<dd> Pass the <code>allow_other</code> option to the FUSE mount. See <code>mount.fuse</code> (8). Note: to do this is a non-root user, <code>user_allow_other</code> needs to be specified in /etc/fuse.conf (with the FUSE implementation on Linux, at least).</dl>
<h2>UNMOUNT OPTIONS</h2>
<dl>
<dt><code>&#8211;commit</code></p>
<dd> Update the WIM file with the changes that have been made. Has no effect if the mount is read-only.</p>
<dt><code>&#8211;force</code></p>
<dd> In combination with <code>&#8211;commit</code>, force the WIM image to be committed even if there are open file descriptors to the WIM image. Any such file descriptors will be immediately closed, and the WIM image will be committed and unmounted.</p>
<dt><code>&#8211;check</code></p>
<dd> When writing <i>WIMFILE</i>, include an integrity table. Has no effect if the mount is read-only or if <code>&#8211;commit</code> was not specified. The default behavior is to include an integrity table if and only if there was one present before.</p>
<dt><code>&#8211;rebuild</code></p>
<dd> Rebuild the entire WIM rather than appending any new data to the end of it. Rebuilding the WIM is slower, but will save a little bit of space that would otherwise be left as a hole in the WIM. Even more space will be saved if the read-write mount resulted in streams being deleted from the WIM. Also see</p>
<dt><code>&#8211;new-image</code></p>
<dd> In combination with <code>&#8211;commit</code> for a read-write mounted image, causes the modified image to be committed as a new, unnamed image appended to the WIM archive. The original image will be unmodified.</dl>
<h2>IMPLEMENTATION DETAILS</h2>
<p> Since a WIM is an archive and not a filesystem, <code>wimlib-imagex mountrw</code> creates a temporary staging directory to contain files that are created or modified. This directory is located in the same directory as <i>WIMFILE</i> by default, but the location can be set using the <code>&#8211;staging-dir</code> option. When the filesystem is unmounted with <code>&#8211;commit</code>, the WIM is modified in-place (or rebuilt completely with <code>&#8211;rebuild</code>), merging in the staging files as needed. Then, the temporary staging directory is deleted. </p>
<p> <code>wimlib-imagex unmount</code> runs in a separate process from the process that previously ran <code>wimlib-imagex mount</code>. When unmounting a read-write mounted WIM image with <code>&#8211;commit</code>, these two processes communicate using a POSIX message queue so that the unmount process can track the progress of the mount process. See <i>src/mount_image.c</i> in the sources for details.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-wimlib-imagex/">wimlib-imagex</a></code>(1) </p>
<h2>Index</h2>
