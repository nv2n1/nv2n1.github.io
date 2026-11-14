---
title: "stdstrstreambufseekoff(3)"
name: "stdstrstreambufseekoff"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdstrstreambufseekoff/"
description: "std::strstreambuf::seekoff – std::strstreambuf::seekoff"
---

<p>std::strstreambuf::seekoff &#8211; std::strstreambuf::seekoff</p>
<h2>Synopsis</h2>
<pre><code>protected:

virtual pos_type seekoff(off_type off,

ios_base::seekdir way,

ios_base::openmode which = ios_base::in | ios_base::out);</code></pre>
<p>Repositions std::basic_streambuf::gptr and/or std::basic_streambuf::pptr, if possible, to the position that corresponds to exactly off characters from beginning, end, or current position of the get and/or put area of the buffer.<br />
* If which includes ios_base::in and this buffer is open for reading, then repositions the read pointer std::basic_streambuf::gptr inside the get area as described below<br />
* If which includes ios_base::out and this buffer is open for writing, then repositions the write pointer std::basic_streambuf::pptr inside the put area as described below<br />
* If which includes both ios_base::in and ios_base::out and the buffer is open for both reading and writing, and when is either ios_base::beg or ios_base::end, then repositions both read and write pointers as described below.<br />
* Otherwise, this function fails.<br />
If the pointer (either gptr or pptr or both) is repositioned, it is done as follows:<br />
1) If the pointer to be repositioned is a null pointer and the new offset newoff would be non-zero, this function fails.<br />
2) The new pointer offset newoff of type off_type is determined<br />
a) if way == ios_base::beg, then newoff is zero<br />
b) if way == ios_base::cur, then newoff is the current position of the pointer (gptr()-eback() or pptr()-pbase())<br />
c) if way == ios_base::end, then newoff is the length of the entire initialized part of the buffer (if overallocation is used, the high watermark pointer minus the beginning pointer)<br />
3) If newoff + off is negative or out of bounds of the initialized part of the buffer, the function fails<br />
4) Otherwise, the pointer is assigned as if by gptr() = eback() + newoff + off or pptr() = pbase() + newoff + off </p>
<h2>Parameters</h2>
<p>off &#8211; relative position to set the next pointer(s) to<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;defines base position to apply the relative offset to. It can be one of the following constants: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Constant Explanation<br />
way &#8211; beg the beginning of a stream<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;end the ending of a stream<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cur the current position of stream position indicator </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;defines whether the input sequences, the output sequence, or both are affected. It can be one or a combination of the following constants: </p>
<p>which &#8211; Constant Explanation<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;in affect the input sequence<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;out affect the output sequence</p>
<h2>Return value</h2>
<p>pos_type(newoff) on success, pos_type(off_type(-1)) on failure and if pos_type cannot represent the resulting stream position. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;strstream&gt;
int main()

{
    char a[] = &quot;123&quot;;
    std::strstream ss(a, sizeof a); // in/out
    std::cout &lt;&lt; &quot;put pos = &quot; &lt;&lt; ss.tellp()
              &lt;&lt; &quot; get pos = &quot; &lt;&lt; ss.tellg() &lt;&lt; '
';
    // absolute positioning both pointers
    ss.rdbuf()-&gt;pubseekoff(1, std::ios_base::beg); // move both forward
    std::cout &lt;&lt; &quot;put pos = &quot; &lt;&lt; ss.tellp()
              &lt;&lt; &quot; get pos = &quot; &lt;&lt; ss.tellg() &lt;&lt; '
';
    // try to move both pointers 1 forward from current position
    if (-1 == ss.rdbuf()-&gt;pubseekoff(1, std::ios_base::cur))
        std::cout &lt;&lt; &quot;moving both pointers from current position failed
&quot;;
    std::cout &lt;&lt; &quot;put pos = &quot; &lt;&lt; ss.tellp()
              &lt;&lt; &quot; get pos = &quot; &lt;&lt; ss.tellg() &lt;&lt; '
';
    // move the write pointer 1 forward, but not the read pointer
    // can also be called as ss.seekp(1, std::ios_base::cur);
    ss.rdbuf()-&gt;pubseekoff(1, std::ios_base::cur, std::ios_base::out);
    std::cout &lt;&lt; &quot;put pos = &quot; &lt;&lt; ss.tellp()
              &lt;&lt; &quot; get pos = &quot; &lt;&lt; ss.tellg() &lt;&lt; '
';
    ss &lt;&lt; 'a'; // write at put position
    std::cout &lt;&lt; &quot;Wrote 'a' at put position, the buffer is now: '&quot;;
    std::cout.write(a, sizeof a);
    std::cout &lt;&lt; &quot;'
&quot;;
    char ch;
    ss &gt;&gt; ch;
    std::cout &lt;&lt; &quot;reading at get position gives '&quot; &lt;&lt; ch &lt;&lt; &quot;'
&quot;;
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;put pos = 0 get pos = 0<br />
&nbsp;<wbr>&nbsp;put pos = 1 get pos = 1<br />
&nbsp;<wbr>&nbsp;moving both pointers from current position failed<br />
&nbsp;<wbr>&nbsp;put pos = 1 get pos = 1<br />
&nbsp;<wbr>&nbsp;put pos = 2 get pos = 1<br />
&nbsp;<wbr>&nbsp;Wrote &#8216;a&#8217; at put position, the buffer is now: &#8217;12a&#8217;<br />
&nbsp;<wbr>&nbsp;reading at get position gives &#8216;2&#8217;</p>
<h2>See also</h2>
<p>seekpos repositions the next pointer in the input sequence, output sequence, or both using absolute addressing<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::basic_streambuf&lt;CharT,Traits&gt;)</i><br />
<code>[virtual]</code><br />
seekoff repositions the next pointer in the input sequence, output sequence, or both, using relative addressing<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::basic_streambuf&lt;CharT,Traits&gt;)</i><br />
<code>[virtual]</code><br />
seekoff repositions the next pointer in the input sequence, output sequence, or both, using relative addressing<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::basic_stringbuf&lt;CharT,Traits,Allocator&gt;)</i><br />
<code>[virtual]</code><br />
seekoff repositions the file position, using relative addressing<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::basic_filebuf&lt;CharT,Traits&gt;)</i><br />
<code>[virtual]</code> </p>
