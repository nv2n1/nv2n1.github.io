---
title: "std__debug(3)"
name: "std__debug"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std__debug/"
description: "std::__debug –"
---

<p>std::__debug &#8211;</p>
<h2>Synopsis</h2>
<h3>Classes</h3>
<p>class <code>bitset</code> </p>
<p> class <code>deque</code> </p>
<p> class <code>forward_list</code> </p>
<p> class <code>list</code> </p>
<p> class <code>map</code> </p>
<p> class <code>multimap</code> </p>
<p> class <code>multiset</code> </p>
<p> class <code>set</code> </p>
<p> class <code>unordered_map</code> </p>
<p> class <code>unordered_multimap</code> </p>
<p> class <code>unordered_multiset</code> </p>
<p> class <code>unordered_set</code> </p>
<p> class <code>vector</code></p>
<h3>Functions</h3>
<p>template&lt;typename _Key , typename _Compare , typename _Allocator &gt; bool <code>operator!=</code> (const <code>multiset</code>&lt; _Key, _Compare, _Allocator &gt; &amp;__lhs, const <code>multiset</code>&lt; _Key, _Compare, _Allocator &gt; &amp;__rhs) </p>
<p> template&lt;typename _Key , typename _Tp , typename _Compare , typename _Allocator &gt; bool <code>operator!=</code> (const <code>multimap</code>&lt; _Key, _Tp, _Compare, _Allocator &gt; &amp;__lhs, const <code>multimap</code>&lt; _Key, _Tp, _Compare, _Allocator &gt; &amp;__rhs) </p>
<p> template&lt;typename _Key , typename _Compare , typename _Allocator &gt; bool <code>operator!=</code> (const <code>set</code>&lt; _Key, _Compare, _Allocator &gt; &amp;__lhs, const <code>set</code>&lt; _Key, _Compare, _Allocator &gt; &amp;__rhs) </p>
<p> template&lt;typename _Key , typename _Tp , typename _Compare , typename _Allocator &gt; bool <code>operator!=</code> (const <code>map</code>&lt; _Key, _Tp, _Compare, _Allocator &gt; &amp;__lhs, const <code>map</code>&lt; _Key, _Tp, _Compare, _Allocator &gt; &amp;__rhs) </p>
<p> template&lt;typename _Value , typename _Hash , typename _Pred , typename _Alloc &gt; bool <code>operator!=</code> (const <code>unordered_set</code>&lt; _Value, _Hash, _Pred, _Alloc &gt; &amp;__x, const <code>unordered_set</code>&lt; _Value, _Hash, _Pred, _Alloc &gt; &amp;__y) </p>
<p> template&lt;typename _Key , typename _Tp , typename _Hash , typename _Pred , typename _Alloc &gt; bool <code>operator!=</code> (const <code>unordered_map</code>&lt; _Key, _Tp, _Hash, _Pred, _Alloc &gt; &amp;__x, const <code>unordered_map</code>&lt; _Key, _Tp, _Hash, _Pred, _Alloc &gt; &amp;__y) </p>
<p> template&lt;typename _Tp , typename _Alloc &gt; bool <code>operator!=</code> (const <code>deque</code>&lt; _Tp, _Alloc &gt; &amp;__lhs, const <code>deque</code>&lt; _Tp, _Alloc &gt; &amp;__rhs) </p>
<p> template&lt;typename _Tp , typename _Alloc &gt; bool <code>operator!=</code> (const <code>vector</code>&lt; _Tp, _Alloc &gt; &amp;__lhs, const <code>vector</code>&lt; _Tp, _Alloc &gt; &amp;__rhs) </p>
<p> template&lt;typename _Tp , typename _Alloc &gt; bool <code>operator!=</code> (const <code>list</code>&lt; _Tp, _Alloc &gt; &amp;__lhs, const <code>list</code>&lt; _Tp, _Alloc &gt; &amp;__rhs) </p>
<p> template&lt;typename _Tp , typename _Alloc &gt; bool <code>operator!=</code> (const <code>forward_list</code>&lt; _Tp, _Alloc &gt; &amp;__lx, const <code>forward_list</code>&lt; _Tp, _Alloc &gt; &amp;__ly) </p>
<p> template&lt;typename _Value , typename _Hash , typename _Pred , typename _Alloc &gt; bool <code>operator!=</code> (const <code>unordered_multiset</code>&lt; _Value, _Hash, _Pred, _Alloc &gt; &amp;__x, const <code>unordered_multiset</code>&lt; _Value, _Hash, _Pred, _Alloc &gt; &amp;__y) </p>
<p> template&lt;typename _Key , typename _Tp , typename _Hash , typename _Pred , typename _Alloc &gt; bool <code>operator!=</code> (const <code>unordered_multimap</code>&lt; _Key, _Tp, _Hash, _Pred, _Alloc &gt; &amp;__x, const <code>unordered_multimap</code>&lt; _Key, _Tp, _Hash, _Pred, _Alloc &gt; &amp;__y) </p>
<p> template&lt;size_t _Nb&gt; <code>bitset</code>&lt; _Nb &gt; <code>operator&amp;</code> (const <code>bitset</code>&lt; _Nb &gt; &amp;__x, const <code>bitset</code>&lt; _Nb &gt; &amp;__y) noexcept </p>
<p> template&lt;typename _Key , typename _Compare , typename _Allocator &gt; bool <code>operator&lt;</code> (const <code>multiset</code>&lt; _Key, _Compare, _Allocator &gt; &amp;__lhs, const <code>multiset</code>&lt; _Key, _Compare, _Allocator &gt; &amp;__rhs) </p>
<p> template&lt;typename _Key , typename _Compare , typename _Allocator &gt; bool <code>operator&lt;</code> (const <code>set</code>&lt; _Key, _Compare, _Allocator &gt; &amp;__lhs, const <code>set</code>&lt; _Key, _Compare, _Allocator &gt; &amp;__rhs) </p>
<p> template&lt;typename _Key , typename _Tp , typename _Compare , typename _Allocator &gt; bool <code>operator&lt;</code> (const <code>multimap</code>&lt; _Key, _Tp, _Compare, _Allocator &gt; &amp;__lhs, const <code>multimap</code>&lt; _Key, _Tp, _Compare, _Allocator &gt; &amp;__rhs) </p>
<p> template&lt;typename _Key , typename _Tp , typename _Compare , typename _Allocator &gt; bool <code>operator&lt;</code> (const <code>map</code>&lt; _Key, _Tp, _Compare, _Allocator &gt; &amp;__lhs, const <code>map</code>&lt; _Key, _Tp, _Compare, _Allocator &gt; &amp;__rhs) </p>
<p> template&lt;typename _Tp , typename _Alloc &gt; bool <code>operator&lt;</code> (const <code>deque</code>&lt; _Tp, _Alloc &gt; &amp;__lhs, const <code>deque</code>&lt; _Tp, _Alloc &gt; &amp;__rhs) </p>
<p> template&lt;typename _Tp , typename _Alloc &gt; bool <code>operator&lt;</code> (const <code>vector</code>&lt; _Tp, _Alloc &gt; &amp;__lhs, const <code>vector</code>&lt; _Tp, _Alloc &gt; &amp;__rhs) </p>
<p> template&lt;typename _Tp , typename _Alloc &gt; bool <code>operator&lt;</code> (const <code>list</code>&lt; _Tp, _Alloc &gt; &amp;__lhs, const <code>list</code>&lt; _Tp, _Alloc &gt; &amp;__rhs) </p>
<p> template&lt;typename _Tp , typename _Alloc &gt; bool <code>operator&lt;</code> (const <code>forward_list</code>&lt; _Tp, _Alloc &gt; &amp;__lx, const <code>forward_list</code>&lt; _Tp, _Alloc &gt; &amp;__ly) </p>
<p> template&lt;typename _CharT , typename _Traits , size_t _Nb&gt; <code>std::basic_ostream</code>&lt; _CharT,<br />
 _Traits &gt; &amp; <code>operator&lt;&lt;</code> (<code>std::basic_ostream</code>&lt; _CharT, _Traits &gt; &amp;__os, const <code>bitset</code>&lt; _Nb &gt; &amp;__x)&quot; </p>
