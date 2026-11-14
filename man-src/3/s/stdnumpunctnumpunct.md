---
title: "stdnumpunctnumpunct(3)"
name: "stdnumpunctnumpunct"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnumpunctnumpunct/"
---

std::numpunct&lt;CharT&gt;::~numpunct - std::numpunct&lt;CharT&gt;::~numpunct

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;locale&gt;

protected: ~numpunct();</code></pre> 
Destructs a std::numpunct facet. This destructor is protected and virtual (due to base_class destructor being virtual). An object of type std::numpunct, like most facets, can only be destroyed when the last std::locale object that implements this facet goes out of scope or if a user-defined class is derived from std::numpunct and implements a public destructor. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;locale&gt;

struct Destructible_numpunct : public std::numpunct&lt;wchar_t&gt;

{
    Destructible_numpunct(std::size_t refs = 0)
        : numpunct(refs)
    {
    }
    // note: the implicit destructor is public
};

int main()

{
    Destructible_numpunct dc;
    // std::numpunct&lt;wchar_t&gt; c;  // compile error: protected destructor
}
</code></pre>
