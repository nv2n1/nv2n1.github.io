---
title: "std__detail_nfa(3)"
name: "std__detail_nfa"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std__detail_nfa/"
description: "std::__detail::_Nfa –"
---

<p>std::__detail::_Nfa &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>std::__detail::_Automaton</code>, and <code>std::vector&lt; _State &gt;</code>.</p>
<h3>Public Types</h3>
<p>typedef<br />
 <code>regex_constants::syntax_option_type</code> <code>_FlagT</code>&quot; </p>
<p> typedef unsigned int <code>_SizeT</code> </p>
<p> typedef <code>_State</code> <code>_StateT</code> </p>
<p> typedef <code>std::allocator</code>&lt; <code>_State</code> &gt; <code>allocator_type</code> </p>
<p> typedef<br />
 __gnu_cxx::__normal_iterator<br />
 &lt; const_pointer, <code>vector</code> &gt; <code>const_iterator</code>&quot; </p>
<p> typedef<br />
 _Alloc_traits::const_pointer <code>const_pointer</code>&quot; </p>
<p> typedef<br />
 _Alloc_traits::const_reference <code>const_reference</code>&quot; </p>
<p> typedef <code>std::reverse_iterator</code><br />
 &lt; const_iterator &gt; <code>const_reverse_iterator</code>&quot; </p>
<p> typedef ptrdiff_t <code>difference_type</code> </p>
<p> typedef<br />
 __gnu_cxx::__normal_iterator<br />
 &lt; pointer, <code>vector</code> &gt; <code>iterator</code>&quot; </p>
<p> typedef _Base::pointer <code>pointer</code> </p>
<p> typedef _Alloc_traits::reference <code>reference</code> </p>
<p> typedef <code>std::reverse_iterator</code><br />
 &lt; iterator &gt; <code>reverse_iterator</code>&quot; </p>
