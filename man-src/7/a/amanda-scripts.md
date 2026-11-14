---
title: "amanda-scripts(7)"
name: "amanda-scripts"
section: "7"
letter: "a"
url: "/docs/linux/man/7-amanda-scripts/"
description: "amanda-scripts – Configuring and using the Script API"
---

<p>amanda-scripts &#8211; Configuring and using the Script API</p>
<h2>Description</h2>
<p>The Script API is a flexible system for invoking user-supplied scripts at various points in the execution of Amanda. This manual page describes the operation and configuration of the API. For help writing Script API scripts, see <a rel="nofollow" href="http://wiki.zmanda.com/index.php/Script_API.">http://wiki.zmanda.com/index.php/Script_API.</a></p>
<h2>Scripts</h2>
<p>This section lists the scripts included with Amanda, see the individual man page for instructions on using them. For complete How-To information, consult the Amanda wiki at <a rel="nofollow" href="http://wiki.zmanda.com.">http://wiki.zmanda.com.</a> </p>
<dl>
<dd>&bull; <code><a href="/docs/linux/man/8-amzfs-snapshot/">amzfs-snapshot</a></code>(8), &#8211; create/destroy zfs snapshot.</dl>
<dl>
<dd>&bull; <code><a href="/docs/linux/man/8-script-email/">script-email</a></code>(8), &#8211; send email.</dl>
<p> Script properties work just like application properties: they are insensitive to case, and &#8211; (dash) and _ (underscore) may be used interchangeably.</p>
<h2>Scripts Output Property</h2>
<p>A pre-dle-amcheck, pre-dle-estimate or pre-dle-backup executed on the client can output property on stdout that are sent to the application. If the output line matches &quot;PROPERTY str1 str2&quot;, Amanda sets a property called &quot;str1&quot; by the value of &quot;str2&quot;, that property is sent to the application.</p>
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
