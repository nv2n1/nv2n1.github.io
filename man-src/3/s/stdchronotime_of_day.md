---
title: "stdchronotime_of_day(3)"
name: "stdchronotime_of_day"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronotime_of_day/"
description: "std::chrono::time_of_day – std::chrono::time_of_day"
---

<p>std::chrono::time_of_day &#8211; std::chrono::time_of_day</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;chrono&gt;

template&lt; class Duration &gt;                             (1) (since C++20)

class time_of_day; // not defined

template&lt;&gt;                                             (2) (since C++20)

class time_of_day&lt;std::chrono::hours&gt;;

template&lt;&gt;                                             (3) (since C++20)

class time_of_day&lt;std::chrono::minutes&gt;;

template&lt;&gt;                                             (4) (since C++20)

class time_of_day&lt;std::chrono::seconds&gt;;

template&lt; class Rep, class Period &gt;                    (5) (since C++20)

class time_of_day&lt;std::chrono::duration&lt;Rep, Period&gt;&gt;;</code></pre>
<p>The class template time_of_day splits a std::chrono::duration representing time since midnight into a &quot;broken down&quot; time such as hours:minutes:seconds, with the precision of the split determined by the Duration template parameter. It also tracks whether it should be output in a 12-hour time format or a 24-hour time format. It is primarily a formatting tool.<br />
The primary template <code>(1)</code> is not defined; four specializations are provided to handle four different levels of precision.<br />
Each specialization of time_of_day is a TriviallyCopyable StandardLayoutType.<br />
The partial specialization <code>(5)</code> only exists if std::chrono::treat_as_floating_point_v&lt;Rep&gt; is false and std::chrono::duration&lt;Rep, Period&gt; is not convertible to std::chrono::seconds. </p>
<h2>Member types</h2>
<p>Member type Definition<br />
precision Duration</p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a time_of_day<br />
constructor <i>(public member function)</i> </p>
<p>hours accesses components of the broken-down time<br />
minutes <i>(public member function)</i><br />
seconds<br />
subseconds<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;accesses the stored std::chrono::duration<br />
operator_precision <i>(public member function)</i><br />
to_duration<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;changes the time format used for output<br />
make12 <i>(public member function)</i><br />
make24 </p>
<p>Nonmember functions </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;outputs a time_of_day into a stream<br />
operator&lt;&lt; <i>(function template)</i></p>
