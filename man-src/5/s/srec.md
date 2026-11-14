---
title: "srec(5)"
name: "srec"
section: "5"
letter: "s"
url: "/docs/linux/man/5-srec/"
description: "srec – Motorola S-record record and file format"
---

<p>srec &#8211; Motorola S-record record and file format</p>
<h2>Description</h2>
<p>Motorola S-records are a form of simple ASCII encoding for binary data. This format is commonly used for firmware uploads to GPSes, industrial robots, and other kinds of microcontroller-driven hardware. It has several convenient properties, including inspectability, easy editing with any text editor, and checksumming for verification of transmission across noisy serial lines. </p>
<p> An S-record file consists of a sequence of specially formatted ASCII character strings. An S-record will be less than or equal to 78 bytes in length. </p>
<p> The order of S-records within a file is of no significance and no particular order may be assumed. </p>
<p> The general format of an S-record follows: </p>
<dl>
<dd>
<pre>+-------------------//------------------//-----------------------+
| type | count | address | data | checksum |
+-------------------//------------------//-----------------------+</pre>
</dl>
<p> type</p>
<dl>
<dd>A char[2] field. These characters describe the type of record (S0, S1, S2, S3, S5, S7, S8, or S9).</dl>
<p> count</p>
<dl>
<dd>A char[2] field. These characters when paired and interpreted as a big-endian hexadecimal integer, display the count of remaining character pairs in the record.</dl>
<p> address</p>
<dl>
<dd>A char[4,6, or 8] field. These characters grouped and interpreted as a big-endian hexadecimal integer, display the address at which the data field is to be loaded into memory. The length of the field depends on the number of bytes necessary to hold the address. A 2-byte address uses 4 characters, a 3-byte address uses 6 characters, and a 4-byte address uses 8 characters.</dl>
<p> data</p>
<dl>
<dd>A char [0-64] field. These characters when paired and interpreted as hexadecimal values represent the memory loadable data or descriptive information.</dl>
<p> checksum</p>
<dl>
<dd>A char[2] field. These characters when paired and interpreted as a big-endian hexadecimal integer display the least significant byte of the ones complement of the sum of the byte values represented by the pairs of characters making up the count, the address, and the data fields.</dl>
<p> Each record is terminated with a line feed. If any additional or different record terminator(s) or delay characters are needed during transmission to the target system it is the responsibility of the transmitting program to provide them. </p>
<p> There are 9 record types, as follows: </p>
<p> S0</p>
<dl>
<dd>The type of record is &#8216;S0&#8217; (0x5330). The address field is unused and will be filled with zeros (0x0000). The header information within the data field is divided into the following subfields. </p>
<dl>
<dd>1. mname is char[20] and is the module name.</dl>
<dl>
<dd>2. ver is char[2] and is the version number.</dl>
<dl>
<dd>3. rev is char[2] and is the revision number.</dl>
<dl>
<dd>4. description is char[0-36] and is a text comment.</dl>
<p> Each of the subfields is composed of ASCII bytes whose associated characters, when paired, represent one byte hexadecimal values in the case of the version and revision numbers, or represent the hexadecimal values of the ASCII characters comprising the module name and description.</dl>
<p> S1</p>
<dl>
<dd>The type of record field is &#8216;S1&#8217; (0x5331). The address field is interpreted as a 2-byte big-endian address. The data field is composed of memory loadable data.</dl>
<p> S2</p>
<dl>
<dd>The type of record field is &#8216;S2&#8217; (0x5332). The address field is interpreted as a 3-byte big-endian address. The data field is composed of memory loadable data.</dl>
<p> S3</p>
<dl>
<dd>The type of record field is &#8216;S3&#8217; (0x5333). The address field is interpreted as a 4-byte big-endian address. The data field is composed of memory loadable data.</dl>
<p> S5</p>
<dl>
<dd>The type of record field is &#8216;S5&#8217; (0x5335). The address field is interpreted as a 2-byte big-endian value and contains the count of S1, S2, and S3 records previously transmitted. There is no data field.</dl>
<p> S7</p>
<dl>
<dd>The type of record field is &#8216;S7&#8217; (0x5337). The address field contains the starting execution address and is interpreted as a 4-byte big-endian address. There is no data field.</dl>
<p> S8</p>
<dl>
<dd>The type of record field is &#8216;S8&#8217; (0x5338). The address field contains the starting execution address and is interpreted as a 3-byte big-endian address. There is no data field.</dl>
<p> S9</p>
<dl>
<dd>The type of record field is &#8216;S9&#8217; (0x5339). The address field contains the starting execution address and is interpreted as a 2-byte big-endian address. There is no data field.</dl>
<h2>Example</h2>
<p>Shown below is a typical S-record format file. </p>
<dl>
<dd>
<pre> S00600004844521B
 S1130000285F245F2212226A000424290008237C2A
 S11300100002000800082629001853812341001813
 S113002041E900084E42234300182342000824A952
 S107003000144ED492
 S5030004F8
 S9030000FC</pre>
