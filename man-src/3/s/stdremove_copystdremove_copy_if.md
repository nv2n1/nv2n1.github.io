---
title: "stdremove_copystdremove_copy_if(3)"
name: "stdremove_copystdremove_copy_if"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdremove_copystdremove_copy_if/"
---

std::remove_copy,std::remove_copy_if - std::remove_copy,std::remove_copy_if

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;algorithm&gt;

    template &lt;class InputIt, class OutputIt, class T&gt;

    OutputIt remove_copy(InputIt first, InputIt last, OutputIt d_first, (until C++ 20)

                                                                            const T &amp;value);

template &lt;class InputIt, class OutputIt, class T&gt;

constexpr OutputIt remove_copy(InputIt first, InputIt last, OutputIt d_first, (since C++ 20)

                                                                                  const T &amp;value);

template &lt;class ExecutionPolicy, class ForwardIt1, class ForwardIt2, class T&gt;

ForwardIt2 remove_copy(ExecutionPolicy &amp;&amp;policy, ForwardIt1 first, ForwardIt1 last, (2)(since C++ 17)

                                                                                        ForwardIt2 d_first,
                       const T &amp;value);
(1)

    template &lt;class InputIt, class OutputIt, class UnaryPredicate&gt;

    OutputIt remove_copy_if(InputIt first, InputIt last, OutputIt d_first, (until C++ 20)

                                                                               UnaryPredicate p);

template &lt;class InputIt, class OutputIt, class UnaryPredicate&gt;

constexpr OutputIt remove_copy_if(InputIt first, InputIt last, OutputIt d_first, (3)(since C++ 20)

                                                                                     UnaryPredicate p);

template &lt;class ExecutionPolicy, class ForwardIt1, class ForwardIt2, class UnaryPredicate&gt;

ForwardIt2 remove_copy_if(ExecutionPolicy &amp;&amp;policy, ForwardIt1 first, ForwardIt1 last, (4)(since C++ 17)

                                                                                           ForwardIt2 d_first,
                          UnaryPredicate p);</code></pre> 
Copies elements from the range [first, last), to another range beginning at d_first, omitting the elements which satisfy specific criteria. Source and destination ranges cannot overlap. 
1) Ignores all elements that are equal to value. 
3) Ignores all elements for which predicate p returns true. 
2,4) Same as (1,3), but executed according to policy. This overload only participates in overload resolution if std::is_execution_policy_v&lt;std::decay_t&lt;ExecutionPolicy&gt;&gt; is true 

<h2>Parameters</h2>

first, last - the range of elements to copy 
d_first - the beginning of the destination range. 
value - the value of the elements not to copy 
policy - the execution policy to use. See execution_policy for details.

<h2>Type requirements</h2>

- 
InputIt must meet the requirements of LegacyInputIterator. 
- 
OutputIt must meet the requirements of LegacyOutputIterator. 
- 
ForwardIt1, ForwardIt2 must meet the requirements of LegacyForwardIterator. 
- 
UnaryPredicate must meet the requirements of Predicate.

<h2>Return value</h2>

Iterator to the element past the last element copied. 

<h2>Complexity</h2>

Exactly last - first applications of the predicate. 
For the overloads with an ExecutionPolicy, there may be a performance cost if ForwardIt1's value_type is not MoveConstructible.

<h2>Exceptions</h2>

The overloads with a template parameter named ExecutionPolicy report errors as follows: 

 
* If execution of a function invoked as part of the algorithm throws an exception and ExecutionPolicy is one of the standard_policies, std::terminate is called. For any other ExecutionPolicy, the behavior is implementation-defined. 
* If the algorithm fails to allocate memory, std::bad_alloc is thrown.

<h2>Possible implementation</h2>

<h2>First version</h2>

&nbsp;<wbr>&nbsp;template&lt;class InputIt, class OutputIt, class T&gt; 
&nbsp;<wbr>&nbsp;OutputIt remove_copy(InputIt first, InputIt last, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;OutputIt d_first, const T&amp; value) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (; first != last; ++first) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (!(*first == value)) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*d_first++ = *first; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return d_first; 
&nbsp;<wbr>&nbsp;}

<h2>Second version</h2>

&nbsp;<wbr>&nbsp;template&lt;class InputIt, class OutputIt, class UnaryPredicate&gt; 
&nbsp;<wbr>&nbsp;OutputIt remove_copy_if(InputIt first, InputIt last, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;OutputIt d_first, UnaryPredicate p) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (; first != last; ++first) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (!p(*first)) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*d_first++ = *first; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return d_first; 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

The following code outputs a string while erasing the spaces on the fly. 
 // Run this code <pre><code>#include &lt;algorithm&gt;

#include &lt;iterator&gt;

#include &lt;string&gt;

#include &lt;iostream&gt;

int main()

{
    std::string str = &quot;Text with some   spaces&quot;;
    std::cout &lt;&lt; &quot;before: &quot; &lt;&lt; str &lt;&lt; &quot;\n&quot;;
    std::cout &lt;&lt; &quot;after:  &quot;;
    std::remove_copy(str.begin(), str.end(),
                     std::ostream_iterator&lt;char&gt;(std::cout), ' ');
    std::cout &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;before: Text with some spaces 
&nbsp;<wbr>&nbsp;after: Textwithsomespaces

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;removes elements satisfying specific criteria 
remove <i>(function template)</i> 
remove_if 
copy 
copy_if copies a range of elements to a new location 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
partition_copy copies a range dividing the elements into two groups 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
