---
title: "std__debugunordered_set(3)"
name: "std__debugunordered_set"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std__debugunordered_set/"
description: "std::__debug::unordered_set< _Value, _Hash, _Pred, _Alloc > –"
---

<p>std::__debug::unordered_set&lt; _Value, _Hash, _Pred, _Alloc &gt; &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits unordered_set&lt; _Value, _Hash, _Pred, _Alloc &gt;, and <code>__gnu_debug::_Safe_unordered_container&lt; unordered_set&lt; _Value, _Hash, _Pred, _Alloc &gt; &gt;</code>.</p>
<h3>Public Types</h3>
<p>typedef _Base::allocator_type <code>allocator_type</code> </p>
<p> typedef<br />
 <code>__gnu_debug::_Safe_iterator</code><br />
 &lt; _Base_const_iterator,<br />
 <code>unordered_set</code> &gt; <code>const_iterator</code>&quot; </p>
<p> typedef<br />
 <code>__gnu_debug::_Safe_local_iterator</code><br />
 &lt; _Base_const_local_iterator,<br />
 <code>unordered_set</code> &gt; <code>const_local_iterator</code>&quot; </p>
<p> typedef _Base::hasher <code>hasher</code> </p>
<p> typedef<br />
 <code>__gnu_debug::_Safe_iterator</code><br />
 &lt; _Base_iterator,<br />
 <code>unordered_set</code> &gt; <code>iterator</code>&quot; </p>
<p> typedef _Base::key_equal <code>key_equal</code> </p>
<p> typedef _Base::key_type <code>key_type</code> </p>
<p> typedef<br />
 <code>__gnu_debug::_Safe_local_iterator</code><br />
 &lt; _Base_local_iterator,<br />
 <code>unordered_set</code> &gt; <code>local_iterator</code>&quot; </p>
<p> typedef _Base::size_type <code>size_type</code> </p>
<p> typedef _Base::value_type <code>value_type</code></p>
<h3>Public Member Functions</h3>
<pre><code>unordered_set (size_type __n=10, const hasher &amp;__hf=hasher(), const key_equal &amp;__eql=key_equal(), const allocator_type &amp;__a=allocator_type())



template&lt;typename _InputIterator &gt; unordered_set (_InputIterator __first, _InputIterator __last, size_type __n=0, const hasher &amp;__hf=hasher(), const key_equal &amp;__eql=key_equal(), const allocator_type &amp;__a=allocator_type())



unordered_set (const unordered_set &amp;__x)=default



unordered_set (const _Base &amp;__x)



unordered_set (unordered_set &amp;&amp;__x)=default



unordered_set (initializer_list&lt; value_type &gt; __l, size_type __n=0, const hasher &amp;__hf=hasher(), const key_equal &amp;__eql=key_equal(), const allocator_type &amp;__a=allocator_type())



void _M_attach (_Safe_iterator_base *__it, bool __constant)



void _M_attach_local (_Safe_iterator_base *__it, bool __constant)



void _M_attach_local_single (_Safe_iterator_base *__it, bool __constant)  throw ()



void _M_attach_single (_Safe_iterator_base *__it, bool __constant)  throw ()



_Base &amp; _M_base () noexcept



const _Base &amp; _M_base () const noexcept



void _M_detach (_Safe_iterator_base *__it)



void _M_detach_local (_Safe_iterator_base *__it)



void _M_detach_local_single (_Safe_iterator_base *__it)  throw ()



void _M_detach_single (_Safe_iterator_base *__it)  throw ()



void _M_invalidate_all () const



void _M_invalidate_if (_Predicate __pred)



void _M_invalidate_local_if (_Predicate __pred)



iterator begin () noexcept



const_iterator begin () const noexcept



local_iterator begin (size_type __b)



const_local_iterator begin (size_type __b) const



size_type bucket_size (size_type __b) const



const_iterator cbegin () const noexcept



const_local_iterator cbegin (size_type __b) const



const_iterator cend () const noexcept



const_local_iterator cend (size_type __b) const



void clear () noexcept



template&lt;typename... _Args&gt; std::pair&lt; iterator, bool &gt; emplace (_Args &amp;&amp;...__args)



template&lt;typename... _Args&gt; iterator emplace_hint (const_iterator __hint, _Args &amp;&amp;...__args)



iterator end () noexcept



const_iterator end () const noexcept



local_iterator end (size_type __b)



const_local_iterator end (size_type __b) const



std::pair&lt; iterator, iterator &gt; equal_range (const key_type &amp;__key)



std::pair&lt; const_iterator,


