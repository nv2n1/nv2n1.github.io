---
title: "stdfill_n(3)"
name: "stdfill_n"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfill_n/"
description: "std::fill_n – std::fill_n"
---

<p>std::fill_n &#8211; std::fill_n</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;algorithm&gt;

    template &lt;class OutputIt, class Size, class T&gt;
    (until C++ 11)

        void fill_n(OutputIt first, Size count, const T &amp;value);

template &lt;class OutputIt, class Size, class T&gt;
(since C++ 11)

    OutputIt fill_n(OutputIt first, Size count, const T &amp;value);
(1)(until C++ 20)

    template &lt;class OutputIt, class Size, class T&gt;
    (since C++ 20)

        constexpr OutputIt fill_n(OutputIt first, Size count, const T &amp;value);

template &lt;class ExecutionPolicy, class ForwardIt, class Size, class T&gt;
(2)(since C++ 17)

    ForwardIt fill_n(ExecutionPolicy &amp;&amp;policy, ForwardIt first, Size count, const T &amp;value);</code></pre>
<p>1) Assigns the given value to the first count elements in the range beginning at first if count &gt; 0. Does nothing otherwise.<br />
2) Same as <code>(1)</code>, but executed according to policy. This overload only participates in overload resolution if std::is_execution_policy_v&lt;std::decay_t&lt;ExecutionPolicy&gt;&gt; is true </p>
<h2>Parameters</h2>
<p>first &#8211; the beginning of the range of elements to modify<br />
count &#8211; number of elements to modify<br />
value &#8211; the value to be assigned<br />
policy &#8211; the execution policy to use. See execution_policy for details.</p>
<h2>Type requirements</h2>
<p>&#8211;<br />
OutputIt must meet the requirements of LegacyOutputIterator.<br />
&#8211;<br />
ForwardIt must meet the requirements of LegacyForwardIterator.</p>
<h2>Return value</h2>
<p><i>(none)</i> <i>(until C++11)</i><br />
Iterator one past the last element assigned if count &gt; 0, first otherwise. <i>(since C++11)</i> </p>
<h2>Complexity</h2>
<p>Exactly count assignments, for count &gt; 0.</p>
<h2>Exceptions</h2>
<p>The overload with a template parameter named ExecutionPolicy reports errors as follows: </p>
<p>* If execution of a function invoked as part of the algorithm throws an exception and ExecutionPolicy is one of the standard_policies, std::terminate is called. For any other ExecutionPolicy, the behavior is implementation-defined.<br />
* If the algorithm fails to allocate memory, std::bad_alloc is thrown.</p>
<h2>Possible implementation</h2>
<p>&nbsp;<wbr>&nbsp;template&lt;class OutputIt, class Size, class T&gt;<br />
&nbsp;<wbr>&nbsp;OutputIt fill_n(OutputIt first, Size count, const T&amp; value)<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (Size i = 0; i &lt; count; i++) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*first++ = value;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return first;<br />
&nbsp;<wbr>&nbsp;}</p>
<h2>Example</h2>
<p>The following code uses fill_n() to assign -1 to the first half of a vector of integers:<br />
 // Run this code </p>
<pre><code>#include &lt;algorithm&gt;

#include &lt;vector&gt;

#include &lt;iostream&gt;

#include &lt;iterator&gt;
int main()

{
    std::vector&lt;int&gt; v1{0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    std::fill_n(v1.begin(), 5, -1);
    std::copy(begin(v1), end(v1), std::ostream_iterator&lt;int&gt;(std::cout, &quot; &quot;));
    std::cout &lt;&lt; &quot;
&quot;;
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;-1 -1 -1 -1 -1 5 6 7 8 9</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copy-assigns the given value to every element in a range<br />
fill <i>(function template)</i> </p>
