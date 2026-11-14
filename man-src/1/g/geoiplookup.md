---
title: "geoiplookup(1)"
name: "geoiplookup"
section: "1"
letter: "g"
url: "/docs/linux/man/1-geoiplookup/"
---

<h2 class="name">NAME</h2>
 

 geoiplookup - look up country using IP Address or hostname 

<h2>SYNOPSIS</h2>

 geoiplookup [-d directory] [-f filename] [-v] &lt;ipaddress|hostname&gt;

<h2>DESCRIPTION</h2>

 geoiplookup uses the GeoIP library and database to find the Country that an IP address or hostname originates from. 

 For example 

 <i>geoiplookup 80.60.233.195</i> 

 will find the Country that 80.60.233.195 originates from, in the following format: 

 <i>NL, Netherlands</i> 

<h2>OPTIONS</h2>

<dl>
<dt>-f
<dd> Specify a custom path to a single GeoIP datafile.
<dt>-d
<dd> Specify a custom directory containing GeoIP datafile(s). By default geoiplookup looks in /usr/share/GeoIP
<dt>-v
<dd> Lists the date and build number for the GeoIP datafile(s).</dl>

<h2>AUTHOR</h2>

 Written by T.J. Mather

<h2>REPORTING BUGS</h2>

 Report bugs to &lt;support [at] maxmind.com&gt;

<h2>COPYRIGHT</h2>

 Copyright &#169; 2006 MaxMind, Inc. 

 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/1-geoipupdate/">geoipupdate</a>(1), <a HREF="/docs/linux/man/1-nslookup/">nslookup</a>(1). 

<h2>Index</h2>


