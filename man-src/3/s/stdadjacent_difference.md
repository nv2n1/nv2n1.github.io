---
title: "stdadjacent_difference(3)"
name: "stdadjacent_difference"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdadjacent_difference/"
description: "std::adjacent_difference – std::adjacent_difference"
---

<p>std::adjacent_difference &#8211; std::adjacent_difference</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;numeric&gt;

    template &lt;class InputIt, class OutputIt&gt;

    OutputIt adjacent_difference(InputIt first, InputIt last, (until C++ 20)

                                                                  OutputIt d_first);

template &lt;class InputIt, class OutputIt&gt;

constexpr OutputIt adjacent_difference(InputIt first, InputIt last, (since C++ 20)

                                                                        OutputIt d_first);

template &lt;class ExecutionPolicy, class ForwardIt1, class ForwardIt2&gt;

ForwardIt2 adjacent_difference(ExecutionPolicy &amp;&amp;policy, ForwardIt1 first, ForwardIt1 last, (2)(since C++ 17)

                                                                                                ForwardIt2 d_first);
(1)

    template &lt;class InputIt, class OutputIt, class BinaryOperation&gt;

    OutputIt adjacent_difference(InputIt first, InputIt last, (until C++ 20)

                                                                  OutputIt d_first,
                                 BinaryOperation op);

template &lt;class InputIt, class OutputIt, class BinaryOperation&gt;

constexpr OutputIt adjacent_difference(InputIt first, InputIt last, (3)(since C++ 20)

                                                                        OutputIt d_first,
                                       BinaryOperation op);

template &lt;class ExecutionPolicy, class ForwardIt1, class ForwardIt2, class BinaryOperation&gt;

ForwardIt2 adjacent_difference(ExecutionPolicy &amp;&amp;policy, ForwardIt1 first, ForwardIt1 last, (4)(since C++ 17)

                                                                                                ForwardIt2 d_first,
                               BinaryOperation op);
Computes the differences between the second and the first of each adjacent pair of elements of the range [first, last) and writes them to the range beginning at d_first + 1. An unmodified copy of *first is written to *d_first.

1,3) First, creates an accumulator acc whose type is InputIt's value type, initializes it with *first, and assigns the result to *d_first. Then, for every iterator i in [first + 1, last) in order, creates an object val whose type is InputIt's value type, initializes it with *i, computes

val - acc

(until C++20)

val - std::move(acc)

(since C++20) (overload (1)) or

op(val, acc)

(until C++20)

op(val, std::move(acc))

(since C++20) (overload (3)), assigns the result to *(d_first + (i - first)), and move assigns from val to acc.

first may be equal to d_first.

2,4) Performs *d_first = *first;. For every d in [1, last - first - 1], assigns *(first + d) - *(first + d - 1) (overload (2)) or op(*(first + d), *(first + d - 1)) (overload (4)) to *(d_first + d). This is executed according to policy. This overload only participates in overload resolution if std::is_execution_policy_v&lt;std::decay_t&lt;ExecutionPolicy&gt;&gt; is true.

