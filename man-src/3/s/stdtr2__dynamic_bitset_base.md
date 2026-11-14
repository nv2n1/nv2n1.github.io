---
title: "stdtr2__dynamic_bitset_base(3)"
name: "stdtr2__dynamic_bitset_base"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdtr2__dynamic_bitset_base/"
description: "std::tr2::__dynamic_bitset_base< _WordT, _Alloc > –"
---

<p>std::tr2::__dynamic_bitset_base&lt; _WordT, _Alloc &gt; &#8211;</p>
<h2>Synopsis</h2>
<p> Inherited by <code>std::tr2::dynamic_bitset&lt; _WordT, _Alloc &gt;</code> [private].</p>
<h3>Public Types</h3>
<p>typedef _Alloc <code>allocator_type</code> </p>
<p> typedef _WordT <code>block_type</code> </p>
<p> typedef size_t <code>size_type</code></p>
<h3>Public Member Functions</h3>
<pre><code>__dynamic_bitset_base (size_type __nbits, unsigned long long __val=0ULL, const allocator_type &amp;__alloc=allocator_type())



size_t _M_are_all_aux () const



void _M_assign (const __dynamic_bitset_base &amp;__b)



void _M_clear ()



void _M_do_and (const __dynamic_bitset_base &amp;__x)



void _M_do_append_block (block_type __block, size_type __pos)



size_t _M_do_count () const



void _M_do_dif (const __dynamic_bitset_base &amp;__x)



size_type _M_do_find_first (size_t __not_found) const



size_type _M_do_find_next (size_t __prev, size_t __not_found) const



void _M_do_flip ()



void _M_do_left_shift (size_t __shift)



void _M_do_or (const __dynamic_bitset_base &amp;__x)



void _M_do_reset ()



void _M_do_right_shift (size_t __shift)



void _M_do_set ()



unsigned long long _M_do_to_ullong () const



unsigned long _M_do_to_ulong () const



void _M_do_xor (const __dynamic_bitset_base &amp;__x)



allocator_type _M_get_allocator () const



block_type &amp; _M_getword (size_type __pos)



block_type _M_getword (size_type __pos) const



block_type &amp; _M_hiword ()



block_type _M_hiword () const



bool _M_is_any () const



bool _M_is_equal (const __dynamic_bitset_base &amp;__x) const



bool _M_is_less (const __dynamic_bitset_base &amp;__x) const



bool _M_is_proper_subset_of (const __dynamic_bitset_base &amp;__b) const



bool _M_is_subset_of (const __dynamic_bitset_base &amp;__b)



void _M_resize (size_t __nbits, bool __value)



size_type _M_size () const noexcept



void _M_swap (__dynamic_bitset_base &amp;__b)



Static Public Member Functions
static block_type _S_maskbit (size_type __pos) noexcept



static size_type _S_whichbit (size_type __pos) noexcept



static size_type _S_whichbyte (size_type __pos) noexcept



static size_type _S_whichword (size_type __pos) noexcept



Public Attributes</code></pre>
<p> <code>__pad0__</code>: <code>_M_w</code>(__alloc) { } explicit <code>__dynamic_bitset_base</code>(<code>__dynamic_bitset_base</code>&amp;&amp; __b) { this-&gt;_M_w.swap(__b._M_w) </p>
<p> <code>std::vector</code>&lt; block_type,<br />
 allocator_type &gt; <code>_M_w</code>&quot;</p>
<h3>Static Public Attributes</h3>
<pre><code>static const size_type _S_bits_per_block



static const size_type npos</code></pre>
<h2>Detailed Description</h2>
<h3>template&lt;typename _WordT = unsigned long long, typename _Alloc = std::allocator&lt;_WordT&gt;&gt;struct std::tr2::__dynamic_bitset_base&lt; _WordT, _Alloc &gt;</h3>
<p>Base class, general case. </p>
<p> See documentation for dynamic_bitset. </p>
<p> Definition at line 80 of file dynamic_bitset.</p>
<h2>Member Data Documentation</h2>
<h3>template&lt;typename _WordT = unsigned long long, typename _Alloc = std::allocator&lt;_WordT&gt;&gt; <code>std::vector</code>&lt;block_type, allocator_type&gt; <code>std::tr2::__dynamic_bitset_base</code>&lt; _WordT, _Alloc &gt;::_M_w</h3>
<p>0 is the least significant word. </p>
<p> Definition at line 93 of file dynamic_bitset.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
