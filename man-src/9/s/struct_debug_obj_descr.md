---
title: "struct_debug_obj_descr(9)"
name: "struct_debug_obj_descr"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_debug_obj_descr/"
description: "struct_debug_obj_descr – object type specific debug description structure"
---

<p>struct_debug_obj_descr &#8211; object type specific debug description structure</p>
<h2>Synopsis</h2>
<pre><code>struct debug_obj_descr {
    const char *name;
    void *(*debug_hint)(void *addr);
    bool (*is_static_object)(void *addr);
    bool (*fixup_init)(void *addr, enum debug_obj_state state);
    bool (*fixup_activate)(void *addr, enum debug_obj_state state);
    bool (*fixup_destroy)(void *addr, enum debug_obj_state state);
    bool (*fixup_free)(void *addr, enum debug_obj_state state);
    bool (*fixup_assert_init)(void *addr, enum debug_obj_state state);
};</code></pre>
<h2>Members</h2>
<p>name</p>
<dl>
<dd>name of the object typee</dd></dl>
<p> debug_hint</p>
<dl>
<dd>function returning address, which have associated kernel symbol, to allow identify the object</dd></dl>
<p> is_static_object</p>
<dl>
<dd>return true if the obj is static, otherwise return false</dd></dl>
<p> fixup_init</p>
<dl>
<dd>fixup function, which is called when the init check fails. All fixup functions must return true if fixup was successful, otherwise return false</dd></dl>
<p> fixup_activate</p>
<dl>
<dd>fixup function, which is called when the activate check fails</dd></dl>
<p> fixup_destroy</p>
<dl>
<dd>fixup function, which is called when the destroy check fails</dd></dl>
<p> fixup_free</p>
<dl>
<dd>fixup function, which is called when the free check fails</dd></dl>
<p> fixup_assert_init</p>
<dl>
<dd>fixup function, which is called when the assert_init check fails</dd></dl>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dd></dl>
<h2>Copyright</h2>
