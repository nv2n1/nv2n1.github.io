---
title: "stddestroying_delete_tstddestroying_delete(3)"
name: "stddestroying_delete_tstddestroying_delete"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stddestroying_delete_tstddestroying_delete/"
---

std::destroying_delete_t,std::destroying_delete - std::destroying_delete_t,std::destroying_delete

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;new&gt;

    struct destroying_delete_t {
    explicit destroying_delete_t() = default;
};
(since C++ 20)

    inline constexpr destroying_delete_t destroying_delete{};
(since C++ 20)</code></pre> 
Tag type used to identify the destroying delete form of operator_delete. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;deallocation functions 
operator_delete <i>(function)</i> 
operator_delete[] 
