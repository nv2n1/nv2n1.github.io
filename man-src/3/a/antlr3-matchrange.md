---
title: "antlr3-matchrange(3)"
name: "antlr3-matchrange"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-matchrange/"
description: "src/antlr3lexer.c –"
---

<p>src/antlr3lexer.c &#8211; </p>
<p> Base implementation of an antlr 3 lexer.</p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/antlr3lexer.h">antlr3lexer.h</a>&gt; </p>
<h3>Functions</h3>
<p>ANTLR3_API <code>pANTLR3_LEXER</code> <code>antlr3LexerNew</code> (<code>ANTLR3_UINT32</code> sizeHint, <code>pANTLR3_RECOGNIZER_SHARED_STATE</code> state) </p>
<p> ANTLR3_API <code>pANTLR3_LEXER</code> <code>antlr3LexerNewStream</code> (<code>ANTLR3_UINT32</code> sizeHint, <code>pANTLR3_INPUT_STREAM</code> input, <code>pANTLR3_RECOGNIZER_SHARED_STATE</code> state) </p>
<p> static void <code>displayRecognitionError</code> (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>pANTLR3_UINT8</code> *tokenNames)<br />
 <i>Default lexer error handler (works for 8 bit streams only!!!). </i><br />
 static <code>pANTLR3_COMMON_TOKEN</code> <code>emit</code> (<code>pANTLR3_LEXER</code> lexer) </p>
<p> static void <code>emitNew</code> (<code>pANTLR3_LEXER</code> lexer, <code>pANTLR3_COMMON_TOKEN</code> token) </p>
<p> static void <code>freeLexer</code> (<code>pANTLR3_LEXER</code> lexer)<br />
 <i>Free the resources allocated by a lexer. </i><br />
 static <code>ANTLR3_MARKER</code> <code>getCharIndex</code> (<code>pANTLR3_LEXER</code> lexer) </p>
<p> static <code>ANTLR3_UINT32</code> <code>getCharPositionInLine</code> (<code>pANTLR3_LEXER</code> lexer) </p>
<p> static void * <code>getCurrentInputSymbol</code> (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>pANTLR3_INT_STREAM</code> istream) </p>
<p> static <code>ANTLR3_UINT32</code> <code>getLine</code> (<code>pANTLR3_LEXER</code> lexer) </p>
<p> static void * <code>getMissingSymbol</code> (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>pANTLR3_INT_STREAM</code> istream, <code>pANTLR3_EXCEPTION</code> e, <code>ANTLR3_UINT32</code> expectedTokenType, <code>pANTLR3_BITSET_LIST</code> follow) </p>
<p> static <code>pANTLR3_STRING</code> <code>getText</code> (<code>pANTLR3_LEXER</code> lexer) </p>
<p> static void <code>matchAny</code> (<code>pANTLR3_LEXER</code> lexer) </p>
<p> static <code>ANTLR3_BOOLEAN</code> <code>matchc</code> (<code>pANTLR3_LEXER</code> lexer, <code>ANTLR3_UCHAR</code> c)<br />
 <i>Implementation of matchc for the lexer, overrides any base implementation in the base recognizer. </i><br />
 static <code>ANTLR3_BOOLEAN</code> <code>matchRange</code> (<code>pANTLR3_LEXER</code> lexer, <code>ANTLR3_UCHAR</code> low, <code>ANTLR3_UCHAR</code> high)<br />
 <i>Implementation of match range for the lexer, overrides any base implementation in the base recognizer. </i><br />
 static <code>ANTLR3_BOOLEAN</code> <code>matchs</code> (<code>pANTLR3_LEXER</code> lexer, <code>ANTLR3_UCHAR</code> *string)<br />
 <i>Implementation of matchs for the lexer, overrides any base implementation in the base recognizer. </i><br />
 static void <code>mTokens</code> (<code>pANTLR3_LEXER</code> lexer) </p>
