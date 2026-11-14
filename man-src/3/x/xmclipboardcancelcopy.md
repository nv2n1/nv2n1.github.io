---
title: "xmclipboardcancelcopy(3)"
name: "xmclipboardcancelcopy"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmclipboardcancelcopy/"
description: "XmClipboardCancelCopy — A clipboard function that cancels a copy to the clipboard"
---

<p><code>XmClipboardCancelCopy</code> &#8212; A clipboard function that cancels a copy to the clipboard</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/CutPaste.h&gt;
int XmClipboardCancelCopy (<i>display, window, item_id</i>)
 Display <i>* display</i>;
 Window <i>window</i>;
 long <i>item_id</i>;
(<code>void</code>)</pre>
<h2>Description</h2>
<p><code>XmClipboardCancelCopy</code> cancels the copy to clipboard that is in progress and frees up temporary storage. When a copy is to be performed, <code>XmClipboardStartCopy</code> allocates temporary storage for the clipboard data. <code>XmClipboardCopy</code> copies the appropriate data into the the temporary storage. <code>XmClipboardEndCopy</code> copies the data to the clipboard structure and frees up the temporary storage structures. If <code>XmClipboardCancelCopy</code> is called, the <code>XmClipboardEndCopy</code> function does not have to be called. A call to <code>XmClipboardCancelCopy</code> is valid only after a call to <code>XmClipboardStartCopy</code>.</p>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies a pointer to the <code>Display</code> structure that was returned in a previous call to <code>XOpenDisplay</code> or <code>XtDisplay</code>.</p>
<dt><i>window</i></p>
<dd>Specifies a widget&#8217;s window ID that relates the application window to the clipboard. The widget&#8217;s window ID can be obtained through <code>XtWindow</code>. The same application instance should pass the same window ID to each of the clipboard functions that it calls.</p>
<dt><i>item_id</i></p>
<dd>Specifies the number assigned to this data item. This number was returned by a previous call to <code>XmClipboardStartCopy</code>.</dl>
<h2>Return</h2>
<dl COMPACT>
<dt><code>XmClipboardSuccess</code></p>
<dd>The function was successful.</p>
<dt><code>XmClipboardLocked</code></p>
<dd>The function failed because the clipboard was locked by another application. The application can continue to call the function again with the same parameters until the lock goes away. This gives the application the opportunity to ask if the user wants to keep trying or to give up on the operation.</p>
<dt><code>XmClipboardFail</code></p>
<dd>The function failed because <code>XmClipboardStartCopy</code> was not called or because the data item contains too many formats.</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmclipboardcopy/">XmClipboardCopy</a></code>(3), <code><a href="/docs/linux/man/3-xmclipboardendcopy/">XmClipboardEndCopy</a></code>(3), and <code><a href="/docs/linux/man/3-xmclipboardstartcopy/">XmClipboardStartCopy</a></code>(3).</p>
