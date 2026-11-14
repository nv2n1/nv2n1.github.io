---
title: "eth_get_headlen(9)"
name: "eth_get_headlen"
section: "9"
letter: "e"
url: "/docs/linux/man/9-eth_get_headlen/"
description: "eth_get_headlen – determine the length of header for an ethernet frame"
---

<p>eth_get_headlen &#8211; determine the length of header for an ethernet frame</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>u32 eth_get_headlen(void&nbsp;<wbr>*&nbsp;<wbr></code><i>data</i><code>, unsigned int&nbsp;<wbr></code><i>len</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>data</i></p>
<dl>
<dd>
<dd>pointer to start of frame</dl>
<p> <i>len</i></p>
<dl>
<dd>total length of frame</dl>
<h2>Description</h2>
<p>Make a best effort attempt to pull the length for all of the headers for a given frame in a linear buffer.</p>
<h2>Copyright</h2>
