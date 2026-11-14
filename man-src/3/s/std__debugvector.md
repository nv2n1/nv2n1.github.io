---
title: "std__debugvector(3)"
name: "std__debugvector"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std__debugvector/"
description: "std::__debug::vector< _Tp, _Allocator > –"
---

<p>std::__debug::vector&lt; _Tp, _Allocator &gt; &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits vector&lt; _Tp, _Allocator &gt;, and <code>__gnu_debug::_Safe_sequence&lt; vector&lt; _Tp, _Allocator &gt; &gt;</code>.</p>
<h3>Public Types</h3>
<p>typedef _Allocator <code>allocator_type</code> </p>
<p> typedef<br />
 <code>__gnu_debug::_Safe_iterator</code><br />
 &lt; <code>_Base_const_iterator</code>, <code>vector</code> &gt; <code>const_iterator</code>&quot; </p>
<p> typedef _Base::const_pointer <code>const_pointer</code> </p>
<p> typedef _Base::const_reference <code>const_reference</code> </p>
<p> typedef <code>std::reverse_iterator</code><br />
 &lt; <code>const_iterator</code> &gt; <code>const_reverse_iterator</code>&quot; </p>
<p> typedef _Base::difference_type <code>difference_type</code> </p>
<p> typedef<br />
 <code>__gnu_debug::_Safe_iterator</code><br />
 &lt; <code>_Base_iterator</code>, <code>vector</code> &gt; <code>iterator</code>&quot; </p>
<p> typedef _Base::pointer <code>pointer</code> </p>
<p> typedef _Base::reference <code>reference</code> </p>
<p> typedef <code>std::reverse_iterator</code><br />
 &lt; <code>iterator</code> &gt; <code>reverse_iterator</code>&quot; </p>
<p> typedef _Base::size_type <code>size_type</code> </p>
<p> typedef _Tp <code>value_type</code></p>
<h3>Public Member Functions</h3>
<pre><code>vector (size_type __n, const _Tp &amp;__value, const _Allocator &amp;__a=_Allocator())



template&lt;class _InputIterator , typename  = std::_RequireInputIter&lt;_InputIterator&gt;&gt; vector (_InputIterator __first, _InputIterator __last, const _Allocator &amp;__a=_Allocator())



vector (const vector &amp;__x)



vector (const _Base &amp;__x)



vector (vector &amp;&amp;__x) noexcept



vector (const vector &amp;__x, const allocator_type &amp;__a)



vector (vector &amp;&amp;__x, const allocator_type &amp;__a)



vector (initializer_list&lt; value_type &gt; __l, const allocator_type &amp;__a=allocator_type())



_Base::swap (__x)



void _M_attach (_Safe_iterator_base *__it, bool __constant)



void _M_attach_single (_Safe_iterator_base *__it, bool __constant)  throw ()



_Base &amp; _M_base () noexcept



const _Base &amp; _M_base () const noexcept



void _M_detach (_Safe_iterator_base *__it)



void _M_detach_single (_Safe_iterator_base *__it)  throw ()



_M_guaranteed_capacity (0)



_M_guaranteed_capacity (__n)



void _M_invalidate_all () const



void _M_invalidate_if (_Predicate __pred)



this _M_swap (__x)



void _M_transfer_from_if (_Safe_sequence &amp;__from, _Predicate __pred)



template&lt;typename _InputIterator , typename  = std::_RequireInputIter&lt;_InputIterator&gt;&gt; void assign (_InputIterator __first, _InputIterator __last)



void assign (size_type __n, const _Tp &amp;__u)



void assign (initializer_list&lt; value_type &gt; __l)



reference back ()



const_reference back () const



iterator begin () noexcept



const_iterator begin () const noexcept



size_type capacity () const noexcept



const_iterator cbegin () const noexcept



const_iterator cend () const noexcept



void clear () noexcept



const_reverse_iterator crbegin () const noexcept



const_reverse_iterator crend () const noexcept



template&lt;typename... _Args&gt; iterator emplace (iterator __position, _Args &amp;&amp;...__args)



template&lt;typename... _Args&gt; void emplace_back (_Args &amp;&amp;...__args)



iterator end () noexcept



const_iterator end () const noexcept



iterator erase (iterator __position)



iterator erase (iterator __first, iterator __last)



reference front ()



const_reference front () const



iterator insert (iterator __position, const _Tp &amp;__x)



template&lt;typename _Up  = _Tp&gt; __gnu_cxx::__enable_if


&lt;!std::__are_same&lt; _Up, bool &gt;

::__value, iterator &gt;::__type insert (iterator __position, _Tp &amp;&amp;__x)&quot;


void insert (iterator __position, initializer_list&lt; value_type &gt; __l)



void insert (iterator __position, size_type __n, const _Tp &amp;__x)



template&lt;class _InputIterator , typename  = std::_RequireInputIter&lt;_InputIterator&gt;&gt; void insert (iterator __position, _InputIterator __first, _InputIterator __last)



vector &amp; operator= (const vector &amp;__x)



vector &amp; operator= (vector &amp;&amp;__x) noexcept(_Alloc_traits::_S_nothrow_move())



vector &amp; operator= (initializer_list&lt; value_type &gt; __l)



reference operator[] (size_type __n)



const_reference operator[] (size_type __n) const



void pop_back ()



void push_back (const _Tp &amp;__x)



template&lt;typename _Up  = _Tp&gt; __gnu_cxx::__enable_if


&lt;!std::__are_same&lt; _Up, bool &gt;

::__value, void &gt;::__type push_back (_Tp &amp;&amp;__x)&quot;


reverse_iterator rbegin () noexcept



