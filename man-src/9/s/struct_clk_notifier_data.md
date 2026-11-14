---
title: "struct_clk_notifier_data(9)"
name: "struct_clk_notifier_data"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_clk_notifier_data/"
---

struct_clk_notifier_data - rate data to pass to the notifier callback

<h2>Synopsis</h2>

<pre><code>struct clk_notifier_data {
    struct clk *clk;
    unsigned long old_rate;
    unsigned long new_rate;
};</code></pre>

<h2>Members</h2>

clk
<dl><dd>struct clk * being changed</dl>
 

 old_rate
<dl><dd>previous rate of this clk</dl>
 

 new_rate
<dl><dd>new rate of this clk</dl>

<h2>Description</h2>

For a pre-notifier, old_rate is the clk's rate before this rate change, and new_rate is what the rate will be in the future. For a post-notifier, old_rate and new_rate are both set to the clk's current rate (this was done to optimize the implementation).

<h2>Copyright</h2>


