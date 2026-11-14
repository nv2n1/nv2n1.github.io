---
title: "elektra-keymeta(3)"
name: "elektra-keymeta"
section: "3"
letter: "e"
url: "/docs/linux/man/3-elektra-keymeta/"
description: "Key :: Meta Info Manipulation Methods –"
---

<h2 class="name">NAME</h2>
<p> Key :: Meta Info Manipulation Methods &#8211; </p>
<p> Methods to do various operations on Key metainfo.</p>
<h3>Functions</h3>
<p> int <code>keyStat</code> (Key *key) </p>
<p> int <code>keyRemove</code> (Key *key) </p>
<p> uid_t <code>keyGetUID</code> (const Key *key) </p>
<p> int <code>keySetUID</code> (Key *key, uid_t uid) </p>
<p> gid_t <code>keyGetGID</code> (const Key *key) </p>
<p> int <code>keySetGID</code> (Key *key, gid_t gid) </p>
<p> int <code>keySetDir</code> (Key *key) </p>
<p> mode_t <code>keyGetMode</code> (const Key *key) </p>
<p> int <code>keySetMode</code> (Key *key, mode_t mode) </p>
<p> type_t <code>keyGetType</code> (const Key *key) </p>
<p> int <code>keySetType</code> (Key *key, type_t newType) </p>
<p> time_t <code>keyGetATime</code> (const Key *key) </p>
<p> int <code>keySetATime</code> (Key *key, time_t atime) </p>
<p> time_t <code>keyGetMTime</code> (const Key *key) </p>
<p> int <code>keySetMTime</code> (Key *key, time_t mtime) </p>
<p> time_t <code>keyGetCTime</code> (const Key *key) </p>
<p> int <code>keySetCTime</code> (Key *key, time_t ctime) </p>
<h2>Detailed Description</h2>
<p> Methods to do various operations on Key metainfo. </p>
<p> To use them: </p>
<pre><code>
#include &lt;kdb.h&gt;
</code></pre>
<p> Next to <code>Name (key and owner) </code> and <code>Value (data and comment) </code> there is the so called metainfo inside every key. </p>
<p> Key metainfo insists of:</p>
<dl>
<dt>*</p>
<dd> UID, the user id</p>
<dt>*</p>
<dd> GID, the group id</p>
<dt>*</p>
<dd> filesystem-like mode permissions (rwx)</p>
<dt>*</p>
<dd> Mode, change and modification times</dl>
<p> The comment can contain userdata which directly belong to that key. </p>
<p> Owner is the user that owns the key. It only works for the user/ hierachy. </p>
<p> Every user and group of your System has a uniqe ID. These values are used in the keys too. They are very important for the mode. See man 2 chown. </p>
<p> With the mode mode you can choose if a user, group or the world can mode your key. See man 2 chmod.</p>
<h2>Function Documentation</h2>
<h3>time_t keyGetATime (const Key * key)Get last time the key data was read from disk.</h3>
<p> Every <code>kdbGet()</code> might update the access time of a key. You get information when the key was read the last time from the database. </p>
<p> You will get 0 when the key was not read already. </p>
<p> Beware that multiple copies of keys with <code>keyDup()</code> might have different atimes because you <code>kdbGet()</code> one, but not the other. You can use this information to decide which key is the latest. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>key</i> Key to get information from.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> the time you got the key with <code>kdbGet()</code> </p>
<p> 0 on key that was never <code>kdbGet()</code> </p>
<p> (time_t)-1 on NULL pointer</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>keySetATime()</code> </p>
<p> <code>kdbGet()</code></dl>
<h3>time_t keyGetCTime (const Key * key)Get last time the key metadata was changed from disk.</h3>
<p> You will get 0 when the key was not read already. </p>
<p> Any changed field in metadata will influence the ctime of a key. </p>
<p> This time is not updated if only value or comment are changed. </p>
<p> Not changed keys will not update this time, even after <code>kdbSet()</code>. </p>
<p> It is possible that other keys written to disc influence this time if the backend is not grained enough. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>key</i> Key to get information from.</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>keySetCTime()</code></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> (time_t)-1 on NULL pointer </p>
<p> the metadata change time</dl>
<h3>gid_t keyGetGID (const Key * key)Get the group ID of a key.</h3>
<h2>GID</h2>
<p> The group ID is a unique identification for every group present on a system. Keys will belong to root (0) as long as you did not get their real GID with <code>kdbGet()</code>. </p>
<p> Unlike UID users might change their group. This makes it possible to share configuration between some users. </p>
<p> A fresh key will have (gid_t)-1 also known as the group nogroup. It means that the key is not related to a group ID at the moment. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>key</i> the key object to work with</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> the system&#8217;s GID of the key </p>
<p> (gid_t)-1 on NULL key or currently unknown ID</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>keySetGID()</code>, <code>keyGetUID()</code></dl>
<h3>mode_t keyGetMode (const Key * key)Return the key mode permissions.</h3>
<p> Default is 0664 (octal) for keys and 0775 for directory keys which used <code>keySetDir()</code>. </p>
<p> The defaults are defined with the macros KEY_DEF_MODE and KEY_DEF_DIR. </p>
<p> For more information about the mode permissions see <code>Mode</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>key</i> the key object to work with</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> mode permissions of the key </p>
<p> (mode_t)-1 on NULL pointer</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>keySetMode()</code></dl>
<h3>time_t keyGetMTime (const Key * key)Get last modification time of the key on disk.</h3>
<p> You will get 0 when the key was not read already. </p>
<p> Everytime you change value or comment and <code>kdbSet()</code> the key the mtime will be updated. When you <code>kdbGet()</code> the key, the atime is set appropriate. </p>
<p> Not changed keys may not even passed to <code>kdbSet_backend()</code> so it will not update this time, even after <code>kdbSet()</code>. </p>
<p> It is possible that other keys written to disc influence this time if the backend is not grained enough. </p>
<p> If you add or remove a key the key thereunder in the hierarchy will update the mtime if written with <code>kdbSet()</code> to disc. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>key</i> Key to get information from.</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>keySetMTime()</code></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> the last modification time </p>
<p> (time_t)-1 on NULL pointer</dl>
<h3>type_t keyGetType (const Key * key)Returns the key data type.</h3>
<p> See type_t for the type definition. </p>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>keySetType()</code> </p>
<p> <code>keyIsBinary()</code> and <code>keyIsString()</code> </p>
<p> <code>keyIsDir()</code> is not related to the type system</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>key</i> key where to get the type.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> the key type </p>
<p> KEY_TYPE_UNDEFINED on keys without type </p>
<p> -1 on NULL pointer</dl>
<h3>uid_t keyGetUID (const Key * key)Get the user ID of a key.</h3>
<h2>UID</h2>
<p> The user ID is a unique identification for every user present on a system. Keys will belong to root (0) as long as you did not get their real UID with <code>kdbGet()</code>. </p>
<p> Although usually the same, the UID of a key is not related to its owner. </p>
<p> A fresh key will have (uid_t)-1 also known as the user nobody. It means that the key is not related to a user ID at the moment. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>key</i> the key object to work with</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> the system&#8217;s UID of the key </p>
<p> (uid_t)-1 on NULL key or currently unknown ID</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>keyGetGID()</code>, <code>keySetUID()</code>, <code>keyGetOwner()</code></dl>
<h3>int keyRemove (Key * key)Permanently remove a key after committing to database.</h3>
<p> This functions sets a flag that the key needs to be removed. It also sets a flag that it is not synced. </p>
<p> Remove the key instead of writing it in the key database when doing <code>kdbSet()</code> and related functions. </p>
<p> This key will be ignored and it is save to delete it afterwards. To be sure that it was removed, check if it needs sync with <code>keyNeedSync()</code>. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Delete in elektra terminology means to free memory, remove means to free permanent storage.</dl>
<p> <code>Warning:</code></p>
<dl>
<dt>
<dd> You should not change a key&#8217;s remove status once it belongs to a keyset. See <code>ksSort()</code> for more information.</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>keyNeedRemove()</code>, <code>kdbSet()</code>, <code>kdbRemove()</code></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>key</i> the key object to work with</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 1 on success </p>
<p> -1 on NULL pointer</dl>
<h3>int keySetATime (Key * key, time_t atime)Update the atime information for a key.</h3>
<p> When you do manual sync of keys you might also update the atime to make them indistinguishable. </p>
<p> It can also be useful if you work with keys not using a keydatabase. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>key</i> The Key object to work with<br />
 <i>atime</i> The new access time for the key</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success </p>
