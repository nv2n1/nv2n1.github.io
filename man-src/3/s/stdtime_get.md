---
title: "stdtime_get(3)"
name: "stdtime_get"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdtime_get/"
---

std::time_get&lt;CharT,InputIt&gt;::~time_get - std::time_get&lt;CharT,InputIt&gt;::~time_get

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;locale&gt;

protected: ~time_get();</code></pre> 
Destructs a std::time_get facet. This destructor is protected and virtual (due to base_class destructor being virtual). An object of type std::time_get, like most facets, can only be destroyed when the last std::locale object that implements this facet goes out of scope or if a user-defined class is derived from std::time_get and implements a public destructor. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;locale&gt;

struct Destructible_time_get : public std::time_get&lt;wchar_t&gt;

{
    Destructible_time_get(std::size_t refs = 0)
        : time_get(refs)
    {
    }
    // note: the implicit destructor is public
};

int main()

{
    Destructible_time_get dc;
    // std::time_get&lt;wchar_t&gt; c;  // compile error: protected destructor
}
</code></pre>
