---
title: "xmdeactivateprotocol(3)"
name: "xmdeactivateprotocol"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmdeactivateprotocol/"
description: "XmDeactivateProtocol — A VendorShell function that deactivates a protocol without removing it"
---

<p><code>XmDeactivateProtocol</code> &#8212; A VendorShell function that deactivates a protocol without removing it</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
#include &lt;Xm/Protocols.h&gt;
<code>void XmDeactivateProtocol</code>(
<code>Widget shell</code>,
<code>Atom property</code>,
<code>Atom protocol</code>);</pre>
<h2>Description</h2>
<p><code>XmDeactivateProtocol</code> deactivates a protocol without removing it. It updates the handlers and the <i>property</i> if the <i>shell</i> is realized. It is sometimes useful to allow a protocol&#8217;s state information (callback lists, and so on) to persist, even though the client may choose to temporarily resign from the interaction. The main use of this capability is to gray/ungray <code>f.send_msg</code> entries in the MWM system menu. To support this capability, <i>protocol</i> is allowed to be in one of two states: active or inactive. If <i>protocol</i> is active and <i>shell</i> is realized, <i>property</i> contains the <i>protocol</i> <code>Atom</code>. If <i>protocol</i> is inactive, <code>Atom</code> is not present in the <i>property</i>. </p>
<p> <code>XmDeactivateWMProtocol</code> is a convenience interface. It calls <code>XmDeactivateProtocol</code> with the property value set to the atom returned by interning <code>WM_PROTOCOLS</code>.</p>
<dl COMPACT>
<dt><i>shell</i></p>
<dd>Specifies the widget with which the protocol property is associated</p>
<dt><i>property</i></p>
<dd>Specifies the protocol property</p>
<dt><i>protocol</i></p>
<dd>Specifies the protocol atom</dl>
<p> For a complete definition of VendorShell and its associated resources, see <code><a href="/docs/linux/man/3-vendorshell/">VendorShell</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/1-mwm/">mwm</a></code>(1), <code><a href="/docs/linux/man/3-vendorshell/">VendorShell</a></code>(3), <code><a href="/docs/linux/man/3-xmactivateprotocol/">XmActivateProtocol</a></code>(3), <code><a href="/docs/linux/man/3-xmdeactivatewmprotocol/">XmDeactivateWMProtocol</a></code>(3), and <code><a href="/docs/linux/man/3-xminternatom/">XmInternAtom</a></code>(3).</p>
