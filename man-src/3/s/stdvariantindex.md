---
title: "stdvariantindex(3)"
name: "stdvariantindex"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdvariantindex/"
---

std::variant&lt;Types...&gt;::index - std::variant&lt;Types...&gt;::index

<h2>Synopsis</h2>

constexpr std::size_t index() const noexcept; <i>(since C++17)</i> 
Returns the zero-based index of the alternative that is currently held by the variant. 
If the variant is valueless_by_exception, returns variant_npos. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;variant&gt;

#include &lt;string&gt;

#include &lt;iostream&gt;

int main()

{
    std::variant&lt;int, std::string&gt; v = &quot;abc&quot;;
    std::cout &lt;&lt; &quot;v.index = &quot; &lt;&lt; v.index() &lt;&lt; '\n';
    v = {};
    std::cout &lt;&lt; &quot;v.index = &quot; &lt;&lt; v.index() &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;v.index = 1 
&nbsp;<wbr>&nbsp;v.index = 0

<h2>See also</h2>

holds_alternative checks if a variant currently holds a given type 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++17)</i> 
std::get(std::variant) reads the value of the variant given the index or the type (if the type is unique), throws on error 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++17)</i> 
