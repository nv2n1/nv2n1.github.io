---
title: "pmns(5)"
name: "pmns"
section: "5"
letter: "p"
url: "/docs/linux/man/5-pmns/"
description: "pmns – the performance metrics name space"
---

<p><code>pmns</code> &#8211; the performance metrics name space</p>
<h2>Synopsis</h2>
<p><i>$PCP_VAR_DIR/pmns</i></p>
<h2>Description</h2>
<p>When using the Performance Metrics Programming Interface (PMAPI) of the Performance Co-Pilot (PCP), performance metrics are identified by an external name in a hierarchic Performance Metrics Name Space (PMNS), and an internal identifier, the Performance Metric Identifier (PMID). </p>
<p> A PMNS specifies the association between a metric&#8217;s name and its PMID. </p>
<p> A PMNS is defined on one or more ASCII source files. </p>
<p> Loading of a PMNS is done by calling <code><a href="/docs/linux/man/3-pmloadnamespace/">pmLoadNameSpace</a></code>(3) or <code><a href="/docs/linux/man/3-pmloadasciinamespace/">pmLoadASCIINameSpace</a></code>(3). </p>
<p> As of Version 3.10.3 of PCP, by default duplicate names for the same PMID <code>are</code> allowed in the PMNS, although <code><a href="/docs/linux/man/3-pmloadasciinamespace/">pmLoadASCIINameSpace</a></code>(3) provides an alternative interface with user-defined control over the processing of duplicate names in the PMNS. The external format for a PMNS conforms to the syntax and semantics described in the following sections. </p>
<p> There is one default PMNS in the files below <i>$PCP_VAR_DIR/pmns</i>, although users and application developers are free to create and use alternate PMNS&#8217;s. For an example of this, see the PCP Tutorial in <i>$PCP_DEMOS_DIR/Tutorial</i>. </p>
<p> Although an application can call <code><a href="/docs/linux/man/3-pmloadnamespace/">pmLoadNameSpace</a></code>(3), normally this is only done directly for the <code>-n</code> command line option where an explicit root PMNS file is specified. Since PCP version 2 uses a distributed PMNS (see below), an application can extract PMNS information from a host&#8217;s PMCD or an archive. If the PMNS source is a version 1 archive (see <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1)), however, then the local PMNS will be loaded using the path specified by the environment variable <code>PMNS_DEFAULT</code>.</p>
<h2>Distributed Pmns</h2>
<p>In PCP version 1, the PMNS functions in the API all operated on a PMNS loaded locally from a file. Since PCP version 2, however, PMNS functions may get the PMNS information remotely from a PMCD or directly from the meta data of an archive.</p>
<h2>Processing Framework</h2>
<p>The PMNS specification is initially passed through <code><a href="/docs/linux/man/1-pmcpp/">pmcpp</a></code>(1). This means the following facilities may be used in the specification</p>
<dl>
<dt>+</p>
<dd>C-style comments</p>
<dt>+</p>
<dd><i>#include</i> directives</p>
<dt>+</p>
<dd><i>#define</i> directives and macro substitution</p>
<dt>+</p>
<dd>conditional processing via <i>#ifdef</i> &#8230; <i>#endif</i>, etc.</dl>
<p> When <code><a href="/docs/linux/man/1-pmcpp/">pmcpp</a></code>(1) is executed, the &#8220;standard&#8221; include directories are the current directory and <i>$PCP_VAR_DIR/pmns</i>. </p>
<p> The pre-processing with <code><a href="/docs/linux/man/1-pmcpp/">pmcpp</a></code>(1) may be omitted in some cases where the PMNS is known to <code>not</code> contain any C-style comments, preprocessor directives or macros. Refer to the descriptions of <code><a href="/docs/linux/man/3-pmloadasciinamespace/">pmLoadASCIINameSpace</a></code>(3) and <code><a href="/docs/linux/man/3-pmloadnamespace/">pmLoadNameSpace</a></code>(3) for details.</p>
<h2>Syntax</h2>
<p>The general syntax for a non-leaf node in the PMNS is as follows </p>
<pre>pathname {
 name [pmid]
 ...
}</pre>
<p>Where <i>pathname</i> is the full pathname from the root of the PMNS to this non-leaf node, with each component in the pathname separated by a &#8220;.&#8221;. The root node for the PMNS must have the special name &#8220;root&#8221;, but the common prefix &#8220;root.&#8221; must be omitted from all pathnames. Each component in the pathname must begin with an alphabetic character, and be followed by zero or more characters drawn from the alphabetics, the digits and the underscore &#8220;_&#8221;) character. For alphabetic characters in a pathname component, upper and lower case are distinguished. </p>
<p> Non-leaf nodes in the PMNS may be defined in any order. </p>
<p> The descendent nodes are defined by the set of <i>names</i>, relative to the <i>pathname</i> of their parent non-leaf node. For the descendent nodes, leaf nodes have a <i>pmid</i> specification, non-leaf nodes do not. The syntax for the <i>pmid</i> specification has been chosen to help manage the allocation of PMIDs across disjoint and autonomous domains of administration and implementation. Each <i>pmid</i> consists of 3 integer parts, separated by colons, e.g. 14:27:11. This hierarchic numbering scheme is intended to mirror the implementation hierarchy of performance metric domain, metrics cluster (data structure or operational similarity) and individual metric. In practice, the two leading components are likely to be macros in the PMNS specification source, and <code><a href="/docs/linux/man/1-pmcpp/">pmcpp</a></code>(1) will convert the macros to integers. These macros for the initial components of the <i>pmid</i> are likely to be defined either in a standard include file, e.g. <i>$PCP_VAR_DIR/pmns/stdpmid</i>, or in the current source file. </p>
<p> To support dynamic metrics, where the existence of a metric is known to a PMDA, but not visible in the PMNS, a variant syntax for the <i>pmid</i> is supported, namely a domain number followed by asterisks for the other components of the <i>pmid</i>, e.g. 14:*:*. The corresponding metric name forms the root of a subtree of dynamic metric names defined in the corresponding PMDA as identified by the domain number. </p>
<p> The current allocation of the high-order (PMD or domain) component of PMIDs is as follows. <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center>Range</td>
<td ALIGN=center>Allocation
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td>reserved
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>1-31&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td>PMDAs from the PCP base product
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>32-39&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td>Oracle
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>40-47&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td>Sybase
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>48-55&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td>Informix
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>56-58&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td>SNMP Gateway PMDA
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>59-63&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td>Linux PMDAs
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>64-69&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td>ISV PMDAs
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>70-128&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td>more PMDAs from the PCP base product
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>129-510&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td>End-user PMDAs and demo PMDAs
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>511&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td>RESERVED
</td>
</tr>
</table>
</table>
<p></center></p>
<h2>Example</h2>
<pre><code>#define KERNEL 1
#define FOO 317
root {
    network
    cpu
    dynamic     FOO:*:*
}

#define NETWORK 26
network {
    intrate     KERNEL:NETWORK:1
    packetrate
}

network.packetrate {
    in          KERNEL:NETWORK:35
    out         KERNEL:NETWORK:36
}

#define CPU 10
cpu {
    syscallrate KERNEL:CPU:10
    util
}

#define USER 20
#define SYSTEM 21
#define IDLE 22

cpu.util {
    user        KERNEL:CPU:USER
    sys         KERNEL:CPU:SYSTEM
    idle        KERNEL:CPU:IDLE
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/1-pmcpp/">pmcpp</a></code>(1), <code><a href="/docs/linux/man/3-pcpintro/">PCPIntro</a></code>(3), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmerrstr/">pmErrStr</a></code>(3), <code><a href="/docs/linux/man/3-pmgetconfig/">pmGetConfig</a></code>(3), <code><a href="/docs/linux/man/3-pmloadasciinamespace/">pmLoadASCIINameSpace</a></code>(3), <code><a href="/docs/linux/man/3-pmloadnamespace/">pmLoadNameSpace</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5). </p>
