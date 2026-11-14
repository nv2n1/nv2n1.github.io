---
title: "stdfor_each_n(3)"
name: "stdfor_each_n"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfor_each_n/"
---

std::for_each_n - std::for_each_n

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;algorithm&gt;

template&lt; class InputIt, class Size, class UnaryFunction &gt;                                           (since C++17)

InputIt for_each_n( InputIt first, Size n, UnaryFunction f );                                        (until C++20)

template&lt; class InputIt, class Size, class UnaryFunction &gt;                                   (1)     (since C++20)

constexpr InputIt for_each_n( InputIt first, Size n, UnaryFunction f );

template&lt; class ExecutionPolicy, class ForwardIt, class Size, class UnaryFunction2 &gt;             (2) (since C++17)

ForwardIt for_each_n( ExecutionPolicy&amp;&amp; policy, ForwardIt first, Size n, UnaryFunction2 f );</code></pre> 
1) Applies the given function object f to the result of dereferencing every iterator in the range [first, first + n), in order. 
2) Applies the given function object f to the result of dereferencing every iterator in the range [first, first + n) (not necessarily in order). The algorithm is executed according to policy. This overload does not participate in overload resolution unless std::is_execution_policy_v&lt;std::decay_t&lt;ExecutionPolicy&gt;&gt; is true. 
For both overloads, if the iterator type is mutable, f may modify the elements of the range through the dereferenced iterator. If f returns a result, the result is ignored. If n is less than zero, the behavior is undefined. 

<h2>Parameters</h2>

first - the beginning of the range to apply the function to 
n - the number of elements to apply the function to 
policy - the execution policy to use. See execution_policy for details. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;function object, to be applied to the result of dereferencing every iterator in the range [first, first + n) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The signature of the function should be equivalent to the following: 
f - void fun(const Type &amp;a); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The signature does not need to have const &amp;. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The type Type must be such that an object of type InputIt can be dereferenced and then implicitly converted to Type. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;

<h2>Type requirements</h2>

- 
InputIt must meet the requirements of LegacyInputIterator. 
- 
ForwardIt must meet the requirements of LegacyForwardIterator. 
- 
UnaryFunction must meet the requirements of MoveConstructible. Does not have to be CopyConstructible 
- 
UnaryFunction2 must meet the requirements of CopyConstructible.

<h2>Return value</h2>

first + n 

<h2>Complexity</h2>

Exactly n applications of f

<h2>Exceptions</h2>

The overload with a template parameter named ExecutionPolicy reports errors as follows: 

 
* If execution of a function invoked as part of the algorithm throws an exception and ExecutionPolicy is one of the standard_policies, std::terminate is called. For any other ExecutionPolicy, the behavior is implementation-defined. 
* If the algorithm fails to allocate memory, std::bad_alloc is thrown.

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;template&lt;class InputIt, class Size, class UnaryFunction&gt; 
&nbsp;<wbr>&nbsp;InputIt for_each_n(InputIt first, Size n, UnaryFunction f) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (Size i = 0; i &lt; n; ++first, (void) ++i) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;f(*first); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return first; 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

// Run this code <pre><code>#include &lt;algorithm&gt;

#include &lt;iostream&gt;

#include &lt;vector&gt;
int main()

{
    std::vector&lt;int&gt; ns{1, 2, 3, 4, 5};
    for (auto n : ns)
        std::cout &lt;&lt; n &lt;&lt; &quot;, &quot;;
    std::cout &lt;&lt; '\n';
    std::for_each_n(ns.begin(), 3, [](auto &amp;n) { n *= 2; });
    for (auto n : ns)
        std::cout &lt;&lt; n &lt;&lt; &quot;, &quot;;
    std::cout &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;1, 2, 3, 4, 5, 
&nbsp;<wbr>&nbsp;2, 4, 6, 4, 5,

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;applies a function to a range of elements 
transform <i>(function template)</i> 
range-for_loop executes loop over range <i>(since C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;applies a function to a range of elements 
for_each <i>(function template)</i> 
