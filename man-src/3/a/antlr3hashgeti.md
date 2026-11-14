---
title: "antlr3hashgeti(3)"
name: "antlr3hashgeti"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3hashgeti/"
description: "src/antlr3collections.c –"
---

<p>src/antlr3collections.c &#8211; </p>
<p> Provides a number of useful functions that are roughly equivalent to java HashTable and List for the purposes of Antlr 3 C runtime.</p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/antlr3.h">antlr3.h</a>&gt;<br />
 #include &#8216;antlr3collections.h&#8217; </p>
<h3>Functions</h3>
<p>static void <code>addEdge</code> (<code>pANTLR3_TOPO</code> topo, <code>ANTLR3_UINT32</code> edge, <code>ANTLR3_UINT32</code> dependency) </p>
<p> static void <code>antlr3EnumFree</code> (<code>pANTLR3_HASH_ENUM</code> en)<br />
 <i>Frees up the memory structures that represent a hash table enumeration. </i><br />
 <code>pANTLR3_HASH_ENUM</code> <code>antlr3EnumNew</code> (<code>pANTLR3_HASH_TABLE</code> table)<br />
 <i>Creates an enumeration structure to traverse the hash table. </i><br />
 static int <code>antlr3EnumNext</code> (<code>pANTLR3_HASH_ENUM</code> en, <code>pANTLR3_HASH_KEY</code> *key, void **data)<br />
 <i>Return the next entry in the hashtable being traversed by the supplied enumeration. </i><br />
 static void <code>antlr3EnumNextEntry</code> (<code>pANTLR3_HASH_ENUM</code> en)<br />
 <i>Local function to advance the entry pointer of an enumeration structure to the next valid entry (if there is one). </i><br />
 ANTLR3_API <code>ANTLR3_UINT32</code> <code>antlr3Hash</code> (void *key, <code>ANTLR3_UINT32</code> keylen)<br />
 <i>Given an input key of arbitrary length, return a hash value of it. </i><br />
 static void <code>antlr3HashDelete</code> (<code>pANTLR3_HASH_TABLE</code> table, void *key)<br />
 <i>Takes the element with the supplied key out of the list, and deletes the data calling the supplied free() routine if any. </i><br />
 static void <code>antlr3HashDeleteI</code> (<code>pANTLR3_HASH_TABLE</code> table, <code>ANTLR3_INTKEY</code> key)<br />
 <i>Takes the element with the supplied key out of the list, and deletes the data calling the supplied free() routine if any. </i><br />
 static void <code>antlr3HashFree</code> (<code>pANTLR3_HASH_TABLE</code> table) </p>
<p> static void * <code>antlr3HashGet</code> (<code>pANTLR3_HASH_TABLE</code> table, void *key)<br />
 <i>Return the element pointer in the hash table for a particular key value, or NULL if it don&#8217;t exist (or was itself NULL). </i><br />
 static void * <code>antlr3HashGetI</code> (<code>pANTLR3_HASH_TABLE</code> table, <code>ANTLR3_INTKEY</code> key)<br />
 <i>Return the element pointer in the hash table for a particular key value, or NULL if it don&#8217;t exist (or was itself NULL). </i><br />
 static <code>ANTLR3_INT32</code> <code>antlr3HashPut</code> (<code>pANTLR3_HASH_TABLE</code> table, void *key, void *element, void(ANTLR3_CDECL *freeptr)(void *))<br />
 <i>Add the element pointer in to the table, based upon the hash of the provided key. </i><br />
 static <code>ANTLR3_INT32</code> <code>antlr3HashPutI</code> (<code>pANTLR3_HASH_TABLE</code> table, <code>ANTLR3_INTKEY</code> key, void *element, void(ANTLR3_CDECL *freeptr)(void *))<br />
 <i>Add the element pointer in to the table, based upon the hash of the provided key. </i><br />
 static <code>pANTLR3_HASH_ENTRY</code> <code>antlr3HashRemove</code> (<code>pANTLR3_HASH_TABLE</code> table, void *key)<br />
 <i>Remove the element in the hash table for a particular key value, if it exists &#8211; no error if it does not. </i><br />
 static <code>pANTLR3_HASH_ENTRY</code> <code>antlr3HashRemoveI</code> (<code>pANTLR3_HASH_TABLE</code> table, <code>ANTLR3_INTKEY</code> key)<br />
 <i>Remove a numeric keyed entry from a hash table if it exists, no error if it does not exist. </i><br />
 static <code>ANTLR3_UINT32</code> <code>antlr3HashSize</code> (<code>pANTLR3_HASH_TABLE</code> table)<br />
 <i>return the current size of the hash table </i><br />
 <code>pANTLR3_HASH_TABLE</code> <code>antlr3HashTableNew</code> (<code>ANTLR3_UINT32</code> sizeHint) </p>
<p> <code>pANTLR3_INT_TRIE</code> <code>antlr3IntTrieNew</code> (<code>ANTLR3_UINT32</code> depth) </p>
<p> static <code>ANTLR3_INT32</code> <code>antlr3ListAdd</code> (<code>pANTLR3_LIST</code> list, void *element, void(ANTLR3_CDECL *freeptr)(void *))<br />
 <i>Add the supplied element to the list, at the next available key. </i><br />
 static void <code>antlr3ListDelete</code> (<code>pANTLR3_LIST</code> list, <code>ANTLR3_INTKEY</code> key) </p>
<p> static void <code>antlr3ListFree</code> (<code>pANTLR3_LIST</code> list) </p>
<p> static void * <code>antlr3ListGet</code> (<code>pANTLR3_LIST</code> list, <code>ANTLR3_INTKEY</code> key) </p>
<p> ANTLR3_API <code>pANTLR3_LIST</code> <code>antlr3ListNew</code> (<code>ANTLR3_UINT32</code> sizeHint) </p>
<p> static <code>ANTLR3_INT32</code> <code>antlr3ListPut</code> (<code>pANTLR3_LIST</code> list, <code>ANTLR3_INTKEY</code> key, void *element, void(ANTLR3_CDECL *freeptr)(void *)) </p>
<p> static void * <code>antlr3ListRemove</code> (<code>pANTLR3_LIST</code> list, <code>ANTLR3_INTKEY</code> key)<br />
 <i>Remove from the list, but don&#8217;t free the element, just send it back to the caller. </i><br />
 static <code>ANTLR3_UINT32</code> <code>antlr3ListSize</code> (<code>pANTLR3_LIST</code> list) </p>
