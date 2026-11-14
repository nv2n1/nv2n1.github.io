---
title: "std__profilebitset(3)"
name: "std__profilebitset"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std__profilebitset/"
---

std::__profile::bitset&lt; _Nb &gt; -

<h2>Synopsis</h2>

 Inherits bitset&lt; _Nb &gt;.

<h3>Public Member Functions</h3>

<pre><code>constexpr bitset (unsigned long long __val) noexcept



template&lt;typename _CharT , typename _Traits , typename _Alloc &gt; bitset (const std::basic_string&lt; _CharT, _Traits, _Alloc &gt; &amp;__str, typename std::basic_string&lt; _CharT, _Traits, _Alloc &gt;::size_type __pos=0, typename std::basic_string&lt; _CharT, _Traits, _Alloc &gt;::size_type __n=(std::basic_string&lt; _CharT, _Traits, _Alloc &gt;::npos))



template&lt;class _CharT , class _Traits , class _Alloc &gt; bitset (const std::basic_string&lt; _CharT, _Traits, _Alloc &gt; &amp;__str, typename std::basic_string&lt; _CharT, _Traits, _Alloc &gt;::size_type __pos, typename std::basic_string&lt; _CharT, _Traits, _Alloc &gt;::size_type __n, _CharT __zero, _CharT __one=_CharT('1'))



bitset (const _Base &amp;__x)



template&lt;typename _CharT &gt; bitset (const _CharT *__str, typename std::basic_string&lt; _CharT &gt;::size_type __n=std::basic_string&lt; _CharT &gt;::npos, _CharT __zero=_CharT('0'), _CharT __one=_CharT('1'))



_Base &amp; _M_base () noexcept



const _Base &amp; _M_base () const noexcept



bitset&lt; _Nb &gt; &amp; flip () noexcept



bitset&lt; _Nb &gt; &amp; flip (size_t __pos)



bool operator!= (const bitset&lt; _Nb &gt; &amp;__rhs) const noexcept



bitset&lt; _Nb &gt; &amp; operator&amp;= (const bitset&lt; _Nb &gt; &amp;__rhs) noexcept



bitset&lt; _Nb &gt; operator&lt;&lt; (size_t __pos) const noexcept



bitset&lt; _Nb &gt; &amp; operator&lt;&lt;= (size_t __pos) noexcept



bool operator== (const bitset&lt; _Nb &gt; &amp;__rhs) const noexcept



bitset&lt; _Nb &gt; operator&gt;&gt; (size_t __pos) const noexcept



bitset&lt; _Nb &gt; &amp; operator&gt;&gt;= (size_t __pos) noexcept



reference operator[] (size_t __pos)



constexpr bool operator[] (size_t __pos) const



bitset&lt; _Nb &gt; &amp; operator^= (const bitset&lt; _Nb &gt; &amp;__rhs) noexcept



bitset&lt; _Nb &gt; &amp; operator|= (const bitset&lt; _Nb &gt; &amp;__rhs) noexcept



bitset&lt; _Nb &gt; operator~ () const noexcept



bitset&lt; _Nb &gt; &amp; reset () noexcept



bitset&lt; _Nb &gt; &amp; reset (size_t __pos)



bitset&lt; _Nb &gt; &amp; set () noexcept



bitset&lt; _Nb &gt; &amp; set (size_t __pos, bool __val=true)



template&lt;typename _CharT , typename _Traits , typename _Alloc &gt; std::basic_string&lt; _CharT,


_Traits, _Alloc &gt; to_string () const &quot;


template&lt;class _CharT , class _Traits , class _Alloc &gt; std::basic_string&lt; _CharT,


_Traits, _Alloc &gt; to_string (_CharT __zero, _CharT __one=_CharT('1')) const &quot;


template&lt;typename _CharT , typename _Traits &gt; std::basic_string&lt; _CharT,


_Traits, std::allocator

&lt; _CharT &gt; &gt; to_string () const &quot;


template&lt;class _CharT , class _Traits &gt; std::basic_string&lt; _CharT,


_Traits, std::allocator

&lt; _CharT &gt; &gt; to_string (_CharT __zero, _CharT __one=_CharT('1')) const &quot;


template&lt;typename _CharT &gt; std::basic_string&lt; _CharT,


std::char_traits&lt; _CharT &gt;

, std::allocator&lt; _CharT &gt; &gt; to_string () const &quot;


template&lt;class _CharT &gt; std::basic_string&lt; _CharT,


std::char_traits&lt; _CharT &gt;

, std::allocator&lt; _CharT &gt; &gt; to_string (_CharT __zero, _CharT __one=_CharT('1')) const &quot;


std::basic_string&lt; char,


std::char_traits&lt; char &gt;

, std::allocator&lt; char &gt; &gt; to_string () const &quot;


std::basic_string&lt; char,


std::char_traits&lt; char &gt;

, std::allocator&lt; char &gt; &gt; to_string (char __zero, char __one= '1') const &quot;</code></pre>

<h2>Detailed Description</h2>

<h3>template&lt;size_t _Nb&gt;class std::__profile::bitset&lt; _Nb &gt;</h3>

Class std::bitset wrapper with performance instrumentation. 

 Definition at line 40 of file profile/bitset.

<h2>Author</h2>

Generated automatically by Doxygen for libstdc++ from the source code.
