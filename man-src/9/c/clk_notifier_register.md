---
title: "clk_notifier_register(9)"
name: "clk_notifier_register"
section: "9"
letter: "c"
url: "/docs/linux/man/9-clk_notifier_register/"
---

clk_notifier_register - change notifier callback

<h2>Synopsis</h2>

<pre><code>int clk_notifier_register(struct clk *clk, struct notifier_block *nb);</code></pre>

<h2>Arguments</h2>

<i>clk</i>
<dl><dd><dd>clock whose rate we are interested in</dl>
 

 <i>nb</i>
<dl><dd>notifier block with callback function pointer</dl>

<h2>Description</h2>

ProTip: debugging across notifier chains can be frustrating. Make sure that your notifier callback function prints a nice big warning in case of failure.

<h2>Copyright</h2>


