---
title: "hpiel(1)"
name: "hpiel"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hpiel/"
description: "hpiel – An openhpi sample application that displays HPI event log entries."
---

<h2 class="name">NAME</h2>
<p> hpiel &#8211; An openhpi sample application that displays HPI event log entries. </p>
<h2>SYNOPSIS</h2>
<pre><code>
hpiel[-D nn][-N host[:port]][-C&lt;cfgfile&gt;][-d][-E entity - path][-c - p - r - X - h] hpiel[--domain = nn][--host = host[:port]][--cfgfile = file]
                                                                                         [--del][--entity - path = "entitypath"][--clear-- resource-- rdr-- debug-- help]
</code></pre>
<h2>DESCRIPTION</h2>
<p> hpiel searches the <font SIZE="-1">RPT </font>(Resource Present Table) for resources with <font SIZE="-1">SAHPI_CAPABILITY_EVENT_LOG</font> and displays event log entries for resources found. </p>
<p> If no domain is selected, hpiel uses a session with the default domain. The selected domain id must be configured via the openhpidclient.conf file specified in the environment.</p>
<h2>OPTIONS</h2>
<h3>Help Options:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show help options</dl>
<h3>Application Options:</h3>
<dl>
<dt><code>-d</code>, <code>&#8211;del</code></p>
<dd> Display domain event log entries</p>
<dt><code>-c</code>, <code>&#8211;clear</code></p>
<dd> Clear log before reading event log entries</p>
<dt><code>-p</code>, <code>&#8211;resource</code></p>
<dd> Pull resource info along with log entry</p>
<dt><code>-r</code>, <code>&#8211;rdr</code></p>
<dd> Pull <font SIZE="-1">RDR</font> info along with log entry</p>
<dt><code>-E</code> <i>&quot;epath&quot;</i>, <code>&#8211;entity-path</code>=<i>&quot;epath&quot;</i></p>
<dd> Use entity path epath and display resource</p>
<dt><code>-D</code> <i>nn</i>, <code>&#8211;domain</code>=<i>nn</i></p>
<dd> Select domain id <i>nn</i></p>
<dt><code>-X</code>, <code>&#8211;debug</code></p>
<dd> Display debug messages</p>
<dt><code>-N</code> <i>&quot;host[:port]&quot;</i>, <code>&#8211;host</code>=<i>&quot;host[:port]&quot;</i></p>
<dd> Open session to the domain served by the daemon at the specified <font SIZE="-1">URL </font>(host:port). This option overrides the <font SIZE="-1">OPENHPI_DAEMON_HOST</font> and <font SIZE="-1">OPENHPI_DAEMON_PORT</font> environment variables. If host contains &#8216;:&#8217; (for example IPv6 address) then enclose it in square brackets. For example: <i>&#8220;[::1]&#8221;</i> or <i>&#8220;[::1]:4743&#8221;</i>.</p>
<dt><code>-C</code> <i>&quot;file&quot;</i>, <code>&#8211;cfgfile</code>=<i>&quot;file&quot;</i></p>
<dd> Use passed file as client configuration file. This option overrides the OPENHPICLIENT_CONf environment variable.</dl>
<p> If neither <code>-d</code> or <code>-E</code> <i>&#8220;epath&#8221;</i> are specified, event log entries will be shown for all supporting resources by default.</p>
<h2>HPI APIs uniquely used in this application</h2>
<dl>
<dt>
<dd> SaErrorT <font SIZE="-1">SAHPI_API</font> saHpiEventLogInfoGet (<br />
&nbsp;<wbr><font SIZE="-1">SAHPI_IN&nbsp;<wbr></font>&nbsp;<wbr>SaHpiSessionIdT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>SessionId,<br />
&nbsp;<wbr><font SIZE="-1">SAHPI_IN&nbsp;<wbr></font>&nbsp;<wbr>SaHpiResourceIdT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ResourceId,<br />
&nbsp;<wbr><font SIZE="-1">SAHPI_OUT</font>&nbsp;<wbr>SaHpiEventLogInfoT&nbsp;<wbr>&nbsp;<wbr>*Info ); </p>
<p> SaErrorT <font SIZE="-1">SAHPI_API</font> saHpiEventLogEntryGet (<br />
&nbsp;<wbr><font SIZE="-1">SAHPI_IN&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></font>&nbsp;<wbr>SaHpiSessionIdT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>SessionId,<br />
&nbsp;<wbr><font SIZE="-1">SAHPI_IN&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></font>&nbsp;<wbr>SaHpiResourceIdT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ResourceId,<br />
&nbsp;<wbr><font SIZE="-1">SAHPI_IN&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></font>&nbsp;<wbr>SaHpiEventLogEntryIdT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>EntryId,<br />
&nbsp;<wbr><font SIZE="-1">SAHPI_OUT&nbsp;<wbr>&nbsp;<wbr></font>&nbsp;<wbr>SaHpiEventLogEntryIdT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>*PrevEntryId,<br />
&nbsp;<wbr><font SIZE="-1">SAHPI_OUT&nbsp;<wbr>&nbsp;<wbr></font>&nbsp;<wbr>SaHpiEventLogEntryIdT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>*NextEntryId,<br />
&nbsp;<wbr><font SIZE="-1">SAHPI_OUT&nbsp;<wbr>&nbsp;<wbr></font>&nbsp;<wbr>SaHpiEventLogEntryT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>*EventLogEntry,<br />
&nbsp;<wbr><font SIZE="-1">SAHPI_INOUT</font>&nbsp;<wbr>SaHpiRdrT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>*Rdr,<br />
&nbsp;<wbr><font SIZE="-1">SAHPI_INOUT</font>&nbsp;<wbr>SaHpiRptEntryT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>*RptEntry ); </p>
<p> SaErrorT <font SIZE="-1">SAHPI_API</font> saHpiEventLogClear (<br />
&nbsp;<wbr><font SIZE="-1">SAHPI_IN&nbsp;<wbr></font>&nbsp;<wbr>SaHpiSessionIdT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>SessionId,<br />
&nbsp;<wbr><font SIZE="-1">SAHPI_IN&nbsp;<wbr></font>&nbsp;<wbr>SaHpiResourceIdT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ResourceId );</dl>
<h2>SEE ALSO</h2>
<pre>
         hpi_shell
         hpialarms      hpigensimdata  hpireset       hpitop
         hpidomain      hpiinv         hpisensor      hpitree
         hpievents      hpionIBMblade  hpisettime     hpiwdt
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
