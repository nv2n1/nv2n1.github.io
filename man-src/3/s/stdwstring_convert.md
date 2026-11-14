---
title: "stdwstring_convert(3)"
name: "stdwstring_convert"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdwstring_convert/"
---

std::wstring_convert&lt;Codecvt,Elem,Wide_alloc,Byte_alloc&gt;::~wstring_convert - std::wstring_convert&lt;Codecvt,Elem,Wide_alloc,Byte_alloc&gt;::~wstring_convert

<h2>Synopsis</h2>

<pre><code>~wstring_convert();</code></pre> 
Destroys the wstring_convert object and deletes the pointer to the conversion facet. 

<h2>Notes</h2>

Some implementations are able to delete any facet, including the locale-specific facets with protected destructors. Other implementations require the facet to have a public destructor, similar to the the locale-independent facets from &lt;codecvt&gt;. This is LWG_issue_721 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;locale&gt;

#include &lt;utility&gt;

#include &lt;codecvt&gt;
// utility wrapper to adapt locale-bound facets for wstring/wbuffer convert

template &lt;class Facet&gt;

struct deletable_facet : Facet

{
    template &lt;class... Args&gt;
    deletable_facet(Args &amp;&amp;...args)
        : Facet(std::forward&lt;Args&gt;(args)...)
    {
    }
    ~deletable_facet()
    {
    }
};
int main()

{
    // GB18030 / UCS4 conversion, using locale-based facet directly
    // typedef std::codecvt_byname&lt;char32_t, char, std::mbstate_t&gt; gbfacet_t;
    // Compiler error: &quot;calling a protected destructor of codecvt_byname&lt;&gt; in ~wstring_convert&quot;
    // std::wstring_convert&lt;gbfacet_t&gt; gbto32(new gbfacet_t(&quot;zh_CN.gb18030&quot;));
    // GB18030 / UCS4 conversion facet using a facet with public destructor
    typedef deletable_facet&lt;std::codecvt_byname&lt;char32_t, char, std::mbstate_t&gt;&gt; gbfacet_t;
    std::wstring_convert&lt;gbfacet_t&gt; gbto32(new gbfacet_t(&quot;zh_CN.gb18030&quot;));

} // destructor called here
</code></pre>
