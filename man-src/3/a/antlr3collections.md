---
title: "antlr3collections(3)"
name: "antlr3collections"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3collections/"
---

<h2 class="name">NAME</h2>
 

 include/antlr3collections.h - 

<h2>SYNOPSIS</h2>

 
 

 #include &lt;<a HREF="file:/usr/include/antlr3defs.h">antlr3defs.h</a>&gt; 
 #include &lt;<a HREF="file:/usr/include/antlr3bitset.h">antlr3bitset.h</a>&gt; 
 

<h3>Data Structures</h3>

 

 
 struct <b>ANTLR3_HASH_BUCKET_struct</b> 
 <i>Internal structure of a hash table bucket, which tracks all keys that hash to the same bucket. </i> 
 struct <b>ANTLR3_HASH_ENTRY_struct</b> 
 <i>Internal structure representing an element in a hash bucket. </i> 
 struct <b>ANTLR3_HASH_ENUM_struct</b> 
 <i>Internal structure representing an enumeration of a table. </i> 
 struct <b>ANTLR3_HASH_KEY_struct</b> 
 
 struct <b>ANTLR3_HASH_TABLE_struct</b> 
 <i>Structure that tracks a hash table. </i> 
 struct <b>ANTLR3_INT_TRIE_NODE_struct</b> 
 <i>Structure that defines an element/node in an ANTLR3_INT_TRIE. </i> 
 struct <b>ANTLR3_INT_TRIE_struct</b> 
 <i>Structure that defines an ANTLR3_INT_TRIE. </i> 
 struct <b>ANTLR3_LIST_struct</b> 
 <i>Structure that represents a LIST collection. </i> 
 struct <b>ANTLR3_STACK_struct</b> 
 <i>Structure that represents a Stack collection. </i> 
 struct <b>ANTLR3_TOPO_struct</b> 
 <i>A topological sort system that given a set of dependencies of a node m on node n, can sort them in dependency order. </i> 
 struct <b>ANTLR3_TRIE_ENTRY_struct</b> 
 <i>Structure that holds the payload entry in an ANTLR3_INT_TRIE or ANTLR3_STRING_TRIE. </i> 
 struct <b>ANTLR3_VECTOR_ELEMENT_struct</b> 
 
 struct <b>ANTLR3_VECTOR_FACTORY_struct</b> 
 <i>Structure that tracks vectors in a vector and auto deletes the vectors in the vector factory when closed. </i> 
 struct <b>ANTLR3_VECTOR_struct</b> 

<h3>Defines</h3>

 

 
 #define <b>ANTLR3_FACTORY_VPOOL_SIZE</b> 256 
 <i>Default vector pool size if otherwise unspecified. </i> 
 #define <b>ANTLR3_HASH_TYPE_INT</b> 0 
 <i>Indicates the hashed file has integer keys. </i> 
 #define <b>ANTLR3_HASH_TYPE_STR</b> 1 
 <i>Indicates the hashed file has numeric keys. </i> 
 #define <b>ANTLR3_VECTOR_INTERNAL_SIZE</b> 16 

