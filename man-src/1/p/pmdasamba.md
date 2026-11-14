---
title: "pmdasamba(1)"
name: "pmdasamba"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdasamba/"
description: "pmdasamba – Samba performance metrics domain agent (PMDA)"
---

<h2 class="name">NAME</h2>
<p> pmdasamba &#8211; Samba performance metrics domain agent (PMDA) </p>
<h2>DESCRIPTION</h2>
<p> <code>pmdasamba</code> is a Performance Metrics Domain Agent (<font SIZE="-1">PMDA</font>) which exports metric values from Samba, a Windows <font SIZE="-1">SMB/CIFS</font> server for <font SIZE="-1">UNIX.</font> </p>
<p> In order for values to be made available by this <font SIZE="-1">PMDA,</font> Samba must have been built with profiling support (<font SIZE="-1">WITH_PROFILE</font> in &#8220;smbd -b&#8221; output). This <font SIZE="-1">PMDA</font> dynamically enumerates much of its metric hierarchy, based on the contents of &#8220;smbstatus &#8211;profile&#8221;. </p>
<p> When the agent is installed (see below), the Install script will attempt to enable Samba statistics gathering, using &#8220;smbcontrol &#8211;profile&#8221;.</p>
<h2>INSTALLATION</h2>
<p> If you want access to the names and values for the samba performance metrics, do the following as root: </p>
<pre>
        # cd $PCP_PMDAS_DIR/samba
        # ./Install
</pre>
<p> If you want to undo the installation, do the following as root: </p>
<pre>
        # cd $PCP_PMDAS_DIR/samba
        # ./Remove
</pre>
<p> <code>pmdasamba</code> is launched by <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1) and should never be executed directly. The Install and Remove scripts notify <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1) when the agent is installed or removed.</p>
<h2>FILES</h2>
<dl>
<dt>$PCP_PMDAS_DIR/samba/Install</p>
<dd> installation script for the <code>pmdasamba</code> agent</p>
<dt>$PCP_PMDAS_DIR/samba/Remove</p>
<dd> undo installation script for the <code>pmdasamba</code> agent</p>
<dt>$PCP_LOG_DIR/pmcd/samba.log</p>
<dd> default log file for error messages from <code>pmdasamba</code></dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1), <i><a href="/docs/linux/man/7-samba/">samba</a></i>(7) and <i><a href="/docs/linux/man/8-smbd/">smbd</a></i>(8). </p>
<h2>Index</h2>
