---
title: "xmgetmenucursor(3)"
name: "xmgetmenucursor"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmgetmenucursor/"
description: "XmGetMenuCursor — A function that returns the cursor ID for the current menu cursor"
---

<p><code>XmGetMenuCursor</code> &#8212; A function that returns the cursor ID for the current menu cursor</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>Cursor XmGetMenuCursor</code>(
<code>Display * display</code>);</pre>
<h2>Description</h2>
<p><code>XmGetMenuCursor</code> queries the menu cursor currently being used by this client on the specified display and returns the cursor ID. This function returns the menu cursor for the default screen of the display. </p>
<p> <code>NOTE:</code> <code>XmGetMenuCursor</code> is obsolete and exists for compatibility with previous releases. Instead of using this function, call <code>XtGetValues</code> for the XmScreen resource <code>XmNmenuCursor</code>.</p>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the display whose menu cursor is to be queried</dl>
<h2>Return</h2>
<p>Returns the cursor ID for the current menu cursor or the value None if a cursor is not yet defined. A cursor will not be defined if the application makes this call before the client has created any menus on the specified display.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmscreen/">XmScreen</a></code>(3).</p>
