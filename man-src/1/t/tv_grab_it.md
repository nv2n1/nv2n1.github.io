---
title: "tv_grab_it(1)"
name: "tv_grab_it"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tv_grab_it/"
description: "tv_grab_it – Grab TV listings for Italy."
---

<h2 class="name">NAME</h2>
<p> tv_grab_it &#8211; Grab TV listings for Italy. </p>
<h2>SYNOPSIS</h2>
<p> tv_grab_it &#8211;help </p>
<p> tv_grab_it [&#8211;config-file <font SIZE="-1">FILE</font>] &#8211;configure </p>
<p> tv_grab_it [&#8211;config-file <font SIZE="-1">FILE</font>] [&#8211;output <font SIZE="-1">FILE</font>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;days N]&nbsp;<wbr>[&#8211;offset N]&nbsp;<wbr>[&#8211;quiet]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;slow]&nbsp;<wbr>[&#8211;verbose]&nbsp;<wbr>[&#8211;errors-in-xml]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;backend SITE1[,SITE2[,SITE3]]] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> [&#8211;cache-slow]</p>
<h2>DESCRIPTION</h2>
<p> Output <font SIZE="-1">TV</font> listings for several channels available in Italy. The grabber relies on parsing <font SIZE="-1">HTML</font> so it might stop working at any time. The data comes from different backends. This is to minimize blackouts in case of site changes but also to extend the number of channels. If the grabber can&#8217;t find the data with the first backend it will try the second one, and so on. You can specify your order of preference using the &#8211;backend option. </p>
<p> Currently configured backends are (in default order):</p>
<dl>
<dt><code>skylife</code> &#8211; grabs data from <a rel="nofollow" href="http://www.skylife.it">www.skylife.it</a></p>
<dd>
<dt><code>mtvit</code> &#8211; grabs data from <a rel="nofollow" href="http://www.mtv.it">www.mtv.it</a></p>
<dd>
<dt><code>boingtv</code> &#8211; grabs data from <a rel="nofollow" href="http://www.boingtv.it">www.boingtv.it</a></p>
<dd>
<dt><code>sitcom1</code> &#8211; grabs data from <a rel="nofollow" href="http://www.sitcom1.it">www.sitcom1.it</a></p>
<dd>
<dt><code>raisat</code> &#8211; grabs data from <a rel="nofollow" href="http://www.risat.it">www.risat.it</a></p>
<dd>
<dt><code>raiit</code> &#8211; grabs data from <a rel="nofollow" href="http://www.rai.it">www.rai.it</a></p>
<dd>
<dt><code>iris</code> &#8211; grabs data from <a rel="nofollow" href="http://www.iris.it">www.iris.it</a></p>
<dd>
<dt><code>mediasetpremium</code> &#8211; grabs data from <a rel="nofollow" href="http://www.mediasetpremium.it">www.mediasetpremium.it</a></p>
<dd></dl>
<p> First run <code>tv_grab_it &#8211;configure</code> to choose which channels you want to download. Then running <code>tv_grab_it</code> with no arguments will output listings in <font SIZE="-1">XML</font> format to standard output. </p>
<p> <code>&#8211;configure</code> Prompt for which channels, and writes the configuration file. </p>
<p> <code>&#8211;config-file </code><font SIZE="-1"><code>FILE</code></font> Set the name of the configuration file, the default is <code>~/.xmltv/tv_grab_it.conf</code>. This is the file written by <code>&#8211;configure</code> and read when grabbing. </p>
<p> <code>&#8211;gui </code><font SIZE="-1"><code>OPTION</code></font> Use this option to enable a graphical interface to be used. <font SIZE="-1">OPTION</font> may be &#8216;Tk&#8217;, or left blank for the best available choice. Additional allowed values of <font SIZE="-1">OPTION</font> are &#8216;Term&#8217; for normal terminal output (default) and &#8216;TermNoProgressBar&#8217; to disable the use of XMLTV::ProgressBar. </p>
<p> <code>&#8211;output </code><font SIZE="-1"><code>FILE</code></font> write to <font SIZE="-1">FILE</font> rather than standard output. </p>
<p> <code>&#8211;days N</code> Grab N days. The default is 7. </p>
<p> <code>&#8211;offset N</code> Start N days in the future. The default is to start from today. </p>
<p> <code>&#8211;quiet</code> Suppress the progress messages normally written to standard error. </p>
<p> <code>&#8211;slow</code> Downloads more details (descriptions, actors&#8230;). This means downloading a new file for each programme, so it&#8217;s off by default to save time. </p>
<p> <code>&#8211;cache-slow</code> If you use the &#8211;cache option to speed up thing when you grab data several times a week, using this option you will cache only the &#8211;slow data, so you shouldn&#8217;t miss changes in schedules. </p>
<p> <code>&#8211;verbose</code> Prints out verbose information useful for debugging. </p>
<p> <code>&#8211;errors-in-xml</code> Outputs warnings as programmes in the xml file, so that you can see errors in your favorite frontend in addition to the default <font SIZE="-1">STDERR. </font> </p>
<p> <code>&#8211;backend</code> Set the backend (or backends) to use. See the examples. </p>
<p> <code>&#8211;version</code> Show the version of the grabber. </p>
<p> <code>&#8211;help</code> Print a help message and exit.</p>
<h2>CAVEATS</h2>
<p> If you use &#8211;quiet you should also use &#8211;errors-in-xml or you won&#8217;t be warned about errors. Note also that, as opposed to previous versions, this grabber doesn&#8217;t die if it cannot find any data, but returns an empty (or optionally containing just warnings) xml file instead. </p>
<p> The backends&#8217; data quality differs a lot. For example, mytv was very basic, yet complete and uses the least amount of bandwith. Skytv has a lot of channels, but unless you use it with the &#8211;slow option the data is not very good (and in this case i would be <font SIZE="-1">VERY</font> slow). wfactory is a good overall site if you don&#8217;t need the whole sky package.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>tv_grab_it &#8211;backend mtvit &#8211;configure</p>
<dd> configures tv_grab_it using only the backend mtvit</p>
<dt>tv_grab_it &#8211;backend skylife,wfactory &#8211;days 1</p>
<dd> grabs one day of data overiding the default order (could also be &#8211;backend skylife &#8211;backend wfactory)</p>
<dt>tv_grab_it &#8211;cache &#8211;slow &#8211;days 3</p>
<dd> grabs the full data for the next three days using the default backend order and using a disk cache.</dl>
<h2>RECOMMENDED USAGE</h2>
<dl>
<dt>tv_grab_it &#8211;cache &#8211;slow &#8211;cache-slow &#8211;errors-in-xml</p>
<dd></dl>
<h2>SEE ALSO</h2>
<p> xmltv.</p>
<h2>AUTHOR</h2>
<p> Davide Chiarini, davide.chiarini [at] gmail.com </p>
<p> you can find some more help at <a rel="nofollow" href="http://www.htpcpoint.it/forum/">http://www.htpcpoint.it/forum/</a> </p>
<h2>Index</h2>
