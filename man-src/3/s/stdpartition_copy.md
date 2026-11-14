---
title: "stdpartition_copy(3)"
name: "stdpartition_copy"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpartition_copy/"
description: "std::partition_copy – std::partition_copy"
---

<p>std::partition_copy &#8211; std::partition_copy</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;algorithm&gt;

template&lt; class InputIt, class OutputIt1,

class OutputIt2, class UnaryPredicate &gt;

std::pair&lt;OutputIt1, OutputIt2&gt;                                                      (since C++11)

partition_copy( InputIt first, InputIt last,                                         (until C++20)

OutputIt1 d_first_true, OutputIt2 d_first_false,

UnaryPredicate p );

template&lt; class InputIt, class OutputIt1,

class OutputIt2, class UnaryPredicate &gt;

constexpr std::pair&lt;OutputIt1, OutputIt2&gt;                                    (1)     (since C++20)

partition_copy( InputIt first, InputIt last,

OutputIt1 d_first_true, OutputIt2 d_first_false,

UnaryPredicate p );

template&lt; class ExecutionPolicy, class ForwardIt1, class ForwardIt2,

class ForwardIt3, class UnaryPredicate &gt;

std::pair&lt;ForwardIt2, ForwardIt3&gt;                                                (2) (since C++17)

partition_copy( ExecutionPolicy&amp;&amp; policy, ForwardIt1 first, ForwardIt1 last,

ForwardIt2 d_first_true, ForwardIt3 d_first_false,

UnaryPredicate p );</code></pre>
<p>1) Copies the elements from the range [first, last) to two different ranges depending on the value returned by the predicate p. The elements that satisfy the predicate p are copied to the range beginning at d_first_true. The rest of the elements are copied to the range beginning at d_first_false.<br />
The behavior is undefined if the input range overlaps either of the output ranges.<br />
2) Same as <code>(1)</code>, but executed according to policy. This overload only participates in overload resolution if std::is_execution_policy_v&lt;std::decay_t&lt;ExecutionPolicy&gt;&gt; is true </p>
<h2>Parameters</h2>
<p>first, last &#8211; the range of elements to sort<br />
d_first_true &#8211; the beginning of the output range for the elements that satisfy p<br />
d_first_false &#8211; the beginning of the output range for the elements that do not satisfy p<br />
policy &#8211; the execution policy to use. See execution_policy for details.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unary predicate which returns true if the element should be placed in d_first_true.<br />
p &#8211; The expression p(v) must be convertible to bool for every argument v of type (possibly const) VT, where VT is the value type of InputIt, regardless of value_category, and must not modify v. Thus, a parameter type of VT&amp;is not allowed<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;, nor is VT unless for VT a move is equivalent to a copy<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++11)</i>.</p>
<h2>Type requirements</h2>
<p>&#8211;<br />
InputIt must meet the requirements of LegacyInputIterator.<br />
&#8211;<br />
The type of dereferenced InputIt must meet the requirements of CopyAssignable.<br />
&#8211;<br />
OutputIt1, OutputIt2 must meet the requirements of LegacyOutputIterator.<br />
&#8211;<br />
ForwardIt1, ForwardIt2, ForwardIt3 must meet the requirements of LegacyForwardIterator. ForwardIt1&#8217;s value type must be CopyAssignable, writable to ForwardIt2 and ForwardIt3, and convertible to UnaryPredicate&#8217;s argument type<br />
&#8211;<br />
UnaryPredicate must meet the requirements of Predicate.</p>
<h2>Return value</h2>
<p>A std::pair constructed from the iterator to the end of the d_first_true range and the iterator to the end of the d_first_false range. </p>
<h2>Complexity</h2>
<p>Exactly distance(first, last) applications of p.<br />
For the overload with an ExecutionPolicy, there may be a performance cost if ForwardIt&#8217;s value type is not CopyConstructible.</p>
<h2>Exceptions</h2>
<p>The overload with a template parameter named ExecutionPolicy reports errors as follows: </p>
<p>* If execution of a function invoked as part of the algorithm throws an exception and ExecutionPolicy is one of the standard_policies, std::terminate is called. For any other ExecutionPolicy, the behavior is implementation-defined.<br />
* If the algorithm fails to allocate memory, std::bad_alloc is thrown.</p>
<h2>Possible implementation</h2>
<p>&nbsp;<wbr>&nbsp;template&lt;class InputIt, class OutputIt1,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;class OutputIt2, class UnaryPredicate&gt;<br />
&nbsp;<wbr>&nbsp;std::pair&lt;OutputIt1, OutputIt2&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;partition_copy(InputIt first, InputIt last,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;OutputIt1 d_first_true, OutputIt2 d_first_false,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;UnaryPredicate p)<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while (first != last) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (p(*first)) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*d_first_true = *first;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;++d_first_true;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} else {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*d_first_false = *first;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;++d_first_false;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;++first;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::pair&lt;OutputIt1, OutputIt2&gt;(d_first_true, d_first_false);<br />
&nbsp;<wbr>&nbsp;}</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;algorithm&gt;

#include &lt;utility&gt;
int main()

{
    int arr[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int true_arr[5] = {0};
    int false_arr[5] = {0};
    std::partition_copy(std::begin(arr), std::end(arr), std::begin(true_arr), std::begin(false_arr),
                        [](int i) { return i &gt; 5; });
    std::cout &lt;&lt; &quot;true_arr: &quot;;
    for (int x : true_arr) {
        std::cout &lt;&lt; x &lt;&lt; ' ';
    }
    std::cout &lt;&lt; '
';
    std::cout &lt;&lt; &quot;false_arr: &quot;;
    for (int x : false_arr) {
        std::cout &lt;&lt; x &lt;&lt; ' ';
    }
    std::cout &lt;&lt; '
';
    return 0;
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;true_arr: 6 7 8 9 10<br />
&nbsp;<wbr>&nbsp;false_arr: 1 2 3 4 5</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;divides a range of elements into two groups<br />
partition <i>(function template)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;divides elements into two groups while preserving their relative order<br />
stable_partition <i>(function template)</i><br />
copy<br />
copy_if copies a range of elements to a new location<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++11)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copies a range of elements omitting those that satisfy specific criteria<br />
remove_copy <i>(function template)</i><br />
remove_copy_if </p>
