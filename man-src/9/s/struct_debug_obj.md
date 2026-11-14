---
title: "struct_debug_obj(9)"
name: "struct_debug_obj"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_debug_obj/"
description: "struct_debug_obj – representaion of an tracked object"
---

<p>struct_debug_obj &#8211; representaion of an tracked object</p>
<h2>Synopsis</h2>
<pre><code>struct debug_obj {
    struct hlist_node node;
    enum debug_obj_state state;
    unsigned int astate;
    void *object;
    struct debug_obj_descr *descr;
};</code></pre>
<h2>Members</h2>
<p>node</p>
<dl>
<dd>hlist node to link the object into the tracker list</dl>
<p> state</p>
<dl>
<dd>tracked object state</dl>
<p> astate</p>
<dl>
<dd>current active state</dl>
<p> object</p>
<dl>
<dd>pointer to the real object</dl>
<p> descr</p>
<dl>
<dd>pointer to an object type specific debug description structure</dl>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
