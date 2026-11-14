---
title: "stdexperimentalpackaged_taskpackaged_tasklibraryfundamentalsts(3)"
name: "stdexperimentalpackaged_taskpackaged_tasklibraryfundamentalsts"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalpackaged_taskpackaged_tasklibraryfundamentalsts/"
---

std::experimental::packaged_task&lt;R(Args...)&gt;::packaged_task(libraryfundamentalsTS) - std::experimental::packaged_task&lt;R(Args...)&gt;::packaged_task(libraryfundamentalsTS)

<h2>Synopsis</h2>

<pre><code>packaged_task() noexcept;
(1)(library fundamentals TS)

    template &lt;class F&gt;
    (2)(library fundamentals TS)

        explicit packaged_task(F &amp;&amp;f);

template &lt;class F, class Allocator&gt;
(3)(library fundamentals TS)

    explicit packaged_task(std::allocator_arg_t, const Allocator &amp;alloc, F &amp;&amp;f);

packaged_task(const packaged_task &amp;) = delete;
(4)(library fundamentals TS)

    packaged_task(packaged_task &amp;&amp;rhs) noexcept;
(5)(library fundamentals TS)</code></pre> 
Constructs a new std::experimental::packaged_task object. 
1) Constructs a std::experimental::packaged_task object with no task and no shared state. 
2) Constructs a std::experimental::packaged_task object with a shared state and a copy of the task, initialized with std::forward&lt;F&gt;(f). This constructor does not participate in overload resolution if std::decay&lt;F&gt;::type is the same type as std::packaged_task&lt;R(ArgTypes...)&gt;. 
3) Constructs a std::experimental::packaged_task object with a shared state and a copy of the task, initialized with std::forward&lt;F&gt;(f). Uses the provided allocator to allocate memory necessary to store the task, which is treated as a type-erased allocator (see below). This constructor does not participate in overload resolution if std::decay&lt;F&gt;::type is the same type as std::packaged_task&lt;R(ArgTypes...)&gt;. 
4) The copy constructor is deleted, std::experimental::packaged_task is move-only. 
5) Constructs a std::experimental::packaged_task with the shared state and task formerly owned by rhs, leaving rhs with no shared state and a moved-from task. 
Type-erased allocator 
The constructors of packaged_task taking an allocator argument alloc treats that argument as a type-erased allocator. The memory resource pointer used by packaged_task to allocate memory is determined using the allocator argument (if specified) as follows: 
Type of alloc value of the memory resource pointer 
Non-existent (no allocator specified at time of construction) The value of std::experimental::pmr::get_default_resource() at time of construction. 
std::nullptr_t The value of std::experimental::pmr::get_default_resource() at time of construction 
A pointer type convertible to static_cast&lt;std::experimental::pmr::memory_resource*&gt;(alloc) 
std::experimental::pmr::memory_resource* 
A specialization of alloc.resource() 
std::experimental::pmr::polymorphic_allocator 
Any other type meeting the Allocator requirements A pointer to a value of type std::experimental::pmr::resource_adaptor&lt;A&gt;(alloc), where A is the type of alloc. The pointer remains valid only for the lifetime of the packaged_task object. 
None of the above The program is ill-formed. 

<h2>Parameters</h2>

f - the callable target <i>(function, member function, lambda-expression, functor) to execute</i> 
alloc - the allocator to use when storing the task 
rhs - the std::experimental::packaged_task to move from

<h2>Exceptions</h2>

2-3) Any exceptions thrown by copy/move constructor of f and possiblly std::bad_alloc if the allocation fails. 
4) <i>(none)</i>
