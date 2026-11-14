---
title: "stdvariant_sizestdvariant_size_v(3)"
name: "stdvariant_sizestdvariant_size_v"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdvariant_sizestdvariant_size_v/"
description: "std::variant_size,std::variant_size_v – std::variant_size,std::variant_size_v"
---

<p>std::variant_size,std::variant_size_v &#8211; std::variant_size,std::variant_size_v</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;variant&gt;

    template &lt;class T&gt;
    (1)(since C++ 17)

        struct variant_size; /* undefined */

template &lt;class... Types&gt;

struct variant_size&lt;std::variant&lt;Types...&gt;&gt;(2)(since C++ 17)

    : std::integral_constant&lt;std::size_t, sizeof...(Types)&gt; {
};

template &lt;class T&gt;
class variant_size&lt;const T&gt;;

template &lt;class T&gt;
class variant_size&lt;volatile T&gt;;
(3)(since C++ 17)

    template &lt;class T&gt;
    class variant_size&lt;const volatile T&gt;;</code></pre>
<p>Provides access to the number of alternatives in a possibly cv-qualified variant as a compile-time constant expression.<br />
Formally,<br />
2) meets the UnaryTypeTrait requirements with a BaseCharacteristic of std::integral_constant&lt;std::size_t, sizeof&#8230;(Types)&gt;<br />
3) meets the UnaryTypeTrait requirements with a BaseCharacteristic of std::integral_constant&lt;std::size_t, variant_size&lt;T&gt;&gt;<br />
Helper variable template </p>
<pre><code>template &lt;class T&gt;                                                          (since C++17)

inline constexpr std::size_t variant_size_v = std::variant_size&lt;T&gt;::value;
</code></pre>
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
<h2>Notes</h2>
<p>All specializations of std::variant_size satisfy UnaryTypeTrait with BaseCharacteristic std::integral_constant&lt;std::size_t, N&gt; for some N. </p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
<h2>See also</h2>
<p>variant_alternative obtains the type of the alternative specified by its index, at compile time<br />
variant_alternative_t <i>(class template)</i> (alias template)<br />
<i>(C++17)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;obtains the size of tuple at compile time<br />
tuple_size <i>(class template specialization)</i> </p>
