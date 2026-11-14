---
title: "hpisettime(1)"
name: "hpisettime"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hpisettime/"
description: "hpisettime – This sample openhpi application excercises Event Log clock APIs."
---

<h2 class="name">NAME</h2>
<p> hpisettime &#8211; This sample openhpi application excercises Event Log clock APIs. </p>
<h2>SYNOPSIS</h2>
<pre><code>
hpisettime[-D nn][-N host[:port]][-C&lt;cfgfile&gt;] - d mm / dd / yyyy - t HH : MM : SS[-X][-h] hpisettime[--domain = nn][--host = host[:port]][--cfgfile = file]-- date = mm / dd / yyyy-- time = HH : MM : SS[--debug][--help]
</code></pre>
<h2>DESCRIPTION</h2>
<p> hpisettime sets new date and time for the Event Log clock. </p>
<p> If no domain is selected, hpisettime uses a session with the default domain. The selected domain id must be configured via the openhpidclient.conf file specified in the environment.</p>
<h2>OPTIONS</h2>
<h3>Help Options:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show help options</dl>
<h3>Application Options:</h3>
<dl>
<dt><code>-d</code> <i>mm/dd/yyyy</i>, <code>&#8211;date</code>=<i>mm/dd/yyyy</i></p>
<dd> New date</p>
<dt><code>-t</code> <i>24:12:60</i>, <code>&#8211;time</code>=<i>24:12:60</i></p>
<dd> New time of day in 24-hr format</p>
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
         hpiel          hpiiinv        hpisensor      hpiwdt
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
