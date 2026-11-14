---
title: "qsgeo(1)"
name: "qsgeo"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qsgeo/"
---

<h2 class="name">NAME</h2>
 

 qsgeo - an utility to lookup a client's country code. 

<h2>SYNOPSIS</h2>

 qsgeo -d &lt;path&gt; [-l] [-s] [-ip &lt;ip&gt;]

<h2>DESCRIPTION</h2>

 Use this utility to resolve the country codes of IP addresses within existing log files. The utility reads the log file data from stdin and writes them, with the injected country code, to stdout.

<h2>OPTIONS</h2>

 

<dl>
<dt>-d &lt;path&gt;
<dd> Specifies the path to the geographical database files (CSV file containing IP address ranges and country codes).
<dt>-s
<dd> Writes a summary of the requests per country only.
<dt>-l
<dd> Writes the database to stdout (ignoring stdin) inserting local (127.*) and private (10.*, 172.16*, 192.168.*) network addresses.
<dt>-ip &lt;ip&gt;
<dd> Resolves a single IP address instead of processing a log file.</dl>

<h2>EXAMPLE</h2>

 Reading the file access_log and adding the country code to the IP address field: 

 
&nbsp;<wbr>&nbsp;<wbr>cat access_log | qsgeo -d GeoIPCountryWhois.csv 

 Reading the file access_log and showing a summary only: 

 
&nbsp;<wbr>&nbsp;<wbr>cat access_log | qsgeo -d GeoIPCountryWhois.csv -s 

 Resolving a single IP address: 

 
&nbsp;<wbr>&nbsp;<wbr>qsgeo -d GeoIPCountryWhois.csv -ip 192.84.12.23 

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/1-qsexec/">qsexec</a>(1), <a HREF="/docs/linux/man/1-qsfilter2/">qsfilter2</a>(1), <a HREF="/docs/linux/man/1-qsgrep/">qsgrep</a>(1), <a HREF="/docs/linux/man/1-qshead/">qshead</a>(1), <a HREF="/docs/linux/man/1-qslog/">qslog</a>(1), <a HREF="/docs/linux/man/1-qslogger/">qslogger</a>(1), <a HREF="/docs/linux/man/1-qspng/">qspng</a>(1), <a HREF="/docs/linux/man/1-qsrotate/">qsrotate</a>(1), <a HREF="/docs/linux/man/1-qssign/">qssign</a>(1), <a HREF="/docs/linux/man/1-qstail/">qstail</a>(1)

<h2>AUTHOR</h2>

 Pascal Buchbinder, <a rel="nofollow" HREF="http://opensource.adnovum.ch/mod_qos/">http://opensource.adnovum.ch/mod_qos/</a> 

<h2>Index</h2>


