---
title: "stdshift_leftstdshift_right(3)"
name: "stdshift_leftstdshift_right"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdshift_leftstdshift_right/"
description: "std::shift_left,std::shift_right – std::shift_left,std::shift_right"
---

<p>std::shift_left,std::shift_right &#8211; std::shift_left,std::shift_right</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;algorithm&gt;

template&lt; class ForwardIt &gt;

constexpr ForwardIt shift_left( ForwardIt first, ForwardIt last,                  (1) (since C++20)

typename std::iterator_traits&lt;ForwardIt&gt;::difference_type n );

template&lt; class ExecutionPolicy, class ForwardIt &gt;

ForwardIt shift_left( ExecutionPolicy&amp;&amp; policy, ForwardIt first, ForwardIt last,  (2) (since C++20)

typename std::iterator_traits&lt;ForwardIt&gt;::difference_type n );

template&lt; class ForwardIt &gt;

constexpr ForwardIt shift_right( ForwardIt first, ForwardIt last,                 (3) (since C++20)

typename std::iterator_traits&lt;ForwardIt&gt;::difference_type n );

template&lt; class ExecutionPolicy, class ForwardIt &gt;

ForwardIt shift_right( ExecutionPolicy&amp;&amp; policy, ForwardIt first, ForwardIt last, (4) (since C++20)

typename std::iterator_traits&lt;ForwardIt&gt;::difference_type n );</code></pre>
<p>Shifts the elements in the range [first, last) by n positions.<br />
1) Shifts the elements towards the beginning of the range. If n &lt;= 0 || n &gt;= last &#8211; first, there are no effects. Otherwise, for every integer i in [0, last &#8211; first &#8211; n), moves the element originally at position first + n + i to position first + i. The moves are performed in increasing order of i starting from 0.<br />
3) Shifts the elements towards the end of the range. If n &lt;= 0 || n &gt;= last &#8211; first, there are no effects. Otherwise, for every integer i in [0, last &#8211; first &#8211; n), moves the element originally at position first + i to position first + n + i. If ForwardIt meets the LegacyBidirectionalIterator requirements, then the moves are performed in decreasing order of i starting from last &#8211; first &#8211; n &#8211; 1.<br />
2,4) Same as <code>(1)</code> and <code>(3)</code>, respectively, but executed according to policy and the moves may be performed in any order. These overloads does not participate in overload resolution unless std::is_execution_policy_v&lt;std::decay_t&lt;ExecutionPolicy&gt;&gt; is true.<br />
Elements that are in the original range but not the new range are left in a valid but unspecified state. </p>
<h2>Parameters</h2>
<p>first &#8211; the beginning of the original range<br />
last &#8211; the end of the original range<br />
n &#8211; the number of positions to shift<br />
policy &#8211; the execution policy to use. See execution_policy for details.</p>
<h2>Type requirements</h2>
<p>&#8211;<br />
ForwardIt must meet the requirements of LegacyForwardIterator.<br />
&#8211;<br />
ForwardIt must meet either the requirements of LegacyBidirectionalIterator or the requirements of ValueSwappable for overloads (3-4).<br />
&#8211;<br />
The type of dereferenced ForwardIt must meet the requirements of MoveAssignable.</p>
<h2>Return value</h2>
<p>1-2) The end of the resulting range. If n is positive and less than last &#8211; first, returns first + (last &#8211; first &#8211; n). Otherwise if n is positive, returns first. Otherwise, returns last.<br />
3-4) The beginning of the resulting range. If n is positive and less than last &#8211; first, returns first + n. Otherwise if n is positive, returns last. Otherwise, returns first. </p>
<h2>Complexity</h2>
<p>1-2) At most std::distance(first, last) &#8211; n assignments.<br />
3-4) At most std::distance(first, last) &#8211; n assignment or swaps.</p>
<h2>Exceptions</h2>
<p>The overloads with a template parameter named ExecutionPolicy report errors as follows: </p>
<p>* If execution of a function invoked as part of the algorithm throws an exception and ExecutionPolicy is one of the standard_policies, std::terminate is called. For any other ExecutionPolicy, the behavior is implementation-defined.<br />
* If the algorithm fails to allocate memory, std::bad_alloc is thrown.</p>
<h2>See also</h2>
<p>move moves a range of elements to a new location<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++11)</i><br />
move_backward moves a range of elements to a new location in backwards order<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++11)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;rotates the order of elements in a range<br />
rotate <i>(function template)</i> </p>
