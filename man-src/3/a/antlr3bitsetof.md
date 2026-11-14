---
title: "antlr3bitsetof(3)"
name: "antlr3bitsetof"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3bitsetof/"
---

include/antlr3defs.h - 

 Basic type and constant definitions for ANTLR3 Runtime.
<h2>Synopsis</h2>#include &lt;<a HREF="file:/usr/include/antlr3errors.h">antlr3errors.h</a>&gt; 
 #include &lt;<a HREF="file:/usr/include/antlr3config.h">antlr3config.h</a>&gt; 
 #include &lt;<a HREF="file:/usr/include/stdio.h">stdio.h</a>&gt; 
 #include &lt;<a HREF="file:/usr/include/antlr3interfaces.h">antlr3interfaces.h</a>&gt; 
 #include &lt;<a HREF="file:/usr/include/antlr3convertutf.h">antlr3convertutf.h</a>&gt; 
 

<h3>Defines</h3>#define <b>_stat</b> stat 
 
 #define <b>ANTLR3_API</b> 
 
 #define <b>ANTLR3_API</b> 
 
 #define <b>ANTLR3_AVERAGE</b> 
 
 #define <b>ANTLR3_CALLOC</b>(numEl, elSize) calloc (numEl, (size_t)(elSize)) 
 <i>Default definition of ANTLR3_CALLOC. </i> 
 #define <b>ANTLR3_CDECL</b> 
 
 #define <b>ANTLR3_CLOSESOCKET</b> close 
 
 #define <b>ANTLR3_ENCODING_LATIN1</b> 0 
 
 #define <b>ANTLR3_ENCODING_UCS2</b> 1 
 
 #define <b>ANTLR3_ENCODING_UTF32</b> 3 
 
 #define <b>ANTLR3_ENCODING_UTF8</b> 2 
 
 #define <b>ANTLR3_FASTCALL</b> 
 
 #define <b>ANTLR3_FPRINTF</b> fprintf 
 <i>Default definition of fprintf, set this to something other than fprintf before including </i><b>antlr3.h</b> if your system does not have a fprintf. 
 #define <b>ANTLR3_FREE</b>(ptr) free ((void *)(ptr)) 
 <i>Default definition of ANTLR3_FREE. </i> 
 #define <b>ANTLR3_FREE_FUNC</b> free 
 <i>Default definition of ANTLR3_FREE_FUNC . </i> 
 #define <b>ANTLR3_FUNC_PTR</b>(ptr) (void *)((<b>ANTLR3_UINT32</b>)(ptr)) 
 
 #define <b>ANTLR3_INLINE</b> inline 
 
 #define <b>ANTLR3_LIST_SIZE_HINT</b> 63 
 
 #define <b>ANTLR3_MALLOC</b>(request) malloc ((size_t)(request)) 
 <i>Default definition of ANTLR3_MALLOC. </i> 
 #define <b>ANTLR3_MEMCPY</b>(target, source, size) memcpy((void *)(target), (const void *)(source), (size_t)(size)) 
 <i>Default definition of ANTLR3_MEMCPY. </i> 
 #define <b>ANTLR3_MEMMOVE</b>(target, source, size) memmove((void *)(target), (const void *)(source), (size_t)(size)) 
 <i>Default definition of ANTLR3_MEMMOVE. </i> 
 #define <b>ANTLR3_MEMSET</b>(target, byte, size) memset((void *)(target), (int)(byte), (size_t)(size)) 
 <i>Default definition of ANTLR3_MEMSET. </i> 
 #define <b>ANTLR3_PRINTF</b> printf 
 <i>Default definition of printf, set this to something other than printf before including </i><b>antlr3.h</b> if your system does not have a printf. 
 #define <b>ANTLR3_REALLOC</b>(current, request) realloc ((void *)(current), (size_t)(request)) 
 <i>Default definition of ANTLR3_REALLOC. </i> 
 #define <b>ANTLR3_SIZE_HINT</b> 1025 
 
 #define <b>ANTLR3_STRDUP</b>(instr) (<b>pANTLR3_UINT8</b>)(strdup ((const char *)(instr))) 
 <i>Default definition of ANTLR3_STRDUP. </i> 
 #define <b>ANTLR3_TRIE_DEPTH</b> 31 
 
 #define <b>ANTLR3_UINT32_CAST</b>(ptr) (<b>ANTLR3_UINT32</b>)(ptr) 
 
 #define <b>ANTLR3_UINT64_CAST</b>(ptr) (<b>ANTLR3_UINT64</b>)((<b>ANTLR3_UINT32</b>)(ptr)) 
 
 #define <b>ANTLR3_UINT64_LIT</b>(lit) lit##ULL 
 
 #define <b>INVALID_SOCKET</b> ((<b>SOCKET</b>)-1) 

<h3>Typedefs</h3>typedef uint64_t <b>ANTLR3_BITWORD</b> 
 
 typedef uint32_t <b>ANTLR3_BOOLEAN</b> 
 
 typedef int32_t <b>ANTLR3_CHAR</b> 
 
 typedef FILE * <b>ANTLR3_FDSC</b> 
 
 typedef struct stat <b>ANTLR3_FSTAT_STRUCT</b> 
 
 typedef int16_t <b>ANTLR3_INT16</b> 
 
 typedef int32_t <b>ANTLR3_INT32</b> 
 
 typedef int64_t <b>ANTLR3_INT64</b> 
 
 typedef int8_t <b>ANTLR3_INT8</b> 
 
 typedef <b>ANTLR3_UINT32</b> <b>ANTLR3_INTKEY</b> 
 
 typedef <b>ANTLR3_INT32</b> <b>ANTLR3_MARKER</b> 
 
 typedef size_t <b>ANTLR3_SALENT</b> 
 
 typedef struct sockaddr_in <b>ANTLR3_SOCKADDRT</b> 
 
 typedef uint32_t <b>ANTLR3_UCHAR</b> 
 
 typedef uint16_t <b>ANTLR3_UINT16</b> 
 
 typedef uint32_t <b>ANTLR3_UINT32</b> 
 
 typedef uint64_t <b>ANTLR3_UINT64</b> 
 
 typedef uint8_t <b>ANTLR3_UINT8</b> 
 
 typedef uint64_t * <b>pANTLR3_BITWORD</b> 
 
 typedef uint32_t * <b>pANTLR3_BOOLEAN</b> 
 
 typedef int32_t * <b>pANTLR3_CHAR</b> 
 
 typedef int16_t * <b>pANTLR3_INT16</b> 
 
 typedef int32_t * <b>pANTLR3_INT32</b> 
 
 typedef int64_t * <b>pANTLR3_INT64</b> 
 
 typedef int8_t * <b>pANTLR3_INT8</b> 
 
 typedef struct sockaddr * <b>pANTLR3_SOCKADDRC</b> 
 
 typedef struct sockaddr_in * <b>pANTLR3_SOCKADDRT</b> 
 
 typedef uint32_t * <b>pANTLR3_UCHAR</b> 
 
 typedef uint16_t * <b>pANTLR3_UINT16</b> 
 
 typedef uint32_t * <b>pANTLR3_UINT32</b> 
 
 typedef uint64_t * <b>pANTLR3_UINT64</b> 
 
 typedef uint8_t * <b>pANTLR3_UINT8</b> 
 
 typedef int <b>SOCKET</b> 

