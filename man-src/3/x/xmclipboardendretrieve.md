---
title: "xmclipboardendretrieve(3)"
name: "xmclipboardendretrieve"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmclipboardendretrieve/"
description: "XmClipboardEndRetrieve — A clipboard function that completes retrieval of data from the clipboard"
---

<p><code>XmClipboardEndRetrieve</code> &#8212; A clipboard function that completes retrieval of data from the clipboard</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/CutPaste.h&gt;
int XmClipboardEndRetrieve (<i>display, window</i>)
 Display <i>* display</i>;
 Window <i>window</i>;
(<code>void</code>)</pre>
<h2>Description</h2>
<p><code>XmClipboardEndRetrieve</code> suspends copying data incrementally from the clipboard. It tells the clipboard routines that the application is through copying an item from the clipboard. Until this function is called, data items can be retrieved incrementally from the clipboard with <code>XmClipboardRetrieve</code>. The act of copying data is started with the <code>XmClipboardStartRetrieve</code> function.</p>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies a pointer to the <code>Display</code> structure that was returned in a previous call to <code>XOpenDisplay</code> or <code>XtDisplay</code>.</p>
<dt><i>window</i></p>
<dd>Specifies the window ID of a widget that relates the application window to the clipboard. The widget&#8217;s window ID can be obtained with <code>XtWindow</code>. The same application instance should pass the same window ID to each of the clipboard functions that it calls.</dl>
<h2>Return</h2>
<dl COMPACT>
<dt><code>XmClipboardSuccess</code></p>
<dd>The function was successful.</p>
<dt><code>XmClipboardLocked</code></p>
<dd>The function failed because the clipboard was locked by another application. The application can continue to call the function again with the same parameters until the lock goes away. This gives the application the opportunity to ask if the user wants to keep trying or to give up on the operation.</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmclipboardretrieve/">XmClipboardRetrieve</a></code>(3), <code><a href="/docs/linux/man/3-xmclipboardstartcopy/">XmClipboardStartCopy</a></code>(3), and <code><a href="/docs/linux/man/3-xmclipboardstartretrieve/">XmClipboardStartRetrieve</a></code>(3).</p>
