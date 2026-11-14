---
title: "stdmake_sharedstdmake_shared_default_init(3)"
name: "stdmake_sharedstdmake_shared_default_init"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmake_sharedstdmake_shared_default_init/"
description: "std::make_shared,std::make_shared_default_init – std::make_shared,std::make_shared_default_init"
---

<p>std::make_shared,std::make_shared_default_init &#8211; std::make_shared,std::make_shared_default_init</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;memory&gt;<br />
template&lt; class T, class&#8230; Args &gt; <code>(1)</code> <i>(since C++11)</i><br />
shared_ptr&lt;T&gt; make_shared( Args&amp;&amp;&#8230; args ); (T is not array)<br />
template&lt;class T&gt; <code>(2)</code> <i>(since C++20)</i><br />
shared_ptr&lt;T&gt; make_shared( std::size_t N ); (T is U[])<br />
template&lt;class T&gt; <code>(3)</code> <i>(since C++20)</i><br />
shared_ptr&lt;T&gt; make_shared(); (T is U[N])<br />
template&lt;class T&gt; <code>(4)</code> <i>(since C++20)</i><br />
shared_ptr&lt;T&gt; make_shared( std::size_t N, const std::remove_extent_t&lt;T&gt;&amp; u ); (T is U[])<br />
template&lt;class T&gt; <code>(5)</code> <i>(since C++20)</i><br />
shared_ptr&lt;T&gt; make_shared( const std::remove_extent_t&lt;T&gt;&amp; u ); (T is U[N])<br />
template&lt;class T&gt; <code>(6)</code> <i>(since C++20)</i><br />
shared_ptr&lt;T&gt; make_shared_default_init(); (T is not U[])<br />
template&lt;class T&gt; <code>(7)</code> <i>(since C++20)</i><br />
shared_ptr&lt;T&gt; make_shared_default_init( std::size_t N ); (T is U[])<br />
1) Constructs an object of type T and wraps it in a std::shared_ptr using args as the parameter list for the constructor of T. The object is constructed as if by the expression ::new (pv) T(std::forward&lt;Args&gt;(args)&#8230;), where pv is an internal void* pointer to storage suitable to hold an object of type T. The storage is typically larger than sizeof(T) in order to use one allocation for both the control block of the shared pointer and the T object. The std::shared_ptr constructor called by this function enables shared_from_this with a pointer to the newly constructed object of type T. This overload only participates in overload resolution if T is not an array type<br />
2,3) Same as <code>(1)</code>, but the object constructed is a possibly-multidimensional array whose non-array elements of type std::remove_all_extents_t&lt;T&gt; are value-initialized as if by placement-new expression ::new(pv) std::remove_all_extents_t&lt;T&gt;(). The overload <code>(2)</code> creates an array of size N along the first dimension. The array elements are initialized in ascending order of their addresses, and when their lifetime ends are destroyed in the reverse order of their original construction.<br />
4,5) Same as (2,3), but every element is initialized from the default value u. If U is not an array type, then this is performed as if by the same placement-new expression as in <code>(1)</code>; otherwise, this is performed as if by initializing every non-array element of the (possibly multidimensional) array with the corresponding element from u with the same placement-new expression as in (1). The overload <code>(4)</code> creates an array of size N along the first dimension. The array elements are initialized in ascending order of their addresses, and when their lifetime ends are destroyed in the reverse order of their original construction.<br />
6) Same as <code>(1)</code> if T is not an array type and <code>(3)</code> if T is U[N], except that the created object is default-initialized.<br />
7) Same as <code>(2)</code>, except that the individual array elements are default-initialized.<br />
In each case, the object<br />
(or individual elements if T is an array type)<br />
<i>(since C++20)</i> will be destroyed by p-&gt;~X(), where p is a pointer to the object and X is its type. </p>
<h2>Parameters</h2>
<p>args &#8211; list of arguments with which an instance of T will be constructed.<br />
N &#8211; array size to use<br />
u &#8211; the initial value to initialize every element of the array</p>
<h2>Return value</h2>
<p>std::shared_ptr of an instance of type T. </p>
<h2>Exceptions</h2>
<p>May throw std::bad_alloc or any exception thrown by the constructor of T. If an exception is thrown, the functions have no effect.<br />
If an exception is thrown during the construction of the array, already-initialized elements are destroyed in reverse order.<br />
<i>(since C++20)</i></p>
<h2>Notes</h2>
<p>This function may be used as an alternative to std::shared_ptr&lt;T&gt;(new T(args&#8230;)). The trade-offs are:<br />
* std::shared_ptr&lt;T&gt;(new T(args&#8230;)) performs at least two allocations (one for the object T and one for the control block of the shared pointer), while std::make_shared&lt;T&gt; typically performs only one allocation (the standard recommends, but does not require this, all known implementations do this)<br />
* If any std::weak_ptr references the control block created by std::make_shared after the lifetime of all shared owners ended, the memory occupied by T persists until all weak owners get destroyed as well, which may be undesirable if sizeof(T) is large.<br />
* std::shared_ptr&lt;T&gt;(new T(args&#8230;)) may call a non-public constructor of T if executed in context where it is accessible, while std::make_shared requires public access to the selected constructor.<br />
* Unlike the std::shared_ptr constructors, std::make_shared does not allow a custom deleter.<br />
* std::make_shared uses ::new, so if any special behavior has been set up using a class-specific operator_new, it will differ from std::shared_ptr&lt;T&gt;(new T(args&#8230;)).<br />
* std::shared_ptr supports array types (as of C++17), but std::make_shared does not. This functionality is supported by boost::make_shared <i>(until C++20)</i><br />
* code such as f(std::shared_ptr&lt;int&gt;(new int<code>(42)</code>), g()) can cause a memory leak if g gets called after new int(42) and throws an exception, while f(std::make_shared&lt;int&gt;(42), g()) is safe, since two function calls are never_interleaved. <i>(until C++17)</i><br />
A constructor enables shared_from_this with a pointer ptr of type U* means that it determines if U has an<br />
unambiguous and accessible<br />
<i>(since C++17)</i> base class that is a specialization of std::enable_shared_from_this, and if so, the constructor evaluates the statement: </p>
<pre><code>if (ptr != nullptr &amp;&amp; ptr-&gt;weak_this.expired())
    ptr-&gt;weak_this = std::shared_ptr&lt;std::remove_cv_t&lt;U&gt;&gt;(*this,
                                                          const_cast&lt;std::remove_cv_t&lt;U&gt; *&gt;(ptr));</code></pre>
<p>Where weak_this is the hidden mutable std::weak_ptr member of std::shared_from_this. The assignment to the weak_this member is not atomic and conflicts with any potentially concurrent access to the same object. This ensures that future calls to shared_from_this() would share ownership with the shared_ptr created by this raw pointer constructor.<br />
The test ptr-&gt;weak_this.expired() in the exposition code above makes sure that weak_this is not reassigned if it already indicates an owner. This test is required as of C++17. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;memory&gt;

#include &lt;type_traits&gt;
struct C

{
    C(int i)
        : i(i)
    {
    } //&lt; constructor needed (until C++20)
    int i;
};
int main()

{
    auto sp = std::make_shared&lt;C&gt;(12);
    static_assert(std::is_same_v&lt;decltype(sp), std::shared_ptr&lt;C&gt;&gt;);
    std::cout &lt;&lt; sp-&gt;i &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;12</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs new shared_ptr<br />
constructor <i>(public member function)</i><br />
allocate_shared<br />
allocate_shared_default_init creates a shared pointer that manages a new object allocated using an allocator<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
(C++20)<br />
make_unique<br />
make_unique_default_init creates a unique pointer that manages a new object<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++14)</i><br />
(C++20)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;allocation functions<br />
operator_new <i>(function)</i><br />
operator_new[] </p>
