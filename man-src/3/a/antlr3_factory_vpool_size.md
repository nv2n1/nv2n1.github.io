---
title: "antlr3_factory_vpool_size(3)"
name: "antlr3_factory_vpool_size"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3_factory_vpool_size/"
description: "include/antlr3collections.h –"
---

<p>include/antlr3collections.h &#8211; </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/antlr3defs.h">antlr3defs.h</a>&gt;<br />
 #include &lt;<a href="file:/usr/include/antlr3bitset.h">antlr3bitset.h</a>&gt; </p>
<h3>Data Structures</h3>
<p>struct <code>ANTLR3_HASH_BUCKET_struct</code><br />
 <i>Internal structure of a hash table bucket, which tracks all keys that hash to the same bucket. </i><br />
 struct <code>ANTLR3_HASH_ENTRY_struct</code><br />
 <i>Internal structure representing an element in a hash bucket. </i><br />
 struct <code>ANTLR3_HASH_ENUM_struct</code><br />
 <i>Internal structure representing an enumeration of a table. </i><br />
 struct <code>ANTLR3_HASH_KEY_struct</code> </p>
<p> struct <code>ANTLR3_HASH_TABLE_struct</code><br />
 <i>Structure that tracks a hash table. </i><br />
 struct <code>ANTLR3_INT_TRIE_NODE_struct</code><br />
 <i>Structure that defines an element/node in an ANTLR3_INT_TRIE. </i><br />
 struct <code>ANTLR3_INT_TRIE_struct</code><br />
 <i>Structure that defines an ANTLR3_INT_TRIE. </i><br />
 struct <code>ANTLR3_LIST_struct</code><br />
 <i>Structure that represents a LIST collection. </i><br />
 struct <code>ANTLR3_STACK_struct</code><br />
 <i>Structure that represents a Stack collection. </i><br />
 struct <code>ANTLR3_TOPO_struct</code><br />
 <i>A topological sort system that given a set of dependencies of a node m on node n, can sort them in dependency order. </i><br />
 struct <code>ANTLR3_TRIE_ENTRY_struct</code><br />
 <i>Structure that holds the payload entry in an ANTLR3_INT_TRIE or ANTLR3_STRING_TRIE. </i><br />
 struct <code>ANTLR3_VECTOR_ELEMENT_struct</code> </p>
<p> struct <code>ANTLR3_VECTOR_FACTORY_struct</code><br />
 <i>Structure that tracks vectors in a vector and auto deletes the vectors in the vector factory when closed. </i><br />
 struct <code>ANTLR3_VECTOR_struct</code> </p>
<h3>Defines</h3>
<p>#define <code>ANTLR3_FACTORY_VPOOL_SIZE</code> 256<br />
 <i>Default vector pool size if otherwise unspecified. </i><br />
 #define <code>ANTLR3_HASH_TYPE_INT</code> 0<br />
 <i>Indicates the hashed file has integer keys. </i><br />
 #define <code>ANTLR3_HASH_TYPE_STR</code> 1<br />
 <i>Indicates the hashed file has numeric keys. </i><br />
 #define <code>ANTLR3_VECTOR_INTERNAL_SIZE</code> 16 </p>
<h3>Typedefs</h3>
<p>typedef struct <code>ANTLR3_HASH_BUCKET_struct</code> <code>ANTLR3_HASH_BUCKET</code><br />
 <i>Internal structure of a hash table bucket, which tracks all keys that hash to the same bucket. </i><br />
 typedef struct <code>ANTLR3_HASH_ENTRY_struct</code> <code>ANTLR3_HASH_ENTRY</code><br />
 <i>Internal structure representing an element in a hash bucket. </i><br />
 typedef struct <code>ANTLR3_HASH_ENUM_struct</code> <code>ANTLR3_HASH_ENUM</code><br />
 <i>Internal structure representing an enumeration of a table. </i><br />
 typedef struct <code>ANTLR3_HASH_KEY_struct</code> <code>ANTLR3_HASH_KEY</code> </p>
