---
title: "calamaris(1)"
name: "calamaris"
section: "1"
letter: "c"
url: "/docs/linux/man/1-calamaris/"
description: "calamaris – generate statistic out of log files from Proxy-Cache-Servers"
---

<h2 class="name">NAME</h2>
<p> calamaris &#8211; generate statistic out of log files from Proxy-Cache-Servers</p>
<h2>SYNOPSIS</h2>
<p> cat log | <code>calamaris</code> [ calamaris_options ] </p>
<h2>DESCRIPTION</h2>
<p> <code>Calamaris</code> is used to produce statistical output from <code>Squid</code>, <code>NetCache,</code> <code>Inktomi Traffic Server,</code> <code>Oops! proxy server,</code> <code>Compaq Tasksmart,</code> <code>Cisco Content Engines</code> or related Proxy log files. The resulting output can be <i>ascii</i> or <i>html</i>. It is possible to cache calculated data in a file to use them in later runs. </p>
<p> This manual page describes the options of <code>Calamaris</code> and gives a few examples. </p>
<h2>OPTIONS</h2>
<h3>Reports</h3>
<dl>
<dt><i>-a</i></p>
<dd> all: extracts all reports available, <i>-a</i> equals <i>-D 10 -d 20 -P 60 -r 20 -s -t 20</i>. </p>
<dt><i>-d n</i></p>
<dd> domain report: switches the top level and the second level report on. The data is derived from the URL. The output is limited by n. (-1 is unlimited) </p>
<dt><i>-p type</i></p>
<dd> peak report: Measures the peaks of the Proxy usage in requests per second, per minute and per hour. It reports peaks for TCP, UDP and ALL requests. If set to <i>&#8216;old&#8217;</i> these values were calculated with the old slow method, if set to <i>&#8216;new&#8217;</i> the new faster (but still slow) method is used. </p>
<dt><i>-P n</i></p>
<dd> performance report: Shows the throughput of TCP requests for every n minutes. </p>
<dt><i>-r n</i></p>
<dd> requester report: Switches the UDP and TCP requester reports on. The output is limited by n. (-1 is unlimited) </p>
<dt><i>-R n</i></p>
<dd> Requested report: adds to each line of the requester report the requested URLs. The output is limited by n. (-1 is unlimited, and can result in very very long reports.) </p>
<p> <code>Warning:</code> Using this option breaks the privacy of your users! (see PRIVACY-Section below) </p>
<dt><i>-s</i></p>
<dd> status report: alters the default behaviour of <code>Calamaris</code> and makes the status reports more verbose. </p>
<dt><i>-t n</i></p>
<dd> type report: switches the content type and the file extension report on. The output is limited by n. (-1 is unlimited) </p>
<dt><i>-D n</i></p>
<dd> Distribution Histogram: shows size-based distribution of requested objects, smaller numbers result in more verbose reports. (choose 2, 10 or 100 for useful output.) </p>
<p> Allocation report: shows how different sized objects perform on your Proxy. </p>
</dl>
<h3>Input Format</h3>
<dl>
<dt><i>-f type</i></p>
<dd> format: sets the type of input logfiles. If set to </p>
<p> <i>&#8216;auto&#8217;</i> <code>Calamaris</code> tries to guess the input file format. This is the Default. </p>
<p> <code>Note:</code> If the first line of your input file is corrupted, Calamaris will stop with an error. </p>
<p> <i>&#8216;squid&#8217;</i> <code>Calamaris</code> expects native logfile derived from <code>Squid V1.1.beta26-V2.x</code> or <code>OOPS.</code> </p>
<p> <i>&#8216;squid-extended&#8217;</i> <code>Calamaris</code> expects native logfile derived from <code>Squid V1.1.alpha1-V2.x</code> with <i>log_mime_hdrs</i> enabled or <code>Squid</code> with <code>Smartfilter-Patch.</code> or squid-style logfiles out of <code>Cisco Content Engines.</code> (This only enables parsing of these kind of logfile, the additional data will be ignored.) </p>
<p> (Logging of MIME-Headers breaks the privacy of your users! (see PRIVACY-Section below) </p>
<p> <i>&#8216;squid-old&#8217;</i> <code>Calamaris</code> expects native logfile derived from <code>Squid V1.1.alpha1-V1.1.beta25.</code> </p>
<p> <i>&#8216;nc&#8217;</i> <code>Calamaris</code> expects Logfiles from <code>NetCache up to V4.x.</code> (Please see the README on this.) </p>
<p> <i>&#8216;its&#8217;</i> <code>Calamaris</code> expects Logfiles from <code>Inktomi Traffic Server.</code> </p>
<p> <i>&#8216;elff&#8217;</i> <code>Calamaris</code> expects Logfiles in Extended Logfile Format (i.e. from <code>Compaq Tasksmart,</code> <code>Novell Internet Caching System</code> or <code>NetCache V5.x</code> ) </p>
<p> <i>&#8216;nse&#8217;</i> <code>Calamaris</code> expects Logfiles in Netscape Extended-1 or Netscape Extended-2 Logfile Format (from <code>Netscape/ipoint Proxy-Server</code> ) </p>
</dl>
<h3>Output Format</h3>
<p> Standard output format is plain ascii with 80 chars width. </p>
<dl>
<dt><i>-F type[,type[,type[,&#8230;]]]</i></p>
<dd> Format: sets the format of the output-report. If set to </p>
<p> <i>&#8216;mail&#8217;</i> adds a subject header to the beginning of the report. </p>
<p> <i>&#8216;html&#8217;</i> all output is given in html with tables. Can be combined with <i>&#8216;mail&#8217;</i> to send html mails. </p>
<p> <i>&#8216;html-embed&#8217;</i> all output is given in html with tables without HTML-Headers. Useful for Server-Side-Includes. </p>
<p> <i>&#8216;unformatted&#8217;</i> gives out the raw numbers seperated by spaces. Useful for re-using the output in other scripts. If you use this along with <i>-U,</i> the byte values are calculated in the given Unit, and displayed without indication along with the numbers. the indication moves up to the header of the report. </p>
<dt><i>-M string</i></p>
<dd> Meta: adds a custom string into the &lt;HEAD&gt; of a HTML-Report. Useful if you want to add Stylesheets or something to the Report. </p>
<p> <code>Note:</code> <i>-M</i> works only in combination with <i>-F</i> html. </p>
<dt><i>-l string</i></p>
<dd> logo: add a custom string to a HTML-Report. It&#8217;ll be added to a table on the top of the output. <i>-l &#8216;&lt;A href=<a rel="nofollow" href="http://cord.de/">http://cord.de/</a>&gt;&lt;IMG BORDER=0 SRC=<a href="http://cord.de/Images/cord/cordlog2n.gif">http://cord.de/Images/cord/cordlog2n.gif</a> ALT=Cord&gt;&lt;/A&gt;&#8217;</i> will add my logo with a link to the Report. </p>
<p> <code>Note:</code> <i>-l</i> works only in combination with <i>-F</i> html. </p>
<dt><i>-U string</i></p>
<dd> Unit: You can define this to K(ilo), M(ega), G(iga) or T(era) for the Byte-units. </p>
<dt><i>-S n[,n[,n[,&#8230;]]]</i></p>
<dd> Show: Shows only the defined reports in the specified order. Default is to display the reports as they are defined through the report-switches above. The following numbers are defined: </p>
<dl>
<dt>
<dd> 0 Summary</dl>
<dl>
<dt>
<dd> 1 Incoming request peak per protocol</dl>
<dl>
<dt>
<dd> 2 Incoming transfer volume per protocol</dl>
<dl>
<dt>
<dd> 3 Incoming requests by method</dl>
<dl>
<dt>
<dd> 4 Incoming UDP-requests by status</dl>
<dl>
<dt>
<dd> 5 Incoming TCP-requests by status</dl>
<dl>
<dt>
<dd> 6 Outgoing requests by status</dl>
<dl>
<dt>
<dd> 7 Outgoing requests by destination</dl>
<dl>
<dt>
<dd> 8 Request-destinations by 2ndlevel-domain</dl>
<dl>
<dt>
<dd> 9 Request-destinations by toplevel-domain</dl>
<dl>
<dt>
<dd> 10 TCP-Request-protocol</dl>
<dl>
<dt>
<dd> 11 Requested content-type</dl>
<dl>
<dt>
<dd> 12 Requested extensions</dl>
<dl>
<dt>
<dd> 13 Incoming UDP-requests by host</dl>
<dl>
<dt>
<dd> 14 Incoming TCP-requests by host</dl>
<dl>
<dt>
<dd> 15 Distribution Histogram</dl>
<dl>
<dt>
<dd> 16 Performance in minute steps </p>
<p> <code>Note:</code> Using this doesn&#8217;t make <code>Calamaris</code> any faster, the internal calculations will be done as the report-switches were set (see above). </p>
</dl>
</dl>
<h3>Caching</h3>
<dl>
<dt><i>-i file</i></p>
<dd> input file: You can reuse a cache file generated with <i>-o file</i> to add old data to a new report. Several files can be seperated with a &#8216;:&#8217;. </p>
<p> <code>Note:</code> if you use more than one cache file, make sure they are chronologicaly ordered (oldest first). </p>
<p> <code>Note:</code> if you reuse cache-files, which were not created with <i>-d -1 -r -1 -t -1 -R -1</i> the number of &#8216;others&#8217; is likely wrong everywhere. </p>
<dt><i>-o file</i></p>
<dd> output file: <code>Calamaris</code> stores a summary of the computed information in <i>file</i> and you can reuse it at a later time with <i>-i</i>. </p>
<p> <code>Note:</code> The output file can be the same as the input file: it is simply overwritten after reading the data. It is not recommended to change the options between different runs if you include older data as this can result in strange measurements. </p>
</dl>
<h3>Misc</h3>
<dl>
<dt><i>-H name</i></p>
<dd> Host name: The name for the title or subject of the output. If set to <i>&#8216;lookup&#8217;</i> <code>Calamaris</code> looks up the host name of the system its been run on. </p>
<dt><i>-n</i></p>
<dd> no lookup: Switches the IP lookup for the requesters off. </p>
<dt><i>-O</i></p>
<dd> Order: Changes the sort order in the reports to request size, default is sorting by number of requests. </p>
<dt><i>-I t-t </i></p>
<dd> Interval: defines which time-interval should be parsed. t has to be the format yyyymmddhhmmss </p>
<p> <code>Note:</code> omitting the beginning or ending date is allowed. </p>
<dt><i>-N</i></p>
<dd> N-level: All URL-Host reports will be switched from 2nd-level to N-level-reports. (-1 shows a full urlhost-report) </p>
<p> <code>Note:</code> This option is only useful with activated domain-report. </p>
<dt><i>-T n</i></p>
<dd> Time: Adjust the Performancereport in minutes for non GMT-Timezoners. </p>
<dt><i>-c</i></p>
<dd> case: Switch to case-insensitive. This is useful for the &#8216;Requested extensions&#8217; report. </p>
<dt><i>-u</i></p>
<dd> user: Switches the usage of eventually available ident information for requester reports on. </p>
<p> <code>Warning:</code> This breaks the privacy of your users! (see PRIVACY-Section below) </p>
<dt><i>-z</i></p>
<dd> zero: Switches reading from standard input off. You can use this to merge many cache files to one (see <i>-i</i> and <i>-o</i>) or to generate a report out of cache files. </p>
<dt><i>-b n</i></p>
<dd> benchmark: A switch for the impatient as it prints a &#8216;#&#8217; for every n parsed lines. </p>
<dt><i>-v</i></p>
<dd> verbose: print more information about what is Calamaris is doing and believing. </p>
<dt><i>-L</i></p>
<dd> Loop: prints the internal loop to STDERR. (for Debugging) </p>
<dt><i>-C</i></p>
<dd> Copyright: Prints the copyright information of <code>Calamaris</code>. </p>
<dt><i>-h</i></p>
<dd> help: Prints a brief description of the command line options. </p>
<dt><i>-V</i></p>
<dd> Version: Prints out the Version-Number. </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>This example mails the daily statistics to root:</p>
<dd> cat /var/log/squid/access.log | nice -39 <code>calamaris</code> -aH &#8216;daily worf&#8217; -F mail | mail root </p>
<dt>This one only caches a summary for later use:</p>
<dd> cat /var/log/squid/access.log | <code>calamaris</code> -a -o daily.`date +&quot;%w&quot;` &gt; /dev/null </p>
<dt>You can then use the caches to have weekly statistics:</p>
<dd>
<p> if [ $DAYOFWEEK = &quot;0&quot; ]; then <code>calamaris</code> -a -i daily.1:daily.2:daily.3:daily.4:daily.5:daily.6:daily.0 -z -F mail -H &quot;weekly worf&quot; | mail root ; fi </p>
</dl>
<h2>BUGS</h2>
<p> If you have a problem with <code>Calamaris</code>, please make sure that you use the recent version of <code>Calamaris</code> (see VERSION below). Also check that your proxy works correctly and doesn&#8217;t produce invalid Logfiles. (see the README for buglist and pointers.) </p>
<p> If you&#8217;re sure that you&#8217;ve encountered a bug in Calamaris, please report it to Calamaris-bug [at] cord.de. This also applies if Calamaris itself says &#8216;please report this&#8217;. </p>
<h2>PRIVACY</h2>
<p> <code>Calamaris</code> can be (mis-)used to track what users are requesting. </p>
<p> So please read the following and think about it, before using <code>Calamaris</code> to be the <i>Big Brother.</i> </p>
<dl>
<dt>&#8211;</p>
<dd> If you don&#8217;t trust your users than there is something more wrong than the loss of productivity. </p>
<dt>&#8211;</p>
<dd> Squid has some nice acl-mechanisms. If you think that your users don&#8217;t use the net properly, don&#8217;t let them use it. (You can also open the net at specific times or to specific sites, if you want.) </p>
<dt>&#8211;</p>
<dd> If you still want to use Calamaris that way, let your vict^Wusers know, that they&#8217;ll be monitored. (in Germany you have to let them know!) </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-squid/">squid</a>(8)</code> </p>
<h2>AUTHOR</h2>
<p> Cord Beermann &lt;Cord [at] Wunder-Nett.org&gt;. There are also a lot of people who contributed code, gave ideas or requested features. Look them up in the executable. </p>
<p> This man page was written by Philipp Frauenfelder &lt;pfrauenf [at] debian.org&gt;, maintainer of the Debian package. Maintenance is now taken over by Cord Beermann. </p>
<h2>VERSION</h2>
<p> Version of this manpage: $Id: calamaris.1,v 1.28 2003/05/14 21:22:37 cord Exp $ </p>
<p> It describes the usage of Calamaris V2.58 and later. </p>
<p> Information about new releases, mailing lists, and other related issues can be found from the <code>Calamaris</code> home page at <a rel="nofollow" href="http://Calamaris.Cord.de/">http://Calamaris.Cord.de/</a> </p>
<h2>WARRANTY</h2>
<p> <code>Calamaris</code> comes with &quot;absolutely no warranty&quot;. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1997, 1998, 1999, 2000, 2001, 2002, 2003 Cord Beermann </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> (If you modify and want to publish it under the name <code>Calamaris</code>, please ask me. I don&#8217;t want to confuse the &#8216;audience&#8217; with many different versions of the same name and/or Version number. (This is not part of the license, it is only a favour i asked of you.)) </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 59 Temple Place &#8211; Suite 330, Boston, MA 02111-1307, USA. </p>
<h2>Index</h2>
