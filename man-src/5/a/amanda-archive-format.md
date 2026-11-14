---
title: "amanda-archive-format(5)"
name: "amanda-archive-format"
section: "5"
letter: "a"
url: "/docs/linux/man/5-amanda-archive-format/"
description: "amanda-archive-format – Format of amanda archive streams"
---

<p>amanda-archive-format &#8211; Format of amanda archive streams</p>
<h2>Description</h2>
<p>The Amanda archive format is designed to be a simple, efficient means of interleaving multiple simultaneous files, allowing an arbitrary number of data streams for a file. It is a streaming format in the sense that the writer need not know the size of files until they are completely written to the archive, and the reader can process the archive in constant space.</p>
<h2>Data Model</h2>
<p>The data stored in an archive consists of an unlimited number of files. Each file consists of a number of &quot;attributes&quot;, each identified by a 16-bit ID. Each attribute can contain an unlimited amount of data. </p>
<p> Attribute IDs less than 16 (AMAR_ATTR_APP_START) are reserved for special purposes, but the remaining IDs are available for application-specific uses.</p>
<h2>Structure</h2>
<h3>Records</h3>
<p>A record can be either a header record or a data record. A header record serves as a &quot;checkpoint&quot; in the file, with a magic value that can be used to recognize archive files. </p>
<p> A header record has a fixed size of 28 bytes, as follows: </p>
<pre> 28 bytes: magic string</pre>
<p>The magic string is the ASCII text &quot;AMANDA ARCHIVE FORMAT &quot; followed by a decimal representation of the format version number (currently &#8216;1&#8217;), padded to 28 bytes with NUL bytes. </p>
<p> A data record has a variable size, as follows: </p>
<pre> 2 bytes: file number
 2 bytes: attribute ID
 4 bytes: data size (N)
 N bytes: data</pre>
<p>The file number and attribute ID serve to identify the data stream to which this data belongs. The low 31 bits of the data size give the number of data bytes following, while the high bit (the EOA bit) indicates the end of the attribute, as described below. Because records are generally read into memory in their entirety, the data size must not exceed 4MB (4194304 bytes). All integers are in network byte order. </p>
<p> A header record is distinguished from a data record by the magic string. The file number 0x414d, corresponding to the characters &quot;AM&quot;, is forbidden and must be skipped on writing. </p>
<p> Attribute ID 0 (AMAR_ATTR_FILENAME) gives the filename of a file. This attribute is mandatory for each file, must be nonempty, must fit in a single record, and must precede any other attributes for the same file in the archive. The filename should be a printable string (ASCII or UTF-8), to facilitate use of generic archive-display utilities, but the format permits any nonempty bytestring. The filename cannot span multiple records. </p>
<p> Attribute ID 1 (AMAR_ATTR_EOF) signals the end of a file. This attribute must contain no data, but should have the EOA bit set.</p>
<h3>Connection To Data Model</h3>
<p>Each file in an archive is assigned a file number distinct from any other active file in the archive. The first record for a file must have attribute ID 0 (AMAR_ATTR_FILENAME), indicating a filename. A file ends with an empty record with ID 1 (AMAR_ATTR_EOF). For every file at which a reader might want to begin reading, the filename record should be preceded by a header record. How often to write header records is left to the discretion of the application. </p>
<p> All data records with the same file number and attribute ID are considered a part of the same attribute. The boundaries between such records are not significant to the contents of the attribute, and both readers and writers are free to alter such boundaries as necessary. </p>
<p> The final data record for each attribute has the high bit (the EOA bit) of its data size field set. A writer must not reuse an attribute ID within a file. An attribute may be terminated by a record containing both data and an EOA bit, or by a zero-length record with its EOA bit set.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Author</h2>
<p><code>Dustin J. Mitchell</code> &lt;dustin [at] zmanda.com&gt;</p>
<dl>
<dd>Zmanda, Inc. (<a rel="nofollow" href="http://www.zmanda.com)">http://www.zmanda.com)</a></dl>
