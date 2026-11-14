---
title: "antlr3readascii(3)"
name: "antlr3readascii"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3readascii/"
description: "include/antlr3filestream.h –"
---

<p>include/antlr3filestream.h &#8211; </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/antlr3defs.h">antlr3defs.h</a>&gt; </p>
<h3>Functions</h3>
<p>ANTLR3_API void <code>antlr3Fclose</code> (<code>ANTLR3_FDSC</code> fd)<br />
 <i>Close an operating system file and free any handles etc. </i><br />
 ANTLR3_API <code>ANTLR3_FDSC</code> <code>antlr3Fopen</code> (<code>pANTLR3_UINT8</code> filename, const char *mode)<br />
 <i>Open an operating system file and return the descriptor We just use the common open() and related functions here. </i><br />
 ANTLR3_API <code>ANTLR3_UINT32</code> <code>antlr3Fread</code> (<code>ANTLR3_FDSC</code> fdsc, <code>ANTLR3_UINT32</code> count, void *data) </p>
<p> ANTLR3_API <code>ANTLR3_UINT32</code> <code>antlr3Fsize</code> (<code>pANTLR3_UINT8</code> filename) </p>
<p> ANTLR3_API <code>ANTLR3_UINT32</code> <code>antlr3readAscii</code> (<code>pANTLR3_INPUT_STREAM</code> input, <code>pANTLR3_UINT8</code> fileName) </p>
<h2>Function Documentation</h2>
<h3>ANTLR3_API void antlr3Fclose (<code>ANTLR3_FDSC</code> fd)</h3>
<p>Close an operating system file and free any handles etc. </p>
<p> Referenced by antlr3readAscii().</p>
<h3>ANTLR3_API <code>ANTLR3_FDSC</code> antlr3Fopen (<code>pANTLR3_UINT8</code> filename, const char * mode)</h3>
<p>Open an operating system file and return the descriptor We just use the common open() and related functions here. Later we might find better ways on systems such as Windows and OpenVMS for instance. But the idea is to read the while file at once anyway, so it may be irrelevant. </p>
<p> Referenced by antlr3readAscii().</p>
<h3>ANTLR3_API <code>ANTLR3_UINT32</code> antlr3Fread (<code>ANTLR3_FDSC</code> fdsc, <code>ANTLR3_UINT32</code> count, void * data)</h3>
<p>Referenced by antlr3readAscii().</p>
<h3>ANTLR3_API <code>ANTLR3_UINT32</code> antlr3Fsize (<code>pANTLR3_UINT8</code> filename)</h3>
<p>References _stat. </p>
<p> Referenced by antlr3readAscii().</p>
<h3>ANTLR3_API <code>ANTLR3_UINT32</code> antlr3readAscii (<code>pANTLR3_INPUT_STREAM</code> input, <code>pANTLR3_UINT8</code> fileName)</h3>
<p>References ANTLR3_ERR_NOFILE, ANTLR3_ERR_NOMEM, ANTLR3_MALLOC, ANTLR3_SUCCESS, ANTLR3_TRUE, antlr3Fclose(), antlr3Fopen(), antlr3Fread(), antlr3Fsize(), ANTLR3_INPUT_STREAM_struct::data, ANTLR3_INPUT_STREAM_struct::isAllocated, and ANTLR3_INPUT_STREAM_struct::sizeBuf. </p>
<p> Referenced by antlr3AsciiFileStreamNew().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for ANTLR3C from the source code.</p>
