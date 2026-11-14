---
title: "stdunary_negate(3)"
name: "stdunary_negate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdunary_negate/"
---

std::unary_negate - std::unary_negate

<h2>Synopsis</h2>

Defined in header &lt;functional&gt; 
template&lt; class Predicate &gt; <i>(until C++11)</i> 
struct unary_negate : public std::unary_function&lt;Predicate::argument_type, bool&gt;; 
template&lt; class Predicate &gt; <i>(since C++11)</i> 
struct unary_negate; (deprecated in C++17) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(removed in C++20) 
unary_negate is a wrapper function object returning the complement of the unary predicate it holds. 
The unary predicate type must define a member type, argument_type, that is convertible to the predicate's parameter type. The unary function objects obtained from std::ref, std::cref, std::negate, std::logical_not, std::mem_fn, std::function, std::hash, or from another call to std::not1 have this type defined, as are function objects derived from the deprecated std::unary_function. 
unary_negate objects are easily constructed with helper function std::not1. 

<h2>Member types</h2>

Type Definition 
argument_type Predicate::argument_type 
result_type bool

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a new unary_negate object with the supplied predicate 
constructor <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the logical complement of the result of a call to the stored predicate 
operator() <i>(public member function)</i> 

 

 
&nbsp;std::unary_negate::unary_negate 

 

 
explicit unary_negate( Predicate const&amp; pred ); <i>(until C++14)</i> 
explicit constexpr unary_negate( Predicate const&amp; pred ); <i>(since C++14)</i> 

 
Constructs a unary_negate function object with the stored predicate pred.

<h2>Parameters</h2>

pred - predicate function object 

 

 
&nbsp;std::unary_negate::operator() 

 

 
bool operator()( argument_type const&amp; x ) const; <i>(until C++14)</i> 
constexpr bool operator()( argument_type const&amp; x ) const; <i>(since C++14)</i> 

 
Returns the logical complement of the result of calling pred(x).

<h2>Parameters</h2>

x - argument to pass through to predicate

<h2>Return value</h2>

The logical complement of the result of calling pred(x). 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;algorithm&gt;

#include &lt;functional&gt;

#include &lt;iostream&gt;

#include &lt;vector&gt;
struct less_than_7 : std::unary_function&lt;int, bool&gt;

{
    bool operator()(int i) const
    {
        return i &lt; 7;
    }
};
int main()

{
    std::vector&lt;int&gt; v;
    for (int i = 0; i &lt; 10; ++i)
        v.push_back(i);
    std::unary_negate&lt;less_than_7&gt; not_less_than_7((less_than_7()));
    std::cout &lt;&lt; std::count_if(v.begin(), v.end(), not_less_than_7);
    /* C++11 solution:
              // Use std::function&lt;bool (int)&gt;
              std::function&lt;bool (int)&gt; not_less_than_7 =
                  [](int x)-&gt;bool{ return !less_than_7()(x); };
    std::cout &lt;&lt; std::count_if(v.begin(), v.end(), not_less_than_7);
          */
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;3

<h2>See also</h2>

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
unary_function adaptor-compatible unary function base class 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
(deprecated in C++11) 
(removed in C++17) 
