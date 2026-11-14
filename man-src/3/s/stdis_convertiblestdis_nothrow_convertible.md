---
title: "stdis_convertiblestdis_nothrow_convertible(3)"
name: "stdis_convertiblestdis_nothrow_convertible"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdis_convertiblestdis_nothrow_convertible/"
description: "std::is_convertible,std::is_nothrow_convertible – std::is_convertible,std::is_nothrow_convertible"
---

<p>std::is_convertible,std::is_nothrow_convertible &#8211; std::is_convertible,std::is_nothrow_convertible</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;type_traits&gt;

    template &lt;class From, class To&gt;
    (1)(since C++ 11)

        struct is_convertible;

template &lt;class From, class To&gt;
(2)(since C++ 20)

    struct is_nothrow_convertible;
1) If the imaginary function definition To test()
{
    return std::declval&lt;From&gt;();
} is well-formed, (that is, either std::declval&lt;From&gt;() can be converted to To using implicit_conversions, or both From and To are possibly cv-qualified void), provides the member constant value equal to true. Otherwise value is false. For the purposes of this check, the use of std::declval in the return statement is not considered an odr-use.

Access_checks are performed as if from a context unrelated to either type. Only the validity of the immediate context of the expression in the return statement (including conversions to the return type) is considered.

2) Same as (1), but the conversion is also noexcept.

From and To shall each be a complete type, (possibly cv-qualified) void, or an array of unknown bound. Otherwise, the behavior is undefined.

If an instantiation of a template above depends, directly or indirectly, on an incomplete type, and that instantiation could yield a different result if that type were hypothetically completed, the behavior is undefined.</code></pre>
<p>Helper variable template template&lt; class From, class To &gt;                                                           (since C++17)</p>
<p>inline constexpr bool is_convertible_v = is_convertible&lt;From, To&gt;::value;</p>
<p>template&lt; class From, class To &gt;                                                           (since C++20)</p>
<p>inline constexpr bool is_nothrow_convertible_v = is_nothrow_convertible&lt;From, To&gt;::value;</p>
<p>Inherited from std::integral_constant </p>
<h2>Member constants</h2>
<p>value true if From is convertible to To , false otherwise<br />
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
<p>Gives well-defined results for reference types, void types, array types, and function types. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;type_traits&gt;
class E
{
  public:
    template &lt;class T&gt;
    E(T &amp;&amp;)
    {
    }
};
int main()

{
    class A
    {
    };
    class B : public A
    {
    };
    class C
    {
    };
    class D
    {
      public:
        operator C()
        {
            return c;
        }
        C c;
    };

    bool b2a = std::is_convertible&lt;B *, A *&gt;::value;
    bool a2b = std::is_convertible&lt;A *, B *&gt;::value;
    bool b2c = std::is_convertible&lt;B *, C *&gt;::value;
    bool d2c = std::is_convertible&lt;D, C&gt;::value;
    // A Perfect Forwarding constructor make the class 'convert' from everything
    bool everything2e = std::is_convertible&lt;A, E&gt;::value; //&lt; B, C, D, etc
    std::cout &lt;&lt; std::boolalpha;
    std::cout &lt;&lt; b2a &lt;&lt; '
';
    std::cout &lt;&lt; a2b &lt;&lt; '
';
    std::cout &lt;&lt; b2c &lt;&lt; '
';
    std::cout &lt;&lt; d2c &lt;&lt; '
';
    std::cout &lt;&lt; '
';
    std::cout &lt;&lt; everything2e &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;true<br />
&nbsp;<wbr>&nbsp;false<br />
&nbsp;<wbr>&nbsp;false<br />
&nbsp;<wbr>&nbsp;true </p>
<p>&nbsp;<wbr>&nbsp;true</p>
<h2>See also</h2>
