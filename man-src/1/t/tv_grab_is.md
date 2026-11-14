---
title: "tv_grab_is(1)"
name: "tv_grab_is"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tv_grab_is/"
description: "tv_grab_is – Grab TV listings for Iceland."
---

<h2 class="name">NAME</h2>
<p> tv_grab_is &#8211; Grab TV listings for Iceland. </p>
<h2>SYNOPSIS</h2>
<p> tv_grab_is &#8211;help </p>
<p> tv_grab_is [&#8211;config-file <font SIZE="-1">FILE</font>] &#8211;configure [&#8211;gui <font SIZE="-1">OPTION</font>] </p>
<p> tv_grab_is [&#8211;config-file <font SIZE="-1">FILE</font>] [&#8211;output <font SIZE="-1">FILE</font>] [&#8211;days N]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;offset N]&nbsp;<wbr>[&#8211;quiet] </p>
<p> tv_grab_is &#8211;capabilities </p>
<p> tv_grab_is &#8211;version</p>
<h2>DESCRIPTION</h2>
<p> Output <font SIZE="-1">TV</font> listings for several channels available in Iceland. </p>
<p> First run <code>tv_grab_is &#8211;configure</code> to choose, which channels you want to download. Then running <code>tv_grab_is</code> with no arguments will output listings in <font SIZE="-1">XML</font> format to standard output. </p>
<p> <code>&#8211;configure</code> Prompt for which channels, and write the configuration file. </p>
<p> <code>&#8211;config-file </code><font SIZE="-1"><code>FILE</code></font> Set the name of the configuration file, the default is <code>~/.xmltv/tv_grab_is.conf</code>. This is the file written by <code>&#8211;configure</code> and read when grabbing. </p>
<p> <code>&#8211;gui </code><font SIZE="-1"><code>OPTION</code></font> Use this option to enable a graphical interface to be used. <font SIZE="-1">OPTION</font> may be &#8216;Tk&#8217;, or left blank for the best available choice. Additional allowed values of <font SIZE="-1">OPTION</font> are &#8216;Term&#8217; for normal terminal output (default) and &#8216;TermNoProgressBar&#8217; to disable the use of Term::ProgressBar. </p>
<p> <code>&#8211;output </code><font SIZE="-1"><code>FILE</code></font> Write to <font SIZE="-1">FILE</font> rather than standard output. </p>
<p> <code>&#8211;days N</code> Grab N days. The default is as many as the source carries. </p>
<p> <code>&#8211;offset N</code> Start N days in the future. The default is to start from today. </p>
<p> <code>&#8211;quiet</code> Suppress the progress messages normally written to standard error. </p>
<p> <code>&#8211;capabilities</code> Show which capabilities the grabber supports. For more information, see &lt;<a rel="nofollow" href="http://wiki.xmltv.org/index.php/XmltvCapabilities">http://wiki.xmltv.org/index.php/XmltvCapabilities</a>&gt; </p>
<p> <code>&#8211;version</code> Show the version of the grabber. </p>
<p> <code>&#8211;help</code> Print a help message and exit.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/5-xmltv/">xmltv</a></i>(5). =head1 <font SIZE="-1">AUTHOR</font> </p>
<p> Yngvi <font SIZE="+2">I</font>oor Sigurjonsson (yngvi [at] teymi.is). Heavily based on tv_grab_dk by Jesper Skov (jskov [at] zoftcorp.dk). tv_grab_dk originally based on tv_grab_nl by Guido Diepen and Ed Avis (ed [at] membled.com) and tv_grab_fi by Matti Airas. </p>
<p> Version 1.1, Eggert Thorlacius (eggert [at] thorlacius.com). Started out by replacing a couple of channels with <font SIZE="-1">XML</font> feeds, but ended up by removing the sjonvarp.is code completely. Left in the &#8220;xxx.sjonvarp.is&#8221; <font SIZE="-1">XMLTV</font> IDs for backwards compatibility.</p>
<h2>BUGS</h2>
<h2>POD ERRORS</h2>
<p> Hey! <code>The above document had some coding errors, which are explained below:</code></p>
<dl>
<dt>Around line 64:</p>
<dd> Non-ASCII character seen before =encoding in &#8216;<font SIZE="+2">I</font>oor&#8217;. Assuming <font SIZE="-1">UTF-8</font> </p>
</dl>
<h2>Index</h2>