const_iterator &gt; equal_range (const key_type &amp;__key) const &quot;


size_type erase (const key_type &amp;__key)



iterator erase (const_iterator __it)



iterator erase (iterator __it)



iterator erase (const_iterator __first, const_iterator __last)



iterator find (const key_type &amp;__key)



const_iterator find (const key_type &amp;__key) const



std::pair&lt; iterator, bool &gt; insert (const value_type &amp;__obj)



iterator insert (const_iterator __hint, const value_type &amp;__obj)



std::pair&lt; iterator, bool &gt; insert (value_type &amp;&amp;__obj)



iterator insert (const_iterator __hint, value_type &amp;&amp;__obj)



void insert (std::initializer_list&lt; value_type &gt; __l)



template&lt;typename _InputIterator &gt; void insert (_InputIterator __first, _InputIterator __last)



float max_load_factor () const noexcept



void max_load_factor (float __f)



unordered_set &amp; operator= (const unordered_set &amp;__x)



unordered_set &amp; operator= (unordered_set &amp;&amp;__x)



unordered_set &amp; operator= (initializer_list&lt; value_type &gt; __l)



void swap (unordered_set &amp;__x)



Public Attributes</code></pre>
<p> _Safe_iterator_base * <code>_M_const_iterators</code> </p>
<p> _Safe_iterator_base * <code>_M_const_local_iterators</code> </p>
<p> _Safe_iterator_base * <code>_M_iterators</code> </p>
<p> _Safe_iterator_base * <code>_M_local_iterators</code> </p>
<p> unsigned int <code>_M_version</code></p>
<h3>Protected Member Functions</h3>
<pre><code>void _M_detach_all ()



void _M_detach_singular ()



__gnu_cxx::__mutex &amp; _M_get_mutex ()  throw ()



void _M_revalidate_singular ()



void _M_swap (_Safe_unordered_container_base &amp;__x)



void _M_swap (_Safe_sequence_base &amp;__x)



