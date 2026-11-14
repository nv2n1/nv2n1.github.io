---
title: "ohdomainlist(1)"
name: "ohdomainlist"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ohdomainlist/"
description: "ohdomainlist – A openhpi sample application that shows information about domains on the level of the openhpi base library."
---

<h2 class="name">NAME</h2>
<p> ohdomainlist &#8211; A openhpi sample application that shows information about domains on the level of the openhpi base library. </p>
<h2>SYNOPSIS</h2>
<pre><code>
hpidomain[-h - V - X] hpidomain[--help][--verbose][--debug]
</code></pre>
<h2>DESCRIPTION</h2>
<p> ohdomainlist displays the list of domains known to the openhpi base library. In verbose mode, it displays more information about those domains. Clients can only access domains known to the library. </p>
<p> Please note that ohdomainlist can only display the domains defined in the openhpiclient.conf file as specified in the <font SIZE="-1">OPENHPICLIEN_CONF</font> environment variable. Dynamic changes of the domain list done using the oHpiDomainAdd and oHpiDomainAddById <font SIZE="-1">API</font> are valid only for the life-time of the client library. </p>
<p> If no domain or host is selected, ohdomainlist lists the domains as specified in the openhpiclient.conf file.</p>
<h2>OPTIONS</h2>
<h3>Help Options:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show help options</dl>
<h3>Application Options:</h3>
<dl>
<dt><code>-D</code>, <code>&#8211;domain</code>=<i>nn</i></p>
<dd> Select domain id nn</p>
<dt><code>-X</code>, <code>&#8211;debug</code></p>
<dd> Display debug messages</p>
<dt><code>-V</code>, <code>&#8211;verbose</code></p>
<dd> Verbose mode</p>
<dt><code>-N</code>, <code>&#8211;host</code>=<i>&quot;host[:port]&quot;</i></p>
<dd> Open session to the domain served by the daemon at the specified <font SIZE="-1">URL </font>(host:port). This option overrides the <font SIZE="-1">OPENHPI_DAEMON_HOST</font> and <font SIZE="-1">OPENHPI_DAEMON_PORT</font> environment variables.</p>
<dt><code>-C</code>, <code>&#8211;cfgfile</code>=<i>&quot;file&quot;</i></p>
<dd> Use passed file as client configuration file. This option overrides the OPENHPICLIENT_CONf environment variable.</dl>
<h2>SEE ALSO</h2>
<pre>
         hpi_shell
         hpialarms      hpifan         hpipower       hpithres
         hpidomain      hpigensimdata  hpireset       hpitop
         hpiel          hpiiinv        hpisensor      hpitree
         hpievents      hpionIBMblade  hpisettime     hpiwdt
         hpixml
         ohhandler      ohparam
</pre>
<h2>AUTHORS</h2>
<p> Authors of this man page: </p>
<pre><code>
Ulrich Kleber(ulikleber[at] users.sourceforge.net)
    Anton Pak(avpak[at] users.sourceforge.net)
</code></pre>
<h2>Index</h2>
