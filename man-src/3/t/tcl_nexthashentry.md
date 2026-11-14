---
title: "tcl_nexthashentry(3)"
name: "tcl_nexthashentry"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_nexthashentry/"
description: "Tcl_InitHashTable, Tcl_InitCustomHashTable, Tcl_InitObjHashTable, Tcl_DeleteHashTable, Tcl_CreateHashEntry, Tcl_DeleteHashEntry, Tcl_FindHashEntry, Tcl_GetHashValue, Tcl_SetHashValue, Tcl_GetHashKe..."
---

<p>Tcl_InitHashTable, Tcl_InitCustomHashTable, Tcl_InitObjHashTable, Tcl_DeleteHashTable, Tcl_CreateHashEntry, Tcl_DeleteHashEntry, Tcl_FindHashEntry, Tcl_GetHashValue, Tcl_SetHashValue, Tcl_GetHashKey, Tcl_FirstHashEntry, Tcl_NextHashEntry, Tcl_HashStats &#8211; procedures to manage hash tables </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
<code>Tcl_InitHashTable</code>(<i>tablePtr, keyType</i>)
<code>Tcl_InitCustomHashTable</code>(<i>tablePtr, keyType, typePtr</i>)
<code>Tcl_InitObjHashTable</code>(<i>tablePtr</i>)
<code>Tcl_DeleteHashTable</code>(<i>tablePtr</i>)
Tcl_HashEntry *
<code>Tcl_CreateHashEntry</code>(<i>tablePtr, key, newPtr</i>)
<code>Tcl_DeleteHashEntry</code>(<i>entryPtr</i>)
Tcl_HashEntry *
<code>Tcl_FindHashEntry</code>(<i>tablePtr, key</i>)
ClientData
<code>Tcl_GetHashValue</code>(<i>entryPtr</i>)
<code>Tcl_SetHashValue</code>(<i>entryPtr, value</i>)
char *
<code>Tcl_GetHashKey</code>(<i>tablePtr, entryPtr</i>)
Tcl_HashEntry *
<code>Tcl_FirstHashEntry</code>(<i>tablePtr, searchPtr</i>)
Tcl_HashEntry *
<code>Tcl_NextHashEntry</code>(<i>searchPtr</i>)
char *
<code>Tcl_HashStats</code>(<i>tablePtr</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_HashTable <i>*tablePtr</i> (in) Address of hash table structure (for all procedures but <code>Tcl_InitHashTable</code>, this must have been initialized by previous call to <code>Tcl_InitHashTable</code>).</p>
<dd>int <i>keyType</i> (in) Kind of keys to use for new hash table. Must be either <code>TCL_STRING_KEYS</code>, <code>TCL_ONE_WORD_KEYS</code>, <code>TCL_CUSTOM_TYPE_KEYS</code>, <code>TCL_CUSTOM_PTR_KEYS</code>, or an integer value greater than 1.</p>
<dd>Tcl_HashKeyType <i>*typePtr</i> (in) Address of structure which defines the behaviour of the hash table.</p>
<dd>const char <i>*key</i> (in) Key to use for probe into table. Exact form depends on <i>keyType</i> used to create table.</p>
<dd>int <i>*newPtr</i> (out) The word at <i>*newPtr</i> is set to 1 if a new entry was created and 0 if there was already an entry for <i>key</i>.</p>
<dd>Tcl_HashEntry <i>*entryPtr</i> (in) Pointer to hash table entry.</p>
<dd>ClientData <i>value</i> (in) New value to assign to hash table entry. Need not have type ClientData, but must fit in same space as ClientData.</p>
<dd>Tcl_HashSearch <i>*searchPtr</i> (in) Pointer to record to use to keep track of progress in enumerating all the entries in a hash table.
</dl>
<h2>Description</h2>
<p>A hash table consists of zero or more entries, each consisting of a key and a value. Given the key for an entry, the hashing routines can very quickly locate the entry, and hence its value. There may be at most one entry in a hash table with a particular key, but many entries may have the same value. Keys can take one of four forms: strings, one-word values, integer arrays, or custom keys defined by a Tcl_HashKeyType structure (See section <code>THE TCL_HASHKEYTYPE STRUCTURE</code> below). All of the keys in a given table have the same form, which is specified when the table is initialized. </p>
<p> The value of a hash table entry can be anything that fits in the same space as a &#8220;char *&#8221; pointer. Values for hash table entries are managed entirely by clients, not by the hash module itself. Typically each entry&#8217;s value is a pointer to a data structure managed by client code. </p>
<p> Hash tables grow gracefully as the number of entries increases, so that there are always less than three entries per hash bucket, on average. This allows for fast lookups regardless of the number of entries in a table. </p>
<p> The core provides three functions for the initialization of hash tables, Tcl_InitHashTable, Tcl_InitObjHashTable and Tcl_InitCustomHashTable. </p>
<p> <code>Tcl_InitHashTable</code> initializes a structure that describes a new hash table. The space for the structure is provided by the caller, not by the hash module. The value of <i>keyType</i> indicates what kinds of keys will be used for all entries in the table. All of the key types described later are allowed, with the exception of <code>TCL_CUSTOM_TYPE_KEYS</code> and <code>TCL_CUSTOM_PTR_KEYS</code>. </p>
<p> <code>Tcl_InitObjHashTable</code> is a wrapper around <code>Tcl_InitCustomHashTable</code> and initializes a hash table whose keys are Tcl_Obj *. </p>
<p> <code>Tcl_InitCustomHashTable</code> initializes a structure that describes a new hash table. The space for the structure is provided by the caller, not by the hash module. The value of <i>keyType</i> indicates what kinds of keys will be used for all entries in the table. <i>KeyType</i> must have one of the following values:</p>
<dl COMPACT>
<dt><code>TCL_STRING_KEYS</code></p>
<dd>Keys are null-terminated strings. They are passed to hashing routines using the address of the first character of the string.</p>
<dt><code>TCL_ONE_WORD_KEYS</code></p>
<dd>Keys are single-word values; they are passed to hashing routines and stored in hash table entries as &#8220;char *&#8221; values. The pointer value is the key; it need not (and usually does not) actually point to a string.</p>
<dt><code>TCL_CUSTOM_TYPE_KEYS</code></p>
<dd>Keys are of arbitrary type, and are stored in the entry. Hashing and comparison is determined by <i>typePtr</i>. The Tcl_HashKeyType structure is described in the section <code>THE TCL_HASHKEYTYPE STRUCTURE</code> below.</p>
<dt><code>TCL_CUSTOM_PTR_KEYS</code></p>
<dd>Keys are pointers to an arbitrary type, and are stored in the entry. Hashing and comparison is determined by <i>typePtr</i>. The Tcl_HashKeyType structure is described in the section <code>THE TCL_HASHKEYTYPE STRUCTURE</code> below.</p>
<dt><i>other</i></p>
<dd>If <i>keyType</i> is not one of the above, then it must be an integer value greater than 1. In this case the keys will be arrays of &#8220;int&#8221; values, where <i>keyType</i> gives the number of ints in each key. This allows structures to be used as keys. All keys must have the same size. Array keys are passed into hashing functions using the address of the first int in the array.</dl>
<p> <code>Tcl_DeleteHashTable</code> deletes all of the entries in a hash table and frees up the memory associated with the table&#8217;s bucket array and entries. It does not free the actual table structure (pointed to by <i>tablePtr</i>), since that memory is assumed to be managed by the client. <code>Tcl_DeleteHashTable</code> also does not free or otherwise manipulate the values of the hash table entries. If the entry values point to dynamically-allocated memory, then it is the client&#8217;s responsibility to free these structures before deleting the table. </p>
<p> <code>Tcl_CreateHashEntry</code> locates the entry corresponding to a particular key, creating a new entry in the table if there was not already one with the given key. If an entry already existed with the given key then <i>*newPtr</i> is set to zero. If a new entry was created, then <i>*newPtr</i> is set to a non-zero value and the value of the new entry will be set to zero. The return value from <code>Tcl_CreateHashEntry</code> is a pointer to the entry, which may be used to retrieve and modify the entry&#8217;s value or to delete the entry from the table. </p>
<p> <code>Tcl_DeleteHashEntry</code> will remove an existing entry from a table. The memory associated with the entry itself will be freed, but the client is responsible for any cleanup associated with the entry&#8217;s value, such as freeing a structure that it points to. </p>
<p> <code>Tcl_FindHashEntry</code> is similar to <code>Tcl_CreateHashEntry</code> except that it does not create a new entry if the key doesn&#8217;t exist; instead, it returns NULL as result. </p>
<p> <code>Tcl_GetHashValue</code> and <code>Tcl_SetHashValue</code> are used to read and write an entry&#8217;s value, respectively. Values are stored and retrieved as type &#8220;ClientData&#8221;, which is large enough to hold a pointer value. On almost all machines this is large enough to hold an integer value too. </p>
<p> <code>Tcl_GetHashKey</code> returns the key for a given hash table entry, either as a pointer to a string, a one-word (&#8220;char *&#8221;) key, or as a pointer to the first word of an array of integers, depending on the <i>keyType</i> used to create a hash table. In all cases <code>Tcl_GetHashKey</code> returns a result with type &#8220;char *&#8221;. When the key is a string or array, the result of <code>Tcl_GetHashKey</code> points to information in the table entry; this information will remain valid until the entry is deleted or its table is deleted. </p>
<p> <code>Tcl_FirstHashEntry</code> and <code>Tcl_NextHashEntry</code> may be used to scan all of the entries in a hash table. A structure of type &#8220;Tcl_HashSearch&#8221;, provided by the client, is used to keep track of progress through the table. <code>Tcl_FirstHashEntry</code> initializes the search record and returns the first entry in the table (or NULL if the table is empty). Each subsequent call to <code>Tcl_NextHashEntry</code> returns the next entry in the table or NULL if the end of the table has been reached. A call to <code>Tcl_FirstHashEntry</code> followed by calls to <code>Tcl_NextHashEntry</code> will return each of the entries in the table exactly once, in an arbitrary order. It is inadvisable to modify the structure of the table, e.g. by creating or deleting entries, while the search is in progress, with the exception of deleting the entry returned by <code>Tcl_FirstHashEntry</code> or <code>Tcl_NextHashEntry</code>. </p>
<p> <code>Tcl_HashStats</code> returns a dynamically-allocated string with overall information about a hash table, such as the number of entries it contains, the number of buckets in its hash array, and the utilization of the buckets. It is the caller&#8217;s responsibility to free the result string by passing it to <code>ckfree</code>. </p>
<p> The header file <code>tcl.h</code> defines the actual data structures used to implement hash tables. This is necessary so that clients can allocate Tcl_HashTable structures and so that macros can be used to read and write the values of entries. However, users of the hashing routines should never refer directly to any of the fields of any of the hash-related data structures; use the procedures and macros defined here.</p>
<h2>The Tcl_Hashkeytype Structure</h2>
<p>Extension writers can define new hash key types by defining four procedures, initializing a <code>Tcl_HashKeyType</code> structure to describe the type, and calling <code>Tcl_InitCustomHashTable</code>. The <code>Tcl_HashKeyType</code> structure is defined as follows:</p>
<dl COMPACT>
<dd>
<pre>typedef struct Tcl_HashKeyType {
 int <i>version</i>;
 int <i>flags</i>;
 Tcl_HashKeyProc *<i>hashKeyProc</i>;
 Tcl_CompareHashKeysProc *<i>compareKeysProc</i>;
 Tcl_AllocHashEntryProc *<i>allocEntryProc</i>;
 Tcl_FreeHashEntryProc *<i>freeEntryProc</i>;
} Tcl_HashKeyType;</pre>
</dl>
<p> The <i>version</i> member is the version of the table. If this structure is extended in future then the version can be used to distinguish between different structures. It should be set to <code>TCL_HASH_KEY_TYPE_VERSION</code>. </p>
<p> The <i>flags</i> member is 0 or one or more of the following values OR&#8217;ed together:</p>
<dl COMPACT>
<dt><code>TCL_HASH_KEY_RANDOMIZE_HASH</code></p>
<dd>There are some things, pointers for example which do not hash well because they do not use the lower bits. If this flag is set then the hash table will attempt to rectify this by randomizing the bits and then using the upper N bits as the index into the table.</p>
<dt><code>TCL_HASH_KEY_SYSTEM_HASH</code></p>
<dd>This flag forces Tcl to use the memory allocation procedures provided by the operating system when allocating and freeing memory used to store the hash table data structures, and not any of Tcl&#8217;s own customized memory allocation routines. This is important if the hash table is to be used in the implementation of a custom set of allocation routines, or something that a custom set of allocation routines might depend on, in order to avoid any circular dependency.</dl>
<p> The <i>hashKeyProc</i> member contains the address of a function called to calculate a hash value for the key.</p>
<dl COMPACT>
<dd>
<pre>typedef unsigned int (Tcl_HashKeyProc) (
 Tcl_HashTable *<i>tablePtr</i>,
 void *<i>keyPtr</i>);</pre>
</dl>
<p> If this is NULL then <i>keyPtr</i> is used and <code>TCL_HASH_KEY_RANDOMIZE_HASH</code> is assumed. </p>
<p> The <i>compareKeysProc</i> member contains the address of a function called to compare two keys.</p>
<dl COMPACT>
<dd>
<pre>typedef int (Tcl_CompareHashKeysProc) (
 void *<i>keyPtr</i>,
 Tcl_HashEntry *<i>hPtr</i>);</pre>
</dl>
<p> If this is NULL then the <i>keyPtr</i> pointers are compared. If the keys do not match then the function returns 0, otherwise it returns 1. </p>
<p> The <i>allocEntryProc</i> member contains the address of a function called to allocate space for an entry and initialize the key and clientData.</p>
<dl COMPACT>
<dd>
<pre>typedef Tcl_HashEntry *(Tcl_AllocHashEntryProc) (
 Tcl_HashTable *<i>tablePtr</i>,
 void *<i>keyPtr</i>);</pre>
</dl>
<p> If this is NULL then Tcl_Alloc is used to allocate enough space for a Tcl_HashEntry, the key pointer is assigned to key.oneWordValue and the clientData is set to NULL. String keys and array keys use this function to allocate enough space for the entry and the key in one block, rather than doing it in two blocks. This saves space for a pointer to the key from the entry and another memory allocation. Tcl_Obj* keys use this function to allocate enough space for an entry and increment the reference count on the object. </p>
<p> The <i>freeEntryProc</i> member contains the address of a function called to free space for an entry.</p>
<dl COMPACT>
<dd>
<pre>typedef void (Tcl_FreeHashEntryProc) (Tcl_HashEntry *<i>hPtr</i>);</pre>
</dl>
<p> If this is NULL then Tcl_Free is used to free the space for the entry. Tcl_Obj* keys use this function to decrement the reference count on the object.</p>
<h2>Keywords</h2>
<p>hash table, key, lookup, search, value</p>
