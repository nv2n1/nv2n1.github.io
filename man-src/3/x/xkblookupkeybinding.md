---
title: "xkblookupkeybinding(3)"
name: "xkblookupkeybinding"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkblookupkeybinding/"
description: "XkbLookupKeyBinding – Find the string bound to a key by XRebindKeySym"
---

<p>XkbLookupKeyBinding &#8211; Find the string bound to a key by XRebindKeySym </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>int XkbLookupKeyBinding</code> <code>(Display *</code><i>dpy</i><code>,</code> <code>KeySym </code><i>sym</i><code>,</code> <code>unsigned int </code><i>state</i><code>,</code> <code>char *</code><i>buf</i><code>,</code> <code>int </code><i>nbytes</i><code>,</code> <code>int *</code><i>extra_rtrn</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; dpy</i></p>
<dd>
<dd>connection to server</p>
<dt><i>&#8211; sym</i></p>
<dd>connection to server</p>
<dt><i>&#8211; state</i></p>
<dd>state for which string is to be looked up</p>
<dt><i>&#8211; buf</i></p>
<dd>buffer into which returned string is written</p>
<dt><i>&#8211; nbytes</i></p>
<dd>size of buffer in bytes</p>
<dt><i>&#8211; extra_rtrn</i></p>
<dd>backfilled with number bytes overflow</dl>
<h2>Description</h2>
<p><i>XkbLookupKeyBinding </i> is the equivalent of the core <i>XLookupString </i> function. </p>
<p> <i>XRebindKeysym </i> binds an ASCII string to a specified keysym, so that the string and keysym are returned when the key is pressed and a specified list of modifiers are also being held down. <i>XkbLookupKeyBinding </i> returns in <i>buf </i> the string associated with the keysym <i>sym </i> and modifier state <i>state. buf </i> is NULL terminated unless there&#8217;s an overflow. If the string returned is larger than <i>nbytes, </i> a count of bytes that does not fit into the buffer is returned in <i>extra_rtrn. </i> <i>XkbTranslateKeySym </i> returns the number of bytes that it placed into <i>buf.</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkbtranslatekeysym/">XkbTranslateKeySym</a></code>(3), <code><a href="/docs/linux/man/3-xlookupstring/">XLookupString</a></code>(3), <code><a href="/docs/linux/man/3-xrebindkeysym/">XRebindKeysym</a></code>(3)</p>