<p> typedef struct <code>ANTLR3_HASH_TABLE_struct</code> <code>ANTLR3_HASH_TABLE</code><br />
 <i>Structure that tracks a hash table. </i><br />
 typedef struct <code>ANTLR3_INT_TRIE_struct</code> <code>ANTLR3_INT_TRIE</code><br />
 <i>Structure that defines an ANTLR3_INT_TRIE. </i><br />
 typedef struct <code>ANTLR3_INT_TRIE_NODE_struct</code> <code>ANTLR3_INT_TRIE_NODE</code><br />
 <i>Structure that defines an element/node in an ANTLR3_INT_TRIE. </i><br />
 typedef struct <code>ANTLR3_LIST_struct</code> <code>ANTLR3_LIST</code><br />
 <i>Structure that represents a LIST collection. </i><br />
 typedef struct <code>ANTLR3_STACK_struct</code> <code>ANTLR3_STACK</code><br />
 <i>Structure that represents a Stack collection. </i><br />
 typedef struct <code>ANTLR3_TOPO_struct</code> <code>ANTLR3_TOPO</code><br />
 <i>A topological sort system that given a set of dependencies of a node m on node n, can sort them in dependency order. </i><br />
 typedef struct <code>ANTLR3_TRIE_ENTRY_struct</code> <code>ANTLR3_TRIE_ENTRY</code><br />
 <i>Structure that holds the payload entry in an ANTLR3_INT_TRIE or ANTLR3_STRING_TRIE. </i><br />
 typedef struct <code>ANTLR3_VECTOR_struct</code> <code>ANTLR3_VECTOR</code> </p>
<p> typedef struct <code>ANTLR3_VECTOR_ELEMENT_struct</code> <code>ANTLR3_VECTOR_ELEMENT</code> </p>
<p> typedef struct <code>ANTLR3_VECTOR_FACTORY_struct</code> <code>ANTLR3_VECTOR_FACTORY</code><br />
 <i>Structure that tracks vectors in a vector and auto deletes the vectors in the vector factory when closed. </i><br />
 typedef struct <code>ANTLR3_HASH_KEY_struct</code> * <code>pANTLR3_HASH_KEY</code> </p>
