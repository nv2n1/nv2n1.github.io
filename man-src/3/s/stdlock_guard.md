---
title: "stdlock_guard(3)"
name: "stdlock_guard"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdlock_guard/"
---

std::lock_guard - std::lock_guard

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;mutex&gt;

template&lt; class Mutex &gt;

class lock_guard;</code></pre> 
The class lock_guard is a mutex wrapper that provides a convenient RAII-style mechanism for owning a mutex for the duration of a scoped block. 
When a lock_guard object is created, it attempts to take ownership of the mutex it is given. When control leaves the scope in which the lock_guard object was created, the lock_guard is destructed and the mutex is released. 
The lock_guard class is non-copyable. 

<h2>Template parameters</h2>

Mutex - the type of the mutex to lock. The type must meet the BasicLockable requirements

<h2>Member types</h2>

Member type Definition 
mutex_type Mutex

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a lock_guard, optionally locking the given mutex 
constructor <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;destructs the lock_guard object, unlocks the underlying mutex 
destructor <i>(public member function)</i> 

 
operator= not copy-assignable 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i> 
[deleted]

<h2>Example</h2>

// Run this code <pre><code>#include &lt;thread&gt;

#include &lt;mutex&gt;

#include &lt;iostream&gt;
int g_i = 0;

std::mutex g_i_mutex; // protects g_i
void safe_increment()

{
    std::lock_guard&lt;std::mutex&gt; lock(g_i_mutex);
    ++g_i;
    std::cout &lt;&lt; std::this_thread::get_id() &lt;&lt; &quot;: &quot; &lt;&lt; g_i &lt;&lt; '\n';
    // g_i_mutex is automatically released when lock
    // goes out of scope
}
int main()

{
    std::cout &lt;&lt; &quot;main: &quot; &lt;&lt; g_i &lt;&lt; '\n';
    std::thread t1(safe_increment);
    std::thread t2(safe_increment);
    t1.join();
    t2.join();
    std::cout &lt;&lt; &quot;main: &quot; &lt;&lt; g_i &lt;&lt; '\n';
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;main: 0 
&nbsp;<wbr>&nbsp;140641306900224: 1 
&nbsp;<wbr>&nbsp;140641298507520: 2 
&nbsp;<wbr>&nbsp;main: 2 

 

 
Defect reports 

 
The following behavior-changing defect reports were applied retroactively to previously published C++ standards. 

 
DR Applied to Behavior as published Correct behavior 
LWG_2981 C++17 redundant deduction guide from lock_guard&lt;Mutex&gt; was provided removed

<h2>See also</h2>

unique_lock implements movable mutex ownership wrapper 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
scoped_lock deadlock-avoiding RAII wrapper for multiple mutexes 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++17)</i> 
