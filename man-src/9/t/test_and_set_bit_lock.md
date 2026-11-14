---
title: "test_and_set_bit_lock(9)"
name: "test_and_set_bit_lock"
section: "9"
letter: "t"
url: "/docs/linux/man/9-test_and_set_bit_lock/"
description: "test_and_set_bit_lock – Set a bit and return its old value for lock"
---

<p>test_and_set_bit_lock &#8211; Set a bit and return its old value for lock</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool test_and_set_bit_lock(long&nbsp;<wbr></code><i>nr</i><code>, volatile unsigned long&nbsp;<wbr>*&nbsp;<wbr></code><i>addr</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>nr</i></p>
<dl>
<dd>
<dd>Bit to set</dl>
<p> <i>addr</i></p>
<dl>
<dd>Address to count from</dl>
<h2>Description</h2>
<p>This is the same as test_and_set_bit on x86.</p>
<h2>Copyright</h2>