<p> -1 on NULL pointer</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>keyGetATime()</code></dl>
<h3>int keySetCTime (Key * key, time_t ctime)Update the ctime information for a key.</h3>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>key</i> The Key object to work with<br />
 <i>ctime</i> The new change metadata time for the key</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success </p>
<p> -1 on NULL pointer</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>keyGetCTime()</code></dl>
<h3>int keySetDir (Key * key)Set mode so that key will be recognized as directory.</h3>
<p> The function will add all executable bits. </p>
<dl>
<dt>*</p>
<dd> Mode 0200 will be translated to 0311</p>
<dt>*</p>
<dd> Mode 0400 will be translated to 0711</p>
<dt>*</p>
<dd> Mode 0664 will be translated to 0775</dl>
<p> The macro KEY_DEF_DIR (defined to 0111) will be used for that. </p>
<p> The executable bits show that child keys are allowed and listable. There is no way to have child keys which are not listable for anyone, but it is possible to restrict listing the keys to the owner only. </p>
<dl>
<dt>*</p>
<dd> Mode 0000 means that it is a key not read or writable to anyone.</p>
<dt>*</p>
<dd> Mode 0111 means that it is a directory not read or writable to anyone. But it is recognized as directory to anyone.</dl>
<p> For more about mode see <code>keySetMode()</code>. </p>
<p> It is not possible to access keys below a not executable key. If a key is not writeable and executable <code>kdbSet()</code> will fail to access the keys below. If a key is not readable and executable <code>kdbGet()</code> will fail to access the keys below. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>key</i> the key to set permissions to be recognized as directory.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success </p>
<p> -1 on NULL pointer</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>keySetMode()</code></dl>
<h3>int keySetGID (Key * key, gid_t gid)Set the group ID of a key.</h3>
<p> See <code>GID</code> for more information about group IDs. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>key</i> the key object to work with<br />
 <i>gid</i> is the group ID</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success </p>
