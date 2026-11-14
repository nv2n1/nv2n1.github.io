---
title: "antlr3-istream(3)"
name: "antlr3-istream"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-istream/"
description: "ANTLR3_INPUT_STREAM_struct –"
---

<h2 class="name">NAME</h2>
<p> ANTLR3_INPUT_STREAM_struct &#8211; </p>
<p> Master context structure for an ANTLR3 C runtime based input stream.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;<a href="file:/usr/include/antlr3input.h">antlr3input.h</a>&gt;</p>
<h3>Data Fields</h3>
<p> void *(* <code>_LT</code> )(struct <code>ANTLR3_INPUT_STREAM_struct</code> *input, <code>ANTLR3_INT32</code> lt)<br />
 <i>Pointer to function to return input stream element at 1 based offset from nextChar. </i><br />
 <code>ANTLR3_UINT8</code> <code>charByteSize</code><br />
 <i>Indicates the size, in 8 bit units, of a single character. </i><br />
 <code>ANTLR3_INT32</code> <code>charPositionInLine</code><br />
 <i>The offset within the current line of the current character. </i><br />
 void(* <code>close</code> )(struct <code>ANTLR3_INPUT_STREAM_struct</code> *input)<br />
 <i>Pointer to function that closes the input stream. </i><br />
 void * <code>currentLine</code><br />
 <i>Pointer into the input buffer where the current line started. </i><br />
 void * <code>data</code><br />
 <i>Pointer the start of the input string, characters may be taken as offsets from here and in original input format encoding. </i><br />
 <code>pANTLR3_STRING</code> <code>fileName</code><br />
 <i>File name string, set to pointer to memory if you set it manually as it will be </i><code>free()</code>d.<br />
 <code>ANTLR3_UINT32</code> <code>fileNo</code><br />
 <i>File number, needs to be set manually to some file index of your devising. </i><br />
 void(* <code>free</code> )(struct <code>ANTLR3_INPUT_STREAM_struct</code> *input) </p>
<p> <code>ANTLR3_UINT32</code>(* <code>getCharPositionInLine</code> )(struct <code>ANTLR3_INPUT_STREAM_struct</code> *input)<br />
 <i>Pointer to function to return the current offset in the current input stream line. </i><br />
 <code>ANTLR3_UINT32</code>(* <code>getLine</code> )(struct <code>ANTLR3_INPUT_STREAM_struct</code> *input)<br />
 <i>Pointer to function to return the current line number in the input stream. </i><br />
 void *(* <code>getLineBuf</code> )(struct <code>ANTLR3_INPUT_STREAM_struct</code> *input)<br />
 <i>Pointer to function to return the current line buffer in the input stream The pointer returned is directly into the input stream so you must copy it if you wish to manipulate it without damaging the input stream. </i><br />
 int <code>isAllocated</code><br />
 <i>Indicates if the data pointer was allocated by us, and so should be freed when the stream dies. </i><br />
 <code>pANTLR3_INT_STREAM</code> <code>istream</code><br />
 <i>Interfaces that provide streams must all provide a generic ANTLR3_INT_STREAM interface and an ANTLR3_INPUT_STREAM is no different. </i><br />
 <code>ANTLR3_UINT32</code> <code>line</code><br />
 <i>The line number we are traversing in the input file. </i><br />
 <code>ANTLR3_UINT32</code> <code>markDepth</code><br />
 <i>Tracks how deep </i><code>mark()</code> calls are nested.<br />
 <code>pANTLR3_VECTOR</code> <code>markers</code><br />
 <i>List of </i><code>mark()</code> points in the input stream.<br />
 <code>ANTLR3_UCHAR</code> <code>newlineChar</code><br />
 <i>Character that automatically causes an internal line count increment. </i><br />
 void * <code>nextChar</code><br />
 <i>Pointer to the next character to be consumed from the input data This is cast to point at the encoding of the original file that was read by the functions installed as pointer in this input stream context instance at file/string/whatever load time. </i><br />
 void(* <code>reset</code> )(struct <code>ANTLR3_INPUT_STREAM_struct</code> *input)<br />
 <i>Pointer to function that resets the input stream. </i><br />
 void(* <code>setCharPositionInLine</code> )(struct <code>ANTLR3_INPUT_STREAM_struct</code> *input, <code>ANTLR3_UINT32</code> position)<br />
 <i>Pointer to function to set the current position in the current line. </i><br />
 void(* <code>setLine</code> )(struct <code>ANTLR3_INPUT_STREAM_struct</code> *input, <code>ANTLR3_UINT32</code> <code>line</code>)<br />
 <i>Pointer to function to set the current line number in the input stream. </i><br />
 void(* <code>SetNewLineChar</code> )(struct <code>ANTLR3_INPUT_STREAM_struct</code> *input, <code>ANTLR3_UINT32</code> <code>newlineChar</code>)<br />
 <i>Pointer to function to override the default newline character that the input stream looks for to trigger the line and offset and line buffer recording information. </i><br />
 void(* <code>setUcaseLA</code> )(<code>pANTLR3_INPUT_STREAM</code> input, <code>ANTLR3_BOOLEAN</code> flag)<br />
 <i>Pinter to function that installs a version of LA that always returns upper case. </i><br />
 <code>ANTLR3_UINT32</code>(* <code>size</code> )(struct <code>ANTLR3_INPUT_STREAM_struct</code> *input)<br />
 <i>Pointer to function to return the total size of the input buffer. </i><br />
 <code>ANTLR3_UINT32</code> <code>sizeBuf</code><br />
 <i>Number of characters that can be consumed at this point in time. </i><br />
 <code>pANTLR3_STRING_FACTORY</code> <code>strFactory</code><br />
 <i>String factory for this input stream. </i><br />
 <code>pANTLR3_STRING</code>(* <code>substr</code> )(struct <code>ANTLR3_INPUT_STREAM_struct</code> *input, <code>ANTLR3_MARKER</code> start, <code>ANTLR3_MARKER</code> stop)<br />
 <i>Pointer to function to return a substring of the input stream. </i><br />
 void * <code>super</code><br />
 <i>Whatever super structure is providing the INPUT stream needs a pointer to itself so that this can be passed back to it whenever the api functions are called back from this interface. </i></p>
