---
title: "struct_w1_family_ops(9)"
name: "struct_w1_family_ops"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_w1_family_ops/"
description: "struct_w1_family_ops – operations for a family type"
---

<p>struct_w1_family_ops &#8211; operations for a family type</p>
<h2>Synopsis</h2>
<pre><code>struct w1_family_ops {
    int (*add_slave)(struct w1_slave *);
    void (*remove_slave)(struct w1_slave *);
    const struct attribute_group **groups;
};</code></pre>
<h2>Members</h2>
<p>add_slave</p>
<dl>
<dd>add_slave</dl>
<p> remove_slave</p>
<dl>
<dd>remove_slave</dl>
<p> groups</p>
<dl>
<dd>sysfs group</dl>
<h2>Author</h2>
<p><code>David Fries</code> &lt;David [at] Fries.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
