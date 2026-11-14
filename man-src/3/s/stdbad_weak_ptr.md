---
title: "stdbad_weak_ptr(3)"
name: "stdbad_weak_ptr"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbad_weak_ptr/"
description: "std::bad_weak_ptr – std::bad_weak_ptr"
---

<p>std::bad_weak_ptr &#8211; std::bad_weak_ptr</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;memory&gt;<br />
class bad_weak_ptr; <i>(since C++11)</i><br />
std::bad_weak_ptr is the type of the object thrown as exceptions by the constructors of std::shared_ptr that take std::weak_ptr as the argument, when the std::weak_ptr refers to an already deleted object.<br />
&nbsp;std-bad weak ptr-inheritance.svg<br />
Inheritance diagram </p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs the bad_weak_ptr object<br />
constructor <i>(public member function)</i> </p>
<p>&nbsp;std::bad_weak_ptr ::bad_weak_ptr() </p>
<p>bad_weak_ptr() noexcept; </p>
<p>Constructs a new instance of std::bad_weak_ptr. what() returns an implementation-defined null-terminated byte string.</p>
<h2>Parameters</h2>
<p><i>(none)</i> </p>
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
<pre><code>#include &lt;memory&gt;

#include &lt;iostream&gt;

int main()

{
    std::shared_ptr&lt;int&gt; p1(new int(42));
    std::weak_ptr&lt;int&gt; wp(p1);
    p1.reset();
    try {
        std::shared_ptr&lt;int&gt; p2(wp);
    } catch (const std::bad_weak_ptr &amp;e) {
        std::cout &lt;&lt; e.what() &lt;&lt; '
';
    }
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;std::bad_weak_ptr</p>
<h2>See also</h2>
<p>shared_ptr smart pointer with shared object ownership semantics<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
weak_ptr weak reference to an object managed by std::shared_ptr<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i> </p>
