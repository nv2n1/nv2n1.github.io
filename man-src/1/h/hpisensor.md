---
title: "hpisensor(1)"
name: "hpisensor"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hpisensor/"
description: "hpisensor - This sample openhpi application displays sensor info for all resources with Sensor Capability SYNOPSIS hpisensor[-D nn][-N host[:port]][-C<cfgfile>][-t - r - s - X - h][-E epath] hpisen..."
---

<h2 class="name">NAME</h2>
<pre>
 hpisensor -  This sample openhpi application displays sensor info for all resources with Sensor Capability
</pre>
<h2>SYNOPSIS</h2>
<pre><code>
hpisensor[-D nn][-N host[:port]][-C&lt;cfgfile&gt;][-t - r - s - X - h][-E epath] hpisensor[--domain = nn][--host = host[:port]][--cfgfile = file]
                                                                                     [--threshold-- range-- eventstate-- debug-- help][--entity - path = "epath"]
</code></pre>
<h2>DESCRIPTION</h2>
<p> hpisensor displays sensor info for all resources with Sensor Capability. Option -E (entity-path) restricts the output on the specified entity-path. </p>
<p> If no domain or host is selected, hpisensor uses the default domain as specified in the openhpiclient.conf file.</p>
<h2>OPTIONS</h2>
<h3>Help Options:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show help options</dl>
<h3>Application Options:</h3>
<dl>
<dt><code>-t</code>, <code>&#8211;threshold</code></p>
<dd> Show Thresholds also</p>
<dt><code>-r</code>, <code>&#8211;range</code></p>
<dd> Show Range values also</p>
<dt><code>-s</code>, <code>&#8211;eventstate</code></p>
<dd> Show EventState also</p>
<dt><code>-E</code> <i>&quot;epath&quot;</i>, <code>&#8211;entity-path</code>=<i>&quot;epath&quot;</i></p>
<dd> Use entity path <i>epath</i></p>
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
         hpidomain      hpigensimdata  hpireset       hpitree
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
