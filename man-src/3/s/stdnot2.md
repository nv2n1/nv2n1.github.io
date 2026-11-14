---
title: "stdnot2(3)"
name: "stdnot2"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnot2/"
---

std::not2 - std::not2

<h2>Synopsis</h2>

Defined in header &lt;functional&gt; 
template&lt; class Predicate &gt; <i>(until C++14)</i> 
std::binary_negate&lt;Predicate&gt; not2(const Predicate&amp; pred); 
template&lt; class Predicate &gt; <i>(since C++14)</i> 
constexpr std::binary_negate&lt;Predicate&gt; not2(const Predicate&amp; pred); (deprecated in C++17) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(removed in C++20) 
not2 is a helper function to create a function object that returns the complement of the binary predicate function passed. The function object created is of type std::binary_negate&lt;Predicate&gt;. 
The binary predicate type must define two member types, first_argument_type and second_argument_type, that are convertible to the predicate's parameter types. The function objects obtained from std::owner_less, std::ref, std::cref, std::plus, std::minus, std::multiplies, std::divides, std::modulus, std::equal_to, std::not_equal_to, std::greater, std::less, std::greater_equal, std::less_equal, std::logical_not, std::logical_or, std::bit_and, std::bit_or, std::bit_xor, std::mem_fn, std::map::value_comp, std::multimap::value_comp, std::function, or from another call to std::not2 have these types defined, as are function objects derived from the deprecated std::binary_function. 

<h2>Parameters</h2>

pred - binary predicate

<h2>Return value</h2>

std::not2 returns an object of type std::binary_negate&lt;Predicate&gt;, constructed with pred. 

<h2>Exceptions</h2>

None.

<h2>Example</h2>

// Run this code <pre><code>#include &lt;algorithm&gt;

#include &lt;functional&gt;

#include &lt;iostream&gt;

#include &lt;vector&gt;
struct old_same : std::binary_function&lt;int, int, bool&gt;

{
    bool operator()(int a, int b) const
    {
        return a == b;
    }
};
struct new_same

{
    bool operator()(int a, int b) const
    {
        return a == b;
    }
};
bool same_fn(int a, int b)

{
    return a == b;
}

int main()

{
    std::vector&lt;int&gt; v1{0, 1, 2};
    std::vector&lt;int&gt; v2{2, 1, 0};
    std::vector&lt;bool&gt; v3(v1.size());
    std::cout &lt;&lt; &quot;negating a binary_function:\n&quot;;
    std::transform(v1.begin(), v1.end(), v2.begin(), v3.begin(),
                   std::not2(old_same()));
    std::cout &lt;&lt; std::boolalpha;
    for (std::size_t i = 0; i &lt; v1.size(); ++i)
        std::cout &lt;&lt; v1[i] &lt;&lt; ' ' &lt;&lt; v2[i] &lt;&lt; ' ' &lt;&lt; v3[i] &lt;&lt; '\n';
    std::cout &lt;&lt; &quot;negating a standard functor:\n&quot;;
    std::transform(v1.begin(), v1.end(), v2.begin(), v3.begin(),
                   std::not2(std::equal_to&lt;int&gt;()));
    for (std::size_t i = 0; i &lt; v1.size(); ++i)
        std::cout &lt;&lt; v1[i] &lt;&lt; ' ' &lt;&lt; v2[i] &lt;&lt; ' ' &lt;&lt; v3[i] &lt;&lt; '\n';
    std::cout &lt;&lt; &quot;negating a std::function:\n&quot;;
    std::transform(v1.begin(), v1.end(), v2.begin(), v3.begin(),
                   std::not2(std::function&lt;bool(int, int)&gt;(new_same())));
    for (std::size_t i = 0; i &lt; v1.size(); ++i)
        std::cout &lt;&lt; v1[i] &lt;&lt; ' ' &lt;&lt; v2[i] &lt;&lt; ' ' &lt;&lt; v3[i] &lt;&lt; '\n';
    std::cout &lt;&lt; &quot;negating a std::reference_wrapper:\n&quot;;
    std::transform(v1.begin(), v1.end(), v2.begin(), v3.begin(),
                   std::not2(std::ref(same_fn)));
    for (std::size_t i = 0; i &lt; v1.size(); ++i)
        std::cout &lt;&lt; v1[i] &lt;&lt; ' ' &lt;&lt; v2[i] &lt;&lt; ' ' &lt;&lt; v3[i] &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;negating a binary_function: 
&nbsp;<wbr>&nbsp;0 2 true 
&nbsp;<wbr>&nbsp;1 1 false 
&nbsp;<wbr>&nbsp;2 0 true 
&nbsp;<wbr>&nbsp;negating a standard functor: 
&nbsp;<wbr>&nbsp;0 2 true 
&nbsp;<wbr>&nbsp;1 1 false 
&nbsp;<wbr>&nbsp;2 0 true 
&nbsp;<wbr>&nbsp;negating a std::function: 
&nbsp;<wbr>&nbsp;0 2 true 
&nbsp;<wbr>&nbsp;1 1 false 
&nbsp;<wbr>&nbsp;2 0 true 
&nbsp;<wbr>&nbsp;negating a std::reference_wrapper: 
&nbsp;<wbr>&nbsp;0 2 true 
&nbsp;<wbr>&nbsp;1 1 false 
&nbsp;<wbr>&nbsp;2 0 true

<h2>See also</h2>

not_fn Creates a function object that returns the complement of the result of the function object it holds 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++17)</i> 
binary_negate wrapper function object returning the complement of the binary predicate it holds 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
(deprecated in C++17) 
(removed in C++20) 
function wraps callable object of any type with specified function call signature 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
not1 constructs custom std::unary_negate object 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
(deprecated in C++17) 
(removed in C++20) 
ptr_fun creates an adaptor-compatible function object wrapper from a pointer to function 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
(deprecated in C++11) 
(removed in C++17) 
binary_function adaptor-compatible binary function base class 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
(deprecated in C++11) 
(removed in C++17) 
