---
title: "curator(1)"
name: "curator"
section: "1"
letter: "c"
url: "/docs/linux/man/1-curator/"
description: "curator – manual page for curator, version 3.0.3"
---

<h2>NAME</h2>
<p> curator &#8211; manual page for curator, version 3.0.3</p>
<h2>SYNOPSIS</h2>
<p> <code>curator</code> [<i>,OPTIONS/</i>] <i>,COMMAND /</i>[<i>,ARGS/</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Curator for Elasticsearch indices.</p>
<dl>
<dt>See <a rel="nofollow" href="http://elastic.co/guide/en/elasticsearch/client/curator/current">http://elastic.co/guide/en/elasticsearch/client/curator/current</a></dt>
<dd></dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;host</code> TEXT</dt>
<dd> Elasticsearch host.</dd>
<dt><code>&#8211;url_prefix</code> TEXT</dt>
<dd> Elasticsearch http url prefix.</dd>
<dt><code>&#8211;port</code> INTEGER</dt>
<dd> Elasticsearch port.</dd>
<dt><code>&#8211;use_ssl</code></dt>
<dd> Connect to Elasticsearch through SSL.</dd>
<dt><code>&#8211;http_auth</code> TEXT</dt>
<dd> Use Basic Authentication ex: user:pass</dd>
<dt><code>&#8211;timeout</code> INTEGER</dt>
<dd> Connection timeout in seconds.</dd>
<dt><code>&#8211;master-only</code></dt>
<dd> Only operate on elected master node.</dd>
<dt><code>&#8211;dry-run</code></dt>
<dd> Do not perform any changes.</dd>
<dt><code>&#8211;debug</code></dt>
<dd> Debug mode</dd>
<dt><code>&#8211;loglevel</code> TEXT</dt>
<dd> Log level</dd>
<dt><code>&#8211;logfile</code> TEXT</dt>
<dd> log file</dd>
<dt><code>&#8211;logformat</code> TEXT</dt>
<dd> Log output format [default|logstash].</dd>
<dt><code>&#8211;version</code></dt>
<dd> Show the version and exit.</dd>
<dt><code>&#8211;help</code></dt>
<dd> Show this message and exit.</dd></dl>
<h2>COMMANDS</h2>
<dl>
<dt>alias</dt>
<dd> Index Aliasing</dd>
<dt>allocation</dt>
<dd> Index Allocation</dd>
<dt>bloom</dt>
<dd> Disable bloom filter cache</dd>
<dt>close</dt>
<dd> Close indices</dd>
<dt>delete</dt>
<dd> Delete indices or snapshots</dd>
<dt>open</dt>
<dd> Open indices</dd>
<dt>optimize</dt>
<dd> Optimize Indices</dd>
<dt>replicas</dt>
<dd> Replica Count Per-shard</dd>
<dt>show</dt>
<dd> Show indices or snapshots</dd>
<dt>snapshot</dt>
<dd> Take snapshots of indices (Backup) </dd>
</dl>
<h2>Index</h2>
