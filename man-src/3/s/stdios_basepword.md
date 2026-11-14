---
title: "stdios_basepword(3)"
name: "stdios_basepword"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdios_basepword/"
description: "std::ios_base::pword – std::ios_base::pword"
---

<p>std::ios_base::pword &#8211; std::ios_base::pword</p>
<h2>Synopsis</h2>
<pre><code>void *&amp;pword(int index);</code></pre>
<p>First, allocates or resizes the private storage (dynamic array of void* or another indexable data structure) sufficiently to make index a valid index, then returns a reference to the void* element of the private storage with the index index.<br />
The reference may be invalidated by any operation on this ios_base object, including another call to pword(), but the stored values are retained, so that reading from pword(index) with the same index later will produce the same value (until the next call to copyfmt()). The value can be used for any purpose. The index of the element must be obtained by xalloc(), otherwise the behavior is undefined. New elements are initialized to NULL.<br />
If allocation fails, calls std::basic_ios&lt;&gt;::setstate(badbit) which may throw std::ios_base::failure </p>
<h2>Parameters</h2>
<p>index &#8211; index value of the element</p>
<h2>Return value</h2>
<p>A reference to the element. </p>
<h2>Exceptions</h2>
<p>May throw std::ios_base::failure when setting the badbit.</p>
<h2>Notes</h2>
<p>If the pointers stored in pword require management, register_callback() may be used to install handlers that execute deep copy or deallocation as needed. </p>
<h2>Example</h2>
<p>Uses base class pword storage for runtime type identification of derived stream objects.<br />
 // Run this code </p>
<pre><code>#include &lt;iostream&gt;
template &lt;class charT, class traits = std::char_traits&lt;charT&gt;&gt;

class mystream : public std::basic_ostream&lt;charT, traits&gt;

{
  public:
    static const int xindex;
    mystream(std::basic_ostream&lt;charT, traits&gt; &amp;ostr)
        : std::basic_ostream&lt;charT, traits&gt;(ostr.rdbuf())
    {
        this-&gt;pword(xindex) = this;
    }
    void myfn()
    {
        *this &lt;&lt; &quot;[special handling for mystream]&quot;;
    }
};
// each specialization of mystream obtains a unique index from xalloc()

template &lt;class charT, class traits&gt;

const int mystream&lt;charT, traits&gt;::xindex = std::ios_base::xalloc();
// This I/O manipulator will be able to recognize ostreams that are mystreams

// by looking up the pointer stored in pword

template &lt;class charT, class traits&gt;

std::basic_ostream&lt;charT, traits&gt; &amp;mymanip(std::basic_ostream&lt;charT, traits&gt; &amp;os)

{
    if (os.pword(mystream&lt;charT, traits&gt;::xindex) == &amp;os)
        static_cast&lt;mystream&lt;charT, traits&gt; &amp;&gt;(os).myfn();
    return os;
}
int main()

{
    std::cout &lt;&lt; &quot;cout, narrow-character test &quot; &lt;&lt; mymanip &lt;&lt; '
';
    mystream&lt;char&gt; myout(std::cout);
    myout &lt;&lt; &quot;myout, narrow-character test &quot; &lt;&lt; mymanip &lt;&lt; '
';
    std::wcout &lt;&lt; &quot;wcout, wide-character test &quot; &lt;&lt; mymanip &lt;&lt; '
';
    mystream&lt;wchar_t&gt; mywout(std::wcout);
    mywout &lt;&lt; &quot;mywout, wide-character test &quot; &lt;&lt; mymanip &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;cout, narrow-character test<br />
&nbsp;<wbr>&nbsp;myout, narrow-character test [special handling for mystream]<br />
&nbsp;<wbr>&nbsp;wcout, wide-character test<br />
&nbsp;<wbr>&nbsp;mywout, wide-character test [special handling for mystream]</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;resizes the private storage if necessary and access to the long element at the given index<br />
iword <i>(public member function)</i><br />
xalloc returns a program-wide unique integer that is safe to use as index to pword() and iword()<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code> </p>
