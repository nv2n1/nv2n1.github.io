---
title: "stdenable_shared_from_this(3)"
name: "stdenable_shared_from_this"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdenable_shared_from_this/"
---

std::enable_shared_from_this - std::enable_shared_from_this

<h2>Synopsis</h2>

Defined in header &lt;memory&gt; 
template&lt; class T &gt; class enable_shared_from_this; <i>(since C++11)</i> 
std::enable_shared_from_this allows an object t that is currently managed by a std::shared_ptr named pt to safely generate additional std::shared_ptr instances pt1, pt2, ... that all share ownership of t with pt. 
Publicly inheriting from std::enable_shared_from_this&lt;T&gt; provides the type T with a member function shared_from_this. If an object t of type T is managed by a std::shared_ptr&lt;T&gt; named pt, then calling T::shared_from_this will return a new std::shared_ptr&lt;T&gt; that shares ownership of t with pt. 

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs an enable_shared_from_this object 
constructor <i>(protected member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;destroys an enable_shared_from_this object 
destructor <i>(protected member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns a reference to this 
operator= <i>(protected member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns a shared_ptr which shares ownership of *this 
shared_from_this <i>(public member function)</i> 

 
weak_from_this returns the weak_ptr which shares ownership of *this 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i> 
<i>(C++17)</i>

<h2>Member objects</h2>

Member name Definition 
weak_this (private)<i>(C++17)</i> std::weak_ptr object tracking the control block of the first shared owner of *this. Exposition only

<h2>Notes</h2>

A common implementation for enable_shared_from_this is to hold a weak reference (such as std::weak_ptr) to this. The constructors of std::shared_ptr detect the presence of an 
unambiguous and accessible 
<i>(since C++17)</i> enable_shared_from_this base and assign the newly created std::shared_ptr to the internally stored weak reference 
if not already owned by a live std::shared_ptr 
<i>(since C++17)</i>. Constructing a std::shared_ptr for an object that is already managed by another std::shared_ptr will not consult the internally stored weak reference and thus will lead to undefined behavior. 
It is permitted to call shared_from_this only on a previously shared object, i.e. on an object managed by std::shared_ptr&lt;T&gt;. Otherwise 
the behavior is undefined 
<i>(until C++17)</i> 
std::bad_weak_ptr is thrown (by the shared_ptr constructor from a default-constructed weak_this) 
<i>(since C++17)</i>. 
enable_shared_from_this provides the safe alternative to an expression like std::shared_ptr&lt;T&gt;(this), which is likely to result in this being destructed more than once by multiple owners that are unaware of each other (see example below) 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;memory&gt;

#include &lt;iostream&gt;
struct Good : std::enable_shared_from_this&lt;Good&gt; // note: public inheritance

{
    std::shared_ptr&lt;Good&gt; getptr()
    {
        return shared_from_this();
    }
};
struct Bad

{
    std::shared_ptr&lt;Bad&gt; getptr()
    {
        return std::shared_ptr&lt;Bad&gt;(this);
    }
    ~Bad()
    {
        std::cout &lt;&lt; &quot;Bad::~Bad() called\n&quot;;
    }
};
int main()

{
    // Good: the two shared_ptr's share the same object
    std::shared_ptr&lt;Good&gt; gp1 = std::make_shared&lt;Good&gt;();
    std::shared_ptr&lt;Good&gt; gp2 = gp1-&gt;getptr();
    std::cout &lt;&lt; &quot;gp2.use_count() = &quot; &lt;&lt; gp2.use_count() &lt;&lt; '\n';
    // Bad: shared_from_this is called without having std::shared_ptr owning the caller
    try {
        Good not_so_good;
        std::shared_ptr&lt;Good&gt; gp1 = not_so_good.getptr();
    } catch (std::bad_weak_ptr &amp;e) {
        // undefined behavior (until C++17) and std::bad_weak_ptr thrown (since C++17)
        std::cout &lt;&lt; e.what() &lt;&lt; '\n';
    }
    // Bad, each shared_ptr thinks it's the only owner of the object
    std::shared_ptr&lt;Bad&gt; bp1 = std::make_shared&lt;Bad&gt;();
    std::shared_ptr&lt;Bad&gt; bp2 = bp1-&gt;getptr();
    std::cout &lt;&lt; &quot;bp2.use_count() = &quot; &lt;&lt; bp2.use_count() &lt;&lt; '\n';

} // UB: double-delete of Bad
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;gp2.use_count() = 2 
&nbsp;<wbr>&nbsp;bad_weak_ptr 
&nbsp;<wbr>&nbsp;bp2.use_count() = 1 
&nbsp;<wbr>&nbsp;Bad::~Bad() called 
&nbsp;<wbr>&nbsp;Bad::~Bad() called 
&nbsp;<wbr>&nbsp;*** glibc detected *** ./test: double free or corruption

<h2>See also</h2>

shared_ptr smart pointer with shared object ownership semantics 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
