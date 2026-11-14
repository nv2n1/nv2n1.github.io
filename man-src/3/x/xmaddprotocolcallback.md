---
title: "xmaddprotocolcallback(3)"
name: "xmaddprotocolcallback"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmaddprotocolcallback/"
description: "XmAddProtocolCallback — A VendorShell function that adds client callbacks for a protocol"
---

<p><code>XmAddProtocolCallback</code> &#8212; A VendorShell function that adds client callbacks for a protocol</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Protocols.h&gt;
<code>void XmAddProtocolCallback</code>(
<code>Widget shell</code>,
<code>Atom property</code>,
<code>Atom protocol</code>,
<code>XtCallbackProc callback</code>,
<code>XtPointer closure</code>);</pre>
<h2>Description</h2>
<p><code>XmAddProtocolCallback</code> adds client callbacks for a protocol. It checks if the protocol is registered, and if it is not, calls <code>XmAddProtocols</code>. It then adds the callback to the internal list. These callbacks are called when the corresponding client message is received. </p>
<p> <code>XmAddWMProtocolCallback</code> is a convenience interface. It calls <code>XmAddProtocolCallback</code> with the property value set to the atom returned by interning <code>WM_PROTOCOLS</code>.</p>
<dl COMPACT>
<dt><i>shell</i></p>
<dd>Specifies the widget with which the protocol property is associated</p>
<dt><i>property</i></p>
<dd>Specifies the protocol property</p>
<dt><i>protocol</i></p>
<dd>Specifies the protocol <code>Atom</code></p>
<dt><i>callback</i></p>
<dd>Specifies the procedure to call when a protocol message is received</p>
<dt><i>closure</i></p>
<dd>Specifies the client data to be passed to the callback when it is invoked</dl>
<p> For a complete definition of VendorShell and its associated resources, see <code><a href="/docs/linux/man/3-vendorshell/">VendorShell</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-vendorshell/">VendorShell</a></code>(3), <code><a href="/docs/linux/man/3-xmaddwmprotocolcallback/">XmAddWMProtocolCallback</a></code>(3), <code><a href="/docs/linux/man/3-xminternatom/">XmInternAtom</a></code>(3), and <code><a href="/docs/linux/man/3-xmremoveprotocolcallback/">XmRemoveProtocolCallback</a></code>(3).</p>
