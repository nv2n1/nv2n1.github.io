---
title: "antlr3-ctnstream(3)"
name: "antlr3-ctnstream"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-ctnstream/"
description: "ANTLR3_TREE_PARSER_struct –"
---

<h2 class="name">NAME</h2>
<p> ANTLR3_TREE_PARSER_struct &#8211; </p>
<p> Internal structure representing an element in a hash bucket.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;<a href="file:/usr/include/antlr3treeparser.h">antlr3treeparser.h</a>&gt;</p>
<h3>Data Fields</h3>
<p> <code>pANTLR3_COMMON_TREE_NODE_STREAM</code> <code>ctnstream</code><br />
 <i>Pointer to the common tree node stream for the parser. </i><br />
 void(* <code>free</code> )(struct <code>ANTLR3_TREE_PARSER_struct</code> *parser)<br />
 <i>Pointer to a function that knows how to free resources of an ANTLR3 tree parser. </i><br />
 <code>pANTLR3_COMMON_TREE_NODE_STREAM</code>(* <code>getTreeNodeStream</code> )(struct <code>ANTLR3_TREE_PARSER_struct</code> *parser)<br />
 <i>Return a pointer to the input stream. </i><br />
 <code>pANTLR3_BASE_RECOGNIZER</code> <code>rec</code><br />
 <i>A pointer to the base recognizer, where most of the parser functions actually live because they are shared between parser and tree parser and this is the easier way than copying the interface all over the place. </i><br />
 void(* <code>setTreeNodeStream</code> )(struct <code>ANTLR3_TREE_PARSER_struct</code> *parser, <code>pANTLR3_COMMON_TREE_NODE_STREAM</code> input)<br />
 <i>Set the input stream and reset the parser. </i><br />
 void * <code>super</code><br />
 <i>Pointer to any super class. </i></p>
<h2>Detailed Description</h2>
<p> Internal structure representing an element in a hash bucket. </p>
<p> Stores the original key so that duplicate keys can be rejected if necessary, and contains function can be supported If the hash key could be unique I would have invented the perfect compression algorithm ;-)</p>
<h2>Field Documentation</h2>
<h3><code>pANTLR3_COMMON_TREE_NODE_STREAM</code> <code>ANTLR3_TREE_PARSER_struct::ctnstream</code></h3>
<p> Pointer to the common tree node stream for the parser. </p>
<p> Referenced by alreadyParsedRule(), antlr3RecognitionExceptionNew(), consumeUntil(), consumeUntilSet(), displayRecognitionError(), getTreeNodeStream(), match(), matchAny(), memoize(), recover(), recoverFromMismatchedElement(), recoverFromMismatchedSet(), recoverFromMismatchedToken(), setTreeNodeStream(), and synpred().</p>
<h3>void(* <code>ANTLR3_TREE_PARSER_struct::free</code>)(struct <code>ANTLR3_TREE_PARSER_struct</code> *parser)</h3>
<p> Pointer to a function that knows how to free resources of an ANTLR3 tree parser. </p>
<p> Referenced by antlr3ArboretumNew(), and antlr3TreeParserNewStream().</p>
<h3><code>pANTLR3_COMMON_TREE_NODE_STREAM</code>(* <code>ANTLR3_TREE_PARSER_struct::getTreeNodeStream</code>)(struct <code>ANTLR3_TREE_PARSER_struct</code> *parser)</h3>
<p> Return a pointer to the input stream. </p>
<p> Referenced by antlr3TreeParserNewStream().</p>
<h3><code>pANTLR3_BASE_RECOGNIZER</code> <code>ANTLR3_TREE_PARSER_struct::rec</code></h3>
<p> A pointer to the base recognizer, where most of the parser functions actually live because they are shared between parser and tree parser and this is the easier way than copying the interface all over the place. Macros hide this for the generated code so it is easier on the eye (though not the debugger ;-). </p>
<p> Referenced by antlr3TreeParserNewStream(), freeParser(), and setTreeNodeStream().</p>
<h3>void(* <code>ANTLR3_TREE_PARSER_struct::setTreeNodeStream</code>)(struct <code>ANTLR3_TREE_PARSER_struct</code> *parser, <code>pANTLR3_COMMON_TREE_NODE_STREAM</code> input)</h3>
<p> Set the input stream and reset the parser. </p>
<p> Referenced by antlr3TreeParserNewStream().</p>
<h3>void* <code>ANTLR3_TREE_PARSER_struct::super</code></h3>
<p> Pointer to any super class. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for ANTLR3C from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAM">Author</a></p>
<dd></dl>
