---
title: "stdmake_tuple(3)"
name: "stdmake_tuple"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmake_tuple/"
---

std::make_tuple - std::make_tuple

<h2>Synopsis</h2>

Defined in header &lt;tuple&gt; 
template&lt; class... Types &gt; <i>(since C++11)</i> 
tuple&lt;VTypes...&gt; make_tuple( Types&amp;&amp;... args ); (constexpr since C++14) 
Creates a tuple object, deducing the target type from the types of arguments. 
For each Ti in Types..., the corresponding type Vi in VTypes... is std::decay&lt;Ti&gt;::type unless application of std::decay results in std::reference_wrapper&lt;X&gt; for some type X, in which case the deduced type is X&amp;. 

<h2>Parameters</h2>

args - zero or more arguments to construct the tuple from

<h2>Return value</h2>

A std::tuple object containing the given values, created as if by std::tuple&lt;VTypes...&gt;(std::forward&lt;Types&gt;(t)...). 

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;template &lt;class T&gt; 
&nbsp;<wbr>&nbsp;struct unwrap_refwrapper 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;using type = T; 
&nbsp;<wbr>&nbsp;}; 

 
&nbsp;<wbr>&nbsp;template &lt;class T&gt; 
&nbsp;<wbr>&nbsp;struct unwrap_refwrapper&lt;std::reference_wrapper&lt;T&gt;&gt; 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;using type = T&amp;; 
&nbsp;<wbr>&nbsp;}; 

 
&nbsp;<wbr>&nbsp;template &lt;class T&gt; 
&nbsp;<wbr>&nbsp;using special_decay_t = typename unwrap_refwrapper&lt;typename std::decay&lt;T&gt;::type&gt;::type; 

 
&nbsp;<wbr>&nbsp;template &lt;class... Types&gt; 
&nbsp;<wbr>&nbsp;auto make_tuple(Types&amp;&amp;... args) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::tuple&lt;special_decay_t&lt;Types&gt;...&gt;(std::forward&lt;Types&gt;(args)...); 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;tuple&gt;

#include &lt;functional&gt;
std::tuple&lt;int, int&gt; f() // this function returns multiple values

{
    int x = 5;
    return std::make_tuple(x, 7); // return {x,7}; in C++17
}
int main()

{
    // heterogeneous tuple construction
    int n = 1;
    auto t = std::make_tuple(10, &quot;Test&quot;, 3.14, std::ref(n), n);
    n = 7;
    std::cout &lt;&lt; &quot;The value of t is &quot;
              &lt;&lt; &quot;(&quot;
              &lt;&lt; std::get&lt;0&gt;(t) &lt;&lt; &quot;, &quot; &lt;&lt; std::get&lt;1&gt;(t) &lt;&lt; &quot;, &quot;
              &lt;&lt; std::get&lt;2&gt;(t) &lt;&lt; &quot;, &quot; &lt;&lt; std::get&lt;3&gt;(t) &lt;&lt; &quot;, &quot;
              &lt;&lt; std::get&lt;4&gt;(t) &lt;&lt; &quot;)\n&quot;;
    // function returning multiple values
    int a, b;
    std::tie(a, b) = f();
    std::cout &lt;&lt; a &lt;&lt; &quot; &quot; &lt;&lt; b &lt;&lt; &quot;\n&quot;;
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;The value of t is (10, Test, 3.14, 7, 1) 
&nbsp;<wbr>&nbsp;5 7

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a tuple of lvalue references or unpacks a tuple into individual objects 
tie <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a tuple of rvalue references 
forward_as_tuple <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a tuple by concatenating any number of tuples 
tuple_cat <i>(function template)</i> 
apply calls a function with a tuple of arguments 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++17)</i> 
