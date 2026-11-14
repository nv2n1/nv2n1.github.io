---
title: "pmdanews(1)"
name: "pmdanews"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdanews/"
description: "pmdanews – sample Usenet news performance metrics domain agent (PMDA)"
---

<h2 class="name">NAME</h2>
<p> pmdanews &#8211; sample Usenet news performance metrics domain agent (PMDA) </p>
<h2>DESCRIPTION</h2>
<p> <code>pmdanews</code> is an example Performance Metrics Domain Agent (<font SIZE="-1">PMDA</font>) which exports metric values related to a set of newsgroups.</p>
<h2>INSTALLATION</h2>
<p> If you want access to the names and values for the news performance metrics, do the following as root: </p>
<pre>
        # cd $PCP_PMDAS_DIR/news
        # ./Install
</pre>
<p> If you want to undo the installation, do the following as root: </p>
<pre>
        # cd $PCP_PMDAS_DIR/news
        # ./Remove
</pre>
<p> <code>pmdanews</code> is launched by <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1) and should never be executed directly. The Install and Remove scripts notify <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1) when the agent is installed or removed.</p>
<h2>FILES</h2>
<dl>
<dt>$PCP_PMDAS_DIR/news/Install</p>
<dd> installation script for the <code>pmdanews</code> agent</p>
<dt>$PCP_PMDAS_DIR/news/Remove</p>
<dd> undo installation script for the <code>pmdanews</code> agent</p>
<dt>$PCP_LOG_DIR/pmcd/news.log</p>
<dd> default log file for error messages from <code>pmdanews</code></dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1). </p>
<h2>Index</h2>