<p> template&lt;typename _Key , typename _Compare , typename _Allocator &gt; bool <code>operator&lt;=</code> (const <code>multiset</code>&lt; _Key, _Compare, _Allocator &gt; &amp;__lhs, const <code>multiset</code>&lt; _Key, _Compare, _Allocator &gt; &amp;__rhs) </p>
<p> template&lt;typename _Key , typename _Compare , typename _Allocator &gt; bool <code>operator&lt;=</code> (const <code>set</code>&lt; _Key, _Compare, _Allocator &gt; &amp;__lhs, const <code>set</code>&lt; _Key, _Compare, _Allocator &gt; &amp;__rhs) </p>
<p> template&lt;typename _Key , typename _Tp , typename _Compare , typename _Allocator &gt; bool <code>operator&lt;=</code> (const <code>multimap</code>&lt; _Key, _Tp, _Compare, _Allocator &gt; &amp;__lhs, const <code>multimap</code>&lt; _Key, _Tp, _Compare, _Allocator &gt; &amp;__rhs) </p>
<p> template&lt;typename _Key , typename _Tp , typename _Compare , typename _Allocator &gt; bool <code>operator&lt;=</code> (const <code>map</code>&lt; _Key, _Tp, _Compare, _Allocator &gt; &amp;__lhs, const <code>map</code>&lt; _Key, _Tp, _Compare, _Allocator &gt; &amp;__rhs) </p>
<p> template&lt;typename _Tp , typename _Alloc &gt; bool <code>operator&lt;=</code> (const <code>deque</code>&lt; _Tp, _Alloc &gt; &amp;__lhs, const <code>deque</code>&lt; _Tp, _Alloc &gt; &amp;__rhs) </p>
<p> template&lt;typename _Tp , typename _Alloc &gt; bool <code>operator&lt;=</code> (const <code>vector</code>&lt; _Tp, _Alloc &gt; &amp;__lhs, const <code>vector</code>&lt; _Tp, _Alloc &gt; &amp;__rhs) </p>
<p> template&lt;typename _Tp , typename _Alloc &gt; bool <code>operator&lt;=</code> (const <code>list</code>&lt; _Tp, _Alloc &gt; &amp;__lhs, const <code>list</code>&lt; _Tp, _Alloc &gt; &amp;__rhs) </p>
<p> template&lt;typename _Tp , typename _Alloc &gt; bool <code>operator&lt;=</code> (const <code>forward_list</code>&lt; _Tp, _Alloc &gt; &amp;__lx, const <code>forward_list</code>&lt; _Tp, _Alloc &gt; &amp;__ly) </p>
<p> template&lt;typename _Key , typename _Compare , typename _Allocator &gt; bool <code>operator==</code> (const <code>multiset</code>&lt; _Key, _Compare, _Allocator &gt; &amp;__lhs, const <code>multiset</code>&lt; _Key, _Compare, _Allocator &gt; &amp;__rhs) </p>
<p> template&lt;typename _Key , typename _Tp , typename _Compare , typename _Allocator &gt; bool <code>operator==</code> (const <code>multimap</code>&lt; _Key, _Tp, _Compare, _Allocator &gt; &amp;__lhs, const <code>multimap</code>&lt; _Key, _Tp, _Compare, _Allocator &gt; &amp;__rhs) </p>
<p> template&lt;typename _Key , typename _Compare , typename _Allocator &gt; bool <code>operator==</code> (const <code>set</code>&lt; _Key, _Compare, _Allocator &gt; &amp;__lhs, const <code>set</code>&lt; _Key, _Compare, _Allocator &gt; &amp;__rhs) </p>
<p> template&lt;typename _Key , typename _Tp , typename _Compare , typename _Allocator &gt; bool <code>operator==</code> (const <code>map</code>&lt; _Key, _Tp, _Compare, _Allocator &gt; &amp;__lhs, const <code>map</code>&lt; _Key, _Tp, _Compare, _Allocator &gt; &amp;__rhs) </p>
<p> template&lt;typename _Value , typename _Hash , typename _Pred , typename _Alloc &gt; bool <code>operator==</code> (const <code>unordered_set</code>&lt; _Value, _Hash, _Pred, _Alloc &gt; &amp;__x, const <code>unordered_set</code>&lt; _Value, _Hash, _Pred, _Alloc &gt; &amp;__y) </p>
<p> template&lt;typename _Key , typename _Tp , typename _Hash , typename _Pred , typename _Alloc &gt; bool <code>operator==</code> (const <code>unordered_map</code>&lt; _Key, _Tp, _Hash, _Pred, _Alloc &gt; &amp;__x, const <code>unordered_map</code>&lt; _Key, _Tp, _Hash, _Pred, _Alloc &gt; &amp;__y) </p>
<p> template&lt;typename _Tp , typename _Alloc &gt; bool <code>operator==</code> (const <code>deque</code>&lt; _Tp, _Alloc &gt; &amp;__lhs, const <code>deque</code>&lt; _Tp, _Alloc &gt; &amp;__rhs) </p>
<p> template&lt;typename _Tp , typename _Alloc &gt; bool <code>operator==</code> (const <code>vector</code>&lt; _Tp, _Alloc &gt; &amp;__lhs, const <code>vector</code>&lt; _Tp, _Alloc &gt; &amp;__rhs) </p>
<p> template&lt;typename _Tp , typename _Alloc &gt; bool <code>operator==</code> (const <code>list</code>&lt; _Tp, _Alloc &gt; &amp;__lhs, const <code>list</code>&lt; _Tp, _Alloc &gt; &amp;__rhs) </p>
<p> template&lt;typename _Tp , typename _Alloc &gt; bool <code>operator==</code> (const <code>forward_list</code>&lt; _Tp, _Alloc &gt; &amp;__lx, const <code>forward_list</code>&lt; _Tp, _Alloc &gt; &amp;__ly) </p>
<p> template&lt;typename _Value , typename _Hash , typename _Pred , typename _Alloc &gt; bool <code>operator==</code> (const <code>unordered_multiset</code>&lt; _Value, _Hash, _Pred, _Alloc &gt; &amp;__x, const <code>unordered_multiset</code>&lt; _Value, _Hash, _Pred, _Alloc &gt; &amp;__y) </p>
<p> template&lt;typename _Key , typename _Tp , typename _Hash , typename _Pred , typename _Alloc &gt; bool <code>operator==</code> (const <code>unordered_multimap</code>&lt; _Key, _Tp, _Hash, _Pred, _Alloc &gt; &amp;__x, const <code>unordered_multimap</code>&lt; _Key, _Tp, _Hash, _Pred, _Alloc &gt; &amp;__y) </p>
<p> template&lt;typename _Key , typename _Compare , typename _Allocator &gt; bool <code>operator&gt;</code> (const <code>multiset</code>&lt; _Key, _Compare, _Allocator &gt; &amp;__lhs, const <code>multiset</code>&lt; _Key, _Compare, _Allocator &gt; &amp;__rhs) </p>
<p> template&lt;typename _Key , typename _Compare , typename _Allocator &gt; bool <code>operator&gt;</code> (const <code>set</code>&lt; _Key, _Compare, _Allocator &gt; &amp;__lhs, const <code>set</code>&lt; _Key, _Compare, _Allocator &gt; &amp;__rhs) </p>
<p> template&lt;typename _Key , typename _Tp , typename _Compare , typename _Allocator &gt; bool <code>operator&gt;</code> (const <code>multimap</code>&lt; _Key, _Tp, _Compare, _Allocator &gt; &amp;__lhs, const <code>multimap</code>&lt; _Key, _Tp, _Compare, _Allocator &gt; &amp;__rhs) </p>
<p> template&lt;typename _Key , typename _Tp , typename _Compare , typename _Allocator &gt; bool <code>operator&gt;</code> (const <code>map</code>&lt; _Key, _Tp, _Compare, _Allocator &gt; &amp;__lhs, const <code>map</code>&lt; _Key, _Tp, _Compare, _Allocator &gt; &amp;__rhs) </p>
<p> template&lt;typename _Tp , typename _Alloc &gt; bool <code>operator&gt;</code> (const <code>deque</code>&lt; _Tp, _Alloc &gt; &amp;__lhs, const <code>deque</code>&lt; _Tp, _Alloc &gt; &amp;__rhs) </p>
<p> template&lt;typename _Tp , typename _Alloc &gt; bool <code>operator&gt;</code> (const <code>vector</code>&lt; _Tp, _Alloc &gt; &amp;__lhs, const <code>vector</code>&lt; _Tp, _Alloc &gt; &amp;__rhs) </p>
<p> template&lt;typename _Tp , typename _Alloc &gt; bool <code>operator&gt;</code> (const <code>list</code>&lt; _Tp, _Alloc &gt; &amp;__lhs, const <code>list</code>&lt; _Tp, _Alloc &gt; &amp;__rhs) </p>
<p> template&lt;typename _Tp , typename _Alloc &gt; bool <code>operator&gt;</code> (const <code>forward_list</code>&lt; _Tp, _Alloc &gt; &amp;__lx, const <code>forward_list</code>&lt; _Tp, _Alloc &gt; &amp;__ly) </p>
<p> template&lt;typename _Key , typename _Compare , typename _Allocator &gt; bool <code>operator&gt;=</code> (const <code>multiset</code>&lt; _Key, _Compare, _Allocator &gt; &amp;__lhs, const <code>multiset</code>&lt; _Key, _Compare, _Allocator &gt; &amp;__rhs) </p>
<p> template&lt;typename _Key , typename _Compare , typename _Allocator &gt; bool <code>operator&gt;=</code> (const <code>set</code>&lt; _Key, _Compare, _Allocator &gt; &amp;__lhs, const <code>set</code>&lt; _Key, _Compare, _Allocator &gt; &amp;__rhs) </p>
<p> template&lt;typename _Key , typename _Tp , typename _Compare , typename _Allocator &gt; bool <code>operator&gt;=</code> (const <code>multimap</code>&lt; _Key, _Tp, _Compare, _Allocator &gt; &amp;__lhs, const <code>multimap</code>&lt; _Key, _Tp, _Compare, _Allocator &gt; &amp;__rhs) </p>
<p> template&lt;typename _Key , typename _Tp , typename _Compare , typename _Allocator &gt; bool <code>operator&gt;=</code> (const <code>map</code>&lt; _Key, _Tp, _Compare, _Allocator &gt; &amp;__lhs, const <code>map</code>&lt; _Key, _Tp, _Compare, _Allocator &gt; &amp;__rhs) </p>
<p> template&lt;typename _Tp , typename _Alloc &gt; bool <code>operator&gt;=</code> (const <code>deque</code>&lt; _Tp, _Alloc &gt; &amp;__lhs, const <code>deque</code>&lt; _Tp, _Alloc &gt; &amp;__rhs) </p>
<p> template&lt;typename _Tp , typename _Alloc &gt; bool <code>operator&gt;=</code> (const <code>vector</code>&lt; _Tp, _Alloc &gt; &amp;__lhs, const <code>vector</code>&lt; _Tp, _Alloc &gt; &amp;__rhs) </p>
<p> template&lt;typename _Tp , typename _Alloc &gt; bool <code>operator&gt;=</code> (const <code>list</code>&lt; _Tp, _Alloc &gt; &amp;__lhs, const <code>list</code>&lt; _Tp, _Alloc &gt; &amp;__rhs) </p>
<p> template&lt;typename _Tp , typename _Alloc &gt; bool <code>operator&gt;=</code> (const <code>forward_list</code>&lt; _Tp, _Alloc &gt; &amp;__lx, const <code>forward_list</code>&lt; _Tp, _Alloc &gt; &amp;__ly) </p>
<p> template&lt;typename _CharT , typename _Traits , size_t _Nb&gt; <code>std::basic_istream</code>&lt; _CharT,<br />
 _Traits &gt; &amp; <code>operator&gt;&gt;</code> (<code>std::basic_istream</code>&lt; _CharT, _Traits &gt; &amp;__is, <code>bitset</code>&lt; _Nb &gt; &amp;__x)&quot; </p>
