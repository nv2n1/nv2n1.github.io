---
title: "elektra-keyset(3)"
name: "elektra-keyset"
section: "3"
letter: "e"
url: "/docs/linux/man/3-elektra-keyset/"
description: "KeySet :: Class Methods –"
---

<h2 class="name">NAME</h2>
<p> KeySet :: Class Methods &#8211; </p>
<p> Methods to manipulate KeySets.</p>
<h3>Functions</h3>
<p> KeySet * <code>ksNew</code> (size_t alloc,&#8230;) </p>
<p> KeySet * <code>ksDup</code> (const KeySet *source) </p>
<p> int <code>ksCopy</code> (KeySet *dest, const KeySet *source) </p>
<p> int <code>ksDel</code> (KeySet *ks) </p>
<p> void <code>ksSort</code> (KeySet *ks) </p>
<p> ssize_t <code>ksGetSize</code> (const KeySet *ks) </p>
<p> ssize_t <code>ksAppendKey</code> (KeySet *ks, Key *toAppend) </p>
<p> ssize_t <code>ksAppend</code> (KeySet *ks, const KeySet *toAppend) </p>
<p> Key * <code>ksPop</code> (KeySet *ks) </p>
<p> int <code>ksRewind</code> (KeySet *ks) </p>
<p> Key * <code>ksNext</code> (KeySet *ks) </p>
<p> Key * <code>ksCurrent</code> (const KeySet *ks) </p>
<p> Key * <code>ksHead</code> (const KeySet *ks) </p>
<p> Key * <code>ksTail</code> (const KeySet *ks) </p>
<p> cursor_t <code>ksGetCursor</code> (const KeySet *ks) </p>
<p> int <code>ksSetCursor</code> (KeySet *ks, cursor_t cursor) </p>
<p> Key * <code>ksLookup</code> (KeySet *ks, Key *key, option_t options) </p>
<p> Key * <code>ksLookupByName</code> (KeySet *ks, const char *name, option_t options) </p>
<h2>Detailed Description</h2>
<p> Methods to manipulate KeySets. </p>
<p> A KeySet is a unsorted set of keys. </p>
<p> Terminate with ksNew(0) or ksNew(20, &#8230;, KS_END) This is because there is a list of Key* required and KS_END has the length of (Key*). </p>
<p> It can be implemented in various ways like a linked list or with a dynamically allocated array. </p>
<p> With <code>ksNew()</code> you can create a new KeySet. </p>
<p> You can add keys with <code>ksAppendKey()</code> in the keyset. <code>ksGetSize()</code> tells you the current size of the keyset. </p>
<p> With <code>ksRewind()</code> and <code>ksNext()</code> you can navigate through the keyset. Don&#8217;t expect any particular order, but it is assured that you will get every key of the set. </p>
<p> KeySets have an <code>internal cursor </code>. This is used for <code>ksLookup()</code> and <code>kdbSet()</code>. </p>
<p> KeySet has a fundamental meaning inside elektra. It makes it possible to get and store many keys at once inside the database. In addition to that the class can be used as high level datastructure in applications. With <code>ksLookupByName()</code> it is possible to fetch easily specific keys out of the list of keys. </p>
<p> You can easily create and iterate keys: </p>
<pre><code>
#include &lt;kdb.h&gt;
// create a new keyset with 3 keys
// with a hint that about 20 keys will be inside
KeySet *myConfig = ksNew(20,
                         keyNew('user/name1', 0),
                         keyNew('user/name2', 0),
                         keyNew('user/name3', 0),
                         KS_END);
// append a key in the keyset
ksAppendKey(myConfig, keyNew('user/name4', 0));
Key *current;
ksRewind(myConfig);
while ((current = ksNext(myConfig)) != 0) {
        printf('Key name is %s., keyName (current));
}
ksDel(myConfig); // delete keyset and all keys appended
</code></pre>
<p>&nbsp;<wbr></p>
<h2>Function Documentation</h2>
<h3>ssize_t ksAppend (KeySet * ks, const KeySet * toAppend)Append all toAppend contained keys to the end of the ks.</h3>
<p> toAppend KeySet will be left unchanged. </p>
<p> Makes the keyset dirty, see <code>ksSort()</code>. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> the size of the KeySet after transfer </p>
<p> -1 on NULL pointers</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ks</i> the KeySet that will receive the keys<br />
 <i>toAppend</i> the KeySet that provides the keys that will be transfered</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ksAppendKey()</code>, ksInsert(), ksInsertKeys()</dl>
<h3>ssize_t ksAppendKey (KeySet * ks, Key * toAppend)Appends a Key to the end of ks.</h3>
<p> A pointer to the key will be stored, and not a private copy. So a future <code>ksDel()</code> on ks may <code>keyDel()</code> the toAppend object, see <code>keyGetRef()</code>. </p>
<p> The reference counter of the key will be incremented, and thus toAppend is not const. </p>
<p> The KeySet internal cursor is not moved. </p>
<p> Makes the keyset dirty, see <code>ksSort()</code>. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> the size of the KeySet after insertion </p>
<p> -1 on NULL pointers</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ks</i> KeySet that will receive the key<br />
 <i>toAppend</i> Key that will be appended to ks</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> ksInsert(), ksInsertKeys(), <code>ksAppend()</code>, <code>keyNew()</code>, <code>ksDel()</code> </p>
<p> <code>keyIncRef()</code></dl>
<h3>int ksCopy (KeySet * dest, const KeySet * source)Copy a keyset.</h3>
<p> Most often you may want a duplicate of a keyset, see <code>ksDup()</code> or append keys, see <code>ksAppend()</code>. But in some situations you need to copy a keyset to a existing keyset, for that this function exists. </p>
<p> You can also use it to clear a keyset when you pass a NULL pointer as source. </p>
<p> Note that all keys in dest will be deleted. Afterwards the content of the source will be added to the destination and the <code>ksCurrent()</code> is set properly in dest. </p>
<p> A flat copy is made, so the keys will not be duplicated, but there reference counter is updated, so both keysets need to be <code>ksDel()</code>. </p>
<p>int f(KeySet *ks)<br />
{<br />
    KeySet *c = ksNew(20, &#8230;, KS_END);<br />
    // c receives keys<br />
    ksCopy(ks, c); // pass the keyset to the caller<br />
    ksDel(c);<br />
} // caller needs to ksDel (ks)</p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>source</i> has to be an initialized source KeySet or NULL<br />
 <i>dest</i> has to be an initialized KeySet where to write the keys</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 1 on success </p>
<p> 0 if dest was cleared successfully (source is NULL) </p>
<p> -1 on NULL pointer</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ksNew()</code>, <code>ksDel()</code>, <code>ksDup()</code> </p>
<p> <code>keyCopy()</code> for copying keys</dl>
<h3>Key* ksCurrent (const KeySet * ks)Return the current Key.</h3>
<p> The pointer is NULL if you reached the end or after <code>ksRewind()</code>. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> You must not delete the key or change the key, use <code>ksPop()</code> if you want to delete it.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ks</i> the keyset object to work with</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> pointer to the Key pointed by ks&#8217;s cursor </p>
<p> 0 on NULL pointer</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ksNext()</code>, <code>ksRewind()</code> </p>
<p> kdbMonitorKeys() for a usage example</dl>
<h3>int ksDel (KeySet * ks)A destructor for KeySet objects.</h3>
<p> Cleans all internal dynamic attributes, decrement all reference pointers to all keys and then <code>keyDel()</code> all contained Keys, and free()s the release the KeySet object memory (that was previously allocated by <code>ksNew()</code>). </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ks</i> the keyset object to work with</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 when the keyset was freed </p>
<p> -1 on null pointer</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ksNew()</code></dl>
<h3>KeySet* ksDup (const KeySet * source)Return a duplicate of a keyset.</h3>
<p> Objects created with <code>ksDup()</code> must be destroyed with <code>ksDel()</code>. </p>
<p> Memory will be allocated as needed for dynamic properties, so you need to <code>ksDel()</code> the returned pointer. </p>
<p> A flat copy is made, so the keys will not be duplicated, but there reference counter is updated, so both keysets need <code>ksDel()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>source</i> has to be an initializised source KeySet</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> a flat copy of source on success </p>
<p> 0 on NULL pointer</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ksNew()</code>, <code>ksDel()</code> </p>
<p> <code>keyDup()</code> for <code>Key :: Basic Methods</code> duplication</dl>
<h3>cursor_t ksGetCursor (const KeySet * ks)Get the KeySet internal cursor.</h3>
<p> Use it to get the cursor of the actual position. </p>
<p> <code>Warning:</code></p>
<dl>
<dt>
<dd> Cursors are getting invalid when the key was <code>ksPop()</code>ed or <code>ksLookup()</code> with KDB_O_POP was used.</dl>
<h2>Read ahead</h2>
<p> With the cursors it is possible to read ahead in a keyset: </p>
<p>cursor_t jump;<br />
ksRewind(ks);<br />
while ((key = keyNext(ks)) != 0) {<br />
    // now mark this key<br />
    jump = ksGetCursor(ks);<br />
    // code..<br />
    keyNext(ks); // now browse on<br />
    // use ksCurrent(ks) to check the keys<br />
    // code..<br />
    // jump back to the position marked before<br />
    ksSetCursor(ks, jump);<br />
}</p>
<h2>Restoring state</h2>
<p> It can also be used to restore the state of a keyset in a function </p>
<p>int f(KeySet *ks)<br />
{<br />
    cursor_t state = ksGetCursor(ks);<br />
    // work with keyset<br />
    // now bring the keyset to the state before<br />
    ksSetCursor(ks, state);<br />
}</p>
<p> It is of course possible to make the KeySet const and cast its const away to set the cursor. Another way to achieve the same is to <code>ksDup()</code> the keyset, but it is not as efficient. </p>
<p> An invalid cursor will be returned directly after <code>ksRewind()</code>. When you set an invalid cursor <code>ksCurrent()</code> is 0 and <code>ksNext()</code> == <code>ksHead()</code>. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Only use a cursor for the same keyset which it was made for.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ks</i> the keyset object to work with</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> a valid cursor on success </p>
<p> an invalid cursor on NULL pointer or after <code>ksRewind()</code></dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ksNext()</code>, <code>ksSetCursor()</code></dl>
<h3>ssize_t ksGetSize (const KeySet * ks)Return the number of keys that ks contains.</h3>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ks</i> the keyset object to work with</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> the number of keys that ks contains. </p>
<p> -1 on NULL pointer</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> ksNew(0), <code>ksDel()</code></dl>
<h3>Key* ksHead (const KeySet * ks)Return the first key in the KeySet.</h3>
<p> The KeySets cursor will not be effected. </p>
<p> If <code>ksCurrent()</code>==ksHead() you know you are on the first key. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ks</i> the keyset object to work with</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> the first Key of a keyset </p>
<p> 0 on NULL pointer or empty keyset</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ksTail()</code> for the last <code>Key :: Basic Methods</code> </p>
<p> <code>ksRewind()</code>, <code>ksCurrent()</code> and <code>ksNext()</code> for iterating over the <code>KeySet :: Class Methods</code></dl>
<h3>Key* ksLookup (KeySet * ks, Key * key, option_t options)Look for a Key contained in ks that matches the name of the key.</h3>
<h2>Introduction</h2>
<p> <code>ksLookup()</code> is designed to let you work with entirely pre-loaded KeySets, so instead of <code>kdbGetKey()</code>, key by key, the idea is to fully <code>kdbGet()</code> for your application root key and process it all at once with <code>ksLookup()</code>. </p>
<p> This function is very efficient by using binary search. Together with <code>kdbGet()</code> which can you load the whole configuration with only some communication to backends you can write very effective but short code for configuration.</p>
<h2>Usage</h2>
<p> If found, ks internal cursor will be positioned in the matched key (also accessible by <code>ksCurrent()</code>), and a pointer to the Key is returned. If not found, ks internal cursor will not move, and a NULL pointer is returned. </p>
<p> Cascading is done if the first character is a /. This leads to ignoring the prefix like system/ and user/. </p>
<p>if (kdbGet(handle, &#8216;user/myapp&#8217;, myConfig, 0) == -1)<br />
    ErrorHandler(&#8216;Could not get Keys&#8217;);<br />
if (kdbGet(handle, &#8216;system/myapp&#8217;, myConfig, 0) == -1)<br />
    ErrorHandler(&#8216;Could not get Keys&#8217;);<br />
if ((myKey = ksLookup(myConfig, key, 0)) == NULL)<br />
    ErrorHandler(&#8216;Could not Lookup Key&#8217;);</p>
<p> This is the way multi user Programs should get there configuration and search after the values. It is guaranteed that more namespaces can be added easily and that all values can be set by admin and user.</p>
<h3>KDB_O_NOALL</h3>
<p> When KDB_O_NOALL is set the keyset will be only searched from <code>ksCurrent()</code> to <code>ksTail()</code>. You need to <code>ksRewind()</code> the keyset yourself. <code>ksCurrent()</code> is always set properly after searching a key, so you can go on searching another key after the found key. </p>
<p> When KDB_O_NOALL is not set the cursor will stay untouched and all keys are considered. A much more efficient binary search will be used then. </p>
<p> So if you change keys, e.g. rename (<code>keySetName()</code>) or remove (<code>keyRemove()</code>) them make sure to sort the keyset with <code>ksSort()</code>. When the keyset is dirty, see ksNeedSort() it will be sorted automatically when needed.</p>
<h3>KDB_O_POP</h3>
<p> When KDB_O_POP is set the key which was found will be <code>ksPop()</code>ed. <code>ksCurrent()</code> will not be changed, only iff <code>ksCurrent()</code> is the searched key, then the keyset will be <code>ksRewind()</code>ed. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Note that <code>keyRemove()</code> keys won&#8217;t be found after the first time the keyset is resorted. Lookup automatically sorts the keyset, if needed, but it can&#8217;t find it out when only keys are changed, not the keyset. </p>
<p> Like in <code>ksPop()</code> the popped key always needs to be <code>keyDel()</code> afterwards, even if it is appended to another keyset.</dl>
<p> <code>Warning:</code></p>
<dl>
<dt>
<dd> All cursors on the keyset will be invalid iff you use KDB_O_POP, so don&#8217;t use this if you rely on a cursor, see <code>ksGetCursor()</code>.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Never use <code>ksLookup()</code> with KDB_O_POP and <code>ksAppendKey()</code> or <code>ksAppend()</code> together in a loop. Otherwise <code>ksLookup()</code> will need to resort the keyset every iteration and spend 99.96% of the time in <code>ksSort()</code> (benchmarked with above 500k iterations).</dl>
<p> You can solve this problem by using KDB_O_NOALL, risking you have to iterate n^2 instead of n. </p>
<p> The more elegant way is to separate the keyset you use for <code>ksLookup()</code> and <code>ksAppendKey()</code>: </p>
<p>int f(KeySet *iterator, KeySet *lookup)<br />
{<br />
    KeySet *append = ksNew(ksGetSize(lookup), KS_END);<br />
    Key *key;<br />
    Key *current;<br />
    ksRewind(iterator);<br />
    while (current = ksNext(iterator)) {<br />
        key = ksLookup(lookup, current, KDB_O_POP);<br />
        // do something&#8230;<br />
        ksAppendKey(append, key); // now append it to append, not lookup!<br />
        keyDel(key);              // make sure to ALWAYS delete poped keys.<br />
    }<br />
    ksAppend(lookup, append);<br />
    // now lookup needs to be sorted only once, append never<br />
    ksDel(append);<br />
}</p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ks</i> where to look for<br />
 <i>key</i> the key object you are looking for<br />
 <i>options</i> some KDB_O_* option bits:</p>
<dl>
<dt>*</p>
<dd> KDB_O_NOCASE </p>
<p>&nbsp;<wbr>Lookup ignoring case.</p>
<dt>*</p>
<dd> KDB_O_WITHOWNER </p>
<p>&nbsp;<wbr>Also consider correct owner.</p>
<dt>*</p>
<dd> KDB_O_NOALL </p>
<p>&nbsp;<wbr>Only search from&nbsp;<wbr><code>ksCurrent()</code>&nbsp;<wbr>to end of keyset, see above text.</p>
<dt>*</p>
<dd> KDB_O_POP </p>
<p>&nbsp;<wbr>Pop the key which was found.</p>
<dt>*</p>
<dd> KDB_O_SORT </p>
<p>&nbsp;<wbr>Force sorting before searching, see&nbsp;<wbr><code>ksSort()</code>. Together with KDB_O_NOALL the search will start from beginning.&nbsp;<wbr></dl>
</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> pointer to the Key found, 0 otherwise </p>
<p> 0 on NULL pointers</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ksLookupByName()</code> to search by a name given by a string </p>
<p> <code>ksCurrent()</code>, <code>ksRewind()</code>, <code>ksNext()</code> for iterating over a <code>KeySet :: Class Methods</code> </p>
<p> <code>ksSort()</code> to understand how <code>KeySet :: Class Methods</code> sort themself</dl>
<h3>Key* ksLookupByName (KeySet * ks, const char * name, option_t options)Look for a Key contained in ks that matches name.</h3>
<p> <code>ksLookupByName()</code> is designed to let you work with entirely pre-loaded KeySets, so instead of <code>kdbGetKey()</code>, key by key, the idea is to fully <code>kdbGetByName()</code> for your application root key and process it all at once with <code>ksLookupByName()</code>. </p>
<p> This function is very efficient by using binary search. Together with <code>kdbGetByName()</code> which can you load the whole configuration with only some communication to backends you can write very effective but short code for configuration. </p>
<p> If found, ks internal cursor will be positioned in the matched key (also accessible by <code>ksCurrent()</code>), and a pointer to the Key is returned. If not found, ks internal cursor will not move, and a NULL pointer is returned.</p>
<h2>Cascading</h2>
<p> Cascading is done if the first character is a /. This leads to ignoring the prefix like system/ and user/. </p>
<p>if (kdbGetByName(handle, &#8216;/sw/myapp/current&#8217;, myConfig, 0) == -1)<br />
    ErrorHandler(&#8216;Could not get Keys&#8217;);<br />
if ((myKey = ksLookupByName(myConfig, &#8216;/myapp/current/key&#8217;, 0)) == NULL)<br />
    ErrorHandler(&#8216;Could not Lookup Key&#8217;);</p>
<p> This is the way multi user Programs should get there configuration and search after the values. It is guaranteed that more namespaces can be added easily and that all values can be set by admin and user.</p>
<h2>Full Search</h2>
<p> When KDB_O_NOALL is set the keyset will be only searched from <code>ksCurrent()</code> to <code>ksTail()</code>. You need to <code>ksRewind()</code> the keyset yourself. <code>ksCurrent()</code> is always set properly after searching a key, so you can go on searching another key after the found key. </p>
<p> When KDB_O_NOALL is not set the cursor will stay untouched and all keys are considered. A much more efficient binary search will be used then. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ks</i> where to look for<br />
 <i>name</i> key name you are looking for<br />
 <i>options</i> some KDB_O_* option bits:</p>
<dl>
<dt>*</p>
<dd> KDB_O_NOCASE </p>
<p>&nbsp;<wbr>Lookup ignoring case.</p>
<dt>*</p>
<dd> KDB_O_WITHOWNER </p>
<p>&nbsp;<wbr>Also consider correct owner.</p>
<dt>*</p>
<dd> KDB_O_NOALL </p>
<p>&nbsp;<wbr>Only search from&nbsp;<wbr><code>ksCurrent()</code>&nbsp;<wbr>to end of keyset, see above text.</p>
<dt>*</p>
<dd> KDB_O_POP </p>
<p>&nbsp;<wbr>Pop the key which was found.</p>
<dt>*</p>
<dd> KDB_O_SORT </p>
<p>&nbsp;<wbr>Force sorting before searching, see&nbsp;<wbr><code>ksSort()</code>. Together with KDB_O_NOALL the search will start from beginning.</dl>
</dl>
<p> Currently no options supported. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> pointer to the Key found, 0 otherwise </p>
<p> 0 on NULL pointers</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> keyCompare() for very powerfull Key lookups in KeySets </p>
<p> <code>ksCurrent()</code>, <code>ksRewind()</code>, <code>ksNext()</code></dl>
<h3>KeySet* ksNew (size_t alloc, &#8230;)Allocate, initialize and return a new KeySet object.</h3>
<p> Objects created with <code>ksNew()</code> must be destroyed with <code>ksDel()</code>. </p>
<p> You can use a various long list of parameters to preload the keyset with a list of keys. Either your first and only parameter is 0 or your last parameter must be KEY_END. </p>
<p> For most uses </p>
<p>KeySet *keys = ksNew(0);<br />
// work with it<br />
ksDel(keys);</p>
<p>&nbsp;<wbr>goes ok, the alloc size will be 16, defined in kdbprivate.h. The alloc size will be doubled whenever size reaches alloc size, so it also performs out large keysets. </p>
<p> But if you have any clue how large your keyset may be you should read the next statements. </p>
<p> If you want a keyset with length 15 (because you know of your application that you normally need about 12 up to 14 keys), use: </p>
<p>KeySet *keys = ksNew(15, KS_END);<br />
// work with it<br />
ksDel(keys);</p>
<p> If you start having 3 keys, and your application needs approximately 200-500 keys, you can use: </p>
<p>KeySet *config = ksNew(500,<br />
                       keyNew(&#8216;user/sw/app/fixedConfiguration/key1&#8217;, KEY_SWITCH_VALUE, &#8216;value1&#8217;, 0),<br />
                       keyNew(&#8216;user/sw/app/fixedConfiguration/key2&#8217;, KEY_SWITCH_VALUE, &#8216;value2&#8217;, 0),<br />
                       keyNew(&#8216;user/sw/app/fixedConfiguration/key3&#8217;, KEY_SWITCH_VALUE, &#8216;value3&#8217;, 0),<br />
                       KS_END); // don&#8217;t forget the KS_END at the end!<br />
// work with it<br />
ksDel(config);</p>
<p>&nbsp;<wbr>Alloc size is 500, the size of the keyset will be 3 after ksNew. This means the keyset will reallocate when appending more than 497 keys. </p>
<p> The main benefit of taking a list of variant length parameters is to be able to have one C-Statement for any possible KeySet. </p>
<p> Due to ABI compatibility, the KeySet structure is only declared in kdb.h, and not defined. So you can only declare pointers to KeySets in your program. See <a rel="nofollow" href="http://tldp.org/HOWTO/Program-Library-HOWTO/shared-libraries.html#AEN135">http://tldp.org/HOWTO/Program-Library-HOWTO/shared-libraries.html#AEN135</a> </p>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ksDel()</code> to free the <code>KeySet :: Class Methods</code> afterwards </p>
<p> <code>ksDup()</code> to duplicate an existing <code>KeySet :: Class Methods</code></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>alloc</i> gives a hint for the size how many Keys may be stored initially</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> a ready to use KeySet object </p>
<p> 0 on memory error</dl>
<h3>Key* ksNext (KeySet * ks)Returns the next Key in a KeySet.</h3>
<p> KeySets have an internal cursor that can be reset with <code>ksRewind()</code>. Every time <code>ksNext()</code> is called the cursor is incremented and the new current Key is returned. </p>
<p> You&#8217;ll get a NULL pointer if the key after the end of the KeySet was reached. It will set the cursor to the beginning of the KeySet and the next time the first key is returned. </p>
<p> The ks internal cursor will be changed, so it is not const. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> You must not delete or change the key, use <code>ksPop()</code> if you want to delete it.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ks</i> the keyset object to work with</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> the new current Key </p>
<p> 0 when the end is reached </p>
<p> 0 on NULL pointer</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ksRewind()</code>, <code>ksCurrent()</code></dl>
<h3>Key* ksPop (KeySet * ks)Remove and return the last key of ks.</h3>
<p> The reference counter will be decremented by one. </p>
<p> The KeySets cursor will not be effected if it did not point to the popped key. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> You need to <code>keyDel()</code> the key afterwards, if you don&#8217;t append it to another keyset. It has the same semantics like a key allocated with <code>keyNew()</code> or <code>keyDup()</code>.</dl>
<p>ks1 = ksNew(0);<br />
ks2 = ksNew(0);<br />
k1 = keyNew(0);       // ref counter 0<br />
ksAppendKey(ks1, k1); // ref counter 1<br />
ksAppendKey(ks2, k1); // ref counter 2<br />
k1 = ksPop(ks1);      // ref counter 1<br />
k1 = ksPop(ks2);      // ref counter 0, like after keyNew()<br />
ksAppendKey(ks1, k1); // ref counter 1<br />
ksDel(ks1);           // key is deleted too<br />
ksDel(ks2);<br />
*</p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> the last key of ks </p>
<p> NULL if ks is empty or on NULL pointer</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ks</i> KeySet to work with</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ksAppendKey()</code>, <code>ksAppend()</code> </p>
<p> commandList() for an example</dl>
<h3>int ksRewind (KeySet * ks)Rewinds the KeySet internal cursor.</h3>
<p> Use it to set the cursor to the beginning of the KeySet. <code>ksCurrent()</code> will then always return NULL afterwards. So you want to <code>ksNext()</code> first. </p>
<p>ksRewind(ks);<br />
while ((key = keyNext(ks)) != 0) {<br />
}</p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ks</i> the keyset object to work with</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success </p>
<p> -1 on NULL pointer</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ksNext()</code>, <code>ksCurrent()</code></dl>
<h3>int ksSetCursor (KeySet * ks, cursor_t cursor)Set the KeySet internal cursor.</h3>
<p> Use it to set the cursor to a stored position. <code>ksCurrent()</code> will then be the position which you got with. </p>
<p> <code>Warning:</code></p>
<dl>
<dt>
<dd> Cursors may get invalid when the key was <code>ksPop()</code>ed or <code>ksLookup()</code> was used together with KDB_O_POP.</dl>
<p>cursor_t cursor;<br />
// key now in any position here<br />
cursor = ksGetCursor(ks);<br />
while ((key = keyNext(ks)) != 0) {<br />
}<br />
ksSetCursor(ks, cursor); // reset state<br />
ksCurrent(ks);           // in same position as before</p>
<p> An invalid cursor will set the keyset to its beginning like <code>ksRewind()</code>. When you set an invalid cursor <code>ksCurrent()</code> is 0 and <code>ksNext()</code> == <code>ksHead()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>cursor</i> the cursor to use<br />
 <i>ks</i> the keyset object to work with</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 when the keyset is <code>ksRewind()</code>ed </p>
<p> 1 otherwise </p>
<p> -1 on NULL pointer</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ksNext()</code>, <code>ksGetCursor()</code></dl>
<h3>void ksSort (KeySet * ks)Sorts a KeySet alphabetically by Key name.</h3>
<p> You need <code>ksSort()</code> only in few cases directly.</p>
<h2>Don&#8217;t need to sort before using ksLookup</h2>
<p> You don&#8217;t need it if you just just <code>kdbGet()</code> and subsequent <code>ksLookup()</code>. </p>
<p>KeySet *ks = ksNew(0);<br />
kdbGet(h, ks, k, 0);<br />
// ksPop(), ksAppend() and ksAppendKey() allowed here<br />
ksLookup(ks, s, 0); // you dont need to sort ks</p>
<p> This is because the KeySet tracks if it needs to be sorted and <code>ksLookup()</code> will sort when needed.</p>
<h2>Sort when iterating</h2>
<p> Before you iterate over a keyset you have to sort it, if you need it in a sorted way. </p>
<p> To achieve that you can pass option_t::KDB_O_SORT to <code>kdbGet()</code> and <code>kdbSet()</code>. Then you will receive a already sorted keyset over which you can iterate. </p>
<pre><code>
KeySet *ks = ksNew(0);
kdbGet(h, ks, k, KDB_O_SORT);
// no changes to keyset allowed
ksRewind(ks);
// now you can iterate over a sorted keyset
</code></pre>
<p> Its of course also possible to use <code>ksLookup()</code> once, because it will sort the keyset too.</p>
<h2>Sort when changing key</h2>
<p> <code>Warning:</code></p>
<dl>
<dt>
<dd> You should not use <code>keySetName()</code> or <code>keyRemove()</code> when a key belongs to a keyset. When you are doing this, you always need to manually sort all keysets where the key was before using <code>ksLookup()</code> (otherwise <code>ksLookup()</code> won&#8217;t find that keys), <code>kdbGet()</code> or <code>kdbSet()</code> methods.</dl>
<p> When you change a key&#8217;s name or its remove status the order which was previously correctly is then wrong. The keyset does not recognize this, so the programmer has to take care that <code>ksSort()</code> is called before any operation which needs a sorted keyset (which are all <code>ksLookup()</code>, all <code>kdbGet()</code> and all <code>kdbSet()</code> functions). </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> You can remember that easily that all functions which get options require one of the following:</p>
<dl>
<dt>*</p>
<dd> that you did not manipulate a keys name or a remove status</p>
<dt>*</p>
<dd> that you pass KDB_O_SORT when you know that you manipulated at least one key</p>
<dt>*</p>
<dd> that you <code>ksSort()</code> yourself after manipulating keys</dl>
</dl>
<h2>Dirty KeySet</h2>
<p> When you use <code>ksAppend()</code>, <code>ksAppendKey()</code>, <code>ksPop()</code> the keyset is dirty afterwards, which means that it needs to be sorted. This is done automatically using a <code>ksLookup()</code> method and in ksGet() or ksSet() (All methods which accept options). </p>
<p> It won&#8217;t be done if you just iterate over the keyset, so you might use a <code>ksLookup()</code> or <code>ksSort()</code> first. <code>ksLookup()</code> will be more efficient in that case, because it will only sort when needed. Don&#8217;t pass KDB_O_NOALL (it will deactivate the sorting feature), see <code>ksLookup()</code> for more information. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ks</i> KeySet to be sorted</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>kdbGet()</code>, <code>kdbSet()</code>, <code>ksLookup()</code> for some functions which may need sorting before they are called. (All functions which take options as arguments) </p>
<p> <code>keySetName()</code>, <code>keySetBaseName()</code>, <code>keyAddBaseName()</code> and <code>keyRemove()</code> for all methods which change the sorting state where the <code>KeySet :: Class Methods</code> can&#8217;t track the change. </p>
<p> <code>ksAppend()</code>, <code>ksAppendKey()</code>, <code>ksPop()</code> for all methods which make a <code>KeySet :: Class Methods</code> dirty.</dl>
<h3>Key* ksTail (const KeySet * ks)Return the last key in the KeySet.</h3>
<p> The KeySets cursor will not be effected. </p>
<p> If <code>ksCurrent()</code>==ksTail() you know you are on the last key. <code>ksNext()</code> will return a NULL pointer afterwards. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ks</i> the keyset object to work with</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> the last Key of a keyset </p>
<p> 0 on NULL pointer or empty keyset</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ksHead()</code> for the first <code>Key :: Basic Methods</code> </p>
<p> <code>ksRewind()</code>, <code>ksCurrent()</code> and <code>ksNext()</code> for iterating over the <code>KeySet :: Class Methods</code></dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Elektra Projekt from the source code. </p>
<h2>Index</h2>
