---
title: "stdtime_base(3)"
name: "stdtime_base"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdtime_base/"
description: "std::time_base – std::time_base"
---

<p>std::time_base &#8211; std::time_base</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;locale&gt;

class time_base;</code></pre>
<p>The class std::time_base provides the date order constants which are inherited by the std::time_get facets. </p>
<h2>Member types</h2>
<p>Member type Definition<br />
enum dateorder { no_order, dmy, mdy, ymd, ydm }; Unscoped enumeration type </p>
<p>Enumeration constant Definition<br />
no_order Unspecified order<br />
dmy Day, month, year (european) order<br />
mdy Month, day, year (american) order<br />
ymd Year, month, day<br />
ydm Year, day, month</p>
<h2>See also</h2>
<p>do_date_order obtains preferred ordering of day, month, and year<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::time_get&lt;CharT,InputIt&gt;)</i><br />
<code>[virtual]</code><br />
do_get_date extracts month, day, and year from input stream<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::time_get&lt;CharT,InputIt&gt;)</i><br />
<code>[virtual]</code> </p>
