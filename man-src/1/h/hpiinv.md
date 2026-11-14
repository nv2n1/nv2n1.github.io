---
title: "hpiinv(1)"
name: "hpiinv"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hpiinv/"
description: "hpiinv – An openhpi sample application that shows resources’ inventory records."
---

<h2 class="name">NAME</h2>
<p> hpiinv &#8211; An openhpi sample application that shows resources&#8217; inventory records. </p>
<h2>SYNOPSIS</h2>
<pre><code>
hpiinv[-D nn][-N host[:port]][-C&lt;cfgfile&gt;][-V][-X][-a tag][-h] hpiinv[--domain = nn][--host = host[:port]][--cfgfile = file][--verbose][--debug][--asset - tag = tag][--help]
</code></pre>
<h2>DESCRIPTION</h2>
<p> hpiinv walks the <font SIZE="-1">RPT </font>(Resource Present Table) looking for resources that have Inventory Capability. It displays all inventory records found. </p>
<p> If no domain is selected, hpiinv uses a session with the default domain. The selected domain id must be configured via the openhpidclient.conf file specified in the environment.</p>
<h2>OPTIONS</h2>
<h3>Help Options:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show help options</dl>
<h3>Application Options:</h3>
<dl>
<dt><code>-a</code> <i>tag</i>, <code>&#8211;asset-tag</code>=<i>tag</i></p>
<dd> Set the asset tag to the specified string</p>
<dt><code>-D</code> <i>nn</i>, <code>&#8211;domain</code>=<i>nn</i></p>
<dd> Select domain id <i>nn</i></p>
<dt><code>-X</code>, <code>&#8211;debug</code></p>
<dd> Display debug messages</p>
<dt><code>-V</code>, <code>&#8211;verbose</code></p>
<dd> Verbose mode</p>
<dt><code>-N</code> <i>&quot;host[:port]&quot;</i>, <code>&#8211;host</code>=<i>&quot;host[:port]&quot;</i></p>
<dd> Open session to the domain served by the daemon at the specified <font SIZE="-1">URL </font>(host:port). This option overrides the <font SIZE="-1">OPENHPI_DAEMON_HOST</font> and <font SIZE="-1">OPENHPI_DAEMON_PORT</font> environment variables. If host contains &#8216;:&#8217; (for example IPv6 address) then enclose it in square brackets. For example: <i>&#8220;[::1]&#8221;</i> or <i>&#8220;[::1]:4743&#8221;</i>.</p>
<dt><code>-C</code> <i>&quot;file&quot;</i>, <code>&#8211;cfgfile</code>=<i>&quot;file&quot;</i></p>
<dd> Use passed file as client configuration file. This option overrides the OPENHPICLIENT_CONf environment variable.</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> For generic OpenHPI, there is *no* additional environment variable required. For some devices; sahalee, mBMC; <font SIZE="-1">BMCONLY</font> flag needs to be set for additional device characterization based on rdr.IdString.Data.</p>
<h2>SEE ALSO</h2>
<pre>
         hpi_shell
         hpialarms      hpifan         hpireset       hpitop
         hpidomain      hpigensimdata  hpisensor      hpitree
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
