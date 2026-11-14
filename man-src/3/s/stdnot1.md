---
title: "stdnot1(3)"
name: "stdnot1"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnot1/"
---

std::not1 - std::not1

<h2>Synopsis</h2>

Defined in header &lt;functional&gt; 
template&lt; class Predicate &gt; <i>(until C++14)</i> 
std::unary_negate&lt;Predicate&gt; not1(const Predicate&amp; pred); 
template&lt; class Predicate &gt; <i>(since C++14)</i> 
constexpr std::unary_negate&lt;Predicate&gt; not1(const Predicate&amp; pred); (deprecated in C++17) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(removed in C++20) 
not1 is a helper function to create a function object that returns the complement of the unary predicate function passed. The function object created is of type std::unary_negate&lt;Predicate&gt;. 
The unary predicate type must define a member type, argument_type, that is convertible to the predicate's parameter type. The unary function objects obtained from std::ref, std::cref, std::negate, std::logical_not, std::mem_fn, std::function, std::hash, or from another call to std::not1 have this type defined, as are function objects derived from the deprecated std::unary_function. 

<h2>Parameters</h2>

pred - unary predicate

<h2>Return value</h2>

std::not1 returns an object of type std::unary_negate&lt;Predicate&gt;, constructed with pred. 

<h2>Exceptions</h2>

None.

<h2>Example</h2>

// Run this code <pre><code>#include &lt;algorithm&gt;

#include &lt;numeric&gt;

#include &lt;iterator&gt;

#include &lt;functional&gt;

#include &lt;iostream&gt;

#include &lt;vector&gt;
struct LessThan7 : std::unary_function&lt;int, bool&gt;

{
    bool operator()(int i) const
    {
        return i &lt; 7;
    }
};
int main()

{
    std::vector&lt;int&gt; v(10);
    std::iota(begin(v), end(v), 0);
    std::cout &lt;&lt; std::count_if(begin(v), end(v), std::not1(LessThan7())) &lt;&lt; &quot;\n&quot;;
    // same as above, but using `std::function`
    std::function&lt;bool(int)&gt; less_than_9 = [](int x) { return x &lt; 9; };
    std::cout &lt;&lt; std::count_if(begin(v), end(v), std::not1(less_than_9)) &lt;&lt; &quot;\n&quot;;
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;3 
&nbsp;<wbr>&nbsp;1

<h2>See also</h2>

not_fn Creates a function object that returns the complement of the result of the function object it holds 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++17)</i> 
unary_negate wrapper function object returning the complement of the unary predicate it holds 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
(deprecated in C++17) 
(removed in C++20) 
function wraps callable object of any type with specified function call signature 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
not2 constructs custom std::binary_negate object 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
(deprecated in C++17) 
(removed in C++20) 
ptr_fun creates an adaptor-compatible function object wrapper from a pointer to function 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
(deprecated in C++11) 
(removed in C++17) 
unary_function adaptor-compatible unary function base class 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
(deprecated in C++11) 
(removed in C++17) 
