---
title: "stdgetstdvariant(3)"
name: "stdgetstdvariant"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdgetstdvariant/"
---

std::get(std::variant) - std::get(std::variant)

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;variant&gt;

    template &lt;std::size_t I, class... Types&gt;

    constexpr std::variant_alternative_t&lt;

        I, std::variant&lt;Types...&gt;

        &gt; &amp;
    get(std::variant&lt;Types...&gt; &amp;v);

template &lt;std::size_t I, class... Types&gt;

constexpr std::variant_alternative_t&lt;

    I, std::variant&lt;Types...&gt;

    &gt; &amp;&amp;
get(std::variant&lt;Types...&gt; &amp;&amp;v);

template &lt;std::size_t I, class... Types&gt;

constexpr std::variant_alternative_t&lt;

    I, std::variant&lt;Types...&gt;

    &gt; const &amp;
get(const std::variant&lt;Types...&gt; &amp;v);
(1)(since C++ 17)

    template &lt;std::size_t I, class... Types&gt;

    constexpr std::variant_alternative_t&lt;

        I, std::variant&lt;Types...&gt;

        &gt; const &amp;&amp;get(const std::variant&lt;Types...&gt; &amp;&amp;v);

template &lt;class T, class... Types&gt;

constexpr T &amp;get(std::variant&lt;Types...&gt; &amp;v);

template &lt;class T, class... Types&gt;

constexpr T &amp;&amp;get(std::variant&lt;Types...&gt; &amp;&amp;v);
(2)(since C++ 17)

    template &lt;class T, class... Types&gt;

    constexpr const T &amp;get(const std::variant&lt;Types...&gt; &amp;v);

template &lt;class T, class... Types&gt;

constexpr const T &amp;&amp;get(const std::variant&lt;Types...&gt; &amp;&amp;v);</code></pre> 
1) Index-based value accessor: If v.index() == I, returns a reference to the value stored in v. Otherwise, throws std::bad_variant_access. The call is ill-formed if I is not a valid index in the variant. 
2) Type-based value accessor: If v holds the alternative T, returns a reference to the value stored in v. Otherwise, throws std::bad_variant_access. The call is ill-formed if T is not a unique element of Types.... 

<h2>Parameters</h2>

I - index to look up 
Type - unique type to look up 
v - a variant

<h2>Return value</h2>

Reference to the value stored in the variant. 

<h2>Exceptions</h2>

1,2) Throws std::bad_variant_access on errors.

<h2>Example</h2>

// Run this code <pre><code>#include &lt;variant&gt;

#include &lt;string&gt;
int main()

{
    std::variant&lt;int, float&gt; v{12}, w;
    int i = std::get&lt;int&gt;(v);
    w = std::get&lt;int&gt;(v);
    w = std::get&lt;0&gt;(v); // same effect as the previous line
    //  std::get&lt;double&gt;(v); // error: no double in [int, float]

    //  std::get&lt;3&gt;(v);      // error: valid index values are 0 and 1
    try {
        std::get&lt;float&gt;(w); // w contains int, not float: will throw
    } catch (std::bad_variant_access &amp;) {
    }
}
</code></pre>

<h2>See also</h2>

get_if obtains a pointer to the value of a pointed-to variant given the index or the type (if unique), returns null on error 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++17)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tuple accesses specified element 
std::get(std::tuple) <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;accesses an element of an array 
std::get(std::array) <i>(function template)</i> 
std::get(std::pair) accesses an element of a pair 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
