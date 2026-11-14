---
title: "amanda-applications(7)"
name: "amanda-applications"
section: "7"
letter: "a"
url: "/docs/linux/man/7-amanda-applications/"
description: "amanda-applications – Application-api for amanda"
---

<p>amanda-applications &#8211; Application-api for amanda</p>
<h2>Description</h2>
<p>Describe how to use application with Amanda</p>
<h2>Applications</h2>
<p>This section lists the applications included with Amanda. See the individual man pages for instructions on using them. For complete How-To information, consult the Amanda wiki at <a rel="nofollow" href="http://wiki.zmanda.com.">http://wiki.zmanda.com.</a> </p>
<dl>
<dd>&bull; <code><a href="/docs/linux/man/8-amgtar/">amgtar</a></code>(8), &#8211; use GNU Tar to backup and restore data.</dl>
<dl>
<dd>&bull; <code><a href="/docs/linux/man/8-ampgsql/">ampgsql</a></code>(8), &#8211; use PostgreSQL&#8217;s continuous WAL archiving.</dl>
<dl>
<dd>&bull; <code><a href="/docs/linux/man/8-amraw/">amraw</a></code>(8), &#8211; use open and read to read the data.</dl>
<dl>
<dd>&bull; <code><a href="/docs/linux/man/8-amsamba/">amsamba</a></code>(8), &#8211; use smbclient to backup and restore data.</dl>
<dl>
<dd>&bull; <code><a href="/docs/linux/man/8-amstar/">amstar</a></code>(8), &#8211; use star to backup and restore data.</dl>
<dl>
<dd>&bull; <code><a href="/docs/linux/man/8-amsuntar/">amsuntar</a></code>(8), &#8211; use native tar on Solaris to backup and restore data.</dl>
<dl>
<dd>&bull; <code><a href="/docs/linux/man/8-amzfs-sendrecv/">amzfs-sendrecv</a></code>(8), &#8211; use zfs to create a snapshot and use &#8216;zfs send&#8217; to generate the backup.</dl>
<dl>
<dd>&bull; <code><a href="/docs/linux/man/8-amzfs-snapshot/">amzfs-snapshot</a></code>(8), &#8211; use zfs to create a snapshot and for use with other applications (e.g. amgtar)</dl>
<h2>Defining Applications</h2>
<p>An application is defined in <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5) as follows: </p>
<pre>define application-tool $appconfigname {
 plugin &quot;$pluginname&quot;
 property &quot;$PROPERTY_NAME&quot; &quot;$PROPERTY_VALUE&quot;
 ...
}</pre>
<p>and then referenced in a dumptype as </p>
<pre>define dumptype $dumptypename {
 ...
 program &quot;APPLICATION&quot;
 application &quot;$appconfigname&quot;
}</pre>
<p>Application properties, like Amanda configuration parameters, are insensitive to case, and &#8211; (dash) and _ (underscore) may be used interchangeably. </p>
<p> See the individual plugin documentation for properties applicable to each plugin.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Authors</h2>
<p><code>Jean-Louis Martineau</code> &lt;martineau [at] zmanda.com&gt;</p>
<dl>
<dd>Zmanda, Inc. (<a rel="nofollow" href="http://www.zmanda.com)">http://www.zmanda.com)</a></dl>
<p> <code>Dustin J. Mitchell</code> &lt;dustin [at] zmanda.com&gt;</p>
<dl>
<dd>Zmanda, Inc. (<a rel="nofollow" href="http://www.zmanda.com)">http://www.zmanda.com)</a></dl>
