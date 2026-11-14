---
title: "pmafm(1)"
name: "pmafm"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmafm/"
description: "pmafm – Performance Co-Pilot archive folio manager"
---

<h2>NAME</h2>
<p> <code>pmafm</code> &#8211; Performance Co-Pilot archive folio manager</p>
<h2>SYNOPSIS</h2>
<p> <code>pmafm</code> <i>folioname</i> [<i>command</i> [<i>arg</i> &#8230;]]</p>
<h2>DESCRIPTION</h2>
<p> A collection of one or more Performance Co-Pilot (PCP) archive logs may be combined with a control file to produce a PCP archive folio. Archive folios are created using either <code><a href="/docs/linux/man/1-mkaf/">mkaf</a></code>(1) or the interactive &#8220;record mode&#8221; services of PCP clients like <code><a href="/docs/linux/man/1-pmchart/">pmchart</a></code>(1). </p>
<p> <code>pmafm</code> provides a number of services that may be used to process folios. In particular, it provides support for execution of PCP tools using one or more of the component archive logs within an archive folio. </p>
<p> The target folio is identified by the folio control file <i>folioname</i>. The syntax for a folio control file is described in <code><a href="/docs/linux/man/1-mkaf/">mkaf</a></code>(1). </p>
<p> If present, the command and arguments following <i>folioname</i> are interpreted and executed as a single command, otherwise commands are read from standard input. </p>
<p> The following commands are supported.</p>
<dl>
<dt><code>archives</code></p>
<dd> Subsequent commands apply to all archives in the folio.</p>
<dt><code>archives</code> <i>N</i>[,&#8230;]</p>
<dd> Archives within a folio are numbered 1, 2, etc. Subsequent commands are restricted to apply only to the designated archives.</p>
<dt><code>archives</code> <i>name</i>[,&#8230;]</p>
<dd> Archives within a folio have unique names. Subsequent commands are restricted to apply only to the designated archives.</p>
<dt><code>check</code></p>
<dd> Validate the presence and format of each file in the folio and the component archives.</p>
<dt><code>help</code></p>
<dd>
 A brief reminder of the command syntax. <code>?</code> is a synonym for <code>help</code>.</p>
<dt><code>hosts</code></p>
<dd>
 Subsequent commands apply to all archives in the folio.</p>
<dt><code>hosts</code> <i>hostname</i>[,&#8230;]</p>
<dd> Subsequent commands are restricted to apply only to those archives that match the designated hostnames.</p>
<dt><code>list</code> [<code>verbose</code>]</p>
<dd> Display the contents of the folio. By default the control header and the ordinal number, hostname and archive base name for each archive in the folio. The <code>verbose</code> option causes <code>pmafm</code> to dump the label record from each archive using <code>pmdumplog -l</code>.</p>
<dt>
<dd> The first named archive in the folio is assumed to be associated with the default host for any tool that tries to replay multiple archives from the folio.</p>
<dt><code>quit</code></p>
<dd>
 Exit <code>pmafm</code>.</p>
<dt><code>remove</code></p>
<dd>
 Echo on standard output the <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1) commands required to remove all of the physical files associated with this archive folio.</p>
<dt><code>repeat</code> <i>tool</i> [<i>arg</i> &#8230;]</p>
<dd> Execute the known PCP <i>tool</i> once per selected archive. For example, the command </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> repeat pmval -t60 kernel.all.load<br />
 would run <code><a href="/docs/linux/man/1-pmval/">pmval</a></code>(1) once per archive, with an appropriate <code>-a</code> argument.</p>
<dt><code>replay</code></p>
<dd>
 Some archive folios are created by tools (e.g. <code><a href="/docs/linux/man/1-pmchart/">pmchart</a></code>(1)) that provide sufficient information to allow all of the information in all of the archives of a folio to be replayed.</p>
<dt>[<code>run</code>] <i>tool</i> [<i>arg</i> &#8230;]</p>
<dd> Execute the known PCP <i>tool</i> on the selected archives. Some PCP tools are able to process multiple concurrent archives, and in this case the tool is run once with the list of all selected archives passed via a <code>-a</code> argument. Otherwise, this command is synonymous with <code>repeat</code>.</p>
<dt><code>selections</code></p>
<dd> Display those archives that would be selected for processing with a <code>repeat</code>, <code>replay</code> or <code>run</code> command.</dl>
<p> The restrictions via any <code>hosts</code> and <code>archives</code> commands are conjuncted. These restrictions serve to limit the specific archives processed in the subsequent <code>repeat</code>, <code>replay</code>, <code>run</code> and <code>selections</code> commands. By default, all archives are selected. </p>
<p> Keywords in commands may be abbreviated provided no ambiguity is introduced, e.g. <code>help</code>, <code>hel</code> and <code>he</code> are synonymous, but <code>h</code> is ambiguous.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_VAR_DIR/config/pmafm/</code><i>*</i></p>
<dd> control files that define the behavior of each PCP tool known to <code>pmafm</code>. This information may be customized or extended, see <i>$PCP_VAR_DIR/config/pmafm/pcp</i> for documentation of the syntax and semantics of these files.</p>
<dt><code>$HOME/.pcp/pmafm/</code><i>*</i></p>
<dd> User customization of the control files. All files in this directory are treated in the same manner as control files in the <i>$PCP_VAR_DIR/config/pmafm</i> directory.</dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mkaf/">mkaf</a></code>(1), <code><a href="/docs/linux/man/1-pmchart/">pmchart</a></code>(1), <code><a href="/docs/linux/man/1-pmview/">pmview</a></code>(1), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmrecordsetup/">pmRecordSetup</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5).</p>
<h2>DIAGNOSTICS</h2>
<p> Many, but all are intended to be easily understood. </p>
<h2>Index</h2>
