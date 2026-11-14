---
title: "euscale-put-scheduled-update-group-action(1)"
name: "euscale-put-scheduled-update-group-action"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euscale-put-scheduled-update-group-action/"
description: "euscale-put-scheduled-update-group-action – Schedule a scaling action for an auto-scaling group"
---

<h2>NAME</h2>
<p> euscale-put-scheduled-update-group-action &#8211; Schedule a scaling action for an auto-scaling group</p>
<h2>SYNOPSIS</h2>
<p> euscale-put-scheduled-update-group-action <code>-g</code> ASGROUP</p>
<dl>
<dt>[-b YYYY-MM-DDThh:mm:ssZ]</p>
<dd> [-e YYYY-MM-DDThh:mm:ssZ] [-r &quot;MIN HOUR DATE MONTH DAY&quot;] [&#8211;desired-capacity COUNT] [&#8211;max-size COUNT] [&#8211;min-size COUNT] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] ACTION</dl>
<h2>DESCRIPTION</h2>
<p> Schedule a scaling action for an auto-scaling group</p>
<h3>positional arguments:</h3>
<dl>
<dt>ACTION</p>
<dd> name of the new scheduled action</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-g</code> ASGROUP, <code>&#8211;auto-scaling-group</code> ASGROUP</p>
<dd> auto-scaling group the new action should affect (required)</p>
<dt><code>-b</code> YYYY-MM-DDThh:mm:ssZ, <code>&#8211;start-time</code> YYYY-MM-DDThh:mm:ssZ</p>
<dd> time for this action to start</p>
<dt><code>-e</code> YYYY-MM-DDThh:mm:ssZ, <code>&#8211;end-time</code> YYYY-MM-DDThh:mm:ssZ</p>
<dd> time for this action to end</p>
<dt><code>-r</code> &quot;MIN HOUR DATE MONTH DAY&quot;, <code>&#8211;recurrence</code> &quot;MIN HOUR DATE MONTH DAY&quot;</p>
<dd> time when recurring future actions will start, in crontab format</p>
<dt><code>&#8211;desired-capacity</code> COUNT</p>
<dd> new capacity setting for the group</p>
<dt><code>&#8211;max-size</code> COUNT</p>
<dd> maximum number of instances to allow in the group</p>
<dt><code>&#8211;min-size</code> COUNT</p>
<dd> minimum number of instances to allow in the group</p>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</p>
<dd> auto-scaling service endpoint URL</p>
<dt><code>&#8211;region</code> USER [at] REGION</p>
<dd> region and/or user names to search when looking up config file data</p>
<dt> <code>-I</code> KEY_ID, <code>&#8211;access-key-id</code> KEY_ID</p>
<dt> <code>-S</code> KEY, <code>&#8211;secret-key</code> KEY</p>
<dt> <code>&#8211;security-token</code> TOKEN</p>
<dt><code>&#8211;debug</code></p>
<dd>
<dd>show debugging output</p>
<dt><code>&#8211;debugger</code></p>
<dd> launch interactive debugger on error</p>
<dt><code>&#8211;version</code></p>
<dd> show the program&#8217;s version and exit</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> show this help message and exit </p>
</dl>
<h2>Index</h2>
