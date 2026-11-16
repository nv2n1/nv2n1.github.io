---
title: "xmremovewmprotocolcallback(3)"
name: "xmremovewmprotocolcallback"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmremovewmprotocolcallback/"
description: "XmRemoveWMProtocolCallback — A VendorShell convenience interface that removes a callback from the internal list"
---

<p><code>XmRemoveWMProtocolCallback</code> &#8212; A VendorShell convenience interface that removes a callback from the internal list</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
#include &lt;Xm/Protocols.h&gt;
<code>void XmRemoveWMProtocolCallback</code>(
<code>Widget shell</code>,
<code>Atom protocol</code>,
<code>XtCallbackProc callback</code>,
<code>XtPointer closure</code>);</pre>
<h2>Description</h2>
<p><code>XmRemoveWMProtocolCallback</code> is a convenience interface. It calls <code>XmRemoveProtocolCallback</code> with the property value set to the atom returned by interning <code>WM_PROTOCOLS</code>.</p>
<dl COMPACT>
<dt><i>shell</i></dt>
<dd>Specifies the widget with which the protocol property is associated</dd>
<dt><i>protocol</i></dt>
<dd>Specifies the protocol atom</dd>
<dt><i>callback</i></dt>
<dd>Specifies the procedure to call when a protocol message is received</dd>
<dt><i>closure</i></dt>
<dd>Specifies the client data to be passed to the callback when it is invoked</dd></dl>
<p> For a complete definition of VendorShell and its associated resources, see <code><a href="/docs/linux/man/3-vendorshell/">VendorShell</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-vendorshell/">VendorShell</a></code>(3), <code><a href="/docs/linux/man/3-xmaddwmprotocolcallback/">XmAddWMProtocolCallback</a></code>(3), <code><a href="/docs/linux/man/3-xminternatom/">XmInternAtom</a></code>(3), and <code><a href="/docs/linux/man/3-xmremoveprotocolcallback/">XmRemoveProtocolCallback</a></code>(3).</p>
