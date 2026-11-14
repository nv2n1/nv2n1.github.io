---
title: "pmdapdns(1)"
name: "pmdapdns"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdapdns/"
description: "pmdapdns – PowerDNS performance metrics domain agent (PMDA)"
---

<h2 class="name">NAME</h2>
<p> pmdapdns &#8211; PowerDNS performance metrics domain agent (PMDA) </p>
<h2>DESCRIPTION</h2>
<p> <code>pmdapdns</code> is a Performance Metrics Domain Agent (<font SIZE="-1">PMDA</font>) which exports metric values from the PowerDNS authoritative daemon as well as the recursive resolver.</p>
<h2>INSTALLATION</h2>
<p> If you want access to the names and values for the PowerDNS performance metrics, do the following as root: </p>
<pre>
        # cd $PCP_PMDAS_DIR/pdns
        # ./Install
</pre>
<p> If you want to undo the installation, do the following as root: </p>
<pre>
        # cd $PCP_PMDAS_DIR/pdns
        # ./Remove
</pre>
<p> <code>pmdapdns</code> is launched by <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1) and should never be executed directly. The Install and Remove scripts notify <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1) when the agent is installed or removed.</p>
<h2>FILES</h2>
<dl>
<dt>$PCP_PMDAS_DIR/pdns/Install</p>
<dd> installation script for the <code>pmdapdns</code> agent</p>
<dt>$PCP_PMDAS_DIR/pdns/Remove</p>
<dd> undo installation script for the <code>pmdapdns</code> agent</p>
<dt>$PCP_LOG_DIR/pmcd/pdns.log</p>
<dd> default log file for error messages from <code>pmdapdns</code></dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1), <i><a href="/docs/linux/man/8-pdns_control/">pdns_control</a></i>(8), and <i><a href="/docs/linux/man/1-rec_control/">rec_control</a></i>(1). </p>
<h2>Index</h2>
