---
title: "tv_grab_uk_rt(1)"
name: "tv_grab_uk_rt"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tv_grab_uk_rt/"
description: "tv_grab_uk_rt – Grab TV listings for United Kingdom/Republic of Ireland"
---

<h2 class="name">NAME</h2>
<p> tv_grab_uk_rt &#8211; Grab TV listings for United Kingdom/Republic of Ireland </p>
<h2>SYNOPSIS</h2>
<p> tv_grab_uk_rt &#8211;help </p>
<p> tv_grab_uk_rt &#8211;version </p>
<p> tv_grab_uk_rt &#8211;capabilities </p>
<p> tv_grab_uk_rt &#8211;description </p>
<p> tv_grab_uk_rt [&#8211;config-file <font SIZE="-1">FILE</font>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;days N]&nbsp;<wbr>[&#8211;offset N]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;output&nbsp;<wbr><font SIZE="-1">FILE</font>]&nbsp;<wbr>[&#8211;quiet]&nbsp;<wbr>[&#8211;debug] </p>
<p> tv_grab_uk_rt &#8211;configure [&#8211;config-file <font SIZE="-1">FILE</font>] </p>
<p> tv_grab_uk_rt &#8211;configure-api [&#8211;stage <font SIZE="-1">NAME</font>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;config-file&nbsp;<wbr><font SIZE="-1">FILE</font>]&nbsp;<wbr>[&#8211;output&nbsp;<wbr><font SIZE="-1">FILE</font>] </p>
<p> tv_grab_uk_rt &#8211;list-channels [&#8211;config-file <font SIZE="-1">FILE</font>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;output&nbsp;<wbr><font SIZE="-1">FILE</font>]&nbsp;<wbr>[&#8211;quiet]&nbsp;<wbr>[&#8211;debug] </p>
<p> tv_grab_uk_rt &#8211;list-lineups </p>
<p> tv_grab_uk_rt &#8211;get-lineup [&#8211;config-file <font SIZE="-1">FILE</font>]</p>
<h2>DESCRIPTION</h2>
<p> Output <font SIZE="-1">TV</font> listings in <font SIZE="-1">XMLTV</font> format for many channels available in the United Kingdom and Republic of Ireland. Source data comes from machine-readable files made available from the Radio Times website.</p>
<h2>USAGE</h2>
<p> First run <code>tv_grab_uk_rt &#8211;configure</code> to choose which channels you want to receive listings for. Then run <code>tv_grab_uk_rt</code> (with optional arguments) to get around 14 days of listings for your configured channels.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;help</code> Print a help message and exit. </p>
<p> <code>&#8211;version</code> Show the versions of the <font SIZE="-1">XMLTV</font> libraries, the grabber and of key modules used for processing listings. </p>
<p> <code>&#8211;capabilities</code> Show which capabilities the grabber supports. For more information, see &lt;<a rel="nofollow" href="http://wiki.xmltv.org/index.php/XmltvCapabilities">http://wiki.xmltv.org/index.php/XmltvCapabilities</a>&gt; </p>
<p> <code>&#8211;description</code> Show a brief description of the grabber. </p>
<p> <code>&#8211;config-file </code><font SIZE="-1"><code>FILE</code></font> Specify the name of the configuration file to use. If not specified, a default of <code>~/.xmltv/tv_grab_uk_rt.conf</code> is used. This is also the default file written by <code>&#8211;configure</code> and read when grabbing. </p>
<p> <code>&#8211;output </code><font SIZE="-1"><code>FILE</code></font> When grabbing, write output to <font SIZE="-1">FILE</font> rather than to standard output. </p>
<p> <code>&#8211;days N</code> When grabbing, grab N days of data instead of all available. Supported values are 1-15. </p>
<p> <code>&#8211;offset N</code> Start grabbing at today + N days. Supported values are 0-14. </p>
<p> Note that due to the format of the source data, tv_grab_uk_rt always downloads data for all available days and then filters for days specified with &#8211;days and &#8211;offset. Specifying &#8211;days and/or &#8211;offset in order to speed up downloads or reduce data transfer will therefore have no effect. </p>
<p> <code>&#8211;quiet</code> Suppress all progress messages normally written to standard error. </p>
<p> <code>&#8211;debug</code> Provide detailed progress messages to standard error. Due to the volume of debug information produced, it is not advised to use this option during normal grabber use. </p>
<p> <code>&#8211;gui </code><font SIZE="-1"><code>OPTION</code></font> Use this option to enable a graphical interface to be used. <font SIZE="-1">OPTION</font> may be &#8216;Tk&#8217;, or left blank for the best available choice. Additional allowed values of <font SIZE="-1">OPTION</font> are &#8216;Term&#8217; for normal terminal output (default) and &#8216;TermNoProgressBar&#8217; to disable the use of Term::ProgressBar. </p>
<p> <code>&#8211;configure</code> Prompt for which channels/lineup to download listings for, where to store the cache directory for retrieved listings, what character encoding to use for output, and whether to enable programme title and bad character fixups. </p>
<p> <code>&#8211;list-channels</code> Outputs an <font SIZE="-1">XML</font> document containing all channels available to the grabber. </p>
<p> <code>&#8211;list-lineups</code> Outputs an <font SIZE="-1">XML</font> document containing all channel lineups available to the grabber. </p>
<p> <code>&#8211;get-lineup</code> Outputs an <font SIZE="-1">XML</font> document containing the configured channel lineup.</p>
<h2>SOURCE DATA TERMS OF USE</h2>
<p> All data is the copyright of the Radio Times and the use of this data is restricted to personal use only. Commercial use of this data is forbidden. &lt;<a rel="nofollow" href="http://www.radiotimes.com/">http://www.radiotimes.com/</a>&gt; </p>
<p> In accessing this <font SIZE="-1">XML</font> feed, you agree that you will only access its contents for your own personal and non-commercial use and not for any commercial or other purposes, including advertising or selling any goods or services, including any third-party software applications available to the general public.</p>
<h2>CHANNEL LINEUPS</h2>
<p> A channel lineup is a list of <font SIZE="-1">TV</font> and radio channels that are available in a particular location on a particular <font SIZE="-1">TV</font> platform (e.g. Freeview). </p>
<p> Whilst configurations containing individual &#8220;channel=&#8230;&#8221; entries are still supported, the grabber allows a user to select their location and <font SIZE="-1">TV</font> platform at configuration time and have their channel lineup generated dynamically at runtime. This means that if a new channel launches or a channel ceases broadcasting, an update to the relevant lineup (stored on the <font SIZE="-1">XMLTV</font> server) will result in listings containing such channel changes without any reconfiguration by the user.</p>
<h2>CHARACTER ENCODING</h2>
<p> During configuration, the software asks the user to choose the character encoding to be used for output. Currently supported encodings are <font SIZE="-1">UTF-8</font> and <font SIZE="-1">ISO-8859-1.</font></p>
<h2>TITLE PROCESSING</h2>
<p> Over time, listings may contain inconsistent programme details, such as the programme title combined with episode details for some showings of a programme, but separate for others; or the episode title being given as the programme title, and the programme title given as the episode title. Some programme titles may also change slightly over time, or across channels. </p>
<p> Enabling title processing during configuration enables this software to process programme titles against a list of flagged titles. The software will correct such programme titles, which in turn should result in better performance of <font SIZE="-1">PVR</font> software which rely on consistent programme data. Please be aware that enabling title processing will result in the grabber taking slightly longer to complete its operation due to the extra processing overhead. </p>
<p> N.B. Please note that title updates can clearly alter programme titles near to transmission time, and it is therefore quite possible for <font SIZE="-1">PVR</font> schedules to fail if they have been configured using an old title. Whilst care is taken to ensure title updates are made as far ahead of transmission as possible, be aware that last minute updates can be made.</p>
<h2>MIS-ENCODED UTF-8 SOURCE DATA</h2>
<p> Prior to the transition of the <font SIZE="-1">XMLTV</font> service to metabroadcast.com in December 2011, there was an ongoing issue with source data containing mis-encoded <font SIZE="-1">UTF-8</font> characters. Since the transition, the source data should be <font SIZE="-1">UTF-8</font> safe and automatic processing of the data may not be required. A configuration option is provided to permit detection and correction of such character encoding errors and users are recommended to enable this option during configuration.</p>
<h2>PERFORMANCE</h2>
<p> Improvements to date and time handling in the grabber have increased performance 6-7X. Grabbing 14 days of listings with utf-8 and title fixups enabled should take about 2 seconds per configured channel on a typical machine.</p>
<h2>ERROR HANDLING</h2>
<p> tv_grab_uk_rt will only terminate early if it is impossible to continue with grabbing data. This can be due to a lack of channel configuration data, a bad/missing configuration file, or filesystem permission problems. Running the grabber in non-quiet mode should report why the grabber failed. </p>
<p> Non-fatal errors are reported during a grabber run, and can result in listings for a channel being skipped either in part, or entirely. Progress messages will state why data is missing when it is possible to do so. A non-zero exit status will normally be given when the grabber has encountered problems during listings retrieval.</p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> The environment variable <font SIZE="-1">HOME</font> can be set to change where the configuration file is stored. All configuration is stored in <tt>$HOME</tt>/.xmltv/ by default. On Windows it might be necessary to set <font SIZE="-1">HOME</font> to a pathname containing no spaces. </p>
<p> The environment variable <font SIZE="-1">XMLTV_SUPPLEMENT</font> can be set to change where the supplemental <font SIZE="-1">XMLTV</font> files are retrieved from. By default, the file is retrieved from the <font SIZE="-1">XMLTV</font> supplement server. See XMLTV::Supplement for more information. </p>
<p> If you want the grabber to use customised local copies of the supplemental files, you should set <font SIZE="-1">XMLTV_SUPPLEMENT</font> to the path of the directory containing a tv_grab_uk_rt/ directory containing the supplement files. For example, if your local supplement files are stored in /usr/local/share/xmltv/tv_grab_uk_rt/ you should `export XMLTV_SUPPLEMENT=&#8220;/usr/local/share/xmltv/&#8221;` before running the grabber.</p>
<h2>RADIO LISTINGS</h2>
<p> Ironically, the Radio Times feed does not offer listings for radio. They have been asked about the possibility of adding radio listings, but stated that this would require significant development effort. It has not been ruled out entirely, but is unlikely to be added soon. </p>
<p> Users who would like to obtain <font SIZE="-1">BBC</font> radio listings in <font SIZE="-1">XMLTV</font> format are advised to investigate a new grabber that obtains listings from the <font SIZE="-1">BBC</font> Backstage service. See &lt;<a rel="nofollow" href="http://wiki.xmltv.org/index.php/BBC_Backstage">http://wiki.xmltv.org/index.php/BBC_Backstage</a>&gt; for more information.</p>
<h2>MAILING LIST</h2>
<p> You can subscribe to and read the <font SIZE="-1">XMLTV</font> users mailing list by visiting &lt;<a rel="nofollow" href="http://lists.sourceforge.net/lists/listinfo/xmltv-users">http://lists.sourceforge.net/lists/listinfo/xmltv-users</a>&gt;. This is a source of help and advice for new users. A searchable archive of the list is available at &lt;<a rel="nofollow" href="http://news.gmane.org/gmane.comp.tv.xmltv.general">http://news.gmane.org/gmane.comp.tv.xmltv.general</a>&gt;.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/5-xmltv/">xmltv</a></i>(5), &lt;<a rel="nofollow" href="http://wiki.xmltv.org">http://wiki.xmltv.org</a>&gt;, &lt;<a href="http://www.radiotimes.com/">http://www.radiotimes.com/</a>&gt;</p>
<h2>BUGS</h2>
<p> If you encounter a reproducible bug, please report it on the <font SIZE="-1">XMLTV</font> bug tracker at &lt;<a rel="nofollow" href="http://sourceforge.net/tracker/?group_id=39046">http://sourceforge.net/tracker/?group_id=39046</a>&amp;atid=424135&gt;, making sure you assign the bug to the tv_grab_uk_rt category. Please check that the bug has not already been reported. </p>
<p> The source data on the Radio Times website is generated daily before 0600. Occasionally the source data may not get recreated, leaving the source files for some (or all) channels empty. Users are encouraged to wait at least 1 day before reporting an issue with missing listings, as they frequently reappear in the next update or later the same day. If listings continue to be missing from the Radio Times website, please report the fact on the <font SIZE="-1">XMLTV</font> users mailing list. </p>
<p> There have been several occasions in the past when the Radio Times channel index has been missing from the Radio Times website. This file is essential to being able to run the grabber, as it contains the list of channels having available listings data. If this file is missing or empty, and there is no locally-cached copy of the file, it will not be possible to run the grabber. The file usually regenerates automatically over the course of the next day, at which point it will be possible to run the grabber successfully. </p>
<p> There are no other reported ongoing issues.</p>
<h2>AUTHOR</h2>
<p> Since 2007 the maintainer has been Nick Morrott (knowledgejunkie at gmail dot com). </p>
<p> The original author was Ed Avis (ed at membled dot com). Parts of this code were copied from tv_grab_se_swedb by Mattias Holmlund, and from the <font SIZE="-1">XMLTV</font> wiki &lt;<a rel="nofollow" href="http://wiki.xmltv.org/">http://wiki.xmltv.org/</a>&gt;. Regional postcode information was kindly made available from &lt;<a rel="nofollow" href="http://www.ukfree.tv">http://www.ukfree.tv</a>&gt;. </p>
<h2>Index</h2>
