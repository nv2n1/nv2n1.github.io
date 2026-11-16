---
title: "xmclipboardregisterformat(3)"
name: "xmclipboardregisterformat"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmclipboardregisterformat/"
description: "XmClipboardRegisterFormat — A clipboard function that registers a new format"
---

<p><code>XmClipboardRegisterFormat</code> &#8212; A clipboard function that registers a new format</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/CutPaste.h&gt;
int XmClipboardRegisterFormat (<i>display, format_name, format_length</i>)
 Display <i>* display</i>;
 char <i>* format_name</i>;
 int <i>format_length</i>;
(<code>void</code>)</pre>
<h2>Description</h2>
<p><code>XmClipboardRegisterFormat</code> registers a new format. Each format stored on the clipboard should have a length associated with it; this length must be known to the clipboard routines. Formats are known as targets in the <i>Inter-Client Communication Conventions Manual</i> (ICCCM). All of the formats specified by version 1.1 of the ICCCM conventions are preregistered. Any other format that the application wants to use must either be 8-bit data or be registered via this routine. Failure to register the length of the data results in incompatible applications across platforms having different byte-swapping orders.</p>
<dl COMPACT>
<dt><i>display</i></dt>
<dd>Specifies a pointer to the <code>Display</code> structure that was returned in a previous call to <code>XOpenDisplay</code> or <code>XtDisplay</code>.</dd>
<dt><i>format_name</i></dt>
<dd>Specifies the string name for the new format (target).</dd>
<dt><i>format_length</i></dt>
<dd>Specifies the format length in bits (8, 16, or 32).</dd></dl>
<h2>Return</h2>
<dl COMPACT>
<dt><code>XmClipboardBadFormat</code></dt>
<dd>The <i>format_name</i> must not be NULL, and the <i>format_length</i> must be 8, 16, or 32.</dd>
<dt><code>XmClipboardSuccess</code></dt>
<dd>The function was successful.</dd>
<dt><code>XmClipboardLocked</code></dt>
<dd>The function failed because the clipboard was locked by another application. The application can continue to call the function again with the same parameters until the lock goes away. This gives the application the opportunity to ask if the user wants to keep trying or to give up on the operation.</dd>
<dt><code>XmClipboardFail</code></dt>
<dd>The function failed because the specified format was already registered with a different length from that specified now. If a specified format was already registered with the same length as that specified now, <code>XmClipboardSuccess</code> is returned.</dd></dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmclipboardstartcopy/">XmClipboardStartCopy</a></code>(3).</p>
