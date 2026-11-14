---
title: "tv_grab_eu_epgdata(1)"
name: "tv_grab_eu_epgdata"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tv_grab_eu_epgdata/"
description: "tv_grab_eu_epgdata – Grab TV listings for parts of Europe."
---

<h2 class="name">NAME</h2>
<p> tv_grab_eu_epgdata &#8211; Grab TV listings for parts of Europe. </p>
<h2>SYNOPSIS</h2>
<p> tv_grab_eu_epgdata &#8211;help tv_grab_eu_epgdata tv_grab_eu_epgdata &#8211;version </p>
<p> tv_grab_eu_epgdata &#8211;capabilities </p>
<p> tv_grab_eu_epgdata &#8211;description </p>
<p> tv_grab_eu_epgdata [&#8211;config-file <font SIZE="-1">FILE</font>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;days N]&nbsp;<wbr>[&#8211;offset N]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;output&nbsp;<wbr><font SIZE="-1">FILE</font>]&nbsp;<wbr>[&#8211;quiet]&nbsp;<wbr>[&#8211;debug] </p>
<p> tv_grab_eu_epgdata &#8211;configure [&#8211;config-file <font SIZE="-1">FILE</font>] </p>
<p> tv_grab_eu_epgdata &#8211;configure-api [&#8211;stage <font SIZE="-1">NAME</font>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;config-file&nbsp;<wbr><font SIZE="-1">FILE</font>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;output&nbsp;<wbr><font SIZE="-1">FILE</font>] </p>
<p> tv_grab_eu_epgdata &#8211;list-channels [&#8211;config-file <font SIZE="-1">FILE</font>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;output&nbsp;<wbr><font SIZE="-1">FILE</font>]&nbsp;<wbr>[&#8211;quiet]&nbsp;<wbr>[&#8211;debug] </p>
<p> tv_grab_eu_epgdata &#8211;preferredmethod</p>
<h2>DESCRIPTION</h2>
<p> Output <font SIZE="-1">TV</font> and listings in <font SIZE="-1">XMLTV</font> format for many stations available in Europe. </p>
<p> First you must run <code>tv_grab_eu_epgdata &#8211;configure</code> to choose which stations you want to receive. </p>
<p> Then running <code>tv_grab_eu_epgdata</code> with no arguments will get a listings for the stations you chose for five days including today. </p>
<p> This is a commercial grabber. Go to <a rel="nofollow" href="http://wiki.xmltv.org/index.php/EU_epgdata">http://wiki.xmltv.org/index.php/EU_epgdata</a> to sign up or send an e-mail to service [at] epgdata.com for further information. It&#8217;s also possible to ask for a test account.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;configure</code> Prompt for which stations to download and write the configuration file. </p>
<p> <code>&#8211;config-file </code><font SIZE="-1"><code>FILE</code></font> Set the name of the configuration file, the default is <code>~/.xmltv/tv_grab_eu_epgdata.conf</code>. This is the file written by <code>&#8211;configure</code> and read when grabbing. </p>
<p> <code>&#8211;gui </code><font SIZE="-1"><code>OPTION</code></font> Use this option to enable a graphical interface to be used. <font SIZE="-1">OPTION</font> may be &#8216;Tk&#8217;, or left blank for the best available choice. Additional allowed values of <font SIZE="-1">OPTION</font> are &#8216;Term&#8217; for normal terminal output (default) and &#8216;TermNoProgressBar&#8217; to disable the use of Term::ProgressBar. </p>
<p> <code>&#8211;output </code><font SIZE="-1"><code>FILE</code></font> When grabbing, write output to <font SIZE="-1">FILE</font> rather than standard output. </p>
<p> <code>&#8211;days N</code> When grabbing, grab N days rather than 5. </p>
<p> <code>&#8211;offset N</code> Start grabbing at today + N days. </p>
<p> <code>&#8211;quiet</code> Do not show status messages. </p>
<p> <code>&#8211;debug</code> Provide more information on progress to stderr to help in debugging. </p>
<p> <code>&#8211;list-channels</code> Output a list of all channels that data is available<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>for. The list is in xmltv-format. </p>
<p> <code>&#8211;version</code> Show the version of the grabber. </p>
<p> <code>&#8211;help</code> Print a help message and exit. </p>
<p> <code>&#8211;preferredmethod</code> Shows the preferred method for downloading data<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(see&nbsp;<wbr><a rel="nofollow" href="http://wiki.xmltv.org/index.php/XmltvCapabilities)">http://wiki.xmltv.org/index.php/XmltvCapabilities)</a> =head1 <font SIZE="-1">ENVIRONMENT VARIABLES</font> </p>
<p> The environment variable <font SIZE="-1">HOME</font> can be set to change where configuration files are stored. All configuration is stored in <tt>$HOME</tt>/.xmltv/. On Windows, it might be necessary to set <font SIZE="-1">HOME</font> to a path without spaces in it.</p>
<h2>SUPPORTED CHANNELS</h2>
<p> For a list of supported channels, see the channel_ids file distributed with this grabber. If additional channels are available, you will receive a warning when you run &#8211;configure. </p>
<p> Once I am aware that new channels are available, the channel_ids file will be updated and this grabber will automatically fetch an updated copy.</p>
<h2>COMPATIBILITY</h2>
<p> The channel ids used in this grabber aim to be mostly possible with other grabbers, eg tv_grab_de_prisma and some other grabbers for other countries. <font SIZE="-1">NOTE:</font> Retaining compatibility was not always possible or practicable. You can get a list of channel ids using &#8211;list-channels</p>
<h2>AUTHOR</h2>
<p> Michael Haas, laga -at- laga -dot- ath -dot &#8211; cx. This documentation is copied from tv_grab_se_swedb by Mattias Holmlund, which in turn was copied from tv_grab_uk by Ed Avis. Parts of the code are copied from tv_grab_se_swedb and tv_grab_na_dd (in <font SIZE="-1">XMLTV 0.5.45</font>) as well as various other sources.</p>
<h2>BUGS</h2>
<p> There&#8217;s no proper support for channels with locally different schedules. For example, if your <font SIZE="-1">EPG</font> package is a German one, you&#8217;ll get the <font SIZE="-1">EPG</font> schedule for Germany even if you preferred the Swiss schedule which is also available in the data (for some channels at least). </p>
<p> Timezones are not handled correctly. Currently, you have to enter your time zone manually during the configure step. You have to do this every time your time zone changes, eg for daylight saving time (&#8220;Sommerzeit&#8221; and &#8220;Normalzeit&#8221; for my fellow Germans). I&#8217;ll try to have this fixed for the next <font SIZE="-1">XMLTV</font> release. Please see this thread for further discussion and some additional issues:<br />
&nbsp;<wbr><a rel="nofollow" href="http://thread.gmane.org/gmane.comp.tv.xmltv.devel/7919">http://thread.gmane.org/gmane.comp.tv.xmltv.devel/7919</a> <font SIZE="-1">FYI:</font> you can modify the time zone directly in the config file which is usually located at ~/.xmltv/tv_grab_eu_epgdata.conf or ~/.mythtv/FOO.xmltv where <font SIZE="-1">FOO</font> is the name of your video source in MythTV. </p>
<p> If the data source gives us data for one day, they&#8217;ll also cover a part of the following day. Maybe this should be fixed. Please note: data is not overlapping! So if we want to get data for today, we might as well grab yesterday because that&#8217;ll give us <font SIZE="-1">EPG</font> till ~5am for today. </p>
<p> I&#8217;m sure this list is not complete. Let me know if you encounter additional problems. </p>
<h2>Index</h2>
