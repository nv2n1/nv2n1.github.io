---
title: "stdunary_function(3)"
name: "stdunary_function"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdunary_function/"
---

std::unary_function - std::unary_function

<h2>Synopsis</h2>

Defined in header &lt;functional&gt; 
template &lt;typename ArgumentType, typename ResultType&gt; (deprecated in C++11) 
struct unary_function; (removed in C++17) 
unary_function is a base class for creating function objects with one argument. 
unary_function does not define operator(); it is expected that derived classes will define this. unary_function provides only two types - argument_type and result_type - defined by the template parameters. 
Some standard library function object adaptors, such as std::not1, require the function objects they adapt to have certain types defined; std::not1 requires the function object being adapted to have a type named argument_type. Deriving function objects that take one argument from unary_function is an easy way to make them compatible with those adaptors. 
unary_function is deprecated in C++11. 

<h2>Member types</h2>

Type Definition 
argument_type ArgumentType 
result_type ResultType

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
    std::cout &lt;&lt; std::count_if(v.begin(), v.end(), std::not1(less_than_7()));
    /* C++11 solution:
              // Cast to std::function&lt;bool (int)&gt; somehow - even with a lambda
              std::cout &lt;&lt; std::count_if(v.begin(), v.end(),
                  std::not1(std::function&lt;bool (int)&gt;([](int i){ return i &lt; 7; }))
              );
          */
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;3

<h2>See also</h2>

function wraps callable object of any type with specified function call signature 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
ptr_fun creates an adaptor-compatible function object wrapper from a pointer to function 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
(deprecated in C++11) 
(removed in C++17) 
pointer_to_unary_function adaptor-compatible wrapper for a pointer to unary function 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
(deprecated in C++11) 
(removed in C++17) 
binary_function adaptor-compatible binary function base class 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
(deprecated in C++11) 
(removed in C++17) 
