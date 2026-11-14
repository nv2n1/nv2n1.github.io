---
title: "antlr3ucs2index(3)"
name: "antlr3ucs2index"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3ucs2index/"
description: "src/antlr3ucs2inputstream.c –"
---

<p>src/antlr3ucs2inputstream.c &#8211; </p>
<p> Base functions to initialize and manipulate a UCS2 input stream.</p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/antlr3input.h">antlr3input.h</a>&gt; </p>
<h3>Functions</h3>
<p>static void <code>antlr3UCS2Consume</code> (<code>pANTLR3_INT_STREAM</code> is)<br />
 <i>Consume the next character in an 8 bit ASCII input stream. </i><br />
 static <code>ANTLR3_MARKER</code> <code>antlr3UCS2Index</code> (<code>pANTLR3_INT_STREAM</code> is)<br />
 <i>Calculate the current index in the output stream. </i><br />
 static <code>ANTLR3_UCHAR</code> <code>antlr3UCS2LA</code> (<code>pANTLR3_INT_STREAM</code> is, <code>ANTLR3_INT32</code> la)<br />
 <i>Return the input element assuming an 8 bit ascii input. </i><br />
 static void <code>antlr3UCS2Seek</code> (<code>pANTLR3_INT_STREAM</code> is, <code>ANTLR3_MARKER</code> seekPoint)<br />
 <i>Rewind the lexer input to the state specified by the supplied mark. </i><br />
 void <code>antlr3UCS2SetupStream</code> (<code>pANTLR3_INPUT_STREAM</code> input, <code>ANTLR3_UINT32</code> type)<br />
 <i>Common function to setup function interface for a 16 bit &#8216;UCS2&#8217; input stream. </i><br />
 static <code>pANTLR3_STRING</code> <code>antlr3UCS2Substr</code> (<code>pANTLR3_INPUT_STREAM</code> input, <code>ANTLR3_MARKER</code> start, <code>ANTLR3_MARKER</code> stop)<br />
 <i>Return a substring of the ucs2 (16 bit) input stream in newly allocated memory. </i></p>
<h2>Detailed Description</h2>
<p>Base functions to initialize and manipulate a UCS2 input stream. </p>
<h2>Function Documentation</h2>
<h3>static void antlr3UCS2Consume (<code>pANTLR3_INT_STREAM</code> is) [static]</h3>
<p>Consume the next character in an 8 bit ASCII input stream. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>input</i> Input stream context pointer</dl>
<p> References ANTLR3_INPUT_STREAM_struct::charPositionInLine, ANTLR3_INPUT_STREAM_struct::currentLine, ANTLR3_INPUT_STREAM_struct::data, ANTLR3_INPUT_STREAM_struct::line, ANTLR3_INPUT_STREAM_struct::newlineChar, ANTLR3_INPUT_STREAM_struct::nextChar, ANTLR3_INPUT_STREAM_struct::sizeBuf, and ANTLR3_INT_STREAM_struct::super. </p>
<p> Referenced by antlr3UCS2SetupStream().</p>
<h3>static <code>ANTLR3_MARKER</code> antlr3UCS2Index (<code>pANTLR3_INT_STREAM</code> is) [static]</h3>
<p>Calculate the current index in the output stream. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>input</i> Input stream context pointer</dl>
<p> References ANTLR3_INPUT_STREAM_struct::nextChar, and ANTLR3_INT_STREAM_struct::super. </p>
<p> Referenced by antlr3UCS2SetupStream().</p>
<h3>static <code>ANTLR3_UCHAR</code> antlr3UCS2LA (<code>pANTLR3_INT_STREAM</code> is, <code>ANTLR3_INT32</code> la) [static]</h3>
<p>Return the input element assuming an 8 bit ascii input. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>input</i> Input stream context pointer<br />
 <i>la</i> 1 based offset of next input stream element</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Next input character in internal ANTLR3 encoding (UTF32)</dl>
<p> References ANTLR3_CHARSTREAM_EOF, ANTLR3_INPUT_STREAM_struct::data, ANTLR3_INPUT_STREAM_struct::nextChar, ANTLR3_INPUT_STREAM_struct::sizeBuf, and ANTLR3_INT_STREAM_struct::super. </p>
<p> Referenced by antlr3UCS2SetupStream().</p>
<h3>static void antlr3UCS2Seek (<code>pANTLR3_INT_STREAM</code> is, <code>ANTLR3_MARKER</code> seekPoint) [static]</h3>
<p>Rewind the lexer input to the state specified by the supplied mark. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>input</i> Input stream context pointer</dl>
<p> <code>Remarks:</code></p>
<dl COMPACT>
<dd>Assumes ASCII (or at least, 8 Bit) input stream.</dl>
<p> References ANTLR3_INT_STREAM_struct::consume, ANTLR3_INPUT_STREAM_struct::nextChar, and ANTLR3_INT_STREAM_struct::super. </p>
<p> Referenced by antlr3UCS2SetupStream().</p>
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
<h3>static <code>pANTLR3_STRING</code> antlr3UCS2Substr (<code>pANTLR3_INPUT_STREAM</code> input, <code>ANTLR3_MARKER</code> start, <code>ANTLR3_MARKER</code> stop) [static]</h3>
<p>Return a substring of the ucs2 (16 bit) input stream in newly allocated memory. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>input</i> Input stream context pointer<br />
 <i>start</i> Offset in input stream where the string starts<br />
 <i>stop</i> Offset in the input stream where the string ends.</dl>
<p> References ANTLR3_UINT32_CAST, ANTLR3_STRING_FACTORY_struct::newPtr, and ANTLR3_INPUT_STREAM_struct::strFactory. </p>
<p> Referenced by antlr3UCS2SetupStream().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for ANTLR3C from the source code.</p>