<p> -1 on NULL key</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>keyGetGID()</code>, <code>keySetUID()</code></dl>
<h3>int keySetMode (Key * key, mode_t mode)Set the key mode permissions.</h3>
<p> The mode consists of 9 individual bits for mode permissions. In the following explanation the octal notation with leading zero will be used. </p>
<p> Default is 0664 (octal) for keys and 0775 for directory keys which used <code>keySetDir()</code>. </p>
<p> The defaults are defined with the macros KEY_DEF_MODE and KEY_DEF_DIR. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> libelektra 0.7.0 only allows 0775 (directory keys) and 0664 (other keys). More will be added later in a sense of the description below.</dl>
<h2>Mode</h2>
<p> 0000 is the most restrictive mode. No user might read, write or execute the key. </p>
<p> Reading the key means to get the value and comment by <code>kdbGet()</code> or all highlevel methods. </p>
<p> Writing the key means to set the value and comment by <code>kdbSet()</code> or all highlevel methods. </p>
<p> Execute the key means to make a step deeper in the hierarchy. But you must be able to read the key to be able to list the keys below. See also <code>keySetDir()</code> in that context. But you must be able to write the key to be able to add or remove keys below. </p>
<p> 0777 is the most relaxing mode. Every user is allowed to read, write and execute the key, if he is allowed to execute and read all keys below. </p>
<p> 0700 allows every action for the current user, identified by the uid. See <code>keyGetUID()</code> and <code>keySetUID()</code>. </p>
<p> To be more specific for the user the single bits can elect the mode for read, write and execute. 0100 only allows executing which gives the information that it is a directory for that user, but not accessable. 0200 only allows reading. This information may be combined to 0300, which allows execute and reading of the directory. Last 0400 decides about the writing permissions. </p>
<p> The same as above is also valid for the 2 other octal digits. 0070 decides about the group permissions, in that case full access. Groups are identified by the gid. See <code>keyGetGID()</code> and <code>keySetGID()</code>. In that example everyone with a different uid, but the gid of the the key, has full access. </p>
<p> 0007 decides about the world permissions. This is taken into account when neighter the uid nor the gid matches. So that example would allow everyone with a different uid and gid of that key gains full access. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>key</i> the key to set mode permissions<br />
 <i>mode</i> the mode permissions</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success </p>
