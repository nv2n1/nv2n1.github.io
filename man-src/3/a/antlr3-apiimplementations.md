---
title: "antlr3-apiimplementations(3)"
name: "antlr3-apiimplementations"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-apiimplementations/"
description: "API Implementation functions –"
---

<h2 class="name">NAME</h2>
<p> API Implementation functions &#8211; </p>
<p> API implementation functions are the default implementation of each of the methods in a particular typedef structure.</p>
<h3>Modules</h3>
<p> <code>pANTLR3_BASE_RECOGNIZER Base Recognizer Implementation</code> </p>
<p> <i>The base recognizer interface is implemented by all higher level recognizers such as </i><code>pANTLR3_PARSER</code> and provides methods common to all recognizers.<br />
 <code>pANTLR3_RECOGNIZER_SHARED_STATE &#8211; Recognizer Shared State Implementation</code> </p>
<p> <i>The recognizer shared state class does not have an implementation because it contains only data fields, documented at </i><code>ANTLR3_RECOGNIZER_SHARED_STATE</code>.<br />
 <code>pANTLR3_BITSET &#8211; Bitset Implementation</code> </p>
<p> <code>pANTLR3_TOKEN_FACTORY &#8211; Token Factory Implementation</code> </p>
<p> <code>pANTLR3_COMMON_TOKEN &#8211; Common Token Implementation</code> </p>
<p> <code>pANTLR3_EXCEPTION &#8211; Exception Implementation</code> </p>
<p> <code>pANTLR3_HASH_BUCKET &#8211; Hash Table Bucket Implementation</code> </p>
<p> <code>pANTLR3_HASH_ENTRY &#8211; Hash Table Entry Implementation</code> </p>
<p> <code>pANTLR3_HASH_ENUM &#8211; Hash Table Enumerator Implementation</code> </p>
<p> <code>pANTLR3_HASH_TABLE &#8211; Hash Table Implementation</code> </p>
<p> <code>pANTLR3_LIST &#8211; List Implementation</code> </p>
<p> <code>pANTLR3_VECTOR_FACTORY &#8211; Vector Factory Implementation</code> </p>
<p> <code>pANTLR3_VECTOR &#8211; Vector Implementation</code> </p>
<p> <code>pANTLR3_STACK &#8211; Stack Implementation</code> </p>
<p> <code>pANTLR3_INPUT_STREAM &#8211; Input Stream Implementation</code> </p>
<p> <code>pANTLR3_LEX_STATE &#8211; Lexer State Implementation</code> </p>
<p> <code>pANTLR3_STRING_FACTORY &#8211; String Factory Implementation</code> </p>
<p> <code>pANTLR3_STRING &#8211; String Implementation</code> </p>
<p> <code>pANTLR3_TOKEN_SOURCE &#8211; Token Source Implementation</code> </p>
<p> <code>pANTLR3_TOKEN_STREAM &#8211; Token Stream Implementation</code> </p>
<p> <code>pANTLR3_COMMON_TOKEN_STREAM &#8211; Common Token Implementation</code> </p>
<p> <code>pANTLR3_CYCLIC_DFA &#8211; Cyclic DFA Implementation</code> </p>
<p> <code>pANTLR3_LEXER &#8211; Lexer Implementation</code> </p>
<p> <code>pANTLR3_PARSER &#8211; Parser Implementation</code> </p>
<p> <code>pANTLR3_BASE_TREE &#8211; Base Tree Implementation</code> </p>
<p> <code>pANTLR3_COMMON_TREE &#8211; Common Tree Implementation</code> </p>
<p> <code>pANTLR3_ARBORETUM &#8211; Tree Factory Implementation</code> </p>
<p> <code>pANTLR3_PARSE_TREE &#8211; Parse Tree Implementation</code> </p>
<p> <code>pANTLR3_TREE_NODE_STREAM &#8211; Tree Node Stream Implementation</code> </p>
<p> <code>pANTLR3_COMMON_TREE_NODE_STREAM &#8211; Common Tree Node Stream Implementation</code> </p>
<p> <code>pANTLR3_TREE_WALK_STATE &#8211; Tree Walk State Implementation</code> </p>
<p> <code>pANTLR3_BASE_TREE_ADAPTOR &#8211; Base Tree Adaptor Implementation</code> </p>
<p> <code>pANTLR3_COMMON_TREE_ADAPTOR &#8211; Common Tree Adaptor Implementation</code> </p>
<p> <code>pANTLR3_TREE_PARSER &#8211; Tree ParserImplementation</code> </p>
<p> <code>pANTLR3_INT_TRIE &#8211; Trie Implementation</code> </p>
<p> <code>pANTLR3_REWRITE_RULE_ELEMENT_STREAM &#8211; Token Rewrite Stream Implementation</code> </p>
<p> <code>pANTLR3_DEBUG_EVENT_LISTENER &#8211; Debugger Implementation</code> </p>
<h2>Detailed Description</h2>
<p> API implementation functions are the default implementation of each of the methods in a particular typedef structure. </p>
<p> They are generally grouped together in the same source code file. For instance the default implementations of the methods contained by a <code>pANTLR3_BASE_RECOGNIZER</code> will be found in the file <code>antlr3baserecognizer.c</code> </p>
<p> A source file that provides the default implementations of functions will usually also supply the public (exported from the .DLL or code library) &#8216;constructor&#8217; functions that create and initialize the typedef structure that they implement. For instance, in the <code>antlr3baserecognizer.c</code> file, you will find the function <code>antlr3BaseRecognizerNew()</code></p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for ANTLR3C from the source code. </p>
<h2>Index</h2>
