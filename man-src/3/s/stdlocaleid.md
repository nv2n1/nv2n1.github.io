---
title: "stdlocaleid(3)"
name: "stdlocaleid"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdlocaleid/"
---

std::locale::id - std::locale::id

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;locale&gt;

class locale::id;</code></pre> 
The class std::locale::id provides implementation-specific identification of a locale facet. Each class derived from std::locale::facet must have a public static member named id of type std::locale::id and each std::locale object maintains a list of facets it implements, indexed by their ids. 
Facets with the same id belong to the same facet category and replace each other when added to a locale object. 

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a new id 
constructor <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copy assignment operator is deleted 
operator= <i>(public member function)</i>

<h2>Example</h2>

The following example shows how to construct a minimal custom facet. 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;locale&gt;
struct myfacet : std::locale::facet

{
    myfacet(std::size_t refs = 0)
        : facet(refs)
    {
    }
    static std::locale::id id;
};
std::locale::id myfacet::id;
int main()

{
    std::locale myloc(std::locale(), new myfacet);
    std::cout &lt;&lt; &quot;has_facet&lt;myfacet&gt;(myloc) returns &quot; &lt;&lt; std::boolalpha
              &lt;&lt; std::has_facet&lt;myfacet&gt;(myloc) &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;has_facet&lt;myfacet&gt;(myloc) returns true

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the base class for all facet categories: each facet of any category is derived from this type 
facet <i>(class)</i> 
