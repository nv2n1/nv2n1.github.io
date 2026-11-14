---
title: "stdinteger_sequence(3)"
name: "stdinteger_sequence"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdinteger_sequence/"
description: "std::integer_sequence – std::integer_sequence"
---

<p>std::integer_sequence &#8211; std::integer_sequence</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;utility&gt;

template&lt; class T, T... Ints &gt;  (since C++14)

class integer_sequence;</code></pre>
<p>The class template std::integer_sequence represents a compile-time sequence of integers. When used as an argument to a function_template, the parameter_pack Ints can be deduced and used in pack expansion. </p>
<h2>Template parameters</h2>
<p>T &#8211; an integer type to use for the elements of the sequence<br />
&#8230;Ints &#8211; a non-type parameter pack representing the sequence</p>
<h2>Member types</h2>
<p>Member type Definition<br />
value_type T</p>
<h2>Member functions</h2>
<p>size returns the number of elements in Ints<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code> </p>
<p>&nbsp;std::integer_sequence::size </p>
<p>static constexpr std::size_t size() noexcept; </p>
<p>Returns the number of elements in Ints. Equivalent to sizeof&#8230;(Ints)</p>
<h2>Parameters</h2>
<p><i>(none)</i></p>
<h2>Return value</h2>
<p>The number of elements in Ints.<br />
Helper templates<br />
A helper alias template std::index_sequence is defined for the common case where T is std::size_t. template&lt;class&#8230; T&gt;</p>
<p>using index_sequence_for = std::make_index_sequence&lt;sizeof&#8230;(T)&gt;;</p>
<p>A helper alias template std::make_integer_sequence is defined to simplify creation of std::integer_sequence and std::index_sequence types with 0, 1, 2, &#8230;, N-1 as Ints: template&lt;class T, T N&gt;</p>
<p>using make_integer_sequence = std::integer_sequence&lt;T, /* a sequence 0, 1, 2, &#8230;, N-1 */ &gt;;</p>
<p>template&lt;std::size_t N&gt;</p>
<p>using make_index_sequence = make_integer_sequence&lt;std::size_t, N&gt;;<br />
The program is ill-formed if N is negative. If N is zero, the indicated type is integer_sequence&lt;T&gt;.<br />
A helper alias template std::index_sequence_for is defined to convert any type parameter pack into an index sequence of the same length template&lt;class&#8230; T&gt;</p>
<p>using index_sequence_for = std::make_index_sequence&lt;sizeof&#8230;(T)&gt;;</p>
<h2>Example</h2>
<p>Note: see Possible Implementation in std::apply for another example<br />
 // Run this code #include &lt;tuple&gt;</p>
<p>#include &lt;iostream&gt;</p>
<p>#include &lt;array&gt;</p>
<p>#include &lt;utility&gt;<br />
// Convert array into a tuple</p>
<p>template &lt;typename Array, std::size_t&#8230; I&gt;</p>
<p>auto a2t_impl(const Array &amp;a, std::index_sequence&lt;I&#8230;&gt;)</p>
<p>{<br />
    return std::make_tuple(a[I]&#8230;);<br />
}<br />
template &lt;typename T, std::size_t N, typename Indices = std::make_index_sequence&lt;N&gt;&gt;</p>
<p>auto a2t(const std::array&lt;T, N&gt; &amp;a)</p>
<p>{<br />
    return a2t_impl(a, Indices{});<br />
}<br />
&nbsp;<wbr>&nbsp;// pretty-print a tuple </p>
<pre><code>template &lt;class Ch, class Tr, class Tuple, std::size_t... Is&gt;

void print_tuple_impl(std::basic_ostream&lt;Ch, Tr&gt; &amp;os,
                      const Tuple &amp;t,
                      std::index_sequence&lt;Is...&gt;)

{
    ((os &lt;&lt; (Is == 0 ? &quot;&quot; : &quot;, &quot;) &lt;&lt; std::get&lt;Is&gt;(t)), ...);
}
template &lt;class Ch, class Tr, class... Args&gt;

auto &amp;operator&lt;&lt;(std::basic_ostream&lt;Ch, Tr&gt; &amp;os,
                 const std::tuple&lt;Args...&gt; &amp;t)

{
    os &lt;&lt; &quot;(&quot;;
    print_tuple_impl(os, t, std::index_sequence_for&lt;Args...&gt;{});
    return os &lt;&lt; &quot;)&quot;;
}
int main()

{
    std::array&lt;int, 4&gt; array = {1, 2, 3, 4};
    // convert an array into a tuple
    auto tuple = a2t(array);
    static_assert(std::is_same&lt;decltype(tuple),
                               std::tuple&lt;int, int, int, int&gt;&gt;::value,
                  &quot;&quot;);
    // print it to cout
    std::cout &lt;&lt; tuple &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;(1, 2, 3, 4)</p>
