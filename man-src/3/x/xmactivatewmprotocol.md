---
title: "xmactivatewmprotocol(3)"
name: "xmactivatewmprotocol"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmactivatewmprotocol/"
description: "XmActivateWMProtocol — A VendorShell convenience interface that activates a protocol"
---

<p><code>XmActivateWMProtocol</code> &#8212; A VendorShell convenience interface that activates a protocol</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Protocols.h&gt;
<code>void XmActivateWMProtocol</code>(
<code>Widget shell</code>,
<code>Atom protocol</code>);</pre>
<h2>Description</h2>
<p><code>XmActivateWMProtocol</code> is a convenience interface. It calls <code>XmActivateProtocol</code> with the property value set to the atom returned by interning <code>WM_PROTOCOLS</code>.</p>
<dl COMPACT>
<dt><i>shell</i></p>
<dd>Specifies the widget with which the protocol property is associated</p>
<dt><i>protocol</i></p>
<dd>Specifies the protocol <code>Atom</code></dl>
<p> For a complete definition of VendorShell and its associated resources, see <code><a href="/docs/linux/man/3-vendorshell/">VendorShell</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-vendorshell/">VendorShell</a></code>(3), <code><a href="/docs/linux/man/3-xmactivateprotocol/">XmActivateProtocol</a></code>(3), <code><a href="/docs/linux/man/3-xminternatom/">XmInternAtom</a></code>(3), and <code><a href="/docs/linux/man/3-xmremovewmprotocols/">XmRemoveWMProtocols</a></code>(3).</p>
