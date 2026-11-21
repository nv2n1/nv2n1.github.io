---
title: "wicd-gtk(1)"
name: "wicd-gtk"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wicd-gtk/"
description: "wicd-client – frontend to the WICD daemon"
---

<h2 class="name">NAME</h2>
<p> wicd-client &#8211; frontend to the WICD daemon </p>
<h2>DESCRIPTION</h2>
<p> wireless (and wired) connection daemon front-end. </p>
<p> If <code>wicd-curses</code> is installed, and you attempt to run wicd-client without an active X server on the current terminal, wicd-client will attempt to run <code>wicd-curses</code> instead. It will warn you the first time this happens.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-t, &#8211;tray</code></dt>
<dd> Run the wicd tray icon only.</dd>
<dt><code>-n, &#8211;no-tray</code></dt>
<dd> Run wicd without the tray icon.</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd> Print this help information.</dd>
<dt><code>-a, &#8211;no-animate</code></dt>
<dd> Run the tray without network traffic tray animations.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-wicd-curses/">wicd-curses</a></code>(8) <code><a href="/docs/linux/man/8-wicd/">wicd</a></code>(8) </p>
