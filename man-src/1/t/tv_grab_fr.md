---
title: "tv_grab_fr(1)"
name: "tv_grab_fr"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tv_grab_fr/"
description: "tv_grab_fr – Grab TV listings for France."
---

<h2 class="name">NAME</h2>
<p> tv_grab_fr &#8211; Grab TV listings for France. </p>
<h2>SYNOPSIS</h2>
<pre><code>
To configure : tv_grab_fr-- configure[--config - file FILE][--gui OPTION] To configure AUTRES CHAINES list : tv_grab_fr-- configure - more - channels To grab listings : tv_grab_fr[--config - file FILE][--output FILE][--days N][--offset N][--quiet][--debug] To list available channels : tv_grab_fr-- list - channels To show capabilities : tv_grab_fr-- capabilities To show version : tv_grab_fr-- version Help : tv_grab_fr-- help
</code></pre>
<h2>DESCRIPTION</h2>
<p> Output <font SIZE="-1">TV</font> listings for several channels available in France (Hertzian, Cable/satellite, Canal+ Sat, <font SIZE="-1">TPS</font>). The data comes from telepoche.guidetele.com. The default is to grab as many days as possible (currently 9) from the current day onwards. </p>
<p> <code>&#8211;configure</code> Grab channels information from the website and ask for channel type and names to grab. </p>
<p> <code>&#8211;configure-more-channels</code> Use this option to create <font SIZE="-1">AUTRES CHAINES</font> list. This allows grabbing listings for some channels that are not listed in the bouquets on the website. For more informations and a list of channels see &lt;<a rel="nofollow" href="http://www.lahiette.com/biboobox/forum/viewtopic.php?t=1842">http://www.lahiette.com/biboobox/forum/viewtopic.php?t=1842</a>&gt;. </p>
<p> <code>&#8211;list-channels</code> List available channels for chosen bouquets. </p>
<p> <code>&#8211;config-file </code><font SIZE="-1"><code>FILE</code></font> Use <font SIZE="-1">FILE</font> as config file instead of the default config file. This allow to have different config files for i.e. different apps. </p>
<p> <code>&#8211;gui </code><font SIZE="-1"><code>OPTION</code></font> Use this option to enable a graphical interface to be used. <font SIZE="-1">OPTION</font> may be &#8216;Tk&#8217;, or left blank for the best available choice. Additional allowed values of <font SIZE="-1">OPTION</font> are &#8216;Term&#8217; for normal terminal output (default) and &#8216;TermNoProgressBar&#8217; to disable the use of Term::ProgressBar. </p>
<p> <code>&#8211;output </code><font SIZE="-1"><code>FILE</code></font> Write to <font SIZE="-1">FILE</font> rather than standard output. </p>
<p> <code>&#8211;days N</code> Grab N days starting from today, rather than as many as possible. </p>
<p> <code>&#8211;offset N</code> Start grabbing N days from today, rather than starting today. N may be negative. Due to the website organization, N cannot be inferior to -1. </p>
<p> <code>&#8211;quiet</code> Suppress the progress messages normally written to standard error. </p>
<p> <code>&#8211;debug</code> Provide additional debugging message during processing. </p>
<p> <code>&#8211;capabilities</code> Show which capabilities the grabber supports. For more information, see &lt;<a rel="nofollow" href="http://wiki.xmltv.org/index.php/XmltvCapabilities">http://wiki.xmltv.org/index.php/XmltvCapabilities</a>&gt;. </p>
<p> <code>&#8211;version</code> Show the version of the grabber. </p>
<p> <code>&#8211;help</code> Print a help message and exit.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/5-xmltv/">xmltv</a></i>(5)</p>
<h2>AUTHOR</h2>
<p> The original author was Sylvain Fabre, centraladmin at lahiette dot com with patches from:<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; Francois Gouget, fgouget at free dot fr<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; Niel Markwick, nielm at bigfoot dot com<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; Zubrick, zubrick at number6 dot ch<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; Nick Morrott, knowledgejunkie at gmail dot com </p>
<p> The application is currently maintained by Nick Morrott (knowledgejunkie at gmail dot com). </p>
<h2>Index</h2>
