---
title: "stdhas_facet(3)"
name: "stdhas_facet"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdhas_facet/"
---

std::has_facet - std::has_facet

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;locale&gt;

    template &lt;class Facet&gt;
    (until C++ 11)

        bool has_facet(const locale &amp;loc) throw();

template &lt;class Facet&gt;
(since C++ 11)

    bool has_facet(const locale &amp;loc) noexcept;</code></pre> 
Checks if the locale loc implements the facet Facet. 

<h2>Parameters</h2>

loc - the locale object to query

<h2>Return value</h2>

Returns true if the facet Facet was installed in the locale loc, false otherwise. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;locale&gt;
// minimal custom facet

struct myfacet : public std::locale::facet {
    static std::locale::id id;
};
std::locale::id myfacet::id;
int main()

{
    // loc is a &quot;C&quot; locale with myfacet added
    std::locale loc(std::locale::classic(), new myfacet);
    std::cout &lt;&lt; std::boolalpha
              &lt;&lt; &quot;Can loc classify chars? &quot;
              &lt;&lt; std::has_facet&lt;std::ctype&lt;char&gt;&gt;(loc) &lt;&lt; '\n'
              &lt;&lt; &quot;Can loc classify char32_t? &quot;
              &lt;&lt; std::has_facet&lt;std::ctype&lt;char32_t&gt;&gt;(loc) &lt;&lt; '\n'
              &lt;&lt; &quot;Does loc implement myfacet? &quot;
              &lt;&lt; std::has_facet&lt;myfacet&gt;(loc) &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Can loc classify chars? true 
&nbsp;<wbr>&nbsp;Can loc classify char32_t? false 
&nbsp;<wbr>&nbsp;Does loc implement myfacet? true

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;set of polymorphic facets that encapsulate cultural differences 
locale <i>(class)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;obtains a facet from a locale 
use_facet <i>(function template)</i> 
