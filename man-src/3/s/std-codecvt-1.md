---
title: "std-codecvt-1(3)"
name: "std-codecvt-1"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std-codecvt-1/"
description: "std::codecvt<InternT,ExternT,State>::length,do_length – std::codecvt<InternT,ExternT,State>::length,do_length"
---

<h2 class="name">NAME</h2>
<p> std::codecvt&lt;InternT,ExternT,State&gt;::length,do_length &#8211; std::codecvt&lt;InternT,ExternT,State&gt;::length,do_length</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;locale&gt;<br />
public:<br />
int length( StateT&amp; state,<br />
const ExternT* from, <b>(1)</b><br />
const ExternT* from_end,<br />
std::size_t max ) const;<br />
protected:<br />
virtual int do_length( StateT&amp; state,<br />
const ExternT* from, <b>(2)</b><br />
const ExternT* from_end,<br />
std::size_t max ) const; </p>
<p>1) public member function, calls the member function do_length of the most derived class.<br />
2) attempts to convert the externT characters from the character array defined by [from, from_end), given initial conversion state state, to at most max internT characters, and returns the number of externT characters that such conversion would consume. Modifies state as if by executing do_in(state, from, from_end, from, to, to+max, to) for some imaginary [to, to+max) output buffer. </p>
<h2>Return value</h2>
<p>The number of externT characters that would be consumed if converted by do_in() until either all from_end-from characters were consumed or max internT characters were produced, or a conversion error occurred.<br />
The non-converting specialization std::codecvt&lt;char, char, std::mbstate_t&gt; returns std::min(max, from_end-from) </p>
<h2>Example</h2>
<pre><code>// Run this code
#include &lt;iostream&gt;
#include &lt;locale&gt;
#include &lt;string&gt;
int main() {
  // narrow multibyte encoding
  std::string s = "z\u00df\u6c34\U0001d10b"; // or u8"zß水"
  // or "\x7a\xc3\x9f\xe6\xb0\xb4\xf0\x9d\x84\x8b";
  std::mbstate_t mb = std::mbstate_t();
  std::cout &lt;&lt; "Only the first "
            &lt;&lt; std::use_facet&lt;std::codecvt&lt;wchar_t, char, std::mbstate_t&gt;&gt;(
                   std::locale("en_US.utf8"))
                   .length(mb, &amp;s[0], &amp;s[s.size()], 2)
            &lt;&lt; " bytes out of " &lt;&lt; s.size()
            &lt;&lt; " would be consumed "
               " to produce the first 2 characters\n";
}</code></pre>
<h2>Output:</h2>
<pre><code>Only the first 3 bytes out of 10 would be consumed to produce the first 2 characters</code></pre>
<h2>See also</h2>
<p>do_in converts a string from externT to internT, such as when reading from file<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function)</i><br />
<b>[virtual]</b> </p>


