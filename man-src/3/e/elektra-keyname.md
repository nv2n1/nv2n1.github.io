---
title: "elektra-keyname(3)"
name: "elektra-keyname"
section: "3"
letter: "e"
url: "/docs/linux/man/3-elektra-keyname/"
description: "Key :: Name Manipulation Methods –"
---
<h2 class="name">NAME</h2>
<p> Key :: Name Manipulation Methods - </p>
<p> Methods to do various operations on Key names.  </p>
<h3>Functions</h3>
<p> <br />
 const char * <code>keyName</code> (const Key *key) <br />
 <br />
 ssize_t <code>keyGetNameSize</code> (const Key *key) <br />
 <br />
 ssize_t <code>keyGetName</code> (const Key *key, char *returnedName, size_t maxSize) <br />
 <br />
 ssize_t <code>keySetName</code> (Key *key, const char *newName) <br />
 <br />
 ssize_t <code>keyGetFullNameSize</code> (const Key *key) <br />
 <br />
 ssize_t <code>keyGetFullName</code> (const Key *key, char *returnedName, size_t maxSize) <br />
 <br />
 const char * <code>keyBaseName</code> (const Key *key) <br />
 <br />
 ssize_t <code>keyGetBaseNameSize</code> (const Key *key) <br />
 <br />
 ssize_t <code>keyGetBaseName</code> (const Key *key, char *returned, size_t maxSize) <br />
 <br />
 ssize_t <code>keyAddBaseName</code> (Key *key, const char *baseName) <br />
 <br />
 ssize_t <code>keySetBaseName</code> (Key *key, const char *baseName) <br />
 <br />
 const char * <code>keyOwner</code> (const Key *key) <br />
 <br />
 ssize_t <code>keyGetOwnerSize</code> (const Key *key) <br />
 <br />
 ssize_t <code>keyGetOwner</code> (const Key *key, char *returned, size_t maxSize) <br />
 <br />
 ssize_t <code>keySetOwner</code> (Key *key, const char *owner) <br />
  </p>
<h2>Detailed Description</h2>
<p> Methods to do various operations on Key names. </p>
<p> To use them: </p>
<pre><code>#include &lt;kdb.h&gt;
</code></pre>
<p> These functions make it easier for c programmers to work with key names. Everything here can also be done with keySetName, described in key. </p>
<p> <code>Rules for Key Names</code>.RS 4 </p>
<p> When using Elektra to store your application&#8217;s configuration and state, please keep in mind the following rules: </p>
<dl>
<dt>*</dt>
<dd> <p> You are not allowed to create keys right under system or user. </p>
 </dd>
<dt>*</dt>
<dd> <p> You are not allowed to create folder keys right under system or user. They are reserved for very essential OS subsystems. </p>
 </dd>
<dt>*</dt>
<dd> <p> The keys for your application, called say <i>MyApp</i>, should be created under system/sw/MyApp and/or user/sw/MyApp. </p>
 </dd>
<dt>*</dt>
<dd> <p> It is suggested to make your application look for default keys under system/sw/MyApp/current and/or user/sw/MyApp/current. This way, from a sysadmin perspective, it will be possible to copy the system/sw/MyApp/current tree to something like system/sw/MyApp/old, and keep system clean and organized. </p>
 </dd>
<dt>*</dt>
<dd> <p> \0 must not occur in names. </p>
 </dd>
<dt>*</dt>
<dd> <p> / is the seperator. </p>
 </dd></dl>
