---
title: "fusecompress(1)"
name: "fusecompress"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fusecompress/"
description: "fusecompress – mounts an compressed virtual filesystem"
---

<h2>NAME</h2>
<p> fusecompress &#8211; mounts an compressed virtual filesystem</p>
<h2>SYNOPSIS</h2>
<p> <code>fusecompress [OPTION]&#8230; rootDir mountPoint</code></p>
<h2>DESCRIPTION</h2>
<p> FuseCompress creates a virtual compressed filesystem which stores compressed data in the rootDir directory and makes the uncompressed data visible at the mountPoint directory. </p>
<p> Compression type (or uncompressed state) of files in the rootDir is not changed during work. Use fusecompress_offline if you want to decompress file(s) or change compression type of the file(s). </p>
<p> <code>Examples:</code> </p>
<p> Storage directory is /tmp/fc and mount point is /mnt/fc in all following examples. </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>o Mount directory</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>fusecompress /tmp/fc /mnt/fc</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>o Unmount directory</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>fusermount -u /mnt/fc</p>
<p> <code>Tips and tricks:</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>How to obtain compression ratio?</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>o<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Run this command in the mountPoint directory when mounted with FuseCompress:</p>
<pre>
                        du -sh # actual size on disk
                        du -sh --apparent-size # actual size of files
</pre>
<p> <code>File and magic utilities:</code> </p>
<p> Put this config into ~/.magic or /etc/magic file to allow file utility recognize FuseCompress file format: </p>
<pre>
        0       string  \135\211    FuseCompress(ed) data
</pre>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Prints help.</p>
<dt><code>-v, &#8211;version</code></p>
<dd> Prints version.</p>
<dt><code>-o, &#8211;options</code></p>
<dd>
<p> <code>fc_c:arg</code> set compression method (lzo/bzip2/zlib/lzma) (default:zlib) </p>
<p> <code>fc_b:arg</code> set size of the blocks in kilobytes (default:100) </p>
<p> <code>fc_d</code> run in debug mode </p>
<p> <code>fc_ma:arg1;arg2</code> files with passed mime types to be always not compressed </p>
<p> <code>fc_mr:arg1;arg2</code> files with passed mime types to be always compressed </p>
<p> Other options are passed directly to the fuse library. See fuse documentation for full list of supported options. </p>
<p> Useful parameters for fuse library: </p>
<p> Fuse library must be configured to support this features &#8211; configuration file /etc/fuse.conf must contains at least this option: user_allow_other. </p>
<p> <code>allow_other</code> </p>
<p> This option overrides the security measure restricting file access to the user mounting the filesystem. So all users (including root) can access the files. This option is by default only allowed to root, but this restriction can be removed with a configuration option described in the previous section. </p>
<p> <code>allow_root</code> </p>
<p> This option is similar to &#8216;allow_other&#8217; but file access is limited to the user mounting the filesystem and root. This option and &#8216;allow_other&#8217; are mutually exclusive. </p>
<p> <code>nonempty</code> </p>
<p> This option allows you to use the same directory for rootDir and mountPoint.<br />
&nbsp;<wbr> Lzo is the fastest, bzip2 has high compression ratio, but it is the slowest, zlib is somewhere between them in terms of speed and compression ratio and lzma has highest compression ratio, it&#8217;s compression speed is better than bzip2 and decompression is fast. The none compression method is there for testing only as it doesn&#8217;t compress data, it copies the data without any modification (fusecompress&#8217; header is added). </p>
<p> Block size influences compression ratio. Bigger block size allows better compression ratio, but random access to data will be slower and memory requirements will be bigger. </p>
</dl>
<h2>DISCLAIMER</h2>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. Please refer to the &quot;COPYING&quot; file distributed with fusecompress for complete details.</p>
<h2>AUTHORS</h2>
<p> fusecompress was written by Milan Svoboda &lt;milan.svoboda [at] centrum.cz&gt;.</p>
<h2>SEE ALSO</h2>
<p> fusecompress_offline </p>
<h2>Index</h2>
