---
title: "tv_grab_hr(1)"
name: "tv_grab_hr"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tv_grab_hr/"
description: "tv_grab_hr – Grab TV listings for Croatia."
---

<h2 class="name">NAME</h2>
<p> tv_grab_hr &#8211; Grab TV listings for Croatia. </p>
<h2>SYNOPSIS</h2>
<p> tv_grab_hr &#8211;help </p>
<p> tv_grab_hr &#8211;configure [&#8211;config-file <font SIZE="-1">FILE</font>] [&#8211;gui <font SIZE="-1">OPTION</font>] </p>
<p> tv_grab_hr [&#8211;config-file <font SIZE="-1">FILE</font>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;days N]&nbsp;<wbr>[&#8211;offset N]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;output&nbsp;<wbr><font SIZE="-1">FILE</font>]&nbsp;<wbr>[&#8211;quiet]&nbsp;<wbr>[&#8211;debug] </p>
<p> tv_grab_hr &#8211;list-channels [&#8211;config-file <font SIZE="-1">FILE</font>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;output&nbsp;<wbr><font SIZE="-1">FILE</font>]&nbsp;<wbr>[&#8211;quiet]&nbsp;<wbr>[&#8211;debug]</p>
<h2>DESCRIPTION</h2>
<p> Output <font SIZE="-1">TV</font> and listings in <font SIZE="-1">XMLTV</font> format for many stations available in Croatia. </p>
<p> First you must run <code>tv_grab_hr &#8211;configure</code> to choose which stations you want to receive. </p>
<p> Then running <code>tv_grab_hr</code> with no arguments will get a listings for the stations you chose for five days including today.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;configure</code> Prompt for which stations to download and write the configuration file. </p>
<p> <code>&#8211;config-file </code><font SIZE="-1"><code>FILE</code></font> Set the name of the configuration file, the default is <code>~/.xmltv/tv_grab_hr.conf</code>. This is the file written by <code>&#8211;configure</code> and read when grabbing. </p>
<p> <code>&#8211;gui </code><font SIZE="-1"><code>OPTION</code></font> Use this option to enable a graphical interface to be used. <font SIZE="-1">OPTION</font> may be &#8216;Tk&#8217;, or left blank for the best available choice. Additional allowed values of <font SIZE="-1">OPTION</font> are &#8216;Term&#8217; for normal terminal output (default) and &#8216;TermNoProgressBar&#8217; to disable the use of Term::ProgressBar. </p>
<p> <code>&#8211;output </code><font SIZE="-1"><code>FILE</code></font> When grabbing, write output to <font SIZE="-1">FILE</font> rather than standard output. </p>
<p> <code>&#8211;days N</code> When grabbing, grab N days rather than 5. </p>
<p> <code>&#8211;offset N</code> Start grabbing at today + N days. N may be negative. </p>
<p> <code>&#8211;quiet</code> Suppress the progress-bar normally shown on standard error. </p>
<p> <code>&#8211;debug</code> Provide more information on progress to stderr to help in debugging. </p>
<p> <code>&#8211;list-channels</code> Output a list of all channels that data is available<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>for. The list is in xmltv-format. </p>
<p> <code>&#8211;version</code> Show the version of the grabber. </p>
<p> <code>&#8211;help</code> Print a help message and exit.</p>
<h2>ERROR HANDLING</h2>
<p> If the grabber fails to download data for some channel on a specific day, it will print an errormessage to <font SIZE="-1">STDERR</font> and then continue with the other channels and days. The grabber will exit with a status code of 1 to indicate that the data is incomplete.</p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> The environment variable <font SIZE="-1">HOME</font> can be set to change where configuration files are stored. All configuration is stored in <tt>$HOME</tt>/.xmltv/. On Windows, it might be necessary to set <font SIZE="-1">HOME</font> to a path without spaces in it.</p>
<h2>SUPPORTED CHANNELS</h2>
<p> For information on supported channels, see <a rel="nofollow" href="http://www.gonix.net/">http://www.gonix.net/</a></p>
<h2>AUTHOR</h2>
<p> Mattias Holmlund, mattias -at- holmlund -dot- se. This documentation and parts of the code copied from tv_grab_uk by Ed Avis, ed -at- membled -dot- com.</p>
<h2>BUGS</h2>
<h2>Index</h2>
