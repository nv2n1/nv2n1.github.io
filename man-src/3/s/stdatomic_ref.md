---
title: "stdatomic_ref(3)"
name: "stdatomic_ref"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatomic_ref/"
description: "std::atomic_ref – std::atomic_ref"
---

<p>std::atomic_ref &#8211; std::atomic_ref</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;atomic&gt;

    template &lt;class T&gt;
    (1)(since C++ 20)

        struct atomic_ref;

template &lt;class T&gt;
(2)(since C++ 20)

    struct atomic_ref&lt;T *&gt;;</code></pre>
<p>The std::atomic_ref class template applies atomic operations to the object it references. For the lifetime of the atomic_ref object, the object it references is considered an atomic object. If one thread writes to an atomic object while another thread reads from it, the behavior is well-defined (see memory_model for details on data races). In addition, accesses to atomic objects may establish inter-thread synchronization and order non-atomic memory accesses as specified by std::memory_order.<br />
The lifetime of an object must exceed the lifetime of all atomic_refs that references the object. While any atomic_ref instances referencing an object exists, the object must be exclusively accessed through these atomic_ref instances. No subobject of an object referenced by an atomic_ref object may be concurrently referenced by any other atomic_ref object.<br />
Atomic operations applied to an object through an atomic_ref are atomic with respect to atomic operations applied through any other atomic_ref referencing the same object.<br />
std::atomic_ref is CopyConstructible.<br />
Like language references, constness is shallow for atomic_ref &#8211; it is possible to modify the referenced value through a const atomic_ref object. </p>
<h2>Specializations</h2>
<p>Primary template </p>
<p>The primary std::atomic_ref template may be instantiated with any TriviallyCopyable type T (including bool): </p>
<p>&nbsp;<wbr>&nbsp;struct Counters { int a; int b; } counter; // user-defined trivially-copyable type<br />
&nbsp;<wbr>&nbsp;std::atomic_ref&lt;Counters&gt; cnt(counter); // specialization for the user-defined type </p>
<p>Partial specialization for pointer types </p>
<p>The standard library provides partial specializations of the std::atomic_ref template for for all pointer types. In addition to the operations provided for all atomic types, these specializations additionally support atomic arithmetic operations appropriate to pointer types, such as fetch_add, fetch_sub. </p>
<p>Specializations for integral types </p>
<p>When instantiated with one of the following integral types, std::atomic_ref provides additional atomic operations appropriate to integral types such as fetch_add, fetch_sub, fetch_and, fetch_or, fetch_xor: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* The character types char<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;, char8_t<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++20)</i>, char16_t, char32_t, and wchar_t;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* The standard signed integer types: signed char, short, int, long, and long long;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* The standard unsigned integer types: unsigned char, unsigned short, unsigned int, unsigned long, and unsigned long long;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* Any additional integral types needed by the typedefs in the header &lt;cstdint&gt;. </p>
<p>Signed integer arithmetic is defined to use two&#8217;s complement; there are no undefined results. </p>
<p>Specializations for floating-point types </p>
<p>When instantiated with one of the floating-point types float, double, and long double, std::atomic_ref provides additional atomic operations appropriate to floating-point types such as fetch_add and fetch_sub.<br />
No operations result in undefined behavior even if the result is not representable in the floating-point type. The floating-point_environment in effect may be different from the calling thread&#8217;s floating-point environment.</p>
<h2>Member types</h2>
<p>Member type Definition<br />
value_type see below<br />
difference_type value_type (only for atomic_ref&lt;Integral&gt; and atomic_ref&lt;Floating&gt; specializations)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::ptrdiff_t (only for atomic_ref&lt;T*&gt; specializations) </p>
<p>For every std::atomic_ref&lt;X&gt; (whether or not specialized), std::atomic_ref&lt;X&gt;::value_type is X.<br />
difference_type is not defined in the primary atomic_ref template.</p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs an atomic_ref object<br />
constructor <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;stores a value into the object referenced by an atomic_ref object<br />
operator= <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if the atomic_ref object is lock-free<br />
is_lock_free <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;atomically replaces the value of the referenced object with a non-atomic argument<br />
store <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;atomically obtains the value of the referenced object<br />
load <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;loads a value from the referenced object<br />
operator_T <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;atomically replaces the value of the referenced object and obtains the value held previously<br />
exchange <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;atomically compares the value of the referenced object with non-atomic argument and performs atomic exchange if equal or atomic load if not<br />
compare_exchange_weak <i>(public member function)</i><br />
compare_exchange_strong</p>
<h2>Constants</h2>
<p>is_always_lock_free indicates that the type is always lock-free<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
<p>required_alignment indicates that the required alignment of an object to be referenced by atomic_ref<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code></p>
<h2>Specialized member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;atomically adds the argument to the value stored in the referenced object and obtains the value held previously<br />
fetch_add <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;atomically subtracts the argument from the value stored in the referenced object and obtains the value held previously<br />
fetch_sub <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;atomically performs bitwise AND between the argument and the value of the referenced object and obtains the value held previously<br />
fetch_and <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;atomically performs bitwise OR between the argument and the value of the referenced object and obtains the value held previously<br />
fetch_or <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;atomically performs bitwise XOR between the argument and the value of the referenced object and obtains the value held previously<br />
fetch_xor <i>(public member function)</i> </p>
<p>operator++ atomically increments or decrements the referenced object by one<br />
operator++(int) <i>(public member function)</i><br />
operator&#8211;<br />
operator&#8211;(int) </p>
<p>operator+=<br />
operator-= atomically adds, subtracts, or performs bitwise AND, OR, XOR with the referenced value<br />
operator&amp;= <i>(public member function)</i><br />
operator|=<br />
operator^=</p>
<h2>See also</h2>
<p>atomic atomic class template and specializations for bool, integral, and pointer types<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i> </p>
