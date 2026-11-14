---
title: "stdscoped_lock(3)"
name: "stdscoped_lock"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdscoped_lock/"
---

std::scoped_lock - std::scoped_lock

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;mutex&gt;

template&lt; class... MutexTypes &gt;  (since C++17)

class scoped_lock;</code></pre> 
The class scoped_lock is a mutex wrapper that provides a convenient RAII-style mechanism for owning one or more mutexes for the duration of a scoped block. 
When a scoped_lock object is created, it attempts to take ownership of the mutexes it is given. When control leaves the scope in which the scoped_lock object was created, the scoped_lock is destructed and the mutexes are released, in reverse order. If several mutexes are given, deadlock avoidance algorithm is used as if by std::lock. 
The scoped_lock class is non-copyable. 

<h2>Template parameters</h2>

MutexTypes - the types of the mutexes to lock. The types must meet the Lockable requirements unless sizeof...(MutexTypes)==1, in which case the only type must meet BasicLockable

<h2>Member types</h2>

Member type Definition 
mutex_type (if sizeof...(MutexTypes)==1) Mutex, the sole type in MutexTypes...

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a scoped_lock, optionally locking the given mutexes 
constructor <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;destructs the scoped_lock object, unlocks the underlying mutexes 
destructor <i>(public member function)</i> 

 
operator= not copy-assignable 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i> 
[deleted]

<h2>Example</h2>

The following example uses std::scoped_lock to lock pairs of mutexes without deadlock and is RAII-style. 
 // Run this code <pre><code>#include &lt;mutex&gt;

#include &lt;thread&gt;

#include &lt;iostream&gt;

#include &lt;vector&gt;

#include &lt;functional&gt;

#include &lt;chrono&gt;

#include &lt;string&gt;
struct Employee {
    Employee(std::string id)
        : id(id)
    {
    }
    std::string id;
    std::vector&lt;std::string&gt; lunch_partners;
    std::mutex m;
    std::string output() const
    {
        std::string ret = &quot;Employee &quot; + id + &quot; has lunch partners: &quot;;
        for (const auto &amp;partner : lunch_partners)
            ret += partner + &quot; &quot;;
        return ret;
    }
};
void send_mail(Employee &amp;, Employee &amp;)

{
    // simulate a time-consuming messaging operation
    std::this_thread::sleep_for(std::chrono::seconds(1));
}
void assign_lunch_partner(Employee &amp;e1, Employee &amp;e2)

{
    static std::mutex io_mutex;
    {
        std::lock_guard&lt;std::mutex&gt; lk(io_mutex);
        std::cout &lt;&lt; e1.id &lt;&lt; &quot; and &quot; &lt;&lt; e2.id &lt;&lt; &quot; are waiting for locks&quot; &lt;&lt; std::endl;
    }
    {
        // use std::scoped_lock to acquire two locks without worrying about
        // other calls to assign_lunch_partner deadlocking us
        // and it also provides a convenient RAII-style mechanism
        std::scoped_lock lock(e1.m, e2.m);
        // Equivalent code 1 (using std::lock and std::lock_guard)
        // std::lock(e1.m, e2.m);
        // std::lock_guard&lt;std::mutex&gt; lk1(e1.m, std::adopt_lock);
        // std::lock_guard&lt;std::mutex&gt; lk2(e2.m, std::adopt_lock);
        // Equivalent code 2 (if unique_locks are needed, e.g. for condition variables)
        // std::unique_lock&lt;std::mutex&gt; lk1(e1.m, std::defer_lock);
        // std::unique_lock&lt;std::mutex&gt; lk2(e2.m, std::defer_lock);
        // std::lock(lk1, lk2);
        {
            std::lock_guard&lt;std::mutex&gt; lk(io_mutex);
            std::cout &lt;&lt; e1.id &lt;&lt; &quot; and &quot; &lt;&lt; e2.id &lt;&lt; &quot; got locks&quot; &lt;&lt; std::endl;
        }
        e1.lunch_partners.push_back(e2.id);
        e2.lunch_partners.push_back(e1.id);
    }
    send_mail(e1, e2);
    send_mail(e2, e1);
}
int main()

{
    Employee alice(&quot;alice&quot;), bob(&quot;bob&quot;), christina(&quot;christina&quot;), dave(&quot;dave&quot;);
    // assign in parallel threads because mailing users about lunch assignments
    // takes a long time
    std::vector&lt;std::thread&gt; threads;
    threads.emplace_back(assign_lunch_partner, std::ref(alice), std::ref(bob));
    threads.emplace_back(assign_lunch_partner, std::ref(christina), std::ref(bob));
    threads.emplace_back(assign_lunch_partner, std::ref(christina), std::ref(alice));
    threads.emplace_back(assign_lunch_partner, std::ref(dave), std::ref(bob));
    for (auto &amp;thread : threads)
        thread.join();
    std::cout &lt;&lt; alice.output() &lt;&lt; '\n'
              &lt;&lt; bob.output() &lt;&lt; '\n'
              &lt;&lt; christina.output() &lt;&lt; '\n'
              &lt;&lt; dave.output() &lt;&lt; '\n';
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;alice and bob are waiting for locks 
&nbsp;<wbr>&nbsp;alice and bob got locks 
&nbsp;<wbr>&nbsp;christina and bob are waiting for locks 
&nbsp;<wbr>&nbsp;christina and alice are waiting for locks 
&nbsp;<wbr>&nbsp;dave and bob are waiting for locks 
&nbsp;<wbr>&nbsp;dave and bob got locks 
&nbsp;<wbr>&nbsp;christina and alice got locks 
&nbsp;<wbr>&nbsp;christina and bob got locks 
&nbsp;<wbr>&nbsp;Employee alice has lunch partners: bob christina 
&nbsp;<wbr>&nbsp;Employee bob has lunch partners: alice dave christina 
&nbsp;<wbr>&nbsp;Employee christina has lunch partners: alice bob 
&nbsp;<wbr>&nbsp;Employee dave has lunch partners: bob 

 

 
Defect reports 

 
The following behavior-changing defect reports were applied retroactively to previously published C++ standards. 

 
DR Applied to Behavior as published Correct behavior 
LWG_2981 C++17 redundant deduction guide from scoped_lock&lt;MutexTypes...&gt; was provided removed

<h2>See also</h2>

unique_lock implements movable mutex ownership wrapper 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
lock_guard implements a strictly scope-based mutex ownership wrapper 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
