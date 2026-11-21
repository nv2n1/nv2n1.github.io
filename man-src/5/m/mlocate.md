---
title: "mlocate(5)"
name: "mlocate"
section: "5"
letter: "m"
url: "/docs/linux/man/5-mlocate/"
description: "mlocate.db – a mlocate database"
---
<p>mlocate.db &#8211; a mlocate database  </p>
<h2>DESCRIPTION</h2>
<p> A mlocate database starts with a file header: 8 bytes for a magic number (<code>&quot;\0mlocate&quot;</code> like a C literal), 4 bytes for the <i>configuration block</i> size in big endian, 1 byte for file format version (<code>0</code>), 1 byte for the ``require visibility&#8217;&#8216; flag (<code>0</code> or <code>1</code>), 2 bytes padding, and a NUL-terminated path name of the root of the database. </p>
<p>The header is followed by a <i>configuration block</i>, included to ensure databases are not reused if some configuration changes could affect their contents. The size of the configuration block in bytes is stored in the file header. The configuration block is a sequence of <i>variable assignments</i>, ordered by variable name. Each <i>variable assignment</i> consists of a NUL-terminated variable name and an ordered list of NUL-terminated values. The value list is terminated by one more <font SIZE="-1">NUL</font> character. The ordering used is defined by the <code>strcmp ()</code> function. </p>
<p>Currently defined variables are: </p>
<dl>
<dt><code>prune_bind_mounts</code></dt>
<dd> <p> A single entry, the value of PRUNE_BIND_MOUNTS; one of the strings <code>0</code> or <code>1</code>. </p>
 </dd>
<dt><code>prunefs</code></dt>
<dd> <p> The value of <code>PRUNEFS</code>, each entry is converted to uppercase. </p>
 </dd>
<dt><code>prunepaths</code></dt>
<dd> <p> The value of <code>PRUNEPATHS</code>. </p>
 </dd></dl>
<p>The rest of the file until <font SIZE="-1">EOF</font> describes directories and their contents. Each directory starts with a header: 8 bytes for <i>directory time</i> (seconds) in big endian, 4 bytes for <i>directory time</i> (nanoseconds) in big endian (0 if unknown, less than 1,000,000,000), 4 bytes padding, and a NUL-terminated path name of the the directory. Directory contents, a sequence of <i>file entries</i> sorted by name, follow. </p>
<p> <i>Directory time</i> is the maximum of <code>st_ctime</code> and <code>st_mtime</code> of the directory. <code><a href="/docs/linux/man/8-updatedb/">updatedb</a></code>(8) uses the original data if the <i>directory time</i> in the database and in the file system match exactly. <i>Directory time</i> equal to 0 always causes rescanning of the directory: this is necessary to handle directories which were being updated while building the database. </p>
<p>Each <i>file entry</i> starts with a single byte, marking its type: </p>
<dl>
<dt><code>0</code></dt>
<dd> <p> A non-directory file. Followed by a NUL-terminated file (not path) name. </p>
 </dd>
<dt><code>1</code></dt>
<dd> <p> A subdirectory. Followed by a NUL-terminated file (not path) name. </p>
 </dd>
<dt><code>2</code></dt>
<dd> <p> Marks the end of the current directory. </p>
 </dd></dl>
<p> <code><a href="/docs/linux/man/1-locate/">locate</a>(1)</code> only reports file entries, directory names are not reported because they are reported as an entry in their parent directory. The only exception is the root directory of the database, which is stored in the file header. </p>
<h2>AUTHOR</h2>
<p> Miloslav Trmac &lt;mitr [at] redhat.com&gt; </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-locate/">locate</a></code>(1), <code>updatedb.conf</code>(5), <code><a href="/docs/linux/man/8-updatedb/">updatedb</a></code>(8) </p>
<h2>Index</h2>
<dl>
<dt><a href="#lbAB">NAME</a></dt>
<dd>  </dd>
<dt><a href="#lbAC">DESCRIPTION</a></dt>
<dd>  </dd>
<dt><a href="#lbAD">AUTHOR</a></dt>
<dd>  </dd>
<dt><a href="#lbAE">SEE ALSO</a></dt>
<dd>  </dd></dl>
