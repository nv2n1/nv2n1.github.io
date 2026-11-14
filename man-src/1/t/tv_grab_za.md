---
title: "tv_grab_za(1)"
name: "tv_grab_za"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tv_grab_za/"
description: "tv_grab_za – Grab TV listings for South Africa."
---

<h2 class="name">NAME</h2>
<p> tv_grab_za &#8211; Grab TV listings for South Africa. </p>
<h2>SYNOPSIS</h2>
<p> tv_grab_za &#8211;help </p>
<p> tv_grab_za [&#8211;config-file <font SIZE="-1">FILE</font>] &#8211;configure [&#8211;gui <font SIZE="-1">OPTION</font>] </p>
<p> tv_grab_za [&#8211;config-file <font SIZE="-1">FILE</font>] [&#8211;output <font SIZE="-1">FILE</font>] [&#8211;days N] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> [&#8211;quiet] [&#8211;retries N]</p>
<h2>DESCRIPTION</h2>
<p> Output <font SIZE="-1">TV</font> listings for <font SIZE="-1">DSTV</font> channels available in South Africa. The data comes from <a rel="nofollow" href="http://www.dstv.com">www.dstv.com</a>. The grabber relies on parsing <font SIZE="-1">HTML</font> so it might stop working at any time. </p>
<p> First run <code>tv_grab_za &#8211;configure</code> to choose, which channels you want to download. Then running <code>tv_grab_za</code> with no arguments will output listings in <font SIZE="-1">XML</font> format to standard output. </p>
<p> <code>&#8211;configure</code> Prompt for which channels, and write the configuration file. </p>
<p> <code>&#8211;config-file </code><font SIZE="-1"><code>FILE</code></font> Set the name of the configuration file, the default is <code>~/.xmltv/tv_grab_za.conf</code>. This is the file written by <code>&#8211;configure</code> and read when grabbing. </p>
<p> <code>&#8211;gui </code><font SIZE="-1"><code>OPTION</code></font> Use this option to enable a graphical interface to be used. <font SIZE="-1">OPTION</font> may be &#8216;Tk&#8217;, or left blank for the best available choice. Additional allowed values of <font SIZE="-1">OPTION</font> are &#8216;Term&#8217; for normal terminal output (default) and &#8216;TermNoProgressBar&#8217; to disable the use of XMLTV::ProgressBar. </p>
<p> <code>&#8211;output </code><font SIZE="-1"><code>FILE</code></font> write to <font SIZE="-1">FILE</font> rather than standard output. </p>
<p> <code>&#8211;days N</code> grab N days. Can be 1, 7, 14 or 30. Default is 14 </p>
<p> <code>&#8211;quiet</code> suppress the progress messages normally written to standard error. </p>
<p> <code>&#8211;retries</code> number of retries before failing channel download. </p>
<p> <code>&#8211;help</code> print a help message and exit.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/5-xmltv/">xmltv</a></i>(5).</p>
<h2>AUTHORS Chris Picton &lt;cpicton [at] users.sf.net&gt; Neil Garratt &lt;ngarratt [at] users.sf.net&gt;</h2>
<p> Based on tv_grab_fi by Matti Airas. </p>
<p> Latest version always available at <a rel="nofollow" href="http://xmltv.cvs.sourceforge.net/xmltv/xmltv/grab/za/">http://xmltv.cvs.sourceforge.net/xmltv/xmltv/grab/za/</a></p>
<h2>BUGS</h2>
<p> Does not automatically update itself, when <font SIZE="-1">DSTV</font> changes their site </p>
<h2>Index</h2>
