---
title: "antlr3-pantlr3_rewrite_rule_subtree_stream(3)"
name: "antlr3-pantlr3_rewrite_rule_subtree_stream"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-pantlr3_rewrite_rule_subtree_stream/"
description: "include/antlr3interfaces.h –"
---

<p>include/antlr3interfaces.h &#8211; </p>
<p> Declarations for all the antlr3 C runtime interfaces/classes.</p>
<h2>Synopsis</h2>
<h3>Typedefs</h3>
<p>typedef struct <code>ANTLR3_ARBORETUM_struct</code> * <code>pANTLR3_ARBORETUM</code><br />
 <i>Pointer to an instantiation of &#8216;class&#8217; </i><code>ANTLR3_ARBORETUM</code>.<br />
 typedef struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> * <code>pANTLR3_BASE_RECOGNIZER</code><br />
 <i>Pointer to an instantiation of the &#8216;class&#8217; </i><code>ANTLR3_BASE_RECOGNIZER</code>.<br />
 typedef struct <code>ANTLR3_BASE_TREE_struct</code> * <code>pANTLR3_BASE_TREE</code><br />
 <i>Pointer to an instantiation of &#8216;class&#8217; </i><code>ANTLR3_BASE_TREE</code>.<br />
 typedef struct <code>ANTLR3_BASE_TREE_ADAPTOR_struct</code> * <code>pANTLR3_BASE_TREE_ADAPTOR</code><br />
 <i>Pointer to an instantiation of &#8216;class&#8217; ANTLR3_BASE_TREE_ADAPTOR. </i><br />
 typedef struct <code>ANTLR3_BITSET_struct</code> * <code>pANTLR3_BITSET</code><br />
 <i>Pointer to an instantiation of &#8216;class&#8217; </i><code>ANTLR3_BITSET</code>.<br />
 typedef struct <code>ANTLR3_BITSET_LIST_struct</code> * <code>pANTLR3_BITSET_LIST</code><br />
 <i>Pointer to an instantiation of &#8216;class&#8217; </i><code>ANTLR3_BITSET_LIST</code>.<br />
 typedef struct <code>ANTLR3_COMMON_TOKEN_struct</code> * <code>pANTLR3_COMMON_TOKEN</code><br />
 <i>Pointer to an instantiation of &#8216;class&#8217; </i><code>ANTLR3_COMMON_TOKEN</code>.<br />
 typedef struct <code>ANTLR3_COMMON_TOKEN_STREAM_struct</code> * <code>pANTLR3_COMMON_TOKEN_STREAM</code><br />
 <i>Pointer to an instantiation of &#8216;class&#8217; </i><code>ANTLR3_COMMON_TOKEN_STREAM</code>.<br />
 typedef struct <code>ANTLR3_COMMON_TREE_struct</code> * <code>pANTLR3_COMMON_TREE</code><br />
 <i>Pointer to an instantiation of &#8216;class&#8217; </i><code>ANTLR3_COMMON_TREE</code>.<br />
 typedef struct <code>ANTLR3_COMMON_TREE_ADAPTOR_struct</code> * <code>pANTLR3_COMMON_TREE_ADAPTOR</code><br />
 <i>Pointer to an instantiation of &#8216;class&#8217; </i><code>ANTLR3_COMMON_TREE_ADAPTOR</code>.<br />
 typedef struct <code>ANTLR3_COMMON_TREE_NODE_STREAM_struct</code> * <code>pANTLR3_COMMON_TREE_NODE_STREAM</code><br />
 <i>Pointer to an instantiation of &#8216;class&#8217; </i><code>ANTLR3_COMMON_TREE_NODE_STREAM</code>.<br />
 typedef struct <code>ANTLR3_CYCLIC_DFA_struct</code> * <code>pANTLR3_CYCLIC_DFA</code><br />
 <i>Pointer to an instantiation of &#8216;class&#8217; </i><code>ANTLR3_CYCLIC_DFA</code>.<br />
 typedef struct <code>ANTLR3_DEBUG_EVENT_LISTENER_struct</code> * <code>pANTLR3_DEBUG_EVENT_LISTENER</code><br />
 <i>Pointer to an instantiation of &#8216;class&#8217; </i><code>ANTLR3_DEBUG_EVENT_LISTENER</code>.<br />
 typedef struct <code>ANTLR3_EXCEPTION_struct</code> * <code>pANTLR3_EXCEPTION</code><br />
 <i>Pointer to an instantiation of &#8216;class&#8217; </i><code>ANTLR3_EXCEPTION</code>.<br />
 typedef struct <code>ANTLR3_HASH_BUCKET_struct</code> * <code>pANTLR3_HASH_BUCKET</code><br />
 <i>Pointer to an instantiation of &#8216;class&#8217; </i><code>ANTLR3_HASH_BUCKET</code>.<br />
 typedef struct <code>ANTLR3_HASH_ENTRY_struct</code> * <code>pANTLR3_HASH_ENTRY</code><br />
 <i>Pointer to an instantiation of &#8216;class&#8217; </i><code>ANTLR3_HASH_ENTRY</code>.<br />
 typedef struct <code>ANTLR3_HASH_ENUM_struct</code> * <code>pANTLR3_HASH_ENUM</code><br />
 <i>Pointer to an instantiation of &#8216;class&#8217; </i><code>ANTLR3_HASH_ENUM</code>.<br />
 typedef struct <code>ANTLR3_HASH_TABLE_struct</code> * <code>pANTLR3_HASH_TABLE</code><br />
 <i>Pointer to an instantiation of &#8216;class&#8217; </i><code>ANTLR3_HASH_TABLE</code>.<br />
 typedef struct <code>ANTLR3_INPUT_STREAM_struct</code> * <code>pANTLR3_INPUT_STREAM</code><br />
 <i>Pointer to an instantiation of &#8216;class&#8217; </i><code>ANTLR3_INPUT_STREAM</code>.<br />
 typedef struct <code>ANTLR3_INT_STREAM_struct</code> * <code>pANTLR3_INT_STREAM</code> </p>