Protected Attributes</code></pre>
<p> noexcept <code>__pad0__</code>: _Safe_unordered_container_base() { } noexcept : _Safe_unordered_container_base() { this-&gt;<code>_M_swap</code>(__x)</p>
<h2>Detailed Description</h2>
<h3>template&lt;typename _Value, typename _Hash = std::hash&lt;_Value&gt;, typename _Pred = std::equal_to&lt;_Value&gt;, typename _Alloc = std::allocator&lt;_Value&gt;&gt;class std::__debug::unordered_set&lt; _Value, _Hash, _Pred, _Alloc &gt;</h3>
<p>Class std::unordered_set with safety/checking/debug instrumentation. </p>
<p> Definition at line 50 of file debug/unordered_set.</p>
<h2>Member Function Documentation</h2>
<h3>void __gnu_debug::_Safe_sequence_base::_M_attach (<code>_Safe_iterator_base</code> *__it, bool__constant) [inherited]</h3>
<p>Attach an iterator to this sequence.</p>
<h3>void __gnu_debug::_Safe_unordered_container_base::_M_attach_local (<code>_Safe_iterator_base</code> *__it, bool__constant) [inherited]</h3>
<p>Attach an iterator to this container.</p>
<h3>void __gnu_debug::_Safe_unordered_container_base::_M_attach_local_single (<code>_Safe_iterator_base</code> *__it, bool__constant) [inherited]</h3>
<p>Likewise but not thread safe.</p>
<h3>void __gnu_debug::_Safe_sequence_base::_M_attach_single (<code>_Safe_iterator_base</code> *__it, bool__constant) [inherited]</h3>
<p>Likewise but not thread safe.</p>
<h3>void __gnu_debug::_Safe_sequence_base::_M_detach (<code>_Safe_iterator_base</code> *__it) [inherited]</h3>
<p>Detach an iterator from this sequence</p>
<h3>void __gnu_debug::_Safe_unordered_container_base::_M_detach_all () [protected], [inherited]</h3>
<p>Detach all iterators, leaving them singular.</p>
<h3>void __gnu_debug::_Safe_unordered_container_base::_M_detach_local (<code>_Safe_iterator_base</code> *__it) [inherited]</h3>
<p>Detach an iterator from this container</p>
<h3>void __gnu_debug::_Safe_unordered_container_base::_M_detach_local_single (<code>_Safe_iterator_base</code> *__it) [inherited]</h3>
<p>Likewise but not thread safe.</p>
<h3>void __gnu_debug::_Safe_sequence_base::_M_detach_single (<code>_Safe_iterator_base</code> *__it) [inherited]</h3>
<p>Likewise but not thread safe.</p>
<h3>void __gnu_debug::_Safe_sequence_base::_M_detach_singular () [protected], [inherited]</h3>
<p>Detach all singular iterators. </p>
<p> <code>Postcondition:</code></p>
<dl>
<dd>for all iterators i attached to this sequence, i-&gt;_M_version == _M_version.</dl>
<h3>__gnu_cxx::__mutex&amp; __gnu_debug::_Safe_sequence_base::_M_get_mutex () [protected], [inherited]</h3>
<p>For use in _Safe_sequence. </p>
<p> Referenced by __gnu_debug::_Safe_sequence&lt; _Sequence &gt;::_M_transfer_from_if().</p>
<h3>void __gnu_debug::_Safe_sequence_base::_M_invalidate_all () const [inline], [inherited]</h3>
<p>Invalidates all iterators. </p>
<p> Definition at line 233 of file safe_base.h. </p>
<p> References __gnu_debug::_Safe_sequence_base::_M_version.</p>
<h3>void <code>__gnu_debug::_Safe_unordered_container</code>&lt; <code>unordered_set</code>&lt; _Value, _Hash, _Pred, _Alloc &gt; &gt;::_M_invalidate_if (_Predicate__pred) [inherited]</h3>
<p>Invalidates all iterators x that reference this container, are not singular, and for which __pred(x) returns true. __pred will be invoked with the normal iterators nested in the safe ones.</p>
<h3>void <code>__gnu_debug::_Safe_unordered_container</code>&lt; <code>unordered_set</code>&lt; _Value, _Hash, _Pred, _Alloc &gt; &gt;::_M_invalidate_local_if (_Predicate__pred) [inherited]</h3>
<p>Invalidates all local iterators x that reference this container, are not singular, and for which __pred(x) returns true. __pred will be invoked with the normal ilocal iterators nested in the safe ones.</p>
<h3>void __gnu_debug::_Safe_sequence_base::_M_revalidate_singular () [protected], [inherited]</h3>
<p>Revalidates all attached singular iterators. This method may be used to validate iterators that were invalidated before (but for some reason, such as an exception, need to become valid again).</p>
<h3>void __gnu_debug::_Safe_unordered_container_base::_M_swap (<code>_Safe_unordered_container_base</code> &amp;__x) [protected], [inherited]</h3>
<p>Swap this container with the given container. This operation also swaps ownership of the iterators, so that when the operation is complete all iterators that originally referenced one container now reference the other container.</p>
<h3>void __gnu_debug::_Safe_sequence_base::_M_swap (<code>_Safe_sequence_base</code> &amp;__x) [protected], [inherited]</h3>
<p>Swap this sequence with the given sequence. This operation also swaps ownership of the iterators, so that when the operation is complete all iterators that originally referenced one container now reference the other container.</p>
<h2>Member Data Documentation</h2>
<h3>_Safe_iterator_base* __gnu_debug::_Safe_sequence_base::_M_const_iterators [inherited]</h3>
<p>The list of constant iterators that reference this container. </p>
<p> Definition at line 184 of file safe_base.h. </p>
<p> Referenced by __gnu_debug::_Safe_sequence&lt; _Sequence &gt;::_M_transfer_from_if().</p>
<h3>_Safe_iterator_base* __gnu_debug::_Safe_unordered_container_base::_M_const_local_iterators [inherited]</h3>
<p>The list of constant local iterators that reference this container. </p>
<p> Definition at line 131 of file safe_unordered_base.h.</p>
<h3>_Safe_iterator_base* __gnu_debug::_Safe_sequence_base::_M_iterators [inherited]</h3>
<p>The list of mutable iterators that reference this container. </p>
<p> Definition at line 181 of file safe_base.h. </p>
<p> Referenced by __gnu_debug::_Safe_sequence&lt; _Sequence &gt;::_M_transfer_from_if().</p>
<h3>_Safe_iterator_base* __gnu_debug::_Safe_unordered_container_base::_M_local_iterators [inherited]</h3>
<p>The list of mutable local iterators that reference this container. </p>
<p> Definition at line 128 of file safe_unordered_base.h.</p>
<h3>unsigned int __gnu_debug::_Safe_sequence_base::_M_version [mutable], [inherited]</h3>
<p>The container version number. This number may never be 0. </p>
<p> Definition at line 187 of file safe_base.h. </p>
<p> Referenced by __gnu_debug::_Safe_sequence_base::_M_invalidate_all(), and __gnu_debug::_Safe_sequence&lt; _Sequence &gt;::_M_transfer_from_if().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
