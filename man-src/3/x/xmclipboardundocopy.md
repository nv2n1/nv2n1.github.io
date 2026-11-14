---
title: "xmclipboardundocopy(3)"
name: "xmclipboardundocopy"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmclipboardundocopy/"
description: "XmClipboardUndoCopy — A clipboard function that deletes the last item placed on the clipboard"
---

<p><code>XmClipboardUndoCopy</code> &#8212; A clipboard function that deletes the last item placed on the clipboard</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/CutPaste.h&gt;
int XmClipboardUndoCopy (<i>display, window</i>)
 Display <i>* display</i>;
 Window <i>window</i>;
(<code>void</code>)</pre>
<h2>Description</h2>
<p><code>XmClipboardUndoCopy</code> deletes the last item placed on the clipboard if the item was placed there by an application with the passed <i>display</i> and <i>window</i> arguments. Any data item deleted from the clipboard by the original call to <code>XmClipboardCopy</code> is restored. If the <i>display</i> or <i>window</i> IDs do not match the last copied item, no action is taken, and this function has no effect.</p>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies a pointer to the <code>Display</code> structure that was returned in a previous call to <code>XOpenDisplay</code> or <code>XtDisplay</code>.</p>
<dt><i>window</i></p>
<dd>Specifies the window ID of a widget that relates the application window to the clipboard. The widget&#8217;s window ID can be obtained through <code>XtWindow</code>. The same application instance should pass the same window ID to each clipboard function it calls.</dl>
<h2>Return</h2>
<dl COMPACT>
<dt><code>XmClipboardSuccess</code></p>
<dd>The function was successful.</p>
<dt><code>XmClipboardLocked</code></p>
<dd>The function failed because the clipboard was locked by another application. The application can continue to call the function again with the same parameters until the lock goes away. This gives the application the opportunity to ask if the user wants to keep trying or to give up on the operation.</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmclipboardlock/">XmClipboardLock</a></code>(3) and <code><a href="/docs/linux/man/3-xmclipboardstartcopy/">XmClipboardStartCopy</a></code>(3).</p>
