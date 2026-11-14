---
title: "ohparam(1)"
name: "ohparam"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ohparam/"
description: "ohparam – An openhpi sample application that uses the openhpi additional interface to control openhpi configuration parameters"
---

<h2 class="name">NAME</h2>
<p> ohparam &#8211; An openhpi sample application that uses the openhpi additional interface to control openhpi configuration parameters </p>
<h2>SYNOPSIS</h2>
<pre><code>
ohparam[-D nn][-N host[:port]][-C&lt;cfgfile&gt;][-X] get
    ohparam[-D nn][-N host[:port]][-C&lt;cfgfile&gt;][-X] set&lt;paramname newvalue&gt;
        ohparam[--domain nn][--host = host[:port]][--cfgfile = file][--debug] get
            ohparam[--domain nn][--host = host[:port]][--cfgfile = file][--debug] set&lt;paramname newvalue&gt;
</code></pre>
<h2>DESCRIPTION</h2>
<p> ohparam get will display all global configuration parameters of the openhpi daemon for the specified domain. </p>
<p> ohparam set will change the given global configuration parameters of the openhpi daemon for the specified domain to the new value. </p>
<p> If no domain or host is selected, ohparam uses the default domain as specified in the openhpiclient.conf file.</p>
<h2>COMMANDS</h2>
<pre>
 Command get: display info about all global parameters  
         no specific arguments                         
 Command set:                                           
         one of the daemon's global parameters:        
         (without the OPENHPI prefix)                  
           LOG_ON_SEV, EVT_QUEUE_LIMIT,         
           DEL_SIZE_LIMIT, DEL_SAVE                    
           DAT_SIZE_LIMIT, DAT_USER_LIMIT, DAT_SAVE    
           PATH, VARPATH, CONF                         
         and the desired new value. Example:           
           ohparam set DEL_SIZE_LIMIT 20000
</pre>
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
         ohdomainlist   ohhandler
</pre>
<h2>AUTHORS</h2>
<p> Authors of this man page: </p>
<pre><code>
Ulrich Kleber(ulikleber[at] users.sourceforge.net)
    Anton Pak(avpak[at] users.sourceforge.net)
</code></pre>
<h2>Index</h2>
