---
title: "stdfor_each(3)"
name: "stdfor_each"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfor_each/"
---

std::for_each - std::for_each

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;algorithm&gt;

    template &lt;class InputIt, class UnaryFunction&gt;
    (until C++ 20)

        UnaryFunction for_each(InputIt first, InputIt last, UnaryFunction f);

template &lt;class InputIt, class UnaryFunction&gt;
(1)(since C++ 20)

    constexpr UnaryFunction for_each(InputIt first, InputIt last, UnaryFunction f);

template &lt;class ExecutionPolicy, class ForwardIt, class UnaryFunction2&gt;
(2)(since C++ 17)

    void for_each(ExecutionPolicy &amp;&amp;policy, ForwardIt first, ForwardIt last, UnaryFunction2 f);</code></pre> 
1) Applies the given function object f to the result of dereferencing every iterator in the range [first, last), in order. 
2) Applies the given function object f to the result of dereferencing every iterator in the range [first, last) (not necessarily in order). The algorithm is executed according to policy. This overload does not participate in overload resolution unless std::is_execution_policy_v&lt;std::decay_t&lt;ExecutionPolicy&gt;&gt; is true. 
For both overloads, if the iterator type is mutable, f may modify the elements of the range through the dereferenced iterator. If f returns a result, the result is ignored. 
Unlike the rest of the algorithms, for_each is not allowed to make copies of the elements in the sequence even if they are trivially copyable. 

<h2>Parameters</h2>

first, last - the range to apply the function to 
policy - the execution policy to use. See execution_policy for details. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;function object, to be applied to the result of dereferencing every iterator in the range [first, last) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The signature of the function should be equivalent to the following: 
f - void fun(const Type &amp;a); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The signature does not need to have const &amp;. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The type Type must be such that an object of type InputIt can be dereferenced and then implicitly converted to Type. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;

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

1) 
f 
<i>(until C++11)</i> 
std::move(f) 
<i>(since C++11)</i> 
2) <i>(none)</i> 

<h2>Complexity</h2>

Exactly last - first applications of f

<h2>Exceptions</h2>

The overload with a template parameter named ExecutionPolicy reports errors as follows: 

 
* If execution of a function invoked as part of the algorithm throws an exception and ExecutionPolicy is one of the standard_policies, std::terminate is called. For any other ExecutionPolicy, the behavior is implementation-defined. 
* If the algorithm fails to allocate memory, std::bad_alloc is thrown.

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;template&lt;class InputIt, class UnaryFunction&gt; 
&nbsp;<wbr>&nbsp;constexpr UnaryFunction for_each(InputIt first, InputIt last, UnaryFunction f) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (; first != last; ++first) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;f(*first); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return f; // implicit move since C++11 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

The following example uses a lambda_function to increment all of the elements of a vector and then uses an overloaded operator() in a functor to compute their sum. Note that to compute the sum, it is recommended to use the dedicated algorithm std::accumulate. 
 // Run this code <pre><code>#include &lt;vector&gt;

#include &lt;algorithm&gt;

#include &lt;iostream&gt;
struct Sum

{
    Sum()
        : sum{0}
    {
    }
    void operator()(int n)
    {
        sum += n;
    }
    int sum;
};
int main()

{
    std::vector&lt;int&gt; nums{3, 4, 2, 8, 15, 267};
    auto print = [](const int &amp;n) { std::cout &lt;&lt; &quot; &quot; &lt;&lt; n; };
    std::cout &lt;&lt; &quot;before:&quot;;
    std::for_each(nums.begin(), nums.end(), print);
    std::cout &lt;&lt; '\n';
    std::for_each(nums.begin(), nums.end(), [](int &amp;n) { n++; });
    // calls Sum::operator() for each number
    Sum s = std::for_each(nums.begin(), nums.end(), Sum());
    std::cout &lt;&lt; &quot;after: &quot;;
    std::for_each(nums.begin(), nums.end(), print);
    std::cout &lt;&lt; '\n';
    std::cout &lt;&lt; &quot;sum: &quot; &lt;&lt; s.sum &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;before: 3 4 2 8 15 267 
&nbsp;<wbr>&nbsp;after: 4 5 3 9 16 268 
&nbsp;<wbr>&nbsp;sum: 305

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;applies a function to a range of elements 
transform <i>(function template)</i> 
range-for_loop executes loop over range <i>(since C++11)</i> 
for_each_n applies a function object to the first n elements of a sequence 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++17)</i> 
