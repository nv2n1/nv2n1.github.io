---
title: "elektra-kdb(3)"
name: "elektra-kdb"
section: "3"
letter: "e"
url: "/docs/linux/man/3-elektra-kdb/"
description: "KDB :: Low Level Methods –"
---

<h2 class="name">NAME</h2>
<p> KDB :: Low Level Methods &#8211; </p>
<p> General methods to access the Key database.</p>
<h3>Functions</h3>
<p> int <code>kdbMount</code> (KDB *handle, const Key *mountpoint, const KeySet *config) </p>
<p> int <code>kdbUnmount</code> (KDB *handle, const Key *mountpoint) </p>
<p> Key * <code>kdbGetMountpoint</code> (KDB *handle, const Key *where) </p>
<p> KDB * <code>kdbOpen</code> () </p>
<p> int <code>kdbClose</code> (KDB *handle) </p>
<p> ssize_t <code>kdbGet</code> (KDB *handle, KeySet *returned, Key *parentKey, option_t options) </p>
<p> ssize_t <code>kdbSet</code> (KDB *handle, KeySet *ks, Key *parentKey, option_t options) </p>
<h2>Detailed Description</h2>
<p> General methods to access the Key database. </p>
<p> To use them: </p>
<pre><code>
#include &lt;kdb.h&gt;
</code></pre>
<p> The kdb*() class of methods are used to access the storage, to get and set <code>Keys </code> or <code>KeySets </code>. </p>
<p> The most important functions are:</p>
<dl>
<dt>*</p>
<dd> <code>kdbOpen()</code></p>
<dt>*</p>
<dd> <code>kdbClose()</code></p>
<dt>*</p>
<dd> <code>kdbGet()</code></p>
<dt>*</p>
<dd> <code>kdbSet()</code></dl>
<p> The two essential functions for dynamic information about backends are:</p>
<dl>
<dt>*</p>
<dd> <code>kdbGetMountpoint()</code></p>
<dt>*</p>
<dd> kdbGetCapability()</dl>
<p> They use some backend implementation to know the details about how to access the storage. Currently we have this backends:</p>
<dl>
<dt>*</p>
<dd> berkeleydb: the keys are stored in a Berkeley DB database, providing very small footprint, speed, and other advantages.</p>
<dt>*</p>
<dd> filesys: the key hierarchy and data are saved as plain text files in the filesystem.</p>
<dt>*</p>
<dd> ini: the key hierarchy are saved into configuration files.</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.libelektra.org/Ini">http://www.libelektra.org/Ini</a></dl>
<dl>
<dt>*</p>
<dd> fstab: a reference backend used to interpret the /etc/fstab file as a set of keys under system/filesystems .</p>
<dt>*</p>
<dd> gconf: makes Elektra use the GConf daemon to access keys. Only the user/ tree is available since GConf is not system wide.</dl>
<p> Backends are physically a library named /lib/libelektra-{NAME}.so. </p>
<p> See <code>writing a new backend </code> for information about how to write a backend. </p>
<p> Language binding writers should follow the same rules:</p>
<dl>
<dt>*</p>
<dd> You must relay completely on the backend-dependent methods.</p>
<dt>*</p>
<dd> You may use or reimplement the second set of methods.</p>
<dt>*</p>
<dd> You should completely reimplement in your language the higher lever methods.</p>
<dt>*</p>
<dd> Many methods are just for comfort in C. These methods are marked and need not to be implemented if the binding language has e.g. string operators which can do the operation easily.</dl>
<h2>Function Documentation</h2>
<h3>int kdbClose (KDB * handle)Closes the session with the Key database.</h3>
<p> You should call this method when you finished your affairs with the key database. You can manipulate Key and KeySet objects also after <code>kdbClose()</code>. You must not use any kdb* call afterwards. You can implement <code>kdbClose()</code> in the atexit() handler. </p>
<p> This is the counterpart of <code>kdbOpen()</code>. </p>
<p> The handle parameter will be finalized and all resources associated to it will be freed. After a <code>kdbClose()</code>, this handle can&#8217;t be used anymore, unless it gets initialized again with another call to <code>kdbOpen()</code>. </p>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>kdbOpen()</code></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> contains internal information of <code>opened </code> key database</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success </p>
<p> -1 on NULL pointer</dl>
<h3>ssize_t kdbGet (KDB * handle, KeySet * returned, Key * parentKey, option_t options)Retrieve keys in an atomic and universal way, all other kdbGet Functions rely on that one.</h3>
<p> The returned KeySet must be initialized or may already contain some keys. The new retrieved keys will be appended using <code>ksAppendKey()</code>. </p>
<p> In default behaviour (options = 0) it will fully retrieve all keys under the parentKey folder, with all subfolders and their children but not inactive keys or folders. </p>
<p> The keyset will not be sorted at first place, but will be marked dirty and sorted afterwards when needed. That could be a subsequent <code>ksLookup()</code>, <code>ksLookupByName()</code> or <code>kdbSet()</code>. See <code>ksSort()</code> on that issue. </p>
<p> The behaviour can be fine-tuned with options in various ways to make <code>kdbGet()</code> more comfortable.</p>
<h2>Options</h2>
<p> The option is an array of the following ORed flags: </p>
<dl>
<dt>*</p>
<dd> option_t::KDB_O_DEL </p>
<p>&nbsp;<wbr>Its often useful to&nbsp;<wbr><code>keyDel()</code>&nbsp;<wbr>the parentKey in the line after&nbsp;<wbr><code>kdbGet()</code>. Using this flag, you can just pass a key allocated with&nbsp;<wbr><code>keyNew()</code>,&nbsp;<wbr><code>kdbGet()</code>&nbsp;<wbr>will free it for you in the end.</p>
<dt>*</p>
<dd> option_t::KDB_O_POP </p>
<p>&nbsp;<wbr>The parentKey itself will always be added to returned. If you only want the children of the parentKey in returned, but not the parentKey itself, use this flag. This is only valid for the first parentKey, the one you passed. The other recursive parentKeys will stay in the keyset. To get only the leaves of the tree, without any parentKey, see&nbsp;<wbr><code>option_t::KDB_O_NODIR</code>&nbsp;<wbr>below.</p>
<dt>*</p>
<dd> option_t::KDB_O_NODIR </p>
<p>&nbsp;<wbr>Don&#8217;t include folders in the returned KeySet, so only keys without subkeys. You can picture it best that you only get the leaves of the tree of keys.</p>
<dt>*</p>
<dd> option_t::KDB_O_DIRONLY </p>
<p>&nbsp;<wbr>Put in returned only the folder keys. The resulting KeySet will be only the skeleton of the tree. This option must not be ORed together with KDB_O_DIR.</p>
<dt>*</p>
<dd> option_t::KDB_O_NOSTAT </p>
<p>&nbsp;<wbr>Don&#8217;t stat they keys, whatever&nbsp;<wbr><code>keyNeedStat()</code>&nbsp;<wbr>says. That means that also the key value and comment will be retrieved. The flag will result in that all keys in returned don&#8217;t have&nbsp;<wbr><code>keyNeedStat()</code>&nbsp;<wbr>set.</p>
<dt>*</p>
<dd> option_t::KDB_O_STATONLY </p>
<p>&nbsp;<wbr>Only stat the keys. It means that key value and comment will not be retrieved. The resulting keys will contain only meta info such as user and group IDs, owner, mode permissions and modification times. You don&#8217;t need that flag if the keys already have&nbsp;<wbr><code>keyNeedStat()</code>&nbsp;<wbr>set. The flag will result in that all keys in returned have&nbsp;<wbr><code>keyNeedStat()</code>&nbsp;<wbr>set.</p>
<dt>*</p>
<dd> option_t::KDB_O_INACTIVE </p>
<p>&nbsp;<wbr>Will make it not ignore inactive keys, so returned will contain also inactive keys. Inactive keys are those that have names begining with&nbsp;<wbr>&#8216;.&#8217;&nbsp;<wbr>(dot). Please be sure that you know what you are doing, inactive keys must not have any semantics to the application. This flag should only be set in key browsers after explicit user request. You might also get inactive keys when you plan to remove a whole hierarchy.</p>
<dt>*</p>
<dd> option_t::KDB_O_SORT </p>
<p>&nbsp;<wbr>Force returned to be&nbsp;<wbr><code>ksSort()</code>ed. Normally you don&#8217;t want that the returned is sorted immediately because you might add other keys or go for another&nbsp;<wbr><code>kdbGet()</code>. Sorting will take place automatically when needed by&nbsp;<wbr><code>ksLookup()</code>&nbsp;<wbr>or&nbsp;<wbr><code>kdbSet()</code>, also without this option set. But you need to sort the keyset for yourself, when you just iterate over it. If you want to do that, pass this flag at the last&nbsp;<wbr><code>kdbGet()</code>.</p>
<dt>*</p>
<dd> option_t::KDB_O_NORECURSIVE </p>
<p>&nbsp;<wbr>Dont get the keys recursive. Only receive keys from one folder. This might not work if the backend does not support it. Be prepared for more keys and use&nbsp;<wbr><code>ksLookup()</code>&nbsp;<wbr>and avoid static assumptions on how many keys you get.</dl>
<p> <code>Example:</code>.RS 4 </p>
<p>KDB *handle;<br />
KeySet *myConfig;<br />
Key *key;<br />
myConfig = ksNew(0);<br />
handle = kdbOpen();<br />
key = keyNew(&#8216;system/sw/MyApp&#8217;, KEY_END);<br />
rc = kdbGet(handle, key, myConfig, 0);<br />
keyDel(key);<br />
key = keyNew(&#8216;user/sw/MyApp&#8217;, KEY_END);<br />
rc = kdbGet(handle, key, myConfig, 0);<br />
keyDel(key);<br />
// will sort keyset here<br />
key = ksLookupByName(myConfig, &#8216;/sw/MyApp/key&#8217;, 0);<br />
// check if key is not 0 and work with it&#8230;<br />
ksDel(myConfig); // delete the in-memory configuration<br />
// maybe you want kdbSet() myConfig here<br />
kdbClose(handle); // no more affairs with the key database.</p>
<h2>Details</h2>
<p> When no backend could be found (e.g. no backend mounted) the default backend will be used. </p>
<p> If you pass a NULL pointer as handle and/or returned <code>kdbGet()</code> will return -1 and do nothing but <code>keyDel()</code> the parentKey when requested and not a NULL pointer. </p>
<p> If you pass NULL as parentKey the root keys of all namespaces will be appended to returned. </p>
<p> For every directory key (<code>keyIsDir()</code>) the appropriate backend will be chosen and keys in it will be requested. </p>
<p> If any backend reports an failure the recursive getting of keys will be stopped. Backends only report failure when they are not able to get keys for any problems. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> contains internal information of <code>opened </code> key database<br />
 <i>parentKey</i> parent key or NULL to get the root keys<br />
 <i>returned</i> the (pre-initialized) KeySet returned with all keys found<br />
 <i>options</i> ORed options to control approaches</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> option_t </p>
<p> <code>kdb higher level Methods </code> that rely on <code>kdbGet()</code> </p>
<p> <code>ksLookupByName()</code>, ksLookupByString() for powerful lookups after the KeySet was retrieved </p>
<p> commandList() code in <code>KDB :: Low Level Methods</code> command for usage example </p>
<p> commandEdit() code in <code>KDB :: Low Level Methods</code> command for usage example </p>
<p> commandExport() code in <code>KDB :: Low Level Methods</code> command for usage example</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> number of keys contained by returned </p>
<p> -1 on failure</dl>
<h3>Key* kdbGetMountpoint (KDB * handle, const Key * where)Lookup a mountpoint in a handle for a specific key.</h3>
<p> Will return a key representing the mountpoint or null if there is no appropriate mountpoint e.g. its the root mountpoint. </p>
<p> Together with kdbGetCapability() the two essential informations about mounted backends. </p>
<p> <code>Example:</code>.RS 4 </p>
<p>Key *key = keyNew(&#8216;system/template&#8217;);<br />
KDB *handle = kdbOpen();<br />
Key *mountpoint = 0;<br />
mountpoint = kdbGetMountpoint(handle, key);<br />
printf(&#8216;The library I am using is %s mounted in %s, keyValue(mountpoint),<br />
       keyName(mountpoint));<br />
kdbClose(handle);<br />
keyDel(key);</p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> is the data structure, where the mounted directories are saved.<br />
 <i>where</i> the key, that should be looked up.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> the mountpoint associated with the key</dl>
<h3>int kdbMount (KDB * handle, const Key * mountpoint, const KeySet * config)Dynamically mount a single backend.</h3>
<p> Maps the mountpoint, defined through its name and value, into the global elektra hierachy. If successfull, under the mountpoint another backend will reside. </p>
<p> This only works for a single KDB, that means a single thread in a single process. You may want statically mounting by editing system/elektra/mountpoints. </p>
<p> If you allocated mountpoint and config first, make sure that you free it! It is ok to free it immediately afterwards. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> handle to the kdb data structure<br />
 <i>mountpoint</i> the <code>keyName()</code> of this key is the mountpoint, <code>keyValue()</code> the backend<br />
 <i>config</i> the configuration passed for that backend</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success, -1 if an error occurred</dl>
<h3>KDB* kdbOpen (void)Opens the session with the Key database.</h3>
<p> The first step is to open the default backend. With it system/elektra/mountpoints will be loaded and all needed libraries and mountpoints will be determined. These libraries for backends will be loaded and with it the KDB datastructure will be initialized. </p>
<p> You must always call this method before retrieving or commiting any keys to the database. In the end of the program, after using the key database, you must not forget to <code>kdbClose()</code>. You can use the atexit () handler for it. </p>
<p> The pointer to the KDB structure returned will be initialized like described above, and it must be passed along on any kdb*() method your application calls. </p>
<p> Get a KDB handle for every thread using elektra. Don&#8217;t share the handle across threads, and also not the pointer accessing it: </p>
<p>thread1<br />
{<br />
    KDB *h;<br />
    h = kdbOpen();<br />
    // fetch keys and work with them<br />
    kdbClose(h);<br />
}<br />
thread2<br />
{<br />
    KDB *h;<br />
    h = kdbOpen();<br />
    // fetch keys and work with them<br />
    kdbClose(h);<br />
}</p>
<p> You don&#8217;t need to use the <code>kdbOpen()</code> if you only want to manipulate plain in-memory Key or KeySet objects without any affairs with the backend key database, </p>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>kdbClose()</code> to end all affairs to the <code>Key :: Basic Methods</code> database.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> a KDB pointer on success </p>
<p> NULL on failure</dl>
<h3>ssize_t kdbSet (KDB * handle, KeySet * ks, Key * parentKey, option_t options)Set keys in an atomic and universal way, all other kdbSet Functions rely on that one.</h3>
<p> The given handle and keyset are the objects to work with. </p>
<p> With parentKey you can only store a part of the given keyset. Otherwise pass a null pointer or a parentKey without a name. </p>
<p>KeySet *ks = ksNew(0);<br />
kdbGet(h, ks, keyNew(&#8216;system/myapp&#8217;, 0), KDB_O_DEL);<br />
kdbGet(h, ks, keyNew(&#8216;user/myapp&#8217;, 0), KDB_O_DEL);<br />
// now only set everything below user, because you can&#8217;t write to system<br />
kdbSet(h, ks, keyNew(&#8216;user/myapp&#8217;, 0), KDB_O_DEL);<br />
ksDel(ks);</p>
<p> Each key is checked with <code>keyNeedSync()</code> before being actually committed. So only changed keys are updated. If no key of a backend needs to be synced the <code>kdbSet_backend()</code> will be omitted. </p>
<p> If some error occurs, <code>kdbSet()</code> will stop. In this situation the KeySet internal cursor will be set on the key that generated the error. This specific key and all behind it were not set. To be failsafe jump over it and try to set the rest, but report the error to the user. </p>
<p> <code>Example of how this method can be used:</code>.RS 4 </p>
<pre><code>
int i;
KeySet *ks; // the KeySet I want to set
// fill ks with some keys
for (i = 0; i &lt; 10; i++) // limit to 10 tries
{
    ret = kdbSet(handle, ks, 0, 0);
    if (ret == -1) {
        // We got an error. Warn user.
        Key *problem;
        problem = ksCurrent(ks);
        if (problem) {
            char keyname[300] ='';
            keyGetFullName(problem, keyname, sizeof(keyname));
            fprintf(stderr, 'kdb import: while importing %s', keyname);
        } else
            break;
        // And try to set keys again starting from the next key,
        // unless we reached the end of KeySet
        if (ksNext(ks) == 0)
            break;
    }
}
</code></pre>
<h2>Options</h2>
<p> There are some options changing the behaviour of <code>kdbSet()</code>: </p>
<dl>
<dt>*</p>
<dd> option_t::KDB_O_DEL </p>
<p>&nbsp;<wbr>Its often useful to&nbsp;<wbr><code>keyDel()</code>&nbsp;<wbr>the parentKey in the line after&nbsp;<wbr><code>kdbGet()</code>. Using this flag, you can just pass a key allocated with&nbsp;<wbr><code>keyNew()</code>,&nbsp;<wbr><code>kdbGet()</code>&nbsp;<wbr>will free it for you in the end.</p>
<dt>*</p>
<dd> option_t::KDB_O_SYNC </p>
<p>&nbsp;<wbr>Will force to save all keys, independent of their sync state.</p>
<dt>*</p>
<dd> option_t::KDB_O_NOREMOVE </p>
<p>&nbsp;<wbr>Don&#8217;t remove any key from disk, even if&nbsp;<wbr><code>keyRemove()</code>&nbsp;<wbr>was set. With that flag removing keys can&#8217;t happen unintentional. The flag will result in that all keys in returned don&#8217;t have&nbsp;<wbr><code>keyNeedRemove()</code>&nbsp;<wbr>set.</p>
<dt>*</p>
<dd> option_t::KDB_O_REMOVEONLY </p>
<p>&nbsp;<wbr>Remove all keys instead of setting them. All keys in returned will have&nbsp;<wbr><code>keyNeedRemove()</code>&nbsp;<wbr>set, but not&nbsp;<wbr><code>keyNeedStat()</code>&nbsp;<wbr>saying to you that the key was deleted permanently. This option implicit also activates option_t::KDB_O_SYNC because the sync state will be changed when they are marked remove. You might need&nbsp;<wbr><code>option_t::KDB_O_INACTIVE</code>&nbsp;<wbr>set for the previous call of&nbsp;<wbr><code>kdbGet()</code>&nbsp;<wbr>if there are any. Otherwise the recursive remove will fail, because removing directories is only possible when all subkeys are removed.</dl>
<h2>Details</h2>
<p> When you dont have a parentKey or its name empty, then all keys will be set. </p>
<p> You can remove some keys instead of setting them by marking them with <code>keyRemove()</code>. The <code>keyNeedSync()</code> flag will be unset after successful removing. But the <code>keyNeedRemove()</code> flag will stay, but its safe to delete the key. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> contains internal information of <code>opened </code> key database<br />
 <i>ks</i> a KeySet which should contain changed keys, otherwise nothing is done<br />
 <i>parentKey</i> holds the information below which key keys should be set<br />
 <i>options</i> see in <code>kdbSet()</code> documentation</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success </p>
<p> -1 on failure</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>keyNeedSync()</code>, <code>ksNext()</code>, <code>ksCurrent()</code> </p>
<p> <code>keyRemove()</code>, <code>keyNeedRemove()</code> </p>
<p> commandEdit(), commandImport() code in <code>KDB :: Low Level Methods</code> command for usage and error handling example</dl>
<h3>int kdbUnmount (KDB * handle, const Key * mountpoint)Dynamically unmount a single backend.</h3>
<p> Unmount a backend that was mounted with <code>kdbMount()</code> before. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> handle to the kdb data structure<br />
 <i>mountpoint</i> directory where backend is mounted to, that should be unmounted</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success, -1 if an error ocurred.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Elektra Projekt from the source code. </p>
<h2>Index</h2>
