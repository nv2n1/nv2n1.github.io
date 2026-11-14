---
title: "antlr3_parser_struct(3)"
name: "antlr3_parser_struct"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3_parser_struct/"
description: "ANTLR3_PARSER_struct –"
---

<p>ANTLR3_PARSER_struct &#8211; </p>
<p> This is the main interface for an ANTLR3 parser.</p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/antlr3parser.h">antlr3parser.h</a>&gt;</p>
<h3>Data Fields</h3>
<p>void(* <code>free</code> )(struct <code>ANTLR3_PARSER_struct</code> *parser)<br />
 <i>Pointer to a function that knows how to free resources of an ANTLR3 parser. </i><br />
 <code>pANTLR3_TOKEN_STREAM</code>(* <code>getTokenStream</code> )(struct <code>ANTLR3_PARSER_struct</code> *parser)<br />
 <i>A pointer to a function that returns the token stream for this parser. </i><br />
 <code>pANTLR3_BASE_RECOGNIZER</code> <code>rec</code><br />
 <i>A pointer to the base recognizer, where most of the parser functions actually live because they are shared between parser and tree parser and this is the easier way than copying the interface all over the place. </i><br />
 void(* <code>setDebugListener</code> )(struct <code>ANTLR3_PARSER_struct</code> *parser, <code>pANTLR3_DEBUG_EVENT_LISTENER</code> dbg)<br />
 <i>A pointer to a function that installs a debugger object (it also installs the debugging versions of the parser methods. </i><br />
 void(* <code>setTokenStream</code> )(struct <code>ANTLR3_PARSER_struct</code> *parser, <code>pANTLR3_TOKEN_STREAM</code>)<br />
 <i>A pointer to a function that installs a token stream for the parser. </i><br />
 void * <code>super</code><br />
 <i>All superstructure implementers of this interface require a pointer to their selves, which they can reference using the super pointer here. </i><br />
 <code>pANTLR3_TOKEN_STREAM</code> <code>tstream</code><br />
 <i>A provider of a tokenstream interface, for the parser to consume tokens from. </i></p>
<h2>Detailed Description</h2>
<p>This is the main interface for an ANTLR3 parser.</p>
<h2>Field Documentation</h2>
<h3>void(* <code>ANTLR3_PARSER_struct::free</code>)(struct <code>ANTLR3_PARSER_struct</code> *parser)</h3>
<p>Pointer to a function that knows how to free resources of an ANTLR3 parser. </p>
<p> Referenced by antlr3ParserNew().</p>
<h3><code>pANTLR3_TOKEN_STREAM</code>(* <code>ANTLR3_PARSER_struct::getTokenStream</code>)(struct <code>ANTLR3_PARSER_struct</code> *parser)</h3>
<p>A pointer to a function that returns the token stream for this parser. </p>
<p> Referenced by antlr3ParserNew().</p>
<h3><code>pANTLR3_BASE_RECOGNIZER</code> <code>ANTLR3_PARSER_struct::rec</code></h3>
<p>A pointer to the base recognizer, where most of the parser functions actually live because they are shared between parser and tree parser and this is the easier way than copying the interface all over the place. Macros hide this for the generated code so it is easier on the eye (though not the debugger ;-). </p>
<p> Referenced by antlr3ParserNew(), freeParser(), setDebugListener(), and setTokenStream().</p>
<h3>void(* <code>ANTLR3_PARSER_struct::setDebugListener</code>)(struct <code>ANTLR3_PARSER_struct</code> *parser, <code>pANTLR3_DEBUG_EVENT_LISTENER</code> dbg)</h3>
<p>A pointer to a function that installs a debugger object (it also installs the debugging versions of the parser methods. This means that a non debug parser incurs no overhead because of the debugging stuff. </p>
<p> Referenced by antlr3ParserNew(), and antlr3ParserNewStreamDbg().</p>
<h3>void(* <code>ANTLR3_PARSER_struct::setTokenStream</code>)(struct <code>ANTLR3_PARSER_struct</code> *parser, <code>pANTLR3_TOKEN_STREAM</code>)</h3>
<p>A pointer to a function that installs a token stream for the parser. </p>
<p> Referenced by antlr3ParserNew(), and antlr3ParserNewStream().</p>
<h3>void* <code>ANTLR3_PARSER_struct::super</code></h3>
<p>All superstructure implementers of this interface require a pointer to their selves, which they can reference using the super pointer here.</p>
<h3><code>pANTLR3_TOKEN_STREAM</code> <code>ANTLR3_PARSER_struct::tstream</code></h3>
<p>A provider of a tokenstream interface, for the parser to consume tokens from. </p>
<p> Referenced by alreadyParsedRule(), antlr3RecognitionExceptionNew(), consumeUntil(), consumeUntilSet(), displayRecognitionError(), getTokenStream(), match(), matchAny(), memoize(), mismatch(), recover(), recoverFromMismatchedElement(), recoverFromMismatchedSet(), recoverFromMismatchedToken(), setDebugListener(), setTokenStream(), and synpred(). </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for ANTLR3C from the source code.</p>