<p> static <code>pANTLR3_COMMON_TOKEN</code> <code>nextToken</code> (<code>pANTLR3_TOKEN_SOURCE</code> toksource)<br />
 <i>Default implementation of the </i><code>nextToken()</code> call for a lexer.<br />
 static ANTLR3_INLINE <code>pANTLR3_COMMON_TOKEN</code> <code>nextTokenStr</code> (<code>pANTLR3_TOKEN_SOURCE</code> toksource)<br />
 <i>Returns the next available token from the current input stream. </i><br />
 static void <code>popCharStream</code> (<code>pANTLR3_LEXER</code> lexer)<br />
 <i>Stops using the current input stream and reverts to any prior input stream on the stack. </i><br />
 static void <code>pushCharStream</code> (<code>pANTLR3_LEXER</code> lexer, <code>pANTLR3_INPUT_STREAM</code> input)<br />
 <i>Change to a new input stream, remembering the old one. </i><br />
 static void <code>recover</code> (<code>pANTLR3_LEXER</code> lexer) </p>
<p> static void <code>reportError</code> (<code>pANTLR3_BASE_RECOGNIZER</code> rec) </p>
<p> static void <code>reset</code> (<code>pANTLR3_BASE_RECOGNIZER</code> rec) </p>
<p> static void <code>setCharStream</code> (<code>pANTLR3_LEXER</code> lexer, <code>pANTLR3_INPUT_STREAM</code> input) </p>
<h2>Detailed Description</h2>
<p>Base implementation of an antlr 3 lexer. </p>
<p> An ANTLR3 lexer implements a base recongizer, a token source and a lexer interface. It constructs a base recognizer with default functions, then overrides any of these that are parser specific (usual default implementation of base recognizer.</p>
<h2>Function Documentation</h2>
<h3>ANTLR3_API <code>pANTLR3_LEXER</code> antlr3LexerNew (<code>ANTLR3_UINT32</code> sizeHint, <code>pANTLR3_RECOGNIZER_SHARED_STATE</code> state)</h3>
<p>References ANTLR3_MALLOC, ANTLR3_TOKEN_EOF, ANTLR3_TOKEN_INVALID, ANTLR3_TRUE, ANTLR3_TYPE_LEXER, antlr3BaseRecognizerNew(), antlr3SetTokenAPI(), displayRecognitionError(), ANTLR3_BASE_RECOGNIZER_struct::displayRecognitionError, emit(), ANTLR3_LEXER_struct::emit, emitNew(), ANTLR3_LEXER_struct::emitNew, ANTLR3_TOKEN_SOURCE_struct::eofToken, ANTLR3_COMMON_TOKEN_struct::factoryMade, ANTLR3_BASE_RECOGNIZER_struct::free, ANTLR3_LEXER_struct::free, freeLexer(), getCharIndex(), ANTLR3_LEXER_struct::getCharIndex, getCharPositionInLine(), ANTLR3_LEXER_struct::getCharPositionInLine, getCurrentInputSymbol(), ANTLR3_BASE_RECOGNIZER_struct::getCurrentInputSymbol, getLine(), ANTLR3_LEXER_struct::getLine, getMissingSymbol(), ANTLR3_BASE_RECOGNIZER_struct::getMissingSymbol, getText(), ANTLR3_LEXER_struct::getText, matchAny(), ANTLR3_LEXER_struct::matchAny, matchc(), ANTLR3_LEXER_struct::matchc, matchRange(), ANTLR3_LEXER_struct::matchRange, matchs(), ANTLR3_LEXER_struct::matchs, mTokens(), ANTLR3_LEXER_struct::mTokens, nextToken(), ANTLR3_TOKEN_SOURCE_struct::nextToken, popCharStream(), ANTLR3_LEXER_struct::popCharStream, pushCharStream(), ANTLR3_LEXER_struct::pushCharStream, ANTLR3_LEXER_struct::rec, recover(), ANTLR3_LEXER_struct::recover, reportError(), ANTLR3_BASE_RECOGNIZER_struct::reportError, reset(), ANTLR3_BASE_RECOGNIZER_struct::reset, setCharStream(), ANTLR3_LEXER_struct::setCharStream, ANTLR3_COMMON_TOKEN_struct::setType, ANTLR3_TOKEN_SOURCE_struct::skipToken, ANTLR3_BASE_RECOGNIZER_struct::state, ANTLR3_COMMON_TOKEN_struct::strFactory, ANTLR3_TOKEN_SOURCE_struct::strFactory, ANTLR3_TOKEN_SOURCE_struct::super, ANTLR3_BASE_RECOGNIZER_struct::super, ANTLR3_RECOGNIZER_SHARED_STATE_struct::tokFactory, and ANTLR3_RECOGNIZER_SHARED_STATE_struct::tokSource. </p>
<p> Referenced by antlr3LexerNewStream().</p>
<h3>ANTLR3_API <code>pANTLR3_LEXER</code> antlr3LexerNewStream (<code>ANTLR3_UINT32</code> sizeHint, <code>pANTLR3_INPUT_STREAM</code> input, <code>pANTLR3_RECOGNIZER_SHARED_STATE</code> state)</h3>
<p>References antlr3LexerNew(), and setCharStream().</p>
<h3>static void displayRecognitionError (<code>pANTLR3_BASE_RECOGNIZER</code> rec, <code>pANTLR3_UINT8</code> * tokenNames) [static]</h3>
<p>Default lexer error handler (works for 8 bit streams only!!!). </p>
<p> References ANTLR3_FPRINTF, ANTLR3_UINT32_CAST, ANTLR3_EXCEPTION_struct::c, ANTLR3_EXCEPTION_struct::charPositionInLine, ANTLR3_STRING_struct::chars, ANTLR3_INPUT_STREAM_struct::data, ANTLR3_RECOGNIZER_SHARED_STATE_struct::exception, ANTLR3_EXCEPTION_struct::index, ANTLR3_LEXER_struct::input, ANTLR3_EXCEPTION_struct::line, ANTLR3_EXCEPTION_struct::message, ANTLR3_EXCEPTION_struct::name, ANTLR3_LEXER_struct::rec, ANTLR3_INPUT_STREAM_struct::size, ANTLR3_BASE_RECOGNIZER_struct::state, ANTLR3_EXCEPTION_struct::streamName, ANTLR3_BASE_RECOGNIZER_struct::super, ANTLR3_STRING_struct::to8, ANTLR3_RECOGNIZER_SHARED_STATE_struct::tokenStartCharIndex, ANTLR3_RECOGNIZER_SHARED_STATE_struct::tokenStartCharPositionInLine, ANTLR3_RECOGNIZER_SHARED_STATE_struct::tokenStartLine, and ANTLR3_EXCEPTION_struct::type. </p>
<p> Referenced by antlr3LexerNew().</p>
<h3>static <code>pANTLR3_COMMON_TOKEN</code> emit (<code>pANTLR3_LEXER</code> lexer) [static]</h3>
<p>References ANTLR3_TEXT_NONE, ANTLR3_TEXT_STRING, ANTLR3_RECOGNIZER_SHARED_STATE_struct::channel, ANTLR3_COMMON_TOKEN_struct::channel, ANTLR3_COMMON_TOKEN_struct::charPosition, ANTLR3_INPUT_STREAM_struct::currentLine, ANTLR3_RECOGNIZER_SHARED_STATE_struct::custom, ANTLR3_COMMON_TOKEN_struct::custom, ANTLR3_LEXER_struct::getCharIndex, ANTLR3_LEXER_struct::input, ANTLR3_COMMON_TOKEN_struct::line, ANTLR3_COMMON_TOKEN_struct::lineStart, ANTLR3_TOKEN_FACTORY_struct::newToken, ANTLR3_LEXER_struct::rec, ANTLR3_COMMON_TOKEN_struct::start, ANTLR3_BASE_RECOGNIZER_struct::state, ANTLR3_COMMON_TOKEN_struct::stop, ANTLR3_COMMON_TOKEN_struct::text, ANTLR3_RECOGNIZER_SHARED_STATE_struct::text, ANTLR3_COMMON_TOKEN_struct::textState, ANTLR3_RECOGNIZER_SHARED_STATE_struct::token, ANTLR3_RECOGNIZER_SHARED_STATE_struct::tokenStartCharIndex, ANTLR3_RECOGNIZER_SHARED_STATE_struct::tokenStartCharPositionInLine, ANTLR3_RECOGNIZER_SHARED_STATE_struct::tokenStartLine, ANTLR3_RECOGNIZER_SHARED_STATE_struct::tokFactory, ANTLR3_COMMON_TOKEN_struct::tokText, ANTLR3_RECOGNIZER_SHARED_STATE_struct::type, ANTLR3_COMMON_TOKEN_struct::type, ANTLR3_RECOGNIZER_SHARED_STATE_struct::user1, ANTLR3_COMMON_TOKEN_struct::user1, ANTLR3_RECOGNIZER_SHARED_STATE_struct::user2, ANTLR3_COMMON_TOKEN_struct::user2, ANTLR3_RECOGNIZER_SHARED_STATE_struct::user3, and ANTLR3_COMMON_TOKEN_struct::user3. </p>
<p> Referenced by antlr3LexerNew(), and nextTokenStr().</p>
<h3>static void emitNew (<code>pANTLR3_LEXER</code> lexer, <code>pANTLR3_COMMON_TOKEN</code> token) [static]</h3>
<p>References ANTLR3_LEXER_struct::rec, ANTLR3_BASE_RECOGNIZER_struct::state, and ANTLR3_RECOGNIZER_SHARED_STATE_struct::token. </p>
<p> Referenced by antlr3LexerNew().</p>
<h3>static void freeLexer (<code>pANTLR3_LEXER</code> lexer) [static]</h3>
<p>Free the resources allocated by a lexer. </p>
<p> References ANTLR3_FREE, ANTLR3_TOKEN_FACTORY_struct::close, ANTLR3_BASE_RECOGNIZER_struct::free, ANTLR3_STACK_struct::free, ANTLR3_LEXER_struct::rec, ANTLR3_BASE_RECOGNIZER_struct::state, ANTLR3_RECOGNIZER_SHARED_STATE_struct::streams, ANTLR3_RECOGNIZER_SHARED_STATE_struct::tokFactory, and ANTLR3_RECOGNIZER_SHARED_STATE_struct::tokSource. </p>
<p> Referenced by antlr3LexerNew().</p>
<h3>static <code>ANTLR3_MARKER</code> getCharIndex (<code>pANTLR3_LEXER</code> lexer) [static]</h3>
<p>References ANTLR3_INT_STREAM_struct::index, ANTLR3_LEXER_struct::input, and ANTLR3_INPUT_STREAM_struct::istream. </p>
<p> Referenced by antlr3LexerNew().</p>
<h3>static <code>ANTLR3_UINT32</code> getCharPositionInLine (<code>pANTLR3_LEXER</code> lexer) [static]</h3>
<p>References ANTLR3_INPUT_STREAM_struct::getCharPositionInLine, and ANTLR3_LEXER_struct::input. </p>
<p> Referenced by antlr3LexerNew().</p>
<h3>static void * getCurrentInputSymbol (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>pANTLR3_INT_STREAM</code> istream) [static]</h3>
<p>Referenced by antlr3LexerNew().</p>
<h3>static <code>ANTLR3_UINT32</code> getLine (<code>pANTLR3_LEXER</code> lexer) [static]</h3>
<p>References ANTLR3_INPUT_STREAM_struct::getLine, and ANTLR3_LEXER_struct::input. </p>
<p> Referenced by antlr3LexerNew().</p>
<h3>static void * getMissingSymbol (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>pANTLR3_INT_STREAM</code> istream, <code>pANTLR3_EXCEPTION</code> e, <code>ANTLR3_UINT32</code> expectedTokenType, <code>pANTLR3_BITSET_LIST</code> follow) [static]</h3>
<p>Referenced by antlr3LexerNew().</p>
<h3>static <code>pANTLR3_STRING</code> getText (<code>pANTLR3_LEXER</code> lexer) [static]</h3>
<p>References ANTLR3_INPUT_STREAM_struct::charByteSize, ANTLR3_LEXER_struct::getCharIndex, ANTLR3_LEXER_struct::input, ANTLR3_LEXER_struct::rec, ANTLR3_BASE_RECOGNIZER_struct::state, ANTLR3_INPUT_STREAM_struct::substr, ANTLR3_RECOGNIZER_SHARED_STATE_struct::text, and ANTLR3_RECOGNIZER_SHARED_STATE_struct::tokenStartCharIndex. </p>
<p> Referenced by antlr3LexerNew().</p>
<h3>static void matchAny (<code>pANTLR3_LEXER</code> lexer) [static]</h3>
<p>References ANTLR3_INT_STREAM_struct::consume, ANTLR3_LEXER_struct::input, and ANTLR3_INPUT_STREAM_struct::istream. </p>
<p> Referenced by antlr3LexerNew().</p>
<h3>static <code>ANTLR3_BOOLEAN</code> matchc (<code>pANTLR3_LEXER</code> lexer, <code>ANTLR3_UCHAR</code> c) [static]</h3>
<p>Implementation of matchc for the lexer, overrides any base implementation in the base recognizer. <code>Remarks:</code></p>
<dl COMPACT>
<dd>Note that the generated code lays down arrays of ints for constant strings so that they are int UTF32 form!</dl>
<p> References ANTLR3_INT_STREAM_struct::_LA, ANTLR3_FALSE, ANTLR3_TRUE, ANTLR3_RECOGNIZER_SHARED_STATE_struct::backtracking, ANTLR3_INT_STREAM_struct::consume, ANTLR3_BASE_RECOGNIZER_struct::exConstruct, ANTLR3_RECOGNIZER_SHARED_STATE_struct::failed, ANTLR3_LEXER_struct::input, ANTLR3_INPUT_STREAM_struct::istream, ANTLR3_LEXER_struct::rec, ANTLR3_LEXER_struct::recover, and ANTLR3_BASE_RECOGNIZER_struct::state. </p>
<p> Referenced by antlr3LexerNew().</p>
<h3>static <code>ANTLR3_BOOLEAN</code> matchRange (<code>pANTLR3_LEXER</code> lexer, <code>ANTLR3_UCHAR</code> low, <code>ANTLR3_UCHAR</code> high) [static]</h3>
<p>Implementation of match range for the lexer, overrides any base implementation in the base recognizer. <code>Remarks:</code></p>
<dl COMPACT>
<dd>Note that the generated code lays down arrays of ints for constant strings so that they are int UTF32 form!</dl>
<p> References ANTLR3_INT_STREAM_struct::_LA, ANTLR3_FALSE, ANTLR3_TRUE, ANTLR3_RECOGNIZER_SHARED_STATE_struct::backtracking, ANTLR3_INT_STREAM_struct::consume, ANTLR3_BASE_RECOGNIZER_struct::exConstruct, ANTLR3_RECOGNIZER_SHARED_STATE_struct::failed, ANTLR3_LEXER_struct::input, ANTLR3_INPUT_STREAM_struct::istream, ANTLR3_LEXER_struct::rec, ANTLR3_LEXER_struct::recover, and ANTLR3_BASE_RECOGNIZER_struct::state. </p>
<p> Referenced by antlr3LexerNew().</p>
<h3>static <code>ANTLR3_BOOLEAN</code> matchs (<code>pANTLR3_LEXER</code> lexer, <code>ANTLR3_UCHAR</code> * string) [static]</h3>
<p>Implementation of matchs for the lexer, overrides any base implementation in the base recognizer. <code>Remarks:</code></p>
<dl COMPACT>
<dd>Note that the generated code lays down arrays of ints for constant strings so that they are int UTF32 form!</dl>
<p> References ANTLR3_INT_STREAM_struct::_LA, ANTLR3_FALSE, ANTLR3_STRING_TERMINATOR, ANTLR3_TRUE, ANTLR3_RECOGNIZER_SHARED_STATE_struct::backtracking, ANTLR3_INT_STREAM_struct::consume, ANTLR3_BASE_RECOGNIZER_struct::exConstruct, ANTLR3_RECOGNIZER_SHARED_STATE_struct::failed, ANTLR3_LEXER_struct::input, ANTLR3_INPUT_STREAM_struct::istream, ANTLR3_LEXER_struct::rec, ANTLR3_LEXER_struct::recover, and ANTLR3_BASE_RECOGNIZER_struct::state. </p>
<p> Referenced by antlr3LexerNew().</p>
<h3>static void mTokens (<code>pANTLR3_LEXER</code> lexer) [static]</h3>
<p>References ANTLR3_FPRINTF. </p>
<p> Referenced by antlr3LexerNew().</p>
<h3>static <code>pANTLR3_COMMON_TOKEN</code> nextToken (<code>pANTLR3_TOKEN_SOURCE</code> toksource) [static]</h3>
<p>Default implementation of the <code>nextToken()</code> call for a lexer. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>toksource</i> Points to the implementation of a token source. The lexer is addressed by the super structure pointer.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The next token in the current input stream or the EOF token if there are no more tokens in any input stream in the stack.</dl>
<p> Write detailed description for nextToken here. </p>
<p> <code>Remarks:</code></p>
<dl COMPACT>
<dd>Write remarks for nextToken here.</dl>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>nextTokenStr</code></dl>
<p> References ANTLR3_TOKEN_EOF, nextTokenStr(), ANTLR3_LEXER_struct::popCharStream, ANTLR3_LEXER_struct::rec, ANTLR3_STACK_struct::size, ANTLR3_BASE_RECOGNIZER_struct::state, ANTLR3_RECOGNIZER_SHARED_STATE_struct::streams, ANTLR3_TOKEN_SOURCE_struct::super, and ANTLR3_COMMON_TOKEN_struct::type. </p>
<p> Referenced by antlr3LexerNew().</p>
<h3>static ANTLR3_INLINE <code>pANTLR3_COMMON_TOKEN</code> nextTokenStr (<code>pANTLR3_TOKEN_SOURCE</code> toksource) [static]</h3>
<p>Returns the next available token from the current input stream. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>toksource</i> Points to the implementation of a token source. The lexer is addressed by the super structure pointer.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The next token in the current input stream or the EOF token if there are no more tokens.</dl>
<p> <code>Remarks:</code></p>
<dl COMPACT>
<dd>Write remarks for nextToken here.</dl>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>nextToken</code></dl>
<p> Loop until we get a non skipped token or EOF </p>
<p> References ANTLR3_INT_STREAM_struct::_LA, ANTLR3_CHARSTREAM_EOF, ANTLR3_FALSE, ANTLR3_TOKEN_DEFAULT_CHANNEL, ANTLR3_TRUE, ANTLR3_RECOGNIZER_SHARED_STATE_struct::channel, ANTLR3_LEXER_struct::ctx, emit(), ANTLR3_TOKEN_SOURCE_struct::eofToken, ANTLR3_RECOGNIZER_SHARED_STATE_struct::error, ANTLR3_COMMON_TOKEN_struct::factoryMade, ANTLR3_RECOGNIZER_SHARED_STATE_struct::failed, ANTLR3_LEXER_struct::getCharIndex, ANTLR3_INPUT_STREAM_struct::getCharPositionInLine, ANTLR3_LEXER_struct::getLine, ANTLR3_INPUT_STREAM_struct::getLine, ANTLR3_INT_STREAM_struct::index, ANTLR3_LEXER_struct::input, ANTLR3_INPUT_STREAM_struct::istream, ANTLR3_LEXER_struct::mTokens, ANTLR3_LEXER_struct::rec, ANTLR3_LEXER_struct::recover, ANTLR3_BASE_RECOGNIZER_struct::reportError, ANTLR3_COMMON_TOKEN_struct::setLine, ANTLR3_COMMON_TOKEN_struct::setStartIndex, ANTLR3_COMMON_TOKEN_struct::setStopIndex, ANTLR3_TOKEN_SOURCE_struct::skipToken, ANTLR3_BASE_RECOGNIZER_struct::state, ANTLR3_TOKEN_SOURCE_struct::super, ANTLR3_RECOGNIZER_SHARED_STATE_struct::text, ANTLR3_RECOGNIZER_SHARED_STATE_struct::token, ANTLR3_RECOGNIZER_SHARED_STATE_struct::tokenStartCharIndex, ANTLR3_RECOGNIZER_SHARED_STATE_struct::tokenStartCharPositionInLine, and ANTLR3_RECOGNIZER_SHARED_STATE_struct::tokenStartLine. </p>
<p> Referenced by nextToken().</p>
<h3>static void popCharStream (<code>pANTLR3_LEXER</code> lexer) [static]</h3>
<p>Stops using the current input stream and reverts to any prior input stream on the stack. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>lexer</i> Description of parameter lexer.</dl>
<p> Pointer to a function that abandons the current input stream, whether it is empty or not and reverts to the previous stacked input stream. </p>
<p> <code>Remarks:</code></p>
<dl COMPACT>
<dd>The function fails silently if there are no prior input streams.</dl>
<p> References ANTLR3_LEXER_struct::input, ANTLR3_INPUT_STREAM_struct::istream, ANTLR3_STACK_struct::pop, ANTLR3_LEXER_struct::rec, ANTLR3_INT_STREAM_struct::rewindLast, ANTLR3_LEXER_struct::setCharStream, ANTLR3_STACK_struct::size, ANTLR3_BASE_RECOGNIZER_struct::state, ANTLR3_RECOGNIZER_SHARED_STATE_struct::streams, and ANTLR3_STACK_struct::top. </p>
<p> Referenced by antlr3LexerNew().</p>
<h3>static void pushCharStream (<code>pANTLR3_LEXER</code> lexer, <code>pANTLR3_INPUT_STREAM</code> input) [static]</h3>
<p>Change to a new input stream, remembering the old one. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>lexer</i> Pointer to the lexer instance to switch input streams for.<br />
 <i>input</i> New input stream to install as the current one.</dl>
<p> Switches the current character input stream to a new one, saving the old one, which we will revert to at the end of this new one. </p>
<p> References antlr3StackNew(), ANTLR3_LEXER_struct::input, ANTLR3_INPUT_STREAM_struct::istream, ANTLR3_INT_STREAM_struct::mark, ANTLR3_STACK_struct::push, ANTLR3_LEXER_struct::rec, ANTLR3_LEXER_struct::setCharStream, ANTLR3_BASE_RECOGNIZER_struct::state, and ANTLR3_RECOGNIZER_SHARED_STATE_struct::streams. </p>
<p> Referenced by antlr3LexerNew().</p>
<h3>static void recover (<code>pANTLR3_LEXER</code> lexer) [static]</h3>
<p>References ANTLR3_INT_STREAM_struct::consume, ANTLR3_LEXER_struct::input, and ANTLR3_INPUT_STREAM_struct::istream. </p>
<p> Referenced by antlr3LexerNew().</p>
<h3>static void reportError (<code>pANTLR3_BASE_RECOGNIZER</code> rec) [static]</h3>
<p>References ANTLR3_BASE_RECOGNIZER_struct::displayRecognitionError, ANTLR3_RECOGNIZER_SHARED_STATE_struct::errorCount, ANTLR3_BASE_RECOGNIZER_struct::state, and ANTLR3_RECOGNIZER_SHARED_STATE_struct::tokenNames. </p>
<p> Referenced by antlr3LexerNew().</p>
<h3>static void reset (<code>pANTLR3_BASE_RECOGNIZER</code> rec) [static]</h3>
<p>References ANTLR3_TOKEN_DEFAULT_CHANNEL, ANTLR3_TOKEN_INVALID, ANTLR3_RECOGNIZER_SHARED_STATE_struct::channel, ANTLR3_LEXER_struct::input, ANTLR3_INPUT_STREAM_struct::istream, ANTLR3_LEXER_struct::rec, ANTLR3_INT_STREAM_struct::seek, ANTLR3_BASE_RECOGNIZER_struct::state, ANTLR3_BASE_RECOGNIZER_struct::super, ANTLR3_RECOGNIZER_SHARED_STATE_struct::text, ANTLR3_RECOGNIZER_SHARED_STATE_struct::token, ANTLR3_RECOGNIZER_SHARED_STATE_struct::tokenStartCharIndex, ANTLR3_RECOGNIZER_SHARED_STATE_struct::tokenStartCharPositionInLine, ANTLR3_RECOGNIZER_SHARED_STATE_struct::tokenStartLine, and ANTLR3_RECOGNIZER_SHARED_STATE_struct::type. </p>
<p> Referenced by antlr3LexerNew().</p>
<h3>static void setCharStream (<code>pANTLR3_LEXER</code> lexer, <code>pANTLR3_INPUT_STREAM</code> input) [static]</h3>
<p>References antlr3RecognitionExceptionNew(), antlr3TokenFactoryNew(), ANTLR3_TOKEN_SOURCE_struct::eofToken, ANTLR3_BASE_RECOGNIZER_struct::exConstruct, ANTLR3_INPUT_STREAM_struct::fileName, ANTLR3_TOKEN_SOURCE_struct::fileName, ANTLR3_LEXER_struct::input, ANTLR3_LEXER_struct::rec, ANTLR3_TOKEN_FACTORY_struct::setInputStream, ANTLR3_BASE_RECOGNIZER_struct::state, ANTLR3_COMMON_TOKEN_struct::strFactory, ANTLR3_INPUT_STREAM_struct::strFactory, ANTLR3_TOKEN_SOURCE_struct::strFactory, ANTLR3_RECOGNIZER_SHARED_STATE_struct::text, ANTLR3_RECOGNIZER_SHARED_STATE_struct::token, ANTLR3_RECOGNIZER_SHARED_STATE_struct::tokenStartCharIndex, ANTLR3_RECOGNIZER_SHARED_STATE_struct::tokFactory, and ANTLR3_RECOGNIZER_SHARED_STATE_struct::tokSource. </p>
<p> Referenced by antlr3LexerNew(), and antlr3LexerNewStream().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for ANTLR3C from the source code.</p>
