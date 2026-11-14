---
title: "stdtime_get_byname(3)"
name: "stdtime_get_byname"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdtime_get_byname/"
description: "std::time_get_byname – std::time_get_byname"
---

<p>std::time_get_byname &#8211; std::time_get_byname</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;locale&gt;

template&lt;

class CharT,

class InputIt = std::istreambuf_iterator&lt;CharT&gt;

&gt; class time_get_byname : public std::time_get&lt;CharT, InputIt&gt;</code></pre>
<p>std::time_get_byname is a std::time_get facet which encapsulates time and date parsing rules of the locale specified at its construction.<br />
Two specializations are provided by the standard library<br />
Defined in header &lt;locale&gt;<br />
std::time_get_byname&lt;char, InputIt&gt; narrow/multibyte time parsing<br />
std::time_get_byname&lt;wchar_t, InputIt&gt; wide string time parsing </p>
<h2>Member types</h2>
<p>Member type Definition<br />
char_type CharT<br />
iter_type InputIt</p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a new time_get_byname facet<br />
constructor <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;destroys a time_get_byname facet<br />
destructor <i>(protected member function)</i> </p>
<p>&nbsp;std::time_get_byname::time_get_byname </p>
<p>explicit time_get_byname( const char* name, std::size_t refs = 0 );<br />
explicit time_get_byname( const std::string&amp; name, std::size_t refs = 0 ); <i>(since C++11)</i> </p>
<p>Constructs a new std::time_get_byname facet for a locale with name.<br />
refs is used for resource management: if refs == 0, the implementation destroys the facet, when the last std::locale object holding it is destroyed. Otherwise, the object is not destroyed.</p>
<h2>Parameters</h2>
<p>name &#8211; the name of the locale<br />
refs &#8211; the number of references that link to the facet </p>
<p>&nbsp;std::time_get_byname::~time_get_byname </p>
<p>protected:<br />
~time_get_byname(); </p>
<p>Destroys the facet. </p>
<p>Inherited from std::time_get </p>
<p>Member type Definition<br />
char_type CharT<br />
iter_type InputIt</p>
<h2>Member objects</h2>
<p>Member name Type<br />
id (static) std::locale::id</p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_date_order<br />
date_order <i>(public member function of std::time_get&lt;CharT,InputIt&gt;)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_get_time<br />
get_time <i>(public member function of std::time_get&lt;CharT,InputIt&gt;)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_get_date<br />
get_date <i>(public member function of std::time_get&lt;CharT,InputIt&gt;)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_get_weekday<br />
get_weekday <i>(public member function of std::time_get&lt;CharT,InputIt&gt;)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_get_monthname<br />
get_monthname <i>(public member function of std::time_get&lt;CharT,InputIt&gt;)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_get_year<br />
get_year <i>(public member function of std::time_get&lt;CharT,InputIt&gt;)</i> </p>
<p>get invokes do_get<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function of std::time_get&lt;CharT,InputIt&gt;)</i><br />
<i>(C++11)</i></p>
<h2>Protected member functions</h2>
<p>do_date_order obtains preferred ordering of day, month, and year<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::time_get&lt;CharT,InputIt&gt;)</i><br />
<code>[virtual]</code> </p>
<p>do_get_time extracts hours, minutes, and seconds from input stream<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::time_get&lt;CharT,InputIt&gt;)</i><br />
<code>[virtual]</code> </p>
<p>do_get_date extracts month, day, and year from input stream<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::time_get&lt;CharT,InputIt&gt;)</i><br />
<code>[virtual]</code> </p>
<p>do_get_weekday extracts the name of a day of the week from input stream<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::time_get&lt;CharT,InputIt&gt;)</i><br />
<code>[virtual]</code> </p>
<p>do_get_monthname extacts a month name from input stream<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::time_get&lt;CharT,InputIt&gt;)</i><br />
<code>[virtual]</code> </p>
<p>do_get_year extracts a year from input stream<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::time_get&lt;CharT,InputIt&gt;)</i><br />
<code>[virtual]</code> </p>
<p>do_get extracts date/time components from input stream, according to the specified format<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::time_get&lt;CharT,InputIt&gt;)</i><br />
<code>[virtual]</code> <i>(C++11)</i> </p>
<p>Inherited from std::time_base </p>
<p>Type Definition<br />
dateorder date order enumeration type, defining the values no_order, dmy, mdy, ymd, and ydm</p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;parses time/date values from an input character sequence into struct std::tm<br />
time_get <i>(class template)</i><br />
get_time parses a date/time value of specified format<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++11)</i> </p>
