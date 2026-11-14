---
title: "antlr3-settokenstream(3)"
name: "antlr3-settokenstream"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-settokenstream/"
description: "src/antlr3parser.c –"
---

<p>src/antlr3parser.c &#8211; </p>
<p> Implementation of the base functionality for an ANTLR3 parser.</p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/antlr3parser.h">antlr3parser.h</a>&gt; </p>
<h3>Functions</h3>
<p>ANTLR3_API <code>pANTLR3_PARSER</code> <code>antlr3ParserNew</code> (<code>ANTLR3_UINT32</code> sizeHint, <code>pANTLR3_RECOGNIZER_SHARED_STATE</code> state) </p>
<p> ANTLR3_API <code>pANTLR3_PARSER</code> <code>antlr3ParserNewStream</code> (<code>ANTLR3_UINT32</code> sizeHint, <code>pANTLR3_TOKEN_STREAM</code> tstream, <code>pANTLR3_RECOGNIZER_SHARED_STATE</code> state) </p>
<p> ANTLR3_API <code>pANTLR3_PARSER</code> <code>antlr3ParserNewStreamDbg</code> (<code>ANTLR3_UINT32</code> sizeHint, <code>pANTLR3_TOKEN_STREAM</code> tstream, <code>pANTLR3_DEBUG_EVENT_LISTENER</code> dbg, <code>pANTLR3_RECOGNIZER_SHARED_STATE</code> state) </p>
<p> static void <code>freeParser</code> (<code>pANTLR3_PARSER</code> parser) </p>
<p> static <code>pANTLR3_TOKEN_STREAM</code> <code>getTokenStream</code> (<code>pANTLR3_PARSER</code> parser) </p>
<p> static void <code>setDebugListener</code> (<code>pANTLR3_PARSER</code> parser, <code>pANTLR3_DEBUG_EVENT_LISTENER</code> dbg) </p>
<p> static void <code>setTokenStream</code> (<code>pANTLR3_PARSER</code> parser, <code>pANTLR3_TOKEN_STREAM</code>) </p>
<h2>Detailed Description</h2>
<p>Implementation of the base functionality for an ANTLR3 parser. </p>
<h2>Function Documentation</h2>
<h3>ANTLR3_API <code>pANTLR3_PARSER</code> antlr3ParserNew (<code>ANTLR3_UINT32</code> sizeHint, <code>pANTLR3_RECOGNIZER_SHARED_STATE</code> state)</h3>
<p>References ANTLR3_MALLOC, ANTLR3_TYPE_PARSER, antlr3BaseRecognizerNew(), antlr3MTExceptionNew(), ANTLR3_BASE_RECOGNIZER_struct::exConstruct, ANTLR3_PARSER_struct::free, freeParser(), getTokenStream(), ANTLR3_PARSER_struct::getTokenStream, ANTLR3_PARSER_struct::rec, setDebugListener(), ANTLR3_PARSER_struct::setDebugListener, setTokenStream(), ANTLR3_PARSER_struct::setTokenStream, and ANTLR3_BASE_RECOGNIZER_struct::super. </p>
<p> Referenced by antlr3ParserNewStream().</p>
<h3>ANTLR3_API <code>pANTLR3_PARSER</code> antlr3ParserNewStream (<code>ANTLR3_UINT32</code> sizeHint, <code>pANTLR3_TOKEN_STREAM</code> tstream, <code>pANTLR3_RECOGNIZER_SHARED_STATE</code> state)</h3>
<p>References antlr3ParserNew(), and ANTLR3_PARSER_struct::setTokenStream. </p>
<p> Referenced by antlr3ParserNewStreamDbg().</p>
<h3>ANTLR3_API <code>pANTLR3_PARSER</code> antlr3ParserNewStreamDbg (<code>ANTLR3_UINT32</code> sizeHint, <code>pANTLR3_TOKEN_STREAM</code> tstream, <code>pANTLR3_DEBUG_EVENT_LISTENER</code> dbg, <code>pANTLR3_RECOGNIZER_SHARED_STATE</code> state)</h3>
<p>References antlr3ParserNewStream(), and ANTLR3_PARSER_struct::setDebugListener.</p>
<h3>static void freeParser (<code>pANTLR3_PARSER</code> parser) [static]</h3>
<p>References ANTLR3_FREE, ANTLR3_RECOGNIZER_SHARED_STATE_struct::following, ANTLR3_BASE_RECOGNIZER_struct::free, ANTLR3_STACK_struct::free, ANTLR3_PARSER_struct::rec, and ANTLR3_BASE_RECOGNIZER_struct::state. </p>
<p> Referenced by antlr3ParserNew().</p>
<h3>static <code>pANTLR3_TOKEN_STREAM</code> getTokenStream (<code>pANTLR3_PARSER</code> parser) [static]</h3>
<p>References ANTLR3_PARSER_struct::tstream. </p>
<p> Referenced by antlr3ParserNew().</p>
<h3>static void setDebugListener (<code>pANTLR3_PARSER</code> parser, <code>pANTLR3_DEBUG_EVENT_LISTENER</code> dbg) [static]</h3>
<p>References ANTLR3_BASE_RECOGNIZER_struct::debugger, ANTLR3_PARSER_struct::rec, ANTLR3_TOKEN_STREAM_struct::setDebugListener, and ANTLR3_PARSER_struct::tstream. </p>
<p> Referenced by antlr3ParserNew().</p>
<h3>static void setTokenStream (<code>pANTLR3_PARSER</code> parser, <code>pANTLR3_TOKEN_STREAM</code> tstream) [static]</h3>
<p>References ANTLR3_PARSER_struct::rec, ANTLR3_BASE_RECOGNIZER_struct::reset, and ANTLR3_PARSER_struct::tstream. </p>
<p> Referenced by antlr3ParserNew().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for ANTLR3C from the source code.</p>
