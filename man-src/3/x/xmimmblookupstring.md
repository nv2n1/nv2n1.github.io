---
title: "xmimmblookupstring(3)"
name: "xmimmblookupstring"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmimmblookupstring/"
description: "XmImMbLookupString — An input manager function that retrieves a composed string from an input method"
---

<p><code>XmImMbLookupString</code> &#8212; An input manager function that retrieves a composed string from an input method</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/XmIm.h&gt;
<code>int XmImMbLookupString</code>(
<code>Widget widget</code>,
<code>XKeyPressedEvent *event</code>,
<code>char *buffer_return</code>,
<code>int bytes_buffer</code>,
<code>KeySym *keysym_return</code>,
<code>int *status_return</code>);</pre>
<h2>Description</h2>
<p><code>XmImMbLookupString</code> returns a string composed in the locale associated with the widget&#8217;s input method and a KeySym that is currently mapped to the keycode in a KeyPress event. The KeySym is obtained by using the standard interpretation of Shift, Lock and Group modifiers as defined in the X Protocol specification. </p>
<p> An XIM will be created, but an XIC will not be created. One of the functions, <code>XmImSetValues</code>, <code>XmImVaSetValues</code>, or <code>XmImGetXIC</code>, needs to be called to create an XIC.</p>
<dl COMPACT>
<dt><i>widget</i></dt>
<dd>Specifies the ID of the widget registered with the input manager</dd>
<dt><i>event</i></dt>
<dd>Specifies the key press event</dd>
<dt><i>buffer_return</i></dt>
<dd>Specifies the buffer in which the string is returned</dd>
<dt><i>bytes_buffer</i></dt>
<dd>Specifies the size of the buffer in bytes</dd>
<dt><i>keysym_return</i></dt>
<dd>Specifies a pointer to the KeySym returned if one exists</dd>
<dt><i>status_return</i></dt>
<dd>Specifies the status values returned by the function. These status values are the same as those for the <code>XmbLookupString</code> function. The possible status values are:</dd>
<dl COMPACT>
<dd>
</dd><dl COMPACT>
<dt><code>XBufferOverflow</code></dt>
<dd>The size of the buffer was insufficient to handle the returned string. The contents of <i>buffer_return</i> and <i>keysym_return</i> are not modified. The required buffer size is returned as a value of the function. The client should repeat the call with a larger buffer size to receive the string.</dd>
<dt><code>XLookupNone</code></dt>
<dd>No consistent input was composed. The contents of <i>buffer_return</i> and <i>keysym_return</i> are not modified and the function returns a value of 0.</dd>
<dt><code>XLookupChars</code></dt>
<dd>Some input characters were composed and returned in <i>buffer_return</i>. The content of <i>keysym_return</i> is not modified. The function returns the length of the string in bytes.</dd>
<dt><code>XLookupKeysym</code></dt>
<dd>A keysym value was returned instead of a string. The content of <i>buffer_return</i> is not modified and the function returns a value of 0.</dd>
<dt><code>XLookupBoth</code></dt>
<dd>A keysym value and a string were returned. The keysym value may not necessarily correspond to the string returned. The function returns the length of the string in bytes.</dd></dl>
</dl>
</dl>
<h2>Return</h2>
<p>Return values depend on the status returned by the function. Refer to the description of status values above.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmimgetxim/">XmImGetXIM</a></code>(3), <code><a href="/docs/linux/man/3-xmimgetxic/">XmImGetXIC</a></code>(3), <code><a href="/docs/linux/man/3-xmimregister/">XmImRegister</a></code>(3), <code><a href="/docs/linux/man/3-xmimsetvalues/">XmImSetValues</a></code>(3), and <code><a href="/docs/linux/man/3-xmimunregister/">XmImUnregister</a></code>(3).</p>
