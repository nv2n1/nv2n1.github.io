---
title: "xkbignoreextension(3)"
name: "xkbignoreextension"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbignoreextension/"
description: "XkbIgnoreExtension – Prevents core X library keyboard functions from using the X Keyboard Extension"
---

<p>XkbIgnoreExtension &#8211; Prevents core X library keyboard functions from using the X Keyboard Extension </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Bool XkbIgnoreExtension</code> <code>(Bool *</code><i>ignore</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>ignore</i></p>
<dd>
<dd>True means ignore the extension</dl>
<h2>Description</h2>
<p>If a server supports the Xkb extension, the X library normally implements preXkb keyboard functions using the Xkb keyboard description and state. The server Xkb keyboard state may differ from the preXkb keyboard state. This difference does not affect most clients, but there are exceptions. To allow these clients to work properly, you may instruct the extension not to use Xkb functionality. </p>
<p> Call <i>XkbIgnoreExtension </i> to prevent core X library keyboard functions from using the X Keyboard Extension. You must call <i>XkbIgnoreExtension </i> before you open a server connection; Xkb does not provide a way to enable or disable use of the extension once a connection is established. </p>
<p> <i>XkbIgnoreExtension </i> tells the X library whether to use the X Keyboard Extension on any subsequently opened X display connections. If ignore is True, the library does not initialize the Xkb extension when it opens a new display. This forces the X server to use compatibility mode and communicate with the client using only core protocol requests and events. If ignore is False, the library treats subsequent calls to <i>XOpenDisplay </i> normally and uses Xkb extension requests, events, and state. Do not explicitly use Xkb on a connection for which it is disabled. <i>XkbIgnoreExtension </i> returns False if it was unable to apply the ignore request.</p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>True</p>
<dd>The <i>XkbIgnoreExtension </i> returns True if</p>
<dt>False</p>
<dd>The <i>XkbIgnoreExtension </i> function returns False if it was unable to apply the ignore request.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xopendisplay/">XOpenDisplay</a></code>(3)</p>
