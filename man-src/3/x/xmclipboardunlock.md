---
title: "xmclipboardunlock(3)"
name: "xmclipboardunlock"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmclipboardunlock/"
description: "XmClipboardUnlock — A clipboard function that unlocks the clipboard"
---

<p><code>XmClipboardUnlock</code> &#8212; A clipboard function that unlocks the clipboard</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/CutPaste.h&gt;
int XmClipboardUnlock (<i>display, window, remove_all_locks</i>)
 Display <i>* display</i>;
 Window <i>window</i>;
 Boolean <i>remove_all_locks</i>;
(<code>void</code>)</pre>
<h2>Description</h2>
<p><code>XmClipboardUnlock</code> unlocks the clipboard, enabling it to be accessed by other applications. </p>
<p> If multiple calls to <code>XmClipboardLock</code> have occurred, the same number of calls to <code>XmClipboardUnlock</code> is necessary to unlock the clipboard, unless <i>remove_all_locks</i> is set to True.</p>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies a pointer to the <code>Display</code> structure that was returned in a previous call to <code>XOpenDisplay</code> or <code>XtDisplay</code>.</p>
<dt><i>window</i></p>
<dd>Specifies the window ID of a widget that relates the application window to the clipboard. The widget&#8217;s window ID can be obtained through <code>XtWindow</code>. The same application instance should pass the same window ID to each of the clipboard functions that it calls.</p>
<dt><i>remove_all_locks</i></p>
<dd>When True, indicates that all nested locks should be removed. When False, indicates that only one level of lock should be removed.</dl>
<h2>Return</h2>
<dl COMPACT>
<dt><code>XmClipboardSuccess</code></p>
<dd>The function was successful.</p>
<dt><code>XmClipboardFail</code></p>
<dd>The function failed because the clipboard was not locked or was locked by another application.</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmclipboardcancelcopy/">XmClipboardCancelCopy</a></code>(3), <code><a href="/docs/linux/man/3-xmclipboardcopy/">XmClipboardCopy</a></code>(3), <code><a href="/docs/linux/man/3-xmclipboardendcopy/">XmClipboardEndCopy</a></code>(3), <code><a href="/docs/linux/man/3-xmclipboardendretrieve/">XmClipboardEndRetrieve</a></code>(3), <code><a href="/docs/linux/man/3-xmclipboardinquirecount/">XmClipboardInquireCount</a></code>(3), <code><a href="/docs/linux/man/3-xmclipboardinquireformat/">XmClipboardInquireFormat</a></code>(3), <code><a href="/docs/linux/man/3-xmclipboardinquirelength/">XmClipboardInquireLength</a></code>(3), <code><a href="/docs/linux/man/3-xmclipboardinquirependingitems/">XmClipboardInquirePendingItems</a></code>(3), <code><a href="/docs/linux/man/3-xmclipboardlock/">XmClipboardLock</a></code>(3), <code><a href="/docs/linux/man/3-xmclipboardregisterformat/">XmClipboardRegisterFormat</a></code>(3), <code><a href="/docs/linux/man/3-xmclipboardretrieve/">XmClipboardRetrieve</a></code>(3), <code><a href="/docs/linux/man/3-xmclipboardstartcopy/">XmClipboardStartCopy</a></code>(3), <code><a href="/docs/linux/man/3-xmclipboardstartretrieve/">XmClipboardStartRetrieve</a></code>(3), <code><a href="/docs/linux/man/3-xmclipboardundocopy/">XmClipboardUndoCopy</a></code>(3), and <code><a href="/docs/linux/man/3-xmclipboardwithdrawformat/">XmClipboardWithdrawFormat</a></code>(3).</p>
