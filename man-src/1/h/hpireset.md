---
title: "hpireset(1)"
name: "hpireset"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hpireset/"
description: "hpireset – This sample openhpi application exercises HPI Reset Management APIs."
---

<h2 class="name">NAME</h2>
<p> hpireset &#8211; This sample openhpi application exercises HPI Reset Management APIs. </p>
<h2>SYNOPSIS</h2>
<pre><code>
hpireset[-D nn][-N host[:port]][-C&lt;cfgfile&gt;][-r - w - h - X] hpireset[--domain nn][--host = host[:port]][--cfgfile = file][--hard-- warm-- help-- debug]
</code></pre>
<h2>DESCRIPTION</h2>
<p> hpireset searches the Resource Presence Table (<font SIZE="-1">RPT</font>) for resources with Reset Capability. It sends the requested reset action to all resources with <font SIZE="-1">SAHPI_CAPABILITY_RESET.</font> </p>
<p> If no domain is selected, hpireset uses a session with the default domain. The selected domain id must be configured via the openhpidclient.conf file specified in the environment.</p>
<h2>OPTIONS</h2>
<h3>Help Options:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show help options</dl>
<h3>Application Options:</h3>
<dl>
<dt><code>-r</code>, <code>&#8211;hard</code></p>
<dd> Hard resets the system</p>
<dt><code>-w</code>, <code>&#8211;warm</code></p>
<dd> Warm resets the system</p>
<dt><code>-D</code> <i>nn</i>, <code>&#8211;domain</code>=<i>nn</i></p>
<dd> Select domain id <i>nn</i></p>
<dt><code>-X</code>, <code>&#8211;debug</code></p>
<dd> Display debug messages</p>
<dt><code>-N</code> <i>&quot;host[:port]&quot;</i>, <code>&#8211;host</code>=<i>&quot;host[:port]&quot;</i></p>
<dd> Open session to the domain served by the daemon at the specified <font SIZE="-1">URL </font>(host:port). This option overrides the <font SIZE="-1">OPENHPI_DAEMON_HOST</font> and <font SIZE="-1">OPENHPI_DAEMON_PORT</font> environment variables. If host contains &#8216;:&#8217; (for example IPv6 address) then enclose it in square brackets. For example: <i>&#8220;[::1]&#8221;</i> or <i>&#8220;[::1]:4743&#8221;</i>.</p>
<dt><code>-C</code> <i>&quot;file&quot;</i>, <code>&#8211;cfgfile</code>=<i>&quot;file&quot;</i></p>
<dd> Use passed file as client configuration file. This option overrides the OPENHPICLIENT_CONf environment variable.</dl>
<h2>SEE ALSO</h2>
<pre>
         hpi_shell
         hpialarms      hpifan         hpipower       hpitop
         hpidomain      hpigensimdata  hpisensor      hpitree
         hpiel          hpiiinv        hpisettime     hpiwdt
         hpievents      hpionIBMblade  hpithres       hpixml
         ohdomainlist   ohhandler      ohparam
</pre>
<h2>AUTHORS</h2>
<p> Authors of this man page: </p>
<pre><code>
Peter D Phan(pdphan[at] users.sourceforge.net)
    Ulrich Kleber(ulikleber[at] users.sourceforge.net)
        Anton Pak(avpak[at] users.sourceforge.net)
</code></pre>
<h2>Index</h2>
