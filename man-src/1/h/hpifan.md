---
title: "hpifan(1)"
name: "hpifan"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hpifan/"
description: "hpifan – An openhpi sample application that shows \"Fan Control\" management instruments"
---

<h2 class="name">NAME</h2>
<p> hpifan &#8211; An openhpi sample application that shows &quot;Fan Control&quot; management instruments </p>
<h2>SYNOPSIS</h2>
<pre><code>
hpifan[-D nn][-N host[:port]][-C&lt;cfgfile&gt;][-h][-s auto | nn][-X] hpifan[--domain = nn][--host = host[:port]][--cfgfile = file][--help][--speed = auto | nn][--debug]
</code></pre>
<h2>DESCRIPTION</h2>
<p> hpifan walks the <font SIZE="-1">RPT </font>(Resource Present Table) for resouces that have &#8220;Fan Control&#8221; management instruments (<font SIZE="-1">SAHPI_CTRL_FAN_SPEED</font>). </p>
<p> If no domain or host is selected, hpifan uses the default domain as specified in the openhpiclient.conf file.</p>
<h2>OPTIONS</h2>
<h3>Help Options:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show help options</dl>
<h3>Application Options:</h3>
<dl>
<dt><code>-s</code>, <code>&#8211;speed</code>=<i>auto|nn</i></p>
<dd> Set fan speed for <font SIZE="-1">ALL</font> fans in domain speed is a number or &#8220;auto&#8221; for setting fan in auto mode</p>
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
         hpialarms      hpigensimdata  hpireset       hpitop
         hpidomain      hpiinv         hpisensor      hpitree
         hpiel          hpionIBMblade  hpisettime     hpiwdt
         hpievents      hpipower       hpithres       hpixml
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
