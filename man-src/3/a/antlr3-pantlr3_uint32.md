---
title: "antlr3-pantlr3_uint32(3)"
name: "antlr3-pantlr3_uint32"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-pantlr3_uint32/"
description: "include/antlr3defs.h –"
---

<p>include/antlr3defs.h &#8211; </p>
<p> Basic type and constant definitions for ANTLR3 Runtime.</p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/antlr3errors.h">antlr3errors.h</a>&gt;<br />
 #include &lt;<a href="file:/usr/include/antlr3config.h">antlr3config.h</a>&gt;<br />
 #include &lt;<a href="file:/usr/include/stdio.h">stdio.h</a>&gt;<br />
 #include &lt;<a href="file:/usr/include/antlr3interfaces.h">antlr3interfaces.h</a>&gt;<br />
 #include &lt;<a href="file:/usr/include/antlr3convertutf.h">antlr3convertutf.h</a>&gt; </p>
<h3>Defines</h3>
<p>#define <code>_stat</code> stat </p>
<p> #define <code>ANTLR3_API</code> </p>
<p> #define <code>ANTLR3_API</code> </p>
<p> #define <code>ANTLR3_AVERAGE</code> </p>
<p> #define <code>ANTLR3_CALLOC</code>(numEl, elSize) calloc (numEl, (size_t)(elSize))<br />
 <i>Default definition of ANTLR3_CALLOC. </i><br />
 #define <code>ANTLR3_CDECL</code> </p>
<p> #define <code>ANTLR3_CLOSESOCKET</code> close </p>
<p> #define <code>ANTLR3_ENCODING_LATIN1</code> 0 </p>
<p> #define <code>ANTLR3_ENCODING_UCS2</code> 1 </p>
<p> #define <code>ANTLR3_ENCODING_UTF32</code> 3 </p>
<p> #define <code>ANTLR3_ENCODING_UTF8</code> 2 </p>
<p> #define <code>ANTLR3_FASTCALL</code> </p>
<p> #define <code>ANTLR3_FPRINTF</code> fprintf<br />
 <i>Default definition of fprintf, set this to something other than fprintf before including </i><code>antlr3.h</code> if your system does not have a fprintf.<br />
 #define <code>ANTLR3_FREE</code>(ptr) free ((void *)(ptr))<br />
 <i>Default definition of ANTLR3_FREE. </i><br />
 #define <code>ANTLR3_FREE_FUNC</code> free<br />
 <i>Default definition of ANTLR3_FREE_FUNC . </i><br />
 #define <code>ANTLR3_FUNC_PTR</code>(ptr) (void *)((<code>ANTLR3_UINT32</code>)(ptr)) </p>
<p> #define <code>ANTLR3_INLINE</code> inline </p>
<p> #define <code>ANTLR3_LIST_SIZE_HINT</code> 63 </p>
<p> #define <code>ANTLR3_MALLOC</code>(request) malloc ((size_t)(request))<br />
 <i>Default definition of ANTLR3_MALLOC. </i><br />
 #define <code>ANTLR3_MEMCPY</code>(target, source, size) memcpy((void *)(target), (const void *)(source), (size_t)(size))<br />
 <i>Default definition of ANTLR3_MEMCPY. </i><br />
 #define <code>ANTLR3_MEMMOVE</code>(target, source, size) memmove((void *)(target), (const void *)(source), (size_t)(size))<br />
 <i>Default definition of ANTLR3_MEMMOVE. </i><br />
 #define <code>ANTLR3_MEMSET</code>(target, byte, size) memset((void *)(target), (int)(byte), (size_t)(size))<br />
 <i>Default definition of ANTLR3_MEMSET. </i><br />
 #define <code>ANTLR3_PRINTF</code> printf<br />
 <i>Default definition of printf, set this to something other than printf before including </i><code>antlr3.h</code> if your system does not have a printf.<br />
 #define <code>ANTLR3_REALLOC</code>(current, request) realloc ((void *)(current), (size_t)(request))<br />
 <i>Default definition of ANTLR3_REALLOC. </i><br />
 #define <code>ANTLR3_SIZE_HINT</code> 1025 </p>
<p> #define <code>ANTLR3_STRDUP</code>(instr) (<code>pANTLR3_UINT8</code>)(strdup ((const char *)(instr)))<br />
 <i>Default definition of ANTLR3_STRDUP. </i><br />
 #define <code>ANTLR3_TRIE_DEPTH</code> 31 </p>
<p> #define <code>ANTLR3_UINT32_CAST</code>(ptr) (<code>ANTLR3_UINT32</code>)(ptr) </p>
<p> #define <code>ANTLR3_UINT64_CAST</code>(ptr) (<code>ANTLR3_UINT64</code>)((<code>ANTLR3_UINT32</code>)(ptr)) </p>
<p> #define <code>ANTLR3_UINT64_LIT</code>(lit) lit##ULL </p>
<p> #define <code>INVALID_SOCKET</code> ((<code>SOCKET</code>)-1) </p>
<h3>Typedefs</h3>
<p>typedef uint64_t <code>ANTLR3_BITWORD</code> </p>
<p> typedef uint32_t <code>ANTLR3_BOOLEAN</code> </p>
<p> typedef int32_t <code>ANTLR3_CHAR</code> </p>
<p> typedef FILE * <code>ANTLR3_FDSC</code> </p>
<p> typedef struct stat <code>ANTLR3_FSTAT_STRUCT</code> </p>
<p> typedef int16_t <code>ANTLR3_INT16</code> </p>
<p> typedef int32_t <code>ANTLR3_INT32</code> </p>
<p> typedef int64_t <code>ANTLR3_INT64</code> </p>
<p> typedef int8_t <code>ANTLR3_INT8</code> </p>
<p> typedef <code>ANTLR3_UINT32</code> <code>ANTLR3_INTKEY</code> </p>
<p> typedef <code>ANTLR3_INT32</code> <code>ANTLR3_MARKER</code> </p>
<p> typedef size_t <code>ANTLR3_SALENT</code> </p>
<p> typedef struct sockaddr_in <code>ANTLR3_SOCKADDRT</code> </p>
<p> typedef uint32_t <code>ANTLR3_UCHAR</code> </p>
<p> typedef uint16_t <code>ANTLR3_UINT16</code> </p>
<p> typedef uint32_t <code>ANTLR3_UINT32</code> </p>
<p> typedef uint64_t <code>ANTLR3_UINT64</code> </p>
<p> typedef uint8_t <code>ANTLR3_UINT8</code> </p>
<p> typedef uint64_t * <code>pANTLR3_BITWORD</code> </p>
<p> typedef uint32_t * <code>pANTLR3_BOOLEAN</code> </p>
<p> typedef int32_t * <code>pANTLR3_CHAR</code> </p>
<p> typedef int16_t * <code>pANTLR3_INT16</code> </p>
<p> typedef int32_t * <code>pANTLR3_INT32</code> </p>
<p> typedef int64_t * <code>pANTLR3_INT64</code> </p>
<p> typedef int8_t * <code>pANTLR3_INT8</code> </p>
<p> typedef struct sockaddr * <code>pANTLR3_SOCKADDRC</code> </p>
<p> typedef struct sockaddr_in * <code>pANTLR3_SOCKADDRT</code> </p>
<p> typedef uint32_t * <code>pANTLR3_UCHAR</code> </p>
<p> typedef uint16_t * <code>pANTLR3_UINT16</code> </p>
<p> typedef uint32_t * <code>pANTLR3_UINT32</code> </p>
<p> typedef uint64_t * <code>pANTLR3_UINT64</code> </p>
<p> typedef uint8_t * <code>pANTLR3_UINT8</code> </p>
<p> typedef int <code>SOCKET</code> </p>
<h3>Functions</h3>
<p>ANTLR3_API <code>pANTLR3_BASE_TREE_ADAPTOR</code> <code>ANTLR3_TREE_ADAPTORDebugNew</code> (<code>pANTLR3_STRING_FACTORY</code> strFactory, <code>pANTLR3_DEBUG_EVENT_LISTENER</code> debugger)<br />
 <i>Debugging version of the tree adaptor (not normally called as generated code calls setDebugEventListener instead which changes a normal token stream to a debugging stream and means that a user&#8217;s instantiation code does not need to be changed just to debug with AW. </i><br />
 ANTLR3_API <code>pANTLR3_BASE_TREE_ADAPTOR</code> <code>ANTLR3_TREE_ADAPTORNew</code> (<code>pANTLR3_STRING_FACTORY</code> strFactory)<br />
 <i>Create a new tree adaptor. </i><br />
 ANTLR3_API <code>pANTLR3_ARBORETUM</code> <code>antlr3ArboretumNew</code> (<code>pANTLR3_STRING_FACTORY</code> factory) </p>
<p> ANTLR3_API <code>pANTLR3_INPUT_STREAM</code> <code>antlr3AsciiFileStreamNew</code> (<code>pANTLR3_UINT8</code> fileName)<br />
 <i>Use the contents of an operating system file as the input for an input stream. </i><br />
 ANTLR3_API <code>pANTLR3_BASE_RECOGNIZER</code> <code>antlr3BaseRecognizerNew</code> (<code>ANTLR3_UINT32</code> type, <code>ANTLR3_UINT32</code> sizeHint, <code>pANTLR3_RECOGNIZER_SHARED_STATE</code> state) </p>
<p> ANTLR3_API void <code>antlr3BaseTreeAdaptorInit</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_DEBUG_EVENT_LISTENER</code> debugger)<br />
 <i>Given a pointer to a base tree adaptor structure (which is usually embedded in the super class the implements the tree adaptor used in the parse), initialize its function pointers and so on. </i><br />
 ANTLR3_API <code>pANTLR3_BASE_TREE</code> <code>antlr3BaseTreeNew</code> (<code>pANTLR3_BASE_TREE</code> tree) </p>
<p> ANTLR3_API <code>pANTLR3_BITSET</code> <code>antlr3BitsetCopy</code> (<code>pANTLR3_BITSET_LIST</code> blist) </p>
<p> ANTLR3_API <code>pANTLR3_BITSET</code> <code>antlr3BitsetList</code> (<code>pANTLR3_HASH_TABLE</code> list) </p>
<p> ANTLR3_API <code>pANTLR3_BITSET</code> <code>antlr3BitsetLoad</code> (<code>pANTLR3_BITSET_LIST</code> blist)<br />
 <i>Creates a new bitset with at least one 64 bit bset of bits, but as many 64 bit sets as are required. </i><br />
 ANTLR3_API <code>pANTLR3_BITSET</code> <code>antlr3BitsetNew</code> (<code>ANTLR3_UINT32</code> numBits) </p>
