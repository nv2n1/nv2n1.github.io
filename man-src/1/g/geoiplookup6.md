---
title: "geoiplookup6(1)"
name: "geoiplookup6"
section: "1"
letter: "g"
url: "/docs/linux/man/1-geoiplookup6/"
---

<h2 class="name">NAME</h2>
 

 geouplookup6 - look up country using IP Address or hostname 

<h2>SYNOPSIS</h2>

 geouplookup6 [-d directory] [-f filename] [-v] &lt;ipaddress|hostname&gt;

<h2>DESCRIPTION</h2>

 geouplookup6 uses the GeoIP library and database to find the Country that an IP address or hostname originates from. You must install a database suitable for geoiplookup6. IE: GeoIPv6.dat 

 For example: 

 <i>geouplookup6 2001:4860:0:1001::68</i> 

 <i>geoiplookup6 ipv6.google.com</i> 

 will find the Country that 2001:4860:0:1001::68 originates from, in the following format: 

 <i>US, United States</i> 

 

 

 

<h2>OPTIONS</h2>

<dl>
<dt>-f
<dd> Specify a custom path to a single GeoIP datafile.
<dt>-d
<dd> Specify a custom directory containing GeoIP datafile(s). By default geouplookup6 looks in /usr/share/GeoIP
<dt>-v
<dd> Lists the date and build number for the GeoIP datafile(s).</dl>

<h2>AUTHOR</h2>

 Written by T.J. Mather

<h2>REPORTING BUGS</h2>

 Report bugs to &lt;support [at] maxmind.com&gt;

<h2>COPYRIGHT</h2>

 Copyright &#169; 2008 MaxMind, Inc. 

 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/1-geoipupdate/">geoipupdate</a>(1), <a HREF="/docs/linux/man/1-nslookup/">nslookup</a>(1). 

<h2>Index</h2>


