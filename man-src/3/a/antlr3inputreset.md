---
title: "antlr3inputreset(3)"
name: "antlr3inputreset"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3inputreset/"
description: "src/antlr3inputstream.c –"
---

<p>src/antlr3inputstream.c &#8211; </p>
<p> Base functions to initialize and manipulate any input stream.</p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/antlr3input.h">antlr3input.h</a>&gt; </p>
<h3>Functions</h3>
<p>static void <code>antlr3AsciiConsume</code> (<code>pANTLR3_INT_STREAM</code> is)<br />
 <i>Consume the next character in an 8 bit ASCII input stream. </i><br />
 static <code>ANTLR3_UINT32</code> <code>antlr3AsciiGetCharPosition</code> (<code>pANTLR3_INPUT_STREAM</code> input)<br />
 <i>Return the current offset in to the current line in the input stream. </i><br />
 static <code>ANTLR3_UINT32</code> <code>antlr3AsciiGetLine</code> (<code>pANTLR3_INPUT_STREAM</code> input)<br />
 <i>Return the line number as understood by the 8 bit/ASCII input stream. </i><br />
 static void * <code>antlr3AsciiGetLineBuf</code> (<code>pANTLR3_INPUT_STREAM</code> input)<br />
 <i>Return a pointer into the input stream that points at the start of the current input line as triggered by the end of line character installed for the stream (&#8216;</i> </p>
<p> static <code>pANTLR3_STRING</code> <code>antlr3AsciiGetSourceName</code> (<code>pANTLR3_INT_STREAM</code> is) </p>
<p> static <code>ANTLR3_MARKER</code> <code>antlr3AsciiIndex</code> (<code>pANTLR3_INT_STREAM</code> is)<br />
 <i>Calculate the current index in the output stream. </i><br />
 static <code>ANTLR3_UCHAR</code> <code>antlr3AsciiLA</code> (<code>pANTLR3_INT_STREAM</code> is, <code>ANTLR3_INT32</code> la)<br />
 <i>Return the input element assuming an 8 bit ascii input. </i><br />
 static <code>ANTLR3_UCHAR</code> <code>antlr3AsciiLA_ucase</code> (<code>pANTLR3_INT_STREAM</code> is, <code>ANTLR3_INT32</code> la)<br />
 <i>Return the input element assuming an 8 bit ASCII input and always return the UPPER CASE character. </i><br />
 static void * <code>antlr3AsciiLT</code> (<code>pANTLR3_INPUT_STREAM</code> input, <code>ANTLR3_INT32</code> lt)<br />
 <i>Return the input element assuming an 8 bit ascii input. </i><br />
 static <code>ANTLR3_MARKER</code> <code>antlr3AsciiMark</code> (<code>pANTLR3_INT_STREAM</code> is)<br />
 <i>Mark the current input point in an Ascii 8 bit stream such as a file stream, where all the input is available in the buffer. </i><br />
 static void <code>antlr3AsciiRelease</code> (<code>pANTLR3_INT_STREAM</code> is, <code>ANTLR3_MARKER</code> mark)<br />
 <i>Rewind the lexer input to the state specified by the supplied mark. </i><br />
 static void <code>antlr3AsciiRewind</code> (<code>pANTLR3_INT_STREAM</code> is, <code>ANTLR3_MARKER</code> mark)<br />
 <i>Rewind the lexer input to the state specified by the supplied mark. </i><br />
 static void <code>antlr3AsciiRewindLast</code> (<code>pANTLR3_INT_STREAM</code> is)<br />
 <i>Rewind the lexer input to the state specified by the last produced mark. </i><br />
 static void <code>antlr3AsciiSeek</code> (<code>pANTLR3_INT_STREAM</code> is, <code>ANTLR3_MARKER</code> seekPoint)<br />
 <i>Rewind the lexer input to the state specified by the supplied mark. </i><br />
 static void <code>antlr3AsciiSetCharPosition</code> (<code>pANTLR3_INPUT_STREAM</code> input, <code>ANTLR3_UINT32</code> position)<br />
 <i>Set the current offset in the current line to be a particular setting. </i><br />
 static void <code>antlr3AsciiSetLine</code> (<code>pANTLR3_INPUT_STREAM</code> input, <code>ANTLR3_UINT32</code> line)<br />
 <i>Set the current line number as understood by the input stream. </i><br />
 static void <code>antlr3AsciiSetNewLineChar</code> (<code>pANTLR3_INPUT_STREAM</code> input, <code>ANTLR3_UINT32</code> newlineChar)<br />
 <i>Set the newline trigger character in the input stream to the supplied parameter. </i><br />
 static void <code>antlr3AsciiSetUcaseLA</code> (<code>pANTLR3_INPUT_STREAM</code> input, <code>ANTLR3_BOOLEAN</code> flag) </p>
<p> void <code>antlr3AsciiSetupStream</code> (<code>pANTLR3_INPUT_STREAM</code> input, <code>ANTLR3_UINT32</code> type)<br />
 <i>Common function to setup function interface for an 8 bit ASCII input stream. </i><br />
 static <code>ANTLR3_UINT32</code> <code>antlr3AsciiSize</code> (<code>pANTLR3_INPUT_STREAM</code> input)<br />
 <i>Return the size of the current input stream, as an Ascii file which in this case is the total input. </i><br />
 static <code>pANTLR3_STRING</code> <code>antlr3AsciiSubstr</code> (<code>pANTLR3_INPUT_STREAM</code> input, <code>ANTLR3_MARKER</code> start, <code>ANTLR3_MARKER</code> stop)<br />
 <i>Return a substring of the ASCII (8 bit) input stream in newly allocated memory. </i><br />
 void <code>antlr3GenericSetupStream</code> (<code>pANTLR3_INPUT_STREAM</code> input, <code>ANTLR3_UINT32</code> type) </p>
<p> static void <code>antlr3InputClose</code> (<code>pANTLR3_INPUT_STREAM</code> input)<br />
 <i>Close down an input stream and free any memory allocated by it. </i><br />
 static void <code>antlr3InputReset</code> (<code>pANTLR3_INPUT_STREAM</code> input)<br />
 <i>Reset a re-startable input stream to the start. </i></p>
<h2>Detailed Description</h2>
<p>Base functions to initialize and manipulate any input stream. </p>
<h2>Function Documentation</h2>
<h3>static void antlr3AsciiConsume (<code>pANTLR3_INT_STREAM</code> is) [static]</h3>
<p>Consume the next character in an 8 bit ASCII input stream. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>input</i> Input stream context pointer</dl>
<p> References ANTLR3_INPUT_STREAM_struct::charPositionInLine, ANTLR3_INPUT_STREAM_struct::currentLine, ANTLR3_INPUT_STREAM_struct::data, ANTLR3_INPUT_STREAM_struct::line, ANTLR3_INPUT_STREAM_struct::newlineChar, ANTLR3_INPUT_STREAM_struct::nextChar, ANTLR3_INPUT_STREAM_struct::sizeBuf, and ANTLR3_INT_STREAM_struct::super. </p>
<p> Referenced by antlr3GenericSetupStream().</p>
<h3>static <code>ANTLR3_UINT32</code> antlr3AsciiGetCharPosition (<code>pANTLR3_INPUT_STREAM</code> input) [static]</h3>
<p>Return the current offset in to the current line in the input stream. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>input</i> Input stream context pointer</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Current line offset</dl>
<p> References ANTLR3_INPUT_STREAM_struct::charPositionInLine. </p>
<p> Referenced by antlr3GenericSetupStream().</p>
<h3>static <code>ANTLR3_UINT32</code> antlr3AsciiGetLine (<code>pANTLR3_INPUT_STREAM</code> input) [static]</h3>
<p>Return the line number as understood by the 8 bit/ASCII input stream. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>input</i> Input stream context pointer</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Line number in input stream that we believe we are working on.</dl>
<p> References ANTLR3_INPUT_STREAM_struct::line. </p>
<p> Referenced by antlr3GenericSetupStream().</p>
<h3>static void * antlr3AsciiGetLineBuf (<code>pANTLR3_INPUT_STREAM</code> input) [static]</h3>
<p>Return a pointer into the input stream that points at the start of the current input line as triggered by the end of line character installed for the stream (&#8216; </p>
<dl COMPACT>
<dd><i>input</i></dl>
<p> References ANTLR3_INPUT_STREAM_struct::currentLine. </p>
<p> Referenced by antlr3GenericSetupStream().</p>
<h3>static <code>pANTLR3_STRING</code> antlr3AsciiGetSourceName (<code>pANTLR3_INT_STREAM</code> is) [static]</h3>
<p>References ANTLR3_INT_STREAM_struct::streamName. </p>
<p> Referenced by antlr3GenericSetupStream().</p>
<h3>static <code>ANTLR3_MARKER</code> antlr3AsciiIndex (<code>pANTLR3_INT_STREAM</code> is) [static]</h3>
<p>Calculate the current index in the output stream. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>input</i> Input stream context pointer</dl>
<p> References ANTLR3_INPUT_STREAM_struct::nextChar, and ANTLR3_INT_STREAM_struct::super. </p>
<p> Referenced by antlr3GenericSetupStream().</p>
<h3>static <code>ANTLR3_UCHAR</code> antlr3AsciiLA (<code>pANTLR3_INT_STREAM</code> is, <code>ANTLR3_INT32</code> la) [static]</h3>
<p>Return the input element assuming an 8 bit ascii input. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>input</i> Input stream context pointer<br />
 <i>la</i> 1 based offset of next input stream element</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Next input character in internal ANTLR3 encoding (UTF32)</dl>
<p> References ANTLR3_CHARSTREAM_EOF, ANTLR3_INPUT_STREAM_struct::data, ANTLR3_INPUT_STREAM_struct::nextChar, ANTLR3_INPUT_STREAM_struct::sizeBuf, and ANTLR3_INT_STREAM_struct::super. </p>
<p> Referenced by antlr3AsciiSetUcaseLA(), and antlr3GenericSetupStream().</p>
<h3>static <code>ANTLR3_UCHAR</code> antlr3AsciiLA_ucase (<code>pANTLR3_INT_STREAM</code> is, <code>ANTLR3_INT32</code> la) [static]</h3>
<p>Return the input element assuming an 8 bit ASCII input and always return the UPPER CASE character. Note that this is 8 bit and so we assume that the toupper function will use the correct locale for 8 bits. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>input</i> Input stream context pointer<br />
 <i>la</i> 1 based offset of next input stream element</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Next input character in internal ANTLR3 encoding (UTF32)</dl>
<p> References ANTLR3_CHARSTREAM_EOF, ANTLR3_INPUT_STREAM_struct::data, ANTLR3_INPUT_STREAM_struct::nextChar, ANTLR3_INPUT_STREAM_struct::sizeBuf, and ANTLR3_INT_STREAM_struct::super. </p>
<p> Referenced by antlr3AsciiSetUcaseLA().</p>
<h3>static void * antlr3AsciiLT (<code>pANTLR3_INPUT_STREAM</code> input, <code>ANTLR3_INT32</code> lt) [static]</h3>
<p>Return the input element assuming an 8 bit ascii input. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>input</i> Input stream context pointer<br />
 <i>lt</i> 1 based offset of next input stream element</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Next input character in internal ANTLR3 encoding (UTF32)</dl>
<p> References ANTLR3_INT_STREAM_struct::_LA, ANTLR3_FUNC_PTR, and ANTLR3_INPUT_STREAM_struct::istream. </p>
<p> Referenced by antlr3GenericSetupStream().</p>
<h3>static <code>ANTLR3_MARKER</code> antlr3AsciiMark (<code>pANTLR3_INT_STREAM</code> is) [static]</h3>
<p>Mark the current input point in an Ascii 8 bit stream such as a file stream, where all the input is available in the buffer. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>is</i> Input stream context pointer</dl>
<p> References ANTLR3_VECTOR_struct::add, ANTLR3_FREE_FUNC, ANTLR3_MALLOC, ANTLR3_INPUT_STREAM_struct::charPositionInLine, ANTLR3_LEX_STATE_struct::charPositionInLine, ANTLR3_VECTOR_struct::count, ANTLR3_INPUT_STREAM_struct::currentLine, ANTLR3_LEX_STATE_struct::currentLine, ANTLR3_VECTOR_struct::get, ANTLR3_INT_STREAM_struct::lastMarker, ANTLR3_INPUT_STREAM_struct::line, ANTLR3_LEX_STATE_struct::line, ANTLR3_INPUT_STREAM_struct::markDepth, ANTLR3_INPUT_STREAM_struct::markers, ANTLR3_INPUT_STREAM_struct::nextChar, ANTLR3_LEX_STATE_struct::nextChar, and ANTLR3_INT_STREAM_struct::super. </p>
<p> Referenced by antlr3GenericSetupStream().</p>
<h3>static void antlr3AsciiRelease (<code>pANTLR3_INT_STREAM</code> is, <code>ANTLR3_MARKER</code> mark) [static]</h3>
<p>Rewind the lexer input to the state specified by the supplied mark. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>input</i> Input stream context pointer</dl>
<p> <code>Remarks:</code></p>
<dl COMPACT>
<dd>Assumes ASCII (or at least, 8 Bit) input stream.</dl>
<p> References ANTLR3_INPUT_STREAM_struct::markDepth, and ANTLR3_INT_STREAM_struct::super. </p>
<p> Referenced by antlr3GenericSetupStream().</p>
<h3>static void antlr3AsciiRewind (<code>pANTLR3_INT_STREAM</code> is, <code>ANTLR3_MARKER</code> mark) [static]</h3>
<p>Rewind the lexer input to the state specified by the supplied mark. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>input</i> Input stream context pointer</dl>
<p> <code>Remarks:</code></p>
<dl COMPACT>
<dd>Assumes ASCII (or at least, 8 Bit) input stream.</dl>
<p> References antlr3AsciiSeek(), ANTLR3_LEX_STATE_struct::charPositionInLine, ANTLR3_INPUT_STREAM_struct::charPositionInLine, ANTLR3_LEX_STATE_struct::currentLine, ANTLR3_INPUT_STREAM_struct::currentLine, ANTLR3_VECTOR_struct::get, ANTLR3_INPUT_STREAM_struct::istream, ANTLR3_LEX_STATE_struct::line, ANTLR3_INPUT_STREAM_struct::line, ANTLR3_INPUT_STREAM_struct::markers, ANTLR3_INPUT_STREAM_struct::nextChar, ANTLR3_LEX_STATE_struct::nextChar, ANTLR3_INT_STREAM_struct::release, and ANTLR3_INT_STREAM_struct::super. </p>
<p> Referenced by antlr3GenericSetupStream().</p>
<h3>static void antlr3AsciiRewindLast (<code>pANTLR3_INT_STREAM</code> is) [static]</h3>
<p>Rewind the lexer input to the state specified by the last produced mark. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>input</i> Input stream context pointer</dl>
<p> <code>Remarks:</code></p>
<dl COMPACT>
<dd>Assumes ASCII (or at least, 8 Bit) input stream.</dl>
<p> References ANTLR3_INT_STREAM_struct::lastMarker, and ANTLR3_INT_STREAM_struct::rewind. </p>
<p> Referenced by antlr3GenericSetupStream().</p>
<h3>static void antlr3AsciiSeek (<code>pANTLR3_INT_STREAM</code> is, <code>ANTLR3_MARKER</code> seekPoint) [static]</h3>
<p>Rewind the lexer input to the state specified by the supplied mark. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>input</i> Input stream context pointer</dl>
<p> <code>Remarks:</code></p>
<dl COMPACT>
<dd>Assumes ASCII (or at least, 8 Bit) input stream.</dl>
<p> References ANTLR3_FUNC_PTR, ANTLR3_INT_STREAM_struct::consume, ANTLR3_INPUT_STREAM_struct::nextChar, and ANTLR3_INT_STREAM_struct::super. </p>
<p> Referenced by antlr3AsciiRewind(), and antlr3GenericSetupStream().</p>
<h3>static void antlr3AsciiSetCharPosition (<code>pANTLR3_INPUT_STREAM</code> input, <code>ANTLR3_UINT32</code> position) [static]</h3>
<p>Set the current offset in the current line to be a particular setting. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>input</i> Input stream context pointer<br />
 <i>position</i> New setting for current offset.</dl>
<p> <code>Remarks:</code></p>
<dl COMPACT>
<dd>This does not set the actual pointers in the input stream, it is purely for reporting purposes and so on as per <code>antlr3AsciiSetLine()</code>;</dl>
<p> References ANTLR3_INPUT_STREAM_struct::charPositionInLine. </p>
<p> Referenced by antlr3GenericSetupStream().</p>
<h3>static void antlr3AsciiSetLine (<code>pANTLR3_INPUT_STREAM</code> input, <code>ANTLR3_UINT32</code> line) [static]</h3>
<p>Set the current line number as understood by the input stream. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>input</i> Input stream context pointer<br />
 <i>line</i> Line number to tell the input stream we are on</dl>
<p> <code>Remarks:</code></p>
<dl COMPACT>
<dd>This function does not change any pointers, it just allows the programmer to set the line number according to some external criterion, such as finding a lexed directive like: nnn &#8216;file.c&#8217; for instance, such that error reporting and so on in is in sync with some original source format.</dl>
<p> References ANTLR3_INPUT_STREAM_struct::line. </p>
<p> Referenced by antlr3GenericSetupStream().</p>
<h3>static void antlr3AsciiSetNewLineChar (<code>pANTLR3_INPUT_STREAM</code> input, <code>ANTLR3_UINT32</code> newlineChar) [static]</h3>
<p>Set the newline trigger character in the input stream to the supplied parameter. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>input</i> Input stream context pointer<br />
 <i>newlineChar</i> Character to set to be the newline trigger.</dl>
<p> <code>Remarks:</code></p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>*</p>
<dd>The supplied newLineChar is in UTF32 encoding (which means ASCII and latin1 etc are the same encodings), but the input stream catered to by this function is 8 bit only, so it is up to the programmer to ensure that the character supplied is valid.</dl>
</dl>
<p> References ANTLR3_INPUT_STREAM_struct::newlineChar. </p>
<p> Referenced by antlr3GenericSetupStream().</p>
<h3>static void antlr3AsciiSetUcaseLA (<code>pANTLR3_INPUT_STREAM</code> input, <code>ANTLR3_BOOLEAN</code> flag) [static]</h3>
<p>References ANTLR3_INT_STREAM_struct::_LA, antlr3AsciiLA(), antlr3AsciiLA_ucase(), and ANTLR3_INPUT_STREAM_struct::istream. </p>
<p> Referenced by antlr3GenericSetupStream().</p>
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
<h3>static <code>ANTLR3_UINT32</code> antlr3AsciiSize (<code>pANTLR3_INPUT_STREAM</code> input) [static]</h3>
<p>Return the size of the current input stream, as an Ascii file which in this case is the total input. Other implementations may provide more sophisticated implementations to deal with non-recoverable streams and so on. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>input</i> Input stream context pointer</dl>
<p> References ANTLR3_INPUT_STREAM_struct::sizeBuf. </p>
<p> Referenced by antlr3GenericSetupStream().</p>
<h3>static <code>pANTLR3_STRING</code> antlr3AsciiSubstr (<code>pANTLR3_INPUT_STREAM</code> input, <code>ANTLR3_MARKER</code> start, <code>ANTLR3_MARKER</code> stop) [static]</h3>
<p>Return a substring of the ASCII (8 bit) input stream in newly allocated memory. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>input</i> Input stream context pointer<br />
 <i>start</i> Offset in input stream where the string starts<br />
 <i>stop</i> Offset in the input stream where the string ends.</dl>
<p> References ANTLR3_STRING_FACTORY_struct::newPtr, and ANTLR3_INPUT_STREAM_struct::strFactory. </p>
<p> Referenced by antlr3GenericSetupStream().</p>
<h3>void antlr3GenericSetupStream (<code>pANTLR3_INPUT_STREAM</code> input, <code>ANTLR3_UINT32</code> type)</h3>
<p>References ANTLR3_INT_STREAM_struct::_LA, ANTLR3_INPUT_STREAM_struct::_LT, ANTLR3_CHARSTREAM, antlr3AsciiConsume(), antlr3AsciiGetCharPosition(), antlr3AsciiGetLine(), antlr3AsciiGetLineBuf(), antlr3AsciiGetSourceName(), antlr3AsciiIndex(), antlr3AsciiLA(), antlr3AsciiLT(), antlr3AsciiMark(), antlr3AsciiRelease(), antlr3AsciiRewind(), antlr3AsciiRewindLast(), antlr3AsciiSeek(), antlr3AsciiSetCharPosition(), antlr3AsciiSetLine(), antlr3AsciiSetNewLineChar(), antlr3AsciiSetUcaseLA(), antlr3AsciiSize(), antlr3AsciiSubstr(), antlr3InputClose(), antlr3InputReset(), antlr3IntStreamNew(), ANTLR3_INPUT_STREAM_struct::charByteSize, ANTLR3_INPUT_STREAM_struct::close, ANTLR3_INT_STREAM_struct::consume, ANTLR3_INPUT_STREAM_struct::free, ANTLR3_INPUT_STREAM_struct::getCharPositionInLine, ANTLR3_INPUT_STREAM_struct::getLine, ANTLR3_INPUT_STREAM_struct::getLineBuf, ANTLR3_INT_STREAM_struct::getSourceName, ANTLR3_INT_STREAM_struct::index, ANTLR3_INPUT_STREAM_struct::istream, ANTLR3_INT_STREAM_struct::mark, ANTLR3_INPUT_STREAM_struct::markers, ANTLR3_INT_STREAM_struct::release, ANTLR3_INPUT_STREAM_struct::reset, ANTLR3_INT_STREAM_struct::rewind, ANTLR3_INT_STREAM_struct::rewindLast, ANTLR3_INT_STREAM_struct::seek, ANTLR3_INPUT_STREAM_struct::setCharPositionInLine, ANTLR3_INPUT_STREAM_struct::setLine, ANTLR3_INPUT_STREAM_struct::SetNewLineChar, ANTLR3_INPUT_STREAM_struct::setUcaseLA, ANTLR3_INPUT_STREAM_struct::size, ANTLR3_INPUT_STREAM_struct::substr, ANTLR3_INT_STREAM_struct::super, and ANTLR3_INT_STREAM_struct::type. </p>
<p> Referenced by antlr3AsciiSetupStream(), and antlr3UCS2SetupStream().</p>
<h3>static void antlr3InputClose (<code>pANTLR3_INPUT_STREAM</code> input) [static]</h3>
<p>Close down an input stream and free any memory allocated by it. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>input</i> Input stream context pointer</dl>
<p> References ANTLR3_FREE, ANTLR3_STRING_FACTORY_struct::close, ANTLR3_INPUT_STREAM_struct::data, ANTLR3_INT_STREAM_struct::free, ANTLR3_INPUT_STREAM_struct::isAllocated, ANTLR3_INPUT_STREAM_struct::istream, ANTLR3_INPUT_STREAM_struct::markers, and ANTLR3_INPUT_STREAM_struct::strFactory. </p>
<p> Referenced by antlr3GenericSetupStream().</p>
<h3>static void antlr3InputReset (<code>pANTLR3_INPUT_STREAM</code> input) [static]</h3>
<p>Reset a re-startable input stream to the start. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>input</i> Input stream context pointer</dl>
<p> References antlr3VectorNew(), ANTLR3_INPUT_STREAM_struct::charPositionInLine, ANTLR3_INPUT_STREAM_struct::currentLine, ANTLR3_INPUT_STREAM_struct::data, ANTLR3_INPUT_STREAM_struct::line, ANTLR3_INPUT_STREAM_struct::markDepth, ANTLR3_INPUT_STREAM_struct::markers, and ANTLR3_INPUT_STREAM_struct::nextChar. </p>
<p> Referenced by antlr3GenericSetupStream().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for ANTLR3C from the source code.</p>
