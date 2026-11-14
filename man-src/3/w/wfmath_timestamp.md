---
title: "wfmath_timestamp(3)"
name: "wfmath_timestamp"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wfmath_timestamp/"
description: "WFMath::TimeStamp – A time stamp."
---

<p>WFMath::TimeStamp &#8211; A time stamp. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/timestamp.h">timestamp.h</a>&gt; </p>
<h3>Public Member Functions</h3>
<p><code>TimeStamp</code> ()<br />
 <i>Construct an uninitialized </i><code>TimeStamp</code>.</p>
<h3>Static Public Member Functions</h3>
<p>static <code>TimeStamp</code> <code>now</code> ()<br />
 <i>set a </i><code>TimeStamp</code> to the current time<br />
 static <code>TimeStamp</code> <code>epochStart</code> ()<br />
 <i>set a </i><code>TimeStamp</code> to Jan 1, 1970</p>
<h2>Detailed Description</h2>
<p>A time stamp. </p>
<p> This class implements the &#8216;generic&#8217; subset of the interface in the fake class <code>Shape</code>, with the exception of the stream operators. It also has the full set of comparison operators (&lt;, &lt;=, &gt;, &gt;=, ==, !=). </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for WFMath from the source code.</p>
