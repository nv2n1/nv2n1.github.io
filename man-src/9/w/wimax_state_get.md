---
title: "wimax_state_get(9)"
name: "wimax_state_get"
section: "9"
letter: "w"
url: "/docs/linux/man/9-wimax_state_get/"
description: "wimax_state_get – Return the current state of a WiMAX device"
---

<p>wimax_state_get &#8211; Return the current state of a WiMAX device</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>enum wimax_st wimax_state_get(struct wimax_dev&nbsp;<wbr>*&nbsp;<wbr></code><i>wimax_dev</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>wimax_dev</i></p>
<dl>
<dd>
<dd>WiMAX device descriptor</dl>
<h2>Return</h2>
<p>Current state of the device according to its driver.</p>
<h2>Copyright</h2>
