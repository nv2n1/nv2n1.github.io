---
title: "stdpointer_traits(3)"
name: "stdpointer_traits"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpointer_traits/"
description: "std::pointer_traits – std::pointer_traits"
---

<p>std::pointer_traits &#8211; std::pointer_traits</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;memory&gt;<br />
template&lt; class Ptr &gt; struct pointer_traits; <code>(1)</code> <i>(since C++11)</i><br />
template&lt; class T &gt; struct pointer_traits&lt;T*&gt;; <code>(2)</code> <i>(since C++11)</i><br />
The pointer_traits class template provides the standardized way to access certain properties of pointer-like types (fancy_pointers, such as boost::interprocess::offset_ptr). The standard template std::allocator_traits relies on pointer_traits to determine the defaults for various typedefs required by Allocator.<br />
1) The non-specialized pointer_traits declares the following types: </p>
<h2>Member types</h2>
<p>Type Definition<br />
pointer Ptr<br />
element_type Ptr::element_type if present. Otherwise T if Ptr is a template instantiation Template&lt;T, Args&#8230;&gt;<br />
difference_type Ptr::difference_type if present, otherwise std::ptrdiff_t</p>
<h2>Member alias templates</h2>
<p>Template Definition<br />
template &lt;class U&gt; using rebind Ptr::rebind&lt;U&gt; if exists, otherwise Template&lt;U, Args&#8230;&gt; if Ptr is a template instantiation Template&lt;T, Args&#8230;&gt;</p>
<h2>Member functions</h2>
<p>pointer_to obtains a dereferenceable pointer to its argument<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code> </p>
<p>2) A specialization is provided for pointer types, T*, which declares the following types</p>
<h2>Member types</h2>
<p>Type Definition<br />
pointer T*<br />
element_type T<br />
difference_type std::ptrdiff_t</p>
<h2>Member alias templates</h2>
<p>Template Definition<br />
template&lt; class U &gt; using rebind U*</p>
<h2>Member functions</h2>
<p>pointer_to obtains a dereferenceable pointer to its argument<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code> </p>
<p>3) A specialization for user-defined fancy pointer types may define an additional static member function </p>
<p>Optional Member functions </p>
<p>to_address obtains a raw pointer from a fancy pointer (inverse of pointer_to)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code> (C++20)</p>
<h2>Notes</h2>
<p>The rebind member template alias makes it possible, given a pointer-like type that points to T, to obtain the same pointer-like type that points to U. For example, </p>
<pre><code>using another_pointer = std::pointer_traits&lt;std::shared_ptr&lt;int&gt;&gt;::rebind&lt;double&gt;;

static_assert(std::is_same&lt;another_pointer, std::shared_ptr&lt;double&gt;&gt;::value);
</code></pre>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;memory&gt;

#include &lt;iostream&gt;
template &lt;class Ptr&gt;

struct BlockList

{
    // Predefine a memory block
    struct block;
    // Define a pointer to a memory block from the kind of pointer Ptr s
    // If Ptr is any kind of T*, block_ptr_t is block*
    // If Ptr is smart_ptr&lt;T&gt;, block_ptr_t is smart_ptr&lt;block&gt;
    using block_ptr_t = typename std::pointer_traits&lt;Ptr&gt;::template rebind&lt;block&gt;;
    struct block {
        std::size_t size;
        block_ptr_t next_block;
    };
    block_ptr_t free_blocks;
};
int main()

{
    BlockList&lt;int *&gt; bl1;
    // The type of bl1.free_blocks is block*
    BlockList&lt;std::shared_ptr&lt;char&gt;&gt; bl2;
    // The type of bl2.free_blocks is std::shared_ptr&lt;block&gt;
    std::cout &lt;&lt; bl2.free_blocks.use_count() &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;0</p>
<h2>See also</h2>
<p>allocator_traits provides information about allocator types<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
addressof obtains actual address of an object, even if the &amp; operator is overloaded<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++11)</i> </p>