<h2>Detailed Description</h2>
<p> Master context structure for an ANTLR3 C runtime based input stream.</p>
<h2>Field Documentation</h2>
<h3>void*(* <code>ANTLR3_INPUT_STREAM_struct::_LT</code>)(struct <code>ANTLR3_INPUT_STREAM_struct</code> *input, <code>ANTLR3_INT32</code> lt)</h3>
<p> Pointer to function to return input stream element at 1 based offset from nextChar. Same as _LA for char stream, but token streams etc. have one of these that does other stuff of course. </p>
<p> Referenced by antlr3GenericSetupStream().</p>
<h3><code>ANTLR3_UINT8</code> <code>ANTLR3_INPUT_STREAM_struct::charByteSize</code></h3>
<p> Indicates the size, in 8 bit units, of a single character. Note that the C runtime does not deal with surrogates and UTF8 directly as this would be slow and complicated. Variable character width inputs are expected to be converted into fixed width formats, so that would be a UTF32 format for anything that cannot work with a UCS2 encoding, such as UTF-8. Generally you are best working internally with 32 bit characters. </p>
<p> Referenced by antlr3GenericSetupStream(), antlr3UCS2SetupStream(), and getText().</p>
<h3><code>ANTLR3_INT32</code> <code>ANTLR3_INPUT_STREAM_struct::charPositionInLine</code></h3>
<p> The offset within the current line of the current character. </p>
<p> Referenced by antlr3AsciiConsume(), antlr3AsciiGetCharPosition(), antlr3AsciiMark(), antlr3AsciiRewind(), antlr3AsciiSetCharPosition(), antlr3InputReset(), and antlr3UCS2Consume().</p>
<h3>void(* <code>ANTLR3_INPUT_STREAM_struct::close</code>)(struct <code>ANTLR3_INPUT_STREAM_struct</code> *input)</h3>
<p> Pointer to function that closes the input stream. </p>
<p> Referenced by antlr3AsciiFileStreamNew(), and antlr3GenericSetupStream().</p>
<h3>void* <code>ANTLR3_INPUT_STREAM_struct::currentLine</code></h3>
<p> Pointer into the input buffer where the current line started. </p>
<p> Referenced by antlr3AsciiConsume(), antlr3AsciiGetLineBuf(), antlr3AsciiMark(), antlr3AsciiRewind(), antlr3InputReset(), antlr3UCS2Consume(), and emit().</p>
<h3>void* <code>ANTLR3_INPUT_STREAM_struct::data</code></h3>
<p> Pointer the start of the input string, characters may be taken as offsets from here and in original input format encoding. </p>
<p> Referenced by antlr3AsciiConsume(), antlr3AsciiLA(), antlr3AsciiLA_ucase(), antlr3InputClose(), antlr3InputReset(), antlr3NewAsciiStringCopyStream(), antlr3NewAsciiStringInPlaceStream(), antlr3NewUCS2StringInPlaceStream(), antlr3readAscii(), antlr3UCS2Consume(), antlr3UCS2LA(), displayRecognitionError(), and getStartIndex().</p>
<h3><code>pANTLR3_STRING</code> <code>ANTLR3_INPUT_STREAM_struct::fileName</code></h3>
<p> File name string, set to pointer to memory if you set it manually as it will be <code>free()</code>d. </p>
<p> Referenced by antlr3AsciiFileStreamNew(), antlr3NewAsciiStringCopyStream(), antlr3NewAsciiStringInPlaceStream(), antlr3NewUCS2StringInPlaceStream(), antlr3RecognitionExceptionNew(), and setCharStream().</p>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_INPUT_STREAM_struct::fileNo</code></h3>
<p> File number, needs to be set manually to some file index of your devising.</p>
<h3>void(* <code>ANTLR3_INPUT_STREAM_struct::free</code>)(struct <code>ANTLR3_INPUT_STREAM_struct</code> *input)</h3>
<p> Referenced by antlr3GenericSetupStream().</p>
<h3><code>ANTLR3_UINT32</code>(* <code>ANTLR3_INPUT_STREAM_struct::getCharPositionInLine</code>)(struct <code>ANTLR3_INPUT_STREAM_struct</code> *input)</h3>
<p> Pointer to function to return the current offset in the current input stream line. </p>
<p> Referenced by antlr3GenericSetupStream(), antlr3RecognitionExceptionNew(), getCharPositionInLine(), and nextTokenStr().</p>
<h3><code>ANTLR3_UINT32</code>(* <code>ANTLR3_INPUT_STREAM_struct::getLine</code>)(struct <code>ANTLR3_INPUT_STREAM_struct</code> *input)</h3>
<p> Pointer to function to return the current line number in the input stream. </p>
<p> Referenced by antlr3GenericSetupStream(), antlr3RecognitionExceptionNew(), getLine(), and nextTokenStr().</p>
<h3>void*(* <code>ANTLR3_INPUT_STREAM_struct::getLineBuf</code>)(struct <code>ANTLR3_INPUT_STREAM_struct</code> *input)</h3>
<p> Pointer to function to return the current line buffer in the input stream The pointer returned is directly into the input stream so you must copy it if you wish to manipulate it without damaging the input stream. Encoding is obviously in the same form as the input stream. </p>
<p> <code>Remarks:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> Note taht this function wil lbe inaccurate if setLine is called as there is no way at the moment to position the input stream at a particular line number offset.</dl>
</dl>
<p> Referenced by antlr3GenericSetupStream().</p>
<h3>int <code>ANTLR3_INPUT_STREAM_struct::isAllocated</code></h3>
<p> Indicates if the data pointer was allocated by us, and so should be freed when the stream dies. </p>
<p> Referenced by antlr3InputClose(), antlr3NewAsciiStringCopyStream(), antlr3NewAsciiStringInPlaceStream(), antlr3NewUCS2StringInPlaceStream(), and antlr3readAscii().</p>
<h3><code>pANTLR3_INT_STREAM</code> <code>ANTLR3_INPUT_STREAM_struct::istream</code></h3>
<p> Interfaces that provide streams must all provide a generic ANTLR3_INT_STREAM interface and an ANTLR3_INPUT_STREAM is no different. </p>
<p> Referenced by alreadyParsedRule(), antlr3AsciiFileStreamNew(), antlr3AsciiLT(), antlr3AsciiRewind(), antlr3AsciiSetUcaseLA(), antlr3GenericSetupStream(), antlr3InputClose(), antlr3NewAsciiStringCopyStream(), antlr3NewAsciiStringInPlaceStream(), antlr3NewUCS2StringInPlaceStream(), antlr3RecognitionExceptionNew(), antlr3UCS2SetupStream(), getCharIndex(), matchAny(), matchc(), matchRange(), matchs(), memoize(), nextTokenStr(), popCharStream(), pushCharStream(), recover(), and reset().</p>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_INPUT_STREAM_struct::line</code></h3>
<p> The line number we are traversing in the input file. This gets incremented by a newline() call in the lexer grammar actions. </p>
<p> Referenced by antlr3AsciiConsume(), antlr3AsciiGetLine(), antlr3AsciiMark(), antlr3AsciiRewind(), antlr3AsciiSetLine(), antlr3InputReset(), and antlr3UCS2Consume().</p>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_INPUT_STREAM_struct::markDepth</code></h3>
<p> Tracks how deep <code>mark()</code> calls are nested. </p>
<p> Referenced by antlr3AsciiMark(), antlr3AsciiRelease(), and antlr3InputReset().</p>
<h3><code>pANTLR3_VECTOR</code> <code>ANTLR3_INPUT_STREAM_struct::markers</code></h3>
<p> List of <code>mark()</code> points in the input stream. </p>
<p> Referenced by antlr3AsciiMark(), antlr3AsciiRewind(), antlr3GenericSetupStream(), antlr3InputClose(), and antlr3InputReset().</p>
<h3><code>ANTLR3_UCHAR</code> <code>ANTLR3_INPUT_STREAM_struct::newlineChar</code></h3>
<p> Character that automatically causes an internal line count increment. </p>
<p> Referenced by antlr3AsciiConsume(), antlr3AsciiSetNewLineChar(), and antlr3UCS2Consume().</p>
<h3>void* <code>ANTLR3_INPUT_STREAM_struct::nextChar</code></h3>
<p> Pointer to the next character to be consumed from the input data This is cast to point at the encoding of the original file that was read by the functions installed as pointer in this input stream context instance at file/string/whatever load time. </p>
<p> Referenced by antlr3AsciiConsume(), antlr3AsciiIndex(), antlr3AsciiLA(), antlr3AsciiLA_ucase(), antlr3AsciiMark(), antlr3AsciiRewind(), antlr3AsciiSeek(), antlr3InputReset(), antlr3UCS2Consume(), antlr3UCS2Index(), antlr3UCS2LA(), and antlr3UCS2Seek().</p>
<h3>void(* <code>ANTLR3_INPUT_STREAM_struct::reset</code>)(struct <code>ANTLR3_INPUT_STREAM_struct</code> *input)</h3>
<p> Pointer to function that resets the input stream. </p>
<p> Referenced by antlr3GenericSetupStream().</p>
<h3>void(* <code>ANTLR3_INPUT_STREAM_struct::setCharPositionInLine</code>)(struct <code>ANTLR3_INPUT_STREAM_struct</code> *input, <code>ANTLR3_UINT32</code> position)</h3>
<p> Pointer to function to set the current position in the current line. </p>
<p> Referenced by antlr3GenericSetupStream().</p>
<h3>void(* <code>ANTLR3_INPUT_STREAM_struct::setLine</code>)(struct <code>ANTLR3_INPUT_STREAM_struct</code> *input, <code>ANTLR3_UINT32</code> <code>line</code>)</h3>
<p> Pointer to function to set the current line number in the input stream. </p>
<p> Referenced by antlr3GenericSetupStream().</p>
<h3>void(* <code>ANTLR3_INPUT_STREAM_struct::SetNewLineChar</code>)(struct <code>ANTLR3_INPUT_STREAM_struct</code> *input, <code>ANTLR3_UINT32</code> <code>newlineChar</code>)</h3>
<p> Pointer to function to override the default newline character that the input stream looks for to trigger the line and offset and line buffer recording information. <code>Remarks:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> By default the chracter &#8216; </p>
<dt>*</p>
<dd> If for some reason you do not want teh counters and pointesr to be restee, yu can set the chracter to some impossible charater such as &#8221; or whatever.</p>
<dt>*</p>
<dd> This is a single character only, so choose the last chracter in a sequence of two or more.</p>
<dt>*</p>
<dd> This is only a simple aid to error reporting &#8211; if you have a complicated binary inptu structure it may not be adequate, but you can always override every function in the input stream with your own of course, and can even write your own complete input stream set if you like.</p>
<dt>*</p>
<dd> It is your responsiblity to set a valid cahracter for the input stream type. Ther is no point setting this to 0xFFFFFFFF if the input stream is 8 bit ASCII as this will just be truncated and never trigger as the comparison will be (INT32)0xFF == (INT32)0xFFFFFFFF</dl>
</dl>
<p> Referenced by antlr3GenericSetupStream().</p>
<h3>void(* <code>ANTLR3_INPUT_STREAM_struct::setUcaseLA</code>)(<code>pANTLR3_INPUT_STREAM</code> input, <code>ANTLR3_BOOLEAN</code> flag)</h3>
<p> Pinter to function that installs a version of LA that always returns upper case. Only valid for character streams and creates a case insensitive lexer if the lexer tokens are described in upper case. The tokens will preserve case in the token text. </p>
<p> Referenced by antlr3GenericSetupStream().</p>
<h3><code>ANTLR3_UINT32</code>(* <code>ANTLR3_INPUT_STREAM_struct::size</code>)(struct <code>ANTLR3_INPUT_STREAM_struct</code> *input)</h3>
<p> Pointer to function to return the total size of the input buffer. For streams this may be just the total we have available so far. This means of course that the input stream must be careful to accumulate enough input so that any backtracking can be satisfied. </p>
<p> Referenced by antlr3GenericSetupStream(), and displayRecognitionError().</p>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_INPUT_STREAM_struct::sizeBuf</code></h3>
<p> Number of characters that can be consumed at this point in time. Mostly this is just what is left in the pre-read buffer, but if the input source is a stream such as a socket or something then we may call special read code to wait for more input. </p>
<p> Referenced by antlr3AsciiConsume(), antlr3AsciiLA(), antlr3AsciiLA_ucase(), antlr3AsciiSize(), antlr3NewAsciiStringCopyStream(), antlr3NewAsciiStringInPlaceStream(), antlr3NewUCS2StringInPlaceStream(), antlr3readAscii(), antlr3UCS2Consume(), and antlr3UCS2LA().</p>
<h3><code>pANTLR3_STRING_FACTORY</code> <code>ANTLR3_INPUT_STREAM_struct::strFactory</code></h3>
<p> String factory for this input stream. </p>
<p> Referenced by antlr3AsciiFileStreamNew(), antlr3AsciiSetupStream(), antlr3AsciiSubstr(), antlr3InputClose(), antlr3NewAsciiStringCopyStream(), antlr3NewAsciiStringInPlaceStream(), antlr3NewUCS2StringInPlaceStream(), antlr3UCS2SetupStream(), antlr3UCS2Substr(), newPoolToken(), setCharStream(), and setInputStream().</p>
<h3><code>pANTLR3_STRING</code>(* <code>ANTLR3_INPUT_STREAM_struct::substr</code>)(struct <code>ANTLR3_INPUT_STREAM_struct</code> *input, <code>ANTLR3_MARKER</code> start, <code>ANTLR3_MARKER</code> stop)</h3>
<p> Pointer to function to return a substring of the input stream. String is returned in allocated memory and is in same encoding as the input stream itself, NOT internal ANTLR3_UCHAR form. </p>
<p> Referenced by antlr3GenericSetupStream(), antlr3UCS2SetupStream(), and getText().</p>
<h3>void* <code>ANTLR3_INPUT_STREAM_struct::super</code></h3>
<p> Whatever super structure is providing the INPUT stream needs a pointer to itself so that this can be passed back to it whenever the api functions are called back from this interface. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for ANTLR3C from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbBJ">Author</a></p>
<dd></dl>
