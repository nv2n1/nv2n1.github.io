---
title: "stdvisit(3)"
name: "stdvisit"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdvisit/"
---

std::visit - std::visit

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;variant&gt;

template &lt;class Visitor, class... Variants&gt;                       (1) (since C++17)

constexpr /*see below*/ visit(Visitor&amp;&amp; vis, Variants&amp;&amp;... vars);

template &lt;class R, class Visitor, class... Variants&gt;              (2) (since C++20)

constexpr R visit(Visitor&amp;&amp;, Variants&amp;&amp;...);</code></pre> 
Applies the visitor vis to the variants vars 
Effectively returns 
std::invoke(std::forward&lt;Visitor&gt;(vis), std::get&lt;is&gt;(std::forward&lt;Variants&gt;(vars))...) 
, where is... is vars.index().... 
1) The return type is deduced from the returned expression as if by decltype. The call is ill-formed if the invocation above is not a valid expression of the same type and value category, for all combinations of alternative types of all variants. 
2) The return type is R. If R is (possibly cv-qualified) void, the result of the invoke expression is discarded. 

<h2>Parameters</h2>

vis - a Callable that accepts every possible alternative from every variant 
vars - list of variants to pass to the visitor

<h2>Return value</h2>

1) The value returned by the selected invocation of the visitor. 
2) Nothing if R is (possibly cv-qualified) void; otherwise the value returned by the selected invocation of the visitor, implicitly converted to R. 

<h2>Exceptions</h2>

Throws std::bad_variant_access if any variant in vars is valueless_by_exception.

<h2>Complexity</h2>

When the number of variants is zero or one, the invocation of the callable object is implemented in constant time, i.e. it does not depend on sizeof...(Types). 
If the number of variants is larger than 1, the invocation of the callable object has no complexity requirements.

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iomanip&gt;

#include &lt;iostream&gt;

#include &lt;string&gt;

#include &lt;type_traits&gt;

#include &lt;variant&gt;

#include &lt;vector&gt;
// the variant to visit

using var_t = std::variant&lt;int, long, double, std::string&gt;;
// helper type for the visitor #3

template &lt;class T&gt;
struct always_false : std::false_type {
};
// helper type for the visitor #4

template &lt;class... Ts&gt;
struct overloaded : Ts... {
    using Ts::operator()...;
};

template &lt;class... Ts&gt;
overloaded(Ts...) -&gt; overloaded&lt;Ts...&gt;;
int main()
{
    std::vector&lt;var_t&gt; vec = {10, 15l, 1.5, &quot;hello&quot;};
    for (auto &amp;v : vec) {
        // 1. void visitor, only called for side-effects (here, for I/O)
        std::visit([](auto &amp;&amp;arg) { std::cout &lt;&lt; arg; }, v);
        // 2. value-returning visitor, demonstrates the idiom of returning another variant
        var_t w = std::visit([](auto &amp;&amp;arg) -&gt; var_t { return arg + arg; }, v);
        // 3. type-matching visitor: a lambda that handles each type differently
        std::cout &lt;&lt; &quot;. After doubling, variant holds &quot;;
        std::visit([](auto &amp;&amp;arg) {
            using T = std::decay_t&lt;decltype(arg)&gt;;
            if constexpr (std::is_same_v&lt;T, int&gt;)
                std::cout &lt;&lt; &quot;int with value &quot; &lt;&lt; arg &lt;&lt; '\n';
            else if constexpr (std::is_same_v&lt;T, long&gt;)
                std::cout &lt;&lt; &quot;long with value &quot; &lt;&lt; arg &lt;&lt; '\n';
            else if constexpr (std::is_same_v&lt;T, double&gt;)
                std::cout &lt;&lt; &quot;double with value &quot; &lt;&lt; arg &lt;&lt; '\n';
            else if constexpr (std::is_same_v&lt;T, std::string&gt;)
                std::cout &lt;&lt; &quot;std::string with value &quot; &lt;&lt; std::quoted(arg) &lt;&lt; '\n';
            else
                static_assert(always_false&lt;T&gt;::value, &quot;non-exhaustive visitor!&quot;);
        },
                   w);
    }
    for (auto &amp;v : vec) {
        // 4. another type-matching visitor: a class with 3 overloaded operator()'s
        std::visit(overloaded{
                       [](auto arg) { std::cout &lt;&lt; arg &lt;&lt; ' '; },
                       [](double arg) { std::cout &lt;&lt; std::fixed &lt;&lt; arg &lt;&lt; ' '; },
                       [](const std::string &amp;arg) { std::cout &lt;&lt; std::quoted(arg) &lt;&lt; ' '; },
                   },
                   v);
    }
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;10. After doubling, variant holds int with value 20 
&nbsp;<wbr>&nbsp;15. After doubling, variant holds long with value 30 
&nbsp;<wbr>&nbsp;1.5. After doubling, variant holds double with value 3 
&nbsp;<wbr>&nbsp;hello. After doubling, variant holds std::string with value &quot;hellohello&quot; 
&nbsp;<wbr>&nbsp;10 15 1.500000 &quot;hello&quot;

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swaps with another variant 
swap <i>(public member function)</i> 
