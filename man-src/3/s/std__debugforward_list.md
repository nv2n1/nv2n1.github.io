---
title: "std__debugforward_list(3)"
name: "std__debugforward_list"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std__debugforward_list/"
description: "std::__debug::forward_list< _Tp, _Alloc > –"
---

<p>std::__debug::forward_list&lt; _Tp, _Alloc &gt; &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits forward_list&lt; _Tp, _Alloc &gt;, and <code>__gnu_debug::_Safe_sequence&lt; forward_list&lt; _Tp, _Alloc &gt; &gt;</code>.</p>
<h3>Public Types</h3>
<p>typedef _Alloc <code>allocator_type</code> </p>
<p> typedef<br />
 <code>__gnu_debug::_Safe_iterator</code><br />
 &lt; <code>_Base_const_iterator</code>,<br />
 <code>forward_list</code> &gt; <code>const_iterator</code>&quot; </p>
<p> typedef _Base::const_pointer <code>const_pointer</code> </p>
<p> typedef _Base::const_reference <code>const_reference</code> </p>
<p> typedef _Base::difference_type <code>difference_type</code> </p>
<p> typedef<br />
 <code>__gnu_debug::_Safe_iterator</code><br />
 &lt; <code>_Base_iterator</code>, <code>forward_list</code> &gt; <code>iterator</code>&quot; </p>
