---

title: "star(5)"
name: "star"
section: "5"
letter: "s"
url: "/docs/linux/man/5-star/"
description: "star – tape archive file format"
---

<p> star - tape archive file format  </p>

<p> <code>Tar</code> Archives are layered archives. The basic structure is defined by the POSIX.1-1988 archive format and documented in the <code>BASIC TAR HEADER DESCRIPTION</code> section below. The higher level structure is defined by the POSIX.1-2001 extended headers and documented in the <code>EXTENDED TAR (PAX) HEADER STRUCTURE</code> section below. POSIX.1-2001 extended headers are pseudo files that contain an unlimited number of extended header keywords and associated values. The header keywords are documented in the <code>EXTENDED TAR (PAX) HEADER KEYWORDS</code> section below.  </p>
<h2>BASIC TAR HEADER DESCRIPTION</h2>
<p>Physically, a POSIX.1-1988 <code>tar</code> archive consists of a series of fixed sized blocks of TBLOCK (512) characters. It contains a series of file entries terminated by a logical end-of-archive marker, which consists of two blocks of 512 bytes of binary zeroes. Each file entry is represented by a header block that describes the file followed by one or more blocks with the content of the file. The length of each file is rounded up to a multiple of 512 bytes. </p>
<p>A number of TBLOCK sizes blocks are grouped together to a tape record for physical I/O operations. Each record of <i>n</i> blocks is written with a single <code><a href="/docs/linux/man/2-write/">write</a></code>(2) operation. On magnetic tapes, this results in a single tape record in case the tape drive is in <code>variable length record mode</code>. </p>
<p>The header block is defined in star.h as follows: </p>
<pre><code>/*
 * POSIX.1-1988 field size values and magic.
 */
#define TBLOCK 512
#define NAMSIZ 100
#define PFXSIZ 155
#define TMODLEN 8
#define TUIDLEN 8
#define TGIDLEN 8
#define TSIZLEN 12
#define TMTMLEN 12
#define TCKSLEN 8
#define TMAGIC &quot;ustar&quot; /* ustar magic 6 chars + '\0' */
#define TMAGLEN 6 /* &quot;ustar&quot; including '\0' */
#define TVERSION &quot;00&quot;
#define TVERSLEN 2
#define TUNMLEN 32
#define TGNMLEN 32
#define TDEVLEN 8
/*
 * POSIX.1-1988 typeflag values
 */
#define REGTYPE '0' /* Regular File */
#define AREGTYPE '\0' /* Regular File (outdated) */
#define LNKTYPE '1' /* Hard Link */
#define SYMTYPE '2' /* Symbolic Link */
#define CHRTYPE '3' /* Character Special */
#define BLKTYPE '4' /* Block Special */
#define DIRTYPE '5' /* Directory */
#define FIFOTYPE '6' /* FIFO (named pipe) */
#define CONTTYPE '7' /* Contiguous File */
/*
 * POSIX.1-2001 typeflag extensions.
 * POSIX.1-2001 calls the extended USTAR format PAX although it is
 * definitely derived from and based on USTAR. The reason may be that
 * POSIX.1-2001 calls the tar program outdated and lists the
 * pax program as the successor.
 */
#define LF_GHDR 'g' /* POSIX.1-2001 global extended header */
#define LF_XHDR 'x' /* POSIX.1-2001 extended header */
</code></pre>
<p>See section <code>EXTENDED TAR (PAX) HEADER KEYWORDS</code> for more information about the structure of a POSIX.1-2001 header. </p>
<pre><code>/*
 * star/gnu/Sun tar extensions:
 *
 * Note that the standards committee allows only capital A through
 * capital Z for user-defined expansion. This means that defining
 * something as, say '8' is a *bad* idea.
 */
#define LF_ACL 'A' /* Solaris Access Control List */
#define LF_DUMPDIR 'D' /* GNU dump dir */
#define LF_EXTATTR 'E' /* Solaris Extended Attribute File */
#define LF_META 'I' /* Inode (metadata only) no file content */
#define LF_LONGLINK 'K' /* NEXT file has a long linkname */
#define LF_LONGNAME 'L' /* NEXT file has a long name */
#define LF_MULTIVOL 'M' /* Continuation file rest to be skipped */
#define LF_NAMES 'N' /* OLD GNU for names &gt; 100 characters */
#define LF_SPARSE 'S' /* This is for sparse files */
#define LF_VOLHDR 'V' /* tape/volume header Ignore on extraction */
#define LF_VU_XHDR 'X' /* POSIX.1-2001 xtended (Sun VU version) */
/*
 * Definitions for the t_mode field
 */
#define TSUID 04000 /* Set UID on execution */
#define TSGID 02000 /* Set GID on execution */
#define TSVTX 01000 /* On directories, restricted deletion flag */
#define TUREAD 00400 /* Read by owner */
#define TUWRITE 00200 /* Write by owner special */
#define TUEXEC 00100 /* Execute/search by owner */
#define TGREAD 00040 /* Read by group */
#define TGWRITE 00020 /* Write by group */
#define TGEXEC 00010 /* Execute/search by group */
#define TOREAD 00004 /* Read by other */
#define TOWRITE 00002 /* Write by other */
#define TOEXEC 00001 /* Execute/search by other */
#define TALLMODES 07777 /* The low 12 bits */
/*
 * This is the ustar (Posix 1003.1) header.
 */
struct header {
        char t_name[NAMSIZ]; /* 0 Filename */
        char t_mode[8]; /* 100 Permissions */
        char t_uid[8]; /* 108 Numerical User ID */
        char t_gid[8]; /* 116 Numerical Group ID */
        char t_size[12]; /* 124 Filesize */
        char t_mtime[12]; /* 136 st_mtime */
        char t_chksum[8]; /* 148 Checksum */
        char t_typeflag; /* 156 Typ of File */
        char t_linkname[NAMSIZ]; /* 157 Target of Links */
        char t_magic[TMAGLEN]; /* 257 &quot;ustar&quot; */
        char t_version[TVERSLEN]; /* 263 Version fixed to 00 */
        char t_uname[TUNMLEN]; /* 265 User Name */
        char t_gname[TGNMLEN]; /* 297 Group Name */
        char t_devmajor[8]; /* 329 Major for devices */
        char t_devminor[8]; /* 337 Minor for devices */
        char t_prefix[PFXSIZ]; /* 345 Prefix for t_name */
                                        /* 500 End */
        char t_mfill[12]; /* 500 Filler up to 512 */
};
/*
 * star header specific definitions
 */
