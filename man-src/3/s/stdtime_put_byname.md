---
title: "stdtime_put_byname(3)"
name: "stdtime_put_byname"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdtime_put_byname/"
description: "std::time_put_byname – std::time_put_byname"
---

<p>std::time_put_byname &#8211; std::time_put_byname</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;locale&gt;

template&lt; class CharT, class OutputIterator = std::ostreambuf_iterator&lt;CharT&gt; &gt;

class time_put_byname : public std::time_put&lt;CharT, OutputIterator&gt;;</code></pre>
<p>std::time_put_byname is a std::time_put facet which encapsulates time and date formatting rules of the locale specified at its construction.<br />
Two specializations are provided by the standard library<br />
Defined in header &lt;locale&gt;<br />
std::time_put_byname&lt;char, OutputIterator&gt; narrow/multibyte time formatting<br />
std::time_put_byname&lt;wchar_t, OutputIterator&gt; wide string time formatting </p>
<h2>Member types</h2>
<p>Member type Definition<br />
char_type CharT<br />
iter_type OutputIterator</p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a new time_put_byname facet<br />
constructor <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;destroys a time_put_byname facet<br />
destructor <i>(protected member function)</i> </p>
<p>&nbsp;std::time_put_byname::time_put_byname </p>
<p>explicit time_put_byname( const char* name, std::size_t refs = 0 );<br />
explicit time_put_byname( const std::string&amp; name, std::size_t refs = 0 ); <i>(since C++11)</i> </p>
<p>Constructs a new std::time_put_byname facet for a locale with name.<br />
refs is used for resource management: if refs == 0, the implementation destroys the facet, when the last std::locale object holding it is destroyed. Otherwise, the object is not destroyed.</p>
<h2>Parameters</h2>
<p>name &#8211; the name of the locale<br />
refs &#8211; the number of references that link to the facet </p>
<p>&nbsp;std::time_put_byname::~time_put_byname </p>
<p>protected:<br />
~time_put_byname(); </p>
<p>Destroys the facet. </p>
<p>Inherited from std::time_put</p>
<h2>Member objects</h2>
<p>Member name Type<br />
id (static) std::locale::id</p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_put<br />
put <i>(public member function of std::time_put&lt;CharT,OutputIt&gt;)</i></p>
<h2>Protected member functions</h2>
<p>do_put formats date/time and writes to output stream<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::time_put&lt;CharT,OutputIt&gt;)</i><br />
<code>[virtual]</code></p>
<h2>Example</h2>
<p>This example prints current time using the &quot;C&quot; locale with the time_put facet replaced by various time_put_byname facets<br />
 // Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;ctime&gt;

#include &lt;iomanip&gt;

#include &lt;codecvt&gt;
int main()

{
    std::time_t t = std::time(NULL);
    std::wbuffer_convert&lt;std::codecvt_utf8&lt;wchar_t&gt;&gt; conv(std::cout.rdbuf());
    std::wostream out(&amp;conv);
    out.imbue(std::locale(out.getloc(),
                          new std::time_put_byname&lt;wchar_t&gt;(&quot;ja_JP&quot;)));
    out &lt;&lt; std::put_time(std::localtime(&amp;t), L&quot;%A %c&quot;) &lt;&lt; '
';
    out.imbue(std::locale(out.getloc(),
                          new std::time_put_byname&lt;wchar_t&gt;(&quot;ru_RU.utf8&quot;)));
    out &lt;&lt; std::put_time(std::localtime(&amp;t), L&quot;%A %c&quot;) &lt;&lt; '
';
    out.imbue(std::locale(out.getloc(),
                          new std::time_put_byname&lt;wchar_t&gt;(&quot;sv_SE.utf8&quot;)));
    out &lt;&lt; std::put_time(std::localtime(&amp;t), L&quot;%A %c&quot;) &lt;&lt; '
';
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;木曜日 2012年08月09日 21時41分02秒<br />
&nbsp;<wbr>&nbsp;Четверг Чт. 09 авг. 2012 21:41:02<br />
&nbsp;<wbr>&nbsp;torsdag tor 9 aug 2012 21:41:02</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;formats contents of struct std::tm for output as character sequence<br />
time_put <i>(class template)</i> </p>
