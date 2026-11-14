---
title: "pmdate(1)"
name: "pmdate"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdate/"
description: "pmdate – display an offset date"
---

<h2>NAME</h2>
<p> <code>pmdate</code> &#8211; display an offset date</p>
<h2>SYNOPSIS</h2>
<p> <code>pmdate</code> [ <i>offset</i> &#8230; ] <i>format</i></p>
<h2>DESCRIPTION</h2>
<p> <code>pmdate</code> displays the current date and/or time, with an optional offset. </p>
<p> An <i>offset</i> is specified with a leading sign (&#8220;+&#8221; or &#8220;-&#8221;), followed by an integer value, followed by one of the following &#8220;scale&#8221; specifiers;</p>
<dl>
<dt>S</p>
<dd> seconds</p>
<dt>M</p>
<dd> minutes</p>
<dt>H</p>
<dd> hours</p>
<dt>d</p>
<dd> days</p>
<dt>m</p>
<dd> months</p>
<dt>y</p>
<dd> years</dl>
<p> The output <i>format</i> follows the same rules as for <code><a href="/docs/linux/man/1-date/">date</a></code>(1) and <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3). </p>
<p> For example, the following will display the date a week ago as DDMMYYYY; pmdate -7d %d%m%Y</p>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-date/">date</a></code>(1), <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5). </p>
<h2>Index</h2>
