---
title: "stdshared_ptr(3)"
name: "stdshared_ptr"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdshared_ptr/"
---

std::shared_ptr - std::shared_ptr

<h2>Synopsis</h2>

Defined in header &lt;memory&gt; 
template&lt; class T &gt; class shared_ptr; <i>(since C++11)</i> 
std::shared_ptr is a smart pointer that retains shared ownership of an object through a pointer. Several shared_ptr objects may own the same object. The object is destroyed and its memory deallocated when either of the following happens: <pre><code>* the last remaining shared_ptr owning the object is destroyed;

* the last remaining shared_ptr owning the object is assigned another pointer via operator= or reset().</code></pre> 
The object is destroyed using delete-expression or a custom deleter that is supplied to shared_ptr during construction. 
A shared_ptr can share ownership of an object while storing a pointer to another object. This feature can be used to point to member objects while owning the object they belong to. The stored pointer is the one accessed by get(), the dereference and the comparison operators. The managed pointer is the one passed to the deleter when use count reaches zero. 
A shared_ptr may also own no objects, in which case it is called empty (an empty shared_ptr may have a non-null stored pointer if the aliasing constructor was used to create it). 
All specializations of shared_ptr meet the requirements of CopyConstructible, CopyAssignable, and LessThanComparable and are contextually_convertible to bool. 
All member functions (including copy constructor and copy assignment) can be called by multiple threads on different instances of shared_ptr without additional synchronization even if these instances are copies and share ownership of the same object. If multiple threads of execution access the same shared_ptr without synchronization and any of those accesses uses a non-const member function of shared_ptr then a data race will occur; the shared_ptr_overloads_of_atomic_functions can be used to prevent the data race. 

<h2>Member types</h2>

Member type Definition 

 
element_type T <i>(until C++17)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::remove_extent_t&lt;T&gt; <i>(since C++17)</i> 

 
weak_type <i>(since C++17)</i> std::weak_ptr&lt;T&gt;

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs new shared_ptr 
constructor <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;destructs the owned object if no more shared_ptrs link to it 
destructor <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;assigns the shared_ptr 
operator= <i>(public member function)</i>

<h2>Modifiers</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;replaces the managed object 
reset <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swaps the managed objects 
swap <i>(public member function)</i>

<h2>Observers</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the stored pointer 
get <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;dereferences the stored pointer 
operator* <i>(public member function)</i> 
operator-&gt; 

 
operator[] provides indexed access to the stored array 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i> 
<i>(C++17)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the number of shared_ptr objects referring to the same managed object 
use_count <i>(public member function)</i> 

 
unique checks whether the managed object is managed only by the current shared_ptr instance 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i> 
<i>(until C++20)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if the stored pointer is not null 
operator_bool <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;provides owner-based ordering of shared pointers 
owner_before <i>(public member function)</i>

<h2>Non-member functions</h2>

make_shared 
make_shared_default_init creates a shared pointer that manages a new object 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 

 
(C++20) 

 
allocate_shared 
allocate_shared_default_init creates a shared pointer that manages a new object allocated using an allocator 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 

 
(C++20) 

 
static_pointer_cast 
dynamic_pointer_cast 
const_pointer_cast 
reinterpret_pointer_cast applies static_cast, dynamic_cast, const_cast, or reinterpret_cast to the stored pointer 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 

 

 

 
<i>(C++17)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the deleter of specified type, if owned 
get_deleter <i>(function template)</i> 

 
operator== 
operator!= compares with another shared_ptr or with nullptr 
operator&lt; <i>(function template)</i> 
operator&lt;= 
operator&gt; 
operator&gt;= 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;outputs the value of the stored pointer to an output stream 
operator&lt;&lt; <i>(function template)</i> 

 
std::swap(std::shared_ptr) specializes the std::swap algorithm 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 

 

 

 
std::atomic_is_lock_free(std::shared_ptr) 
std::atomic_load(std::shared_ptr) 
std::atomic_load_explicit(std::shared_ptr) 
std::atomic_store(std::shared_ptr) 
std::atomic_store_explicit(std::shared_ptr) 
std::atomic_exchange(std::shared_ptr) specializes atomic operations for std::shared_ptr 
std::atomic_exchange_explicit(std::shared_ptr) <i>(function template)</i> 
std::atomic_compare_exchange_weak(std::shared_ptr) 
std::atomic_compare_exchange_strong(std::shared_ptr) 
std::atomic_compare_exchange_weak_explicit(std::shared_ptr) 
std::atomic_compare_exchange_strong_explicit(std::shared_ptr) 

 
(deprecated in C++20)

<h2>Helper classes</h2>

std::atomic&lt;std::shared_ptr&gt; atomic shared pointer 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template specialization)</i> 
(C++20) 

 
std::hash&lt;std::shared_ptr&gt; hash support for std::shared_ptr 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template specialization)</i> 
<i>(C++11)</i> 

 

 
Deduction_guides<i>(since C++17)</i>

<h2>Notes</h2>

The ownership of an object can only be shared with another shared_ptr by copy constructing or copy assigning its value to another shared_ptr. Constructing a new shared_ptr using the raw underlying pointer owned by another shared_ptr leads to undefined behavior. 
std::shared_ptr may be used with an incomplete_type T. However, the constructor from a raw pointer (template&lt;class Y&gt; shared_ptr(Y*)) and the template&lt;class Y&gt; void reset(Y*) member function may only be called with a pointer to a complete type (note that std::unique_ptr may be constructed from a raw pointer to an incomplete type). 
The T in std::shared_ptr&lt;T&gt; may be a function type: in this case it manages a pointer to function, rather than an object pointer. This is sometimes used to keep a dynamic library or a plugin loaded as long as any of its functions are referenced: void del(void (*)())
{
}

