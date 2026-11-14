---
title: "stdcollatecollate(3)"
name: "stdcollatecollate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcollatecollate/"
---

std::collate&lt;CharT&gt;::~collate - std::collate&lt;CharT&gt;::~collate

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;locale&gt;

protected: ~collate();</code></pre> 
Destructs a std::collate facet. This destructor is protected and virtual (due to base_class destructor being virtual). An object of type std::collate, like most facets, can only be destroyed when the last std::locale object that implements this facet goes out of scope or if a user-defined class is derived from std::collate and implements a public destructor. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;locale&gt;

struct Destructible_collate : public std::collate&lt;wchar_t&gt;

{
    Destructible_collate(std::size_t refs = 0)
        : collate(refs)
    {
    }
    // note: the implicit destructor is public
};

int main()

{
    Destructible_collate dc;
    // std::collate&lt;wchar_t&gt; c;  // compile error: protected destructor
}
</code></pre>
