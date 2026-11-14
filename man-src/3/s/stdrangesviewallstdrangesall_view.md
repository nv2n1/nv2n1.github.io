---
title: "stdrangesviewallstdrangesall_view(3)"
name: "stdrangesviewallstdrangesall_view"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrangesviewallstdrangesall_view/"
---

std::ranges::view::all,std::ranges::all_view - std::ranges::view::all,std::ranges::all_view

<h2>Synopsis</h2>

<pre><code>template &lt;ViewableRange R&gt;                               (1) (since C++20)

using all_view = decltype(view::all(std::declval&lt;R&gt;()));

namespace view {

    inline constexpr /*unspecified*/ all = /*unspecified*/;  (2) (since C++20)

}</code></pre> 
A range adaptor that returns a View that includes all elements of its Range argument. 
The expression view::all(E) is expression-equivalent (has the same effect) to: *decay - copy(E) if the decayed type of E models View.

             *Otherwise,
    std::ranges::ref_view
{
    E
}
if that
    expression is well - formed

                             *Otherwise,
        std::ranges::subrange
    {
        E
    }


<h2>Example</h2>

// Run this code <pre><code>#include &lt;ranges&gt;

#include &lt;vector&gt;

#include &lt;iostream&gt;
int main()

{
    std::vector&lt;int&gt; v{0, 1, 2, 3, 4, 5};
    for (int n : std::view::all(v) | std::view::take(2)) {
        std::cout &lt;&lt; n &lt;&lt; ' ';
    }
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;0 1
