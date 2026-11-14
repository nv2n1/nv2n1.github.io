---
title: "stdexperimentalpmrresource_adaptor(3)"
name: "stdexperimentalpmrresource_adaptor"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalpmrresource_adaptor/"
---

std::experimental::pmr::resource_adaptor - std::experimental::pmr::resource_adaptor

<h2>Synopsis</h2>

Defined in header &lt;experimental/memory_resource&gt; 
template &lt; class Alloc &gt; 
class resource_adaptor_imp : public memory_resource; // for exposition only <pre><code>template &lt;class Allocator&gt;
(library fundamentals TS)

    using resource_adaptor = resource_adaptor_imp&lt;

        typename std::allocator_traits&lt;Allocator&gt;::

            template rebind_alloc&lt;char&gt;&gt;;</code></pre> 
The alias template resource_adaptor adapts the allocator type Allocator with a memory_resource interface. The allocator is rebound to a char value type before it is actually adapted (using the resource_adaptor_imp class template), so that adapting specializations of the same allocator template always yields the same type, regardless of the value type the allocator template is originally instantiated with. 
resource_adaptor_imp is a class template whose members are described below. The name resource_adaptor_imp is for exposition purposes only and not normative. 
In addition to meeting the Allocator requirements, Allocator must additionally satisfy the following requirements: 
* Its pointer shall be identical to value_type*. 
* Its const_pointer shall be identical to value_type const*. 
* Its void_pointer shall be identical to void*. 
* Its const_void_pointer shall be identical to void const*. 
Member types of resource_adaptor_imp 
Member type Definition 
allocator_type Alloc 
Member functions of resource_adaptor_imp 
std::experimental::pmr::resource_adaptor_imp::resource_adaptor_imp <pre><code>resource_adaptor_imp() = default;
(1)(library fundamentals TS)

    resource_adaptor_imp(const resource_adaptor_imp &amp;other) = default;
(2)(library fundamentals TS)

    resource_adaptor_imp(resource_adaptor_imp &amp;&amp;other) = default;
(3)(library fundamentals TS)

    explicit resource_adaptor_imp(const Alloc &amp;a2);
(4)(library fundamentals TS)

    explicit resource_adaptor_imp(Alloc &amp;&amp;a2);
(5)(library fundamentals TS)</code></pre> 
1) Default constructor. Default constructs the wrapped allocator. 
2) Copy constructor. Copy constructs the wrapped allocator from the allocator wrapped by other. 
3) Move constructor. Move constructs the wrapped allocator from the allocator wrapped by other. 
4) Initializes the wrapped allocator with a2. 
5) Initializes the wrapped allocator with std::move(a2). 

<h2>Parameters</h2>

other - another resource_adaptor_imp object to copy or move from 
a2 - another Alloc object to copy or move from 

 

 
std::experimental::pmr::resource_adaptor_imp::get_allocator 

 

 
allocator_type get_allocator() const; (library fundamentals TS) 

 
Returns a copy of the wrapped allocator. 

 
std::experimental::pmr::resource_adaptor_imp::operator= 

 

 
resource_adaptor_imp&amp; operator=(const resource_adaptor_imp&amp; other) = default; (library fundamentals TS) 

 
Defaulted copy assignment operator. Copy assigns the wrapped allocator from that of other. 

 
std::experimental::pmr::resource_adaptor_imp::do_allocate 

 

 
virtual void* do_allocate(std::size_t bytes, std::size_t alignment); (library fundamentals TS) 

 
Allocates memory using the allocate member function of the wrapped allocator. 

 
std::experimental::pmr::resource_adaptor_imp::do_deallocate 

 

 
virtual void do_deallocate(void *p, std::size_t bytes, std::size_t alignment); (library fundamentals TS) 

 
Deallocates the storage pointed to by p using the deallocate member function of the wrapped allocator. p must have been allocated using the allocate member function of an allocator that compares equal to the wrapped allocator, and must not have been subsequently deallocated. 

 
std::experimental::pmr::resource_adaptor_imp::do_is_equal 

 

 
virtual bool do_is_equal(const memory_resource&amp; other); (library fundamentals TS) 

 
Let p be dynamic_cast&lt;const resource_adaptor_imp*&gt;(&amp;other). If p is nullptr, returns false. Otherwise, return the result of comparing the allocators wrapped by *p and *this using operator==.
