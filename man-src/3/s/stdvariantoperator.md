---
title: "stdvariantoperator(3)"
name: "stdvariantoperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdvariantoperator/"
---

std::variant&lt;Types...&gt;::operator= - std::variant&lt;Types...&gt;::operator=

<h2>Synopsis</h2>

<pre><code>constexpr variant &amp;operator=(const variant &amp;rhs);
(1)(since C++ 17)

    constexpr variant &amp;
    operator=(variant &amp;&amp;rhs) noexcept(/* see below */);
(2)(since C++ 17)

    template &lt;class T&gt;
    variant &amp;operator=(T &amp;&amp;t) noexcept(/* see below */);
(3)(since C++ 17)</code></pre> 
Assigns a new value to an existing variant object. 
1) Copy-assignment: * If both *this and rhs are valueless by exception, does nothing.

* Otherwise, if rhs is valueless, but *this is not, destroys the value contained in *this and makes it valueless.

* Otherwise, if rhs holds the same alternative as *this, assigns the value contained in rhs to the value contained in *this. If an exception is thrown, *this does not become valueless: the value depends on the exception safety guarantee of the alternative's copy assignment.

* Otherwise, if the alternative held by rhs is either nothrow copy constructible or not nothrow move constructible (as determined by std::is_nothrow_copy_constructible and std::is_nothrow_move_constructible, respectively), equivalent to this-&gt;emplace&lt;rhs.index()&gt;(get&lt;rhs.index()&gt;(rhs)).

* Otherwise, equivalent to this-&gt;operator=(variant(rhs)). Note that *this may become valueless_by_exception as described in (2). 
This overload is defined as deleted unless std::is_copy_constructible_v&lt;T_i&gt; and std::is_copy_assignable_v&lt;T_i&gt; are both true for all T_i in Types.... This overload is trivial if std::is_trivially_copy_constructible_v&lt;T_i&gt;,std::is_trivially_copy_assignable_v&lt;T_i&gt; and std::is_trivially_destructible_v&lt;T_i&gt; are all true for all T_i in Types.... 
2) Move-assignment: 
* If both *this and rhs are valueless by exception, does nothing 
* Otherwise, if rhs is valueless, but *this is not, destroys the value contained in *this and makes it valueless 
* Otherwise, if rhs holds the same alternative as *this, assigns std::get&lt;j&gt;(std::move(rhs)) to the value contained in *this, with j being index(). If an exception is thrown, *this does not become valueless: the value depends on the exception safety guarantee of the alternative's move assignment. 
* Otherwise (if rhs and *this hold different alternatives), equivalent to this-&gt;emplace&lt;rhs.index()&gt;(get&lt;rhs.index()&gt;(std::move(rhs))). If an exception is thrown by T_i's move constructor, *this becomes valueless_by_exception. 
This overload only participates in overload resolution if std::is_move_constructible_v&lt;T_i&gt; and std::is_move_assignable_v&lt;T_i&gt; are both true for all T_i in Types.... This overload is trivial if std::is_trivially_move_constructible_v&lt;T_i&gt;, std::is_trivially_move_assignable_v&lt;T_i&gt;, and std::is_trivially_destructible_v&lt;T_i&gt; are all true for all T_i in Types.... 
3) Converting assignment. 
* Determines the alternative type T_j that would be selected by overload resolution for the expression F(std::forward&lt;T&gt;(t)) if there was an overload of imaginary function F(T_i) for every T_i from Types... in scope at the same time, except that: *An overload F(T_i)
is only considered if the declaration T_i x[] = {std::forward&lt;T&gt;(t)}; is valid for some invented variable x;
*If T_i is(possibly cv - qualified) bool, F(T_i) is only considered if std : remove_cvref_t&lt;T&gt; is also bool.

                                                                                 *If *this already holds a T_j,
    assigns std::forward&lt;T&gt;(t) to the value contained in *this.If an exception is thrown, *this does not become valueless : the value depends on the exception safety guarantee of the assignment called.

                                                                                              * Otherwise,
    if std::is_nothrow_constructible_v&lt;T_j, T&gt; || !std::is_nothrow_move_constructible_v&lt;T_j&gt; is true, equivalent to this-&gt;emplace&lt;j&gt;(std::forward&lt;T&gt;(t));

*Otherwise, equivalent to this-&gt;operator=(variant(std::forward&lt;T&gt;(t))). 
This overload only participates in overload resolution if 
std::decay_t&lt;T&gt; 
<i>(until C++20)</i> 
std::remove_cvref_t&lt;T&gt; 
<i>(since C++20)</i> is not the same type as variant and std::is_assignable_v&lt;T_j&amp;, T&gt; is true and std::is_constructible_v&lt;T_j, T&gt; is true and the expression F(std::forward&lt;T&gt;(t)) (with F being the above-mentioned set of imaginary functions) is well formed. <pre><code>std::variant&lt;string&gt; v1;

v1 = &quot;abc&quot;; // OK

std::variant&lt;std::string, std::string&gt; v2;

v2 = &quot;abc&quot;; // Error

std::variant &lt;std::string, bool&gt; v3;

v3 = &quot;abc&quot;; // OK, chooses string; bool is not a candidate

std::variant&lt;float, long, double&gt; v4; //holds float

v4 = 0; // OK, holds long; float and double are not candidates

</code></pre>

<h2>Parameters</h2>

rhs - another variant 
t - a value convertible to one of the variant's alternatives

<h2>Return value</h2>

*this 

<h2>Exceptions</h2>

1) May throw any exception thrown by assignment and copy/move initialization of any alternative 
2) 
noexcept specification: 
noexcept(((std::is_nothrow_move_constructible_v&lt;Types&gt; &amp;&amp; std::is_nothrow_move_assignable_v&lt;Types&gt;) &amp;&amp; ...)) 
3) 
noexcept specification: 
noexcept(std::is_nothrow_assignable_v&lt;T_j&amp;, T&gt; &amp;&amp; std::is_nothrow_constructible_v&lt;T_j, T&gt;)

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 
Defect reports 
The following behavior-changing defect reports were applied retroactively to previously published C++ standards. 
DR Applied to Behavior as published Correct behavior 
LWG_3024 C++17 copy assignment operator doesn't participate in overload resolution if any member type is not copyable defined as deleted instead 
P0602R4 C++17 copy/move assignment may not be trivial even if underlying operations are trivial required to propagate triviality 
P0608R3 C++17 converting assignment blindly assembles an overload set, leading to unintended conversions narrowing and boolean conversions not considered 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a value in the variant, in place 
emplace <i>(public member function)</i> 
