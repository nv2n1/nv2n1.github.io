---
title: "euca-describe-snapshots(1)"
name: "euca-describe-snapshots"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-describe-snapshots/"
description: "euca-describe-snapshots – Show information about snapshots"
---

<h2>NAME</h2>
<p> euca-describe-snapshots &#8211; Show information about snapshots</p>
<h2>SYNOPSIS</h2>
<p> euca-describe-snapshots [-a] [-o ACCOUNT] [-r ACCOUNT]</p>
<dl>
<dt>[&#8211;show-empty-fields] [-U URL]</p>
<dd> [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;filter NAME=VALUE] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] [SNAPSHOT [SNAPSHOT &#8230;]]</dl>
<h2>DESCRIPTION</h2>
<p> Show information about snapshots</p>
<h2>DESCRIPTION</h2>
<p> By default, only snapshots your account owns and snapshots for which your account has explicit restore permissions are shown.</p>
<h3>positional arguments:</h3>
<dl>
<dt>SNAPSHOT</p>
<dd> limit results to specific snapshots</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-a</code>, <code>&#8211;all</code></p>
<dd> describe all snapshots</p>
<dt><code>-o</code> ACCOUNT, <code>&#8211;owner</code> ACCOUNT</p>
<dd> limit results to snapshots owned by specific accounts</p>
<dt><code>-r</code> ACCOUNT, <code>&#8211;restorable-by</code> ACCOUNT</p>
<dd> limit results to snapahots restorable by specific accounts</p>
<dt><code>&#8211;show-empty-fields</code></p>
<dd> show empty values as &quot;(nil)&quot;</p>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</p>
<dd> compute service endpoint URL</p>
<dt><code>&#8211;region</code> USER [at] REGION</p>
<dd> region and/or user names to search when looking up config file data</p>
<dt> <code>-I</code> KEY_ID, <code>&#8211;access-key-id</code> KEY_ID</p>
<dt> <code>-S</code> KEY, <code>&#8211;secret-key</code> KEY</p>
<dt> <code>&#8211;security-token</code> TOKEN</p>
<dt><code>&#8211;filter</code> NAME=VALUE</p>
<dd>
<dd>restrict results to those that meet criteria</p>
<dt><code>&#8211;debug</code></p>
<dd> show debugging output</p>
<dt><code>&#8211;debugger</code></p>
<dd> launch interactive debugger on error</p>
<dt><code>&#8211;version</code></p>
<dd> show the program&#8217;s version and exit</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> show this help message and exit</dl>
<h3>allowed filter names:</h3>
<dl>
<dt>description</p>
<dd> snapshot description</p>
<dt>owner-alias</p>
<dd> snapshot owner&#8217;s account alias</p>
<dt>owner-id</p>
<dd> snapshot owner&#8217;s account ID</p>
<dt>progress</p>
<dd> snapshot progress, in percentage snapshot-id start-time snapshot initiation time status tag-key key of a tag assigned to the snapshot tag-value value of a tag assigned to the snapshot tag:KEY specific tag key/value combination volume-id source volume ID volume-size </p>
</dl>
<h2>Index</h2>
