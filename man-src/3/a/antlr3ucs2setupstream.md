---
title: "antlr3ucs2setupstream(3)"
name: "antlr3ucs2setupstream"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3ucs2setupstream/"
description: "include/antlr3input.h –"
---

<p>include/antlr3input.h &#8211; </p>
<p> Defines the basic structures used to manipulate character streams from any input source.</p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/antlr3defs.h">antlr3defs.h</a>&gt;<br />
 #include &lt;<a href="file:/usr/include/antlr3string.h">antlr3string.h</a>&gt;<br />
 #include &lt;<a href="file:/usr/include/antlr3commontoken.h">antlr3commontoken.h</a>&gt;<br />
 #include &lt;<a href="file:/usr/include/antlr3intstream.h">antlr3intstream.h</a>&gt; </p>
<h3>Data Structures</h3>
<p>struct <code>ANTLR3_INPUT_STREAM_struct</code><br />
 <i>Master context structure for an ANTLR3 C runtime based input stream. </i><br />
 struct <code>ANTLR3_LEX_STATE_struct</code><br />
 <i>Structure for track lex input states as part of </i><code>mark()</code> and rewind() of lexer.</p>
<h3>Typedefs</h3>
<p>typedef struct <code>ANTLR3_INPUT_STREAM_struct</code> <code>ANTLR3_INPUT_STREAM</code><br />
 <i>Master context structure for an ANTLR3 C runtime based input stream. </i><br />
 typedef struct <code>ANTLR3_LEX_STATE_struct</code> <code>ANTLR3_LEX_STATE</code><br />
 <i>Structure for track lex input states as part of </i><code>mark()</code> and rewind() of lexer.</p>
<h3>Functions</h3>
<p>void <code>antlr3AsciiSetupStream</code> (<code>pANTLR3_INPUT_STREAM</code> input, <code>ANTLR3_UINT32</code> type)<br />
 <i>Common function to setup function interface for an 8 bit ASCII input stream. </i><br />
 void <code>antlr3GenericSetupStream</code> (<code>pANTLR3_INPUT_STREAM</code> input, <code>ANTLR3_UINT32</code> type) </p>
<p> void <code>antlr3UCS2SetupStream</code> (<code>pANTLR3_INPUT_STREAM</code> input, <code>ANTLR3_UINT32</code> type)<br />
 <i>Common function to setup function interface for a 16 bit &#8216;UCS2&#8217; input stream. </i></p>
