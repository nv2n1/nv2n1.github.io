---
title: "stdallocate_sharedstdallocate_shared_default_init(3)"
name: "stdallocate_sharedstdallocate_shared_default_init"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdallocate_sharedstdallocate_shared_default_init/"
description: "std::allocate_shared,std::allocate_shared_default_init – std::allocate_shared,std::allocate_shared_default_init"
---

<p>std::allocate_shared,std::allocate_shared_default_init &#8211; std::allocate_shared,std::allocate_shared_default_init</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;memory&gt;<br />
template&lt; class T, class Alloc, class&#8230; Args &gt; <code>(1)</code> <i>(since C++11)</i><br />
shared_ptr&lt;T&gt; allocate_shared( const Alloc&amp; alloc, Args&amp;&amp;&#8230; args ); (T is non-array)<br />
template&lt; class T, class Alloc &gt; <code>(2)</code> <i>(since C++20)</i><br />
shared_ptr&lt;T&gt; allocate_shared( const Alloc&amp; alloc, std::size_t N ); (T is U[])<br />
template&lt; class T, class Alloc &gt; <code>(3)</code> <i>(since C++20)</i><br />
shared_ptr&lt;T&gt; allocate_shared( const Alloc&amp; alloc ); (T is U[N])<br />
template&lt; class T, class Alloc &gt; <i>(since C++20)</i><br />
shared_ptr&lt;T&gt; allocate_shared( const Alloc&amp; alloc, std::size_t N, <code>(4)</code> (T is U[])<br />
const std::remove_extent_t&lt;T&gt;&amp; u );<br />
template&lt; class T, class Alloc &gt; <i>(since C++20)</i><br />
shared_ptr&lt;T&gt; allocate_shared( const Alloc&amp; alloc, <code>(5)</code> (T is U[N])<br />
const std::remove_extent_t&lt;T&gt;&amp; u );<br />
template&lt; class T, class Alloc &gt; <code>(6)</code> <i>(since C++20)</i><br />
shared_ptr&lt;T&gt; allocate_shared_default_init( const Alloc&amp; alloc ); (T is not U[])<br />
template&lt; class T, class Alloc &gt; <code>(7)</code> <i>(since C++20)</i><br />
shared_ptr&lt;T&gt; allocate_shared_default_init( const Alloc&amp; alloc, std::size_t N ); (T is U[])<br />
1) Constructs an object of type T and wraps it in a std::shared_ptr using args as the parameter list for the constructor of T. The object is constructed as if by the expression std::allocator_traits&lt;A2&gt;::construct(a, pv, v), where pv is an internal void* pointer to storage suitable to hold an object of type T and a is a copy of the allocator rebound to std::remove_cv_t&lt;T&gt;. The storage is typically larger than sizeof(T) in order to use one allocation for both the control block of the shared pointer and the T object. The std::shared_ptr constructor called by this function enables shared_from_this with a pointer to the newly constructed object of type T. All memory allocation is done using a copy of alloc, which must satisfy the Allocator requirements. This overload only participates in overload resolution if T is not an array type<br />
2,3) Same as <code>(1)</code>, but the object constructed is a possibly-multidimensional array whose every non-array element is initialized as if by the expression std::allocator_traits&lt;A2&gt;::construct(a2, pv) where a2 of type A2 is the copy of the allocator rebound to manage objects of type std::remove_cv_t&lt;std::remove_all_extents_t&lt;T&gt;&gt;. The overload <code>(2)</code> creates an array of size N along its first dimension. The array elements are initialized in ascending order of their addresses, and when their lifetime ends are destroyed in the reverse order of their original construction.<br />
4,5) Same as (2,3), but the elements of the array are initialized from the default value u. If std::remove_extent_t&lt;T&gt; is not itself an array type, then this is performed as if by the same allocator expression as in <code>(1)</code>, except that the allocator is rebound to the std::remove_cv_t&lt;std::remove_all_extents_t&lt;T&gt;&gt;. Otherwise, this is performed as if by initializing every non-array element of the (possibly multidimensional) array with the corresponding element from u using the same allocator expression as in (1), except that the allocator is rebound to the type std::remove_cv_t&lt;std::remove_all_extents_t&lt;T&gt;&gt;. The overload <code>(4)</code> creates an array of size N along the first dimension. The array elements are initialized in ascending order of their addresses, and when their lifetime ends are destroyed in the reverse order of their original construction.<br />
6) Same as <code>(1)</code> if T is not an array type and <code>(3)</code> if T is U[N], except that the created object is default-initialized.<br />
7) Same as <code>(2)</code>, except that the individual array elements are default-initialized.<br />
For allocate_shared, the object<br />
(or the individual array elements for (2-5))<br />
<i>(since C++20)</i> are destroyed via the expression std::allocator_traits&lt;A2&gt;::destroy(a, p), where p is a pointer to the object and a is a copy of the allocator passed to allocate_shared, rebound to the type of the object being destroyed.<br />
For allocate_shared_default_init, the object (or individual elements if T is an array type) will be destroyed by p-&gt;~X(), where p is a pointer to the object and X is its type. <i>(since C++20)</i> </p>
<h2>Parameters</h2>
<p>alloc &#8211; The Allocator to use.<br />
args&#8230; &#8211; list of arguments with which an instance of T will be constructed.<br />
N &#8211; array size to use<br />
u &#8211; the initial value to initialize every element of the array</p>
<h2>Return value</h2>
<p>std::shared_ptr of an instance of type T. </p>
<h2>Exceptions</h2>
<p>Can throw the exceptions thrown from Alloc::allocate() or from the constructor of T. If an exception is thrown, <code>(1)</code> has no effect.<br />
If an exception is thrown during the construction of the array, already-initialized elements are destroyed in reverse order<br />
<i>(since C++20)</i></p>
<h2>Notes</h2>
<p>Like std::make_shared, this function typically performs only one allocation, and places both the T object and the control block in the allocated memory block (the standard recommends but does not require this, all known implementations do this). A copy of alloc is stored as part of the control block so that it can be used to deallocate it once both shared and weak reference counts reach zero.<br />
Unlike the std::shared_ptr constructors, std::allocate_shared does not accept a separate custom deleter: the supplied allocator is used for destruction of the control block and the T object, and for deallocation of their shared memory block.<br />
std::shared_ptr supports array types (as of C++17), but std::allocate_shared does not. This functionality is supported by boost::allocate_shared <i>(until C++20)</i><br />
A constructor enables shared_from_this with a pointer ptr of type U* means that it determines if U has an<br />
unambiguous and accessible<br />
<i>(since C++17)</i> base class that is a specialization of std::enable_shared_from_this, and if so, the constructor evaluates the statement: </p>
<pre><code>if (ptr != nullptr &amp;&amp; ptr-&gt;weak_this.expired())
    ptr-&gt;weak_this = std::shared_ptr&lt;std::remove_cv_t&lt;U&gt;&gt;(*this,
                                                          const_cast&lt;std::remove_cv_t&lt;U&gt; *&gt;(ptr));</code></pre>
<p>Where weak_this is the hidden mutable std::weak_ptr member of std::shared_from_this. The assignment to the weak_this member is not atomic and conflicts with any potentially concurrent access to the same object. This ensures that future calls to shared_from_this() would share ownership with the shared_ptr created by this raw pointer constructor.<br />
The test ptr-&gt;weak_this.expired() in the exposition code above makes sure that weak_this is not reassigned if it already indicates an owner. This test is required as of C++17. </p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs new shared_ptr<br />
constructor <i>(public member function)</i><br />
make_shared<br />
make_shared_default_init creates a shared pointer that manages a new object<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
(C++20) </p>
