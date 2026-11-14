---
title: "stdis_placeholder(3)"
name: "stdis_placeholder"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdis_placeholder/"
description: "std::is_placeholder – std::is_placeholder"
---

<p>std::is_placeholder &#8211; std::is_placeholder</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;functional&gt;

    template &lt;class T&gt;
    (since C++ 11)

        struct is_placeholder;</code></pre>
<p>If T is the type of a standard placeholder (_1, _2, _3, &#8230;), then this template is derived from std::integral_constant&lt;int,1&gt;, std::integral_constant&lt;int,2&gt;, std::integral_constant&lt;int,3&gt;, respectively.<br />
If T is not a standard placeholder type, this template is derived from std::integral_constant&lt;int,0&gt;<br />
The template may be specialized for any user-defined T type: the specialization must satisfy UnaryTypeTrait with BaseCharacteristic of std::integral_constant&lt;int, N&gt; with N &gt; 0 to indicate that T should be treated as N&#8217;th placeholder type.<br />
std::bind uses std::is_placeholder to detect placeholders for unbound arguments.<br />
Helper variable template template &lt;class T&gt;<br />
(since C++ 17)</p>
<p>    inline constexpr int is_placeholder_v = is_placeholder&lt;T&gt;::value;</p>
<p>Inherited from std::integral_constant </p>
<h2>Member constants</h2>
<p>value placeholder value or 0 for non-placeholder types<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code></p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts the object to int, returns value<br />
operator int <i>(public member function)</i> </p>
<p>operator() returns value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i><br />
<i>(C++14)</i></p>
<h2>Member types</h2>
<p>Type Definition<br />
value_type int<br />
type std::integral_constant&lt;int, value&gt;</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;type_traits&gt;

#include &lt;functional&gt;
struct My_2 {

} my_2;
namespace std
{
template &lt;&gt;
struct is_placeholder&lt;My_2&gt; : public integral_constant&lt;int, 2&gt; {
};

} // namespace std
int f(int n1, int n2)

{
    return n1 + n2;
}
int main()

{
    std::cout &lt;&lt; &quot;Standard placeholder _5 is for the argument number &quot;
              &lt;&lt; std::is_placeholder&lt;decltype(std::placeholders::_5)&gt;::value
              &lt;&lt; '
';
    auto b = std::bind(f, my_2, 2);
    std::cout &lt;&lt; &quot;Adding 2 to 11 selected with a custom placeholder gives &quot;
              &lt;&lt; b(10, 11) // the first argument, namely 10, is ignored
              &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;Standard placeholder _5 is for the argument number 5<br />
&nbsp;<wbr>&nbsp;Adding 2 to 11 selected with a custom placeholder gives 13</p>
<h2>See also</h2>
<p>bind binds one or more arguments to a function object<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++11)</i><br />
_1,__2,__3,__4,_&#8230; placeholders for the unbound arguments in a std::bind expression<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(constant)<br />
<i>(C++11)</i> </p>
