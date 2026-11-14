---
title: "std-codecvt-2(3)"
name: "std-codecvt-2"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std-codecvt-2/"
description: "std::codecvt_byname – std::codecvt_byname"
---

<h2 class="name">NAME</h2>
<p> std::codecvt_byname &#8211; std::codecvt_byname</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;locale&gt;<br />
template&lt; class InternT, class ExternT, class State &gt;<br />
class codecvt_byname : public std::codecvt&lt;InternT, ExternT, State&gt;; </p>
<p>std::codecvt_byname is a std::codecvt facet which encapsulates multibyte/wide character conversion rules of a locale specified at its construction.<br />
Four specializations are provided by the standard library </p>
<p>Defined in header &lt;locale&gt;<br />
std::codecvt_byname&lt;char, char, std::mbstate_t&gt; identity conversion<br />
std::codecvt_byname&lt;char16_t, char, std::mbstate_t&gt; conversion between UTF-16 and UTF-8 <i>(since C++11)</i>(deprecated in C++20)<br />
std::codecvt_byname&lt;char16_t, char8_t, std::mbstate_t&gt; conversion between UTF-16 and UTF-8 <i>(since C++20)</i><br />
std::codecvt_byname&lt;char32_t, char, std::mbstate_t&gt; conversion between UTF-32 and UTF-8 <i>(since C++11)</i>(deprecated in C++20)<br />
std::codecvt_byname&lt;char32_t, char8_t, std::mbstate_t&gt; conversion between UTF-32 and UTF-8 <i>(since C++20)</i><br />
std::codecvt_byname&lt;wchar_t, char, std::mbstate_t&gt; locale-specific conversion between wide string and narrow character sets </p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a new codecvt_byname facet<br />
constructor <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;destroys a codecvt_byname facet<br />
destructor <i>(protected member function)</i> </p>
<p>&nbsp;std::codecvt_byname::codecvt_byname </p>
<p>explicit codecvt_byname( const char* name, std::size_t refs = 0 );<br />
explicit codecvt_byname( const std::string&amp; name, std::size_t refs = 0 ); <i>(since C++11)</i> </p>
<p>Constructs a new std::codecvt_byname facet for a locale with name.<br />
refs is used for resource management: if refs == 0, the implementation destroys the facet, when the last std::locale object holding it is destroyed. Otherwise, the object is not destroyed. </p>
<h2>Parameters</h2>
<p>name &#8211; the name of the locale<br />
refs &#8211; the number of references that link to the facet </p>
<p>&nbsp;std::codecvt_byname::~codecvt_byname </p>
<p>protected:<br />
~codecvt_byname(); </p>
<p>Destroys the facet. </p>
<p>Inherited from std::codecvt </p>
<h2>Member types</h2>
<p>Member type Definition<br />
intern_type internT<br />
extern_type externT<br />
state_type stateT </p>
<h2>Member objects</h2>
<p>Member name Type<br />
id (static) std::locale::id </p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_out<br />
out <i>(public member function of std::codecvt&lt;InternT,ExternT,State&gt;)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_in<br />
in <i>(public member function of std::codecvt&lt;InternT,ExternT,State&gt;)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_unshift<br />
unshift <i>(public member function of std::codecvt&lt;InternT,ExternT,State&gt;)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_encoding<br />
encoding <i>(public member function of std::codecvt&lt;InternT,ExternT,State&gt;)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_always_noconv<br />
always_noconv <i>(public member function of std::codecvt&lt;InternT,ExternT,State&gt;)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_length<br />
length <i>(public member function of std::codecvt&lt;InternT,ExternT,State&gt;)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_max_length<br />
max_length <i>(public member function of std::codecvt&lt;InternT,ExternT,State&gt;)</i> </p>
<h2>Protected member functions</h2>
<p>do_out converts a string from internT to externT, such as when writing to file<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::codecvt&lt;InternT,ExternT,State&gt;)</i><br />
<code>[virtual]</code> </p>
<p>do_in converts a string from externT to internT, such as when reading from file<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::codecvt&lt;InternT,ExternT,State&gt;)</i><br />
<code>[virtual]</code> </p>
<p>do_unshift generates the termination character sequence of externT characters for incomplete conversion<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::codecvt&lt;InternT,ExternT,State&gt;)</i><br />
<code>[virtual]</code> </p>
<p>do_encoding returns the number of externT characters necessary to produce one internT character, if constant<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::codecvt&lt;InternT,ExternT,State&gt;)</i><br />
<code>[virtual]</code> </p>
<p>do_always_noconv tests if the facet encodes an identity conversion for all valid argument values<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::codecvt&lt;InternT,ExternT,State&gt;)</i><br />
<code>[virtual]</code> </p>
<p>do_length calculates the length of the externT string that would be consumed by conversion into given internT buffer<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::codecvt&lt;InternT,ExternT,State&gt;)</i><br />
<code>[virtual]</code> </p>
<p>do_max_length returns the maximum number of externT characters that could be converted into a single internT character<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::codecvt&lt;InternT,ExternT,State&gt;)</i><br />
<code>[virtual]</code> </p>
<p>Inherited from std::codecvt_base </p>
<p>Member type Definition<br />
enum result { ok, partial, error, noconv }; Unscoped enumeration type </p>
<p>Enumeration constant Definition<br />
ok conversion was completed with no error<br />
partial not all source characters were converted<br />
error encountered an invalid character<br />
noconv no conversion required, input and output types are the same </p>
<h2>Example</h2>
<p>This example demonstrates reading a GB18030-encoded file using the codecvt facet from a GB18030-aware locale<br />
 // Run this code </p>
<p>&nbsp;<wbr>&nbsp;#include &lt;iostream&gt;<br />
&nbsp;<wbr>&nbsp;#include &lt;fstream&gt;<br />
&nbsp;<wbr>&nbsp;#include &lt;string&gt;<br />
&nbsp;<wbr>&nbsp;#include &lt;locale&gt; </p>
<p>&nbsp;<wbr>&nbsp;int main()<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;// GB18030 narrow multibyte encoding<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::ofstream(&quot;text.txt&quot;) &lt;&lt; &quot;z&quot; // letter &#8216;z&#8217;, U+007a<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;�0�8&quot; // letter &#8216;ß&#8217;, U+00df<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;ˮ&quot; // CJK ideogram &#8216;水&#8217; (water), U+6c34<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;�2�5&quot;; // musical sign &#8221; (segno), U+1d10b<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::wifstream fin(&quot;text.txt&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fin.imbue(std::locale(fin.getloc(),<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;new std::codecvt_byname&lt;wchar_t, char, std::mbstate_t&gt;(&quot;zh_CN.gb18030&quot;)));<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (wchar_t c; fin.get(c); )<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::cout &lt;&lt; std::hex &lt;&lt; std::showbase &lt;&lt; c &lt;&lt; &#8216;
&#8217;;<br />
&nbsp;<wbr>&nbsp;} </p>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;0x7a<br />
&nbsp;<wbr>&nbsp;0xdf<br />
&nbsp;<wbr>&nbsp;0x6c34<br />
&nbsp;<wbr>&nbsp;0x1d10b </p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts between character encodings, including UTF-8, UTF-16, UTF-32<br />
codecvt <i>(class template)</i> </p>
<h2>Index</h2>
