---
title: "pmdavmware(1)"
name: "pmdavmware"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdavmware/"
description: "pmdavmware – VMware performance metrics domain agent (PMDA)"
---

<h2 class="name">NAME</h2>
<p> pmdavmware &#8211; VMware performance metrics domain agent (PMDA) </p>
<h2>DESCRIPTION</h2>
<p> <code>pmdavmware</code> is a Performance Metrics Domain Agent (<font SIZE="-1">PMDA</font>) which exports metric values from a (possibly remote) VMware virtualisation host. </p>
<p> This implementation uses the VMare Perl <font SIZE="-1">API </font>(refer to the online docs at <a rel="nofollow" href="http://www.vmware.com/support/developer/viperltoolkit">http://www.vmware.com/support/developer/viperltoolkit</a>). VIPerl is a prerequisite for this <font SIZE="-1">PMDA,</font> it needs to be installed and configured before attempting to use this agent. It is highly recommended that you test your VIPerl installation using the demo programs that are shipped with VIPerl, before attempting to use this <font SIZE="-1">PMDA.</font></p>
<h2>INSTALLATION</h2>
<p> In order to access performance data using the VIPerl <font SIZE="-1">API,</font> it is necessary to be able to login to the metrics source. Hence, a valid VMware server name, user name and pass word are needed by the <font SIZE="-1">PMDA. </font> These can be passed in on the command line (via the pmcd.conf file) or via a vmware.conf file in the <font SIZE="-1">PMDA</font> directory. </p>
<pre>
        # cd $PCP_PMDAS_DIR/vmware
        # [ edit vmware.conf ]
</pre>
<p> This file should contain connection information, such as: </p>
<pre><code>
$host = 'vm.host.net';
$server = 'vm.server.net';
$username = 'XXXX';
$password = 'YYYY';
</code></pre>
<p> Once this is setup, you can access the names and values for the vmware performance metrics by doing the following as root: </p>
<pre>
        # cd $PCP_PMDAS_DIR/vmware
        # ./Install
</pre>
<p> If you want to undo the installation, do the following as root: </p>
<pre>
        # cd $PCP_PMDAS_DIR/vmware
        # ./Remove
</pre>
<p> <code>pmdavmware</code> is launched by <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1) and should never be executed directly. The Install and Remove scripts notify <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1) when the agent is installed or removed.</p>
<h2>FILES</h2>
<dl>
<dt>$PCP_PMDAS_DIR/vmware/vmware.conf</p>
<dd> configuration file for the <code>pmdavmware</code> agent</p>
<dt>$PCP_PMDAS_DIR/vmware/Install</p>
<dd> installation script for the <code>pmdavmware</code> agent</p>
<dt>$PCP_PMDAS_DIR/vmware/Remove</p>
<dd> undo installation script for the <code>pmdavmware</code> agent</p>
<dt>$PCP_LOG_DIR/pmcd/vmware.log</p>
<dd> default log file for error messages from <code>pmdavmware</code></dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1). </p>
<h2>Index</h2>
