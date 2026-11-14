---
title: "hpionibmblade(1)"
name: "hpionibmblade"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hpionibmblade/"
description: "hpionIBMblade – An openhpi sample application that shows how two (2) openhpi plugins can be used to display and manage resources of an IBM Blade with Basedboard Management Controller (BMC)."
---

<p>hpionIBMblade &#8211; An openhpi sample application that shows how two (2) openhpi plugins can be used to display and manage resources of an IBM Blade with Basedboard Management Controller (BMC). </p>
<h2>Synopsis</h2>
<pre> hpionIBMblade [-D nn] [-N host[:port]] [-C &lt;cfgfile&gt;] [ -X ] [ -h ]
 hpionIBMblade [--domain nn] [--host=host[:port]] [--cfgfile=file] [--debug] [--help]</pre>
<h2>Description</h2>
<pre> hpionIBMblade shows how two (2) openhpi plugins can be used to display 
and manage resources of an IBM Blade with Basedboard Management Controller (BMC).
 
 Both the ipmi and snmp_bc plugin have the same IBM Blade target. Resources from
both plugins are combined to show a complete view of the IBM Blade. 
 
 @@ WARNING @@ RESTRICTIONS @@ WARNING @@ RESTRICTIONS @@ WARNING @@ RESTRICTIONS @@
 
 This client application is designed to run **only** inband on an IBM Blade with Basedboard
Management Controller (BMC)</pre>
<p>If no domain or host is selected, hpionIBMblade uses the default domain as specified in the openhpiclient.conf file.</p>
<h2>Options</h2>
<h3>Help Options:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Show help options</dl>
<h3>Application Options:</h3>
<dl>
<dt><code>-D</code> <i>nn</i>, <code>&#8211;domain</code>=<i>nn</i></p>
<dd>Select domain id <i>nn</i></p>
<dt><code>-X</code>, <code>&#8211;debug</code></p>
<dd>Display debug messages</p>
<dt><code>-N</code> <i>&quot;host[:port]&quot;</i>, <code>&#8211;host</code>=<i>&quot;host[:port]&quot;</i></p>
<dd>Open session to the domain served by the daemon at the specified <font SIZE="-1">URL </font>(host:port). This option overrides the <font SIZE="-1">OPENHPI_DAEMON_HOST</font> and <font SIZE="-1">OPENHPI_DAEMON_PORT</font> environment variables. If host contains &#8216;:&#8217; (for example IPv6 address) then enclose it in square brackets. For example: <i>&#8220;[::1]&#8221;</i> or <i>&#8220;[::1]:4743&#8221;</i>.</p>
<dt><code>-C</code> <i>&quot;file&quot;</i>, <code>&#8211;cfgfile</code>=<i>&quot;file&quot;</i></p>
<dd>Use passed file as client configuration file. This option overrides the OPENHPICLIENT_CONf environment variable.</dl>
<h2>Sample Configuration File</h2>
<pre> handler libipmi {
 entity_root = &quot;{SYSTEM_CHASSIS,2}&quot;
 name = &quot;smi&quot;
 addr = 0
 }
 handler libsnmp_bc {
 host = &quot;bc.mm.ip.address&quot;
 version = &quot;3&quot;
 community = &quot;bc_community&quot;
 entity_root = &quot;{SYSTEM_CHASSIS,1}&quot;
 security_name = &quot;myid&quot;
 passphrase = &quot;mypassword&quot;
 security_level = &quot;authNoPriv&quot;
 auth_type = &quot;MD5&quot; 
 }</pre>
<h2>See Also</h2>
<pre> hpi_shell
 hpialarms hpifan hpireset hpitop
 hpidomain hpigensimdata hpisensor hpitree
 hpiel hpiiinv hpisettime hpiwdt
 hpievents hpipower hpithres hpixml
 ohdomainlist ohhandler ohparam</pre>
<h2>Authors</h2>
<p>Authors of this man page: </p>
<pre> Peter D Phan (pdphan [at] users.sourceforge.net)
 Ulrich Kleber (ulikleber [at] users.sourceforge.net)
 Anton Pak (avpak [at] users.sourceforge.net)</pre>
