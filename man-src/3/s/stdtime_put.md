---
title: "stdtime_put(3)"
name: "stdtime_put"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdtime_put/"
---

std::time_put&lt;CharT,OutputIt&gt;::~time_put - std::time_put&lt;CharT,OutputIt&gt;::~time_put

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;locale&gt;

protected: ~time_put();</code></pre> 
Destructs a std::time_put facet. This destructor is protected and virtual (due to base_class destructor being virtual). An object of type std::time_put, like most facets, can only be destroyed when the last std::locale object that implements this facet goes out of scope or if a user-defined class is derived from std::time_put and implements a public destructor. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;locale&gt;

struct Destructible_time_put : public std::time_put&lt;wchar_t&gt;

{
    Destructible_time_put(std::size_t refs = 0)
        : time_put(refs)
    {
    }
    // note: the implicit destructor is public
};

int main()

{
    Destructible_time_put dc;
    // std::time_put&lt;wchar_t&gt; c;  // compile error: protected destructor
}
</code></pre>
