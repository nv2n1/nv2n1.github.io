---

title: "pmdagpfs(1)"
name: "pmdagpfs"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdagpfs/"
description: "pmdagpfs – gpfs filesystem statistics performance metrics domain agent (PMDA)"
---

<p> <code>pmdagpfs</code> &#8211; gpfs filesystem statistics performance metrics domain agent (PMDA)</p>
<h2>DESCRIPTION</h2>
<p> <code>pmdagpfs</code> is a Performance Metrics Domain Agent (PMDA) which exports metric values from the <i>/usr/lpp/mmfs/bin/mmpmon</i> program to provide information on mounted gpfs filesystems.</p>
<h2>INSTALLATION</h2>
<p> Install the gpfs PMDA by using the Install script as root: </p>
<p>#&nbsp;<wbr>cd&nbsp;<wbr>$PCP_PMDAS_DIR/gpfs </p>
<p>#&nbsp;<wbr>./Install </p>
<p> To uninstall, do the following as root: </p>
<p>#&nbsp;<wbr>cd&nbsp;<wbr>$PCP_PMDAS_DIR/gpfs </p>
<p>#&nbsp;<wbr>./Remove </p>
<p> <code>pmdagpfs</code> is launched by <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1) and should never be executed directly. The Install and Remove scripts notify <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1) when the agent is installed or removed.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_PMDAS_DIR/gpfs/Install</code></dt>
<dd> installation script for the <code>pmdagpfs</code> agent</dd>
<dt><code>$PCP_PMDAS_DIR/gpfs/Remove</code></dt>
<dd> undo installation script for the <code>pmdagpfs</code> agent</dd>
<dt><code>$PCP_LOG_DIR/pmcd/gpfs.log</code></dt>
<dd> default log file for error messages from <code>pmdagpfs</code></dd></dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by <code>PCP</code>. On each installation, the file <code>/etc/pcp.conf</code> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <i><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></i>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), and <code>mmpmon</code>(8). </p>
