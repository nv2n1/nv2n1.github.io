---
title: "std__profileunordered_map(3)"
name: "std__profileunordered_map"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std__profileunordered_map/"
description: "std::__profile::unordered_map< _Key, _Tp, _Hash, _Pred, _Alloc > –"
---

<p>std::__profile::unordered_map&lt; _Key, _Tp, _Hash, _Pred, _Alloc &gt; &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits unordered_map&lt; _Key, _Tp, _Hash, _Pred, _Alloc &gt;, and std::__profile::_Unordered_profile&lt; _UnorderedCont, _Unique_keys &gt;.</p>
<h3>Public Types</h3>
<p>typedef _Base::allocator_type <code>allocator_type</code> </p>
<p> typedef _Base::const_iterator <code>const_iterator</code> </p>
<p> typedef _Base::const_reference <code>const_reference</code> </p>
<p> typedef _Base::difference_type <code>difference_type</code> </p>
<p> typedef _Base::hasher <code>hasher</code> </p>
<p> typedef _Base::iterator <code>iterator</code> </p>
<p> typedef _Base::key_equal <code>key_equal</code> </p>
<p> typedef _Base::key_type <code>key_type</code> </p>
<p> typedef _Base::mapped_type <code>mapped_type</code> </p>
<p> typedef _Base::reference <code>reference</code> </p>
<p> typedef _Base::size_type <code>size_type</code> </p>
<p> typedef _Base::value_type <code>value_type</code></p>
<h3>Public Member Functions</h3>
<pre><code>unordered_map (size_type __n=10, const hasher &amp;__hf=hasher(), const key_equal &amp;__eql=key_equal(), const allocator_type &amp;__a=allocator_type())



template&lt;typename _InputIterator &gt; unordered_map (_InputIterator __f, _InputIterator __l, size_type __n=0, const hasher &amp;__hf=hasher(), const key_equal &amp;__eql=key_equal(), const allocator_type &amp;__a=allocator_type())



unordered_map (const unordered_map &amp;)=default



unordered_map (const _Base &amp;__x)



unordered_map (unordered_map &amp;&amp;)=default



unordered_map (initializer_list&lt; value_type &gt; __l, size_type __n=0, const hasher &amp;__hf=hasher(), const key_equal &amp;__eql=key_equal(), const allocator_type &amp;__a=allocator_type())



void clear () noexcept



template&lt;typename... _Args&gt; std::pair&lt; iterator, bool &gt; emplace (_Args &amp;&amp;...__args)



template&lt;typename... _Args&gt; iterator emplace_hint (const_iterator __it, _Args &amp;&amp;...__args)



void insert (std::initializer_list&lt; value_type &gt; __l)



std::pair&lt; iterator, bool &gt; insert (const value_type &amp;__obj)



iterator insert (const_iterator __iter, const value_type &amp;__v)



template&lt;typename _Pair , typename  = typename std::enable_if&lt;std::is_constructible&lt;value_type,    _Pair&amp;&amp;&gt;::value&gt;::type&gt; std::pair&lt; iterator, bool &gt; insert (_Pair &amp;&amp;__obj)



template&lt;typename _Pair , typename  = typename std::enable_if&lt;std::is_constructible&lt;value_type,    _Pair&amp;&amp;&gt;::value&gt;::type&gt; iterator insert (const_iterator __iter, _Pair &amp;&amp;__v)



template&lt;typename _InputIter &gt; void insert (_InputIter __first, _InputIter __last)



unordered_map &amp; operator= (const unordered_map &amp;)=default



unordered_map &amp; operator= (unordered_map &amp;&amp;)=default



unordered_map &amp; operator= (initializer_list&lt; value_type &gt; __l)



mapped_type &amp; operator[] (const _Key &amp;__k)



mapped_type &amp; operator[] (_Key &amp;&amp;__k)



void rehash (size_type __n)



void swap (unordered_map &amp;__x)



Protected Member Functions
void _M_profile_destruct ()</code></pre>
<h2>Detailed Description</h2>
<h3>template&lt;typename _Key, typename _Tp, typename _Hash = std::hash&lt;_Key&gt;, typename _Pred = std::equal_to&lt;_Key&gt;, typename _Alloc = std::allocator&lt;std::pair&lt;const _Key, _Tp&gt; &gt;&gt;class std::__profile::unordered_map&lt; _Key, _Tp, _Hash, _Pred, _Alloc &gt;</h3>
<p>Class std::unordered_map wrapper with performance instrumentation. </p>
<p> Definition at line 51 of file profile/unordered_map.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
