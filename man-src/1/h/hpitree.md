---
title: "hpitree(1)"
name: "hpitree"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hpitree/"
description: "hpitree – A openhpi sample application that shows in details the resources (rpt’s) and resources’ manamegement instruments (rdr’s) data structures of the managed openHPI complex."
---

<h2 class="name">NAME</h2>
<p> hpitree &#8211; A openhpi sample application that shows in details the resources (rpt&#8217;s) and resources&#8217; manamegement instruments (rdr&#8217;s) data structures of the managed openHPI complex. </p>
<h2>SYNOPSIS</h2>
<pre><code>
hpitree[-D nn][-N host[:port]][-C&lt;cfgfile&gt;][-acdiorsw][-n nn][-X][-h] hpitree[--domain = nn][--host = host[:port]][--cfgfile = file][--all][--controls][--rdrs][--inventories][--rpts]
                                                                             [--sensors][--watchdogs][--overview][--resource = nn][--debug][--help]
</code></pre>
<h2>DESCRIPTION</h2>
<p> hpitree walks the Resource Presence Table (<font SIZE="-1">RPT</font>) of the managed openHPI complex, and displays in details the resources (rpt&#8217;s) and resources&#8217; management instruments (rdr&#8217;s) data structures. </p>
<p> If no domain or host is selected, hpitree uses the default domain as specified in the openhpiclient.conf file.</p>
<h2>OPTIONS</h2>
<p> (No Option) Display all rpts and rdrs</p>
<h3>Help Options:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Show help options</dd></dl>
<h3>Application Options:</h3>
<dl>
<dt><code>-a</code>, <code>&#8211;all</code></dt>
<dd> Display all rpts and rdrs (default)</dd>
<dt><code>-r</code>, <code>&#8211;rpts</code></dt>
<dd> Display only rpts</dd>
<dt><code>-d</code>, <code>&#8211;rdrs</code></dt>
<dd> Display rdr records</dd>
<dt><code>-o</code>, <code>&#8211;overview</code></dt>
<dd> Display system overview: rpt &amp; rdr headers</dd>
<dt><code>-s</code>, <code>&#8211;sensors</code></dt>
<dd> Display only sensors</dd>
<dt><code>-c</code>, <code>&#8211;controls</code></dt>
<dd> Display only controls</dd>
<dt><code>-w</code>, <code>&#8211;watchdogs</code></dt>
<dd> Display only watchdogs</dd>
<dt><code>-i</code>, <code>&#8211;inventories</code></dt>
<dd> Display only inventories</dd>
<dt><code>-n</code> <i>nn</i>, <code>&#8211;resource</code>=<i>nn</i></dt>
<dd> Display only resource <i>nn</i> and its topology</dd>
<dt><code>-D</code> <i>nn</i>, <code>&#8211;domain</code>=<i>nn</i></dt>
<dd> Select domain id <i>nn</i></dd>
<dt><code>-X</code>, <code>&#8211;debug</code></dt>
<dd> Display debug messages</dd>
<dt><code>-N</code> <i>&quot;host[:port]&quot;</i>, <code>&#8211;host</code>=<i>&quot;host[:port]&quot;</i></dt>
<dd> Open session to the domain served by the daemon at the specified <font SIZE="-1">URL </font>(host:port). This option overrides the <font SIZE="-1">OPENHPI_DAEMON_HOST</font> and <font SIZE="-1">OPENHPI_DAEMON_PORT</font> environment variables. If host contains &#8216;:&#8217; (for example IPv6 address) then enclose it in square brackets. For example: <i>&#8220;[::1]&#8221;</i> or <i>&#8220;[::1]:4743&#8221;</i>.</dd>
<dt><code>-C</code> <i>&quot;file&quot;</i>, <code>&#8211;cfgfile</code>=<i>&quot;file&quot;</i></dt>
<dd> Use passed file as client configuration file. This option overrides the OPENHPICLIENT_CONf environment variable.</dd></dl>
<h2>SEE ALSO</h2>
<pre>
         hpi_shell
         hpialarms      hpifan         hpipower       hpithres
         hpidomain      hpigensimdata  hpireset       hpitop
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