<p> ANTLR3_API void <code>antlr3SetVectorApi</code> (<code>pANTLR3_VECTOR</code> vector, <code>ANTLR3_UINT32</code> sizeHint) </p>
<p> static void <code>antlr3StackFree</code> (<code>pANTLR3_STACK</code> stack) </p>
<p> static void * <code>antlr3StackGet</code> (<code>pANTLR3_STACK</code> stack, <code>ANTLR3_INTKEY</code> key) </p>
<p> ANTLR3_API <code>pANTLR3_STACK</code> <code>antlr3StackNew</code> (<code>ANTLR3_UINT32</code> sizeHint) </p>
<p> static void * <code>antlr3StackPeek</code> (<code>pANTLR3_STACK</code> stack) </p>
<p> static void * <code>antlr3StackPop</code> (<code>pANTLR3_STACK</code> stack) </p>
<p> static <code>ANTLR3_BOOLEAN</code> <code>antlr3StackPush</code> (<code>pANTLR3_STACK</code> stack, void *element, void(ANTLR3_CDECL *freeptr)(void *)) </p>
<p> static <code>ANTLR3_UINT32</code> <code>antlr3StackSize</code> (<code>pANTLR3_STACK</code> stack) </p>
<p> ANTLR3_API <code>pANTLR3_TOPO</code> <code>antlr3TopoNew</code> ()<br />
 <i>Allocate and initialize a new ANTLR3 topological sorter, which can be used to define edges that identify numerical node indexes that depend on other numerical node indexes, which can then be sorted topologically such that any node is sorted after all its dependent nodes. </i><br />
 static <code>ANTLR3_UINT32</code> <code>antlr3VectorAdd</code> (<code>pANTLR3_VECTOR</code> vector, void *element, void(ANTLR3_CDECL *freeptr)(void *))<br />
 <i>Add the supplied pointer and freeing function pointer to the list, expanding the vector if needed. </i><br />
 static void <code>antlr3VectorClear</code> (<code>pANTLR3_VECTOR</code> vector) </p>
<p> static void <code>antlr3VectorDel</code> (<code>pANTLR3_VECTOR</code> vector, <code>ANTLR3_UINT32</code> entry) </p>
<p> ANTLR3_API <code>pANTLR3_VECTOR_FACTORY</code> <code>antlr3VectorFactoryNew</code> (<code>ANTLR3_UINT32</code> sizeHint)<br />
 <i>Vector factory creation. </i><br />
 static void ANTLR3_CDECL <code>antlr3VectorFree</code> (<code>pANTLR3_VECTOR</code> vector) </p>
<p> static void * <code>antlr3VectorGet</code> (<code>pANTLR3_VECTOR</code> vector, <code>ANTLR3_UINT32</code> entry) </p>
<p> ANTLR3_API <code>pANTLR3_VECTOR</code> <code>antlr3VectorNew</code> (<code>ANTLR3_UINT32</code> sizeHint) </p>
<p> static void <code>antlr3VectorResize</code> (<code>pANTLR3_VECTOR</code> vector, <code>ANTLR3_UINT32</code> hint) </p>
<p> static <code>ANTLR3_UINT32</code> <code>antlr3VectorSet</code> (<code>pANTLR3_VECTOR</code> vector, <code>ANTLR3_UINT32</code> entry, void *element, void(ANTLR3_CDECL *freeptr)(void *), <code>ANTLR3_BOOLEAN</code> freeExisting)<br />
 <i>Replace the element at the specified entry point with the supplied entry. </i><br />
 static <code>ANTLR3_UINT32</code> <code>antlr3VectorSize</code> (<code>pANTLR3_VECTOR</code> vector) </p>
<p> static <code>ANTLR3_BOOLEAN</code> <code>antlr3VectorSwap</code> (<code>pANTLR3_VECTOR</code> vector, <code>ANTLR3_UINT32</code> entry1, <code>ANTLR3_UINT32</code> entry2)<br />
 <i>Replace the element at the specified entry point with the supplied entry. </i><br />
 static void * <code>antrl3VectorRemove</code> (<code>pANTLR3_VECTOR</code> vector, <code>ANTLR3_UINT32</code> entry)<br />
 <i>Remove the entry from the vector, but do not free any entry, even if it has a free pointer. </i><br />
 static void <code>closeVectorFactory</code> (<code>pANTLR3_VECTOR_FACTORY</code> factory) </p>
<p> static void <code>DFS</code> (<code>pANTLR3_TOPO</code> topo, <code>ANTLR3_UINT32</code> node)<br />
 <i>Given a starting node, descend its dependent nodes (ones that it has edges to) until we find one without edges. </i><br />
 static void <code>freeIntNode</code> (<code>pANTLR3_INT_TRIE_NODE</code> node)<br />
 <i>Release memory allocated to this tree. </i><br />
 static void <code>freeTopo</code> (<code>pANTLR3_TOPO</code> topo) </p>
<p> static <code>ANTLR3_BOOLEAN</code> <code>intTrieAdd</code> (<code>pANTLR3_INT_TRIE</code> trie, <code>ANTLR3_INTKEY</code> key, <code>ANTLR3_UINT32</code> type, <code>ANTLR3_INTKEY</code> intVal, void *data, void(ANTLR3_CDECL *freeptr)(void *))<br />
 <i>Add an entry into the INT trie. </i><br />
 static <code>ANTLR3_BOOLEAN</code> <code>intTrieDel</code> (<code>pANTLR3_INT_TRIE</code> trie, <code>ANTLR3_INTKEY</code> key) </p>
<p> static void <code>intTrieFree</code> (<code>pANTLR3_INT_TRIE</code> trie)<br />
 <i>Called to free all nodes and the structure itself. </i><br />
 static <code>pANTLR3_TRIE_ENTRY</code> <code>intTrieGet</code> (<code>pANTLR3_INT_TRIE</code> trie, <code>ANTLR3_INTKEY</code> key)<br />
 <i>Search the int Trie and return a pointer to the first bucket indexed by the key if it is contained in the trie, otherwise NULL. </i><br />
 static void <code>newPool</code> (<code>pANTLR3_VECTOR_FACTORY</code> factory) </p>
<p> static <code>pANTLR3_VECTOR</code> <code>newVector</code> (<code>pANTLR3_VECTOR_FACTORY</code> factory) </p>
<p> static void <code>returnVector</code> (<code>pANTLR3_VECTOR_FACTORY</code> factory, <code>pANTLR3_VECTOR</code> vector) </p>
<p> static <code>pANTLR3_UINT32</code> <code>sortToArray</code> (<code>pANTLR3_TOPO</code> topo) </p>
<p> static void <code>sortVector</code> (<code>pANTLR3_TOPO</code> topo, <code>pANTLR3_VECTOR</code> v) </p>
<h3>Variables</h3>
<p>static <code>ANTLR3_UINT8</code> <code>bitIndex</code> [256]<br />
 <i>Array of left most significant bit positions for an 8 bit element provides an efficient way to find the highest bit that is set in an n byte value (n&gt;0). </i><br />
 static <code>ANTLR3_UINT64</code> <code>bitMask</code> [64]<br />
 <i>Rather than use the bit index of a trie node to shift 0x01 left that many times, then &amp; with the result, it is faster to use the bit index as an index into this table which holds precomputed masks for any of the 64 bits we need to mask off singly. </i></p>
