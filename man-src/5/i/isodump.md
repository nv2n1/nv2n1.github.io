---
title: "isodump(5)"
name: "isodump"
section: "5"
letter: "i"
url: "/docs/linux/man/5-isodump/"
description: "isodump – format of IEEE 1394 isochronous packets dump file"
---

<p>isodump &#8211; format of IEEE 1394 isochronous packets dump file</p>
<h2>Description</h2>
<p>The isodump format stores a series of IEEE 1394 isochronous stream packets (possibly from multiple channels), including their headers. Its main use is as the output format of <code><a href="/docs/linux/man/1-dumpiso/">dumpiso</a></code>(1) and the input format of <code><a href="/docs/linux/man/1-sendiso/">sendiso</a></code>(1). </p>
<p> The 32 byte header starts at offset 0 with the string &quot;1394 isodump v1&quot; followed by a zero byte. The next 8 bytes form a 64 bit big endian integer, which represents a bit mask of the channels that were dumped. A set bit at position (1 &lt;&lt; x) signifies that channel x was being listened on. The following 8 bytes are set to zero. </p>
<p> The iso packets follow the header and are appended to the data stream in the order they were received. The packets consist of the header quadlet as originally received and the data quadlets following directly. The CRC quadlets after header and data do not appear and everything is in big endian, as seen on the bus. </p>
<p> There is no further framing of the packets in the format, packet boundaries can be found by looking at the data size field in the header quadlet of each packet. The data size field appears in the most significant 16 bits of the header quadlet, contain the size in bytes (the actual packet is padded to a multiple of four bytes) and do not include the header packet.</p>
<h2>Compatibility</h2>
<p>This format was introduced with the iso send and dump tools distributed with libraw1394. No one else uses it so far.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-sendiso/">sendiso</a></code>(1), <code><a href="/docs/linux/man/1-dumpiso/">dumpiso</a></code>(1)</p>
<h2>Author</h2>
<p>Andreas Bombe &lt;aeb [at] debian.org&gt;</p>
