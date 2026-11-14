---
title: "ohhandler(1)"
name: "ohhandler"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ohhandler/"
description: "ohhandler – An openhpi sample application that uses the openhpi additional interfaces to control openhpi configuration. That is plugins can be loaded, plugin instances (handlers) created, unloaded ..."
---

<h2 class="name">NAME</h2>
<p> ohhandler &#8211; An openhpi sample application that uses the openhpi additional interfaces to control openhpi configuration. That is plugins can be loaded, plugin instances (handlers) created, unloaded or their configuration displayed. </p>
<h2>SYNOPSIS</h2>
<pre><code>
ohhandler[-D nn][-N host[:port]][-C&lt;cfgfile&gt;][-X] command&lt;specific arguments&gt;
    ohhandler[--domain nn][--host = host[:port]][--cfgfile = file][--debug] command&lt;specific arguments&gt;
        ohhandler[-D nn][-X] list
            ohhandler[-D nn][-X] info&lt;handler - id&gt;
                ohhandler[-D nn][-X] destroy&lt;handler - id&gt;
                    ohhandler[-D nn][-X] getnext&lt;handler - id&gt;
                        ohhandler[-D nn][-X] find&lt;resource - id&gt;
                            ohhandler[-D nn][-X] retry&lt;handler - id&gt;
                                ohhandler[-D nn][-X] create plugin&lt;plugin - name&gt;&lt;configuration - parameters&gt;
</code></pre>
<h2>DESCRIPTION</h2>
<p> ohhandler list will display a list of all plugin instances (handlers) currently defined in the openhpi daemon for the specified domain. Part of the output is the handler-id that can be used in subsequent commands. </p>
<p> ohhandler info will display specific info for the handler with the specified id. This information includes all configuration parameters of the handler as specified in the openhpi.conf file or as dynamically defined during a &#8220;ohhandler create&#8221; call. </p>
<p> ohhandler destroy will unload the specified handler and delete all its configuration information. </p>
<p> ohhandler getnext will allows to walk through all hanlers currently defined in the openhpi daemon for the specified domain. </p>
<p> ohhandler find will find the handler that is managing the specified resource. </p>
<p> ohhandler retry allows to try again to load and initialize the specified handler. </p>
<p> ohhandler create allows to dynamically create a new handler with configuration parameters like they are specified in the openhpi.conf file.<br />
&nbsp;<wbr>&#8211; The type of plugin is specified with the keyword plugin<br />
&nbsp;<wbr>&#8211; Configuration parameters should follow as name value pairs<br />
&nbsp;<wbr>&#8211; Complex strings like entity paths must be enclosed with&nbsp;<wbr>&quot;&#8220;<br />
&nbsp;<wbr>Example:<br />
&nbsp;<wbr>ohhandler create plugin libsimulator entity_root&nbsp;<wbr>&#8221;{<font SIZE="-1">SYSTEM_CHASSIS,1</font>}&quot;&nbsp;<wbr>name sim </p>
<p> If no domain or host is selected, ohhandler uses the default domain as specified in the openhpiclient.conf file.</p>
<h2>OPTIONS</h2>
<h3>Help Options:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show help options</dl>
<h3>Application Options:</h3>
<dl>
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
         hpievents      hpionIBMblade  hpisettime     hpiwdt
         hpixml
         ohdomainlist   ohparam
</pre>
<h2>AUTHORS</h2>
<p> Authors of this man page: </p>
<pre><code>
Ulrich Kleber(ulikleber[at] users.sourceforge.net)
    Anton Pak(avpak[at] users.sourceforge.net)
</code></pre>
<h2>Index</h2>
