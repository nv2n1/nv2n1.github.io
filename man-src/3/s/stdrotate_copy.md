---
title: "stdrotate_copy(3)"
name: "stdrotate_copy"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrotate_copy/"
description: "std::rotate_copy – std::rotate_copy"
---

<p>std::rotate_copy &#8211; std::rotate_copy</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;algorithm&gt;

template&lt; class ForwardIt, class OutputIt &gt;

OutputIt rotate_copy( ForwardIt first, ForwardIt n_first,                                       (until C++20)

ForwardIt last, OutputIt d_first );

template&lt; class ForwardIt, class OutputIt &gt;

constexpr OutputIt rotate_copy( ForwardIt first, ForwardIt n_first,                     (1)     (since C++20)

ForwardIt last, OutputIt d_first );

template&lt; class ExecutionPolicy, class ForwardIt1, class ForwardIt2 &gt;

ForwardIt2 rotate_copy( ExecutionPolicy&amp;&amp; policy, ForwardIt1 first, ForwardIt1 n_first,     (2) (since C++17)

ForwardIt1 last, ForwardIt2 d_first );</code></pre>
<p>1) Copies the elements from the range [first, last), to another range beginning at d_first in such a way, that the element n_first becomes the first element of the new range and n_first &#8211; 1 becomes the last element.<br />
2) Same as <code>(1)</code>, but executed according to policy. This overload only participates in overload resolution if std::is_execution_policy_v&lt;std::decay_t&lt;ExecutionPolicy&gt;&gt; is true </p>
<h2>Parameters</h2>
<p>first, last &#8211; the range of elements to copy<br />
n_first &#8211; an iterator to an element in [first, last) that should appear at the beginning of the new range<br />
d_first &#8211; beginning of the destination range<br />
policy &#8211; the execution policy to use. See execution_policy for details.</p>
<h2>Type requirements</h2>
<p>&#8211;<br />
ForwardIt, ForwardIt1, ForwardIt2 must meet the requirements of LegacyForwardIterator.<br />
&#8211;<br />
OutputIt must meet the requirements of LegacyOutputIterator.</p>
<h2>Return value</h2>
<p>Output iterator to the element past the last element copied. </p>
<h2>Exceptions</h2>
<p>The overload with a template parameter named ExecutionPolicy reports errors as follows: </p>
<p>* If execution of a function invoked as part of the algorithm throws an exception and ExecutionPolicy is one of the standard_policies, std::terminate is called. For any other ExecutionPolicy, the behavior is implementation-defined.<br />
* If the algorithm fails to allocate memory, std::bad_alloc is thrown.</p>
<h2>Possible implementation</h2>
<p>See also the implementations in libstdc++ and libc++. </p>
<p>&nbsp;<wbr>&nbsp;template&lt;class ForwardIt, class OutputIt&gt;<br />
&nbsp;<wbr>&nbsp;OutputIt rotate_copy(ForwardIt first, ForwardIt n_first,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ForwardIt last, OutputIt d_first)<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;d_first = std::copy(n_first, last, d_first);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::copy(first, n_first, d_first);<br />
&nbsp;<wbr>&nbsp;}</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;algorithm&gt;

#include &lt;vector&gt;

#include &lt;iostream&gt;
int main()

{
    std::vector&lt;int&gt; src = {1, 2, 3, 4, 5};
    auto pivot = std::find(src.begin(), src.end(), 3);
    std::vector&lt;int&gt; dest(src.size());
    std::rotate_copy(src.begin(), pivot, src.end(), dest.begin());
    for (const auto &amp;i : dest) {
        std::cout &lt;&lt; i &lt;&lt; ' ';
    }
    std::cout &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;3 4 5 1 2</p>
<h2>Complexity</h2>
<p>linear in the distance between first and last</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;rotates the order of elements in a range<br />
rotate <i>(function template)</i> </p>
