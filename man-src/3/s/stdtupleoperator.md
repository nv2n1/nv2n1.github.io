---
title: "stdtupleoperator(3)"
name: "stdtupleoperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdtupleoperator/"
description: "std::tuple<Types…>::operator= – std::tuple<Types…>::operator="
---

<p>std::tuple&lt;Types&#8230;&gt;::operator= &#8211; std::tuple&lt;Types&#8230;&gt;::operator=</p>
<h2>Synopsis</h2>
<pre><code>tuple &amp;operator=(const tuple &amp;other);
(since C++ 11)(until C++ 20)

    constexpr tuple &amp;
    operator=(const tuple &amp;other);
(since C++ 20)

    tuple &amp;
    operator=(tuple &amp;&amp;other) noexcept(/* see below */);
(since C++ 11)(until C++ 20)

    constexpr tuple &amp;
    operator=(tuple &amp;&amp;other) noexcept(/* see below */);
(since C++ 20)

    template &lt;class... UTypes&gt;
    (since C++ 11)

        tuple &amp;
        operator=(const tuple&lt;UTypes...&gt; &amp;other);
(until C++ 20)

    template &lt;class... UTypes&gt;
    (since C++ 20)

        constexpr tuple &amp;
        operator=(const tuple&lt;UTypes...&gt; &amp;other);

template &lt;class... UTypes&gt;
(1)(since C++ 11)

    tuple &amp;
    operator=(tuple&lt;UTypes...&gt; &amp;&amp;other);
(until C++ 20)

    template &lt;class... UTypes&gt;
    (2)(since C++ 20)

        constexpr tuple &amp;
        operator=(tuple&lt;UTypes...&gt; &amp;&amp;other);
(3)

    template &lt;class U1, class U2&gt;
    (since C++ 11)

        tuple &amp;
        operator=(const pair&lt;U1, U2&gt; &amp;p);
(4)(until C++ 20)

    template &lt;class U1, class U2&gt;
    (since C++ 20)

        constexpr tuple &amp;
        operator=(const pair&lt;U1, U2&gt; &amp;p);
(5)

    template &lt;class U1, class U2&gt;
    (since C++ 11)

        tuple &amp;
        operator=(pair&lt;U1, U2&gt; &amp;&amp;p);
(6)(until C++ 20)

    template &lt;class U1, class U2&gt;
    (since C++ 20)

        constexpr tuple &amp;
        operator=(pair&lt;U1, U2&gt; &amp;&amp;p);</code></pre>
<p>Replaces the contents of the tuple with the contents of another tuple or a pair.<br />
1) Copy assignment operator. Assigns each element of other to the corresponding element of *this.<br />
2) Move assignment operator. For all i, assigns std::forward&lt;Ti&gt;(get&lt;i&gt;(other)) to get&lt;i&gt;(*this).<br />
3) For all i, assigns std::get&lt;i&gt;(other) to std::get&lt;i&gt;(*this).<br />
4) For all i, assigns std::forward&lt;Ui&gt;(std::get&lt;i&gt;(other)) to std::get&lt;i&gt;(*this).<br />
5) Assigns p.first to the first element of *this and p.second to the second element of *this.<br />
6) Assigns std::forward&lt;U1&gt;(p.first) to the first element of *this and std::forward&lt;U2&gt;(p.second) to the second element of *this.<br />
The behavior of these functions is undefined unless:<br />
* For <code>(1)</code>, std::is_copy_assignable&lt;T_i&gt;::value is true for all T_i in Types.<br />
* For <code>(2)</code>, std::is_move_assignable&lt;T_i&gt;::value is true for all T_i in Types.<br />
* For <code>(3)</code>, sizeof&#8230;(UTypes) == sizeof&#8230;(Types) and std::is_assignable&lt;T_i&amp;, const U_i&amp;&gt;::value is true for all corresponding pairs of types T_i in Types and U_i in UTypes. <i>(until C++17)</i><br />
* For <code>(4)</code>, sizeof&#8230;(UTypes) == sizeof&#8230;(Types) and std::is_assignable&lt;T_i&amp;, U_i&amp;&amp;&gt;::value is true for all corresponding pairs of types T_i in Types and U_i in UTypes.<br />
* For <code>(5)</code>, sizeof&#8230;(Types) == 2 and std::is_assignable&lt;T_0&amp;, const U1&amp;&gt;::value and std::is_assignable&lt;T_1&amp;, const U2&amp;&gt;::value are both true, where T_0 and T_1 are the two types constituting Types.<br />
* For <code>(6)</code>, sizeof&#8230;(Types) == 2 and std::is_assignable&lt;T_0&amp;, U1&amp;&amp;&gt;::value and std::is_assignable&lt;T_1&amp;, U2&amp;&amp;&gt;::value are both true, where T_0 and T_1 are the two types constituting Types.<br />
These functions do not participate in overload resolution (or, for the copy assignment operator, is defined as deleted) if any required assignment operation is invalid or if there is a size mismatch. Specifically:<br />
* <code>(1)</code> is defined as deleted unless std::is_copy_assignable&lt;T_i&gt;::value is true for all T_i in Types.<br />
* <code>(2)</code> does not participate in overload resolution unless std::is_move_assignable&lt;T_i&gt;::value is true for all T_i in Types.<br />
* <code>(3)</code> does not participate in overload resolution unless sizeof&#8230;(UTypes) == sizeof&#8230;(Types) and std::is_assignable&lt;T_i&amp;, const U_i&amp;&gt;::value is true for all corresponding pairs of types T_i in Types and U_i in UTypes. <i>(since C++17)</i><br />
* <code>(4)</code> does not participate in overload resolution unless sizeof&#8230;(UTypes) == sizeof&#8230;(Types) and std::is_assignable&lt;T_i&amp;, U_i&amp;&amp;&gt;::value is true for all corresponding pairs of types T_i in Types and U_i in UTypes.<br />
* <code>(5)</code> does not participate in overload resolution unless sizeof&#8230;(Types) == 2, std::is_assignable&lt;T_0&amp;, const U1&amp;&gt;::value and std::is_assignable&lt;T_1&amp;, const U2&amp;&gt;::value are both true, where T_0 and T_1 are the two types constituting Types.<br />
* <code>(6)</code> does not participate in overload resolution unless std::is_assignable&lt;T_0&amp;, U1&amp;&amp;&gt;::value and std::is_assignable&lt;T_1&amp;, U2&amp;&amp;&gt;::value are both true, where T_0 and T_1 are the two types constituting Types. </p>
<h2>Parameters</h2>
<p>other &#8211; tuple to replace the contents of this tuple<br />
p &#8211; pair to replace the contents of this 2-tuple</p>
<h2>Return value</h2>
<p>*this </p>
<h2>Exceptions</h2>
<p>1) <i>(none)</i><br />
2)<br />
noexcept specification:<br />
noexcept(<br />
is_nothrow_move_assignable&lt;T0&gt;::value &amp;&amp;<br />
is_nothrow_move_assignable&lt;T1&gt;::value &amp;&amp;<br />
is_nothrow_move_assignable&lt;T2&gt;::value &amp;&amp;<br />
&#8230;<br />
)<br />
3-6) <i>(none)</i></p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
<h2>See also</h2>
