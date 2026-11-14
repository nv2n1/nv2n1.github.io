---
title: "stdoptionaloperator(3)"
name: "stdoptionaloperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdoptionaloperator/"
description: "std::optional<T>::operator= – std::optional<T>::operator="
---

<p>std::optional&lt;T&gt;::operator= &#8211; std::optional&lt;T&gt;::operator=</p>
<h2>Synopsis</h2>
<pre><code>optional &amp;operator=(std::nullopt_t) noexcept;
(1)(since C++ 17)

    constexpr optional &amp;
    operator=(const optional &amp;other);
(2)(since C++ 17)

    constexpr optional &amp;
    operator=(optional &amp;&amp;other) noexcept(/* see below */);
(3)(since C++ 17)

    template &lt;class U = T&gt;
    (4)(since C++ 17)

        optional &amp;
        operator=(U &amp;&amp;value);

template &lt;class U&gt;
(5)(since C++ 17)

    optional &amp;
    operator=(const optional&lt;U&gt; &amp;other);

template &lt;class U&gt;
(6)(since C++ 17)

    optional &amp;
    operator=(optional&lt;U&gt; &amp;&amp;other);</code></pre>
<p>Replaces contents of *this with the contents of other<br />
1) If *this contains a value before the call, the contained value is destroyed by calling its destructor as if by value().T::~T(). *this does not contain a value after this call.<br />
2-3) Assigns the state of other.<br />
* If both *this and other do not contain a value, the function has no effect.<br />
* If *this contains a value, but other does not, then the contained value is destroyed by calling its destructor. *this does not contain a value after the call.<br />
* If other contains a value, then depending on whether *this contains a value, the contained value is either direct-initialized or assigned from *other <code>(2)</code> or std::move(*other) <code>(3)</code>. Note that a moved-from optional still contains a value.<br />
* Overload <code>(2)</code> is defined as deleted unless std::is_copy_constructible_v&lt;T&gt; and std::is_copy_assignable_v&lt;T&gt; are both true. It is trivial if std::is_trivially_copy_constructible_v&lt;T&gt;, std::is_trivially_copy_assignable_v&lt;T&gt; and std::is_trivially_destructible_v&lt;T&gt; are all true.<br />
* Overload <code>(3)</code> does not participate in overload resolution unless std::is_move_constructible_v&lt;T&gt; and std::is_move_assignable_v&lt;T&gt; are both true. It is trivial if std::is_trivially_move_constructible_v&lt;T&gt;, std::is_trivially_move_assignable_v&lt;T&gt; and std::is_trivially_destructible_v&lt;T&gt; are all true.<br />
4) Perfect-forwarded assignment: depending on whether *this contains a value before the call, the contained value is either direct-initialized from std::forward&lt;U&gt;(value) or assigned from std::forward&lt;U&gt;(value). The function does not participate in overload resolution unless<br />
std::decay_t&lt;U&gt;<br />
<i>(until C++20)</i><br />
std::remove_cvref_t&lt;U&gt;<br />
<i>(since C++20)</i> is not std::optional&lt;T&gt;, std::is_constructible_v&lt;T, U&gt; is true, std::is_assignable_v&lt;T&amp;, U&gt; is true, and at least one of the following is true:<br />
* T is not a scalar_type;<br />
* std::decay_t&lt;U&gt; is not T.<br />
5-6) Assigns the state of other.<br />
* If both *this and other do not contain a value, the function has no effect.<br />
* If *this contains a value, but other does not, then the contained value is destroyed by calling its destructor. *this does not contain a value after the call.<br />
* If other contains a value, then depending on whether *this contains a value, the contained value is either direct-initialized or assigned from *other <code>(5)</code> or std::move(*other) <code>(6)</code>. Note that a moved-from optional still contains a value.<br />
* These overloads do not participate in overload resolution unless the following conditions are met:<br />
&nbsp;<wbr>&nbsp;o T is not constructible, convertible, or assignable from any expression of type (possibly const) std::optional&lt;U&gt;, i.e., the following 12 type traits are all false:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;# std::is_constructible_v&lt;T, std::optional&lt;U&gt;&amp;&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;# std::is_constructible_v&lt;T, const std::optional&lt;U&gt;&amp;&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;# std::is_constructible_v&lt;T, std::optional&lt;U&gt;&amp;&amp;&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;# std::is_constructible_v&lt;T, const std::optional&lt;U&gt;&amp;&amp;&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;# std::is_convertible_v&lt;std::optional&lt;U&gt;&amp;, T&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;# std::is_convertible_v&lt;const std::optional&lt;U&gt;&amp;, T&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;# std::is_convertible_v&lt;std::optional&lt;U&gt;&amp;&amp;, T&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;# std::is_convertible_v&lt;const std::optional&lt;U&gt;&amp;&amp;, T&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;# std::is_assignable_v&lt;T&amp;, std::optional&lt;U&gt;&amp;&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;# std::is_assignable_v&lt;T&amp;, const std::optional&lt;U&gt;&amp;&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;# std::is_assignable_v&lt;T&amp;, std::optional&lt;U&gt;&amp;&amp;&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;# std::is_assignable_v&lt;T&amp;, const std::optional&lt;U&gt;&amp;&amp;&gt;.<br />
&nbsp;<wbr>&nbsp;o For overload <code>(5)</code>, std::is_constructible_v&lt;T, const U&amp;&gt; and std::is_assignable_v&lt;T&amp;, const U&amp;&gt; are both true.<br />
&nbsp;<wbr>&nbsp;o For overload <code>(6)</code>, std::is_constructible_v&lt;T, U&gt; and std::is_assignable_v&lt;T&amp;, U&gt; are both true. </p>
<h2>Parameters</h2>
<p>other &#8211; another optional object whose contained value to assign<br />
value &#8211; value to assign to the contained value</p>
<h2>Return value</h2>
<p>*this </p>
<h2>Exceptions</h2>
<p>2-6) Throws any exception thrown by the constructor or assignment operator of T. If an exception is thrown, the initialization state of *this (and of other in case of (2-3) and (5-6) ) is unchanged, i.e. if the object contained a value, it still contains a value, and the other way round. The contents of value and the contained values of *this and other depend on the exception safety guarantees of the operation from which the exception originates (copy-constructor, move-assignment, etc.).<br />
<code>(3)</code> has the following<br />
noexcept specification:<br />
noexcept(std::is_nothrow_move_assignable&lt;T&gt;::value &amp;&amp; std::is_nothrow_move_constructible&lt;T&gt;::value)</p>
<h2>Notes</h2>
<p>An optional object op may be turned into an empty optional with both op = {}; and op = nullopt;. The first expression constructs an empty optional object with {} and assigns it to op. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;optional&gt;

#include &lt;iostream&gt;

int main()

{
    std::optional&lt;const char *&gt; s1 = &quot;abc&quot;, s2; // constructor
    s2 = s1;                                    // assignment
    s1 = &quot;def&quot;;                                 // decaying assignment (U = char[4], T = const char*)
    std::cout &lt;&lt; *s2 &lt;&lt; ' ' &lt;&lt; *s1 &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;abc def </p>
<p>Defect reports </p>
<p>The following behavior-changing defect reports were applied retroactively to previously published C++ standards. </p>
<p>DR Applied to Behavior as published Correct behavior<br />
P0602R4 C++17 copy/move assignment operator may not be trivial even if underlying operations are trivial required to propagate triviality</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs the contained value in-place<br />
emplace <i>(public member function)</i> </p>
