---
title: "stdforward_as_tuple(3)"
name: "stdforward_as_tuple"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdforward_as_tuple/"
---

std::forward_as_tuple - std::forward_as_tuple

<h2>Synopsis</h2>

Defined in header &lt;tuple&gt; 
template&lt; class... Types &gt; <i>(since C++11)</i> 
tuple&lt;Types&amp;&amp;...&gt; forward_as_tuple( Types&amp;&amp;... args ) noexcept; (constexpr since C++14) 
Constructs a tuple of references to the arguments in args suitable for forwarding as an argument to a function. The tuple has rvalue reference data members when rvalues are used as arguments, and otherwise has lvalue reference data members. 

<h2>Parameters</h2>

args - zero or more arguments to construct the tuple from

<h2>Return value</h2>

A std::tuple object created as if by std::tuple&lt;Types&amp;&amp;...&gt;(std::forward&lt;Types&gt;(args)...) 

<h2>Notes</h2>

If the arguments are temporaries, forward_as_tuple does not extend their lifetime; they have to be used before the end of the full expression. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;map&gt;

#include &lt;tuple&gt;

#include &lt;string&gt;
int main()

{
    std::map&lt;int, std::string&gt; m;
    m.emplace(std::piecewise_construct,
              std::forward_as_tuple(10),
              std::forward_as_tuple(20, 'a'));
    std::cout &lt;&lt; &quot;m[10] = &quot; &lt;&lt; m[10] &lt;&lt; '\n';
    // The following is an error: it produces a
    // std::tuple&lt;int&amp;&amp;, char&amp;&amp;&gt; holding two dangling references.
    //
    // auto t = std::forward_as_tuple(20, 'a');
    // m.emplace(std::piecewise_construct, std::forward_as_tuple(10), t);
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;m[10] = aaaaaaaaaaaaaaaaaaaa

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a tuple object of the type defined by the argument types 
make_tuple <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a tuple of lvalue references or unpacks a tuple into individual objects 
tie <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a tuple by concatenating any number of tuples 
tuple_cat <i>(function template)</i> 
apply calls a function with a tuple of arguments 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++17)</i> 
