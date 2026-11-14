---
title: "std__profilemultimap(3)"
name: "std__profilemultimap"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std__profilemultimap/"
description: "std::__profile::multimap< _Key, _Tp, _Compare, _Allocator > –"
---

<p>std::__profile::multimap&lt; _Key, _Tp, _Compare, _Allocator &gt; &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits multimap&lt; _Key, _Tp, _Compare, _Allocator &gt;.</p>
<h3>Public Types</h3>
<p>typedef _Allocator <code>allocator_type</code> </p>
<p> typedef _Base::const_iterator <code>const_iterator</code> </p>
<p> typedef _Base::const_pointer <code>const_pointer</code> </p>
<p> typedef _Base::const_reference <code>const_reference</code> </p>
<p> typedef<br />
 _Base::const_reverse_iterator <code>const_reverse_iterator</code>&quot; </p>
<p> typedef _Base::difference_type <code>difference_type</code> </p>
<p> typedef _Base::iterator <code>iterator</code> </p>
<p> typedef _Compare <code>key_compare</code> </p>
<p> typedef _Key <code>key_type</code> </p>
<p> typedef _Tp <code>mapped_type</code> </p>
<p> typedef _Base::pointer <code>pointer</code> </p>
<p> typedef _Base::reference <code>reference</code> </p>
<p> typedef _Base::reverse_iterator <code>reverse_iterator</code> </p>
<p> typedef _Base::size_type <code>size_type</code> </p>
<p> typedef <code>std::pair</code>&lt; const _Key,<br />
 _Tp &gt; <code>value_type</code>&quot;</p>
<h3>Public Member Functions</h3>
<pre><code>multimap (const _Compare &amp;__comp=_Compare(), const _Allocator &amp;__a=_Allocator())



template&lt;typename _InputIterator , typename  = std::_RequireInputIter&lt;_InputIterator&gt;&gt; multimap (_InputIterator __first, _InputIterator __last, const _Compare &amp;__comp=_Compare(), const _Allocator &amp;__a=_Allocator())



multimap (const multimap &amp;__x)



multimap (const _Base &amp;__x)



multimap (initializer_list&lt; value_type &gt; __l, const _Compare &amp;__c=_Compare(), const allocator_type &amp;__a=allocator_type())



_Base &amp; _M_base () noexcept



const _Base &amp; _M_base () const noexcept



iterator begin () noexcept



const_iterator begin () const noexcept



const_iterator cbegin () const noexcept



const_iterator cend () const noexcept



void clear () noexcept



const_reverse_iterator crbegin () const noexcept



const_reverse_iterator crend () const noexcept



template&lt;typename... _Args&gt; iterator emplace (_Args &amp;&amp;...__args)



template&lt;typename... _Args&gt; iterator emplace_hint (const_iterator __pos, _Args &amp;&amp;...__args)



iterator end () noexcept



const_iterator end () const noexcept



std::pair&lt; iterator, iterator &gt; equal_range (const key_type &amp;__x)



std::pair&lt; const_iterator,


const_iterator &gt; equal_range (const key_type &amp;__x) const &quot;


iterator erase (const_iterator __position)



iterator erase (iterator __position)



size_type erase (const key_type &amp;__x)



iterator erase (const_iterator __first, const_iterator __last)



iterator find (const key_type &amp;__x)



const_iterator find (const key_type &amp;__x) const



iterator insert (const value_type &amp;__x)



template&lt;typename _Pair , typename  = typename std::enable_if&lt;std::is_constructible&lt;value_type,    _Pair&amp;&amp;&gt;::value&gt;::type&gt; iterator insert (_Pair &amp;&amp;__x)



void insert (std::initializer_list&lt; value_type &gt; __list)



template&lt;typename _Pair , typename  = typename std::enable_if&lt;std::is_constructible&lt;value_type,    _Pair&amp;&amp;&gt;::value&gt;::type&gt; iterator insert (const_iterator __position, _Pair &amp;&amp;__x)



template&lt;typename _InputIterator , typename  = std::_RequireInputIter&lt;_InputIterator&gt;&gt; void insert (_InputIterator __first, _InputIterator __last)



iterator lower_bound (const key_type &amp;__x)



const_iterator lower_bound (const key_type &amp;__x) const



noexcept (is_nothrow_copy_constructible&lt; _Compare &gt;::value)



multimap &amp; operator= (const multimap &amp;__x)



multimap &amp; operator= (multimap &amp;&amp;__x)



multimap &amp; operator= (initializer_list&lt; value_type &gt; __l)



reverse_iterator rbegin () noexcept



const_reverse_iterator rbegin () const noexcept



reverse_iterator rend () noexcept



const_reverse_iterator rend () const noexcept



void swap (multimap &amp;__x)



iterator upper_bound (const key_type &amp;__x)



const_iterator upper_bound (const key_type &amp;__x) const



Public Attributes</code></pre>
<p> <code>iterator</code></p>
<h2>Detailed Description</h2>
<h3>template&lt;typename _Key, typename _Tp, typename _Compare = std::less&lt;_Key&gt;, typename _Allocator = std::allocator&lt;std::pair&lt;const _Key, _Tp&gt; &gt;&gt;class std::__profile::multimap&lt; _Key, _Tp, _Compare, _Allocator &gt;</h3>
<p>Class std::multimap wrapper with performance instrumentation. </p>
<p> Definition at line 41 of file profile/multimap.h.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
