---
title: "tv_grab_ch_search(1)"
name: "tv_grab_ch_search"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tv_grab_ch_search/"
description: "tv_grab_ch_search – Grab TV listings for Switzerland (from tv.search.ch webpage)."
---

<h2 class="name">NAME</h2>
<p> tv_grab_ch_search &#8211; Grab TV listings for Switzerland (from tv.search.ch webpage). </p>
<h2>SYNOPSIS</h2>
<p> tv_grab_ch_search &#8211;help </p>
<p> tv_grab_ch_search [&#8211;config-file <font SIZE="-1">FILE</font>] &#8211;configure [&#8211;gui <font SIZE="-1">OPTION</font>] </p>
<p> tv_grab_ch_search [&#8211;config-file <font SIZE="-1">FILE</font>] [&#8211;output <font SIZE="-1">FILE</font>] [&#8211;quiet]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;days N]&nbsp;<wbr>[&#8211;offset N] </p>
<p> tv_grab_ch_search &#8211;list-channels </p>
<p> tv_grab_ch_search &#8211;capabilities </p>
<p> tv_grab_ch_search &#8211;version</p>
<h2>DESCRIPTION</h2>
<p> Output <font SIZE="-1">TV</font> listings for several channels available in Switzerland and (partly) central Europe. The data comes from tv.search.ch. The grabber relies on parsing <font SIZE="-1">HTML</font> so it might stop working at any time. </p>
<p> First run <code>tv_grab_ch_search &#8211;configure</code> to choose, which channels you want to download. Then running <code>tv_grab_ch_search</code> with no arguments will output listings in <font SIZE="-1">XML</font> format to standard output. </p>
<p> <code>&#8211;configure</code> Ask for each available channel whether to download and write the configuration file. </p>
<p> <code>&#8211;config-file </code><font SIZE="-1"><code>FILE</code></font> Set the name of the configuration file, the default is <code>~/.xmltv/tv_grab_ch_search.conf</code>. This is the file written by <code>&#8211;configure</code> and read when grabbing. </p>
<p> <code>&#8211;gui </code><font SIZE="-1"><code>OPTION</code></font> Use this option to enable a graphical interface to be used. <font SIZE="-1">OPTION</font> may be &#8216;Tk&#8217;, or left blank for the best available choice. Additional allowed values of <font SIZE="-1">OPTION</font> are &#8216;Term&#8217; for normal terminal output (default) and &#8216;TermNoProgressBar&#8217; to disable the use of Term::ProgressBar. </p>
<p> <code>&#8211;output </code><font SIZE="-1"><code>FILE</code></font> Write to <font SIZE="-1">FILE</font> rather than standard output. </p>
<p> <code>&#8211;days N</code> Grab N days. The default is fourteen. </p>
<p> <code>&#8211;offset N</code> Start N days in the future. The default is to start from now on (= zero). </p>
<p> <code>&#8211;quiet</code> Suppress the progress messages normally written to standard error. </p>
<p> <code>&#8211;list-channels</code> Write output giving &lt;channel&gt; elements for every channel available (ignoring the config file), but no programmes. </p>
<p> <code>&#8211;capabilities</code> Show which capabilities the grabber supports. For more information, see &lt;<a rel="nofollow" href="http://wiki.xmltv.org/index.php/XmltvCapabilities">http://wiki.xmltv.org/index.php/XmltvCapabilities</a>&gt; </p>
<p> <code>&#8211;version</code> Show the version of the grabber. </p>
<p> <code>&#8211;help</code> print a help message and exit.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/5-xmltv/">xmltv</a></i>(5).</p>
<h2>AUTHOR</h2>
<p> Daniel Bittel &lt;betlit [at] gmx.net&gt;. Inspired by tv_grab_ch by Stefan Siegl.</p>
<h2>BUGS</h2>
<p> If you happen to find a bug, you&#8217;re requested to send a mail to me at <code>betlit [at] gmx.net</code> or to one of the <font SIZE="-1">XMLTV</font> mailing lists, see webpages at <a rel="nofollow" href="http://sourceforge.net/projects/xmltv/.">http://sourceforge.net/projects/xmltv/.</a> </p>
<h2>Index</h2>
