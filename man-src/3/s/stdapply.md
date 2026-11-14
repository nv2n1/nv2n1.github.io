---
title: "stdapply(3)"
name: "stdapply"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdapply/"
---

std::apply - std::apply

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;tuple&gt;

template &lt;class F, class Tuple&gt;                    (since C++17)

constexpr decltype(auto) apply(F&amp;&amp; f, Tuple&amp;&amp; t);</code></pre> 
Invoke the Callable object f with a tuple of arguments. 

<h2>Parameters</h2>

f - Callable object to be invoked 
t - tuple whose elements to be used as arguments to f

<h2>Return value</h2>

The value returned by f. 

<h2>Notes</h2>

The tuple need not be std::tuple, and instead may be anything that supports std::get and std::tuple_size; in particular, std::array and std::pair may be used. 

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;namespace detail { 
&nbsp;<wbr>&nbsp;template &lt;class F, class Tuple, std::size_t... I&gt; 
&nbsp;<wbr>&nbsp;constexpr decltype(auto) apply_impl(F&amp;&amp; f, Tuple&amp;&amp; t, std::index_sequence&lt;I...&gt;) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::invoke(std::forward&lt;F&gt;(f), std::get&lt;I&gt;(std::forward&lt;Tuple&gt;(t))...); 
&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;} // namespace detail 

 
&nbsp;<wbr>&nbsp;template &lt;class F, class Tuple&gt; 
&nbsp;<wbr>&nbsp;constexpr decltype(auto) apply(F&amp;&amp; f, Tuple&amp;&amp; t) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return detail::apply_impl( 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::forward&lt;F&gt;(f), std::forward&lt;Tuple&gt;(t), 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::make_index_sequence&lt;std::tuple_size_v&lt;std::remove_reference_t&lt;Tuple&gt;&gt;&gt;{}); 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;tuple&gt;

#include &lt;utility&gt;
int add(int first, int second)
{
    return first + second;
}
template &lt;typename T&gt;

T add_generic(T first, T second)
{
    return first + second;
}
auto add_lambda = [](auto first, auto second) { return first + second; };
int main()

{
    // OK
    std::cout &lt;&lt; std::apply(add, std::make_pair(1, 2)) &lt;&lt; '\n';
    // Error: can't deduce the function type
    // std::cout &lt;&lt; std::apply(add_generic, std::make_pair(2.0f, 3.0f)) &lt;&lt; '\n';
    // OK
    std::cout &lt;&lt; std::apply(add_lambda, std::make_pair(2.0f, 3.0f)) &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;3 
&nbsp;<wbr>&nbsp;5

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a tuple object of the type defined by the argument types 
make_tuple <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a tuple of rvalue references 
forward_as_tuple <i>(function template)</i> 
make_from_tuple Construct an object with a tuple of arguments 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++17)</i> 
invoke invokes any Callable object with given arguments 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++17)</i> 