<h2>Detailed Description</h2>
<p>Provides a number of useful functions that are roughly equivalent to java HashTable and List for the purposes of Antlr 3 C runtime. </p>
<p> Also useable by the C programmer for things like symbol tables pointers and so on.</p>
<h2>Function Documentation</h2>
<h3>static void addEdge (<code>pANTLR3_TOPO</code> topo, <code>ANTLR3_UINT32</code> edge, <code>ANTLR3_UINT32</code> dependency) [static]</h3>
<p>References ANTLR3_BITSET_struct::add, ANTLR3_CALLOC, ANTLR3_REALLOC, antlr3BitsetNew(), ANTLR3_TOPO_struct::edges, and ANTLR3_TOPO_struct::limit. </p>
<p> Referenced by antlr3TopoNew().</p>
<h3>static void antlr3EnumFree (<code>pANTLR3_HASH_ENUM</code> en) [static]</h3>
<p>Frees up the memory structures that represent a hash table enumeration. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>enum</i> Pointer to ANTLR3 enumeration structure returned by <code>antlr3EnumNew()</code></dl>
<p> References ANTLR3_FREE. </p>
<p> Referenced by antlr3EnumNew().</p>
<h3><code>pANTLR3_HASH_ENUM</code> antlr3EnumNew (<code>pANTLR3_HASH_TABLE</code> table)</h3>
<p>Creates an enumeration structure to traverse the hash table. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>table</i> Table to enumerate</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Pointer to enumeration structure.</dl>
<p> References ANTLR3_ERR_NOMEM, ANTLR3_FUNC_PTR, ANTLR3_MALLOC, antlr3EnumFree(), antlr3EnumNext(), antlr3EnumNextEntry(), ANTLR3_HASH_ENUM_struct::bucket, ANTLR3_HASH_TABLE_struct::buckets, ANTLR3_HASH_BUCKET_struct::entries, ANTLR3_HASH_ENUM_struct::entry, ANTLR3_HASH_ENUM_struct::free, ANTLR3_HASH_ENUM_struct::next, and ANTLR3_HASH_ENUM_struct::table. </p>
<p> Referenced by antlr3BitsetList().</p>
<h3>static int antlr3EnumNext (<code>pANTLR3_HASH_ENUM</code> en, <code>pANTLR3_HASH_KEY</code> * key, void ** data) [static]</h3>
<p>Return the next entry in the hashtable being traversed by the supplied enumeration. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>en</i> Pointer to the enumeration tracking structure<br />
 <i>key</i> Pointer to void pointer, where the key pointer is returned.<br />
 <i>data</i> Pointer to void pointer where the data pointer is returned.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>*</p>
