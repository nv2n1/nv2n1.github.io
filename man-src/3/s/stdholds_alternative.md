---
title: "stdholds_alternative(3)"
name: "stdholds_alternative"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdholds_alternative/"
---

std::holds_alternative - std::holds_alternative

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;variant&gt;

    template &lt;class T, class... Types&gt;
    (since C++ 17)

        constexpr bool holds_alternative(const std::variant&lt;Types...&gt; &amp;v) noexcept;</code></pre> 
Checks if the variant v holds the alternative T. The call is ill-formed if T does not appear exactly once in Types... 

<h2>Parameters</h2>

v - variant to examine

<h2>Return value</h2>

true if the variant currently holds the alternative T, false otherwise. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;variant&gt;

#include &lt;string&gt;

#include &lt;iostream&gt;

int main()

{
    std::variant&lt;int, std::string&gt; v = &quot;abc&quot;;
    std::cout &lt;&lt; std::boolalpha
              &lt;&lt; &quot;variant holds int? &quot;
              &lt;&lt; std::holds_alternative&lt;int&gt;(v) &lt;&lt; '\n'
              &lt;&lt; &quot;variant holds string? &quot;
              &lt;&lt; std::holds_alternative&lt;std::string&gt;(v) &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;variant holds int? false 
&nbsp;<wbr>&nbsp;variant holds string? true

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the zero-based index of the alternative held by the variant 
index <i>(public member function)</i> 
std::get(std::variant) reads the value of the variant given the index or the type (if the type is unique), throws on error 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++17)</i> 
