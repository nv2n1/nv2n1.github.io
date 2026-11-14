---
title: "stdptr_fun(3)"
name: "stdptr_fun"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdptr_fun/"
---

std::ptr_fun - std::ptr_fun

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;functional&gt;

template&lt; class Arg, class Result &gt;                   (deprecated in C++11)

std::pointer_to_unary_function&lt;Arg,Result&gt;        (1) (removed in C++17)

ptr_fun( Result (*f)(Arg) );

template&lt; class Arg1, class Arg2, class Result &gt;      (deprecated in C++11)

std::pointer_to_binary_function&lt;Arg1,Arg2,Result&gt; (2) (removed in C++17)

ptr_fun( Result (*f)(Arg1, Arg2) );</code></pre> 
Creates a function wrapper object (either std::pointer_to_unary_function or std::pointer_to_binary_function), deducing the target type from the template arguments. 
1) Effectively calls std::pointer_to_unary_function&lt;Arg,Result&gt;(f). 
2) Effectively calls std::pointer_to_binary_function&lt;Arg1,Arg2,Result&gt;(f). 
This function and the related types are deprecated as of C++11 in favor of the more general std::function and std::ref, both of which create callable adapter-compatible function objects from plain functions. 

<h2>Parameters</h2>

f - pointer to a function to create a wrapper for

<h2>Return value</h2>

A function object wrapping f. 

<h2>Exceptions</h2>

<i>(none)</i>

<h2>Example</h2>

// Run this code <pre><code>#include &lt;string&gt;

#include &lt;iostream&gt;

#include &lt;algorithm&gt;

#include &lt;functional&gt;
bool isvowel(char c)

{
    return std::string(&quot;aeoiuAEIOU&quot;).find(c) != std::string::npos;
}
int main()

{
    std::string s = &quot;Hello, world!&quot;;
    std::copy_if(s.begin(), s.end(), std::ostreambuf_iterator&lt;char&gt;(std::cout),
                 std::not1(std::ptr_fun(isvowel)));

    // C++11 alternatives:

    //               std::not1(std::cref(isvowel)));

    //               std::not1(std::function&lt;bool(char)&gt;(isvowel)));
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Hll, wrld!
