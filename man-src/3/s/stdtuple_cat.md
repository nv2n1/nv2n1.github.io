---
title: "stdtuple_cat(3)"
name: "stdtuple_cat"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdtuple_cat/"
---

std::tuple_cat - std::tuple_cat

<h2>Synopsis</h2>

Defined in header &lt;tuple&gt; 
template&lt; class... Tuples &gt; <i>(since C++11)</i> 
std::tuple&lt;CTypes...&gt; tuple_cat(Tuples&amp;&amp;... args); (constexpr since C++14) 
Constructs a tuple that is a concatenation of all tuples in args. 

<h2>Parameters</h2>

args - zero or more tuples to concatenate

<h2>Return value</h2>

A std::tuple object composed of all elements of all argument tuples constructed from std::get&lt;i&gt;(std::forward&lt;Ti&gt;(arg)) for each individual element. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;tuple&gt;

#include &lt;string&gt;
// helper function to print a tuple of any size

template &lt;class Tuple, std::size_t N&gt;

struct TuplePrinter {
    static void print(const Tuple &amp;t)
    {
        TuplePrinter&lt;Tuple, N - 1&gt;::print(t);
        std::cout &lt;&lt; &quot;, &quot; &lt;&lt; std::get&lt;N - 1&gt;(t);
    }
};
template &lt;class Tuple&gt;

struct TuplePrinter&lt;Tuple, 1&gt; {
    static void print(const Tuple &amp;t)
    {
        std::cout &lt;&lt; std::get&lt;0&gt;(t);
    }
};</code></pre> 
&nbsp;<wbr>&nbsp;template&lt;class... Args&gt; 
&nbsp;<wbr>&nbsp;void print(const std::tuple&lt;Args...&gt;&amp; t) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::cout &lt;&lt; &quot;(&quot;; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;TuplePrinter&lt;decltype(t), sizeof...(Args)&gt;::print(t); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::cout &lt;&lt; &quot;)\n&quot;; 
&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;// end helper function <pre><code>int main()

{
    std::tuple&lt;int, std::string, float&gt; t1(10, &quot;Test&quot;, 3.14);
    int n = 7;
    auto t2 = std::tuple_cat(t1, std::make_pair(&quot;Foo&quot;, &quot;bar&quot;), t1, std::tie(n));
    n = 10;
    print(t2);
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;(10, Test, 3.14, Foo, bar, 10, Test, 3.14, 10)

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a tuple object of the type defined by the argument types 
make_tuple <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a tuple of lvalue references or unpacks a tuple into individual objects 
tie <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a tuple of rvalue references 
forward_as_tuple <i>(function template)</i> 
