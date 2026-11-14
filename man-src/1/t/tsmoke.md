---
title: "tsmoke(1)"
name: "tsmoke"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tsmoke/"
description: "tSmoke – Commandline tool for sending SmokePing information"
---

<p>tSmoke &#8211; Commandline tool for sending SmokePing information </p>
<h2>Synopsis</h2>
<p><code>tSmoke</code> [ <code>&#8211;testmail</code> | <code>&#8211;morning</code> | <code>&#8211;weekly</code> | <code>&#8211;version</code> | <code>&#8211;help</code> | <code>&#8211;man</code>] </p>
<pre> Options:
 --man Show the manpage
 --help Help :-)
 --version Show SmokePing Version
 --testmail Send a test message
 --listrrds List the RRDs used by this Smokeping
 --morning Send a morning synopsis
 --weekly Send a weekly status report
 --to E-mail address to send message (i.e. '--to=xyz [at] company.com.invalid'
 --detail How much detail to send in weekly report (i.e. '--detail=1')
 --quiet Do not print welcome</pre>
<h2>Description</h2>
<p>The <code>tSmoke</code> tool is a commandline tool which interfaces with the SmokePing system. Its main function is to send a message indicating the current status of the systems being monitored by Smokeping or an <font SIZE="-1">HTML</font> mail file containing the status over the past day, past week and past month including an overview. </p>
<p> Typical crontab used to invoke this are </p>
<pre> # Quick morning alert to see what's down
 0 6 * * * /usr/local/smokeping/bin/tSmoke.pl --q --to=mobilephone [at] att.net.invalid --morning
 # Weekly report on the percent availability of network systems with no detail
 0 8 * * * /usr/local/smokeping/bin/tSmoke.pl --q --to=mailbox [at] company.com.invalid --weekly --detail=0</pre>
<h2>Setup</h2>
<p>When installing tSmoke, some variables must be adjusted to fit your local system. </p>
<p> We need to use the following <code>libraries</code>:</p>
<dl COMPACT>
<dt>Smokeping</p>
<dd>
<dt>RRDTool Perl bindings</p>
<dd>
<dt>Getopt::Long</p>
<dd></dl>
<p> Set up your libraries: </p>
<pre> use lib &quot;/usr/local/smokeping/lib&quot;;
 use lib &quot;/usr/local/rrdtool-1.0.39/lib/perl&quot;;</pre>
<p>Point to your Smokeping <code>config</code> file </p>
<pre> my $cfgfile = &quot;/usr/local/smokeping/etc/config&quot;;</pre>
<p>Modify the Smokeping config file to include a path for tmail in the General section: </p>
<pre> tmail = /usr/local/smokeping/etc/tmail</pre>
<h2>Copyright</h2>
<p>Copyright (c) 2003 by Dan McGinn-Combs. All right reserved.</p>
<h2>License</h2>
<p>This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE. </font> See the <font SIZE="-1">GNU</font> General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, <font SIZE="-1">MA 02139, USA.</font></p>
<h2>Author</h2>
<p>Dan McGinn-Combs &lt;d.mcginn-combs [at] mindspring.com&gt; </p>
<p> Modified for Smokeping official distribution by Niko Tyni &lt;ntyni [at] iki.fi&gt;</p>
