---
title: "xmaddwmprotocols(3)"
name: "xmaddwmprotocols"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmaddwmprotocols/"
description: "XmAddWMProtocols — A VendorShell convenience interface that adds the protocols to the protocol manager and allocates the internal tables"
---

<p><code>XmAddWMProtocols</code> &#8212; A VendorShell convenience interface that adds the protocols to the protocol manager and allocates the internal tables</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Protocols.h&gt;
<code>void XmAddWMProtocols</code>(
<code>Widget shell</code>,
<code>Atom *protocols</code>,
<code>Cardinal num_protocols</code>);</pre>
<h2>Description</h2>
<p><code>XmAddWMProtocols</code> is a convenience interface. It calls <code>XmAddProtocols</code> with the property value set to the atom returned by interning <code>WM_PROTOCOLS</code>.</p>
<dl COMPACT>
<dt><i>shell</i></p>
<dd>Specifies the widget with which the protocol property is associated</p>
<dt><i>protocols</i></p>
<dd>Specifies the protocol <code>Atoms</code></p>
<dt><i>num_protocols</i></p>
<dd>Specifies the number of elements in <i>protocols</i></dl>
<p> For a complete definition of VendorShell and its associated resources, see <code><a href="/docs/linux/man/3-vendorshell/">VendorShell</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-vendorshell/">VendorShell</a></code>(3), <code><a href="/docs/linux/man/3-xmaddprotocols/">XmAddProtocols</a></code>(3), <code><a href="/docs/linux/man/3-xminternatom/">XmInternAtom</a></code>(3), and <code>XmRemoveWMProtocols</code>.</p>
