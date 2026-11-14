---
title: "struct_clk_notifier(9)"
name: "struct_clk_notifier"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_clk_notifier/"
---

struct_clk_notifier - associate a clk with a notifier

<h2>Synopsis</h2>

<pre><code>struct clk_notifier {
    struct clk *clk;
    struct srcu_notifier_head notifier_head;
    struct list_head node;
};</code></pre>

<h2>Members</h2>

clk
<dl><dd>struct clk * to associate the notifier with</dl>
 

 notifier_head
<dl><dd>a blocking_notifier_head for this clk</dl>
 

 node
<dl><dd>linked list pointers</dl>

<h2>Description</h2>

A list of struct clk_notifier is maintained by the notifier code. An entry is created whenever code registers the first notifier on a particular <i>clk</i>. Future notifiers on that <i>clk</i> are added to the <i>notifier_head</i>.

<h2>Copyright</h2>


