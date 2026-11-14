---
title: "pmnsdel(1)"
name: "pmnsdel"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmnsdel/"
description: "pmnsdel – delete a subtree of names from the Performance Co-Pilot PMNS"
---

<h2>NAME</h2>
<p> <code>pmnsdel</code> &#8211; delete a subtree of names from the Performance Co-Pilot PMNS</p>
<h2>SYNOPSIS</h2>
<p> <code>$PCP_BINADM_DIR/pmnsdel</code> [<code>-n</code> <i>namespace</i>] <i>metricpath</i> [ &#8230; ]</p>
<h2>DESCRIPTION</h2>
<p> <code>pmnsdel</code> removes subtrees of names from a Performance Metrics Name Space (PMNS), as used by the components of the Performance Co-Pilot (PCP). </p>
<p> Normally <code>pmnsdel</code> operates on the default Performance Metrics Name Space (PMNS), however if the <code>-n</code> option is specified an alternative namespace is used from the file <i>namespace</i>. </p>
<p> The default PMNS is found in the file <i>$PCP_VAR_DIR/pmns/root</i> unless the environment variable <code>PMNS_DEFAULT</code> is set, in which case the value is assumed to be the pathname to the file containing the default PMNS. </p>
<p> The metric names to be deleted are all those for which one of the <i>metricpath</i> arguments is a prefix in the PMNS, see <code><a href="/docs/linux/man/5-pmns/">pmns</a></code>(5). </p>
<p> All of the files defining the PMNS must be located within the directory that contains the root of the PMNS, and this would typically be <code>$PCP_VAR_DIR/pmns</code> for the default PMNS, and this would typically imply running <code>pmnsdel</code> as root. </p>
<p> Provided some initial integrity checks are satisfied, <code>pmnsdel</code> will update the necessary PMNS files. Should an error be encountered the original namespace is restored. Note that any PMNS files that are no longer referenced by the modified namespace will not be removed, even though their contents are not part of the new namespace.</p>
<h2>CAVEAT</h2>
<p> Once the writing of the new <i>namespace</i> file has begun, the signals SIGINT, SIGHUP and SIGTERM will be ignored to protect the integrity of the new files.</p>
<h2>FILES</h2>
<dl>
<dt><i>$PCP_VAR_DIR/pmns/root</i></p>
<dd> the default PMNS, when then environment variable <code>PMNS_DEFAULT</code> is unset</dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pmnsadd/">pmnsadd</a></code>(1), <code><a href="/docs/linux/man/1-pmnsmerge/">pmnsmerge</a></code>(1), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5), <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5) and <code><a href="/docs/linux/man/5-pmns/">pmns</a></code>(5). </p>
<h2>Index</h2>
