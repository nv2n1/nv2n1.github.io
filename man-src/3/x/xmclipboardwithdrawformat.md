---
title: "xmclipboardwithdrawformat(3)"
name: "xmclipboardwithdrawformat"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmclipboardwithdrawformat/"
description: "XmClipboardWithdrawFormat — A clipboard function that indicates that the application no longer wants to supply a data item"
---

<p><code>XmClipboardWithdrawFormat</code> &#8212; A clipboard function that indicates that the application no longer wants to supply a data item</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/CutPaste.h&gt;
int XmClipboardWithdrawFormat (<i>display, window, data_id</i>)
 Display <i>* display</i>;
 Window <i>window</i>;
 long <i>data_id</i>;
(<code>void</code>)</pre>
<h2>Description</h2>
<p><code>XmClipboardWithdrawFormat</code> indicates that the application no longer supplies a data item to the clipboard that the application had previously passed by name.</p>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies a pointer to the <code>Display</code> structure that was returned in a previous call to <code>XOpenDisplay</code> or <code>XtDisplay</code>.</p>
<dt><i>window</i></p>
<dd>Specifies the window ID of a widget that relates the application window to the clipboard. The widget&#8217;s window ID can be obtained through <code>XtWindow</code>. The same application instance should pass the same window ID to each clipboard function it calls.</p>
<dt><i>data_id</i></p>
<dd>Specifies an identifying number assigned to the data item, that uniquely identifies the data item and the format. This was assigned to the item when it was originally passed by <code>XmClipboardCopy</code>.</dl>
<h2>Return</h2>
<dl COMPACT>
<dt><code>XmClipboardSuccess</code></p>
<dd>The function was successful.</p>
<dt><code>XmClipboardLocked</code></p>
<dd>The function failed because the clipboard was locked by another application. The application can continue to call the function again with the same parameters until the lock goes away. This gives the application the opportunity to ask if the user wants to keep trying or to give up on the operation.</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmclipboardcopy/">XmClipboardCopy</a></code>(3) and <code><a href="/docs/linux/man/3-xmclipboardstartcopy/">XmClipboardStartCopy</a></code>(3).</p>
