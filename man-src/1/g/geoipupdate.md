---
title: "geoipupdate(1)"
name: "geoipupdate"
section: "1"
letter: "g"
url: "/docs/linux/man/1-geoipupdate/"
---

<h2 class="name">NAME</h2>
 

 geoipupdate - a program for updating the MaxMind GeoIP databases 

<h2>SYNOPSIS</h2>

 geoipupdate [-v] [-f licensefile]

<h2>DESCRIPTION</h2>

 geoipupdate automatically updates the GeoIP database for GeoIP subscribers. It connects to the MaxMind GeoIP Update server and checks for an updated database. If it finds an updated database, then it downloads it, uncompresses it, and installs it. If you are running a firewall, it requires that the DNS and HTTP (80) ports be open. 

 For example 

 <i>geoipupdate -v</i> 

 Performs the update in verbose mode. 

<h2>OPTIONS</h2>

<dl>
<dt>-v
<dd> Verbose mode, prints out the steps that geoipupdate takes.
<dt>-d
<dd> Specify a custom directory target to install the GeoIP datafile(s). By default geoipupdate installs to /usr/share/GeoIP
<dt>-f
<dd> Specifies the configuration file that contains the license key. Defaults to /etc/GeoIP.conf</dl>

<h2>USAGE</h2>

 Typically you'll want to write a weekly crontab that will run geoipupdate. Below is a sample crontab that runs geoipupdate on each Wednesday at noon: 

<dl>
<dt>
<dd> # top of crontab 

 MAILTO=your [at] email.com 

 0 12 * * 3 BIN_DIR/geoipupdate 

 # end of crontab</dl>
 To use with a proxy server, set the http_proxy environment variable. E.g.
<dl>
<dt>
<dd> export http_proxy=&quot;<a rel="nofollow" HREF="http://proxy-hostname:port">http://proxy-hostname:port</a>&quot;</dl>

<h2>RETURN CODES</h2>

 geoipupdate returns 0 on success, 1 on error.

<h2>FILES</h2>

 

 <i>/etc/GeoIP.conf</i> 

 Configuration file for GeoIP, should contain license key.

<h2>AUTHOR</h2>

 Written by T.J. Mather

<h2>REPORTING BUGS</h2>

 Report bugs to &lt;support [at] maxmind.com&gt;

<h2>COPYRIGHT</h2>

 Copyright &#169; 2011 MaxMind, Inc. 

 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

<h2>SEE ALSO</h2>

 Visit &lt;<a rel="nofollow" HREF="http://www.maxmind.com/app/products">http://www.maxmind.com/app/products</a>&gt; to sign up for a GeoIP subscription. 

 <a HREF="/docs/linux/man/1-geoiplookup/">geoiplookup</a>(1), <a HREF="/docs/linux/man/5-crontab/">crontab</a>(5) 

<h2>Index</h2>


