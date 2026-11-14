---
title: "stdnum_get(3)"
name: "stdnum_get"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnum_get/"
---

std::num_get&lt;CharT,InputIt&gt;::~num_get - std::num_get&lt;CharT,InputIt&gt;::~num_get

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;locale&gt;

protected: ~num_get();</code></pre> 
Destructs a std::num_get facet. This destructor is protected and virtual (due to base_class destructor being virtual). An object of type std::num_get, like most facets, can only be destroyed when the last std::locale object that implements this facet goes out of scope or if a user-defined class is derived from std::num_get and implements a public destructor. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;locale&gt;

struct Destructible_num_get : public std::num_get&lt;wchar_t&gt;

{
    Destructible_num_get(std::size_t refs = 0)
        : num_get(refs)
    {
    }
    // note: the implicit destructor is public
};

int main()

{
    Destructible_num_get dc;
    // std::num_get&lt;wchar_t&gt; c;  // compile error: protected destructor
}
</code></pre>
