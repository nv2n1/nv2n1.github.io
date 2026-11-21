---
title: "elektra-key(3)"
name: "elektra-key"
section: "3"
letter: "e"
url: "/docs/linux/man/3-elektra-key/"
description: "Key :: Basic Methods –"
---

<p> Key construction and initialization methods.</p>
<h3>Functions</h3>
<p> Key * <code>keyNew</code> (const char *keyName,&#8230;) </p>
<p> Key * <code>keyDup</code> (const Key *source) </p>
<p> int <code>keyCopy</code> (Key *dest, const Key *source) </p>
<p> int <code>keyDel</code> (Key *key) </p>
<p> ssize_t <code>keyIncRef</code> (Key *key) </p>
<p> ssize_t <code>keyDecRef</code> (Key *key) </p>
<p> ssize_t <code>keyGetRef</code> (const Key *key) </p>
<h2>Detailed Description</h2>
<p> Key construction and initialization methods. </p>
<p> To use them: </p>
<pre><code>
#include &lt;kdb.h&gt;
</code></pre>
<p> A Key is the essential class that encapsulates key <code>name </code>, <code>value </code> and <code>metainfo </code>. Key properties are:</p>
<dl>
<dt>*</dt>
<dd> <code>Key name </code></dd>
<dt>*</dt>
<dd> <code>Key value </code></dd>
<dt>*</dt>
<dd> <code>Data type </code></dd>
<dt>*</dt>
<dd> <code>Key comment </code></dd>
<dt>*</dt>
<dd> <code>Key owner </code></dd>
<dt>*</dt>
<dd> <code>UID, GID and filesystem-like mode permissions </code></dd>
<dt>*</dt>
<dd> <code>Mode, change and modification times </code></dd></dl>
<p> Described here the methods to allocate and free the key.</p>
<h2>Function Documentation</h2>
<h3>int keyCopy (Key * dest, const Key * source)Copy or Clear a key.</h3>
<p> Most often you may prefer <code>keyDup()</code> which allocates a new key and returns a duplication of another key. </p>
<p> But when you need to copy into an existing key, e.g. because it was passed by a pointer in a function you can do so: </p>
<p>int h(Key *k)<br />
{<br />
    // receive key c<br />
    keyCopy(k, c);<br />
    // the caller will see the changed key k<br />
}</p>
<p> The reference counter will not change for the destination key. Affiliation to keysets are also not affected. </p>
<p> When you pass a NULL-pointer as source the data of dest will be cleaned completely and you get a fresh dest key. </p>
<p>int g(Key *k)<br />
{<br />
    keyCopy(k, 0);<br />
    // k is now an empty and fresh key<br />
}</p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
</dt><dd> <i>dest</i> the key which will be written to<br />
 <i>source</i> the key which should be copied or NULL to clean the destination key</dd></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
</dt><dd> -1 on failure when a NULL pointer was passed for dest or a dynamic property could not be written. </dd>
<p> 0 when dest was cleaned </p>
<p> 1 when source was successfully copied</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
</dt><dd> <code>keyDup()</code> to get a duplication of a <code>Key :: Basic Methods</code></dd></dl>
<h3>ssize_t keyDecRef (Key * key)Decrement the viability of a key object.</h3>
<p> The reference counter can&#8217;t be decremented once it reached 0. In that situation nothing will happen and 0 will be returned. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
</dt><dd> the value of the new reference counter </dd>
<p> -1 on null pointer </p>
<p> 0 when the key is ready to be freed</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
</dt><dd> <i>key</i> the key object to work with</dd></dl>
<p> <code>See also:</code></p>
<dl>
<dt>
</dt><dd> <code>keyGetRef()</code>, <code>keyDel()</code>, <code>keyIncRef()</code></dd></dl>
<h3>int keyDel (Key * key)A destructor for Key objects.</h3>
<p> Every key created by <code>keyNew()</code> must be deleted with <code>keyDel()</code>. </p>
<p> It is save to delete keys which are in a keyset, the number of references will be returned then. </p>
<p> It is save to delete a nullpointer, -1 will be returned then. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
</dt><dd> <i>key</i> the key object to delete</dd></dl>
<p> <code>See also:</code></p>
<dl>
<dt>
</dt><dd> <code>keyNew()</code>, keyInc(), <code>keyGetRef()</code></dd></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
</dt><dd> the value of the reference counter if the key is within keyset(s) </dd>
<p> 0 when the key was freed </p>
<p> -1 on null pointers</dl>
<h3>Key* keyDup (const Key * source)Return a duplicate of a key.</h3>
<p> Memory will be allocated as needed for dynamic properties. </p>
<p> The new key will not be member of any KeySet and will start with a new reference counter at 0. A subsequent <code>keyDel()</code> will delete the key. </p>
<p>int f(const Key *source)<br />
{<br />
    Key *dup = keyDup(source);<br />
    // work with duplicate<br />
    keyDel(dup);<br />
    // everything related to dup is freed<br />
    // and source is unchanged<br />
}</p>
<p> Like for a new key after <code>keyNew()</code> a subsequent <code>ksAppend()</code> makes a KeySet to take care of the lifecycle of the key. </p>
<p>int g(const Key *source, KeySet *ks)<br />
{<br />
    Key *dup = keyDup(source);<br />
    // work with duplicate<br />
    ksAppendKey(ks, dup);<br />
    // ksDel(ks) will also free the duplicate<br />
    // source remains unchanged.<br />
}</p>
<p> Duplication of keys should be preferred to <code>keyNew()</code>, because data like owner can be filled with a copy of the key instead of asking the environment. It can also be optimized in the checks, because the keyname is known to be valid. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
</dt><dd> <i>source</i> has to be an initializised source Key</dd></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
</dt><dd> 0 failure or on NULL pointer </dd>
<p> a fully copy of source on success</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
</dt><dd> <code>ksAppend()</code>, <code>keyDel()</code> </dd>
<p> keyClear(), <code>keyNew()</code></dl>
<h3>ssize_t keyGetRef (const Key * key)Return how many references the key has.</h3>
<p> The references will be incremented when <code>ksAppendKey()</code> or <code>ksAppend()</code> uses the key and will be decremented when <code>ksPop()</code> is used. </p>
<p> <code>keyDup()</code> will reset the references for dupped key. </p>
<p> For your own applications you can use <code>keyIncRef()</code> and keyDelRef() for reference counting. Keys with zero references will be deleted when using <code>keyDel()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
</dt><dd> <i>key</i> the key object to work with</dd></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
</dt><dd> the number of references </dd>
<p> -1 on null pointer</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
</dt><dd> <code>keyIncRef()</code> and <code>keyDecRef()</code></dd></dl>
<h3>ssize_t keyIncRef (Key * key)Increment the viability of a key object.</h3>
<p> This function is intended for applications using their own reference counter for key objects. With it you can increment the reference and thus avoid destruction of the object in a subsequent <code>keyDel()</code>. </p>
<p>Key *k;<br />
keyInc(k);<br />
function_that_keyDec(k);<br />
// work with k<br />
keyDel(k); // now really free it</p>
<p> The reference counter can&#8217;t be incremented once it reached SSIZE_MAX. In that situation nothing will happen and SSIZE_MAX will be returned. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
</dt><dd> the value of the new reference counter </dd>
<p> -1 on null pointer </p>
<p> SSIZE_MAX when maximum exceeded</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
</dt><dd> <i>key</i> the key object to work with</dd></dl>
<p> <code>See also:</code></p>
<dl>
<dt>
</dt><dd> <code>keyGetRef()</code>, <code>keyDecRef()</code>, <code>keyDel()</code></dd></dl>
<h3>Key* keyNew (const char * keyName, &#8230;)A practical way to fully create a Key object in one step.</h3>
<p> This function tries to mimic the C++ way for constructors. </p>
<p> To just get a key object, simple do: </p>
<p>Key *k = keyNew(0);<br />
// work with it<br />
keyDel(k);</p>
<p> If you want the key object to contain a name, value, comment and other meta info read on. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
</dt><dd> When you already have a key with similar properties its easier and cheaper to <code>keyDup()</code> the key.</dd></dl>
<p> Due to ABI compatibility, the Key structure is not defined in kdb.h, only declared. So you can only declare pointers to Keys in your program, and allocate and free memory for them with <code>keyNew()</code> and <code>keyDel()</code> respectively. See <a rel="nofollow" href="http://tldp.org/HOWTO/Program-Library-HOWTO/shared-libraries.html#AEN135">http://tldp.org/HOWTO/Program-Library-HOWTO/shared-libraries.html#AEN135</a> </p>
<p> You can call it in many different ways depending on the attribute tags you pass as parameters. Tags are represented as the keyswitch_t values, and tell <code>keyNew()</code> which Key attribute comes next. </p>
<p> The simplest and minimum way to use it is with no tags, only a key name: </p>
<p>Key *nullKey, *emptyNamedKey;<br />
// Create a key that has no name, is completely empty, but is initialized<br />
nullKey = keyNew(0);<br />
keyDel(nullKey);<br />
// Is the same as above<br />
nullKey = keyNew(&#8221;, KEY_END);<br />
keyDel(nullKey);<br />
// Create and initialize a key with a name and nothing else<br />
emptyNamedKey = keyNew(&#8216;user/some/example&#8217;, KEY_END);<br />
keyDel(emptyNamedKey);</p>
<p> <code>keyNew()</code> allocates memory for a key object and cleans everything up. After that, it processes the given argument list. </p>
<p> The Key attribute tags are the following:</p>
<dl>
<dt>*</dt>
<dd> keyswitch_t::KEY_TYPE </dd>
<p>&nbsp;<wbr>Next parameter is a type of the value. Default assumed is KEY_TYPE_UNDEFINED. Set this attribute so that a subsequent KEY_VALUE can toggle to&nbsp;<wbr><code>keySetString()</code>&nbsp;<wbr>or&nbsp;<wbr><code>keySetBinary()</code>&nbsp;<wbr>regarding to&nbsp;<wbr><code>keyIsString()</code>&nbsp;<wbr>or&nbsp;<wbr><code>keyIsBinary()</code>. If you don&#8217;t use KEY_TYPE but a KEY_VALUE follows afterwards, KEY_TYPE_STRING will be used.</p>
<dt>*</dt>
<dd> keyswitch_t::KEY_SIZE </dd>
<p>&nbsp;<wbr>Define a maximum length of the value. This is especially useful for setting a binary key. So make sure you use that before you KEY_VALUE for binary keys.</p>
<dt>*</dt>
<dd> keyswitch_t::KEY_VALUE </dd>
<p>&nbsp;<wbr>Next parameter is a pointer to the value that will be set to the key If no keyswitch_t::KEY_TYPE was used before, keyswitch_t::KEY_TYPE_STRING is assumed. If KEY_TYPE was previously passed with a KEY_TYPE_BINARY, you should have passed KEY_SIZE before!&nbsp;<wbr>Otherwise it will be cut of with first&nbsp;<wbr>&nbsp;<wbr>\0 in string! </p>
<dt>*</dt>
<dd> <p> keyswitch_t::KEY_UID, keyswitch_t::KEY_GID <br />
 <br />
&nbsp;<wbr>Next parameter is taken as the UID&nbsp;<wbr>(uid_t)&nbsp;<wbr>or GID&nbsp;<wbr>(gid_t)&nbsp;<wbr>that will be defined on the key. See&nbsp;<wbr><code>keySetUID()</code>&nbsp;<wbr>and&nbsp;<wbr><code>keySetGID()</code>. </p>
 </dd>
<dt>*</dt>
<dd> <p> keyswitch_t::KEY_MODE <br />
 <br />
&nbsp;<wbr>Next parameter is taken as mode permissions&nbsp;<wbr>(mode_t)&nbsp;<wbr>to the key. See&nbsp;<wbr><code>keySetMode()</code>. </p>
 </dd>
<dt>*</dt>
<dd> <p> keyswitch_t::KEY_DIR <br />
 <br />
&nbsp;<wbr>Define that the key is a directory rather than a ordinary key. This means its executable bits in its mode are set. This option allows the key to have subkeys. See&nbsp;<wbr><code>keySetDir()</code>. </p>
 </dd>
<dt>*</dt>
<dd> <p> keyswitch_t::KEY_OWNER <br />
 <br />
&nbsp;<wbr>Next parameter is the owner. See&nbsp;<wbr><code>keySetOwner()</code>. </p>
 </dd>
<dt>*</dt>
<dd> <p> keyswitch_t::KEY_COMMENT <br />
 <br />
&nbsp;<wbr>Next parameter is a comment. See&nbsp;<wbr><code>keySetComment()</code>. </p>
 </dd>
<dt>*</dt>
<dd> <p> keyswitch_t::KEY_REMOVE <br />
 <br />
&nbsp;<wbr>Mark the key to be removed instead of set it. See&nbsp;<wbr><code>keyRemove()</code>. </p>
 </dd>
<dt>*</dt>
<dd> <p> keyswitch_t::KEY_STAT <br />
 <br />
&nbsp;<wbr>Mark the key to be stated instead of get it. See&nbsp;<wbr><code>keyStat()</code>. </p>
 </dd>
<dt>*</dt>
<dd> <p> keyswitch_t::KEY_END <br />
 <br />
&nbsp;<wbr>Must be the last parameter passed to&nbsp;<wbr><code>keyNew()</code>. It is always required, unless the keyName is 0. </p>
 </dd></dl>
<p> <code>Example:</code>.RS 4 </p>
<pre><code>KeySet *ks=ksNew(0);
ksAppendKey(ks,keyNew(0)); // an empty key
ksAppendKey(ks,keyNew('user/sw', // the name of the key
        KEY_END)); // no more args
ksAppendKey(ks,keyNew('user/tmp/ex1',
        KEY_VALUE,'some data', // set a string value
        KEY_END)); // end of args
ksAppendKey(ks,keyNew('user/tmp/ex2',
        KEY_VALUE,'some data', // with a simple value
        KEY_MODE,0777, // permissions
        KEY_END)); // end of args
ksAppendKey(ks,keyNew('user/tmp/ex4',
        KEY_TYPE,KEY_TYPE_BINARY, // key type
        KEY_SIZE,7, // assume binary length 7
        KEY_VALUE,'some data', // value that will be truncated in 7 bytes
        KEY_COMMENT,'value is truncated',
        KEY_OWNER,'root', // owner (not uid) is root
        KEY_UID,0, // root uid
        KEY_END)); // end of args
ksAppendKey(ks,keyNew('user/tmp/ex5',
        KEY_TYPE,
                KEY_TYPE_DIR | KEY_TYPE_BINARY,// dir key with a binary value
        KEY_SIZE,7,
        KEY_VALUE,'some data', // value that will be truncated in 7 bytes
        KEY_COMMENT,'value is truncated',
        KEY_OWNER,'root', // owner (not uid) is root
        KEY_UID,0, // root uid
        KEY_END)); // end of args
ksDel(ks);
</code></pre>
<p> The reference counter (see <code>keyGetRef()</code>) will be initialized with 0, that means a subsequent call of <code>keyDel()</code> will delete the key. If you append the key to a keyset the reference counter will be incremented by one (see keyInc()) and the key can&#8217;t be be deleted by a <code>keyDel()</code>. </p>
<pre><code>Key *k = keyNew(0); // ref counter 0
ksAppendKey(ks, k); // ref counter of key 1
ksDel(ks); // key will be deleted with keyset
 *
</code></pre>
<p> If you increment only by one with keyInc() the same as said above is valid: </p>
<pre><code>Key *k = keyNew(0); // ref counter 0
keyIncRef(k); // ref counter of key 1
keyDel(k); // has no effect
keyDecRef(k); // ref counter back to 0
keyDel(k); // key is now deleted
 *
</code></pre>
<p> If you add the key to more keySets: </p>
<pre><code>Key *k = keyNew(0); // ref counter 0
ksAppendKey(ks1, k); // ref counter of key 1
ksAppendKey(ks2, k); // ref counter of key 2
ksDel(ks1); // ref counter of key 1
ksDel(ks2); // k is now deleted
 *
</code></pre>
<p> or use keyInc() more than once: </p>
<pre><code>Key *k = keyNew(0); // ref counter 0
keyIncRef(k); // ref counter of key 1
keyDel (k); // has no effect
keyIncRef(k); // ref counter of key 2
keyDel (k); // has no effect
keyDecRef(k); // ref counter of key 1
keyDel (k); // has no effect
keyDecRef(k); // ref counter is now 0
keyDel (k); // k is now deleted
 *
</code></pre>
<p> they key won&#8217;t be deleted by a <code>keyDel()</code> as long refcounter is not 0. </p>
<p> The key&#8217;s sync bit will always be set for any call, except: </p>
<pre><code>Key *k = keyNew(0);
// keyNeedSync() will be false
</code></pre>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>keyName</i> a valid name to the key, or NULL to get a simple initialized, but really empty, object </p>
 </dd></dl>
<p> <code>See also:</code> </p>
<dl>
<dd> <p> <code>keyDel()</code> </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> a pointer to a new allocated and initialized Key object, or NULL if an invalid keyName was passed (see <code>keySetName()</code>). </p>
 </dd></dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Elektra Projekt from the source code. </p>
