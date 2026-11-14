---
title: "stdmessagesmessages(3)"
name: "stdmessagesmessages"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmessagesmessages/"
---

std::messages&lt;CharT&gt;::~messages - std::messages&lt;CharT&gt;::~messages

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;locale&gt;

protected: ~messages();</code></pre> 
Destructs a std::messages facet. This destructor is protected and virtual (due to base_class destructor being virtual). An object of type std::messages, like most facets, can only be destroyed when the last std::locale object that implements this facet goes out of scope or if a user-defined class is derived from std::messages and implements a public destructor. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;locale&gt;

struct Destructible_messages : public std::messages&lt;wchar_t&gt;

{
    Destructible_messages(std::size_t refs = 0)
        : messages(refs)
    {
    }
    // note: the implicit destructor is public
};

int main()

{
    Destructible_messages dc;
    // std::messages&lt;wchar_t&gt; c;  // compile error: protected destructor
}
</code></pre>
