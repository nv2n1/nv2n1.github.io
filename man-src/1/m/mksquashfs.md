---
title: "mksquashfs(1)"
name: "mksquashfs"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mksquashfs/"
description: "mksquashfs – tool to create and append to squashfs filesystems"
---

<h2 class="name">NAME</h2>
<p> mksquashfs &#8211; tool to create and append to squashfs filesystems</p>
<h2>SYNOPSIS</h2>
<p> <code>mksquashfs</code> <i>SOURCE</i> [<i>SOURCE2</i> <i>&#8230;</i>] <i>DESTINATION</i> [<i>OPTIONS</i>] </p>
<h2>DESCRIPTION</h2>
<p> Squashfs is a highly compressed read-only filesystem for Linux. It uses zlib compression to compress both files, inodes and directories. Inodes in the system are very small and all blocks are packed to minimize data overhead. Block sizes greater than 4K are supported up to a maximum of 64K. </p>
<p> Squashfs is intended for general read-only filesystem use, for archival use (i.e. in cases where a .tar.gz file may be used), and in constrained block device/memory systems (e.g. embedded systems) where low overhead is needed. </p>
<h2>OPTIONS</h2>
<h3>Filesystem build options</h3>
<dl>
<dt>-comp <i>COMPRESSION</i></p>
<dd> select <i>COMPRESSION</i> compression. Compressors available: gzip (default), lzo, xz.</p>
<dt>-b <i>BLOCK_SIZE</i></p>
<dd> set data block to <i>BLOCK_SIZE</i>. Default 131072 bytes.</p>
<dt>-no-exports</p>
<dd> don&#8217;t make the filesystem exportable via NFS.</p>
<dt>-no-sparse</p>
<dd> don&#8217;t detect sparse files.</p>
<dt>-no-xattrs</p>
<dd> don&#8217;t store extended attributes.</p>
<dt>-xattrs</p>
<dd> store extended attributes (default).</p>
<dt>-noI</p>
<dd> do not compress inode table.</p>
<dt>-noD</p>
<dd> do not compress data blocks.</p>
<dt>-noF</p>
<dd> do not compress fragment blocks.</p>
<dt>-noX</p>
<dd> do not compress extended attributes.</p>
<dt>-no-fragments</p>
<dd> do not use fragments.</p>
<dt>-always-use-fragments</p>
<dd> use fragment blocks for files larger than block size.</p>
<dt>-no-duplicates</p>
<dd> do not perform duplicate checking.</p>
<dt>-all-root</p>
<dd> make all files owned by root.</p>
<dt>-force-uid uid</p>
<dd> set all file uids to uid.</p>
<dt>-force-gid gid</p>
<dd> set all file gids to gid.</p>
<dt>-nopad</p>
<dd> do not pad filesystem to a multiple of 4K.</p>
<dt>-keep-as-directory</p>
<dd> if one source directory is specified, create a root directory containing that directory, rather than the contents of the directory. </p>
</dl>
<h3>Filesystem filter options</h3>
<dl>
<dt>-p <i>PSEUDO_DEFINITION</i></p>
<dd> Add pseudo file definition.</p>
<dt>-pf <i>PSEUDO_FILE</i></p>
<dd> Add list of pseudo file definitions.</p>
<dt>-sort <i>SORT_FILE</i></p>
<dd> sort files according to priorities in <i>SORT_FILE</i>. One file or dir with priority per line. Priority -32768 to 32767, default priority 0.</p>
<dt>-ef <i>EXCLUDE_FILE</i></p>
<dd> list of exclude dirs/files. One per line.</p>
<dt>-wildcards</p>
<dd> Allow extended shell wildcards (globbing) to be used in exclude dirs/files</p>
<dt>-regex</p>
<dd> Allow POSIX regular expressions to be used in exclude dirs/files. </p>
</dl>
<h3>Filesystem append options</h3>
<dl>
<dt>-noappend</p>
<dd> do not append to existing filesystem.</p>
<dt>-root-becomes <i>NAME</i></p>
<dd> when appending source files/directories, make the original root become a subdirectory in the new root called <i>NAME</i>, rather than adding the new source items to the original root. </p>
</dl>
<h3>Mksquashfs runtime options:</h3>
<dl>
<dt>-version</p>
<dd> print version, licence and copyright message.</p>
<dt>-recover <i>NAME</i></p>
<dd> recover filesystem data using recovery file <i>NAME</i>.</p>
<dt>-no-recovery</p>
<dd> don&#8217;t generate a recovery file.</p>
<dt>-info</p>
<dd> print files written to filesystem.</p>
<dt>-no-progress</p>
<dd> don&#8217;t display the progress bar.</p>
<dt>-processors <i>NUMBER</i></p>
<dd> Use <i>NUMBER</i> processors. By default will use number of processors available.</p>
<dt>-read-queue <i>SIZE</i></p>
<dd> Set input queue to <i>SIZE</i> Mbytes. Default 64 Mbytes.</p>
<dt>-write-queue <i>SIZE</i></p>
<dd> Set output queue to <i>SIZE</i> Mbytes. Default 512 Mbytes.</p>
<dt>-fragment-queue <i>SIZE</i></p>
<dd> Set fragment queue to <i>SIZE</i> Mbytes. Default 64 Mbytes. </p>
</dl>
<h3>Miscellaneous options</h3>
<dl>
<dt>-root-owned</p>
<dd> alternative name for -all-root.</p>
<dt>-noInodeCompression</p>
<dd> alternative name for -noI.</p>
<dt>-noDataCompression</p>
<dd> alternative name for -noD.</p>
<dt>-noFragmentCompression</p>
<dd> alternative name for -noF.</p>
<dt>-noXattrCompression</p>
<dd> alternative name for -noX. </p>
</dl>
<h3>Compressors available and compressor specific options</h3>
<dl>
<dt>gzip (no options) (default)</p>
<dd>
<dt>lzo (no options)</p>
<dd>
<dt>xz</p>
<dd>
<dt>-Xbcj filter1,filter2,&#8230;,filterN</p>
<dd> Compress using filter1,filter2,&#8230;,filterN in turn (in addition to no filter), and choose the best compression. Available filters: x86, arm, armthumb, powerpc, sparc, ia64.</p>
<dt>-Xdict-size <i>DICT_SIZE</i></p>
<dd> Use <i>DICT_SIZE</i> as the XZ dictionary size. The dictionary size can be specified as a percentage of the block size, or as an absolute value. The dictionary size must be less than or equal to the block size and 8192 bytes or larger. It must also be storable in the xz header as either 2^n or as 2^n+2^(n+1). Example dict-sizes are 75%, 50%, 37.5%, 25%, or 32K, 16K, 8K etc. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-unsquashfs/">unsquashfs</a>(1) </p>
<h2>HOMEPAGE</h2>
<p> More information about mksquashfs and the squashfs filesystem can be found at &lt;<i><a rel="nofollow" href="http://squashfs.sourceforge.net/">http://squashfs.sourceforge.net/</a></i>&gt;. </p>
<h2>AUTHOR</h2>
<p> squashfs was written by Phillip Lougher &lt;<i>phillip [at] squashfs.org.uk</i>&gt;. </p>
<p> This manual page was written by Daniel Baumann &lt;<i>mail [at] daniel-baumann.ch</i>&gt;. </p>
<h2>Index</h2>