<p> template&lt;size_t _Nb&gt; <code>bitset</code>&lt; _Nb &gt; <code>operator^</code> (const <code>bitset</code>&lt; _Nb &gt; &amp;__x, const <code>bitset</code>&lt; _Nb &gt; &amp;__y) noexcept </p>
<p> template&lt;size_t _Nb&gt; <code>bitset</code>&lt; _Nb &gt; <code>operator|</code> (const <code>bitset</code>&lt; _Nb &gt; &amp;__x, const <code>bitset</code>&lt; _Nb &gt; &amp;__y) noexcept </p>
<p> template&lt;typename _Value , typename _Hash , typename _Pred , typename _Alloc &gt; void <code>swap</code> (<code>unordered_set</code>&lt; _Value, _Hash, _Pred, _Alloc &gt; &amp;__x, <code>unordered_set</code>&lt; _Value, _Hash, _Pred, _Alloc &gt; &amp;__y) </p>
<p> template&lt;typename _Key , typename _Compare , typename _Allocator &gt; void <code>swap</code> (<code>multiset</code>&lt; _Key, _Compare, _Allocator &gt; &amp;__x, <code>multiset</code>&lt; _Key, _Compare, _Allocator &gt; &amp;__y) </p>
<p> template&lt;typename _Key , typename _Tp , typename _Hash , typename _Pred , typename _Alloc &gt; void <code>swap</code> (<code>unordered_map</code>&lt; _Key, _Tp, _Hash, _Pred, _Alloc &gt; &amp;__x, <code>unordered_map</code>&lt; _Key, _Tp, _Hash, _Pred, _Alloc &gt; &amp;__y) </p>
<p> template&lt;typename _Key , typename _Compare , typename _Allocator &gt; void <code>swap</code> (<code>set</code>&lt; _Key, _Compare, _Allocator &gt; &amp;__x, <code>set</code>&lt; _Key, _Compare, _Allocator &gt; &amp;__y) </p>
<p> template&lt;typename _Key , typename _Tp , typename _Compare , typename _Allocator &gt; void <code>swap</code> (<code>multimap</code>&lt; _Key, _Tp, _Compare, _Allocator &gt; &amp;__lhs, <code>multimap</code>&lt; _Key, _Tp, _Compare, _Allocator &gt; &amp;__rhs) </p>
<p> template&lt;typename _Key , typename _Tp , typename _Compare , typename _Allocator &gt; void <code>swap</code> (<code>map</code>&lt; _Key, _Tp, _Compare, _Allocator &gt; &amp;__lhs, <code>map</code>&lt; _Key, _Tp, _Compare, _Allocator &gt; &amp;__rhs) </p>
<p> template&lt;typename _Tp , typename _Alloc &gt; void <code>swap</code> (<code>deque</code>&lt; _Tp, _Alloc &gt; &amp;__lhs, <code>deque</code>&lt; _Tp, _Alloc &gt; &amp;__rhs) </p>
<p> template&lt;typename _Tp , typename _Alloc &gt; void <code>swap</code> (<code>vector</code>&lt; _Tp, _Alloc &gt; &amp;__lhs, <code>vector</code>&lt; _Tp, _Alloc &gt; &amp;__rhs) </p>
<p> template&lt;typename _Tp , typename _Alloc &gt; void <code>swap</code> (<code>list</code>&lt; _Tp, _Alloc &gt; &amp;__lhs, <code>list</code>&lt; _Tp, _Alloc &gt; &amp;__rhs) </p>
<p> template&lt;typename _Tp , typename _Alloc &gt; void <code>swap</code> (<code>forward_list</code>&lt; _Tp, _Alloc &gt; &amp;__lx, <code>forward_list</code>&lt; _Tp, _Alloc &gt; &amp;__ly) </p>
<p> template&lt;typename _Value , typename _Hash , typename _Pred , typename _Alloc &gt; void <code>swap</code> (<code>unordered_multiset</code>&lt; _Value, _Hash, _Pred, _Alloc &gt; &amp;__x, <code>unordered_multiset</code>&lt; _Value, _Hash, _Pred, _Alloc &gt; &amp;__y) </p>
<p> template&lt;typename _Key , typename _Tp , typename _Hash , typename _Pred , typename _Alloc &gt; void <code>swap</code> (<code>unordered_multimap</code>&lt; _Key, _Tp, _Hash, _Pred, _Alloc &gt; &amp;__x, <code>unordered_multimap</code>&lt; _Key, _Tp, _Hash, _Pred, _Alloc &gt; &amp;__y)</p>
<h2>Detailed Description</h2>
<p>GNU debug code, replaces standard behavior with debug behavior. </p>
<p> Macros and namespaces used by the implementation outside of debug wrappers to verify certain properties. The __glibcxx_requires_xxx macros are merely wrappers around the __glibcxx_check_xxx wrappers when we are compiling with debug mode, but disappear when we are in release mode so that there is no checking performed in, e.g., the standard library algorithms.</p>
<h2>Function Documentation</h2>
<h3>template&lt;typename _Tp , typename _Alloc &gt; bool std::__debug::operator&lt;= (const forward_list&lt; _Tp, _Alloc &gt; &amp;__lx, const forward_list&lt; _Tp, _Alloc &gt; &amp;__ly) [inline]</h3>
<p>Based on operator&lt;. </p>
<p> Definition at line 768 of file debug/forward_list.</p>
<h3>template&lt;typename _Tp , typename _Alloc &gt; bool std::__debug::operator&gt; (const forward_list&lt; _Tp, _Alloc &gt; &amp;__lx, const forward_list&lt; _Tp, _Alloc &gt; &amp;__ly) [inline]</h3>
<p>Based on operator&lt;. </p>
<p> Definition at line 754 of file debug/forward_list.</p>
<h3>template&lt;typename _Tp , typename _Alloc &gt; bool std::__debug::operator&gt;= (const forward_list&lt; _Tp, _Alloc &gt; &amp;__lx, const forward_list&lt; _Tp, _Alloc &gt; &amp;__ly) [inline]</h3>
<p>Based on operator&lt;. </p>
<p> Definition at line 761 of file debug/forward_list.</p>
<h3>template&lt;typename _Tp , typename _Alloc &gt; void std::__debug::swap (forward_list&lt; _Tp, _Alloc &gt; &amp;__lx, forward_list&lt; _Tp, _Alloc &gt; &amp;__ly) [inline]</h3>
<p>See std::forward_list::swap(). </p>
<p> Definition at line 775 of file debug/forward_list. </p>
<p> References std::swap().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