<p> -1 on NULL key</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>keyGetMode()</code></dl>
<h3>int keySetMTime (Key * key, time_t mtime)Update the mtime information for a key.</h3>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>key</i> The Key object to work with<br />
 <i>mtime</i> The new modification time for the key</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>keyGetMTime()</code></dl>
<h3>int keySetType (Key * key, type_t newType)Set a new key type.</h3>
<p> This method is usually not needed, unless you are working with more semantic value types, or want to force a specific value type for a key. It is not usually needed because the data type is automatically set when setting the key value. </p>
<p> See type_t for the type defintion. </p>
<p> <code>Example:</code>.RS 4 </p>
<pre><code>
// here we define the new type
enum {
    KEY_TYPE_COLOR = KEY_TYPE_STRING + 4
};
// here we make a new key with the type
Key *k1 = keyNew('user/sw/oyranos/current/color1',
                 KEY_VALUE, '#4B52CA',
                 KEY_COMMENT, 'a custom color',
                 KEY_TYPE, KEY_TYPE_COLOR,
                 KEY_END);
// lets check if it is really correct type
if (keyGetType(k1) == KEY_TYPE_COLOR)
    printf('correct type');
</code></pre>
<p> When using type_t::KEY_TYPE_DIR, this method will not set mode permissions to the key. You&#8217;ll have to set it manually after <code>keySetType()</code>, calling <code>keySetMode()</code> with appropriate permissions. Or use the <code>keySetDir()</code>. </p>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>keyGetType()</code> </p>
<p> <code>keySetDir()</code> to see that the directory concept is independent of types</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>key</i> the key object to work with<br />
 <i>newType</i> contains the new type</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on sucess </p>
<p> -1 on NULL pointer and when newType &gt;= KEY_TYPE_MAX</dl>
<h3>int keySetUID (Key * key, uid_t uid)Set the user ID of a key.</h3>
<p> See <code>UID</code> for more information about user IDs. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>key</i> the key object to work with<br />
 <i>uid</i> the user ID to set</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success </p>
<p> -1 on NULL key</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>keySetGID()</code>, <code>keyGetUID()</code>, <code>keyGetOwner()</code></dl>
<h3>int keyStat (Key * key)Only stat a key instead of receiving value, comment and key type.</h3>
<p> Only stat the key in the database when doing <code>kdbGet()</code>. The key may not have any value, comment or key type set. </p>
<p> It is not possible to revert the action on per-key basis. When you want to remove the flag you have to pass option_t::KDB_O_NOSTAT to the next <code>kdbGet()</code>. </p>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>keyNeedStat()</code>, <code>kdbGet()</code></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>key</i> the key object to work with</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 1 on succuess </p>
<p> -1 on NULL pointer</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Elektra Projekt from the source code. </p>
<h2>Index</h2>
