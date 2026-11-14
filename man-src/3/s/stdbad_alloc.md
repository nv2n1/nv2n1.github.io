---
title: "stdbad_alloc(3)"
name: "stdbad_alloc"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbad_alloc/"
description: "std::bad_alloc – std::bad_alloc"
---

<p>std::bad_alloc &#8211; std::bad_alloc</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;new&gt;

class bad_alloc;</code></pre>
<p>std::bad_alloc is the type of the object thrown as exceptions by the allocation_functions to report failure to allocate storage.<br />
&nbsp;std-bad alloc-inheritance.svg<br />
Inheritance diagram </p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs the bad_alloc object<br />
constructor <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;replaces a bad_alloc object<br />
operator= <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns explanatory string<br />
what <i>(public member function)</i> </p>
<p>&nbsp;std::bad_alloc::bad_alloc </p>
<p>bad_alloc(); </p>
<p>Constructs new bad_alloc object with an implementation-defined null-terminated byte string which is accessible through what().</p>
<h2>Parameters</h2>
<p><i>(none)</i></p>
<h2>Exceptions</h2>
<p><i>(none)</i> <i>(until C++11)</i><br />
noexcept specification: <i>(since C++11)</i><br />
noexcept </p>
<p>&nbsp;std::bad_alloc::operator= </p>
<p>bad_alloc&amp; operator=( const bad_alloc&amp; other ); </p>
<p>Assigns the contents of other.</p>
<h2>Parameters</h2>
<p>other &#8211; another exception object to assign</p>
<h2>Return value</h2>
<p>*this </p>
<h2>Exceptions</h2>
<p><i>(none)</i> <i>(until C++11)</i><br />
noexcept specification: <i>(since C++11)</i><br />
noexcept </p>
<p>&nbsp;std::bad_alloc::what </p>
<p>virtual const char* what() const; </p>
<p>Returns the explanatory string.</p>
<h2>Parameters</h2>
<p><i>(none)</i></p>
<h2>Return value</h2>
<p>Pointer to a null-terminated string with explanatory information. </p>
<h2>Exceptions</h2>
<p><i>(none)</i> <i>(until C++11)</i><br />
noexcept specification: <i>(since C++11)</i><br />
noexcept </p>
<p>Inherited from std::exception</p>
<h2>Member functions</h2>
<p>destructor destroys the exception object<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual public member function of std::exception)</i><br />
<code>[virtual]</code> </p>
<p>what returns an explanatory string<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual public member function of std::exception)</i><br />
<code>[virtual]</code></p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;new&gt;
int main()

{
    try {
        while (true) {
            new int[100000000ul];
        }
    } catch (const std::bad_alloc &amp;e) {
        std::cout &lt;&lt; &quot;Allocation failed: &quot; &lt;&lt; e.what() &lt;&lt; '
';
    }
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;Allocation failed: std::bad_alloc</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;allocation functions<br />
operator_new <i>(function)</i><br />
operator_new[] </p>
