---
title: "mrtg-webserver(1)"
name: "mrtg-webserver"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mrtg-webserver/"
---

<h2 class="name">NAME</h2>
 

 mrtg-webserver - hints for web server configuration 

<h2>SYNOPSIS</h2>

 If you want people to actually see the results of your network monitoring efforts you will need a webserver. 

 This document lists some configuration hints for webservers. Contributions welcome.

<h2>APACHE</h2>

<h3>Configuring mod_expire</h3>

 A big issue with mrtg monitoring data is the expiry time. All these nice graphs you can create are only valid for a short time. If you do not take special action some webbrowsers will not notice this and you may end up with people seeing old data because of caching issues. 

 The apache module mod_expire allows you to setup special expiry properties for individual file. 

 Here is an example for how this may look for an mrtg web directory. The configuration directives can be stored into a <i>.htaccess</i> file. 

 <pre>
 ############################################################
 # Example .htaccess for use with apache-1.2 and mod_expire.
 # (mod_expire come with apache-1.2 but you have to explicitly
 # activate it when compiling the httpd ...)
 #############################################################
 #
 &lt;Files &quot;*-day.png&quot;&gt;
 ExpiresActive On                  # enable expirations
 # five minutes
 ExpiresDefault M300
 &lt;/Files&gt;
 &lt;Files &quot;*-week.png&quot;&gt;
 ExpiresActive On
 ExpiresDefault M1800
 &lt;/Files&gt;
 &lt;Files &quot;*-month.png&quot;&gt;
 ExpiresActive On
 ExpiresDefault M7200
 &lt;/Files&gt;
 &lt;Files &quot;*-year.png&quot;&gt;
 ExpiresActive On
 ExpiresDefault M86400
 &lt;/Files&gt;
 &lt;Files &quot;*.html&quot;&gt;
 ExpiresActive On
 ExpiresDefault M300
 &lt;/Files&gt;
 # index.html is not automatically generated
 &lt;Files &quot;index.html&quot;&gt;
 ExpiresActive Off
 &lt;/Files&gt;
</pre>

<h2>AUTHOR</h2>

 Unknown 

<h2>Index</h2>


