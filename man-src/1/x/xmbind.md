---
title: "xmbind(1)"
name: "xmbind"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xmbind/"
description: "xmbind — Configures virtual key bindings"
---

<h2>NAME</h2>
<p> <code>xmbind</code> &#8212; Configures virtual key bindings</p>
<h2>SYNOPSIS</h2>
<p> <code>xmbind</code> [<i>options</i> ] [<i>file</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>xmbind</code> is an X Window System client that configures the virtual key bindings for Motif applications. This action is performed by <code>mwm</code> at its startup, so the <code>xmbind</code> client is only needed when <code>mwm</code> is not in use, or when you want to change bindings without restarting <code>mwm</code>. If a file is specified, its contents are used as the virtual key bindings. If a file is not specified, the file <code>.motifbind</code> in the user&#8217;s home directory is used. If this file is not found, <code>xmbind</code> loads the default virtual key bindings, as described in <code><a href="/docs/linux/man/3-virtualbindings/">VirtualBindings</a></code>(3).</p>
<h3>Options</h3>
<dl>
<dt><code>-display</code></p>
<dd> This option specifies the display to use; see <a href="/docs/linux/man/1-x/">X</a>(1).</dl>
<h2>RELATED</h2>
<p> <code><a href="/docs/linux/man/3-virtualbindings/">VirtualBindings</a></code>(3) and <code><a href="/docs/linux/man/1-x/">X</a></code>(1). </p>
<h2>Index</h2>
