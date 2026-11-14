---
title: "stdweak_ptr(3)"
name: "stdweak_ptr"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdweak_ptr/"
---

std::weak_ptr - std::weak_ptr

<h2>Synopsis</h2>

Defined in header &lt;memory&gt; 
template&lt; class T &gt; class weak_ptr; <i>(since C++11)</i> 
std::weak_ptr is a smart pointer that holds a non-owning (&quot;weak&quot;) reference to an object that is managed by std::shared_ptr. It must be converted to std::shared_ptr in order to access the referenced object. 
std::weak_ptr models temporary ownership: when an object needs to be accessed only if it exists, and it may be deleted at any time by someone else, std::weak_ptr is used to track the object, and it is converted to std::shared_ptr to assume temporary ownership. If the original std::shared_ptr is destroyed at this time, the object's lifetime is extended until the temporary std::shared_ptr is destroyed as well. 
Another use for std::weak_ptr is to break reference cycles formed by objects managed by std::shared_ptr. If such cycle is orphaned (i,e. there are no outside shared pointers into the cycle), the shared_ptr reference counts cannot reach zero and the memory is leaked. To prevent this, one of the pointers in the cycle can be made weak. 

<h2>Member types</h2>

Member type Definition 

 
element_type T <i>(until C++17)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::remove_extent_t&lt;T&gt; <i>(since C++17)</i>

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a new weak_ptr 
constructor <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;destroys a weak_ptr 
destructor <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;assigns the weak_ptr 
operator= <i>(public member function)</i>

<h2>Modifiers</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;releases the ownership of the managed object 
reset <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swaps the managed objects 
swap <i>(public member function)</i>

<h2>Observers</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the number of shared_ptr objects that manage the object 
use_count <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks whether the referenced object was already deleted 
expired <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a shared_ptr that manages the referenced object 
lock <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;provides owner-based ordering of weak pointers 
owner_before <i>(public member function)</i>

<h2>Non-member functions</h2>

std::swap(std::weak_ptr) specializes the std::swap algorithm 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i>

<h2>Helper classes</h2>

std::atomic&lt;std::weak_ptr&gt; atomic weak pointer 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template specialization)</i> 
(C++20) 

 

 
Deduction_guides<i>(since C++17)</i>

<h2>Notes</h2>

Like std::shared_ptr, a typical implementation of weak_ptr stores two pointers: 
* a pointer to the control block; and 
* the stored pointer of the shared_ptr it was constructed from. 
A separate stored pointer is necessary to ensure that converting a shared_ptr to weak_ptr and then back works correctly, even for aliased shared_ptrs. It is not possible to access the stored pointer in a weak_ptr without locking it into a shared_ptr. 
Defect reports 
The following behavior-changing defect reports were applied retroactively to previously published C++ standards. 
DR Applied to Behavior as published Correct behavior 
LWG_3001 C++17 element_type was not updated for array support updated 

<h2>Example</h2>

Demonstrates how lock is used to ensure validity of the pointer. 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;memory&gt;
std::weak_ptr&lt;int&gt; gw;
void observe()

{
    std::cout &lt;&lt; &quot;use_count == &quot; &lt;&lt; gw.use_count() &lt;&lt; &quot;: &quot;;
    if (auto spt = gw.lock()) { // Has to be copied into a shared_ptr before usage

        std::cout &lt;&lt; *spt &lt;&lt; &quot;\n&quot;;
    } else {
        std::cout &lt;&lt; &quot;gw is expired\n&quot;;
    }
}
int main()

{
    {
        auto sp = std::make_shared&lt;int&gt;(42);

        gw = sp;
        observe();
    }
    observe();
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;use_count == 1: 42 
&nbsp;<wbr>&nbsp;use_count == 0: gw is expired
