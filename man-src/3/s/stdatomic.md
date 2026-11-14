---
title: "stdatomic(3)"
name: "stdatomic"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatomic/"
description: "std::atomic – std::atomic"
---

<p>std::atomic &#8211; std::atomic</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;atomic&gt;

    template &lt;class T&gt;
    (1)(since C++ 11)

        struct atomic;

template &lt;class T&gt;
(2)(since C++ 11)

    struct atomic&lt;T *&gt;;

Defined in header&lt;memory&gt;

    template &lt;class T&gt;
    (3)(since C++ 20)

        struct atomic&lt;std::shared_ptr&lt;T&gt;&gt;;

template &lt;class T&gt;
(4)(since C++ 20)

    struct atomic&lt;std::weak_ptr&lt;T&gt;&gt;;</code></pre>
<p>Each instantiation and full specialization of the std::atomic template defines an atomic type. If one thread writes to an atomic object while another thread reads from it, the behavior is well-defined (see memory_model for details on data races)<br />
In addition, accesses to atomic objects may establish inter-thread synchronization and order non-atomic memory accesses as specified by std::memory_order.<br />
std::atomic is neither copyable nor movable. </p>
<h2>Specializations</h2>
<p>Primary template </p>
<p>The primary std::atomic template may be instantiated with any TriviallyCopyable type T satisfying both CopyConstructible and CopyAssignable. The program is ill-formed if any of following values is false: </p>
<p>* std::is_trivially_copyable&lt;T&gt;::value<br />
* std::is_copy_constructible&lt;T&gt;::value<br />
* std::is_move_constructible&lt;T&gt;::value<br />
* std::is_copy_assignable&lt;T&gt;::value<br />
* std::is_move_assignable&lt;T&gt;::value </p>
<p>&nbsp;<wbr>&nbsp;struct Counters { int a; int b; }; // user-defined trivially-copyable type<br />
&nbsp;<wbr>&nbsp;std::atomic&lt;Counters&gt; cnt; // specialization for the user-defined type </p>
<p>std::atomic&lt;bool&gt; uses the primary template. It is guaranteed to be a standard layout struct. </p>
<p>Partial specializations </p>
<p>The standard library provides partial specializations of the std::atomic template for the following types with additional properties that the primary template does not have:<br />
2) Partial specializations std::atomic&lt;T*&gt; for all pointer types. These specializations have standard layout, trivial default constructors, and trivial destructors. Besides the operations provided for all atomic types, these specializations additionally support atomic arithmetic operations appropriate to pointer types, such as fetch_add, fetch_sub. </p>
<p>3-4) Partial specializations std::atomic&lt;std::shared_ptr&lt;T&gt;&gt; and std::atomic&lt;std::weak_ptr&lt;T&gt;&gt; are provided for std::shared_ptr and std::weak_ptr. <i>(since C++20)</i><br />
See std::atomic&lt;std::shared_ptr&gt; and std::atomic&lt;std::weak_ptr&gt; for details. </p>
<p>Specializations for integral types </p>
<p>When instantiated with one of the following integral types, std::atomic provides additional atomic operations appropriate to integral types such as fetch_add, fetch_sub, fetch_and, fetch_or, fetch_xor: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* The character types char<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;, char8_t<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++20)</i>, char16_t, char32_t, and wchar_t;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* The standard signed integer types: signed char, short, int, long, and long long;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* The standard unsigned integer types: unsigned char, unsigned short, unsigned int, unsigned long, and unsigned long long;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* Any additional integral types needed by the typedefs in the header &lt;cstdint&gt;. </p>
<p>Additionally, the resulting std::atomic&lt;Integral&gt; specialization has standard layout, a trivial default constructor, and a trivial destructor. Signed integer arithmetic is defined to use two&#8217;s complement; there are no undefined results. </p>
<p>&nbsp;Specializations for floating-point types<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++20)</i><br />
When instantiated with one of the floating-point types float, double, and long double, std::atomic provides additional atomic operations appropriate to floating-point types such as fetch_add and fetch_sub.<br />
Additionally, the resulting std::atomic&lt;Floating&gt; specialization has standard layout, a trivial default constructor, and a trivial destructor.<br />
No operations result in undefined behavior even if the result is not representable in the floating-point type. The floating-point_environment in effect may be different from the calling thread&#8217;s floating-point environment. </p>
<p>Type aliases </p>
<p>Type aliases are provided for bool and all integral types listed above, as follows: </p>
<p>Type alias Definition<br />
std::atomic_bool std::atomic&lt;bool&gt;<br />
std::atomic_char std::atomic&lt;char&gt;<br />
std::atomic_schar std::atomic&lt;signed char&gt;<br />
std::atomic_uchar std::atomic&lt;unsigned char&gt;<br />
std::atomic_short std::atomic&lt;short&gt;<br />
std::atomic_ushort std::atomic&lt;unsigned short&gt;<br />
std::atomic_int std::atomic&lt;int&gt;<br />
std::atomic_uint std::atomic&lt;unsigned int&gt;<br />
std::atomic_long std::atomic&lt;long&gt;<br />
std::atomic_ulong std::atomic&lt;unsigned long&gt;<br />
std::atomic_llong std::atomic&lt;long long&gt;<br />
std::atomic_ullong std::atomic&lt;unsigned long long&gt;<br />
std::atomic_char8_t std::atomic&lt;char8_t&gt; (C++20)<br />
std::atomic_char16_t std::atomic&lt;char16_t&gt;<br />
std::atomic_char32_t std::atomic&lt;char32_t&gt;<br />
std::atomic_wchar_t std::atomic&lt;wchar_t&gt;<br />
std::atomic_int8_t std::atomic&lt;std::int8_t&gt;<br />
std::atomic_uint8_t std::atomic&lt;std::uint8_t&gt;<br />
std::atomic_int16_t std::atomic&lt;std::int16_t&gt;<br />
std::atomic_uint16_t std::atomic&lt;std::uint16_t&gt;<br />
std::atomic_int32_t std::atomic&lt;std::int32_t&gt;<br />
std::atomic_uint32_t std::atomic&lt;std::uint32_t&gt;<br />
std::atomic_int64_t std::atomic&lt;std::int64_t&gt;<br />
std::atomic_uint64_t std::atomic&lt;std::uint64_t&gt;<br />
std::atomic_int_least8_t std::atomic&lt;std::int_least8_t&gt;<br />
std::atomic_uint_least8_t std::atomic&lt;std::uint_least8_t&gt;<br />
std::atomic_int_least16_t std::atomic&lt;std::int_least16_t&gt;<br />
std::atomic_uint_least16_t std::atomic&lt;std::uint_least16_t&gt;<br />
std::atomic_int_least32_t std::atomic&lt;std::int_least32_t&gt;<br />
std::atomic_uint_least32_t std::atomic&lt;std::uint_least32_t&gt;<br />
std::atomic_int_least64_t std::atomic&lt;std::int_least64_t&gt;<br />
std::atomic_uint_least64_t std::atomic&lt;std::uint_least64_t&gt;<br />
std::atomic_int_fast8_t std::atomic&lt;std::int_fast8_t&gt;<br />
std::atomic_uint_fast8_t std::atomic&lt;std::uint_fast8_t&gt;<br />
std::atomic_int_fast16_t std::atomic&lt;std::int_fast16_t&gt;<br />
std::atomic_uint_fast16_t std::atomic&lt;std::uint_fast16_t&gt;<br />
std::atomic_int_fast32_t std::atomic&lt;std::int_fast32_t&gt;<br />
std::atomic_uint_fast32_t std::atomic&lt;std::uint_fast32_t&gt;<br />
std::atomic_int_fast64_t std::atomic&lt;std::int_fast64_t&gt;<br />
std::atomic_uint_fast64_t std::atomic&lt;std::uint_fast64_t&gt;<br />
std::atomic_intptr_t std::atomic&lt;std::intptr_t&gt;<br />
std::atomic_uintptr_t std::atomic&lt;std::uintptr_t&gt;<br />
std::atomic_size_t std::atomic&lt;std::size_t&gt;<br />
std::atomic_ptrdiff_t std::atomic&lt;std::ptrdiff_t&gt;<br />
std::atomic_intmax_t std::atomic&lt;std::intmax_t&gt;<br />
std::atomic_uintmax_t std::atomic&lt;std::uintmax_t&gt; </p>
<p>Note: std::atomic_intN_t, std::atomic_uintN_t, std::atomic_intptr_t, and atomic_uintptr_t are defined if and only if std::intN_t, std::uintN_t, std::intptr_t, and std::uintptr_t are defined, respectively.</p>
<h2>Member types</h2>
<p>Member type Definition<br />
value_type see below<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;value_type (only for atomic&lt;Integral&gt;<br />
difference_type and atomic&lt;Floating&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++20)</i> specializations)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::ptrdiff_t (only for atomic&lt;T*&gt; specializations) </p>
<p>For every std::atomic&lt;X&gt; (whether or not specialized), std::atomic&lt;X&gt;::value_type is X.<br />
difference_type is not defined in the primary atomic template or in the partial specializations for std::shared_ptr and std::weak_ptr.</p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs an atomic object<br />
constructor <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;stores a value into an atomic object<br />
operator= <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if the atomic object is lock-free<br />
is_lock_free <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;atomically replaces the value of the atomic object with a non-atomic argument<br />
store <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;atomically obtains the value of the atomic object<br />
load <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;loads a value from an atomic object<br />
operator_T <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;atomically replaces the value of the atomic object and obtains the value held previously<br />
exchange <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;atomically compares the value of the atomic object with non-atomic argument and performs atomic exchange if equal or atomic load if not<br />
compare_exchange_weak <i>(public member function)</i><br />
compare_exchange_strong</p>
<h2>Constants</h2>
<p>is_always_lock_free indicates that the type is always lock-free<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> <i>(C++17)</i></p>
<h2>Specialized member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;atomically adds the argument to the value stored in the atomic object and obtains the value held previously<br />
fetch_add <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;atomically subtracts the argument from the value stored in the atomic object and obtains the value held previously<br />
fetch_sub <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;atomically performs bitwise AND between the argument and the value of the atomic object and obtains the value held previously<br />
fetch_and <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;atomically performs bitwise OR between the argument and the value of the atomic object and obtains the value held previously<br />
fetch_or <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;atomically performs bitwise XOR between the argument and the value of the atomic object and obtains the value held previously<br />
fetch_xor <i>(public member function)</i> </p>
<p>operator++ increments or decrements the atomic value by one<br />
operator++(int) <i>(public member function)</i><br />
operator&#8211;<br />
operator&#8211;(int) </p>
<p>operator+=<br />
operator-= adds, subtracts, or performs bitwise AND, OR, XOR with the atomic value<br />
operator&amp;= <i>(public member function)</i><br />
operator|=<br />
operator^=</p>
<h2>Notes</h2>
<p>There are non-member function template equivalents for all member functions of std::atomic. Those non-member functions may be additionally overloaded for types that are not specializations of std::atomic, but are able to guarantee atomicity. The only such type in the standard library is std::shared_ptr&lt;T&gt;.<br />
On gcc and clang, some of the functionality described here requires linking against -latomic.<br />
Defect reports<br />
The following behavior-changing defect reports were applied retroactively to previously published C++ standards.<br />
DR Applied to Behavior as published Correct behavior<br />
LWG_2441 C++11 added specializations for the (optional) fixed_width_integer_types<br />
P0558R1 C++11 specification was substantially rewritten to resolve numerous issues<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;in particular, member typedefs value_type and difference_type are added<br />
LWG_3012 C++11 std::atomic&lt;T&gt; was permitted for such specializations are forbidden<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;any T that is trivially copyable but not copyable </p>
<h2>See also</h2>
<p>atomic_flag the lock-free boolean atomic type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i><br />
<i>(C++11)</i> </p>
