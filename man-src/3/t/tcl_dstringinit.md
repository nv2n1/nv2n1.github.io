---
title: "tcl_dstringinit(3)"
name: "tcl_dstringinit"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_dstringinit/"
description: "Tcl_DStringInit, Tcl_DStringAppend, Tcl_DStringAppendElement, Tcl_DStringStartSublist, Tcl_DStringEndSublist, Tcl_DStringLength, Tcl_DStringValue, Tcl_DStringSetLength, Tcl_DStringTrunc, Tcl_DStrin..."
---

<p>Tcl_DStringInit, Tcl_DStringAppend, Tcl_DStringAppendElement, Tcl_DStringStartSublist, Tcl_DStringEndSublist, Tcl_DStringLength, Tcl_DStringValue, Tcl_DStringSetLength, Tcl_DStringTrunc, Tcl_DStringFree, Tcl_DStringResult, Tcl_DStringGetResult &#8211; manipulate dynamic strings </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
<code>Tcl_DStringInit</code>(<i>dsPtr</i>)
char *
<code>Tcl_DStringAppend</code>(<i>dsPtr, bytes, length</i>)
char *
<code>Tcl_DStringAppendElement</code>(<i>dsPtr, element</i>)
<code>Tcl_DStringStartSublist</code>(<i>dsPtr</i>)
<code>Tcl_DStringEndSublist</code>(<i>dsPtr</i>)
int
<code>Tcl_DStringLength</code>(<i>dsPtr</i>)
char *
<code>Tcl_DStringValue</code>(<i>dsPtr</i>)
<code>Tcl_DStringSetLength</code>(<i>dsPtr, newLength</i>)
<code>Tcl_DStringTrunc</code>(<i>dsPtr, newLength</i>)
<code>Tcl_DStringFree</code>(<i>dsPtr</i>)
<code>Tcl_DStringResult</code>(<i>interp, dsPtr</i>)
<code>Tcl_DStringGetResult</code>(<i>interp, dsPtr</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_DString <i>*dsPtr</i> (in/out) Pointer to structure that is used to manage a dynamic string.</p>
<dd>const char <i>*bytes</i> (in) Pointer to characters to append to dynamic string.</p>
<dd>const char <i>*element</i> (in) Pointer to characters to append as list element to dynamic string.</p>
<dd>int <i>length</i> (in) Number of bytes from <i>bytes</i> to add to dynamic string. If -1, add all characters up to null terminating character.</p>
<dd>int <i>newLength</i> (in) New length for dynamic string, not including null terminating character.</p>
<dd>Tcl_Interp <i>*interp</i> (in/out) Interpreter whose result is to be set from or moved to the dynamic string. </p>
</dl>
<h2>Description</h2>
<p>Dynamic strings provide a mechanism for building up arbitrarily long strings by gradually appending information. If the dynamic string is short then there will be no memory allocation overhead; as the string gets larger, additional space will be allocated as needed. </p>
<p> <code>Tcl_DStringInit</code> initializes a dynamic string to zero length. The Tcl_DString structure must have been allocated by the caller. No assumptions are made about the current state of the structure; anything already in it is discarded. If the structure has been used previously, <code>Tcl_DStringFree</code> should be called first to free up any memory allocated for the old string. </p>
<p> <code>Tcl_DStringAppend</code> adds new information to a dynamic string, allocating more memory for the string if needed. If <i>length</i> is less than zero then everything in <i>bytes</i> is appended to the dynamic string; otherwise <i>length</i> specifies the number of bytes to append. <code>Tcl_DStringAppend</code> returns a pointer to the characters of the new string. The string can also be retrieved from the <i>string</i> field of the Tcl_DString structure. </p>
<p> <code>Tcl_DStringAppendElement</code> is similar to <code>Tcl_DStringAppend</code> except that it does not take a <i>length</i> argument (it appends all of <i>element</i>) and it converts the string to a proper list element before appending. <code>Tcl_DStringAppendElement</code> adds a separator space before the new list element unless the new list element is the first in a list or sub-list (i.e. either the current string is empty, or it contains the single character &#8220;{&#8221;, or the last two characters of the current string are &#8220; {&#8221;). <code>Tcl_DStringAppendElement</code> returns a pointer to the characters of the new string. </p>
<p> <code>Tcl_DStringStartSublist</code> and <code>Tcl_DStringEndSublist</code> can be used to create nested lists. To append a list element that is itself a sublist, first call <code>Tcl_DStringStartSublist</code>, then call <code>Tcl_DStringAppendElement</code> for each of the elements in the sublist, then call <code>Tcl_DStringEndSublist</code> to end the sublist. <code>Tcl_DStringStartSublist</code> appends a space character if needed, followed by an open brace; <code>Tcl_DStringEndSublist</code> appends a close brace. Lists can be nested to any depth. </p>
<p> <code>Tcl_DStringLength</code> is a macro that returns the current length of a dynamic string (not including the terminating null character). <code>Tcl_DStringValue</code> is a macro that returns a pointer to the current contents of a dynamic string. </p>
<p> <code>Tcl_DStringSetLength</code> changes the length of a dynamic string. If <i>newLength</i> is less than the string&#8217;s current length, then the string is truncated. If <i>newLength</i> is greater than the string&#8217;s current length, then the string will become longer and new space will be allocated for the string if needed. However, <code>Tcl_DStringSetLength</code> will not initialize the new space except to provide a terminating null character; it is up to the caller to fill in the new space. <code>Tcl_DStringSetLength</code> does not free up the string&#8217;s storage space even if the string is truncated to zero length, so <code>Tcl_DStringFree</code> will still need to be called. </p>
<p> <code>Tcl_DStringTrunc</code> changes the length of a dynamic string. This procedure is now deprecated. <code>Tcl_DStringSetLength</code> should be used instead. </p>
<p> <code>Tcl_DStringFree</code> should be called when you are finished using the string. It frees up any memory that was allocated for the string and reinitializes the string&#8217;s value to an empty string. </p>
<p> <code>Tcl_DStringResult</code> sets the result of <i>interp</i> to the value of the dynamic string given by <i>dsPtr</i>. It does this by moving a pointer from <i>dsPtr</i> to the interpreter&#8217;s result. This saves the cost of allocating new memory and copying the string. <code>Tcl_DStringResult</code> also reinitializes the dynamic string to an empty string. </p>
<p> <code>Tcl_DStringGetResult</code> does the opposite of <code>Tcl_DStringResult</code>. It sets the value of <i>dsPtr</i> to the result of <i>interp</i> and it clears <i>interp</i>&#8216;s result. If possible it does this by moving a pointer rather than by copying the string. </p>
<h2>Keywords</h2>
<p>append, dynamic string, free, result</p>
