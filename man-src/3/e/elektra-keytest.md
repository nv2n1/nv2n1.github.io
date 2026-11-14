---
title: "elektra-keytest(3)"
name: "elektra-keytest"
section: "3"
letter: "e"
url: "/docs/linux/man/3-elektra-keytest/"
description: "Key :: Methods for Making Tests –"
---

<h2 class="name">NAME</h2>
<p> Key :: Methods for Making Tests &#8211; </p>
<p> Methods to do various tests on Keys.</p>
<h3>Functions</h3>
<p> int <code>keyNeedStat</code> (const Key *key) </p>
<p> int <code>keyNeedSync</code> (const Key *key) </p>
<p> int <code>keyNeedRemove</code> (const Key *key) </p>
<p> int <code>keyIsSystem</code> (const Key *key) </p>
<p> int <code>keyIsUser</code> (const Key *key) </p>
<p> int <code>keyIsBelow</code> (const Key *key, const Key *check) </p>
<p> int <code>keyIsDirectBelow</code> (const Key *key, const Key *check) </p>
<p> int <code>keyIsInactive</code> (const Key *key) </p>
<p> int <code>keyIsDir</code> (const Key *key) </p>
<p> int <code>keyIsBinary</code> (const Key *key) </p>
<p> int <code>keyIsString</code> (const Key *key) </p>
<h2>Detailed Description</h2>
<p> Methods to do various tests on Keys. </p>
<p> To use them: </p>
<pre><code>
#include &lt;kdb.h&gt;
</code></pre>
<p>&nbsp;<wbr></p>
<h2>Function Documentation</h2>
<h3>int keyIsBelow (const Key * key, const Key * check)Check if the key check is below the key key or not.</h3>
<pre>
Example:
key user/sw/app
check user/sw/app/key
returns true because check is below key
Example:
key user/sw/app
check user/sw/app/folder/key
returns also true because check is indirect below key
</pre>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>key</i> the key object to work with<br />
 <i>check</i> the key to find the relative position of</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 1 if check is below key </p>
<p> 0 if it is not below or if it is the same key</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>keySetName()</code>, <code>keyGetName()</code>, <code>keyIsDirectBelow()</code></dl>
<h3>int keyIsBinary (const Key * key)Check if a key is binary type.</h3>
<p> The function checks if the keytype is in the range between KEY_TYPE_BINARY and less than excluding KEY_TYPE_STRING. Then it will be interpreted as binary. </p>
<p> Make sure to use this function and don&#8217;t test the binary type another way to ensure compatibility and to write less error prone programs. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 1 if it is binary </p>
<p> 0 if it is not </p>
<p> -1 on NULL pointer</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>keySetType()</code> for more information on types </p>
<p> <code>keyGetBinary()</code>, <code>keySetBinary()</code></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>key</i> the key to check</dl>
<h3>int keyIsDir (const Key * key)Check if a key is directory key.</h3>
<p> Folder keys may also have value and comment. They are discern by having a executable bit set. </p>
<p> If any executable bit is set it will be recognized as a directory. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> keyIsDir may return true even though you can&#8217;t access the directory.</dl>
<p> To know if you can access the directory, you need to check, if your</p>
<dl>
<dt>*</p>
<dd> user ID is equal the key&#8217;s user ID and the mode &amp; 100 is true</p>
<dt>*</p>
<dd> group ID is equal the key&#8217;s group ID and the mode &amp; 010 is true</p>
<dt>*</p>
<dd> mode &amp; 001 is true</dl>
<p> Accessing does not mean that you can get any value or comments below, see <code>Mode</code> for more information. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>key</i> the key object to work with</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 1 if key is a directory, 0 otherwise </p>
<p> -1 on NULL pointer</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>keySetDir()</code>, <code>keySetMode()</code></dl>
<h3>int keyIsDirectBelow (const Key * key, const Key * check)Check if the key check is direct below the key key or not.</h3>
<pre>
Example:
key user/sw/app
check user/sw/app/key
returns true because check is below key
Example:
key user/sw/app
check user/sw/app/folder/key
does not return true, because there is only a indirect relation
</pre>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>key</i> the key object to work with<br />
 <i>check</i> the key to find the relative position of</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 1 if check is below key </p>
