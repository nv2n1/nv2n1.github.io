---
title: "stdatomic_is_lock_freeatomic_xxx_lock_free(3)"
name: "stdatomic_is_lock_freeatomic_xxx_lock_free"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatomic_is_lock_freeatomic_xxx_lock_free/"
description: "std::atomic_is_lock_free,ATOMIC_xxx_LOCK_FREE – std::atomic_is_lock_free,ATOMIC_xxx_LOCK_FREE"
---

<p>std::atomic_is_lock_free,ATOMIC_xxx_LOCK_FREE &#8211; std::atomic_is_lock_free,ATOMIC_xxx_LOCK_FREE</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;atomic&gt;

    template &lt;class T&gt;

    bool atomic_is_lock_free(const volatile std::atomic&lt;T&gt; *obj) noexcept;

template &lt;class T&gt;

bool atomic_is_lock_free(const std::atomic&lt;T&gt; *obj) noexcept;

#define ATOMIC_BOOL_LOCK_FREE /* unspecified */

#define ATOMIC_CHAR_LOCK_FREE /* unspecified */

#define ATOMIC_CHAR16_T_LOCK_FREE /* unspecified */

#define ATOMIC_CHAR32_T_LOCK_FREE /* unspecified */ (1)(since C++ 11)

#define ATOMIC_WCHAR_T_LOCK_FREE /* unspecified */ (2)(since C++ 11)

#define ATOMIC_SHORT_LOCK_FREE /* unspecified */

#define ATOMIC_INT_LOCK_FREE /* unspecified */

#define ATOMIC_LONG_LOCK_FREE /* unspecified */

#define ATOMIC_LLONG_LOCK_FREE /* unspecified */

#define ATOMIC_POINTER_LOCK_FREE /* unspecified */

#define ATOMIC_CHAR8_T_LOCK_FREE /* unspecified */ (3)(since C++ 20)</code></pre>
<p>1) Determines if the atomic object pointed to by obj is implemented lock-free, as if by calling obj-&gt;is_lock_free(). In any given program execution, the result of the lock-free query is the same for all pointers of the same type.<br />
2,3) Expands to an integer constant expression with value<br />
* 0 for the built-in atomic types that are never lock-free<br />
* 1 for the built-in atomic types that are sometimes lock-free<br />
* 2 for the built-in atomic types that are always lock-free. </p>
<h2>Parameters</h2>
<p>obj &#8211; pointer to the atomic object to examine</p>
<h2>Return value</h2>
<p>true if *obj is a lock-free atomic, false otherwise. </p>
<h2>Notes</h2>
<p>All atomic types except for std::atomic_flag may be implemented using mutexes or other locking operations, rather than using the lock-free atomic CPU instructions. Atomic types are also allowed to be sometimes lock-free: for example, if only some subarchitectures support lock-free atomic access for a given type (such as the CMPXCHG16B instruction on x86-64), whether atomics are lock-free may not be known until runtime.<br />
The C++ standard recommends (but does not require) that lock-free atomic operations are also address-free, that is, suitable for communication between processes using shared memory. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;utility&gt;

#include &lt;atomic&gt;
struct A {
    int a[100];
};

struct B {
    int x, y;
};

int main()

{
    std::atomic&lt;A&gt; a;
    std::atomic&lt;B&gt; b;
    std::cout &lt;&lt; std::boolalpha
              &lt;&lt; &quot;std::atomic&lt;A&gt; is lock free? &quot;
              &lt;&lt; std::atomic_is_lock_free(&amp;a) &lt;&lt; '
'
              &lt;&lt; &quot;std::atomic&lt;B&gt; is lock free? &quot;
              &lt;&lt; std::atomic_is_lock_free(&amp;b) &lt;&lt; '
';
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;std::atomic&lt;A&gt; is lock free? false<br />
&nbsp;<wbr>&nbsp;std::atomic&lt;B&gt; is lock free? true</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if the atomic object is lock-free<br />
is_lock_free <i>(public member function of std::atomic&lt;T&gt;)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;specializes atomic operations for std::shared_ptr<br />
std::atomic_is_lock_free(std::shared_ptr) <i>(function template)</i><br />
atomic_flag the lock-free boolean atomic type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i><br />
<i>(C++11)</i><br />
is_always_lock_free indicates that the type is always lock-free<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant of std::atomic&lt;T&gt;)</i><br />
<code>[static]</code> <i>(C++17)</i> </p>