<p> ANTLR3_API <code>pANTLR3_BITSET</code> <code>antlr3BitsetOf</code> (<code>ANTLR3_INT32</code> bit,&#8230;)<br />
 <i>Creates a new bitset with at least one element, but as many elements are required. </i><br />
 ANTLR3_API void <code>antlr3BitsetSetAPI</code> (<code>pANTLR3_BITSET</code> bitset) </p>
<p> ANTLR3_API <code>ANTLR3_UCHAR</code> <code>antlr3c8toAntlrc</code> (<code>ANTLR3_INT8</code> inc)<br />
 <i>Provides basic utility functions to convert between the various Unicode character conversions. </i><br />
 ANTLR3_API <code>pANTLR3_COMMON_TOKEN_STREAM</code> <code>antlr3CommonTokenDebugStreamSourceNew</code> (<code>ANTLR3_UINT32</code> hint, <code>pANTLR3_TOKEN_SOURCE</code> source, <code>pANTLR3_DEBUG_EVENT_LISTENER</code> debugger) </p>
<p> ANTLR3_API <code>pANTLR3_COMMON_TOKEN</code> <code>antlr3CommonTokenNew</code> (<code>ANTLR3_UINT32</code> ttype) </p>
<p> ANTLR3_API <code>pANTLR3_COMMON_TOKEN_STREAM</code> <code>antlr3CommonTokenStreamNew</code> (<code>ANTLR3_UINT32</code> hint) </p>
<p> ANTLR3_API <code>pANTLR3_COMMON_TOKEN_STREAM</code> <code>antlr3CommonTokenStreamSourceNew</code> (<code>ANTLR3_UINT32</code> hint, <code>pANTLR3_TOKEN_SOURCE</code> source) </p>
<p> ANTLR3_API <code>pANTLR3_COMMON_TREE</code> <code>antlr3CommonTreeNew</code> (void) </p>
<p> ANTLR3_API <code>pANTLR3_COMMON_TREE</code> <code>antlr3CommonTreeNewFromToken</code> (<code>pANTLR3_COMMON_TOKEN</code> tree) </p>
<p> ANTLR3_API <code>pANTLR3_COMMON_TREE</code> <code>antlr3CommonTreeNewFromTree</code> (<code>pANTLR3_COMMON_TREE</code> tree) </p>
<p> ANTLR3_API <code>pANTLR3_COMMON_TREE_NODE_STREAM</code> <code>antlr3CommonTreeNodeStreamNew</code> (<code>pANTLR3_STRING_FACTORY</code> strFactory, <code>ANTLR3_UINT32</code> hint) </p>
<p> ANTLR3_API <code>pANTLR3_COMMON_TREE_NODE_STREAM</code> <code>antlr3CommonTreeNodeStreamNewStream</code> (<code>pANTLR3_COMMON_TREE_NODE_STREAM</code> inStream) </p>
<p> ANTLR3_API <code>pANTLR3_COMMON_TREE_NODE_STREAM</code> <code>antlr3CommonTreeNodeStreamNewTree</code> (<code>pANTLR3_BASE_TREE</code> tree, <code>ANTLR3_UINT32</code> hint) </p>
<p> ANTLR3_API <code>pANTLR3_DEBUG_EVENT_LISTENER</code> <code>antlr3DebugListenerNew</code> ()<br />
 <i>Create and initialize a new debug event listener that can be connected to by ANTLRWorks and any other debugger via a socket. </i><br />
 ANTLR3_API <code>ANTLR3_INT32</code> <code>antlr3dfapredict</code> (void *ctx, <code>pANTLR3_BASE_RECOGNIZER</code> rec, <code>pANTLR3_INT_STREAM</code> is, <code>pANTLR3_CYCLIC_DFA</code> cdfa)<br />
 <i>From the input stream, predict what alternative will succeed using this DFA (representing the covering regular approximation to the underlying CFL). </i><br />
 ANTLR3_API <code>ANTLR3_INT32</code> <code>antlr3dfaspecialStateTransition</code> (void *ctx, <code>pANTLR3_BASE_RECOGNIZER</code> rec, <code>pANTLR3_INT_STREAM</code> is, <code>pANTLR3_CYCLIC_DFA</code> dfa, <code>ANTLR3_INT32</code> s)<br />
 <i>Default special state implementation. </i><br />
 ANTLR3_API <code>ANTLR3_INT32</code> <code>antlr3dfaspecialTransition</code> (void *ctx, <code>pANTLR3_BASE_RECOGNIZER</code> rec, <code>pANTLR3_INT_STREAM</code> is, <code>pANTLR3_CYCLIC_DFA</code> dfa, <code>ANTLR3_INT32</code> s) </p>
<p> ANTLR3_API <code>pANTLR3_HASH_ENUM</code> <code>antlr3EnumNew</code> (<code>pANTLR3_HASH_TABLE</code> table)<br />
 <i>Creates an enumeration structure to traverse the hash table. </i><br />
 ANTLR3_API <code>pANTLR3_EXCEPTION</code> <code>antlr3ExceptionNew</code> (<code>ANTLR3_UINT32</code> exception, void *name, void *message, <code>ANTLR3_BOOLEAN</code> freeMessage)<br />
 <i>Creates a new ANTLR3 exception structure. </i><br />
 ANTLR3_API <code>ANTLR3_UINT32</code> <code>antlr3Hash</code> (void *key, <code>ANTLR3_UINT32</code> keylen)<br />
 <i>Given an input key of arbitrary length, return a hash value of it. </i><br />
 ANTLR3_API <code>pANTLR3_HASH_TABLE</code> <code>antlr3HashTableNew</code> (<code>ANTLR3_UINT32</code> sizeHint) </p>
<p> ANTLR3_API <code>pANTLR3_INT_STREAM</code> <code>antlr3IntStreamNew</code> (void) </p>
<p> ANTLR3_API <code>pANTLR3_INT_TRIE</code> <code>antlr3IntTrieNew</code> (<code>ANTLR3_UINT32</code> depth) </p>
<p> ANTLR3_API <code>pANTLR3_LEXER</code> <code>antlr3LexerNew</code> (<code>ANTLR3_UINT32</code> sizeHint, <code>pANTLR3_RECOGNIZER_SHARED_STATE</code> state) </p>
<p> ANTLR3_API <code>pANTLR3_LEXER</code> <code>antlr3LexerNewStream</code> (<code>ANTLR3_UINT32</code> sizeHint, <code>pANTLR3_INPUT_STREAM</code> input, <code>pANTLR3_RECOGNIZER_SHARED_STATE</code> state) </p>
<p> ANTLR3_API <code>pANTLR3_LIST</code> <code>antlr3ListNew</code> (<code>ANTLR3_UINT32</code> sizeHint) </p>
<p> ANTLR3_API void <code>antlr3MTExceptionNew</code> (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer)<br />
 <i>Creates a new Mismatched Token Exception and inserts in the recognizer exception stack. </i><br />
 ANTLR3_API void <code>antlr3MTNExceptionNew</code> (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer)<br />
 <i>Creates a new Mismatched Tree Nde Exception and inserts in the recognizer exception stack. </i><br />
 ANTLR3_API <code>pANTLR3_INPUT_STREAM</code> <code>antlr3NewAsciiStringCopyStream</code> (<code>pANTLR3_UINT8</code> inString, <code>ANTLR3_UINT32</code> size, <code>pANTLR3_UINT8</code> name)<br />
 <i>Create an ASCII string stream as input to ANTLR 3, copying the input string. </i><br />
 ANTLR3_API <code>pANTLR3_INPUT_STREAM</code> <code>antlr3NewAsciiStringInPlaceStream</code> (<code>pANTLR3_UINT8</code> inString, <code>ANTLR3_UINT32</code> size, <code>pANTLR3_UINT8</code> name)<br />
 <i>Create an in-place ASCII string stream as input to ANTLR 3. </i><br />
 ANTLR3_API <code>pANTLR3_INPUT_STREAM</code> <code>antlr3NewUCS2StringInPlaceStream</code> (<code>pANTLR3_UINT16</code> inString, <code>ANTLR3_UINT32</code> size, <code>pANTLR3_UINT16</code> name)<br />
 <i>Create an in-place UCS2 string stream as input to ANTLR 3. </i><br />
 ANTLR3_API <code>pANTLR3_PARSER</code> <code>antlr3ParserNew</code> (<code>ANTLR3_UINT32</code> sizeHint, <code>pANTLR3_RECOGNIZER_SHARED_STATE</code> state) </p>
<p> ANTLR3_API <code>pANTLR3_PARSER</code> <code>antlr3ParserNewStream</code> (<code>ANTLR3_UINT32</code> sizeHint, <code>pANTLR3_TOKEN_STREAM</code> tstream, <code>pANTLR3_RECOGNIZER_SHARED_STATE</code> state) </p>
<p> ANTLR3_API <code>pANTLR3_PARSER</code> <code>antlr3ParserNewStreamDbg</code> (<code>ANTLR3_UINT32</code> sizeHint, <code>pANTLR3_TOKEN_STREAM</code> tstream, <code>pANTLR3_DEBUG_EVENT_LISTENER</code> dbg, <code>pANTLR3_RECOGNIZER_SHARED_STATE</code> state) </p>
<p> ANTLR3_API void <code>antlr3RecognitionExceptionNew</code> (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer) </p>
<p> ANTLR3_API <code>pANTLR3_REWRITE_RULE_NODE_STREAM</code> <code>antlr3RewriteRuleNODEStreamNewAE</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_RECOGNIZER</code> rec, <code>pANTLR3_UINT8</code> description) </p>
<p> ANTLR3_API <code>pANTLR3_REWRITE_RULE_NODE_STREAM</code> <code>antlr3RewriteRuleNODEStreamNewAEE</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_RECOGNIZER</code> rec, <code>pANTLR3_UINT8</code> description, void *oneElement) </p>
<p> ANTLR3_API <code>pANTLR3_REWRITE_RULE_NODE_STREAM</code> <code>antlr3RewriteRuleNODEStreamNewAEV</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_RECOGNIZER</code> rec, <code>pANTLR3_UINT8</code> description, <code>pANTLR3_VECTOR</code> vector) </p>
<p> ANTLR3_API <code>pANTLR3_REWRITE_RULE_SUBTREE_STREAM</code> <code>antlr3RewriteRuleSubtreeStreamNewAE</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_RECOGNIZER</code> rec, <code>pANTLR3_UINT8</code> description) </p>
<p> ANTLR3_API <code>pANTLR3_REWRITE_RULE_SUBTREE_STREAM</code> <code>antlr3RewriteRuleSubtreeStreamNewAEE</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_RECOGNIZER</code> rec, <code>pANTLR3_UINT8</code> description, void *oneElement) </p>
<p> ANTLR3_API <code>pANTLR3_REWRITE_RULE_SUBTREE_STREAM</code> <code>antlr3RewriteRuleSubtreeStreamNewAEV</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_RECOGNIZER</code> rec, <code>pANTLR3_UINT8</code> description, <code>pANTLR3_VECTOR</code> vector) </p>
<p> ANTLR3_API <code>pANTLR3_REWRITE_RULE_TOKEN_STREAM</code> <code>antlr3RewriteRuleTOKENStreamNewAE</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_RECOGNIZER</code> rec, <code>pANTLR3_UINT8</code> description) </p>
<p> ANTLR3_API <code>pANTLR3_REWRITE_RULE_TOKEN_STREAM</code> <code>antlr3RewriteRuleTOKENStreamNewAEE</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_RECOGNIZER</code> rec, <code>pANTLR3_UINT8</code> description, void *oneElement) </p>
<p> ANTLR3_API <code>pANTLR3_REWRITE_RULE_TOKEN_STREAM</code> <code>antlr3RewriteRuleTOKENStreamNewAEV</code> (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_RECOGNIZER</code> rec, <code>pANTLR3_UINT8</code> description, <code>pANTLR3_VECTOR</code> vector) </p>
<p> ANTLR3_API void <code>antlr3SetCTAPI</code> (<code>pANTLR3_COMMON_TREE</code> tree) </p>
<p> ANTLR3_API void <code>antlr3SetTokenAPI</code> (<code>pANTLR3_COMMON_TOKEN</code> token) </p>
<p> ANTLR3_API void <code>antlr3SetVectorApi</code> (<code>pANTLR3_VECTOR</code> vector, <code>ANTLR3_UINT32</code> sizeHint) </p>
<p> ANTLR3_API <code>pANTLR3_STACK</code> <code>antlr3StackNew</code> (<code>ANTLR3_UINT32</code> sizeHint) </p>
<p> ANTLR3_API <code>pANTLR3_STRING_FACTORY</code> <code>antlr3StringFactoryNew</code> (void) </p>
<p> ANTLR3_API <code>pANTLR3_TOKEN_FACTORY</code> <code>antlr3TokenFactoryNew</code> (<code>pANTLR3_INPUT_STREAM</code> input) </p>
<p> ANTLR3_API <code>pANTLR3_TOPO</code> <code>antlr3TopoNew</code> ()<br />
 <i>Allocate and initialize a new ANTLR3 topological sorter, which can be used to define edges that identify numerical node indexes that depend on other numerical node indexes, which can then be sorted topologically such that any node is sorted after all its dependent nodes. </i><br />
 ANTLR3_API <code>pANTLR3_TREE_NODE_STREAM</code> <code>antlr3TreeNodeStreamNew</code> () </p>
<p> ANTLR3_API <code>pANTLR3_TREE_PARSER</code> <code>antlr3TreeParserNewStream</code> (<code>ANTLR3_UINT32</code> sizeHint, <code>pANTLR3_COMMON_TREE_NODE_STREAM</code> ctnstream, <code>pANTLR3_RECOGNIZER_SHARED_STATE</code> state) </p>
<p> ANTLR3_API <code>pANTLR3_STRING_FACTORY</code> <code>antlr3UCS2StringFactoryNew</code> (void)<br />
 <i>Create a string factory that is UCS2 (16 bit) encoding based. </i><br />
 ANTLR3_API <code>pANTLR3_COMMON_TREE_NODE_STREAM</code> <code>antlr3UnbufTreeNodeStreamNew</code> (<code>pANTLR3_STRING_FACTORY</code> strFactory, <code>ANTLR3_UINT32</code> hint) </p>
<p> ANTLR3_API <code>pANTLR3_COMMON_TREE_NODE_STREAM</code> <code>antlr3UnbufTreeNodeStreamNewTree</code> (<code>pANTLR3_BASE_TREE</code> tree, <code>ANTLR3_UINT32</code> hint) </p>
<p> ANTLR3_API <code>pANTLR3_VECTOR_FACTORY</code> <code>antlr3VectorFactoryNew</code> (<code>ANTLR3_UINT32</code> sizeHint)<br />
 <i>Vector factory creation. </i><br />
 ANTLR3_API <code>pANTLR3_VECTOR</code> <code>antlr3VectorNew</code> (<code>ANTLR3_UINT32</code> sizeHint) </p>
