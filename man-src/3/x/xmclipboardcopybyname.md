---
title: "xmclipboardcopybyname(3)"
name: "xmclipboardcopybyname"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmclipboardcopybyname/"
description: "XmClipboardCopyByName — A clipboard function that copies a data item passed by name"
---

<p><code>XmClipboardCopyByName</code> &#8212; A clipboard function that copies a data item passed by name</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/CutPaste.h&gt;
int XmClipboardCopyByName (<i>display, window, data_id,
 buffer, length, private_id</i>)
 Display <i>* display</i>;
 Window <i>window</i>;
 long <i>data_id</i>;
 XtPointer <i>buffer</i>;
 unsigned long <i>length</i>;
 long <i>private_id</i>;
(<code>void</code>)</pre>
<h2>Description</h2>
<p><code>XmClipboardCopyByName</code> copies the actual data for a data item that was previously passed by name to the clipboard. Data is considered to be passed by name when a call to <code>XmClipboardCopy</code> is made with a NULL buffer parameter. Additional calls to this function append new data to the existing data.</p>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies a pointer to the <code>Display</code> structure that was returned in a previous call to <code>XOpenDisplay</code> or <code>XtDisplay</code>.</p>
<dt><i>window</i></p>
<dd>Specifies the window ID of a widget that relates the application window to the clipboard. The widget&#8217;s window ID can be obtained through <code>XtWindow</code>. The same application instance should pass the same window ID to each clipboard function it calls.</p>
<dt><i>data_id</i></p>
<dd>Specifies an identifying number assigned to the data item that uniquely identifies the data item and the format. This number was assigned by <code>XmClipboardCopy</code> to the data item.</p>
<dt><i>buffer</i></p>
<dd>Specifies the buffer from which the clipboard copies the data.</p>
<dt><i>length</i></p>
<dd>Specifies the number of bytes in the data item.</p>
<dt><i>private_id</i></p>
<dd>Specifies the private data that the application wants to store with the data item.</dl>
<h2>Return</h2>
<dl COMPACT>
<dt><code>XmClipboardSuccess</code></p>
<dd>The function was successful.</p>
<dt><code>XmClipboardLocked</code></p>
<dd>The function failed because the clipboard was locked by another application. The application can continue to call the function again with the same parameters until the lock goes away. This gives the application the opportunity to ask if the user wants to keep trying or to give up on the operation.</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmclipboardcopy/">XmClipboardCopy</a></code>(3), <code><a href="/docs/linux/man/3-xmclipboardlock/">XmClipboardLock</a></code>(3), <code><a href="/docs/linux/man/3-xmclipboardstartcopy/">XmClipboardStartCopy</a></code>(3), and <code><a href="/docs/linux/man/3-xmclipboardunlock/">XmClipboardUnlock</a></code>(3).</p>