#define STMAGIC &quot;tar&quot; /* star magic */
#define STMAGLEN 4 /* &quot;tar&quot; including '\0' */
/*
 * This is the new (post Posix 1003.1-1988) xstar header
 * defined in 1994.
 *
 * t_prefix[130] is guaranteed to be '&nbsp;<wbr>' to prevent ustar
 * compliant implementations from failing.
 * t_mfill &amp; t_xmagic need to be zero for a 100% ustar compliant
 * implementation, so setting t_xmagic to
 * &quot;tar&quot; should be avoided in the future.
 *
 * A different method to recognize this format is to verify that
 * t_prefix[130] is equal to '&nbsp;<wbr>' and
 * t_atime[0]/t_ctime[0] is an octal number and
 * t_atime[11] is equal to ' ' and
 * t_ctime[11] is equal to ' '.
 *
 * Note that t_atime[11]/t_ctime[11] may be changed in future.
 */
struct xstar_header {
        char t_name[NAMSIZ]; /* 0 Filename */
        char t_mode[8]; /* 100 Permissions */
        char t_uid[8]; /* 108 Numerical User ID */
        char t_gid[8]; /* 116 Numerical Group ID */
        char t_size[12]; /* 124 Filesize */
        char t_mtime[12]; /* 136 st_mtime */
        char t_chksum[8]; /* 148 Checksum */
        char t_typeflag; /* 156 Typ of File */
        char t_linkname[NAMSIZ]; /* 157 Target of Links */
        char t_magic[TMAGLEN]; /* 257 &quot;ustar&quot; */
        char t_version[TVERSLEN]; /* 263 Version fixed to 00 */
        char t_uname[TUNMLEN]; /* 265 User Name */
        char t_gname[TGNMLEN]; /* 297 Group Name */
        char t_devmajor[8]; /* 329 Major for devices */
        char t_devminor[8]; /* 337 Minor for devices */
        char t_prefix[131]; /* 345 Prefix for t_name */
        char t_atime[12]; /* 476 st_atime */
        char t_ctime[12]; /* 488 st_ctime */
        char t_mfill[8]; /* 500 Filler up to star magic */
        char t_xmagic[4]; /* 508 &quot;tar&quot; */
};
struct sparse {
        char t_offset[12];
        char t_numbytes[12];
};
#define SPARSE_EXT_HDR 21
struct xstar_ext_header {
        struct sparse t_sp[21];
        char t_isextended;
};
typedef union hblock {
        char dummy[TBLOCK];
        long ldummy[TBLOCK/sizeof (long)]; /* force long alignment */
        struct header dbuf;
        struct xstar_header xstar_dbuf;
        struct xstar_ext_header xstar_ext_dbuf;
} TCB;
</code></pre>
<p>For maximum portability, all fields that contain character strings should be limited to use the low 7 bits of a character. </p>
<p>The <i>name</i>, <i>linkname</i> and <i>prefix</i> field contain character strings. The strings are null terminated except when they use the full space of 100 characters for the <i>name</i> or <i>linkname</i> field or 155 characters for the <i>prefix</i> field. </p>
<p>If the <i>prefix</i> does not start with a null character, then <i>prefix</i> and <i>name</i> need to be concatenated by using the <i>prefix</i>, followed by a slash character followed by the <i>name</i> field. If a null character appears in <i>name</i> or <i>prefix</i> before the maximum size is reached, the field in question is terminated. This way file names up to 256 characters may be archived. The <i>prefix</i> is not used together with the <i>linkname</i> field, so the maximum length of a link name is 100 characters. </p>
<p>The fields <i>magic</i>, <i>uname</i> and <i>gname</i> contain null terminated character strings. </p>
<p>The version field contains the string <code>&quot;00&quot;</code> without a trailing zero. It cannot be set to different values as POSIX.1-1988 did not specify a way to handle different version strings. </p>
<p>The <i>typeflag</i> field contains a single character. </p>
<p>All numeric fields contain <i>size-1</i> leading zero-filled numbers using octal digits. They are followed by one or more space or null characters. All recent implementations only use one space or null character at the end of a numerical field to get maximum space for the octal number. <code>Star</code> always uses a space character as terminator. Numeric fields with 8 characters may hold up to 7 octal digits (7777777) which results is a maximum value of 2097151. Numeric fields with 12 characters may hold up to 11 octal digits (77777777777) which results is a maximum value of 8589934591. </p>
<p> <i>Star</i> implements a vendor specific (and thus non-POSIX) extension to put bigger numbers into the numeric fields. This is done by using a <code>base 256</code> coding. The top bit of the first character in the appropriate 8 character or 12 character field is set to flag non octal coding. If base 256 coding is in use, then all remaining characters are used to code the number. This results in 7 base 256 digits in 8 character fields and in 11 base 256 digits in 12 character fields. All base 256 numbers are two&#8217;s complement numbers. A base 256 number in a 8 character field may hold 56 bits, a base 256 number in a 12 character field may hold 88 bits. This may be extended to 63 bits for 8 character fields and to 95 bits for 12 character fields. For a negative number the first character currently is set to a value of 255 (all 8 bits are set). The rightmost character in a 8 or 12 character field contains the least significant base 256 number. Recent GNU tar versions implement the same extension. </p>
<p>While the POSIX standard makes it obvious that the fields <i>mode</i>,<i> uid</i>,<i> gid</i>, <i> size,</i> chksum <i>,</i> <i>devmajor</i> and <i>devminor</i> should be treated as unsigned numbers, there is no such definition for the <i>time</i> field. </p>
<p>The mode field contains 12 bits holding permissions, see above for the definitions for each of the permission bits. </p>
<p>The <i>uid</i> and <i>gid</i> fields contain the numerical user id of the file. </p>
<p>The <i>size</i> field contains the size of the file in characters. If the <i>tar header</i> is followed by file data, then the amount of data that follows is computed by <i>(size + 511) / 512</i>. </p>
<p>The <i>mtime</i> field contains the number of seconds since Jan 1st 1970 00:00 UTC as retrived via <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) in <i>st_mtime</i>. If the <i>mtime</i> fiels is assumed to be a signed 33 bit number, the latest representable time is 2106 Feb 7 06:28:15 GMT. </p>
<p>The <i>chksum</i> field contains a simple checksum over all bytes of the header. To compute the value, all characters in the header are treated as unsigned integers and the characters in the <i>chksum</i> field are treated as if they were all spaces. When the computation starts, the checksum value is initialized to 0. </p>
<p>The <i>typeflag</i> field specifies the type of the file that is archived. If a specific <code>tar</code> implementation does not include support for a specific typeflag value, this implementation will extract the unknown file types as if they were plain files. For this reason, the <i>size</i> field for any file type except directories, hard links, symbolic links, character special, block specials and FIFOs must always follow the rules for plain files. </p>
<dl>
<dt><code>&#8216;0&#8217; REGTYPE</code></dt>
<dd> <p> A regular file. If the <i>size</i> field is non zero, then file data follows the header. </p>
 </dd>
<dt><code>&#8216;\0&#8217; AREGTYPE</code></dt>
<dd> <p> For backwards compatibility with pre POSIX.1-1988 <code>tar</code> implementations, a nul character is also recognized as marker for plain files. It is not generated by recent <code>tar</code> implementations. If the <i>size</i> field is non zero, then file data follows the header. </p>
 </dd>
