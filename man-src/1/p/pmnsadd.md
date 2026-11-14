---
title: "pmnsadd(1)"
name: "pmnsadd"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmnsadd/"
description: "pmnsadd – add new names to the Performance Co-Pilot PMNS"
---

<h2>NAME</h2>
<p> <code>pmnsadd</code> &#8211; add new names to the Performance Co-Pilot PMNS</p>
<h2>SYNOPSIS</h2>
<p> <code>$PCP_BINADM_DIR/pmnsadd</code> [<code>-n</code> <i>namespace</i>] <i>file</i></p>
<h2>DESCRIPTION</h2>
<p> <code><a href="/docs/linux/man/1-pmnsmerge/">pmnsmerge</a></code>(1) performs the same function as <code>pmnsadd</code> and is faster, more robust and more flexible. It is therefore recommended that <code><a href="/docs/linux/man/1-pmnsmerge/">pmnsmerge</a></code>(1) be used instead. </p>
<p> <code>pmnsadd</code> adds subtree(s) of new names into a Performance Metrics Name Space (PMNS), as used by the components of the Performance Co-Pilot (PCP). </p>
<p> Normally <code>pmnsadd</code> operates on the default Performance Metrics Name Space (PMNS), however if the <code>-n</code> option is specified an alternative namespace is used from the file <i>namespace</i>. </p>
<p> The default PMNS is found in the file <i>$PCP_VAR_DIR/pmns/root</i> unless the environment variable <code>PMNS_DEFAULT</code> is set, in which case the value is assumed to be the pathname to the file containing the default PMNS. </p>
<p> The new names are specified in the <i>file</i>, arguments and conform to the syntax for PMNS specifications, see <code><a href="/docs/linux/man/5-pmns/">pmns</a></code>(5). There is one PMNS subtree in each <i>file</i>, and the base PMNS pathname to the inserted subtree is identified by the first group named in each <i>file</i>, e.g. if the specifications begin </p>
<pre>
myagent.foo.stuff {
    mumble      123:45:1
    fumble      123:45:2
}
</pre>
<p> then the new names will be added into the PMNS at the non-leaf position identified by myagent.foo.stuff , and following all other names with the prefix myagent.foo . </p>
<p> The new names must be contained within a single subtree of the namespace. If disjoint subtrees need to be added, these must be packaged into separate files and <code>pmnsadd</code> used on each, one at a time. </p>
<p> All of the files defining the PMNS must be located within the directory that contains the root of the PMNS, this would typically be <code>$PCP_VAR_DIR/pmns</code> for the default PMNS, and this would typically imply running <code>pmnsadd</code> as root. </p>
<p> As a special case, if <i>file</i> contains a line that begins root { then it is assumed to be a complete PMNS that needs to be merged, so none of the subtree extraction and rewriting is performed and <i>file</i> is handed directly to <code><a href="/docs/linux/man/1-pmnsmerge/">pmnsmerge</a></code>(1). </p>
<p> Provided some initial integrity checks are satisfied, <code>pmnsadd</code> will update the PMNS using <code><a href="/docs/linux/man/1-pmnsmerge/">pmnsmerge</a></code>(1) &#8211; if this fails for any reason, the original namespace remains unchanged.</p>
<h2>CAVEAT</h2>
<p> Once the writing of the new <i>namespace</i> file has begun, the signals SIGINT, SIGHUP and SIGTERM will be ignored to protect the integrity of the new files.</p>
<h2>FILES</h2>
<dl>
<dt><i>$PCP_VAR_DIR/pmns/root</i></p>
<dd> the default PMNS, when then environment variable <code>PMNS_DEFAULT</code> is unset</dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pmnsdel/">pmnsdel</a></code>(1), <code><a href="/docs/linux/man/1-pmnsmerge/">pmnsmerge</a></code>(1), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5), <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5) and <code><a href="/docs/linux/man/5-pmns/">pmns</a></code>(5). </p>
<h2>Index</h2>
