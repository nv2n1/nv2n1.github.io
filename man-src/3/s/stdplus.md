---
title: "stdplus(3)"
name: "stdplus"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdplus/"
---

std::plus&lt;void&gt; - std::plus&lt;void&gt;

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;functional&gt;

    template &lt;&gt;
    (since C++ 14)

        class plus&lt;void&gt;;</code></pre> 
std::plus&lt;&gt; is a specialization of std::plus with parameter and return type deduced. 

<h2>Member types</h2>

Member type Definition 
is_transparent /* unspecified */

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the sum of two arguments 
operator() <i>(public member function)</i> 

 

 
&nbsp;std::plus&lt;&gt;::operator() 

 

 
template&lt; class T, class U&gt; 
constexpr auto operator()( T&amp;&amp; lhs, U&amp;&amp; rhs ) const 
-&gt; decltype(std::forward&lt;T&gt;(lhs) + std::forward&lt;U&gt;(rhs)); 

 
Returns the sum of lhs and rhs.

<h2>Parameters</h2>

lhs, rhs - values to sum

<h2>Return value</h2>

The result of lhs + rhs. 

<h2>Notes</h2>

The member type is_transparent indicates to the caller that this function object is a transparent function object: it accepts arguments of arbitrary types and uses perfect forwarding, which avoids unnecessary copying and conversion when the function object is used in heterogeneous context, or with rvalue arguments. In particular, template functions such as std::set::find and std::set::lower_bound make use of this member type on their Compare types. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;functional&gt;

#include &lt;iostream&gt;
int main()

{
    std::string a = &quot;Hello &quot;;
    const char *b = &quot;world&quot;;
    std::cout &lt;&lt; std::plus&lt;&gt;{}(a, b) &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Hello world
