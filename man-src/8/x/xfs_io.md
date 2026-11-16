---
title: "xfs_io(8)"
name: "xfs_io"
section: "8"
letter: "x"
url: "/docs/linux/man/8-xfs_io/"
description: "xfs_io – debug the I/O path of an XFS filesystem"
---

<p>xfs_io &#8211; debug the I/O path of an XFS filesystem</p>
<h2>Synopsis</h2>
<p><code>xfs_io</code> [ <code>-adfimrRstxT</code> ] [ <code>-c</code> <i>cmd</i> ] &#8230; [ <code>-p</code> <i>prog</i> ] <i>file</i><br />
 <code>xfs_io -V</code></p>
<h2>Description</h2>
<p><code>xfs_io</code> is a debugging tool like <code><a href="/docs/linux/man/8-xfs_db/">xfs_db</a></code>(8), but is aimed at examining the regular file I/O paths rather than the raw XFS volume itself. These code paths include not only the obvious read/write/mmap interfaces for manipulating files, but also cover all of the XFS extensions (such as space preallocation, additional inode flags, etc).</p>
<h2>Options</h2>
<dl>
<dt><code>-c</code><i> cmd</i></dt>
<dd><code>xfs_io</code> commands may be run interactively (the default) or as arguments on the command line. Multiple <code>-c</code> arguments may be given. The commands are run in the sequence given, then the program exits.</dd>
<dt><code>-p</code><i> prog</i></dt>
<dd>Set the program name for prompts and some error messages, the default value is <code>xfs_io</code>.</dd>
<dt><code>-f</code></dt>
<dd>Create <i>file</i> if it does not already exist.</dd>
<dt><code>-r</code></dt>
<dd>Open <i>file</i> read-only, initially. This is required if <i>file</i> is immutable or append-only.</dd>
<dt><code>-i</code></dt>
<dd>Start an idle thread. The purpose of this idle thread is to test io from a multi threaded process. With single threaded process, the file table is not shared and file structs are not reference counted. Spawning an idle thread can help detecting file struct reference leaks.</dd>
<dt><code>-x</code></dt>
<dd>Expert mode. Dangerous commands are only available in this mode. These commands also tend to require additional privileges.</dd>
<dt><code>-V</code></dt>
<dd>Prints the version number and exits.</dd></dl>
<p> The other <code><a href="/docs/linux/man/2-open/">open</a></code>(2) options described below are also available from the command line.</p>
<h2>Concepts</h2>
<p><code>xfs_io</code> maintains a number of open files and memory mappings. Files can be initially opened on the command line (optionally), and additional files can also be opened later. </p>
<p> <code>xfs_io</code> commands can be broken up into three groups. Some commands are aimed at doing regular file I/O &#8211; read, write, sync, space preallocation, etc. </p>
<p> The second set of commands exist for manipulating memory mapped regions of a file &#8211; mapping, accessing, storing, unmapping, flushing, etc. </p>
<p> The remaining commands are for the navigation and display of data structures relating to the open files, mappings, and the filesystems where they reside. </p>
<p> Many commands have extensive online help. Use the <code>help</code> command for more details on any command.</p>
<h2>File I/O Commands</h2>
<dl>
<dt><code>file [ </code><i>N</i><code> ]</code></dt>
<dd>Display a list of all open files and (optionally) switch to an alternate current open file.</dd>
<dt><code>open [[ -acdfrstRT ] </code><i>path</i><code> ]</code></dt>
<dd>Closes the current file, and opens the file specified by <i>path</i> instead. Without any arguments, displays statistics about the current file &#8211; see the <code>stat</code> command.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>-a</code></dt>
<dd>opens append-only (O_APPEND).</dd>
<dt><code>-d</code></dt>
<dd>opens for direct I/O (O_DIRECT).</dd>
<dt><code>-f</code></dt>
<dd>creates the file if it doesn&#8217;t already exist (O_CREAT).</dd>
<dt><code>-r</code></dt>
<dd>opens read-only (O_RDONLY).</dd>
<dt><code>-s</code></dt>
<dd>opens for synchronous I/O (O_SYNC).</dd>
<dt><code>-t</code></dt>
<dd>truncates on open (O_TRUNC).</dd>
<dt><code>-n</code></dt>
<dd>opens in non-blocking mode if possible (O_NONBLOCK).</dd>
<dt><code>-T</code></dt>
<dd>create a temporary file not linked into the filesystem namespace (O_TMPFILE). The pathname passed must refer to a directory which is treated as virtual parent for the newly created invisible file. Can not be used together with the <code>-r</code> option.</dd>
<dt><code>-R</code></dt>
<dd>marks the file as a realtime XFS file after opening it, if it is not already marked as such.</dd></dl>
</dl>
<dt><code>o</code></dt>
<dd>See the <code>open</code> command.</dd>
<dt><code>close</code></dt>
<dd>Closes the current open file, marking the next open file as current (if one exists).</dd>
<dt><code>c</code></dt>
<dd>See the <code>close</code> command.</dd>
<dt><code>pread [ -b </code><i>bsize</i><code> ] [ -v ] [ -FBR [ -Z </code><i>seed</i><code> ] ] [ -V </code><i>vectors</i><code> ] </code><i>offset length</i></dt>
<dd>Reads a range of bytes in a specified blocksize from the given <i>offset</i>.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>-b</code></dt>
<dd>can be used to set the blocksize into which the <code><a href="/docs/linux/man/2-read/">read</a></code>(2) requests will be split. The default blocksize is 4096 bytes.</dd>
<dt><code>-v</code></dt>
<dd>dump the contents of the buffer after reading, by default only the count of bytes actually read is dumped.</dd>
<dt><code>-F</code></dt>
<dd>read the buffers in a forwards sequential direction.</dd>
<dt><code>-B</code></dt>
<dd>read the buffers in a reserve sequential direction.</dd>
<dt><code>-R</code></dt>
<dd>read the buffers in the give range in a random order.</dd>
<dt><code>-Z seed</code></dt>
<dd>specify the random number seed used for random reads.</dd>
<dt><code>-V vectors</code></dt>
<dd>Use the vectored IO read syscall <code><a href="/docs/linux/man/2-preadv/">preadv</a></code>(2) with a number of blocksize length iovecs. The number of iovecs is set by the <i>vectors</i> parameter.</dd></dl>
</dl>
<dt><code>r</code></dt>
<dd>See the <code>pread</code> command.</dd>
<dt><code>pwrite [ -i </code><i>file</i><code> ] [ -d ] [ -s </code><i>skip</i><code> ] [ -b </code><i>size</i><code> ] [ -S </code><i>seed</i><code> ] [ -FBR [ -Z </code><i>zeed</i><code> ] ] [ -wW ] [ -V </code><i>vectors</i><code> ] </code><i>offset length</i></dt>
<dd>Writes a range of bytes in a specified blocksize from the given <i>offset</i>. The bytes written can be either a set pattern or read in from another file before writing.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>-i</code></dt>
<dd>allows an input <i>file</i> to be specified as the source of the data to be written.</dd>
<dt><code>-d</code></dt>
<dd>causes direct I/O, rather than the usual buffered I/O, to be used when reading the input file.</dd>
<dt><code>-s</code></dt>
<dd>specifies the number of bytes to <i>skip</i> from the start of the input file before starting to read.</dd>
<dt><code>-b</code></dt>
<dd>used to set the blocksize into which the <code><a href="/docs/linux/man/2-write/">write</a></code>(2) requests will be split. The default blocksize is 4096 bytes.</dd>
<dt><code>-S</code></dt>
<dd>used to set the (repeated) fill pattern which is used when the data to write is not coming from a file. The default buffer fill pattern value is 0xcdcdcdcd.</dd>
<dt><code>-F</code></dt>
<dd>write the buffers in a forwards sequential direction.</dd>
<dt><code>-B</code></dt>
<dd>write the buffers in a reserve sequential direction.</dd>
<dt><code>-R</code></dt>
<dd>write the buffers in the give range in a random order.</dd>
<dt><code>-Z seed</code></dt>
<dd>specify the random number seed used for random write</dd>
<dt><code>-w</code></dt>
<dd>call <code><a href="/docs/linux/man/2-fdatasync/">fdatasync</a></code>(2) once all writes are complete (included in timing results)</dd>
<dt><code>-W</code></dt>
<dd>call <code><a href="/docs/linux/man/2-fsync/">fsync</a></code>(2) once all writes are complete (included in timing results)</dd>
<dt><code>-V vectors</code></dt>
<dd>Use the vectored IO write syscall <code><a href="/docs/linux/man/2-pwritev/">pwritev</a></code>(2) with a number of blocksize length iovecs. The number of iovecs is set by the <i>vectors</i> parameter.</dd></dl>
</dl>
<dt><code>w</code></dt>
<dd>See the <code>pwrite</code> command.</dd>
<dt><code>bmap [ -acdelpv ] [ -n </code><i>nx</i><code> ]</code></dt>
<dd>Prints the block mapping for the current open file. Refer to the <code><a href="/docs/linux/man/8-xfs_bmap/">xfs_bmap</a></code>(8) manual page for complete documentation.</dd>
<dt><code>fiemap [ -alv ] [ -n </code><i>nx</i><code> ]</code></dt>
<dd>Prints the block mapping for the current open file using the fiemap ioctl. Options behave as described in the <code><a href="/docs/linux/man/8-xfs_bmap/">xfs_bmap</a></code>(8) manual page.</dd>
<dt><code>extsize [ -R | -D ] [ </code><i>value</i><code> ]</code></dt>
<dd>Display and/or modify the preferred extent size used when allocating space for the currently open file. If the <code>-R</code> option is specified, a recursive descent is performed for all directory entries below the currently open file (<code>-D</code> can be used to restrict the output to directories only). If the target file is a directory, then the inherited extent size is set for that directory (new files created in that directory inherit that extent size). The <i>value</i> should be specified in bytes, or using one of the usual units suffixes (k, m, g, b, etc). The extent size is always reported in units of bytes.</dd>
<dt><code>cowextsize [ -R | -D ] [ </code><i>value</i><code> ]</code></dt>
<dd>Display and/or modify the preferred copy-on-write extent size used when allocating space for the currently open file. If the <code>-R</code> option is specified, a recursive descent is performed for all directory entries below the currently open file (<code>-D</code> can be used to restrict the output to directories only). If the target file is a directory, then the inherited CoW extent size is set for that directory (new files created in that directory inherit that CoW extent size). The <i>value</i> should be specified in bytes, or using one of the usual units suffixes (k, m, g, b, etc). The extent size is always reported in units of bytes.</dd>
<dt><code>allocsp </code><i>size</i><code> 0</code></dt>
<dd>Sets the size of the file to <i>size</i> and zeroes any additional space allocated using the XFS_IOC_ALLOCSP/XFS_IOC_FREESP system call described in the <code><a href="/docs/linux/man/3-xfsctl/">xfsctl</a></code>(3) manual page. <code>allocsp</code> and <code>freesp</code> do exactly the same thing.</dd>
<dt><code>freesp </code><i>size</i><code> 0</code></dt>
<dd>See the <code>allocsp</code> command.</dd>
<dt><code>fadvise [ -r | -s | [[ -d | -n | -w ] </code><i>offset length </i><code>]]</code></dt>
<dd>On platforms which support it, allows hints be given to the system regarding the expected I/O patterns on the file. The range arguments are required by some advise commands ([*] below), and the others must have no range arguments. With no arguments, the POSIX_FADV_NORMAL advice is implied (default readahead).</dd>
<dl>
<dd>
</dd><dl>
<dt><code>-d</code></dt>
<dd>the data will not be accessed again in the near future (POSIX_FADV_DONTNEED[*]).</dd>
<dt><code>-n</code></dt>
<dd>data will be accessed once and not be reused (POSIX_FADV_NOREUSE[*]).</dd>
<dt><code>-r</code></dt>
<dd>expect access to data in random order (POSIX_FADV_RANDOM), which sets readahead to zero.</dd>
<dt><code>-s</code></dt>
<dd>expect access to data in sequential order (POSIX_FADV_SEQUENTIAL), which doubles the default readahead on the file.</dd>
<dt><code>-w</code></dt>
<dd>advises the specified data will be needed again (POSIX_FADV_WILLNEED[*]) which forces the maximum readahead.</dd></dl>
</dl>
<dt><code>fdatasync</code></dt>
<dd>Calls <code><a href="/docs/linux/man/2-fdatasync/">fdatasync</a></code>(2) to flush the file&#8217;s in-core data to disk.</dd>
<dt><code>fsync</code></dt>
<dd>Calls <code><a href="/docs/linux/man/2-fsync/">fsync</a></code>(2) to flush all in-core file state to disk.</dd>
<dt><code>s</code></dt>
<dd>See the <code>fsync</code> command.</dd>
<dt><code>sync_range [ -a | -b | -w ] offset length </code></dt>
<dd>On platforms which support it, allows control of syncing a range of the file to disk. With no options, SYNC_FILE_RANGE_WRITE is implied on the range supplied.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>-a</code></dt>
<dd>wait for IO in the given range to finish after writing (SYNC_FILE_RANGE_WAIT_AFTER).</dd>
<dt><code>-b</code></dt>
<dd>wait for IO in the given range to finish before writing (SYNC_FILE_RANGE_WAIT_BEFORE).</dd>
<dt><code>-w</code></dt>
<dd>start writeback of dirty data in the given range (SYNC_FILE_RANGE_WRITE).</dd></dl>
</dl>
<dt><code>sync</code></dt>
<dd>Calls <code><a href="/docs/linux/man/2-sync/">sync</a></code>(2) to flush all filesystems&#8217; in-core data to disk.</dd>
<dt><code>syncfs</code></dt>
<dd>Calls <code><a href="/docs/linux/man/2-syncfs/">syncfs</a></code>(2) to flush this filesystem&#8217;s in-core data to disk.</dd>
<dt><code>resvsp</code><i> offset length</i></dt>
<dd>Allocates reserved, unwritten space for part of a file using the XFS_IOC_RESVSP system call described in the <code><a href="/docs/linux/man/3-xfsctl/">xfsctl</a></code>(3) manual page.</dd>
<dt><code>unresvsp</code><i> offset length</i></dt>
<dd>Frees reserved space for part of a file using the XFS_IOC_UNRESVSP system call described in the <code><a href="/docs/linux/man/3-xfsctl/">xfsctl</a></code>(3) manual page.</dd>
<dt><code>falloc [ -k ]</code><i> offset length</i></dt>
<dd>Allocates reserved, unwritten space for part of a file using the fallocate routine as described in the <code><a href="/docs/linux/man/2-fallocate/">fallocate</a></code>(2) manual page.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>-k</code></dt>
<dd>will set the FALLOC_FL_KEEP_SIZE flag as described in <code><a href="/docs/linux/man/2-fallocate/">fallocate</a></code>(2).</dd></dl>
</dl>
<dt><code>fcollapse</code><i> offset length</i></dt>
<dd>Call fallocate with FALLOC_FL_COLLAPSE_RANGE flag as described in the <code><a href="/docs/linux/man/2-fallocate/">fallocate</a></code>(2) manual page to de-allocates blocks and eliminates the hole created in this process by shifting data blocks into the hole.</dd>
<dt><code>finsert</code><i> offset length</i></dt>
<dd>Call fallocate with FALLOC_FL_INSERT_RANGE flag as described in the <code><a href="/docs/linux/man/2-fallocate/">fallocate</a></code>(2) manual page to create the hole by shifting data blocks.</dd>
<dt><code>fpunch</code><i> offset length</i></dt>
<dd>Punches (de-allocates) blocks in the file by calling fallocate with the FALLOC_FL_PUNCH_HOLE flag as described in the <code><a href="/docs/linux/man/2-fallocate/">fallocate</a></code>(2) manual page.</dd>
<dt><code>funshare</code><i> offset length</i></dt>
<dd>Call fallocate with FALLOC_FL_UNSHARE_RANGE flag as described in the <code><a href="/docs/linux/man/2-fallocate/">fallocate</a></code>(2) manual page to unshare all shared blocks within the range.</dd>
<dt><code>fzero</code><i> offset length</i></dt>
<dd>Call fallocate with FALLOC_FL_ZERO_RANGE flag as described in the <code><a href="/docs/linux/man/2-fallocate/">fallocate</a></code>(2) manual page to allocate and zero blocks within the range.</dd>
<dt><code>zero</code><i> offset length</i></dt>
<dd>Call xfsctl with <code>XFS_IOC_ZERO_RANGE</code> as described in the <code><a href="/docs/linux/man/3-xfsctl/">xfsctl</a></code>(3) manual page to allocate and zero blocks within the range.</dd>
<dt><code>truncate</code><i> offset</i></dt>
<dd>Truncates the current file at the given offset using <code><a href="/docs/linux/man/2-ftruncate/">ftruncate</a></code>(2).</dd>
<dt><code>sendfile -i </code><i>srcfile</i><code> | -f </code><i>N</i><code> [ </code><i>offset length </i><code>]</code></dt>
<dd>On platforms which support it, allows a direct in-kernel copy between two file descriptors. The current open file is the target, the source must be specified as another open file (<code>-f</code>) or by path (<code>-i</code>).</dd>
<dt><code>readdir [ -v ] [ -o </code><i>offset</i><code> ] [ -l </code><i>length</i><code> ] </code></dt>
<dd>Read a range of directory entries from a given offset of a directory.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>-v</code></dt>
<dd>verbose mode &#8211; dump dirent content as defined in <code><a href="/docs/linux/man/3-readdir/">readdir</a></code>(3)</dd>
<dt><code>-o</code></dt>
<dd>specify starting <i>offset</i></dd>
<dt><code>-l</code></dt>
<dd>specify total <i>length</i> to read (in bytes)</dd></dl>
</dl>
<dt>
</dt><dt><code>seek -a | -d | -h [ -r ] [ -s ] offset</code></dt>
<dd>
</dd><dd>On platforms that support the <code><a href="/docs/linux/man/2-lseek/">lseek</a></code>(2) <code>SEEK_DATA</code> and <code>SEEK_HOLE</code> options, display the offsets of the specified segments.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>-a</code></dt>
<dd>Display both <code>data</code> and <code>hole</code> segments starting at the specified <code>offset.</code></dd>
<dt><code>-d</code></dt>
<dd>Display the <code>data</code> segment starting at the specified <code>offset.</code></dd>
<dt><code>-h</code></dt>
<dd>Display the <code>hole</code> segment starting at the specified <code>offset.</code></dd>
<dt><code>-r</code></dt>
<dd>Recursively display all the specified segments starting at the specified <code>offset.</code></dd>
<dt><code>-s</code></dt>
<dd>Display the starting <a href="/docs/linux/man/2-lseek/">lseek</a>(2) offset. This offset will be a calculated value when both data and holes are displayed together or performing a recusively display.</dd></dl>
</dl>
<dt>
</dt><dt><code>reflink [ -C ] [ -q ] src_file [src_offset dst_offset length]</code></dt>
<dd>
</dd><dd>On filesystems that support the <code>XFS_IOC_CLONE_RANGE</code> or <code>BTRFS_IOC_CLONE_RANGE</code> ioctls, map <i>length</i> bytes at offset <i>dst_offset</i> in the open file to the same physical blocks that are mapped at offset <i>src_offset</i> in the file <i>src_file</i> , replacing any contents that may already have been there. If a program writes into a reflinked block range of either file, the dirty blocks will be cloned, written to, and remapped (&quot;copy on write&quot;) in the affected file, leaving the other file(s) unchanged. If src_offset, dst_offset, and length are omitted, all contents of src_file will be reflinked into the open file.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>-C</code></dt>
<dd>Print timing statistics in a condensed format.</dd>
<dt><code>-q</code></dt>
<dd>Do not print timing statistics at all.</dd></dl>
</dl>
<dt>
</dt><dt><code>dedupe [ -C ] [ -q ] src_file src_offset dst_offset length</code></dt>
<dd>
</dd><dd>On filesystems that support the <code>XFS_IOC_FILE_EXTENT_SAME</code> or <code>BTRFS_IOC_FILE_EXTENT_SAME</code> ioctls, map <i>length</i> bytes at offset <i>dst_offset</i> in the open file to the same physical blocks that are mapped at offset <i>src_offset</i> in the file <i>src_file</i> , but only if the contents of both ranges are identical. This is known as block-based deduplication. If a program writes into a reflinked block range of either file, the dirty blocks will be cloned, written to, and remapped (&quot;copy on write&quot;) in the affected file, leaving the other file(s) unchanged.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>-C</code></dt>
<dd>Print timing statistics in a condensed format.</dd>
<dt><code>-q</code></dt>
<dd>Do not print timing statistics at all.</dd></dl>
</dl>
<dt>
</dt><dt><code>copy_range [ -s </code><i>src_offset</i><code> ] [ -d </code><i>dst_offset</i><code> ] [ -l </code><i>length</i><code> ] src_file</code></dt>
<dd>
</dd><dd>On filesystems that support the <code><a href="/docs/linux/man/2-copy_file_range/">copy_file_range</a></code>(2) system call, copies data from the <i>src_file</i> into the open file. If <i>src_offset</i>, <i>dst_offset</i>, and <i>length</i> are omitted the contents of src_file will be copied to the beginning of the open file, overwriting any data already there.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>-s</code></dt>
<dd>Copy data from <i>src_file</i> beginning from <i>src_offset</i>.</dd>
<dt><code>-d</code></dt>
<dd>Copy data into the open file beginning at <i>dst_offset</i>.</dd>
<dt><code>-l</code></dt>
<dd>Copy up to <i>length</i> bytes of data. </dd>
</dl>
</dl>
</dl>
<h2>Memory Mapped I/O Commands</h2>
<dl>
<dt><code>mmap [ </code><i>N</i><code> | [[ -rwx ] [-s </code><i>size</i><code> ] </code><i>offset length </i><code>]]</code></dt>
<dd>With no arguments, <code>mmap</code> shows the current mappings. Specifying a single numeric argument <i>N</i> sets the current mapping. If two arguments are specified (a range specified by <i>offset</i> and <i>length</i>), a new mapping is created spanning the range, and the protection mode can be given as a combination of PROT_READ (<code>-r</code>), PROT_WRITE (<code>-w</code>), and PROT_EXEC (<code>-x</code>). <code>-s</code><i> size</i> is used to do a mmap(size) &amp;&amp; munmap(size) operation at first, try to reserve some extendible free memory space, if <i>size</i> is bigger than <i>length</i> parameter. But there&#8217;s not guarantee that the memory after <i>length</i> ( up to <i>size</i> ) will stay free. <code>e.g.</code> &quot;mmap -rw -s 8192 1024&quot; will mmap 0 ~ 1024 bytes memory, but try to reserve 1024 ~ 8192 free space(no guarantee). This free space will helpful for &quot;mremap 8192&quot; without MREMAP_MAYMOVE flag.</dd>
<dt><code>mm</code></dt>
<dd>See the <code>mmap</code> command.</dd>
<dt><code>mremap [ -f &lt;new_address&gt; ] [ -m ] </code><i>new_length</i></dt>
<dd>Changes the current mapping size to <i>new_length</i>. Whether the mapping may be moved is controlled by the flags passed; MREMAP_FIXED (<code>-f</code>), or MREMAP_MAYMOVE (<code>-m</code>). <i>new_length</i> specifies a page-aligned address to which the mapping must be moved. It can be setted to 139946004389888, 4096k or 1g etc.</dd>
<dt><code>mrm</code></dt>
<dd>See the <code>mremap</code> command.</dd>
<dt><code>munmap</code></dt>
<dd>Unmaps the current memory mapping.</dd>
<dt><code>mu</code></dt>
<dd>See the <code>munmap</code> command.</dd>
<dt><code>mread [ -f | -v ] [ -r ] [</code><i> offset length </i><code>]</code></dt>
<dd>Accesses a segment of the current memory mapping, optionally dumping it to the standard output stream (with <code>-v</code> or <code>-f</code> option) for inspection. The accesses are performed sequentially from the start <i>offset</i> by default, but can also be done from the end backwards through the mapping if the <code>-r</code> option in specified. The two verbose modes differ only in the relative offsets they display, the <code>-f</code> option is relative to file start, whereas <code>-v</code> shows offsets relative to the start of the mapping.</dd>
<dt><code>mr</code></dt>
<dd>See the <code>mread</code> command.</dd>
<dt><code>mwrite [ -r ] [ -S </code><i>seed</i><code> ] [ </code><i>offset length </i><code>]</code></dt>
<dd>Stores a byte into memory for a range within a mapping. The default stored value is &#8216;X&#8217;, repeated to fill the range specified, but this can be changed using the <code>-S</code> option. The memory stores are performed sequentially from the start offset by default, but can also be done from the end backwards through the mapping if the <code>-r</code> option in specified.</dd>
<dt><code>mw</code></dt>
<dd>See the <code>mwrite</code> command.</dd>
<dt><code>msync [ -i ] [ -a | -s ] [ </code><i>offset length </i><code>]</code></dt>
<dd>Writes all modified copies of pages over the specified range (or entire mapping if no range specified) to their backing storage locations. Also, optionally invalidates (<code>-i</code>) so that subsequent references to the pages will be obtained from their backing storage locations (instead of cached copies). The flush can be done synchronously (<code>-s)</code> or asynchronously (<code>-a</code>).</dd>
<dt><code>ms</code></dt>
<dd>See the <code>msync</code> command.</dd>
<dt><code>madvise [ -d | -r | -s | -w ] [ </code><i>offset length </i><code>]</code></dt>
<dd>Modifies page cache behavior when operating on the current mapping. The range arguments are required by some advise commands ([*] below). With no arguments, the POSIX_MADV_NORMAL advice is implied (default readahead).</dd>
<dl>
<dd>
</dd><dl>
<dt><code>-d</code></dt>
<dd>the pages will not be needed (POSIX_MADV_DONTNEED[*]).</dd>
<dt><code>-r</code></dt>
<dd>expect random page references (POSIX_MADV_RANDOM), which sets readahead to zero.</dd>
<dt><code>-s</code></dt>
<dd>expect sequential page references (POSIX_MADV_SEQUENTIAL), which doubles the default readahead on the file.</dd>
<dt><code>-w</code></dt>
<dd>advises the specified pages will be needed again (POSIX_MADV_WILLNEED[*]) which forces the maximum readahead.</dd></dl>
</dl>
<dt><code>mincore</code></dt>
<dd>Dumps a list of pages or ranges of pages that are currently in core, for the current memory mapping. </dd>
</dl>
<h2>Other Commands</h2>
<dl>
<dt><code>help [ </code>command<code> ]</code></dt>
<dd>Display a brief description of one or all commands.</dd>
<dt><code>print</code></dt>
<dd>Display a list of all open files and memory mapped regions. The current file and current mapping are distinguishable from any others.</dd>
<dt><code>p</code></dt>
<dd>See the <code>print</code> command.</dd>
<dt><code>quit</code></dt>
<dd>Exit <code>xfs_io</code>.</dd>
<dt><code>q</code></dt>
<dd>See the <code>quit</code> command.</dd>
<dt><code>lsattr</code> [ <code>-R</code> | <code>-D</code> | <code>-a</code> | <code>-v</code> ]</dt>
<dd>List extended inode flags on the currently open file. If the <code>-R</code> option is specified, a recursive descent is performed for all directory entries below the currently open file (<code>-D</code> can be used to restrict the output to directories only). This is a depth first descent, it does not follow symlinks and it also does not cross mount points.</dd>
<dt><code>chattr</code> [ <code>-R</code> | <code>-D</code> ] [ <code>+</code>/<code>-riasAdtPneEfS</code> ]</dt>
<dd>Change extended inode flags on the currently open file. The <code>-R</code> and <code>-D</code> options have the same meaning as above. The mapping between each letter and the inode flags (refer to <code><a href="/docs/linux/man/3-xfsctl/">xfsctl</a></code>(3) for the full list) is available via the <code>help</code> command.</dd>
<dt><code>freeze</code></dt>
<dd>Suspend all write I/O requests to the filesystem of the current file. Only available in expert mode and requires privileges.</dd>
<dt><code>thaw</code></dt>
<dd>Undo the effects of a filesystem freeze operation. Only available in expert mode and requires privileges.</dd>
<dt><code>flink </code><i>path</i></dt>
<dd>Link the currently open file descriptor into the filesystem namespace.</dd>
<dt><code>inject [ </code><i>tag</i><code> ]</code></dt>
<dd>Inject errors into a filesystem to observe filesystem behavior at specific points under adverse conditions. Without the <i>tag</i> argument, displays the list of error tags available. Only available in expert mode and requires privileges.</dd>
<dt><code>resblks [ </code><i>blocks</i><code> ]</code></dt>
<dd>Get and/or set count of reserved filesystem blocks using the XFS_IOC_GET_RESBLKS or XFS_IOC_SET_RESBLKS system calls. Note &#8212; this can be useful for exercising out of space behavior. Only available in expert mode and requires privileges.</dd>
<dt><code>shutdown</code> [ <code>-f</code> ]</dt>
<dd>Force the filesystem to shutdown (with or without flushing the log). Only available in expert mode and requires privileges.</dd>
<dt><code>stat</code> [ <code>-v</code> ]</dt>
<dd>Selected statistics from <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) and the XFS_IOC_GETXATTR system call on the current file. If the <code>-v</code> option is specified, the atime (last access), mtime (last modify), and ctime (last change) timestamps are also displayed.</dd>
<dt><code>statfs</code></dt>
<dd>Selected statistics from <code><a href="/docs/linux/man/2-statfs/">statfs</a></code>(2) and the XFS_IOC_FSGEOMETRY system call on the filesystem where the current file resides.</dd>
<dt><code>chproj</code> [ <code>-R</code>|<code>-D</code> ]</dt>
<dd>Modifies the project identifier associated with the current path. The <code>-R</code> option will recursively descend if the current path is a directory. The <code>-D</code> option will also recursively descend, only setting modifying projects on subdirectories. See the <code><a href="/docs/linux/man/8-xfs_quota/">xfs_quota</a></code>(8) manual page for more information about project identifiers.</dd>
<dt><code>lsproj</code> [ <code>-R</code>|<code>-D</code> ]</dt>
<dd>Displays the project identifier associated with the current path. The <code>-R</code> and <code>-D</code> options behave as described above, in <code>chproj.</code></dd>
<dt><code>parent</code> [ <code>-cpv</code> ]</dt>
<dd>By default this command prints out the parent inode numbers, inode generation numbers and basenames of all the hardlinks which point to the inode of the current file.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>-p</code></dt>
<dd>the output is similar to the default output except pathnames up to the mount-point are printed out instead of the component name.</dd>
<dt><code>-c</code></dt>
<dd>the file&#8217;s filesystem will check all the parent attributes for consistency.</dd>
<dt><code>-v</code></dt>
<dd>verbose output will be printed.</dd></dl>
</dl>
<dd><code>[NOTE: Not currently operational on Linux.]</code> </dd>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mkfs-xfs/">mkfs.xfs</a></code>(8), <code><a href="/docs/linux/man/3-xfsctl/">xfsctl</a></code>(3), <code><a href="/docs/linux/man/8-xfs_bmap/">xfs_bmap</a></code>(8), <code><a href="/docs/linux/man/8-xfs_db/">xfs_db</a></code>(8), <code><a href="/docs/linux/man/5-xfs/">xfs</a></code>(5), <code><a href="/docs/linux/man/2-fdatasync/">fdatasync</a></code>(2), <code><a href="/docs/linux/man/2-fstat/">fstat</a></code>(2), <code><a href="/docs/linux/man/2-fstatfs/">fstatfs</a></code>(2), <code><a href="/docs/linux/man/2-fsync/">fsync</a></code>(2), <code><a href="/docs/linux/man/2-ftruncate/">ftruncate</a></code>(2), <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), <code><a href="/docs/linux/man/2-msync/">msync</a></code>(2), <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/2-pread/">pread</a></code>(2), <code><a href="/docs/linux/man/2-pwrite/">pwrite</a></code>(2), <code><a href="/docs/linux/man/3-readdir/">readdir</a></code>(3). </p>
