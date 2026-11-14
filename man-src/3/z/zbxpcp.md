---
title: "zbxpcp(3)"
name: "zbxpcp"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zbxpcp/"
description: "zbxpcp – Zabbix Agent Loadable PCP Module"
---

<p><code>zbxpcp</code> &#8211; Zabbix Agent Loadable PCP Module</p>
<h2>Description</h2>
<p>The <code>zbxpcp</code> loadable module extends Zabbix agent by making Performance Co-Pilot (PCP) metrics available to it. With the <code>zbxpcp</code> module configured in <i>zabbix_agentd.conf</i> all the PCP metrics are available from the Zabbix agent like any other agent items. As a loadable module (DSO) <code>zbxpcp</code> does not rely on any external programs but directly uses the PCP APIs to fetch PCP metrics when requested. </p>
<p> A typical Linux PCP installation offers over 1,000 metrics by default and is in turn extensible with its own plugins, or PMDAs (&#8220;Performance Metrics Domain Agents&#8221;). In addition to very complete <i>/proc</i> based statistics, readily available PCP PMDAs provide support for such system and application level components as 389 Directory Server, Apache, containers, GFS2, Gluster, KVM, MySQL, NFS, Oracle, Postfix, PostgreSQL, Samba, and Sendmail, among others. PCP also runs on many platforms, including Linux, Mac OS X, FreeBSD, NetBSD, Solaris, and Windows. </p>
<p> For PCP introduction, see <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1). To investigate the available PCP metrics, use for example <code><a href="/docs/linux/man/1-pminfo/">pminfo</a></code>(1). The <i>PCP Quick Reference Guide</i> is available at the PCP home page <a rel="nofollow" href="http://pcp.io/.">http://pcp.io/.</a> </p>
<p> For general information about Zabbix data collection and loadable modules, see <a rel="nofollow" href="https://www.zabbix.com/documentation/3.0/manual/config/items.">https://www.zabbix.com/documentation/3.0/manual/config/items.</a> For Zabbix introduction and downloads, see <a rel="nofollow" href="http://www.zabbix.com/.">http://www.zabbix.com/.</a> </p>
<p> <code>zbxpcp</code> is compatible with the Zabbix module API version <code>1</code>.</p>
<h2>Configuration</h2>
<p>First make sure PCP is installed and configured properly, see the above references for instructions and use for example <code><a href="/docs/linux/man/1-pminfo/">pminfo</a></code>(1) to make sure the PCP metrics can be fetched. To enable the <code>zbxpcp</code> loadable module in a Zabbix agent, the following lines must be added to the Zabbix agent configuration file <i>zabbix_agentd.conf</i> (make sure to use the correct <i>LoadModulePath</i>): </p>
<dl>
<dd>
<pre>LoadModulePath=/usr/lib64/zabbix/agent/
LoadModule=zbxpcp.so</pre>
</dl>
<p> After restarting the Zabbix agent all the PCP metrics will be available with the &#8220;<code>pcp.</code>&#8221; prefix like all the other agent items. This can be verified with the commands: </p>
<dl>
<dd>
<pre>$ pminfo -t
$ zabbix_agentd -p
$ pminfo -f kernel.all.sysfork
$ zabbix_get -s 127.0.0.1 -p 10050 -k pcp.kernel.all.sysfork</pre>
</dl>
<p> Then to collect PCP metrics from Zabbix agents, the Zabbix server side configuration is as usual (see Zabbix documentation if needed). </p>
<p> The PCP <code>pmcd</code> service must always be running when starting up a <code>zbxpcp</code> enabled Zabbix agent, otherwise the module will fail to load and the PCP metrics will not become available. Special care must be taken to make sure this happens also when rebooting the system.</p>
<h2>Files</h2>
<dl>
<dt><code>/etc/zabbix/zabbix_agentd.conf</code></p>
<dd>Typical Zabbix agent configuration file location.</p>
<dt><code>/etc/zabbix/zbxpcp-derived-metrics.conf</code></p>
<dd>Optional PCP derived metrics configuration file for <code>zbxpcp</code>. See <code><a href="/docs/linux/man/3-pmloadderivedconfig/">pmLoadDerivedConfig</a></code>(3) for more info on derived metrics.</p>
<dt><code>$(PCP_LIB_DIR)/zabbix/agent/zbxpcp.so</code></p>
<dd>Zabbix agent loadable PCP module.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pminfo/">pminfo</a></code>(1), <code><a href="/docs/linux/man/1-pmrep/">pmrep</a></code>(1), <code><a href="/docs/linux/man/1-zabbix_get/">zabbix_get</a></code>(1), <code><a href="/docs/linux/man/3-pmloadderivedconfig/">pmLoadDerivedConfig</a></code>(3) and <code><a href="/docs/linux/man/8-zabbix_agentd/">zabbix_agentd</a></code>(8). </p>
