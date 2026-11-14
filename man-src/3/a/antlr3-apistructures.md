---
title: "antlr3-apistructures(3)"
name: "antlr3-apistructures"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-apistructures/"
description: "API Typedefs and Structs –"
---

<h2 class="name">NAME</h2>
<p> API Typedefs and Structs &#8211; </p>
<p> These structures (and the typedefs that you use to reference them and their pointers) are the C equivalent of objects.</p>
<h3>Data Structures</h3>
<p> struct <code>ANTLR3_INPUT_STREAM_struct</code><br />
 <i>Master context structure for an ANTLR3 C runtime based input stream. </i></p>
<h3>Modules</h3>
<p> <code>ANTLR3_BASE_RECOGNIZER &#8211; Base Recognizer Class Definition</code> </p>
<p> <i>This is the definition of the base recognizer interface, instantiations of which are referred to via </i><code>pANTLR3_BASE_RECOGNIZER</code>.<br />
 <code>ANTLR3_RECOGNIZER_SHARED_STATE Recognizer Shared State Class Definition</code> </p>
<p> <code>ANTLR3_BITSET &#8211; Bitset Class Definition</code> </p>
<p> <code>ANTLR3_TOKEN_FACTORY &#8211; Token Factory Class Definition</code> </p>
<p> <code>ANTLR3_COMMON_TOKEN &#8211; Common Token Class Definition</code> </p>
<p> <code>ANTLR3_EXCEPTION &#8211; Exception Class Definition</code> </p>
<p> <code>ANTLR3_HASH_BUCKET &#8211; Hash Table Bucket Class Definition</code> </p>
<p> <code>ANTLR3_HASH_ENTRY &#8211; Hash Table Entry Class Definition</code> </p>
<p> <code>ANTLR3_HASH_ENUM &#8211; Hash Table Enumerator Class Definition</code> </p>
<p> <code>ANTLR3_HASH_TABLE &#8211; Hash Table Class Definition</code> </p>
<p> <code>ANTLR3_LIST &#8211; List Class Definition</code> </p>
<p> <code>ANTLR3_VECTOR_FACTORY &#8211; Vector Factory Class Definition</code> </p>
<p> <code>ANTLR3_VECTOR &#8211; Vector Class Definition</code> </p>
<p> <code>ANTLR3_STACK &#8211; Stack Class Definition</code> </p>
<p> <code>ANTLR3_INPUT_STREAM &#8211; Input Stream Class Definition</code> </p>
<p> <code>ANTLR3_LEX_STATE &#8211; Lexer State Class Definition</code> </p>
<p> <code>ANTLR3_STRING_FACTORY &#8211; String Factory Class Definition</code> </p>
<p> <code>ANTLR3_STRING &#8211; String Class Definition</code> </p>
<p> <code>ANTLR3_TOKEN_SOURCE &#8211; Token Source Class Definition</code> </p>
<p> <code>ANTLR3_TOKEN_STREAM &#8211; Token Stream Class Definition</code> </p>
<p> <code>ANTLR3_COMMON_TOKEN_STREAM &#8211; Common Token Stream Class Definition</code> </p>
<p> <code>ANTLR3_CYCLIC_DFA &#8211; Cyclic DFA Class Definition</code> </p>
<p> <code>ANTLR3_LEXER &#8211; Lexer Class Definition</code> </p>
<p> <code>ANTLR3_PARSER &#8211; Parser Class Definition</code> </p>
<p> <code>ANTLR3_BASE_TREE &#8211; Base Tree Class Definition</code> </p>
<p> <code>ANTLR3_COMMON_TREE &#8211; Common Tree Class Definition</code> </p>
<p> <code>ANTLR3_ARBORETUM &#8211; Tree Factory Class Definition</code> </p>
<p> <code>ANTLR3_PARSE_TREE &#8211; Parse Tree Class Definition</code> </p>
<p> <code>ANTLR3_TREE_NODE_STREAM &#8211; Tree Node Class Definition</code> </p>
<p> <code>ANTLR3_COMMON_TREE_NODE_STREAM &#8211; Common Tree Node Class Definition</code> </p>
<p> <code>ANTLR3_TREE_WALK_STATE &#8211; Tree Walk State Class Definition</code> </p>
<p> <code>ANTLR3_BASE_TREE_ADAPTOR &#8211; Base Tree Class Definition</code> </p>
<p> <code>ANTLR3_COMMON_TREE_ADAPTOR &#8211; Common Tree Adaptor Class Definition</code> </p>
<p> <code>ANTLR3_TREE_PARSER &#8211; Tree Parser Class Definition</code> </p>
<p> <code>ANTLR3_INT_TRIE &#8211; Trie Class Definition</code> </p>
<p> <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM &#8211; Token Rewrite Stream Class Definition</code> </p>
<p> <code>ANTLR3_DEBUG_EVENT_LISTENER &#8211; Debugger Class Definition</code> </p>
<h3>Typedefs</h3>
<p> typedef struct <code>ANTLR3_INPUT_STREAM_struct</code> <code>ANTLR3_INPUT_STREAM</code><br />
 <i>Master context structure for an ANTLR3 C runtime based input stream. </i></p>
<h2>Detailed Description</h2>
<p> These structures (and the typedefs that you use to reference them and their pointers) are the C equivalent of objects. </p>
<p> They correspond (roughly) to the Java runtime system classes and contain all the data elements for a particular interface as well as all the pointers to functions that implement these interfaces. </p>
<p> There are constructor functions exported from the C runtime, which you use to create a default implementation of one of these &#8216;classes&#8217;. You can then override any part of the implementation by installing your own function pointers, before using the interface &#8216;object&#8217; you have created. </p>
<p> For instance, you can override the default error message reporting function by replacing the standard (example) implementation of this function with your own. In your grammar, you would place the following </p>
<pre><code>
@parser::apifuncs
{
    // Install custom error message display
    //
    RECOGNIZER-&gt;displayRecognitionError = produceError;
}
</code></pre>
<p> The special section apiFuncs is guaranteed to be generated after the RECONGIZER &#8216;object&#8217; has already be created and initialized, so you may install your own implementations of the <code>ANTLR3_BASE_RECOGNIZER</code> interface functions. The error display function is likely to be the only one you are interested in replacing. </p>
<p> Some typedef structures contain either pointers to &#8216;inherited&#8217; objects (usual) or embedded structures/typedefs (unusual). In some cases, the pointers passed around by the paresr or tree parser are actually the pointers to these embedded structures (such as <code>pANTLR3_BASE_TREE</code>), and these embedded &#8216;objects&#8217; contain pointers to their encapsulating objects. This is the equivalent of passing interface objects around in object oriented languages.</p>
<h2>Typedef Documentation</h2>
<h3>typedef struct <code>ANTLR3_INPUT_STREAM_struct</code></h3>
<p>&nbsp;<wbr>&nbsp;<wbr><code>ANTLR3_INPUT_STREAM</code>&quot; </p>
<p> Master context structure for an ANTLR3 C runtime based input stream.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for ANTLR3C from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAI">Author</a></p>
<dd></dl>
