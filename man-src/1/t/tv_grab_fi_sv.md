---
title: "tv_grab_fi_sv(1)"
name: "tv_grab_fi_sv"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tv_grab_fi_sv/"
description: "tv_grab_fi_sv – Grab TV listings for Finland in Swedish."
---

<h2 class="name">NAME</h2>
<p> tv_grab_fi_sv &#8211; Grab TV listings for Finland in Swedish. </p>
<h2>SYNOPSIS</h2>
<p> tv_grab_fi_sv &#8211;help </p>
<p> tv_grab_fi_sv &#8211;version </p>
<p> tv_grab_fi_sv &#8211;capabilities </p>
<p> tv_grab_fi_sv &#8211;description </p>
<p> tv_grab_fi_sv [&#8211;config-file <font SIZE="-1">FILE</font>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;days N]&nbsp;<wbr>[&#8211;offset N]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;output&nbsp;<wbr><font SIZE="-1">FILE</font>]&nbsp;<wbr>[&#8211;quiet]&nbsp;<wbr>[&#8211;debug] </p>
<p> tv_grab_fi_sv &#8211;configure [&#8211;config-file <font SIZE="-1">FILE</font>] </p>
<p> tv_grab_fi_sv &#8211;configure-api [&#8211;stage <font SIZE="-1">NAME</font>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;config-file&nbsp;<wbr><font SIZE="-1">FILE</font>]&nbsp;<wbr>[&#8211;output&nbsp;<wbr><font SIZE="-1">FILE</font>] </p>
<p> tv_grab_fi_sv &#8211;list-channels [&#8211;config-file <font SIZE="-1">FILE</font>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;output&nbsp;<wbr><font SIZE="-1">FILE</font>]&nbsp;<wbr>[&#8211;quiet]&nbsp;<wbr>[&#8211;debug]</p>
<h2>DESCRIPTION</h2>
<p> Retrieves and displays <font SIZE="-1">TV</font> listings for the Finnish <font SIZE="-1">YLE</font> channels plus some of the most popular commercial channels. The data comes from <a rel="nofollow" href="http://www.yle.fi">www.yle.fi</a> and the Swedish listings are retrieved rather than the Finnish. Just like tv_grab_fi, this grabber relies on parsing <font SIZE="-1">HTML</font> so it could very well stop working at any time. You have been warned.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;help</code> Print a help message and exit. </p>
<p> <code>&#8211;version</code> Show the versions of the <font SIZE="-1">XMLTV</font> libraries, the grabber and of key modules used for processing listings. </p>
<p> <code>&#8211;capabilities</code> Show which capabilities the grabber supports. For more information, see &lt;<a rel="nofollow" href="http://xmltv.org/wiki/xmltvcapabilities.html">http://xmltv.org/wiki/xmltvcapabilities.html</a>&gt; </p>
<p> <code>&#8211;description</code> Show a brief description of the grabber. </p>
<p> <code>&#8211;config-file </code><font SIZE="-1"><code>FILE</code></font> Specify the name of the configuration file to use. If not specified, a default of <code>~/.xmltv/tv_grab_fi_sv.conf</code> is used. This is the file written by <code>&#8211;configure</code> and read when grabbing. </p>
<p> <code>&#8211;output </code><font SIZE="-1"><code>FILE</code></font> When grabbing, write output to <font SIZE="-1">FILE</font> rather than to standard output. </p>
<p> <code>&#8211;days N</code> When grabbing, grab N days of data instead of all available. Supported values are 1-14. </p>
<p> <code>&#8211;offset N</code> Start grabbing at today + N days. Supported values are 0-13.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/5-xmltv/">xmltv</a></i>(5).</p>
<h2>AUTHOR</h2>
<p> Per Lundberg, (perlun at gmail dot com). Inspired/based on other grabbers, like tv_grab_uk_rt, tv_grab_se_swedb and tv_grab_fi. </p>
<h2>Index</h2>