<h2>Function Documentation</h2>
<h3>ssize_t keyAddBaseName (Key * key, const char * baseName)Adds baseName to the current key name.</h3>
<p> Assumes that key is a directory. baseName is appended to it. The function adds &#8216;/&#8216; if needed while concatenating. </p>
<p> So if key has name &#8216;system/dir1/dir2&#8217; and this method is called with baseName &#8216;mykey&#8217;, the resulting key will have name &#8216;system/dir1/dir2/mykey&#8217;. </p>
<p> When baseName is 0 or &#8216;&#8216; nothing will happen and the size of the name is returned. </p>
<p> <code>Warning:</code> </p>
<dl>
<dd> <p> You should not change a keys name once it belongs to a keyset. See <code>ksSort()</code> for more information. </p>
 </dd></dl>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>key</i> the key object to work with <br />
 <i>baseName</i> the string to append to the name </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> the size in bytes of the new key name including the ending NULL </p>
<p> -1 if the key had no name </p>
<p> -1 on NULL pointers </p>
 </dd></dl>
<p> <code>See also:</code> </p>
<dl>
<dd> <p> <code>keySetBaseName()</code> </p>
<p> <code>keySetName()</code> to set a new name. </p>
 </dd></dl>
<h3>const char* keyBaseName (const Key * key)Returns a pointer to the real internal key name where the basename starts.</h3>
<p> This is a much more efficient version of <code>keyGetBaseName()</code> and you should use it if you are responsible enough to not mess up things. The name might change or even point to a wrong place after a <code>keySetName()</code>. If you need a copy of the basename consider to use <code>keyGetBaseName()</code>. </p>
<p> <code>keyBaseName()</code> returns &#8216;&#8216; when there is no keyBaseName. The reason is </p>
<pre><code>key=keyNew(0);
keySetName(key,'');
keyName(key); // you would expect '' here
keySetName(key,'user');
keyName(key); // you would expect '' here
keyDel(key);
</code></pre>
<p> <code>Note:</code> </p>
<dl>
<dd> <p> Note that the Key structure keeps its own size field that is calculated by library internal calls, so to avoid inconsistencies, you must never use the pointer returned by <code>keyBaseName()</code> method to set a new value. Use <code>keySetBaseName()</code> instead. </p>
 </dd></dl>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>key</i> the object to obtain the basename from </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> a pointer to the basename </p>
<p> 0 on NULL pointer </p>
 </dd></dl>
<p> <code>See also:</code> </p>
<dl>
<dd> <p> <code>keyGetBaseName()</code>, <code>keyGetBaseNameSize()</code> </p>
<p> <code>keyName()</code> to get a pointer to the name </p>
<p> <code>keyOwner()</code> to get a pointer to the owner </p>
 </dd></dl>
<h3>ssize_t keyGetBaseName (const Key * key, char * returned, size_t maxSize)Calculate the basename of a key name and put it in returned finalizing the string with NULL.</h3>
<p> Some examples: </p>
<dl>
<dt>*</dt>
<dd> <p> basename of system/some/keyname is keyname </p>
 </dd>
<dt>*</dt>
<dd> <p> basename of &#8216;user/tmp/some key&#8217; is &#8216;some key&#8217; </p>
 </dd></dl>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>key</i> the key to extract basename from <br />
 <i>returned</i> a pre-allocated buffer to store the basename <br />
 <i>maxSize</i> size of the returned buffer </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> number of bytes copied to returned </p>
<p> 1 on empty name </p>
<p> -1 on NULL pointers </p>
<p> -1 when maxSize is 0 or larger than SSIZE_MAX </p>
 </dd></dl>
<p> <code>See also:</code> </p>
<dl>
<dd> <p> <code>keyBaseName()</code>, <code>keyGetBaseNameSize()</code> </p>
<p> <code>keyName()</code>, <code>keyGetName()</code>, <code>keySetName()</code> </p>
 </dd></dl>
