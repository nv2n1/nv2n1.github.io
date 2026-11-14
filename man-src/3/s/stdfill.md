---
title: "stdfill(3)"
name: "stdfill"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfill/"
description: "std::fill – std::fill"
---

<p>std::fill &#8211; std::fill</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;algorithm&gt;

    template &lt;class ForwardIt, class T&gt;
    (until C++ 20)

        void fill(ForwardIt first, ForwardIt last, const T &amp;value);

template &lt;class ForwardIt, class T&gt;
(1)(since C++ 20)

    constexpr void fill(ForwardIt first, ForwardIt last, const T &amp;value);

template &lt;class ExecutionPolicy, class ForwardIt, class T&gt;
(2)(since C++ 17)

    void fill(ExecutionPolicy &amp;&amp;policy, ForwardIt first, ForwardIt last, const T &amp;value);</code></pre>
<p>1) Assigns the given value to the elements in the range [first, last).<br />
2) Same as <code>(1)</code>, but executed according to policy. This overload does not participate in overload resolution unless std::is_execution_policy_v&lt;std::decay_t&lt;ExecutionPolicy&gt;&gt; is true </p>
<h2>Parameters</h2>
<p>first, last &#8211; the range of elements to modify<br />
value &#8211; the value to be assigned<br />
policy &#8211; the execution policy to use. See execution_policy for details.</p>
<h2>Type requirements</h2>
<p>&#8211;<br />
ForwardIt must meet the requirements of LegacyForwardIterator.</p>
<h2>Return value</h2>
<p><i>(none)</i> </p>
<h2>Complexity</h2>
<p>Exactly last &#8211; first assignments.</p>
<h2>Exceptions</h2>
<p>The overload with a template parameter named ExecutionPolicy reports errors as follows: </p>
<p>* If execution of a function invoked as part of the algorithm throws an exception and ExecutionPolicy is one of the standard_policies, std::terminate is called. For any other ExecutionPolicy, the behavior is implementation-defined.<br />
* If the algorithm fails to allocate memory, std::bad_alloc is thrown.</p>
<h2>Possible implementation</h2>
<p>&nbsp;<wbr>&nbsp;template&lt; class ForwardIt, class T &gt;<br />
&nbsp;<wbr>&nbsp;void fill(ForwardIt first, ForwardIt last, const T&amp; value)<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (; first != last; ++first) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*first = value;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;}</p>
<h2>Example</h2>
<p>The following code uses fill() to set all of the elements of a vector of integers to -1:<br />
 // Run this code </p>
<pre><code>#include &lt;algorithm&gt;

#include &lt;vector&gt;

#include &lt;iostream&gt;
int main()

{
    std::vector&lt;int&gt; v{0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    std::fill(v.begin(), v.end(), -1);
    for (auto elem : v) {
        std::cout &lt;&lt; elem &lt;&lt; &quot; &quot;;
    }
    std::cout &lt;&lt; &quot;
&quot;;
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;-1 -1 -1 -1 -1 -1 -1 -1 -1 -1</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copy-assigns the given value to N elements in a range<br />
fill_n <i>(function template)</i><br />
copy<br />
copy_if copies a range of elements to a new location<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++11)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;assigns the results of successive function calls to every element in a range<br />
generate <i>(function template)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;applies a function to a range of elements<br />
transform <i>(function template)</i> </p>
