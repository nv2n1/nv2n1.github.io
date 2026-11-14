---
title: "std_temporary_buffer(3)"
name: "std_temporary_buffer"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std_temporary_buffer/"
description: "std::_Temporary_buffer< _ForwardIterator, _Tp > –"
---

<p>std::_Temporary_buffer&lt; _ForwardIterator, _Tp &gt; &#8211;</p>
<h2>Synopsis</h2>
<p> Inherited by <code>__gnu_cxx::temporary_buffer&lt; _ForwardIterator, _Tp &gt;</code>.</p>
<h3>Public Types</h3>
<p>typedef pointer <code>iterator</code> </p>
<p> typedef value_type * <code>pointer</code> </p>
<p> typedef ptrdiff_t <code>size_type</code> </p>
<p> typedef _Tp <code>value_type</code></p>
<h3>Public Member Functions</h3>
<p><code>_Temporary_buffer</code> (_ForwardIterator __first, _ForwardIterator __last) </p>
<p> iterator <code>begin</code> () </p>
<p> iterator <code>end</code> () </p>
<p> size_type <code>requested_size</code> () const </p>
<p> size_type <code>size</code> () const</p>
<h3>Protected Attributes</h3>
<p>pointer <code>_M_buffer</code> </p>
<p> size_type <code>_M_len</code> </p>
<p> size_type <code>_M_original_len</code></p>
<h2>Detailed Description</h2>
<h3>template&lt;typename _ForwardIterator, typename _Tp&gt;class std::_Temporary_buffer&lt; _ForwardIterator, _Tp &gt;</h3>
<p>This class is used in two places: stl_algo.h and ext/memory, where it is wrapped as the temporary_buffer class. See temporary_buffer docs for more notes. </p>
<p> Definition at line 122 of file stl_tempbuf.h.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>template&lt;typename _ForwardIterator , typename _Tp &gt; <code>std::_Temporary_buffer</code>&lt; _ForwardIterator, _Tp &gt;::<code>_Temporary_buffer</code> (_ForwardIterator__first, _ForwardIterator__last)</h3>
<p>Constructs a temporary buffer of a size somewhere between zero and the size of the given range. </p>
<p> Definition at line 244 of file stl_tempbuf.h. </p>
<p> References std::pair&lt; _T1, _T2 &gt;::first, std::get_temporary_buffer(), std::return_temporary_buffer(), and std::pair&lt; _T1, _T2 &gt;::second.</p>
<h2>Member Function Documentation</h2>
<h3>template&lt;typename _ForwardIterator, typename _Tp&gt; iterator <code>std::_Temporary_buffer</code>&lt; _ForwardIterator, _Tp &gt;::begin () [inline]</h3>
<p>As per Table mumble. </p>
<p> Definition at line 151 of file stl_tempbuf.h. </p>
<p> Referenced by std::inplace_merge(), std::stable_partition(), and std::stable_sort().</p>
<h3>template&lt;typename _ForwardIterator, typename _Tp&gt; iterator <code>std::_Temporary_buffer</code>&lt; _ForwardIterator, _Tp &gt;::end () [inline]</h3>
<p>As per Table mumble. </p>
<p> Definition at line 156 of file stl_tempbuf.h.</p>
<h3>template&lt;typename _ForwardIterator, typename _Tp&gt; size_type <code>std::_Temporary_buffer</code>&lt; _ForwardIterator, _Tp &gt;::requested_size () const [inline]</h3>
<p>Returns the size requested by the constructor; may be &gt;size(). </p>
<p> Definition at line 146 of file stl_tempbuf.h. </p>
<p> Referenced by std::stable_partition().</p>
<h3>template&lt;typename _ForwardIterator, typename _Tp&gt; size_type <code>std::_Temporary_buffer</code>&lt; _ForwardIterator, _Tp &gt;::size () const [inline]</h3>
<p>As per Table mumble. </p>
<p> Definition at line 141 of file stl_tempbuf.h. </p>
<p> Referenced by std::inplace_merge(), std::stable_partition(), and std::stable_sort().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
