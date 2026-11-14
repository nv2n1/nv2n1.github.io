---
title: "antlr3_type_lexer(3)"
name: "antlr3_type_lexer"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3_type_lexer/"
description: "ANTLR3_BASE_RECOGNIZER – Base Recognizer Class Definition –"
---

<p>ANTLR3_BASE_RECOGNIZER &#8211; Base Recognizer Class Definition &#8211; </p>
<p> This is the definition of the base recognizer interface, instantiations of which are referred to via <code>pANTLR3_BASE_RECOGNIZER</code>.</p>
<h3>Data Structures</h3>
<p>struct <code>ANTLR3_BASE_RECOGNIZER_struct</code><br />
 <i>Base tracking context structure for all types of recognizers. </i></p>
<h3>Defines</h3>
<p>#define <code>ANTLR3_TYPE_LEXER</code> 0x0001<br />
 <i>Type indicator for a lexer recognizer. </i><br />
 #define <code>ANTLR3_TYPE_PARSER</code> 0x0002<br />
 <i>Type indicator for a parser recognizer. </i><br />
 #define <code>ANTLR3_TYPE_TREE_PARSER</code> 0x0004<br />
 <i>Type indicator for a tree parser recognizer. </i></p>
<h3>Typedefs</h3>
<p>typedef struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> <code>ANTLR3_BASE_RECOGNIZER</code><br />
 <i>Base tracking context structure for all types of recognizers. </i><br />
 typedef struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> * <code>pANTLR3_BASE_RECOGNIZER</code><br />
 <i>Pointer to an instantiation of the &#8216;class&#8217; </i><code>ANTLR3_BASE_RECOGNIZER</code>.</p>
<h2>Detailed Description</h2>
<p>This is the definition of the base recognizer interface, instantiations of which are referred to via <code>pANTLR3_BASE_RECOGNIZER</code>. </p>
<p> In general you will not refer to one of these structures directly as a a <code>pANTLR3_BASE_RECOGNIZER</code> will be embedded within a higher level object such as <code>pANTLR3_PARSER</code></p>
<h2>Define Documentation</h2>
<h3>#define ANTLR3_TYPE_LEXER 0x0001</h3>
<p>Type indicator for a lexer recognizer. </p>
<p> Referenced by alreadyParsedRule(), antlr3LexerNew(), antlr3RecognitionExceptionNew(), and memoize().</p>
<h3>#define ANTLR3_TYPE_PARSER 0x0002</h3>
<p>Type indicator for a parser recognizer. </p>
<p> Referenced by alreadyParsedRule(), antlr3ParserNew(), antlr3RecognitionExceptionNew(), antlr3TreeParserNewStream(), consumeUntil(), consumeUntilSet(), displayRecognitionError(), match(), matchAny(), memoize(), mismatch(), recover(), recoverFromMismatchedElement(), recoverFromMismatchedSet(), recoverFromMismatchedToken(), and synpred().</p>
<h3>#define ANTLR3_TYPE_TREE_PARSER 0x0004</h3>
<p>Type indicator for a tree parser recognizer. </p>
<p> Referenced by alreadyParsedRule(), antlr3RecognitionExceptionNew(), antlr3TreeParserNewStream(), consumeUntil(), consumeUntilSet(), displayRecognitionError(), match(), matchAny(), memoize(), recover(), recoverFromMismatchedElement(), recoverFromMismatchedSet(), recoverFromMismatchedToken(), and synpred().</p>
<h2>Typedef Documentation</h2>
<h3>typedef struct <code>ANTLR3_BASE_RECOGNIZER_struct</code></h3>
<p>&nbsp;<wbr>&nbsp;<wbr><code>ANTLR3_BASE_RECOGNIZER</code>&quot; </p>
<p> Base tracking context structure for all types of recognizers.</p>
<h3>typedef struct <code>ANTLR3_BASE_RECOGNIZER_struct</code>* <code>pANTLR3_BASE_RECOGNIZER</code></h3>
<p>Pointer to an instantiation of the &#8216;class&#8217; <code>ANTLR3_BASE_RECOGNIZER</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for ANTLR3C from the source code.</p>
