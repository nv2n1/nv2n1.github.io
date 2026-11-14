---
title: "xmactivateprotocol(3)"
name: "xmactivateprotocol"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmactivateprotocol/"
description: "XmActivateProtocol — A VendorShell function that activates a protocol"
---

<p><code>XmActivateProtocol</code> &#8212; A VendorShell function that activates a protocol</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Protocols.h&gt;
<code>void XmActivateProtocol</code>(
<code>Widget shell</code>,
<code>Atom property</code>,
<code>Atom protocol</code>);</pre>
<h2>Description</h2>
<p><code>XmActivateProtocol</code> activates a protocol. It updates the handlers and the <i>property</i> if the <i>shell</i> is realized. It is sometimes useful to allow a protocol&#8217;s state information (callback lists, and so on) to persist, even though the client may choose to temporarily resign from the interaction. This is supported by allowing a <i>protocol</i> to be in one of two states: active or inactive. If the <i>protocol</i> is active and the <i>shell</i> is realized, the <i>property</i> contains the <i>protocol</i> <code>Atom</code>. If the <i>protocol</i> is inactive, the <code>Atom</code> is not present in the <i>property</i>. </p>
<p> <code>XmActivateWMProtocol</code> is a convenience interface. It calls <code>XmActivateProtocol</code> with the property value set to the atom returned by interning <code>WM_PROTOCOLS</code>.</p>
<dl COMPACT>
<dt><i>shell</i></p>
<dd>Specifies the widget with which the protocol property is associated</p>
<dt><i>property</i></p>
<dd>Specifies the protocol property</p>
<dt><i>protocol</i></p>
<dd>Specifies the protocol <code>Atom</code></dl>
<p> For a complete definition of VendorShell and its associated resources, see <code><a href="/docs/linux/man/3-vendorshell/">VendorShell</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-vendorshell/">VendorShell</a></code>(3), <code><a href="/docs/linux/man/3-xmactivatewmprotocol/">XmActivateWMProtocol</a></code>(3), <code><a href="/docs/linux/man/3-xmremoveprotocols/">XmRemoveProtocols</a></code>(3) and <code><a href="/docs/linux/man/3-xminternatom/">XmInternAtom</a></code>(3).</p>
