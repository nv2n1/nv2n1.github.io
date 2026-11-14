---
title: "stdliteralschrono_literalsoperatord(3)"
name: "stdliteralschrono_literalsoperatord"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdliteralschrono_literalsoperatord/"
description: "std::literals::chrono_literals::operator\"\"d – std::literals::chrono_literals::operator\"\"d"
---

<p>std::literals::chrono_literals::operator&quot;&quot;d &#8211; std::literals::chrono_literals::operator&quot;&quot;d</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;chrono&gt;<br />
constexpr std::chrono::day operator &quot;&quot;d(unsigned long long d) noexcept; <code>(1)</code> <i>(since C++20)</i><br />
Forms a std::chrono::day literal representing a day of the month in the calendar. </p>
<h2>Parameters</h2>
<p>d &#8211; the day value</p>
<h2>Return value</h2>
<p>A std::chrono::day storing d. If d &gt; 255, the stored value is unspecified. </p>
<h2>Possible implementation</h2>
<p>&nbsp;<wbr>&nbsp;constexpr std::chrono::day operator &quot;&quot;d(unsigned long long d) noexcept<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::chrono::day(d);<br />
&nbsp;<wbr>&nbsp;}</p>
<h2>Notes</h2>
<p>This operator is declared in the namespace std::literals::chrono_literals, where both literals and chrono_literals are inline namespaces. Access to this operator can be gained with using namespace std::literals, using namespace std::chrono_literals, and using namespace std::literals::chrono_literals.<br />
In addition, within the namespace std::chrono, the directive using namespace literals::chrono_literals; is provided by the standard library, so that if a programmer uses using namespace std::chrono; to gain access to the classes in the chrono library, the corresponding literal operators become visible as well. </p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a day<br />
constructor <i>(public member function of std::chrono::day)</i> </p>
