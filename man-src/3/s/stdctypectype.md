---
title: "stdctypectype(3)"
name: "stdctypectype"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdctypectype/"
---

std::ctype&lt;char&gt;::~ctype - std::ctype&lt;char&gt;::~ctype

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;locale&gt;

protected: ~ctype();</code></pre> 
Destructs a std::ctype&lt;char&gt; facet. This destructor is protected and virtual (due to base_class destructor being virtual). An object of type std::ctype&lt;char&gt;, like most facets, can only be destroyed when the last std::locale object that implements this facet goes out of scope or if a user-defined class is derived from std::ctype&lt;char&gt; and implements a public destructor. 
If, when this instance of std::ctype&lt;char&gt; was constructed, a custom classification table was provided and the second argument to the constructor (the boolean del) was true, then this destructor executes delete[] table(). 
