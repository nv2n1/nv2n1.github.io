---
title: "hpiwdt(1)"
name: "hpiwdt"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hpiwdt/"
description: "hpiwdt – This sample openhpi application reads and enables the watchdog timer."
---

<h2 class="name">NAME</h2>
<p> hpiwdt &#8211; This sample openhpi application reads and enables the watchdog timer. </p>
<h2>SYNOPSIS</h2>
<pre><code>
hpiwdt[-D nn][-N host[:port]][-C&lt;cfgfile&gt;][-t sec][-X][-h] hpiwdt[--domain = nn][--host = host[:port]][--cfgfile = file]
                                                                 [--disable][--enable][--reset][--timeout n][--debug][--help]
</code></pre>
<h2>DESCRIPTION</h2>
<p> hpiwdt reads and enables the watchdog timer. </p>
<p> If no domain or host is selected, hpiwdt uses the default domain as specified in the openhpiclient.conf file.</p>
<h2>OPTIONS</h2>
<h3>Help Options:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show help options</dl>
<h3>Application Options:</h3>
<dl>
<dt><code>-e</code>, <code>&#8211;enable</code></p>
<dd> Enables the watchdog timer</p>
<dt><code>-d</code>, <code>&#8211;disable</code></p>
<dd> Disables the watchdog timer</p>
<dt><code>-r</code>, <code>&#8211;reset</code></p>
<dd> Resets the watchdog timer</p>
<dt><code>-t</code> <i>sec</i>, <code>&#8211;timeout</code>=<i>sec</i></p>
<dd> Sets timeout to <i>sec</i> seconds</p>
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
         hpialarms      hpifan         hpipower       hpithres
         hpidomain      hpigensimdata  hpireset       hpitop
         hpiel          hpiiinv        hpisensor      hpitree
         hpievents      hpionIBMblade  hpisettime     hpixml
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
