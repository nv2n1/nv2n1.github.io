---
title: "stdatomic_bool(3)"
name: "stdatomic_bool"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatomic_bool/"
description: "std::atomic_bool –"
---

<p>std::atomic_bool &#8211;</p>
<h2>Synopsis</h2>
<p> Inherited by <code>std::atomic&lt; bool &gt;</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>atomic_bool (const atomic_bool &amp;)=delete



constexpr atomic_bool (bool __i) noexcept



bool compare_exchange_strong (bool &amp;__i1, bool __i2, memory_order __m1, memory_order __m2) noexcept



bool compare_exchange_strong (bool &amp;__i1, bool __i2, memory_order __m1, memory_order __m2) volatilenoexcept



bool compare_exchange_strong (bool &amp;__i1, bool __i2, memory_order __m=memory_order_seq_cst) noexcept



bool compare_exchange_strong (bool &amp;__i1, bool __i2, memory_order __m=memory_order_seq_cst) volatilenoexcept



bool compare_exchange_weak (bool &amp;__i1, bool __i2, memory_order __m1, memory_order __m2) noexcept



bool compare_exchange_weak (bool &amp;__i1, bool __i2, memory_order __m1, memory_order __m2) volatilenoexcept



bool compare_exchange_weak (bool &amp;__i1, bool __i2, memory_order __m=memory_order_seq_cst) noexcept



bool compare_exchange_weak (bool &amp;__i1, bool __i2, memory_order __m=memory_order_seq_cst) volatilenoexcept



bool exchange (bool __i, memory_order __m=memory_order_seq_cst) noexcept



bool exchange (bool __i, memory_order __m=memory_order_seq_cst) volatilenoexcept



bool is_lock_free () const noexcept



bool is_lock_free () const volatilenoexcept



bool load (memory_order __m=memory_order_seq_cst) const noexcept



bool load (memory_order __m=memory_order_seq_cst) const volatilenoexcept



operator bool () const noexcept



operator bool () const volatilenoexcept



atomic_bool &amp; operator= (const atomic_bool &amp;)=delete



atomic_bool &amp; operator= (const atomic_bool &amp;) volatile=delete



bool operator= (bool __i) noexcept



bool operator= (bool __i) volatilenoexcept



void store (bool __i, memory_order __m=memory_order_seq_cst) noexcept



void store (bool __i, memory_order __m=memory_order_seq_cst) volatilenoexcept</code></pre>
<h2>Detailed Description</h2>
<p>atomic_bool </p>
<p> Definition at line 54 of file atomic.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
