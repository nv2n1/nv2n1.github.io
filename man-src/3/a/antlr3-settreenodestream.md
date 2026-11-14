---
title: "antlr3-settreenodestream(3)"
name: "antlr3-settreenodestream"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-settreenodestream/"
description: "src/antlr3treeparser.c –"
---

<p>src/antlr3treeparser.c &#8211; </p>
<p> Implementation of the tree parser and overrides for the base recognizer.</p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/antlr3treeparser.h">antlr3treeparser.h</a>&gt; </p>
<h3>Functions</h3>
<p>ANTLR3_API void <code>antlr3MTNExceptionNew</code> (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer)<br />
 <i>Creates a new Mismatched Tree Nde Exception and inserts in the recognizer exception stack. </i><br />
 ANTLR3_API <code>pANTLR3_TREE_PARSER</code> <code>antlr3TreeParserNewStream</code> (<code>ANTLR3_UINT32</code> sizeHint, <code>pANTLR3_COMMON_TREE_NODE_STREAM</code> ctnstream, <code>pANTLR3_RECOGNIZER_SHARED_STATE</code> state) </p>
<p> static void <code>freeParser</code> (<code>pANTLR3_TREE_PARSER</code> parser) </p>
<p> static void * <code>getCurrentInputSymbol</code> (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>pANTLR3_INT_STREAM</code> istream) </p>
<p> static void * <code>getMissingSymbol</code> (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>pANTLR3_INT_STREAM</code> istream, <code>pANTLR3_EXCEPTION</code> e, <code>ANTLR3_UINT32</code> expectedTokenType, <code>pANTLR3_BITSET_LIST</code> follow) </p>
<p> static <code>pANTLR3_COMMON_TREE_NODE_STREAM</code> <code>getTreeNodeStream</code> (<code>pANTLR3_TREE_PARSER</code> parser)<br />
 <i>Return a pointer to the input stream. </i><br />
 static void <code>mismatch</code> (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>ANTLR3_UINT32</code> ttype, <code>pANTLR3_BITSET_LIST</code> follow)<br />
 <i>Override for standard base recognizer mismatch function as we have DOWN/UP nodes in the stream that have no line info, plus we want to alter the exception type. </i><br />
 static void <code>setTreeNodeStream</code> (<code>pANTLR3_TREE_PARSER</code> parser, <code>pANTLR3_COMMON_TREE_NODE_STREAM</code> input)<br />
 <i>Set the input stream and reset the parser. </i></p>
