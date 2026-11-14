---
title: "stduse_facet(3)"
name: "stduse_facet"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stduse_facet/"
---

std::use_facet - std::use_facet

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;locale&gt;

    template &lt;class Facet&gt;

    const Facet &amp;use_facet(const std::locale &amp;loc);</code></pre> 
Obtains a reference to a facet implemented by loc. 

<h2>Parameters</h2>

loc - the locale object to query

<h2>Return value</h2>

Returns a reference to the facet. The reference returned by this function is valid as long as any std::locale object exists that implements Facet. 

<h2>Exceptions</h2>

std::bad_cast if std::has_facet&lt;Facet&gt;(loc) == false.

<h2>Example</h2>

Display the 3-letter currency name used by the user's preferred locale 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;locale&gt;
int main()

{
    std::locale loc = std::locale(&quot;&quot;); // user's preferred locale
    std::cout &lt;&lt; &quot;Your currency string is &quot;
              &lt;&lt; std::use_facet&lt;std::moneypunct&lt;char, true&gt;&gt;(loc).curr_symbol() &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Your currency string is USD

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;set of polymorphic facets that encapsulate cultural differences 
locale <i>(class)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if a locale implements a specific facet 
has_facet <i>(function template)</i> 
