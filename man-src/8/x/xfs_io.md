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
<dt><code>-c</code><i> cmd</i></p>
<dd><code>xfs_io</code> commands may be run interactively (the default) or as arguments on the command line. Multiple <code>-c</code> arguments may be given. The commands are run in the sequence given, then the program exits.</p>
<dt><code>-p</code><i> prog</i></p>
<dd>Set the program name for prompts and some error messages, the default value is <code>xfs_io</code>.</p>
<dt><code>-f</code></p>
<dd>Create <i>file</i> if it does not already exist.</p>
<dt><code>-r</code></p>
<dd>Open <i>file</i> read-only, initially. This is required if <i>file</i> is immutable or append-only.</p>
<dt><code>-i</code></p>
<dd>Start an idle thread. The purpose of this idle thread is to test io from a multi threaded process. With single threaded process, the file table is not shared and file structs are not reference counted. Spawning an idle thread can help detecting file struct reference leaks.</p>
<dt><code>-x</code></p>
<dd>Expert mode. Dangerous commands are only available in this mode. These commands also tend to require additional privileges.</p>
<dt><code>-V</code></p>
<dd>Prints the version number and exits.</dl>
<p> The other <code><a href="/docs/linux/man/2-open/">open</a></code>(2) options described below are also available from the command line.</p>
<h2>Concepts</h2>
<p><code>xfs_io</code> maintains a number of open files and memory mappings. Files can be initially opened on the command line (optionally), and additional files can also be opened later. </p>
<p> <code>xfs_io</code> commands can be broken up into three groups. Some commands are aimed at doing regular file I/O &#8211; read, write, sync, space preallocation, etc. </p>
<p> The second set of commands exist for manipulating memory mapped regions of a file &#8211; mapping, accessing, storing, unmapping, flushing, etc. </p>
<p> The remaining commands are for the navigation and display of data structures relating to the open files, mappings, and the filesystems where they reside. </p>
<p> Many commands have extensive online help. Use the <code>help</code> command for more details on any command.</p>
<h2>File I/O Commands</h2>
<dl>
<dt><code>file [ </code><i>N</i><code> ]</code></p>
<dd>Display a list of all open files and (optionally) switch to an alternate current open file.</p>
<dt><code>open [[ -acdfrstRT ] </code><i>path</i><code> ]</code></p>
<dd>Closes the current file, and opens the file specified by <i>path</i> instead. Without any arguments, displays statistics about the current file &#8211; see the <code>stat</code> command.</p>
<dl>
<dd>
<dl>
<dt><code>-a</code></p>
<dd>opens append-only (O_APPEND).</p>
<dt><code>-d</code></p>
<dd>opens for direct I/O (O_DIRECT).</p>
<dt><code>-f</code></p>
<dd>creates the file if it doesn&#8217;t already exist (O_CREAT).</p>
<dt><code>-r</code></p>
<dd>opens read-only (O_RDONLY).</p>
<dt><code>-s</code></p>
<dd>opens for synchronous I/O (O_SYNC).</p>
<dt><code>-t</code></p>
<dd>truncates on open (O_TRUNC).</p>
<dt><code>-n</code></p>
<dd>opens in non-blocking mode if possible (O_NONBLOCK).</p>
<dt><code>-T</code></p>
<dd>create a temporary file not linked into the filesystem namespace (O_TMPFILE). The pathname passed must refer to a directory which is treated as virtual parent for the newly created invisible file. Can not be used together with the <code>-r</code> option.</p>
<dt><code>-R</code></p>
<dd>marks the file as a realtime XFS file after opening it, if it is not already marked as such.</dl>
</dl>
<dt><code>o</code></p>
<dd>See the <code>open</code> command.</p>
<dt><code>close</code></p>
<dd>Closes the current open file, marking the next open file as current (if one exists).</p>
<dt><code>c</code></p>
<dd>See the <code>close</code> command.</p>
<dt><code>pread [ -b </code><i>bsize</i><code> ] [ -v ] [ -FBR [ -Z </code><i>seed</i><code> ] ] [ -V </code><i>vectors</i><code> ] </code><i>offset length</i></p>
<dd>Reads a range of bytes in a specified blocksize from the given <i>offset</i>.</p>
<dl>
<dd>
<dl>
<dt><code>-b</code></p>
<dd>can be used to set the blocksize into which the <code><a href="/docs/linux/man/2-read/">read</a></code>(2) requests will be split. The default blocksize is 4096 bytes.</p>
<dt><code>-v</code></p>
<dd>dump the contents of the buffer after reading, by default only the count of bytes actually read is dumped.</p>
<dt><code>-F</code></p>
<dd>read the buffers in a forwards sequential direction.</p>
<dt><code>-B</code></p>
<dd>read the buffers in a reserve sequential direction.</p>
<dt><code>-R</code></p>
<dd>read the buffers in the give range in a random order.</p>
<dt><code>-Z seed</code></p>
<dd>specify the random number seed used for random reads.</p>
<dt><code>-V vectors</code></p>
<dd>Use the vectored IO read syscall <code><a href="/docs/linux/man/2-preadv/">preadv</a></code>(2) with a number of blocksize length iovecs. The number of iovecs is set by the <i>vectors</i> parameter.</dl>
</dl>
<dt><code>r</code></p>
<dd>See the <code>pread</code> command.</p>
<dt><code>pwrite [ -i </code><i>file</i><code> ] [ -d ] [ -s </code><i>skip</i><code> ] [ -b </code><i>size</i><code> ] [ -S </code><i>seed</i><code> ] [ -FBR [ -Z </code><i>zeed</i><code> ] ] [ -wW ] [ -V </code><i>vectors</i><code> ] </code><i>offset length</i></p>
<dd>Writes a range of bytes in a specified blocksize from the given <i>offset</i>. The bytes written can be either a set pattern or read in from another file before writing.</p>
<dl>
<dd>
<dl>
<dt><code>-i</code></p>
<dd>allows an input <i>file</i> to be specified as the source of the data to be written.</p>
<dt><code>-d</code></p>
<dd>causes direct I/O, rather than the usual buffered I/O, to be used when reading the input file.</p>
<dt><code>-s</code></p>
<dd>specifies the number of bytes to <i>skip</i> from the start of the input file before starting to read.</p>
<dt><code>-b</code></p>
<dd>used to set the blocksize into which the <code><a href="/docs/linux/man/2-write/">write</a></code>(2) requests will be split. The default blocksize is 4096 bytes.</p>
<dt><code>-S</code></p>
<dd>used to set the (repeated) fill pattern which is used when the data to write is not coming from a file. The default buffer fill pattern value is 0xcdcdcdcd.</p>
<dt><code>-F</code></p>
<dd>write the buffers in a forwards sequential direction.</p>
<dt><code>-B</code></p>
<dd>write the buffers in a reserve sequential direction.</p>
<dt><code>-R</code></p>
<dd>write the buffers in the give range in a random order.</p>
<dt><code>-Z seed</code></p>
<dd>specify the random number seed used for random write</p>
<dt><code>-w</code></p>
<dd>call <code><a href="/docs/linux/man/2-fdatasync/">fdatasync</a></code>(2) once all writes are complete (included in timing results)</p>
<dt><code>-W</code></p>
<dd>call <code><a href="/docs/linux/man/2-fsync/">fsync</a></code>(2) once all writes are complete (included in timing results)</p>
<dt><code>-V vectors</code></p>
<dd>Use the vectored IO write syscall <code><a href="/docs/linux/man/2-pwritev/">pwritev</a></code>(2) with a number of blocksize length iovecs. The number of iovecs is set by the <i>vectors</i> parameter.</dl>
</dl>
<dt><code>w</code></p>
<dd>See the <code>pwrite</code> command.</p>
<dt><code>bmap [ -acdelpv ] [ -n </code><i>nx</i><code> ]</code></p>
<dd>Prints the block mapping for the current open file. Refer to the <code><a href="/docs/linux/man/8-xfs_bmap/">xfs_bmap</a></code>(8) manual page for complete documentation.</p>
<dt><code>fiemap [ -alv ] [ -n </code><i>nx</i><code> ]</code></p>
<dd>Prints the block mapping for the current open file using the fiemap ioctl. Options behave as described in the <code><a href="/docs/linux/man/8-xfs_bmap/">xfs_bmap</a></code>(8) manual page.</p>
<dt><code>extsize [ -R | -D ] [ </code><i>value</i><code> ]</code></p>
<dd>Display and/or modify the preferred extent size used when allocating space for the currently open file. If the <code>-R</code> option is specified, a recursive descent is performed for all directory entries below the currently open file (<code>-D</code> can be used to restrict the output to directories only). If the target file is a directory, then the inherited extent size is set for that directory (new files created in that directory inherit that extent size). The <i>value</i> should be specified in bytes, or using one of the usual units suffixes (k, m, g, b, etc). The extent size is always reported in units of bytes.</p>
<dt><code>cowextsize [ -R | -D ] [ </code><i>value</i><code> ]</code></p>
<dd>Display and/or modify the preferred copy-on-write extent size used when allocating space for the currently open file. If the <code>-R</code> option is specified, a recursive descent is performed for all directory entries below the currently open file (<code>-D</code> can be used to restrict the output to directories only). If the target file is a directory, then the inherited CoW extent size is set for that directory (new files created in that directory inherit that CoW extent size). The <i>value</i> should be specified in bytes, or using one of the usual units suffixes (k, m, g, b, etc). The extent size is always reported in units of bytes.</p>
<dt><code>allocsp </code><i>size</i><code> 0</code></p>
<dd>Sets the size of the file to <i>size</i> and zeroes any additional space allocated using the XFS_IOC_ALLOCSP/XFS_IOC_FREESP system call described in the <code><a href="/docs/linux/man/3-xfsctl/">xfsctl</a></code>(3) manual page. <code>allocsp</code> and <code>freesp</code> do exactly the same thing.</p>
<dt><code>freesp </code><i>size</i><code> 0</code></p>
<dd>See the <code>allocsp</code> command.</p>
<dt><code>fadvise [ -r | -s | [[ -d | -n | -w ] </code><i>offset length </i><code>]]</code></p>
<dd>On platforms which support it, allows hints be given to the system regarding the expected I/O patterns on the file. The range arguments are required by some advise commands ([*] below), and the others must have no range arguments. With no arguments, the POSIX_FADV_NORMAL advice is implied (default readahead).</p>
<dl>
<dd>
<dl>
<dt><code>-d</code></p>
<dd>the data will not be accessed again in the near future (POSIX_FADV_DONTNEED[*]).</p>
<dt><code>-n</code></p>
<dd>data will be accessed once and not be reused (POSIX_FADV_NOREUSE[*]).</p>
<dt><code>-r</code></p>
<dd>expect access to data in random order (POSIX_FADV_RANDOM), which sets readahead to zero.</p>
<dt><code>-s</code></p>
<dd>expect access to data in sequential order (POSIX_FADV_SEQUENTIAL), which doubles the default readahead on the file.</p>
<dt><code>-w</code></p>
<dd>advises the specified data will be needed again (POSIX_FADV_WILLNEED[*]) which forces the maximum readahead.</dl>
</dl>
<dt><code>fdatasync</code></p>
<dd>Calls <code><a href="/docs/linux/man/2-fdatasync/">fdatasync</a></code>(2) to flush the file&#8217;s in-core data to disk.</p>
<dt><code>fsync</code></p>
<dd>Calls <code><a href="/docs/linux/man/2-fsync/">fsync</a></code>(2) to flush all in-core file state to disk.</p>
<dt><code>s</code></p>
<dd>See the <code>fsync</code> command.</p>
<dt><code>sync_range [ -a | -b | -w ] offset length </code></p>
<dd>On platforms which support it, allows control of syncing a range of the file to disk. With no options, SYNC_FILE_RANGE_WRITE is implied on the range supplied.</p>
<dl>
<dd>
<dl>
<dt><code>-a</code></p>
<dd>wait for IO in the given range to finish after writing (SYNC_FILE_RANGE_WAIT_AFTER).</p>
<dt><code>-b</code></p>
<dd>wait for IO in the given range to finish before writing (SYNC_FILE_RANGE_WAIT_BEFORE).</p>
<dt><code>-w</code></p>
<dd>start writeback of dirty data in the given range (SYNC_FILE_RANGE_WRITE).</dl>
</dl>
<dt><code>sync</code></p>
<dd>Calls <code><a href="/docs/linux/man/2-sync/">sync</a></code>(2) to flush all filesystems&#8217; in-core data to disk.</p>
<dt><code>syncfs</code></p>
<dd>Calls <code><a href="/docs/linux/man/2-syncfs/">syncfs</a></code>(2) to flush this filesystem&#8217;s in-core data to disk.</p>
<dt><code>resvsp</code><i> offset length</i></p>
<dd>Allocates reserved, unwritten space for part of a file using the XFS_IOC_RESVSP system call described in the <code><a href="/docs/linux/man/3-xfsctl/">xfsctl</a></code>(3) manual page.</p>
<dt><code>unresvsp</code><i> offset length</i></p>
<dd>Frees reserved space for part of a file using the XFS_IOC_UNRESVSP system call described in the <code><a href="/docs/linux/man/3-xfsctl/">xfsctl</a></code>(3) manual page.</p>
<dt><code>falloc [ -k ]</code><i> offset length</i></p>
<dd>Allocates reserved, unwritten space for part of a file using the fallocate routine as described in the <code><a href="/docs/linux/man/2-fallocate/">fallocate</a></code>(2) manual page.</p>
<dl>
<dd>
<dl>
<dt><code>-k</code></p>
<dd>will set the FALLOC_FL_KEEP_SIZE flag as described in <code><a href="/docs/linux/man/2-fallocate/">fallocate</a></code>(2).</dl>
</dl>
<dt><code>fcollapse</code><i> offset length</i></p>
<dd>Call fallocate with FALLOC_FL_COLLAPSE_RANGE flag as described in the <code><a href="/docs/linux/man/2-fallocate/">fallocate</a></code>(2) manual page to de-allocates blocks and eliminates the hole created in this process by shifting data blocks into the hole.</p>
<dt><code>finsert</code><i> offset length</i></p>
<dd>Call fallocate with FALLOC_FL_INSERT_RANGE flag as described in the <code><a href="/docs/linux/man/2-fallocate/">fallocate</a></code>(2) manual page to create the hole by shifting data blocks.</p>
<dt><code>fpunch</code><i> offset length</i></p>
<dd>Punches (de-allocates) blocks in the file by calling fallocate with the FALLOC_FL_PUNCH_HOLE flag as described in the <code><a href="/docs/linux/man/2-fallocate/">fallocate</a></code>(2) manual page.</p>
<dt><code>funshare</code><i> offset length</i></p>
<dd>Call fallocate with FALLOC_FL_UNSHARE_RANGE flag as described in the <code><a href="/docs/linux/man/2-fallocate/">fallocate</a></code>(2) manual page to unshare all shared blocks within the range.</p>
<dt><code>fzero</code><i> offset length</i></p>
<dd>Call fallocate with FALLOC_FL_ZERO_RANGE flag as described in the <code><a href="/docs/linux/man/2-fallocate/">fallocate</a></code>(2) manual page to allocate and zero blocks within the range.</p>
<dt><code>zero</code><i> offset length</i></p>
<dd>Call xfsctl with <code>XFS_IOC_ZERO_RANGE</code> as described in the <code><a href="/docs/linux/man/3-xfsctl/">xfsctl</a></code>(3) manual page to allocate and zero blocks within the range.</p>
<dt><code>truncate</code><i> offset</i></p>
<dd>Truncates the current file at the given offset using <code><a href="/docs/linux/man/2-ftruncate/">ftruncate</a></code>(2).</p>
<dt><code>sendfile -i </code><i>srcfile</i><code> | -f </code><i>N</i><code> [ </code><i>offset length </i><code>]</code></p>
<dd>On platforms which support it, allows a direct in-kernel copy between two file descriptors. The current open file is the target, the source must be specified as another open file (<code>-f</code>) or by path (<code>-i</code>).</p>
<dt><code>readdir [ -v ] [ -o </code><i>offset</i><code> ] [ -l </code><i>length</i><code> ] </code></p>
<dd>Read a range of directory entries from a given offset of a directory.</p>
<dl>
<dd>
<dl>
<dt><code>-v</code></p>
<dd>verbose mode &#8211; dump dirent content as defined in <code><a href="/docs/linux/man/3-readdir/">readdir</a></code>(3)</p>
<dt><code>-o</code></p>
<dd>specify starting <i>offset</i></p>
<dt><code>-l</code></p>
<dd>specify total <i>length</i> to read (in bytes)</dl>
</dl>
<dt>
<dt><code>seek -a | -d | -h [ -r ] [ -s ] offset</code></p>
<dd>
<dd>On platforms that support the <code><a href="/docs/linux/man/2-lseek/">lseek</a></code>(2) <code>SEEK_DATA</code> and <code>SEEK_HOLE</code> options, display the offsets of the specified segments.</p>
<dl>
<dd>
<dl>
<dt><code>-a</code></p>
<dd>Display both <code>data</code> and <code>hole</code> segments starting at the specified <code>offset.</code></p>
<dt><code>-d</code></p>
<dd>Display the <code>data</code> segment starting at the specified <code>offset.</code></p>
<dt><code>-h</code></p>
<dd>Display the <code>hole</code> segment starting at the specified <code>offset.</code></p>
<dt><code>-r</code></p>
<dd>Recursively display all the specified segments starting at the specified <code>offset.</code></p>
<dt><code>-s</code></p>
<dd>Display the starting <a href="/docs/linux/man/2-lseek/">lseek</a>(2) offset. This offset will be a calculated value when both data and holes are displayed together or performing a recusively display.</dl>
</dl>
<dt>
<dt><code>reflink [ -C ] [ -q ] src_file [src_offset dst_offset length]</code></p>
<dd>
<dd>On filesystems that support the <code>XFS_IOC_CLONE_RANGE</code> or <code>BTRFS_IOC_CLONE_RANGE</code> ioctls, map <i>length</i> bytes at offset <i>dst_offset</i> in the open file to the same physical blocks that are mapped at offset <i>src_offset</i> in the file <i>src_file</i> , replacing any contents that may already have been there. If a program writes into a reflinked block range of either file, the dirty blocks will be cloned, written to, and remapped (&quot;copy on write&quot;) in the affected file, leaving the other file(s) unchanged. If src_offset, dst_offset, and length are omitted, all contents of src_file will be reflinked into the open file.</p>
<dl>
<dd>
<dl>
<dt><code>-C</code></p>
<dd>Print timing statistics in a condensed format.</p>
<dt><code>-q</code></p>
<dd>Do not print timing statistics at all.</dl>
</dl>
<dt>
<dt><code>dedupe [ -C ] [ -q ] src_file src_offset dst_offset length</code></p>
<dd>
<dd>On filesystems that support the <code>XFS_IOC_FILE_EXTENT_SAME</code> or <code>BTRFS_IOC_FILE_EXTENT_SAME</code> ioctls, map <i>length</i> bytes at offset <i>dst_offset</i> in the open file to the same physical blocks that are mapped at offset <i>src_offset</i> in the file <i>src_file</i> , but only if the contents of both ranges are identical. This is known as block-based deduplication. If a program writes into a reflinked block range of either file, the dirty blocks will be cloned, written to, and remapped (&quot;copy on write&quot;) in the affected file, leaving the other file(s) unchanged.</p>
<dl>
<dd>
<dl>
<dt><code>-C</code></p>
<dd>Print timing statistics in a condensed format.</p>
<dt><code>-q</code></p>
<dd>Do not print timing statistics at all.</dl>
</dl>
<dt>
<dt><code>copy_range [ -s </code><i>src_offset</i><code> ] [ -d </code><i>dst_offset</i><code> ] [ -l </code><i>length</i><code> ] src_file</code></p>
<dd>
<dd>On filesystems that support the <code><a href="/docs/linux/man/2-copy_file_range/">copy_file_range</a></code>(2) system call, copies data from the <i>src_file</i> into the open file. If <i>src_offset</i>, <i>dst_offset</i>, and <i>length</i> are omitted the contents of src_file will be copied to the beginning of the open file, overwriting any data already there.</p>
<dl>
<dd>
<dl>
<dt><code>-s</code></p>
<dd>Copy data from <i>src_file</i> beginning from <i>src_offset</i>.</p>
<dt><code>-d</code></p>
<dd>Copy data into the open file beginning at <i>dst_offset</i>.</p>
<dt><code>-l</code></p>
<dd>Copy up to <i>length</i> bytes of data. </p>
</dl>
</dl>
</dl>
<h2>Memory Mapped I/O Commands</h2>
<dl>
<dt><code>mmap [ </code><i>N</i><code> | [[ -rwx ] [-s </code><i>size</i><code> ] </code><i>offset length </i><code>]]</code></p>
<dd>With no arguments, <code>mmap</code> shows the current mappings. Specifying a single numeric argument <i>N</i> sets the current mapping. If two arguments are specified (a range specified by <i>offset</i> and <i>length</i>), a new mapping is created spanning the range, and the protection mode can be given as a combination of PROT_READ (<code>-r</code>), PROT_WRITE (<code>-w</code>), and PROT_EXEC (<code>-x</code>). <code>-s</code><i> size</i> is used to do a mmap(size) &amp;&amp; munmap(size) operation at first, try to reserve some extendible free memory space, if <i>size</i> is bigger than <i>length</i> parameter. But there&#8217;s not guarantee that the memory after <i>length</i> ( up to <i>size</i> ) will stay free. <code>e.g.</code> &quot;mmap -rw -s 8192 1024&quot; will mmap 0 ~ 1024 bytes memory, but try to reserve 1024 ~ 8192 free space(no guarantee). This free space will helpful for &quot;mremap 8192&quot; without MREMAP_MAYMOVE flag.</p>
<dt><code>mm</code></p>
<dd>See the <code>mmap</code> command.</p>
<dt><code>mremap [ -f &lt;new_address&gt; ] [ -m ] </code><i>new_length</i></p>
<dd>Changes the current mapping size to <i>new_length</i>. Whether the mapping may be moved is controlled by the flags passed; MREMAP_FIXED (<code>-f</code>), or MREMAP_MAYMOVE (<code>-m</code>). <i>new_length</i> specifies a page-aligned address to which the mapping must be moved. It can be setted to 139946004389888, 4096k or 1g etc.</p>
<dt><code>mrm</code></p>
<dd>See the <code>mremap</code> command.</p>
<dt><code>munmap</code></p>
<dd>Unmaps the current memory mapping.</p>
<dt><code>mu</code></p>
<dd>See the <code>munmap</code> command.</p>
<dt><code>mread [ -f | -v ] [ -r ] [</code><i> offset length </i><code>]</code></p>
<dd>Accesses a segment of the current memory mapping, optionally dumping it to the standard output stream (with <code>-v</code> or <code>-f</code> option) for inspection. The accesses are performed sequentially from the start <i>offset</i> by default, but can also be done from the end backwards through the mapping if the <code>-r</code> option in specified. The two verbose modes differ only in the relative offsets they display, the <code>-f</code> option is relative to file start, whereas <code>-v</code> shows offsets relative to the start of the mapping.</p>
<dt><code>mr</code></p>
<dd>See the <code>mread</code> command.</p>
<dt><code>mwrite [ -r ] [ -S </code><i>seed</i><code> ] [ </code><i>offset length </i><code>]</code></p>
<dd>Stores a byte into memory for a range within a mapping. The default stored value is &#8216;X&#8217;, repeated to fill the range specified, but this can be changed using the <code>-S</code> option. The memory stores are performed sequentially from the start offset by default, but can also be done from the end backwards through the mapping if the <code>-r</code> option in specified.</p>
<dt><code>mw</code></p>
<dd>See the <code>mwrite</code> command.</p>
<dt><code>msync [ -i ] [ -a | -s ] [ </code><i>offset length </i><code>]</code></p>
<dd>Writes all modified copies of pages over the specified range (or entire mapping if no range specified) to their backing storage locations. Also, optionally invalidates (<code>-i</code>) so that subsequent references to the pages will be obtained from their backing storage locations (instead of cached copies). The flush can be done synchronously (<code>-s)</code> or asynchronously (<code>-a</code>).</p>
<dt><code>ms</code></p>
<dd>See the <code>msync</code> command.</p>
<dt><code>madvise [ -d | -r | -s | -w ] [ </code><i>offset length </i><code>]</code></p>
<dd>Modifies page cache behavior when operating on the current mapping. The range arguments are required by some advise commands ([*] below). With no arguments, the POSIX_MADV_NORMAL advice is implied (default readahead).</p>
<dl>
<dd>
<dl>
<dt><code>-d</code></p>
<dd>the pages will not be needed (POSIX_MADV_DONTNEED[*]).</p>
<dt><code>-r</code></p>
<dd>expect random page references (POSIX_MADV_RANDOM), which sets readahead to zero.</p>
<dt><code>-s</code></p>
<dd>expect sequential page references (POSIX_MADV_SEQUENTIAL), which doubles the default readahead on the file.</p>
<dt><code>-w</code></p>
<dd>advises the specified pages will be needed again (POSIX_MADV_WILLNEED[*]) which forces the maximum readahead.</dl>
</dl>
<dt><code>mincore</code></p>
<dd>Dumps a list of pages or ranges of pages that are currently in core, for the current memory mapping. </p>
</dl>
<h2>Other Commands</h2>
<dl>
<dt><code>help [ </code>command<code> ]</code></p>
<dd>Display a brief description of one or all commands.</p>
<dt><code>print</code></p>
<dd>Display a list of all open files and memory mapped regions. The current file and current mapping are distinguishable from any others.</p>
<dt><code>p</code></p>
<dd>See the <code>print</code> command.</p>
<dt><code>quit</code></p>
<dd>Exit <code>xfs_io</code>.</p>
<dt><code>q</code></p>
<dd>See the <code>quit</code> command.</p>
<dt><code>lsattr</code> [ <code>-R</code> | <code>-D</code> | <code>-a</code> | <code>-v</code> ]</p>
<dd>List extended inode flags on the currently open file. If the <code>-R</code> option is specified, a recursive descent is performed for all directory entries below the currently open file (<code>-D</code> can be used to restrict the output to directories only). This is a depth first descent, it does not follow symlinks and it also does not cross mount points.</p>
<dt><code>chattr</code> [ <code>-R</code> | <code>-D</code> ] [ <code>+</code>/<code>-riasAdtPneEfS</code> ]</p>
<dd>Change extended inode flags on the currently open file. The <code>-R</code> and <code>-D</code> options have the same meaning as above. The mapping between each letter and the inode flags (refer to <code><a href="/docs/linux/man/3-xfsctl/">xfsctl</a></code>(3) for the full list) is available via the <code>help</code> command.</p>
<dt><code>freeze</code></p>
<dd>Suspend all write I/O requests to the filesystem of the current file. Only available in expert mode and requires privileges.</p>
<dt><code>thaw</code></p>
<dd>Undo the effects of a filesystem freeze operation. Only available in expert mode and requires privileges.</p>
<dt><code>flink </code><i>path</i></p>
<dd>Link the currently open file descriptor into the filesystem namespace.</p>
<dt><code>inject [ </code><i>tag</i><code> ]</code></p>
<dd>Inject errors into a filesystem to observe filesystem behavior at specific points under adverse conditions. Without the <i>tag</i> argument, displays the list of error tags available. Only available in expert mode and requires privileges.</p>
<dt><code>resblks [ </code><i>blocks</i><code> ]</code></p>
<dd>Get and/or set count of reserved filesystem blocks using the XFS_IOC_GET_RESBLKS or XFS_IOC_SET_RESBLKS system calls. Note &#8212; this can be useful for exercising out of space behavior. Only available in expert mode and requires privileges.</p>
<dt><code>shutdown</code> [ <code>-f</code> ]</p>
<dd>Force the filesystem to shutdown (with or without flushing the log). Only available in expert mode and requires privileges.</p>
<dt><code>stat</code> [ <code>-v</code> ]</p>
<dd>Selected statistics from <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) and the XFS_IOC_GETXATTR system call on the current file. If the <code>-v</code> option is specified, the atime (last access), mtime (last modify), and ctime (last change) timestamps are also displayed.</p>
<dt><code>statfs</code></p>
<dd>Selected statistics from <code><a href="/docs/linux/man/2-statfs/">statfs</a></code>(2) and the XFS_IOC_FSGEOMETRY system call on the filesystem where the current file resides.</p>
<dt><code>chproj</code> [ <code>-R</code>|<code>-D</code> ]</p>
<dd>Modifies the project identifier associated with the current path. The <code>-R</code> option will recursively descend if the current path is a directory. The <code>-D</code> option will also recursively descend, only setting modifying projects on subdirectories. See the <code><a href="/docs/linux/man/8-xfs_quota/">xfs_quota</a></code>(8) manual page for more information about project identifiers.</p>
<dt><code>lsproj</code> [ <code>-R</code>|<code>-D</code> ]</p>
<dd>Displays the project identifier associated with the current path. The <code>-R</code> and <code>-D</code> options behave as described above, in <code>chproj.</code></p>
<dt><code>parent</code> [ <code>-cpv</code> ]</p>
<dd>By default this command prints out the parent inode numbers, inode generation numbers and basenames of all the hardlinks which point to the inode of the current file.</p>
<dl>
<dd>
<dl>
<dt><code>-p</code></p>
<dd>the output is similar to the default output except pathnames up to the mount-point are printed out instead of the component name.</p>
<dt><code>-c</code></p>
<dd>the file&#8217;s filesystem will check all the parent attributes for consistency.</p>
<dt><code>-v</code></p>
<dd>verbose output will be printed.</dl>
</dl>
<dd><code>[NOTE: Not currently operational on Linux.]</code> </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mkfs-xfs/">mkfs.xfs</a></code>(8), <code><a href="/docs/linux/man/3-xfsctl/">xfsctl</a></code>(3), <code><a href="/docs/linux/man/8-xfs_bmap/">xfs_bmap</a></code>(8), <code><a href="/docs/linux/man/8-xfs_db/">xfs_db</a></code>(8), <code><a href="/docs/linux/man/5-xfs/">xfs</a></code>(5), <code><a href="/docs/linux/man/2-fdatasync/">fdatasync</a></code>(2), <code><a href="/docs/linux/man/2-fstat/">fstat</a></code>(2), <code><a href="/docs/linux/man/2-fstatfs/">fstatfs</a></code>(2), <code><a href="/docs/linux/man/2-fsync/">fsync</a></code>(2), <code><a href="/docs/linux/man/2-ftruncate/">ftruncate</a></code>(2), <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), <code><a href="/docs/linux/man/2-msync/">msync</a></code>(2), <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/2-pread/">pread</a></code>(2), <code><a href="/docs/linux/man/2-pwrite/">pwrite</a></code>(2), <code><a href="/docs/linux/man/3-readdir/">readdir</a></code>(3). </p>
