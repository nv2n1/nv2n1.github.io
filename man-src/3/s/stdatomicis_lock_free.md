---
title: "stdatomicis_lock_free(3)"
name: "stdatomicis_lock_free"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatomicis_lock_free/"
description: "std::atomic<T>::is_lock_free – std::atomic<T>::is_lock_free"
---

<p>std::atomic&lt;T&gt;::is_lock_free &#8211; std::atomic&lt;T&gt;::is_lock_free</p>
<h2>Synopsis</h2>
<pre><code>bool is_lock_free() const noexcept;
(since C++ 11)

    bool is_lock_free() const volatile noexcept;</code></pre>
<p>Checks whether the atomic operations on all objects of this type are lock-free. </p>
<h2>Parameters</h2>
<p><i>(none)</i></p>
<h2>Return value</h2>
<p>true if the atomic operations on the objects of this type are lock-free, false otherwise. </p>
<h2>Notes</h2>
<p>All atomic types except for std::atomic_flag may be implemented using mutexes or other locking operations, rather than using the lock-free atomic CPU instructions. Atomic types are also allowed to be sometimes lock-free, e.g. if only aligned memory accesses are naturally atomic on a given architecture, misaligned objects of the same type have to use locks.<br />
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
    std::cout &lt;&lt; std::boolalpha
              &lt;&lt; &quot;std::atomic&lt;A&gt; is lock free? &quot;
              &lt;&lt; std::atomic&lt;A&gt;{}.is_lock_free() &lt;&lt; '
'
              &lt;&lt; &quot;std::atomic&lt;B&gt; is lock free? &quot;
              &lt;&lt; std::atomic&lt;B&gt;{}.is_lock_free() &lt;&lt; '
';
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;std::atomic&lt;A&gt; is lock free? false<br />
&nbsp;<wbr>&nbsp;std::atomic&lt;B&gt; is lock free? true</p>
<h2>See also</h2>
<p>atomic_is_lock_free checks if the atomic type&#8217;s operations are lock-free<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++11)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;specializes atomic operations for std::shared_ptr<br />
atomic_is_lock_free(std::shared_ptr) <i>(function template)</i><br />
is_always_lock_free indicates that the type is always lock-free<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> <i>(C++17)</i> </p>
