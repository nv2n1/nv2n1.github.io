---
title: "struct_nand_hw_control(9)"
name: "struct_nand_hw_control"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_nand_hw_control/"
description: "struct_nand_hw_control – Control structure for hardware controller (e.g ECC generator) shared among independent devices"
---

<p>struct_nand_hw_control &#8211; Control structure for hardware controller (e.g ECC generator) shared among independent devices</p>
<h2>Synopsis</h2>
<pre><code>struct nand_hw_control {
    spinlock_t lock;
    struct nand_chip *active;
    wait_queue_head_t wq;
};</code></pre>
<h2>Members</h2>
<p>lock</p>
<dl>
<dd>protection lock</dl>
<p> active</p>
<dl>
<dd>the mtd device which holds the controller currently</dl>
<p> wq</p>
<dl>
<dd>wait queue to sleep on if a NAND operation is in progress used instead of the per chip wait queue when a hw controller is available.</dl>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
