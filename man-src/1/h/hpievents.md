---
title: "hpievents(1)"
name: "hpievents"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hpievents/"
description: "hpievents – An openhpi sample application that polls for events."
---

<h2 class="name">NAME</h2>
<p> hpievents &#8211; An openhpi sample application that polls for events. </p>
<h2>SYNOPSIS</h2>
<pre><code>
hpievents[-D&lt;value&gt;][-N host[:port]][-C&lt;cfgfile&gt;][-t BLOCK | SAHPI_TIMEOUT_BLOCK | n][-d - X - h] hpievents[--domain = nn][--host = host[:port]][--cfgfile = file]
                                                                                                           [--timeout = BLOCK | SAHPI_TIMEOUT_BLOCK | n][--discover][--debug][--help]
</code></pre>
<h2>DESCRIPTION</h2>
<p> hpievents polls for events in an opened <font SIZE="-1">HPI</font> session. User can specify wait time for the event. User can also select the order between hpi resource (resource event) discovery and hpi event subscription. </p>
<p> If no domain or host is selected, hpievents polls for events in the default domain as specified in the openhpiclient.conf file.</p>
<h2>OPTIONS</h2>
<h3>Help Options:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show help options</dl>
<h3>Application Options:</h3>
<dl>
<dt><code>-t</code> <i>n|BLOCK</i>, <code>&#8211;timeout</code>=<i>n|BLOCK</i></p>
<dd> Wait <i>n</i> seconds for event or infinite wait (<i></i><font SIZE="-1"><i>BLOCK</i></font><i></i>)</p>
<dt><code>-d</code>, <code>&#8211;discover</code></p>
<dd> Call <i>saHpiDiscover()</i> after <i>saHpiSubscribe()</i></p>
<dt><code>-D</code> <i>nn</i>, <code>&#8211;domain</code>=<i>nn</i></p>
<dd> Select domain id <i>nn</i></p>
<dt><code>-X</code>, <code>&#8211;debug</code></p>
<dd> Display debug messages</p>
<dt><code>-N</code> <i>&quot;host[:port]&quot;</i>, <code>&#8211;host</code>=<i>&quot;host[:port]&quot;</i></p>
<dd> Open session to the domain served by the daemon at the specified <font SIZE="-1">URL </font>(host:port). This option overrides the <font SIZE="-1">OPENHPI_DAEMON_HOST</font> and <font SIZE="-1">OPENHPI_DAEMON_PORT</font> environment variables. If host contains &#8216;:&#8217; (for example IPv6 address) then enclose it in square brackets. For example: <i>&#8220;[::1]&#8221;</i> or <i>&#8220;[::1]:4743&#8221;</i>.</p>
<dt><code>-C</code> <i>&quot;file&quot;</i>, <code>&#8211;cfgfile</code>=<i>&quot;file&quot;</i></p>
<dd> Use passed file as client configuration file. This option overrides the OPENHPICLIENT_CONf environment variable.</dl>
<h2>HPI APIs uniquely used in this application</h2>
<dl>
<dt>
<dd> SaErrorT <font SIZE="-1">SAHPI_API</font> saHpiSubscribe (<br />
&nbsp;<wbr><font SIZE="-1">SAHPI_IN</font>&nbsp;<wbr>SaHpiSessionIdT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>SessionId ); </p>
<p> SaErrorT <font SIZE="-1">SAHPI_API</font> saHpiUnsubscribe (<br />
&nbsp;<wbr><font SIZE="-1">SAHPI_IN</font>&nbsp;<wbr>SaHpiSessionIdT&nbsp;<wbr>&nbsp;<wbr>SessionId ); </p>
<p> SaErrorT <font SIZE="-1">SAHPI_API</font> saHpiEventGet (<br />
&nbsp;<wbr><font SIZE="-1">SAHPI_IN</font>&nbsp;<wbr>SaHpiSessionIdT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>SessionId,<br />
&nbsp;<wbr><font SIZE="-1">SAHPI_IN</font>&nbsp;<wbr>SaHpiTimeoutT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Timeout,<br />
&nbsp;<wbr><font SIZE="-1">SAHPI_OUT</font>&nbsp;<wbr>SaHpiEventT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>*Event,<br />
&nbsp;<wbr><font SIZE="-1">SAHPI_INOUT</font>&nbsp;<wbr>SaHpiRdrT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>*Rdr,<br />
&nbsp;<wbr><font SIZE="-1">SAHPI_INOUT</font>&nbsp;<wbr>SaHpiRptEntryT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>*RptEntry,<br />
&nbsp;<wbr><font SIZE="-1">SAHPI_INOUT</font>&nbsp;<wbr>SaHpiEvtQueueStatusT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>*EventQueueStatus );</dl>
<h2>SEE ALSO</h2>
<pre>
         hpi_shell
         hpialarms      hpigensimdata  hpireset       hpitop
         hpidomain      hpiinv         hpisensor      hpitree
         hpiel          hpionIBMblade  hpisettime     hpiwdt
         hpifan         hpipower       hpithres       hpixml
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