<p> typedef struct <code>ANTLR3_INT_TRIE_struct</code> * <code>pANTLR3_INT_TRIE</code><br />
 <i>Pointer to an instantiation of &#8216;class&#8217; </i><code>ANTLR3_INT_TRIE</code>.<br />
 typedef struct <code>ANTLR3_LEX_STATE_struct</code> * <code>pANTLR3_LEX_STATE</code><br />
 <i>Pointer to an instantiation of &#8216;class&#8217; </i><code>ANTLR3_LEX_STATE</code>.<br />
 typedef struct <code>ANTLR3_LEXER_struct</code> * <code>pANTLR3_LEXER</code><br />
 <i>Pointer to an instantiation of &#8216;class&#8217; </i><code>ANTLR3_LEXER</code>.<br />
 typedef struct <code>ANTLR3_LIST_struct</code> * <code>pANTLR3_LIST</code><br />
 <i>Pointer to an instantiation of &#8216;class&#8217; </i><code>ANTLR3_LIST</code>.<br />
 typedef struct <code>ANTLR3_PARSE_TREE_struct</code> * <code>pANTLR3_PARSE_TREE</code><br />
 <i>Pointer to an instantiation of &#8216;class&#8217; </i><code>ANTLR3_PARSE_TREE</code>.<br />
 typedef struct <code>ANTLR3_PARSER_struct</code> * <code>pANTLR3_PARSER</code><br />
 <i>Pointer to an instantiation of &#8216;class&#8217; </i><code>ANTLR3_PARSER</code>.<br />
 typedef struct <code>ANTLR3_RECOGNIZER_SHARED_STATE_struct</code> * <code>pANTLR3_RECOGNIZER_SHARED_STATE</code><br />
 <i>Pointer to an instantiation of &#8216;class&#8217; </i><code>ANTLR3_RECOGNIZER_SHARED_STATE</code>.<br />
 typedef struct <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct</code> * <code>pANTLR3_REWRITE_RULE_ELEMENT_STREAM</code><br />
 <i>Pointer to an instantiation of &#8216;class&#8217; </i><code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM</code>.<br />
 typedef struct <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct</code> * <code>pANTLR3_REWRITE_RULE_NODE_STREAM</code><br />
 <i>Pointer to an instantiation of &#8216;class&#8217; </i><code>ANTLR3_REWRITE_RULE_NODE_STREAM</code>.<br />
 typedef struct <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct</code> * <code>pANTLR3_REWRITE_RULE_SUBTREE_STREAM</code><br />
 <i>Pointer to an instantiation of &#8216;class&#8217; ANTLR3_REWRITE_RULE_SUBSTREE_STREAM. </i><br />
 typedef struct <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct</code> * <code>pANTLR3_REWRITE_RULE_TOKEN_STREAM</code><br />
 <i>Pointer to an instantiation of &#8216;class&#8217; </i><code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM</code>.<br />
 typedef struct <code>ANTLR3_STACK_struct</code> * <code>pANTLR3_STACK</code><br />
 <i>Pointer to an instantiation of &#8216;class&#8217; </i><code>ANTLR3_STACK</code>.<br />
 typedef struct <code>ANTLR3_STRING_struct</code> * <code>pANTLR3_STRING</code><br />
 <i>Pointer to an instantiation of &#8216;class&#8217; </i><code>ANTLR3_STRING</code>.<br />
 typedef struct <code>ANTLR3_STRING_FACTORY_struct</code> * <code>pANTLR3_STRING_FACTORY</code><br />
 <i>Pointer to an instantiation of &#8216;class&#8217; </i><code>ANTLR3_STRING_FACTORY</code>.<br />
 typedef struct <code>ANTLR3_TOKEN_FACTORY_struct</code> * <code>pANTLR3_TOKEN_FACTORY</code><br />
 <i>Pointer to an instantiation of &#8216;class&#8217; </i><code>ANTLR3_TOKEN_FACTORY</code>.<br />
 typedef struct <code>ANTLR3_TOKEN_SOURCE_struct</code> * <code>pANTLR3_TOKEN_SOURCE</code><br />
 <i>Pointer to an instantiation of &#8216;class&#8217; </i><code>ANTLR3_TOKEN_SOURCE</code>.<br />
 typedef struct <code>ANTLR3_TOKEN_STREAM_struct</code> * <code>pANTLR3_TOKEN_STREAM</code><br />
 <i>Pointer to an instantiation of &#8216;class&#8217; </i><code>ANTLR3_TOKEN_STREAM</code>.<br />
 typedef struct <code>ANTLR3_TOPO_struct</code> * <code>pANTLR3_TOPO</code><br />
 <i>Pointer to an instantiation of &#8216;class&#8217; </i><code>ANTLR3_TOPO</code>.<br />
 typedef struct <code>ANTLR3_TREE_NODE_STREAM_struct</code> * <code>pANTLR3_TREE_NODE_STREAM</code><br />
 <i>Pointer to an instantiation of &#8216;class&#8217; </i><code>ANTLR3_TREE_NODE_STREAM</code>.<br />
 typedef struct <code>ANTLR3_TREE_PARSER_struct</code> * <code>pANTLR3_TREE_PARSER</code><br />
 <i>Pointer to an instantiation of &#8216;class&#8217; </i><code>ANTLR3_TREE_PARSER</code>.<br />
 typedef struct <code>ANTLR3_TREE_WALK_STATE_struct</code> * <code>pANTLR3_TREE_WALK_STATE</code><br />
 <i>Pointer to an instantiation of &#8216;class&#8217; </i><code>ANTLR3_TREE_WALK_STATE</code>.<br />
 typedef struct <code>ANTLR3_VECTOR_struct</code> * <code>pANTLR3_VECTOR</code><br />
 <i>Pointer to an instantiation of &#8216;class&#8217; </i><code>ANTLR3_VECTOR</code>.<br />
 typedef struct <code>ANTLR3_VECTOR_FACTORY_struct</code> * <code>pANTLR3_VECTOR_FACTORY</code><br />
 <i>Pointer to an instantiation of &#8216;class&#8217; </i><code>ANTLR3_VECTOR_FACTORY</code>.</p>
