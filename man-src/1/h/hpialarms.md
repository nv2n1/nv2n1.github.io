---
title: "hpialarms(1)"
name: "hpialarms"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hpialarms/"
description: "hpialarms – A openhpi sample application that shows \"Alarm Control\" management instruments"
---

<h2 class="name">NAME</h2>
<p> hpialarms &#8211; A openhpi sample application that shows &quot;Alarm Control&quot; management instruments </p>
<h2>SYNOPSIS</h2>
<pre><code>
hpialarms[-D id][-N host[:port]][-C&lt;cfgfile&gt;]
         [-a 1 | 0][-b 1 | 0][-c 1 | 0][-m 1 | 0][-n 1 | 0][-p 1 | 0][-i n][-o][-X][-h] hpialarms[--domain = id][--host = host[:port]][--cfgfile = file]
                                                                                                 [--diska = 1 | 0][--diskb = 1 | 0][--critical = 1 | 0][--major = 1 | 0]
                                                                                                 [--minor = 1 | 0][--power = 1 | 0][--chassisid = n][--all][--debug][--help]
</code></pre>
<h2>DESCRIPTION</h2>
<p> hpialarms walks the <font SIZE="-1">RPT </font>(Resource Presence Table) for resources that have &#8220;Alarm Control&#8221; management instruments (<font SIZE="-1">SAHPI_CTRL_LED</font>). </p>
<p> If no domain or host is selected, hpialarms uses the default domain as specified in the openhpiclient.conf file.</p>
<h2>OPTIONS</h2>
<p> (No Option) Display alarm states</p>
<h3>Help Options:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show help options</dl>
<h3>Application Options:</h3>
<dl>
<dt><code>-c</code> <i>1|0</i>, &#8211;<code>-critical</code>=<i>1|0</i></p>
<dd> Set critical alarm on|off</p>
<dt><code>-m</code> <i>1|0</i>, &#8211;<code>-major</code>=<i>1|0</i></p>
<dd> Set major alarm on|off</p>
<dt><code>-n</code> <i>1|0</i>, &#8211;<code>-minor</code>=<i>1|0</i></p>
<dd> Set minor alarm on|off</p>
<dt><code>-a</code> <i>1|0</i>, &#8211;<code>-diska</code>=<i>1|0</i></p>
<dd> Set diska alarm on|off</p>
<dt><code>-b</code> <i>1|0</i>, &#8211;<code>-diskb</code>=<i>1|0</i></p>
<dd> Set diskb alarm on|off</p>
<dt><code>-p</code> <i>1|0</i>, &#8211;<code>-power</code>=<i>1|0</i></p>
<dd> Set power alarm on|off</p>
<dt><code>-i</code> <i>n</i>, &#8211;<code>-chassisid</code>=<i>n</i></p>
<dd> Set chassis id on for <i>n</i> seconds</p>
<dt><code>-o</code>, &#8211;<code>-all</code></p>
<dd> Set all alarms off</p>
<dt><code>-D</code> <i>nn</i>, <code>&#8211;domain</code>=<i>nn</i></p>
<dd> Select domain id <i>nn</i></p>
<dt><code>-X</code>, <code>&#8211;debug</code></p>
<dd> Display debug messages</p>
<dt><code>-N</code> <i>&quot;host[:port]&quot;</i>, <code>&#8211;host</code>=<i>&quot;host[:port]&quot;</i></p>
<dd> Open session to the domain served by the daemon at the specified <font SIZE="-1">URL </font>(host:port). This option overrides the <font SIZE="-1">OPENHPI_DAEMON_HOST</font> and <font SIZE="-1">OPENHPI_DAEMON_PORT</font> environment variables. If host contains &#8216;:&#8217; (for example IPv6 address) then enclose it in square brackets. For example: <i>&#8220;[::1]&#8221;</i> or <i>&#8220;[::1]:4743&#8221;</i>.</p>
<dt><code>-C</code> <i>&quot;file&quot;</i>, <code>&#8211;cfgfile</code>=<i>&quot;file&quot;</i></p>
<dd> Use passed file as client configuration file. This option overrides the OPENHPICLIENT_CONf environment variable.</dl>
<h2>SAMPLE OUTPUT</h2>
<p>hpialarmpanel ver 0.6 RptInfo : UpdateCount = 5, UpdateTime = 8a2dc6c0 rptentry[0] resourceid = 1 tag : Mullins<br />
                                                                                                            RDR[45] : ctltype = 2 : 1 oem = 0 Chassis Identify Control<br />
                                                                                                                          RDR[48] : ctltype = 0 : 1 oem = 10 Front Panel Power Alarm LED state = off<br />
                                                                                                                                        RDR[51] : ctltype = 0 : 1 oem = 13 Front Panel Minor Alarm LED state = ON<br />
                                                                                                                                                      RDR[46] : ctltype = 0 : 0 oem = 0 Cold Reset Control<br />
                                                                                                                                                                    RDR[49] : ctltype = 0 : 1 oem = 11 Front Panel Critical Alarm LED state = off<br />
                                                                                                                                                                                  RDR[50] : ctltype = 0 : 1 oem = 12 Front Panel Major Alarm LED state = off</p>
<h2>SEE ALSO</h2>
<pre>
         hpi_shell
         hpidomain      hpigensimdata  hpireset       hpitop
         hpiel          hpiinv         hpisensor      hpitree
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
