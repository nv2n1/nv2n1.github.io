---
title: "stdbinary_function(3)"
name: "stdbinary_function"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbinary_function/"
---

std::binary_function - std::binary_function

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;functional&gt;

    template &lt;

        class Arg1, (deprecated in C++ 11)

                        class Arg2,
        (removed in C++ 17)

            class Result

        &gt;
    struct binary_function;</code></pre> 
binary_function is a base class for creating function objects with two arguments. 
binary_function does not define operator(); it is expected that derived classes will define this. binary_function provides only three types - first_argument_type, second_argument_type and result_type - defined by the template parameters. 
Some standard library function object adaptors, such as std::not2, require the function objects they adapt to have certain types defined; std::not2 requires the function object being adapted to have two types named first_argument_type and second_argument_type. Deriving function objects that take two arguments from binary_function is an easy way to make them compatible with those adaptors. 
binary_function is deprecated in C++11 and removed in C++17. 

<h2>Member types</h2>

Type Definition 
first_argument_type Arg1 
second_argument_type Arg2 
result_type Result

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
    std::vector&lt;int&gt; v1{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    std::vector&lt;int&gt; v2{10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0};
    std::vector&lt;bool&gt; v3(v1.size());
    std::transform(v1.begin(), v1.end(), v2.begin(), v3.begin(), std::not2(same()));
    std::cout &lt;&lt; std::boolalpha;
    for (std::size_t i = 0; i &lt; v1.size(); ++i)
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
&nbsp;<wbr>&nbsp;10 0 true

<h2>See also</h2>

function wraps callable object of any type with specified function call signature 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
ptr_fun creates an adaptor-compatible function object wrapper from a pointer to function 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
(deprecated in C++11) 
(removed in C++17) 
pointer_to_binary_function adaptor-compatible wrapper for a pointer to binary function 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
(deprecated in C++11) 
(removed in C++17) 
unary_function adaptor-compatible unary function base class 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
(deprecated in C++11) 
(removed in C++17) 
