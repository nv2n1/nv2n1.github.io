---

title: "euca-describe-route-tables(1)"
name: "euca-describe-route-tables"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-describe-route-tables/"
description: "euca-describe-route-tables – Describe one or more VPC route tables"
---

<p> euca-describe-route-tables &#8211; Describe one or more VPC route tables</p>
<h2>SYNOPSIS</h2>
<p> euca-describe-route-tables [&#8211;show-empty-fields] [-U URL]</p>
<dl>
<dt>[&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY]</dt>
<dd> [&#8211;security-token TOKEN] [&#8211;filter NAME=VALUE] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] [RTABLE [RTABLE &#8230;]]</dd></dl>
<h2>DESCRIPTION</h2>
<p> Describe one or more VPC route tables</p>
<h3>positional arguments:</h3>
<dl>
<dt>RTABLE</dt>
<dd> limit results to specific route tables</dd></dl>
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
<dt>association.route-table-association-id</dt>
<dd> ID of an association for the route table</dd>
<dt>association.route-table-id</dt>
<dd> ID of a route table involved in an association</dd>
<dt>association.subnet-id</dt>
<dd> ID of a subnet involved in an association</dd>
<dt>association.main</dt>
<dd> whether the route table is the main route table for its VPC route-table-id route.destination-cidr-block</dd>
<dt>CIDR address block specified in one of the</dt>
<dd> table&#8217;s routes</dd>
<dt>route.gateway-id</dt>
<dd> ID of a gateway specified by a route in the table</dd>
<dt>route.instance-id</dt>
<dd> ID of an instance specified by a route in the table</dd>
<dt>route.nat-gateway-id</dt>
<dd> ID of a NAT gateway specified by a route in the table route.vpc-peering-connection-id ID of a VPC peering connection specified by a route in the table</dd>
<dt>route.origin</dt>
<dd> which operation created a route in the table</dd>
<dt>route.state</dt>
<dd> whether a route in the table has state &quot;active&quot; or &quot;blackhole&quot;</dd>
<dt>tag-key</dt>
<dd> key of a tag assigned to the route table</dd>
<dt>tag-value</dt>
<dd> value of a tag assigned to the route table</dd>
<dt>tag:KEY</dt>
<dd> specific tag key/value combination</dd>
<dt>vpc-id</dt>
<dd> the associated VPC&#8217;s ID </dd>
</dl>
