---
title: "stdget_if(3)"
name: "stdget_if"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdget_if/"
description: "std::get_if – std::get_if"
---

<p>std::get_if &#8211; std::get_if</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;variant&gt;

    template &lt;std::size_t I, class... Types&gt;

    constexpr std::add_pointer_t&lt;

        std::variant_alternative_t&lt;I, std::variant&lt;Types...&gt;&gt;

        &gt;
    get_if(std::variant&lt;Types...&gt; *pv) noexcept;

template &lt;std::size_t I, class... Types&gt;

constexpr std::add_pointer_t&lt;(1)(since C++ 17)

                                 const std::variant_alternative_t&lt;I, variant&lt;Types...&gt;&gt;

                             &gt;
get_if(const std::variant&lt;Types...&gt; *pv) noexcept;

template &lt;class T, class... Types&gt;

constexpr std::add_pointer_t&lt;T&gt; get_if(std::variant&lt;Types...&gt; *pv) noexcept;
(2)(since C++ 17)

    template &lt;class T, class... Types&gt;

    constexpr std::add_pointer_t&lt;const T&gt; get_if(const std::variant&lt;Types...&gt; *pv) noexcept;</code></pre>
<p>1) Index-based non-throwing accessor: If pv is not a null pointer and pv-&gt;index() == I, returns a pointer to the value stored in the variant pointed to by pv. Otherwise, returns a null pointer value. The call is ill-formed if I is not a valid index in the variant.<br />
2) Type-based non-throwing accessor: Equivalent to <code>(1)</code> with I being the zero-based index of T in Types&#8230;. The call is ill-formed if T is not a unique element of Types&#8230;. </p>
<h2>Parameters</h2>
<p>I &#8211; index to look up<br />
Type &#8211; unique type to look up<br />
pv &#8211; pointer to a variant</p>
<h2>Return value</h2>
<p>Pointer to the value stored in the pointed-to variant or null pointer on error. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;variant&gt;

#include &lt;iostream&gt;
int main()

{
    std::variant&lt;int, float&gt; v{12};
    if (auto pval = std::get_if&lt;int&gt;(&amp;v))
        std::cout &lt;&lt; &quot;variant value: &quot; &lt;&lt; *pval &lt;&lt; '
';
    else
        std::cout &lt;&lt; &quot;failed to get value!&quot; &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;variant value: 12</p>
<h2>See also</h2>
<p>std::get(std::variant) reads the value of the variant given the index or the type (if the type is unique), throws on error<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++17)</i> </p>