The behavior is undefined if the input and output ranges overlap in any way.</code></pre>
<p>Equivalent operation: *(d_first)   = *first;</p>
<p>*(d_first+1) = *(first+1) &#8211; *(first);</p>
<p>*(d_first+2) = *(first+2) &#8211; *(first+1);</p>
<p>*(d_first+3) = *(first+3) &#8211; *(first+2);</p>
<p>&#8230;</p>
<p>op must not have side effects. <i>(until C++11)</i><br />
op must not invalidate any iterators, including the end iterators, or modify any elements of the ranges involved. <i>(since C++11)</i> </p>
<h2>Parameters</h2>
<p>first, last &#8211; the range of elements<br />
d_first &#8211; the beginning of the destination range<br />
policy &#8211; the execution policy to use. See execution_policy for details.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;binary operation function object that will be applied.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The signature of the function should be equivalent to the following:<br />
op &#8211; Ret fun(const Type1 &amp;a, const Type2 &amp;b);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The signature does not need to have const &amp;.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The types Type1 and Type2 must be such that an object of type iterator_traits&lt;InputIt&gt;::value_type can be implicitly converted to both of them. The type Ret must be such that an object of type OutputIt can be dereferenced and assigned a value of type Ret.</p>
<h2>Type requirements</h2>
<p>&#8211;<br />
InputIt must meet the requirements of LegacyInputIterator. InputIt&#8217;s value type must be MoveAssignable and constructible from the type of *first<br />
&#8211;<br />
OutputIt must meet the requirements of LegacyOutputIterator. both acc (the accumulated value) and the result of<br />
val &#8211; acc or op(val, acc)<br />
<i>(until C++20)</i><br />
val &#8211; std::move(acc) or op(val, std::move(acc))<br />
<i>(since C++20)</i> must be writable to OutputIt<br />
&#8211;<br />
ForwardIt1, ForwardIt2 must meet the requirements of LegacyForwardIterator. The results of *first, *first &#8211; *first (for <code>(2)</code>) and op(*first, *first) (for <code>(4)</code>) must be writable to ForwardIt2.</p>
<h2>Return value</h2>
<p>Iterator to the element past the last element written. </p>
<h2>Notes</h2>
<p>If first == last, this function has no effect and will merely return d_first. </p>
<h2>Complexity</h2>
<p>Exactly (last &#8211; first) &#8211; 1 applications of the binary operation</p>
<h2>Exceptions</h2>
<p>The overloads with a template parameter named ExecutionPolicy report errors as follows: </p>
<p>* If execution of a function invoked as part of the algorithm throws an exception and ExecutionPolicy is one of the standard_policies, std::terminate is called. For any other ExecutionPolicy, the behavior is implementation-defined.<br />
* If the algorithm fails to allocate memory, std::bad_alloc is thrown.</p>
<h2>Possible implementation</h2>
<h2>First version</h2>
<p>&nbsp;<wbr>&nbsp;template&lt;class InputIt, class OutputIt&gt;<br />
&nbsp;<wbr>&nbsp;OutputIt adjacent_difference(InputIt first, InputIt last,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;OutputIt d_first)<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (first == last) return d_first; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;typedef typename std::iterator_traits&lt;InputIt&gt;::value_type value_t;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;value_t acc = *first;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*d_first = acc;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while (++first != last) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;value_t val = *first;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*++d_first = val &#8211; std::move(acc); // std::move since C++20<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;acc = std::move(val);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return ++d_first;<br />
&nbsp;<wbr>&nbsp;}</p>
<h2>Second version</h2>
<p>&nbsp;<wbr>&nbsp;template&lt;class InputIt, class OutputIt, class BinaryOperation&gt;<br />
&nbsp;<wbr>&nbsp;OutputIt adjacent_difference(InputIt first, InputIt last,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;OutputIt d_first, BinaryOperation op)<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (first == last) return d_first; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;typedef typename std::iterator_traits&lt;InputIt&gt;::value_type value_t;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;value_t acc = *first;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*d_first = acc;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while (++first != last) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;value_t val = *first;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*++d_first = op(val, std::move(acc)); // std::move since C++20<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;acc = std::move(val);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return ++d_first;<br />
&nbsp;<wbr>&nbsp;}</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;numeric&gt;

#include &lt;vector&gt;

#include &lt;array&gt;

#include &lt;iostream&gt;

#include &lt;functional&gt;

#include &lt;iterator&gt;
int main()

{
    // Default implementation - the difference b/w two adjacent items
    std::vector v{2, 4, 6, 8, 10, 12, 14, 16, 18, 20};
    std::adjacent_difference(v.begin(), v.end(), v.begin());
    for (auto n : v)
        std::cout &lt;&lt; n &lt;&lt; ' ';
    std::cout &lt;&lt; '
';
    // Fibonacci
    std::array&lt;int, 10&gt; a{1};
    adjacent_difference(begin(a), std::prev(end(a)), std::next(begin(a)), std::plus&lt;&gt;{});
    copy(begin(a), end(a), std::ostream_iterator&lt;int&gt;{std::cout, &quot; &quot;});
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;2 2 2 2 2 2 2 2 2 2<br />
&nbsp;<wbr>&nbsp;1 1 2 3 5 8 13 21 34 55</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;computes the partial sum of a range of elements<br />
partial_sum <i>(function template)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sums up a range of elements<br />
accumulate <i>(function template)</i> </p>
