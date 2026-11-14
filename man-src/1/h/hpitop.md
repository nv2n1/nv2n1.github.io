---
title: "hpitop(1)"
name: "hpitop"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hpitop/"
description: "hpitop – A openhpi sample application that displays highlevel topology for a managed openHPI complex."
---

<h2 class="name">NAME</h2>
<p> hpitop &#8211; A openhpi sample application that displays highlevel topology for a managed openHPI complex. </p>
<h2>SYNOPSIS</h2>
<pre><code>
hpitop[-D nn][-N host[:port]][-C&lt;cfgfile&gt;][-rscwiafd][-n nn][-X][-h] hpitop[--domain = nn][--host = host[:port]][--cfgfile = file][--rpts][--sensors]
                                                                           [--controls][--watchdogs][--inventories][--annunciators][--fumis][--dimis]
                                                                           [--resource = nn][--debug][--help]
</code></pre>
<h2>DESCRIPTION</h2>
<p> hpitop walks the Resource Present Table (<font SIZE="-1">RPT</font>) of the managed openHPI complex and displays all the resources and resources&#8217; management instruments. </p>
<p> If no domain or host is selected, hpitop uses the default domain as specified in the openhpiclient.conf file.</p>
<h2>OPTIONS</h2>
<p> (No Option) Display system topology via default domain: rpt &amp; rdr headers</p>
<h3>Help Options:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show help options</dl>
<h3>Application Options:</h3>
<dl>
<dt><code>-r</code>, <code>&#8211;rpts</code></p>
<dd> Display only rpts</p>
<dt><code>-s</code>, <code>&#8211;sensors</code></p>
<dd> Display only sensors</p>
<dt><code>-c</code>, <code>&#8211;controls</code></p>
<dd> Display only controls</p>
<dt><code>-w</code>, <code>&#8211;watchdogs</code></p>
<dd> Display only watchdogs</p>
<dt><code>-i</code>, <code>&#8211;inventories</code></p>
<dd> Display only inventories</p>
<dt><code>-a</code>, <code>&#8211;annunciators</code></p>
<dd> Display only annunciators</p>
<dt><code>-f</code>, <code>&#8211;fumis</code></p>
<dd> Display only fumis</p>
<dt><code>-d</code>, <code>&#8211;dimis</code></p>
<dd> Display only dimis</p>
<dt><code>-n</code> <i>nn</i>, <code>&#8211;resource</code>=<i>nn</i></p>
<dd> Display only resource <i>nn</i> and its topology</p>
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
         hpidomain      hpigensimdata  hpireset       hpitree
         hpiel          hpiiinv        hpisensor      hpiwdt
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