<p> 0 if it is not below or if it is the same key </p>
<p> -1 on null pointer</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>keyIsBelow()</code>, <code>keySetName()</code>, <code>keyGetName()</code></dl>
<h3>int keyIsInactive (const Key * key)Check whether a key is inactive or not.</h3>
<p> In elektra terminology any key is inactive if the it&#8217;s basename starts with &#8216;.&#8217;. Inactive keys must not have any meaning to applications, they are reserved for users and administrators. </p>
<p> To remove a whole hierarchy in elektra, don&#8217;t forget to pass option_t::KDB_O_INACTIVE to <code>kdbGet()</code> to receive the inactive keys in order to remove them. </p>
<p> Otherwise you should not fetch these keys. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>key</i> the key object to work with</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 1 if the key is inactive, 0 otherwise </p>
<p> -1 on NULL pointer or when key has no name</dl>
<h3>int keyIsString (const Key * key)Check if a key is string type.</h3>
<p> The function checks if the keytype is larger or equal KEY_TYPE_STRING. Then it will be considered as string type. </p>
<p> Make sure to use this function and don&#8217;t test the string type another way to ensure compatibility and to write less error prone programs. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 1 if it is string </p>
<p> 0 if it is not </p>
<p> -1 on NULL pointer</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>keySetType</code> for more information on types </p>
<p> <code>keyGetString()</code>, <code>keySetString()</code></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>key</i> the key to check</dl>
<h3>int keyIsSystem (const Key * key)Check whether a key is under the system namespace or not</h3>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>key</i> the key object to work with</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 1 if key name begins with system, 0 otherwise </p>
<p> -1 on NULL pointer</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>keyIsUser()</code>, <code>keySetName()</code>, <code>keyName()</code></dl>
<h3>int keyIsUser (const Key * key)Check whether a key is under the user namespace or not.</h3>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>key</i> the key object to work with</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 1 if key name begins with user, 0 otherwise </p>
<p> -1 on NULL pointer</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>keyIsSystem()</code>, <code>keySetName()</code>, <code>keyName()</code></dl>
<h3>int keyNeedRemove (const Key * key)Ask if key is marked for permanent remove.</h3>
<p> Ask if the key will be removed instead of writing in the key database when doing <code>kdbSetKey()</code> or <code>kdbSet()</code>. </p>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>keyRemove()</code> </p>
<p> <code>kdbSet()</code>, <code>kdbSetKey()</code>, <code>kdbRemove()</code></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>key</i> the key object to work with</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 1 if it is marked, 0 otherwise </p>
<p> -1 on NULL pointer</dl>
<h3>int keyNeedStat (const Key * key)Ask if key is marked for stat only.</h3>
<p> Ask if the key will be stat instead of get it from the key database completely doing <code>kdbGetKey()</code> or <code>kdbGet()</code>. This is useful if you are not interested in the value, comment or key type. </p>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>keyStat()</code>, <code>kdbGet()</code></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>key</i> the key object to work with</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 1 if it is marked, 0 otherwise </p>
<p> -1 on NULL pointer</dl>
<h3>int keyNeedSync (const Key * key)Test if a key needs to be synced to backend storage.</h3>
<p> If any key modification took place the key will be flagged with KEY_FLAG_SYNC so that <code>kdbSet()</code> knows which keys were modified and which not. </p>
<p> After <code>keyNew()</code> the flag will normally be set, but after <code>kdbGet()</code> and <code>kdbSet()</code> the flag will be removed. When you modify the key the flag will be set again. </p>
<p> In your application you can make use of that flag to know if you changed something in a key after a <code>kdbGet()</code> or <code>kdbSet()</code>. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Note that also changes in the meta data will set that flag.</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>keyNew()</code></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>key</i> the key object to work with</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 1 if key was changed in memory, 0 otherwise </p>
<p> -1 on NULL pointer</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Elektra Projekt from the source code. </p>
<h2>Index</h2>
