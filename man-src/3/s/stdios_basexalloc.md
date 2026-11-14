---
title: "stdios_basexalloc(3)"
name: "stdios_basexalloc"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdios_basexalloc/"
---

std::ios_base::xalloc - std::ios_base::xalloc

<h2>Synopsis</h2>

<pre><code>static int xalloc();</code></pre> 
Returns a unique (program-wide) index value that can be used to access one long and one void* elements in the private storage of std::ios_base by calling iword() and pword(). The call to xalloc does not allocate memory. 
This function is thread-safe; concurrent access by multiple threads does not result in a data race. 
<i>(since C++14)</i> 
Effectively increments a private static data member of std::ios_base, as if by executing return index++;, if index is the name of that static member 
(which may be std::atomic to support concurrent access by multiple threads, or otherwise synchronized) 
<i>(since C++14)</i> 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

Unique integer for use as pword/iword index. 

<h2>Example</h2>

Uses base class pword storage for runtime type identification of derived stream objects. 
 // Run this code <pre><code>#include &lt;iostream&gt;
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
    std::cout &lt;&lt; &quot;cout, narrow-character test &quot; &lt;&lt; mymanip &lt;&lt; '\n';
    mystream&lt;char&gt; myout(std::cout);
    myout &lt;&lt; &quot;myout, narrow-character test &quot; &lt;&lt; mymanip &lt;&lt; '\n';
    std::wcout &lt;&lt; &quot;wcout, wide-character test &quot; &lt;&lt; mymanip &lt;&lt; '\n';
    mystream&lt;wchar_t&gt; mywout(std::wcout);
    mywout &lt;&lt; &quot;mywout, wide-character test &quot; &lt;&lt; mymanip &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;cout, narrow-character test 
&nbsp;<wbr>&nbsp;myout, narrow-character test [special handling for mystream] 
&nbsp;<wbr>&nbsp;wcout, wide-character test 
&nbsp;<wbr>&nbsp;mywout, wide-character test [special handling for mystream]

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;resizes the private storage if necessary and access to the void* element at the given index 
pword <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;resizes the private storage if necessary and access to the long element at the given index 
iword <i>(public member function)</i> 
