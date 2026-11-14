---
title: "hpidomain(1)"
name: "hpidomain"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hpidomain/"
description: "hpidomain – A openhpi sample application that shows information about domains. It can also set the domain tag."
---

<h2 class="name">NAME</h2>
<p> hpidomain &#8211; A openhpi sample application that shows information about domains. It can also set the domain tag. </p>
<h2>SYNOPSIS</h2>
<pre><code>
hpidomain[-D id][-N host[:port]][-C&lt;cfgfile&gt;][-t tttt][-V - X - h] hpidomain[--domain = id][--host = host[:port]][--cfgfile = file]
                                                                            [--tag = tttt][--verbose][--debug][--help]
</code></pre>
<h2>DESCRIPTION</h2>
<p> hpidomain displays the domain info for the specified domain. If no domain or host is selected, ohparam uses the default domain as specified in the openhpiclient.conf file. </p>
<p> In verbose mode, it walks the <font SIZE="-1">DRT</font> and displays domaininfo for all directly related domains. Option -t allows to change the domain tag. </p>
<p> (No Option) Display domain info</p>
<h2>OPTIONS</h2>
<h3>Help Options:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show help options</dl>
<h3>Application Options:</h3>
<dl>
<dt><code>-t</code> <i>tttt</i>, <code>&#8211;tag</code>=<i>tttt</i></p>
<dd> Set domain tag to the specified string</p>
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
         hpiel          hpiinv         hpisensor      hpitree
         hpievents      hpionIBMblade  hpisettime     hpiwdt
         hpifan         hpipower       hpithres       hpixml
         ohdomainlist   ohhandler      ohparam
</pre>
<h2>AUTHORS</h2>
<p> Authors of this man page: </p>
<pre><code>
Ulrich Kleber(ulikleber[at] users.sourceforge.net)
    Anton Pak(avpak[at] users.sourceforge.net)
</code></pre>
<h2>Index</h2>
