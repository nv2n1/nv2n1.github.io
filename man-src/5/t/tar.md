---
title: "tar(5)"
name: "tar"
section: "5"
letter: "t"
url: "/docs/linux/man/5-tar/"
description: "tar – format of tape archive files"
---

<p><code>tar</code> &#8211; format of tape archive files</p>
<h2>Description</h2>
<p>The archive format collects any number of files, directories, and other file system objects (symbolic links, device nodes, etc.) into a single stream of bytes. The format was originally designed to be used with tape drives that operate with fixed-size blocks, but is widely used as a general packaging mechanism.</p>
<h3>General Format</h3>
<p>A archive consists of a series of 512-byte records. Each file system object requires a header record which stores basic metadata (pathname, owner, permissions, etc.) and zero or more records containing any file data. The end of the archive is indicated by two records consisting entirely of zero bytes. For compatibility with tape drives that use fixed block sizes, programs that read or write tar files always read or write a fixed number of records with each I/O operation. These &#8220;blocks&#8221; are always a multiple of the record size. The maximum block size supported by early implementations was 10240 bytes or 20 records. This is still the default for most implementations although block sizes of 1MiB (2048 records) or larger are commonly used with modern high-speed tape drives. (Note: the terms &#8220;block&#8221; and &#8220;record&#8221; here are not entirely standard; this document follows the convention established by John Gilmore in documenting <code>pdtar .</code></p>
<h3>Old-Style Archive Format</h3>
<p>The original tar archive format has been extended many times to include additional information that various implementors found necessary. This section describes the variant implemented by the tar command included in AT&amp;T System v7 , which seems to be the earliest widely-used version of the tar program. The header record for an old-style archive consists of the following: </p>
<blockquote>
<pre>struct header_old_tar {
 char name[100];
 char mode[8];
 char uid[8];
 char gid[8];
 char size[12];
 char mtime[12];
 char checksum[8];
 char linkflag[1];
 char linkname[100];
 char pad[255];
};</pre>
</blockquote>
<p> All unused bytes in the header record are filled with nulls.</p>
<dl>
<dt><i>name</i></p>
<dd>Pathname, stored as a null-terminated string. Early tar implementations only stored regular files (including hardlinks to those files). One common early convention used a trailing &quot;/&quot; character to indicate a directory name, allowing directory permissions and owner information to be archived and restored.</p>
<dt><i>mode</i></p>
<dd>File mode, stored as an octal number in ASCII.</p>
<dt><i>uid , gid</i></p>
<dd>User id and group id of owner, as octal numbers in ASCII.</p>
<dt><i>size</i></p>
<dd>Size of file, as octal number in ASCII. For regular files only, this indicates the amount of data that follows the header. In particular, this field was ignored by early tar implementations when extracting hardlinks. Modern writers should always store a zero length for hardlink entries.</p>
<dt><i>mtime</i></p>
<dd>Modification time of file, as an octal number in ASCII. This indicates the number of seconds since the start of the epoch, 00:00:00 UTC January 1, 1970. Note that negative values should be avoided here, as they are handled inconsistently.</p>
<dt><i>checksum</i></p>
<dd>Header checksum, stored as an octal number in ASCII. To compute the checksum, set the checksum field to all spaces, then sum all bytes in the header using unsigned arithmetic. This field should be stored as six octal digits followed by a null and a space character. Note that many early implementations of tar used signed arithmetic for the checksum field, which can cause interoperability problems when transferring archives between systems. Modern robust readers compute the checksum both ways and accept the header if either computation matches.</p>
<dt><i>linkflag , linkname</i></p>
<dd>In order to preserve hardlinks and conserve tape, a file with multiple links is only written to the archive the first time it is encountered. The next time it is encountered, the <i>linkflag</i> is set to an ASCII `1&#8242; and the <i>linkname</i> field holds the first name under which this file appears. (Note that regular files have a null value in the <i>linkflag</i> field.)</dl>
<p> Early tar implementations varied in how they terminated these fields. The tar command in AT&amp;T System v7 used the following conventions (this is also documented in early BSD manpages): the pathname must be null-terminated; the mode, uid, and gid fields must end in a space and a null byte; the size and mtime fields must end in a space; the checksum is terminated by a null and a space. Early implementations filled the numeric fields with leading spaces. This seems to have been common practice until the St -p1003.1-88 standard was released. For best portability, modern implementations should fill the numeric fields with leading zeros.</p>
<h3>Pre-POSIX Archives</h3>
<p>An early draft of St -p1003.1-88 served as the basis for John Gilmore&#8217;s <code>pdtar</code> program and many system implementations from the late 1980s and early 1990s. These archives generally follow the POSIX ustar format described below with the following variations: </p>
<ul>
<li> The magic value consists of the five characters &#8220;ustar&#8221; followed by a space. The version field contains a space character followed by a null.
<li> The numeric fields are generally filled with leading spaces (not leading zeros as recommended in the final standard).
<li> The prefix field is often not used, limiting pathnames to the 100 characters of old-style archives. </ul>
<h3>POSIX ustar Archives</h3>
<p>St -p1003.1-88 defined a standard tar file format to be read and written by compliant implementations of <a href="/docs/linux/man/1-tar/">tar</a>(1). This format is often called the &#8220;ustar&#8221; format, after the magic value used in the header. (The name is an acronym for &#8220;Unix Standard TAR .&#8221; It extends the historic format with new fields: </p>
<blockquote>
<pre>struct header_posix_ustar {
 char name[100];
 char mode[8];
 char uid[8];
 char gid[8];
 char size[12];
 char mtime[12];
 char checksum[8];
 char typeflag[1];
 char linkname[100];
 char magic[6];
 char version[2];
 char uname[32];
 char gname[32];
 char devmajor[8];
 char devminor[8];
 char prefix[155];
 char pad[12];
};</pre>
</blockquote>
<dl>
<dt><i>typeflag</i></p>
<dd>Type of entry. POSIX extended the earlier <i>linkflag</i> field with several new type values:</p>
<dl>
<dt><code>&#8220;0&#8221; </code></p>
<dd>Regular file. NUL should be treated as a synonym, for compatibility purposes.</p>
<dt><code>&#8220;1&#8221; </code></p>
<dd>Hard link.</p>
<dt><code>&#8220;2&#8221; </code></p>
<dd>Symbolic link.</p>
<dt><code>&#8220;3&#8221; </code></p>
<dd>Character device node.</p>
<dt><code>&#8220;4&#8221; </code></p>
<dd>Block device node.</p>
<dt><code>&#8220;5&#8221; </code></p>
<dd>Directory.</p>
<dt><code>&#8220;6&#8221; </code></p>
<dd>FIFO node.</p>
<dt><code>&#8220;7&#8221; </code></p>
<dd>Reserved.</p>
<dt><code>Other</code></p>
<dd>A POSIX-compliant implementation must treat any unrecognized typeflag value as a regular file. In particular, writers should ensure that all entries have a valid filename so that they can be restored by readers that do not support the corresponding extension. Uppercase letters &quot;A&quot; through &quot;Z&quot; are reserved for custom extensions. Note that sockets and whiteout entries are not archivable.</dl>
<p> It is worth noting that the <i>size</i> field, in particular, has different meanings depending on the type. For regular files, of course, it indicates the amount of data following the header. For directories, it may be used to indicate the total size of all files in the directory, for use by operating systems that pre-allocate directory space. For all other types, it should be set to zero by writers and ignored by readers.</p>
<dt><i>magic</i></p>
<dd>Contains the magic value &#8220;ustar&#8221; followed by a NUL byte to indicate that this is a POSIX standard archive. Full compliance requires the uname and gname fields be properly set.</p>
<dt><i>version</i></p>
<dd>Version. This should be &#8220;00&#8221; (two copies of the ASCII digit zero) for POSIX standard archives.</p>
<dt><i>uname , gname</i></p>
<dd>User and group names, as null-terminated ASCII strings. These should be used in preference to the uid/gid values when they are set and the corresponding names exist on the system.</p>
<dt><i>devmajor , devminor</i></p>
<dd>Major and minor numbers for character device or block device entry.</p>
<dt><i>name , prefix</i></p>
<dd>If the pathname is too long to fit in the 100 bytes provided by the standard format, it can be split at any / character with the first portion going into the prefix field. If the prefix field is not empty, the reader will prepend the prefix value and a / character to the regular name field to obtain the full pathname. The standard does not require a trailing / character on directory names, though most implementations still include this for compatibility reasons.</dl>
<p> Note that all unused bytes must be set to <code>NUL</code> Field termination is specified slightly differently by POSIX than by previous implementations. The <i>magic</i> <i>uname</i> and <i>gname</i> fields must have a trailing <code>NUL</code> The <i>pathname</i> <i>linkname</i> and <i>prefix</i> fields must have a trailing <code>NUL</code> unless they fill the entire field. (In particular, it is possible to store a 256-character pathname if it happens to have a / as the 156th character.) POSIX requires numeric fields to be zero-padded in the front, and requires them to be terminated with either space or <code>NUL</code> characters. Currently, most tar implementations comply with the ustar format, occasionally extending it by adding new fields to the blank area at the end of the header record.</p>
<h3>Numeric Extensions</h3>
<p>There have been several attempts to extend the range of sizes or times supported by modifying how numbers are stored in the header. One obvious extension to increase the size of files is to eliminate the terminating characters from the various numeric fields. For example, the standard only allows the size field to contain 11 octal digits, reserving the twelfth byte for a trailing NUL character. Allowing 12 octal digits allows file sizes up to 64 GB. Another extension, utilized by GNU tar, star, and other newer implementations, permits binary numbers in the standard numeric fields. This is flagged by setting the high bit of the first byte. The remainder of the field is treated as a signed twos-complement value. This permits 95-bit values for the length and time fields and 63-bit values for the uid, gid, and device numbers. In particular, this provides a consistent way to handle negative time values. GNU tar supports this extension for the length, mtime, ctime, and atime fields. Joerg Schilling&#8217;s star program and the libarchive library support this extension for all numeric fields. Note that this extension is largely obsoleted by the extended attribute record provided by the pax interchange format. Another early GNU extension allowed base-64 values rather than octal. This extension was short-lived and is no longer supported by any implementation.</p>
<h3>Pax Interchange Format</h3>
<p>There are many attributes that cannot be portably stored in a POSIX ustar archive. St -p1003.1-2001 defined a &#8220;pax interchange format&#8221; that uses two new types of entries to hold text-formatted metadata that applies to following entries. Note that a pax interchange format archive is a ustar archive in every respect. The new data is stored in ustar-compatible archive entries that use the &#8220;x&#8221; or &#8220;g&#8221; typeflag. In particular, older implementations that do not fully support these extensions will extract the metadata into regular files, where the metadata can be examined as necessary. An entry in a pax interchange format archive consists of one or two standard ustar entries, each with its own header and data. The first optional entry stores the extended attributes for the following entry. This optional first entry has an &quot;x&quot; typeflag and a size field that indicates the total size of the extended attributes. The extended attributes themselves are stored as a series of text-format lines encoded in the portable UTF-8 encoding. Each line consists of a decimal number, a space, a key string, an equals sign, a value string, and a new line. The decimal number indicates the length of the entire line, including the initial length field and the trailing newline. An example of such a field is: </p>
<blockquote><p><tt>25 ctime=1084839148.1212
</tt></p></blockquote>
<p> Keys in all lowercase are standard keys. Vendors can add their own keys by prefixing them with an all uppercase vendor name and a period. Note that, unlike the historic header, numeric values are stored using decimal, not octal. A description of some common keys follows:</p>
<dl>
<dt><code>atime , ctime , mtime</code></p>
<dd>File access, inode change, and modification times. These fields can be negative or include a decimal point and a fractional value.</p>
<dt><code>hdrcharset</code></p>
<dd>The character set used by the pax extension values. By default, all textual values in the pax extended attributes are assumed to be in UTF-8, including pathnames, user names, and group names. In some cases, it is not possible to translate local conventions into UTF-8. If this key is present and the value is the six-character ASCII string &#8220;BINARY&#8221; then all textual values are assumed to be in a platform-dependent multi-byte encoding. Note that there are only two valid values for this key: &#8220;BINARY&#8221; or &#8220;ISO-IR 10646 2000 UTF-8&#8221; No other values are permitted by the standard, and the latter value should generally not be used as it is the default when this key is not specified. In particular, this flag should not be used as a general mechanism to allow filenames to be stored in arbitrary encodings.</p>
<dt><code>uname , uid , gname , gid</code></p>
<dd>User name, group name, and numeric UID and GID values. The user name and group name stored here are encoded in UTF8 and can thus include non-ASCII characters. The UID and GID fields can be of arbitrary length.</p>
<dt><code>linkpath</code></p>
<dd>The full path of the linked-to file. Note that this is encoded in UTF8 and can thus include non-ASCII characters.</p>
<dt><code>path</code></p>
<dd>The full pathname of the entry. Note that this is encoded in UTF8 and can thus include non-ASCII characters.</p>
<dt><code>realtime.* , security.*</code></p>
<dd>These keys are reserved and may be used for future standardization.</p>
<dt><code>size</code></p>
<dd>The size of the file. Note that there is no length limit on this field, allowing conforming archives to store files much larger than the historic 8GB limit.</p>
<dt><code>SCHILY.*</code></p>
<dd>Vendor-specific attributes used by Joerg Schilling&#8217;s <code>star</code> implementation.</p>
<dt><code>SCHILY.acl.access , SCHILY.acl.default</code></p>
<dd>Stores the access and default ACLs as textual strings in a format that is an extension of the format specified by POSIX.1e draft 17. In particular, each user or group access specification can include a fourth colon-separated field with the numeric UID or GID. This allows ACLs to be restored on systems that may not have complete user or group information available (such as when NIS/YP or LDAP services are temporarily unavailable).</p>
<dt><code>SCHILY.devminor , SCHILY.devmajor</code></p>
<dd>The full minor and major numbers for device nodes.</p>
<dt><code>SCHILY.fflags</code></p>
<dd>The file flags.</p>
<dt><code>SCHILY.realsize</code></p>
<dd>The full size of the file on disk. XXX explain? XXX</p>
<dt><code>SCHILY.dev, SCHILY.ino , SCHILY.nlinks</code></p>
<dd>The device number, inode number, and link count for the entry. In particular, note that a pax interchange format archive using Joerg Schilling&#8217;s <code>SCHILY.*</code> extensions can store all of the data from <i>struct stat</i></p>
<dt><code>LIBARCHIVE.*</code></p>
<dd>Vendor-specific attributes used by the <code>libarchive</code> library and programs that use it.</p>
<dt><code>LIBARCHIVE.creationtime</code></p>
<dd>The time when the file was created. (This should not be confused with the POSIX &#8220;ctime&#8221; attribute, which refers to the time when the file metadata was last changed.)</p>
<dt><code>LIBARCHIVE.xattr. </code><i>namespace </i><code>. </code><i>key</i></p>
<dd>Libarchive stores POSIX.1e-style extended attributes using keys of this form. The <i>key</i> value is URL-encoded: All non-ASCII characters and the two special characters &#8220;=&#8221; and &#8220;%&#8221; are encoded as &#8220;%&#8221; followed by two uppercase hexadecimal digits. The value of this key is the extended attribute value encoded in base 64. XXX Detail the base-64 format here XXX</p>
<dt><code>VENDOR.*</code></p>
<dd>XXX document other vendor-specific extensions XXX</dl>
<p> Any values stored in an extended attribute override the corresponding values in the regular tar header. Note that compliant readers should ignore the regular fields when they are overridden. This is important, as existing archivers are known to store non-compliant values in the standard header fields in this situation. There are no limits on length for any of these fields. In particular, numeric fields can be arbitrarily large. All text fields are encoded in UTF8. Compliant writers should store only portable 7-bit ASCII characters in the standard ustar header and use extended attributes whenever a text value contains non-ASCII characters. In addition to the <code>x</code> entry described above, the pax interchange format also supports a <code>g</code> entry. The <code>g</code> entry is identical in format, but specifies attributes that serve as defaults for all subsequent archive entries. The <code>g</code> entry is not widely used. Besides the new <code>x</code> and <code>g</code> entries, the pax interchange format has a few other minor variations from the earlier ustar format. The most troubling one is that hardlinks are permitted to have data following them. This allows readers to restore any hardlink to a file without having to rewind the archive to find an earlier entry. However, it creates complications for robust readers, as it is no longer clear whether or not they should ignore the size field for hardlink entries.</p>
<h3>GNU Tar Archives</h3>
<p>The GNU tar program started with a pre-POSIX format similar to that described earlier and has extended it using several different mechanisms: It added new fields to the empty space in the header (some of which was later used by POSIX for conflicting purposes); it allowed the header to be continued over multiple records; and it defined new entries that modify following entries (similar in principle to the <code>x</code> entry described above, but each GNU special entry is single-purpose, unlike the general-purpose <code>x</code> entry). As a result, GNU tar archives are not POSIX compatible, although more lenient POSIX-compliant readers can successfully extract most GNU tar archives. </p>
<blockquote>
<pre>struct header_gnu_tar {
 char name[100];
 char mode[8];
 char uid[8];
 char gid[8];
 char size[12];
 char mtime[12];
 char checksum[8];
 char typeflag[1];
 char linkname[100];
 char magic[6];
 char version[2];
 char uname[32];
 char gname[32];
 char devmajor[8];
 char devminor[8];
 char atime[12];
 char ctime[12];
 char offset[12];
 char longnames[4];
 char unused[1];
 struct {
 char offset[12];
 char numbytes[12];
 } sparse[4];
 char isextended[1];
 char realsize[12];
 char pad[17];
};</pre>
</blockquote>
<dl>
<dt><i>typeflag</i></p>
<dd>GNU tar uses the following special entry types, in addition to those defined by POSIX:</p>
<dl>
<dt><code>&quot;7&quot;</code></p>
<dd>GNU tar treats type &quot;7&quot; records identically to type &quot;0&quot; records, except on one obscure RTOS where they are used to indicate the pre-allocation of a contiguous file on disk.</p>
<dt><code>&quot;D&quot;</code></p>
<dd>This indicates a directory entry. Unlike the POSIX-standard &quot;5&quot; typeflag, the header is followed by data records listing the names of files in this directory. Each name is preceded by an ASCII &quot;Y&quot; if the file is stored in this archive or &quot;N&quot; if the file is not stored in this archive. Each name is terminated with a null, and an extra null marks the end of the name list. The purpose of this entry is to support incremental backups; a program restoring from such an archive may wish to delete files on disk that did not exist in the directory when the archive was made. Note that the &quot;D&quot; typeflag specifically violates POSIX, which requires that unrecognized typeflags be restored as normal files. In this case, restoring the &quot;D&quot; entry as a file could interfere with subsequent creation of the like-named directory.</p>
<dt><code>&quot;K&quot;</code></p>
<dd>The data for this entry is a long linkname for the following regular entry.</p>
<dt><code>&quot;L&quot;</code></p>
<dd>The data for this entry is a long pathname for the following regular entry.</p>
<dt><code>&quot;M&quot;</code></p>
<dd>This is a continuation of the last file on the previous volume. GNU multi-volume archives guarantee that each volume begins with a valid entry header. To ensure this, a file may be split, with part stored at the end of one volume, and part stored at the beginning of the next volume. The &quot;M&quot; typeflag indicates that this entry continues an existing file. Such entries can only occur as the first or second entry in an archive (the latter only if the first entry is a volume label). The <i>size</i> field specifies the size of this entry. The <i>offset</i> field at bytes 369-380 specifies the offset where this file fragment begins. The <i>realsize</i> field specifies the total size of the file (which must equal <i>size</i> plus <i>offset )</i> When extracting, GNU tar checks that the header file name is the one it is expecting, that the header offset is in the correct sequence, and that the sum of offset and size is equal to realsize.</p>
<dt><code>&quot;N&quot;</code></p>
<dd>Type &quot;N&quot; records are no longer generated by GNU tar. They contained a list of files to be renamed or symlinked after extraction; this was originally used to support long names. The contents of this record are a text description of the operations to be done, in the form &#8220;Rename %s to %s
&#8221; or &#8220;Symlink %s to %s
&#8221; in either case, both filenames are escaped using K&amp;R C syntax. Due to security concerns, &quot;N&quot; records are now generally ignored when reading archives.</p>
<dt><code>&quot;S&quot;</code></p>
<dd>This is a &#8220;sparse&#8221; regular file. Sparse files are stored as a series of fragments. The header contains a list of fragment offset/length pairs. If more than four such entries are required, the header is extended as necessary with &#8220;extra&#8221; header extensions (an older format that is no longer used), or &#8220;sparse&#8221; extensions.</p>
<dt><code>&quot;V&quot;</code></p>
<dd>The <i>name</i> field should be interpreted as a tape/volume header name. This entry should generally be ignored on extraction.</dl>
<dt><i>magic</i></p>
<dd>The magic field holds the five characters &#8220;ustar&#8221; followed by a space. Note that POSIX ustar archives have a trailing null.</p>
<dt><i>version</i></p>
<dd>The version field holds a space character followed by a null. Note that POSIX ustar archives use two copies of the ASCII digit &#8220;0&#8221;</p>
<dt><i>atime , ctime</i></p>
<dd>The time the file was last accessed and the time of last change of file information, stored in octal as with <i>mtime</i></p>
<dt><i>longnames</i></p>
<dd>This field is apparently no longer used.</p>
<dt><code>Sparse </code><i>offset / numbytes</i></p>
<dd>Each such structure specifies a single fragment of a sparse file. The two fields store values as octal numbers. The fragments are each padded to a multiple of 512 bytes in the archive. On extraction, the list of fragments is collected from the header (including any extension headers), and the data is then read and written to the file at appropriate offsets.</p>
<dt><i>isextended</i></p>
<dd>If this is set to non-zero, the header will be followed by additional &#8220;sparse header&#8221; records. Each such record contains information about as many as 21 additional sparse blocks as shown here: </p>
<blockquote>
<pre>struct gnu_sparse_header {
 struct {
 char offset[12];
 char numbytes[12];
 } sparse[21];
 char isextended[1];
 char padding[7];
};</pre>
</blockquote>
<dt><i>realsize</i></p>
<dd>A binary representation of the file&#8217;s complete size, with a much larger range than the POSIX file size. In particular, with <code>M</code> type files, the current entry is only a portion of the file. In that case, the POSIX size field will indicate the size of this entry; the <i>realsize</i> field will indicate the total size of the file.</dl>
<h3>GNU tar pax archives</h3>
<p>GNU tar 1.14 (XXX check this XXX) and later will write pax interchange format archives when you specify the &#8211;<code>-posix</code> flag. This format follows the pax interchange format closely, using some <code>SCHILY</code> tags and introducing new keywords to store sparse file information. There have been three iterations of the sparse file support, referred to as &#8220;0.0&#8221; &#8220;0.1&#8221; and &#8220;1.0&#8221;</p>
<dl>
<dt><code>GNU.sparse.numblocks , GNU.sparse.offset , GNU.sparse.numbytes , GNU.sparse.size</code></p>
<dd>The &#8220;0.0&#8221; format used an initial <code>GNU.sparse.numblocks</code> attribute to indicate the number of blocks in the file, a pair of <code>GNU.sparse.offset</code> and <code>GNU.sparse.numbytes</code> to indicate the offset and size of each block, and a single <code>GNU.sparse.size</code> to indicate the full size of the file. This is not the same as the size in the tar header because the latter value does not include the size of any holes. This format required that the order of attributes be preserved and relied on readers accepting multiple appearances of the same attribute names, which is not officially permitted by the standards.</p>
<dt><code>GNU.sparse.map</code></p>
<dd>The &#8220;0.1&#8221; format used a single attribute that stored a comma-separated list of decimal numbers. Each pair of numbers indicated the offset and size, respectively, of a block of data. This does not work well if the archive is extracted by an archiver that does not recognize this extension, since many pax implementations simply discard unrecognized attributes.</p>
<dt><code>GNU.sparse.major , GNU.sparse.minor , GNU.sparse.name , GNU.sparse.realsize</code></p>
<dd>The &#8220;1.0&#8221; format stores the sparse block map in one or more 512-byte blocks prepended to the file data in the entry body. The pax attributes indicate the existence of this map (via the <code>GNU.sparse.major</code> and <code>GNU.sparse.minor</code> fields) and the full size of the file. The <code>GNU.sparse.name</code> holds the true name of the file. To avoid confusion, the name stored in the regular tar header is a modified name so that extraction errors will be apparent to users.</dl>
<h3>Solaris Tar</h3>
<p>XXX More Details Needed XXX Solaris tar (beginning with SunOS XXX 5.7 ?? XXX) supports an &#8220;extended&#8221; format that is fundamentally similar to pax interchange format, with the following differences: </p>
<ul>
<li> Extended attributes are stored in an entry whose type is <code>X</code> not <code>x</code> as used by pax interchange format. The detailed format of this entry appears to be the same as detailed above for the <code>x</code> entry.
<li> An additional <code>A</code> header is used to store an ACL for the following regular entry. The body of this entry contains a seven-digit octal number followed by a zero byte, followed by the textual ACL description. The octal value is the number of ACL entries plus a constant that indicates the ACL type: 01000000 for POSIX.1e ACLs and 03000000 for NFSv4 ACLs. </ul>
<h3>AIX Tar</h3>
<p>XXX More details needed XXX AIX Tar uses a ustar-formatted header with the type <code>A</code> for storing coded ACL information. Unlike the Solaris format, AIX tar writes this header after the regular file body to which it applies. The pathname in this header is either <code>NFS4</code> or <code>AIXC</code> to indicate the type of ACL stored. The actual ACL is stored in platform-specific binary format.</p>
<h3>Mac OS X Tar</h3>
<p>The tar distributed with Apple&#8217;s Mac OS X stores most regular files as two separate files in the tar archive. The two files have the same name except that the first one has &#8220;._&#8221; prepended to the last path element. This special file stores an AppleDouble-encoded binary blob with additional metadata about the second file, including ACL, extended attributes, and resources. To recreate the original file on disk, each separate file can be extracted and the Mac OS X Fn copyfile function can be used to unpack the separate metadata file and apply it to th regular file. Conversely, the same function provides a &#8220;pack&#8221; option to encode the extended metadata from a file into a separate file whose contents can then be put into a tar archive. Note that the Apple extended attributes interact badly with long filenames. Since each file is stored with the full name, a separate set of extensions needs to be included in the archive for each one, doubling the overhead required for files with long names.</p>
<h3>Summary of tar type codes</h3>
<p>The following list is a condensed summary of the type codes used in tar header records generated by different tar implementations. More details about specific implementations can be found above:</p>
<dl>
<dt><code>NUL</code></p>
<dd>Early tar programs stored a zero byte for regular files.</p>
<dt><code>0</code></p>
<dd>POSIX standard type code for a regular file.</p>
<dt><code>1</code></p>
<dd>POSIX standard type code for a hard link description.</p>
<dt><code>2</code></p>
<dd>POSIX standard type code for a symbolic link description.</p>
<dt><code>3</code></p>
<dd>POSIX standard type code for a character device node.</p>
<dt><code>4</code></p>
<dd>POSIX standard type code for a block device node.</p>
<dt><code>5</code></p>
<dd>POSIX standard type code for a directory.</p>
<dt><code>6</code></p>
<dd>POSIX standard type code for a FIFO.</p>
<dt><code>7</code></p>
<dd>POSIX reserved.</p>
<dt><code>7</code></p>
<dd>GNU tar used for pre-allocated files on some systems.</p>
<dt><code>A</code></p>
<dd>Solaris tar ACL description stored prior to a regular file header.</p>
<dt><code>A</code></p>
<dd>AIX tar ACL description stored after the file body.</p>
<dt><code>D</code></p>
<dd>GNU tar directory dump.</p>
<dt><code>K</code></p>
<dd>GNU tar long linkname for the following header.</p>
<dt><code>L</code></p>
<dd>GNU tar long pathname for the following header.</p>
<dt><code>M</code></p>
<dd>GNU tar multivolume marker, indicating the file is a continuation of a file from the previous volume.</p>
<dt><code>N</code></p>
<dd>GNU tar long filename support. Deprecated.</p>
<dt><code>S</code></p>
<dd>GNU tar sparse regular file.</p>
<dt><code>V</code></p>
<dd>GNU tar tape/volume header name.</p>
<dt><code>X</code></p>
<dd>Solaris tar general-purpose extension header.</p>
<dt><code>g</code></p>
<dd>POSIX pax interchange format global extensions.</p>
<dt><code>x</code></p>
<dd>POSIX pax interchange format per-file extensions.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-ar/">ar</a>(1), <a href="/docs/linux/man/1-pax/">pax</a>(1), <a href="/docs/linux/man/1-tar/">tar</a>(1)</p>
<h2>Standards</h2>
<p>The <code>tar</code> utility is no longer a part of POSIX or the Single Unix Standard. It last appeared in St -susv2 . It has been supplanted in subsequent standards by <a href="/docs/linux/man/1-pax/">pax</a>(1). The ustar format is currently part of the specification for the <a href="/docs/linux/man/1-pax/">pax</a>(1) utility. The pax interchange file format is new with St -p1003.1-2001 .</p>
<h2>History</h2>
<p>A <code>tar</code> command appeared in Seventh Edition Unix, which was released in January, 1979. It replaced the <code>tp</code> program from Fourth Edition Unix which in turn replaced the <code>tap</code> program from First Edition Unix. John Gilmore&#8217;s <code>pdtar</code> public-domain implementation (circa 1987) was highly influential and formed the basis of <code>GNU tar</code> (circa 1988). Joerg Shilling&#8217;s <code>star</code> archiver is another open-source (GPL) archiver (originally developed circa 1985) which features complete support for pax interchange format. </p>
<p> This documentation was written as part of the <code>libarchive</code> and <code>bsdtar</code> project by An Tim Kientzle Aq kientzle [at] FreeBSD.org .</p>