<dd>ANTLR3_SUCCESS if there was a next key</p>
<dt>*</p>
<dd>ANTLR3_FAIL if there were no more keys</dl>
</dl>
<p> <code>Remarks:</code></p>
<dl COMPACT>
<dd>No checking of input structure is performed!</dl>
<p> References ANTLR3_FAIL, ANTLR3_SUCCESS, antlr3EnumNextEntry(), ANTLR3_HASH_ENUM_struct::bucket, ANTLR3_HASH_ENTRY_struct::data, ANTLR3_HASH_ENUM_struct::entry, ANTLR3_HASH_ENTRY_struct::keybase, ANTLR3_HASH_TABLE_struct::modulo, and ANTLR3_HASH_ENUM_struct::table. </p>
<p> Referenced by antlr3EnumNew().</p>
<h3>static void antlr3EnumNextEntry (<code>pANTLR3_HASH_ENUM</code> en) [static]</h3>
<p>Local function to advance the entry pointer of an enumeration structure to the next valid entry (if there is one). <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>enum</i> Pointer to ANTLR3 enumeration structure returned by <code>antlr3EnumNew()</code></dl>
<p> <code>Remarks:</code></p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>*</p>
<dd>The function always leaves the pointers pointing at a valid entry if there is one, so if the entry pointer is NULL when this function exits, there were no more entries in the table.</dl>
</dl>
<p> References ANTLR3_HASH_ENUM_struct::bucket, ANTLR3_HASH_TABLE_struct::buckets, ANTLR3_HASH_BUCKET_struct::entries, ANTLR3_HASH_ENUM_struct::entry, ANTLR3_HASH_TABLE_struct::modulo, ANTLR3_HASH_ENTRY_struct::nextEntry, and ANTLR3_HASH_ENUM_struct::table. </p>
<p> Referenced by antlr3EnumNew(), and antlr3EnumNext().</p>
<h3>ANTLR3_API <code>ANTLR3_UINT32</code> antlr3Hash (void * key, <code>ANTLR3_UINT32</code> keylen)</h3>
<p>Given an input key of arbitrary length, return a hash value of it. This can then be used (with suitable modulo) to index other structures. </p>
<p> Referenced by antlr3HashGet(), antlr3HashPut(), and antlr3HashRemove().</p>
<h3>static void antlr3HashDelete (<code>pANTLR3_HASH_TABLE</code> table, void * key) [static]</h3>
<p>Takes the element with the supplied key out of the list, and deletes the data calling the supplied free() routine if any. </p>
<p> References ANTLR3_FREE, antlr3HashRemove(), and ANTLR3_HASH_ENTRY_struct::data. </p>
<p> Referenced by antlr3HashTableNew().</p>
<h3>static void antlr3HashDeleteI (<code>pANTLR3_HASH_TABLE</code> table, <code>ANTLR3_INTKEY</code> key) [static]</h3>
<p>Takes the element with the supplied key out of the list, and deletes the data calling the supplied free() routine if any. </p>
<p> References ANTLR3_FREE, antlr3HashRemoveI(), and ANTLR3_HASH_ENTRY_struct::data. </p>
<p> Referenced by antlr3HashTableNew().</p>
<h3>static void antlr3HashFree (<code>pANTLR3_HASH_TABLE</code> table) [static]</h3>
<p>References ANTLR3_FREE, ANTLR3_HASH_TYPE_STR, ANTLR3_HASH_TABLE_struct::buckets, ANTLR3_HASH_ENTRY_struct::data, ANTLR3_HASH_BUCKET_struct::entries, ANTLR3_HASH_KEY_struct::key, ANTLR3_HASH_ENTRY_struct::keybase, ANTLR3_HASH_TABLE_struct::modulo, ANTLR3_HASH_ENTRY_struct::nextEntry, ANTLR3_HASH_KEY_struct::sKey, and ANTLR3_HASH_KEY_struct::type. </p>
<p> Referenced by antlr3HashTableNew().</p>
<h3>static void * antlr3HashGet (<code>pANTLR3_HASH_TABLE</code> table, void * key) [static]</h3>
<p>Return the element pointer in the hash table for a particular key value, or NULL if it don&#8217;t exist (or was itself NULL). </p>
<p> References antlr3Hash(), ANTLR3_HASH_TABLE_struct::buckets, ANTLR3_HASH_ENTRY_struct::data, ANTLR3_HASH_BUCKET_struct::entries, ANTLR3_HASH_KEY_struct::key, ANTLR3_HASH_ENTRY_struct::keybase, ANTLR3_HASH_TABLE_struct::modulo, ANTLR3_HASH_ENTRY_struct::nextEntry, and ANTLR3_HASH_KEY_struct::sKey. </p>
<p> Referenced by antlr3HashTableNew().</p>
<h3>static void * antlr3HashGetI (<code>pANTLR3_HASH_TABLE</code> table, <code>ANTLR3_INTKEY</code> key) [static]</h3>
<p>Return the element pointer in the hash table for a particular key value, or NULL if it don&#8217;t exist (or was itself NULL). </p>
<p> References ANTLR3_HASH_TABLE_struct::buckets, ANTLR3_HASH_ENTRY_struct::data, ANTLR3_HASH_BUCKET_struct::entries, ANTLR3_HASH_KEY_struct::iKey, ANTLR3_HASH_KEY_struct::key, ANTLR3_HASH_ENTRY_struct::keybase, ANTLR3_HASH_TABLE_struct::modulo, and ANTLR3_HASH_ENTRY_struct::nextEntry. </p>
<p> Referenced by antlr3HashTableNew().</p>
<h3>static <code>ANTLR3_INT32</code> antlr3HashPut (<code>pANTLR3_HASH_TABLE</code> table, void * key, void * element, void(ANTLR3_CDECL *freeptr)(void *)) [static]</h3>
<p>Add the element pointer in to the table, based upon the hash of the provided key. </p>
<p> References ANTLR3_HASH_TABLE_struct::allowDups, ANTLR3_ERR_HASHDUP, ANTLR3_ERR_NOMEM, ANTLR3_FALSE, ANTLR3_HASH_TYPE_STR, ANTLR3_MALLOC, ANTLR3_STRDUP, ANTLR3_SUCCESS, ANTLR3_TRUE, antlr3Hash(), ANTLR3_HASH_TABLE_struct::buckets, ANTLR3_HASH_TABLE_struct::count, ANTLR3_HASH_ENTRY_struct::data, ANTLR3_HASH_TABLE_struct::doStrdup, ANTLR3_HASH_BUCKET_struct::entries, ANTLR3_HASH_KEY_struct::key, ANTLR3_HASH_ENTRY_struct::keybase, ANTLR3_HASH_TABLE_struct::modulo, ANTLR3_HASH_ENTRY_struct::nextEntry, ANTLR3_HASH_KEY_struct::sKey, and ANTLR3_HASH_KEY_struct::type. </p>
<p> Referenced by antlr3HashTableNew().</p>
<h3>static <code>ANTLR3_INT32</code> antlr3HashPutI (<code>pANTLR3_HASH_TABLE</code> table, <code>ANTLR3_INTKEY</code> key, void * element, void(ANTLR3_CDECL *freeptr)(void *)) [static]</h3>
<p>Add the element pointer in to the table, based upon the hash of the provided key. </p>
<p> References ANTLR3_HASH_TABLE_struct::allowDups, ANTLR3_ERR_HASHDUP, ANTLR3_ERR_NOMEM, ANTLR3_FALSE, ANTLR3_HASH_TYPE_INT, ANTLR3_MALLOC, ANTLR3_SUCCESS, ANTLR3_HASH_TABLE_struct::buckets, ANTLR3_HASH_TABLE_struct::count, ANTLR3_HASH_ENTRY_struct::data, ANTLR3_HASH_BUCKET_struct::entries, ANTLR3_HASH_KEY_struct::iKey, ANTLR3_HASH_KEY_struct::key, ANTLR3_HASH_ENTRY_struct::keybase, ANTLR3_HASH_TABLE_struct::modulo, ANTLR3_HASH_ENTRY_struct::nextEntry, and ANTLR3_HASH_KEY_struct::type. </p>
<p> Referenced by antlr3HashTableNew().</p>
<h3>static <code>pANTLR3_HASH_ENTRY</code> antlr3HashRemove (<code>pANTLR3_HASH_TABLE</code> table, void * key) [static]</h3>
<p>Remove the element in the hash table for a particular key value, if it exists &#8211; no error if it does not. </p>
<p> References ANTLR3_FREE, ANTLR3_TRUE, antlr3Hash(), ANTLR3_HASH_TABLE_struct::buckets, ANTLR3_HASH_TABLE_struct::count, ANTLR3_HASH_TABLE_struct::doStrdup, ANTLR3_HASH_BUCKET_struct::entries, ANTLR3_HASH_KEY_struct::key, ANTLR3_HASH_ENTRY_struct::keybase, ANTLR3_HASH_TABLE_struct::modulo, ANTLR3_HASH_ENTRY_struct::nextEntry, and ANTLR3_HASH_KEY_struct::sKey. </p>
<p> Referenced by antlr3HashDelete(), and antlr3HashTableNew().</p>
<h3>static <code>pANTLR3_HASH_ENTRY</code> antlr3HashRemoveI (<code>pANTLR3_HASH_TABLE</code> table, <code>ANTLR3_INTKEY</code> key) [static]</h3>
<p>Remove a numeric keyed entry from a hash table if it exists, no error if it does not exist. </p>
<p> References ANTLR3_HASH_TABLE_struct::buckets, ANTLR3_HASH_TABLE_struct::count, ANTLR3_HASH_BUCKET_struct::entries, ANTLR3_HASH_KEY_struct::iKey, ANTLR3_HASH_KEY_struct::key, ANTLR3_HASH_ENTRY_struct::keybase, ANTLR3_HASH_TABLE_struct::modulo, and ANTLR3_HASH_ENTRY_struct::nextEntry. </p>
<p> Referenced by antlr3HashDeleteI(), and antlr3HashTableNew().</p>
<h3>static <code>ANTLR3_UINT32</code> antlr3HashSize (<code>pANTLR3_HASH_TABLE</code> table) [static]</h3>
<p>return the current size of the hash table </p>
<p> References ANTLR3_HASH_TABLE_struct::count. </p>
<p> Referenced by antlr3HashTableNew().</p>
<h3><code>pANTLR3_HASH_TABLE</code> antlr3HashTableNew (<code>ANTLR3_UINT32</code> sizeHint)</h3>
<p>References ANTLR3_HASH_TABLE_struct::allowDups, ANTLR3_FALSE, ANTLR3_FREE, ANTLR3_MALLOC, ANTLR3_TRUE, antlr3HashDelete(), antlr3HashDeleteI(), antlr3HashFree(), antlr3HashGet(), antlr3HashGetI(), antlr3HashPut(), antlr3HashPutI(), antlr3HashRemove(), antlr3HashRemoveI(), antlr3HashSize(), ANTLR3_HASH_TABLE_struct::buckets, ANTLR3_HASH_TABLE_struct::count, ANTLR3_HASH_TABLE_struct::del, ANTLR3_HASH_TABLE_struct::delI, ANTLR3_HASH_TABLE_struct::doStrdup, ANTLR3_HASH_BUCKET_struct::entries, ANTLR3_HASH_TABLE_struct::free, ANTLR3_HASH_TABLE_struct::get, ANTLR3_HASH_TABLE_struct::getI, ANTLR3_HASH_TABLE_struct::modulo, ANTLR3_HASH_TABLE_struct::put, ANTLR3_HASH_TABLE_struct::putI, ANTLR3_HASH_TABLE_struct::remove, ANTLR3_HASH_TABLE_struct::removeI, and ANTLR3_HASH_TABLE_struct::size. </p>
<p> Referenced by antlr3ListNew().</p>
<h3><code>pANTLR3_INT_TRIE</code> antlr3IntTrieNew (<code>ANTLR3_UINT32</code> depth)</h3>
<p>References ANTLR3_INT_TRIE_struct::add, ANTLR3_CALLOC, ANTLR3_ERR_NOMEM, ANTLR3_FREE, ANTLR3_FUNC_PTR, ANTLR3_INT_TRIE_NODE_struct::bitNum, ANTLR3_INT_TRIE_struct::count, ANTLR3_INT_TRIE_struct::del, ANTLR3_INT_TRIE_struct::free, ANTLR3_INT_TRIE_struct::get, intTrieAdd(), intTrieDel(), intTrieFree(), intTrieGet(), ANTLR3_INT_TRIE_NODE_struct::leftN, ANTLR3_INT_TRIE_NODE_struct::rightN, and ANTLR3_INT_TRIE_struct::root. </p>
<p> Referenced by getRuleMemoization(), and reset().</p>
<h3>static <code>ANTLR3_INT32</code> antlr3ListAdd (<code>pANTLR3_LIST</code> list, void * element, void(ANTLR3_CDECL *freeptr)(void *)) [static]</h3>
<p>Add the supplied element to the list, at the next available key. </p>
<p> References ANTLR3_LIST_struct::put, ANTLR3_HASH_TABLE_struct::size, and ANTLR3_LIST_struct::table. </p>
<p> Referenced by antlr3ListNew().</p>
<h3>static void antlr3ListDelete (<code>pANTLR3_LIST</code> list, <code>ANTLR3_INTKEY</code> key) [static]</h3>
<p>References ANTLR3_HASH_TABLE_struct::delI, and ANTLR3_LIST_struct::table. </p>
<p> Referenced by antlr3ListNew().</p>
<h3>static void antlr3ListFree (<code>pANTLR3_LIST</code> list) [static]</h3>
<p>References ANTLR3_FREE, ANTLR3_HASH_TABLE_struct::free, and ANTLR3_LIST_struct::table. </p>
<p> Referenced by antlr3ListNew().</p>
<h3>static void * antlr3ListGet (<code>pANTLR3_LIST</code> list, <code>ANTLR3_INTKEY</code> key) [static]</h3>
<p>References ANTLR3_HASH_TABLE_struct::getI, and ANTLR3_LIST_struct::table. </p>
<p> Referenced by antlr3ListNew().</p>
<h3>ANTLR3_API <code>pANTLR3_LIST</code> antlr3ListNew (<code>ANTLR3_UINT32</code> sizeHint)</h3>
<p>References ANTLR3_LIST_struct::add, ANTLR3_ERR_NOMEM, ANTLR3_FUNC_PTR, ANTLR3_MALLOC, antlr3HashTableNew(), antlr3ListAdd(), antlr3ListDelete(), antlr3ListFree(), antlr3ListGet(), antlr3ListPut(), antlr3ListRemove(), antlr3ListSize(), ANTLR3_LIST_struct::del, ANTLR3_LIST_struct::free, ANTLR3_LIST_struct::get, ANTLR3_LIST_struct::put, ANTLR3_LIST_struct::remove, ANTLR3_LIST_struct::size, and ANTLR3_LIST_struct::table. </p>
<p> Referenced by discardTokenType(), getTokensSet(), and setTokenTypeChannel().</p>
<h3>static <code>ANTLR3_INT32</code> antlr3ListPut (<code>pANTLR3_LIST</code> list, <code>ANTLR3_INTKEY</code> key, void * element, void(ANTLR3_CDECL *freeptr)(void *)) [static]</h3>
<p>References ANTLR3_HASH_TABLE_struct::putI, and ANTLR3_LIST_struct::table. </p>
<p> Referenced by antlr3ListNew().</p>
<h3>static void * antlr3ListRemove (<code>pANTLR3_LIST</code> list, <code>ANTLR3_INTKEY</code> key) [static]</h3>
<p>Remove from the list, but don&#8217;t free the element, just send it back to the caller. </p>
<p> References ANTLR3_HASH_ENTRY_struct::data, ANTLR3_HASH_TABLE_struct::removeI, and ANTLR3_LIST_struct::table. </p>
<p> Referenced by antlr3ListNew().</p>
<h3>static <code>ANTLR3_UINT32</code> antlr3ListSize (<code>pANTLR3_LIST</code> list) [static]</h3>
<p>References ANTLR3_HASH_TABLE_struct::size, and ANTLR3_LIST_struct::table. </p>
<p> Referenced by antlr3ListNew().</p>
<h3>ANTLR3_API void antlr3SetVectorApi (<code>pANTLR3_VECTOR</code> vector, <code>ANTLR3_UINT32</code> sizeHint)</h3>
<p>References ANTLR3_VECTOR_struct::add, ANTLR3_FALSE, ANTLR3_FREE, ANTLR3_MALLOC, ANTLR3_VECTOR_INTERNAL_SIZE, antlr3VectorAdd(), antlr3VectorClear(), antlr3VectorDel(), antlr3VectorFree(), antlr3VectorGet(), antlr3VectorSet(), antlr3VectorSize(), antlr3VectorSwap(), antrl3VectorRemove(), ANTLR3_VECTOR_struct::clear, ANTLR3_VECTOR_struct::count, ANTLR3_VECTOR_struct::del, ANTLR3_VECTOR_struct::elements, ANTLR3_VECTOR_struct::elementsSize, ANTLR3_VECTOR_struct::factoryMade, ANTLR3_VECTOR_struct::get, ANTLR3_VECTOR_struct::internal, ANTLR3_VECTOR_struct::remove, ANTLR3_VECTOR_struct::set, ANTLR3_VECTOR_struct::size, and ANTLR3_VECTOR_struct::swap. </p>
<p> Referenced by antlr3VectorFactoryNew(), antlr3VectorNew(), and newVector().</p>
<h3>static void antlr3StackFree (<code>pANTLR3_STACK</code> stack) [static]</h3>
<p>References ANTLR3_FREE, ANTLR3_STACK_struct::top, and ANTLR3_STACK_struct::vector. </p>
<p> Referenced by antlr3StackNew().</p>
<h3>static void * antlr3StackGet (<code>pANTLR3_STACK</code> stack, <code>ANTLR3_INTKEY</code> key) [static]</h3>
<p>References ANTLR3_VECTOR_struct::get, and ANTLR3_STACK_struct::vector. </p>
<p> Referenced by antlr3StackNew().</p>
<h3>ANTLR3_API <code>pANTLR3_STACK</code> antlr3StackNew (<code>ANTLR3_UINT32</code> sizeHint)</h3>
<p>References ANTLR3_ERR_NOMEM, ANTLR3_FUNC_PTR, ANTLR3_MALLOC, antlr3StackFree(), antlr3StackGet(), antlr3StackPeek(), antlr3StackPop(), antlr3StackPush(), antlr3StackSize(), antlr3VectorNew(), ANTLR3_STACK_struct::free, ANTLR3_STACK_struct::get, ANTLR3_STACK_struct::peek, ANTLR3_STACK_struct::pop, ANTLR3_STACK_struct::push, ANTLR3_STACK_struct::size, ANTLR3_STACK_struct::top, and ANTLR3_STACK_struct::vector. </p>
<p> Referenced by antlr3ArboretumNew(), antlr3CommonTreeNodeStreamNew(), antlr3VectorFactoryNew(), pushCharStream(), and reset().</p>
<h3>static void * antlr3StackPeek (<code>pANTLR3_STACK</code> stack) [static]</h3>
<p>References ANTLR3_STACK_struct::top. </p>
<p> Referenced by antlr3StackNew().</p>
<h3>static void * antlr3StackPop (<code>pANTLR3_STACK</code> stack) [static]</h3>
<p>References ANTLR3_VECTOR_struct::count, ANTLR3_VECTOR_struct::del, ANTLR3_VECTOR_struct::get, ANTLR3_STACK_struct::top, and ANTLR3_STACK_struct::vector. </p>
<p> Referenced by antlr3StackNew().</p>
<h3>static <code>ANTLR3_BOOLEAN</code> antlr3StackPush (<code>pANTLR3_STACK</code> stack, void * element, void(ANTLR3_CDECL *freeptr)(void *)) [static]</h3>
<p>References ANTLR3_VECTOR_struct::add, ANTLR3_STACK_struct::top, and ANTLR3_STACK_struct::vector. </p>
<p> Referenced by antlr3StackNew().</p>
<h3>static <code>ANTLR3_UINT32</code> antlr3StackSize (<code>pANTLR3_STACK</code> stack) [static]</h3>
<p>References ANTLR3_VECTOR_struct::count, and ANTLR3_STACK_struct::vector. </p>
<p> Referenced by antlr3StackNew().</p>
<h3>ANTLR3_API <code>pANTLR3_TOPO</code> antlr3TopoNew ()</h3>
<p>Allocate and initialize a new ANTLR3 topological sorter, which can be used to define edges that identify numerical node indexes that depend on other numerical node indexes, which can then be sorted topologically such that any node is sorted after all its dependent nodes. Use: </p>
<p> /verbatim </p>
<p> pANTLR3_TOPO topo; topo = antlr3NewTopo(); </p>
<p> if (topo == NULL) { out of memory } </p>
<p> topo-&gt;addEdge(topo, 3, 0); // Node 3 depends on node 0 topo-&gt;addEdge(topo, 0, 1); // Node &#8211; depends on node 1 topo-&gt;sortVector(topo, myVector); // Sort the vector in place (node numbers are the vector entry numbers) </p>
<p> /verbatim </p>
<p> References addEdge(), ANTLR3_TOPO_struct::addEdge, ANTLR3_FALSE, ANTLR3_MALLOC, ANTLR3_TOPO_struct::cycle, ANTLR3_TOPO_struct::cycleMark, ANTLR3_TOPO_struct::edges, ANTLR3_TOPO_struct::free, freeTopo(), ANTLR3_TOPO_struct::hasCycle, ANTLR3_TOPO_struct::limit, ANTLR3_TOPO_struct::sorted, sortToArray(), ANTLR3_TOPO_struct::sortToArray, sortVector(), ANTLR3_TOPO_struct::sortVector, and ANTLR3_TOPO_struct::visited.</p>
<h3>static <code>ANTLR3_UINT32</code> antlr3VectorAdd (<code>pANTLR3_VECTOR</code> vector, void * element, void(ANTLR3_CDECL *freeptr)(void *)) [static]</h3>
<p>Add the supplied pointer and freeing function pointer to the list, expanding the vector if needed. </p>
<p> References antlr3VectorResize(), ANTLR3_VECTOR_struct::count, ANTLR3_VECTOR_ELEMENT_struct::element, ANTLR3_VECTOR_struct::elements, and ANTLR3_VECTOR_struct::elementsSize. </p>
<p> Referenced by antlr3SetVectorApi().</p>
<h3>static void antlr3VectorClear (<code>pANTLR3_VECTOR</code> vector) [static]</h3>
<p>References ANTLR3_VECTOR_struct::count, ANTLR3_VECTOR_ELEMENT_struct::element, and ANTLR3_VECTOR_struct::elements. </p>
<p> Referenced by antlr3SetVectorApi().</p>
<h3>static void antlr3VectorDel (<code>pANTLR3_VECTOR</code> vector, <code>ANTLR3_UINT32</code> entry) [static]</h3>
<p>References ANTLR3_MEMMOVE, ANTLR3_VECTOR_struct::count, ANTLR3_VECTOR_ELEMENT_struct::element, and ANTLR3_VECTOR_struct::elements. </p>
<p> Referenced by antlr3SetVectorApi().</p>
<h3>ANTLR3_API <code>pANTLR3_VECTOR_FACTORY</code> antlr3VectorFactoryNew (<code>ANTLR3_UINT32</code> sizeHint)</h3>
<p>Vector factory creation. </p>
<p> References ANTLR3_MALLOC, ANTLR3_TRUE, ANTLR3_VECTOR_INTERNAL_SIZE, antlr3SetVectorApi(), antlr3StackNew(), ANTLR3_VECTOR_FACTORY_struct::close, closeVectorFactory(), ANTLR3_VECTOR_struct::factoryMade, ANTLR3_VECTOR_FACTORY_struct::freeStack, newPool(), newVector(), ANTLR3_VECTOR_FACTORY_struct::newVector, ANTLR3_VECTOR_FACTORY_struct::pools, returnVector(), ANTLR3_VECTOR_FACTORY_struct::returnVector, ANTLR3_VECTOR_FACTORY_struct::thisPool, and ANTLR3_VECTOR_FACTORY_struct::unTruc. </p>
<p> Referenced by antlr3ArboretumNew().</p>
<h3>static void ANTLR3_CDECL antlr3VectorFree (<code>pANTLR3_VECTOR</code> vector) [static]</h3>
<p>References ANTLR3_FALSE, ANTLR3_FREE, ANTLR3_VECTOR_INTERNAL_SIZE, ANTLR3_VECTOR_struct::count, ANTLR3_VECTOR_ELEMENT_struct::element, ANTLR3_VECTOR_struct::elements, ANTLR3_VECTOR_struct::elementsSize, and ANTLR3_VECTOR_struct::factoryMade. </p>
<p> Referenced by antlr3SetVectorApi().</p>
<h3>static void * antlr3VectorGet (<code>pANTLR3_VECTOR</code> vector, <code>ANTLR3_UINT32</code> entry) [static]</h3>
<p>References ANTLR3_VECTOR_ELEMENT_struct::element, and ANTLR3_VECTOR_struct::elements. </p>
<p> Referenced by antlr3SetVectorApi().</p>
<h3>ANTLR3_API <code>pANTLR3_VECTOR</code> antlr3VectorNew (<code>ANTLR3_UINT32</code> sizeHint)</h3>
<p>References ANTLR3_ERR_NOMEM, ANTLR3_FUNC_PTR, ANTLR3_MALLOC, and antlr3SetVectorApi(). </p>
<p> Referenced by antlr3BaseRecognizerNew(), antlr3CommonTokenStreamNew(), antlr3CommonTreeNodeStreamNew(), antlr3CommonTreeNodeStreamNewStream(), antlr3InputReset(), antlr3StackNew(), antlr3StringFactoryNew(), and replaceChildren().</p>
<h3>static void antlr3VectorResize (<code>pANTLR3_VECTOR</code> vector, <code>ANTLR3_UINT32</code> hint) [static]</h3>
<p>References ANTLR3_MALLOC, ANTLR3_MEMCPY, ANTLR3_REALLOC, ANTLR3_VECTOR_INTERNAL_SIZE, ANTLR3_VECTOR_struct::elements, ANTLR3_VECTOR_struct::elementsSize, and ANTLR3_VECTOR_struct::internal. </p>
<p> Referenced by antlr3VectorAdd(), and antlr3VectorSet().</p>
<h3>static <code>ANTLR3_UINT32</code> antlr3VectorSet (<code>pANTLR3_VECTOR</code> vector, <code>ANTLR3_UINT32</code> entry, void * element, void(ANTLR3_CDECL *freeptr)(void *), <code>ANTLR3_BOOLEAN</code> freeExisting) [static]</h3>
<p>Replace the element at the specified entry point with the supplied entry. </p>
<p> References antlr3VectorResize(), ANTLR3_VECTOR_struct::count, ANTLR3_VECTOR_ELEMENT_struct::element, ANTLR3_VECTOR_struct::elements, and ANTLR3_VECTOR_struct::elementsSize. </p>
<p> Referenced by antlr3SetVectorApi().</p>
<h3>static <code>ANTLR3_UINT32</code> antlr3VectorSize (<code>pANTLR3_VECTOR</code> vector) [static]</h3>
<p>References ANTLR3_VECTOR_struct::count. </p>
<p> Referenced by antlr3SetVectorApi().</p>
<h3>static <code>ANTLR3_BOOLEAN</code> antlr3VectorSwap (<code>pANTLR3_VECTOR</code> vector, <code>ANTLR3_UINT32</code> entry1, <code>ANTLR3_UINT32</code> entry2) [static]</h3>
<p>Replace the element at the specified entry point with the supplied entry. </p>
<p> References ANTLR3_CDECL, ANTLR3_FALSE, ANTLR3_TRUE, ANTLR3_VECTOR_ELEMENT_struct::element, ANTLR3_VECTOR_struct::elements, and ANTLR3_VECTOR_struct::elementsSize. </p>
<p> Referenced by antlr3SetVectorApi().</p>
<h3>static void * antrl3VectorRemove (<code>pANTLR3_VECTOR</code> vector, <code>ANTLR3_UINT32</code> entry) [static]</h3>
<p>Remove the entry from the vector, but do not free any entry, even if it has a free pointer. </p>
<p> References ANTLR3_MEMMOVE, ANTLR3_VECTOR_struct::count, ANTLR3_VECTOR_ELEMENT_struct::element, and ANTLR3_VECTOR_struct::elements. </p>
<p> Referenced by antlr3SetVectorApi().</p>
<h3>static void closeVectorFactory (<code>pANTLR3_VECTOR_FACTORY</code> factory) [static]</h3>
<p>References ANTLR3_FACTORY_VPOOL_SIZE, ANTLR3_FREE, ANTLR3_TRUE, ANTLR3_VECTOR_INTERNAL_SIZE, ANTLR3_VECTOR_struct::elements, ANTLR3_VECTOR_struct::elementsSize, ANTLR3_VECTOR_struct::factoryMade, ANTLR3_STACK_struct::free, ANTLR3_VECTOR_FACTORY_struct::freeStack, ANTLR3_VECTOR_FACTORY_struct::nextVector, ANTLR3_VECTOR_FACTORY_struct::pools, and ANTLR3_VECTOR_FACTORY_struct::thisPool. </p>
<p> Referenced by antlr3VectorFactoryNew().</p>
<h3>static void DFS (<code>pANTLR3_TOPO</code> topo, <code>ANTLR3_UINT32</code> node) [static]</h3>
<p>Given a starting node, descend its dependent nodes (ones that it has edges to) until we find one without edges. Having found a node without edges, we have discovered the bottom of a depth first search, which we can then ascend, adding the nodes in order from the bottom, which gives us the dependency order. </p>
<p> References ANTLR3_BITSET_struct::add, ANTLR3_FALSE, ANTLR3_TRUE, ANTLR3_TOPO_struct::cycle, ANTLR3_TOPO_struct::cycleMark, ANTLR3_TOPO_struct::edges, ANTLR3_TOPO_struct::hasCycle, ANTLR3_BITSET_struct::isMember, ANTLR3_TOPO_struct::limit, ANTLR3_BITSET_struct::numBits, ANTLR3_BITSET_struct::size, ANTLR3_TOPO_struct::sorted, and ANTLR3_TOPO_struct::visited. </p>
<p> Referenced by sortToArray().</p>
<h3>static void freeIntNode (<code>pANTLR3_INT_TRIE_NODE</code> node) [static]</h3>
<p>Release memory allocated to this tree. Basic algorithm is that we do a depth first left descent and free up any nodes that are not backward pointers. </p>
<p> References ANTLR3_FREE, ANTLR3_HASH_TYPE_STR, ANTLR3_INT_TRIE_NODE_struct::bitNum, ANTLR3_INT_TRIE_NODE_struct::buckets, ANTLR3_TRIE_ENTRY_struct::data, ANTLR3_INT_TRIE_NODE_struct::leftN, ANTLR3_TRIE_ENTRY_struct::next, ANTLR3_TRIE_ENTRY_struct::ptr, ANTLR3_INT_TRIE_NODE_struct::rightN, and ANTLR3_TRIE_ENTRY_struct::type. </p>
<p> Referenced by intTrieFree().</p>
<h3>static void freeTopo (<code>pANTLR3_TOPO</code> topo) [static]</h3>
<p>References ANTLR3_FREE, ANTLR3_TOPO_struct::cycle, ANTLR3_TOPO_struct::edges, ANTLR3_BITSET_struct::free, ANTLR3_TOPO_struct::limit, ANTLR3_TOPO_struct::sorted, and ANTLR3_TOPO_struct::visited. </p>
<p> Referenced by antlr3TopoNew().</p>
<h3>static <code>ANTLR3_BOOLEAN</code> intTrieAdd (<code>pANTLR3_INT_TRIE</code> trie, <code>ANTLR3_INTKEY</code> key, <code>ANTLR3_UINT32</code> type, <code>ANTLR3_INTKEY</code> intVal, void * data, void(ANTLR3_CDECL *freeptr)(void *)) [static]</h3>
<p>Add an entry into the INT trie. Basically we descend the trie as we do when searching it, which will locate the only node in the trie that can be reached by the bit pattern of the key. If the key is actually at that node, then if the trie accepts duplicates we add the supplied data in a new chained bucket to that data node. If it does not accept duplicates then we merely return FALSE in case the caller wants to know whether the key was already in the trie. If the node we locate is not the key we are looking to add, then we insert a new node into the trie with a bit index of the leftmost differing bit and the left or right node pointing to itself or the data node we are inserting &#8216;before&#8217;. </p>
<p> References ANTLR3_INT_TRIE_struct::allowDups, ANTLR3_CALLOC, ANTLR3_FALSE, ANTLR3_HASH_TYPE_STR, ANTLR3_TRUE, ANTLR3_INT_TRIE_NODE_struct::bitNum, ANTLR3_INT_TRIE_NODE_struct::buckets, ANTLR3_INT_TRIE_struct::count, ANTLR3_TRIE_ENTRY_struct::data, ANTLR3_TRIE_ENTRY_struct::intVal, ANTLR3_INT_TRIE_NODE_struct::key, ANTLR3_INT_TRIE_NODE_struct::leftN, ANTLR3_TRIE_ENTRY_struct::next, nextNode(), ANTLR3_TRIE_ENTRY_struct::ptr, ANTLR3_INT_TRIE_NODE_struct::rightN, ANTLR3_INT_TRIE_struct::root, and ANTLR3_TRIE_ENTRY_struct::type. </p>
<p> Referenced by antlr3IntTrieNew().</p>
<h3>static <code>ANTLR3_BOOLEAN</code> intTrieDel (<code>pANTLR3_INT_TRIE</code> trie, <code>ANTLR3_INTKEY</code> key) [static]</h3>
<p>References ANTLR3_FALSE, and ANTLR3_INT_TRIE_struct::root. </p>
<p> Referenced by antlr3IntTrieNew().</p>
<h3>static void intTrieFree (<code>pANTLR3_INT_TRIE</code> trie) [static]</h3>
<p>Called to free all nodes and the structure itself. </p>
<p> References ANTLR3_FREE, freeIntNode(), and ANTLR3_INT_TRIE_struct::root. </p>
<p> Referenced by antlr3IntTrieNew().</p>
<h3>static <code>pANTLR3_TRIE_ENTRY</code> intTrieGet (<code>pANTLR3_INT_TRIE</code> trie, <code>ANTLR3_INTKEY</code> key) [static]</h3>
<p>Search the int Trie and return a pointer to the first bucket indexed by the key if it is contained in the trie, otherwise NULL. </p>
<p> References ANTLR3_INT_TRIE_NODE_struct::bitNum, ANTLR3_INT_TRIE_NODE_struct::buckets, ANTLR3_INT_TRIE_struct::count, ANTLR3_INT_TRIE_NODE_struct::key, ANTLR3_INT_TRIE_NODE_struct::leftN, nextNode(), ANTLR3_INT_TRIE_NODE_struct::rightN, and ANTLR3_INT_TRIE_struct::root. </p>
<p> Referenced by antlr3IntTrieNew().</p>
<h3>static void newPool (<code>pANTLR3_VECTOR_FACTORY</code> factory) [static]</h3>
<p>References ANTLR3_FACTORY_VPOOL_SIZE, ANTLR3_MALLOC, ANTLR3_REALLOC, ANTLR3_VECTOR_FACTORY_struct::nextVector, ANTLR3_VECTOR_FACTORY_struct::pools, and ANTLR3_VECTOR_FACTORY_struct::thisPool. </p>
<p> Referenced by antlr3VectorFactoryNew(), and newVector().</p>
<h3>static <code>pANTLR3_VECTOR</code> newVector (<code>pANTLR3_VECTOR_FACTORY</code> factory) [static]</h3>
<p>References ANTLR3_FACTORY_VPOOL_SIZE, ANTLR3_TRUE, ANTLR3_VECTOR_INTERNAL_SIZE, antlr3SetVectorApi(), ANTLR3_VECTOR_struct::elements, ANTLR3_VECTOR_struct::factoryMade, ANTLR3_VECTOR_FACTORY_struct::freeStack, ANTLR3_VECTOR_struct::internal, newPool(), ANTLR3_VECTOR_FACTORY_struct::nextVector, ANTLR3_STACK_struct::peek, ANTLR3_VECTOR_FACTORY_struct::pools, ANTLR3_STACK_struct::pop, and ANTLR3_VECTOR_FACTORY_struct::thisPool. </p>
<p> Referenced by antlr3VectorFactoryNew().</p>
<h3>static void returnVector (<code>pANTLR3_VECTOR_FACTORY</code> factory, <code>pANTLR3_VECTOR</code> vector) [static]</h3>
<p>References ANTLR3_VECTOR_struct::clear, ANTLR3_VECTOR_FACTORY_struct::freeStack, and ANTLR3_STACK_struct::push. </p>
<p> Referenced by antlr3VectorFactoryNew().</p>
<h3>static <code>pANTLR3_UINT32</code> sortToArray (<code>pANTLR3_TOPO</code> topo) [static]</h3>
<p>References ANTLR3_FALSE, ANTLR3_MALLOC, ANTLR3_TRUE, antlr3BitsetNew(), ANTLR3_TOPO_struct::cycle, DFS(), ANTLR3_TOPO_struct::edges, ANTLR3_TOPO_struct::hasCycle, ANTLR3_BITSET_struct::isMember, ANTLR3_TOPO_struct::limit, ANTLR3_TOPO_struct::sorted, and ANTLR3_TOPO_struct::visited. </p>
<p> Referenced by antlr3TopoNew().</p>
<h3>static void sortVector (<code>pANTLR3_TOPO</code> topo, <code>pANTLR3_VECTOR</code> v) [static]</h3>
<p>References ANTLR3_FREE, ANTLR3_MALLOC, ANTLR3_TRUE, ANTLR3_VECTOR_struct::count, ANTLR3_TOPO_struct::hasCycle, ANTLR3_TOPO_struct::limit, ANTLR3_TOPO_struct::sorted, ANTLR3_TOPO_struct::sortToArray, and ANTLR3_VECTOR_struct::swap. </p>
<p> Referenced by antlr3TopoNew().</p>
<h2>Variable Documentation</h2>
<h3><code>ANTLR3_UINT8</code> <code>bitIndex</code>[256] [static]<code>Initial value:</code></h3>
<pre>{ 
 0, 
 0, 
 1, 1, 
 2, 2, 2, 2, 
 3, 3, 3, 3, 3, 3, 3, 3, 
 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 
 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 
 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 
 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 
 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 
 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 
 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 
 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7
}</pre>
<p>Array of left most significant bit positions for an 8 bit element provides an efficient way to find the highest bit that is set in an n byte value (n&gt;0). Assuming the values will all hit the data cache, coding without conditional elements should allow branch prediction to work well and of course a parallel instruction cache will whip through this. Otherwise we must loop shifting a one bit and masking. The values we tend to be placing in out integer patricia trie are usually a lot lower than the 64 bits we allow for the key allows. Hence there is a lot of redundant looping and shifting in a while loop. Whereas, the lookup table is just a few ands and indirect lookups, while testing for 0. This is likely to be done in parallel on many processors available when I wrote this. If this code survives as long as yacc, then I may already be dead by the time you read this and maybe there is a single machine instruction to perform the operation. What else are you going to do with all those transistors? Jim 2007 </p>
<p> The table is probably obvious but it is just the number 0..7 of the MSB in each integer value 0..256</p>
<h3><code>ANTLR3_UINT64</code> bitMask[64] [static]<code>Initial value:</code></h3>
<pre>{
 0x0000000000000001ULL, 0x0000000000000002ULL, 0x0000000000000004ULL, 0x0000000000000008ULL,
 0x0000000000000010ULL, 0x0000000000000020ULL, 0x0000000000000040ULL, 0x0000000000000080ULL,
 0x0000000000000100ULL, 0x0000000000000200ULL, 0x0000000000000400ULL, 0x0000000000000800ULL,
 0x0000000000001000ULL, 0x0000000000002000ULL, 0x0000000000004000ULL, 0x0000000000008000ULL,
 0x0000000000010000ULL, 0x0000000000020000ULL, 0x0000000000040000ULL, 0x0000000000080000ULL,
 0x0000000000100000ULL, 0x0000000000200000ULL, 0x0000000000400000ULL, 0x0000000000800000ULL,
 0x0000000001000000ULL, 0x0000000002000000ULL, 0x0000000004000000ULL, 0x0000000008000000ULL,
 0x0000000010000000ULL, 0x0000000020000000ULL, 0x0000000040000000ULL, 0x0000000080000000ULL,
 0x0000000100000000ULL, 0x0000000200000000ULL, 0x0000000400000000ULL, 0x0000000800000000ULL,
 0x0000001000000000ULL, 0x0000002000000000ULL, 0x0000004000000000ULL, 0x0000008000000000ULL,
 0x0000010000000000ULL, 0x0000020000000000ULL, 0x0000040000000000ULL, 0x0000080000000000ULL,
 0x0000100000000000ULL, 0x0000200000000000ULL, 0x0000400000000000ULL, 0x0000800000000000ULL,
 0x0001000000000000ULL, 0x0002000000000000ULL, 0x0004000000000000ULL, 0x0008000000000000ULL,
 0x0010000000000000ULL, 0x0020000000000000ULL, 0x0040000000000000ULL, 0x0080000000000000ULL,
 0x0100000000000000ULL, 0x0200000000000000ULL, 0x0400000000000000ULL, 0x0800000000000000ULL,
 0x1000000000000000ULL, 0x2000000000000000ULL, 0x4000000000000000ULL, 0x8000000000000000ULL
}</pre>
<p>Rather than use the bit index of a trie node to shift 0x01 left that many times, then &amp; with the result, it is faster to use the bit index as an index into this table which holds precomputed masks for any of the 64 bits we need to mask off singly. The data values will stay in cache while ever a trie is in heavy use, such as in memoization. It is also pretty enough to be ASCII art.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for ANTLR3C from the source code.</p>