<h3>Typedefs</h3>

 

 
 typedef struct <b>ANTLR3_HASH_BUCKET_struct</b> <b>ANTLR3_HASH_BUCKET</b> 
 <i>Internal structure of a hash table bucket, which tracks all keys that hash to the same bucket. </i> 
 typedef struct <b>ANTLR3_HASH_ENTRY_struct</b> <b>ANTLR3_HASH_ENTRY</b> 
 <i>Internal structure representing an element in a hash bucket. </i> 
 typedef struct <b>ANTLR3_HASH_ENUM_struct</b> <b>ANTLR3_HASH_ENUM</b> 
 <i>Internal structure representing an enumeration of a table. </i> 
 typedef struct <b>ANTLR3_HASH_KEY_struct</b> <b>ANTLR3_HASH_KEY</b> 
 
 typedef struct <b>ANTLR3_HASH_TABLE_struct</b> <b>ANTLR3_HASH_TABLE</b> 
 <i>Structure that tracks a hash table. </i> 
 typedef struct <b>ANTLR3_INT_TRIE_struct</b> <b>ANTLR3_INT_TRIE</b> 
 <i>Structure that defines an ANTLR3_INT_TRIE. </i> 
 typedef struct <b>ANTLR3_INT_TRIE_NODE_struct</b> <b>ANTLR3_INT_TRIE_NODE</b> 
 <i>Structure that defines an element/node in an ANTLR3_INT_TRIE. </i> 
 typedef struct <b>ANTLR3_LIST_struct</b> <b>ANTLR3_LIST</b> 
 <i>Structure that represents a LIST collection. </i> 
 typedef struct <b>ANTLR3_STACK_struct</b> <b>ANTLR3_STACK</b> 
 <i>Structure that represents a Stack collection. </i> 
 typedef struct <b>ANTLR3_TOPO_struct</b> <b>ANTLR3_TOPO</b> 
 <i>A topological sort system that given a set of dependencies of a node m on node n, can sort them in dependency order. </i> 
 typedef struct <b>ANTLR3_TRIE_ENTRY_struct</b> <b>ANTLR3_TRIE_ENTRY</b> 
 <i>Structure that holds the payload entry in an ANTLR3_INT_TRIE or ANTLR3_STRING_TRIE. </i> 
 typedef struct <b>ANTLR3_VECTOR_struct</b> <b>ANTLR3_VECTOR</b> 
 
 typedef struct <b>ANTLR3_VECTOR_ELEMENT_struct</b> <b>ANTLR3_VECTOR_ELEMENT</b> 
 
 typedef struct <b>ANTLR3_VECTOR_FACTORY_struct</b> <b>ANTLR3_VECTOR_FACTORY</b> 
 <i>Structure that tracks vectors in a vector and auto deletes the vectors in the vector factory when closed. </i> 
 typedef struct <b>ANTLR3_HASH_KEY_struct</b> * <b>pANTLR3_HASH_KEY</b> 
 
 typedef struct <b>ANTLR3_INT_TRIE_NODE_struct</b> * <b>pANTLR3_INT_TRIE_NODE</b> 
 
 typedef struct <b>ANTLR3_TRIE_ENTRY_struct</b> * <b>pANTLR3_TRIE_ENTRY</b> 
 
 typedef struct <b>ANTLR3_VECTOR_ELEMENT_struct</b> * <b>pANTLR3_VECTOR_ELEMENT</b> 

<h2>Define Documentation</h2>

 

<h3>#define ANTLR3_FACTORY_VPOOL_SIZE 256</h3>

 

 Default vector pool size if otherwise unspecified. 

 Referenced by closeVectorFactory(), newPool(), and newVector().

<h3>#define ANTLR3_HASH_TYPE_INT 0</h3>

 

 Indicates the hashed file has integer keys. 

 Referenced by antlr3HashPutI(), and memoize().

<h3>#define ANTLR3_HASH_TYPE_STR 1</h3>

 

 Indicates the hashed file has numeric keys. 

 Referenced by antlr3HashFree(), antlr3HashPut(), freeIntNode(), getRuleMemoization(), and intTrieAdd().

<h3>#define ANTLR3_VECTOR_INTERNAL_SIZE 16</h3>

 

 Referenced by antlr3SetVectorApi(), antlr3VectorFactoryNew(), antlr3VectorFree(), antlr3VectorResize(), closeVectorFactory(), and newVector().

<h2>Typedef Documentation</h2>

 

<h3>typedef struct <b>ANTLR3_HASH_BUCKET_struct</b></h3>

 
&nbsp;<wbr>&nbsp;<wbr><b>ANTLR3_HASH_BUCKET</b>&quot; 

 Internal structure of a hash table bucket, which tracks all keys that hash to the same bucket.

<h3>typedef struct <b>ANTLR3_HASH_ENTRY_struct</b></h3>

 
&nbsp;<wbr>&nbsp;<wbr><b>ANTLR3_HASH_ENTRY</b>&quot; 

 Internal structure representing an element in a hash bucket. Stores the original key so that duplicate keys can be rejected if necessary, and contains function can be supported. If the hash key could be unique I would have invented the perfect compression algorithm ;-)

<h3>typedef struct <b>ANTLR3_HASH_ENUM_struct</b></h3>

 
&nbsp;<wbr>&nbsp;<wbr><b>ANTLR3_HASH_ENUM</b>&quot; 

 Internal structure representing an enumeration of a table. This is returned by antlr3Enumeration() Allows the programmer to traverse the table in hash order without knowing what is in the actual table. 

 Note that it is up to the caller to ensure that the table structure does not change in the hash bucket that is currently being enumerated as this structure just tracks the next pointers in the bucket series.

<h3>typedef struct <b>ANTLR3_HASH_KEY_struct</b> <b>ANTLR3_HASH_KEY</b></h3>

<h3>typedef struct <b>ANTLR3_HASH_TABLE_struct</b></h3>

 
&nbsp;<wbr>&nbsp;<wbr><b>ANTLR3_HASH_TABLE</b>&quot; 

 Structure that tracks a hash table.