<dt><code>&#8216;1&#8217; LNKTYPE</code></dt>
<dd> <p> The file is a hard link to another file. The name of the file that the file is linked to is in the <i>linkname</i> part of the header. For <code>tar</code> archives written by pre POSIX.1-1988 implementations, the <i>size</i> field usually contains the size of the file and needs to be ignored as no data may follow this header type. For POSIX.1-1988 compliant archives, the <i>size</i> field needs to be 0. For POSIX.1-2001 compliant archives, the <i>size</i> field may be non zero, indicating that file data is included in the archive. </p>
 </dd>
<dt><code>&#8216;2&#8217; SYMTYPE</code></dt>
<dd> <p> The file is a symbolic link to another file. The name of the file that the file is linked to is in the <i>linkname</i> part of the header. The <i>size</i> field needs to be 0. No file data may follow the header. </p>
 </dd>
<dt><code>&#8216;3&#8217; CHRTYPE</code></dt>
<dd> <p> A character special file. The fields <i>devmajor</i> and <i>devminor</i> contain information that defines the file. The meaning of the <i>size</i> field is unspecified by the POSIX standard. No file data may follow the header. </p>
 </dd>
<dt><code>&#8216;4&#8217; BLKTYPE</code></dt>
<dd> <p> A block special file. The fields <i>devmajor</i> and <i>devminor</i> contain information that defines the file. The meaning of the <i>size</i> field is unspecified by the POSIX standard. No file data may follow the header. </p>
 </dd>
<dt><code>&#8216;5&#8217; DIRTYPE</code></dt>
<dd> <p> A directory or sub directory. Old (pre POSIX.1-1988) <code>tar</code> implementations did use the same <i>typeflag</i> value as for plain files and added a slash to the name. If the <i>size</i> field is non zero then it indicates the maximum size in characters the system may allocate for this directory. If the <i>size</i> field is 0, then the system shall not limit the size of the directory. On operating systems where the disk allocation is not done on a directory base, the <i>size</i> field is ignored on extraction. No file data may follow the header. </p>
 </dd>
<dt><code>&#8216;6&#8217; FIFOTYPE</code></dt>
<dd> <p> A named pipe. The meaning of the size field is unspecified by the POSIX standard. The <i>size</i> field must be ignored on extraction. No file data may follow the header. </p>
 </dd>
<dt><code>&#8216;7&#8217; CONTTYPE</code></dt>
<dd> <p> A contiguous file. This is a file that gives special performance attributes. Operating systems that don&#8217;t support this file type extract this file type as plain files. If the <i>size</i> field is non zero, then file data follows the header. </p>
 </dd>
<dt><code>&#8216;g&#8217; GLOBAL POSIX.1-2001 HEADER</code></dt>
<dd> <p> With POSIX.1-2001 pax archives, this type defines a global extended header. The <i>size</i> is always non zero and denotes the sum of the length fields in the extended header data. The data that follows the header is in the <code>pax extended header</code> format. The extended header records in this header type affect all following files in the archive unless they are overwritten by new values. See <code>EXTENDED TAR (PAX) HEADER FORMAT</code> section below. </p>
 </dd>
<dt><code>&#8216;x&#8217; EXTENDED POSIX.1-2001 HEADER</code></dt>
<dd> <p> With POSIX.1-2001 pax archives, this type defines an extended header. The <i>size</i> is always non zero and denotes the sum of the length fields in the extended header data. The data that follows the header is in the <code>pax extended header</code> format. The extended header records in this header type only affect the following file in the archive. See <code>EXTENDED TAR (PAX) HEADER FORMAT</code> section below. </p>
 </dd>
<dt><code>&#8216;A&#8217; - &#8216;Z&#8217;</code></dt>
<dd> <p> Reserved for vendor specific implementations. </p>
 </dd>
<dt><code>&#8216;A&#8217;</code></dt>
<dd> <p> A Solaris ACL entry as used by the <code>tar</code> implementation from Sun. The <i>size</i> is always non zero and denotes the length of the data that follows the header. <code>Star</code> currently is not able to handle this header type. </p>
 </dd>
<dt><code>&#8216;D&#8217;</code></dt>
<dd> <p> A GNU dump directory. This header type is not created by <code>star</code> and handled like a directory during an extract operation, so the content is ignored by <code>star</code>. The <i>size</i> field denotes the length of the data that follows the header. </p>
 </dd>
<dt><code>&#8216;E&#8217;</code></dt>
<dd> <p> A Solaris Extended Attribute File. The <i>size</i> field denotes the length of the data that follows the header. <code>Star</code> currently is not able to handle this header type. </p>
 </dd>
<dt><code>&#8216;I&#8217;</code></dt>
<dd> <p> A <code>inode metadata</code> entry. This header type is used by <code>star</code> to archive inode meta data only. To archive more inode meta data than possible with a POSIX-1.1988 <code>tar</code> header, a header with type <code>&#8216;I&#8217;</code> is usually preceded by a <code>&#8216;x&#8217;</code> header. It is used with incremental backups. The <i>size</i> field holds the length of the file. No file data follows this header. </p>
 </dd>
<dt><code>&#8216;K&#8217;</code></dt>
<dd> <p> A long link name. <code>Star</code> is able to read and write this type of header with the <code>star</code>, <code>xstar</code> and <code>gnutar</code> formats. With the <code>xustar</code> and <code>exustar</code> formats, <code>star</code> prefers to store long link names using the POSIX.1-2001 method. The <i>size</i> is always non zero and denotes the length of the long link name including the trailing null byte. The link name is in the data that follows the header. </p>
 </dd>
<dt><code>&#8216;L&#8217;</code></dt>
<dd> <p> A long file name. <code>Star</code> is able to read and write this type of header with the <code>star</code>, <code>xstar</code> and <code>gnutar</code> formats. With the <code>xustar</code> and <code>exustar</code> formats, <code>star</code> prefers to store long file names using the POSIX.1-2001 method. The <i>size</i> is always non zero and denotes the length of the long file name including the trailing null byte. The file name is in the data that follows the header. </p>
 </dd>
<dt><code>&#8216;M&#8217;</code></dt>
<dd> <p> A multi volume continuation entry. It is used by <code>star</code> to tell the extraction program via the <i>size</i> field when the next regular archive header will follow. This allows to start extracting multi volume archives with a volume number greater than one. It is used by GNU tar to verify multi volume continuation volumes. Other fields in the GNU multi volume continuation header are a result of a GNU tar miss conception and cannot be used in a reliable tar implementation. If the <i>size</i> field is non zero the data following the header is skipped by <code>star</code> if the volume that starts with it is mounted as the first volume. This header is ignored if the volume that starts with it is mounted as continuation volume. </p>
 </dd>
<dt><code>&#8216;N&#8217;</code></dt>
<dd> <p> An outdated linktype used by old GNU tar versions to store long file names. This type is unsupported by <code>star</code>. </p>
 </dd>
