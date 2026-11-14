---
title: "stdmoneypunct(3)"
name: "stdmoneypunct"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmoneypunct/"
---

std::moneypunct&lt;CharT,International&gt;::~moneypunct - std::moneypunct&lt;CharT,International&gt;::~moneypunct

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;locale&gt;

protected: ~moneypunct();</code></pre> 
Destructs a std::moneypunct facet. This destructor is protected and virtual (due to base_class destructor being virtual). An object of type std::moneypunct, like most facets, can only be destroyed when the last std::locale object that implements this facet goes out of scope or if a user-defined class is derived from std::moneypunct and implements a public destructor. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;locale&gt;

struct Destructible_moneypunct : public std::moneypunct&lt;wchar_t&gt;

{
    Destructible_moneypunct(std::size_t refs = 0)
        : moneypunct(refs)
    {
    }
    // note: the implicit destructor is public
};

int main()

{
    Destructible_moneypunct dc;
    // std::moneypunct&lt;wchar_t&gt; c;  // compile error: protected destructor
}
</code></pre>
