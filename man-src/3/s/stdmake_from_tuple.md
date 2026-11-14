---
title: "stdmake_from_tuple(3)"
name: "stdmake_from_tuple"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmake_from_tuple/"
---

std::make_from_tuple - std::make_from_tuple

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;tuple&gt;

template &lt;class T, class Tuple&gt;          (since C++17)

constexpr T make_from_tuple(Tuple&amp;&amp; t);</code></pre> 
Construct an object of type T, using the elements of the tuple t as the arguments to the constructor. 

<h2>Parameters</h2>

t - tuple whose elements to be used as arguments to the constructor of T

<h2>Return value</h2>

The constructed T object. 

<h2>Notes</h2>

The tuple need not be std::tuple, and instead may be anything that supports std::get and std::tuple_size; in particular, std::array and std::pair may be used. 
Due to guaranteed_copy_elision, T need not be movable. 

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;namespace detail { 
&nbsp;<wbr>&nbsp;template &lt;class T, class Tuple, std::size_t... I&gt; 
&nbsp;<wbr>&nbsp;constexpr T make_from_tuple_impl( Tuple&amp;&amp; t, std::index_sequence&lt;I...&gt; ) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return T(std::get&lt;I&gt;(std::forward&lt;Tuple&gt;(t))...); 
&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;} // namespace detail 

 
&nbsp;<wbr>&nbsp;template &lt;class T, class Tuple&gt; 
&nbsp;<wbr>&nbsp;constexpr T make_from_tuple( Tuple&amp;&amp; t ) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return detail::make_from_tuple_impl&lt;T&gt;(std::forward&lt;Tuple&gt;(t), 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::make_index_sequence&lt;std::tuple_size_v&lt;std::remove_reference_t&lt;Tuple&gt;&gt;&gt;{}); 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;tuple&gt;
struct Foo {
    Foo(int first, float second, int third)
    {
        std::cout &lt;&lt; first &lt;&lt; &quot;, &quot; &lt;&lt; second &lt;&lt; &quot;, &quot; &lt;&lt; third &lt;&lt; &quot;\n&quot;;
    }
};
int main()

{
    auto tuple = std::make_tuple(42, 3.14f, 0);
    std::make_from_tuple&lt;Foo&gt;(std::move(tuple));
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;42, 3.14, 0

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a tuple object of the type defined by the argument types 
make_tuple <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a tuple of rvalue references 
forward_as_tuple <i>(function template)</i> 
apply calls a function with a tuple of arguments 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++17)</i> 
