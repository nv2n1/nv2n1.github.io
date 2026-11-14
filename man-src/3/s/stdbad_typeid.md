---
title: "stdbad_typeid(3)"
name: "stdbad_typeid"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbad_typeid/"
description: "std::bad_typeid – std::bad_typeid"
---

<p>std::bad_typeid &#8211; std::bad_typeid</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;typeinfo&gt;

class bad_typeid : public std::exception;</code></pre>
<p>An exception of this type is thrown when a typeid operator is applied to a dereferenced null pointer value of a polymorphic type.<br />
&nbsp;std-bad typeid-inheritance.svg<br />
Inheritance diagram </p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a new bad_typeid object<br />
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
struct S { // The type has to be polymorphic
    virtual void f();
};
int main()

{
    S *p = nullptr;
    try {
        std::cout &lt;&lt; typeid(*p).name() &lt;&lt; '
';
    } catch (const std::bad_typeid &amp;e) {
        std::cout &lt;&lt; e.what() &lt;&lt; '
';
    }
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;Attempted a typeid of NULL pointer!</p>
