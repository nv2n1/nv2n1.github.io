---
title: "stdmoney_put(3)"
name: "stdmoney_put"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmoney_put/"
---

std::money_put&lt;CharT,OutputIt&gt;::~money_put - std::money_put&lt;CharT,OutputIt&gt;::~money_put

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;locale&gt;

protected: ~money_put();</code></pre> 
Destructs a std::money_put facet. This destructor is protected and virtual (due to base_class destructor being virtual). An object of type std::money_put, like most facets, can only be destroyed when the last std::locale object that implements this facet goes out of scope or if a user-defined class is derived from std::money_put and implements a public destructor. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;locale&gt;

struct Destructible_money_put : public std::money_put&lt;wchar_t&gt;

{
    Destructible_money_put(std::size_t refs = 0)
        : money_put(refs)
    {
    }
    // note: the implicit destructor is public
};

int main()

{
    Destructible_money_put dc;
    // std::money_put&lt;wchar_t&gt; c;  // compile error: protected destructor
}
</code></pre>
