---
title: "stdbinary_negate(3)"
name: "stdbinary_negate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbinary_negate/"
---

std::binary_negate - std::binary_negate

<h2>Synopsis</h2>

Defined in header &lt;functional&gt; 
template&lt; class Predicate &gt; 
struct binary_negate : 
public std::binary_function&lt; 
Predicate::first_argument_type, <i>(until C++11)</i> 
Predicate::second_argument_type, 
bool 
&gt;; 
template&lt; class Predicate &gt; <i>(since C++11)</i> 
struct binary_negate; (deprecated in C++17) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(removed in C++20) 
binary_negate is a wrapper function object returning the complement of the binary predicate it holds. 
The binary predicate type must define two member types, first_argument_type and second_argument_type, that are convertible to the predicate's parameter types. The function objects obtained from std::owner_less, std::ref, std::cref, std::plus, std::minus, std::multiplies, std::divides, std::modulus, std::equal_to, std::not_equal_to, std::greater, std::less, std::greater_equal, std::less_equal, std::logical_not, std::logical_or, std::bit_and, std::bit_or, std::bit_xor, std::mem_fn, std::map::value_comp, std::multimap::value_comp, std::function, or from a call to std::not2 have these types defined, as are function objects derived from the deprecated std::binary_function. 
binary_negate objects are easily constructed with helper function std::not2. 

<h2>Member types</h2>

Type Definition 
first_argument_type Predicate::first_argument_type 
second_argument_type Predicate::second_argument_type 
result_type bool

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a new binary_negate object with the supplied predicate 
constructor <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the logical complement of the result of a call to the stored predicate 
operator() <i>(public member function)</i> 

 

 
&nbsp;std::binary_negate::binary_negate 

 

 
explicit binary_negate( Predicate const&amp; pred ); <i>(until C++14)</i> 
explicit constexpr binary_negate( Predicate const&amp; pred ); <i>(since C++14)</i> 

 
Constructs a binary_negate function object with the stored predicate pred.

<h2>Parameters</h2>

pred - predicate function object 

 

 
&nbsp;std::binary_negate::operator() 

 

 
bool operator()( first_argument_type const&amp; x, <i>(until C++14)</i> 
second_argument_type const&amp; y ) const; 
constexpr bool operator()( first_argument_type const&amp; x, <i>(since C++14)</i> 
second_argument_type const&amp; y ) const; 

 
Returns the logical complement of the result of calling pred(x, y).

<h2>Parameters</h2>

x - first argument to pass through to predicate 
y - second argument to pass through to predicate

<h2>Return value</h2>

The logical complement of the result of calling pred(x, y). 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;algorithm&gt;

#include &lt;functional&gt;

#include &lt;iostream&gt;

#include &lt;vector&gt;
struct same : std::binary_function&lt;int, int, bool&gt;

{
    bool operator()(int a, int b) const
    {
        return a == b;
    }
};
int main()

{
    std::vector&lt;int&gt; v1;
    std::vector&lt;int&gt; v2;
    for (int i = 0; i &lt; 10; ++i)
        v1.push_back(i);
    for (int i = 0; i &lt; 10; ++i)
        v2.push_back(10 - i);
    std::vector&lt;bool&gt; v3(v1.size());
    std::binary_negate&lt;same&gt; not_same((same()));
    std::transform(v1.begin(), v1.end(), v2.begin(), v3.begin(), not_same);
    /* C++11 solution:
              // Use std::function&lt;bool (int, int)&gt;
              std::function&lt;bool (int, int)&gt; not_same =
                  [](int x, int y)-&gt;bool{ return !same()(x, y); };
    std::transform(v1.begin(), v1.end(), v2.begin(), v3.begin(), not_same);
          */
    std::cout.setf(std::ios_base::boolalpha);
    for (int i = 0; i &lt; 10; ++i)
        std::cout &lt;&lt; v1[i] &lt;&lt; ' ' &lt;&lt; v2[i] &lt;&lt; ' ' &lt;&lt; v3[i] &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;0 10 true 
&nbsp;<wbr>&nbsp;1 9 true 
&nbsp;<wbr>&nbsp;2 8 true 
&nbsp;<wbr>&nbsp;3 7 true 
&nbsp;<wbr>&nbsp;4 6 true 
&nbsp;<wbr>&nbsp;5 5 false 
&nbsp;<wbr>&nbsp;6 4 true 
&nbsp;<wbr>&nbsp;7 3 true 
&nbsp;<wbr>&nbsp;8 2 true 
&nbsp;<wbr>&nbsp;9 1 true

<h2>See also</h2>

binary_function adaptor-compatible binary function base class 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
(deprecated in C++11) 
(removed in C++17) 
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
unary_negate wrapper function object returning the complement of the unary predicate it holds 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
(deprecated in C++17) 
(removed in C++20) 
