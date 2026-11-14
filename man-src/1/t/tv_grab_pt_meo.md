---
title: "tv_grab_pt_meo(1)"
name: "tv_grab_pt_meo"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tv_grab_pt_meo/"
description: "tv_grab_pt_meo – Grab TV listings for MEO from SAPO in Portugal."
---

<h2 class="name">NAME</h2>
<p> tv_grab_pt_meo &#8211; Grab TV listings for MEO from SAPO in Portugal. </p>
<h2>SYNOPSIS</h2>
<p> tv_grab_pt_meo &#8211;help </p>
<p> tv_grab_pt_meo &#8211;configure [&#8211;config-file <font SIZE="-1">FILE</font>] [&#8211;root-url <font SIZE="-1">URL</font>] </p>
<p> tv_grab_pt_meo [&#8211;config-file <font SIZE="-1">FILE</font>] [&#8211;root-url <font SIZE="-1">URL</font>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;days N]&nbsp;<wbr>[&#8211;offset N]&nbsp;<wbr>[&#8211;channel xmltvid,xmltvid,&#8230;]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;output&nbsp;<wbr><font SIZE="-1">FILE</font>]&nbsp;<wbr>[&#8211;quiet]&nbsp;<wbr>[&#8211;debug] </p>
<p> tv_grab_pt_meo &#8211;list-channels [&#8211;config-file <font SIZE="-1">FILE</font>] [&#8211;root-url <font SIZE="-1">URL</font>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;output&nbsp;<wbr><font SIZE="-1">FILE</font>]&nbsp;<wbr>[&#8211;quiet]&nbsp;<wbr>[&#8211;debug]</p>
<h2>DESCRIPTION</h2>
<p> Output <font SIZE="-1">TV</font> and listings in <font SIZE="-1">XMLTV</font> format for many stations available in Portugal. This program consumes the <font SIZE="-1">EPG</font> service offering from <font SIZE="-1">SAPO</font> at &lt;<a rel="nofollow" href="http://services.sapo.pt/Metadata/Service/EPG?culture=EN">http://services.sapo.pt/Metadata/Service/EPG?culture=EN</a>&gt;. See &lt;<a rel="nofollow" href="http://seguranca.sapo.pt/termosdeutilizacao/apis_rss_webservices.html">http://seguranca.sapo.pt/termosdeutilizacao/apis_rss_webservices.html</a>&gt; for their terms of service. (automatic translation suggests it&#8217;s free for personal use, verfication appreciated) </p>
<p> First you must run <code>tv_grab_pt_meo &#8211;configure</code> to choose which stations you want to receive. </p>
<p> Then running <code>tv_grab_pt_meo</code> with no arguments will get a listings for the stations you chose for all available days including today.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;configure</code> Prompt for which stations to download and write the configuration file. </p>
<p> <code>&#8211;config-file </code><font SIZE="-1"><code>FILE</code></font> Set the name of the configuration file, the default is <code>~/.xmltv/tv_grab_pt_meo.conf</code>. This is the file written by <code>&#8211;configure</code> and read when grabbing. </p>
<p> <code>&#8211;output </code><font SIZE="-1"><code>FILE</code></font> When grabbing, write output to <font SIZE="-1">FILE</font> rather than standard output. </p>
<p> <code>&#8211;days N</code> When grabbing, grab N days rather than everything available. </p>
<p> <code>&#8211;offset N</code> Start grabbing at today + N days. </p>
<p> <code>&#8211;quiet</code> Only print error-messages on <font SIZE="-1">STDERR.</font> </p>
<p> <code>&#8211;debug</code> Provide more information on progress to stderr to help in debugging. </p>
<p> <code>&#8211;list-channels</code> Output a list of all channels that data is available<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>for. The list is in xmltv-format. </p>
<p> <code>&#8211;capabilities</code> Show which capabilities the grabber supports. For more information, see &lt;<a rel="nofollow" href="http://wiki.xmltv.org/index.php/XmltvCapabilities">http://wiki.xmltv.org/index.php/XmltvCapabilities</a>&gt; </p>
<p> <code>&#8211;version</code> Show the version of the grabber. </p>
<p> <code>&#8211;help</code> Print a help message and exit.</p>
<h2>ERROR HANDLING</h2>
<p> If the grabber fails to download data from webstep, it will print an errormessage to <font SIZE="-1">STDERR</font> and then exit with a status code of 1 to indicate that the data is missing.</p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> The environment variable <font SIZE="-1">HOME</font> can be set to change where configuration files are stored. All configuration is stored in <tt>$HOME</tt>/.xmltv/. On Windows, it might be necessary to set <font SIZE="-1">HOME</font> to a path without spaces in it.</p>
<h2>CREDITS</h2>
<p> Grabber written by Karl Dietz, dekarl -at- users -dot- sourceforge -dot- net as a test of the documentation on grabber writing. This documentation copied from tv_grab_cz by Mattias Holmlund, This documentation copied from tv_grab_uk by Ed Avis, ed -at- membled -dot- com. Original grabber by Jiri Kaderavek, jiri -dot- kaderavek -at- webstep -dot- net with modifications by Petr Stehlik, pstehlik -at- sophics -dot- cz. </p>
<p> Data provided via web service from <font SIZE="-1">SAPO</font> accompanying their <font SIZE="-1">MEO TV</font> service. Check their terms of usage!</p>
<h2>BUGS</h2>
<p> None known. </p>
<h2>Index</h2>
