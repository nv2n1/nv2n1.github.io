---
title: "std_deque_iterator(3)"
name: "std_deque_iterator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std_deque_iterator/"
description: "std::_Deque_iterator< _Tp, _Ref, _Ptr > –"
---

<p>std::_Deque_iterator&lt; _Tp, _Ref, _Ptr &gt; &#8211;</p>
<h2>Synopsis</h2>
<h3>Public Types</h3>
<p>typedef _Tp ** <code>_Map_pointer</code> </p>
<p> typedef <code>_Deque_iterator</code> <code>_Self</code> </p>
<p> typedef <code>_Deque_iterator</code>&lt; _Tp,<br />
 const _Tp &amp;, const _Tp * &gt; <code>const_iterator</code>&quot; </p>
<p> typedef ptrdiff_t <code>difference_type</code> </p>
<p> typedef <code>_Deque_iterator</code>&lt; _Tp,<br />
 _Tp &amp;, _Tp * &gt; <code>iterator</code>&quot; </p>
<p> typedef<br />
 <code>std::random_access_iterator_tag</code> <code>iterator_category</code>&quot; </p>
<p> typedef _Ptr <code>pointer</code> </p>
<p> typedef _Ref <code>reference</code> </p>
<p> typedef size_t <code>size_type</code> </p>
<p> typedef _Tp <code>value_type</code></p>
<h3>Public Member Functions</h3>
<pre><code>_Deque_iterator (_Tp *__x, _Map_pointer __y)



_Deque_iterator (const iterator &amp;__x)



void _M_set_node (_Map_pointer __new_node)



reference operator* () const



_Self operator+ (difference_type __n) const



_Self &amp; operator++ ()



_Self operator++ (int)



_Self &amp; operator+= (difference_type __n)



_Self operator- (difference_type __n) const



_Self &amp; operator-- ()



_Self operator-- (int)



_Self &amp; operator-= (difference_type __n)



pointer operator-&gt; () const



reference operator[] (difference_type __n) const



Static Public Member Functions
static size_t _S_buffer_size ()



Public Attributes</code></pre>
<p> _Tp * <code>_M_cur</code> </p>
<p> _Tp * <code>_M_first</code> </p>
<p> _Tp * <code>_M_last</code> </p>
<p> _Map_pointer <code>_M_node</code></p>
<h2>Detailed Description</h2>
<h3>template&lt;typename _Tp, typename _Ref, typename _Ptr&gt;struct std::_Deque_iterator&lt; _Tp, _Ref, _Ptr &gt;</h3>
<p>A deque::iterator. </p>
<p> Quite a bit of intelligence here. Much of the functionality of deque is actually passed off to this class. A deque holds two of these internally, marking its valid range. Access to elements is done as offsets of either of those two, relying on operator overloading in this class. </p>
<p> All the functions are op overloads except for _M_set_node. </p>
<p> Definition at line 106 of file stl_deque.h.</p>
<h2>Member Function Documentation</h2>
<h3>template&lt;typename _Tp, typename _Ref, typename _Ptr&gt; void <code>std::_Deque_iterator</code>&lt; _Tp, _Ref, _Ptr &gt;::_M_set_node (_Map_pointer__new_node) [inline]</h3>
<p>Prepares to traverse new_node. Sets everything except _M_cur, which should therefore be set by the caller immediately afterwards, based on _M_first and _M_last. </p>
<p> Definition at line 234 of file stl_deque.h.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
