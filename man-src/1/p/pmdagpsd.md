---
title: "pmdagpsd(1)"
name: "pmdagpsd"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdagpsd/"
description: "pmdagpsd – gpsd performance metrics domain agent (PMDA)"
---

<h2 class="name">NAME</h2>
<p> pmdagpsd &#8211; gpsd performance metrics domain agent (PMDA) </p>
<h2>DESCRIPTION</h2>
<p> <code>pmdagpsd</code> is a Performance Metrics Domain Agent (<font SIZE="-1">PMDA</font>) which exports values from the gpsd daemon.</p>
<h2>INSTALLATION</h2>
<p> If you want access to the names and values for gpsd, do the following as root: </p>
<pre>
    # cd $PCP_PMDAS_DIR/gpsd
    # ./Install
</pre>
<p> If you want to undo the installation, do the following as root: </p>
<pre>
    # cd $PCP_PMDAS_DIR/gpsd
    # ./Remove
</pre>
<p> <code>pmdagpsd</code> is launched by <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1) and should never be executed directly. The Install and Remove scripts notify <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1) when the agent is installed or removed.</p>
<h2>FILES</h2>
<dl>
<dt>$PCP_PMDAS_DIR/gpsd/Install</p>
<dd> installation script for the <code>pmdagpsd</code> agent</p>
<dt>$PCP_PMDAS_DIR/gpsd/Remove</p>
<dd> undo installation script for the <code>pmdagpsd</code> agent</p>
<dt>$PCP_LOG_DIR/pmcd/gpsd.log</p>
<dd> default log file for error messages from <code>pmdagpsd</code></dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1). </p>
<h2>Index</h2>
