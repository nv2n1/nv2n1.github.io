---
title: "pmdaelasticsearch(1)"
name: "pmdaelasticsearch"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdaelasticsearch/"
description: "pmdaelasticsearch – elasticsearch performance metrics domain agent (PMDA)"
---

<h2>NAME</h2>
<p> <code>pmdaelasticsearch</code> &#8211; elasticsearch performance metrics domain agent (PMDA)</p>
<h2>DESCRIPTION</h2>
<p> <code>pmdaelasticsearch</code> is a Performance Metrics Domain Agent (<font SIZE="-1">PMDA</font>) which exports performance metrics from elasticsearch.</p>
<h2>INSTALLATION</h2>
<p> This <font SIZE="-1">PMDA</font> requires that elasticsearch is running on the local host and is accepting queries on <font SIZE="-1">TCP</font> port 9200. </p>
<p> Install the elasticsearch <font SIZE="-1">PMDA</font> by using the Install script as root: </p>
<p>#&nbsp;<wbr>cd&nbsp;<wbr>$PCP_PMDAS_DIR/elasticsearch </p>
<p>#&nbsp;<wbr>./Install </p>
<p> To uninstall, do the following as root: </p>
<p>#&nbsp;<wbr>cd&nbsp;<wbr>$PCP_PMDAS_DIR/elasticsearch </p>
<p>#&nbsp;<wbr>./Remove </p>
<p> <code>pmdaelasticsearch</code> is launched by <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1) and should never be executed directly. The Install and Remove scripts notify <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1) when the agent is installed or removed.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_PMDAS_DIR/elasticsearch/es.conf</code></p>
<dd> optional configuration file for <code>pmdaelasticsearch</code></p>
<dt><code>$PCP_PMDAS_DIR/elasticsearch/Install</code></p>
<dd> installation script for the <code>pmdaelasticsearch</code> agent</p>
<dt><code>$PCP_PMDAS_DIR/elasticsearch/Remove</code></p>
<dd> undo installation script for the <code>pmdaelasticsearch</code> agent</p>
<dt><code>$PCP_LOG_DIR/pmcd/elasticsearch.log</code></p>
<dd> default log file for error messages from <code>pmdaelasticsearch</code></dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by <code>PCP</code>. On each installation, the file <code>/etc/pcp.conf</code> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <i><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></i>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1). </p>
<h2>Index</h2>
