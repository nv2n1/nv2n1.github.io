---
title: "elektra-keyvalue(3)"
name: "elektra-keyvalue"
section: "3"
letter: "e"
url: "/docs/linux/man/3-elektra-keyvalue/"
description: "Key :: Value Manipulation Methods –"
---

<h2 class="name">NAME</h2>
<p> Key :: Value Manipulation Methods &#8211; </p>
<p> Methods to do various operations on Key values.</p>
<h3>Functions</h3>
<p> const void * <code>keyValue</code> (const Key *key) </p>
<p> ssize_t <code>keyGetValueSize</code> (const Key *key) </p>
<p> ssize_t <code>keyGetString</code> (const Key *key, char *returnedString, size_t maxSize) </p>
<p> ssize_t <code>keySetString</code> (Key *key, const char *newStringValue) </p>
<p> ssize_t <code>keyGetBinary</code> (const Key *key, void *returnedBinary, size_t maxSize) </p>
<p> ssize_t <code>keySetBinary</code> (Key *key, const void *newBinary, size_t dataSize) </p>
<p> const char * <code>keyComment</code> (const Key *key) </p>
<p> ssize_t <code>keyGetCommentSize</code> (const Key *key) </p>
<p> ssize_t <code>keyGetComment</code> (const Key *key, char *returnedComment, size_t maxSize) </p>
<p> ssize_t <code>keySetComment</code> (Key *key, const char *newComment) </p>
<h2>Detailed Description</h2>
<p> Methods to do various operations on Key values. </p>
<p> A key can contain a value in different format. The most likely situation is, that the value is interpreted as text. Use <code>keyGetString()</code> for that. You can save any Unicode Symbols and Elektra will take care that you get the same back, independent of your current environment. </p>
<p> In some situations this idea fails. When you need exactly the same value back without any interpretation of the characters, there is <code>keySetBinary()</code>. If you use that, its very likely that your Configuration is not according to the standard. Also for Numbers, Booleans and Date you should use <code>keyGetString()</code>. To do so, you might use strtod() strtol() and then atol() or atof() to convert back. </p>
<p> To use them: </p>
<pre><code>
#include &lt;kdb.h&gt;
</code></pre>
<p>&nbsp;<wbr></p>
<h2>Function Documentation</h2>
<h3>const char* keyComment (const Key * key)Return a pointer to the real internal key comment.</h3>
<p> This is a much more efficient version of <code>keyGetComment()</code> and you should use it if you are responsible enough to not mess up things. You are not allowed to change anything in the memory region the returned pointer points to. </p>
<p> <code>keyComment()</code> returns &#8221; when there is no keyComment. The reason is </p>
<p>key = keyNew(0);<br />
keySetComment(key,&#8221;);<br />
keyComment(key); // you would expect &#8221; here<br />
keyDel(key);</p>
<p> See <code>keySetComment()</code> for more information on comments. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Note that the Key structure keeps its own size field that is calculated by library internal calls, so to avoid inconsistencies, you must never use the pointer returned by <code>keyComment()</code> method to set a new value. Use <code>keySetComment()</code> instead.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>key</i> the key object to work with</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> a pointer to the internal managed comment </p>
<p> 0 on NULL pointer</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>keyGetCommentSize()</code> for size and <code>keyGetComment()</code> as alternative</dl>
<h3>ssize_t keyGetBinary (const Key * key, void * returnedBinary, size_t maxSize)Get the value of a key as a binary.</h3>
<p> If the type is not binary -1 will be returned. </p>
<p> When the binary data is empty (this is not the same as &#8221;!) 0 will be returned and the returnedBinary will not be changed. </p>
<p> For string values see <code>keyGetString()</code> and <code>keyIsString()</code>. </p>
<p> When the returnedBinary is to small to hold the data (its maximum size is given by maxSize), the returnedBinary will not be changed and -1 is returned. </p>
<p> <code>Example:</code>.RS 4 </p>
<p>Key *key = keyNew(&#8216;user/keyname&#8217;, KEY_TYPE, KEY_TYPE_BINARY, KEY_END);<br />
char buffer[300];<br />
if (keyGetBinary(key, buffer, sizeof(buffer)) == -1) {<br />
    // handle error<br />
}</p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>key</i> the object to gather the value from<br />
 <i>returnedBinary</i> pre-allocated memory to store a copy of the key value<br />
 <i>maxSize</i> number of bytes of pre-allocated memory in returnedBinary</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> the number of bytes actually copied to returnedBinary </p>
<p> 0 if the binary is empty </p>
<p> -1 on NULL pointers </p>
<p> -1 when maxSize is 0, too small to hold the value or larger than SSIZE_MAX </p>
<p> -1 on typing error when the key is not binary</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>keyValue()</code>, <code>keyGetValueSize()</code>, <code>keySetBinary()</code> </p>
<p> <code>keyGetString()</code> and <code>keySetString()</code> as preferred alternative to binary </p>
<p> <code>keyIsBinary()</code> to see how to check for binary type</dl>
<h3>ssize_t keyGetComment (const Key * key, char * returnedComment, size_t maxSize)Get the key comment.</h3>
<h2>Comments</h2>
<p> A Key comment is description for humans what this key is for. It may be a textual explanation of valid values, when and why a user or administrator changed the key or any other text that helps the user or administrator related to that key. </p>
<p> Don&#8217;t depend on a comment in your program. A user is always allowed to remove or change it in any way he wants to. But you are allowed or even encouraged to always show the content of the comment to the user and allow him to change it. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>key</i> the key object to work with<br />
 <i>returnedComment</i> pre-allocated memory to copy the comments to<br />
 <i>maxSize</i> number of bytes that will fit returnedComment</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> the number of bytes actually copied to returnedString, including final NULL </p>
<p> 1 if the string is empty </p>
<p> -1 on NULL pointer </p>
<p> -1 if maxSize is 0, not enough to store the comment or when larger then SSIZE_MAX</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>keyGetCommentSize()</code>, <code>keySetComment()</code></dl>
<h3>ssize_t keyGetCommentSize (const Key * key)Calculates number of bytes needed to store a key comment, including final NULL.</h3>
<p> Use this method to know to size for allocated memory to retrieve a key comment. </p>
<p> See <code>keySetComment()</code> for more information on comments. </p>
<p> For an empty key name you need one byte to store the ending NULL. For that reason 1 is returned. </p>
<p>char *buffer;<br />
buffer = malloc(keyGetCommentSize(key));<br />
// use this buffer to store the comment<br />
// pass keyGetCommentSize (key) for maxSize</p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>key</i> the key object to work with</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> number of bytes needed </p>
<p> 1 if there is no comment </p>
<p> -1 on NULL pointer</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>keyGetComment()</code>, <code>keySetComment()</code></dl>
<h3>ssize_t keyGetString (const Key * key, char * returnedString, size_t maxSize)Get the value of a key as a string.</h3>
<p> When there is no value inside the string, 1 will be returned and the returnedString will be empty &#8221; to avoid programming errors that old strings are shown to the user. </p>
<p> For binary values see <code>keyGetBinary()</code> and <code>keyIsBinary()</code>. </p>
<p> <code>Example:</code>.RS 4 </p>
<p>Key *key = keyNew(&#8216;user/keyname&#8217;, KEY_END);<br />
char buffer[300];<br />
if (keyGetString(key, buffer, sizeof(buffer)) == -1) {<br />
    // handle error<br />
} else {<br />
        printf (&#8216;buffer: %s, buffer);<br />
}</p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>key</i> the object to gather the value from<br />
 <i>returnedString</i> pre-allocated memory to store a copy of the key value<br />
 <i>maxSize</i> number of bytes of allocated memory in returnedString</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> the number of bytes actually copied to returnedString, including final NULL </p>
<p> 1 if the string is empty </p>
<p> -1 on NULL pointer </p>
<p> -1 on type mismatch </p>
<p> maxSize is 0, too small for string or is larger than SSIZE_MAX</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>keyValue()</code>, <code>keyGetValueSize()</code>, <code>keySetString()</code> </p>
<p> <code>keyGetBinary()</code> for working with binary data</dl>
<h3>ssize_t keyGetValueSize (const Key * key)Returns the number of bytes needed to store the key value, including the NULL terminator.</h3>
<p> It returns the correct size, independent of the Key Type. If it is a binary there might be &#8216;
