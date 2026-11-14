---
title: "mrtg-rrd(1)"
name: "mrtg-rrd"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mrtg-rrd/"
description: "mrtg-rrd – How to use RRDtool with MRTG"
---

<h2 class="name">NAME</h2>
<p> mrtg-rrd &#8211; How to use RRDtool with MRTG </p>
<h2>SYNOPSIS</h2>
<p> After using <font SIZE="-1">MRTG</font> for some time you may find some limitations, mostly in the areas of performance and graphing flexibility. These are exactly the areas addressed by RRDtool. To learn more about RRDtool check out its website on </p>
<pre>
 <a rel="nofollow" href="http://oss.oetiker.ch/rrdtool">http://oss.oetiker.ch/rrdtool</a>
</pre>
<h2>RRDTOOL INTEGRATION</h2>
<p> When using mrtg with RRDtool you are replacing <i>rateup</i> with the RRDtool perl module <i>RRDs.pm</i>. To enable RRDtool support in mrtg you have to add the line </p>
<pre>
 LogFormat: rrdtool
</pre>
<p> to your mrtg config file. </p>
<p> <font SIZE="-1">MRTG</font> needs access to both the RRDtool perl module <code>RRDs.pm</code> and to the <code>rrdtool</code> executable. </p>
<p> If these two items are not installed in locations where perl can find them on its own, then you can use the following two parameters to supply the appropriate directories. </p>
<p> For the location of the <code>rrdtool</code> executable you put </p>
<pre>
 PathAdd: /usr/local/rrdtool/bin/
</pre>
<p> or </p>
<pre>
 PathAdd: c:rdtoolin
</pre>
<p> For the location of the perl module it would be: </p>
<pre>
 LibAdd: /usr/local/rrdtool/lib/perl/
</pre>
<p> or </p>
<pre>
 LibAdd: c:rdtoolin\lib\perl
</pre>
<p> When you have made this modification to the configuration file, several things will happen when you run mrtg again with the new config file:</p>
<dl>
<dt>1.</p>
<dd> mrtg will take all your old <tt>&quot;.log&quot;</tt> files and <code>convert</code> them to <tt>&quot;.rrd&quot;</tt> format. (The <tt>&quot;.log&quot;</tt> files don&#8217;t get touched in the process, so if things don&#8217;t work out they are still there.)</p>
<dt>2.</p>
<dd> mrtg will use <code>rrdtool</code> to update its databases. These will have a new format called <i>rrd</i> which is totally different than the native <i>log</i> format of the classic mrtg.</p>
<dt>3.</p>
<dd> mrtg will <code>not</code> create any webpages of graphs anymore. It will only query the routers for traffic information and update its <i>rrd</i> databases.</dl>
<p> The advantage of whole thing is that the mrtg will become <code>much</code> faster. Expect the runtime to drop to 20% of the previous value. (I would like to get some feedback on this from folks with large installations.) </p>
<p> Mind you, though, while the logging process of RRDtool is <code>very</code> fast, you are also gaining some time by neither creating graphs nor updating webpages. The idea behind this is that it is more efficient to create graphs and webpages on demand by using a cgi script. </p>
<p> At the moment there is no <code>official</code> script to do this, but two contributers have created such scripts:</p>
<dl>
<dt>One4All aka 14all.cgi</p>
<dd> This was the first program to take over the webpage creation and graphing task. It has been developed by Rainer Bawidamann rainer.bawidamann [at] web.de. You can find a copy on Rainers website: <a rel="nofollow" href="http://my14all.sourceforge.net/">http://my14all.sourceforge.net/</a> The program comes with its own documentation</p>
<dt><code>routers2.cgi</code></p>
<dd> This is another <font SIZE="-1">CGI</font> frontend for mrtg running with rrdtool. The main difference between this and 14all is that the web pages it creates are much more stylish than the ones from mrtg, plus they support User Defined summary graphs and different levels of Authentication and Authorisation. This has been written by Steve Shipway (steve [at] steveshipway.org). You obtain a copy, and find a forum and demonstration system at <a rel="nofollow" href="http://www.steveshipway.org/software/">http://www.steveshipway.org/software/</a> The program comes with its own installation instructions and install script.</p>
<dt><code>mrtg-rrd</code></p>
<dd> The mrtg-rrd script is a CGI/FastCGI application by Jan &#8220;Yenya&#8221; Kasprzak for displaying <font SIZE="-1">MRTG</font> graphs from data in the RRDtool format. It is an intended replacement for the 14all.cgi script. It can make your monitoring system faster because <font SIZE="-1">MRTG</font> does not have to generate all the <font SIZE="-1">PNG</font> files with graphs every 5 minutes or so. Instead of this the graphs are generated on-demand when the user wants to see them. <a rel="nofollow" href="http://www.fi.muni.cz/~kas/mrtg-rrd/">http://www.fi.muni.cz/~kas/mrtg-rrd/</a></dl>
<h2>FUTURE</h2>
<p> Just as a side note: <font SIZE="-1">MRTG-3</font> will be based entirely on rrdtool technology. But don&#8217;t wait for it &#8230; get going <code>now</code>!</p>
<h2>AUTHOR</h2>
<p> Tobias Oetiker &lt;tobi [at] oetiker.ch&gt; </p>
<h2>Index</h2>
