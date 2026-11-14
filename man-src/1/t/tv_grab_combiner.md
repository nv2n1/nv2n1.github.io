---
title: "tv_grab_combiner(1)"
name: "tv_grab_combiner"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tv_grab_combiner/"
description: "tv_grab_combiner – Grab listings by combining data from several grabbers."
---

<h2 class="name">NAME</h2>
<p> tv_grab_combiner &#8211; Grab listings by combining data from several grabbers. </p>
<h2>SYNOPSIS</h2>
<p> tv_grab_combiner &#8211;help </p>
<p> tv_grab_combiner &#8211;configure [&#8211;config-file <font SIZE="-1">FILE</font>] </p>
<p> tv_grab_combiner [&#8211;config-file <font SIZE="-1">FILE</font>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;days N]&nbsp;<wbr>[&#8211;offset N]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;output&nbsp;<wbr><font SIZE="-1">FILE</font>]&nbsp;<wbr>[&#8211;quiet]</p>
<h2>DESCRIPTION</h2>
<p> Output <font SIZE="-1">TV</font> and listings in <font SIZE="-1">XMLTV</font> format by combining data from several other grabbers. </p>
<p> First you must run <code>tv_grab_combiner &#8211;configure</code> to choose which grabbers you want to grab data with and how these grabbers should be configured. </p>
<p> Then you can run <code>tv_grab_combiner</code> with the &#8211;days and &#8211;offset options to grab data. Omitting these options will use the default values for these parameters for each grabber. Since these defaults differs between grabbers, you might end up with data for different periods of time for different channels.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;configure</code> Prompt for which grabbers to use, how these grabbers shall be configured and write the configuration file. </p>
<p> <code>&#8211;config-file </code><font SIZE="-1"><code>FILE</code></font> Set the name of the configuration file, the default is <code>~/.xmltv/tv_grab_combiner.conf</code>. This is the file written by <code>&#8211;configure</code> and read when grabbing. </p>
<p> <code>&#8211;output </code><font SIZE="-1"><code>FILE</code></font> When grabbing, write output to <font SIZE="-1">FILE</font> rather than standard output. </p>
<p> <code>&#8211;days N</code> When grabbing, grab N days rather than 5. </p>
<p> <code>&#8211;offset N</code> Start grabbing at today + N days. N may be negative. </p>
<p> <code>&#8211;quiet</code> Suppress the progress-bar normally shown on standard error. </p>
<p> <code>&#8211;version</code> Show the version of the grabber. </p>
<p> <code>&#8211;help</code> Print a help message and exit.</p>
<h2>ERROR HANDLING</h2>
<p> If any of the called grabbers exit with an error, tv_grab_combiner will exit with a status code of 1 to indicate that the data is incomplete. If any grabber produces output that is not well-formed xml, the output from that grabber will be ignored and tv_grab_combiner will exit with a status code of 1.</p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> The environment variable <font SIZE="-1">HOME</font> can be set to change where configuration files are stored. All configuration is stored in <tt>$HOME</tt>/.xmltv/.</p>
<h2>AUTHOR</h2>
<p> Mattias Holmlund, mattias -at- holmlund -dot- se.</p>
<h2>BUGS</h2>
<h2>Index</h2>
