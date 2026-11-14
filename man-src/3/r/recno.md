---
title: "recno(3)"
name: "recno"
section: "3"
letter: "r"
url: "/docs/linux/man/3-recno/"
description: "recno – record number database access method"
---

<p>recno &#8211; record number database access method</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sys/types.h&gt;
#include &lt;db.h&gt;</code></pre>
<h2>Description</h2>
<p><i>Note well</i>: This page documents interfaces provided in glibc up until version 2.1. Since version 2.2, glibc no longer provides these interfaces. Probably, you are looking for the APIs provided by the <i>libdb</i> library instead. </p>
<p> The routine <code><a href="/docs/linux/man/3-dbopen/">dbopen</a></code>(3) is the library interface to database files. One of the supported file formats is record number files. The general description of the database access methods is in <code><a href="/docs/linux/man/3-dbopen/">dbopen</a></code>(3), this manual page describes only the recno-specific information. </p>
<p> The record number data structure is either variable or fixed-length records stored in a flat-file format, accessed by the logical record number. The existence of record number five implies the existence of records one through four, and the deletion of record number one causes record number five to be renumbered to record number four, as well as the cursor, if positioned after record number one, to shift down one record. </p>
<p> The recno access-method-specific data structure provided to <code><a href="/docs/linux/man/3-dbopen/">dbopen</a></code>(3) is defined in the <i>&lt;db.h&gt;</i> include file as follows: </p>
<p> typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long flags;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int&nbsp;<wbr>&nbsp;cachesize;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int&nbsp;<wbr>&nbsp;psize;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;lorder;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;reclen;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned char bval;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*bfname; } RECNOINFO; </p>
<p> The elements of this structure are defined as follows:</p>
<dl>
<dt><i>flags</i></p>
<dd>The flag value is specified by ORing any of the following values:</p>
<dl>
<dd>
<dl>
<dt><code>R_FIXEDLEN</code></p>
<dd>The records are fixed-length, not byte delimited. The structure element <i>reclen</i> specifies the length of the record, and the structure element <i>bval</i> is used as the pad character. Any records, inserted into the database, that are less than <i>reclen</i> bytes long are automatically padded.</p>
<dt><code>R_NOKEY</code></p>
<dd>In the interface specified by <code><a href="/docs/linux/man/3-dbopen/">dbopen</a></code>(3), the sequential record retrieval fills in both the caller&#8217;s key and data structures. If the <code>R_NOKEY</code> flag is specified, the <i>cursor</i> routines are not required to fill in the key structure. This permits applications to retrieve records at the end of files without reading all of the intervening records.</p>
<dt><code>R_SNAPSHOT</code></p>
<dd>This flag requires that a snapshot of the file be taken when <code><a href="/docs/linux/man/3-dbopen/">dbopen</a></code>(3) is called, instead of permitting any unmodified records to be read from the original file.</dl>
</dl>
<dt><i>cachesize</i></p>
<dd>A suggested maximum size, in bytes, of the memory cache. This value is <code>only</code> advisory, and the access method will allocate more memory rather than fail. If <i>cachesize</i> is 0 (no size is specified), a default cache is used.</p>
<dt><i>psize</i></p>
<dd>The recno access method stores the in-memory copies of its records in a btree. This value is the size (in bytes) of the pages used for nodes in that tree. If <i>psize</i> is 0 (no page size is specified), a page size is chosen based on the underlying filesystem I/O block size. See <code><a href="/docs/linux/man/3-btree/">btree</a></code>(3) for more information.</p>
<dt><i>lorder</i></p>
<dd>The byte order for integers in the stored database metadata. The number should represent the order as an integer; for example, big endian order would be the number 4,321. If <i>lorder</i> is 0 (no order is specified), the current host order is used.</p>
<dt><i>reclen</i></p>
<dd>The length of a fixed-length record.</p>
<dt><i>bval</i></p>
<dd>The delimiting byte to be used to mark the end of a record for variable-length records, and the pad character for fixed-length records. If no value is specified, newlines (&quot;
&quot;) are used to mark the end of variable-length records and fixed-length records are padded with spaces.</p>
<dt><i>bfname</i></p>
<dd>The recno access method stores the in-memory copies of its records in a btree. If <i>bfname</i> is non-NULL, it specifies the name of the btree file, as if specified as the filename for a <code><a href="/docs/linux/man/3-dbopen/">dbopen</a></code>(3) of a btree file.</dl>
<p> The data part of the key/data pair used by the <i>recno</i> access method is the same as other access methods. The key is different. The <i>data</i> field of the key should be a pointer to a memory location of type <i>recno_t</i>, as defined in the <i>&lt;db.h&gt;</i> include file. This type is normally the largest unsigned integral type available to the implementation. The <i>size</i> field of the key should be the size of that type. </p>
<p> Because there can be no metadata associated with the underlying recno access method files, any changes made to the default values (e.g., fixed record length or byte separator value) must be explicitly specified each time the file is opened. </p>
<p> In the interface specified by <code><a href="/docs/linux/man/3-dbopen/">dbopen</a></code>(3), using the <i>put</i> interface to create a new record will cause the creation of multiple, empty records if the record number is more than one greater than the largest record currently in the database.</p>
<h2>Errors</h2>
<p>The <i>recno</i> access method routines may fail and set <i>errno</i> for any of the errors specified for the library routine <code><a href="/docs/linux/man/3-dbopen/">dbopen</a></code>(3) or the following:</p>
<dl>
<dt><code>EINVAL</code></p>
<dd>An attempt was made to add a record to a fixed-length database that was too large to fit.</dl>
<h2>Bugs</h2>
<p>Only big and little endian byte order is supported.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-btree/">btree</a></code>(3), <code><a href="/docs/linux/man/3-dbopen/">dbopen</a></code>(3), <code><a href="/docs/linux/man/3-hash/">hash</a></code>(3), <code><a href="/docs/linux/man/3-mpool/">mpool</a></code>(3) </p>
<p> <i>Document Processing in a Relational Database System</i>, Michael Stonebraker, Heidi Stettner, Joseph Kalash, Antonin Guttman, Nadene Lynn, Memorandum No. UCB/ERL M82/32, May 1982.</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
