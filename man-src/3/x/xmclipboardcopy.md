---
title: "xmclipboardcopy(3)"
name: "xmclipboardcopy"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmclipboardcopy/"
description: "XmClipboardCopy — A clipboard function that copies a data item to temporary storage for later copying to clipboard"
---

<p><code>XmClipboardCopy</code> &#8212; A clipboard function that copies a data item to temporary storage for later copying to clipboard</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/CutPaste.h&gt;
int XmClipboardCopy (<i>display, window, item_id, format_name,
 buffer, length, private_id, data_id</i>)
 Display <i>* display</i>;
 Window <i>window</i>;
 long <i>item_id</i>;
 char <i>* format_name</i>;
 XtPointer <i>buffer</i>;
 unsigned long <i>length</i>;
 long <i>private_id</i>;
 long <i>* data_id</i>;
(<code>void</code>)</pre>
<h2>Description</h2>
<p><code>XmClipboardCopy</code> copies a data item to temporary storage. The data item is moved from temporary storage to the clipboard data structure when a call to <code>XmClipboardEndCopy</code> is made. Additional calls to <code>XmClipboardCopy</code> before a call to <code>XmClipboardEndCopy</code> add additional data item formats to the same data item or append data to an existing format. Formats are described in the <i>Inter-Client Communication Conventions Manual</i> (ICCCM) as targets. </p>
<p> <code>NOTE:</code> Do not call <code>XmClipboardCopy</code> before a call to <code>XmClipboardStartCopy</code> has been made. The latter function allocates temporary storage required by <code>XmClipboardCopy</code>. </p>
<p> If the <i>buffer</i> argument is NULL, the data is considered to be passed by name. When data that has been passed by name is later requested by another application, the application that owns the data receives a callback with a request for the data. The application that owns the data must then transfer the data to the clipboard with the <code>XmClipboardCopyByName</code> function. When a data item that was passed by name is deleted from the clipboard, the application that owns the data receives a callback stating that the data is no longer needed. </p>
<p> For information on the callback function, see the callback argument description for <code>XmClipboardStartCopy</code>.</p>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies a pointer to the <code>Display</code> structure that was returned in a previous call to <code>XOpenDisplay</code> or <code>XtDisplay</code>.</p>
<dt><i>window</i></p>
<dd>Specifies the window ID of a widget that relates the application window to the clipboard. The widget&#8217;s window ID can be obtained through <code>XtWindow</code>. The same application instance should pass the same window ID to each of the clipboard functions that it calls.</p>
<dt><i>item_id</i></p>
<dd>Specifies the number assigned to this data item. This number was returned by a previous call to <code>XmClipboardStartCopy</code>.</p>
<dt><i>format_name</i></p>
<dd>Specifies the name of the format in which the data item is stored on the clipboard. The format was known as target in the ICCCM.</p>
<dt><i>buffer</i></p>
<dd>Specifies the buffer from which the clipboard copies the data.</p>
<dt><i>length</i></p>
<dd>Specifies the length, in bytes, of the data being copied to the clipboard.</p>
<dt><i>private_id</i></p>
<dd>Specifies the private data that the application wants to store with the data item.</p>
<dt><i>data_id</i></p>
<dd>Specifies an identifying number assigned to the data item that uniquely identifies the data item and the format. This argument is required only for data that is passed by name.</dl>
<h2>Return</h2>
<dl COMPACT>
<dt><code>XmClipboardSuccess</code></p>
<dd>The function was successful.</p>
<dt><code>XmClipboardLocked</code></p>
<dd>The function failed because the clipboard was locked by another application. The application can continue to call the function again with the same parameters until the lock goes away. This gives the application the opportunity to ask if the user wants to keep trying or to give up on the operation.</p>
<dt><code>XmClipboardFail</code></p>
<dd>The function failed because <code>XmClipboardStartCopy</code> was not called or because the data item contains too many formats.</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmclipboardcopybyname/">XmClipboardCopyByName</a></code>(3), <code><a href="/docs/linux/man/3-xmclipboardendcopy/">XmClipboardEndCopy</a></code>(3), and <code><a href="/docs/linux/man/3-xmclipboardstartcopy/">XmClipboardStartCopy</a></code>(3).</p>
