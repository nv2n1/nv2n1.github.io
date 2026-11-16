---
title: "mkudffs(8)"
name: "mkudffs"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mkudffs/"
description: "mkudffs – create an UDF filesystem"
---

<p>mkudffs &#8211; create an UDF filesystem</p>
<h2>Synopsis</h2>
<p><code>mkudffs [ switches ] </code><i>device</i><code> [ </code><i>blocks-count</i><code> ] </code> </p>
<h2>Description</h2>
<p><code>mkudffs</code> is used to create a UDF filesystem on a device (usually a disk). <i>device</i> is the special file corresponding to the device (e.g <i>/dev/hdX</i>). <i>blocks-count</i> is the number of blocks on the device. If omitted, <code>mkudffs</code> automagically figures the file system size. </p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;help</code></dt>
<dd>Display the usage and list of options. </dd>
<dt><code>-b,&#8211;blocksize=</code><i> block-size </i></dt>
<dd>Specify the size of blocks in bytes. Valid block size vales are 1024, 2048 and 4096 bytes per block. If omitted, <code>mkudffs</code> block-size is 2048. </dd>
<dt><code>-r,&#8211;udfrev=</code><i> udf-revision </i></dt>
<dd>Specify the udf revision to use. Valid revisions are 0x0201, 0x0200, 0x0150, and 0x0102. If omitted, <code>mkudffs</code> udf-revision is 0x0201. </dd>
<dt><code>&#8211;lvid=</code><i> logical-volume-ident </i></dt>
<dd>Specify the logical volume identifier. </dd>
<dt><code>&#8211;vid=</code><i> volume-ident </i></dt>
<dd>Specify the volume identifier. </dd>
<dt><code>&#8211;vsid=</code><i> volume-set-ident </i></dt>
<dd>Specify the volume set identifier. </dd>
<dt><code>&#8211;fsid=</code><i> file-set-ident </i></dt>
<dd>Specify the file set identifier. </dd>
<dt><code>&#8211;strategy=</code><i> strategy </i></dt>
<dd>Specify the allocation strategy to use. Valid strategies are 4 and 4096. If omitted, <code>mkudffs</code> strategy is based on the <i>media-type</i>. </dd>
<dt><code>&#8211;spartable=</code><i> spartable-number </i></dt>
<dd>Specify the number of sparing tables to write to disc. Valid numbers are 1 &#8211; 4. This option implies <code>&#8211;media-type=</code><i>cdrw</i>. </dd>
<dt><code>&#8211;media-type=</code><i> media-type </i></dt>
<dd>Specify the media type. Valid media types are:</dd>
<dl>
<dd>
</dd><dl>
<dt>hd</dt>
<dd>hard drive</dd>
<dt>dvd</dt>
<dd>DVD (Digital Versital Disc)</dd>
<dt>dvdram</dt>
<dd>DVD-RAM (Digital Versital Disc-Random Access Memory)</dd>
<dt>worm</dt>
<dd>WORM (Write Once Ready Many)</dd>
<dt>mo</dt>
<dd>MO (Magneto Optical)</dd>
<dt>cdrw</dt>
<dd>CD-RW (CD Read-Write)</dd></dl>
</dl>
<dt><code>&#8211;space=</code><i> space </i></dt>
<dd>
</dd><dl>
<dd>
</dd><dl>
<dt>freedbitmap</dt>
<dd>Freed bitmap</dd>
<dt>freedtable</dt>
<dd>Freed table</dd>
<dt>unallocbitmap</dt>
<dd>Unallocated bitmap</dd>
<dt>unalloctable</dt>
<dd>Unallocated table</dd></dl>
</dl>
<dt><code>&#8211;ad=</code><i> ad </i></dt>
<dd>
</dd><dl>
<dd>
</dd><dl>
<dt>inicb</dt>
<dd>Allocation Descriptors in ICB</dd>
<dt>short</dt>
<dd>Short Allocation Descriptors</dd>
<dt>long</dt>
<dd>Long Allocation Descriptors</dd></dl>
</dl>
<dt><code>&#8211;noefe</code></dt>
<dd>Don&#8217;t Use Extended File Entries</dd>
<dt><code>&#8211;u8</code></dt>
<dd>Use 8-bit unicode for file names</dd>
<dt><code>&#8211;u16</code></dt>
<dd>Use 16-bit unicode for file names</dd>
<dt><code>&#8211;utf8</code></dt>
<dd>Use UTF-8 for file names</dd>
<dt><code>&#8211;closed</code></dt>
<dd>
</dd><dt><code>&#8211;bridge</code></dt>
<dd>
</dd><dt><code>&#8211;packetlen=</code><i> length </i></dt>
<dd></dd></dl>
<h2>Exit Status</h2>
<p><code>mkudffs</code> returns 0 if successful, non-zero if there are problems.</p>
<h2>Author</h2>
<pre>Ben Fennema &lt;bfennema [at] falcon.csc.calpoly.edu&gt;</pre>
<h2>Availability</h2>
<p><code>mkudffs</code> is part of the udftools package and is available from <a rel="nofollow" href="http://linux-udf.sourceforge.net.">http://linux-udf.sourceforge.net.</a></p>
