---
title: "stdchronolocal_info(3)"
name: "stdchronolocal_info"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronolocal_info/"
description: "std::chrono::local_info – std::chrono::local_info"
---

<p>std::chrono::local_info &#8211; std::chrono::local_info</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;chrono&gt;<br />
struct local_info; <i>(since C++20)</i><br />
The class local_info describes the result of converting a std::chrono::local_time to a std::chrono::sys_time.<br />
* If the result of the conversion is unique, then result == local_info::unique, first is filled out with the correct std::chrono::sys_info, and second is zero-initialized.<br />
* If the local_time is nonexistent, then result == local_info::nonexistent, first is filled out with the std::chrono::sys_info that ends just prior to the local_time, and second is filled out with the std::chrono::sys_info that begins just after the local_time.<br />
* If the local_time is ambiguous, then result == local_info::ambiguous, first is filled out with the std::chrono::sys_info that ends just after the local_time, and second is filled with the std::chrono::sys_info that starts just before the local_time.<br />
This is a low-level data structure; typical conversions from local_time to sys_time will use it implicitly rather than explicitly. </p>
<h2>Member constants</h2>
<p>Name Value </p>
<p>constexpr int unique 0<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
<p>constexpr int nonexistent 1<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
<p>constexpr int ambiguous 2<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code></p>
<h2>Member objects</h2>
<p>Member object Type<br />
result int<br />
first, second std::chrono::sys_info </p>
<p>Nonmember functions </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;outputs a local_info into a stream<br />
operator&lt;&lt; <i>(function template)</i></p>
