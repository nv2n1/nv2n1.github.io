---
title: "stdchronoduration_values(3)"
name: "stdchronoduration_values"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronoduration_values/"
description: "std::chrono::duration_values – std::chrono::duration_values"
---

<p>std::chrono::duration_values &#8211; std::chrono::duration_values</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;chrono&gt;

    template &lt;class Rep&gt;
    (since C++ 11)

        struct duration_values;</code></pre>
<p>The std::chrono::duration_values type defines three common durations:<br />
* std::chrono::duration_values::zero<br />
* std::chrono::duration_values::min<br />
* std::chrono::duration_values::max<br />
The zero, min, and max methods in std::chrono::duration forward their work to these methods.<br />
This type can be specialized if the representation Rep requires a specific implementation to return these duration objects. </p>
<h2>Member functions</h2>
<p>zero returns a zero-length representation<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code> </p>
<p>min returns the smallest possible representation<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code> </p>
<p>max returns the largest possible representation<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code></p>