<dt><code>&#8216;S&#8217;</code></dt>
<dd> <p> A sparse file. This header type is used by <code>star</code> and <code>GNU tar</code>. A sparse header is used instead of a plain file header to denote a sparse file that follows. Directly after the header, a list of sparse hole descriptors follows followed by the compacted file data. With <i>star</i> formats, the <i>size</i> field holds a size that represents the sum of the sparse hole descriptors plus the size of the compacted file data. This allows other <code>tar</code> implementations to correctly skip to the next <code>tar header</code>. With GNU tar, up to 4 sparse hole descriptors fit into the sparse header. Additional hole descriptors are not needed if the file has less than 4 holes. With GNU tar, the size field breaks general <i>tar</i> header rules in case more than 4 sparse hole descriptors are used and is meaningless because the size of the additional sparse hole descriptors used by GNU tar does not count and cannot be determined before parsing all sparse hole descriptors. </p>
 </dd>
<dt><code>&#8216;V&#8217;</code></dt>
<dd> <p> A volume header. The <i>name</i> field is is used to hold the volume name. <code>Star </code> uses the <i>atime</i> field to hold the volume number in case there is no POSIX.1-2001 extended header. This header type is used by <code>star</code> and <code>GNU tar</code>. If the <i>size</i> field is non zero the data following the header is skipped by <code>star</code>. </p>
 </dd>
<dt><code>&#8216;X&#8217;</code></dt>
<dd> <p> A vendor unique variant of the POSIX.1-2001 extended header type. It has been implemented by Sun many years before the POSIX.1-2001 standard has been approved. See also the <i>typeflag</i> &#8216;x&#8217; header type. <code>Star</code> is able to read and write this type of header. </p>
 </dd></dl>