<h3>ssize_t keyGetBaseNameSize (const Key * key)Calculates number of bytes needed to store basename of key.</h3>
<p> Key names that have only root names (e.g. &#8216;system&#8217; or &#8216;user&#8217; or &#8216;user:domain&#8217; ) does not have basenames, thus the function will return 1 bytes to store &#8216;&#8216;. </p>
<p> Basenames are denoted as: </p>
<dl>
<dt>*</dt>
<dd> <p> system/some/thing/basename -&gt; basename </p>
 </dd>
<dt>*</dt>
<dd> <p> user:domain/some/thing/base\/name &gt; base\/name </p>
 </dd></dl>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>key</i> the key object to work with </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> size in bytes of key&#8217;s basename including ending NULL </p>
 </dd></dl>
<p> <code>See also:</code> </p>
<dl>
<dd> <p> <code>keyBaseName()</code>, <code>keyGetBaseName()</code> </p>
<p> <code>keyName()</code>, <code>keyGetName()</code>, <code>keySetName()</code> </p>
 </dd></dl>
<h3>ssize_t keyGetFullName (const Key * key, char * returnedName, size_t maxSize)Get key full name, including the user domain name.</h3>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> number of bytes written </p>
<p> 1 on empty name </p>
<p> -1 on NULL pointers </p>
<p> -1 if maxSize is 0 or larger than SSIZE_MAX </p>
 </dd></dl>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>key</i> the key object <br />
 <i>returnedName</i> pre-allocated memory to write the key name <br />
 <i>maxSize</i> maximum number of bytes that will fit in returnedName, including the final NULL </p>
 </dd></dl>
<h3>ssize_t keyGetFullNameSize (const Key * key)Bytes needed to store the key name including user domain and ending NULL.</h3>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>key</i> the key object to work with </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> number of bytes needed to store key name including user domain </p>
<p> 1 on empty name </p>
<p> -1 on NULL pointer </p>
 </dd></dl>
<p> <code>See also:</code> </p>
<dl>
<dd> <p> <code>keyGetFullName()</code>, <code>keyGetNameSize()</code> </p>
 </dd></dl>
<h3>ssize_t keyGetName (const Key * key, char * returnedName, size_t maxSize)Get abbreviated key name (without owner name).</h3>
<p> When there is not enough space to write the name, nothing will be written and -1 will be returned. </p>
<p> maxSize is limited to SSIZE_MAX. When this value is exceeded -1 will be returned. The reason for that is that any value higher is just a negative return value passed by accident. Of course malloc is not as failure tolerant and will try to allocate. </p>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> number of bytes written to returnedName </p>
<p> 1 when only a null was written </p>
<p> -1 when keyname is longer then maxSize or 0 or any NULL pointer </p>
 </dd></dl>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>key</i> the key object to work with <br />
 <i>returnedName</i> pre-allocated memory to write the key name <br />
 <i>maxSize</i> maximum number of bytes that will fit in returnedName, including the final NULL </p>
 </dd></dl>
<p> <code>See also:</code> </p>
<dl>
<dd> <p> <code>keyGetNameSize()</code>, <code>keyGetFullName()</code>, <code>keyGetFullNameSize()</code> </p>
 </dd></dl>
<h3>ssize_t keyGetNameSize (const Key * key)Bytes needed to store the key name without owner.</h3>
<p> For an empty key name you need one byte to store the ending NULL. For that reason 1 is returned. </p>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>key</i> the key object to work with </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> number of bytes needed, including ending NULL, to store key name without owner </p>
<p> 1 if there is is no key Name </p>
<p> -1 on NULL pointer </p>
 </dd></dl>
<p> <code>See also:</code> </p>
<dl>
<dd> <p> <code>keyGetName()</code>, <code>keyGetFullNameSize()</code> </p>
 </dd></dl>
<h3>ssize_t keyGetOwner (const Key * key, char * returned, size_t maxSize)Return the owner of the key.</h3>
<dl>
<dt>*</dt>
<dd> <p> Given user:someuser/..... return someuser </p>
 </dd>
<dt>*</dt>
<dd> <p> Given user:some.user/.... return some.user </p>
 </dd>
<dt>*</dt>
<dd> <p> Given user/.... return the current user </p>
 </dd></dl>
<p> Only user/... keys have a owner. For system/... keys (that doesn&#8217;t have a key owner) an empty string (&#8216;&#8216;) is returned. </p>
<p> Although usually the same, the owner of a key is not related to its UID. Owner are related to WHERE the key is stored on disk, while UIDs are related to mode controls of a key. </p>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>key</i> the object to work with <br />
 <i>returned</i> a pre-allocated space to store the owner <br />
 <i>maxSize</i> maximum number of bytes that fit returned </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> number of bytes written to buffer </p>
<p> 1 if there is no owner </p>
<p> -1 on NULL pointers </p>
<p> -1 when maxSize is 0, larger than SSIZE_MAX or too small for ownername </p>
 </dd></dl>
<p> <code>See also:</code> </p>
<dl>
<dd> <p> <code>keySetName()</code>, <code>keySetOwner()</code>, <code>keyOwner()</code>, <code>keyGetFullName()</code> </p>
 </dd></dl>
<h3>ssize_t keyGetOwnerSize (const Key * key)Return the size of the owner of the Key with concluding 0.</h3>
<p> The returned number can be used to allocate a string. 1 will returned on an empty owner to store the concluding 0 on using <code>keyGetOwner()</code>. </p>
<pre><code>char * buffer;
buffer = malloc (keyGetOwnerSize (key));
// use buffer and keyGetOwnerSize (key) for maxSize
</code></pre>
<p> <code>Note:</code> </p>
<dl>
<dd> <p> that -1 might be returned on null pointer, so when you directly allocate afterwards its best to check if you will pass a null pointer before. </p>
 </dd></dl>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>key</i> the key object to work with </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> number of bytes </p>
<p> 1 if there is no owner </p>
<p> -1 on NULL pointer </p>
 </dd></dl>
<p> <code>See also:</code> </p>
<dl>
<dd> <p> <code>keyGetOwner()</code> </p>
 </dd></dl>
<h3>const char* keyName (const Key * key)Returns a pointer to the abbreviated real internal key name.</h3>
<p> This is a much more efficient version of <code>keyGetName()</code> and can use it if you are responsible enough to not mess up things. You are not allowed to change anything in the returned array. The content of that string may change after <code>keySetName()</code> and similar functions. If you need a copy of the name, consider using <code>keyGetName()</code>. </p>
<p> The name will be without owner, see <code>keyGetFullName()</code> if you need the name with its owner. </p>
<p> <code>keyName()</code> returns &#8216;&#8216; when there is no keyName. The reason is </p>
<pre><code>key=keyNew(0);
keySetName(key,'');
keyName(key); // you would expect '' here
keyDel(key);
</code></pre>
<p> <code>Note:</code> </p>
<dl>
<dd> <p> Note that the Key structure keeps its own size field that is calculated by library internal calls, so to avoid inconsistencies, you must never use the pointer returned by <code>keyName()</code> method to set a new value. Use <code>keySetName()</code> instead. </p>
 </dd></dl>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>key</i> the key object to work with </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> a pointer to the keyname which must not be changed. </p>
<p> 0 on NULL pointer </p>
 </dd></dl>
<p> <code>See also:</code> </p>
<dl>
<dd> <p> <code>keyGetNameSize()</code> for the string length </p>
<p> <code>keyGetFullName()</code>, <code>keyGetFullNameSize()</code> to get the full name </p>
<p> <code>keyGetName()</code> as alternative to get a copy </p>
<p> <code>keyOwner()</code> to get a pointer to owner </p>
 </dd></dl>
<h3>const char* keyOwner (const Key * key)Return a pointer to the real internal key owner.</h3>
<p> This is a much more efficient version of <code>keyGetOwner()</code> and you should use it if you are responsible enough to not mess up things. You are not allowed to modify the returned string in any way. If you need a copy of the string, consider to use <code>keyGetOwner()</code> instead. </p>
<p> <code>keyOwner()</code> returns &#8216;&#8216; when there is no keyOwner. The reason is </p>
<pre><code>key=keyNew(0);
keySetOwner(key,'');
keyOwner(key); // you would expect '' here
keySetOwner(key,'system');
keyOwner(key); // you would expect '' here
</code></pre>
<p> <code>Note:</code> </p>
<dl>
<dd> <p> Note that the Key structure keeps its own size field that is calculated by library internal calls, so to avoid inconsistencies, you must never use the pointer returned by <code>keyOwner()</code> method to set a new value. Use <code>keySetOwner()</code> instead. </p>
 </dd></dl>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>key</i> the key object to work with </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> a pointer to internal owner </p>
<p> 0 on NULL pointer </p>
 </dd></dl>
<p> <code>See also:</code> </p>
<dl>
<dd> <p> <code>keyGetOwnerSize()</code> for the size of the string with concluding 0 </p>
<p> <code>keyGetOwner()</code>, <code>keySetOwner()</code> </p>
<p> <code>keyName()</code> for name without owner </p>
<p> <code>keyGetFullName()</code> for name with owner </p>
 </dd></dl>
<h3>ssize_t keySetBaseName (Key * key, const char * baseName)Sets baseName as the new basename for key.</h3>
<p> All text after the last &#8216;/&#8216; in the key keyname is erased and baseName is appended. </p>
<p> So lets suppose key has name &#8216;system/dir1/dir2/key1&#8217;. If baseName is &#8216;key2&#8217;, the resulting key name will be &#8216;system/dir1/dir2/key2&#8217;. If baseName is empty or NULL, the resulting key name will be &#8216;system/dir1/dir2&#8217;. </p>
<p> <code>Warning:</code> </p>
<dl>
<dd> <p> You should not change a keys name once it belongs to a keyset. See <code>ksSort()</code> for more information. </p>
 </dd></dl>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>key</i> the key object to work with <br />
 <i>baseName</i> the string used to overwrite the basename of the key </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> the size in bytes of the new key name </p>
<p> -1 on NULL pointers </p>
 </dd></dl>
<p> <code>See also:</code> </p>
<dl>
<dd> <p> <code>keyAddBaseName()</code> </p>
<p> <code>keySetName()</code> to set a new name </p>
 </dd></dl>
<h3>ssize_t keySetName (Key * key, const char * newName)Set a new name to a key.</h3>
<p> A valid name is of the forms: </p>
<dl>
<dt>*</dt>
<dd> <p> system/something </p>
 </dd>
<dt>*</dt>
<dd> <p> user/something </p>
 </dd>
<dt>*</dt>
<dd> <p> user:username/something </p>
 </dd></dl>
<p> The last form has explicitly set the owner, to let the library know in which user folder to save the key. A owner is a user name. If not defined (the second form) current user is calculated and used as default. </p>
<p> You should always follow the guidelines for key tree structure creation. </p>
<p> A private copy of the key name will be stored, and the newName parameter can be freed after this call. </p>
<p> On invalid names, NULL or &#8216;&#8216; the name will be &#8216;&#8216; afterwards. </p>
<p> <code>Warning:</code> </p>
<dl>
<dd> <p> You should not change a keys name once it belongs to a keyset. See <code>ksSort()</code> for more information. </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> size in bytes of this new key name including ending NULL </p>
<p> -1 if newName is empty or invalid or any NULL pointer </p>
 </dd></dl>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>key</i> the key object to work with <br />
 <i>newName</i> the new key name </p>
 </dd></dl>
<p> <code>See also:</code> </p>
<dl>
<dd> <p> <code>keyNew()</code>, <code>keySetOwner()</code> </p>
<p> <code>keyGetName()</code>, <code>keyGetFullName()</code>, <code>keyName()</code> </p>
<p> <code>keySetBaseName()</code>, <code>keyAddBaseName()</code> to manipulate a name </p>
 </dd></dl>
<h3>ssize_t keySetOwner (Key * key, const char * owner)Set the owner of a key.</h3>
<p> A owner is a name of a system user related to a UID. The owner decides on which location on the disc the key goes. </p>
<p> A private copy is stored, so the passed parameter can be freed after the call. </p>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>key</i> the key object to work with <br />
 <i>owner</i> the owner (or user name) </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> the number of bytes actually saved including final NULL </p>
<p> 1 when owner is freed (by setting 0 or &#8216;&#8216;) </p>
<p> -1 on null pointer or memory problems </p>
 </dd></dl>
<p> <code>See also:</code> </p>
<dl>
<dd> <p> <code>keySetName()</code>, <code>keyGetOwner()</code>, <code>keyGetFullName()</code> </p>
 </dd></dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Elektra Projekt from the source code. </p>
<h2>Index</h2>
<dl>
<dt><a href="#lbAB">NAME</a></dt>
<dd>  </dd>
<dl>
<dt><a href="#lbAC">Functions</a></dt>
<dd>  </dd></dl>
<dt><a href="#lbAD">Detailed Description</a></dt>
<dd>  </dd>
<dt><a href="#lbAE">Function Documentation</a></dt>
<dd>  </dd>
<dl>
<dt><a href="#lbAF">ssize_t keyAddBaseName (Key * key, const char * baseName)Adds baseName to the current key name.</a></dt>
<dd>  </dd>
<dt><a href="#lbAG">const char* keyBaseName (const Key * key)Returns a pointer to the real internal key name where the basename starts.</a></dt>
<dd>  </dd>
<dt><a href="#lbAH">ssize_t keyGetBaseName (const Key * key, char * returned, size_t maxSize)Calculate the basename of a key name and put it in returned finalizing the string with NULL.</a></dt>
<dd>  </dd>
<dt><a href="#lbAI">ssize_t keyGetBaseNameSize (const Key * key)Calculates number of bytes needed to store basename of key.</a></dt>
<dd>  </dd>
<dt><a href="#lbAJ">ssize_t keyGetFullName (const Key * key, char * returnedName, size_t maxSize)Get key full name, including the user domain name.</a></dt>
<dd>  </dd>
<dt><a href="#lbAK">ssize_t keyGetFullNameSize (const Key * key)Bytes needed to store the key name including user domain and ending NULL.</a></dt>
<dd>  </dd>
<dt><a href="#lbAL">ssize_t keyGetName (const Key * key, char * returnedName, size_t maxSize)Get abbreviated key name (without owner name).</a></dt>
<dd>  </dd>
<dt><a href="#lbAM">ssize_t keyGetNameSize (const Key * key)Bytes needed to store the key name without owner.</a></dt>
<dd>  </dd>
<dt><a href="#lbAN">ssize_t keyGetOwner (const Key * key, char * returned, size_t maxSize)Return the owner of the key.</a></dt>
<dd>  </dd>
<dt><a href="#lbAO">ssize_t keyGetOwnerSize (const Key * key)Return the size of the owner of the Key with concluding 0.</a></dt>
<dd>  </dd>
<dt><a href="#lbAP">const char* keyName (const Key * key)Returns a pointer to the abbreviated real internal key name.</a></dt>
<dd>  </dd>
<dt><a href="#lbAQ">const char* keyOwner (const Key * key)Return a pointer to the real internal key owner.</a></dt>
<dd>  </dd>
<dt><a href="#lbAR">ssize_t keySetBaseName (Key * key, const char * baseName)Sets baseName as the new basename for key.</a></dt>
<dd>  </dd>
<dt><a href="#lbAS">ssize_t keySetName (Key * key, const char * newName)Set a new name to a key.</a></dt>
<dd>  </dd>
<dt><a href="#lbAT">ssize_t keySetOwner (Key * key, const char * owner)Set the owner of a key.</a></dt>
<dd>  </dd></dl>
<dt><a href="#lbAU">Author</a></dt>
<dd>  </dd></dl>
