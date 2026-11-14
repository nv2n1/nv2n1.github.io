---
title: "xmclipboardstartretrieve(3)"
name: "xmclipboardstartretrieve"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmclipboardstartretrieve/"
description: "XmClipboardStartRetrieve — A clipboard function that prepares to retrieve data from the clipboard"
---

<p><code>XmClipboardStartRetrieve</code> &#8212; A clipboard function that prepares to retrieve data from the clipboard</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/CutPaste.h&gt;
int XmClipboardStartRetrieve (<i>display, window, timestamp</i>)
 Display <i>* display</i>;
 Window <i>window</i>;
 Time <i>timestamp</i>;
(<code>void</code>)</pre>
<h2>Description</h2>
<p><code>XmClipboardStartRetrieve</code> tells the clipboard routines that the application is ready to start copying an item from the clipboard. The clipboard is locked by this routine and stays locked until <code>XmClipboardEndRetrieve</code> is called. Between a call to <code>XmClipboardStartRetrieve</code> and a call to <code>XmClipboardEndRetrieve</code>, multiple calls to <code>XmClipboardRetrieve</code> with the same format name result in data being incrementally copied from the clipboard until the data in that format has all been retrieved. </p>
<p> A return value of <code>XmClipboardTruncate</code> from calls to <code>XmClipboardRetrieve</code> indicates that more data remains to be copied in the given format. It is recommended that any calls to the <code>Inquire</code> functions that the application needs to make to complete the copy from the clipboard be made between the call to <code>XmClipboardStartRetrieve</code> and the first call to <code>XmClipboardRetrieve</code>. This way, the application does not need to call <code>XmClipboardLock</code> and <code>XmClipboardUnlock</code>.</p>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies a pointer to the <code>Display</code> structure that was returned in a previous call to <code>XOpenDisplay</code> or <code>XtDisplay</code>.</p>
<dt><i>window</i></p>
<dd>Specifies the window ID of a widget that relates the application window to the clipboard. The widget&#8217;s window ID can be obtained through <code>XtWindow</code>. The same application instance should pass the same window ID to each of the clipboard functions that it calls.</p>
<dt><i>timestamp</i></p>
<dd>Specifies the time of the event that triggered the copy. A valid timestamp must be supplied; it is not sufficient to use <code>CurrentTime</code>.</dl>
<h2>Return</h2>
<dl COMPACT>
<dt><code>XmClipboardSuccess</code></p>
<dd>The function is successful.</p>
<dt><code>XmClipboardLocked</code></p>
<dd>The function failed because the clipboard was locked by another application. The application can continue to call the function again with the same parameters until the lock goes away. This gives the application the opportunity to ask if the user wants to keep trying or to give up on the operation.</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmclipboardendretrieve/">XmClipboardEndRetrieve</a></code>(3), <code><a href="/docs/linux/man/3-xmclipboardinquirecount/">XmClipboardInquireCount</a></code>(3), <code><a href="/docs/linux/man/3-xmclipboardinquireformat/">XmClipboardInquireFormat</a></code>(3), <code><a href="/docs/linux/man/3-xmclipboardinquirelength/">XmClipboardInquireLength</a></code>(3), <code><a href="/docs/linux/man/3-xmclipboardinquirependingitems/">XmClipboardInquirePendingItems</a></code>(3), <code><a href="/docs/linux/man/3-xmclipboardlock/">XmClipboardLock</a></code>(3), <code><a href="/docs/linux/man/3-xmclipboardretrieve/">XmClipboardRetrieve</a></code>(3), <code><a href="/docs/linux/man/3-xmclipboardstartcopy/">XmClipboardStartCopy</a></code>(3), and <code><a href="/docs/linux/man/3-xmclipboardunlock/">XmClipboardUnlock</a></code>(3).</p>
