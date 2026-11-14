---
title: "tv_grab_il(1)"
name: "tv_grab_il"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tv_grab_il/"
description: "tv_grab_il – Grab TV listings for Israel."
---

<h2 class="name">NAME</h2>
<p> tv_grab_il &#8211; Grab TV listings for Israel. </p>
<h2>SYNOPSIS</h2>
<p> tv_grab_il &#8211;help </p>
<p> tv_grab_il &#8211;version </p>
<p> tv_grab_il &#8211;capabilities </p>
<p> tv_grab_il &#8211;description </p>
<p> tv_grab_il [&#8211;config-file <font SIZE="-1">FILE</font>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;days N]&nbsp;<wbr>[&#8211;offset N]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;output&nbsp;<wbr><font SIZE="-1">FILE</font>]&nbsp;<wbr>[&#8211;quiet]&nbsp;<wbr>[&#8211;debug] </p>
<p> tv_grab_il &#8211;configure [&#8211;config-file <font SIZE="-1">FILE</font>] </p>
<p> tv_grab_il &#8211;configure-api [&#8211;stage <font SIZE="-1">NAME</font>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;config-file&nbsp;<wbr><font SIZE="-1">FILE</font>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;output&nbsp;<wbr><font SIZE="-1">FILE</font>] </p>
<p> tv_grab_il &#8211;list-channels [&#8211;config-file <font SIZE="-1">FILE</font>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;output&nbsp;<wbr><font SIZE="-1">FILE</font>]&nbsp;<wbr>[&#8211;quiet]&nbsp;<wbr>[&#8211;debug]</p>
<h2>DESCRIPTION</h2>
<p> Output <font SIZE="-1">TV</font> listings in <font SIZE="-1">XMLTV</font> format for many channels available in Israel. The data comes from tv.walla.co.il. </p>
<p> First you must run <code>tv_grab_il &#8211;configure</code> to choose which channels you want to receive. </p>
<p> Then running <code>tv_grab_il</code> with no arguments will get a listings in <font SIZE="-1">XML</font> format for the channels you chose for available days including today.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;configure</code> Prompt for which channels to download and write the configuration file. </p>
<p> <code>&#8211;config-file </code><font SIZE="-1"><code>FILE</code></font> Set the name of the configuration file, the default is <code>~/.xmltv/tv_grab_il.conf</code>. This is the file written by <code>&#8211;configure</code> and read when grabbing. </p>
<p> <code>&#8211;output </code><font SIZE="-1"><code>FILE</code></font> When grabbing, write output to <font SIZE="-1">FILE</font> rather than standard output. </p>
<p> <code>&#8211;days N</code> When grabbing, grab N days rather than all available days. </p>
<p> <code>&#8211;offset N</code> Start grabbing at today + N days. N may be negative. </p>
<p> <code>&#8211;quiet</code> Suppress the progress-bar normally shown on standard error. </p>
<p> <code>&#8211;debug</code> Provide more information on progress to stderr to help in debugging. </p>
<p> <code>&#8211;list-channels</code> Write output giving &lt;channel&gt; elements for every channel available (ignoring the config file), but no programmes. </p>
<p> <code>&#8211;capabilities</code> Show which capabilities the grabber supports. For more information, see &lt;<a rel="nofollow" href="http://wiki.xmltv.org/index.php/XmltvCapabilities">http://wiki.xmltv.org/index.php/XmltvCapabilities</a>&gt; </p>
<p> <code>&#8211;version</code> Show the version of the grabber. </p>
<p> <code>&#8211;help</code> Print a help message and exit.</p>
<h2>ERROR HANDLING</h2>
<p> If the grabber fails to download data for some channel on a specific day, it will print an errormessage to <font SIZE="-1">STDERR</font> and then continue with the other channels and days. The grabber will exit with a status code of 1 to indicate that the data is incomplete.</p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> The environment variable <font SIZE="-1">HOME</font> can be set to change where configuration files are stored. All configuration is stored in <tt>$HOME</tt>/.xmltv/. On Windows, it might be necessary to set <font SIZE="-1">HOME</font> to a path without spaces in it.</p>
<h2>SUPPORTED CHANNELS</h2>
<p> For information on supported channels, see <a rel="nofollow" href="http://tv.walla.co.il/">http://tv.walla.co.il/</a></p>
<h2>AUTHOR</h2>
<p> lightpriest. This documentation and parts of the code based on various other tv_grabbers from the XMLTV-project.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/5-xmltv/">xmltv</a></i>(5). </p>
<h2>Index</h2>
