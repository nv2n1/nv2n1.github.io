---
title: "checksums-h(3)"
name: "checksums-h"
section: "3"
letter: "c"
url: "/docs/linux/man/3-checksums-h/"
description: "checksums.h –"
---

<p>checksums.h &#8211; </p>
<h2>Synopsis</h2>
<p>#include &lt;stddef.h&gt;<br />
 #include &#8216;io.h&#8217; </p>
<h3>Functions</h3>
<p>char * <code>dmlite_checksum_full_name</code> (const char *shortName, char *output, size_t osize)<br />
 <i>Puts into output the full name of the checksum algorithm specified with shortName. </i><br />
 char * <code>dmlite_checksum_short_name</code> (const char *longName, char *output, size_t osize)<br />
 <i>Puts into output the short name of the checksum algorithm specified with longName. </i><br />
 int <code>dmlite_checksum_md5</code> (<code>dmlite_fd</code> *fd, off_t offset, off_t size, char *output, size_t outsize)<br />
 <i>Generated the MD5 checksum of the given file. </i><br />
 int <code>dmlite_checksum_crc32</code> (<code>dmlite_fd</code> *fd, off_t offset, off_t size, char *output, size_t outsize)<br />
 <i>Generated the CRC32 checksum of the given file. </i><br />
 int <code>dmlite_checksum_adler32</code> (<code>dmlite_fd</code> *fd, off_t offset, off_t size, char *output, size_t outsize)<br />
 <i>Generated the Adler32 checksum of the given file. </i></p>
<h2>Function Documentation</h2>
<h3>int dmlite_checksum_adler32 (<code>dmlite_fd</code> *fd, off_toffset, off_tsize, char *output, size_toutsize)</h3>
<p>Generated the Adler32 checksum of the given file. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>fd</i> The file descriptor where to read the data to digest.<br />
 <i>offset</i> Where to start to digest.<br />
 <i>size</i> The number of bytes to digest. 0 means the whole file.<br />
 <i>output</i> Where to put the resulting checksum (in hexadecimal)<br />
 <i>outsize</i> The size of the memory area pointed by output.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3>int dmlite_checksum_crc32 (<code>dmlite_fd</code> *fd, off_toffset, off_tsize, char *output, size_toutsize)</h3>
<p>Generated the CRC32 checksum of the given file. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>fd</i> The file descriptor where to read the data to digest.<br />
 <i>offset</i> Where to start to digest.<br />
 <i>size</i> The number of bytes to digest. 0 means the whole file.<br />
 <i>output</i> Where to put the resulting checksum (in decimal)<br />
 <i>outsize</i> The size of the memory area pointed by output.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3>char* dmlite_checksum_full_name (const char *shortName, char *output, size_tosize)</h3>
<p>Puts into output the full name of the checksum algorithm specified with shortName. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>shortName</i> The checksum short name (CS, AD, MD)<br />
 <i>output</i> The full name will be put here.<br />
 <i>osize</i> The size of the buffer pointed by output.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The same value as the pointer output</dl>
<h3>int dmlite_checksum_md5 (<code>dmlite_fd</code> *fd, off_toffset, off_tsize, char *output, size_toutsize)</h3>
<p>Generated the MD5 checksum of the given file. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>fd</i> The file descriptor where to read the data to digest.<br />
 <i>offset</i> Where to start to digest.<br />
 <i>size</i> The number of bytes to digest. 0 means the whole file.<br />
 <i>output</i> Where to put the resulting checksum (in hexadecimal)<br />
 <i>outsize</i> The size of the memory area pointed by output.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3>char* dmlite_checksum_short_name (const char *longName, char *output, size_tosize)</h3>
<p>Puts into output the short name of the checksum algorithm specified with longName. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>shortName</i> The checksum long name (MD5, ADLER32, &#8230;)<br />
 <i>output</i> The short name will be put here.<br />
 <i>osize</i> The size of the buffer pointed by output.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The same value as the pointer output</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for dmlite from the source code.</p>
