---
title: "hpi_shell(1)"
name: "hpi_shell"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hpi_shell/"
description: "hpi_shell – An openhpi sample application that allows a user to interactively perform a number of HPI operations."
---

<h2 class="name">NAME</h2>
<p> hpi_shell &#8211; An openhpi sample application that allows a user to interactively perform a number of HPI operations. </p>
<h2>SYNOPSIS</h2>
<pre><code>
hpi_shell[-D nn][-N host[:port]][-C&lt;cfgfile&gt;][-e][-f&lt;file&gt;][-X][-h] hpi_shell[--domain = nn][--host = host[:port]][--cfgfile = file][--events][--cmdfile = filename][--debug][--help]
</code></pre>
<h2>DESCRIPTION</h2>
<p> hpi_shell reads commands and performs <font SIZE="-1">HPI</font> operations based on those commands. This allows it to exercise HPI-managed hardware and do manual operations on that hardware. </p>
<p> Once in hpi_shell, use the &#8220;help&#8221; command for a list of commands, or &#8220;help command&#8221; for details on a particular command. </p>
<p> If no domain or host is selected, ohparam uses the default domain as specified in the openhpiclient.conf file.</p>
<h2>OPTIONS</h2>
<h3>Help Options:</h3>
<pre>
  -h, --help                   Show help options
</pre>
<h3>Application Options:</h3>
<dl>
<dt><code>-f</code> <i>filename</i>, <code>&#8211;cmdfile</code>=<i>filename</i></p>
<dd> Execute command file</p>
<dt><code>-e</code>, <code>&#8211;events</code></p>
<dd> Show short events, discover after subscribe</p>
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
  hpialarms      hpifan         hpipower       hpithres       
  hpidomain      hpigensimdata  hpireset       hpitop         
  hpiel          hpiinv         hpisensor      hpitree        
  hpievents      hpionIBMblade  hpisettime     hpiwdt
  hpixml
  ohdomainlist   ohhandler      ohparam
</pre>
<h2>AUTHORS</h2>
<p> Author(s) of this man page: </p>
<pre><code>
Bryan Sutula(sutula[at] users.sourceforge.net)
    Ulrich Kleber(ulikleber[at] users.sourceforge.net)
        Anton Pak(avpak[at] users.sourceforge.net)
</code></pre>
<h2>Index</h2>
