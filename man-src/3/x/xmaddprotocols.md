---
title: "xmaddprotocols(3)"
name: "xmaddprotocols"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmaddprotocols/"
description: "XmAddProtocols — A VendorShell function that adds the protocols to the protocol manager and allocates the internal tables"
---

<p><code>XmAddProtocols</code> &#8212; A VendorShell function that adds the protocols to the protocol manager and allocates the internal tables</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Protocols.h&gt;
<code>void XmAddProtocols</code>(
<code>Widget shell</code>,
<code>Atom property</code>,
<code>Atom *protocols</code>,
<code>Cardinal num_protocols</code>);</pre>
<h2>Description</h2>
<p><code>XmAddProtocols</code> adds the protocols to the protocol manager and allocates the internal tables. </p>
<p> <code>XmAddWMProtocols</code> is a convenience interface. It calls <code>XmAddProtocols</code> with the property value set to the atom returned by interning <code>WM_PROTOCOLS</code>.</p>
<dl COMPACT>
<dt><i>shell</i></dt>
<dd>Specifies the widget with which the protocol property is associated</dd>
<dt><i>property</i></dt>
<dd>Specifies the protocol property</dd>
<dt><i>protocols</i></dt>
<dd>Specifies the protocol <code>Atoms</code></dd>
<dt><i>num_protocols</i></dt>
<dd>Specifies the number of elements in <i>protocols</i></dd></dl>
<p> For a complete definition of VendorShell and its associated resources, see <code><a href="/docs/linux/man/3-vendorshell/">VendorShell</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-vendorshell/">VendorShell</a></code>(3), <code><a href="/docs/linux/man/3-xmaddwmprotocols/">XmAddWMProtocols</a></code>(3), <code><a href="/docs/linux/man/3-xminternatom/">XmInternAtom</a></code>(3), and <code><a href="/docs/linux/man/3-xmremoveprotocols/">XmRemoveProtocols</a></code>(3).</p>
