---
title: "stdbad_cast(3)"
name: "stdbad_cast"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbad_cast/"
description: "std::bad_cast – std::bad_cast"
---

<p>std::bad_cast &#8211; std::bad_cast</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;typeinfo&gt;

class bad_cast : public std::exception;</code></pre>
<p>An exception of this type is thrown when a dynamic_cast to a reference type fails the run-time check (e.g. because the types are not related by inheritance), and also from std::use_facet if the requested facet does not exist in the locale.<br />
&nbsp;std-bad cast-inheritance.svg<br />
Inheritance diagram </p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a new bad_cast object<br />
constructor <i>(public member function)</i> </p>
<p>Inherited from std::exception</p>
<h2>Member functions</h2>
<p>destructor destroys the exception object<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual public member function of std::exception)</i><br />
<code>[virtual]</code> </p>
<p>what returns an explanatory string<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual public member function of std::exception)</i><br />
<code>[virtual]</code></p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;typeinfo&gt;
struct Foo {
    virtual ~Foo()
    {
    }
};

struct Bar {
    virtual ~Bar()
    {
    }
};
int main()

{
    Bar b;
    try {
        Foo &amp;f = dynamic_cast&lt;Foo &amp;&gt;(b);
    } catch (const std::bad_cast &amp;e) {
        std::cout &lt;&lt; e.what() &lt;&lt; '
';
    }
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;Bad dynamic cast</p>
