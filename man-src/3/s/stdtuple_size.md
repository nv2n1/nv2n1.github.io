---
title: "stdtuple_size(3)"
name: "stdtuple_size"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdtuple_size/"
description: "std::tuple_size<std::tuple> – std::tuple_size<std::tuple>"
---

<p>std::tuple_size&lt;std::tuple&gt; &#8211; std::tuple_size&lt;std::tuple&gt;</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;tuple&gt;

    template &lt;class T&gt;
    (1)(since C++ 11)

        class tuple_size; /*undefined*/

template &lt;class... Types&gt;

class tuple_size&lt;std::tuple&lt;Types...&gt;&gt;(2)(since C++ 11)

    : public std::integral_constant&lt;std::size_t, sizeof...(Types)&gt;
{
};

Defined in header&lt;tuple&gt;

    Defined in header&lt;array&gt;(since C++ 17)

        Defined in header&lt;utility&gt;(since C++ 17)

            Defined in header&lt;ranges&gt;(since C++ 20)

                Defined in header&lt;span&gt;(since C++ 20)

                    template &lt;class T&gt;

                    class tuple_size&lt;const T&gt;(3)(since C++ 11)

    : public std::integral_constant&lt;std::size_t, tuple_size&lt;T&gt;::value&gt;
{
};

template &lt;class T&gt;

class tuple_size&lt;volatile T&gt;(4)(since C++ 11)

    : public std::integral_constant&lt;std::size_t, tuple_size&lt;T&gt;::value&gt;
{
};

template &lt;class T&gt;

class tuple_size&lt;const volatile T&gt;(5)(since C++ 11)

    : public std::integral_constant&lt;std::size_t, tuple_size&lt;T&gt;::value&gt;
{
};</code></pre>
<p>Provides access to the number of elements in a tuple as a compile-time constant expression.<br />
In addition to being available via inclusion of the &lt;tuple&gt; header, the templates (3-5) are available when either of the headers &lt;array&gt; or &lt;utility&gt; are included.<br />
All specializations of std::tuple_size satisfy UnaryTypeTrait with BaseCharacteristic std::integral_constant&lt;std::size_t, N&gt; for some N.<br />
The cv-T templates (3-5) are SFINAE-friendly: if std::tuple_size&lt;T&gt;::value is ill-formed when treated as an unevaluated operand, (3-5) do not provide the member value. Access checking is performed as if in a context unrelated to tuple_size and T. Only the validity of the immediate context of the expression is considered. This allows #include &lt;utility&gt;</p>
<p>struct X {<br />
    int a, b;<br />
};<br />
(since C++ 17)</p>
<p>    const auto [x, y] = X(); // decomposition declaration first attempts tuple_size&lt;const X&gt;<br />
                             // which attempts to use tuple_size&lt;X&gt;::value, and that&#8217;s OK</p>
<p>Helper variable template template&lt; class T &gt;                                                (since C++17)</p>
<p>inline constexpr std::size_t tuple_size_v = tuple_size&lt;T&gt;::value;</p>
<p>Inherited from std::integral_constant </p>
<h2>Member constants</h2>
<p>value sizeof&#8230;(Types)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code></p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts the object to std::size_t, returns value<br />
operator std::size_t <i>(public member function)</i> </p>
<p>operator() returns value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i><br />
<i>(C++14)</i></p>
<h2>Member types</h2>
<p>Type Definition<br />
value_type std::size_t<br />
type std::integral_constant&lt;std::size_t, value&gt;</p>
<h2>Example</h2>
<p>// Run this code #include &lt;iostream&gt;</p>
<p>#include &lt;tuple&gt;<br />
&nbsp;<wbr>&nbsp;template &lt;class T&gt;<br />
&nbsp;<wbr>&nbsp;void test(T t)<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int a[std::tuple_size&lt;T&gt;::value]; // can be used at compile time </p>
<pre><code>std::cout &lt;&lt; std::tuple_size&lt;T&gt;::value &lt;&lt; '
'; // or at run time
}
int main()

{
    test(std::make_tuple(1, 2, 3.14));
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;3</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;obtains the size of an array<br />
std::tuple_size&lt;std::array&gt; <i>(class template specialization)</i><br />
std::tuple_size&lt;std::pair&gt; obtains the size of a pair<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template specialization)</i><br />
<i>(C++11)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tuple accesses specified element<br />
std::get(std::tuple) <i>(function template)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;obtains the type of the specified element<br />
tuple_element <i>(class template specialization)</i> </p>