const_reverse_iterator rbegin () const noexcept



reverse_iterator rend () noexcept



const_reverse_iterator rend () const noexcept



void reserve (size_type __n)



void resize (size_type __sz)



void resize (size_type __sz, const _Tp &amp;__c)



void shrink_to_fit ()



std::swap (_M_guaranteed_capacity, __x._M_guaranteed_capacity)



Public Attributes</code></pre>
<p> <code>__a</code> </p>
<p> <code>__pad0__</code>: <code>_Base</code>(__a) </p>
<p> <code>__pad1__</code>: <code>_Base</code>(__n </p>
<p> _Safe_iterator_base * <code>_M_const_iterators</code> </p>
<p> _Safe_iterator_base * <code>_M_iterators</code> </p>
<p> unsigned int <code>_M_version</code> </p>
<p> <code>void</code></p>
<h3>Protected Member Functions</h3>
<pre><code>void _M_detach_all ()



void _M_detach_singular ()



__gnu_cxx::__mutex &amp; _M_get_mutex ()  throw ()



void _M_revalidate_singular ()



void _M_swap (_Safe_sequence_base &amp;__x)</code></pre>
<h2>Detailed Description</h2>
<h3>template&lt;typename _Tp, typename _Allocator = std::allocator&lt;_Tp&gt;&gt;class std::__debug::vector&lt; _Tp, _Allocator &gt;</h3>
<p>Class std::vector with safety/checking/debug instrumentation. </p>
<p> Definition at line 44 of file debug/vector.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>template&lt;typename _Tp, typename _Allocator = std::allocator&lt;_Tp&gt;&gt; <code>std::__debug::vector</code>&lt; _Tp, _Allocator &gt;::<code>vector</code> (const <code>_Base</code> &amp;__x) [inline]</h3>
<p>Construction from a release-mode vector. </p>
<p> Definition at line 115 of file debug/vector.</p>
<h2>Member Function Documentation</h2>
<h3>void __gnu_debug::_Safe_sequence_base::_M_attach (<code>_Safe_iterator_base</code> *__it, bool__constant) [inherited]</h3>
<p>Attach an iterator to this sequence.</p>
<h3>void __gnu_debug::_Safe_sequence_base::_M_attach_single (<code>_Safe_iterator_base</code> *__it, bool__constant) [inherited]</h3>
<p>Likewise but not thread safe.</p>
<h3>void __gnu_debug::_Safe_sequence_base::_M_detach (<code>_Safe_iterator_base</code> *__it) [inherited]</h3>
<p>Detach an iterator from this sequence</p>
<h3>void __gnu_debug::_Safe_sequence_base::_M_detach_all () [protected], [inherited]</h3>
<p>Detach all iterators, leaving them singular. </p>
<p> Referenced by __gnu_debug::_Safe_sequence_base::~_Safe_sequence_base().</p>
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
<h3>void <code>__gnu_debug::_Safe_sequence</code>&lt; <code>vector</code>&lt; _Tp, _Allocator &gt; &gt;::_M_invalidate_if (_Predicate__pred) [inherited]</h3>
<p>Invalidates all iterators x that reference this sequence, are not singular, and for which __pred(x) returns true. __pred will be invoked with the normal iterators nested in the safe ones.</p>
<h3>void __gnu_debug::_Safe_sequence_base::_M_revalidate_singular () [protected], [inherited]</h3>
<p>Revalidates all attached singular iterators. This method may be used to validate iterators that were invalidated before (but for some reason, such as an exception, need to become valid again).</p>
<h3>void __gnu_debug::_Safe_sequence_base::_M_swap (<code>_Safe_sequence_base</code> &amp;__x) [protected], [inherited]</h3>
<p>Swap this sequence with the given sequence. This operation also swaps ownership of the iterators, so that when the operation is complete all iterators that originally referenced one container now reference the other container.</p>
<h3>void <code>__gnu_debug::_Safe_sequence</code>&lt; <code>vector</code>&lt; _Tp, _Allocator &gt; &gt;::_M_transfer_from_if (<code>_Safe_sequence</code>&lt; <code>vector</code>&lt; _Tp, _Allocator &gt; &gt; &amp;__from, _Predicate__pred) [inherited]</h3>
<p>Transfers all iterators x that reference from sequence, are not singular, and for which __pred(x) returns true. __pred will be invoked with the normal iterators nested in the safe ones.</p>
<h2>Member Data Documentation</h2>
<h3>_Safe_iterator_base* __gnu_debug::_Safe_sequence_base::_M_const_iterators [inherited]</h3>
<p>The list of constant iterators that reference this container. </p>
<p> Definition at line 184 of file safe_base.h. </p>
<p> Referenced by __gnu_debug::_Safe_sequence&lt; _Sequence &gt;::_M_transfer_from_if().</p>
<h3>_Safe_iterator_base* __gnu_debug::_Safe_sequence_base::_M_iterators [inherited]</h3>
<p>The list of mutable iterators that reference this container. </p>
<p> Definition at line 181 of file safe_base.h. </p>
<p> Referenced by __gnu_debug::_Safe_sequence&lt; _Sequence &gt;::_M_transfer_from_if().</p>
<h3>unsigned int __gnu_debug::_Safe_sequence_base::_M_version [mutable], [inherited]</h3>
<p>The container version number. This number may never be 0. </p>
<p> Definition at line 187 of file safe_base.h. </p>
<p> Referenced by __gnu_debug::_Safe_sequence_base::_M_invalidate_all(), and __gnu_debug::_Safe_sequence&lt; _Sequence &gt;::_M_transfer_from_if().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