<h2>Detailed Description</h2>
<p>Defines the basic structures used to manipulate character streams from any input source. </p>
<p> The first implementation of this stream was ASCII 8 bit, but any character size and encoding can in theory be used, so long as they can return a 32 bit Integer representation of their characters amd efficiently mark and revert to specific offsets into their input streams.</p>
<h2>Typedef Documentation</h2>
<h3>typedef struct <code>ANTLR3_LEX_STATE_struct</code></h3>
<p>&nbsp;<wbr>&nbsp;<wbr><code>ANTLR3_LEX_STATE</code>&quot; </p>
<p> Structure for track lex input states as part of <code>mark()</code> and rewind() of lexer.</p>
<h2>Function Documentation</h2>
<h3>void antlr3AsciiSetupStream (<code>pANTLR3_INPUT_STREAM</code> input, <code>ANTLR3_UINT32</code> type)</h3>
<p>Common function to setup function interface for an 8 bit ASCII input stream. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>input</i> Input stream context pointer</dl>
<p> <code>Remarks:</code></p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>*</p>
<dd>Many of the 8 bit ASCII oriented file stream handling functions will be usable by any or at least some other input streams. Therefore it is perfectly acceptable to call this function to install the ASCII handler then override just those functions that would not work for the particular input encoding, such as consume for instance.</dl>
</dl>
<p> References antlr3GenericSetupStream(), antlr3StringFactoryNew(), and ANTLR3_INPUT_STREAM_struct::strFactory. </p>
<p> Referenced by antlr3AsciiFileStreamNew(), antlr3NewAsciiStringCopyStream(), and antlr3NewAsciiStringInPlaceStream().</p>
<h3>void antlr3GenericSetupStream (<code>pANTLR3_INPUT_STREAM</code> input, <code>ANTLR3_UINT32</code> type)</h3>
<p>References ANTLR3_INT_STREAM_struct::_LA, ANTLR3_INPUT_STREAM_struct::_LT, ANTLR3_CHARSTREAM, antlr3AsciiConsume(), antlr3AsciiGetCharPosition(), antlr3AsciiGetLine(), antlr3AsciiGetLineBuf(), antlr3AsciiGetSourceName(), antlr3AsciiIndex(), antlr3AsciiLA(), antlr3AsciiLT(), antlr3AsciiMark(), antlr3AsciiRelease(), antlr3AsciiRewind(), antlr3AsciiRewindLast(), antlr3AsciiSeek(), antlr3AsciiSetCharPosition(), antlr3AsciiSetLine(), antlr3AsciiSetNewLineChar(), antlr3AsciiSetUcaseLA(), antlr3AsciiSize(), antlr3AsciiSubstr(), antlr3InputClose(), antlr3InputReset(), antlr3IntStreamNew(), ANTLR3_INPUT_STREAM_struct::charByteSize, ANTLR3_INPUT_STREAM_struct::close, ANTLR3_INT_STREAM_struct::consume, ANTLR3_INPUT_STREAM_struct::free, ANTLR3_INPUT_STREAM_struct::getCharPositionInLine, ANTLR3_INPUT_STREAM_struct::getLine, ANTLR3_INPUT_STREAM_struct::getLineBuf, ANTLR3_INT_STREAM_struct::getSourceName, ANTLR3_INT_STREAM_struct::index, ANTLR3_INPUT_STREAM_struct::istream, ANTLR3_INT_STREAM_struct::mark, ANTLR3_INPUT_STREAM_struct::markers, ANTLR3_INT_STREAM_struct::release, ANTLR3_INPUT_STREAM_struct::reset, ANTLR3_INT_STREAM_struct::rewind, ANTLR3_INT_STREAM_struct::rewindLast, ANTLR3_INT_STREAM_struct::seek, ANTLR3_INPUT_STREAM_struct::setCharPositionInLine, ANTLR3_INPUT_STREAM_struct::setLine, ANTLR3_INPUT_STREAM_struct::SetNewLineChar, ANTLR3_INPUT_STREAM_struct::setUcaseLA, ANTLR3_INPUT_STREAM_struct::size, ANTLR3_INPUT_STREAM_struct::substr, ANTLR3_INT_STREAM_struct::super, and ANTLR3_INT_STREAM_struct::type. </p>
<p> Referenced by antlr3AsciiSetupStream(), and antlr3UCS2SetupStream().</p>
<h3>void antlr3UCS2SetupStream (<code>pANTLR3_INPUT_STREAM</code> input, <code>ANTLR3_UINT32</code> type)</h3>
<p>Common function to setup function interface for a 16 bit &#8216;UCS2&#8217; input stream. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>input</i> Input stream context pointer</dl>
<p> <code>Remarks:</code></p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>*</p>
<dd>Strictly speaking, there is no such thing as a UCS2 input stream as the term tends to confuse the notions of character encoding, unicode and so on. However because there will possibly be a need for a UTF-16 stream, I needed to identify 16 bit streams that do not support surrogate encodings and UCS2 is how it is mostly referred to. For instance Java, Oracle and others use a 16 bit encoding of characters and so this type of stream is very common. Take it to mean, therefore, a straight 16 bit uncomplicated encoding of Unicode code points.</dl>
</dl>
<p> References ANTLR3_INT_STREAM_struct::_LA, antlr3GenericSetupStream(), antlr3UCS2Consume(), antlr3UCS2Index(), antlr3UCS2LA(), antlr3UCS2Seek(), antlr3UCS2StringFactoryNew(), antlr3UCS2Substr(), ANTLR3_INPUT_STREAM_struct::charByteSize, ANTLR3_INT_STREAM_struct::consume, ANTLR3_INT_STREAM_struct::index, ANTLR3_INPUT_STREAM_struct::istream, ANTLR3_INT_STREAM_struct::seek, ANTLR3_INPUT_STREAM_struct::strFactory, and ANTLR3_INPUT_STREAM_struct::substr. </p>
<p> Referenced by antlr3NewUCS2StringInPlaceStream().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for ANTLR3C from the source code.</p>
