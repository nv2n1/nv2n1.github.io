---
title: "stdbasic_streambuf(3)"
name: "stdbasic_streambuf"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbasic_streambuf/"
---

std::basic_streambuf&lt;CharT,Traits&gt;::~basic_streambuf - std::basic_streambuf&lt;CharT,Traits&gt;::~basic_streambuf

<h2>Synopsis</h2>

<pre><code>virtual ~basic_streambuf();</code></pre> 
This destruction is empty: the members of this basic_streambuf (the pointers and the locale) are destructed in accordance with the usual object destruction sequence after this destructor returns. However, since it is declared public virtual, it allows the objects that are derived from std::basic_streambuf to be deleted through a pointer to base class. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;fstream&gt;
int main()

{
    std::filebuf *fbp = new std::filebuf;
    fbp-&gt;open(&quot;test.txt&quot;, std::ios_base::out);
    fbp-&gt;sputn(&quot;Hello\n&quot;, 6);
    std::streambuf *sbp = fbp;
    delete sbp; // the file is closed, output flushed and written
    std::ifstream f(&quot;test.txt&quot;);
    std::cout &lt;&lt; f.rdbuf(); // proof
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Hello

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a basic_streambuf object 
constructor <i>(protected member function)</i> 
