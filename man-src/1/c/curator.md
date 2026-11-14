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
<dt>See <a rel="nofollow" href="http://elastic.co/guide/en/elasticsearch/client/curator/current">http://elastic.co/guide/en/elasticsearch/client/curator/current</a></p>
<dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;host</code> TEXT</p>
<dd> Elasticsearch host.</p>
<dt><code>&#8211;url_prefix</code> TEXT</p>
<dd> Elasticsearch http url prefix.</p>
<dt><code>&#8211;port</code> INTEGER</p>
<dd> Elasticsearch port.</p>
<dt><code>&#8211;use_ssl</code></p>
<dd> Connect to Elasticsearch through SSL.</p>
<dt><code>&#8211;http_auth</code> TEXT</p>
<dd> Use Basic Authentication ex: user:pass</p>
<dt><code>&#8211;timeout</code> INTEGER</p>
<dd> Connection timeout in seconds.</p>
<dt><code>&#8211;master-only</code></p>
<dd> Only operate on elected master node.</p>
<dt><code>&#8211;dry-run</code></p>
<dd> Do not perform any changes.</p>
<dt><code>&#8211;debug</code></p>
<dd> Debug mode</p>
<dt><code>&#8211;loglevel</code> TEXT</p>
<dd> Log level</p>
<dt><code>&#8211;logfile</code> TEXT</p>
<dd> log file</p>
<dt><code>&#8211;logformat</code> TEXT</p>
<dd> Log output format [default|logstash].</p>
<dt><code>&#8211;version</code></p>
<dd> Show the version and exit.</p>
<dt><code>&#8211;help</code></p>
<dd> Show this message and exit.</dl>
<h2>COMMANDS</h2>
<dl>
<dt>alias</p>
<dd> Index Aliasing</p>
<dt>allocation</p>
<dd> Index Allocation</p>
<dt>bloom</p>
<dd> Disable bloom filter cache</p>
<dt>close</p>
<dd> Close indices</p>
<dt>delete</p>
<dd> Delete indices or snapshots</p>
<dt>open</p>
<dd> Open indices</p>
<dt>optimize</p>
<dd> Optimize Indices</p>
<dt>replicas</p>
<dd> Replica Count Per-shard</p>
<dt>show</p>
<dd> Show indices or snapshots</p>
<dt>snapshot</p>
<dd> Take snapshots of indices (Backup) </p>
</dl>
<h2>Index</h2>
