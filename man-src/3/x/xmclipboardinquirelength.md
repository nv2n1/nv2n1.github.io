---
title: "xmclipboardinquirelength(3)"
name: "xmclipboardinquirelength"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmclipboardinquirelength/"
description: "XmClipboardInquireLength — A clipboard function that returns the length of the stored data"
---

<p><code>XmClipboardInquireLength</code> &#8212; A clipboard function that returns the length of the stored data</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/CutPaste.h&gt;
int XmClipboardInquireLength (<i>display, window, format_name, length</i>)
 Display <i>* display</i>;
 Window <i>window</i>;
 char <i>* format_name</i>;
 unsigned long <i>* length</i>;
(<code>void</code>)</pre>
<h2>Description</h2>
<p><code>XmClipboardInquireLength</code> returns the length of the data stored under a specified format name for the clipboard data item. If no data is found for the specified format, or if there is no item on the clipboard, this function returns a value of 0 (zero) in the <i>length</i> argument. </p>
<p> Any format passed by name is assumed to have <i>length</i> passed in a call to <code>XmClipboardCopy</code>, even though the data has not yet been transferred to the clipboard in that format.</p>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies a pointer to the <code>Display</code> structure that was returned in a previous call to <code>XOpenDisplay</code> or <code>XtDisplay</code>.</p>
<dt><i>window</i></p>
<dd>Specifies the window ID of a widget that relates the application window to the clipboard. The widget&#8217;s window ID can be obtained through <code>XtWindow</code>. The same application instance should pass the same window ID to each of the clipboard functions that it calls.</p>
<dt><i>format_name</i></p>
<dd>Specifies the name of the format for the data item.</p>
<dt><i>length</i></p>
<dd>Specifies the length of the next data item in the specified format. This argument equals 0 (zero) if no data is found for the specified format, or if there is no item on the clipboard.</dl>
<h2>Return</h2>
<dl COMPACT>
<dt><code>XmClipboardSuccess</code></p>
<dd>The function was successful.</p>
<dt><code>XmClipboardLocked</code></p>
<dd>The function failed because the clipboard was locked by another application. The application can continue to call the function again with the same parameters until the lock goes away. This gives the application the opportunity to ask if the user wants to keep trying or to give up on the operation.</p>
<dt><code>XmClipboardNoData</code></p>
<dd>The function could not find data on the clipboard corresponding to the format requested. This could occur because the clipboard is empty; there is data on the clipboard, but not in the requested format; or the data in the requested format was passed by name and is no longer available.</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmclipboardcopy/">XmClipboardCopy</a></code>(3) and <code><a href="/docs/linux/man/3-xmclipboardstartcopy/">XmClipboardStartCopy</a></code>(3).</p>
