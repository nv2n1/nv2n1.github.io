---
title: "stdmoney_get(3)"
name: "stdmoney_get"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmoney_get/"
---

std::money_get&lt;CharT,InputIt&gt;::~money_get - std::money_get&lt;CharT,InputIt&gt;::~money_get

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;locale&gt;

protected: ~money_get();</code></pre> 
Destructs a std::money_get facet. This destructor is protected and virtual (due to base_class destructor being virtual). An object of type std::money_get, like most facets, can only be destroyed when the last std::locale object that implements this facet goes out of scope or if a user-defined class is derived from std::money_get and implements a public destructor. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;locale&gt;

struct Destructible_money_get : public std::money_get&lt;wchar_t&gt;

{
    Destructible_money_get(std::size_t refs = 0)
        : money_get(refs)
    {
    }
    // note: the implicit destructor is public
};

int main()

{
    Destructible_money_get dc;
    // std::money_get&lt;wchar_t&gt; c;  // compile error: protected destructor
}
</code></pre>
