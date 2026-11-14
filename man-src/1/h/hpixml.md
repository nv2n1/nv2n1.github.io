---
title: "hpixml(1)"
name: "hpixml"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hpixml/"
description: "hpxml – An openhpi sample application that displays system view in XML."
---

<h2 class="name">NAME</h2>
<p> hpxml &#8211; An openhpi sample application that displays system view in XML. </p>
<h2>SYNOPSIS</h2>
<pre><code>
hpixml[-D nn][-s][-i - t][-N host[:port]][-C = file][-h] hpixml[--domain = nn][--xsd][--indent-- text][--host = host[:port]][--cfgfile = file][--help]
</code></pre>
<h2>DESCRIPTION</h2>
<p> hpixml displays system view in <font SIZE="-1">XML.</font> </p>
<p> If no domain or host is selected, hpixml uses the default domain as specified in the openhpiclient.conf file.</p>
<h2>OPTIONS</h2>
<h3>Help Options:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show help options</dl>
<h3>Application Options:</h3>
<dl>
<dt><code>-i</code>, <code>&#8211;indent</code></p>
<dd> Use indentation</p>
<dt><code>-t</code>, <code>&#8211;text</code></p>
<dd> Use enum and flag text names instead of raw values</p>
<dt><code>-s</code>, <code>&#8211;xsd</code></p>
<dd> Show <font SIZE="-1">XML</font> schema</p>
<dt><code>-D</code> <i>nn</i>, <code>&#8211;domain</code>=<i>nn</i></p>
<dd> Select domain id <i>nn</i></p>
<dt><code>-N</code> <i>&quot;host[:port]&quot;</i>, <code>&#8211;host</code>=<i>&quot;host[:port]&quot;</i></p>
<dd> Open session to the domain served by the daemon at the specified <font SIZE="-1">URL </font>(host:port). This option overrides the <font SIZE="-1">OPENHPI_DAEMON_HOST</font> and <font SIZE="-1">OPENHPI_DAEMON_PORT</font> environment variables. If host contains &#8216;:&#8217; (for example IPv6 address) then enclose it in square brackets. For example: <i>&#8220;[::1]&#8221;</i> or <i>&#8220;[::1]:4743&#8221;</i>.</p>
<dt><code>-C</code> <i>&quot;file&quot;</i>, <code>&#8211;cfgfile</code>=<i>&quot;file&quot;</i></p>
<dd> Use passed file as client configuration file. This option overrides the OPENHPICLIENT_CONf environment variable.</dl>
<h2>SEE ALSO</h2>
<pre>
         hpi_shell
         hpialarms      hpigensimdata  hpireset       hpitop
         hpidomain      hpiinv         hpisensor      hpitree
         hpievents      hpionIBMblade  hpisettime     hpiwdt
         hpifan         hpipower       hpithres
         ohdomainlist   ohhandler      ohparam
</pre>
<h2>AUTHORS</h2>
<p> Authors of this man page: </p>
<pre><code>
Anton Pak(anton.pak[at] pigeonpoint.com)
    Ulrich Kleber(ulikleber[at] users.sourceforge.net)
</code></pre>
<h2>Index</h2>
