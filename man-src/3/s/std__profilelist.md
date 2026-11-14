---
title: "std__profilelist(3)"
name: "std__profilelist"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std__profilelist/"
description: "std::__profile::list< _Tp, _Allocator > –"
---

<p>std::__profile::list&lt; _Tp, _Allocator &gt; &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits list&lt; _Tp, _Allocator &gt;.</p>
<h3>Public Types</h3>
<p>typedef _Allocator <code>allocator_type</code> </p>
<p> typedef __iterator_tracker<br />
 &lt; typename<br />
 _Base::const_iterator, <code>list</code> &gt; <code>const_iterator</code>&quot; </p>
<p> typedef _Base::const_pointer <code>const_pointer</code> </p>
<p> typedef _Base::const_reference <code>const_reference</code> </p>
<p> typedef <code>std::reverse_iterator</code><br />
 &lt; const_iterator &gt; <code>const_reverse_iterator</code>&quot; </p>
<p> typedef _Base::difference_type <code>difference_type</code> </p>
<p> typedef __iterator_tracker<br />
 &lt; typename _Base::iterator,<br />
 <code>list</code> &gt; <code>iterator</code>&quot; </p>
<p> typedef _Base::pointer <code>pointer</code> </p>
<p> typedef _Base::reference <code>reference</code> </p>
<p> typedef <code>std::reverse_iterator</code><br />
 &lt; iterator &gt; <code>reverse_iterator</code>&quot; </p>
<p> typedef _Base::size_type <code>size_type</code> </p>
<p> typedef _Tp <code>value_type</code></p>
<h3>Public Member Functions</h3>
<pre><code>list (size_type __n)



list (size_type __n, const _Tp &amp;__value, const _Allocator &amp;__a=_Allocator())



template&lt;typename _InputIterator , typename  = std::_RequireInputIter&lt;_InputIterator&gt;&gt; list (_InputIterator __first, _InputIterator __last, const _Allocator &amp;__a=_Allocator())



list (const list &amp;__x)



list (const _Base &amp;__x)



list (list &amp;&amp;__x) noexcept



list (initializer_list&lt; value_type &gt; __l, const allocator_type &amp;__a=allocator_type())



_Base &amp; _M_base () noexcept



const _Base &amp; _M_base () const noexcept



void _M_profile_find () const



void _M_profile_iterate (int __rewind=0) const



void assign (initializer_list&lt; value_type &gt; __l)



template&lt;typename _InputIterator , typename  = std::_RequireInputIter&lt;_InputIterator&gt;&gt; void assign (_InputIterator __first, _InputIterator __last)



void assign (size_type __n, const _Tp &amp;__t)



reference back ()



const_reference back () const



iterator begin () noexcept



const_iterator begin () const noexcept



const_iterator cbegin () const noexcept



const_iterator cend () const noexcept



void clear () noexcept



const_reverse_iterator crbegin () const noexcept



const_reverse_iterator crend () const noexcept



template&lt;typename... _Args&gt; iterator emplace (iterator __position, _Args &amp;&amp;...__args)



iterator end () noexcept



const_iterator end () const noexcept



iterator erase (iterator __position)



iterator erase (iterator __position, iterator __last)



reference front ()



const_reference front () const



iterator insert (iterator __position, const _Tp &amp;__x)



iterator insert (iterator __position, _Tp &amp;&amp;__x)



void insert (iterator __position, initializer_list&lt; value_type &gt; __l)



void insert (iterator __position, size_type __n, const _Tp &amp;__x)



template&lt;typename _InputIterator , typename  = std::_RequireInputIter&lt;_InputIterator&gt;&gt; void insert (iterator __position, _InputIterator __first, _InputIterator __last)



list &amp; operator= (const list &amp;__x)



list &amp; operator= (list &amp;&amp;__x)



list &amp; operator= (initializer_list&lt; value_type &gt; __l)



void pop_back ()



void pop_front ()



void push_front (const value_type &amp;__x)



reverse_iterator rbegin () noexcept



const_reverse_iterator rbegin () const noexcept



void remove (const _Tp &amp;__value)



template&lt;class _Predicate &gt; void remove_if (_Predicate __pred)



reverse_iterator rend () noexcept



const_reverse_iterator rend () const noexcept



void resize (size_type __sz)



void resize (size_type __sz, const _Tp &amp;__c)



void splice (iterator __position, list &amp;__x)



void splice (iterator __position, list &amp;__x, iterator __i)



void splice (iterator __position, list &amp;&amp;__x, iterator __first, iterator __last)



void splice (iterator __position, list &amp;__x, iterator __first, iterator __last)



void swap (list &amp;__x)



void unique ()



template&lt;class _BinaryPredicate &gt; void unique (_BinaryPredicate __binary_pred)



Public Attributes</code></pre>
<p> <code>__pad0__</code>: <code>_Base</code>(__a) { </p>
<p> <code>void</code></p>
<h2>Detailed Description</h2>
<h3>template&lt;typename _Tp, typename _Allocator = std::allocator&lt;_Tp&gt;&gt;class std::__profile::list&lt; _Tp, _Allocator &gt;</h3>
<p>List wrapper with performance instrumentation. </p>
<p> Definition at line 42 of file profile/list.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
