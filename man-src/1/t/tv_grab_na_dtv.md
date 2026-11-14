---
title: "tv_grab_na_dtv(1)"
name: "tv_grab_na_dtv"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tv_grab_na_dtv/"
description: "tv_grab_na_dtv – Grab TV listings from DirecTV."
---

<h2 class="name">NAME</h2>
<p> tv_grab_na_dtv &#8211; Grab TV listings from DirecTV. </p>
<h2>SYNOPSIS</h2>
<p> tv_grab_na_dtv &#8211;help </p>
<p> tv_grab_na_dtv &#8211;configure [&#8211;config-file <font SIZE="-1">FILE</font>] [&#8211;root-url <font SIZE="-1">URL</font>] </p>
<p> tv_grab_na_dtv [&#8211;config-file <font SIZE="-1">FILE</font>] [&#8211;root-url <font SIZE="-1">URL</font>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;days N]&nbsp;<wbr>[&#8211;offset N]&nbsp;<wbr>[&#8211;channel xmltvid,xmltvid,&#8230;]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;output&nbsp;<wbr><font SIZE="-1">FILE</font>]&nbsp;<wbr>[&#8211;quiet]&nbsp;<wbr>[&#8211;debug] </p>
<p> tv_grab_na_dtv &#8211;list-channels [&#8211;config-file <font SIZE="-1">FILE</font>] [&#8211;root-url <font SIZE="-1">URL</font>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;output&nbsp;<wbr><font SIZE="-1">FILE</font>]&nbsp;<wbr>[&#8211;quiet]&nbsp;<wbr>[&#8211;debug]</p>
<h2>DESCRIPTION</h2>
<p> Output <font SIZE="-1">TV</font> and listings in <font SIZE="-1">XMLTV</font> format from directv.com. </p>
<p> First you must run <code>tv_grab_na_dtv &#8211;configure</code> to choose which stations you want to receive. </p>
<p> Then running <code>tv_grab_na_dtv</code> with no arguments will get listings for the stations you chose for five days including today.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;configure</code> Prompt for which stations to download and write the configuration file. </p>
<p> <code>&#8211;config-file </code><font SIZE="-1"><code>FILE</code></font> Set the name of the configuration file, the default is <code>~/.xmltv/tv_grab_na_dtv.conf</code>. This is the file written by <code>&#8211;configure</code> and read when grabbing. </p>
<p> <code>&#8211;output </code><font SIZE="-1"><code>FILE</code></font> When grabbing, write output to <font SIZE="-1">FILE</font> rather than standard output. </p>
<p> <code>&#8211;days N</code> When grabbing, grab N days rather than 5. </p>
<p> <code>&#8211;offset N</code> Start grabbing at today + N days. </p>
<p> <code>&#8211;quiet</code> Only print error-messages on <font SIZE="-1">STDERR.</font> </p>
<p> <code>&#8211;debug</code> Provide more information on progress to stderr to help in debugging. </p>
<p> <code>&#8211;list-channels</code> Output a list of all channels that data is available<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>for. The list is in xmltv-format. </p>
<p> <code>&#8211;capabilities</code> Show which capabilities the grabber supports. </p>
<p> <code>&#8211;version</code> Show the version of the grabber. </p>
<p> <code>&#8211;help</code> Print a help message and exit.</p>
<h2>ERROR HANDLING</h2>
<p> If the grabber fails to download data, it will print an error message to <font SIZE="-1">STDERR</font> and then exit with a status code of 1 to indicate that the data is missing.</p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> The environment variable <font SIZE="-1">HOME</font> can be set to change where configuration files are stored. All configuration is stored in <tt>$HOME</tt>/.xmltv/. On Windows, it might be necessary to set <font SIZE="-1">HOME</font> to a path without spaces in it. </p>
<p> <font SIZE="-1">TEMP</font> or <font SIZE="-1">TMP,</font> if present, will override the directory used to contain temporary files. Default is &#8220;/tmp&#8221;, so under Windows one of these is required.</p>
<h2>CREDITS</h2>
<p> Grabber written Rod Roark (<a rel="nofollow" href="http://www.sunsetsystems.com/">http://www.sunsetsystems.com/</a>), modified by Adam Lewandowski (adam [at] alewando.com) in January 2011 to account for DirecTV site changes.</p>
<h2>BUGS</h2>
<p> Like any screen-scraping grabber, this one will break regularly as the web site changes, and you should try to fetch a new one from the project&#8217;s repository. At some point the breakage might not be fixable or it may be that nobody wants to fix it. Sane people should use Schedules Direct instead. </p>
<h2>Index</h2>
