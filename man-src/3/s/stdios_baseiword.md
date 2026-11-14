---
title: "stdios_baseiword(3)"
name: "stdios_baseiword"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdios_baseiword/"
description: "std::ios_base::iword – std::ios_base::iword"
---

<p>std::ios_base::iword &#8211; std::ios_base::iword</p>
<h2>Synopsis</h2>
<pre><code>long &amp;iword(int index);</code></pre>
<p>First, allocates or resizes the private storage (dynamic array of long or another indexable data structure) sufficiently to make index a valid index, then returns a reference to the long element of the private storage with the index index.<br />
The reference may be invalidated by any operation on this ios_base object, including another call to iword(), but the stored values are retained, so that reading from iword(index) with the same index later will produce the same value (until the next call to std::basic_ios::copyfmt()). The value can be used for any purpose. The index of the element must be obtained by a previous call to xalloc(), otherwise the behavior is undefined. New elements are initialized to 0.<br />
If allocation fails, calls std::basic_ios&lt;&gt;::setstate(badbit) which may throw std::ios_base::failure </p>
<h2>Notes</h2>
<p>Typical use of iword storage is to pass information (e.g. custom formatting flags) from user-defined I/O manipulators to user-defined operator&lt;&lt; and operator&gt;&gt; or to user-defined formatting facets imbued into standard streams. </p>
<h2>Parameters</h2>
<p>index &#8211; index value of the element</p>
<h2>Return value</h2>
<p>A reference to the element. </p>
<h2>Exceptions</h2>
<p>May throw std::ios_base::failure when setting the badbit.</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;string&gt;
struct Foo {
    static int foo_xalloc;
    std::string data;
    Foo(const std::string &amp;s)
        : data(s)
    {
    }
};
// allocates the iword storage for use with Foo objects

int Foo::foo_xalloc = std::ios_base::xalloc();
// This user-defined operator&lt;&lt; prints the string in reverse if the iword holds 1

std::ostream &amp;operator&lt;&lt;(std::ostream &amp;os, Foo &amp;f)

{
    if (os.iword(Foo::foo_xalloc) == 1)
        return os &lt;&lt; std::string(f.data.rbegin(), f.data.rend());
    else
        return os &lt;&lt; f.data;
}
// This I/O manipulator flips the number stored in iword between 0 and 1

std::ios_base &amp;rev(std::ios_base &amp;os)

{
    os.iword(Foo::foo_xalloc) = !os.iword(Foo::foo_xalloc);
    return os;
}
int main()

{
    Foo f(&quot;example&quot;);
    std::cout &lt;&lt; f &lt;&lt; '
'
              &lt;&lt; rev &lt;&lt; f &lt;&lt; '
'
              &lt;&lt; rev &lt;&lt; f &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;example<br />
&nbsp;<wbr>&nbsp;elpmaxe<br />
&nbsp;<wbr>&nbsp;example</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;resizes the private storage if necessary and access to the void* element at the given index<br />
pword <i>(public member function)</i><br />
xalloc returns a program-wide unique integer that is safe to use as index to pword() and iword()<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code> </p>
