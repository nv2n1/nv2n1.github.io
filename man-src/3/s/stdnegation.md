---
title: "stdnegation(3)"
name: "stdnegation"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnegation/"
description: "std::negation – std::negation"
---

<p>std::negation &#8211; std::negation</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;type_traits&gt;

    template &lt;class B&gt;
    (1)(since C++ 17)

        struct negation;</code></pre>
<p>Forms the logical negation of the type trait B.<br />
The type std::negation&lt;B&gt; is a UnaryTypeTrait with a BaseCharacteristic of std::bool_constant&lt;!bool(B::value)&gt;. </p>
<h2>Template parameters</h2>
<p>B &#8211; any type such that the expression bool(B::value) is a valid constant expression </p>
<p>Helper variable template </p>
<p>template&lt;class B&gt; <i>(since C++17)</i><br />
inline constexpr bool negation_v = negation&lt;B&gt;::value; </p>
<p>Inherited from std::integral_constant</p>
<h2>Member constants</h2>
<p>value true if B has a member ::value that is false when explicitly converted to bool , false otherwise<br />
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
&nbsp;<wbr>&nbsp;struct negation : std::bool_constant&lt;!bool(B::value)&gt; { };</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;type_traits&gt;
static_assert(
    std::is_same&lt;
        std::bool_constant&lt;false&gt;,
        typename std::negation&lt;std::bool_constant&lt;true&gt;&gt;::type&gt;::value,
    &quot;&quot;);

static_assert(
    std::is_same&lt;
        std::bool_constant&lt;true&gt;,
        typename std::negation&lt;std::bool_constant&lt;false&gt;&gt;::type&gt;::value,
    &quot;&quot;);
int main()

{
    std::cout &lt;&lt; std::boolalpha;
    std::cout &lt;&lt; std::negation&lt;std::bool_constant&lt;true&gt;&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; std::negation&lt;std::bool_constant&lt;false&gt;&gt;::value &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;false<br />
&nbsp;<wbr>&nbsp;true</p>
<h2>See also</h2>
<p>conjunction variadic logical AND metafunction<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++17)</i><br />
disjunction variadic logical OR metafunction<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++17)</i><br />
integral_constant<br />
bool_constant compile-time constant of specified type with specified value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
<i>(C++17)</i> </p>
