---
title: "fallocate(1)"
name: "fallocate"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fallocate/"
description: "fallocate – preallocate or deallocate space to a file"
---

<h2 class="name">NAME</h2>
<p> fallocate &#8211; preallocate or deallocate space to a file </p>
<h2>SYNOPSIS</h2>
<p> <code>fallocate</code> [<code>-c</code>|<code>-p</code>|<code>-z</code>] [<code>-o</code> <i>offset</i>] <code>-l</code> <i>length</i> [<code>-n</code>] <i>filename</i> </p>
<p> <code>fallocate</code> <code>-d</code> [<code>-o</code> <i>offset</i>] [<code>-l</code> <i>length</i>] <i>filename</i> </p>
<p> <code>fallocate</code> <code>-x</code> [<code>-o</code> <i>offset</i>] <code>-l</code> <i>length filename</i></p>
<h2>DESCRIPTION</h2>
<p> <code>fallocate</code> is used to manipulate the allocated disk space for a file, either to deallocate or preallocate it. For filesystems which support the fallocate system call, preallocation is done quickly by allocating blocks and marking them as uninitialized, requiring no IO to the data blocks. This is much faster than creating a file by filling it with zeroes. </p>
<p> The exit status returned by <code>fallocate</code> is 0 on success and 1 on failure.</p>
<h2>OPTIONS</h2>
<p> The <i>length</i> and <i>offset</i> arguments may be followed by the multiplicative suffixes KiB (=1024), MiB (=1024*1024), and so on for GiB, TiB, PiB, EiB, ZiB, and YiB (the &quot;iB&quot; is optional, e.g., &quot;K&quot; has the same meaning as &quot;KiB&quot;) or the suffixes KB (=1000), MB (=1000*1000), and so on for GB, TB, PB, EB, ZB, and YB. </p>
<p> The options <code>&#8211;collapse-range</code>, <code>&#8211;dig-holes</code>, <code>&#8211;punch-hole</code>, and <code>&#8211;zero-range</code> are mutually exclusive. </p>
<p> <code>-c</code>, <code>&#8211;collapse-range</code></p>
<dl>
<dt>
<dd> Removes a byte range from a file, without leaving a hole. The byte range to be collapsed starts at <i>offset</i> and continues for <i>length</i> bytes. At the completion of the operation, the contents of the file starting at the location <i>offset</i>+<i>length</i> will be appended at the location <i>offset</i>, and the file will be <i>length</i> bytes smaller. The option <code>&#8211;keep-size</code> may not be specified for the collapse-range operation. </p>
<p> Available since Linux 3.15 for ext4 (only for extent-based files) and XFS. </p>
<p> A filesystem may place limitations on the granularity of the operation, in order to ensure efficient implementation. Typically, offset and len must be a multiple of the filesystem logical block size, which varies according to the filesystem type and configuration. If a filesystem has such a requirement, the operation will fail with the error EINVAL if this requirement is violated.</dl>
<p> <code>-d</code>, <code>&#8211;dig-holes</code></p>
<dl>
<dt>
<dd> Detect and dig holes. This makes the file sparse in-place, without using extra disk space. The minimum size of the hole depends on filesystem I/O block size (usually 4096 bytes). Also, when using this option, <code>&#8211;keep-size</code> is implied. If no range is specified by <code>&#8211;offset</code> and <code>&#8211;length</code>, then the entire file is analyzed for holes. </p>
<p> You can think of this option as doing a &quot;<code>cp &#8211;sparse</code>&quot; and then renaming the destination file to the original, without the need for extra disk space. </p>
<p> See <code>&#8211;punch-hole</code> for a list of supported filesystems.</dl>
<p> <code>-i</code>, <code>&#8211;insert-range</code></p>
<dl>
<dt>
<dd> Insert a hole of <i>length</i> bytes from <i>offset</i>, shifting existing data.</dl>
<p> <code>-l</code>, <code>&#8211;length</code> <i>length</i></p>
<dl>
<dt>
<dd> Specifies the length of the range, in bytes.</dl>
<p> <code>-n</code>, <code>&#8211;keep-size</code></p>
<dl>
<dt>
<dd> Do not modify the apparent length of the file. This may effectively allocate blocks past EOF, which can be removed with a truncate.</dl>
<p> <code>-o</code>, <code>&#8211;offset</code> <i>offset</i></p>
<dl>
<dt>
<dd> Specifies the beginning offset of the range, in bytes.</dl>
<p> <code>-p</code>, <code>&#8211;punch-hole</code></p>
<dl>
<dt>
<dd> Deallocates space (i.e., creates a hole) in the byte range starting at <i>offset</i> and continuing for <i>length</i> bytes. Within the specified range, partial filesystem blocks are zeroed, and whole filesystem blocks are removed from the file. After a successful call, subsequent reads from this range will return zeroes. This option may not be specified at the same time as the <code>&#8211;zero-range</code> option. Also, when using this option, <code>&#8211;keep-size</code> is implied. </p>
<p> Supported for XFS (since Linux 2.6.38), ext4 (since Linux 3.0), Btrfs (since Linux 3.7), tmpfs (since Linux 3.5) and gfs2 (since Linux 4.16).</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Enable verbose mode.</dl>
<p> <code>-x</code>, <code>&#8211;posix</code></p>
<dl>
<dt>
<dd> Enable POSIX operation mode. In that mode allocation operation always completes, but it may take longer time when fast allocation is not supported by the underlying filesystem.</dl>
<p> <code>-z</code>, <code>&#8211;zero-range</code></p>
<dl>
<dt>
<dd> Zeroes space in the byte range starting at <i>offset</i> and continuing for <i>length</i> bytes. Within the specified range, blocks are preallocated for the regions that span the holes in the file. After a successful call, subsequent reads from this range will return zeroes. </p>
<p> Zeroing is done within the filesystem preferably by converting the range into unwritten extents. This approach means that the specified range will not be physically zeroed out on the device (except for partial blocks at the either end of the range), and I/O is (otherwise) required only to update metadata. </p>
<p> Option <code>&#8211;keep-size</code> can be specified to prevent file length modification. </p>
<p> Available since Linux 3.14 for ext4 (only for extent-based files) and XFS.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display help text and exit.</dl>
<h2>AUTHORS</h2>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-truncate/">truncate</a></code>(1), <code><a href="/docs/linux/man/2-fallocate/">fallocate</a></code>(2), <code><a href="/docs/linux/man/3-posix_fallocate/">posix_fallocate</a></code>(3)</p>
<h2>REPORTING BUGS</h2>
<p> For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>AVAILABILITY</h2>
<p> The <code>fallocate</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
<h2>Index</h2>