</dl>
<p> The file consists of one S0 record, four S1 records, one S5 record and an S9 record. </p>
<p> The S0 record is comprised as follows: </p>
<dl>
<dd>&bull; S0 S-record type S0, indicating it is a header record.</dl>
<dl>
<dd>&bull; 06 Hexadecimal 06 (decimal 6), indicating that six character pairs (or ASCII bytes) follow.</dl>
<dl>
<dd>&bull; 00 00 Four character 2-byte address field, zeroes in this example.</dl>
<dl>
<dd>&bull; 48 44 52 ASCII H, D, and R &#8211; &quot;HDR&quot;.</dl>
<dl>
<dd>&bull; 1B The checksum.</dl>
<p> The first S1 record is comprised as follows: </p>
<dl>
<dd>&bull; S1 S-record type S1, indicating it is a data record to be loaded at a 2-byte address.</dl>
<dl>
<dd>&bull; 13 Hexadecimal 13 (decimal 19), indicating that nineteen character pairs, representing a 2 byte address, 16 bytes of binary data, and a 1 byte checksum, follow.</dl>
<dl>
<dd>&bull; 00 00 Four character 2-byte address field; hexidecimal address 0x0000, where the data which follows is to be loaded.</dl>
<dl>
<dd>&bull; 28 5F 24 5F 22 12 22 6A 00 04 24 29 00 08 23 7C Sixteen character pairs representing the actual binary data.</dl>
<dl>
<dd>&bull; 2A The checksum.</dl>
<p> The second and third S1 records each contain 0x13 (19) character pairs and are ended with checksums of 13 and 52, respectively. The fourth S1 record contains 07 character pairs and has a checksum of 92. </p>
<p> The S5 record is comprised as follows: </p>
<dl>
<dd>&bull; S5 S-record type S5, indicating it is a count record indicating the number of S1 records</dl>
<dl>
<dd>&bull; 03 Hexadecimal 03 (decimal 3), indicating that three character pairs follow.</dl>
<dl>
<dd>&bull; 00 04 Hexadecimal 0004 (decimal 4), indicating that there are four data records previous to this record.</dl>
<dl>
<dd>&bull; F8 The checksum.</dl>
<p> The S9 record is comprised as follows: </p>
<dl>
<dd>&bull; S9 S-record type S9, indicating it is a termination record.</dl>
<dl>
<dd>&bull; 03 Hexadecimal 03 (decimal 3), indicating that three character pairs follow.</dl>
<dl>
<dd>&bull; 00 00 The address field, hexadecimal 0 (decimal 0) indicating the starting execution address.</dl>
<dl>
<dd>&bull; FC The checksum.</dl>
<h2>Notes</h2>
<dl>
<dd>&bull; There isn&#8217;t any evidence that Motorola ever made use of the header information within the data field of the S0 record, as described above. This may have been used by some third party vendors.</dl>
<dl>
<dd>&bull; The Unix manual page on S-records is the only place that a 78-byte limit on total record length or 64-byte limit on data length is documented. These values shouldn&#8217;t be trusted for the general case.</dl>
<dl>
<dd>&bull; The count field can have values in the range of 0x3 (2 bytes of address + 1 byte checksum = 3, a not very useful record) to 0xff; this is the count of remaining character <i>pairs</i>, including checksum.</dl>
<dl>
<dd>&bull; If you write code to convert S-Records, you should always assume that a record can be as long as 514 (decimal) characters in length (255 * 2 = 510, plus 4 characters for the type and count fields), plus any terminating character(s). That is, in establishing an input buffer in C, you would declare it to be an array of 515 chars, thus leaving room for the terminating null character.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-gpsd/">gpsd</a></code>(8), <code><a href="/docs/linux/man/1-gps/">gps</a></code>(1), <code><a href="/docs/linux/man/3-libgps/">libgps</a></code>(3), <code><a href="/docs/linux/man/3-libgpsd/">libgpsd</a></code>(3), <code><a href="/docs/linux/man/1-gpsfake/">gpsfake</a></code>(1). <code><a href="/docs/linux/man/1-gpsprof/">gpsprof</a></code>(1).</p>
<h2>Author</h2>
<p>From an anonymous web page, itself claiming to have been derived from an old Unix manual page. Now maintained by the GPSD project, which added endianness clarifications.</p>
