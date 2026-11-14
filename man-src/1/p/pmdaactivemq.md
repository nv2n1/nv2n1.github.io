---
title: "pmdaactivemq(1)"
name: "pmdaactivemq"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdaactivemq/"
description: "pmdaactivemq – ActiveMQ performance metrics domain agent (PMDA)"
---

<h2>NAME</h2>
<p> <code>pmdaactivemq</code> &#8211; ActiveMQ performance metrics domain agent (PMDA)</p>
<h2>DESCRIPTION</h2>
<p> <code>pmdaactivemq</code> is a Performance Metrics Domain Agent (<font SIZE="-1">PMDA</font>) which exports performance metrics from ActiveMQ.</p>
<h2>INSTALLATION</h2>
<p> This <font SIZE="-1">PMDA</font> requires that ActiveMQ has been installed with the Jolokia JMX-HTTP bridge enabled. By default the PNDA will connect to localhost at port 8161 with a username and password of &#8216;admin&#8217;. This can be configured in PCP_PMDAS_DIR/activemq/activemq.conf </p>
<p> Install the ActiveMQ <font SIZE="-1">PMDA</font> by using the Install script as root: </p>
<p>#&nbsp;<wbr>cd&nbsp;<wbr>$PCP_PMDAS_DIR/activemq </p>
<p>#&nbsp;<wbr>./Install </p>
<p> To uninstall, do the following as root: </p>
<p>#&nbsp;<wbr>cd&nbsp;<wbr>$PCP_PMDAS_DIR/activemq </p>
<p>#&nbsp;<wbr>./Remove </p>
<p> <code>pmdaactivemq</code> is launched by <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1) and should never be executed directly. The Install and Remove scripts notify <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1) when the agent is installed or removed.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_PMDAS_DIR/activemq/activemq.conf</code></p>
<dd> optional configuration file for <code>pmdaactivemq</code></p>
<dt><code>$PCP_PMDAS_DIR/activemq/Install</code></p>
<dd> installation script for the <code>pmdaactivemq</code> agent</p>
<dt><code>$PCP_PMDAS_DIR/activemq/Remove</code></p>
<dd> undo installation script for the <code>pmdaactivemq</code> agent</p>
<dt><code>$PCP_LOG_DIR/pmcd/activemq.log</code></p>
<dd> default log file for error messages from <code>pmdaactivemq</code></dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by <code>PCP</code>. On each installation, the file <code>/etc/pcp.conf</code> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <i><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></i>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1). </p>
<h2>Index</h2>