<h2>EXTENDED TAR (PAX) HEADER STRUCTURE</h2>
<table>
<tr VALIGN=top>
<td><code>Block type</code></td>
<td><code>Description</code>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td><i></i>
</td>
</tr>
<tr VALIGN=top>
<td>Ustar Header [typeflag=&#8216;g&#8217;]</td>
<td><i>Global Extended Header</i>
</td>
</tr>
<tr VALIGN=top>
<td>Global Extended Data</td>
<td><i></i>
</td>
</tr>
<tr VALIGN=top>
<td>Ustar Header [typeflag=&#8216;x&#8217;]</td>
<td><i>Extended Header</i>
</td>
</tr>
<tr VALIGN=top>
<td>Extended Data</td>
<td><i></i>
</td>
</tr>
<tr VALIGN=top>
<td>Ustar header [typeflag=&#8216;0&#8217;]</td>
<td><i>File with Extended Header</i>
</td>
</tr>
<tr VALIGN=top>
<td>Data for File #1</td>
<td><i></i>
</td>
</tr>
<tr VALIGN=top>
<td>Ustar header [typeflag=&#8216;0&#8217;]</td>
<td><i>File without Extended Header</i>
</td>
</tr>
<tr VALIGN=top>
<td>Data for File #2</td>
<td><i></i>
</td>
</tr>
<tr VALIGN=top>
<td>Block of binary zeroes</td>
<td><i>First EOF Block</i>
</td>
</tr>
<tr VALIGN=top>
<td>Block of binary zeroes</td>
<td><i>Second EOF Block</i>
</td>
</tr>
</table>
<h2>EXTENDED TAR (PAX) HEADER FORMAT</h2>
<p>The data block that follows a <code>tar</code> archive header with <i>typeflag</i> <code>&#8216;g&#8217;</code> or <code>&#8216;x&#8217;</code> contains one or more records in the following format: </p>
<dl>
<dd> <p> &quot;%d %s=%s\n&quot;, <i>&lt;length&gt;</i>, <i>&lt;keyword&gt;</i>, <i>&lt;value&gt;</i> </p>
 </dd></dl>
<p>Each record starts with a a decimal length field. The length includes the total size of a record including the length field itself and the trailing new line. </p>
<p>The <i>keyword</i> may not include an equal sign. All keywords beginning with lower case letters and digits are reserved for future use by the POSIX standard. </p>
<p>If the value field is of zero length, it deletes any header field of the same name that is in effect from the same extended header or from a previous global header. </p>
<p>Null characters do not delimit any value. The data used for <i>value </i> is only limited by its implicit length.  </p>
<h2>EXTENDED TAR (PAX) HEADER KEYWORDS</h2>
<p> POSIX.1-2001 extended <code>pax</code> header keywords. All numerical values are represented as decimal strings. All texts are represented as 7-bit ascii or UTF-8: </p>
<dl>
<dt><code>atime</code></dt>
<dd> <p> The time from <code>st_atime</code> in sub second granularity. <code>Star</code> currently supports a nanosecond granularity. </p>
 </dd>
<dt><code>charset</code></dt>
<dd> <p> The name of the character set used to encode the data in the following file(s). </p>
 </dd>
<dl>
<dd> <p>The following values are supported for <code>charset</code>: </p>
 </dd>
<dl>
<dt><code>ISO-IR 646 1990</code></dt>
<dd> <p> SO/IEC 646:1990 </p>
 </dd>
<dt><code>ISO-IR 8859 1 1998</code></dt>
<dd> <p> ISO/IEC 8859-1:1998 </p>
 </dd>
<dt><code>ISO-IR 8859 2 1998</code></dt>
<dd> <p> ISO/IEC 8859-2:1998 </p>
 </dd>
<dt><code>ISO-IR 8859 3 1998</code></dt>
<dd> <p> ISO/IEC 8859-3:1998 </p>
 </dd>
<dt><code>ISO-IR 8859 4 1998</code></dt>
<dd> <p> ISO/IEC 8859-4:1998 </p>
 </dd>
<dt><code>ISO-IR 8859 5 1998</code></dt>
<dd> <p> ISO/IEC 8859-5:1998 </p>
 </dd>
<dt><code>ISO-IR 8859 6 1998</code></dt>
<dd> <p> ISO/IEC 8859-6:1998 </p>
 </dd>
<dt><code>ISO-IR 8859 7 1998</code></dt>
<dd> <p> ISO/IEC 8859-7:1998 </p>
 </dd>
<dt><code>ISO-IR 8859 8 1998</code></dt>
<dd> <p> ISO/IEC 8859-8:1998 </p>
 </dd>
<dt><code>ISO-IR 8859 9 1998</code></dt>
<dd> <p> ISO/IEC 8859-9:1998 </p>
 </dd>
<dt><code>ISO-IR 8859 10 1998</code></dt>
<dd> <p> ISO/IEC 8859-10:1998 </p>
 </dd>
<dt><code>ISO-IR 8859 11 1998</code></dt>
<dd> <p> ISO/IEC 8859-11:1998 </p>
 </dd>
<dt><code>ISO-IR 8859 12 1998</code></dt>
<dd> <p> ISO/IEC 8859-12:1998 </p>
 </dd>
<dt><code>ISO-IR 8859 13 1998</code></dt>
<dd> <p> ISO/IEC 8859-13:1998 </p>
 </dd>
<dt><code>ISO-IR 8859 14 1998</code></dt>
<dd> <p> ISO/IEC 8859-14:1998 </p>
 </dd>
<dt><code>ISO-IR 8859 15 1998</code></dt>
<dd> <p> ISO/IEC 8859-15:1998 </p>
 </dd>
<dt><code>ISO-IR 10646 2000</code></dt>
<dd> <p> ISO/IEC 10646:2000 </p>
 </dd>
<dt><code>ISO-IR 10646 2000 UTF-8</code></dt>
<dd> <p> ISO/IEC 10646, UTF-8 encoding </p>
 </dd>
<dt><code>BINARY</code></dt>
<dd> <p> None </p>
 </dd></dl>
<p>This keyword is currently ignored by <code>star</code>. </dl>
 </p>
<dt><code>comment</code></dt>
<dd> <p> Any number of characters that should be treated as comment. <code>Star</code> ignores the comment as documented by the POSIX standard. </p>
 </dd>
<dt><code>ctime</code></dt>
<dd> <p> The time from <code>st_ctime</code> in sub second granularity. <code>Star</code> currently supports a nanosecond granularity. </p>
 </dd>
<dt><code>gid</code></dt>
<dd> <p> The group ID of the group that owns the file. The argument is a decimal number. This field is used if the group ID of a file is greater than 2097151 (octal 7777777). </p>
 </dd>
<dt><code>gname</code></dt>
<dd> <p> The group name of the following file(s) coded in UTF-8 if the group name does not fit into 32 characters or cannot be expressed in 7-Bit ASCII. </p>
 </dd>
<dt><code>hdrcharset</code></dt>
<dd> <p> The name of the character set used to encode the data for the <code>gname</code>, <code>linkpath</code>, <code>path</code> and <code>uname</code> fields in the POSIX.1-2001 extended header records. </p>
 </dd>
<dl>
<dd> <p>The following values are supported for <code>hdrcharset</code>: </p>
 </dd>
<dl>
<dt><code>ISO-IR 10646 2000 UTF-8</code></dt>
<dd> <p> ISO/IEC 10646, UTF-8 encoding </p>
 </dd>
<dt><code>BINARY</code></dt>
<dd> <p> None </p>
 </dd></dl>
<p>This keyword is currently ignored by <code>star</code>. </dl>
 </p>
<dt><code>linkpath</code></dt>
<dd> <p> The name of the <i>linkpath</i> coded in UTF-8 if it is longer than 100 characters or cannot be expressed in 7-Bit ASCII. </p>
 </dd>
<dt><code>mtime</code></dt>
<dd> <p> The time from <code>st_mtime</code> in sub second granularity. <code>Star</code> currently supports a nanosecond granularity. </p>
 </dd>
<dt><code>path</code></dt>
<dd> <p> The name of the <i>linkpath</i> coded in UTF-8 if it does not fit into 100 characters + 155 characters prefix or cannot be expressed in 7-Bit ASCII. </p>
 </dd>
<dt><code>realtime.</code><i>any</i></dt>
<dd> <p> The keywords prefixed by <code>realtime.</code> are reserved for future standardization. </p>
 </dd>
<dt><code>security.</code><i>any</i></dt>
<dd> <p> The keywords prefixed by <code>security.</code> are reserved for future standardization. </p>
 </dd>
<dt><code>size</code></dt>
<dd> <p> The size of the file as decimal number if the file size is greater than 8589934591 (octal 77777777777). The <code>size</code> keyword may not refer to the real file size but is related to the size if the file in the archive. See also <code>SCHILY.realsize</code> for more information. </p>
 </dd>
<dt><code>uid</code></dt>
<dd> <p> The uid ID of the group that owns the file. The argument is a decimal number. This field is used if the uid ID of a file is greater than 2097151 (octal 7777777). </p>
 </dd>
<dt><code>uname</code></dt>
<dd> <p> The user name of the following file(s) coded in UTF-8 if the user name does not fit into 32 characters or cannot be expressed in 7-Bit ASCII. </p>
 </dd>
<dt><i>VENDOR</i>.keyword </dt>
<dd> <p> Any keyword that starts with a vendor name in capital letters is reserved for vendor specific extensions by the standard. <code>Star</code> uses a lot of these vendor specific extension. See below for more informations. </p>
 </dd></dl>
<h2>SCHILY PAX EXTENSION KEYWORDS</h2>
<p> <code>Star</code> uses own vendor specific extensions. The <code>SCHILY</code> vendor specific extended <code>pax</code> header keywords are: </p>
<dl>
<dt><code>SCHILY.acl.access</code></dt>
<dd> <p> The ACL for a file. </p>
<p>Since no official backup format for POSIX access control lists has been defined, <code>star</code> uses the vendor defined attributes <code>SCHILY.acl.access</code> and <code>SCHILY.acl.default</code> for storing the <code>ACL </code> and <code>Default ACL</code> of a file, respectively. The access control lists are stored in the short text form as defined in <code>POSIX 1003.1e draft standard 17</code>. </p>
<p>Note that the POSIX 1003.1e draft has been withdrawn in 1997 but some operating systems still support it with some filesystems. </p>
<p>To each named user <code>ACL</code> entry a fourth colon separated field field containing the <i>user identifier (UID)</i> of the associated user is appended. To each named group entry a fourth colon separated field containing the <i>group identifier (GID)</i> of the associated group is appended. (POSIX 1003.1e draft standard 17 allows to add fields to ACL entries.) </p>
<p>This is an example of the format used for <code>SCHILY.acl.access</code> (a space has been inserted after the equal sign and lines are broken [marked with &#8216;\&#8216; ] for readability, additional fields in bold): </p>
<pre><code>SCHILY.acl.access= user::rwx,user:lisa:r-x: 502 ,&nbsp;<wbr>\
                   group::r-x,group:toolies:rwx: 102 ,&nbsp;<wbr>\
                   mask::rwx,other::r--x
</code></pre>
<p>The numerical user and group identifiers are essential when restoring a system completely from a backup, as initially the name-to-identifier mappings may not be available, and then file ownership restoration would not work. </p>
<p>As the archive format that is used for backing up access control lists is compatible with the <code>pax</code> archive format, archives created that way can be restored by <code>star</code> or a POSIX.1-2001 compliant <code>pax</code>. Note that programs other than <code>star</code> will ignore the ACL information. </p>
 </dd>
<dt><code>SCHILY.acl.default</code></dt>
<dd> <p> The default ACL for a file. See <code>SCHILY.acl.access</code> for more information. </p>
<p>This is an example of the format used for <code>SCHILY.acl.default</code> (a space has been inserted after the equal sign and lines are broken [marked with &#8216;\&#8216; ] for readability, additional fields in bold): </p>
<pre><code>SCHILY.acl.default= user::rwx,user:lisa:r-x: 502 ,&nbsp;<wbr>\
                    group::r-x,mask::r-x,other::r-x
</code></pre>
 </dd>
<dt><code>SCHILY.acl.type</code></dt>
<dd> <p> The ACL type used for coding access control lists. </p>
<p>The following ACL types are possible: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>POSIX draft</code></dt>
<dd> <p> ACLs as defined in <code>POSIX 1003.1e draft standard 17</code>. </p>
 </dd>
<dt><code>NFSv4</code></dt>
<dd> <p> ACLs as used by <code>NFSv4</code>, <code>NTFS</code> and <code>ZFS</code>. </p>
 </dd></dl>
</dl>
<p> <code>Star</code> currently only implements <code>POSIX draft</code> ACLs. If the <code>SCHILY.acl.type</code> keyword is missing, <code>POSIX draft</code> ACLs are asumed. </p>
<dt><code>SCHILY.ddev</code></dt>
<dd> <p> The device ids for names used is the <code>SCHILY.dir</code> dump directory list from <code>st_dev</code> of the file as decimal number. The <code>SCHILY.ddev</code> keyword is followed by a space separated list of device id numbers. Each corresponds exactly to a name in the list found in <code>SCHILY.dir</code>. If a specific device id number is repeated, a comma (,) without a following space may be use to denote that the current device id number is identical to the previous number. This keyword is used in <code>dump</code> mode. This keyword is not yet implemented. </p>
<p>The value is a signed int. An implementation should be able to handle at least 64 bit values. Note that the value is signed because POSIX does not specify more than the type should be an int. </p>
 </dd>
<dt><code>SCHILY.dev</code></dt>
<dd> <p> The device id from <code>st_dev</code> of the file as decimal number. This keyword is used in <code>dump</code> mode. </p>
<p>The value is a signed int. An implementation should be able to handle at least 64 bit values. Note that the value is signed because POSIX does not specify more than the type should be an int. </p>
 </dd>
<dt><code>SCHILY.devmajor</code></dt>
<dd> <p> The device major number of the file if it is a character or block special file. The argument is a decimal number. This field is used if the device major of the file is greater than 2097151 (octal 7777777). </p>
<p>The value is a signed int. An implementation should be able to handle at least 64 bit values. Note that the value is signed because POSIX does not specify more than the type should be an int. </p>
 </dd>
<dt><code>SCHILY.devminor</code></dt>
<dd> <p> The device minor number of the file if it is a character or block special file. The argument is a decimal number. This field is used if the device minor of the file is greater than 2097151 (octal 7777777). </p>
<p>The value is a signed int. An implementation should be able to handle at least 64 bit values. Note that the value is signed because POSIX does not specify more than the type should be an int. </p>
 </dd>
<dt><code>SCHILY.dino</code></dt>
<dd> <p> The inode numbers for names used is the <code>SCHILY.dir</code> dump directory list from <code>st_ino</code> of the file as decimal number. The <code>SCHILY.dino</code> keyword is followed by a space separated list of inode numbers. Each corresponds exactly to a name in the list found in <code>SCHILY.dir</code>. This keyword is used in <code>dump</code> mode. </p>
<p>The values are unsigned int. An implementation should be able to handle at least 64 bit unsigned values. </p>
 </dd>
<dt><code>SCHILY.dir</code></dt>
<dd> <p> A list of filenames (the content) for the current directory. The names are coded in UTF-8. Each file name is prefixed by a single character that is used as a flag. Each file name is limited by a null character. The null character is directly followed by he flag character for the next file name in case the list is not terminated by the current file name. The flag character must not be a null character. By default, a ^A (octal 001) is used. The following flags are defined: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>\000</code></dt>
<dd> <p> This is the list terminator character - the second null byte, see below. </p>
 </dd>
<dt><code>^A</code></dt>
<dd> <p> The default flag that is used in case the <code>dump dir</code> features have not been active. </p>
 </dd>
<dt><code>Y</code></dt>
<dd> <p> A non directory file that is in the current (incremental) dump. </p>
 </dd>
<dt><code>N</code></dt>
<dd> <p> A non directory file that is not in the current (incremental) dump. </p>
 </dd>
<dt><code>D</code></dt>
<dd> <p> A directory that is in the current (incremental) dump. </p>
 </dd>
<dt><code>d</code></dt>
<dd> <p> A directory that is not in the current (incremental) dump. </p>
 </dd></dl>
<p>The list is terminated by two successive null bytes. The first is the null byte for the last file name. The second null byte is at the position where a flag character would be expected, it acts ad a list terminator. The length tag for the <code>SCHILY.dir</code> data includes both null bytes. </p>
<p>If a dump mode has been selected that writes compact complete directory information to the beginning of the archive, the flag character may contain values different from ^A. <code>Star</code> implementations at least up to <code>star-1.5.1</code> do not use the feature to tag entries and use the default entry \001 (^A) for all files. Tar implementations that like to read archives that use the <code>SCHILY.dir</code> keyword, shall not rely on values other than \000 (^@) or \001 (^A). </p>
<p>This keyword is used in <code>dump</code> mode. </dl>
 </p>
<dt><code>SCHILY.fflags</code></dt>
<dd> <p> A textual version of the BSD or Linux extended file flags. </p>
<p>The following flags are defined by star: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>arch</code></dt>
<dd> <p> set the archived flag (super-user only). </p>
 </dd>
<dt>archived</dt>
<dd> <p> Alias for <code>arch</code>. </p>
 </dd>
<dt><code>nodump</code></dt>
<dd> <p> set the nodump flag (owner or super-user). </p>
 </dd>
<dt><code>opaque</code></dt>
<dd> <p> set the opaque flag (owner or super-user). </p>
 </dd>
<dt><code>sappnd</code></dt>
<dd> <p> set the system append-only flag (super-user only). </p>
 </dd>
<dt>sappend</dt>
<dd> <p> Alias for <code>sappnd</code>. </p>
 </dd>
<dt><code>schg</code></dt>
<dd> <p> set the system immutable flag (super-user only). </p>
 </dd>
<dt>schange</dt>
<dd> <p> Alias for <code>schg</code>. </p>
 </dd>
<dt>simmutable</dt>
<dd> <p> Alias for <code>schg</code>. </p>
 </dd>
<dt><code>sunlnk</code></dt>
<dd> <p> set the system undeletable flag (super-user only). </p>
 </dd>
<dt>sunlink</dt>
<dd> <p> Alias for <code>sunlnk</code>. </p>
 </dd>
<dt><code>uappnd</code></dt>
<dd> <p> set the user append-only flag (owner or super-user). </p>
 </dd>
<dt>uappend</dt>
<dd> <p> Alias for <code>uappnd</code>. </p>
 </dd>
<dt><code>uchg</code></dt>
<dd> <p> set the user immutable flag (owner or super-user). </p>
 </dd>
<dt>uchange</dt>
<dd> <p> Alias for <code>uchg</code>. </p>
 </dd>
<dt>uimmutable</dt>
<dd> <p> Alias for <code>uchg</code>. </p>
 </dd>
<dt><code>uunlnk</code></dt>
<dd> <p> set the user undeletable flag (owner or super-user). </p>
 </dd>
<dt>uunlink</dt>
<dd> <p> Alias for <code>uunlnk</code>. <br />
 </p>
 </dd></dl>
<p>The following flags are only available on Linux: </p>
<dl>
<dt><code>compress</code></dt>
<dd> <p> Set the Linux ext3 journal data flag (owner or super-user). </p>
 </dd>
<dt><code>journal-data</code></dt>
<dd> <p> Set the Linux ext3 journal data flag (super-user only). </p>
 </dd>
<dt><code>noatime</code></dt>
<dd> <p> Set the Linux ext3 no access time flag (owner or super-user). </p>
 </dd>
<dt><code>secdel</code></dt>
<dd> <p> Set the Linux ext3 secure deletion (purge before delete) flag (owner or super-user). </p>
 </dd>
<dt><code>sync</code></dt>
<dd> <p> Set the Linux ext3 sync flag (owner or super-user). </p>
 </dd>
<dt><code>undel</code></dt>
<dd> <p> Set the Linux ext3 &quot;allow unrm&quot; flag (owner or super-user). </p>
 </dd></dl>
</dl>
<dt><code>SCHILY.filetype</code></dt>
<dd> <p> A textual version of the real file type of the file. The following names are used: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>unallocated</code></dt>
<dd> <p> An unknown file type that may be a result of a <code><a href="/docs/linux/man/2-unlink/">unlink</a></code>(2) operation. This should never happen. </p>
 </dd>
<dt><code>regular</code></dt>
<dd> <p> A regular file. </p>
 </dd>
<dt><code>contiguous</code></dt>
<dd> <p> A contiguous file. On operating systems or file systems that don&#8217;t support this file type, it is handled like a regular file. </p>
 </dd>
<dt><code>symlink</code></dt>
<dd> <p> A symbolic link to any file type. </p>
 </dd>
<dt><code>directory</code></dt>
<dd> <p> A directory. </p>
 </dd>
<dt><code>character special</code></dt>
<dd> <p> A character special file. </p>
 </dd>
<dt><code>block special</code></dt>
<dd> <p> A block special file. </p>
 </dd>
<dt><code>fifo</code></dt>
<dd> <p> A named pipe. </p>
 </dd>
<dt><code>socket</code></dt>
<dd> <p> A UNIX domain socket. </p>
 </dd>
<dt><code>mpx character special</code></dt>
<dd> <p> A multiplexed character special file. </p>
 </dd>
<dt><code>mpx block special</code></dt>
<dd> <p> A multiplexed block special file. </p>
 </dd>
<dt><code>XENIX nsem</code></dt>
<dd> <p> A XENIX named semaphore. </p>
 </dd>
<dt><code>XENIX nshd</code></dt>
<dd> <p> XENIX shared data. </p>
 </dd>
<dt><code>door</code></dt>
<dd> <p> A Solaris door. </p>
 </dd>
<dt><code>eventcount</code></dt>
<dd> <p> A UNOS event count. </p>
 </dd>
<dt><code>whiteout</code></dt>
<dd> <p> A BSD whiteout directory entry. </p>
 </dd>
<dt><code>sparse</code></dt>
<dd> <p> A sparse regular file. </p>
 </dd>
<dt><code>volheader</code></dt>
<dd> <p> A volume header. </p>
 </dd>
<dt><code>unknown/bad</code></dt>
<dd> <p> Any other unknown file type. This should never happen. </p>
 </dd></dl>
</dl>
<dt><code>SCHILY.ino</code></dt>
<dd> <p> The inode number from <code>st_ino</code> of the file as decimal number. This keyword is used in <code>dump</code> mode. </p>
<p>The value is an unsigned int. An implementation should be able to handle at least 64 bit unsigned values. </p>
 </dd>
<dt><code>SCHILY.nlink</code></dt>
<dd> <p> The link count of the file as decimal number. This keyword is used in <code>dump</code> mode. </p>
<p>The value is an unsigned int. An implementation should be able to handle at least 32 bit unsigned values. </p>
 </dd>
<dt><code>SCHILY.offset</code></dt>
<dd> <p> The <code>offset</code> value for a multi volume continuation header. This keyword is used with multi volume continuation headers. Multi volume continuation headers are used to allow to start reading a multi volume archive past the first volume. </p>
<p> <code>SCHILY.offset</code> specifies the byte offset within a file that was split across volumes as a result of a multi volume media change operation. </p>
<p>The value is an unsigned int. An implementation should be able to handle at least 64 bit unsigned values. </p>
 </dd>
<dt><code>SCHILY.realsize</code></dt>
<dd> <p> The real size of the file as decimal number. This keyword is used if the real size of the file differs from the visible size of the file in the archive. The real file size differs from the size in the archive if the file type is <code>sparse</code> or if the file is a continuation file on a multi volume archive. In case the <code>SCHILY.realsize</code> keyword is needed, it must be past any <code>size</code> keyword in case a <code>size</code> keyword is also present. </p>
<p>As sparse files allocate less space on tape than a regular file and as a continued file that started on a previous volume only holds parts of the file, the <code>SCHILY.realsize</code> keyword holds a bigger number than the <code>size</code> keyword. </p>
<p>The value is an unsigned int. An implementation should be able to handle at least 64 bit unsigned values. </p>
 </dd>
<dt><code>SCHILY.tarfiletype</code></dt>
<dd> <p> The following additional file types are used in <code>SCHILY.tarfiletype</code>: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>hardlink</code></dt>
<dd> <p> A hard link to any file type. </p>
 </dd>
<dt><code>dumpdir</code></dt>
<dd> <p> A directory with dump entries </p>
 </dd>
<dt><code>multivol continuation</code></dt>
<dd> <p> A multi volume continuation for any file type. </p>
 </dd>
<dt><code>meta</code></dt>
<dd> <p> A meta entry (inode meta data only) for any file type. </p>
 </dd></dl>
</dl>
<dt><code>SCHILY.xattr.</code><i>attr</i></dt>
<dd> <p> A POSIX.1-2001 coded version of the Linux extended file attributes. Linux extended file attributes are name/value pairs. Every attribute <i>name</i> results in a <code>SCHILY.xattr.</code><i>name</i> tag and the value of the extended attribute is used as the value of the POSIX.1-2001 header tag. Note that this way of coding is not portable across platforms. A version for BSD may be created but Solaris includes far more features with extended attribute files than Linux does. </p>
<p>A future version of <code>star</code> will implement a similar method as the <code>tar</code> program on Solaris currently uses. When this implementation is ready, the <code>SCHILY.xattr.</code><i>name</i> feature may be removed in favor of a truly portable implementation that supports Solaris also. </p>
 </dd></dl>
<h2>SCHILY 'G'LOBAL PAX EXTENSION KEYWORDS</h2>
<p> The following <code>star</code> vendor unique extensions may only appear in <code>&#8216;g&#8217;lobal</code> extended <code>pax</code> headers: </p>
<dl>
<dt><code>SCHILY.archtype</code></dt>
<dd> <p> The textual version of the archive type used. The textual values used for <code>SCHILY.archtype</code> are the same names that are used in the <code>star</code> command line options to set up a specific archive type. </p>
<p>The following values may currently appear in a global extended header: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>xustar</code></dt>
<dd> <p> &#8216;xstar&#8217; format without &quot;tar&quot; signature at header offset 508. </p>
 </dd>
<dt><code>exustar</code></dt>
<dd> <p> &#8216;xustar&#8217; format variant that always includes x-headers and g-headers. </p>
 </dd></dl>
<p>A complete tar implementation must be prepared to handle all archives names as documented in <code><a href="/docs/linux/man/1-star/">star</a></code>(1). </p>
<p>In order to allow archive type recognition from this keyword, the minimum tape block size must be 2x512 bytes (1024 bytes) and the <code>SCHILY.archtype</code> keyword needs to be in the first 512 bytes of the content of the first <code>&#8216;g&#8217;lobal pax</code> header. Then the first tape block may be scanned to recognize the archive type. </dl>
 </p>
<dt><code>SCHILY.release</code></dt>
<dd> <p> The textual version of the <code>star</code> version string and the platform name where this <code>star</code> has been compiled. The same text appears when calling <i>star -version</i>. </p>
<p>Other implementations may use a version string that does not start with the text <code>star</code>. </p>
 </dd>
<dt><code>SCHILY.volhdr.blockoff</code></dt>
<dd> <p> This keyword is used for multi volume archives. It represents the offset within the whole archive expressed in 512 byte units. </p>
<p>The value is an unsigned int with a valid range between 1 and infinity. An implementation should be able to handle at least 64 bit unsigned values. </p>
 </dd>
<dt><code>SCHILY.volhdr.blocksize</code></dt>
<dd> <p> The tape blocksize expressed in 512 byte units that was used when writing the archive. </p>
<p>The value is an unsigned int with a valid range between 1 and infinity. An implementation should be able to handle at least 31 bit unsigned values. </p>
 </dd>
<dt><code>SCHILY.volhdr.cwd</code></dt>
<dd> <p> This keyword is used in dump mode. It is only emitted in case the <code>fs-name=</code> option of star was used to overwrite the <code>SCHILY.volhdr.filesys</code> value. If <code>SCHILY.volhdr.cwd</code> is present, it contains the real backup working directory. </p>
<p>Overwriting <code>SCHILY.volhdr.filesys</code> is needed when backups are run on file system snapshots rather than on the real file system. </p>
 </dd>
<dt><code>SCHILY.volhdr.device</code></dt>
<dd> <p> This keyword is used in dump mode. It represents the name of the device that holds the file system data. For disk based file systems, this is the device name of the mounted device. </p>
<p>This keyword is optional. It helps to correctly identify the file system from which this dump has been made. </p>
 </dd>
<dt><code>SCHILY.volhdr.dumpdate</code></dt>
<dd> <p> This keyword is used in dump mode. It represents the time the current dump did start. </p>
 </dd>
<dt><code>SCHILY.volhdr.dumplevel</code></dt>
<dd> <p> This keyword is used in dump mode. It represents the level of the current dump. Dump levels are small numbers, the lowest possible number is 0. Dump level 0 represents a full backup. Dump level 1 represents a backup that contains all changes that did occur since the last level 0 dump. Dump level 2 represents a backup that contains all changes that did occur since the last level 1 dump. <code>Star</code> does not specify a maximum allowed dump level but you should try to keep the numbers less than 100. </p>
<p>The value is an unsigned int with a valid range between 0 and at least 100. </p>
 </dd>
<dt><code>SCHILY.volhdr.dumptype</code></dt>
<dd> <p> This keyword is used in dump mode. If the dump is a complete dump of a file system (i.e. no files are excluded via command line), then the argument is the text <code>full</code>, else the argument is the text <code>partial</code>. </p>
 </dd>
<dt><code>SCHILY.volhdr.filesys</code></dt>
<dd> <p> This keyword is used in dump mode. It represents the top level directory for the file system from which this dump has been made. If the dump represents a dump that has an associated level, then the this directory needs to be identical to the root directory of this file system which is the mount point. </p>
 </dd>
<dt><code>SCHILY.volhdr.hostname</code></dt>
<dd> <p> This keyword is used in dump mode. The value is retrieved from <code>gethostname(3)</code> or <code><a href="/docs/linux/man/2-uname/">uname</a>(2)</code>. </p>
 </dd>
<dt><code>SCHILY.volhdr.label</code></dt>
<dd> <p> The textual volume label. The volume label must be identical within a set of multi volume archives. </p>
 </dd>
<dt><code>SCHILY.volhdr.refdate</code></dt>
<dd> <p> This keyword is used in dump mode if the current dump is an incremental dump with a level &gt; 0. It represents the time the related dump did start. </p>
 </dd>
<dt><code>SCHILY.volhdr.reflevel</code></dt>
<dd> <p> This keyword is used in dump mode if the current dump is an incremental dump with a level &gt; 0. It represents the level of the related dump. The related dump is the last dump with a level that is lower that the level of this dump. If a dump with the level of the current dump -1 exists, then this is the related dump level. Otherwise, the dump level is decremented until a valid dump level could be found in the dump database. </p>
<p>The value is an unsigned int with a valid range between 0 and at least 100. </p>
 </dd>
<dt><code>SCHILY.volhdr.tapesize</code></dt>
<dd> <p> This keyword is used for multi volume archives and may be used to verify the volume size on read back. It represents the tape size expressed in 512 byte units. This keyword is set in multi volume mode if the size of the tape was not autodetected but set from a command line option. </p>
<p>The value is an unsigned int with a valid range between 1 and infinity. An implementation should be able to handle at least 64 bit unsigned values. </p>
 </dd>
<dt><code>SCHILY.volhdr.volume</code></dt>
<dd> <p> This keyword is used for multi volume archives. It represents the volume number within a volume set. The number used for the first volume is 1. </p>
<p>The value is an unsigned int with a valid range between 1 and infinity. An implementation should be able to handle at least 31 bit unsigned values. </p>
 </dd></dl>
<h2>MULTI VOLUME ARCHIVE HANDLING</h2>
<p>To be documented in the future.  </p>
<h2>SEE ALSO</h2>
<h2>NOTES</h2>
<h2>BUGS</h2>
<h2>AUTHOR</h2>
