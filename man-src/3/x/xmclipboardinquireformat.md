---
title: "xmclipboardinquireformat(3)"
name: "xmclipboardinquireformat"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmclipboardinquireformat/"
description: "XmClipboardInquireFormat — A clipboard function that returns a specified format name"
---

<p><code>XmClipboardInquireFormat</code> &#8212; A clipboard function that returns a specified format name</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/CutPaste.h&gt;
int XmClipboardInquireFormat (<i>display, window, index, format_name_buf,
 buffer_len, copied_len</i>)
 Display <i>* display</i>;
 Window <i>window</i>;
 int <i>index</i>;
 XtPointer <i>format_name_buf</i>;
 unsigned long <i>buffer_len</i>;
 unsigned long <i>* copied_len</i>;
(<code>void</code>)</pre>
<h2>Description</h2>
<p><code>XmClipboardInquireFormat</code> returns a specified format name for the data item in the clipboard. If the name must be truncated, the function returns a warning status.</p>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies a pointer to the <code>Display</code> structure that was returned in a previous call to <code>XOpenDisplay</code> or <code>XtDisplay</code>.</p>
<dt><i>window</i></p>
<dd>Specifies the window ID of a widget that relates the application window to the clipboard. The widget&#8217;s window ID can be obtained through <code>XtWindow</code>. The same application instance should pass the same window ID to each of the clipboard functions that it calls.</p>
<dt><i>index</i></p>
<dd>Specifies which of the ordered format names to obtain. If this index is greater than the number of formats for the data item, this function returns a 0 (zero) in the <i>copied_len</i> argument.</p>
<dt><i>format_name_buf</i></p>
<dd>Specifies the buffer that receives the format name.</p>
<dt><i>buffer_len</i></p>
<dd>Specifies the number of bytes in the format name buffer.</p>
<dt><i>copied_len</i></p>
<dd>Specifies the number of bytes in the data item copied to the buffer. If this argument equals 0 (zero), there is no <i>n</i>th format for the data item.</dl>
<h2>Return</h2>
<dl COMPACT>
<dt><code>XmClipboardSuccess</code></p>
<dd>The function was successful.</p>
<dt><code>XmClipboardLocked</code></p>
<dd>The function failed because the clipboard was locked by another application. The application can continue to call the function again with the same parameters until the lock goes away. This gives the application the opportunity to ask if the user wants to keep trying or to give up on the operation.</p>
<dt><code>XmClipboardTruncate</code></p>
<dd>The data returned is truncated because the user did not provide a buffer large enough to hold the data.</p>
<dt><code>XmClipboardNoData</code></p>
<dd>The function could not find data on the clipboard corresponding to the format requested. This could occur because the clipboard is empty; there is data on the clipboard, but not in the requested format; or the data in the requested format was passed by name and is no longer available.</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmclipboardstartcopy/">XmClipboardStartCopy</a></code>(3).</p>