<h3>typedef struct <b>ANTLR3_INT_TRIE_struct</b></h3>

 
&nbsp;<wbr>&nbsp;<wbr><b>ANTLR3_INT_TRIE</b>&quot; 

 Structure that defines an ANTLR3_INT_TRIE. For this particular implementation, as you might expect, the key is turned into a 'string' by looking at bit(key, depth) of the integer key. Using 64 bit keys gives us a depth limit of 64 (or bit 0..63) and potentially a huge trie. This is the algorithm for a Patricia Trie. Note also that this trie [can] accept multiple entries for the same key and is therefore a kind of elastic bucket patricia trie. 

 If you find this code useful, please feel free to 'steal' it for any purpose as covered by the BSD license under which ANTLR is issued. You can cut the code but as the ANTLR library is only about 50K (Windows Vista), you might find it easier to just link the library. Please keep all comments and licenses and so on in any version of this you create of course. 

 Jim Idle.

<h3>typedef struct <b>ANTLR3_INT_TRIE_NODE_struct</b></h3>

 
&nbsp;<wbr>&nbsp;<wbr><b>ANTLR3_INT_TRIE_NODE</b>&quot; 

 Structure that defines an element/node in an ANTLR3_INT_TRIE.

<h3>typedef struct <b>ANTLR3_LIST_struct</b></h3>

 
&nbsp;<wbr>&nbsp;<wbr><b>ANTLR3_LIST</b>&quot; 

 Structure that represents a LIST collection.

<h3>typedef struct <b>ANTLR3_STACK_struct</b></h3>

 
&nbsp;<wbr>&nbsp;<wbr><b>ANTLR3_STACK</b>&quot; 

 Structure that represents a Stack collection.

<h3>typedef struct <b>ANTLR3_TOPO_struct</b></h3>

 
&nbsp;<wbr>&nbsp;<wbr><b>ANTLR3_TOPO</b>&quot; 

 A topological sort system that given a set of dependencies of a node m on node n, can sort them in dependency order. This is a generally useful utility object that does not care what the things are it is sorting. Generally the set to be sorted will be numeric indexes into some other structure such as an ANTLR3_VECTOR. I have provided a sort method that given ANTLR3_VECTOR as an input will sort the vector entries in place, as well as a sort method that just returns an array of the sorted noded indexes, in case you are not sorting ANTLR3_VECTORS but some set of your own device. 

 Of the two main algorithms that could be used, I chose to use the depth first search for unvisited nodes as a) This runs in linear time, and b) it is what we used in the ANTLR Tool to perform a topological sort of the input grammar files based on their dependencies.

<h3>typedef struct <b>ANTLR3_TRIE_ENTRY_struct</b></h3>

 
&nbsp;<wbr><b>ANTLR3_TRIE_ENTRY</b>&quot; 

 Structure that holds the payload entry in an ANTLR3_INT_TRIE or ANTLR3_STRING_TRIE.

<h3>typedef struct <b>ANTLR3_VECTOR_struct</b></h3>

 
&nbsp;<wbr>&nbsp;<wbr><b>ANTLR3_VECTOR</b>&quot;

<h3>typedef struct <b>ANTLR3_VECTOR_ELEMENT_struct</b></h3>

 
&nbsp;<wbr>&nbsp;<wbr><b>ANTLR3_VECTOR_ELEMENT</b>&quot;

<h3>typedef struct <b>ANTLR3_VECTOR_FACTORY_struct</b></h3>

 
&nbsp;<wbr><b>ANTLR3_VECTOR_FACTORY</b>&quot; 

 Structure that tracks vectors in a vector and auto deletes the vectors in the vector factory when closed.

<h3>typedef struct <b>ANTLR3_HASH_KEY_struct</b> * <b>pANTLR3_HASH_KEY</b></h3>

<h3>typedef struct <b>ANTLR3_INT_TRIE_NODE_struct</b> * <b>pANTLR3_INT_TRIE_NODE</b></h3>

<h3>typedef struct <b>ANTLR3_TRIE_ENTRY_struct</b> * <b>pANTLR3_TRIE_ENTRY</b></h3>

<h3>typedef struct <b>ANTLR3_VECTOR_ELEMENT_struct</b> * <b>pANTLR3_VECTOR_ELEMENT</b></h3>

<h2>Author</h2>

 

 Generated automatically by Doxygen for ANTLR3C from the source code. 

<h2>Index</h2>



<dt><a HREF="#lbBE">Author</a>
<dd></dl>
