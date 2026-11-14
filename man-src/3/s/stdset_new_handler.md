---
title: "stdset_new_handler(3)"
name: "stdset_new_handler"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdset_new_handler/"
---

std::set_new_handler - std::set_new_handler

<h2>Synopsis</h2>

Defined in header &lt;new&gt; 
std::new_handler set_new_handler( std::new_handler new_p ) throw(); <i>(until C++11)</i> 
std::new_handler set_new_handler( std::new_handler new_p ) noexcept; <i>(since C++11)</i> 
Makes new_p the new global new-handler function and returns the previously installed new-handler. 
The new-handler function is the function called by allocation_functions whenever a memory allocation attempt fails. Its intended purpose is one of three things: 
1) make more memory available 
2) terminate the program (e.g. by calling std::terminate) 
3) throw exception of type std::bad_alloc or derived from std::bad_alloc. 
The default implementation throws std::bad_alloc. The user can install his own new-handler, which may offer behavior different than the default one. 
If new-handler returns, the allocation function repeats the previously-failed allocation attempt and calls the new-handler again if the allocation fails again. To end the loop, new-handler may call std::set_new_handler(nullptr): if, after a failed allocation attempt, allocation function finds that std::get_new_handler returns a null pointer value, it will throw std::bad_alloc. 
At program startup, new-handler is a null pointer. 
This function is thread-safe. Every call to std::set_new_handler synchronizes-with (see std::memory_order) the subsequent std::set_new_handler and std::get_new_handler calls. <i>(since C++11)</i> 

<h2>Parameters</h2>

new_p - pointer to function of type std::new_handler, or null pointer

<h2>Return value</h2>

The previously-installed new handler, or a null pointer value if none was installed. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;new&gt;
void handler()

{
    std::cout &lt;&lt; &quot;Memory allocation failed, terminating\n&quot;;
    std::set_new_handler(nullptr);
}
int main()

{
    std::set_new_handler(handler);
    try {
        while (true) {
            new int[100000000ul];
        }
    } catch (const std::bad_alloc &amp;e) {
        std::cout &lt;&lt; e.what() &lt;&lt; '\n';
    }
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Memory allocation failed, terminating 
&nbsp;<wbr>&nbsp;std::bad_alloc

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;allocation functions 
operator_new <i>(function)</i> 
operator_new[] 
get_new_handler obtains the current new handler 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;function pointer type of the new handler 
new_handler <i>(typedef)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exception thrown when memory allocation fails 
bad_alloc <i>(class)</i> 
