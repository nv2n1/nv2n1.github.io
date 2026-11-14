---
title: "stdtupletuple(3)"
name: "stdtupletuple"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdtupletuple/"
description: "std::tuple<Types…>::tuple – std::tuple<Types…>::tuple"
---

<p>std::tuple&lt;Types&#8230;&gt;::tuple &#8211; std::tuple&lt;Types&#8230;&gt;::tuple</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;tuple&gt;

    constexpr tuple();
(1)(since C++ 11)(conditionally explicit)(since C++ 11)

    tuple(const Types &amp;...args);
(2)(constexpr since C++ 14)(conditionally explicit)

    template &lt;class... UTypes&gt;
    (since C++ 11)

        tuple(UTypes &amp;&amp;...args);
(3)(constexpr since C++ 14)(conditionally explicit)

    template &lt;class... UTypes&gt;
    (since C++ 11)

        tuple(const tuple&lt;UTypes...&gt; &amp;other);
(4)(constexpr since C++ 14)(conditionally explicit)

    template &lt;class... UTypes&gt;
    (since C++ 11)

        tuple(tuple&lt;UTypes...&gt; &amp;&amp;other);
(5)(constexpr since C++ 14)(conditionally explicit)

    template &lt;class U1, class U2&gt;
    (since C++ 11)

        tuple(const pair&lt;U1, U2&gt; &amp;p);
(6)(constexpr since C++ 14)(conditionally explicit)

    template &lt;class U1, class U2&gt;
    (since C++ 11)

        tuple(pair&lt;U1, U2&gt; &amp;&amp;p);
(7)(constexpr since C++ 14)(conditionally explicit)

    tuple(const tuple &amp;other) = default;
(8)(since C++ 11)

    tuple(tuple &amp;&amp;other) = default;
(9)(since C++ 11)

    template &lt;class Alloc&gt;
    (10)(since C++ 11)

        tuple(std::allocator_arg_t, const Alloc &amp;a);
(constexpr since C++ 20)

    template &lt;class Alloc&gt;
    (since C++ 11)

        tuple(std::allocator_arg_t, const Alloc &amp;a, (11)(constexpr since C++ 20)

                                                        const Types &amp;...args);
(conditionally explicit)

    template &lt;class Alloc, class... UTypes&gt;
    (since C++ 11)

        tuple(std::allocator_arg_t, const Alloc &amp;a, (12)(constexpr since C++ 20)

                                                        UTypes &amp;&amp;...args);
(conditionally explicit)

    template &lt;class Alloc, class... UTypes&gt;
    (since C++ 11)

        tuple(std::allocator_arg_t, const Alloc &amp;a, (13)(constexpr since C++ 20)

                                                        const tuple&lt;UTypes...&gt; &amp;other);
(conditionally explicit)

    template &lt;class Alloc, class... UTypes&gt;
    (since C++ 11)

        tuple(std::allocator_arg_t, const Alloc &amp;a, (14)(constexpr since C++ 20)

                                                        tuple&lt;UTypes...&gt; &amp;&amp;other);
(conditionally explicit)

    template &lt;class Alloc, class U1, class U2&gt;
    (since C++ 11)

        tuple(std::allocator_arg_t, const Alloc &amp;a, (15)(constexpr since C++ 20)

                                                        const pair&lt;U1, U2&gt; &amp;p);
(conditionally explicit)

    template &lt;class Alloc, class U1, class U2&gt;
    (since C++ 11)

        tuple(std::allocator_arg_t, const Alloc &amp;a, (16)(constexpr since C++ 20)

                                                        pair&lt;U1, U2&gt; &amp;&amp;p);
(conditionally explicit)

    template &lt;class Alloc&gt;
    (since C++ 11)

        tuple(std::allocator_arg_t, const Alloc &amp;a, (17)(constexpr since C++ 20)

                                                        const tuple &amp;other);

template &lt;class Alloc&gt;
(since C++ 11)

    tuple(std::allocator_arg_t, const Alloc &amp;a, (18)(constexpr since C++ 20)

                                                    tuple &amp;&amp;other);</code></pre>
