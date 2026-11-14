---
title: "stdreplace_copystdreplace_copy_if(3)"
name: "stdreplace_copystdreplace_copy_if"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdreplace_copystdreplace_copy_if/"
---

std::replace_copy,std::replace_copy_if - std::replace_copy,std::replace_copy_if

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;algorithm&gt;

    template &lt;class InputIt, class OutputIt, class T&gt;

    OutputIt replace_copy(InputIt first, InputIt last, OutputIt d_first, (until C++ 20)

                                                                             const T &amp;old_value,
                          const T &amp;new_value);

template &lt;class InputIt, class OutputIt, class T&gt;

constexpr OutputIt replace_copy(InputIt first, InputIt last, OutputIt d_first, (since C++ 20)

                                                                                   const T &amp;old_value,
                                const T &amp;new_value);

template &lt;class ExecutionPolicy, class ForwardIt1, class ForwardIt2, class T&gt;

ForwardIt2 replace_copy(ExecutionPolicy &amp;&amp;policy, ForwardIt1 first, ForwardIt1 last, (2)(since C++ 17)

                                                                                         ForwardIt2 d_first,
                        const T &amp;old_value, const T &amp;new_value);
(1)

    template &lt;class InputIt, class OutputIt, class UnaryPredicate, class T&gt;

    OutputIt replace_copy_if(InputIt first, InputIt last, OutputIt d_first, (until C++ 20)

                                                                                UnaryPredicate p,
                             const T &amp;new_value);

template &lt;class InputIt, class OutputIt, class UnaryPredicate, class T&gt;

constexpr OutputIt replace_copy_if(InputIt first, InputIt last, OutputIt d_first, (3)(since C++ 20)

                                                                                      UnaryPredicate p,
                                   const T &amp;new_value);

template &lt;class ExecutionPolicy, class ForwardIt1, class ForwardIt2, class UnaryPredicate, class T&gt;

ForwardIt2 replace_copy_if(ExecutionPolicy &amp;&amp;policy, ForwardIt1 first, ForwardIt1 last, (4)(since C++ 17)

                                                                                            ForwardIt2 d_first,
                           UnaryPredicate p, const T &amp;new_value);</code></pre> 
Copies the elements from the range [first, last) to another range beginning at d_first replacing all elements satisfying specific criteria with new_value. The source and destination ranges cannot overlap. 
1) Replaces all elements that are equal to old_value. 
3) Replaces all elements for which predicate p returns true. 
2,4) Same as (1,3), but executed according to policy. This overload only participates in overload resolution if std::is_execution_policy_v&lt;std::decay_t&lt;ExecutionPolicy&gt;&gt; is true 

<h2>Parameters</h2>

first, last - the range of elements to copy 
d_first - the beginning of the destination range 
old_value - the value of elements to replace 
policy - the execution policy to use. See execution_policy for details. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unary predicate which returns true if the element value should be replaced. 
p - The expression p(v) must be convertible to bool for every argument v of type (possibly const) VT, where VT is the value type of InputIt, regardless of value_category, and must not modify v. Thus, a parameter type of VT&amp;is not allowed 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;, nor is VT unless for VT a move is equivalent to a copy 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++11)</i>. 
new_value - the value to use as replacement

<h2>Type requirements</h2>

- 
InputIt must meet the requirements of LegacyInputIterator. 
- 
OutputIt must meet the requirements of LegacyOutputIterator. 
- 
ForwardIt1, ForwardIt2 must meet the requirements of LegacyForwardIterator.

<h2>Return value</h2>

Iterator to the element past the last element copied. 

<h2>Complexity</h2>

Exactly last - first applications of the predicate.

<h2>Exceptions</h2>

The overloads with a template parameter named ExecutionPolicy report errors as follows: 

 
* If execution of a function invoked as part of the algorithm throws an exception and ExecutionPolicy is one of the standard_policies, std::terminate is called. For any other ExecutionPolicy, the behavior is implementation-defined. 
* If the algorithm fails to allocate memory, std::bad_alloc is thrown.

<h2>Possible implementation</h2>

<h2>First version</h2>

&nbsp;<wbr>&nbsp;template&lt;class InputIt, class OutputIt, class T&gt; 
&nbsp;<wbr>&nbsp;OutputIt replace_copy(InputIt first, InputIt last, OutputIt d_first, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;const T&amp; old_value, const T&amp; new_value) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (; first != last; ++first) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*d_first++ = (*first == old_value) ? new_value : *first; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return d_first; 
&nbsp;<wbr>&nbsp;}

<h2>Second version</h2>

&nbsp;<wbr>&nbsp;template&lt;class InputIt, class OutputIt, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;class UnaryPredicate, class T&gt; 
&nbsp;<wbr>&nbsp;OutputIt replace_copy_if(InputIt first, InputIt last, OutputIt d_first, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;UnaryPredicate p, const T&amp; new_value) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (; first != last; ++first) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*d_first++ = p( *first ) ? new_value : *first; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return d_first; 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

The following copy prints a vector, replacing all values over 5 with 99 on the fly. 
 // Run this code <pre><code>#include &lt;algorithm&gt;

#include &lt;vector&gt;

#include &lt;iostream&gt;

#include &lt;iterator&gt;

#include &lt;functional&gt;
int main()

{
    std::vector&lt;int&gt; v{5, 7, 4, 2, 8, 6, 1, 9, 0, 3};
    std::replace_copy_if(
        v.begin(), v.end(),
        std::ostream_iterator&lt;int&gt;(std::cout, &quot; &quot;),
        [](int n) { return n &gt; 5; }, 99);
    std::cout &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;5 99 4 2 99 99 1 99 0 3

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;removes elements satisfying specific criteria 
remove <i>(function template)</i> 
remove_if 
