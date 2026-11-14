---
title: "std-codecvt-0(3)"
name: "std-codecvt-0"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std-codecvt-0/"
description: "std::codecvt<InternT,ExternT,State>::in,std::codecvt<InternT,ExternT,State>::do_in – std::codecvt<InternT,ExternT,State>::in,std::codecvt<InternT,ExternT,State>::do_in"
---

<h2 class="name">NAME</h2>
<p> std::codecvt&lt;InternT,ExternT,State&gt;::in,std::codecvt&lt;InternT,ExternT,State&gt;::do_in &#8211; std::codecvt&lt;InternT,ExternT,State&gt;::in,std::codecvt&lt;InternT,ExternT,State&gt;::do_in</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;locale&gt;<br />
public:<br />
result in( StateT&amp; state,<br />
const ExternT* from,<br />
const ExternT* from_end, <b>(1)</b><br />
const ExternT*&amp; from_next,<br />
InternT* to,<br />
InternT* to_end,<br />
InternT*&amp; to_next ) const;<br />
protected:<br />
virtual result do_in( StateT&amp; state,<br />
const ExternT* from,<br />
const ExternT* from_end, <b>(2)</b><br />
const ExternT*&amp; from_next,<br />
InternT* to,<br />
InternT* to_end,<br />
InternT*&amp; to_next ) const; </p>
<p>1) Public member function, calls the member function do_in of the most derived class.<br />
2) If this codecvt facet defines a conversion, translates the external characters from the source range [from, from_end) to internal characters, placing the results in the subsequent locations starting at to. Converts no more than from_end &#8211; from external characters and writes no more than to_end &#8211; to internal characters. Leaves from_next and to_next pointing one beyond the last element successfully converted.<br />
If this codecvt facet does not define a conversion, no characters are converted. to_next is set to be equal to to, state is unchanged, and std::codecvt_base::noconv is returned. </p>
<h2>Return value</h2>
<p>A value of type std::codecvt_base::result, indicating the success status as follows: </p>
<p>ok conversion completed<br />
partial not enough space in the output buffer or unexpected end of source buffer<br />
error encountered a character that could not be converted<br />
noconv this facet is non-converting, no output written </p>
<p>The non-converting specialization std::codecvt&lt;char, char, std::mbstate_t&gt; always returns std::codecvt_base::noconv </p>
<h2>Notes</h2>
<p>Requires that from &lt;= from_end &amp;&amp; to &lt;= to_end and that state either representing the initial shift state or obtained by converting the preceding characters in the sequence.<br />
The effect on state is deliberately unspecified. In standard facets, it is used to maintain shift state like when calling std::mbsrtowcs, and is therefore updated to reflect the conversion state after the last processed external character, but a user-defined facet is free to use it to maintain any other state, e.g. count the number of special characters encountered. </p>
<h2>Example</h2>
<pre><code>// Run this code
#include &lt;iostream&gt;
#include &lt;locale&gt;
#include &lt;string&gt;
int main() {
  std::locale::global(std::locale("en_US.utf8"));
  auto &amp;f = std::use_facet&lt;std::codecvt&lt;wchar_t, char, std::mbstate_t&gt;&gt;(
      std::locale());
  std::string external = u8"z\u00df\u6c34\U0001d10b"; // or u8"zß水"
  // or "\x7a\xc3\x9f\xe6\xb0\xb4\xf0\x9d\x84\x8b";
  // note that the following can be done with wstring_convert
  std::mbstate_t mb = std::mbstate_t(); // initial shift state
  std::wstring internal(external.size(), '\0');
  const char *from_next;
  wchar_t *to_next;
  f.in(mb, &amp;external[0], &amp;external[external.size()], from_next, &amp;internal[0],
       &amp;internal[internal.size()], to_next);
  // error checking skipped for brevity
  internal.resize(to_next - &amp;internal[0]);
  std::wcout &lt;&lt; L"The string in wide encoding: " &lt;&lt; internal &lt;&lt; '\n';
}</code></pre>
<h2>Output:</h2>
<pre><code>The string in wide encoding: zß水</code></pre>
<h2>See also</h2>
<p>underflow reads from the associated file<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::basic_filebuf&lt;CharT,Traits&gt;)</i><br />
<b>[virtual]</b><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts a byte string into a wide string<br />
from_bytes <i>(public member function of std::wstring_convert&lt;Codecvt,Elem,Wide_alloc,Byte_alloc&gt;)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts a narrow multibyte character string to wide string, given state<br />
mbsrtowcs <i>(function)</i> </p>
<p>do_out converts a string from internT to externT, such as when writing to file<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function)</i><br />
<b>[virtual]</b> </p>


