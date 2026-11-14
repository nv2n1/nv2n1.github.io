---
title: "deductionguidesforstdchronozoned_time(3)"
name: "deductionguidesforstdchronozoned_time"
section: "3"
letter: "d"
url: "/docs/linux/man/3-deductionguidesforstdchronozoned_time/"
description: "Deductionguidesforstd::chrono::zoned_time – Deductionguidesforstd::chrono::zoned_time"
---

<p>Deductionguidesforstd::chrono::zoned_time &#8211; Deductionguidesforstd::chrono::zoned_time</p>
<h2>Synopsis</h2>
<p>zoned_time() -&gt; zoned_time&lt;std::chrono::seconds&gt;; <code>(1)</code> <i>(since C++20)</i><br />
template&lt; class Duration &gt;<br />
zoned_time(std::chrono::sys_time&lt;Duration&gt;) <code>(2)</code> <i>(since C++20)</i><br />
-&gt; zoned_time&lt;std::common_type_t&lt;Duration, std::chrono::seconds&gt;&gt;;<br />
template&lt; class TimeZonePtrOrName &gt; <code>(3)</code> <i>(since C++20)</i><br />
zoned_time(TimeZonePtrOrName) -&gt; zoned_time&lt;std::chrono::seconds, /* see below */&gt;;<br />
template&lt; class TimeZonePtrOrName, class Duration &gt;<br />
zoned_time(TimeZonePtrOrName, std::chrono::sys_time&lt;Duration&gt;) <code>(4)</code> <i>(since C++20)</i><br />
-&gt; zoned_time&lt;std::common_type_t&lt;Duration, std::chrono::seconds&gt;, /* see below */&gt;;<br />
template&lt; class TimeZonePtrOrName, class Duration &gt;<br />
zoned_time(TimeZonePtrOrName, std::chrono::local_time&lt;Duration&gt;, <code>(5)</code> <i>(since C++20)</i><br />
std::chrono::choose = std::chrono::choose::earliest)<br />
-&gt; zoned_time&lt;std::common_type_t&lt;Duration, std::chrono::seconds&gt;, /* see below */&gt;;<br />
template&lt; class TimeZonePtrOrName, class Duration, class TimeZonePtr2 &gt;<br />
zoned_time(TimeZonePtrOrName, std::chrono::zoned_time&lt;Duration, TimeZonePtr2&gt;, <code>(6)</code> <i>(since C++20)</i><br />
std::chrono::choose = std::chrono::choose::earliest)<br />
-&gt; zoned_time&lt;std::common_type_t&lt;Duration, std::chrono::seconds&gt;, /* see below */&gt;; </p>
<p>Six deduction guides are provided for zoned_time. They normalize Duration to a minimum resolution of std::chrono::seconds, and provide correct handling for time zone names specified using types convertible to std::string_view.<br />
3-6) If std::is_convertible_v&lt;TimeZonePtrOrName, std::string_view&gt; is true, the deduced second template argument is const std::chrono::time_zone*. Otherwise it is TimeZonePtrOrName.</p>
