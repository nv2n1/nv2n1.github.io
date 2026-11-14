---
title: "xmsetwmprotocolhooks(3)"
name: "xmsetwmprotocolhooks"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmsetwmprotocolhooks/"
description: "XmSetWMProtocolHooks — A VendorShell convenience interface that allows preactions and postactions to be executed when a protocol message is received from the window manager"
---

<p><code>XmSetWMProtocolHooks</code> &#8212; A VendorShell convenience interface that allows preactions and postactions to be executed when a protocol message is received from the window manager</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
#include &lt;Xm/Protocols.h&gt;
<code>void XmSetWMProtocolHooks</code>(
<code>Widget shell</code>,
<code>Atom protocol</code>,
<code>XtCallbackProc prehook</code>,
<code>XtPointer pre_closure</code>,
<code>XtCallbackProc posthook</code>,
<code>XtPointer post_closure</code>);</pre>
<h2>Description</h2>
<p><code>XmSetWMProtocolHooks</code> is a convenience interface. It calls <code>XmSetProtocolHooks</code> with the property value set to the atom returned by interning <code>WM_PROTOCOLS</code>.</p>
<dl COMPACT>
<dt><i>shell</i></p>
<dd>Specifies the widget with which the protocol property is associated</p>
<dt><i>protocol</i></p>
<dd>Specifies the protocol atom (or an <i>int</i> cast to <code>Atom</code>)</p>
<dt><i>prehook</i></p>
<dd>Specifies the procedure to call before calling entries on the client callback list</p>
<dt><i>pre_closure</i></p>
<dd>Specifies the client data to be passed to the prehook when it is invoked</p>
<dt><i>posthook</i></p>
<dd>Specifies the procedure to call after calling entries on the client callback list</p>
<dt><i>post_closure</i></p>
<dd>Specifies the client data to be passed to the posthook when it is invoked</dl>
<p> For a complete definition of VendorShell and its associated resources, see <code><a href="/docs/linux/man/3-vendorshell/">VendorShell</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-vendorshell/">VendorShell</a></code>(3), <code><a href="/docs/linux/man/3-xminternatom/">XmInternAtom</a></code>(3), and <code><a href="/docs/linux/man/3-xmsetprotocolhooks/">XmSetProtocolHooks</a></code>(3).</p>
