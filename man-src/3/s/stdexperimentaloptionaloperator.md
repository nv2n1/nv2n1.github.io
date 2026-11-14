---
title: "stdexperimentaloptionaloperator(3)"
name: "stdexperimentaloptionaloperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentaloptionaloperator/"
description: "std::experimental::optional<T>::operator= – std::experimental::optional<T>::operator="
---

<p>std::experimental::optional&lt;T&gt;::operator= &#8211; std::experimental::optional&lt;T&gt;::operator=</p>
<h2>Synopsis</h2>
<pre><code>optional &amp;operator=(std::experimental::nullopt_t) noexcept;
(1)(library fundamentals TS)

    optional &amp;
    operator=(const optional &amp;other);
(2)(library fundamentals TS)

    optional &amp;
    operator=(optional &amp;&amp;other) noexcept(/* see below */);
(3)(library fundamentals TS)

    template &lt;class U&gt;
    (4)(library fundamentals TS)

        optional &amp;
        operator=(U &amp;&amp;value);</code></pre>
<p>Replaces contents of *this with the contents of other<br />
1) If *this contains a value before the call, the contained value is destroyed by calling its destructor as if by val-&gt;T::~T(). *this does not contain a value after this call.<br />
2-3) Assigns the state of other.<br />
* If both *this and other do not contain a value, the function has no effect.<br />
* If *this contains a value, but other does not, then the contained value is destroyed by calling its destructor. *this does not contain a value after the call.<br />
* If other contains a value, then depending on whether *this contains a value, the contained value is either direct-initialized or assigned from *other <code>(2)</code> or std::move(*other) <code>(3)</code>. Note that a moved-from optional still contains a value.<br />
4) Decay-only perfect-forwarded assignment: depending on whether *this contains a value before the call, the contained value is either direct-initialized from std::forward&lt;U&gt;(value) or assigned from std::forward&lt;U&gt;(value). The function does not participate in overload resolution unless std::is_same&lt;std::decay_t&lt;U&gt;, T&gt;::value is true. </p>
<h2>Parameters</h2>
<p>other &#8211; another optional object whose contained value to assign<br />
value &#8211; value to assign to the contained value</p>
<h2>Type requirements</h2>
<p>&#8211;<br />
T must meet the requirements of CopyAssignable and CopyConstructible in order to use overload <code>(2)</code>.<br />
&#8211;<br />
T must meet the requirements of MoveAssignable and MoveConstructible in order to use overload <code>(3)</code>.</p>
<h2>Return value</h2>
<p>*this </p>
<h2>Exceptions</h2>
<p>2-4) Throws any exception thrown by the constructor or assignment operator of T. If an exception is thrown, the initialization state of *this (and of other in case of <code>(2)</code> ) is unchanged, i.e. if the object contained a value, it still contains a value, and the other way round. The contents of value and the contained values of *this and other depend on the exception safety guarantees of the operation from which the exception originates (copy-constructor, move-assignment, etc.).<br />
<code>(3)</code> has the following noexcept declaration:<br />
noexcept specification:<br />
noexcept(std::is_nothrow_move_assignable&lt;T&gt;::value &amp;&amp; std::is_nothrow_move_constructible&lt;T&gt;::value)</p>
<h2>Notes</h2>
<p>An optional object op may be turned into an empty optional with both op = {}; and op = nullopt;. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;experimental/optional&gt;

#include &lt;iostream&gt;

int main()

{
    std::experimental::optional&lt;const char *&gt; s1 = &quot;abc&quot;, s2; // constructor
    s2 = s1;                                                  // assignment
    s1 = &quot;def&quot;;                                               // decaying assignment (U = char[4], T = const char*)
    std::cout &lt;&lt; *s2 &lt;&lt; ' ' &lt;&lt; *s1 &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;abc def</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs the contained value in-place<br />
emplace <i>(public member function)</i> </p>
