---
title: "struct_w1_async_cmd(9)"
name: "struct_w1_async_cmd"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_w1_async_cmd/"
description: "struct_w1_async_cmd – execute callback from the w1_process kthread"
---

<p>struct_w1_async_cmd &#8211; execute callback from the w1_process kthread</p>
<h2>Synopsis</h2>
<pre><code>struct w1_async_cmd {
    struct list_head async_entry;
    void (*cb)(struct w1_master *dev, struct w1_async_cmd *async_cmd);
};</code></pre>
<h2>Members</h2>
<p>async_entry</p>
<dl>
<dd>link entry</dl>
<p> cb</p>
<dl>
<dd>callback function, must list_del and destroy this list before returning</dl>
<h2>Description</h2>
<p>When inserted into the w1_master async_list, w1_process will execute the callback. Embed this into the structure with the command details.</p>
<h2>Author</h2>
<p><code>David Fries</code> &lt;David [at] Fries.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
