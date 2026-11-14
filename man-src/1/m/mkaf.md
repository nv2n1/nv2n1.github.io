---
title: "mkaf(1)"
name: "mkaf"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mkaf/"
description: "mkaf – create a Performance Co-Pilot archive folio"
---

<h2>NAME</h2>
<p> <code>mkaf</code> &#8211; create a Performance Co-Pilot archive folio</p>
<h2>SYNOPSIS</h2>
<p> <code>$PCP_BINADM_DIR/mkaf</code> [<i>findopts</i>] <i>filename</i> &#8230;</p>
<h2>DESCRIPTION</h2>
<p> A collection of one or more Performance Co-Pilot (see <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1)) archive logs may be combined with <code>mkaf</code> to produce a PCP archive folio and the associated archive folio control file. Some PCP tools use <code>mkaf</code> to create archive folios, e.g. the &#8220;record&#8221; facility in the <code><a href="/docs/linux/man/1-pmchart/">pmchart</a></code>(1) and <code><a href="/docs/linux/man/1-pmview/">pmview</a></code>(1) tools, to facilitate playback with <code><a href="/docs/linux/man/1-pmafm/">pmafm</a></code>(1). </p>
<p> <code>mkaf</code> processes each <i>filename</i> argument, and if this is a component file from a PCP archive that archive is added to the folio. </p>
<p> If <i>filename</i> is a directory, then this is searched recursively using <code><a href="/docs/linux/man/1-find/">find</a></code>(1). Any <i>filename</i> argument beginning with a &#8220;-&#8221; is assumed to be a <code><a href="/docs/linux/man/1-find/">find</a></code>(1) command line option (<i>findopts</i>); the default is <code>-follow</code> if no <i>findopts</i> are specified. </p>
<p> The first named archive in the folio is assumed to be associated with the default host for any tool that tries to replay multiple archives from the folio. </p>
<p> The folio control file is written to standard output, and has the following format.</p>
<dl>
<dt>1.</p>
<dd> The first line contains the word <code>PCPFolio</code>.</p>
<dt>2.</p>
<dd> The second line contains the tag <code>Version:</code> followed by the format version number (currently 1).</p>
<dt>3.</p>
<dd> For subsequent lines, blank lines and lines beginning with &#8220;#&#8221; are ignored.</p>
<dt>4.</p>
<dd> The line beginning with the tag <code>Created:</code> documents where and when the folio was created.</p>
<dt>5.</p>
<dd> The line beginning with the tag <code>Creator:</code> identifies the tool which created the folio (and is assumed to know how to replay the archive folio). If present, the second argument is the name of a configuration file that the creator tool could use to replay the archive folio, e.g. with the <code>replay</code> command for <code><a href="/docs/linux/man/1-pmafm/">pmafm</a></code>(1). In the case of <code>mkaf</code> (unlike <code><a href="/docs/linux/man/1-pmchart/">pmchart</a></code>(1) or <code><a href="/docs/linux/man/1-pmview/">pmview</a></code>(1)) there is no knowledge of the contents of the archives, so the &#8220;creator&#8221; cannot replay the archive, however <code><a href="/docs/linux/man/1-pmchart/">pmchart</a></code>(1) is able to replay any archive, and so this tool is identified as the <code>Creator:</code> for archive folios created by <code><a href="/docs/linux/man/1-mkaf/">mkaf</a></code>(1).</p>
<dt>6.</p>
<dd> This is then followed by one or more lines beginning with the tag <code>Archive:</code> followed by the hostname and base name of the archive.</dl>
<p> For example<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> $ mkaf mydir/gonzo<br />
 might produce the following folio control file. </p>
<pre>
PCPFolio
Version: 1
# use <a href="//www.systutorials.com/docs/linux/man/1-pmafm/">pmafm</a>(1) to process this PCP archive folio
#
Created: on gonzo at Tue Jul  2 03:35:54 EST 1996
Creator: pmchart
#               Host                    Basename
#
Archive:        gonzo                   mydir/gonzo/960627
Archive:        gonzo                   mydir/gonzo/960628
Archive:        gonzo                   mydir/gonzo/960629
Archive:        gonzo                   mydir/gonzo/960630
Archive:        gonzo                   mydir/gonzo/960701
Archive:        gonzo                   mydir/gonzo/960701.00.10
Archive:        gonzo                   mydir/gonzo/960701.05.25
Archive:        gonzo                   mydir/gonzo/960702.00.10
</pre>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-find/">find</a></code>(1), <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmafm/">pmafm</a></code>(1), <code><a href="/docs/linux/man/1-pmchart/">pmchart</a></code>(1), <code><a href="/docs/linux/man/1-pmview/">pmview</a></code>(1), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5).</p>
<h2>DIAGNOSTICS</h2>
<p> Some informational messages, warnings and pathological conditions are reported on standard error. </p>
<h2>Index</h2>
