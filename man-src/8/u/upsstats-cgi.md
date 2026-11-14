---
title: "upsstats-cgi(8)"
name: "upsstats-cgi"
section: "8"
letter: "u"
url: "/docs/linux/man/8-upsstats-cgi/"
description: "upsstats.cgi – Web-based UPS status viewer"
---

<p>upsstats.cgi &#8211; Web-based UPS status viewer</p>
<h2>Synopsis</h2>
<p><code>upsstats.cgi</code></p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 As a CGI program, this should be invoked through your web server. If you run it from the command line, it will either complain about unauthorized access or spew a bunch of HTML at you. </p>
<h2>Description</h2>
<p><code>upsstats.cgi</code> uses template files to build web pages containing status information from UPS hardware. It can repeat sections of those template files to monitor several UPSes simultaneously, or focus on a single UPS. </p>
<p> These templates can also include references to <code><a href="/docs/linux/man/8-upsimage-cgi/">upsimage.cgi</a></code>(8) for graphical displays of battery charge levels, voltage readings, and the UPS load.</p>
<h2>Access Control</h2>
<p>upsstats will only talk to <code><a href="/docs/linux/man/8-upsd/">upsd</a></code>(8) servers that have been defined in your <code><a href="/docs/linux/man/5-hosts-conf/">hosts.conf</a></code>(5). If it complains that &quot;Access to that host is not authorized&quot;, check that file first.</p>
<h2>Templates</h2>
<p>The web page that is displayed is actually a template containing commands to upsstats which are replaced by status information. The default file used for the overview is upsstats.html. </p>
<p> When monitoring a single UPS, the file displayed is upsstats-single.html. </p>
<p> The format of these files, including the possible commands, is documented in <code><a href="/docs/linux/man/5-upsstats-html/">upsstats.html</a></code>(5).</p>
<h2>Files</h2>
<p><code><a href="/docs/linux/man/5-hosts-conf/">hosts.conf</a></code>(5), <code><a href="/docs/linux/man/5-upsstats-html/">upsstats.html</a></code>(5), upsstats-single.html</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-upsimage-cgi/">upsimage.cgi</a></code>(8)</p>
<h3>Internet resources:</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> </p>
