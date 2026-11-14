---
title: "stdis_base_of(3)"
name: "stdis_base_of"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdis_base_of/"
description: "std::is_base_of – std::is_base_of"
---

<p>std::is_base_of &#8211; std::is_base_of</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;type_traits&gt;

    template &lt;class Base, class Derived&gt;
    (since C++ 11)

        struct is_base_of;</code></pre>
<p>If Derived is derived from Base or if both are the same non-union class (in both cases ignoring cv-qualification), provides the member constant value equal to true. Otherwise value is false.<br />
If both Base and Derived are non-union class types, and they are not the same type (ignoring cv-qualification), Derived shall be a complete_type; otherwise the behavior is undefined.<br />
Helper variable template template&lt; class Base, class Derived &gt;                                   (since C++17)</p>
<p>inline constexpr bool is_base_of_v = is_base_of&lt;Base, Derived&gt;::value;</p>
<p>Inherited from std::integral_constant </p>
<h2>Member constants</h2>
<p>value true if Derived is derived from Base or if both are the same non-union class (in both cases ignoring cv-qualification), false otherwise<br />
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
<h2>Notes</h2>
<p>std::is_base_of&lt;A, B&gt;::value is true even if A is a private, protected, or ambiguous base class of B. In many situations, std::is_convertible&lt;B*, A*&gt; is the more appropriate test.<br />
Although no class is its own base, std::is_base_of&lt;T, T&gt;::value is true because the intent of the trait is to model the &quot;is-a&quot; relationship, and T is a T. Despite that, std::is_base_of&lt;int, int&gt;::value is false because only classes participate in the relationship that this trait models.<br />
Possible Implementation namespace details<br />
{<br />
template &lt;typename Base&gt;<br />
std::true_type is_base_of_test_func(const volatile Base *);<br />
template &lt;typename Base&gt;<br />
std::false_type is_base_of_test_func(const volatile void *);<br />
template &lt;typename Base, typename Derived&gt;<br />
using pre_is_base_of = decltype(is_base_of_test_func&lt;Base&gt;(std::declval&lt;Derived *&gt;()));<br />
// with &lt;experimental/type_traits&gt;:<br />
// template &lt;typename Base, typename Derived&gt;<br />
// using pre_is_base_of2 = std::experimental::detected_or_t&lt;std::true_type, pre_is_base_of, Base, Derived&gt;;<br />
template &lt;typename Base, typename Derived, typename = void&gt;<br />
struct pre_is_base_of2 : public std::true_type {<br />
};<br />
// note std::void_t is a C++17 feature<br />
template &lt;typename Base, typename Derived&gt;<br />
struct pre_is_base_of2&lt;Base, Derived, std::void_t&lt;pre_is_base_of&lt;Base, Derived&gt;&gt;&gt; : public pre_is_base_of&lt;Base, Derived&gt; {<br />
};</p>
<p>} // namespace details<br />
template &lt;typename Base, typename Derived&gt;</p>
<p>struct is_base_of : public std::conditional_t&lt;<br />
                        std::is_class&lt;Base&gt;::value &amp;&amp; std::is_class&lt;Derived&gt;::value,<br />
                        details::pre_is_base_of2&lt;Base, Derived&gt;,<br />
                        std::false_type&gt; {<br />
};</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;type_traits&gt;
class A
{
};
class B : A
{
};
class C
{
};
int main()

{
    std::cout &lt;&lt; std::boolalpha;
    std::cout &lt;&lt; &quot;a2b: &quot; &lt;&lt; std::is_base_of&lt;A, B&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; &quot;b2a: &quot; &lt;&lt; std::is_base_of&lt;B, A&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; &quot;c2b: &quot; &lt;&lt; std::is_base_of&lt;C, B&gt;::value &lt;&lt; '
';
    std::cout &lt;&lt; &quot;same type: &quot; &lt;&lt; std::is_base_of&lt;C, C&gt;::value &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;a2b: true<br />
&nbsp;<wbr>&nbsp;b2a: false<br />
&nbsp;<wbr>&nbsp;c2b: false<br />
&nbsp;<wbr>&nbsp;same type: true</p>
<h2>See also</h2>
<p>is_convertible<br />
is_nothrow_convertible checks if a type can be converted to the other type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
(C++20) </p>
