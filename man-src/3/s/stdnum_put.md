---
title: "stdnum_put(3)"
name: "stdnum_put"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnum_put/"
---

std::num_put&lt;CharT,OutputIt&gt;::~num_put - std::num_put&lt;CharT,OutputIt&gt;::~num_put

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;locale&gt;

protected: ~num_put();</code></pre> 
Destructs a std::num_put facet. This destructor is protected and virtual (due to base_class destructor being virtual). An object of type std::num_put, like most facets, can only be destroyed when the last std::locale object that implements this facet goes out of scope or if a user-defined class is derived from std::num_put and implements a public destructor. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;locale&gt;

struct Destructible_num_put : public std::num_put&lt;wchar_t&gt;

{
    Destructible_num_put(std::size_t refs = 0)
        : num_put(refs)
    {
    }
    // note: the implicit destructor is public
};

int main()

{
    Destructible_num_put dc;
    // std::num_put&lt;wchar_t&gt; c;  // compile error: protected destructor
}
</code></pre>