<p>Constructs a new tuple.<br />
1) Default constructor. Value-initializes all elements.<br />
This overload only participates in overload resolution if std::is_default_constructible&lt;Ti&gt;::value is true for all i<br />
The constructor is explicit if and only if Ti is not implicitly default-constructible for at least one i.<br />
2) Direct constructor. Initializes each element of the tuple with the corresponding parameter.<br />
This overload only participates in overload resolution if sizeof&#8230;(Types) &gt;= 1 and std::is_copy_constructible&lt;Ti&gt;::value is true for all i.<br />
This constructor is explicit if and only if std::is_convertible&lt;const Ti&amp;, Ti&gt;::value is false for at least one i.<br />
3) Converting constructor. Initializes each element of the tuple with the corresponding value in std::forward&lt;UTypes&gt;(args).<br />
This overload only participates in overload resolution if sizeof&#8230;(Types) == sizeof&#8230;(UTypes) and sizeof&#8230;(Types) &gt;= 1 and std::is_constructible&lt;Ti, Ui&amp;&amp;&gt;::value is true for all i.<br />
The constructor is explicit if and only if std::is_convertible&lt;Ui&amp;&amp;, Ti&gt;::value is false for at least one i.<br />
4) Converting copy-constructor. For all i in sizeof&#8230;(UTypes), initializes ith element of the tuple with std::get&lt;i&gt;(other).<br />
This overload only participates in overload resolution if<br />
sizeof&#8230;(Types) == sizeof&#8230;(UTypes) and<br />
std::is_constructible_v&lt;Ti, const Ui&amp;&gt; is true for all i and<br />
sizeof&#8230;(Types) != 1 or<br />
(when Types&#8230; expands to T and UTypes&#8230; expands to U) std::is_convertible_v&lt;const tuple&lt;U&gt;&amp;, T&gt;, std::is_constructible_v&lt;T, const tuple&lt;U&gt;&amp;&gt;, and std::is_same_v&lt;T, U&gt; are all false .<br />
The constructor is explicit if and only if std::is_convertible&lt;const Ui&amp;, Ti&gt;::value is false for at least one i.<br />
5) Converting move-constructor. For all i in sizeof&#8230;(UTypes), initializes ith element of the tuple with std::forward&lt;Ui&gt;(std::get&lt;i&gt;(other)).<br />
This overload only participates in overload resolution if<br />
sizeof&#8230;(Types) == sizeof&#8230;(UTypes) and<br />
std::is_constructible_v&lt;Ti, Ui&amp;&amp;&gt; is true for all i and<br />
sizeof&#8230;(Types) != 1 or<br />
(when Types&#8230; expands to T and UTypes&#8230; expands to U) std::is_convertible_v&lt;tuple&lt;U&gt;, T&gt;, std::is_constructible_v&lt;T, tuple&lt;U&gt;&gt;, and std::is_same_v&lt;T, U&gt; are all false .<br />
The constructor is explicit if and only if std::is_convertible&lt;Ui&amp;&amp;, Ti&gt;::value is false for at least one i.<br />
6) Pair copy constructor. Constructs a 2-element tuple with the first element constructed from p.first and the second element from p.second<br />
This overload only participates in overload resolution if sizeof&#8230;(Types) == 2 and std::is_constructible&lt;T0,const U1&amp;&gt;::value and std::is_constructible&lt;T1, const U2&amp;&gt;::value are both true<br />
The constructor is explicit if and only if std::is_convertible&lt;const U1&amp;, T0&gt;::value or std::is_convertible&lt;const U2&amp;, T1&gt;::value is false.<br />
7) Pair move constructor. Constructs a 2-element tuple with the first element constructed from std::forward&lt;U1&gt;(p.first) and the second element from std::forward&lt;U2&gt;(p.second)<br />
This overload only participates in overload resolution if sizeof&#8230;(Types) == 2 and std::is_constructible&lt;T0, U1&amp;&amp;&gt;::value and std::is_constructible&lt;T1, U2&amp;&amp;&gt;::value are both true<br />
The constructor is explicit if and only if std::is_convertible&lt;U1&amp;&amp;, T0&gt;::value or std::convertible&lt;U2&amp;&amp;, T1&gt;::value is false.<br />
8) Implicitly-defined copy constructor. Initializes each element of the tuple with the corresponding element of other.<br />
This constructor is constexpr if every operation it performs is constexpr. For the empty tuple std::tuple&lt;&gt;, it is constexpr.<br />
Requires that std::is_copy_constructible&lt;Ti&gt;::value is true for all i.<br />
9) Implicitly-defined move constructor. Initializes each ith element of the tuple with std::forward&lt;Ui&gt;(std::get&lt;i&gt;(other)).<br />
This constructor is constexpr if every operation it performs is constexpr. For the empty tuple std::tuple&lt;&gt;, it is constexpr.<br />
Requires that std::is_move_constructible&lt;Ti&gt;::value is true for all i.<br />
10-18) Identical to (1-9) except each element is created by uses-allocator_construction, that is, the Allocator object a is passed as an additional argument to the constructor of each element for which std::uses_allocator&lt;Ui, Alloc&gt;::value is true. </p>
<h2>Parameters</h2>
<p>args &#8211; values used to initialize each element of the tuple<br />
other &#8211; a tuple of values used to initialize each element of the tuple<br />
p &#8211; pair of values used to initialize both elements of this 2-tuple<br />
a &#8211; allocator to use in uses-allocator construction</p>
<h2>Notes</h2>
<p>Conditionally-explicit constructors make it possible to construct a tuple in copy-initialization context using list-initialization syntax:<br />
Note that if some element of the list is not implicitly convertible to the corresponding element of the target tuple, the constructors become explicit: using namespace std::chrono;</p>
<p>void launch_rocket_at(std::tuple&lt;hours, minutes, seconds&gt;);<br />
&nbsp;<wbr>&nbsp;launch_rocket_at({<a href="/docs/linux/man/1-hours/">hours</a><code>(1)</code>, <a href="/docs/linux/man/2-minutes/">minutes</a><code>(2)</code>, <a href="/docs/linux/man/3-seconds/">seconds</a><code>(3)</code>}); // OK<br />
&nbsp;<wbr>&nbsp;launch_rocket_at({1, 2, 3}); // Error: int is not implicitly convertible to duration<br />
&nbsp;<wbr>&nbsp;launch_rocket_at(std::tuple&lt;hours, minutes, seconds&gt;{1, 2, 3}); // OK<br />
Defect reports<br />
The following behavior-changing defect reports were applied retroactively to previously published C++ standards.<br />
DR Applied to Behavior as published Correct behavior<br />
N4387 C++11 some constructors were explicit, preventing useful behavior most constructors made conditionally-explicit<br />
LWG_2510 C++11 default constructor was implicit made conditionally-explicit </p>
<h2>Example</h2>
<p>// Run this code #include &lt;iostream&gt;</p>
<p>#include &lt;string&gt;</p>
<p>#include &lt;vector&gt;</p>
<p>#include &lt;tuple&gt;</p>
<p>#include &lt;memory&gt;<br />
// helper function to print a tuple of any size</p>
<p>template &lt;class Tuple, std::size_t N&gt;</p>
<p>struct TuplePrinter {<br />
    static void print(const Tuple &amp;t)<br />
    {<br />
        TuplePrinter&lt;Tuple, N &#8211; 1&gt;::print(t);<br />
        std::cout &lt;&lt; &quot;, &quot; &lt;&lt; std::get&lt;N &#8211; 1&gt;(t);<br />
    }<br />
};<br />
template &lt;class Tuple&gt;</p>
<p>struct TuplePrinter&lt;Tuple, 1&gt; {<br />
    static void print(const Tuple &amp;t)<br />
    {<br />
        std::cout &lt;&lt; std::get&lt;0&gt;(t);<br />
    }<br />
};<br />
&nbsp;<wbr>&nbsp;template&lt;class&#8230; Args&gt;<br />
&nbsp;<wbr>&nbsp;void print(const std::tuple&lt;Args&#8230;&gt;&amp; t)<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::cout &lt;&lt; &quot;(&quot;;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;TuplePrinter&lt;decltype(t), sizeof&#8230;(Args)&gt;::print(t);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::cout &lt;&lt; &quot;)
&quot;;<br />
&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;// end helper function </p>
<pre><code>int main()

{
    std::tuple&lt;int, std::string, double&gt; t1;
    std::cout &lt;&lt; &quot;Value-initialized: &quot;;
    print(t1);
    std::tuple&lt;int, std::string, double&gt; t2(42, &quot;Test&quot;, -3.14);
    std::cout &lt;&lt; &quot;Initialized with values: &quot;;
    print(t2);
    std::tuple&lt;char, std::string, int&gt; t3(t2);
    std::cout &lt;&lt; &quot;Implicitly converted: &quot;;
    print(t3);
    std::tuple&lt;int, double&gt; t4(std::make_pair(42, 3.14));
    std::cout &lt;&lt; &quot;Constructed from a pair&quot;;
    print(t4);
    // given Allocator my_alloc with a single-argument constructor my_alloc(int)
    // use my_alloc(1) to allocate 10 ints in a vector
    std::vector&lt;int, my_alloc&gt; v(10, 1, my_alloc(1));
    // use my_alloc(2) to allocate 10 ints in a vector in a tuple
    std::tuple&lt;int, std::vector&lt;int, my_alloc&gt;, double&gt; t5(std::allocator_arg,
                                                           my_alloc(2), 42, v, -3.14);
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;Value-initialized: (0, , 0)<br />
&nbsp;<wbr>&nbsp;Initialized with values: (42, Test, -3.14)<br />
&nbsp;<wbr>&nbsp;Implicitly converted: (*, Test, -3)<br />
&nbsp;<wbr>&nbsp;Constructed from a pair(42, 3.14)</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a tuple object of the type defined by the argument types<br />
make_tuple <i>(function template)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a tuple of lvalue references or unpacks a tuple into individual objects<br />
tie <i>(function template)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a tuple of rvalue references<br />
forward_as_tuple <i>(function template)</i> </p>
