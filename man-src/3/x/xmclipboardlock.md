---
title: "xmclipboardlock(3)"
name: "xmclipboardlock"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmclipboardlock/"
description: "XmClipboardLock — A clipboard function that locks the clipboard"
---

<p><code>XmClipboardLock</code> &#8212; A clipboard function that locks the clipboard</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/CutPaste.h&gt;
int XmClipboardLock (<i>display, window</i>)
 Display <i>* display</i>;
 Window <i>window</i>;
(<code>void</code>)</pre>
<h2>Description</h2>
<p><code>XmClipboardLock</code> locks the clipboard from access by another application until <code>XmClipboardUnlock</code> is called. All clipboard functions lock and unlock the clipboard to prevent simultaneous access. This function allows the application to keep the clipboard data from changing between calls to <code>Inquire</code> and other clipboard functions. The application does not need to lock the clipboard between calls to <code>XmClipboardStartCopy</code> and <code>XmClipboardEndCopy</code> or to <code>XmClipboardStartRetrieve</code> and <code>XmClipboardEndRetrieve</code>. </p>
<p> If the clipboard is already locked by another application, <code>XmClipboardLock</code> returns an error status. Multiple calls to this function by the same application increase the lock level.</p>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies a pointer to the <code>Display</code> structure that was returned in a previous call to <code>XOpenDisplay</code> or <code>XtDisplay</code>.</p>
<dt><i>window</i></p>
<dd>Specifies the window ID of a widget that relates the application window to the clipboard. The widget&#8217;s window ID can be obtained through <code>XtWindow</code>. The same application instance should pass the same window ID to each of the clipboard functions that it calls.</dl>
<h2>Return</h2>
<dl COMPACT>
<dt><code>XmClipboardSuccess</code></p>
<dd>The function was successful.</p>
<dt><code>XmClipboardLocked</code></p>
<dd>The function failed because the clipboard was locked by another application. The application can continue to call the function again with the same parameters until the lock goes away. This gives the application the opportunity to ask if the user wants to keep trying or to give up on the operation.</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmclipboardendcopy/">XmClipboardEndCopy</a></code>(3), <code><a href="/docs/linux/man/3-xmclipboardendretrieve/">XmClipboardEndRetrieve</a></code>(3), <code><a href="/docs/linux/man/3-xmclipboardstartcopy/">XmClipboardStartCopy</a></code>(3), <code><a href="/docs/linux/man/3-xmclipboardstartretrieve/">XmClipboardStartRetrieve</a></code>(3), and <code><a href="/docs/linux/man/3-xmclipboardunlock/">XmClipboardUnlock</a></code>(3).</p>
