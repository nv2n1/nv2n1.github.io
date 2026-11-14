---
title: "clk_notifier_unregister(9)"
name: "clk_notifier_unregister"
section: "9"
letter: "c"
url: "/docs/linux/man/9-clk_notifier_unregister/"
---

clk_notifier_unregister - change notifier callback

<h2>Synopsis</h2>

<pre><code>int clk_notifier_unregister(struct clk *clk, struct notifier_block *nb);</code></pre>

<h2>Arguments</h2>

<i>clk</i>
<dl><dd><dd>clock whose rate we are no longer interested in</dl>
 

 <i>nb</i>
<dl><dd>notifier block which will be unregistered</dl>

<h2>Copyright</h2>


