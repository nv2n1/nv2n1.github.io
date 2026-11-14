---
title: "stdchronononexistent_local_time(3)"
name: "stdchronononexistent_local_time"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronononexistent_local_time/"
description: "std::chrono::nonexistent_local_time – std::chrono::nonexistent_local_time"
---

<p>std::chrono::nonexistent_local_time &#8211; std::chrono::nonexistent_local_time</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;chrono&gt;<br />
class nonexistent_local_time; <i>(since C++20)</i><br />
Defines a type of object to be thrown as exception to report that an attempt was made to convert a nonexistent std::chrono::local_time to a std::chrono::sys_time without specifying a std::chrono::choose (such as choose::earliest or choose::latest).<br />
This exception is thrown by std::chrono::time_zone::to_sys and functions that call it (such as the constructors of std::chrono::zoned_time that takes a std::chrono::local_time).<br />
&nbsp;std-chrono-nonexistent local time-inheritance.svg<br />
Inheritance diagram </p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs the exception object<br />
constructor <i>(public member function)</i> </p>
<p>&nbsp;std::chrono::nonexistent_local_time::nonexistent_local_time </p>
<p>template&lt; class Duration &gt;<br />
nonexistent_local_time(const std::chrono::local_time&lt;Duration&gt;&amp; tp,<br />
const std::chrono::local_info&amp; i); </p>
<p>Constructs the exception object. The explanatory string returned by what() is equivalent to that produced by os.str() after the following code: </p>
<p>&nbsp;<wbr>&nbsp;std::ostringstream os;<br />
&nbsp;<wbr>&nbsp;os &lt;&lt; tp &lt;&lt; &quot; is in a gap between
&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;&lt; std::chrono::local_seconds(i.first.end.time_since_epoch()) + i.first.offset<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;&lt; &#8216; &#8216; &lt;&lt; i.first.abbrev &lt;&lt; &quot; and
&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;&lt; std::chrono::local_seconds(i.second.begin.time_since_epoch()) + i.second.offset<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;&lt; &#8216; &#8216; &lt;&lt; i.second.abbrev<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;&lt; &quot; which are both equivalent to
&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;&lt; i.first.end &lt;&lt; &quot; UTC&quot;; </p>
<p>Because copying a standard library class derived from std::exception is not permitted to throw exceptions, this message is typically stored internally as a separately-allocated reference-counted string.<br />
The behavior is undefined if i.result != std::chrono::local_info::nonexistent.</p>
<h2>Parameters</h2>
<p>tp &#8211; the time point for which conversion was attempted<br />
i &#8211; a std::chrono::local_info describing the result of the conversion attempt</p>
<h2>Exceptions</h2>
<p>May throw std::bad_alloc </p>
<p>Inherited from std::exception</p>
<h2>Member functions</h2>
<p>destructor destroys the exception object<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual public member function of std::exception)</i><br />
<code>[virtual]</code> </p>
<p>what returns an explanatory string<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual public member function of std::exception)</i><br />
<code>[virtual]</code></p>