<p> ANTLR3_API void <code>fillBufferExt</code> (<code>pANTLR3_COMMON_TOKEN_STREAM</code> tokenStream) </p>
<h2>Detailed Description</h2>
<p>Basic type and constant definitions for ANTLR3 Runtime. </p>
<h2>Define Documentation</h2>
<h3>#define _stat stat</h3>
<p>Referenced by antlr3Fsize().</p>
<h3>#define ANTLR3_API</h3>
<h3>#define ANTLR3_API</h3>
<h3>#define ANTLR3_AVERAGE</h3>
<h3>#define ANTLR3_CALLOC(numEl, elSize) calloc (numEl, (size_t)(elSize))</h3>
<p>Default definition of ANTLR3_CALLOC. You can override this before including <code>antlr3.h</code> if you wish to use your own implementation. </p>
<p> Referenced by addEdge(), antlr3AsciiFileStreamNew(), antlr3BaseRecognizerNew(), antlr3CommonTreeNodeStreamNew(), antlr3CommonTreeNodeStreamNewStream(), antlr3DebugListenerNew(), antlr3ExceptionNew(), antlr3IntStreamNew(), antlr3IntTrieNew(), antlr3TreeNodeStreamNew(), grow(), and intTrieAdd().</p>
<h3>#define ANTLR3_CDECL</h3>
<p>Referenced by addChild(), antlr3VectorSwap(), newRaw16(), and newRaw8().</p>
<h3>#define ANTLR3_CLOSESOCKET close</h3>
<p>Referenced by handshake().</p>
<h3>#define ANTLR3_ENCODING_LATIN1 0</h3>
<p>Referenced by stringInit8().</p>
<h3>#define ANTLR3_ENCODING_UCS2 1</h3>
<p>Referenced by stringInit16().</p>
<h3>#define ANTLR3_ENCODING_UTF32 3</h3>
<h3>#define ANTLR3_ENCODING_UTF8 2</h3>
<h3>#define ANTLR3_FASTCALL</h3>
<h3>#define ANTLR3_FPRINTF fprintf</h3>
<p>Default definition of fprintf, set this to something other than fprintf before including <code>antlr3.h</code> if your system does not have a fprintf. Note that you can define this to be // without harming the runtime. </p>
<p> Referenced by addChild(), alreadyParsedRule(), antlr3ExceptionPrint(), antlr3RecognitionExceptionNew(), becomeRoot(), consumeUntil(), consumeUntilSet(), ConvertUTF16toUTF32(), displayRecognitionError(), dupTok(), dupTreeNode(), getChild(), getChildCount(), getText(), match(), matchAny(), memoize(), mismatch(), mTokens(), recover(), recoverFromMismatchedElement(), recoverFromMismatchedSet(), recoverFromMismatchedToken(), replaceChildren(), setText(), setText8(), setType(), and synpred().</p>
<h3>#define ANTLR3_FREE(ptr) free ((void *)(ptr))</h3>
<p>Default definition of ANTLR3_FREE. You can override this before including <code>antlr3.h</code> if you wish to use your own implementation. </p>
<p> Referenced by antlr3BaseRecognizerNew(), antlr3BitsetCopy(), antlr3BitsetFree(), antlr3BitsetNew(), antlr3CommonTreeNodeStreamFree(), antlr3CTSFree(), antlr3EnumFree(), antlr3ExceptionFree(), antlr3HashDelete(), antlr3HashDeleteI(), antlr3HashFree(), antlr3HashRemove(), antlr3HashTableNew(), antlr3InputClose(), antlr3IntTrieNew(), antlr3ListFree(), antlr3SetVectorApi(), antlr3StackFree(), antlr3StringFactoryNew(), antlr3TokenStreamFree(), antlr3TreeNodeStreamFree(), antlr3VectorFree(), closeFactory(), closeVectorFactory(), ctaFree(), expungeRS(), factoryClose(), freeBR(), freeIntNode(), freeLexer(), freeParser(), freeStream(), freeTopo(), grow(), intTrieFree(), replaceChildren(), sortVector(), stringFree(), and toUTF8_16().</p>
<h3>#define ANTLR3_FREE_FUNC free</h3>
<p>Default definition of ANTLR3_FREE_FUNC . You can override this before including <code>antlr3.h</code> if you wish to use your own implementation. </p>
<p> Referenced by antlr3AsciiMark().</p>
<h3>#define ANTLR3_FUNC_PTR(ptr) (void *)((<code>ANTLR3_UINT32</code>)(ptr))</h3>
<p>Referenced by antlr3AsciiLT(), antlr3AsciiSeek(), antlr3EnumNew(), antlr3IntTrieNew(), antlr3ListNew(), antlr3StackNew(), antlr3VectorNew(), discardTokenType(), getRuleMemoization(), and setTokenTypeChannel().</p>
<h3>#define ANTLR3_INLINE inline</h3>
<h3>#define ANTLR3_LIST_SIZE_HINT 63</h3>
<h3>#define ANTLR3_MALLOC(request) malloc ((size_t)(request))</h3>
<p>Default definition of ANTLR3_MALLOC. You can override this before including <code>antlr3.h</code> if you wish to use your own implementation. </p>
<p> Referenced by ANTLR3_TREE_ADAPTORNew(), antlr3ArboretumNew(), antlr3AsciiMark(), antlr3BaseRecognizerNew(), antlr3BitsetCopy(), antlr3BitsetNew(), antlr3BitsetToIntList(), antlr3CommonTokenStreamNew(), antlr3CommonTreeNew(), antlr3EnumNew(), antlr3HashPut(), antlr3HashPutI(), antlr3HashTableNew(), antlr3LexerNew(), antlr3ListNew(), antlr3NewAsciiStringCopyStream(), antlr3NewAsciiStringInPlaceStream(), antlr3NewUCS2StringInPlaceStream(), antlr3ParserNew(), antlr3readAscii(), antlr3RewriteRuleElementStreamNewAE(), antlr3SetVectorApi(), antlr3StackNew(), antlr3StringFactoryNew(), antlr3TokenFactoryNew(), antlr3TokenStreamNew(), antlr3TopoNew(), antlr3TreeParserNewStream(), antlr3VectorFactoryNew(), antlr3VectorNew(), antlr3VectorResize(), newPool(), newRaw16(), newRaw8(), newSize16(), newSize8(), newToken(), sortToArray(), sortVector(), to8_16(), and toUTF8_16().</p>
<h3>#define ANTLR3_MEMCPY(target, source, size) memcpy((void *)(target), (const void *)(source), (size_t)(size))</h3>
<p>Default definition of ANTLR3_MEMCPY. You can override this before including <code>antlr3.h</code> if you wish to use your own implementation. </p>
<p> Referenced by antlr3BitsetClone(), antlr3BitsetCopy(), antlr3VectorResize(), and grow().</p>
<h3>#define ANTLR3_MEMMOVE(target, source, size) memmove((void *)(target), (const void *)(source), (size_t)(size))</h3>
<p>Default definition of ANTLR3_MEMMOVE. You can override this before including <code>antlr3.h</code> if you wish to use your own implementation. </p>
<p> Referenced by antlr3NewAsciiStringCopyStream(), antlr3VectorDel(), antrl3VectorRemove(), append16_16(), append8(), insert16_16(), insert16_8(), insert8(), newPtr16_16(), newPtr8(), set16_16(), and set8().</p>
<h3>#define ANTLR3_MEMSET(target, byte, size) memset((void *)(target), (int)(byte), (size_t)(size))</h3>
<p>Default definition of ANTLR3_MEMSET. You can override this before including <code>antlr3.h</code> if you wish to use your own implementation.</p>
<h3>#define ANTLR3_PRINTF printf</h3>
<p>Default definition of printf, set this to something other than printf before including <code>antlr3.h</code> if your system does not have a printf. Note that you can define this to be // without harming the runtime. </p>
<p> Referenced by ack().</p>
<h3>#define ANTLR3_REALLOC(current, request) realloc ((void *)(current), (size_t)(request))</h3>
<p>Default definition of ANTLR3_REALLOC. You can override this before including <code>antlr3.h</code> if you wish to use your own implementation. </p>
<p> Referenced by addc16(), addc8(), addEdge(), antlr3VectorResize(), append16_16(), append16_8(), append8(), insert16_16(), insert16_8(), insert8(), newPool(), set16_16(), set16_8(), and set8().</p>
<h3>#define ANTLR3_SIZE_HINT 1025</h3>
<h3>#define ANTLR3_STRDUP(instr) (<code>pANTLR3_UINT8</code>)(strdup ((const char *)(instr)))</h3>
<p>Default definition of ANTLR3_STRDUP. You can override this before including <code>antlr3.h</code> if you wish to use your own implementation. </p>
<p> Referenced by antlr3HashPut().</p>
<h3>#define ANTLR3_TRIE_DEPTH 31</h3>
<h3>#define ANTLR3_UINT32_CAST(ptr) (<code>ANTLR3_UINT32</code>)(ptr)</h3>
<p>Referenced by antlr3UCS2Substr(), displayRecognitionError(), getUniqueID(), and toUTF8_16().</p>
<h3>#define ANTLR3_UINT64_CAST(ptr) (<code>ANTLR3_UINT64</code>)((<code>ANTLR3_UINT32</code>)(ptr))</h3>
<h3>#define ANTLR3_UINT64_LIT(lit) lit##ULL</h3>
<h3>#define INVALID_SOCKET ((<code>SOCKET</code>)-1)</h3>
<p>Referenced by handshake().</p>
<h2>Typedef Documentation</h2>
<h3>typedef uint64_t <code>ANTLR3_BITWORD</code></h3>
<h3>typedef uint32_t <code>ANTLR3_BOOLEAN</code></h3>
<h3>typedef int32_t <code>ANTLR3_CHAR</code></h3>
<h3>typedef FILE* <code>ANTLR3_FDSC</code></h3>
<h3>typedef struct stat <code>ANTLR3_FSTAT_STRUCT</code></h3>
<h3>typedef int16_t <code>ANTLR3_INT16</code></h3>
<h3>typedef int32_t <code>ANTLR3_INT32</code></h3>
<h3>typedef int64_t <code>ANTLR3_INT64</code></h3>
<h3>typedef int8_t <code>ANTLR3_INT8</code></h3>
<h3>typedef <code>ANTLR3_UINT32</code> <code>ANTLR3_INTKEY</code></h3>
<h3>typedef <code>ANTLR3_INT32</code> <code>ANTLR3_MARKER</code></h3>
<h3>typedef size_t <code>ANTLR3_SALENT</code></h3>
<h3>typedef struct sockaddr_in <code>ANTLR3_SOCKADDRT</code></h3>
<h3>typedef uint32_t <code>ANTLR3_UCHAR</code></h3>
<h3>typedef uint16_t <code>ANTLR3_UINT16</code></h3>
<h3>typedef uint32_t <code>ANTLR3_UINT32</code></h3>
<h3>typedef uint64_t <code>ANTLR3_UINT64</code></h3>
<h3>typedef uint8_t <code>ANTLR3_UINT8</code></h3>
<h3>typedef uint64_t * <code>pANTLR3_BITWORD</code></h3>
<h3>typedef uint32_t * <code>pANTLR3_BOOLEAN</code></h3>
<h3>typedef int32_t * <code>pANTLR3_CHAR</code></h3>
<h3>typedef int16_t * <code>pANTLR3_INT16</code></h3>
<h3>typedef int32_t * <code>pANTLR3_INT32</code></h3>
<h3>typedef int64_t * <code>pANTLR3_INT64</code></h3>
<h3>typedef int8_t * <code>pANTLR3_INT8</code></h3>
<h3>typedef struct sockaddr* <code>pANTLR3_SOCKADDRC</code></h3>
<h3>typedef struct sockaddr_in * <code>pANTLR3_SOCKADDRT</code></h3>
<h3>typedef uint32_t * <code>pANTLR3_UCHAR</code></h3>
<h3>typedef uint16_t * <code>pANTLR3_UINT16</code></h3>
<h3>typedef uint32_t * <code>pANTLR3_UINT32</code></h3>
<h3>typedef uint64_t * <code>pANTLR3_UINT64</code></h3>
<h3>typedef uint8_t * <code>pANTLR3_UINT8</code></h3>
<h3>typedef int <code>SOCKET</code></h3>
<h2>Function Documentation</h2>
<h3>ANTLR3_API <code>pANTLR3_BASE_TREE_ADAPTOR</code> ANTLR3_TREE_ADAPTORDebugNew (<code>pANTLR3_STRING_FACTORY</code> strFactory, <code>pANTLR3_DEBUG_EVENT_LISTENER</code> debugger)</h3>
<p>Debugging version of the tree adaptor (not normally called as generated code calls setDebugEventListener instead which changes a normal token stream to a debugging stream and means that a user&#8217;s instantiation code does not need to be changed just to debug with AW. </p>
<p> References ANTLR3_TREE_ADAPTORNew(), antlr3BaseTreeAdaptorInit(), ANTLR3_BASE_TREE_ADAPTOR_struct::create, dbgCreate(), dbgSetTokenBoundaries(), and ANTLR3_BASE_TREE_ADAPTOR_struct::setTokenBoundaries.</p>
<h3>ANTLR3_API <code>pANTLR3_BASE_TREE_ADAPTOR</code> ANTLR3_TREE_ADAPTORNew (<code>pANTLR3_STRING_FACTORY</code> strFactory)</h3>
<p>Create a new tree adaptor. Note that despite the fact that this is creating a new COMMON_TREE adaptor, we return the address of the BASE_TREE interface, as should any other adaptor that wishes to be used as the tree element of a tree parse/build. It needs to be given the address of a valid string factory as we do not know what the originating input stream encoding type was. This way we can rely on just using the original input stream&#8217;s string factory or one of the correct type which the user supplies us. </p>
<p> References ANTLR3_MALLOC, antlr3ArboretumNew(), antlr3BaseTreeAdaptorInit(), antlr3TokenFactoryNew(), ANTLR3_COMMON_TREE_ADAPTOR_struct::arboretum, ANTLR3_COMMON_TREE_ADAPTOR_struct::baseAdaptor, create(), ANTLR3_BASE_TREE_ADAPTOR_struct::create, createToken(), ANTLR3_BASE_TREE_ADAPTOR_struct::createToken, createTokenFromToken(), ANTLR3_BASE_TREE_ADAPTOR_struct::createTokenFromToken, ctaFree(), deleteChild(), ANTLR3_BASE_TREE_ADAPTOR_struct::deleteChild, dupNode(), ANTLR3_BASE_TREE_ADAPTOR_struct::dupNode, errorNode(), ANTLR3_BASE_TREE_ADAPTOR_struct::errorNode, ANTLR3_BASE_TREE_ADAPTOR_struct::free, getChild(), ANTLR3_BASE_TREE_ADAPTOR_struct::getChild, getChildCount(), ANTLR3_BASE_TREE_ADAPTOR_struct::getChildCount, getChildIndex(), ANTLR3_BASE_TREE_ADAPTOR_struct::getChildIndex, getParent(), ANTLR3_BASE_TREE_ADAPTOR_struct::getParent, getText(), ANTLR3_BASE_TREE_ADAPTOR_struct::getText, getTokenStartIndex(), ANTLR3_BASE_TREE_ADAPTOR_struct::getTokenStartIndex, getTokenStopIndex(), ANTLR3_BASE_TREE_ADAPTOR_struct::getTokenStopIndex, getType(), ANTLR3_BASE_TREE_ADAPTOR_struct::getType, replaceChildren(), ANTLR3_BASE_TREE_ADAPTOR_struct::replaceChildren, setChild(), ANTLR3_BASE_TREE_ADAPTOR_struct::setChild, setChildIndex(), ANTLR3_BASE_TREE_ADAPTOR_struct::setChildIndex, setDebugEventListener(), ANTLR3_BASE_TREE_ADAPTOR_struct::setDebugEventListener, setParent(), ANTLR3_BASE_TREE_ADAPTOR_struct::setParent, setTokenBoundaries(), ANTLR3_BASE_TREE_ADAPTOR_struct::setTokenBoundaries, ANTLR3_BASE_TREE_ADAPTOR_struct::strFactory, ANTLR3_COMMON_TOKEN_struct::strFactory, ANTLR3_BASE_TREE_ADAPTOR_struct::super, ANTLR3_BASE_TREE_ADAPTOR_struct::tokenFactory, and ANTLR3_TOKEN_FACTORY_struct::unTruc. </p>
<p> Referenced by ANTLR3_TREE_ADAPTORDebugNew(), and antlr3CommonTreeNodeStreamNew().</p>
<h3>ANTLR3_API <code>pANTLR3_ARBORETUM</code> antlr3ArboretumNew (<code>pANTLR3_STRING_FACTORY</code> factory)</h3>
<p>References ANTLR3_MALLOC, antlr3SetCTAPI(), antlr3StackNew(), antlr3VectorFactoryNew(), ANTLR3_COMMON_TREE_struct::baseTree, ANTLR3_ARBORETUM_struct::close, ANTLR3_COMMON_TREE_struct::factory, factoryClose(), ANTLR3_TREE_PARSER_struct::free, newFromToken(), ANTLR3_ARBORETUM_struct::newFromToken, newFromTree(), ANTLR3_ARBORETUM_struct::newFromTree, newPool(), newPoolTree(), ANTLR3_ARBORETUM_struct::newTree, ANTLR3_ARBORETUM_struct::nilStack, ANTLR3_ARBORETUM_struct::pools, ANTLR3_BASE_TREE_struct::strFactory, ANTLR3_ARBORETUM_struct::thisPool, ANTLR3_ARBORETUM_struct::unTruc, and ANTLR3_ARBORETUM_struct::vFactory. </p>
<p> Referenced by ANTLR3_TREE_ADAPTORNew().</p>
<h3>ANTLR3_API <code>pANTLR3_INPUT_STREAM</code> antlr3AsciiFileStreamNew (<code>pANTLR3_UINT8</code> fileName)</h3>
<p>Use the contents of an operating system file as the input for an input stream. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>fileName</i> Name of operating system file to read.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>*</p>
<dd>Pointer to new input stream context upon success</p>
<dt>*</p>
<dd>One of the ANTLR3_ERR_ defines on error.</dl>
</dl>
<p> References ANTLR3_CALLOC, ANTLR3_CHARSTREAM, ANTLR3_SUCCESS, antlr3AsciiSetupStream(), antlr3readAscii(), ANTLR3_INPUT_STREAM_struct::close, ANTLR3_INPUT_STREAM_struct::fileName, ANTLR3_INPUT_STREAM_struct::istream, ANTLR3_STRING_FACTORY_struct::newStr, ANTLR3_INT_STREAM_struct::streamName, and ANTLR3_INPUT_STREAM_struct::strFactory.</p>
<h3>ANTLR3_API void antlr3BaseTreeAdaptorInit (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_DEBUG_EVENT_LISTENER</code> debugger)</h3>
<p>Given a pointer to a base tree adaptor structure (which is usually embedded in the super class the implements the tree adaptor used in the parse), initialize its function pointers and so on. </p>
<p> References ANTLR3_DEBUG_EVENT_LISTENER_struct::adaptor, addChild(), ANTLR3_BASE_TREE_ADAPTOR_struct::addChild, addChildToken(), ANTLR3_BASE_TREE_ADAPTOR_struct::addChildToken, becomeRoot(), ANTLR3_BASE_TREE_ADAPTOR_struct::becomeRoot, becomeRootToken(), ANTLR3_BASE_TREE_ADAPTOR_struct::becomeRootToken, createTypeText(), ANTLR3_BASE_TREE_ADAPTOR_struct::createTypeText, createTypeToken(), ANTLR3_BASE_TREE_ADAPTOR_struct::createTypeToken, createTypeTokenText(), ANTLR3_BASE_TREE_ADAPTOR_struct::createTypeTokenText, dbgAddChild(), dbgAddChildToken(), dbgBecomeRoot(), dbgBecomeRootToken(), dbgCreateTypeText(), dbgCreateTypeToken(), dbgCreateTypeTokenText(), dbgDupTree(), dbgNil(), dupTree(), ANTLR3_BASE_TREE_ADAPTOR_struct::dupTree, dupTreeTT(), ANTLR3_BASE_TREE_ADAPTOR_struct::dupTreeTT, getChild(), ANTLR3_BASE_TREE_ADAPTOR_struct::getChild, getChildCount(), ANTLR3_BASE_TREE_ADAPTOR_struct::getChildCount, getText(), ANTLR3_BASE_TREE_ADAPTOR_struct::getText, getType(), ANTLR3_BASE_TREE_ADAPTOR_struct::getType, getUniqueID(), ANTLR3_BASE_TREE_ADAPTOR_struct::getUniqueID, isNilNode(), ANTLR3_BASE_TREE_ADAPTOR_struct::isNilNode, makeDot(), ANTLR3_BASE_TREE_ADAPTOR_struct::makeDot, nilNode(), ANTLR3_BASE_TREE_ADAPTOR_struct::nilNode, rulePostProcessing(), ANTLR3_BASE_TREE_ADAPTOR_struct::rulePostProcessing, setText(), ANTLR3_BASE_TREE_ADAPTOR_struct::setText, setText8(), ANTLR3_BASE_TREE_ADAPTOR_struct::setText8, setType(), and ANTLR3_BASE_TREE_ADAPTOR_struct::setType. </p>
<p> Referenced by ANTLR3_TREE_ADAPTORDebugNew(), ANTLR3_TREE_ADAPTORNew(), and setDebugEventListener().</p>
<h3>ANTLR3_API <code>pANTLR3_BASE_TREE</code> antlr3BaseTreeNew (<code>pANTLR3_BASE_TREE</code> tree)</h3>
<p>References addChild(), ANTLR3_BASE_TREE_struct::addChild, addChildren(), ANTLR3_BASE_TREE_struct::addChildren, ANTLR3_BASE_TREE_struct::children, deleteChild(), ANTLR3_BASE_TREE_struct::deleteChild, dupTree(), ANTLR3_BASE_TREE_struct::dupTree, freshenPACIndexes(), ANTLR3_BASE_TREE_struct::freshenPACIndexes, freshenPACIndexesAll(), ANTLR3_BASE_TREE_struct::freshenPACIndexesAll, getCharPositionInLine(), ANTLR3_BASE_TREE_struct::getCharPositionInLine, getChild(), ANTLR3_BASE_TREE_struct::getChild, getChildCount(), ANTLR3_BASE_TREE_struct::getChildCount, getFirstChildWithType(), ANTLR3_BASE_TREE_struct::getFirstChildWithType, getLine(), ANTLR3_BASE_TREE_struct::getLine, replaceChildren(), ANTLR3_BASE_TREE_struct::replaceChildren, setChild(), ANTLR3_BASE_TREE_struct::setChild, ANTLR3_BASE_TREE_struct::strFactory, toStringTree(), and ANTLR3_BASE_TREE_struct::toStringTree. </p>
<p> Referenced by antlr3SetCTAPI().</p>
<h3>ANTLR3_API <code>pANTLR3_BITSET</code> antlr3BitsetCopy (<code>pANTLR3_BITSET_LIST</code> blist)</h3>
<p>References ANTLR3_FREE, ANTLR3_MALLOC, ANTLR3_MEMCPY, ANTLR3_BITSET_LIST_struct::bits, ANTLR3_BITSET_struct::blist, and ANTLR3_BITSET_LIST_struct::length.</p>
<h3>ANTLR3_API <code>pANTLR3_BITSET</code> antlr3BitsetList (<code>pANTLR3_HASH_TABLE</code> list)</h3>
<p>References ANTLR3_BITSET_struct::add, ANTLR3_SUCCESS, antlr3BitsetNew(), antlr3EnumNew(), ANTLR3_HASH_ENUM_struct::free, and ANTLR3_HASH_ENUM_struct::next. </p>
<p> Referenced by getTokensList().</p>
<h3>ANTLR3_API <code>pANTLR3_BITSET</code> antlr3BitsetLoad (<code>pANTLR3_BITSET_LIST</code> inBits)</h3>
<p>Creates a new bitset with at least one 64 bit bset of bits, but as many 64 bit sets as are required. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>bset</i> A variable number of bits to add to the set, ending in -1 (impossible bit).</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A new bit set with all of the specified bitmaps in it and the API initialized.</dl>
<p> Call as:</p>
<dl COMPACT>
<dt>*</p>
<dd>pANTLR3_BITSET = antlrBitsetLoad(bset, bset11, &#8230;, -1);</p>
<dt>*</p>
<dd>pANTLR3_BITSET = antlrBitsetOf(-1); Create empty bitset</dl>
<p> <code>Remarks:</code></p>
<dl COMPACT>
<dd>Stdargs function &#8211; must supply -1 as last paremeter, which is NOT added to the set.</dl>
<p> References antlr3BitsetNew(), ANTLR3_BITSET_LIST_struct::bits, ANTLR3_BITSET_struct::blist, ANTLR3_BITSET_struct::grow, and ANTLR3_BITSET_LIST_struct::length. </p>
<p> Referenced by combineFollows(), displayRecognitionError(), mismatchIsMissingToken(), and recoverFromMismatchedElement().</p>
<h3>ANTLR3_API <code>pANTLR3_BITSET</code> antlr3BitsetNew (<code>ANTLR3_UINT32</code> numBits)</h3>
<p>References ANTLR3_BITSET_BITS, ANTLR3_BITSET_LOG_BITS, ANTLR3_FREE, ANTLR3_MALLOC, antlr3BitsetSetAPI(), ANTLR3_BITSET_LIST_struct::bits, ANTLR3_BITSET_struct::blist, and ANTLR3_BITSET_LIST_struct::length. </p>
<p> Referenced by addEdge(), antlr3BitsetClone(), antlr3BitsetList(), antlr3BitsetLoad(), antlr3BitsetOf(), combineFollows(), and sortToArray().</p>
<h3>ANTLR3_API <code>pANTLR3_BITSET</code> antlr3BitsetOf (<code>ANTLR3_INT32</code> bit, &#8230;)</h3>
<p>Creates a new bitset with at least one element, but as many elements are required. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>bit</i> A variable number of bits to add to the set, ending in -1 (impossible bit).</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A new bit set with all of the specified elements added into it.</dl>
<p> Call as:</p>
<dl COMPACT>
<dt>*</p>
<dd>pANTLR3_BITSET = antlrBitsetOf(n, n1, n2, -1);</p>
<dt>*</p>
<dd>pANTLR3_BITSET = antlrBitsetOf(-1); Create empty bitset</dl>
<p> <code>Remarks:</code></p>
<dl COMPACT>
<dd>Stdargs function &#8211; must supply -1 as last paremeter, which is NOT added to the set.</dl>
<p> References antlr3BitsetAdd(), and antlr3BitsetNew(). </p>
<p> Referenced by getTokensType().</p>
<h3>ANTLR3_API void antlr3BitsetSetAPI (<code>pANTLR3_BITSET</code> bitset)</h3>
<p>References ANTLR3_BITSET_struct::add, antlr3BitsetAdd(), antlr3BitsetClone(), antlr3BitsetEquals(), antlr3BitsetFree(), antlr3BitsetIsNil(), antlr3BitsetMember(), antlr3BitsetNumBits(), antlr3BitsetOR(), antlr3BitsetORInPlace(), antlr3BitsetRemove(), antlr3BitsetSize(), antlr3BitsetToIntList(), ANTLR3_BITSET_struct::bor, ANTLR3_BITSET_struct::borInPlace, ANTLR3_BITSET_struct::clone, ANTLR3_BITSET_struct::equals, ANTLR3_BITSET_struct::free, grow(), ANTLR3_BITSET_struct::grow, ANTLR3_BITSET_struct::isMember, ANTLR3_BITSET_struct::isNilNode, ANTLR3_BITSET_struct::numBits, ANTLR3_BITSET_struct::remove, ANTLR3_BITSET_struct::size, and ANTLR3_BITSET_struct::toIntList. </p>
<p> Referenced by antlr3BitsetNew().</p>
<h3>ANTLR3_API <code>ANTLR3_UCHAR</code> antlr3c8toAntlrc (<code>ANTLR3_INT8</code> inc)</h3>
<p>Provides basic utility functions to convert between the various Unicode character conversions. There are of course various packages that could be used instead of these functions, but then the Antlr 3 C runtime would be dependant on the particular package. Using ICU for this is a good idea if your project is already dependant on it. Convert 8 bit character to ANTLR char form. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>inc</i> Input character to transform in 8 bit ASCII form.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ANTLR3_UCHAR encoding of the character.</dl>
<h3>ANTLR3_API <code>pANTLR3_COMMON_TOKEN_STREAM</code> antlr3CommonTokenDebugStreamSourceNew (<code>ANTLR3_UINT32</code> hint, <code>pANTLR3_TOKEN_SOURCE</code> source, <code>pANTLR3_DEBUG_EVENT_LISTENER</code> debugger)</h3>
<p>References ANTLR3_INT_STREAM_struct::_LA, ANTLR3_TOKEN_STREAM_struct::_LT, ANTLR3_FALSE, antlr3CommonTokenStreamSourceNew(), ANTLR3_INT_STREAM_struct::consume, dbgConsume(), dbgLA(), dbgMark(), dbgRewindLast(), dbgRewindStream(), dbgSeek(), dbgTokLT(), ANTLR3_TOKEN_STREAM_struct::debugger, ANTLR3_TOKEN_STREAM_struct::initialStreamState, ANTLR3_TOKEN_STREAM_struct::istream, ANTLR3_INT_STREAM_struct::mark, ANTLR3_INT_STREAM_struct::rewind, ANTLR3_INT_STREAM_struct::rewindLast, ANTLR3_INT_STREAM_struct::seek, and ANTLR3_COMMON_TOKEN_STREAM_struct::tstream.</p>
<h3>ANTLR3_API <code>pANTLR3_COMMON_TOKEN</code> antlr3CommonTokenNew (<code>ANTLR3_UINT32</code> ttype)</h3>
<p>References newToken(), and ANTLR3_COMMON_TOKEN_struct::setType. </p>
<p> Referenced by antlr3CommonTreeNodeStreamNew().</p>
<h3>ANTLR3_API <code>pANTLR3_COMMON_TOKEN_STREAM</code> antlr3CommonTokenStreamNew (<code>ANTLR3_UINT32</code> hint)</h3>
<p>References _LA(), ANTLR3_INT_STREAM_struct::_LA, ANTLR3_TOKEN_STREAM_struct::_LT, ANTLR3_MALLOC, ANTLR3_TOKENSTREAM, antlr3IntStreamNew(), antlr3TokenStreamNew(), antlr3VectorNew(), consume(), ANTLR3_INT_STREAM_struct::consume, discardOffChannel(), ANTLR3_COMMON_TOKEN_STREAM_struct::discardOffChannelToks, discardTokenType(), ANTLR3_COMMON_TOKEN_STREAM_struct::discardTokenType, ANTLR3_TOKEN_STREAM_struct::get, getSourceName(), ANTLR3_INT_STREAM_struct::getSourceName, getTokenRange(), ANTLR3_COMMON_TOKEN_STREAM_struct::getTokenRange, getTokens(), ANTLR3_COMMON_TOKEN_STREAM_struct::getTokens, getTokensList(), ANTLR3_COMMON_TOKEN_STREAM_struct::getTokensList, getTokenSource(), ANTLR3_TOKEN_STREAM_struct::getTokenSource, getTokensSet(), ANTLR3_COMMON_TOKEN_STREAM_struct::getTokensSet, getTokensType(), ANTLR3_COMMON_TOKEN_STREAM_struct::getTokensType, ANTLR3_INT_STREAM_struct::index, ANTLR3_TOKEN_STREAM_struct::istream, mark(), ANTLR3_INT_STREAM_struct::mark, ANTLR3_COMMON_TOKEN_STREAM_struct::p, release(), ANTLR3_INT_STREAM_struct::release, ANTLR3_INT_STREAM_struct::rewind, rewindLast(), ANTLR3_INT_STREAM_struct::rewindLast, rewindStream(), seek(), ANTLR3_INT_STREAM_struct::seek, setDebugListener(), ANTLR3_TOKEN_STREAM_struct::setDebugListener, setTokenSource(), ANTLR3_TOKEN_STREAM_struct::setTokenSource, setTokenTypeChannel(), ANTLR3_COMMON_TOKEN_STREAM_struct::setTokenTypeChannel, size(), ANTLR3_INT_STREAM_struct::size, ANTLR3_INT_STREAM_struct::super, ANTLR3_TOKEN_STREAM_struct::super, tindex(), ANTLR3_COMMON_TOKEN_STREAM_struct::tokens, tokLT(), toString(), ANTLR3_TOKEN_STREAM_struct::toString, toStringSS(), ANTLR3_TOKEN_STREAM_struct::toStringSS, toStringTT(), ANTLR3_TOKEN_STREAM_struct::toStringTT, ANTLR3_COMMON_TOKEN_STREAM_struct::tstream, and ANTLR3_INT_STREAM_struct::type. </p>
<p> Referenced by antlr3CommonTokenStreamSourceNew().</p>
<h3>ANTLR3_API <code>pANTLR3_COMMON_TOKEN_STREAM</code> antlr3CommonTokenStreamSourceNew (<code>ANTLR3_UINT32</code> hint, <code>pANTLR3_TOKEN_SOURCE</code> source)</h3>
<p>References ANTLR3_FALSE, ANTLR3_TOKEN_DEFAULT_CHANNEL, antlr3CommonTokenStreamNew(), antlr3CTSFree(), ANTLR3_COMMON_TOKEN_STREAM_struct::channel, ANTLR3_COMMON_TOKEN_STREAM_struct::channelOverrides, ANTLR3_COMMON_TOKEN_STREAM_struct::discardOffChannel, ANTLR3_COMMON_TOKEN_STREAM_struct::discardSet, ANTLR3_COMMON_TOKEN_STREAM_struct::free, ANTLR3_TOKEN_STREAM_struct::setTokenSource, and ANTLR3_COMMON_TOKEN_STREAM_struct::tstream. </p>
<p> Referenced by antlr3CommonTokenDebugStreamSourceNew().</p>
<h3>ANTLR3_API <code>pANTLR3_COMMON_TREE</code> antlr3CommonTreeNew (void)</h3>
<p>References ANTLR3_MALLOC, and antlr3SetCTAPI(). </p>
<p> Referenced by antlr3CommonTreeNewFromToken().</p>
<h3>ANTLR3_API <code>pANTLR3_COMMON_TREE</code> antlr3CommonTreeNewFromToken (<code>pANTLR3_COMMON_TOKEN</code> tree)</h3>
<p>References antlr3CommonTreeNew(), and ANTLR3_COMMON_TREE_struct::token.</p>
<h3>ANTLR3_API <code>pANTLR3_COMMON_TREE</code> antlr3CommonTreeNewFromTree (<code>pANTLR3_COMMON_TREE</code> tree)</h3>
<h3>ANTLR3_API <code>pANTLR3_COMMON_TREE_NODE_STREAM</code> antlr3CommonTreeNodeStreamNew (<code>pANTLR3_STRING_FACTORY</code> strFactory, <code>ANTLR3_UINT32</code> hint)</h3>
<p>References _LA(), ANTLR3_INT_STREAM_struct::_LA, _LT(), ANTLR3_TREE_NODE_STREAM_struct::_LT, ANTLR3_COMMON_TREE_NODE_STREAM_struct::adaptor, addNavigationNode(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::addNavigationNode, ANTLR3_CALLOC, ANTLR3_COMMONTREENODE, ANTLR3_FALSE, ANTLR3_TEXT_CHARP, ANTLR3_TOKEN_DOWN, ANTLR3_TOKEN_EOF, ANTLR3_TOKEN_INVALID, ANTLR3_TOKEN_UP, ANTLR3_TREE_ADAPTORNew(), antlr3CommonTokenNew(), antlr3CommonTreeNodeStreamFree(), antlr3IntStreamNew(), antlr3SetCTAPI(), antlr3StackNew(), antlr3TreeNodeStreamNew(), antlr3VectorNew(), ANTLR3_COMMON_TOKEN_struct::chars, consume(), ANTLR3_INT_STREAM_struct::consume, ANTLR3_TREE_NODE_STREAM_struct::ctns, DEFAULT_INITIAL_BUFFER_SIZE, ANTLR3_COMMON_TREE_NODE_STREAM_struct::DOWN, ANTLR3_COMMON_TREE_NODE_STREAM_struct::EOF_NODE, ANTLR3_TREE_NODE_STREAM_struct::free, ANTLR3_BASE_TREE_ADAPTOR_struct::free, ANTLR3_COMMON_TREE_NODE_STREAM_struct::free, ANTLR3_TREE_NODE_STREAM_struct::get, getTreeAdaptor(), ANTLR3_TREE_NODE_STREAM_struct::getTreeAdaptor, getTreeSource(), ANTLR3_TREE_NODE_STREAM_struct::getTreeSource, hasUniqueNavigationNodes(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::hasUniqueNavigationNodes, ANTLR3_INT_STREAM_struct::index, INITIAL_CALL_STACK_SIZE, ANTLR3_COMMON_TREE_NODE_STREAM_struct::INVALID_NODE, ANTLR3_TREE_NODE_STREAM_struct::istream, mark(), ANTLR3_INT_STREAM_struct::mark, ANTLR3_COMMON_TREE_NODE_STREAM_struct::markers, newDownNode(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::newDownNode, newUpNode(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::newUpNode, ANTLR3_COMMON_TREE_NODE_STREAM_struct::nodes, ANTLR3_COMMON_TREE_NODE_STREAM_struct::nodeStack, ANTLR3_COMMON_TREE_NODE_STREAM_struct::p, pop(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::pop, push(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::push, release(), ANTLR3_INT_STREAM_struct::release, reset(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::reset, ANTLR3_INT_STREAM_struct::rewind, rewindLast(), ANTLR3_INT_STREAM_struct::rewindLast, rewindMark(), seek(), ANTLR3_INT_STREAM_struct::seek, setUniqueNavigationNodes(), ANTLR3_TREE_NODE_STREAM_struct::setUniqueNavigationNodes, size(), ANTLR3_INT_STREAM_struct::size, ANTLR3_COMMON_TOKEN_struct::strFactory, ANTLR3_COMMON_TREE_NODE_STREAM_struct::stringFactory, ANTLR3_COMMON_TREE_NODE_STREAM_struct::super, ANTLR3_INT_STREAM_struct::super, ANTLR3_COMMON_TOKEN_struct::textState, tindex(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::tnstream, ANTLR3_COMMON_TREE_struct::token, ANTLR3_COMMON_TOKEN_struct::tokText, toString(), ANTLR3_TREE_NODE_STREAM_struct::toString, toStringSS(), ANTLR3_TREE_NODE_STREAM_struct::toStringSS, toStringWork(), ANTLR3_TREE_NODE_STREAM_struct::toStringWork, ANTLR3_INT_STREAM_struct::type, ANTLR3_COMMON_TREE_NODE_STREAM_struct::uniqueNavigationNodes, and ANTLR3_COMMON_TREE_NODE_STREAM_struct::UP. </p>
<p> Referenced by antlr3CommonTreeNodeStreamNewTree().</p>
<h3>ANTLR3_API <code>pANTLR3_COMMON_TREE_NODE_STREAM</code> antlr3CommonTreeNodeStreamNewStream (<code>pANTLR3_COMMON_TREE_NODE_STREAM</code> inStream)</h3>
<p>References _LA(), ANTLR3_INT_STREAM_struct::_LA, _LT(), ANTLR3_TREE_NODE_STREAM_struct::_LT, ANTLR3_COMMON_TREE_NODE_STREAM_struct::adaptor, addNavigationNode(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::addNavigationNode, ANTLR3_CALLOC, ANTLR3_COMMONTREENODE, ANTLR3_FALSE, ANTLR3_TRUE, antlr3CommonTreeNodeStreamFree(), antlr3IntStreamNew(), antlr3SetCTAPI(), antlr3TreeNodeStreamNew(), antlr3VectorNew(), consume(), ANTLR3_INT_STREAM_struct::consume, ANTLR3_TREE_NODE_STREAM_struct::ctns, DEFAULT_INITIAL_BUFFER_SIZE, ANTLR3_COMMON_TREE_NODE_STREAM_struct::DOWN, ANTLR3_COMMON_TREE_NODE_STREAM_struct::EOF_NODE, ANTLR3_TREE_NODE_STREAM_struct::free, ANTLR3_COMMON_TREE_NODE_STREAM_struct::free, ANTLR3_TREE_NODE_STREAM_struct::get, getLookaheadSize(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::getLookaheadSize, getTreeAdaptor(), ANTLR3_TREE_NODE_STREAM_struct::getTreeAdaptor, getTreeSource(), ANTLR3_TREE_NODE_STREAM_struct::getTreeSource, hasUniqueNavigationNodes(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::hasUniqueNavigationNodes, ANTLR3_INT_STREAM_struct::index, ANTLR3_COMMON_TREE_NODE_STREAM_struct::INVALID_NODE, ANTLR3_COMMON_TREE_NODE_STREAM_struct::isRewriter, ANTLR3_TREE_NODE_STREAM_struct::istream, mark(), ANTLR3_INT_STREAM_struct::mark, ANTLR3_COMMON_TREE_NODE_STREAM_struct::markers, newDownNode(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::newDownNode, newUpNode(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::newUpNode, ANTLR3_COMMON_TREE_NODE_STREAM_struct::nodes, ANTLR3_COMMON_TREE_NODE_STREAM_struct::nodeStack, ANTLR3_COMMON_TREE_NODE_STREAM_struct::p, pop(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::pop, push(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::push, release(), ANTLR3_INT_STREAM_struct::release, reset(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::reset, ANTLR3_INT_STREAM_struct::rewind, rewindLast(), ANTLR3_INT_STREAM_struct::rewindLast, rewindMark(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::root, seek(), ANTLR3_INT_STREAM_struct::seek, setUniqueNavigationNodes(), ANTLR3_TREE_NODE_STREAM_struct::setUniqueNavigationNodes, size(), ANTLR3_INT_STREAM_struct::size, ANTLR3_COMMON_TOKEN_struct::strFactory, ANTLR3_COMMON_TREE_NODE_STREAM_struct::stringFactory, ANTLR3_COMMON_TREE_NODE_STREAM_struct::super, ANTLR3_INT_STREAM_struct::super, tindex(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::tnstream, ANTLR3_COMMON_TREE_struct::token, toString(), ANTLR3_TREE_NODE_STREAM_struct::toString, toStringSS(), ANTLR3_TREE_NODE_STREAM_struct::toStringSS, toStringWork(), ANTLR3_TREE_NODE_STREAM_struct::toStringWork, ANTLR3_INT_STREAM_struct::type, ANTLR3_COMMON_TREE_NODE_STREAM_struct::uniqueNavigationNodes, and ANTLR3_COMMON_TREE_NODE_STREAM_struct::UP.</p>
<h3>ANTLR3_API <code>pANTLR3_COMMON_TREE_NODE_STREAM</code> antlr3CommonTreeNodeStreamNewTree (<code>pANTLR3_BASE_TREE</code> tree, <code>ANTLR3_UINT32</code> hint)</h3>
<p>References antlr3CommonTreeNodeStreamNew(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::root, and ANTLR3_BASE_TREE_struct::strFactory.</p>
<h3>ANTLR3_API <code>pANTLR3_DEBUG_EVENT_LISTENER</code> antlr3DebugListenerNew ()</h3>
<p>Create and initialize a new debug event listener that can be connected to by ANTLRWorks and any other debugger via a socket. </p>
<p> References addChild(), ANTLR3_DEBUG_EVENT_LISTENER_struct::addChild, ANTLR3_CALLOC, becomeRoot(), ANTLR3_DEBUG_EVENT_LISTENER_struct::becomeRoot, beginBacktrack(), ANTLR3_DEBUG_EVENT_LISTENER_struct::beginBacktrack, beginResync(), ANTLR3_DEBUG_EVENT_LISTENER_struct::beginResync, commence(), ANTLR3_DEBUG_EVENT_LISTENER_struct::commence, consumeHiddenToken(), ANTLR3_DEBUG_EVENT_LISTENER_struct::consumeHiddenToken, consumeNode(), ANTLR3_DEBUG_EVENT_LISTENER_struct::consumeNode, consumeToken(), ANTLR3_DEBUG_EVENT_LISTENER_struct::consumeToken, createNode(), ANTLR3_DEBUG_EVENT_LISTENER_struct::createNode, createNodeTok(), ANTLR3_DEBUG_EVENT_LISTENER_struct::createNodeTok, DEFAULT_DEBUGGER_PORT, endBacktrack(), ANTLR3_DEBUG_EVENT_LISTENER_struct::endBacktrack, endResync(), ANTLR3_DEBUG_EVENT_LISTENER_struct::endResync, enterAlt(), ANTLR3_DEBUG_EVENT_LISTENER_struct::enterAlt, enterDecision(), ANTLR3_DEBUG_EVENT_LISTENER_struct::enterDecision, enterRule(), ANTLR3_DEBUG_EVENT_LISTENER_struct::enterRule, enterSubRule(), ANTLR3_DEBUG_EVENT_LISTENER_struct::enterSubRule, errorNode(), ANTLR3_DEBUG_EVENT_LISTENER_struct::errorNode, exitDecision(), ANTLR3_DEBUG_EVENT_LISTENER_struct::exitDecision, exitRule(), ANTLR3_DEBUG_EVENT_LISTENER_struct::exitRule, exitSubRule(), ANTLR3_DEBUG_EVENT_LISTENER_struct::exitSubRule, handshake(), ANTLR3_DEBUG_EVENT_LISTENER_struct::handshake, location(), ANTLR3_DEBUG_EVENT_LISTENER_struct::location, LT(), ANTLR3_DEBUG_EVENT_LISTENER_struct::LT, LTT(), ANTLR3_DEBUG_EVENT_LISTENER_struct::LTT, mark(), ANTLR3_DEBUG_EVENT_LISTENER_struct::mark, nilNode(), ANTLR3_DEBUG_EVENT_LISTENER_struct::nilNode, ANTLR3_DEBUG_EVENT_LISTENER_struct::port, ANTLR3_DEBUG_EVENT_LISTENER_struct::PROTOCOL_VERSION, recognitionException(), ANTLR3_DEBUG_EVENT_LISTENER_struct::recognitionException, ANTLR3_DEBUG_EVENT_LISTENER_struct::rewind, rewindLast(), ANTLR3_DEBUG_EVENT_LISTENER_struct::rewindLast, rewindMark(), semanticPredicate(), ANTLR3_DEBUG_EVENT_LISTENER_struct::semanticPredicate, setTokenBoundaries(), ANTLR3_DEBUG_EVENT_LISTENER_struct::setTokenBoundaries, terminate(), and ANTLR3_DEBUG_EVENT_LISTENER_struct::terminate. </p>
<p> Referenced by antlr3DebugListenerNewPort().</p>
<h3>ANTLR3_API <code>ANTLR3_INT32</code> antlr3dfapredict (void * ctx, <code>pANTLR3_BASE_RECOGNIZER</code> rec, <code>pANTLR3_INT_STREAM</code> is, <code>pANTLR3_CYCLIC_DFA</code> cdfa)</h3>
<p>From the input stream, predict what alternative will succeed using this DFA (representing the covering regular approximation to the underlying CFL). Return an alternative number 1..n. Throw an exception upon error. </p>
<p> References ANTLR3_INT_STREAM_struct::_LA, ANTLR3_CYCLIC_DFA_struct::accept, ANTLR3_TOKEN_EOF, ANTLR3_TRUE, ANTLR3_INT_STREAM_struct::consume, ANTLR3_CYCLIC_DFA_struct::eof, ANTLR3_CYCLIC_DFA_struct::eot, ANTLR3_RECOGNIZER_SHARED_STATE_struct::error, ANTLR3_INT_STREAM_struct::mark, mark(), ANTLR3_CYCLIC_DFA_struct::min, noViableAlt(), ANTLR3_INT_STREAM_struct::rewind, ANTLR3_CYCLIC_DFA_struct::special, ANTLR3_CYCLIC_DFA_struct::specialStateTransition, ANTLR3_BASE_RECOGNIZER_struct::state, and ANTLR3_CYCLIC_DFA_struct::transition.</p>
<h3>ANTLR3_API <code>ANTLR3_INT32</code> antlr3dfaspecialStateTransition (void * ctx, <code>pANTLR3_BASE_RECOGNIZER</code> rec, <code>pANTLR3_INT_STREAM</code> is, <code>pANTLR3_CYCLIC_DFA</code> dfa, <code>ANTLR3_INT32</code> s)</h3>
<p>Default special state implementation.</p>
<h3>ANTLR3_API <code>ANTLR3_INT32</code> antlr3dfaspecialTransition (void * ctx, <code>pANTLR3_BASE_RECOGNIZER</code> rec, <code>pANTLR3_INT_STREAM</code> is, <code>pANTLR3_CYCLIC_DFA</code> dfa, <code>ANTLR3_INT32</code> s)</h3>
<h3>ANTLR3_API <code>pANTLR3_HASH_ENUM</code> antlr3EnumNew (<code>pANTLR3_HASH_TABLE</code> table)</h3>
<p>Creates an enumeration structure to traverse the hash table. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>table</i> Table to enumerate</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Pointer to enumeration structure.</dl>
<p> References ANTLR3_ERR_NOMEM, ANTLR3_FUNC_PTR, ANTLR3_MALLOC, antlr3EnumFree(), antlr3EnumNext(), antlr3EnumNextEntry(), ANTLR3_HASH_ENUM_struct::bucket, ANTLR3_HASH_TABLE_struct::buckets, ANTLR3_HASH_BUCKET_struct::entries, ANTLR3_HASH_ENUM_struct::entry, ANTLR3_HASH_ENUM_struct::free, ANTLR3_HASH_ENUM_struct::next, and ANTLR3_HASH_ENUM_struct::table. </p>
<p> Referenced by antlr3BitsetList().</p>
<h3>ANTLR3_API <code>pANTLR3_EXCEPTION</code> antlr3ExceptionNew (<code>ANTLR3_UINT32</code> exception, void * name, void * message, <code>ANTLR3_BOOLEAN</code> freeMessage)</h3>
<p>Creates a new ANTLR3 exception structure. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>exception</i> One of the ANTLR3_xxx_EXCEPTION indicators such as <code>ANTLR3_RECOGNITION_EXCEPTION</code><br />
 <i>message</i> Pointer to message string<br />
 <i>freeMessage</i> Set to ANTLR3_TRUE if the message parameter should be freed by a call to <code>ANTLR3_FREE()</code> when the exception is destroyed.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Pointer to newly initialized exception structure, or an ANTLR3_ERR_xx defined value upon failure.</dl>
<p> An exception is &#8216;thrown&#8217; by a recognizer when input is seen that is not predicted by the grammar productions or when some other error condition occurs. In C we do not have the luxury of try and catch blocks, so exceptions are added in the order they occur to a list in the baserecognizer structure. The last one to be thrown is inserted at the head of the list and the one currently installed is pointed to by the newly installed exception. </p>
<p> <code>Remarks:</code></p>
<dl COMPACT>
<dd>After an exception is created, you may add a pointer to your own structure and a pointer to a function to free this structure when the exception is destroyed.</dl>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>ANTLR3_EXCEPTION</code></dl>
<p> References ANTLR3_CALLOC, antlr3ExceptionFree(), antlr3ExceptionPrint(), ANTLR3_EXCEPTION_struct::freeEx, ANTLR3_EXCEPTION_struct::freeMessage, ANTLR3_EXCEPTION_struct::message, ANTLR3_EXCEPTION_struct::name, ANTLR3_EXCEPTION_struct::print, and ANTLR3_EXCEPTION_struct::type. </p>
<p> Referenced by antlr3RecognitionExceptionNew().</p>
<h3>ANTLR3_API <code>ANTLR3_UINT32</code> antlr3Hash (void * key, <code>ANTLR3_UINT32</code> keylen)</h3>
<p>Given an input key of arbitrary length, return a hash value of it. This can then be used (with suitable modulo) to index other structures. </p>
<p> Referenced by antlr3HashGet(), antlr3HashPut(), and antlr3HashRemove().</p>
<h3>ANTLR3_API <code>pANTLR3_HASH_TABLE</code> antlr3HashTableNew (<code>ANTLR3_UINT32</code> sizeHint)</h3>
<p>References ANTLR3_HASH_TABLE_struct::allowDups, ANTLR3_FALSE, ANTLR3_FREE, ANTLR3_MALLOC, ANTLR3_TRUE, antlr3HashDelete(), antlr3HashDeleteI(), antlr3HashFree(), antlr3HashGet(), antlr3HashGetI(), antlr3HashPut(), antlr3HashPutI(), antlr3HashRemove(), antlr3HashRemoveI(), antlr3HashSize(), ANTLR3_HASH_TABLE_struct::buckets, ANTLR3_HASH_TABLE_struct::count, ANTLR3_HASH_TABLE_struct::del, ANTLR3_HASH_TABLE_struct::delI, ANTLR3_HASH_TABLE_struct::doStrdup, ANTLR3_HASH_BUCKET_struct::entries, ANTLR3_HASH_TABLE_struct::free, ANTLR3_HASH_TABLE_struct::get, ANTLR3_HASH_TABLE_struct::getI, ANTLR3_HASH_TABLE_struct::modulo, ANTLR3_HASH_TABLE_struct::put, ANTLR3_HASH_TABLE_struct::putI, ANTLR3_HASH_TABLE_struct::remove, ANTLR3_HASH_TABLE_struct::removeI, and ANTLR3_HASH_TABLE_struct::size. </p>
<p> Referenced by antlr3ListNew().</p>
<h3>ANTLR3_API <code>pANTLR3_INT_TRIE</code> antlr3IntTrieNew (<code>ANTLR3_UINT32</code> depth)</h3>
<p>References ANTLR3_INT_TRIE_struct::add, ANTLR3_CALLOC, ANTLR3_ERR_NOMEM, ANTLR3_FREE, ANTLR3_FUNC_PTR, ANTLR3_INT_TRIE_NODE_struct::bitNum, ANTLR3_INT_TRIE_struct::count, ANTLR3_INT_TRIE_struct::del, ANTLR3_INT_TRIE_struct::free, ANTLR3_INT_TRIE_struct::get, intTrieAdd(), intTrieDel(), intTrieFree(), intTrieGet(), ANTLR3_INT_TRIE_NODE_struct::leftN, ANTLR3_INT_TRIE_NODE_struct::rightN, and ANTLR3_INT_TRIE_struct::root. </p>
<p> Referenced by getRuleMemoization(), and reset().</p>
<h3>ANTLR3_API <code>pANTLR3_LEXER</code> antlr3LexerNew (<code>ANTLR3_UINT32</code> sizeHint, <code>pANTLR3_RECOGNIZER_SHARED_STATE</code> state)</h3>
<p>References ANTLR3_MALLOC, ANTLR3_TOKEN_EOF, ANTLR3_TOKEN_INVALID, ANTLR3_TRUE, ANTLR3_TYPE_LEXER, antlr3BaseRecognizerNew(), antlr3SetTokenAPI(), displayRecognitionError(), ANTLR3_BASE_RECOGNIZER_struct::displayRecognitionError, emit(), ANTLR3_LEXER_struct::emit, emitNew(), ANTLR3_LEXER_struct::emitNew, ANTLR3_TOKEN_SOURCE_struct::eofToken, ANTLR3_COMMON_TOKEN_struct::factoryMade, ANTLR3_BASE_RECOGNIZER_struct::free, ANTLR3_LEXER_struct::free, freeLexer(), getCharIndex(), ANTLR3_LEXER_struct::getCharIndex, getCharPositionInLine(), ANTLR3_LEXER_struct::getCharPositionInLine, getCurrentInputSymbol(), ANTLR3_BASE_RECOGNIZER_struct::getCurrentInputSymbol, getLine(), ANTLR3_LEXER_struct::getLine, getMissingSymbol(), ANTLR3_BASE_RECOGNIZER_struct::getMissingSymbol, getText(), ANTLR3_LEXER_struct::getText, matchAny(), ANTLR3_LEXER_struct::matchAny, matchc(), ANTLR3_LEXER_struct::matchc, matchRange(), ANTLR3_LEXER_struct::matchRange, matchs(), ANTLR3_LEXER_struct::matchs, mTokens(), ANTLR3_LEXER_struct::mTokens, nextToken(), ANTLR3_TOKEN_SOURCE_struct::nextToken, popCharStream(), ANTLR3_LEXER_struct::popCharStream, pushCharStream(), ANTLR3_LEXER_struct::pushCharStream, ANTLR3_LEXER_struct::rec, recover(), ANTLR3_LEXER_struct::recover, reportError(), ANTLR3_BASE_RECOGNIZER_struct::reportError, reset(), ANTLR3_BASE_RECOGNIZER_struct::reset, setCharStream(), ANTLR3_LEXER_struct::setCharStream, ANTLR3_COMMON_TOKEN_struct::setType, ANTLR3_TOKEN_SOURCE_struct::skipToken, ANTLR3_BASE_RECOGNIZER_struct::state, ANTLR3_COMMON_TOKEN_struct::strFactory, ANTLR3_TOKEN_SOURCE_struct::strFactory, ANTLR3_TOKEN_SOURCE_struct::super, ANTLR3_BASE_RECOGNIZER_struct::super, ANTLR3_RECOGNIZER_SHARED_STATE_struct::tokFactory, and ANTLR3_RECOGNIZER_SHARED_STATE_struct::tokSource. </p>
<p> Referenced by antlr3LexerNewStream().</p>
<h3>ANTLR3_API <code>pANTLR3_LEXER</code> antlr3LexerNewStream (<code>ANTLR3_UINT32</code> sizeHint, <code>pANTLR3_INPUT_STREAM</code> input, <code>pANTLR3_RECOGNIZER_SHARED_STATE</code> state)</h3>
<p>References antlr3LexerNew(), and setCharStream().</p>
<h3>ANTLR3_API <code>pANTLR3_LIST</code> antlr3ListNew (<code>ANTLR3_UINT32</code> sizeHint)</h3>
<p>References ANTLR3_LIST_struct::add, ANTLR3_ERR_NOMEM, ANTLR3_FUNC_PTR, ANTLR3_MALLOC, antlr3HashTableNew(), antlr3ListAdd(), antlr3ListDelete(), antlr3ListFree(), antlr3ListGet(), antlr3ListPut(), antlr3ListRemove(), antlr3ListSize(), ANTLR3_LIST_struct::del, ANTLR3_LIST_struct::free, ANTLR3_LIST_struct::get, ANTLR3_LIST_struct::put, ANTLR3_LIST_struct::remove, ANTLR3_LIST_struct::size, and ANTLR3_LIST_struct::table. </p>
<p> Referenced by discardTokenType(), getTokensSet(), and setTokenTypeChannel().</p>
<h3>ANTLR3_API void antlr3MTNExceptionNew (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer)</h3>
<p>Creates a new Mismatched Tree Nde Exception and inserts in the recognizer exception stack. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>recognizer</i> Context pointer for this recognizer</dl>
<p> References ANTLR3_MISMATCHED_TREE_NODE_EXCEPTION, ANTLR3_MISMATCHED_TREE_NODE_NAME, antlr3RecognitionExceptionNew(), ANTLR3_RECOGNIZER_SHARED_STATE_struct::exception, ANTLR3_EXCEPTION_struct::name, ANTLR3_BASE_RECOGNIZER_struct::state, and ANTLR3_EXCEPTION_struct::type. </p>
<p> Referenced by antlr3TreeParserNewStream().</p>
<h3>ANTLR3_API <code>pANTLR3_INPUT_STREAM</code> antlr3NewAsciiStringCopyStream (<code>pANTLR3_UINT8</code> inString, <code>ANTLR3_UINT32</code> size, <code>pANTLR3_UINT8</code> name)</h3>
<p>Create an ASCII string stream as input to ANTLR 3, copying the input string. This string stream first makes a copy of the string at the supplied pointer </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>inString</i> Pointer to the string to be copied as the input stream<br />
 <i>size</i> Size (in 8 bit ASCII characters) of the input string<br />
 <i>name</i> NAme to attach the input stream (can be NULL pointer)</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>*</p>
<dd>Pointer to new input stream context upon success</p>
<dt>*</p>
<dd>One of the ANTLR3_ERR_ defines on error.</dl>
</dl>
<p> <code>Remarks:</code></p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>*</p>
<dd>ANTLR does not alter the input string in any way.</p>
<dt>*</p>
<dd>String is slightly incorrect in that the passed in pointer can be to any memory in C version of ANTLR3 of course.</dl>
</dl>
<p> References ANTLR3_CHARSTREAM, ANTLR3_MALLOC, ANTLR3_MEMMOVE, ANTLR3_TRUE, antlr3AsciiSetupStream(), ANTLR3_INPUT_STREAM_struct::data, ANTLR3_INPUT_STREAM_struct::fileName, ANTLR3_INPUT_STREAM_struct::isAllocated, ANTLR3_INPUT_STREAM_struct::istream, ANTLR3_STRING_FACTORY_struct::newStr, ANTLR3_INPUT_STREAM_struct::sizeBuf, ANTLR3_INT_STREAM_struct::streamName, and ANTLR3_INPUT_STREAM_struct::strFactory.</p>
<h3>ANTLR3_API <code>pANTLR3_INPUT_STREAM</code> antlr3NewAsciiStringInPlaceStream (<code>pANTLR3_UINT8</code> inString, <code>ANTLR3_UINT32</code> size, <code>pANTLR3_UINT8</code> name)</h3>
<p>Create an in-place ASCII string stream as input to ANTLR 3. An in-place string steam is the preferred method of supplying strings to ANTLR as input for lexing and compiling. This is because we make no copies of the input string but read from it right where it is. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>inString</i> Pointer to the string to be used as the input stream<br />
 <i>size</i> Size (in 8 bit ASCII characters) of the input string<br />
 <i>name</i> NAme to attach the input stream (can be NULL pointer)</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>*</p>
<dd>Pointer to new input stream context upon success</p>
<dt>*</p>
<dd>One of the ANTLR3_ERR_ defines on error.</dl>
</dl>
<p> <code>Remarks:</code></p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>*</p>
<dd>ANTLR does not alter the input string in any way.</p>
<dt>*</p>
<dd>String is slightly incorrect in that the passed in pointer can be to any memory in C version of ANTLR3 of course.</dl>
</dl>
<p> References ANTLR3_CHARSTREAM, ANTLR3_FALSE, ANTLR3_MALLOC, antlr3AsciiSetupStream(), ANTLR3_INPUT_STREAM_struct::data, ANTLR3_INPUT_STREAM_struct::fileName, ANTLR3_INPUT_STREAM_struct::isAllocated, ANTLR3_INPUT_STREAM_struct::istream, ANTLR3_STRING_FACTORY_struct::newStr, ANTLR3_INPUT_STREAM_struct::sizeBuf, ANTLR3_INT_STREAM_struct::streamName, and ANTLR3_INPUT_STREAM_struct::strFactory.</p>
<h3>ANTLR3_API <code>pANTLR3_INPUT_STREAM</code> antlr3NewUCS2StringInPlaceStream (<code>pANTLR3_UINT16</code> inString, <code>ANTLR3_UINT32</code> size, <code>pANTLR3_UINT16</code> name)</h3>
<p>Create an in-place UCS2 string stream as input to ANTLR 3. An in-place string steam is the preferred method of supplying strings to ANTLR as input for lexing and compiling. This is because we make no copies of the input string but read from it right where it is. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>inString</i> Pointer to the string to be used as the input stream<br />
 <i>size</i> Size (in 16 bit ASCII characters) of the input string<br />
 <i>name</i> Name to attach the input stream (can be NULL pointer)</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>*</p>
<dd>Pointer to new input stream context upon success</p>
<dt>*</p>
<dd>One of the ANTLR3_ERR_ defines on error.</dl>
</dl>
<p> <code>Remarks:</code></p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>*</p>
<dd>ANTLR does not alter the input string in any way.</p>
<dt>*</p>
<dd>String is slightly incorrect in that the passed in pointer can be to any memory in C version of ANTLR3 of course.</dl>
</dl>
<p> References ANTLR3_CHARSTREAM, ANTLR3_FALSE, ANTLR3_MALLOC, antlr3UCS2SetupStream(), ANTLR3_INPUT_STREAM_struct::data, ANTLR3_INPUT_STREAM_struct::fileName, ANTLR3_INPUT_STREAM_struct::isAllocated, ANTLR3_INPUT_STREAM_struct::istream, ANTLR3_STRING_FACTORY_struct::newStr, ANTLR3_INPUT_STREAM_struct::sizeBuf, ANTLR3_INT_STREAM_struct::streamName, and ANTLR3_INPUT_STREAM_struct::strFactory.</p>
<h3>ANTLR3_API <code>pANTLR3_PARSER</code> antlr3ParserNew (<code>ANTLR3_UINT32</code> sizeHint, <code>pANTLR3_RECOGNIZER_SHARED_STATE</code> state)</h3>
<p>References ANTLR3_MALLOC, ANTLR3_TYPE_PARSER, antlr3BaseRecognizerNew(), antlr3MTExceptionNew(), ANTLR3_BASE_RECOGNIZER_struct::exConstruct, ANTLR3_PARSER_struct::free, freeParser(), getTokenStream(), ANTLR3_PARSER_struct::getTokenStream, ANTLR3_PARSER_struct::rec, setDebugListener(), ANTLR3_PARSER_struct::setDebugListener, setTokenStream(), ANTLR3_PARSER_struct::setTokenStream, and ANTLR3_BASE_RECOGNIZER_struct::super. </p>
<p> Referenced by antlr3ParserNewStream().</p>
<h3>ANTLR3_API <code>pANTLR3_PARSER</code> antlr3ParserNewStream (<code>ANTLR3_UINT32</code> sizeHint, <code>pANTLR3_TOKEN_STREAM</code> tstream, <code>pANTLR3_RECOGNIZER_SHARED_STATE</code> state)</h3>
<p>References antlr3ParserNew(), and ANTLR3_PARSER_struct::setTokenStream. </p>
<p> Referenced by antlr3ParserNewStreamDbg().</p>
<h3>ANTLR3_API <code>pANTLR3_PARSER</code> antlr3ParserNewStreamDbg (<code>ANTLR3_UINT32</code> sizeHint, <code>pANTLR3_TOKEN_STREAM</code> tstream, <code>pANTLR3_DEBUG_EVENT_LISTENER</code> dbg, <code>pANTLR3_RECOGNIZER_SHARED_STATE</code> state)</h3>
<p>References antlr3ParserNewStream(), and ANTLR3_PARSER_struct::setDebugListener.</p>
<h3>ANTLR3_API <code>pANTLR3_REWRITE_RULE_NODE_STREAM</code> antlr3RewriteRuleNODEStreamNewAE (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_RECOGNIZER</code> rec, <code>pANTLR3_UINT8</code> description)</h3>
<p>References antlr3RewriteRuleElementStreamNewAE(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::dup, dupTreeNode(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::free, freeNodeRS(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::nextNode, nextNodeNode(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::toTree, and toTreeNode().</p>
<h3>ANTLR3_API <code>pANTLR3_REWRITE_RULE_NODE_STREAM</code> antlr3RewriteRuleNODEStreamNewAEE (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_RECOGNIZER</code> rec, <code>pANTLR3_UINT8</code> description, void * oneElement)</h3>
<p>References antlr3RewriteRuleElementStreamNewAEE(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::dup, dupTreeNode(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::free, freeNodeRS(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::nextNode, nextNodeNode(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::toTree, and toTreeNode().</p>
<h3>ANTLR3_API <code>pANTLR3_REWRITE_RULE_NODE_STREAM</code> antlr3RewriteRuleNODEStreamNewAEV (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_RECOGNIZER</code> rec, <code>pANTLR3_UINT8</code> description, <code>pANTLR3_VECTOR</code> vector)</h3>
<p>References antlr3RewriteRuleElementStreamNewAEV(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::dup, dupTreeNode(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::free, freeNodeRS(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::nextNode, nextNodeNode(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::toTree, and toTreeNode().</p>
<h3>ANTLR3_API <code>pANTLR3_REWRITE_RULE_SUBTREE_STREAM</code> antlr3RewriteRuleSubtreeStreamNewAE (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_RECOGNIZER</code> rec, <code>pANTLR3_UINT8</code> description)</h3>
<p>References antlr3RewriteRuleElementStreamNewAE(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::dup, dupTree(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::free, freeNodeRS(), nextNode(), and ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::nextNode.</p>
<h3>ANTLR3_API <code>pANTLR3_REWRITE_RULE_SUBTREE_STREAM</code> antlr3RewriteRuleSubtreeStreamNewAEE (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_RECOGNIZER</code> rec, <code>pANTLR3_UINT8</code> description, void * oneElement)</h3>
<p>References antlr3RewriteRuleElementStreamNewAEE(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::dup, dupTree(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::free, freeNodeRS(), nextNode(), and ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::nextNode.</p>
<h3>ANTLR3_API <code>pANTLR3_REWRITE_RULE_SUBTREE_STREAM</code> antlr3RewriteRuleSubtreeStreamNewAEV (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_RECOGNIZER</code> rec, <code>pANTLR3_UINT8</code> description, <code>pANTLR3_VECTOR</code> vector)</h3>
<p>References antlr3RewriteRuleElementStreamNewAEV(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::dup, dupTree(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::free, freeNodeRS(), nextNode(), and ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::nextNode.</p>
<h3>ANTLR3_API <code>pANTLR3_REWRITE_RULE_TOKEN_STREAM</code> antlr3RewriteRuleTOKENStreamNewAE (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_RECOGNIZER</code> rec, <code>pANTLR3_UINT8</code> description)</h3>
<p>References antlr3RewriteRuleElementStreamNewAE(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::dup, dupTok(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::nextNode, and nextNodeToken().</p>
<h3>ANTLR3_API <code>pANTLR3_REWRITE_RULE_TOKEN_STREAM</code> antlr3RewriteRuleTOKENStreamNewAEE (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_RECOGNIZER</code> rec, <code>pANTLR3_UINT8</code> description, void * oneElement)</h3>
<p>References antlr3RewriteRuleElementStreamNewAEE(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::dup, dupTok(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::nextNode, and nextNodeToken().</p>
<h3>ANTLR3_API <code>pANTLR3_REWRITE_RULE_TOKEN_STREAM</code> antlr3RewriteRuleTOKENStreamNewAEV (<code>pANTLR3_BASE_TREE_ADAPTOR</code> adaptor, <code>pANTLR3_BASE_RECOGNIZER</code> rec, <code>pANTLR3_UINT8</code> description, <code>pANTLR3_VECTOR</code> vector)</h3>
<p>References antlr3RewriteRuleElementStreamNewAEV(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::dup, dupTok(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::nextNode, and nextNodeToken().</p>
<h3>ANTLR3_API void antlr3SetCTAPI (<code>pANTLR3_COMMON_TREE</code> tree)</h3>
<p>References antlr3BaseTreeNew(), ANTLR3_COMMON_TREE_struct::baseTree, ANTLR3_COMMON_TREE_struct::childIndex, ANTLR3_BASE_TREE_struct::children, createChildrenList(), ANTLR3_BASE_TREE_struct::createChildrenList, dupNode(), ANTLR3_BASE_TREE_struct::dupNode, ANTLR3_BASE_TREE_struct::free, getCharPositionInLine(), ANTLR3_BASE_TREE_struct::getCharPositionInLine, getChildIndex(), ANTLR3_BASE_TREE_struct::getChildIndex, getLine(), ANTLR3_BASE_TREE_struct::getLine, getParent(), ANTLR3_BASE_TREE_struct::getParent, getText(), ANTLR3_BASE_TREE_struct::getText, getToken(), ANTLR3_BASE_TREE_struct::getToken, getType(), ANTLR3_BASE_TREE_struct::getType, isNilNode(), ANTLR3_BASE_TREE_struct::isNilNode, ANTLR3_COMMON_TREE_struct::parent, reuse(), ANTLR3_BASE_TREE_struct::reuse, setChildIndex(), ANTLR3_BASE_TREE_struct::setChildIndex, setParent(), ANTLR3_BASE_TREE_struct::setParent, ANTLR3_COMMON_TREE_struct::startIndex, ANTLR3_COMMON_TREE_struct::stopIndex, ANTLR3_BASE_TREE_struct::super, ANTLR3_COMMON_TREE_struct::token, toString(), and ANTLR3_BASE_TREE_struct::toString. </p>
<p> Referenced by antlr3ArboretumNew(), antlr3CommonTreeNew(), antlr3CommonTreeNodeStreamNew(), antlr3CommonTreeNodeStreamNewStream(), and newPoolTree().</p>
<h3>ANTLR3_API void antlr3SetTokenAPI (<code>pANTLR3_COMMON_TOKEN</code> token)</h3>
<p>References ANTLR3_TEXT_NONE, ANTLR3_TOKEN_DEFAULT_CHANNEL, ANTLR3_TOKEN_INVALID, ANTLR3_COMMON_TOKEN_struct::channel, ANTLR3_COMMON_TOKEN_struct::custom, ANTLR3_COMMON_TOKEN_struct::freeCustom, getChannel(), ANTLR3_COMMON_TOKEN_struct::getChannel, getCharPositionInLine(), ANTLR3_COMMON_TOKEN_struct::getCharPositionInLine, getLine(), ANTLR3_COMMON_TOKEN_struct::getLine, getStartIndex(), ANTLR3_COMMON_TOKEN_struct::getStartIndex, getStopIndex(), ANTLR3_COMMON_TOKEN_struct::getStopIndex, getText(), ANTLR3_COMMON_TOKEN_struct::getText, getTokenIndex(), ANTLR3_COMMON_TOKEN_struct::getTokenIndex, getType(), ANTLR3_COMMON_TOKEN_struct::getType, ANTLR3_COMMON_TOKEN_struct::index, ANTLR3_COMMON_TOKEN_struct::input, ANTLR3_COMMON_TOKEN_struct::line, setChannel(), ANTLR3_COMMON_TOKEN_struct::setChannel, setCharPositionInLine(), ANTLR3_COMMON_TOKEN_struct::setCharPositionInLine, setLine(), ANTLR3_COMMON_TOKEN_struct::setLine, setStartIndex(), ANTLR3_COMMON_TOKEN_struct::setStartIndex, setStopIndex(), ANTLR3_COMMON_TOKEN_struct::setStopIndex, setText(), ANTLR3_COMMON_TOKEN_struct::setText, setText8(), ANTLR3_COMMON_TOKEN_struct::setText8, setTokenIndex(), ANTLR3_COMMON_TOKEN_struct::setTokenIndex, setType(), ANTLR3_COMMON_TOKEN_struct::setType, ANTLR3_COMMON_TOKEN_struct::start, ANTLR3_COMMON_TOKEN_struct::stop, ANTLR3_COMMON_TOKEN_struct::textState, toString(), ANTLR3_COMMON_TOKEN_struct::toString, ANTLR3_COMMON_TOKEN_struct::type, ANTLR3_COMMON_TOKEN_struct::user1, ANTLR3_COMMON_TOKEN_struct::user2, and ANTLR3_COMMON_TOKEN_struct::user3. </p>
<p> Referenced by antlr3LexerNew(), antlr3TokenFactoryNew(), newPoolToken(), and newToken().</p>
<h3>ANTLR3_API void antlr3SetVectorApi (<code>pANTLR3_VECTOR</code> vector, <code>ANTLR3_UINT32</code> sizeHint)</h3>
<p>References ANTLR3_VECTOR_struct::add, ANTLR3_FALSE, ANTLR3_FREE, ANTLR3_MALLOC, ANTLR3_VECTOR_INTERNAL_SIZE, antlr3VectorAdd(), antlr3VectorClear(), antlr3VectorDel(), antlr3VectorFree(), antlr3VectorGet(), antlr3VectorSet(), antlr3VectorSize(), antlr3VectorSwap(), antrl3VectorRemove(), ANTLR3_VECTOR_struct::clear, ANTLR3_VECTOR_struct::count, ANTLR3_VECTOR_struct::del, ANTLR3_VECTOR_struct::elements, ANTLR3_VECTOR_struct::elementsSize, ANTLR3_VECTOR_struct::factoryMade, ANTLR3_VECTOR_struct::get, ANTLR3_VECTOR_struct::internal, ANTLR3_VECTOR_struct::remove, ANTLR3_VECTOR_struct::set, ANTLR3_VECTOR_struct::size, and ANTLR3_VECTOR_struct::swap. </p>
<p> Referenced by antlr3VectorFactoryNew(), antlr3VectorNew(), and newVector().</p>
<h3>ANTLR3_API <code>pANTLR3_STACK</code> antlr3StackNew (<code>ANTLR3_UINT32</code> sizeHint)</h3>
<p>References ANTLR3_ERR_NOMEM, ANTLR3_FUNC_PTR, ANTLR3_MALLOC, antlr3StackFree(), antlr3StackGet(), antlr3StackPeek(), antlr3StackPop(), antlr3StackPush(), antlr3StackSize(), antlr3VectorNew(), ANTLR3_STACK_struct::free, ANTLR3_STACK_struct::get, ANTLR3_STACK_struct::peek, ANTLR3_STACK_struct::pop, ANTLR3_STACK_struct::push, ANTLR3_STACK_struct::size, ANTLR3_STACK_struct::top, and ANTLR3_STACK_struct::vector. </p>
<p> Referenced by antlr3ArboretumNew(), antlr3CommonTreeNodeStreamNew(), antlr3VectorFactoryNew(), pushCharStream(), and reset().</p>
<h3>ANTLR3_API <code>pANTLR3_STRING_FACTORY</code> antlr3StringFactoryNew (void)</h3>
<p>References ANTLR3_FREE, ANTLR3_MALLOC, antlr3VectorNew(), ANTLR3_STRING_FACTORY_struct::close, closeFactory(), destroy(), ANTLR3_STRING_FACTORY_struct::destroy, ANTLR3_STRING_FACTORY_struct::index, ANTLR3_STRING_FACTORY_struct::newPtr, ANTLR3_STRING_FACTORY_struct::newPtr8, newPtr8(), ANTLR3_STRING_FACTORY_struct::newRaw, newRaw8(), ANTLR3_STRING_FACTORY_struct::newSize, newSize8(), ANTLR3_STRING_FACTORY_struct::newStr, ANTLR3_STRING_FACTORY_struct::newStr8, newStr8(), ANTLR3_STRING_FACTORY_struct::printable, printable8(), and ANTLR3_STRING_FACTORY_struct::strings. </p>
<p> Referenced by antlr3AsciiSetupStream(), and antlr3UCS2StringFactoryNew().</p>
<h3>ANTLR3_API <code>pANTLR3_TOKEN_FACTORY</code> antlr3TokenFactoryNew (<code>pANTLR3_INPUT_STREAM</code> input)</h3>
<p>References ANTLR3_MALLOC, ANTLR3_TRUE, antlr3SetTokenAPI(), ANTLR3_TOKEN_FACTORY_struct::close, factoryClose(), ANTLR3_COMMON_TOKEN_struct::factoryMade, newPool(), newPoolToken(), ANTLR3_TOKEN_FACTORY_struct::newToken, ANTLR3_TOKEN_FACTORY_struct::pools, setInputStream(), ANTLR3_TOKEN_FACTORY_struct::setInputStream, ANTLR3_TOKEN_FACTORY_struct::thisPool, and ANTLR3_TOKEN_FACTORY_struct::unTruc. </p>
<p> Referenced by ANTLR3_TREE_ADAPTORNew(), getMissingSymbol(), and setCharStream().</p>
<h3>ANTLR3_API <code>pANTLR3_TOPO</code> antlr3TopoNew ()</h3>
<p>Allocate and initialize a new ANTLR3 topological sorter, which can be used to define edges that identify numerical node indexes that depend on other numerical node indexes, which can then be sorted topologically such that any node is sorted after all its dependent nodes. Use: </p>
<p> /verbatim </p>
<p> pANTLR3_TOPO topo; topo = antlr3NewTopo(); </p>
<p> if (topo == NULL) { out of memory } </p>
<p> topo-&gt;addEdge(topo, 3, 0); // Node 3 depends on node 0 topo-&gt;addEdge(topo, 0, 1); // Node &#8211; depends on node 1 topo-&gt;sortVector(topo, myVector); // Sort the vector in place (node numbers are the vector entry numbers) </p>
<p> /verbatim </p>
<p> References addEdge(), ANTLR3_TOPO_struct::addEdge, ANTLR3_FALSE, ANTLR3_MALLOC, ANTLR3_TOPO_struct::cycle, ANTLR3_TOPO_struct::cycleMark, ANTLR3_TOPO_struct::edges, ANTLR3_TOPO_struct::free, freeTopo(), ANTLR3_TOPO_struct::hasCycle, ANTLR3_TOPO_struct::limit, ANTLR3_TOPO_struct::sorted, sortToArray(), ANTLR3_TOPO_struct::sortToArray, sortVector(), ANTLR3_TOPO_struct::sortVector, and ANTLR3_TOPO_struct::visited.</p>
<h3>ANTLR3_API <code>pANTLR3_TREE_NODE_STREAM</code> antlr3TreeNodeStreamNew ()</h3>
<p>References ANTLR3_CALLOC, antlr3TreeNodeStreamFree(), ANTLR3_TREE_NODE_STREAM_struct::free, replaceChildren(), and ANTLR3_TREE_NODE_STREAM_struct::replaceChildren. </p>
<p> Referenced by antlr3CommonTreeNodeStreamNew(), and antlr3CommonTreeNodeStreamNewStream().</p>
<h3>ANTLR3_API <code>pANTLR3_TREE_PARSER</code> antlr3TreeParserNewStream (<code>ANTLR3_UINT32</code> sizeHint, <code>pANTLR3_COMMON_TREE_NODE_STREAM</code> ctnstream, <code>pANTLR3_RECOGNIZER_SHARED_STATE</code> state)</h3>
<p>Allocate tree parser memory </p>
<p> References ANTLR3_MALLOC, ANTLR3_TYPE_PARSER, ANTLR3_TYPE_TREE_PARSER, antlr3BaseRecognizerNew(), antlr3MTNExceptionNew(), ANTLR3_BASE_RECOGNIZER_struct::exConstruct, ANTLR3_TREE_PARSER_struct::free, freeParser(), getCurrentInputSymbol(), ANTLR3_BASE_RECOGNIZER_struct::getCurrentInputSymbol, getMissingSymbol(), ANTLR3_BASE_RECOGNIZER_struct::getMissingSymbol, getTreeNodeStream(), ANTLR3_TREE_PARSER_struct::getTreeNodeStream, mismatch(), ANTLR3_BASE_RECOGNIZER_struct::mismatch, ANTLR3_TREE_PARSER_struct::rec, setTreeNodeStream(), ANTLR3_TREE_PARSER_struct::setTreeNodeStream, ANTLR3_BASE_RECOGNIZER_struct::super, and ANTLR3_BASE_RECOGNIZER_struct::type.</p>
<h3>ANTLR3_API <code>pANTLR3_STRING_FACTORY</code> antlr3UCS2StringFactoryNew (void)</h3>
<p>Create a string factory that is UCS2 (16 bit) encoding based. </p>
<p> References antlr3StringFactoryNew(), ANTLR3_STRING_FACTORY_struct::close, closeFactory(), destroy(), ANTLR3_STRING_FACTORY_struct::destroy, ANTLR3_STRING_FACTORY_struct::newPtr, newPtr16_16(), newPtr16_8(), ANTLR3_STRING_FACTORY_struct::newPtr8, ANTLR3_STRING_FACTORY_struct::newRaw, newRaw16(), ANTLR3_STRING_FACTORY_struct::newSize, newSize16(), ANTLR3_STRING_FACTORY_struct::newStr, newStr16_16(), newStr16_8(), ANTLR3_STRING_FACTORY_struct::newStr8, ANTLR3_STRING_FACTORY_struct::printable, and printable16(). </p>
<p> Referenced by antlr3UCS2SetupStream().</p>
<h3>ANTLR3_API <code>pANTLR3_COMMON_TREE_NODE_STREAM</code> antlr3UnbufTreeNodeStreamNew (<code>pANTLR3_STRING_FACTORY</code> strFactory, <code>ANTLR3_UINT32</code> hint)</h3>
<h3>ANTLR3_API <code>pANTLR3_COMMON_TREE_NODE_STREAM</code> antlr3UnbufTreeNodeStreamNewTree (<code>pANTLR3_BASE_TREE</code> tree, <code>ANTLR3_UINT32</code> hint)</h3>
<h3>ANTLR3_API <code>pANTLR3_VECTOR_FACTORY</code> antlr3VectorFactoryNew (<code>ANTLR3_UINT32</code> sizeHint)</h3>
<p>Vector factory creation. </p>
<p> References ANTLR3_MALLOC, ANTLR3_TRUE, ANTLR3_VECTOR_INTERNAL_SIZE, antlr3SetVectorApi(), antlr3StackNew(), ANTLR3_VECTOR_FACTORY_struct::close, closeVectorFactory(), ANTLR3_VECTOR_struct::factoryMade, ANTLR3_VECTOR_FACTORY_struct::freeStack, newPool(), newVector(), ANTLR3_VECTOR_FACTORY_struct::newVector, ANTLR3_VECTOR_FACTORY_struct::pools, returnVector(), ANTLR3_VECTOR_FACTORY_struct::returnVector, ANTLR3_VECTOR_FACTORY_struct::thisPool, and ANTLR3_VECTOR_FACTORY_struct::unTruc. </p>
<p> Referenced by antlr3ArboretumNew().</p>
<h3>ANTLR3_API <code>pANTLR3_VECTOR</code> antlr3VectorNew (<code>ANTLR3_UINT32</code> sizeHint)</h3>
<p>References ANTLR3_ERR_NOMEM, ANTLR3_FUNC_PTR, ANTLR3_MALLOC, and antlr3SetVectorApi(). </p>
<p> Referenced by antlr3BaseRecognizerNew(), antlr3CommonTokenStreamNew(), antlr3CommonTreeNodeStreamNew(), antlr3CommonTreeNodeStreamNewStream(), antlr3InputReset(), antlr3StackNew(), antlr3StringFactoryNew(), and replaceChildren().</p>
<h3>ANTLR3_API void fillBufferExt (<code>pANTLR3_COMMON_TOKEN_STREAM</code> tokenStream)</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for ANTLR3C from the source code.</p>
