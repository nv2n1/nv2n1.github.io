---
title: "ndptool(8)"
name: "ndptool"
section: "8"
letter: "n"
url: "/docs/linux/man/8-ndptool/"
description: "ndptool — Neighbor Discovery Protocol tool"
---

<p>ndptool &#8212; Neighbor Discovery Protocol tool</p>
<h2>Synopsis</h2>
<p><code>ndptool</code> <code>-h</code></p>
<dl>
<dt><code>ndptool [OPTIONS] COMMAND</code></p>
<dd>
<dt></dl>
<h2>Description</h2>
<p> ndptool is a tool which provides wrapper over Neighbor Discovery Protocol messages. </p>
<h2>Options</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd>Print help text to console and exit. </p>
<dt><code>-v, &#8211;verbose</code></p>
<dd>Increase output verbosity. </p>
<dt><code>-t type, &#8211;msg-type type</code></p>
<dd>Specified message type. Following are supported: </p>
<p> <code>rs &#8211;</code> Router Solicitation. </p>
<p> <code>ra &#8211;</code> Router Advertisement. </p>
<p> <code>ns &#8211;</code> Neighbor Solicitation. </p>
<p> <code>na &#8211;</code> Neighbor Advertisement. </p>
<dt><code>-i ifname, &#8211;ifname ifname</code></p>
<dd>Specified interface name. </p>
<dt><code>-U, &#8211;unsolicited</code></p>
<dd>Send Unsolicited NA. </p>
</dl>
<h2>Command</h2>
<dl>
<dt><code>monitor</code></p>
<dd>Monitor incoming NDP messages and print them out. </p>
<dt><code>send</code></p>
<dd>Send NDP message of specified type. </p>
</dl>
<h2>Author</h2>
<p>Jiri Pirko is the original author and current maintainer of libndp.</p>
