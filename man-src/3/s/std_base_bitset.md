---
title: "std_base_bitset(3)"
name: "std_base_bitset"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std_base_bitset/"
description: "std::_Base_bitset< _Nw > –"
---

<p>std::_Base_bitset&lt; _Nw &gt; &#8211;</p>
<h2>Synopsis</h2>
<h3>Public Types</h3>
<p>typedef unsigned long <code>_WordT</code></p>
<h3>Public Member Functions</h3>
<p>constexpr <code>_Base_bitset</code> (unsigned long long __val) noexcept </p>
<p> template&lt;size_t _Nb&gt; bool <code>_M_are_all</code> () const noexcept </p>
<p> void <code>_M_do_and</code> (const <code>_Base_bitset</code>&lt; _Nw &gt; &amp;__x) noexcept </p>
<p> size_t <code>_M_do_count</code> () const noexcept </p>
<p> size_t <code>_M_do_find_first</code> (size_t) const noexcept </p>
<p> size_t <code>_M_do_find_next</code> (size_t, size_t) const noexcept </p>
<p> void <code>_M_do_flip</code> () noexcept </p>
<p> void <code>_M_do_left_shift</code> (size_t __shift) noexcept </p>
<p> void <code>_M_do_or</code> (const <code>_Base_bitset</code>&lt; _Nw &gt; &amp;__x) noexcept </p>
<p> void <code>_M_do_reset</code> () noexcept </p>
<p> void <code>_M_do_right_shift</code> (size_t __shift) noexcept </p>
<p> void <code>_M_do_set</code> () noexcept </p>
<p> unsigned long long <code>_M_do_to_ullong</code> () const </p>
<p> unsigned long <code>_M_do_to_ulong</code> () const </p>
<p> void <code>_M_do_xor</code> (const <code>_Base_bitset</code>&lt; _Nw &gt; &amp;__x) noexcept </p>
<p> const _WordT * <code>_M_getdata</code> () const noexcept </p>
<p> _WordT &amp; <code>_M_getword</code> (size_t __pos) noexcept </p>
<p> constexpr _WordT <code>_M_getword</code> (size_t __pos) const noexcept </p>
<p> _WordT &amp; <code>_M_hiword</code> () noexcept </p>
<p> constexpr _WordT <code>_M_hiword</code> () const noexcept </p>
<p> bool <code>_M_is_any</code> () const noexcept </p>
<p> bool <code>_M_is_equal</code> (const <code>_Base_bitset</code>&lt; _Nw &gt; &amp;__x) const noexcept</p>
<h3>Static Public Member Functions</h3>
<pre><code>static constexpr _WordT _S_maskbit (size_t __pos) noexcept



static constexpr size_t _S_whichbit (size_t __pos) noexcept



static constexpr size_t _S_whichbyte (size_t __pos) noexcept



static constexpr size_t _S_whichword (size_t __pos) noexcept



Public Attributes</code></pre>
<p> _WordT <code>_M_w</code> [_Nw]</p>
<h2>Detailed Description</h2>
<h3>template&lt;size_t _Nw&gt;struct std::_Base_bitset&lt; _Nw &gt;</h3>
<p>Base class, general case. It is a class invariant that _Nw will be nonnegative. </p>
<p> See documentation for bitset. </p>
<p> Definition at line 71 of file bitset.</p>
<h2>Member Data Documentation</h2>
<h3>template&lt;size_t _Nw&gt; _WordT <code>std::_Base_bitset</code>&lt; _Nw &gt;::_M_w[_Nw]</h3>
<p>0 is the least significant word. </p>
<p> Definition at line 76 of file bitset.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
