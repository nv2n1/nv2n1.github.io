---
title: "std__atomic_base(3)"
name: "std__atomic_base"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std__atomic_base/"
description: "std::__atomic_base< _IntTp > –"
---

<p>std::__atomic_base&lt; _IntTp &gt; &#8211;</p>
<h2>Synopsis</h2>
<p> Inherited by <code>std::atomic&lt; char &gt;</code>, <code>std::atomic&lt; char16_t &gt;</code>, <code>std::atomic&lt; char32_t &gt;</code>, <code>std::atomic&lt; int &gt;</code>, <code>std::atomic&lt; long &gt;</code>, <code>std::atomic&lt; long long &gt;</code>, <code>std::atomic&lt; short &gt;</code>, <code>std::atomic&lt; signed char &gt;</code>, <code>std::atomic&lt; unsigned char &gt;</code>, <code>std::atomic&lt; unsigned int &gt;</code>, <code>std::atomic&lt; unsigned long &gt;</code>, <code>std::atomic&lt; unsigned long long &gt;</code>, <code>std::atomic&lt; unsigned short &gt;</code>, and <code>std::atomic&lt; wchar_t &gt;</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>__atomic_base (const __atomic_base &amp;)=delete



constexpr __atomic_base (__int_type __i) noexcept



bool compare_exchange_strong (__int_type &amp;__i1, __int_type __i2, memory_order __m1, memory_order __m2) noexcept



bool compare_exchange_strong (__int_type &amp;__i1, __int_type __i2, memory_order __m1, memory_order __m2) volatilenoexcept



bool compare_exchange_strong (__int_type &amp;__i1, __int_type __i2, memory_order __m=memory_order_seq_cst) noexcept



bool compare_exchange_strong (__int_type &amp;__i1, __int_type __i2, memory_order __m=memory_order_seq_cst) volatilenoexcept



bool compare_exchange_weak (__int_type &amp;__i1, __int_type __i2, memory_order __m1, memory_order __m2) noexcept



bool compare_exchange_weak (__int_type &amp;__i1, __int_type __i2, memory_order __m1, memory_order __m2) volatilenoexcept



bool compare_exchange_weak (__int_type &amp;__i1, __int_type __i2, memory_order __m=memory_order_seq_cst) noexcept



bool compare_exchange_weak (__int_type &amp;__i1, __int_type __i2, memory_order __m=memory_order_seq_cst) volatilenoexcept



__int_type exchange (__int_type __i, memory_order __m=memory_order_seq_cst) noexcept



__int_type exchange (__int_type __i, memory_order __m=memory_order_seq_cst) volatilenoexcept



__int_type fetch_add (__int_type __i, memory_order __m=memory_order_seq_cst) noexcept



__int_type fetch_add (__int_type __i, memory_order __m=memory_order_seq_cst) volatilenoexcept



__int_type fetch_and (__int_type __i, memory_order __m=memory_order_seq_cst) noexcept



__int_type fetch_and (__int_type __i, memory_order __m=memory_order_seq_cst) volatilenoexcept



__int_type fetch_or (__int_type __i, memory_order __m=memory_order_seq_cst) noexcept



__int_type fetch_or (__int_type __i, memory_order __m=memory_order_seq_cst) volatilenoexcept



__int_type fetch_sub (__int_type __i, memory_order __m=memory_order_seq_cst) noexcept



__int_type fetch_sub (__int_type __i, memory_order __m=memory_order_seq_cst) volatilenoexcept



__int_type fetch_xor (__int_type __i, memory_order __m=memory_order_seq_cst) noexcept



__int_type fetch_xor (__int_type __i, memory_order __m=memory_order_seq_cst) volatilenoexcept



bool is_lock_free () const noexcept



bool is_lock_free () const volatilenoexcept



__int_type load (memory_order __m=memory_order_seq_cst) const noexcept



__int_type load (memory_order __m=memory_order_seq_cst) const volatilenoexcept



operator __int_type () const noexcept



operator __int_type () const volatilenoexcept



__int_type operator&amp;= (__int_type __i) noexcept



__int_type operator&amp;= (__int_type __i) volatilenoexcept



__int_type operator++ (int) noexcept



__int_type operator++ (int) volatilenoexcept



__int_type operator++ () noexcept



__int_type operator++ () volatilenoexcept



__int_type operator+= (__int_type __i) noexcept



__int_type operator+= (__int_type __i) volatilenoexcept



__int_type operator-- (int) noexcept



__int_type operator-- (int) volatilenoexcept



__int_type operator-- () noexcept



__int_type operator-- () volatilenoexcept



__int_type operator-= (__int_type __i) noexcept



__int_type operator-= (__int_type __i) volatilenoexcept



__atomic_base &amp; operator= (const __atomic_base &amp;)=delete



__atomic_base &amp; operator= (const __atomic_base &amp;) volatile=delete



__int_type operator= (__int_type __i) noexcept



__int_type operator= (__int_type __i) volatilenoexcept



__int_type operator^= (__int_type __i) noexcept



__int_type operator^= (__int_type __i) volatilenoexcept



__int_type operator|= (__int_type __i) noexcept



__int_type operator|= (__int_type __i) volatilenoexcept



void store (__int_type __i, memory_order __m=memory_order_seq_cst) noexcept



void store (__int_type __i, memory_order __m=memory_order_seq_cst) volatilenoexcept</code></pre>
<h2>Detailed Description</h2>
<h3>template&lt;typename _IntTp&gt;struct std::__atomic_base&lt; _IntTp &gt;</h3>
<p>Base class for atomic integrals. </p>
<p> Definition at line 117 of file atomic_base.h.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
