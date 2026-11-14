---
title: "xmclipboardinquirependingitems(3)"
name: "xmclipboardinquirependingitems"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmclipboardinquirependingitems/"
description: "XmClipboardInquirePendingItems — A clipboard function that returns a list of data ID/private ID pairs"
---

<p><code>XmClipboardInquirePendingItems</code> &#8212; A clipboard function that returns a list of data ID/private ID pairs</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/CutPaste.h&gt;
int XmClipboardInquirePendingItems (<i>display, window, format_name, item_list, count</i>)
 Display <i>* display</i>;
 Window <i>window</i>;
 char <i>* format_name</i>;
 XmClipboardPendingList <i>* item_list</i>;
 unsigned long <i>* count</i>;
(<code>void</code>)</pre>
<h2>Description</h2>
<p><code>XmClipboardInquirePendingItems</code> returns a list of data ID/private ID pairs for the specified format name. A data item is considered pending if the application originally passed it by name, the application has not yet copied the data, and the item has not been deleted from the clipboard. The application is responsible for freeing the memory provided by this function to store the list. To free the memory, call <code>XtFree</code>. </p>
<p> This function is used by an application when exiting, to determine if the data that is passed by name should be sent to the clipboard.</p>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies a pointer to the <code>Display</code> structure that was returned in a previous call to <code>XOpenDisplay</code> or <code>XtDisplay</code>.</p>
<dt><i>window</i></p>
<dd>Specifies the window ID of a widget that relates the application window to the clipboard. The widget&#8217;s window ID can be obtained through <code>XtWindow</code>. The same application instance should pass the same window ID to each of the clipboard functions that it calls.</p>
<dt><i>format_name</i></p>
<dd>Specifies a string that contains the name of the format for which the list of data ID/private ID pairs is to be obtained.</p>
<dt><i>item_list</i></p>
<dd>Specifies the address of the array of data ID/private ID pairs for the specified format name. This argument is a type <code>XmClipboardPendingList</code>. The application is responsible for freeing the memory provided by this function for storing the list.</p>
<dt><i>count</i></p>
<dd>Specifies the number of items returned in the list. If there is no data for the specified format name, or if there is no item on the clipboard, this argument equals 0 (zero).</dl>
<h2>Return</h2>
<dl COMPACT>
<dt><code>XmClipboardSuccess</code></p>
<dd>The function was successful.</p>
<dt><code>XmClipboardLocked</code></p>
<dd>The function failed because the clipboard was locked by another application. The application can continue to call the function again with the same parameters until the lock goes away. This gives the application the opportunity to ask if the user wants to keep trying or to give up on the operation.</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmclipboardstartcopy/">XmClipboardStartCopy</a></code>(3).</p>
