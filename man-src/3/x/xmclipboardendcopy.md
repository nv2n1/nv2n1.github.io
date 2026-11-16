---
title: "xmclipboardendcopy(3)"
name: "xmclipboardendcopy"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmclipboardendcopy/"
description: "XmClipboardEndCopy — A clipboard function that completes the copying of data to the clipboard"
---

<p><code>XmClipboardEndCopy</code> &#8212; A clipboard function that completes the copying of data to the clipboard</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/CutPaste.h&gt;
int XmClipboardEndCopy (<i>display, window, item_id</i>)
 Display <i>* display</i>;
 Window <i>window</i>;
 long <i>item_id</i>;
(<code>void</code>)</pre>
<h2>Description</h2>
<p><code>XmClipboardEndCopy</code> locks the clipboard from access by other applications, places data in the clipboard data structure, and unlocks the clipboard. Data items copied to the clipboard by <code>XmClipboardCopy</code> are not actually entered in the clipboard data structure until the call to <code>XmClipboardEndCopy</code>. </p>
<p> This function also frees up temporary storage that was allocated by <code>XmClipboardStartCopy</code>, which must be called before <code>XmClipboardEndCopy</code>. The latter function should not be called if <code>XmClipboardCancelCopy</code> has been called.</p>
<dl COMPACT>
<dt><i>display</i></dt>
<dd>Specifies a pointer to the <code>Display</code> structure that was returned in a previous call to <code>XOpenDisplay</code> or <code>XtDisplay</code>.</dd>
<dt><i>window</i></dt>
<dd>Specifies the window ID of a widget that relates the application window to the clipboard. The widget&#8217;s window ID can be obtained through <code>XtWindow</code>. The same application instance should pass the same window ID to each clipboard function it calls.</dd>
<dt><i>item_id</i></dt>
<dd>Specifies the number assigned to this data item, which was returned by a previous call to <code>XmClipboardStartCopy</code>.</dd></dl>
<h2>Return</h2>
<dl COMPACT>
<dt><code>XmClipboardSuccess</code></dt>
<dd>The function was successful.</dd>
<dt><code>XmClipboardLocked</code></dt>
<dd>The function failed because the clipboard was locked by another application. The application can continue to call the function again with the same parameters until the lock goes away. This gives the application the opportunity to ask if the user wants to keep trying or to give up on the operation.</dd>
<dt><code>XmClipboardFail</code></dt>
<dd>The function failed because <code>XmClipboardStartCopy</code> was not called.</dd></dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmclipboardcancelcopy/">XmClipboardCancelCopy</a></code>(3), <code><a href="/docs/linux/man/3-xmclipboardcopy/">XmClipboardCopy</a></code>(3) and <code><a href="/docs/linux/man/3-xmclipboardstartcopy/">XmClipboardStartCopy</a></code>(3).</p>
