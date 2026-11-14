---
title: "htnotify(1)"
name: "htnotify"
section: "1"
letter: "h"
url: "/docs/linux/man/1-htnotify/"
description: "htnotify – sends email notifications about out-dated web pages discovered by htmerge"
---

<h2 class="name">NAME</h2>
<p> htnotify &#8211; sends email notifications about out-dated web pages discovered by htmerge </p>
<h2>SYNOPSIS</h2>
<p> <code>htnotify</code> <i>[options]</i></p>
<h2>DESCRIPTION</h2>
<p> <i>Htnotify</i> scans the document database created by <i>htmerge</i> and sends an email message for every page that is out of date. Please have a look at the ht://Dig notification manual for instructions on how to set up this service.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b </code><i>database</i></p>
<dd> Specifies an alternative database than what is specified in the configuration file.</p>
<dt><code>-c </code><i>configfile</i></p>
<dd> Use the specified <i>configfile</i> instead of the default. <code>-v</code> Verbose mode. This increases the verbosity of the program. Used once will display a log of what email messages were sent. Used more than once will display information about each document that has email notification set.</dl>
<h2>FILES</h2>
<dl>
<dt><code>/etc/htdig/htdig.conf</code></p>
<dd> The default configuration file.</dl>
<h2>SEE ALSO</h2>
<p> Please refer to the HTML pages (in the htdig-doc package) <code>/usr/share/doc/htdig-doc/html/index.html</code> and the manual pages <i><a href="/docs/linux/man/1-htdig/">htdig</a>(1)</i> and <i><a href="/docs/linux/man/1-htmerge/">htmerge</a>(1)</i> for a detailed description of ht://Dig and its commands.</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Christian Schwarz, modified by Stijn de Bekker, based on the HTML documentation of ht://Dig. </p>
<h2>Index</h2>
