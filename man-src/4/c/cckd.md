---
title: "cckd(4)"
name: "cckd"
section: "4"
letter: "c"
url: "/docs/linux/man/4-cckd/"
description: "cckd – Hercules Compressed CKD DASD image file"
---

<p><code>cckd</code> &#8211; Hercules Compressed CKD DASD image file </p>
<h2>Description</h2>
<p>Hercules DASD image file that emulates IBM mainframe DASD devices on a (usually) non-mainframe platform. Specified in the Hercules configuration file (default name hercules.cnf) to describe the DASD devices Hercules is to emulate. Also specified as input and/or output file to several Hercules utilities. Hercules compressed DASD devices are frequently referred to as CCKD. Hercules uncompressed DASD devices are frequently referred to as CKD. Hercules CKD DASD image files are largely compatible with P/390 AWS DASD files. </p>
<h2>Technical Overview</h2>
<p>The following provides a technical overview of CCKD internal structures. Except as indicated below, data in the following structures is stored in the byte order indicated by the CDEVHDR.options CCKD_BIGENDIAN bit (the 0x02 bit). This bit is 1 when data is big-endian byte order, 0 when data is little-endian byte order.</p>
<h3>Devhdr</h3>
<p>occupies the first 512 bytes of a CKD or CCKD DASD file. The DEVHDR contains the device type and the number of heads per cylinder. Its contents are the same whether the DASD image is compressed (CCKD) or not (CKD). Described by the CKDDASD_DEVHDR struct; 512 bytes in size.</p>
<h3>Cdevhdr</h3>
<p>immediately follows the DEVHDR, and contains fields describing the number of L1ENTs in the L1TAB, the number of L2ENTs in each L2TAB, and anchors the free space chain. Described by the CCKDDASD_DEVHDR struct; 512 bytes in size.</p>
<h3>L1Tab</h3>
<p>immediately follows the CDEVHDR, and consists of L1ENT entries, each of which points to an L2TAB. Each L1ENT is an U32 (4 bytes) offset into the CCKD DASD file. The CDEVHDR numl1tab field describes how many L1ENTs are in the L1TAB. L1ENTs are described by the CCKD_L1ENT typedef; the L1TAB is of variable size. Conceptually each L1ENT describes cdevhdr.numl2tab tracks.</p>
<h3>L2Tab</h3>
<p>is pointed to by an L1ENT, and is composed of L2ENT entries, the number of which is described by the CDEVHDR numl2tab field; currently 256 L2ENTs in each L2TAB. L2ENTs contain the offset to the TRKHDR, and the combined length of the TRKHDR and (optionally) compressed track data. The CDEVHDR numl2tab field describes how many L2ENTs are in each L2TAB. Currently, there are 256 L2ENTs in each L2TAB. Described by the CCKD_L2ENT struct; (256 * 8) bytes in size. Conceptually each L2ENT describes one track.</p>
<h3>Freeblk</h3>
<p>describes free space in the CCKD DASD image, anchored by the CDEVHDR free field. Consists of a 4 byte offset to the next free space (or zero for end of free space chain), and a 4 byte length of the free space (which length includes the 8 bytes occupied by the FREEBLK itself), followed by zero or more bytes of residual data. Described by the first 8 bytes of the CCKD_FREEBLK struct; 8 bytes in size.</p>
<h3>Trkhdr</h3>
<p>Occurs once at the beginning of each track. contains flag (one byte), CC (two bytes), and HH (two bytes) of the track. When the flag byte = 0x00, TRKHDR is the same as the Home Address on real DASD. Flag bits are described in hercules.h, and are of the format nlllllcc where n=1 for new track header format, lllll is used for track recovery purposes, and cc describes the track compression algorithm. The compression algorithms are: B&#8217;00&#8217; = uncompressed, B&#8217;01&#8217; = zlib, B&#8217;10&#8217; = bzip2, B&#8217;11&#8217; is currently invalid. Data in TRKHDR is stored in big-endian byte order. Described by the CKDDASD_TRKHDR struct; 5 bytes in size.</p>
<h3>COUNT field</h3>
<p>8 bytes, containing CC (two bytes), HH (two bytes), R (one byte), KL (one byte), and DL (two bytes). CC is the (relative zero) cylinder number. HH is the (relative zero) head number. R is the (relative zero) record number on the track. KL is the key length; if zero no key is present. DL is the length of the data record. Data in the COUNT field is stored in big-endian byte order. Described by the CKDDASD_RECHDR struct; 8 bytes in size.</p>
<h3>KEY field</h3>
<p>if present, KL bytes of record key; immediately follows the COUNT field. Byte order is not a factor for the KEY field; to the extent it is examined by Hercules code it is simply a byte stream. Size varies.</p>
<h3>DATA field.</h3>
<p>if present, DL bytes of record data; immediately follows the KEY field for keyed record, else immediately follows the COUNT field for unkeyed records. Byte order is not a factor for the DATA field; to the extent it is examined by Hercules code it is simply a byte stream. Size varies.</p>
<h2>Glossary</h2>
<h3>Ckd</h3>
<p>Count, Key, Data &#8211; contents of an track. Also refers to the Hercules uncompressed DASD image file.</p>
<h3>Cckd</h3>
<p>Compressed Count, Key, Data &#8211; compressed contents of a track. Also refers to the Hercules compressed DASD image file.</p>
<h3>Dasd</h3>
<p>Direct Access Storage Device &#8211; term the IBM mainframe world uses to refer to hard drives.</p>
<h3>Eot</h3>
<p>End Of Track &#8211; indicated by 8X&#8217;FF&#8217; in the COUNT field.</p>
<h2>See Also</h2>
<dl>
<dt><code><a rel="nofollow" href="http://www.hercules-390.org/">http://www.hercules-390.org/</a></code> the Hercules emulator homepage.</p>
<dd>
<dt><code><a rel="nofollow" href="http://www.hercules-390.org/cckddasd.html">http://www.hercules-390.org/cckddasd.html</a></code> which describes</p>
<dd>the Hercules CCKD DASD facility.</p>
<dt><code><a rel="nofollow" href="http://www.hercules-390.org/hercconf.html">http://www.hercules-390.org/hercconf.html</a></code> which describes</p>
<dd>the Hercules configuration file. </p>
<h2>History</h2>
<p>2003-02-07 originally written by James M. Morrison</p>