<p> typedef struct <code>ANTLR3_INT_TRIE_NODE_struct</code> * <code>pANTLR3_INT_TRIE_NODE</code> </p>
<p> typedef struct <code>ANTLR3_TRIE_ENTRY_struct</code> * <code>pANTLR3_TRIE_ENTRY</code> </p>
<p> typedef struct <code>ANTLR3_VECTOR_ELEMENT_struct</code> * <code>pANTLR3_VECTOR_ELEMENT</code> </p>
<h2>Define Documentation</h2>
<h3>#define ANTLR3_FACTORY_VPOOL_SIZE 256</h3>
<p>Default vector pool size if otherwise unspecified. </p>
<p> Referenced by closeVectorFactory(), newPool(), and newVector().</p>
<h3>#define ANTLR3_HASH_TYPE_INT 0</h3>
<p>Indicates the hashed file has integer keys. </p>
<p> Referenced by antlr3HashPutI(), and memoize().</p>
<h3>#define ANTLR3_HASH_TYPE_STR 1</h3>
<p>Indicates the hashed file has numeric keys. </p>
<p> Referenced by antlr3HashFree(), antlr3HashPut(), freeIntNode(), getRuleMemoization(), and intTrieAdd().</p>
<h3>#define ANTLR3_VECTOR_INTERNAL_SIZE 16</h3>
<p>Referenced by antlr3SetVectorApi(), antlr3VectorFactoryNew(), antlr3VectorFree(), antlr3VectorResize(), closeVectorFactory(), and newVector().</p>
<h2>Typedef Documentation</h2>
<h3>typedef struct <code>ANTLR3_HASH_BUCKET_struct</code></h3>
<p>&nbsp;<wbr>&nbsp;<wbr><code>ANTLR3_HASH_BUCKET</code>&quot; </p>
<p> Internal structure of a hash table bucket, which tracks all keys that hash to the same bucket.</p>
<h3>typedef struct <code>ANTLR3_HASH_ENTRY_struct</code></h3>
<p>&nbsp;<wbr>&nbsp;<wbr><code>ANTLR3_HASH_ENTRY</code>&quot; </p>
<p> Internal structure representing an element in a hash bucket. Stores the original key so that duplicate keys can be rejected if necessary, and contains function can be supported. If the hash key could be unique I would have invented the perfect compression algorithm ;-)</p>
<h3>typedef struct <code>ANTLR3_HASH_ENUM_struct</code></h3>
<p>&nbsp;<wbr>&nbsp;<wbr><code>ANTLR3_HASH_ENUM</code>&quot; </p>
<p> Internal structure representing an enumeration of a table. This is returned by antlr3Enumeration() Allows the programmer to traverse the table in hash order without knowing what is in the actual table. </p>
<p> Note that it is up to the caller to ensure that the table structure does not change in the hash bucket that is currently being enumerated as this structure just tracks the next pointers in the bucket series.</p>
<h3>typedef struct <code>ANTLR3_HASH_KEY_struct</code> <code>ANTLR3_HASH_KEY</code></h3>
<h3>typedef struct <code>ANTLR3_HASH_TABLE_struct</code></h3>
<p>&nbsp;<wbr>&nbsp;<wbr><code>ANTLR3_HASH_TABLE</code>&quot; </p>
<p> Structure that tracks a hash table.</p>
<h3>typedef struct <code>ANTLR3_INT_TRIE_struct</code></h3>
<p>&nbsp;<wbr>&nbsp;<wbr><code>ANTLR3_INT_TRIE</code>&quot; </p>
<p> Structure that defines an ANTLR3_INT_TRIE. For this particular implementation, as you might expect, the key is turned into a &#8216;string&#8217; by looking at bit(key, depth) of the integer key. Using 64 bit keys gives us a depth limit of 64 (or bit 0..63) and potentially a huge trie. This is the algorithm for a Patricia Trie. Note also that this trie [can] accept multiple entries for the same key and is therefore a kind of elastic bucket patricia trie. </p>
<p> If you find this code useful, please feel free to &#8216;steal&#8217; it for any purpose as covered by the BSD license under which ANTLR is issued. You can cut the code but as the ANTLR library is only about 50K (Windows Vista), you might find it easier to just link the library. Please keep all comments and licenses and so on in any version of this you create of course. </p>
<p> Jim Idle.</p>
<h3>typedef struct <code>ANTLR3_INT_TRIE_NODE_struct</code></h3>
<p>&nbsp;<wbr>&nbsp;<wbr><code>ANTLR3_INT_TRIE_NODE</code>&quot; </p>
<p> Structure that defines an element/node in an ANTLR3_INT_TRIE.</p>
<h3>typedef struct <code>ANTLR3_LIST_struct</code></h3>
<p>&nbsp;<wbr>&nbsp;<wbr><code>ANTLR3_LIST</code>&quot; </p>
<p> Structure that represents a LIST collection.</p>
<h3>typedef struct <code>ANTLR3_STACK_struct</code></h3>
<p>&nbsp;<wbr>&nbsp;<wbr><code>ANTLR3_STACK</code>&quot; </p>
<p> Structure that represents a Stack collection.</p>
<h3>typedef struct <code>ANTLR3_TOPO_struct</code></h3>
<p>&nbsp;<wbr>&nbsp;<wbr><code>ANTLR3_TOPO</code>&quot; </p>
<p> A topological sort system that given a set of dependencies of a node m on node n, can sort them in dependency order. This is a generally useful utility object that does not care what the things are it is sorting. Generally the set to be sorted will be numeric indexes into some other structure such as an ANTLR3_VECTOR. I have provided a sort method that given ANTLR3_VECTOR as an input will sort the vector entries in place, as well as a sort method that just returns an array of the sorted noded indexes, in case you are not sorting ANTLR3_VECTORS but some set of your own device. </p>
<p> Of the two main algorithms that could be used, I chose to use the depth first search for unvisited nodes as a) This runs in linear time, and b) it is what we used in the ANTLR Tool to perform a topological sort of the input grammar files based on their dependencies.</p>
<h3>typedef struct <code>ANTLR3_TRIE_ENTRY_struct</code></h3>
<p>&nbsp;<wbr><code>ANTLR3_TRIE_ENTRY</code>&quot; </p>
<p> Structure that holds the payload entry in an ANTLR3_INT_TRIE or ANTLR3_STRING_TRIE.</p>
<h3>typedef struct <code>ANTLR3_VECTOR_struct</code></h3>
<p>&nbsp;<wbr>&nbsp;<wbr><code>ANTLR3_VECTOR</code>&quot;</p>
<h3>typedef struct <code>ANTLR3_VECTOR_ELEMENT_struct</code></h3>
<p>&nbsp;<wbr>&nbsp;<wbr><code>ANTLR3_VECTOR_ELEMENT</code>&quot;</p>
<h3>typedef struct <code>ANTLR3_VECTOR_FACTORY_struct</code></h3>
<p>&nbsp;<wbr><code>ANTLR3_VECTOR_FACTORY</code>&quot; </p>
<p> Structure that tracks vectors in a vector and auto deletes the vectors in the vector factory when closed.</p>
<h3>typedef struct <code>ANTLR3_HASH_KEY_struct</code> * <code>pANTLR3_HASH_KEY</code></h3>
<h3>typedef struct <code>ANTLR3_INT_TRIE_NODE_struct</code> * <code>pANTLR3_INT_TRIE_NODE</code></h3>
<h3>typedef struct <code>ANTLR3_TRIE_ENTRY_struct</code> * <code>pANTLR3_TRIE_ENTRY</code></h3>
<h3>typedef struct <code>ANTLR3_VECTOR_ELEMENT_struct</code> * <code>pANTLR3_VECTOR_ELEMENT</code></h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for ANTLR3C from the source code.</p>
