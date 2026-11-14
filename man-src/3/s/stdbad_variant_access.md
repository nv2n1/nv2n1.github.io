---
title: "stdbad_variant_access(3)"
name: "stdbad_variant_access"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbad_variant_access/"
description: "std::bad_variant_access – std::bad_variant_access"
---

<p>std::bad_variant_access &#8211; std::bad_variant_access</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;variant&gt;<br />
class bad_variant_access : public std::exception <i>(since C++17)</i><br />
std::bad_variant_access is the type of the exception thrown in the following situations:<br />
* std::get(std::variant) called with an index or type that does not match the currently active alternative<br />
* std::visit called to visit a variant that is valueless_by_exception </p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs the bad_variant_access object<br />
constructor <i>(public member function)</i> </p>
<p>&nbsp;std::bad_variant_access ::bad_variant_access() </p>
<p>bad_variant_access() noexcept; </p>
<p>Constructs a new instance of std::bad_variant_access.</p>
<h2>Parameters</h2>
<p><i>(none)</i> </p>
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
<pre><code>#include &lt;variant&gt;

#include &lt;iostream&gt;
int main()

{
    std::variant&lt;int, float&gt; v;
    v = 12;
    try {
        std::get&lt;float&gt;(v);
    } catch (const std::bad_variant_access &amp;e) {
        std::cout &lt;&lt; e.what() &lt;&lt; '
';
    }
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;bad_variant_access</p>
<h2>See also</h2>
<p>std::get(std::variant) reads the value of the variant given the index or the type (if the type is unique), throws on error<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++17)</i><br />
visit calls the provided functor with the arguments held by one or more variants<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++17)</i> </p>
