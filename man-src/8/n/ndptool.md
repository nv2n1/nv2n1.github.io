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
<dt><code>ndptool [OPTIONS] COMMAND</code></dt>
<dd>
</dd><dt></dt></dl>
<h2>Description</h2>
<p> ndptool is a tool which provides wrapper over Neighbor Discovery Protocol messages. </p>
<h2>Options</h2>
<dl>
<dt><code>-h, &#8211;help</code></dt>
<dd>Print help text to console and exit. </dd>
<dt><code>-v, &#8211;verbose</code></dt>
<dd>Increase output verbosity. </dd>
<dt><code>-t type, &#8211;msg-type type</code></dt>
<dd>Specified message type. Following are supported: </dd>
<p> <code>rs &#8211;</code> Router Solicitation. </p>
<p> <code>ra &#8211;</code> Router Advertisement. </p>
<p> <code>ns &#8211;</code> Neighbor Solicitation. </p>
<p> <code>na &#8211;</code> Neighbor Advertisement. </p>
<dt><code>-i ifname, &#8211;ifname ifname</code></dt>
<dd>Specified interface name. </dd>
<dt><code>-U, &#8211;unsolicited</code></dt>
<dd>Send Unsolicited NA. </dd>
</dl>
<h2>Command</h2>
<dl>
<dt><code>monitor</code></dt>
<dd>Monitor incoming NDP messages and print them out. </dd>
<dt><code>send</code></dt>
<dd>Send NDP message of specified type. </dd>
</dl>
<h2>Author</h2>
<p>Jiri Pirko is the original author and current maintainer of libndp.</p>
