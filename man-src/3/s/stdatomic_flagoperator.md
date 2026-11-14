---
title: "stdatomic_flagoperator(3)"
name: "stdatomic_flagoperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatomic_flagoperator/"
---

std::atomic_flag::operator= - std::atomic_flag::operator=

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;atomic&gt;

    atomic_flag &amp;operator=(const atomic_flag &amp;) = delete;
(1)(since C++ 11)

    atomic_flag &amp;
    operator=(const atomic_flag &amp;) volatile = delete;
(2)(since C++ 11)</code></pre> 
std::atomic_flag is not assignable, its assignment operators are deleted. 
