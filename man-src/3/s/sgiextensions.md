---
title: "sgiextensions(3)"
name: "sgiextensions"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sgiextensions/"
description: "SGI –"
---

<p>SGI &#8211;</p>
<h2>Synopsis</h2>
<h3>Classes</h3>
<p>class <code>__gnu_cxx::binary_compose&lt; _Operation1, _Operation2, _Operation3 &gt;</code> </p>
<p> struct <code>__gnu_cxx::constant_binary_fun&lt; _Result, _Arg1, _Arg2 &gt;</code> </p>
<p> struct <code>__gnu_cxx::constant_unary_fun&lt; _Result, _Argument &gt;</code> </p>
<p> struct <code>__gnu_cxx::constant_void_fun&lt; _Result &gt;</code> </p>
<p> class <code>__gnu_cxx::hash_map&lt; _Key, _Tp, _HashFn, _EqualKey, _Alloc &gt;</code> </p>
<p> class <code>__gnu_cxx::hash_multimap&lt; _Key, _Tp, _HashFn, _EqualKey, _Alloc &gt;</code> </p>
<p> class <code>__gnu_cxx::hash_multiset&lt; _Value, _HashFcn, _EqualKey, _Alloc &gt;</code> </p>
<p> class <code>__gnu_cxx::hash_set&lt; _Value, _HashFcn, _EqualKey, _Alloc &gt;</code> </p>
<p> struct <code>__gnu_cxx::project1st&lt; _Arg1, _Arg2 &gt;</code> </p>
<p> struct <code>__gnu_cxx::project2nd&lt; _Arg1, _Arg2 &gt;</code> </p>
<p> struct <code>__gnu_cxx::rb_tree&lt; _Key, _Value, _KeyOfValue, _Compare, _Alloc &gt;</code> </p>
<p> class <code>__gnu_cxx::rope&lt; _CharT, _Alloc &gt;</code> </p>
<p> struct <code>__gnu_cxx::select1st&lt; _Pair &gt;</code> </p>
<p> struct <code>__gnu_cxx::select2nd&lt; _Pair &gt;</code> </p>
<p> class <code>__gnu_cxx::slist&lt; _Tp, _Alloc &gt;</code> </p>
<p> class <code>__gnu_cxx::subtractive_rng</code> </p>
<p> struct <code>__gnu_cxx::temporary_buffer&lt; _ForwardIterator, _Tp &gt;</code> </p>
<p> class <code>__gnu_cxx::unary_compose&lt; _Operation1, _Operation2 &gt;</code> </p>
<h3>Functions</h3>
<p>template&lt;typename _Tp &gt; const _Tp &amp; <code>__gnu_cxx::__median</code> (const _Tp &amp;__a, const _Tp &amp;__b, const _Tp &amp;__c) </p>
<p> template&lt;typename _Tp , typename _Compare &gt; const _Tp &amp; <code>__gnu_cxx::__median</code> (const _Tp &amp;__a, const _Tp &amp;__b, const _Tp &amp;__c, _Compare __comp) </p>
<p> size_t <code>std::_Find_first</code> () const noexcept </p>
<p> size_t <code>std::_Find_next</code> (size_t __prev) const noexcept </p>
<p> template&lt;class _Operation1 , class _Operation2 &gt; unary_compose&lt; _Operation1,<br />
 _Operation2 &gt; <code>__gnu_cxx::compose1</code> (const _Operation1 &amp;__fn1, const _Operation2 &amp;__fn2)&quot; </p>
<p> template&lt;class _Operation1 , class _Operation2 , class _Operation3 &gt; binary_compose&lt; _Operation1,<br />
 _Operation2, _Operation3 &gt; <code>__gnu_cxx::compose2</code> (const _Operation1 &amp;__fn1, const _Operation2 &amp;__fn2, const _Operation3 &amp;__fn3)&quot; </p>
