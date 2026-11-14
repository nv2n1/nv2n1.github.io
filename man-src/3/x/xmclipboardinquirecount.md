---
title: "xmclipboardinquirecount(3)"
name: "xmclipboardinquirecount"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmclipboardinquirecount/"
description: "XmClipboardInquireCount — A clipboard function that returns the number of data item formats"
---

<p><code>XmClipboardInquireCount</code> &#8212; A clipboard function that returns the number of data item formats</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/CutPaste.h&gt;
int XmClipboardInquireCount (<i>display, window, count,
 max_format_name_length</i>)
 Display <i>* display</i>;
 Window <i>window</i>;
 int <i>* count</i>;
 unsigned long <i>* max_format_name_length</i>;
(<code>void</code>)</pre>
<h2>Description</h2>
<p><code>XmClipboardInquireCount</code> returns the number of data item formats available for the data item in the clipboard. This function also returns the maximum name-length for all formats in which the data item is stored.</p>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies a pointer to the <code>Display</code> structure that was returned in a previous call to <code>XOpenDisplay</code> or <code>XtDisplay</code>.</p>
<dt><i>window</i></p>
<dd>Specifies the window ID of a widget that relates the application window to the clipboard. The widget&#8217;s window ID can be obtained through <code>XtWindow</code>. The same application instance should pass the same window ID to each of the clipboard functions that it calls.</p>
<dt><i>count</i></p>
<dd>Returns the number of data item formats available for the data item in the clipboard. If no formats are available, this argument equals 0 (zero). The count includes the formats that were passed by name.</p>
<dt><i>max_format_name_length</i></p>
<dd>Specifies the maximum length of all format names for the data item in the clipboard.</dl>
<h2>Return</h2>
<dl COMPACT>
<dt><code>XmClipboardSuccess</code></p>
<dd>The function was successful.</p>
<dt><code>XmClipboardLocked</code></p>
<dd>The function failed because the clipboard was locked by another application. The application can continue to call the function again with the same parameters until the lock goes away. This gives the application the opportunity to ask if the user wants to keep trying or to give up on the operation.</p>
<dt><code>XmClipboardNoData</code></p>
<dd>The function could not find data on the clipboard corresponding to the format requested. This could occur because the clipboard is empty; there is data on the clipboard, but not in the requested format; or the data in the requested format was passed by name and is no longer available.</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmclipboardstartcopy/">XmClipboardStartCopy</a></code>(3).</p>
