---
title: "stdswap_ranges(3)"
name: "stdswap_ranges"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdswap_ranges/"
description: "std::swap_ranges – std::swap_ranges"
---

<p>std::swap_ranges &#8211; std::swap_ranges</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;algorithm&gt;

template&lt; class ForwardIt1, class ForwardIt2 &gt;

ForwardIt2 swap_ranges( ForwardIt1 first1, ForwardIt1 last1,                   (until C++20)

ForwardIt2 first2 );

template&lt; class ForwardIt1, class ForwardIt2 &gt;

constexpr ForwardIt2 swap_ranges( ForwardIt1 first1, ForwardIt1 last1, (1)     (since C++20)

ForwardIt2 first2 );

template&lt; class ExecutionPolicy, class ForwardIt1, class ForwardIt2 &gt;

ForwardIt2 swap_ranges( ExecutionPolicy&amp;&amp; policy,                          (2) (since C++17)

ForwardIt1 first1, ForwardIt1 last1, ForwardIt2 first2 );</code></pre>
<p>1) Exchanges elements between range [first1, last1) and another range starting at first2.<br />
2) Same as <code>(1)</code>, but executed according to policy. This overload does not participate in overload resolution unless std::is_execution_policy_v&lt;std::decay_t&lt;ExecutionPolicy&gt;&gt; is true </p>
<h2>Parameters</h2>
<p>first1, last1 &#8211; the first range of elements to swap<br />
first2 &#8211; beginning of the second range of elements to swap<br />
policy &#8211; the execution policy to use. See execution_policy for details.</p>
<h2>Type requirements</h2>
<p>&#8211;<br />
ForwardIt1, ForwardIt2 must meet the requirements of LegacyForwardIterator.<br />
&#8211;<br />
The types of dereferenced ForwardIt1 and ForwardIt2 must meet the requirements of Swappable</p>
<h2>Return value</h2>
<p>Iterator to the element past the last element exchanged in the range beginning with first2. </p>
<h2>Exceptions</h2>
<p>The overload with a template parameter named ExecutionPolicy reports errors as follows: </p>
<p>* If execution of a function invoked as part of the algorithm throws an exception and ExecutionPolicy is one of the standard_policies, std::terminate is called. For any other ExecutionPolicy, the behavior is implementation-defined.<br />
* If the algorithm fails to allocate memory, std::bad_alloc is thrown.</p>
<h2>Possible implementation</h2>
<p>&nbsp;<wbr>&nbsp;template&lt;class ForwardIt1, class ForwardIt2&gt;<br />
&nbsp;<wbr>&nbsp;constexpr ForwardIt2 swap_ranges(ForwardIt1 first1,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ForwardIt1 last1,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ForwardIt2 first2)<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while (first1 != last1) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::iter_swap(first1++, first2++);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return first2;<br />
&nbsp;<wbr>&nbsp;}</p>
<h2>Example</h2>
<p>Demonstrates swapping of subranges from different containers<br />
 // Run this code </p>
<pre><code>#include &lt;algorithm&gt;

#include &lt;list&gt;

#include &lt;vector&gt;

#include &lt;iostream&gt;

int main()

{
    std::vector&lt;int&gt; v = {1, 2, 3, 4, 5};
    std::list&lt;int&gt; l = {-1, -2, -3, -4, -5};
    std::swap_ranges(v.begin(), v.begin() + 3, l.begin());
    for (int n : v)
        std::cout &lt;&lt; n &lt;&lt; ' ';
    std::cout &lt;&lt; '
';
    for (int n : l)
        std::cout &lt;&lt; n &lt;&lt; ' ';
    std::cout &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;-1 -2 -3 4 5<br />
&nbsp;<wbr>&nbsp;1 2 3 -4 -5</p>
<h2>Complexity</h2>
<p>linear in the distance between first1 and last1</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swaps the elements pointed to by two iterators<br />
iter_swap <i>(function template)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swaps the values of two objects<br />
swap <i>(function template)</i> </p>
