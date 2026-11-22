---

title: "tv_grab_is(1)"
name: "tv_grab_is"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tv_grab_is/"
description: "tv_grab_is – Grab TV listings for Iceland."
---

<p> tv_grab_is &#8211; Grab TV listings for Iceland. </p>
<h2>SYNOPSIS</h2>
<p> tv_grab_is &#8211;help </p>
<p> tv_grab_is [&#8211;config-file FILE] &#8211;configure [&#8211;gui OPTION] </p>
<p> tv_grab_is [&#8211;config-file FILE] [&#8211;output FILE] [&#8211;days N]<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;offset N]&nbsp;<wbr>[&#8211;quiet] </p>
<p> tv_grab_is &#8211;capabilities </p>
<p> tv_grab_is &#8211;version</p>
<h2>DESCRIPTION</h2>
<p> Output TV listings for several channels available in Iceland. </p>
<p> First run <code>tv_grab_is &#8211;configure</code> to choose, which channels you want to download. Then running <code>tv_grab_is</code> with no arguments will output listings in XML format to standard output. </p>
<p> <code>&#8211;configure</code> Prompt for which channels, and write the configuration file. </p>
<p> <code>&#8211;config-file </code><code>FILE</code> Set the name of the configuration file, the default is <code>~/.xmltv/tv_grab_is.conf</code>. This is the file written by <code>&#8211;configure</code> and read when grabbing. </p>
<p> <code>&#8211;gui </code><code>OPTION</code> Use this option to enable a graphical interface to be used. OPTION may be &#8216;Tk&#8217;, or left blank for the best available choice. Additional allowed values of OPTION are &#8216;Term&#8217; for normal terminal output (default) and &#8216;TermNoProgressBar&#8217; to disable the use of Term::ProgressBar. </p>
<p> <code>&#8211;output </code><code>FILE</code> Write to FILE rather than standard output. </p>
<p> <code>&#8211;days N</code> Grab N days. The default is as many as the source carries. </p>
<p> <code>&#8211;offset N</code> Start N days in the future. The default is to start from today. </p>
<p> <code>&#8211;quiet</code> Suppress the progress messages normally written to standard error. </p>
<p> <code>&#8211;capabilities</code> Show which capabilities the grabber supports. For more information, see &lt;<a rel="nofollow" href="http://wiki.xmltv.org/index.php/XmltvCapabilities">http://wiki.xmltv.org/index.php/XmltvCapabilities</a>&gt; </p>
<p> <code>&#8211;version</code> Show the version of the grabber. </p>
<p> <code>&#8211;help</code> Print a help message and exit.</p>
<h2>SEE ALSO</h2>
<p> <i>xmltv</i>(5). =head1 AUTHOR </p>
<p> Yngvi Ioor Sigurjonsson (yngvi [at] teymi.is). Heavily based on tv_grab_dk by Jesper Skov (jskov [at] zoftcorp.dk). tv_grab_dk originally based on tv_grab_nl by Guido Diepen and Ed Avis (ed [at] membled.com) and tv_grab_fi by Matti Airas. </p>
<p> Version 1.1, Eggert Thorlacius (eggert [at] thorlacius.com). Started out by replacing a couple of channels with XML feeds, but ended up by removing the sjonvarp.is code completely. Left in the &#8220;xxx.sjonvarp.is&#8221; XMLTV IDs for backwards compatibility.</p>
<h2>BUGS</h2>
<h2>POD ERRORS</h2>
<p> Hey! <code>The above document had some coding errors, which are explained below:</code></p>
<dl>
<dt>Around line 64:</dt>
<dd> Non-ASCII character seen before =encoding in &#8216;Ioor&#8217;. Assuming UTF-8 </dd>
</dl>