<h3>Functions</h3>ANTLR3_API <b>pANTLR3_BASE_TREE_ADAPTOR</b> <b>ANTLR3_TREE_ADAPTORDebugNew</b> (<b>pANTLR3_STRING_FACTORY</b> strFactory, <b>pANTLR3_DEBUG_EVENT_LISTENER</b> debugger) 
 <i>Debugging version of the tree adaptor (not normally called as generated code calls setDebugEventListener instead which changes a normal token stream to a debugging stream and means that a user's instantiation code does not need to be changed just to debug with AW. </i> 
 ANTLR3_API <b>pANTLR3_BASE_TREE_ADAPTOR</b> <b>ANTLR3_TREE_ADAPTORNew</b> (<b>pANTLR3_STRING_FACTORY</b> strFactory) 
 <i>Create a new tree adaptor. </i> 
 ANTLR3_API <b>pANTLR3_ARBORETUM</b> <b>antlr3ArboretumNew</b> (<b>pANTLR3_STRING_FACTORY</b> factory) 
 
 ANTLR3_API <b>pANTLR3_INPUT_STREAM</b> <b>antlr3AsciiFileStreamNew</b> (<b>pANTLR3_UINT8</b> fileName) 
 <i>Use the contents of an operating system file as the input for an input stream. </i> 
 ANTLR3_API <b>pANTLR3_BASE_RECOGNIZER</b> <b>antlr3BaseRecognizerNew</b> (<b>ANTLR3_UINT32</b> type, <b>ANTLR3_UINT32</b> sizeHint, <b>pANTLR3_RECOGNIZER_SHARED_STATE</b> state) 
 
 ANTLR3_API void <b>antlr3BaseTreeAdaptorInit</b> (<b>pANTLR3_BASE_TREE_ADAPTOR</b> adaptor, <b>pANTLR3_DEBUG_EVENT_LISTENER</b> debugger) 
 <i>Given a pointer to a base tree adaptor structure (which is usually embedded in the super class the implements the tree adaptor used in the parse), initialize its function pointers and so on. </i> 
 ANTLR3_API <b>pANTLR3_BASE_TREE</b> <b>antlr3BaseTreeNew</b> (<b>pANTLR3_BASE_TREE</b> tree) 
 
 ANTLR3_API <b>pANTLR3_BITSET</b> <b>antlr3BitsetCopy</b> (<b>pANTLR3_BITSET_LIST</b> blist) 
 
 ANTLR3_API <b>pANTLR3_BITSET</b> <b>antlr3BitsetList</b> (<b>pANTLR3_HASH_TABLE</b> list) 
 
 ANTLR3_API <b>pANTLR3_BITSET</b> <b>antlr3BitsetLoad</b> (<b>pANTLR3_BITSET_LIST</b> blist) 
 <i>Creates a new bitset with at least one 64 bit bset of bits, but as many 64 bit sets as are required. </i> 
 ANTLR3_API <b>pANTLR3_BITSET</b> <b>antlr3BitsetNew</b> (<b>ANTLR3_UINT32</b> numBits) 
 
 ANTLR3_API <b>pANTLR3_BITSET</b> <b>antlr3BitsetOf</b> (<b>ANTLR3_INT32</b> bit,...) 
 <i>Creates a new bitset with at least one element, but as many elements are required. </i> 
 ANTLR3_API void <b>antlr3BitsetSetAPI</b> (<b>pANTLR3_BITSET</b> bitset) 
 
 ANTLR3_API <b>ANTLR3_UCHAR</b> <b>antlr3c8toAntlrc</b> (<b>ANTLR3_INT8</b> inc) 
 <i>Provides basic utility functions to convert between the various Unicode character conversions. </i> 
 ANTLR3_API <b>pANTLR3_COMMON_TOKEN_STREAM</b> <b>antlr3CommonTokenDebugStreamSourceNew</b> (<b>ANTLR3_UINT32</b> hint, <b>pANTLR3_TOKEN_SOURCE</b> source, <b>pANTLR3_DEBUG_EVENT_LISTENER</b> debugger) 
 
 ANTLR3_API <b>pANTLR3_COMMON_TOKEN</b> <b>antlr3CommonTokenNew</b> (<b>ANTLR3_UINT32</b> ttype) 
 
 ANTLR3_API <b>pANTLR3_COMMON_TOKEN_STREAM</b> <b>antlr3CommonTokenStreamNew</b> (<b>ANTLR3_UINT32</b> hint) 
 
 ANTLR3_API <b>pANTLR3_COMMON_TOKEN_STREAM</b> <b>antlr3CommonTokenStreamSourceNew</b> (<b>ANTLR3_UINT32</b> hint, <b>pANTLR3_TOKEN_SOURCE</b> source) 
 
 ANTLR3_API <b>pANTLR3_COMMON_TREE</b> <b>antlr3CommonTreeNew</b> (void) 
 
 ANTLR3_API <b>pANTLR3_COMMON_TREE</b> <b>antlr3CommonTreeNewFromToken</b> (<b>pANTLR3_COMMON_TOKEN</b> tree) 
 
 ANTLR3_API <b>pANTLR3_COMMON_TREE</b> <b>antlr3CommonTreeNewFromTree</b> (<b>pANTLR3_COMMON_TREE</b> tree) 
 
 ANTLR3_API <b>pANTLR3_COMMON_TREE_NODE_STREAM</b> <b>antlr3CommonTreeNodeStreamNew</b> (<b>pANTLR3_STRING_FACTORY</b> strFactory, <b>ANTLR3_UINT32</b> hint) 
 
 ANTLR3_API <b>pANTLR3_COMMON_TREE_NODE_STREAM</b> <b>antlr3CommonTreeNodeStreamNewStream</b> (<b>pANTLR3_COMMON_TREE_NODE_STREAM</b> inStream) 
 
 ANTLR3_API <b>pANTLR3_COMMON_TREE_NODE_STREAM</b> <b>antlr3CommonTreeNodeStreamNewTree</b> (<b>pANTLR3_BASE_TREE</b> tree, <b>ANTLR3_UINT32</b> hint) 
 
 ANTLR3_API <b>pANTLR3_DEBUG_EVENT_LISTENER</b> <b>antlr3DebugListenerNew</b> () 
 <i>Create and initialize a new debug event listener that can be connected to by ANTLRWorks and any other debugger via a socket. </i> 
 ANTLR3_API <b>ANTLR3_INT32</b> <b>antlr3dfapredict</b> (void *ctx, <b>pANTLR3_BASE_RECOGNIZER</b> rec, <b>pANTLR3_INT_STREAM</b> is, <b>pANTLR3_CYCLIC_DFA</b> cdfa) 
 <i>From the input stream, predict what alternative will succeed using this DFA (representing the covering regular approximation to the underlying CFL). </i> 
 ANTLR3_API <b>ANTLR3_INT32</b> <b>antlr3dfaspecialStateTransition</b> (void *ctx, <b>pANTLR3_BASE_RECOGNIZER</b> rec, <b>pANTLR3_INT_STREAM</b> is, <b>pANTLR3_CYCLIC_DFA</b> dfa, <b>ANTLR3_INT32</b> s) 
 <i>Default special state implementation. </i> 
 ANTLR3_API <b>ANTLR3_INT32</b> <b>antlr3dfaspecialTransition</b> (void *ctx, <b>pANTLR3_BASE_RECOGNIZER</b> rec, <b>pANTLR3_INT_STREAM</b> is, <b>pANTLR3_CYCLIC_DFA</b> dfa, <b>ANTLR3_INT32</b> s) 
 
 ANTLR3_API <b>pANTLR3_HASH_ENUM</b> <b>antlr3EnumNew</b> (<b>pANTLR3_HASH_TABLE</b> table) 
 <i>Creates an enumeration structure to traverse the hash table. </i> 
 ANTLR3_API <b>pANTLR3_EXCEPTION</b> <b>antlr3ExceptionNew</b> (<b>ANTLR3_UINT32</b> exception, void *name, void *message, <b>ANTLR3_BOOLEAN</b> freeMessage) 
 <i>Creates a new ANTLR3 exception structure. </i> 
 ANTLR3_API <b>ANTLR3_UINT32</b> <b>antlr3Hash</b> (void *key, <b>ANTLR3_UINT32</b> keylen) 
 <i>Given an input key of arbitrary length, return a hash value of it. </i> 
 ANTLR3_API <b>pANTLR3_HASH_TABLE</b> <b>antlr3HashTableNew</b> (<b>ANTLR3_UINT32</b> sizeHint) 
 
 ANTLR3_API <b>pANTLR3_INT_STREAM</b> <b>antlr3IntStreamNew</b> (void) 
 
 ANTLR3_API <b>pANTLR3_INT_TRIE</b> <b>antlr3IntTrieNew</b> (<b>ANTLR3_UINT32</b> depth) 
 
 ANTLR3_API <b>pANTLR3_LEXER</b> <b>antlr3LexerNew</b> (<b>ANTLR3_UINT32</b> sizeHint, <b>pANTLR3_RECOGNIZER_SHARED_STATE</b> state) 
 
 ANTLR3_API <b>pANTLR3_LEXER</b> <b>antlr3LexerNewStream</b> (<b>ANTLR3_UINT32</b> sizeHint, <b>pANTLR3_INPUT_STREAM</b> input, <b>pANTLR3_RECOGNIZER_SHARED_STATE</b> state) 
 
 ANTLR3_API <b>pANTLR3_LIST</b> <b>antlr3ListNew</b> (<b>ANTLR3_UINT32</b> sizeHint) 
 
 ANTLR3_API void <b>antlr3MTExceptionNew</b> (<b>pANTLR3_BASE_RECOGNIZER</b> recognizer) 
 <i>Creates a new Mismatched Token Exception and inserts in the recognizer exception stack. </i> 
 ANTLR3_API void <b>antlr3MTNExceptionNew</b> (<b>pANTLR3_BASE_RECOGNIZER</b> recognizer) 
 <i>Creates a new Mismatched Tree Nde Exception and inserts in the recognizer exception stack. </i> 
 ANTLR3_API <b>pANTLR3_INPUT_STREAM</b> <b>antlr3NewAsciiStringCopyStream</b> (<b>pANTLR3_UINT8</b> inString, <b>ANTLR3_UINT32</b> size, <b>pANTLR3_UINT8</b> name) 
 <i>Create an ASCII string stream as input to ANTLR 3, copying the input string. </i> 
 ANTLR3_API <b>pANTLR3_INPUT_STREAM</b> <b>antlr3NewAsciiStringInPlaceStream</b> (<b>pANTLR3_UINT8</b> inString, <b>ANTLR3_UINT32</b> size, <b>pANTLR3_UINT8</b> name) 
 <i>Create an in-place ASCII string stream as input to ANTLR 3. </i> 
 ANTLR3_API <b>pANTLR3_INPUT_STREAM</b> <b>antlr3NewUCS2StringInPlaceStream</b> (<b>pANTLR3_UINT16</b> inString, <b>ANTLR3_UINT32</b> size, <b>pANTLR3_UINT16</b> name) 
 <i>Create an in-place UCS2 string stream as input to ANTLR 3. </i> 
 ANTLR3_API <b>pANTLR3_PARSER</b> <b>antlr3ParserNew</b> (<b>ANTLR3_UINT32</b> sizeHint, <b>pANTLR3_RECOGNIZER_SHARED_STATE</b> state) 
 
 ANTLR3_API <b>pANTLR3_PARSER</b> <b>antlr3ParserNewStream</b> (<b>ANTLR3_UINT32</b> sizeHint, <b>pANTLR3_TOKEN_STREAM</b> tstream, <b>pANTLR3_RECOGNIZER_SHARED_STATE</b> state) 
 
 ANTLR3_API <b>pANTLR3_PARSER</b> <b>antlr3ParserNewStreamDbg</b> (<b>ANTLR3_UINT32</b> sizeHint, <b>pANTLR3_TOKEN_STREAM</b> tstream, <b>pANTLR3_DEBUG_EVENT_LISTENER</b> dbg, <b>pANTLR3_RECOGNIZER_SHARED_STATE</b> state) 
 
 ANTLR3_API void <b>antlr3RecognitionExceptionNew</b> (<b>pANTLR3_BASE_RECOGNIZER</b> recognizer) 
 
 ANTLR3_API <b>pANTLR3_REWRITE_RULE_NODE_STREAM</b> <b>antlr3RewriteRuleNODEStreamNewAE</b> (<b>pANTLR3_BASE_TREE_ADAPTOR</b> adaptor, <b>pANTLR3_BASE_RECOGNIZER</b> rec, <b>pANTLR3_UINT8</b> description) 
 
 ANTLR3_API <b>pANTLR3_REWRITE_RULE_NODE_STREAM</b> <b>antlr3RewriteRuleNODEStreamNewAEE</b> (<b>pANTLR3_BASE_TREE_ADAPTOR</b> adaptor, <b>pANTLR3_BASE_RECOGNIZER</b> rec, <b>pANTLR3_UINT8</b> description, void *oneElement) 
 
 ANTLR3_API <b>pANTLR3_REWRITE_RULE_NODE_STREAM</b> <b>antlr3RewriteRuleNODEStreamNewAEV</b> (<b>pANTLR3_BASE_TREE_ADAPTOR</b> adaptor, <b>pANTLR3_BASE_RECOGNIZER</b> rec, <b>pANTLR3_UINT8</b> description, <b>pANTLR3_VECTOR</b> vector) 
 
 ANTLR3_API <b>pANTLR3_REWRITE_RULE_SUBTREE_STREAM</b> <b>antlr3RewriteRuleSubtreeStreamNewAE</b> (<b>pANTLR3_BASE_TREE_ADAPTOR</b> adaptor, <b>pANTLR3_BASE_RECOGNIZER</b> rec, <b>pANTLR3_UINT8</b> description) 
 
 ANTLR3_API <b>pANTLR3_REWRITE_RULE_SUBTREE_STREAM</b> <b>antlr3RewriteRuleSubtreeStreamNewAEE</b> (<b>pANTLR3_BASE_TREE_ADAPTOR</b> adaptor, <b>pANTLR3_BASE_RECOGNIZER</b> rec, <b>pANTLR3_UINT8</b> description, void *oneElement) 
 
 ANTLR3_API <b>pANTLR3_REWRITE_RULE_SUBTREE_STREAM</b> <b>antlr3RewriteRuleSubtreeStreamNewAEV</b> (<b>pANTLR3_BASE_TREE_ADAPTOR</b> adaptor, <b>pANTLR3_BASE_RECOGNIZER</b> rec, <b>pANTLR3_UINT8</b> description, <b>pANTLR3_VECTOR</b> vector) 
 
 ANTLR3_API <b>pANTLR3_REWRITE_RULE_TOKEN_STREAM</b> <b>antlr3RewriteRuleTOKENStreamNewAE</b> (<b>pANTLR3_BASE_TREE_ADAPTOR</b> adaptor, <b>pANTLR3_BASE_RECOGNIZER</b> rec, <b>pANTLR3_UINT8</b> description) 
 
 ANTLR3_API <b>pANTLR3_REWRITE_RULE_TOKEN_STREAM</b> <b>antlr3RewriteRuleTOKENStreamNewAEE</b> (<b>pANTLR3_BASE_TREE_ADAPTOR</b> adaptor, <b>pANTLR3_BASE_RECOGNIZER</b> rec, <b>pANTLR3_UINT8</b> description, void *oneElement) 
 
 ANTLR3_API <b>pANTLR3_REWRITE_RULE_TOKEN_STREAM</b> <b>antlr3RewriteRuleTOKENStreamNewAEV</b> (<b>pANTLR3_BASE_TREE_ADAPTOR</b> adaptor, <b>pANTLR3_BASE_RECOGNIZER</b> rec, <b>pANTLR3_UINT8</b> description, <b>pANTLR3_VECTOR</b> vector) 
 
 ANTLR3_API void <b>antlr3SetCTAPI</b> (<b>pANTLR3_COMMON_TREE</b> tree) 
 
 ANTLR3_API void <b>antlr3SetTokenAPI</b> (<b>pANTLR3_COMMON_TOKEN</b> token) 
 
 ANTLR3_API void <b>antlr3SetVectorApi</b> (<b>pANTLR3_VECTOR</b> vector, <b>ANTLR3_UINT32</b> sizeHint) 
 
 ANTLR3_API <b>pANTLR3_STACK</b> <b>antlr3StackNew</b> (<b>ANTLR3_UINT32</b> sizeHint) 
 
 ANTLR3_API <b>pANTLR3_STRING_FACTORY</b> <b>antlr3StringFactoryNew</b> (void) 
 
 ANTLR3_API <b>pANTLR3_TOKEN_FACTORY</b> <b>antlr3TokenFactoryNew</b> (<b>pANTLR3_INPUT_STREAM</b> input) 
 
 ANTLR3_API <b>pANTLR3_TOPO</b> <b>antlr3TopoNew</b> () 
 <i>Allocate and initialize a new ANTLR3 topological sorter, which can be used to define edges that identify numerical node indexes that depend on other numerical node indexes, which can then be sorted topologically such that any node is sorted after all its dependent nodes. </i> 
 ANTLR3_API <b>pANTLR3_TREE_NODE_STREAM</b> <b>antlr3TreeNodeStreamNew</b> () 
 
 ANTLR3_API <b>pANTLR3_TREE_PARSER</b> <b>antlr3TreeParserNewStream</b> (<b>ANTLR3_UINT32</b> sizeHint, <b>pANTLR3_COMMON_TREE_NODE_STREAM</b> ctnstream, <b>pANTLR3_RECOGNIZER_SHARED_STATE</b> state) 
 
 ANTLR3_API <b>pANTLR3_STRING_FACTORY</b> <b>antlr3UCS2StringFactoryNew</b> (void) 
 <i>Create a string factory that is UCS2 (16 bit) encoding based. </i> 
 ANTLR3_API <b>pANTLR3_COMMON_TREE_NODE_STREAM</b> <b>antlr3UnbufTreeNodeStreamNew</b> (<b>pANTLR3_STRING_FACTORY</b> strFactory, <b>ANTLR3_UINT32</b> hint) 
 
 ANTLR3_API <b>pANTLR3_COMMON_TREE_NODE_STREAM</b> <b>antlr3UnbufTreeNodeStreamNewTree</b> (<b>pANTLR3_BASE_TREE</b> tree, <b>ANTLR3_UINT32</b> hint) 
 
 ANTLR3_API <b>pANTLR3_VECTOR_FACTORY</b> <b>antlr3VectorFactoryNew</b> (<b>ANTLR3_UINT32</b> sizeHint) 
 <i>Vector factory creation. </i> 
 ANTLR3_API <b>pANTLR3_VECTOR</b> <b>antlr3VectorNew</b> (<b>ANTLR3_UINT32</b> sizeHint) 
 
 ANTLR3_API void <b>fillBufferExt</b> (<b>pANTLR3_COMMON_TOKEN_STREAM</b> tokenStream) 

<h2>Detailed Description</h2>Basic type and constant definitions for ANTLR3 Runtime. 

 

<h2>Define Documentation</h2><h3>#define _stat stat</h3>Referenced by antlr3Fsize().
<h3>#define ANTLR3_API</h3><h3>#define ANTLR3_API</h3><h3>#define ANTLR3_AVERAGE</h3><h3>#define ANTLR3_CALLOC(numEl, elSize) calloc (numEl, (size_t)(elSize))</h3>Default definition of ANTLR3_CALLOC. You can override this before including <b>antlr3.h</b> if you wish to use your own implementation. 

 Referenced by addEdge(), antlr3AsciiFileStreamNew(), antlr3BaseRecognizerNew(), antlr3CommonTreeNodeStreamNew(), antlr3CommonTreeNodeStreamNewStream(), antlr3DebugListenerNew(), antlr3ExceptionNew(), antlr3IntStreamNew(), antlr3IntTrieNew(), antlr3TreeNodeStreamNew(), grow(), and intTrieAdd().
<h3>#define ANTLR3_CDECL</h3>Referenced by addChild(), antlr3VectorSwap(), newRaw16(), and newRaw8().
<h3>#define ANTLR3_CLOSESOCKET close</h3>Referenced by handshake().
<h3>#define ANTLR3_ENCODING_LATIN1 0</h3>Referenced by stringInit8().
<h3>#define ANTLR3_ENCODING_UCS2 1</h3>Referenced by stringInit16().
<h3>#define ANTLR3_ENCODING_UTF32 3</h3><h3>#define ANTLR3_ENCODING_UTF8 2</h3><h3>#define ANTLR3_FASTCALL</h3><h3>#define ANTLR3_FPRINTF fprintf</h3>Default definition of fprintf, set this to something other than fprintf before including <b>antlr3.h</b> if your system does not have a fprintf. Note that you can define this to be // without harming the runtime. 

 Referenced by addChild(), alreadyParsedRule(), antlr3ExceptionPrint(), antlr3RecognitionExceptionNew(), becomeRoot(), consumeUntil(), consumeUntilSet(), ConvertUTF16toUTF32(), displayRecognitionError(), dupTok(), dupTreeNode(), getChild(), getChildCount(), getText(), match(), matchAny(), memoize(), mismatch(), mTokens(), recover(), recoverFromMismatchedElement(), recoverFromMismatchedSet(), recoverFromMismatchedToken(), replaceChildren(), setText(), setText8(), setType(), and synpred().
<h3>#define ANTLR3_FREE(ptr) free ((void *)(ptr))</h3>Default definition of ANTLR3_FREE. You can override this before including <b>antlr3.h</b> if you wish to use your own implementation. 

 Referenced by antlr3BaseRecognizerNew(), antlr3BitsetCopy(), antlr3BitsetFree(), antlr3BitsetNew(), antlr3CommonTreeNodeStreamFree(), antlr3CTSFree(), antlr3EnumFree(), antlr3ExceptionFree(), antlr3HashDelete(), antlr3HashDeleteI(), antlr3HashFree(), antlr3HashRemove(), antlr3HashTableNew(), antlr3InputClose(), antlr3IntTrieNew(), antlr3ListFree(), antlr3SetVectorApi(), antlr3StackFree(), antlr3StringFactoryNew(), antlr3TokenStreamFree(), antlr3TreeNodeStreamFree(), antlr3VectorFree(), closeFactory(), closeVectorFactory(), ctaFree(), expungeRS(), factoryClose(), freeBR(), freeIntNode(), freeLexer(), freeParser(), freeStream(), freeTopo(), grow(), intTrieFree(), replaceChildren(), sortVector(), stringFree(), and toUTF8_16().
<h3>#define ANTLR3_FREE_FUNC free</h3>Default definition of ANTLR3_FREE_FUNC . You can override this before including <b>antlr3.h</b> if you wish to use your own implementation. 

 Referenced by antlr3AsciiMark().
<h3>#define ANTLR3_FUNC_PTR(ptr) (void *)((<b>ANTLR3_UINT32</b>)(ptr))</h3>Referenced by antlr3AsciiLT(), antlr3AsciiSeek(), antlr3EnumNew(), antlr3IntTrieNew(), antlr3ListNew(), antlr3StackNew(), antlr3VectorNew(), discardTokenType(), getRuleMemoization(), and setTokenTypeChannel().
<h3>#define ANTLR3_INLINE inline</h3><h3>#define ANTLR3_LIST_SIZE_HINT 63</h3><h3>#define ANTLR3_MALLOC(request) malloc ((size_t)(request))</h3>Default definition of ANTLR3_MALLOC. You can override this before including <b>antlr3.h</b> if you wish to use your own implementation. 

 Referenced by ANTLR3_TREE_ADAPTORNew(), antlr3ArboretumNew(), antlr3AsciiMark(), antlr3BaseRecognizerNew(), antlr3BitsetCopy(), antlr3BitsetNew(), antlr3BitsetToIntList(), antlr3CommonTokenStreamNew(), antlr3CommonTreeNew(), antlr3EnumNew(), antlr3HashPut(), antlr3HashPutI(), antlr3HashTableNew(), antlr3LexerNew(), antlr3ListNew(), antlr3NewAsciiStringCopyStream(), antlr3NewAsciiStringInPlaceStream(), antlr3NewUCS2StringInPlaceStream(), antlr3ParserNew(), antlr3readAscii(), antlr3RewriteRuleElementStreamNewAE(), antlr3SetVectorApi(), antlr3StackNew(), antlr3StringFactoryNew(), antlr3TokenFactoryNew(), antlr3TokenStreamNew(), antlr3TopoNew(), antlr3TreeParserNewStream(), antlr3VectorFactoryNew(), antlr3VectorNew(), antlr3VectorResize(), newPool(), newRaw16(), newRaw8(), newSize16(), newSize8(), newToken(), sortToArray(), sortVector(), to8_16(), and toUTF8_16().
<h3>#define ANTLR3_MEMCPY(target, source, size) memcpy((void *)(target), (const void *)(source), (size_t)(size))</h3>Default definition of ANTLR3_MEMCPY. You can override this before including <b>antlr3.h</b> if you wish to use your own implementation. 

 Referenced by antlr3BitsetClone(), antlr3BitsetCopy(), antlr3VectorResize(), and grow().
<h3>#define ANTLR3_MEMMOVE(target, source, size) memmove((void *)(target), (const void *)(source), (size_t)(size))</h3>Default definition of ANTLR3_MEMMOVE. You can override this before including <b>antlr3.h</b> if you wish to use your own implementation. 

 Referenced by antlr3NewAsciiStringCopyStream(), antlr3VectorDel(), antrl3VectorRemove(), append16_16(), append8(), insert16_16(), insert16_8(), insert8(), newPtr16_16(), newPtr8(), set16_16(), and set8().
<h3>#define ANTLR3_MEMSET(target, byte, size) memset((void *)(target), (int)(byte), (size_t)(size))</h3>Default definition of ANTLR3_MEMSET. You can override this before including <b>antlr3.h</b> if you wish to use your own implementation.
<h3>#define ANTLR3_PRINTF printf</h3>Default definition of printf, set this to something other than printf before including <b>antlr3.h</b> if your system does not have a printf. Note that you can define this to be // without harming the runtime. 

 Referenced by ack().
<h3>#define ANTLR3_REALLOC(current, request) realloc ((void *)(current), (size_t)(request))</h3>Default definition of ANTLR3_REALLOC. You can override this before including <b>antlr3.h</b> if you wish to use your own implementation. 

 Referenced by addc16(), addc8(), addEdge(), antlr3VectorResize(), append16_16(), append16_8(), append8(), insert16_16(), insert16_8(), insert8(), newPool(), set16_16(), set16_8(), and set8().
<h3>#define ANTLR3_SIZE_HINT 1025</h3><h3>#define ANTLR3_STRDUP(instr) (<b>pANTLR3_UINT8</b>)(strdup ((const char *)(instr)))</h3>Default definition of ANTLR3_STRDUP. You can override this before including <b>antlr3.h</b> if you wish to use your own implementation. 

 Referenced by antlr3HashPut().
<h3>#define ANTLR3_TRIE_DEPTH 31</h3><h3>#define ANTLR3_UINT32_CAST(ptr) (<b>ANTLR3_UINT32</b>)(ptr)</h3>Referenced by antlr3UCS2Substr(), displayRecognitionError(), getUniqueID(), and toUTF8_16().
<h3>#define ANTLR3_UINT64_CAST(ptr) (<b>ANTLR3_UINT64</b>)((<b>ANTLR3_UINT32</b>)(ptr))</h3><h3>#define ANTLR3_UINT64_LIT(lit) lit##ULL</h3><h3>#define INVALID_SOCKET ((<b>SOCKET</b>)-1)</h3>Referenced by handshake().
<h2>Typedef Documentation</h2><h3>typedef uint64_t <b>ANTLR3_BITWORD</b></h3><h3>typedef uint32_t <b>ANTLR3_BOOLEAN</b></h3><h3>typedef int32_t <b>ANTLR3_CHAR</b></h3><h3>typedef FILE* <b>ANTLR3_FDSC</b></h3><h3>typedef struct stat <b>ANTLR3_FSTAT_STRUCT</b></h3><h3>typedef int16_t <b>ANTLR3_INT16</b></h3><h3>typedef int32_t <b>ANTLR3_INT32</b></h3><h3>typedef int64_t <b>ANTLR3_INT64</b></h3><h3>typedef int8_t <b>ANTLR3_INT8</b></h3><h3>typedef <b>ANTLR3_UINT32</b> <b>ANTLR3_INTKEY</b></h3><h3>typedef <b>ANTLR3_INT32</b> <b>ANTLR3_MARKER</b></h3><h3>typedef size_t <b>ANTLR3_SALENT</b></h3><h3>typedef struct sockaddr_in <b>ANTLR3_SOCKADDRT</b></h3><h3>typedef uint32_t <b>ANTLR3_UCHAR</b></h3><h3>typedef uint16_t <b>ANTLR3_UINT16</b></h3><h3>typedef uint32_t <b>ANTLR3_UINT32</b></h3><h3>typedef uint64_t <b>ANTLR3_UINT64</b></h3><h3>typedef uint8_t <b>ANTLR3_UINT8</b></h3><h3>typedef uint64_t * <b>pANTLR3_BITWORD</b></h3><h3>typedef uint32_t * <b>pANTLR3_BOOLEAN</b></h3><h3>typedef int32_t * <b>pANTLR3_CHAR</b></h3><h3>typedef int16_t * <b>pANTLR3_INT16</b></h3><h3>typedef int32_t * <b>pANTLR3_INT32</b></h3><h3>typedef int64_t * <b>pANTLR3_INT64</b></h3><h3>typedef int8_t * <b>pANTLR3_INT8</b></h3><h3>typedef struct sockaddr* <b>pANTLR3_SOCKADDRC</b></h3><h3>typedef struct sockaddr_in * <b>pANTLR3_SOCKADDRT</b></h3><h3>typedef uint32_t * <b>pANTLR3_UCHAR</b></h3><h3>typedef uint16_t * <b>pANTLR3_UINT16</b></h3><h3>typedef uint32_t * <b>pANTLR3_UINT32</b></h3><h3>typedef uint64_t * <b>pANTLR3_UINT64</b></h3><h3>typedef uint8_t * <b>pANTLR3_UINT8</b></h3><h3>typedef int <b>SOCKET</b></h3><h2>Function Documentation</h2><h3>ANTLR3_API <b>pANTLR3_BASE_TREE_ADAPTOR</b> ANTLR3_TREE_ADAPTORDebugNew (<b>pANTLR3_STRING_FACTORY</b> strFactory, <b>pANTLR3_DEBUG_EVENT_LISTENER</b> debugger)</h3>Debugging version of the tree adaptor (not normally called as generated code calls setDebugEventListener instead which changes a normal token stream to a debugging stream and means that a user's instantiation code does not need to be changed just to debug with AW. 

 References ANTLR3_TREE_ADAPTORNew(), antlr3BaseTreeAdaptorInit(), ANTLR3_BASE_TREE_ADAPTOR_struct::create, dbgCreate(), dbgSetTokenBoundaries(), and ANTLR3_BASE_TREE_ADAPTOR_struct::setTokenBoundaries.
<h3>ANTLR3_API <b>pANTLR3_BASE_TREE_ADAPTOR</b> ANTLR3_TREE_ADAPTORNew (<b>pANTLR3_STRING_FACTORY</b> strFactory)</h3>Create a new tree adaptor. Note that despite the fact that this is creating a new COMMON_TREE adaptor, we return the address of the BASE_TREE interface, as should any other adaptor that wishes to be used as the tree element of a tree parse/build. It needs to be given the address of a valid string factory as we do not know what the originating input stream encoding type was. This way we can rely on just using the original input stream's string factory or one of the correct type which the user supplies us. 

 References ANTLR3_MALLOC, antlr3ArboretumNew(), antlr3BaseTreeAdaptorInit(), antlr3TokenFactoryNew(), ANTLR3_COMMON_TREE_ADAPTOR_struct::arboretum, ANTLR3_COMMON_TREE_ADAPTOR_struct::baseAdaptor, create(), ANTLR3_BASE_TREE_ADAPTOR_struct::create, createToken(), ANTLR3_BASE_TREE_ADAPTOR_struct::createToken, createTokenFromToken(), ANTLR3_BASE_TREE_ADAPTOR_struct::createTokenFromToken, ctaFree(), deleteChild(), ANTLR3_BASE_TREE_ADAPTOR_struct::deleteChild, dupNode(), ANTLR3_BASE_TREE_ADAPTOR_struct::dupNode, errorNode(), ANTLR3_BASE_TREE_ADAPTOR_struct::errorNode, ANTLR3_BASE_TREE_ADAPTOR_struct::free, getChild(), ANTLR3_BASE_TREE_ADAPTOR_struct::getChild, getChildCount(), ANTLR3_BASE_TREE_ADAPTOR_struct::getChildCount, getChildIndex(), ANTLR3_BASE_TREE_ADAPTOR_struct::getChildIndex, getParent(), ANTLR3_BASE_TREE_ADAPTOR_struct::getParent, getText(), ANTLR3_BASE_TREE_ADAPTOR_struct::getText, getTokenStartIndex(), ANTLR3_BASE_TREE_ADAPTOR_struct::getTokenStartIndex, getTokenStopIndex(), ANTLR3_BASE_TREE_ADAPTOR_struct::getTokenStopIndex, getType(), ANTLR3_BASE_TREE_ADAPTOR_struct::getType, replaceChildren(), ANTLR3_BASE_TREE_ADAPTOR_struct::replaceChildren, setChild(), ANTLR3_BASE_TREE_ADAPTOR_struct::setChild, setChildIndex(), ANTLR3_BASE_TREE_ADAPTOR_struct::setChildIndex, setDebugEventListener(), ANTLR3_BASE_TREE_ADAPTOR_struct::setDebugEventListener, setParent(), ANTLR3_BASE_TREE_ADAPTOR_struct::setParent, setTokenBoundaries(), ANTLR3_BASE_TREE_ADAPTOR_struct::setTokenBoundaries, ANTLR3_BASE_TREE_ADAPTOR_struct::strFactory, ANTLR3_COMMON_TOKEN_struct::strFactory, ANTLR3_BASE_TREE_ADAPTOR_struct::super, ANTLR3_BASE_TREE_ADAPTOR_struct::tokenFactory, and ANTLR3_TOKEN_FACTORY_struct::unTruc. 

 Referenced by ANTLR3_TREE_ADAPTORDebugNew(), and antlr3CommonTreeNodeStreamNew().
<h3>ANTLR3_API <b>pANTLR3_ARBORETUM</b> antlr3ArboretumNew (<b>pANTLR3_STRING_FACTORY</b> factory)</h3>References ANTLR3_MALLOC, antlr3SetCTAPI(), antlr3StackNew(), antlr3VectorFactoryNew(), ANTLR3_COMMON_TREE_struct::baseTree, ANTLR3_ARBORETUM_struct::close, ANTLR3_COMMON_TREE_struct::factory, factoryClose(), ANTLR3_TREE_PARSER_struct::free, newFromToken(), ANTLR3_ARBORETUM_struct::newFromToken, newFromTree(), ANTLR3_ARBORETUM_struct::newFromTree, newPool(), newPoolTree(), ANTLR3_ARBORETUM_struct::newTree, ANTLR3_ARBORETUM_struct::nilStack, ANTLR3_ARBORETUM_struct::pools, ANTLR3_BASE_TREE_struct::strFactory, ANTLR3_ARBORETUM_struct::thisPool, ANTLR3_ARBORETUM_struct::unTruc, and ANTLR3_ARBORETUM_struct::vFactory. 

 Referenced by ANTLR3_TREE_ADAPTORNew().
<h3>ANTLR3_API <b>pANTLR3_INPUT_STREAM</b> antlr3AsciiFileStreamNew (<b>pANTLR3_UINT8</b> fileName)</h3>Use the contents of an operating system file as the input for an input stream. <b>Parameters:</b>
<dl COMPACT><dd><i>fileName</i> Name of operating system file to read.</dl>
 

 <b>Returns:</b>
<dl COMPACT><dd><dl COMPACT><dt>*
<dd>Pointer to new input stream context upon success
<dt>*
<dd>One of the ANTLR3_ERR_ defines on error.</dl></dl>
 

 

 

 References ANTLR3_CALLOC, ANTLR3_CHARSTREAM, ANTLR3_SUCCESS, antlr3AsciiSetupStream(), antlr3readAscii(), ANTLR3_INPUT_STREAM_struct::close, ANTLR3_INPUT_STREAM_struct::fileName, ANTLR3_INPUT_STREAM_struct::istream, ANTLR3_STRING_FACTORY_struct::newStr, ANTLR3_INT_STREAM_struct::streamName, and ANTLR3_INPUT_STREAM_struct::strFactory.
<h3>ANTLR3_API void antlr3BaseTreeAdaptorInit (<b>pANTLR3_BASE_TREE_ADAPTOR</b> adaptor, <b>pANTLR3_DEBUG_EVENT_LISTENER</b> debugger)</h3>Given a pointer to a base tree adaptor structure (which is usually embedded in the super class the implements the tree adaptor used in the parse), initialize its function pointers and so on. 

 References ANTLR3_DEBUG_EVENT_LISTENER_struct::adaptor, addChild(), ANTLR3_BASE_TREE_ADAPTOR_struct::addChild, addChildToken(), ANTLR3_BASE_TREE_ADAPTOR_struct::addChildToken, becomeRoot(), ANTLR3_BASE_TREE_ADAPTOR_struct::becomeRoot, becomeRootToken(), ANTLR3_BASE_TREE_ADAPTOR_struct::becomeRootToken, createTypeText(), ANTLR3_BASE_TREE_ADAPTOR_struct::createTypeText, createTypeToken(), ANTLR3_BASE_TREE_ADAPTOR_struct::createTypeToken, createTypeTokenText(), ANTLR3_BASE_TREE_ADAPTOR_struct::createTypeTokenText, dbgAddChild(), dbgAddChildToken(), dbgBecomeRoot(), dbgBecomeRootToken(), dbgCreateTypeText(), dbgCreateTypeToken(), dbgCreateTypeTokenText(), dbgDupTree(), dbgNil(), dupTree(), ANTLR3_BASE_TREE_ADAPTOR_struct::dupTree, dupTreeTT(), ANTLR3_BASE_TREE_ADAPTOR_struct::dupTreeTT, getChild(), ANTLR3_BASE_TREE_ADAPTOR_struct::getChild, getChildCount(), ANTLR3_BASE_TREE_ADAPTOR_struct::getChildCount, getText(), ANTLR3_BASE_TREE_ADAPTOR_struct::getText, getType(), ANTLR3_BASE_TREE_ADAPTOR_struct::getType, getUniqueID(), ANTLR3_BASE_TREE_ADAPTOR_struct::getUniqueID, isNilNode(), ANTLR3_BASE_TREE_ADAPTOR_struct::isNilNode, makeDot(), ANTLR3_BASE_TREE_ADAPTOR_struct::makeDot, nilNode(), ANTLR3_BASE_TREE_ADAPTOR_struct::nilNode, rulePostProcessing(), ANTLR3_BASE_TREE_ADAPTOR_struct::rulePostProcessing, setText(), ANTLR3_BASE_TREE_ADAPTOR_struct::setText, setText8(), ANTLR3_BASE_TREE_ADAPTOR_struct::setText8, setType(), and ANTLR3_BASE_TREE_ADAPTOR_struct::setType. 

 Referenced by ANTLR3_TREE_ADAPTORDebugNew(), ANTLR3_TREE_ADAPTORNew(), and setDebugEventListener().
<h3>ANTLR3_API <b>pANTLR3_BASE_TREE</b> antlr3BaseTreeNew (<b>pANTLR3_BASE_TREE</b> tree)</h3>References addChild(), ANTLR3_BASE_TREE_struct::addChild, addChildren(), ANTLR3_BASE_TREE_struct::addChildren, ANTLR3_BASE_TREE_struct::children, deleteChild(), ANTLR3_BASE_TREE_struct::deleteChild, dupTree(), ANTLR3_BASE_TREE_struct::dupTree, freshenPACIndexes(), ANTLR3_BASE_TREE_struct::freshenPACIndexes, freshenPACIndexesAll(), ANTLR3_BASE_TREE_struct::freshenPACIndexesAll, getCharPositionInLine(), ANTLR3_BASE_TREE_struct::getCharPositionInLine, getChild(), ANTLR3_BASE_TREE_struct::getChild, getChildCount(), ANTLR3_BASE_TREE_struct::getChildCount, getFirstChildWithType(), ANTLR3_BASE_TREE_struct::getFirstChildWithType, getLine(), ANTLR3_BASE_TREE_struct::getLine, replaceChildren(), ANTLR3_BASE_TREE_struct::replaceChildren, setChild(), ANTLR3_BASE_TREE_struct::setChild, ANTLR3_BASE_TREE_struct::strFactory, toStringTree(), and ANTLR3_BASE_TREE_struct::toStringTree. 

 Referenced by antlr3SetCTAPI().
<h3>ANTLR3_API <b>pANTLR3_BITSET</b> antlr3BitsetCopy (<b>pANTLR3_BITSET_LIST</b> blist)</h3>References ANTLR3_FREE, ANTLR3_MALLOC, ANTLR3_MEMCPY, ANTLR3_BITSET_LIST_struct::bits, ANTLR3_BITSET_struct::blist, and ANTLR3_BITSET_LIST_struct::length.
<h3>ANTLR3_API <b>pANTLR3_BITSET</b> antlr3BitsetList (<b>pANTLR3_HASH_TABLE</b> list)</h3>References ANTLR3_BITSET_struct::add, ANTLR3_SUCCESS, antlr3BitsetNew(), antlr3EnumNew(), ANTLR3_HASH_ENUM_struct::free, and ANTLR3_HASH_ENUM_struct::next. 

 Referenced by getTokensList().
<h3>ANTLR3_API <b>pANTLR3_BITSET</b> antlr3BitsetLoad (<b>pANTLR3_BITSET_LIST</b> inBits)</h3>Creates a new bitset with at least one 64 bit bset of bits, but as many 64 bit sets as are required. <b>Parameters:</b>
<dl COMPACT><dd><i>bset</i> A variable number of bits to add to the set, ending in -1 (impossible bit).</dl>
 

 <b>Returns:</b>
<dl COMPACT><dd>A new bit set with all of the specified bitmaps in it and the API initialized.</dl>
 

 Call as:
<dl COMPACT><dt>*
<dd>pANTLR3_BITSET = antlrBitsetLoad(bset, bset11, ..., -1);
<dt>*
<dd>pANTLR3_BITSET = antlrBitsetOf(-1); Create empty bitset</dl>
 

 

 <b>Remarks:</b>
<dl COMPACT><dd>Stdargs function - must supply -1 as last paremeter, which is NOT added to the set.</dl>
 

 

 

 References antlr3BitsetNew(), ANTLR3_BITSET_LIST_struct::bits, ANTLR3_BITSET_struct::blist, ANTLR3_BITSET_struct::grow, and ANTLR3_BITSET_LIST_struct::length. 

 Referenced by combineFollows(), displayRecognitionError(), mismatchIsMissingToken(), and recoverFromMismatchedElement().
<h3>ANTLR3_API <b>pANTLR3_BITSET</b> antlr3BitsetNew (<b>ANTLR3_UINT32</b> numBits)</h3>References ANTLR3_BITSET_BITS, ANTLR3_BITSET_LOG_BITS, ANTLR3_FREE, ANTLR3_MALLOC, antlr3BitsetSetAPI(), ANTLR3_BITSET_LIST_struct::bits, ANTLR3_BITSET_struct::blist, and ANTLR3_BITSET_LIST_struct::length. 

 Referenced by addEdge(), antlr3BitsetClone(), antlr3BitsetList(), antlr3BitsetLoad(), antlr3BitsetOf(), combineFollows(), and sortToArray().
<h3>ANTLR3_API <b>pANTLR3_BITSET</b> antlr3BitsetOf (<b>ANTLR3_INT32</b> bit, ...)</h3>Creates a new bitset with at least one element, but as many elements are required. <b>Parameters:</b>
<dl COMPACT><dd><i>bit</i> A variable number of bits to add to the set, ending in -1 (impossible bit).</dl>
 

 <b>Returns:</b>
<dl COMPACT><dd>A new bit set with all of the specified elements added into it.</dl>
 

 Call as:
<dl COMPACT><dt>*
<dd>pANTLR3_BITSET = antlrBitsetOf(n, n1, n2, -1);
<dt>*
<dd>pANTLR3_BITSET = antlrBitsetOf(-1); Create empty bitset</dl>
 

 

 <b>Remarks:</b>
<dl COMPACT><dd>Stdargs function - must supply -1 as last paremeter, which is NOT added to the set.</dl>
 

 

 

 References antlr3BitsetAdd(), and antlr3BitsetNew(). 

 Referenced by getTokensType().
<h3>ANTLR3_API void antlr3BitsetSetAPI (<b>pANTLR3_BITSET</b> bitset)</h3>References ANTLR3_BITSET_struct::add, antlr3BitsetAdd(), antlr3BitsetClone(), antlr3BitsetEquals(), antlr3BitsetFree(), antlr3BitsetIsNil(), antlr3BitsetMember(), antlr3BitsetNumBits(), antlr3BitsetOR(), antlr3BitsetORInPlace(), antlr3BitsetRemove(), antlr3BitsetSize(), antlr3BitsetToIntList(), ANTLR3_BITSET_struct::bor, ANTLR3_BITSET_struct::borInPlace, ANTLR3_BITSET_struct::clone, ANTLR3_BITSET_struct::equals, ANTLR3_BITSET_struct::free, grow(), ANTLR3_BITSET_struct::grow, ANTLR3_BITSET_struct::isMember, ANTLR3_BITSET_struct::isNilNode, ANTLR3_BITSET_struct::numBits, ANTLR3_BITSET_struct::remove, ANTLR3_BITSET_struct::size, and ANTLR3_BITSET_struct::toIntList. 

 Referenced by antlr3BitsetNew().
<h3>ANTLR3_API <b>ANTLR3_UCHAR</b> antlr3c8toAntlrc (<b>ANTLR3_INT8</b> inc)</h3>Provides basic utility functions to convert between the various Unicode character conversions. There are of course various packages that could be used instead of these functions, but then the Antlr 3 C runtime would be dependant on the particular package. Using ICU for this is a good idea if your project is already dependant on it. Convert 8 bit character to ANTLR char form. 

 <b>Parameters:</b>
<dl COMPACT><dd><i>inc</i> Input character to transform in 8 bit ASCII form.</dl>
 

 <b>Returns:</b>
<dl COMPACT><dd>ANTLR3_UCHAR encoding of the character.</dl><h3>ANTLR3_API <b>pANTLR3_COMMON_TOKEN_STREAM</b> antlr3CommonTokenDebugStreamSourceNew (<b>ANTLR3_UINT32</b> hint, <b>pANTLR3_TOKEN_SOURCE</b> source, <b>pANTLR3_DEBUG_EVENT_LISTENER</b> debugger)</h3>References ANTLR3_INT_STREAM_struct::_LA, ANTLR3_TOKEN_STREAM_struct::_LT, ANTLR3_FALSE, antlr3CommonTokenStreamSourceNew(), ANTLR3_INT_STREAM_struct::consume, dbgConsume(), dbgLA(), dbgMark(), dbgRewindLast(), dbgRewindStream(), dbgSeek(), dbgTokLT(), ANTLR3_TOKEN_STREAM_struct::debugger, ANTLR3_TOKEN_STREAM_struct::initialStreamState, ANTLR3_TOKEN_STREAM_struct::istream, ANTLR3_INT_STREAM_struct::mark, ANTLR3_INT_STREAM_struct::rewind, ANTLR3_INT_STREAM_struct::rewindLast, ANTLR3_INT_STREAM_struct::seek, and ANTLR3_COMMON_TOKEN_STREAM_struct::tstream.
<h3>ANTLR3_API <b>pANTLR3_COMMON_TOKEN</b> antlr3CommonTokenNew (<b>ANTLR3_UINT32</b> ttype)</h3>References newToken(), and ANTLR3_COMMON_TOKEN_struct::setType. 

 Referenced by antlr3CommonTreeNodeStreamNew().
<h3>ANTLR3_API <b>pANTLR3_COMMON_TOKEN_STREAM</b> antlr3CommonTokenStreamNew (<b>ANTLR3_UINT32</b> hint)</h3>References _LA(), ANTLR3_INT_STREAM_struct::_LA, ANTLR3_TOKEN_STREAM_struct::_LT, ANTLR3_MALLOC, ANTLR3_TOKENSTREAM, antlr3IntStreamNew(), antlr3TokenStreamNew(), antlr3VectorNew(), consume(), ANTLR3_INT_STREAM_struct::consume, discardOffChannel(), ANTLR3_COMMON_TOKEN_STREAM_struct::discardOffChannelToks, discardTokenType(), ANTLR3_COMMON_TOKEN_STREAM_struct::discardTokenType, ANTLR3_TOKEN_STREAM_struct::get, getSourceName(), ANTLR3_INT_STREAM_struct::getSourceName, getTokenRange(), ANTLR3_COMMON_TOKEN_STREAM_struct::getTokenRange, getTokens(), ANTLR3_COMMON_TOKEN_STREAM_struct::getTokens, getTokensList(), ANTLR3_COMMON_TOKEN_STREAM_struct::getTokensList, getTokenSource(), ANTLR3_TOKEN_STREAM_struct::getTokenSource, getTokensSet(), ANTLR3_COMMON_TOKEN_STREAM_struct::getTokensSet, getTokensType(), ANTLR3_COMMON_TOKEN_STREAM_struct::getTokensType, ANTLR3_INT_STREAM_struct::index, ANTLR3_TOKEN_STREAM_struct::istream, mark(), ANTLR3_INT_STREAM_struct::mark, ANTLR3_COMMON_TOKEN_STREAM_struct::p, release(), ANTLR3_INT_STREAM_struct::release, ANTLR3_INT_STREAM_struct::rewind, rewindLast(), ANTLR3_INT_STREAM_struct::rewindLast, rewindStream(), seek(), ANTLR3_INT_STREAM_struct::seek, setDebugListener(), ANTLR3_TOKEN_STREAM_struct::setDebugListener, setTokenSource(), ANTLR3_TOKEN_STREAM_struct::setTokenSource, setTokenTypeChannel(), ANTLR3_COMMON_TOKEN_STREAM_struct::setTokenTypeChannel, size(), ANTLR3_INT_STREAM_struct::size, ANTLR3_INT_STREAM_struct::super, ANTLR3_TOKEN_STREAM_struct::super, tindex(), ANTLR3_COMMON_TOKEN_STREAM_struct::tokens, tokLT(), toString(), ANTLR3_TOKEN_STREAM_struct::toString, toStringSS(), ANTLR3_TOKEN_STREAM_struct::toStringSS, toStringTT(), ANTLR3_TOKEN_STREAM_struct::toStringTT, ANTLR3_COMMON_TOKEN_STREAM_struct::tstream, and ANTLR3_INT_STREAM_struct::type. 

 Referenced by antlr3CommonTokenStreamSourceNew().
<h3>ANTLR3_API <b>pANTLR3_COMMON_TOKEN_STREAM</b> antlr3CommonTokenStreamSourceNew (<b>ANTLR3_UINT32</b> hint, <b>pANTLR3_TOKEN_SOURCE</b> source)</h3>References ANTLR3_FALSE, ANTLR3_TOKEN_DEFAULT_CHANNEL, antlr3CommonTokenStreamNew(), antlr3CTSFree(), ANTLR3_COMMON_TOKEN_STREAM_struct::channel, ANTLR3_COMMON_TOKEN_STREAM_struct::channelOverrides, ANTLR3_COMMON_TOKEN_STREAM_struct::discardOffChannel, ANTLR3_COMMON_TOKEN_STREAM_struct::discardSet, ANTLR3_COMMON_TOKEN_STREAM_struct::free, ANTLR3_TOKEN_STREAM_struct::setTokenSource, and ANTLR3_COMMON_TOKEN_STREAM_struct::tstream. 

 Referenced by antlr3CommonTokenDebugStreamSourceNew().
<h3>ANTLR3_API <b>pANTLR3_COMMON_TREE</b> antlr3CommonTreeNew (void)</h3>References ANTLR3_MALLOC, and antlr3SetCTAPI(). 

 Referenced by antlr3CommonTreeNewFromToken().
<h3>ANTLR3_API <b>pANTLR3_COMMON_TREE</b> antlr3CommonTreeNewFromToken (<b>pANTLR3_COMMON_TOKEN</b> tree)</h3>References antlr3CommonTreeNew(), and ANTLR3_COMMON_TREE_struct::token.
<h3>ANTLR3_API <b>pANTLR3_COMMON_TREE</b> antlr3CommonTreeNewFromTree (<b>pANTLR3_COMMON_TREE</b> tree)</h3><h3>ANTLR3_API <b>pANTLR3_COMMON_TREE_NODE_STREAM</b> antlr3CommonTreeNodeStreamNew (<b>pANTLR3_STRING_FACTORY</b> strFactory, <b>ANTLR3_UINT32</b> hint)</h3>References _LA(), ANTLR3_INT_STREAM_struct::_LA, _LT(), ANTLR3_TREE_NODE_STREAM_struct::_LT, ANTLR3_COMMON_TREE_NODE_STREAM_struct::adaptor, addNavigationNode(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::addNavigationNode, ANTLR3_CALLOC, ANTLR3_COMMONTREENODE, ANTLR3_FALSE, ANTLR3_TEXT_CHARP, ANTLR3_TOKEN_DOWN, ANTLR3_TOKEN_EOF, ANTLR3_TOKEN_INVALID, ANTLR3_TOKEN_UP, ANTLR3_TREE_ADAPTORNew(), antlr3CommonTokenNew(), antlr3CommonTreeNodeStreamFree(), antlr3IntStreamNew(), antlr3SetCTAPI(), antlr3StackNew(), antlr3TreeNodeStreamNew(), antlr3VectorNew(), ANTLR3_COMMON_TOKEN_struct::chars, consume(), ANTLR3_INT_STREAM_struct::consume, ANTLR3_TREE_NODE_STREAM_struct::ctns, DEFAULT_INITIAL_BUFFER_SIZE, ANTLR3_COMMON_TREE_NODE_STREAM_struct::DOWN, ANTLR3_COMMON_TREE_NODE_STREAM_struct::EOF_NODE, ANTLR3_TREE_NODE_STREAM_struct::free, ANTLR3_BASE_TREE_ADAPTOR_struct::free, ANTLR3_COMMON_TREE_NODE_STREAM_struct::free, ANTLR3_TREE_NODE_STREAM_struct::get, getTreeAdaptor(), ANTLR3_TREE_NODE_STREAM_struct::getTreeAdaptor, getTreeSource(), ANTLR3_TREE_NODE_STREAM_struct::getTreeSource, hasUniqueNavigationNodes(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::hasUniqueNavigationNodes, ANTLR3_INT_STREAM_struct::index, INITIAL_CALL_STACK_SIZE, ANTLR3_COMMON_TREE_NODE_STREAM_struct::INVALID_NODE, ANTLR3_TREE_NODE_STREAM_struct::istream, mark(), ANTLR3_INT_STREAM_struct::mark, ANTLR3_COMMON_TREE_NODE_STREAM_struct::markers, newDownNode(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::newDownNode, newUpNode(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::newUpNode, ANTLR3_COMMON_TREE_NODE_STREAM_struct::nodes, ANTLR3_COMMON_TREE_NODE_STREAM_struct::nodeStack, ANTLR3_COMMON_TREE_NODE_STREAM_struct::p, pop(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::pop, push(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::push, release(), ANTLR3_INT_STREAM_struct::release, reset(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::reset, ANTLR3_INT_STREAM_struct::rewind, rewindLast(), ANTLR3_INT_STREAM_struct::rewindLast, rewindMark(), seek(), ANTLR3_INT_STREAM_struct::seek, setUniqueNavigationNodes(), ANTLR3_TREE_NODE_STREAM_struct::setUniqueNavigationNodes, size(), ANTLR3_INT_STREAM_struct::size, ANTLR3_COMMON_TOKEN_struct::strFactory, ANTLR3_COMMON_TREE_NODE_STREAM_struct::stringFactory, ANTLR3_COMMON_TREE_NODE_STREAM_struct::super, ANTLR3_INT_STREAM_struct::super, ANTLR3_COMMON_TOKEN_struct::textState, tindex(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::tnstream, ANTLR3_COMMON_TREE_struct::token, ANTLR3_COMMON_TOKEN_struct::tokText, toString(), ANTLR3_TREE_NODE_STREAM_struct::toString, toStringSS(), ANTLR3_TREE_NODE_STREAM_struct::toStringSS, toStringWork(), ANTLR3_TREE_NODE_STREAM_struct::toStringWork, ANTLR3_INT_STREAM_struct::type, ANTLR3_COMMON_TREE_NODE_STREAM_struct::uniqueNavigationNodes, and ANTLR3_COMMON_TREE_NODE_STREAM_struct::UP. 

 Referenced by antlr3CommonTreeNodeStreamNewTree().
<h3>ANTLR3_API <b>pANTLR3_COMMON_TREE_NODE_STREAM</b> antlr3CommonTreeNodeStreamNewStream (<b>pANTLR3_COMMON_TREE_NODE_STREAM</b> inStream)</h3>References _LA(), ANTLR3_INT_STREAM_struct::_LA, _LT(), ANTLR3_TREE_NODE_STREAM_struct::_LT, ANTLR3_COMMON_TREE_NODE_STREAM_struct::adaptor, addNavigationNode(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::addNavigationNode, ANTLR3_CALLOC, ANTLR3_COMMONTREENODE, ANTLR3_FALSE, ANTLR3_TRUE, antlr3CommonTreeNodeStreamFree(), antlr3IntStreamNew(), antlr3SetCTAPI(), antlr3TreeNodeStreamNew(), antlr3VectorNew(), consume(), ANTLR3_INT_STREAM_struct::consume, ANTLR3_TREE_NODE_STREAM_struct::ctns, DEFAULT_INITIAL_BUFFER_SIZE, ANTLR3_COMMON_TREE_NODE_STREAM_struct::DOWN, ANTLR3_COMMON_TREE_NODE_STREAM_struct::EOF_NODE, ANTLR3_TREE_NODE_STREAM_struct::free, ANTLR3_COMMON_TREE_NODE_STREAM_struct::free, ANTLR3_TREE_NODE_STREAM_struct::get, getLookaheadSize(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::getLookaheadSize, getTreeAdaptor(), ANTLR3_TREE_NODE_STREAM_struct::getTreeAdaptor, getTreeSource(), ANTLR3_TREE_NODE_STREAM_struct::getTreeSource, hasUniqueNavigationNodes(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::hasUniqueNavigationNodes, ANTLR3_INT_STREAM_struct::index, ANTLR3_COMMON_TREE_NODE_STREAM_struct::INVALID_NODE, ANTLR3_COMMON_TREE_NODE_STREAM_struct::isRewriter, ANTLR3_TREE_NODE_STREAM_struct::istream, mark(), ANTLR3_INT_STREAM_struct::mark, ANTLR3_COMMON_TREE_NODE_STREAM_struct::markers, newDownNode(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::newDownNode, newUpNode(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::newUpNode, ANTLR3_COMMON_TREE_NODE_STREAM_struct::nodes, ANTLR3_COMMON_TREE_NODE_STREAM_struct::nodeStack, ANTLR3_COMMON_TREE_NODE_STREAM_struct::p, pop(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::pop, push(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::push, release(), ANTLR3_INT_STREAM_struct::release, reset(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::reset, ANTLR3_INT_STREAM_struct::rewind, rewindLast(), ANTLR3_INT_STREAM_struct::rewindLast, rewindMark(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::root, seek(), ANTLR3_INT_STREAM_struct::seek, setUniqueNavigationNodes(), ANTLR3_TREE_NODE_STREAM_struct::setUniqueNavigationNodes, size(), ANTLR3_INT_STREAM_struct::size, ANTLR3_COMMON_TOKEN_struct::strFactory, ANTLR3_COMMON_TREE_NODE_STREAM_struct::stringFactory, ANTLR3_COMMON_TREE_NODE_STREAM_struct::super, ANTLR3_INT_STREAM_struct::super, tindex(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::tnstream, ANTLR3_COMMON_TREE_struct::token, toString(), ANTLR3_TREE_NODE_STREAM_struct::toString, toStringSS(), ANTLR3_TREE_NODE_STREAM_struct::toStringSS, toStringWork(), ANTLR3_TREE_NODE_STREAM_struct::toStringWork, ANTLR3_INT_STREAM_struct::type, ANTLR3_COMMON_TREE_NODE_STREAM_struct::uniqueNavigationNodes, and ANTLR3_COMMON_TREE_NODE_STREAM_struct::UP.
<h3>ANTLR3_API <b>pANTLR3_COMMON_TREE_NODE_STREAM</b> antlr3CommonTreeNodeStreamNewTree (<b>pANTLR3_BASE_TREE</b> tree, <b>ANTLR3_UINT32</b> hint)</h3>References antlr3CommonTreeNodeStreamNew(), ANTLR3_COMMON_TREE_NODE_STREAM_struct::root, and ANTLR3_BASE_TREE_struct::strFactory.
<h3>ANTLR3_API <b>pANTLR3_DEBUG_EVENT_LISTENER</b> antlr3DebugListenerNew ()</h3>Create and initialize a new debug event listener that can be connected to by ANTLRWorks and any other debugger via a socket. 

 References addChild(), ANTLR3_DEBUG_EVENT_LISTENER_struct::addChild, ANTLR3_CALLOC, becomeRoot(), ANTLR3_DEBUG_EVENT_LISTENER_struct::becomeRoot, beginBacktrack(), ANTLR3_DEBUG_EVENT_LISTENER_struct::beginBacktrack, beginResync(), ANTLR3_DEBUG_EVENT_LISTENER_struct::beginResync, commence(), ANTLR3_DEBUG_EVENT_LISTENER_struct::commence, consumeHiddenToken(), ANTLR3_DEBUG_EVENT_LISTENER_struct::consumeHiddenToken, consumeNode(), ANTLR3_DEBUG_EVENT_LISTENER_struct::consumeNode, consumeToken(), ANTLR3_DEBUG_EVENT_LISTENER_struct::consumeToken, createNode(), ANTLR3_DEBUG_EVENT_LISTENER_struct::createNode, createNodeTok(), ANTLR3_DEBUG_EVENT_LISTENER_struct::createNodeTok, DEFAULT_DEBUGGER_PORT, endBacktrack(), ANTLR3_DEBUG_EVENT_LISTENER_struct::endBacktrack, endResync(), ANTLR3_DEBUG_EVENT_LISTENER_struct::endResync, enterAlt(), ANTLR3_DEBUG_EVENT_LISTENER_struct::enterAlt, enterDecision(), ANTLR3_DEBUG_EVENT_LISTENER_struct::enterDecision, enterRule(), ANTLR3_DEBUG_EVENT_LISTENER_struct::enterRule, enterSubRule(), ANTLR3_DEBUG_EVENT_LISTENER_struct::enterSubRule, errorNode(), ANTLR3_DEBUG_EVENT_LISTENER_struct::errorNode, exitDecision(), ANTLR3_DEBUG_EVENT_LISTENER_struct::exitDecision, exitRule(), ANTLR3_DEBUG_EVENT_LISTENER_struct::exitRule, exitSubRule(), ANTLR3_DEBUG_EVENT_LISTENER_struct::exitSubRule, handshake(), ANTLR3_DEBUG_EVENT_LISTENER_struct::handshake, location(), ANTLR3_DEBUG_EVENT_LISTENER_struct::location, LT(), ANTLR3_DEBUG_EVENT_LISTENER_struct::LT, LTT(), ANTLR3_DEBUG_EVENT_LISTENER_struct::LTT, mark(), ANTLR3_DEBUG_EVENT_LISTENER_struct::mark, nilNode(), ANTLR3_DEBUG_EVENT_LISTENER_struct::nilNode, ANTLR3_DEBUG_EVENT_LISTENER_struct::port, ANTLR3_DEBUG_EVENT_LISTENER_struct::PROTOCOL_VERSION, recognitionException(), ANTLR3_DEBUG_EVENT_LISTENER_struct::recognitionException, ANTLR3_DEBUG_EVENT_LISTENER_struct::rewind, rewindLast(), ANTLR3_DEBUG_EVENT_LISTENER_struct::rewindLast, rewindMark(), semanticPredicate(), ANTLR3_DEBUG_EVENT_LISTENER_struct::semanticPredicate, setTokenBoundaries(), ANTLR3_DEBUG_EVENT_LISTENER_struct::setTokenBoundaries, terminate(), and ANTLR3_DEBUG_EVENT_LISTENER_struct::terminate. 

 Referenced by antlr3DebugListenerNewPort().
<h3>ANTLR3_API <b>ANTLR3_INT32</b> antlr3dfapredict (void * ctx, <b>pANTLR3_BASE_RECOGNIZER</b> rec, <b>pANTLR3_INT_STREAM</b> is, <b>pANTLR3_CYCLIC_DFA</b> cdfa)</h3>From the input stream, predict what alternative will succeed using this DFA (representing the covering regular approximation to the underlying CFL). Return an alternative number 1..n. Throw an exception upon error. 

 References ANTLR3_INT_STREAM_struct::_LA, ANTLR3_CYCLIC_DFA_struct::accept, ANTLR3_TOKEN_EOF, ANTLR3_TRUE, ANTLR3_INT_STREAM_struct::consume, ANTLR3_CYCLIC_DFA_struct::eof, ANTLR3_CYCLIC_DFA_struct::eot, ANTLR3_RECOGNIZER_SHARED_STATE_struct::error, ANTLR3_INT_STREAM_struct::mark, mark(), ANTLR3_CYCLIC_DFA_struct::min, noViableAlt(), ANTLR3_INT_STREAM_struct::rewind, ANTLR3_CYCLIC_DFA_struct::special, ANTLR3_CYCLIC_DFA_struct::specialStateTransition, ANTLR3_BASE_RECOGNIZER_struct::state, and ANTLR3_CYCLIC_DFA_struct::transition.
<h3>ANTLR3_API <b>ANTLR3_INT32</b> antlr3dfaspecialStateTransition (void * ctx, <b>pANTLR3_BASE_RECOGNIZER</b> rec, <b>pANTLR3_INT_STREAM</b> is, <b>pANTLR3_CYCLIC_DFA</b> dfa, <b>ANTLR3_INT32</b> s)</h3>Default special state implementation.
<h3>ANTLR3_API <b>ANTLR3_INT32</b> antlr3dfaspecialTransition (void * ctx, <b>pANTLR3_BASE_RECOGNIZER</b> rec, <b>pANTLR3_INT_STREAM</b> is, <b>pANTLR3_CYCLIC_DFA</b> dfa, <b>ANTLR3_INT32</b> s)</h3><h3>ANTLR3_API <b>pANTLR3_HASH_ENUM</b> antlr3EnumNew (<b>pANTLR3_HASH_TABLE</b> table)</h3>Creates an enumeration structure to traverse the hash table. <b>Parameters:</b>
<dl COMPACT><dd><i>table</i> Table to enumerate</dl>
 

 <b>Returns:</b>
<dl COMPACT><dd>Pointer to enumeration structure.</dl>
 

 

 

 References ANTLR3_ERR_NOMEM, ANTLR3_FUNC_PTR, ANTLR3_MALLOC, antlr3EnumFree(), antlr3EnumNext(), antlr3EnumNextEntry(), ANTLR3_HASH_ENUM_struct::bucket, ANTLR3_HASH_TABLE_struct::buckets, ANTLR3_HASH_BUCKET_struct::entries, ANTLR3_HASH_ENUM_struct::entry, ANTLR3_HASH_ENUM_struct::free, ANTLR3_HASH_ENUM_struct::next, and ANTLR3_HASH_ENUM_struct::table. 

 Referenced by antlr3BitsetList().
<h3>ANTLR3_API <b>pANTLR3_EXCEPTION</b> antlr3ExceptionNew (<b>ANTLR3_UINT32</b> exception, void * name, void * message, <b>ANTLR3_BOOLEAN</b> freeMessage)</h3>Creates a new ANTLR3 exception structure. <b>Parameters:</b>
<dl COMPACT><dd><i>exception</i> One of the ANTLR3_xxx_EXCEPTION indicators such as <b>ANTLR3_RECOGNITION_EXCEPTION</b> 
 <i>message</i> Pointer to message string 
 <i>freeMessage</i> Set to ANTLR3_TRUE if the message parameter should be freed by a call to <b>ANTLR3_FREE()</b> when the exception is destroyed.</dl>
 

 <b>Returns:</b>
<dl COMPACT><dd>Pointer to newly initialized exception structure, or an ANTLR3_ERR_xx defined value upon failure.</dl>
 

 An exception is 'thrown' by a recognizer when input is seen that is not predicted by the grammar productions or when some other error condition occurs. In C we do not have the luxury of try and catch blocks, so exceptions are added in the order they occur to a list in the baserecognizer structure. The last one to be thrown is inserted at the head of the list and the one currently installed is pointed to by the newly installed exception. 

 <b>Remarks:</b>
<dl COMPACT><dd>After an exception is created, you may add a pointer to your own structure and a pointer to a function to free this structure when the exception is destroyed.</dl>
 

 <b>See also:</b>
<dl COMPACT><dd><b>ANTLR3_EXCEPTION</b></dl>
 

 

 

 References ANTLR3_CALLOC, antlr3ExceptionFree(), antlr3ExceptionPrint(), ANTLR3_EXCEPTION_struct::freeEx, ANTLR3_EXCEPTION_struct::freeMessage, ANTLR3_EXCEPTION_struct::message, ANTLR3_EXCEPTION_struct::name, ANTLR3_EXCEPTION_struct::print, and ANTLR3_EXCEPTION_struct::type. 

 Referenced by antlr3RecognitionExceptionNew().
<h3>ANTLR3_API <b>ANTLR3_UINT32</b> antlr3Hash (void * key, <b>ANTLR3_UINT32</b> keylen)</h3>Given an input key of arbitrary length, return a hash value of it. This can then be used (with suitable modulo) to index other structures. 

 Referenced by antlr3HashGet(), antlr3HashPut(), and antlr3HashRemove().
<h3>ANTLR3_API <b>pANTLR3_HASH_TABLE</b> antlr3HashTableNew (<b>ANTLR3_UINT32</b> sizeHint)</h3>References ANTLR3_HASH_TABLE_struct::allowDups, ANTLR3_FALSE, ANTLR3_FREE, ANTLR3_MALLOC, ANTLR3_TRUE, antlr3HashDelete(), antlr3HashDeleteI(), antlr3HashFree(), antlr3HashGet(), antlr3HashGetI(), antlr3HashPut(), antlr3HashPutI(), antlr3HashRemove(), antlr3HashRemoveI(), antlr3HashSize(), ANTLR3_HASH_TABLE_struct::buckets, ANTLR3_HASH_TABLE_struct::count, ANTLR3_HASH_TABLE_struct::del, ANTLR3_HASH_TABLE_struct::delI, ANTLR3_HASH_TABLE_struct::doStrdup, ANTLR3_HASH_BUCKET_struct::entries, ANTLR3_HASH_TABLE_struct::free, ANTLR3_HASH_TABLE_struct::get, ANTLR3_HASH_TABLE_struct::getI, ANTLR3_HASH_TABLE_struct::modulo, ANTLR3_HASH_TABLE_struct::put, ANTLR3_HASH_TABLE_struct::putI, ANTLR3_HASH_TABLE_struct::remove, ANTLR3_HASH_TABLE_struct::removeI, and ANTLR3_HASH_TABLE_struct::size. 

 Referenced by antlr3ListNew().
<h3>ANTLR3_API <b>pANTLR3_INT_TRIE</b> antlr3IntTrieNew (<b>ANTLR3_UINT32</b> depth)</h3>References ANTLR3_INT_TRIE_struct::add, ANTLR3_CALLOC, ANTLR3_ERR_NOMEM, ANTLR3_FREE, ANTLR3_FUNC_PTR, ANTLR3_INT_TRIE_NODE_struct::bitNum, ANTLR3_INT_TRIE_struct::count, ANTLR3_INT_TRIE_struct::del, ANTLR3_INT_TRIE_struct::free, ANTLR3_INT_TRIE_struct::get, intTrieAdd(), intTrieDel(), intTrieFree(), intTrieGet(), ANTLR3_INT_TRIE_NODE_struct::leftN, ANTLR3_INT_TRIE_NODE_struct::rightN, and ANTLR3_INT_TRIE_struct::root. 

 Referenced by getRuleMemoization(), and reset().
<h3>ANTLR3_API <b>pANTLR3_LEXER</b> antlr3LexerNew (<b>ANTLR3_UINT32</b> sizeHint, <b>pANTLR3_RECOGNIZER_SHARED_STATE</b> state)</h3>References ANTLR3_MALLOC, ANTLR3_TOKEN_EOF, ANTLR3_TOKEN_INVALID, ANTLR3_TRUE, ANTLR3_TYPE_LEXER, antlr3BaseRecognizerNew(), antlr3SetTokenAPI(), displayRecognitionError(), ANTLR3_BASE_RECOGNIZER_struct::displayRecognitionError, emit(), ANTLR3_LEXER_struct::emit, emitNew(), ANTLR3_LEXER_struct::emitNew, ANTLR3_TOKEN_SOURCE_struct::eofToken, ANTLR3_COMMON_TOKEN_struct::factoryMade, ANTLR3_BASE_RECOGNIZER_struct::free, ANTLR3_LEXER_struct::free, freeLexer(), getCharIndex(), ANTLR3_LEXER_struct::getCharIndex, getCharPositionInLine(), ANTLR3_LEXER_struct::getCharPositionInLine, getCurrentInputSymbol(), ANTLR3_BASE_RECOGNIZER_struct::getCurrentInputSymbol, getLine(), ANTLR3_LEXER_struct::getLine, getMissingSymbol(), ANTLR3_BASE_RECOGNIZER_struct::getMissingSymbol, getText(), ANTLR3_LEXER_struct::getText, matchAny(), ANTLR3_LEXER_struct::matchAny, matchc(), ANTLR3_LEXER_struct::matchc, matchRange(), ANTLR3_LEXER_struct::matchRange, matchs(), ANTLR3_LEXER_struct::matchs, mTokens(), ANTLR3_LEXER_struct::mTokens, nextToken(), ANTLR3_TOKEN_SOURCE_struct::nextToken, popCharStream(), ANTLR3_LEXER_struct::popCharStream, pushCharStream(), ANTLR3_LEXER_struct::pushCharStream, ANTLR3_LEXER_struct::rec, recover(), ANTLR3_LEXER_struct::recover, reportError(), ANTLR3_BASE_RECOGNIZER_struct::reportError, reset(), ANTLR3_BASE_RECOGNIZER_struct::reset, setCharStream(), ANTLR3_LEXER_struct::setCharStream, ANTLR3_COMMON_TOKEN_struct::setType, ANTLR3_TOKEN_SOURCE_struct::skipToken, ANTLR3_BASE_RECOGNIZER_struct::state, ANTLR3_COMMON_TOKEN_struct::strFactory, ANTLR3_TOKEN_SOURCE_struct::strFactory, ANTLR3_TOKEN_SOURCE_struct::super, ANTLR3_BASE_RECOGNIZER_struct::super, ANTLR3_RECOGNIZER_SHARED_STATE_struct::tokFactory, and ANTLR3_RECOGNIZER_SHARED_STATE_struct::tokSource. 

 Referenced by antlr3LexerNewStream().
<h3>ANTLR3_API <b>pANTLR3_LEXER</b> antlr3LexerNewStream (<b>ANTLR3_UINT32</b> sizeHint, <b>pANTLR3_INPUT_STREAM</b> input, <b>pANTLR3_RECOGNIZER_SHARED_STATE</b> state)</h3>References antlr3LexerNew(), and setCharStream().
<h3>ANTLR3_API <b>pANTLR3_LIST</b> antlr3ListNew (<b>ANTLR3_UINT32</b> sizeHint)</h3>References ANTLR3_LIST_struct::add, ANTLR3_ERR_NOMEM, ANTLR3_FUNC_PTR, ANTLR3_MALLOC, antlr3HashTableNew(), antlr3ListAdd(), antlr3ListDelete(), antlr3ListFree(), antlr3ListGet(), antlr3ListPut(), antlr3ListRemove(), antlr3ListSize(), ANTLR3_LIST_struct::del, ANTLR3_LIST_struct::free, ANTLR3_LIST_struct::get, ANTLR3_LIST_struct::put, ANTLR3_LIST_struct::remove, ANTLR3_LIST_struct::size, and ANTLR3_LIST_struct::table. 

 Referenced by discardTokenType(), getTokensSet(), and setTokenTypeChannel().
<h3>ANTLR3_API void antlr3MTNExceptionNew (<b>pANTLR3_BASE_RECOGNIZER</b> recognizer)</h3>Creates a new Mismatched Tree Nde Exception and inserts in the recognizer exception stack. <b>Parameters:</b>
<dl COMPACT><dd><i>recognizer</i> Context pointer for this recognizer</dl>
 

 

 

 References ANTLR3_MISMATCHED_TREE_NODE_EXCEPTION, ANTLR3_MISMATCHED_TREE_NODE_NAME, antlr3RecognitionExceptionNew(), ANTLR3_RECOGNIZER_SHARED_STATE_struct::exception, ANTLR3_EXCEPTION_struct::name, ANTLR3_BASE_RECOGNIZER_struct::state, and ANTLR3_EXCEPTION_struct::type. 

 Referenced by antlr3TreeParserNewStream().
<h3>ANTLR3_API <b>pANTLR3_INPUT_STREAM</b> antlr3NewAsciiStringCopyStream (<b>pANTLR3_UINT8</b> inString, <b>ANTLR3_UINT32</b> size, <b>pANTLR3_UINT8</b> name)</h3>Create an ASCII string stream as input to ANTLR 3, copying the input string. This string stream first makes a copy of the string at the supplied pointer 

 <b>Parameters:</b>
<dl COMPACT><dd><i>inString</i> Pointer to the string to be copied as the input stream 
 <i>size</i> Size (in 8 bit ASCII characters) of the input string 
 <i>name</i> NAme to attach the input stream (can be NULL pointer)</dl>
 

 <b>Returns:</b>
<dl COMPACT><dd><dl COMPACT><dt>*
<dd>Pointer to new input stream context upon success
<dt>*
<dd>One of the ANTLR3_ERR_ defines on error.</dl></dl>
 

 <b>Remarks:</b>
<dl COMPACT><dd><dl COMPACT><dt>*
<dd>ANTLR does not alter the input string in any way.
<dt>*
<dd>String is slightly incorrect in that the passed in pointer can be to any memory in C version of ANTLR3 of course.</dl></dl>
 

 

 

 References ANTLR3_CHARSTREAM, ANTLR3_MALLOC, ANTLR3_MEMMOVE, ANTLR3_TRUE, antlr3AsciiSetupStream(), ANTLR3_INPUT_STREAM_struct::data, ANTLR3_INPUT_STREAM_struct::fileName, ANTLR3_INPUT_STREAM_struct::isAllocated, ANTLR3_INPUT_STREAM_struct::istream, ANTLR3_STRING_FACTORY_struct::newStr, ANTLR3_INPUT_STREAM_struct::sizeBuf, ANTLR3_INT_STREAM_struct::streamName, and ANTLR3_INPUT_STREAM_struct::strFactory.
<h3>ANTLR3_API <b>pANTLR3_INPUT_STREAM</b> antlr3NewAsciiStringInPlaceStream (<b>pANTLR3_UINT8</b> inString, <b>ANTLR3_UINT32</b> size, <b>pANTLR3_UINT8</b> name)</h3>Create an in-place ASCII string stream as input to ANTLR 3. An in-place string steam is the preferred method of supplying strings to ANTLR as input for lexing and compiling. This is because we make no copies of the input string but read from it right where it is. 

 <b>Parameters:</b>
<dl COMPACT><dd><i>inString</i> Pointer to the string to be used as the input stream 
 <i>size</i> Size (in 8 bit ASCII characters) of the input string 
 <i>name</i> NAme to attach the input stream (can be NULL pointer)</dl>
 

 <b>Returns:</b>
<dl COMPACT><dd><dl COMPACT><dt>*
<dd>Pointer to new input stream context upon success
<dt>*
<dd>One of the ANTLR3_ERR_ defines on error.</dl></dl>
 

 <b>Remarks:</b>
<dl COMPACT><dd><dl COMPACT><dt>*
<dd>ANTLR does not alter the input string in any way.
<dt>*
<dd>String is slightly incorrect in that the passed in pointer can be to any memory in C version of ANTLR3 of course.</dl></dl>
 

 

 

 References ANTLR3_CHARSTREAM, ANTLR3_FALSE, ANTLR3_MALLOC, antlr3AsciiSetupStream(), ANTLR3_INPUT_STREAM_struct::data, ANTLR3_INPUT_STREAM_struct::fileName, ANTLR3_INPUT_STREAM_struct::isAllocated, ANTLR3_INPUT_STREAM_struct::istream, ANTLR3_STRING_FACTORY_struct::newStr, ANTLR3_INPUT_STREAM_struct::sizeBuf, ANTLR3_INT_STREAM_struct::streamName, and ANTLR3_INPUT_STREAM_struct::strFactory.
<h3>ANTLR3_API <b>pANTLR3_INPUT_STREAM</b> antlr3NewUCS2StringInPlaceStream (<b>pANTLR3_UINT16</b> inString, <b>ANTLR3_UINT32</b> size, <b>pANTLR3_UINT16</b> name)</h3>Create an in-place UCS2 string stream as input to ANTLR 3. An in-place string steam is the preferred method of supplying strings to ANTLR as input for lexing and compiling. This is because we make no copies of the input string but read from it right where it is. 

 <b>Parameters:</b>
<dl COMPACT><dd><i>inString</i> Pointer to the string to be used as the input stream 
 <i>size</i> Size (in 16 bit ASCII characters) of the input string 
 <i>name</i> Name to attach the input stream (can be NULL pointer)</dl>
 

 <b>Returns:</b>
<dl COMPACT><dd><dl COMPACT><dt>*
<dd>Pointer to new input stream context upon success
<dt>*
<dd>One of the ANTLR3_ERR_ defines on error.</dl></dl>
 

 <b>Remarks:</b>
<dl COMPACT><dd><dl COMPACT><dt>*
<dd>ANTLR does not alter the input string in any way.
<dt>*
<dd>String is slightly incorrect in that the passed in pointer can be to any memory in C version of ANTLR3 of course.</dl></dl>
 

 

 

 References ANTLR3_CHARSTREAM, ANTLR3_FALSE, ANTLR3_MALLOC, antlr3UCS2SetupStream(), ANTLR3_INPUT_STREAM_struct::data, ANTLR3_INPUT_STREAM_struct::fileName, ANTLR3_INPUT_STREAM_struct::isAllocated, ANTLR3_INPUT_STREAM_struct::istream, ANTLR3_STRING_FACTORY_struct::newStr, ANTLR3_INPUT_STREAM_struct::sizeBuf, ANTLR3_INT_STREAM_struct::streamName, and ANTLR3_INPUT_STREAM_struct::strFactory.
<h3>ANTLR3_API <b>pANTLR3_PARSER</b> antlr3ParserNew (<b>ANTLR3_UINT32</b> sizeHint, <b>pANTLR3_RECOGNIZER_SHARED_STATE</b> state)</h3>References ANTLR3_MALLOC, ANTLR3_TYPE_PARSER, antlr3BaseRecognizerNew(), antlr3MTExceptionNew(), ANTLR3_BASE_RECOGNIZER_struct::exConstruct, ANTLR3_PARSER_struct::free, freeParser(), getTokenStream(), ANTLR3_PARSER_struct::getTokenStream, ANTLR3_PARSER_struct::rec, setDebugListener(), ANTLR3_PARSER_struct::setDebugListener, setTokenStream(), ANTLR3_PARSER_struct::setTokenStream, and ANTLR3_BASE_RECOGNIZER_struct::super. 

 Referenced by antlr3ParserNewStream().
<h3>ANTLR3_API <b>pANTLR3_PARSER</b> antlr3ParserNewStream (<b>ANTLR3_UINT32</b> sizeHint, <b>pANTLR3_TOKEN_STREAM</b> tstream, <b>pANTLR3_RECOGNIZER_SHARED_STATE</b> state)</h3>References antlr3ParserNew(), and ANTLR3_PARSER_struct::setTokenStream. 

 Referenced by antlr3ParserNewStreamDbg().
<h3>ANTLR3_API <b>pANTLR3_PARSER</b> antlr3ParserNewStreamDbg (<b>ANTLR3_UINT32</b> sizeHint, <b>pANTLR3_TOKEN_STREAM</b> tstream, <b>pANTLR3_DEBUG_EVENT_LISTENER</b> dbg, <b>pANTLR3_RECOGNIZER_SHARED_STATE</b> state)</h3>References antlr3ParserNewStream(), and ANTLR3_PARSER_struct::setDebugListener.
<h3>ANTLR3_API <b>pANTLR3_REWRITE_RULE_NODE_STREAM</b> antlr3RewriteRuleNODEStreamNewAE (<b>pANTLR3_BASE_TREE_ADAPTOR</b> adaptor, <b>pANTLR3_BASE_RECOGNIZER</b> rec, <b>pANTLR3_UINT8</b> description)</h3>References antlr3RewriteRuleElementStreamNewAE(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::dup, dupTreeNode(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::free, freeNodeRS(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::nextNode, nextNodeNode(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::toTree, and toTreeNode().
<h3>ANTLR3_API <b>pANTLR3_REWRITE_RULE_NODE_STREAM</b> antlr3RewriteRuleNODEStreamNewAEE (<b>pANTLR3_BASE_TREE_ADAPTOR</b> adaptor, <b>pANTLR3_BASE_RECOGNIZER</b> rec, <b>pANTLR3_UINT8</b> description, void * oneElement)</h3>References antlr3RewriteRuleElementStreamNewAEE(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::dup, dupTreeNode(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::free, freeNodeRS(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::nextNode, nextNodeNode(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::toTree, and toTreeNode().
<h3>ANTLR3_API <b>pANTLR3_REWRITE_RULE_NODE_STREAM</b> antlr3RewriteRuleNODEStreamNewAEV (<b>pANTLR3_BASE_TREE_ADAPTOR</b> adaptor, <b>pANTLR3_BASE_RECOGNIZER</b> rec, <b>pANTLR3_UINT8</b> description, <b>pANTLR3_VECTOR</b> vector)</h3>References antlr3RewriteRuleElementStreamNewAEV(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::dup, dupTreeNode(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::free, freeNodeRS(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::nextNode, nextNodeNode(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::toTree, and toTreeNode().
<h3>ANTLR3_API <b>pANTLR3_REWRITE_RULE_SUBTREE_STREAM</b> antlr3RewriteRuleSubtreeStreamNewAE (<b>pANTLR3_BASE_TREE_ADAPTOR</b> adaptor, <b>pANTLR3_BASE_RECOGNIZER</b> rec, <b>pANTLR3_UINT8</b> description)</h3>References antlr3RewriteRuleElementStreamNewAE(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::dup, dupTree(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::free, freeNodeRS(), nextNode(), and ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::nextNode.
<h3>ANTLR3_API <b>pANTLR3_REWRITE_RULE_SUBTREE_STREAM</b> antlr3RewriteRuleSubtreeStreamNewAEE (<b>pANTLR3_BASE_TREE_ADAPTOR</b> adaptor, <b>pANTLR3_BASE_RECOGNIZER</b> rec, <b>pANTLR3_UINT8</b> description, void * oneElement)</h3>References antlr3RewriteRuleElementStreamNewAEE(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::dup, dupTree(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::free, freeNodeRS(), nextNode(), and ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::nextNode.
<h3>ANTLR3_API <b>pANTLR3_REWRITE_RULE_SUBTREE_STREAM</b> antlr3RewriteRuleSubtreeStreamNewAEV (<b>pANTLR3_BASE_TREE_ADAPTOR</b> adaptor, <b>pANTLR3_BASE_RECOGNIZER</b> rec, <b>pANTLR3_UINT8</b> description, <b>pANTLR3_VECTOR</b> vector)</h3>References antlr3RewriteRuleElementStreamNewAEV(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::dup, dupTree(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::free, freeNodeRS(), nextNode(), and ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::nextNode.
<h3>ANTLR3_API <b>pANTLR3_REWRITE_RULE_TOKEN_STREAM</b> antlr3RewriteRuleTOKENStreamNewAE (<b>pANTLR3_BASE_TREE_ADAPTOR</b> adaptor, <b>pANTLR3_BASE_RECOGNIZER</b> rec, <b>pANTLR3_UINT8</b> description)</h3>References antlr3RewriteRuleElementStreamNewAE(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::dup, dupTok(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::nextNode, and nextNodeToken().
<h3>ANTLR3_API <b>pANTLR3_REWRITE_RULE_TOKEN_STREAM</b> antlr3RewriteRuleTOKENStreamNewAEE (<b>pANTLR3_BASE_TREE_ADAPTOR</b> adaptor, <b>pANTLR3_BASE_RECOGNIZER</b> rec, <b>pANTLR3_UINT8</b> description, void * oneElement)</h3>References antlr3RewriteRuleElementStreamNewAEE(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::dup, dupTok(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::nextNode, and nextNodeToken().
<h3>ANTLR3_API <b>pANTLR3_REWRITE_RULE_TOKEN_STREAM</b> antlr3RewriteRuleTOKENStreamNewAEV (<b>pANTLR3_BASE_TREE_ADAPTOR</b> adaptor, <b>pANTLR3_BASE_RECOGNIZER</b> rec, <b>pANTLR3_UINT8</b> description, <b>pANTLR3_VECTOR</b> vector)</h3>References antlr3RewriteRuleElementStreamNewAEV(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::dup, dupTok(), ANTLR3_REWRITE_RULE_ELEMENT_STREAM_struct::nextNode, and nextNodeToken().
<h3>ANTLR3_API void antlr3SetCTAPI (<b>pANTLR3_COMMON_TREE</b> tree)</h3>References antlr3BaseTreeNew(), ANTLR3_COMMON_TREE_struct::baseTree, ANTLR3_COMMON_TREE_struct::childIndex, ANTLR3_BASE_TREE_struct::children, createChildrenList(), ANTLR3_BASE_TREE_struct::createChildrenList, dupNode(), ANTLR3_BASE_TREE_struct::dupNode, ANTLR3_BASE_TREE_struct::free, getCharPositionInLine(), ANTLR3_BASE_TREE_struct::getCharPositionInLine, getChildIndex(), ANTLR3_BASE_TREE_struct::getChildIndex, getLine(), ANTLR3_BASE_TREE_struct::getLine, getParent(), ANTLR3_BASE_TREE_struct::getParent, getText(), ANTLR3_BASE_TREE_struct::getText, getToken(), ANTLR3_BASE_TREE_struct::getToken, getType(), ANTLR3_BASE_TREE_struct::getType, isNilNode(), ANTLR3_BASE_TREE_struct::isNilNode, ANTLR3_COMMON_TREE_struct::parent, reuse(), ANTLR3_BASE_TREE_struct::reuse, setChildIndex(), ANTLR3_BASE_TREE_struct::setChildIndex, setParent(), ANTLR3_BASE_TREE_struct::setParent, ANTLR3_COMMON_TREE_struct::startIndex, ANTLR3_COMMON_TREE_struct::stopIndex, ANTLR3_BASE_TREE_struct::super, ANTLR3_COMMON_TREE_struct::token, toString(), and ANTLR3_BASE_TREE_struct::toString. 

 Referenced by antlr3ArboretumNew(), antlr3CommonTreeNew(), antlr3CommonTreeNodeStreamNew(), antlr3CommonTreeNodeStreamNewStream(), and newPoolTree().
<h3>ANTLR3_API void antlr3SetTokenAPI (<b>pANTLR3_COMMON_TOKEN</b> token)</h3>References ANTLR3_TEXT_NONE, ANTLR3_TOKEN_DEFAULT_CHANNEL, ANTLR3_TOKEN_INVALID, ANTLR3_COMMON_TOKEN_struct::channel, ANTLR3_COMMON_TOKEN_struct::custom, ANTLR3_COMMON_TOKEN_struct::freeCustom, getChannel(), ANTLR3_COMMON_TOKEN_struct::getChannel, getCharPositionInLine(), ANTLR3_COMMON_TOKEN_struct::getCharPositionInLine, getLine(), ANTLR3_COMMON_TOKEN_struct::getLine, getStartIndex(), ANTLR3_COMMON_TOKEN_struct::getStartIndex, getStopIndex(), ANTLR3_COMMON_TOKEN_struct::getStopIndex, getText(), ANTLR3_COMMON_TOKEN_struct::getText, getTokenIndex(), ANTLR3_COMMON_TOKEN_struct::getTokenIndex, getType(), ANTLR3_COMMON_TOKEN_struct::getType, ANTLR3_COMMON_TOKEN_struct::index, ANTLR3_COMMON_TOKEN_struct::input, ANTLR3_COMMON_TOKEN_struct::line, setChannel(), ANTLR3_COMMON_TOKEN_struct::setChannel, setCharPositionInLine(), ANTLR3_COMMON_TOKEN_struct::setCharPositionInLine, setLine(), ANTLR3_COMMON_TOKEN_struct::setLine, setStartIndex(), ANTLR3_COMMON_TOKEN_struct::setStartIndex, setStopIndex(), ANTLR3_COMMON_TOKEN_struct::setStopIndex, setText(), ANTLR3_COMMON_TOKEN_struct::setText, setText8(), ANTLR3_COMMON_TOKEN_struct::setText8, setTokenIndex(), ANTLR3_COMMON_TOKEN_struct::setTokenIndex, setType(), ANTLR3_COMMON_TOKEN_struct::setType, ANTLR3_COMMON_TOKEN_struct::start, ANTLR3_COMMON_TOKEN_struct::stop, ANTLR3_COMMON_TOKEN_struct::textState, toString(), ANTLR3_COMMON_TOKEN_struct::toString, ANTLR3_COMMON_TOKEN_struct::type, ANTLR3_COMMON_TOKEN_struct::user1, ANTLR3_COMMON_TOKEN_struct::user2, and ANTLR3_COMMON_TOKEN_struct::user3. 

 Referenced by antlr3LexerNew(), antlr3TokenFactoryNew(), newPoolToken(), and newToken().
<h3>ANTLR3_API void antlr3SetVectorApi (<b>pANTLR3_VECTOR</b> vector, <b>ANTLR3_UINT32</b> sizeHint)</h3>References ANTLR3_VECTOR_struct::add, ANTLR3_FALSE, ANTLR3_FREE, ANTLR3_MALLOC, ANTLR3_VECTOR_INTERNAL_SIZE, antlr3VectorAdd(), antlr3VectorClear(), antlr3VectorDel(), antlr3VectorFree(), antlr3VectorGet(), antlr3VectorSet(), antlr3VectorSize(), antlr3VectorSwap(), antrl3VectorRemove(), ANTLR3_VECTOR_struct::clear, ANTLR3_VECTOR_struct::count, ANTLR3_VECTOR_struct::del, ANTLR3_VECTOR_struct::elements, ANTLR3_VECTOR_struct::elementsSize, ANTLR3_VECTOR_struct::factoryMade, ANTLR3_VECTOR_struct::get, ANTLR3_VECTOR_struct::internal, ANTLR3_VECTOR_struct::remove, ANTLR3_VECTOR_struct::set, ANTLR3_VECTOR_struct::size, and ANTLR3_VECTOR_struct::swap. 

 Referenced by antlr3VectorFactoryNew(), antlr3VectorNew(), and newVector().
<h3>ANTLR3_API <b>pANTLR3_STACK</b> antlr3StackNew (<b>ANTLR3_UINT32</b> sizeHint)</h3>References ANTLR3_ERR_NOMEM, ANTLR3_FUNC_PTR, ANTLR3_MALLOC, antlr3StackFree(), antlr3StackGet(), antlr3StackPeek(), antlr3StackPop(), antlr3StackPush(), antlr3StackSize(), antlr3VectorNew(), ANTLR3_STACK_struct::free, ANTLR3_STACK_struct::get, ANTLR3_STACK_struct::peek, ANTLR3_STACK_struct::pop, ANTLR3_STACK_struct::push, ANTLR3_STACK_struct::size, ANTLR3_STACK_struct::top, and ANTLR3_STACK_struct::vector. 

 Referenced by antlr3ArboretumNew(), antlr3CommonTreeNodeStreamNew(), antlr3VectorFactoryNew(), pushCharStream(), and reset().
<h3>ANTLR3_API <b>pANTLR3_STRING_FACTORY</b> antlr3StringFactoryNew (void)</h3>References ANTLR3_FREE, ANTLR3_MALLOC, antlr3VectorNew(), ANTLR3_STRING_FACTORY_struct::close, closeFactory(), destroy(), ANTLR3_STRING_FACTORY_struct::destroy, ANTLR3_STRING_FACTORY_struct::index, ANTLR3_STRING_FACTORY_struct::newPtr, ANTLR3_STRING_FACTORY_struct::newPtr8, newPtr8(), ANTLR3_STRING_FACTORY_struct::newRaw, newRaw8(), ANTLR3_STRING_FACTORY_struct::newSize, newSize8(), ANTLR3_STRING_FACTORY_struct::newStr, ANTLR3_STRING_FACTORY_struct::newStr8, newStr8(), ANTLR3_STRING_FACTORY_struct::printable, printable8(), and ANTLR3_STRING_FACTORY_struct::strings. 

 Referenced by antlr3AsciiSetupStream(), and antlr3UCS2StringFactoryNew().
<h3>ANTLR3_API <b>pANTLR3_TOKEN_FACTORY</b> antlr3TokenFactoryNew (<b>pANTLR3_INPUT_STREAM</b> input)</h3>References ANTLR3_MALLOC, ANTLR3_TRUE, antlr3SetTokenAPI(), ANTLR3_TOKEN_FACTORY_struct::close, factoryClose(), ANTLR3_COMMON_TOKEN_struct::factoryMade, newPool(), newPoolToken(), ANTLR3_TOKEN_FACTORY_struct::newToken, ANTLR3_TOKEN_FACTORY_struct::pools, setInputStream(), ANTLR3_TOKEN_FACTORY_struct::setInputStream, ANTLR3_TOKEN_FACTORY_struct::thisPool, and ANTLR3_TOKEN_FACTORY_struct::unTruc. 

 Referenced by ANTLR3_TREE_ADAPTORNew(), getMissingSymbol(), and setCharStream().
<h3>ANTLR3_API <b>pANTLR3_TOPO</b> antlr3TopoNew ()</h3>Allocate and initialize a new ANTLR3 topological sorter, which can be used to define edges that identify numerical node indexes that depend on other numerical node indexes, which can then be sorted topologically such that any node is sorted after all its dependent nodes. Use: 

 /verbatim 

 pANTLR3_TOPO topo; topo = antlr3NewTopo(); 

 if (topo == NULL) { out of memory } 

 topo-&gt;addEdge(topo, 3, 0); // Node 3 depends on node 0 topo-&gt;addEdge(topo, 0, 1); // Node - depends on node 1 topo-&gt;sortVector(topo, myVector); // Sort the vector in place (node numbers are the vector entry numbers) 

 /verbatim 

 References addEdge(), ANTLR3_TOPO_struct::addEdge, ANTLR3_FALSE, ANTLR3_MALLOC, ANTLR3_TOPO_struct::cycle, ANTLR3_TOPO_struct::cycleMark, ANTLR3_TOPO_struct::edges, ANTLR3_TOPO_struct::free, freeTopo(), ANTLR3_TOPO_struct::hasCycle, ANTLR3_TOPO_struct::limit, ANTLR3_TOPO_struct::sorted, sortToArray(), ANTLR3_TOPO_struct::sortToArray, sortVector(), ANTLR3_TOPO_struct::sortVector, and ANTLR3_TOPO_struct::visited.
<h3>ANTLR3_API <b>pANTLR3_TREE_NODE_STREAM</b> antlr3TreeNodeStreamNew ()</h3>References ANTLR3_CALLOC, antlr3TreeNodeStreamFree(), ANTLR3_TREE_NODE_STREAM_struct::free, replaceChildren(), and ANTLR3_TREE_NODE_STREAM_struct::replaceChildren. 

 Referenced by antlr3CommonTreeNodeStreamNew(), and antlr3CommonTreeNodeStreamNewStream().
<h3>ANTLR3_API <b>pANTLR3_TREE_PARSER</b> antlr3TreeParserNewStream (<b>ANTLR3_UINT32</b> sizeHint, <b>pANTLR3_COMMON_TREE_NODE_STREAM</b> ctnstream, <b>pANTLR3_RECOGNIZER_SHARED_STATE</b> state)</h3>Allocate tree parser memory 

 References ANTLR3_MALLOC, ANTLR3_TYPE_PARSER, ANTLR3_TYPE_TREE_PARSER, antlr3BaseRecognizerNew(), antlr3MTNExceptionNew(), ANTLR3_BASE_RECOGNIZER_struct::exConstruct, ANTLR3_TREE_PARSER_struct::free, freeParser(), getCurrentInputSymbol(), ANTLR3_BASE_RECOGNIZER_struct::getCurrentInputSymbol, getMissingSymbol(), ANTLR3_BASE_RECOGNIZER_struct::getMissingSymbol, getTreeNodeStream(), ANTLR3_TREE_PARSER_struct::getTreeNodeStream, mismatch(), ANTLR3_BASE_RECOGNIZER_struct::mismatch, ANTLR3_TREE_PARSER_struct::rec, setTreeNodeStream(), ANTLR3_TREE_PARSER_struct::setTreeNodeStream, ANTLR3_BASE_RECOGNIZER_struct::super, and ANTLR3_BASE_RECOGNIZER_struct::type.
<h3>ANTLR3_API <b>pANTLR3_STRING_FACTORY</b> antlr3UCS2StringFactoryNew (void)</h3>Create a string factory that is UCS2 (16 bit) encoding based. 

 References antlr3StringFactoryNew(), ANTLR3_STRING_FACTORY_struct::close, closeFactory(), destroy(), ANTLR3_STRING_FACTORY_struct::destroy, ANTLR3_STRING_FACTORY_struct::newPtr, newPtr16_16(), newPtr16_8(), ANTLR3_STRING_FACTORY_struct::newPtr8, ANTLR3_STRING_FACTORY_struct::newRaw, newRaw16(), ANTLR3_STRING_FACTORY_struct::newSize, newSize16(), ANTLR3_STRING_FACTORY_struct::newStr, newStr16_16(), newStr16_8(), ANTLR3_STRING_FACTORY_struct::newStr8, ANTLR3_STRING_FACTORY_struct::printable, and printable16(). 

 Referenced by antlr3UCS2SetupStream().
<h3>ANTLR3_API <b>pANTLR3_COMMON_TREE_NODE_STREAM</b> antlr3UnbufTreeNodeStreamNew (<b>pANTLR3_STRING_FACTORY</b> strFactory, <b>ANTLR3_UINT32</b> hint)</h3><h3>ANTLR3_API <b>pANTLR3_COMMON_TREE_NODE_STREAM</b> antlr3UnbufTreeNodeStreamNewTree (<b>pANTLR3_BASE_TREE</b> tree, <b>ANTLR3_UINT32</b> hint)</h3><h3>ANTLR3_API <b>pANTLR3_VECTOR_FACTORY</b> antlr3VectorFactoryNew (<b>ANTLR3_UINT32</b> sizeHint)</h3>Vector factory creation. 

 References ANTLR3_MALLOC, ANTLR3_TRUE, ANTLR3_VECTOR_INTERNAL_SIZE, antlr3SetVectorApi(), antlr3StackNew(), ANTLR3_VECTOR_FACTORY_struct::close, closeVectorFactory(), ANTLR3_VECTOR_struct::factoryMade, ANTLR3_VECTOR_FACTORY_struct::freeStack, newPool(), newVector(), ANTLR3_VECTOR_FACTORY_struct::newVector, ANTLR3_VECTOR_FACTORY_struct::pools, returnVector(), ANTLR3_VECTOR_FACTORY_struct::returnVector, ANTLR3_VECTOR_FACTORY_struct::thisPool, and ANTLR3_VECTOR_FACTORY_struct::unTruc. 

 Referenced by antlr3ArboretumNew().
<h3>ANTLR3_API <b>pANTLR3_VECTOR</b> antlr3VectorNew (<b>ANTLR3_UINT32</b> sizeHint)</h3>References ANTLR3_ERR_NOMEM, ANTLR3_FUNC_PTR, ANTLR3_MALLOC, and antlr3SetVectorApi(). 

 Referenced by antlr3BaseRecognizerNew(), antlr3CommonTokenStreamNew(), antlr3CommonTreeNodeStreamNew(), antlr3CommonTreeNodeStreamNewStream(), antlr3InputReset(), antlr3StackNew(), antlr3StringFactoryNew(), and replaceChildren().
<h3>ANTLR3_API void fillBufferExt (<b>pANTLR3_COMMON_TOKEN_STREAM</b> tokenStream)</h3><h2>Author</h2>Generated automatically by Doxygen for ANTLR3C from the source code.
