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
<p> euscale-put-scheduled-update-group-action <code>-g</code> ASGROUP</p>
<dl>
<dt>[-b YYYY-MM-DDThh:mm:ssZ]</dt>
<dd> [-e YYYY-MM-DDThh:mm:ssZ] [-r &quot;MIN HOUR DATE MONTH DAY&quot;] [&#8211;desired-capacity COUNT] [&#8211;max-size COUNT] [&#8211;min-size COUNT] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] ACTION</dd></dl>
<p> Schedule a scaling action for an auto-scaling group</p>
<h3>positional arguments:</h3>
<dl>
<dt>ACTION</dt>
<dd> name of the new scheduled action</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-g</code> ASGROUP, <code>&#8211;auto-scaling-group</code> ASGROUP</dt>
<dd> auto-scaling group the new action should affect (required)</dd>
<dt><code>-b</code> YYYY-MM-DDThh:mm:ssZ, <code>&#8211;start-time</code> YYYY-MM-DDThh:mm:ssZ</dt>
<dd> time for this action to start</dd>
<dt><code>-e</code> YYYY-MM-DDThh:mm:ssZ, <code>&#8211;end-time</code> YYYY-MM-DDThh:mm:ssZ</dt>
<dd> time for this action to end</dd>
<dt><code>-r</code> &quot;MIN HOUR DATE MONTH DAY&quot;, <code>&#8211;recurrence</code> &quot;MIN HOUR DATE MONTH DAY&quot;</dt>
<dd> time when recurring future actions will start, in crontab format</dd>
<dt><code>&#8211;desired-capacity</code> COUNT</dt>
<dd> new capacity setting for the group</dd>
<dt><code>&#8211;max-size</code> COUNT</dt>
<dd> maximum number of instances to allow in the group</dd>
<dt><code>&#8211;min-size</code> COUNT</dt>
<dd> minimum number of instances to allow in the group</dd>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</dt>
<dd> auto-scaling service endpoint URL</dd>
<dt><code>&#8211;region</code> USER [at] REGION</dt>
<dd> region and/or user names to search when looking up config file data</dd>
<dt> <code>-I</code> KEY_ID, <code>&#8211;access-key-id</code> KEY_ID</dt>
<dt> <code>-S</code> KEY, <code>&#8211;secret-key</code> KEY</dt>
<dt> <code>&#8211;security-token</code> TOKEN</dt>
<dt><code>&#8211;debug</code></dt>
<dd>
</dd><dd>show debugging output</dd>
<dt><code>&#8211;debugger</code></dt>
<dd> launch interactive debugger on error</dd>
<dt><code>&#8211;version</code></dt>
<dd> show the program&#8217;s version and exit</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> show this help message and exit </dd>
</dl>
