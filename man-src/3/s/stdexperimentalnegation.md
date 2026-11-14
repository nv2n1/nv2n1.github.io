---
title: "stdexperimentalnegation(3)"
name: "stdexperimentalnegation"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalnegation/"
description: "std::experimental::negation – std::experimental::negation"
---

<p>std::experimental::negation &#8211; std::experimental::negation</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;experimental / type_traits&gt;

    template &lt;class B&gt;
    (1)(library fundamentals TS v2)

        struct negation;</code></pre>
<p>Forms the logical negation of the type trait B.<br />
The type negation&lt;B&gt; is a UnaryTypeTrait with a BaseCharacteristic of std::integral_constant&lt;bool, !bool(B::value)&gt;. </p>
<h2>Template parameters</h2>
<p>B &#8211; any type such that the expression bool(B::value) is a valid constant expression </p>
<p>Helper variable template </p>
<p>template&lt;class B&gt; (library fundamentals TS v2)<br />
constexpr bool negation_v = negation&lt;B&gt;::value; </p>
<p>Inherited from std::integral_constant</p>
<h2>Member constants</h2>
<p>value true if B has a member ::value such that !bool(B::value) is true , false otherwise<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code></p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts the object to bool, returns value<br />
operator bool <i>(public member function)</i> </p>
<p>operator() returns value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i><br />
<i>(C++14)</i></p>
<h2>Member types</h2>
<p>Type Definition<br />
value_type bool<br />
type std::integral_constant&lt;bool, value&gt;</p>
<h2>Possible implementation</h2>
<p>&nbsp;<wbr>&nbsp;template&lt;class B&gt;<br />
&nbsp;<wbr>&nbsp;struct negation : std::integral_constant&lt;bool, !bool(B::value)&gt; { };</p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
<h2>See also</h2>
<p>negation logical NOT metafunction<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++17)</i> </p>