<p> typedef _Base::pointer <code>pointer</code> </p>
<p> typedef _Base::reference <code>reference</code> </p>
<p> typedef _Base::size_type <code>size_type</code> </p>
<p> typedef _Tp <code>value_type</code></p>
<h3>Public Member Functions</h3>
<p><code>_Base::swap</code> (__list) </p>
<p> void <code>_M_attach</code> (<code>_Safe_iterator_base</code> *__it, bool __constant) </p>
<p> void <code>_M_attach_single</code> (<code>_Safe_iterator_base</code> *__it, bool __constant) throw () </p>
<p> <code>_Base</code> &amp; <code>_M_base</code> () noexcept </p>
<p> const <code>_Base</code> &amp; <code>_M_base</code> () const noexcept </p>
<p> void <code>_M_detach</code> (<code>_Safe_iterator_base</code> *__it) </p>
<p> void <code>_M_detach_single</code> (<code>_Safe_iterator_base</code> *__it) throw () </p>
<p> void <code>_M_invalidate_all</code> () const </p>
<p> void <code>_M_invalidate_if</code> (_Predicate __pred) </p>
<p> this <code>_M_swap</code> (__list) </p>
<p> void <code>_M_transfer_from_if</code> (_Safe_sequence &amp;__from, _Predicate __pred) </p>
<p> <code>iterator</code> <code>before_begin</code> () noexcept </p>
<p> <code>const_iterator</code> <code>before_begin</code> () const noexcept </p>
<p> <code>iterator</code> <code>begin</code> () noexcept </p>
<p> <code>const_iterator</code> <code>begin</code> () const noexcept </p>
<p> <code>const_iterator</code> <code>cbefore_begin</code> () const noexcept </p>
<p> <code>const_iterator</code> <code>cbegin</code> () const noexcept </p>
<p> <code>const_iterator</code> <code>cend</code> () const noexcept </p>
<p> void <code>clear</code> () noexcept </p>
<p> template&lt;typename&#8230; _Args&gt; <code>iterator</code> <code>emplace_after</code> (<code>const_iterator</code> __pos, _Args &amp;&amp;&#8230;__args) </p>
<p> <code>iterator</code> <code>end</code> () noexcept </p>
<p> <code>const_iterator</code> <code>end</code> () const noexcept </p>
<p> <code>iterator</code> <code>erase_after</code> (<code>const_iterator</code> __pos) </p>
<p> <code>iterator</code> <code>erase_after</code> (<code>const_iterator</code> __pos, <code>const_iterator</code> __last) </p>
<p> reference <code>front</code> () </p>
<p> const_reference <code>front</code> () const </p>
<p> <code>iterator</code> <code>insert_after</code> (<code>const_iterator</code> __pos, const _Tp &amp;__val) </p>
<p> <code>iterator</code> <code>insert_after</code> (<code>const_iterator</code> __pos, _Tp &amp;&amp;__val) </p>
<p> <code>iterator</code> <code>insert_after</code> (<code>const_iterator</code> __pos, size_type __n, const _Tp &amp;__val) </p>
<p> template&lt;typename _InputIterator , typename = std::_RequireInputIter&lt;_InputIterator&gt;&gt; <code>iterator</code> <code>insert_after</code> (<code>const_iterator</code> __pos, _InputIterator __first, _InputIterator __last) </p>
<p> <code>iterator</code> <code>insert_after</code> (<code>const_iterator</code> __pos, <code>std::initializer_list</code>&lt; _Tp &gt; __il) </p>
<p> void <code>merge</code> (<code>forward_list</code> &amp;&amp;__list) </p>
<p> void <code>merge</code> (<code>forward_list</code> &amp;__list) </p>
<p> template&lt;typename _Comp &gt; void <code>merge</code> (<code>forward_list</code> &amp;&amp;__list, _Comp __comp) </p>
<p> template&lt;typename _Comp &gt; void <code>merge</code> (<code>forward_list</code> &amp;__list, _Comp __comp) </p>
<p> void <code>pop_front</code> () </p>
<p> void <code>remove</code> (const _Tp &amp;__val) </p>
<p> template&lt;typename _Pred &gt; void <code>remove_if</code> (_Pred __pred) </p>
<p> void <code>resize</code> (size_type __sz) </p>
<p> void <code>resize</code> (size_type __sz, const value_type &amp;__val) </p>
<p> void <code>splice_after</code> (<code>const_iterator</code> __pos, <code>forward_list</code> &amp;&amp;__list) </p>
<p> void <code>splice_after</code> (<code>const_iterator</code> __pos, <code>forward_list</code> &amp;__list) </p>
<p> void <code>splice_after</code> (<code>const_iterator</code> __pos, <code>forward_list</code> &amp;&amp;__list, <code>const_iterator</code> __i) </p>
<p> void <code>splice_after</code> (<code>const_iterator</code> __pos, <code>forward_list</code> &amp;__list, <code>const_iterator</code> __i) </p>
<p> void <code>splice_after</code> (<code>const_iterator</code> __pos, <code>forward_list</code> &amp;&amp;__list, <code>const_iterator</code> __before, <code>const_iterator</code> __last) </p>
<p> void <code>splice_after</code> (<code>const_iterator</code> __pos, <code>forward_list</code> &amp;__list, <code>const_iterator</code> __before, <code>const_iterator</code> __last) </p>
<p> void <code>unique</code> () </p>
<p> template&lt;typename _BinPred &gt; void <code>unique</code> (_BinPred __binary_pred)</p>
<h3>Public Attributes</h3>
<pre><code>const _Alloc &amp; __al: _Base(__list



const _Alloc __al



__pad0__: _Base(__al) { } forward_list(const forward_list&amp; __list



_Safe_iterator_base * _M_const_iterators



_Safe_iterator_base * _M_iterators



unsigned int _M_version



void



Protected Member Functions
void _M_detach_all ()



void _M_detach_singular ()



__gnu_cxx::__mutex &amp; _M_get_mutex ()  throw ()



void _M_revalidate_singular ()



void _M_swap (_Safe_sequence_base &amp;__x)</code></pre>
<h2>Detailed Description</h2>
<h3>template&lt;typename _Tp, typename _Alloc = std::allocator&lt;_Tp&gt;&gt;class std::__debug::forward_list&lt; _Tp, _Alloc &gt;</h3>
<p>Class std::forward_list with safety/checking/debug instrumentation. </p>
<p> Definition at line 44 of file debug/forward_list.</p>
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
<h3>void <code>__gnu_debug::_Safe_sequence</code>&lt; <code>forward_list</code>&lt; _Tp, _Alloc &gt; &gt;::_M_invalidate_if (_Predicate__pred) [inherited]</h3>
<p>Invalidates all iterators x that reference this sequence, are not singular, and for which __pred(x) returns true. __pred will be invoked with the normal iterators nested in the safe ones.</p>
<h3>void __gnu_debug::_Safe_sequence_base::_M_revalidate_singular () [protected], [inherited]</h3>
<p>Revalidates all attached singular iterators. This method may be used to validate iterators that were invalidated before (but for some reason, such as an exception, need to become valid again).</p>
<h3>void __gnu_debug::_Safe_sequence_base::_M_swap (<code>_Safe_sequence_base</code> &amp;__x) [protected], [inherited]</h3>
<p>Swap this sequence with the given sequence. This operation also swaps ownership of the iterators, so that when the operation is complete all iterators that originally referenced one container now reference the other container.</p>
<h3>void <code>__gnu_debug::_Safe_sequence</code>&lt; <code>forward_list</code>&lt; _Tp, _Alloc &gt; &gt;::_M_transfer_from_if (<code>_Safe_sequence</code>&lt; <code>forward_list</code>&lt; _Tp, _Alloc &gt; &gt; &amp;__from, _Predicate__pred) [inherited]</h3>
<p>Transfers all iterators x that reference from sequence, are not singular, and for which __pred(x) returns true. __pred will be invoked with the normal iterators nested in the safe ones.</p>
<h2>Member Data Documentation</h2>
<h3><code>_Safe_iterator_base</code>* __gnu_debug::_Safe_sequence_base::_M_const_iterators [inherited]</h3>
<p>The list of constant iterators that reference this container. </p>
<p> Definition at line 184 of file safe_base.h. </p>
<p> Referenced by __gnu_debug::_Safe_sequence&lt; _Sequence &gt;::_M_transfer_from_if().</p>
<h3><code>_Safe_iterator_base</code>* __gnu_debug::_Safe_sequence_base::_M_iterators [inherited]</h3>
<p>The list of mutable iterators that reference this container. </p>
<p> Definition at line 181 of file safe_base.h. </p>
<p> Referenced by __gnu_debug::_Safe_sequence&lt; _Sequence &gt;::_M_transfer_from_if().</p>
<h3>unsigned int __gnu_debug::_Safe_sequence_base::_M_version [mutable], [inherited]</h3>
<p>The container version number. This number may never be 0. </p>
<p> Definition at line 187 of file safe_base.h. </p>
<p> Referenced by __gnu_debug::_Safe_sequence_base::_M_invalidate_all(), and __gnu_debug::_Safe_sequence&lt; _Sequence &gt;::_M_transfer_from_if().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
