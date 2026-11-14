---
title: "xmsetmenucursor(3)"
name: "xmsetmenucursor"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmsetmenucursor/"
description: "XmSetMenuCursor — A function that modifies the menu cursor for a client"
---

<p><code>XmSetMenuCursor</code> &#8212; A function that modifies the menu cursor for a client</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>void XmSetMenuCursor</code>(
<code>Display * display</code>,
<code>Cursor cursorId</code>);</pre>
<h2>Description</h2>
<p><code>XmSetMenuCursor</code> programmatically modifies the menu cursor for a client; after the cursor has been created by the client, this function registers the cursor with the menu system. After calling this function, the specified cursor is displayed whenever this client displays a Motif menu on the indicated display. The client can then specify different cursors on different displays. </p>
<p> This function sets the menu cursor for all screens on the display. <code>XmSetMenuCursor</code> is obsolete and exists for compatibility with previous releases. Instead of using this function, provide initial values or call <code>XtSetValues</code> for the XmScreen resource <code>XmNmenuCursor</code>.</p>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the display to which the cursor is to be associated</p>
<dt><i>cursorId</i></p>
<dd>Specifies the <code>X</code> cursor ID</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmscreen/">XmScreen</a></code>(3).</p>