void fun()
{
}

int main()
{
    std::shared_ptr&lt;void()&gt; ee(fun, del);
    (*ee)();
}


<h2>Implementation notes</h2>

In a typical implementation, std::shared_ptr holds only two pointers: 

 
* the stored pointer (one returned by get()); 
* a pointer to control block. 

 
The control block is a dynamically-allocated object that holds: 

 
* either a pointer to the managed object or the managed object itself; 
* the deleter (type-erased); 
* the allocator (type-erased); 
* the number of shared_ptrs that own the managed object; 
* the number of weak_ptrs that refer to the managed object. 

 
When shared_ptr is created by calling std::make_shared or std::allocate_shared, the memory for both the control block and the managed object is created with a single allocation. The managed object is constructed in-place in a data member of the control block. When shared_ptr is created via one of the shared_ptr constructors, the managed object and the control block must be allocated separately. In this case, the control block stores a pointer to the managed object. 
The pointer held by the shared_ptr directly is the one returned by get(), while the pointer/object held by the control block is the one that will be deleted when the number of shared owners reaches zero. These pointers are not necessarily equal. 
The destructor of shared_ptr decrements the number of shared owners of the control block. If that counter reaches zero, the control block calls the destructor of the managed object. The control block does not deallocate itself until the std::weak_ptr counter reaches zero as well. 
In existing implementations, the number of weak pointers is incremented ([1], [2]) if there is a shared pointer to the same control block. 
To satisfy thread safety requirements, the reference counters are typically incremented using an equivalent of std::atomic::fetch_add with std::memory_order_relaxed (decrementing requires stronger ordering to safely destroy the control block).

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;memory&gt;

#include &lt;thread&gt;

#include &lt;chrono&gt;

#include &lt;mutex&gt;
struct Base

{
    Base()
    {
        std::cout &lt;&lt; &quot;  Base::Base()\n&quot;;
    }
    // Note: non-virtual destructor is OK here
    ~Base()
    {
        std::cout &lt;&lt; &quot;  Base::~Base()\n&quot;;
    }
};
struct Derived : public Base

{
    Derived()
    {
        std::cout &lt;&lt; &quot;  Derived::Derived()\n&quot;;
    }
    ~Derived()
    {
        std::cout &lt;&lt; &quot;  Derived::~Derived()\n&quot;;
    }
};
void thr(std::shared_ptr&lt;Base&gt; p)

{
    std::this_thread::sleep_for(std::chrono::seconds(1));
    std::shared_ptr&lt;Base&gt; lp = p; // thread-safe, even though the
                                  // shared use_count is incremented
    {
        static std::mutex io_mutex;
        std::lock_guard&lt;std::mutex&gt; lk(io_mutex);
        std::cout &lt;&lt; &quot;local pointer in a thread:\n&quot;
                  &lt;&lt; &quot;  lp.get() = &quot; &lt;&lt; lp.get()
                  &lt;&lt; &quot;, lp.use_count() = &quot; &lt;&lt; lp.use_count() &lt;&lt; '\n';
    }
}
int main()

{
    std::shared_ptr&lt;Base&gt; p = std::make_shared&lt;Derived&gt;();
    std::cout &lt;&lt; &quot;Created a shared Derived (as a pointer to Base)\n&quot;
              &lt;&lt; &quot;  p.get() = &quot; &lt;&lt; p.get()
              &lt;&lt; &quot;, p.use_count() = &quot; &lt;&lt; p.use_count() &lt;&lt; '\n';
    std::thread t1(thr, p), t2(thr, p), t3(thr, p);
    p.reset(); // release ownership from main
    std::cout &lt;&lt; &quot;Shared ownership between 3 threads and released\n&quot;
              &lt;&lt; &quot;ownership from main:\n&quot;
              &lt;&lt; &quot;  p.get() = &quot; &lt;&lt; p.get()
              &lt;&lt; &quot;, p.use_count() = &quot; &lt;&lt; p.use_count() &lt;&lt; '\n';
    t1.join();
    t2.join();
    t3.join();
    std::cout &lt;&lt; &quot;All threads completed, the last one deleted Derived\n&quot;;
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;Base::Base() 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Derived::Derived() 
&nbsp;<wbr>&nbsp;Created a shared Derived (as a pointer to Base) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;p.get() = 0xc99028, p.use_count() = 1 
&nbsp;<wbr>&nbsp;Shared ownership between 3 threads and released 
&nbsp;<wbr>&nbsp;ownership from main: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;p.get() = (nil), p.use_count() = 0 
&nbsp;<wbr>&nbsp;local pointer in a thread: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;lp.get() = 0xc99028, lp.use_count() = 3 
&nbsp;<wbr>&nbsp;local pointer in a thread: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;lp.get() = 0xc99028, lp.use_count() = 4 
&nbsp;<wbr>&nbsp;local pointer in a thread: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;lp.get() = 0xc99028, lp.use_count() = 2 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Derived::~Derived() 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Base::~Base() 
&nbsp;<wbr>&nbsp;All threads completed, the last one deleted Derived
