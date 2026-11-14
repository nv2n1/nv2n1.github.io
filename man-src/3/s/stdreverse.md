---
title: "stdreverse(3)"
name: "stdreverse"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdreverse/"
description: "std::reverse – std::reverse"
---

<p>std::reverse &#8211; std::reverse</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;algorithm&gt;

    template &lt;class BidirIt&gt;
    (until C++ 20)

        void reverse(BidirIt first, BidirIt last);

template &lt;class BidirIt&gt;
(1)(since C++ 20)

    constexpr void reverse(BidirIt first, BidirIt last);

template &lt;class ExecutionPolicy, class BidirIt&gt;
(2)(since C++ 17)

    void reverse(ExecutionPolicy &amp;&amp;policy, BidirIt first, BidirIt last);</code></pre>
<p>1) Reverses the order of the elements in the range [first, last)<br />
Behaves as if applying std::iter_swap to every pair of iterators first+i, (last-i) &#8211; 1 for each non-negative i &lt; (last-first)/2<br />
2) Same as <code>(1)</code>, but executed according to policy. This overload does not participate in overload resolution unless std::is_execution_policy_v&lt;std::decay_t&lt;ExecutionPolicy&gt;&gt; is true </p>
<h2>Parameters</h2>
<p>first, last &#8211; the range of elements to reverse<br />
policy &#8211; the execution policy to use. See execution_policy for details.</p>
<h2>Type requirements</h2>
<p>&#8211;<br />
BidirIt must meet the requirements of ValueSwappable and LegacyBidirectionalIterator.</p>
<h2>Return value</h2>
<p><i>(none)</i> </p>
<h2>Exceptions</h2>
<p>The overload with a template parameter named ExecutionPolicy reports errors as follows: </p>
<p>* If execution of a function invoked as part of the algorithm throws an exception and ExecutionPolicy is one of the standard_policies, std::terminate is called. For any other ExecutionPolicy, the behavior is implementation-defined.<br />
* If the algorithm fails to allocate memory, std::bad_alloc is thrown.</p>
<h2>Possible implementation</h2>
<p>See also the implementations in libstdc++ and libc++. </p>
<p>&nbsp;<wbr>&nbsp;template&lt;class BidirIt&gt;<br />
&nbsp;<wbr>&nbsp;void reverse(BidirIt first, BidirIt last)<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while ((first != last) &amp;&amp; (first != &#8211;last)) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::iter_swap(first++, last);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;}</p>
<h2>Complexity</h2>
<p>Exactly (last &#8211; first)/2 swaps.</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;vector&gt;

#include &lt;iostream&gt;

#include &lt;iterator&gt;

#include &lt;algorithm&gt;
int main()

{
    std::vector&lt;int&gt; v{1, 2, 3};
    std::reverse(std::begin(v), std::end(v));
    for (auto e : v)
        std::cout &lt;&lt; e;
    std::cout &lt;&lt; '
';
    int a[] = {4, 5, 6, 7};
    std::reverse(std::begin(a), std::end(a));
    for (auto e : a)
        std::cout &lt;&lt; e;
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;321<br />
&nbsp;<wbr>&nbsp;7654</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a copy of a range that is reversed<br />
reverse_copy <i>(function template)</i> </p>
