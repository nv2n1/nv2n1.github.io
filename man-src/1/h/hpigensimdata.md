---
title: "hpigensimdata(1)"
name: "hpigensimdata"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hpigensimdata/"
description: "hpigensimdata – A openhpi client application supplementing the dynamic simulator plugin."
---

<h2 class="name">NAME</h2>
<p> hpigensimdata &#8211; A openhpi client application supplementing the dynamic simulator plugin. </p>
<h2>SYNOPSIS</h2>
<pre><code>
hpigensimdata[-D nn][-N host[:port]][-C&lt;cfgfile&gt;][-r res_id][-f filename][-m UPD | INIT][-h] hpigensimdata[--domain = nn][--host = host[:port]][--cfgfile = file]
                                                                                                          [--resource = res_id][--file = filename][--mode = UPD | INIT][--help]
</code></pre>
<h2>DESCRIPTION</h2>
<p> hpigensimdata generates data for the dynamic simulator plugin by reading the current configuration. It will print all <font SIZE="-1">HPI</font> information in a format that can be parsed by Dynamic Simulator plugin. To spare some encoding/decoding function, values of enums are printed as int values instead of encode them to <font SIZE="-1">ASCII</font> values and decode them afterwards. Since this client is primarily for the Dynamic Simulator, the output functions don&#8217;t depend on the oh_.. &#8211; output function. Therefore they can be easily changed without influence on other clients. </p>
<p> Please refer to <font SIZE="-1">README</font> and detailed documentation with the plugin. </p>
<p> If no domain or host is selected, ohparam uses the default domain as specified in the openhpiclient.conf file. </p>
<p> If no file name is specified, the data is displayed on console.</p>
<h2>OPTIONS</h2>
<h3>Help Options:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show help options</dl>
<h3>Application Options:</h3>
<dl>
<dt><code>-r</code> <i>res_id</i>, <code>&#8211;resource</code>=<i>res_id</i></p>
<dd> Select particular resource id for an update file</p>
<dt><code>-f</code> <i>filename</i>, <code>&#8211;file</code>=<i>filename</i></p>
<dd> Name of the file to be generated</p>
<dt><code>-m</code> <i>UPD|INIT</i>, <code>&#8211;mode</code>=<i>UPD|INIT</i></p>
<dd> Write update or initial file</p>
<dt><code>-D</code> <i>nn</i>, <code>&#8211;domain</code>=<i>nn</i></p>
<dd> Select domain id <i>nn</i></p>
<dt><code>-N</code> <i>&quot;host[:port]&quot;</i>, <code>&#8211;host</code>=<i>&quot;host[:port]&quot;</i></p>
<dd> Open session to the domain served by the daemon at the specified <font SIZE="-1">URL </font>(host:port). This option overrides the <font SIZE="-1">OPENHPI_DAEMON_HOST</font> and <font SIZE="-1">OPENHPI_DAEMON_PORT</font> environment variables. If host contains &#8216;:&#8217; (for example IPv6 address) then enclose it in square brackets. For example: <i>&#8220;[::1]&#8221;</i> or <i>&#8220;[::1]:4743&#8221;</i>.</p>
<dt><code>-C</code> <i>&quot;file&quot;</i>, <code>&#8211;cfgfile</code>=<i>&quot;file&quot;</i></p>
<dd> Use passed file as client configuration file. This option overrides the OPENHPICLIENT_CONf environment variable.</dl>
<h2>SEE ALSO</h2>
<pre>
         hpi_shell
         hpialarms      hpifan         hpireset       hpitop
         hpidomain      hpiinv         hpisensor      hpitree
         hpiel          hpionIBMblade  hpisettime     hpiwdt
         hpievents      hpipower       hpithres       hpixml
         ohdomainlist   ohhandler      ohparam
</pre>
<h2>AUTHORS</h2>
<p> Authors of this man page: </p>
<pre><code>
Ulrich Kleber(ulikleber[at] users.sourceforge.net)
    Lars Wetzel(larswetzel[at] users.sourceforge.net)
        Anton Pak(avpak[at] users.sourceforge.net)
</code></pre>
<h2>Index</h2>
