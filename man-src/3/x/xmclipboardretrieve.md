---
title: "xmclipboardretrieve(3)"
name: "xmclipboardretrieve"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmclipboardretrieve/"
description: "XmClipboardRetrieve — A clipboard function that retrieves a data item from the clipboard"
---

<p><code>XmClipboardRetrieve</code> &#8212; A clipboard function that retrieves a data item from the clipboard</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/CutPaste.h&gt;
int XmClipboardRetrieve (<i>display, window, format_name,
 buffer, length, num_bytes, private_id</i>)
 Display <i>* display</i>;
 Window <i>window</i>;
 char <i>* format_name</i>;
 XtPointer <i>buffer</i>;
 unsigned long <i>length</i>;
 unsigned long <i>* num_bytes</i>;
 long <i>* private_id</i>;
(<code>void</code>)</pre>
<h2>Description</h2>
<p><code>XmClipboardRetrieve</code> retrieves the current data item from clipboard storage. It returns a warning if the clipboard is locked, if there is no data on the clipboard, or if the data needs to be truncated because the buffer length is too short. </p>
<p> Between a call to <code>XmClipboardStartRetrieve</code> and a call to <code>XmClipboardEndRetrieve</code>, multiple calls to <code>XmClipboardRetrieve</code> with the same format name result in data being incrementally copied from the clipboard until the data in that format has all been copied. </p>
<p> The return value <code>XmClipboardTruncate</code> from calls to <code>XmClipboardRetrieve</code> indicates that more data remains to be copied in the given format. It is recommended that any calls to the <code>Inquire</code> functions that the application needs to make to effect the copy from the clipboard be made between the call to <code>XmClipboardStartRetrieve</code> and the first call to <code>XmClipboardRetrieve</code>. This way, the application does not need to call <code>XmClipboardLock</code> and <code>XmClipboardUnlock</code>.</p>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies a pointer to the <code>Display</code> structure that was returned in a previous call to <code>XOpenDisplay</code> or <code>XtDisplay</code>.</p>
<dt><i>window</i></p>
<dd>Specifies the window ID of a widget that relates the application window to the clipboard. The widget&#8217;s window ID can be obtained through <code>XtWindow</code>. The same application instance should pass the same window ID to each of the clipboard functions that it calls.</p>
<dt><i>format_name</i></p>
<dd>Specifies the name of a format in which the data is stored on the clipboard.</p>
<dt><i>buffer</i></p>
<dd>Specifies the buffer to which the application wants the clipboard to copy the data. The function allocates space to hold the data returned into the buffer. The application is responsible for managing this allocated space. The application can recover this allocated space by calling <code>XtFree</code>.</p>
<dt><i>length</i></p>
<dd>Specifies the length of the application buffer.</p>
<dt><i>num_bytes</i></p>
<dd>Specifies the number of bytes of data copied into the application buffer.</p>
<dt><i>private_id</i></p>
<dd>Specifies the private data stored with the data item by the application that placed the data item on the clipboard. If the application did not store private data with the data item, this argument returns 0 (zero).</dl>
<h2>Return</h2>
<dl COMPACT>
<dt><code>XmClipboardSuccess</code></p>
<dd>The function was successful.</p>
<dt><code>XmClipboardLocked</code></p>
<dd>The function failed because the clipboard was locked by another application. The application can continue to call the function again with the same parameters until the lock goes away. This gives the application the opportunity to ask if the user wants to keep trying or to give up on the operation.</p>
<dt><code>XmClipboardTruncate</code></p>
<dd>The data returned is truncated because the user did not provide a buffer large enough to hold the data.</p>
<dt><code>XmClipboardNoData</code></p>
<dd>The function could not find data on the clipboard corresponding to the format requested. This could occur because the clipboard is empty; there is data on the clipboard but not in the requested format; or the data in the requested format was passed by name and is no longer available.</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmclipboardendretrieve/">XmClipboardEndRetrieve</a></code>(3), <code><a href="/docs/linux/man/3-xmclipboardlock/">XmClipboardLock</a></code>(3), <code><a href="/docs/linux/man/3-xmclipboardstartcopy/">XmClipboardStartCopy</a></code>(3), <code><a href="/docs/linux/man/3-xmclipboardstartretrieve/">XmClipboardStartRetrieve</a></code>(3), and <code><a href="/docs/linux/man/3-xmclipboardunlock/">XmClipboardUnlock</a></code>(3).</p>
