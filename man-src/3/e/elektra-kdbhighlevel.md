---
title: "elektra-kdbhighlevel(3)"
name: "elektra-kdbhighlevel"
section: "3"
letter: "e"
url: "/docs/linux/man/3-elektra-kdbhighlevel/"
description: "KDB :: High Level methods –"
---

<h2 class="name">NAME</h2>
<p> KDB :: High Level methods &#8211; </p>
<p> High level methods to access the Key database.</p>
<h3>Functions</h3>
<p> int <code>kdbGetKey</code> (KDB *handle, Key *dest) </p>
<p> int <code>kdbSetKey</code> (KDB *handle, const Key *key) </p>
<p> int <code>kdbGetString</code> (KDB *handle, const char *keyname, char *returned, size_t maxSize) </p>
<p> int <code>kdbSetString</code> (KDB *handle, const char *keyname, const char *value) </p>
<p> int <code>kdbRemove</code> (KDB *handle, const char *keyname) </p>
<p> ssize_t <code>kdbGetByName</code> (KDB *handle, KeySet *returned, const char *name, option_t options) </p>
<h2>Detailed Description</h2>
<p> High level methods to access the Key database. </p>
<p> To use them: </p>
<pre><code>
#include &lt;kdb.h&gt;
</code></pre>
<p> These methods are higher level. They use <code>kdbOpen()</code>, <code>kdbClose()</code>, <code>kdbGet()</code> and <code>kdbSet()</code> methods to do their job, and don&#8217;t have to be reimplemented for a different backend. </p>
<p> These functions avoid limitations through not implemented capabilities. This will of course cost some effort, so read through the description carefully and decide if it is appropriate for your problem. </p>
<p> Binding writers don&#8217;t have to implement these functions, use features of the binding language instead. But you can use these functions as ideas what high level methods may be useful. </p>
<p> Don&#8217;t use writing single keys in a loop, prefer always writing out a keyset!</p>
<h2>Function Documentation</h2>
<h3>ssize_t kdbGetByName (KDB * handle, KeySet * returned, const char * name, option_t options)This method is similar <code>kdbGet()</code> but the path is given by a string.</h3>
<p> When it is not possible to make a key out of that string -1 is returned . </p>
<p> When parentName starts with / cascading will be used and both keys from user and system will be fetched. </p>
<p> A typically app with about 3000 keys may have this line: </p>
<p>KDB *handle = kdbOpen();<br />
KeySet *myConfig = (4096, KS_END);<br />
ssize_t ret = kdbGetByName(handle, myConfig, &#8216;/sw/app/current&#8217;, 0);<br />
// check ret and work with keyset myConfig<br />
ksDel(myConfig);<br />
kdbClose(handle);<br />
*</p>
<p> myConfig will be loaded with keys from system/sw/app/current but also user/sw/app/current. </p>
<p> When one of these <code>kdbGet()</code> fails -1 will be returned, but the other <code>kdbGet()</code> will be tried too. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> contains internal information of <code>opened </code> key database<br />
 <i>name</i> the name where to get the keys below<br />
 <i>returned</i> the (pre-initialized) KeySet returned with all keys found<br />
 <i>options</i> ORed options to control approaches Unlike to <code>kdbGet()</code> is KDB_O_POP set per default.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> number of keys contained by returned </p>
<p> -1 on failure </p>
<p> -1 when name is no valid key </p>
<p> -1 on NULL pointer</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>kdbGet()</code></dl>
<h3>int kdbGetKey (KDB * handle, Key * dest)Fully retrieves the passed key from the backend storage.</h3>
<p> The backend will try to get the key, identified through its name. </p>
<p> It uses <code>kdbGet()</code> for retrieving the key and copies the found data to dest. </p>
<p> While <code>kdbGetKey()</code> is perfect for a simple get of a specific key, <code>kdbGet()</code> and <code>kdbGetByName()</code> gives you more control over the keyset. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> contains internal information of <code>opened </code> key database<br />
 <i>dest</i> a pointer to a Key that has a name set</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success </p>
<p> -1 on failure </p>
<p> -1 on NULL pointer</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>kdbSetKey()</code> to set a single <code>Key :: Basic Methods</code> </p>
<p> commandGet() code in <code>KDB :: Low Level Methods</code> command for usage example </p>
<p> <code>kdbGet()</code> and <code>kdbGetByName()</code> to have more control over <code>KeySet :: Class Methods</code> and options</dl>
<h3>int kdbGetString (KDB * handle, const char * keyname, char * returned, size_t maxSize)A high-level method to get a key value, by key name.</h3>
<p> This method gets a backend from any backend with <code>kdbGetKey()</code> and extracts the string and store it into returned. It only works with string keys. </p>
<p> This method gives you the direct relation between a keyname and the value, without any kdb specific structures. Use it when you just want some values out of the kdb namespace. </p>
<p> You need to know the maximum string length of the object. That could be the case when you e.g. save a path which is limited with MAX_PATH. </p>
<pre><code>
KDB *handle = kdbOpen();
char buffer[MAX_PATH];
if (kdbGetString(handle, 'user/key/to/get/pathname', buffer, sizeof(buffer)) == -1) {
    // handle error cases
} else {
        printf ('The keys value is %s, buffer);
}
kdbClose(handle);
</code></pre>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> contains internal information of <code>opened </code> key database<br />
 <i>keyname</i> the name of the key to receive the value<br />
 <i>returned</i> a buffer to put the key value<br />
 <i>maxSize</i> the size of the buffer</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success </p>
<p> -1 on failure </p>
<p> -1 on NULL pointers </p>
<p> -1 if maxSize is 0 or larger than SSIZE_MAX</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>kdbSetString()</code> and <code>kdbRemove()</code> to set and remove a string </p>
<p> <code>kdbGetKey()</code>, keySetKey() to work with Keys </p>
<p> <code>kdbGet()</code> and <code>kdbGetByName()</code> for full access to <code>KDB Backends :: Internal Helper for Elektra</code> datastructures</dl>
<h3>int kdbRemove (KDB * handle, const char * keyname)Remove a key by its name from the backend storage.</h3>
<p> With <code>kdbSetString()</code> its only possible to set a key with an empty string. To really remove a key in a highlevel way you can use this method. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> contains internal information of <code>opened </code> key database<br />
 <i>keyname</i> the name of the key to be removed</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success </p>
<p> -1 on failure </p>
<p> -1 on NULL pointers</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> together with <code>kdbSetString()</code> and <code>kdbGetString()</code> a highlevel interface for <code>KDB :: Low Level Methods</code> </p>
<p> commandRemove() code in <code>KDB :: Low Level Methods</code> command for usage example</dl>
<h3>int kdbSetKey (KDB * handle, const Key * key)Sets key in the backend storage.</h3>
<p> While <code>kdbSetKey()</code> is perfect for a simple get of a specific key, <code>kdbGet()</code> and <code>kdbGetByName()</code> gives you more control over the keyset. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> contains internal information of <code>opened </code> key database<br />
 <i>key</i> Key to set</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success </p>
<p> -1 on failure </p>
<p> -1 on NULL pointer</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>kdbGetKey()</code> to get a single <code>Key :: Basic Methods</code> </p>
<p> <code>kdbSet()</code> for more control over <code>KeySet :: Class Methods</code> and options </p>
<p> commandSet() code in <code>KDB :: Low Level Methods</code> command for usage example</dl>
<h3>int kdbSetString (KDB * handle, const char * keyname, const char * value)A high-level method to set a value to a key, by key name.</h3>
<p> It will check if key exists first, and keep its metadata. So you&#8217;ll not loose the previous key comment. </p>
<p> This will set a text key. So if the key was previously a binary it will be retyped as string. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> contains internal information of <code>opened </code> key database<br />
 <i>keyname</i> the name of the key to receive the value<br />
 <i>value</i> the value to be set</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success </p>
<p> -1 on NULL pointers </p>
<p> -1 on failure</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>kdbGetString()</code>, <code>keySetString()</code>, <code>kdbSetKey()</code></dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Elektra Projekt from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAL">Author</a></p>
<dd></dl>
