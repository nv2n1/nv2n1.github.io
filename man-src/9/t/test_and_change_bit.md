---
title: "test_and_change_bit(9)"
name: "test_and_change_bit"
section: "9"
letter: "t"
url: "/docs/linux/man/9-test_and_change_bit/"
description: "test_and_change_bit – Change a bit and return its old value"
---

<p>test_and_change_bit &#8211; Change a bit and return its old value</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool test_and_change_bit(long&nbsp;<wbr></code><i>nr</i><code>, volatile unsigned long&nbsp;<wbr>*&nbsp;<wbr></code><i>addr</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>nr</i></p>
<dl>
<dd>
<dd>Bit to change</dl>
<p> <i>addr</i></p>
<dl>
<dd>Address to count from</dl>
<h2>Description</h2>
<p>This operation is atomic and cannot be reordered. It also implies a memory barrier.</p>
<h2>Copyright</h2>
