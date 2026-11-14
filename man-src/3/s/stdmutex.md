---
title: "stdmutex(3)"
name: "stdmutex"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmutex/"
---

std::mutex - std::mutex

<h2>Synopsis</h2>

Defined in header &lt;mutex&gt; 
class mutex; <i>(since C++11)</i> 
The mutex class is a synchronization primitive that can be used to protect shared data from being simultaneously accessed by multiple threads. 
mutex offers exclusive, non-recursive ownership semantics: <pre><code>* A calling thread owns a mutex from the time that it successfully calls either lock or try_lock until it calls unlock.

* When a thread owns a mutex, all other threads will block (for calls to lock) or receive a false return value (for try_lock) if they attempt to claim ownership of the mutex.

* A calling thread must not own the mutex prior to calling lock or try_lock.</code></pre> 
The behavior of a program is undefined if a mutex is destroyed while still owned by any threads, or a thread terminates while owning a mutex. The mutex class satisfies all requirements of Mutex and StandardLayoutType. 
std::mutex is neither copyable nor movable. 

<h2>Member types</h2>

Member type Definition 
native_handle_type(optional) implementation-defined

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs the mutex 
constructor <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;destroys the mutex 
destructor <i>(public member function)</i> 

 
operator= not copy-assignable 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i> 
[deleted]

<h2>Locking</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;locks the mutex, blocks if the mutex is not available 
lock <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tries to lock the mutex, returns if the mutex is not available 
try_lock <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unlocks the mutex 
unlock <i>(public member function)</i>

<h2>Native handle</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the underlying implementation-defined native handle object 
native_handle <i>(public member function)</i>

<h2>Notes</h2>

std::mutex is usually not accessed directly: std::unique_lock, std::lock_guard, 
or std::scoped_lock 
<i>(since C++17)</i> manage locking in a more exception-safe manner. 

<h2>Example</h2>

This example shows how a mutex can be used to protect a std::map shared between two threads. 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;map&gt;

#include &lt;string&gt;

#include &lt;chrono&gt;

#include &lt;thread&gt;

#include &lt;mutex&gt;
std::map&lt;std::string, std::string&gt; g_pages;

std::mutex g_pages_mutex;
void save_page(const std::string &amp;url)

{
    // simulate a long page fetch
    std::this_thread::sleep_for(std::chrono::seconds(2));
    std::string result = &quot;fake content&quot;;
    std::lock_guard&lt;std::mutex&gt; guard(g_pages_mutex);
    g_pages[url] = result;
}
int main()

{
    std::thread t1(save_page, &quot;http://foo&quot;);
    std::thread t2(save_page, &quot;http://bar&quot;);
    t1.join();
    t2.join();
    // safe to access g_pages without lock now, as the threads are joined
    for (const auto &amp;pair : g_pages) {
        std::cout &lt;&lt; pair.first &lt;&lt; &quot; =&gt; &quot; &lt;&lt; pair.second &lt;&lt; '\n';
    }
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;<a rel="nofollow" HREF="http://bar">http://bar</a> =&gt; fake content 
&nbsp;<wbr>&nbsp;<a rel="nofollow" HREF="http://foo">http://foo</a> =&gt; fake content