<h2>Detailed Description</h2>
<p>Implementation of the tree parser and overrides for the base recognizer. </p>
<h2>Function Documentation</h2>
<h3>ANTLR3_API void antlr3MTNExceptionNew (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer)</h3>
<p>Creates a new Mismatched Tree Nde Exception and inserts in the recognizer exception stack. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>recognizer</i> Context pointer for this recognizer</dl>
<p> References ANTLR3_MISMATCHED_TREE_NODE_EXCEPTION, ANTLR3_MISMATCHED_TREE_NODE_NAME, antlr3RecognitionExceptionNew(), ANTLR3_RECOGNIZER_SHARED_STATE_struct::exception, ANTLR3_EXCEPTION_struct::name, ANTLR3_BASE_RECOGNIZER_struct::state, and ANTLR3_EXCEPTION_struct::type. </p>
<p> Referenced by antlr3TreeParserNewStream().</p>
<h3>ANTLR3_API <code>pANTLR3_TREE_PARSER</code> antlr3TreeParserNewStream (<code>ANTLR3_UINT32</code> sizeHint, <code>pANTLR3_COMMON_TREE_NODE_STREAM</code> ctnstream, <code>pANTLR3_RECOGNIZER_SHARED_STATE</code> state)</h3>
<p>Allocate tree parser memory </p>
<p> References ANTLR3_MALLOC, ANTLR3_TYPE_PARSER, ANTLR3_TYPE_TREE_PARSER, antlr3BaseRecognizerNew(), antlr3MTNExceptionNew(), ANTLR3_BASE_RECOGNIZER_struct::exConstruct, ANTLR3_TREE_PARSER_struct::free, freeParser(), getCurrentInputSymbol(), ANTLR3_BASE_RECOGNIZER_struct::getCurrentInputSymbol, getMissingSymbol(), ANTLR3_BASE_RECOGNIZER_struct::getMissingSymbol, getTreeNodeStream(), ANTLR3_TREE_PARSER_struct::getTreeNodeStream, mismatch(), ANTLR3_BASE_RECOGNIZER_struct::mismatch, ANTLR3_TREE_PARSER_struct::rec, setTreeNodeStream(), ANTLR3_TREE_PARSER_struct::setTreeNodeStream, ANTLR3_BASE_RECOGNIZER_struct::super, and ANTLR3_BASE_RECOGNIZER_struct::type.</p>
<h3>static void freeParser (<code>pANTLR3_TREE_PARSER</code> parser) [static]</h3>
<p>References ANTLR3_FREE, ANTLR3_RECOGNIZER_SHARED_STATE_struct::following, ANTLR3_BASE_RECOGNIZER_struct::free, ANTLR3_STACK_struct::free, ANTLR3_TREE_PARSER_struct::rec, and ANTLR3_BASE_RECOGNIZER_struct::state. </p>
<p> Referenced by antlr3TreeParserNewStream().</p>
<h3>static void * getCurrentInputSymbol (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>pANTLR3_INT_STREAM</code> istream) [static]</h3>
<p>References ANTLR3_TREE_NODE_STREAM_struct::_LT, ANTLR3_TREE_NODE_STREAM_struct::ctns, and ANTLR3_INT_STREAM_struct::super. </p>
<p> Referenced by antlr3TreeParserNewStream().</p>
<h3>static void * getMissingSymbol (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>pANTLR3_INT_STREAM</code> istream, <code>pANTLR3_EXCEPTION</code> e, <code>ANTLR3_UINT32</code> expectedTokenType, <code>pANTLR3_BITSET_LIST</code> follow) [static]</h3>
<p>References ANTLR3_TREE_NODE_STREAM_struct::_LT, ANTLR3_STRING_struct::append8, ANTLR3_COMMON_TREE_struct::baseTree, ANTLR3_TREE_NODE_STREAM_struct::ctns, ANTLR3_BASE_TREE_struct::dupNode, ANTLR3_COMMON_TREE_NODE_STREAM_struct::EOF_NODE, ANTLR3_COMMON_TOKEN_struct::getText, ANTLR3_BASE_TREE_struct::getToken, ANTLR3_COMMON_TOKEN_struct::setText8, ANTLR3_BASE_RECOGNIZER_struct::state, ANTLR3_BASE_TREE_struct::super, ANTLR3_INT_STREAM_struct::super, and ANTLR3_RECOGNIZER_SHARED_STATE_struct::tokenNames. </p>
<p> Referenced by antlr3TreeParserNewStream().</p>
<h3>static <code>pANTLR3_COMMON_TREE_NODE_STREAM</code> getTreeNodeStream (<code>pANTLR3_TREE_PARSER</code> parser) [static]</h3>
<p>Return a pointer to the input stream. </p>
<p> References ANTLR3_TREE_PARSER_struct::ctnstream. </p>
<p> Referenced by antlr3TreeParserNewStream().</p>
<h3>static void mismatch (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>ANTLR3_UINT32</code> ttype, <code>pANTLR3_BITSET_LIST</code> follow) [static]</h3>
<p>Override for standard base recognizer mismatch function as we have DOWN/UP nodes in the stream that have no line info, plus we want to alter the exception type. </p>
<p> References ANTLR3_BASE_RECOGNIZER_struct::exConstruct, and ANTLR3_BASE_RECOGNIZER_struct::recoverFromMismatchedToken. </p>
<p> Referenced by antlr3TreeParserNewStream().</p>
<h3>static void setTreeNodeStream (<code>pANTLR3_TREE_PARSER</code> parser, <code>pANTLR3_COMMON_TREE_NODE_STREAM</code> input) [static]</h3>
<p>Set the input stream and reset the parser. </p>
<p> References ANTLR3_TREE_PARSER_struct::ctnstream, ANTLR3_TREE_PARSER_struct::rec, ANTLR3_COMMON_TREE_NODE_STREAM_struct::reset, and ANTLR3_BASE_RECOGNIZER_struct::reset. </p>
<p> Referenced by antlr3TreeParserNewStream().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for ANTLR3C from the source code.</p>