<h2>Detailed Description</h2>
<p>Declarations for all the antlr3 C runtime interfaces/classes. </p>
<p> This allows the structures that define the interfaces to contain pointers to each other without trying to sort out the cyclic interdependencies that would otherwise result.</p>
<h2>Typedef Documentation</h2>
<h3>typedef struct <code>ANTLR3_BITSET_LIST_struct</code>* <code>pANTLR3_BITSET_LIST</code></h3>
<p>Pointer to an instantiation of &#8216;class&#8217; <code>ANTLR3_BITSET_LIST</code>.</p>
<h3>typedef struct <code>ANTLR3_INT_STREAM_struct</code>* <code>pANTLR3_INT_STREAM</code></h3>
<h3>typedef struct <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct</code>* <code>pANTLR3_REWRITE_RULE_NODE_STREAM</code></h3>
<p>Pointer to an instantiation of &#8216;class&#8217; <code>ANTLR3_REWRITE_RULE_NODE_STREAM</code>.</p>
<h3>typedef struct <code>ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct</code>* <code>pANTLR3_REWRITE_RULE_SUBTREE_STREAM</code></h3>
<p>Pointer to an instantiation of &#8216;class&#8217; ANTLR3_REWRITE_RULE_SUBSTREE_STREAM.</p>
<h3>typedef struct <code>ANTLR3_TOPO_struct</code>* <code>pANTLR3_TOPO</code></h3>
<p>Pointer to an instantiation of &#8216;class&#8217; <code>ANTLR3_TOPO</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for ANTLR3C from the source code.</p>
