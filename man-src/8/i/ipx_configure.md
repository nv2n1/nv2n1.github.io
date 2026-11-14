---
title: "ipx_configure(8)"
name: "ipx_configure"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipx_configure/"
description: "ipx_configure – query/configure IPX behavior"
---

<p>ipx_configure &#8211; query/configure IPX behavior</p>
<h2>Synopsis</h2>
<p><code>ipx_configure</code> [ <code>&#8211;help</code> | <code>-h</code> ] [ <code>&#8211;auto_interface=</code><i>on|off</i> | <code>-i</code> <i>on|off</i> ] [ <code>&#8211;auto_primary=</code><i>on|off</i> | <code>-p</code> <i>on|off</i> ]</p>
<h2>Description</h2>
<p><code>ipx_configure</code> queries or configures IPX behavior with respect to automatic IPX interface detection. IPX can be configured to automatically create interfaces as they are detected. It can also be configured to automatically select a primary interface when none is explicitly selected. By default, it is configured to <code>NOT </code> have this behavior. Without arguments, <code>ipx_configure</code> returns the current configuration state. The behavior with arguments is described in the section <code>OPTIONS.</code></p>
<h2>Options</h2>
<p><code>&#8211;auto_interface=</code><i>on|off</i><br />
 <code>-i</code> <i>on|off</i></p>
<dl>
<dd>This argument either turns on or off the behavior of automatically creating interfaces.</dl>
<p> <code>&#8211;auto_primary=</code><i>on|off</i><br />
 <code>-p</code> <i>on|off</i></p>
<dl>
<dd>This argument either turns on or off the behavior of automatically selecting a primary interface.</dl>
<p> <code>&#8211;help</code><br />
 <code>-h</code></p>
<dl>
<dd>Print out information about utility.</dl>
<h2>Files</h2>
<p><i>/proc/net/ipx_interface</i></p>
<h2>Bugs</h2>
<p>This functionality really belongs in <code><a href="/docs/linux/man/8-ifconfig/">ifconfig</a>(8).</code></p>
<h2>Author</h2>
<p>Greg Page &lt;greg.page [at] caldera.com&gt;</p>
