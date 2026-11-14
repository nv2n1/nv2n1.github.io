---
title: "xkbrefreshkeyboardmapping(3)"
name: "xkbrefreshkeyboardmapping"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbrefreshkeyboardmapping/"
description: "XkbRefreshKeyboardMapping – Update the keyboard description that is internal to the X library"
---

<p>XkbRefreshKeyboardMapping &#8211; Update the keyboard description that is internal to the X library </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Status XkbRefreshKeyboardMapping</code> <code>(XkbMapNotifyEvent *</code><i>event</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; event</i></p>
<dd>
<dd>event initiating remapping</dl>
<h2>Description</h2>
<p><i>XkbRefreshKeyboardMapping </i> is the Xkb equivalent of the core <i>XRefreshKeyboardMapping </i> function. It requests that the X server send the current key mapping information to this client. A client usually invokes <i>XkbRefreshKeyboardMapping </i> after receiving an XkbMapNotify event. <i>XkbRefreshKeyboardMapping </i> returns Success if it succeeds and BadMatch if the event is not an Xkb event. </p>
<p> The XkbMapNotify event can be generated when some client calls <i>XkbSetMap, XkbChangeMap, XkbGetKeyboardByName, </i> or any of the standard X library functions that change the keyboard mapping or modifier mapping.</p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>Success</p>
<dd>The <i>XkbRefreshKeyboardMapping </i> function returns Success when the request that the X server send the current key mapping information to this client is successful.</dl>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadMatch</code></p>
<dd>A compatible version of Xkb was not available in the server or an argument has correct type and range, but is otherwise invalid</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkbchangemap/">XkbChangeMap</a></code>(3), <code><a href="/docs/linux/man/3-xkbgetkeyboardbyname/">XkbGetKeyboardByName</a></code>(3), <code><a href="/docs/linux/man/3-xkbsetmap/">XkbSetMap</a></code>(3), <code><a href="/docs/linux/man/3-xrefreshkeyboardmapping/">XRefreshKeyboardMapping</a></code>(3)</p>
