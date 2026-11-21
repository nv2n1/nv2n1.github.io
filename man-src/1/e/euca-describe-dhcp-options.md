---

title: "euca-describe-dhcp-options(1)"
name: "euca-describe-dhcp-options"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-describe-dhcp-options/"
description: "euca-describe-dhcp-options – Show information about VPC DHCP option sets"
---

<h2>NAME</h2>
<p> euca-describe-dhcp-options &#8211; Show information about VPC DHCP option sets</p>
<p> euca-describe-dhcp-options [&#8211;show-empty-fields] [-U URL]</p>
<dl>
<dt>[&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY]</dt>
<dd> [&#8211;security-token TOKEN] [&#8211;filter NAME=VALUE] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] [DHCPOPTS [DHCPOPTS &#8230;]]</dd></dl>
<p> Show information about VPC DHCP option sets</p>
<h3>positional arguments:</h3>
<dl>
<dt>DHCPOPTS</dt>
<dd> limit results to specific DHCP option sets</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>&#8211;show-empty-fields</code></dt>
<dd> show empty values as &quot;(nil)&quot;</dd>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</dt>
<dd> compute service endpoint URL</dd>
<dt><code>&#8211;region</code> USER [at] REGION</dt>
<dd> region and/or user names to search when looking up config file data</dd>
<dt> <code>-I</code> KEY_ID, <code>&#8211;access-key-id</code> KEY_ID</dt>
<dt> <code>-S</code> KEY, <code>&#8211;secret-key</code> KEY</dt>
<dt> <code>&#8211;security-token</code> TOKEN</dt>
<dt><code>&#8211;filter</code> NAME=VALUE</dt>
<dd>
</dd><dd>restrict results to those that meet criteria</dd>
<dt><code>&#8211;debug</code></dt>
<dd> show debugging output</dd>
<dt><code>&#8211;debugger</code></dt>
<dd> launch interactive debugger on error</dd>
<dt><code>&#8211;version</code></dt>
<dd> show the program&#8217;s version and exit</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> show this help message and exit</dd></dl>
<h3>allowed filter names:</h3>
<dl>
<dt>dhcp-options-id</dt>
<dd> dhcp option set ID</dd>
<dt>key</dt>
<dd> key for one of the options (e.g. domain-name)</dd>
<dt>tag-key</dt>
<dd> key of a tag assigned to the DHCP option set</dd>
<dt>tag-value</dt>
<dd> value of a tag assigned to the DHCP option set</dd>
<dt>tag:KEY</dt>
<dd> specific tag key/value combination</dd>
<dt>value</dt>
<dd> value for one of the options </dd>
</dl>
