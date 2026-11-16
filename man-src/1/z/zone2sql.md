---
title: "zone2sql(1)"
name: "zone2sql"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zone2sql/"
description: "zone2sql – Convert ISC Bind zones to SQL"
---

<h2>NAME</h2>
<p> zone2sql &#8211; Convert ISC Bind zones to SQL</p>
<h2>SYNOPSIS</h2>
<p> <code>zone2sql [OPTIONS]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>Zone2sql</code> parses Bind <i>named.conf</i> files and zonefiles and outputs SQL on standard out, which can then be fed to your database. </p>
<p> <code>zone2sql</code> understands the Bind master file extension &#8216;$GENERATE&#8217; and will also honour &#8216;$ORIGIN&#8217; and &#8216;$TTL&#8217;. </p>
<p> For backends supporting slave operation there is also an option to keep slave zones as slaves, and not convert them to native operation. </p>
<p> zone2sql can generate SQL for the Generic MySQL, Generic PostgreSQL and Oracle backends.</p>
<h2>OPTIONS</h2>
<p> Input options:</p>
<dl>
<dt><code>&#8211;named-conf=</code><i>&lt;filename&gt;</i></dt>
<dd> Read <i>&lt;filename&gt;</i> to get the bind configuration</dd>
<dt><code>&#8211;zone=</code><i>&lt;zone-file&gt;</i></dt>
<dd> Parse only this zone file. Conflicts with <code>&#8211;named-conf</code> parameter.</dd>
<dt><code>&#8211;zone-name=</code><i>&lt;name&gt;</i></dt>
<dd> When parsing a single zone without $ORIGIN statement, set this as the zone name.</dd></dl>
<p> Output options:</p>
<dl>
<dt><code>&#8211;gmysql</code></dt>
<dd> Output in format suitable for the default configuration of the Generic MySQL backend.</dd>
<dt><code>&#8211;gpgsql</code></dt>
<dd> Output in format suitable for the default configuration of the Generic PostgreSQL backend.</dd>
<dt><code>&#8211;oracle</code></dt>
<dd> Output in format suitable for the default configuration of the Generic Oracle backend.</dd>
<dt><code>&#8211;transactions</code></dt>
<dd> For Oracle and PostgreSQL output, wrap each domain in a transaction for higher speed and integrity.</dd></dl>
<p> Other options:</p>
<dl>
<dt><code>&#8211;slave</code></dt>
<dd> Maintain slave status of zones listed in named.conf as being slaves. The default behaviour is to convert all zones to native operation.</dd>
<dt><code>&#8211;on-error-resume-next</code></dt>
<dd> Ignore missing files during parsing. Dangerous.</dd>
<dt><code>&#8211;help</code></dt>
<dd> List all options</dd>
<dt><code>&#8211;verbose</code></dt>
<dd> Be verbose during conversion.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code>pdns_server</code>(8) </p>
<h2>Index</h2>
