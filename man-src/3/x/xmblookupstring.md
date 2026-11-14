---
title: "xmblookupstring(3)"
name: "xmblookupstring"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmblookupstring/"
description: "XmbLookupString, XwcLookupString, Xutf8LookupString – obtain composed input from an input method"
---

<p>XmbLookupString, XwcLookupString, Xutf8LookupString &#8211; obtain composed input from an input method </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XmbLookupString(XIC <i>ic</i>, XKeyPressedEvent *<i>event</i>, char *<i>buffer_return</i>, int <i>bytes_buffer</i>, KeySym *<i>keysym_return</i>, Status *<i>status_return</i>);</p>
<dd>int XwcLookupString(XIC <i>ic</i>, XKeyPressedEvent *<i>event</i>, wchar_t *<i>buffer_return</i>, int <i>wchars_buffer</i>, KeySym *<i>keysym_return</i>, Status *<i>status_return</i>);</p>
<dd>int Xutf8LookupString(XIC <i>ic</i>, XKeyPressedEvent *<i>event</i>, char *<i>buffer_return</i>, int <i>bytes_buffer</i>, KeySym *<i>keysym_return</i>, Status *<i>status_return</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>buffer_return</i></p>
<dd>Returns a multibyte string or wide character string (if any) from the input method.</p>
<dt><i>bytes_buffer</i></p>
<dd>
<dt><i>wchars_buffer</i></p>
<dd>Specifies space available in the return buffer.</p>
<dt><i>event</i></p>
<dd>Specifies the key event to be used.</p>
<dt><i>ic</i></p>
<dd>Specifies the input context.</p>
<dt><i>keysym_return</i></p>
<dd>Returns the KeySym computed from the event if this argument is not NULL.</p>
<dt><i>status_return</i></p>
<dd>Returns a value indicating what kind of data is returned.</dl>
<h2>Description</h2>
<p>The <code>XmbLookupString</code>, <code>XwcLookupString</code> and <code>Xutf8LookupString</code> functions return the string from the input method specified in the buffer_return argument. If no string is returned, the buffer_return argument is unchanged. </p>
<p> The KeySym into which the KeyCode from the event was mapped is returned in the keysym_return argument if it is non-NULL and the status_return argument indicates that a KeySym was returned. If both a string and a KeySym are returned, the KeySym value does not necessarily correspond to the string returned. </p>
<p> <code>XmbLookupString</code> and <code>Xutf8LookupString</code> return the length of the string in bytes, and <code>XwcLookupString</code> returns the length of the string in characters. Both <code>XmbLookupString</code> and <code>XwcLookupString</code> return text in the encoding of the locale bound to the input method of the specified input context, and <code>Xutf8LookupString</code> returns text in UTF-8 encoding. </p>
<p> Each string returned by <code>XmbLookupString</code> and <code>XwcLookupString</code> begins in the initial state of the encoding of the locale (if the encoding of the locale is state-dependent). </p>
<p> Note: To ensure proper input processing, it is essential that the client pass only <code>KeyPress</code> events to <code>XmbLookupString</code>, <code>XwcLookupString</code> and <code>Xutf8LookupString</code>. Their behavior when a client passes a <code>KeyRelease</code> event is undefined. </p>
<p> Clients should check the status_return argument before using the other returned values. These three functions each return a value to status_return that indicates what has been returned in the other arguments. The possible values returned are: </p>
<table>
<tr VALIGN=top>
<td> <code>XBufferOverflow</code> </td>
<td> The input string to be returned is too large for the supplied buffer_return. The required size (for <code>XmbLookupString</code>, <code>Xutf8LookupString</code> in bytes; for <code>XwcLookupString</code> in characters) is returned as the value of the function, and the contents of buffer_return and keysym_return are not modified. The client should recall the function with the same event and a buffer of adequate size to obtain the string.
</td>
</tr>
<tr VALIGN=top>
<td> <code>XLookupNone</code> </td>
<td> No consistent input has been composed so far. The contents of buffer_return and keysym_return are not modified, and the function returns zero.
</td>
</tr>
<tr VALIGN=top>
<td> <code>XLookupChars</code> </td>
<td> Some input characters have been composed. They are placed in the buffer_return argument, using the encoding described above, and the string length is returned as the value of the function. The content of the keysym_return argument is not modified.
</td>
</tr>
<tr VALIGN=top>
<td> <code>XLookupKeySym</code> </td>
<td> A KeySym has been returned instead of a string and is returned in keysym_return. The content of the buffer_return argument is not modified, and the function returns zero.
</td>
</tr>
<tr VALIGN=top>
<td> <code>XLookupBoth</code> </td>
<td> Both a KeySym and a string are returned; <code>XLookupChars</code> and <code>XLookupKeySym</code> occur simultaneously.
</td>
</tr>
</table>
<p> It does not make any difference if the input context passed as an argument to <code>XmbLookupString</code>, <code>XwcLookupString</code> and <code>Xutf8LookupString</code> is the one currently in possession of the focus or not. Input may have been composed within an input context before it lost the focus, and that input may be returned on subsequent calls to <code>XmbLookupString</code>, <code>XwcLookupString</code> or <code>Xutf8LookupString</code> even though it does not have any more keyboard focus. </p>
<p> The function <code>Xutf8LookupString</code> is an extension introduced by The XFree86 Project, Inc., in their 4.0.2 release. Its presence is indicated by the macro <code>X_HAVE_UTF8_STRING</code>.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xlookupkeysym/">XLookupKeysym</a>(3), <a href="/docs/linux/man/5-compose/">Compose</a>(5)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
