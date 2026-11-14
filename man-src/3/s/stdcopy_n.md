---
title: "stdcopy_n(3)"
name: "stdcopy_n"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcopy_n/"
---

std::copy_n - std::copy_n

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;algorithm&gt;

    template &lt;class InputIt, class Size, class OutputIt&gt;
    (since C++ 11)

        OutputIt copy_n(InputIt first, Size count, OutputIt result);
(until C++ 20)

    template &lt;class InputIt, class Size, class OutputIt&gt;
    (1)(since C++ 20)

        constexpr OutputIt copy_n(InputIt first, Size count, OutputIt result);

template &lt;class ExecutionPolicy, class ForwardIt1, class Size, class ForwardIt2&gt;
(2)(since C++ 17)

    ForwardIt2 copy_n(ExecutionPolicy &amp;&amp;policy, ForwardIt1 first, Size count, ForwardIt2 result);
1) Copies exactly count values from the range beginning at first to the range beginning at result. Formally, for each non-negative integer i &lt; n, performs *(result + i) = *(first + i). Overlap of ranges is not permitted.

2) Same as (1), but executed according to policy. This overload only participates in overload resolution if std::is_execution_policy_v&lt;std::decay_t&lt;ExecutionPolicy&gt;&gt; is true
</code></pre>

<h2>Parameters</h2>

first - the beginning of the range of elements to copy from 
count - number of the elements to copy 
result - the beginning of the destination range 
policy - the execution policy to use. See execution_policy for details.

<h2>Type requirements</h2>

- 
InputIt must meet the requirements of LegacyInputIterator. 
- 
OutputIt must meet the requirements of LegacyOutputIterator. 
- 
ForwardIt1, ForwardIt2 must meet the requirements of LegacyForwardIterator.

<h2>Return value</h2>

Iterator in the destination range, pointing past the last element copied if count&gt;0 or result otherwise. 

<h2>Complexity</h2>

Exactly count assignments, if count&gt;0.

<h2>Exceptions</h2>

The overload with a template parameter named ExecutionPolicy reports errors as follows: 

 
* If execution of a function invoked as part of the algorithm throws an exception and ExecutionPolicy is one of the standard_policies, std::terminate is called. For any other ExecutionPolicy, the behavior is implementation-defined. 
* If the algorithm fails to allocate memory, std::bad_alloc is thrown.

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;template&lt; class InputIt, class Size, class OutputIt&gt; 
&nbsp;<wbr>&nbsp;OutputIt copy_n(InputIt first, Size count, OutputIt result) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (count &gt; 0) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*result++ = *first; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (Size i = 1; i &lt; count; ++i) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*result++ = *++first; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return result; 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;string&gt;

#include &lt;algorithm&gt;

#include &lt;iterator&gt;
int main()

{
    std::string in = &quot;1234567890&quot;;
    std::string out;
    std::copy_n(in.begin(), 4, std::back_inserter(out));
    std::cout &lt;&lt; out &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;1234

<h2>See also</h2>

copy 
copy_if copies a range of elements to a new location 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
