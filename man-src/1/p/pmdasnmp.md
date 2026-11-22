---

title: "pmdasnmp(1)"
name: "pmdasnmp"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdasnmp/"
description: "pmdasnmp – Gateway from SNMP to PCP (PMDA)"
---

<p> pmdasnmp &#8211; Gateway from SNMP to PCP (PMDA) </p>
<h2>DESCRIPTION</h2>
<p> <code>pmdasnmp</code> is a Performance Metrics Domain Agent (PMDA) which provides a generic gateway from PCP queries from a PCP client to SNMP queries to one or more SNMP agents.</p>
<h2>INSTALLATION</h2>
<p> If you want access to the SNMP gateway performance metrics, do the following as root: </p>
<pre>
        # cd $PCP_PMDAS_DIR/snmp
        # ./Install
</pre>
<p> If you want to undo the installation, do the following as root: </p>
<pre>
        # cd $PCP_PMDAS_DIR/snmp
        # ./Remove
</pre>
<p> <code>pmdasnmp</code> is launched by <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1) and should never be executed directly. The Install and Remove scripts notify <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1) when the agent is installed or removed.</p>
<h2>CONFIGURATION</h2>
<p> TODO: define config file format here &#8211; map/set/host/&#8230; etc</p>
<h2>FILES</h2>
<dl>
<dt>$PCP_PMDAS_DIR/snmp/snmp.conf</dt>
<dd> optional configuration file for <code>pmdasnmp</code></dd>
<dt>$PCP_PMDAS_DIR/snmp/Install</dt>
<dd> installation script for the <code>pmdasnmp</code> agent</dd>
<dt>$PCP_PMDAS_DIR/snmp/Remove</dt>
<dd> undo installation script for the <code>pmdasnmp</code> agent</dd>
<dt>$PCP_LOG_DIR/pmcd/snmp.log</dt>
<dd> default log file for error and <i>warn()</i> messages from <code>pmdasnmp</code></dd></dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1) and SNMP </p>