<p> typedef size_t <code>size_type</code> </p>
<p> typedef <code>_State</code> <code>value_type</code></p>
<h3>Public Member Functions</h3>
<p><code>_Nfa</code> (_FlagT __f) </p>
<p> <code>_Alloc_traits::_S_on_swap</code> (_M_get_Tp_allocator(), __x._M_get_Tp_allocator()) </p>
<p> const <code>_StateSet</code> &amp; <code>_M_final_states</code> () const </p>
<p> <code>_StateIdT</code> <code>_M_insert_accept</code> () </p>
<p> <code>_StateIdT</code> <code>_M_insert_alt</code> (<code>_StateIdT</code> __next, <code>_StateIdT</code> __alt) </p>
<p> <code>_StateIdT</code> <code>_M_insert_matcher</code> (<code>_Matcher</code> __m) </p>
<p> <code>_StateIdT</code> <code>_M_insert_subexpr_begin</code> (const <code>_Tagger</code> &amp;__t) </p>
<p> <code>_StateIdT</code> <code>_M_insert_subexpr_end</code> (unsigned int __i, const <code>_Tagger</code> &amp;__t) </p>
<p> _FlagT <code>_M_options</code> () const </p>
<p> <code>_StateIdT</code> <code>_M_start</code> () const </p>
<p> _SizeT <code>_M_sub_count</code> () const </p>
<p> <code>void</code> <code>assign</code> (size_type __n, const value_type &amp;__val) </p>
<p> <code>void</code> <code>assign</code> (_InputIterator __first, _InputIterator __last) </p>
<p> <code>void</code> <code>assign</code> (<code>initializer_list</code>&lt; value_type &gt; __l) </p>
<p> reference <code>at</code> (size_type __n) </p>
<p> const_reference <code>at</code> (size_type __n) const </p>
<p> reference <code>back</code> () </p>
<p> const_reference <code>back</code> () const </p>
<p> iterator <code>begin</code> () noexcept </p>
<p> const_iterator <code>begin</code> () const noexcept </p>
<p> size_type <code>capacity</code> () const noexcept </p>
<p> const_iterator <code>cbegin</code> () const noexcept </p>
<p> const_iterator <code>cend</code> () const noexcept </p>
<p> <code>void</code> <code>clear</code> () noexcept </p>
<p> <code>const_reverse_iterator</code> <code>crbegin</code> () const noexcept </p>
<p> <code>const_reverse_iterator</code> <code>crend</code> () const noexcept </p>
<p> <code>_State</code> * <code>data</code> () noexcept </p>
<p> const <code>_State</code> * <code>data</code> () const noexcept </p>
<p> iterator <code>emplace</code> (iterator __position, _Args &amp;&amp;&#8230;__args) </p>
<p> <code>void</code> <code>emplace_back</code> (_Args &amp;&amp;&#8230;__args) </p>
<p> bool <code>empty</code> () const noexcept </p>
<p> iterator <code>end</code> () noexcept </p>
<p> const_iterator <code>end</code> () const noexcept </p>
<p> iterator <code>erase</code> (iterator __position) </p>
<p> iterator <code>erase</code> (iterator __first, iterator __last) </p>
<p> reference <code>front</code> () </p>
<p> const_reference <code>front</code> () const </p>
<p> iterator <code>insert</code> (iterator __position, const value_type &amp;__x) </p>
<p> iterator <code>insert</code> (iterator __position, value_type &amp;&amp;__x) </p>
<p> <code>void</code> <code>insert</code> (iterator __position, <code>initializer_list</code>&lt; value_type &gt; __l) </p>
<p> <code>void</code> <code>insert</code> (iterator __position, size_type __n, const value_type &amp;__x) </p>
<p> <code>void</code> <code>insert</code> (iterator __position, _InputIterator __first, _InputIterator __last) </p>
<p> size_type <code>max_size</code> () const noexcept </p>
<p> reference <code>operator[]</code> (size_type __n) </p>
<p> const_reference <code>operator[]</code> (size_type __n) const </p>
<p> <code>void</code> <code>pop_back</code> () </p>
<p> <code>void</code> <code>push_back</code> (const value_type &amp;__x) </p>
<p> <code>void</code> <code>push_back</code> (value_type &amp;&amp;__x) </p>
<p> <code>reverse_iterator</code> <code>rbegin</code> () noexcept </p>
<p> <code>const_reverse_iterator</code> <code>rbegin</code> () const noexcept </p>
<p> <code>reverse_iterator</code> <code>rend</code> () noexcept </p>
<p> <code>const_reverse_iterator</code> <code>rend</code> () const noexcept </p>
<p> <code>void</code> <code>reserve</code> (size_type __n) </p>
<p> <code>void</code> <code>resize</code> (size_type __new_size) </p>
<p> <code>void</code> <code>resize</code> (size_type __new_size, const value_type &amp;__x) </p>
<p> <code>void</code> <code>shrink_to_fit</code> () </p>
<p> size_type <code>size</code> () const noexcept</p>
<h3>Public Attributes</h3>
<p><code>__a</code> </p>
<p> <code>__pad0__</code> </p>
<p> <code>void</code></p>
<h3>Protected Member Functions</h3>
<p>pointer <code>_M_allocate</code> (size_t __n) </p>
<p> pointer <code>_M_allocate_and_copy</code> (size_type __n, _ForwardIterator __first, _ForwardIterator __last) </p>
<p> <code>void</code> <code>_M_assign_aux</code> (_InputIterator __first, _InputIterator __last, <code>std::input_iterator_tag</code>) </p>
<p> <code>void</code> <code>_M_assign_aux</code> (_ForwardIterator __first, _ForwardIterator __last, <code>std::forward_iterator_tag</code>) </p>
<p> <code>void</code> <code>_M_assign_dispatch</code> (_Integer __n, _Integer __val, __true_type) </p>
<p> <code>void</code> <code>_M_assign_dispatch</code> (_InputIterator __first, _InputIterator __last, __false_type) </p>
<p> size_type <code>_M_check_len</code> (size_type __n, const char *__s) const </p>
<p> <code>void</code> <code>_M_deallocate</code> (pointer __p, size_t __n) </p>
<p> <code>void</code> <code>_M_default_append</code> (size_type __n) </p>
<p> <code>void</code> <code>_M_default_initialize</code> (size_type __n) </p>
<p> <code>void</code> <code>_M_emplace_back_aux</code> (_Args &amp;&amp;&#8230;__args) </p>
<p> <code>void</code> <code>_M_erase_at_end</code> (pointer __pos) </p>
<p> <code>void</code> <code>_M_fill_assign</code> (size_type __n, const value_type &amp;__val) </p>
<p> <code>void</code> <code>_M_fill_initialize</code> (size_type __n, const value_type &amp;__value) </p>
<p> <code>void</code> <code>_M_fill_insert</code> (iterator __pos, size_type __n, const value_type &amp;__x) </p>
<p> _Tp_alloc_type &amp; <code>_M_get_Tp_allocator</code> () noexcept </p>
<p> const _Tp_alloc_type &amp; <code>_M_get_Tp_allocator</code> () const noexcept </p>
<p> <code>void</code> <code>_M_initialize_dispatch</code> (_Integer __n, _Integer __value, __true_type) </p>
<p> <code>void</code> <code>_M_initialize_dispatch</code> (_InputIterator __first, _InputIterator __last, __false_type) </p>
<p> <code>void</code> <code>_M_insert_aux</code> (iterator __position, _Args &amp;&amp;&#8230;__args) </p>
<p> <code>void</code> <code>_M_insert_dispatch</code> (iterator __pos, _Integer __n, _Integer __val, __true_type) </p>
<p> <code>void</code> <code>_M_insert_dispatch</code> (iterator __pos, _InputIterator __first, _InputIterator __last, __false_type) </p>
<p> <code>void</code> <code>_M_range_check</code> (size_type __n) const </p>
<p> <code>void</code> <code>_M_range_initialize</code> (_InputIterator __first, _InputIterator __last, <code>std::input_iterator_tag</code>) </p>
<p> <code>void</code> <code>_M_range_initialize</code> (_ForwardIterator __first, _ForwardIterator __last, <code>std::forward_iterator_tag</code>) </p>
<p> <code>void</code> <code>_M_range_insert</code> (iterator __pos, _InputIterator __first, _InputIterator __last, <code>std::input_iterator_tag</code>) </p>
<p> <code>void</code> <code>_M_range_insert</code> (iterator __pos, _ForwardIterator __first, _ForwardIterator __last, <code>std::forward_iterator_tag</code>) </p>
<p> bool <code>_M_shrink_to_fit</code> () </p>
<p> <code>allocator_type</code> <code>get_allocator</code> () const noexcept</p>
<h3>Protected Attributes</h3>
<p>_Vector_impl <code>_M_impl</code></p>
<h2>Detailed Description</h2>
<p>struct _Nfa </p>
<p> A collection of all states making up an NFA. </p>
<p> An NFA is a 4-tuple M = (K, S, s, F), where K is a finite set of states, S is the alphabet of the NFA, s is the initial state, F is a set of final (accepting) states. </p>
<p> This NFA class is templated on S, a type that will hold values of the underlying alphabet (without regard to semantics of that alphabet). The other elements of the tuple are generated during construction of the NFA and are available through accessor member functions. </p>
<p> Definition at line 269 of file regex_nfa.h.</p>
<h2>Member Function Documentation</h2>
<h3>pointer <code>std::vector</code>&lt; <code>_State</code> , <code>std::allocator</code>&lt;<code>_State</code> &gt; &gt;::_M_allocate_and_copy (size_type__n, _ForwardIterator__first, _ForwardIterator__last) [inline], [protected], [inherited]</h3>
<p>Memory expansion handler. Uses the member allocation function to obtain <i>n</i> bytes of memory, and then copies [first,last) into it. </p>
<p> Definition at line 1135 of file stl_vector.h.</p>
<h3><code>void</code> <code>std::vector</code>&lt; <code>_State</code> , <code>std::allocator</code>&lt;<code>_State</code> &gt; &gt;::_M_range_check (size_type__n) const [inline], [protected], [inherited]</h3>
<p>Safety check used only from at(). </p>
<p> Definition at line 791 of file stl_vector.h. </p>
<p> References std::vector&lt; _Tp, _Alloc &gt;::size().</p>
<h3><code>void</code> <code>std::vector</code>&lt; <code>_State</code> , <code>std::allocator</code>&lt;<code>_State</code> &gt; &gt;::assign (size_type__n, const value_type &amp;__val) [inline], [inherited]</h3>
<p>Assigns a given value to a vector. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__n</i> Number of elements to be assigned.<br />
 <i>__val</i> Value to be assigned.</dl>
<p> This function fills a vector with <i>__n</i> copies of the given value. Note that the assignment completely changes the vector and that the resulting vector&#8217;s size is the same as the number of elements assigned. Old data may be lost. </p>
<p> Definition at line 479 of file stl_vector.h.</p>
<h3><code>void</code> <code>std::vector</code>&lt; <code>_State</code> , <code>std::allocator</code>&lt;<code>_State</code> &gt; &gt;::assign (_InputIterator__first, _InputIterator__last) [inline], [inherited]</h3>
<p>Assigns a range to a vector. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__first</i> An input iterator.<br />
 <i>__last</i> An input iterator.</dl>
<p> This function fills a vector with copies of the elements in the range [__first,__last). </p>
<p> Note that the assignment completely changes the vector and that the resulting vector&#8217;s size is the same as the number of elements assigned. Old data may be lost. </p>
<p> Definition at line 498 of file stl_vector.h.</p>
<h3><code>void</code> <code>std::vector</code>&lt; <code>_State</code> , <code>std::allocator</code>&lt;<code>_State</code> &gt; &gt;::assign (<code>initializer_list</code>&lt; value_type &gt;__l) [inline], [inherited]</h3>
<p>Assigns an initializer list to a vector. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__l</i> An initializer_list.</dl>
<p> This function fills a vector with copies of the elements in the initializer list <i>__l</i>. </p>
<p> Note that the assignment completely changes the vector and that the resulting vector&#8217;s size is the same as the number of elements assigned. Old data may be lost. </p>
<p> Definition at line 524 of file stl_vector.h. </p>
<p> References std::vector&lt; _Tp, _Alloc &gt;::assign().</p>
<h3>reference <code>std::vector</code>&lt; <code>_State</code> , <code>std::allocator</code>&lt;<code>_State</code> &gt; &gt;::at (size_type__n) [inline], [inherited]</h3>
<p>Provides access to the data contained in the vector. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__n</i> The index of the element for which data should be accessed.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>Read/write reference to data.</dl>
<p> <code>Exceptions:</code></p>
<dl>
<dd><i>std::out_of_range</i> If <i>__n</i> is an invalid index.</dl>
<p> This function provides for safer data access. The parameter is first checked that it is in the range of the vector. The function throws out_of_range if the check fails. </p>
<p> Definition at line 810 of file stl_vector.h. </p>
<p> References std::vector&lt; _Tp, _Alloc &gt;::_M_range_check().</p>
<h3>const_reference <code>std::vector</code>&lt; <code>_State</code> , <code>std::allocator</code>&lt;<code>_State</code> &gt; &gt;::at (size_type__n) const [inline], [inherited]</h3>
<p>Provides access to the data contained in the vector. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__n</i> The index of the element for which data should be accessed.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>Read-only (constant) reference to data.</dl>
<p> <code>Exceptions:</code></p>
<dl>
<dd><i>std::out_of_range</i> If <i>__n</i> is an invalid index.</dl>
<p> This function provides for safer data access. The parameter is first checked that it is in the range of the vector. The function throws out_of_range if the check fails. </p>
<p> Definition at line 828 of file stl_vector.h. </p>
<p> References std::vector&lt; _Tp, _Alloc &gt;::_M_range_check().</p>
<h3>reference <code>std::vector</code>&lt; <code>_State</code> , <code>std::allocator</code>&lt;<code>_State</code> &gt; &gt;::back () [inline], [inherited]</h3>
<p>Returns a read/write reference to the data at the last element of the vector. </p>
<p> Definition at line 855 of file stl_vector.h. </p>
<p> References std::vector&lt; _Tp, _Alloc &gt;::end().</p>
<h3>const_reference <code>std::vector</code>&lt; <code>_State</code> , <code>std::allocator</code>&lt;<code>_State</code> &gt; &gt;::back () const [inline], [inherited]</h3>
<p>Returns a read-only (constant) reference to the data at the last element of the vector. </p>
<p> Definition at line 863 of file stl_vector.h. </p>
<p> References std::vector&lt; _Tp, _Alloc &gt;::end().</p>
<h3>iterator <code>std::vector</code>&lt; <code>_State</code> , <code>std::allocator</code>&lt;<code>_State</code> &gt; &gt;::begin () [inline], [noexcept], [inherited]</h3>
<p>Returns a read/write iterator that points to the first element in the vector. Iteration is done in ordinary element order. </p>
<p> Definition at line 538 of file stl_vector.h.</p>
<h3>const_iterator <code>std::vector</code>&lt; <code>_State</code> , <code>std::allocator</code>&lt;<code>_State</code> &gt; &gt;::begin () const [inline], [noexcept], [inherited]</h3>
<p>Returns a read-only (constant) iterator that points to the first element in the vector. Iteration is done in ordinary element order. </p>
<p> Definition at line 547 of file stl_vector.h.</p>
<h3>size_type <code>std::vector</code>&lt; <code>_State</code> , <code>std::allocator</code>&lt;<code>_State</code> &gt; &gt;::capacity () const [inline], [noexcept], [inherited]</h3>
<p>Returns the total number of elements that the vector can hold before needing to allocate more memory. </p>
<p> Definition at line 725 of file stl_vector.h.</p>
<h3>const_iterator <code>std::vector</code>&lt; <code>_State</code> , <code>std::allocator</code>&lt;<code>_State</code> &gt; &gt;::cbegin () const [inline], [noexcept], [inherited]</h3>
<p>Returns a read-only (constant) iterator that points to the first element in the vector. Iteration is done in ordinary element order. </p>
<p> Definition at line 611 of file stl_vector.h.</p>
<h3>const_iterator <code>std::vector</code>&lt; <code>_State</code> , <code>std::allocator</code>&lt;<code>_State</code> &gt; &gt;::cend () const [inline], [noexcept], [inherited]</h3>
<p>Returns a read-only (constant) iterator that points one past the last element in the vector. Iteration is done in ordinary element order. </p>
<p> Definition at line 620 of file stl_vector.h.</p>
<h3><code>void</code> <code>std::vector</code>&lt; <code>_State</code> , <code>std::allocator</code>&lt;<code>_State</code> &gt; &gt;::clear () [inline], [noexcept], [inherited]</h3>
<p>Erases all the elements. Note that this function only erases the elements, and that if the elements themselves are pointers, the pointed-to memory is not touched in any way. Managing the pointer is the user&#8217;s responsibility. </p>
<p> Definition at line 1125 of file stl_vector.h.</p>
<h3><code>const_reverse_iterator</code> <code>std::vector</code>&lt; <code>_State</code> , <code>std::allocator</code>&lt;<code>_State</code> &gt; &gt;::crbegin () const [inline], [noexcept], [inherited]</h3>
<p>Returns a read-only (constant) reverse iterator that points to the last element in the vector. Iteration is done in reverse element order. </p>
<p> Definition at line 629 of file stl_vector.h. </p>
<p> References std::vector&lt; _Tp, _Alloc &gt;::end().</p>
<h3><code>const_reverse_iterator</code> <code>std::vector</code>&lt; <code>_State</code> , <code>std::allocator</code>&lt;<code>_State</code> &gt; &gt;::crend () const [inline], [noexcept], [inherited]</h3>
<p>Returns a read-only (constant) reverse iterator that points to one before the first element in the vector. Iteration is done in reverse element order. </p>
<p> Definition at line 638 of file stl_vector.h. </p>
<p> References std::vector&lt; _Tp, _Alloc &gt;::begin().</p>
<h3><code>_State</code> * <code>std::vector</code>&lt; <code>_State</code> , <code>std::allocator</code>&lt;<code>_State</code> &gt; &gt;::data () [inline], [noexcept], [inherited]</h3>
<p>Returns a pointer such that [data(), data() + size()) is a valid range. For a non-empty vector, data() == &amp;front(). </p>
<p> Definition at line 878 of file stl_vector.h. </p>
<p> References std::__addressof(), and std::vector&lt; _Tp, _Alloc &gt;::front().</p>
<h3>iterator <code>std::vector</code>&lt; <code>_State</code> , <code>std::allocator</code>&lt;<code>_State</code> &gt; &gt;::emplace (iterator__position, _Args &amp;&amp;&#8230;__args) [inherited]</h3>
<p>Inserts an object in vector before specified iterator. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__position</i> An iterator into the vector.<br />
 <i>__args</i> Arguments.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>An iterator that points to the inserted data.</dl>
<p> This function will insert an object of type T constructed with T(std::forward&lt;Args&gt;(args)&#8230;) before the specified location. Note that this kind of operation could be expensive for a vector and if it is frequently used the user should consider using std::list.</p>
<h3>bool <code>std::vector</code>&lt; <code>_State</code> , <code>std::allocator</code>&lt;<code>_State</code> &gt; &gt;::empty () const [inline], [noexcept], [inherited]</h3>
<p>Returns true if the vector is empty. (Thus begin() would equal end().) </p>
<p> Definition at line 734 of file stl_vector.h. </p>
<p> References std::vector&lt; _Tp, _Alloc &gt;::begin(), and std::vector&lt; _Tp, _Alloc &gt;::end().</p>
<h3>iterator <code>std::vector</code>&lt; <code>_State</code> , <code>std::allocator</code>&lt;<code>_State</code> &gt; &gt;::end () [inline], [noexcept], [inherited]</h3>
<p>Returns a read/write iterator that points one past the last element in the vector. Iteration is done in ordinary element order. </p>
<p> Definition at line 556 of file stl_vector.h.</p>
<h3>const_iterator <code>std::vector</code>&lt; <code>_State</code> , <code>std::allocator</code>&lt;<code>_State</code> &gt; &gt;::end () const [inline], [noexcept], [inherited]</h3>
<p>Returns a read-only (constant) iterator that points one past the last element in the vector. Iteration is done in ordinary element order. </p>
<p> Definition at line 565 of file stl_vector.h.</p>
<h3>iterator <code>std::vector</code>&lt; <code>_State</code> , <code>std::allocator</code>&lt;<code>_State</code> &gt; &gt;::erase (iterator__position) [inherited]</h3>
<p>Remove element at given position. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__position</i> Iterator pointing to element to be erased.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>An iterator pointing to the next element (or end()).</dl>
<p> This function will erase the element at the given position and thus shorten the vector by one. </p>
<p> Note This operation could be expensive and if it is frequently used the user should consider using std::list. The user is also cautioned that this function only erases the element, and that if the element is itself a pointer, the pointed-to memory is not touched in any way. Managing the pointer is the user&#8217;s responsibility.</p>
<h3>iterator <code>std::vector</code>&lt; <code>_State</code> , <code>std::allocator</code>&lt;<code>_State</code> &gt; &gt;::erase (iterator__first, iterator__last) [inherited]</h3>
<p>Remove a range of elements. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__first</i> Iterator pointing to the first element to be erased.<br />
 <i>__last</i> Iterator pointing to one past the last element to be erased.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>An iterator pointing to the element pointed to by <i>__last</i> prior to erasing (or end()).</dl>
<p> This function will erase the elements in the range [__first,__last) and shorten the vector accordingly. </p>
<p> Note This operation could be expensive and if it is frequently used the user should consider using std::list. The user is also cautioned that this function only erases the elements, and that if the elements themselves are pointers, the pointed-to memory is not touched in any way. Managing the pointer is the user&#8217;s responsibility.</p>
<h3>reference <code>std::vector</code>&lt; <code>_State</code> , <code>std::allocator</code>&lt;<code>_State</code> &gt; &gt;::front () [inline], [inherited]</h3>
<p>Returns a read/write reference to the data at the first element of the vector. </p>
<p> Definition at line 839 of file stl_vector.h. </p>
<p> References std::vector&lt; _Tp, _Alloc &gt;::begin().</p>
<h3>const_reference <code>std::vector</code>&lt; <code>_State</code> , <code>std::allocator</code>&lt;<code>_State</code> &gt; &gt;::front () const [inline], [inherited]</h3>
<p>Returns a read-only (constant) reference to the data at the first element of the vector. </p>
<p> Definition at line 847 of file stl_vector.h. </p>
<p> References std::vector&lt; _Tp, _Alloc &gt;::begin().</p>
<h3>iterator <code>std::vector</code>&lt; <code>_State</code> , <code>std::allocator</code>&lt;<code>_State</code> &gt; &gt;::insert (iterator__position, const value_type &amp;__x) [inherited]</h3>
<p>Inserts given value into vector before specified iterator. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__position</i> An iterator into the vector.<br />
 <i>__x</i> Data to be inserted.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>An iterator that points to the inserted data.</dl>
<p> This function will insert a copy of the given value before the specified location. Note that this kind of operation could be expensive for a vector and if it is frequently used the user should consider using std::list.</p>
<h3>iterator <code>std::vector</code>&lt; <code>_State</code> , <code>std::allocator</code>&lt;<code>_State</code> &gt; &gt;::insert (iterator__position, value_type &amp;&amp;__x) [inline], [inherited]</h3>
<p>Inserts given rvalue into vector before specified iterator. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__position</i> An iterator into the vector.<br />
 <i>__x</i> Data to be inserted.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>An iterator that points to the inserted data.</dl>
<p> This function will insert a copy of the given rvalue before the specified location. Note that this kind of operation could be expensive for a vector and if it is frequently used the user should consider using std::list. </p>
<p> Definition at line 988 of file stl_vector.h. </p>
<p> References std::vector&lt; _Tp, _Alloc &gt;::emplace().</p>
<h3><code>void</code> <code>std::vector</code>&lt; <code>_State</code> , <code>std::allocator</code>&lt;<code>_State</code> &gt; &gt;::insert (iterator__position, <code>initializer_list</code>&lt; value_type &gt;__l) [inline], [inherited]</h3>
<p>Inserts an initializer_list into the vector. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__position</i> An iterator into the vector.<br />
 <i>__l</i> An initializer_list.</dl>
<p> This function will insert copies of the data in the initializer_list <i>l</i> into the vector before the location specified by <i>position</i>. </p>
<p> Note that this kind of operation could be expensive for a vector and if it is frequently used the user should consider using std::list. </p>
<p> Definition at line 1005 of file stl_vector.h. </p>
<p> References std::vector&lt; _Tp, _Alloc &gt;::insert().</p>
<h3><code>void</code> <code>std::vector</code>&lt; <code>_State</code> , <code>std::allocator</code>&lt;<code>_State</code> &gt; &gt;::insert (iterator__position, size_type__n, const value_type &amp;__x) [inline], [inherited]</h3>
<p>Inserts a number of copies of given data into the vector. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__position</i> An iterator into the vector.<br />
 <i>__n</i> Number of elements to be inserted.<br />
 <i>__x</i> Data to be inserted.</dl>
<p> This function will insert a specified number of copies of the given data before the location specified by <i>position</i>. </p>
<p> Note that this kind of operation could be expensive for a vector and if it is frequently used the user should consider using std::list. </p>
<p> Definition at line 1023 of file stl_vector.h.</p>
<h3><code>void</code> <code>std::vector</code>&lt; <code>_State</code> , <code>std::allocator</code>&lt;<code>_State</code> &gt; &gt;::insert (iterator__position, _InputIterator__first, _InputIterator__last) [inline], [inherited]</h3>
<p>Inserts a range into the vector. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__position</i> An iterator into the vector.<br />
 <i>__first</i> An input iterator.<br />
 <i>__last</i> An input iterator.</dl>
<p> This function will insert copies of the data in the range [__first,__last) into the vector before the location specified by <i>pos</i>. </p>
<p> Note that this kind of operation could be expensive for a vector and if it is frequently used the user should consider using std::list. </p>
<p> Definition at line 1044 of file stl_vector.h.</p>
<h3>size_type <code>std::vector</code>&lt; <code>_State</code> , <code>std::allocator</code>&lt;<code>_State</code> &gt; &gt;::max_size () const [inline], [noexcept], [inherited]</h3>
<p>Returns the size() of the largest possible vector. </p>
<p> Definition at line 650 of file stl_vector.h. </p>
<p> References std::allocator_traits&lt; _Tp_alloc_type &gt;::max_size().</p>
<h3>reference <code>std::vector</code>&lt; <code>_State</code> , <code>std::allocator</code>&lt;<code>_State</code> &gt; &gt;::operator[] (size_type__n) [inline], [inherited]</h3>
<p>Subscript access to the data contained in the vector. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__n</i> The index of the element for which data should be accessed.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>Read/write reference to data.</dl>
<p> This operator allows for easy, array-style, data access. Note that data access with this operator is unchecked and out_of_range lookups are not defined. (For checked lookups see at().) </p>
<p> Definition at line 770 of file stl_vector.h.</p>
<h3>const_reference <code>std::vector</code>&lt; <code>_State</code> , <code>std::allocator</code>&lt;<code>_State</code> &gt; &gt;::operator[] (size_type__n) const [inline], [inherited]</h3>
<p>Subscript access to the data contained in the vector. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__n</i> The index of the element for which data should be accessed.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>Read-only (constant) reference to data.</dl>
<p> This operator allows for easy, array-style, data access. Note that data access with this operator is unchecked and out_of_range lookups are not defined. (For checked lookups see at().) </p>
<p> Definition at line 785 of file stl_vector.h.</p>
<h3><code>void</code> <code>std::vector</code>&lt; <code>_State</code> , <code>std::allocator</code>&lt;<code>_State</code> &gt; &gt;::pop_back () [inline], [inherited]</h3>
<p>Removes last element. This is a typical stack operation. It shrinks the vector by one. </p>
<p> Note that no data is returned, and if the last element&#8217;s data is needed, it should be retrieved before pop_back() is called. </p>
<p> Definition at line 937 of file stl_vector.h.</p>
<h3><code>void</code> <code>std::vector</code>&lt; <code>_State</code> , <code>std::allocator</code>&lt;<code>_State</code> &gt; &gt;::push_back (const value_type &amp;__x) [inline], [inherited]</h3>
<p>Add data to the end of the vector. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__x</i> Data to be added.</dl>
<p> This is a typical stack operation. The function creates an element at the end of the vector and assigns the given data to it. Due to the nature of a vector this operation can be done in constant time if the vector has preallocated space available. </p>
<p> Definition at line 901 of file stl_vector.h. </p>
<p> References std::vector&lt; _Tp, _Alloc &gt;::end().</p>
<h3><code>reverse_iterator</code> <code>std::vector</code>&lt; <code>_State</code> , <code>std::allocator</code>&lt;<code>_State</code> &gt; &gt;::rbegin () [inline], [noexcept], [inherited]</h3>
<p>Returns a read/write reverse iterator that points to the last element in the vector. Iteration is done in reverse element order. </p>
<p> Definition at line 574 of file stl_vector.h. </p>
<p> References std::vector&lt; _Tp, _Alloc &gt;::end().</p>
<h3><code>const_reverse_iterator</code> <code>std::vector</code>&lt; <code>_State</code> , <code>std::allocator</code>&lt;<code>_State</code> &gt; &gt;::rbegin () const [inline], [noexcept], [inherited]</h3>
<p>Returns a read-only (constant) reverse iterator that points to the last element in the vector. Iteration is done in reverse element order. </p>
<p> Definition at line 583 of file stl_vector.h. </p>
<p> References std::vector&lt; _Tp, _Alloc &gt;::end().</p>
<h3><code>reverse_iterator</code> <code>std::vector</code>&lt; <code>_State</code> , <code>std::allocator</code>&lt;<code>_State</code> &gt; &gt;::rend () [inline], [noexcept], [inherited]</h3>
<p>Returns a read/write reverse iterator that points to one before the first element in the vector. Iteration is done in reverse element order. </p>
<p> Definition at line 592 of file stl_vector.h. </p>
<p> References std::vector&lt; _Tp, _Alloc &gt;::begin().</p>
<h3><code>const_reverse_iterator</code> <code>std::vector</code>&lt; <code>_State</code> , <code>std::allocator</code>&lt;<code>_State</code> &gt; &gt;::rend () const [inline], [noexcept], [inherited]</h3>
<p>Returns a read-only (constant) reverse iterator that points to one before the first element in the vector. Iteration is done in reverse element order. </p>
<p> Definition at line 601 of file stl_vector.h. </p>
<p> References std::vector&lt; _Tp, _Alloc &gt;::begin().</p>
<h3><code>void</code> <code>std::vector</code>&lt; <code>_State</code> , <code>std::allocator</code>&lt;<code>_State</code> &gt; &gt;::reserve (size_type__n) [inherited]</h3>
<p>Attempt to preallocate enough memory for specified number of elements. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__n</i> Number of elements required.</dl>
<p> <code>Exceptions:</code></p>
<dl>
<dd><i>std::length_error</i> If <i>n</i> exceeds max_size().</dl>
<p> This function attempts to reserve enough memory for the vector to hold the specified number of elements. If the number requested is more than max_size(), length_error is thrown. </p>
<p> The advantage of this function is that if optimal code is a necessity and the user can determine the number of elements that will be required, the user can reserve the memory in advance, and thus prevent a possible reallocation of memory and copying of vector data.</p>
<h3><code>void</code> <code>std::vector</code>&lt; <code>_State</code> , <code>std::allocator</code>&lt;<code>_State</code> &gt; &gt;::resize (size_type__new_size) [inline], [inherited]</h3>
<p>Resizes the vector to the specified number of elements. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__new_size</i> Number of elements the vector should contain.</dl>
<p> This function will resize the vector to the specified number of elements. If the number is smaller than the vector&#8217;s current size the vector is truncated, otherwise default constructed elements are appended. </p>
<p> Definition at line 664 of file stl_vector.h. </p>
<p> References std::vector&lt; _Tp, _Alloc &gt;::size().</p>
<h3><code>void</code> <code>std::vector</code>&lt; <code>_State</code> , <code>std::allocator</code>&lt;<code>_State</code> &gt; &gt;::resize (size_type__new_size, const value_type &amp;__x) [inline], [inherited]</h3>
<p>Resizes the vector to the specified number of elements. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__new_size</i> Number of elements the vector should contain.<br />
 <i>__x</i> Data with which new elements should be populated.</dl>
<p> This function will resize the vector to the specified number of elements. If the number is smaller than the vector&#8217;s current size the vector is truncated, otherwise the vector is extended and new elements are populated with given data. </p>
<p> Definition at line 684 of file stl_vector.h. </p>
<p> References std::vector&lt; _Tp, _Alloc &gt;::end(), std::vector&lt; _Tp, _Alloc &gt;::insert(), and std::vector&lt; _Tp, _Alloc &gt;::size().</p>
<h3><code>void</code> <code>std::vector</code>&lt; <code>_State</code> , <code>std::allocator</code>&lt;<code>_State</code> &gt; &gt;::shrink_to_fit () [inline], [inherited]</h3>
<p>A non-binding request to reduce capacity() to size(). </p>
<p> Definition at line 716 of file stl_vector.h.</p>
<h3>size_type <code>std::vector</code>&lt; <code>_State</code> , <code>std::allocator</code>&lt;<code>_State</code> &gt; &gt;::size () const [inline], [noexcept], [inherited]</h3>
<p>Returns the number of elements in the vector. </p>
<p> Definition at line 645 of file stl_vector.h.</p>
<h2>Member Data Documentation</h2>
<h3><code>std::vector</code>&lt; <code>_State</code> , <code>std::allocator</code>&lt;<code>_State</code> &gt; &gt;::__pad0__ [explicit], [inherited]</h3>
<p>Creates a vector with default constructed elements. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__n</i> The number of elements to initially create.<br />
 <i>__a</i> An allocator.</dl>
<p> This constructor fills the vector with <i>__n</i> default constructed elements. </p>
<p> Definition at line 270 of file stl_vector.h.</p>
<h3><code>std::vector</code>&lt; <code>_State</code> , <code>std::allocator</code>&lt;<code>_State</code> &gt; &gt;::void [inherited]</h3>
<p>Swaps data with another vector. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__x</i> A vector of the same element and allocator types.</dl>
<p> This exchanges the elements between two vectors in constant time. (Three pointers, so it should be quite fast.) Note that the global std::swap() function is specialized such that std::swap(v1,v2) will feed to this function. </p>
<p> Definition at line 1112 of file stl_vector.h.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
