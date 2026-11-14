---
title: "stdexperimentalapply(3)"
name: "stdexperimentalapply"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalapply/"
---

std::experimental::apply - std::experimental::apply

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/tuple&gt;

template &lt;class F, class Tuple&gt;                    (library fundamentals TS)

constexpr decltype(auto) apply(F&amp;&amp; f, Tuple&amp;&amp; t);</code></pre> 
Invoke the Callable object f with a tuple of arguments. 

<h2>Parameters</h2>

f - Callable object to be invoked 
t - tuple whose elements to be used as arguments to f

<h2>Return value</h2>

What returned by f. 

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;namespace detail { 
&nbsp;<wbr>&nbsp;template &lt;class F, class Tuple, std::size_t... I&gt; 
&nbsp;<wbr>&nbsp;constexpr decltype(auto) apply_impl( F&amp;&amp; f, Tuple&amp;&amp; t, std::index_sequence&lt;I...&gt; ) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::invoke(std::forward&lt;F&gt;(f), std::get&lt;I&gt;(std::forward&lt;Tuple&gt;(t))...); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;// Note: std::invoke is a C++17 feature 
&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;} // namespace detail 

 
&nbsp;<wbr>&nbsp;template &lt;class F, class Tuple&gt; 
&nbsp;<wbr>&nbsp;constexpr decltype(auto) apply(F&amp;&amp; f, Tuple&amp;&amp; t) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return detail::apply_impl(std::forward&lt;F&gt;(f), std::forward&lt;Tuple&gt;(t), 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::make_index_sequence&lt;std::tuple_size_v&lt;std::decay_t&lt;Tuple&gt;&gt;&gt;{}); 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;tuple&gt;
template &lt;typename... Ts&gt;

void print_tuple(const std::tuple&lt;Ts...&gt; &amp;tuple)

{
    std::apply([](const auto &amp;...elem) {
        ((std::cout &lt;&lt; elem &lt;&lt; '\n'), ...);
    },
               tuple);
}
int main()
{
    const std::tuple&lt;int, char&gt; t = std::make_tuple(5, 'a');
    print_tuple(t);
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;5 
&nbsp;<wbr>&nbsp;a

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a tuple object of the type defined by the argument types 
make_tuple <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a tuple of rvalue references 
forward_as_tuple <i>(function template)</i> 