<p> template&lt;class _Result &gt; constant_void_fun&lt; _Result &gt; <code>__gnu_cxx::constant0</code> (const _Result &amp;__val) </p>
<p> template&lt;class _Result &gt; constant_unary_fun&lt; _Result,<br />
 _Result &gt; <code>__gnu_cxx::constant1</code> (const _Result &amp;__val)&quot; </p>
<p> template&lt;class _Result &gt; constant_binary_fun&lt; _Result,<br />
 _Result, _Result &gt; <code>__gnu_cxx::constant2</code> (const _Result &amp;__val)&quot; </p>
<p> template&lt;typename _InputIterator , typename _Size , typename _OutputIterator &gt; pair&lt; _InputIterator,<br />
 _OutputIterator &gt; <code>__gnu_cxx::copy_n</code> (_InputIterator __first, _Size __count, _OutputIterator __result)&quot; </p>
<p> template&lt;typename _InputIterator , typename _Distance &gt; void <code>__gnu_cxx::distance</code> (_InputIterator __first, _InputIterator __last, _Distance &amp;__n) </p>
<p> template&lt;class _Tp &gt; _Tp <code>__gnu_cxx::identity_element</code> (<code>std::plus</code>&lt; _Tp &gt;) </p>
<p> template&lt;class _Tp &gt; _Tp <code>__gnu_cxx::identity_element</code> (<code>std::multiplies</code>&lt; _Tp &gt;) </p>
<p> template&lt;typename _InputIterator1 , typename _InputIterator2 &gt; int <code>__gnu_cxx::lexicographical_compare_3way</code> (_InputIterator1 __first1, _InputIterator1 __last1, _InputIterator2 __first2, _InputIterator2 __last2) </p>
<p> template&lt;typename _Tp , typename _Integer , typename _MonoidOperation &gt; _Tp <code>__gnu_cxx::power</code> (_Tp __x, _Integer __n, _MonoidOperation __monoid_op) </p>
<p> template&lt;typename _Tp , typename _Integer &gt; _Tp <code>__gnu_cxx::power</code> (_Tp __x, _Integer __n) </p>
<p> template&lt;typename _InputIterator , typename _RandomAccessIterator &gt; _RandomAccessIterator <code>__gnu_cxx::random_sample</code> (_InputIterator __first, _InputIterator __last, _RandomAccessIterator __out_first, _RandomAccessIterator __out_last) </p>
<p> template&lt;typename _InputIterator , typename _RandomAccessIterator , typename _RandomNumberGenerator &gt; _RandomAccessIterator <code>__gnu_cxx::random_sample</code> (_InputIterator __first, _InputIterator __last, _RandomAccessIterator __out_first, _RandomAccessIterator __out_last, _RandomNumberGenerator &amp;__rand) </p>
<p> template&lt;typename _ForwardIterator , typename _OutputIterator , typename _Distance &gt; _OutputIterator <code>__gnu_cxx::random_sample_n</code> (_ForwardIterator __first, _ForwardIterator __last, _OutputIterator __out, const _Distance __n) </p>
<p> template&lt;typename _ForwardIterator , typename _OutputIterator , typename _Distance , typename _RandomNumberGenerator &gt; _OutputIterator <code>__gnu_cxx::random_sample_n</code> (_ForwardIterator __first, _ForwardIterator __last, _OutputIterator __out, const _Distance __n, _RandomNumberGenerator &amp;__rand) </p>
<p> template&lt;typename _InputIter , typename _Size , typename _ForwardIter &gt; pair&lt; _InputIter, _ForwardIter &gt; <code>__gnu_cxx::uninitialized_copy_n</code> (_InputIter __first, _Size __count, _ForwardIter __result) </p>
<p> bitset&lt; _Nb &gt; &amp; <code>std::_Unchecked_set</code> (size_t __pos) noexcept </p>
<p> bitset&lt; _Nb &gt; &amp; <code>std::_Unchecked_set</code> (size_t __pos, int __val) noexcept </p>
<p> bitset&lt; _Nb &gt; &amp; <code>std::_Unchecked_reset</code> (size_t __pos) noexcept </p>
<p> bitset&lt; _Nb &gt; &amp; <code>std::_Unchecked_flip</code> (size_t __pos) noexcept </p>
<p> constexpr bool <code>std::_Unchecked_test</code> (size_t __pos) const noexcept </p>
<h2>Detailed Description</h2>
<p>Because libstdc++ based its implementation of the STL subsections of the library on the SGI 3.3 implementation, we inherited their extensions as well. </p>
<p> They are additionally documented in the online documentation, a copy of which is also shipped with the library source code (in &#8230;/docs/html/documentation.html). You can also read the documentation on SGI&#8217;s site, which is still running even though the code is not maintained. </p>
<p> <code>NB</code> that the following notes are pulled from various comments all over the place, so they may seem stilted. </p>
<p> The identity_element functions are not part of the C++ standard; SGI provided them as an extension. Its argument is an operation, and its return value is the identity element for that operation. It is overloaded for addition and multiplication, and you can overload it for your own nefarious operations. </p>
<p> As an extension to the binders, SGI provided composition functors and wrapper functions to aid in their creation. The unary_compose functor is constructed from two functions/functors, f and g. Calling operator() with a single argument x returns f(g(x)). The function compose1 takes the two functions and constructs a unary_compose variable for you. </p>
<p> binary_compose is constructed from three functors, f, g1, and g2. Its operator() returns f(g1(x),g2(x)). The function compose2 takes f, g1, and g2, and constructs the binary_compose instance for you. For example, if f returns an int, then </p>
<pre>* int answer = (compose2(f,g1,g2))(x);
* </pre>
<p>&nbsp;<wbr>is equivalent to&nbsp;<wbr> </p>
<pre>* int temp1 = g1(x);
* int temp2 = g2(x);
* int answer = f(temp1,temp2);
* </pre>
<p>&nbsp;<wbr>But the first form is more compact, and can be passed around as a functor to other algorithms. </p>
<p> As an extension, SGI provided a functor called identity. When a functor is required but no operations are desired, this can be used as a pass-through. Its operator() returns its argument unchanged. </p>
<p> select1st and select2nd are extensions provided by SGI. Their operator()s take a std::pair as an argument, and return either the first member or the second member, respectively. They can be used (especially with the composition functors) to <i>strip</i> data from a sequence before performing the remainder of an algorithm. </p>
<p> The operator() of the project1st functor takes two arbitrary arguments and returns the first one, while project2nd returns the second one. They are extensions provided by SGI. </p>
<p> These three functors are each constructed from a single arbitrary variable/value. Later, their operator()s completely ignore any arguments passed, and return the stored value.</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>constant_void_fun&#8217;s operator() takes no arguments</p>
<dt>&bull;</p>
<dd>constant_unary_fun&#8217;s operator() takes one argument (ignored)</p>
<dt>&bull;</p>
<dd>constant_binary_fun&#8217;s operator() takes two arguments (ignored)</dl>
<p> The helper creator functions constant0, constant1, and constant2 each take a <i>result</i> argument and construct variables of the appropriate functor type.</p>
<h2>Function Documentation</h2>
<h3>template&lt;typename _Tp &gt; const _Tp&amp; __gnu_cxx::__median (const _Tp &amp;__a, const _Tp &amp;__b, const _Tp &amp;__c)</h3>
<p>Find the median of three values. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>__a</i> A value.<br />
 <i>__b</i> A value.<br />
 <i>__c</i> A value.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>One of a, b or c.</dl>
<p> If {l,m,n} is some convolution of {a,b,c} such that l&lt;=m&lt;=n then the value returned will be m. This is an SGI extension. </p>
<p> Definition at line 546 of file ext/algorithm.</p>
<h3>template&lt;typename _Tp , typename _Compare &gt; const _Tp&amp; __gnu_cxx::__median (const _Tp &amp;__a, const _Tp &amp;__b, const _Tp &amp;__c, _Compare__comp)</h3>
<p>Find the median of three values using a predicate for comparison. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>__a</i> A value.<br />
 <i>__b</i> A value.<br />
 <i>__c</i> A value.<br />
 <i>__comp</i> A binary predicate.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>One of a, b or c.</dl>
<p> If {l,m,n} is some convolution of {a,b,c} such that comp(l,m) and comp(m,n) are both true then the value returned will be m. This is an SGI extension. </p>
<p> Definition at line 580 of file ext/algorithm.</p>
<h3>size_t std::_Find_first () const [noexcept]</h3>
<p>Finds the index of the first &#8216;on&#8217; bit. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The index of the first bit set, or size() if not found.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>_Find_next</dl>
<p> Definition at line 1354 of file bitset.</p>
<h3>size_t std::_Find_next (size_t__prev) const [noexcept]</h3>
<p>Finds the index of the next &#8216;on&#8217; bit after prev. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The index of the next bit set, or size() if not found.</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>__prev</i> Where to start searching.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>_Find_first</dl>
<p> Definition at line 1365 of file bitset.</p>
<h3>bitset&lt;_Nb&gt;&amp; std::_Unchecked_flip (size_t__pos) [noexcept]</h3>
<p>These versions of single-bit set, reset, flip, and test are extensions from the SGI version. They do no range checking. </p>
<p> Definition at line 1037 of file bitset. </p>
<p> Referenced by std::flip().</p>
<h3>bitset&lt;_Nb&gt;&amp; std::_Unchecked_reset (size_t__pos) [noexcept]</h3>
<p>These versions of single-bit set, reset, flip, and test are extensions from the SGI version. They do no range checking. </p>
<p> Definition at line 1030 of file bitset. </p>
<p> Referenced by std::reset().</p>
<h3>bitset&lt;_Nb&gt;&amp; std::_Unchecked_set (size_t__pos) [noexcept]</h3>
<p>These versions of single-bit set, reset, flip, and test are extensions from the SGI version. They do no range checking. </p>
<p> Definition at line 1013 of file bitset. </p>
<p> Referenced by std::set().</p>
<h3>bitset&lt;_Nb&gt;&amp; std::_Unchecked_set (size_t__pos, int__val) [noexcept]</h3>
<p>These versions of single-bit set, reset, flip, and test are extensions from the SGI version. They do no range checking. </p>
<p> Definition at line 1020 of file bitset.</p>
<h3>constexpr bool std::_Unchecked_test (size_t__pos) const [noexcept]</h3>
<p>These versions of single-bit set, reset, flip, and test are extensions from the SGI version. They do no range checking. </p>
<p> Definition at line 1044 of file bitset. </p>
<p> Referenced by std::test().</p>
<h3>template&lt;class _Operation1 , class _Operation2 &gt; unary_compose&lt;_Operation1, _Operation2&gt; __gnu_cxx::compose1 (const _Operation1 &amp;__fn1, const _Operation2 &amp;__fn2) [inline]</h3>
<p>An <code>SGI extension </code>. </p>
<p> Definition at line 145 of file ext/functional.</p>
<h3>template&lt;class _Operation1 , class _Operation2 , class _Operation3 &gt; binary_compose&lt;_Operation1, _Operation2, _Operation3&gt; __gnu_cxx::compose2 (const _Operation1 &amp;__fn1, const _Operation2 &amp;__fn2, const _Operation3 &amp;__fn3) [inline]</h3>
<p>An <code>SGI extension </code>. </p>
<p> Definition at line 172 of file ext/functional.</p>
<h3>template&lt;class _Result &gt; constant_void_fun&lt;_Result&gt; __gnu_cxx::constant0 (const _Result &amp;__val) [inline]</h3>
<p>An <code>SGI extension </code>. </p>
<p> Definition at line 330 of file ext/functional.</p>
<h3>template&lt;class _Result &gt; constant_unary_fun&lt;_Result, _Result&gt; __gnu_cxx::constant1 (const _Result &amp;__val) [inline]</h3>
<p>An <code>SGI extension </code>. </p>
<p> Definition at line 336 of file ext/functional.</p>
<h3>template&lt;class _Result &gt; constant_binary_fun&lt;_Result,_Result,_Result&gt; __gnu_cxx::constant2 (const _Result &amp;__val) [inline]</h3>
<p>An <code>SGI extension </code>. </p>
<p> Definition at line 342 of file ext/functional.</p>
<h3>template&lt;typename _InputIterator , typename _Size , typename _OutputIterator &gt; pair&lt;_InputIterator, _OutputIterator&gt; __gnu_cxx::copy_n (_InputIterator__first, _Size__count, _OutputIterator__result) [inline]</h3>
<p>Copies the range [first,first+count) into [result,result+count). </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>__first</i> An input iterator.<br />
 <i>__count</i> The number of elements to copy.<br />
 <i>__result</i> An output iterator.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A std::pair composed of first+count and result+count.</dl>
<p> This is an SGI extension. This inline function will boil down to a call to memmove whenever possible. Failing that, if random access iterators are passed, then the loop count will be known (and therefore a candidate for compiler optimizations such as unrolling). </p>
<p> Definition at line 120 of file ext/algorithm. </p>
<p> References std::__iterator_category().</p>
<h3>template&lt;typename _InputIterator , typename _Distance &gt; void __gnu_cxx::distance (_InputIterator__first, _InputIterator__last, _Distance &amp;__n) [inline]</h3>
<p>This is an SGI extension. </p>
<p> <code>Todo</code></p>
<dl COMPACT>
<dd>Needs documentation! See <a rel="nofollow" href="http://gcc.gnu.org/onlinedocs/libstdc++/manual/documentation_style.html">http://gcc.gnu.org/onlinedocs/libstdc++/manual/documentation_style.html</a></dl>
<p> Definition at line 105 of file ext/iterator. </p>
<p> References std::__iterator_category().</p>
<h3>template&lt;class _Tp &gt; _Tp __gnu_cxx::identity_element (<code>std::plus</code>&lt; _Tp &gt;) [inline]</h3>
<p>An <code>SGI extension </code>. </p>
<p> Definition at line 87 of file ext/functional.</p>
<h3>template&lt;class _Tp &gt; _Tp __gnu_cxx::identity_element (<code>std::multiplies</code>&lt; _Tp &gt;) [inline]</h3>
<p>An <code>SGI extension </code>. </p>
<p> Definition at line 93 of file ext/functional.</p>
<h3>template&lt;typename _InputIterator1 , typename _InputIterator2 &gt; int __gnu_cxx::lexicographical_compare_3way (_InputIterator1__first1, _InputIterator1__last1, _InputIterator2__first2, _InputIterator2__last2)</h3>
<p>memcmp on steroids. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>__first1</i> An input iterator.<br />
 <i>__last1</i> An input iterator.<br />
 <i>__first2</i> An input iterator.<br />
 <i>__last2</i> An input iterator.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>An int, as with memcmp.</dl>
<p> The return value will be less than zero if the first range is <i>lexigraphically less than</i> the second, greater than zero if the second range is <i>lexigraphically less than</i> the first, and zero otherwise. This is an SGI extension. </p>
<p> Definition at line 201 of file ext/algorithm.</p>
<h3>template&lt;typename _Tp , typename _Integer , typename _MonoidOperation &gt; _Tp __gnu_cxx::power (_Tp__x, _Integer__n, _MonoidOperation__monoid_op) [inline]</h3>
<p>This is an SGI extension. </p>
<p> <code>Todo</code></p>
<dl COMPACT>
<dd>Needs documentation! See <a rel="nofollow" href="http://gcc.gnu.org/onlinedocs/libstdc++/manual/documentation_style.html">http://gcc.gnu.org/onlinedocs/libstdc++/manual/documentation_style.html</a></dl>
<p> Definition at line 113 of file ext/numeric.</p>
<h3>template&lt;typename _Tp , typename _Integer &gt; _Tp __gnu_cxx::power (_Tp__x, _Integer__n) [inline]</h3>
<p>This is an SGI extension. </p>
<p> <code>Todo</code></p>
<dl COMPACT>
<dd>Needs documentation! See <a rel="nofollow" href="http://gcc.gnu.org/onlinedocs/libstdc++/manual/documentation_style.html">http://gcc.gnu.org/onlinedocs/libstdc++/manual/documentation_style.html</a></dl>
<p> Definition at line 123 of file ext/numeric.</p>
<h3>template&lt;typename _InputIterator , typename _RandomAccessIterator &gt; _RandomAccessIterator __gnu_cxx::random_sample (_InputIterator__first, _InputIterator__last, _RandomAccessIterator__out_first, _RandomAccessIterator__out_last) [inline]</h3>
<p>This is an SGI extension. </p>
<p> <code>Todo</code></p>
<dl COMPACT>
<dd>Needs documentation! See <a rel="nofollow" href="http://gcc.gnu.org/onlinedocs/libstdc++/manual/documentation_style.html">http://gcc.gnu.org/onlinedocs/libstdc++/manual/documentation_style.html</a></dl>
<p> Definition at line 388 of file ext/algorithm.</p>
<h3>template&lt;typename _InputIterator , typename _RandomAccessIterator , typename _RandomNumberGenerator &gt; _RandomAccessIterator __gnu_cxx::random_sample (_InputIterator__first, _InputIterator__last, _RandomAccessIterator__out_first, _RandomAccessIterator__out_last, _RandomNumberGenerator &amp;__rand) [inline]</h3>
<p>This is an SGI extension. </p>
<p> <code>Todo</code></p>
<dl COMPACT>
<dd>Needs documentation! See <a rel="nofollow" href="http://gcc.gnu.org/onlinedocs/libstdc++/manual/documentation_style.html">http://gcc.gnu.org/onlinedocs/libstdc++/manual/documentation_style.html</a></dl>
<p> Definition at line 411 of file ext/algorithm.</p>
<h3>template&lt;typename _ForwardIterator , typename _OutputIterator , typename _Distance &gt; _OutputIterator __gnu_cxx::random_sample_n (_ForwardIterator__first, _ForwardIterator__last, _OutputIterator__out, const _Distance__n)</h3>
<p>This is an SGI extension. </p>
<p> <code>Todo</code></p>
<dl COMPACT>
<dd>Needs documentation! See <a rel="nofollow" href="http://gcc.gnu.org/onlinedocs/libstdc++/manual/documentation_style.html">http://gcc.gnu.org/onlinedocs/libstdc++/manual/documentation_style.html</a></dl>
<p> Definition at line 267 of file ext/algorithm. </p>
<p> References std::distance(), and std::min().</p>
<h3>template&lt;typename _ForwardIterator , typename _OutputIterator , typename _Distance , typename _RandomNumberGenerator &gt; _OutputIterator __gnu_cxx::random_sample_n (_ForwardIterator__first, _ForwardIterator__last, _OutputIterator__out, const _Distance__n, _RandomNumberGenerator &amp;__rand)</h3>
<p>This is an SGI extension. </p>
<p> <code>Todo</code></p>
<dl COMPACT>
<dd>Needs documentation! See <a rel="nofollow" href="http://gcc.gnu.org/onlinedocs/libstdc++/manual/documentation_style.html">http://gcc.gnu.org/onlinedocs/libstdc++/manual/documentation_style.html</a></dl>
<p> Definition at line 301 of file ext/algorithm. </p>
<p> References std::distance(), and std::min().</p>
<h3>template&lt;typename _InputIter , typename _Size , typename _ForwardIter &gt; pair&lt;_InputIter, _ForwardIter&gt; __gnu_cxx::uninitialized_copy_n (_InputIter__first, _Size__count, _ForwardIter__result) [inline]</h3>
<p>Copies the range [first,last) into result. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>__first</i> An input iterator.<br />
 <i>__count</i> Length<br />
 <i>__result</i> An output iterator.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>__result + (__first + __count)</dl>
<p> Like copy(), but does not require an initialized output range. </p>
<p> Definition at line 122 of file ext/memory. </p>
<p> References std::__iterator_category().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
