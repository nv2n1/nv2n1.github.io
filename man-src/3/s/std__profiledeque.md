---
title: "std__profiledeque(3)"
name: "std__profiledeque"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std__profiledeque/"
description: "std::__profile::deque< _Tp, _Allocator > –"
---

<p>std::__profile::deque&lt; _Tp, _Allocator &gt; &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits deque&lt; _Tp, _Allocator &gt;.</p>
<h3>Public Types</h3>
<p>typedef _Allocator <code>allocator_type</code> </p>
<p> typedef _Base::const_iterator <code>const_iterator</code> </p>
<p> typedef _Base::const_pointer <code>const_pointer</code> </p>
<p> typedef _Base::const_reference <code>const_reference</code> </p>
<p> typedef<br />
 _Base::const_reverse_iterator <code>const_reverse_iterator</code>&quot; </p>
<p> typedef _Base::difference_type <code>difference_type</code> </p>
<p> typedef _Base::iterator <code>iterator</code> </p>
<p> typedef _Base::pointer <code>pointer</code> </p>
<p> typedef _Base::reference <code>reference</code> </p>
<p> typedef _Base::reverse_iterator <code>reverse_iterator</code> </p>
<p> typedef _Base::size_type <code>size_type</code> </p>
<p> typedef _Tp <code>value_type</code></p>
<h3>Public Member Functions</h3>
<p><code>_Base</code> &amp; <code>_M_base</code> () noexcept </p>
<p> const <code>_Base</code> &amp; <code>_M_base</code> () const noexcept </p>
<p> reference <code>back</code> () </p>
<p> const_reference <code>back</code> () const </p>
<p> const _Tp const _Allocator iterator <code>begin</code> () noexcept </p>
<p> const_iterator <code>begin</code> () const noexcept </p>
<p> const_iterator <code>cbegin</code> () const noexcept </p>
<p> const_iterator <code>cend</code> () const noexcept </p>
<p> void <code>clear</code> () noexcept </p>
<p> const_reverse_iterator <code>crbegin</code> () const noexcept </p>
<p> const_reverse_iterator <code>crend</code> () const noexcept </p>
<p> template&lt;typename&#8230; _Args&gt; iterator <code>emplace</code> (iterator __position, _Args &amp;&amp;&#8230;__args) </p>
<p> template&lt;typename&#8230; _Args&gt; void <code>emplace_back</code> (_Args &amp;&amp;&#8230;__args) </p>
<p> template&lt;typename&#8230; _Args&gt; void <code>emplace_front</code> (_Args &amp;&amp;&#8230;__args) </p>
<p> iterator <code>end</code> () noexcept </p>
<p> const_iterator <code>end</code> () const noexcept </p>
<p> iterator <code>erase</code> (iterator __position) </p>
<p> iterator <code>erase</code> (iterator __first, iterator __last) </p>
<p> reference <code>front</code> () </p>
<p> const_reference <code>front</code> () const </p>
<p> iterator <code>insert</code> (iterator __position, const _Tp &amp;__x) </p>
<p> iterator <code>insert</code> (iterator __position, _Tp &amp;&amp;__x) </p>
<p> void <code>insert</code> (iterator __p, <code>initializer_list</code>&lt; value_type &gt; __l) </p>
<p> void <code>insert</code> (iterator __position, size_type __n, const _Tp &amp;__x) </p>
<p> template&lt;typename _InputIterator , typename = std::_RequireInputIter&lt;_InputIterator&gt;&gt; void <code>insert</code> (iterator __position, _InputIterator __first, _InputIterator __last) </p>
<p> reference <code>operator[]</code> (size_type __n) </p>
<p> const_reference <code>operator[]</code> (size_type __n) const </p>
<p> void <code>pop_back</code> () </p>
<p> void <code>pop_front</code> () </p>
<p> void <code>push_back</code> (const _Tp &amp;__x) </p>
<p> void <code>push_back</code> (_Tp &amp;&amp;__x) </p>
<p> void <code>push_front</code> (const _Tp &amp;__x) </p>
<p> void <code>push_front</code> (_Tp &amp;&amp;__x) </p>
<p> reverse_iterator <code>rbegin</code> () noexcept </p>
<p> const_reverse_iterator <code>rbegin</code> () const noexcept </p>
<p> reverse_iterator <code>rend</code> () noexcept </p>
<p> const_reverse_iterator <code>rend</code> () const noexcept </p>
<p> void <code>resize</code> (size_type __sz) </p>
<p> void <code>resize</code> (size_type __sz, const _Tp &amp;__c) </p>
<p> void <code>swap</code> (<code>deque</code> &amp;__x)</p>
<h3>Public Attributes</h3>
<pre><code>const _Tp const _Allocator &amp;__a

    __pad0__ : _Base(__a)
{
}
explicit deque(size_type __n)
    : _Base(__n)
{
} deque(size_type __n



const _Tp &amp; __value</code></pre>
<h2>Detailed Description</h2>
<h3>template&lt;typename _Tp, typename _Allocator = std::allocator&lt;_Tp&gt;&gt;class std::__profile::deque&lt; _Tp, _Allocator &gt;</h3>
<p>Class std::deque wrapper with performance instrumentation. </p>
<p> Definition at line 40 of file profile/deque.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
