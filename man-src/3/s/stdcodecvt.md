---
title: "stdcodecvt(3)"
name: "stdcodecvt"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcodecvt/"
---

std::codecvt&lt;InternT,ExternT,State&gt;::~codecvt - std::codecvt&lt;InternT,ExternT,State&gt;::~codecvt

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;locale&gt;

protected: ~codecvt();</code></pre> 
Destructs a std::codecvt facet. This destructor is protected and virtual (due to base_class destructor being virtual). An object of type std::codecvt, like most facets, can only be destroyed when the last std::locale object that implements this facet goes out of scope or if a user-defined class is derived from std::codecvt and implements a public destructor. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;locale&gt;

struct Destructible_codecvt : public std::codecvt&lt;wchar_t, char, std::mbstate_t&gt;

{
    Destructible_codecvt(std::size_t refs = 0)
        : codecvt(refs)
    {
    }
    // note: the implicit destructor is public
};

int main()

{
    Destructible_codecvt dc;
    // std::codecvt&lt;wchar_t&gt; c;  // compile error: protected destructor
}
</code></pre>
