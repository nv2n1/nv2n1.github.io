---
title: "upsset-conf(5)"
name: "upsset-conf"
section: "5"
letter: "u"
url: "/docs/linux/man/5-upsset-conf/"
description: "upsset.conf – Configuration for Network UPS Tools upsset.cgi"
---

<p>upsset.conf &#8211; Configuration for Network UPS Tools upsset.cgi</p>
<h2>Description</h2>
<p>This file only does one job&#8212;it lets you convince <code><a href="/docs/linux/man/8-upsset-cgi/">upsset.cgi</a></code>(8) that your system&#8217;s CGI directory is secure. The program will not run until this file has been properly defined.</p>
<h2>Security Requirements</h2>
<p><code><a href="/docs/linux/man/8-upsset-cgi/">upsset.cgi</a></code>(8) allows you to try login name and password combinations. There is no rate limiting, as the program shuts down between every request. Such is the nature of CGI programs. </p>
<p> Normally, attackers would not be able to access your <code><a href="/docs/linux/man/8-upsd/">upsd</a></code>(8) server directly as it would be protected by the LISTEN directives in your <code><a href="/docs/linux/man/5-upsd-conf/">upsd.conf</a></code>(5) file, tcp-wrappers (if available when NUT was built), and hopefully local firewall settings in your OS. </p>
<p> <code>upsset</code> runs on your web server, so upsd will see it as a connection from a host on an internal network. It doesn&#8217;t know that the connection is actually coming from someone on the outside. This is why you must secure it. </p>
<p> On Apache, you can use the .htaccess file or put the directives in your httpd.conf. It looks something like this, assuming the .htaccess method: </p>
<dl>
<dd>
<pre>&lt;Files upsset.cgi&gt;
deny from all
allow from your.network.addresses
&lt;/Files&gt;</pre>
</dl>
<p> You will probably have to set &quot;AllowOverride Limit&quot; for this directory in your server-level configuration file as well. </p>
<p> If this doesn&#8217;t make sense, then stop reading and leave this program alone. It&#8217;s not something you absolutely need to have anyway. </p>
<p> Assuming you have all this done, and it actually works (test it!), then you may add the following directive to this file: </p>
<dl>
<dd>
<pre>I_HAVE_SECURED_MY_CGI_DIRECTORY</pre>
</dl>
<p> If you lie to the program and someone beats on your upsd through your web server, don&#8217;t blame me.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-upsset-cgi/">upsset.cgi</a></code>(8)</p>
<h3>Internet resources:</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> </p>
