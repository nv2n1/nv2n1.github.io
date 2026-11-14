---
title: "pmdanamed(1)"
name: "pmdanamed"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdanamed/"
description: "pmdanamed – BIND (named) PMDA"
---

<h2 class="name">NAME</h2>
<p> pmdanamed &#8211; BIND (named) PMDA </p>
<h2>DESCRIPTION</h2>
<p> <code>pmdanamed</code> is a Performance Metrics Domain Agent (<font SIZE="-1">PMDA</font>) which exports metric values from the <font SIZE="-1">BIND DNS</font> server. Further details on <font SIZE="-1">BIND</font> can be found at <a rel="nofollow" href="http://isc.org/.">http://isc.org/.</a></p>
<h2>INSTALLATION</h2>
<p> If you want access to the names and values for the named performance metrics, do the following as root: </p>
<pre>
        # cd $PCP_PMDAS_DIR/named
        # ./Install
</pre>
<p> If you want to undo the installation, do the following as root: </p>
<pre>
        # cd $PCP_PMDAS_DIR/named
        # ./Remove
</pre>
<p> <code>pmdanamed</code> is launched by <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1) and should never be executed directly. The Install and Remove scripts notify <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1) when the agent is installed or removed.</p>
<h2>FILES</h2>
<dl>
<dt>/var/named/data/named_stats.txt</p>
<dd> statistics file showing values exported from named</p>
<dt>/var/named/chroot/var/named/data/named_stats.txt</p>
<dd> chroot variant of statistics file showing values exported from named</p>
<dt>$PCP_PMDAS_DIR/named/Install</p>
<dd> installation script for the <code>pmdanamed</code> agent</p>
<dt>$PCP_PMDAS_DIR/named/Remove</p>
<dd> undo installation script for the <code>pmdanamed</code> agent</p>
<dt>$PCP_LOG_DIR/pmcd/named.log</p>
<dd> default log file for error messages from <code>pmdanamed</code></dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1), <i><a href="/docs/linux/man/5-named-conf/">named.conf</a></i>(5), <i><a href="/docs/linux/man/8-named/">named</a></i>(8). </p>
<h2>Index</h2>
