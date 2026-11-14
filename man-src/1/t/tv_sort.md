---
title: "tv_sort(1)"
name: "tv_sort"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tv_sort/"
description: "tv_sort – Sort XMLTV listings files by date, and add stop times."
---

<h2 class="name">NAME</h2>
<p> tv_sort &#8211; Sort XMLTV listings files by date, and add stop times. </p>
<h2>SYNOPSIS</h2>
<p> tv_sort [&#8211;help] [&#8211;by-channel] [&#8211;output <font SIZE="-1">FILE</font>] [<font SIZE="-1">FILE&#8230;</font>]</p>
<h2>DESCRIPTION</h2>
<p> Read <font SIZE="-1">XMLTV</font> data and write out the same data sorted in date order. Where stop times of programmes are missing, guess them from the start time of the next programme on the same channel. For the last programme of a channel, no stop time can be added. </p>
<p> Tv_sort also performs some sanity checks such as making sure no two programmes on the same channel overlap. </p>
<p> <code>&#8211;output </code><font SIZE="-1"><code>FILE</code></font> write to <font SIZE="-1">FILE</font> rather than standard output </p>
<p> <code>&#8211;by-channel</code> sort first by channel id, then by date within each<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>channel. </p>
<p> <code>&#8211;duplicate-error</code> If the input contains the same programme more than once,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>consider this as an error. Default is to silently<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ignore duplicate entries. </p>
<p> The time sorting is by start time, then by stop time. Without <code>&#8211;by-channel</code>, if start times and stop times are equal then two programmes are sorted by internal channel id. With <code>&#8211;by-channel</code>, channel id is compared first and then times. </p>
<p> You can think of tv_sort as converting <font SIZE="-1">XMLTV</font> data into a canonical form, useful for diffing two files.</p>
<h2>EXAMPLES</h2>
<p> At a typical Unix shell or Windows command prompt:</p>
<dl>
<dt>tv_sort &lt;in.xml &gt;out.xml</p>
<dd>
<dt>tv_sort in.xml &#8211;output out.xml</p>
<dd></dl>
<p> These are different ways of saying the same thing.</p>
<h2>AUTHOR</h2>
<p> Ed Avis, ed [at] membled.com </p>
<h2>Index</h2>
