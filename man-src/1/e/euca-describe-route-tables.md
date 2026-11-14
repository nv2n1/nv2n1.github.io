---
title: "euca-describe-route-tables(1)"
name: "euca-describe-route-tables"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-describe-route-tables/"
description: "euca-describe-route-tables – Describe one or more VPC route tables"
---

<h2>NAME</h2>
<p> euca-describe-route-tables &#8211; Describe one or more VPC route tables</p>
<h2>SYNOPSIS</h2>
<p> euca-describe-route-tables [&#8211;show-empty-fields] [-U URL]</p>
<dl>
<dt>[&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY]</p>
<dd> [&#8211;security-token TOKEN] [&#8211;filter NAME=VALUE] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] [RTABLE [RTABLE &#8230;]]</dl>
<h2>DESCRIPTION</h2>
<p> Describe one or more VPC route tables</p>
<h3>positional arguments:</h3>
<dl>
<dt>RTABLE</p>
<dd> limit results to specific route tables</dl>
<h3>optional arguments:</h3>
<dl>
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
<dt>association.route-table-association-id</p>
<dd> ID of an association for the route table</p>
<dt>association.route-table-id</p>
<dd> ID of a route table involved in an association</p>
<dt>association.subnet-id</p>
<dd> ID of a subnet involved in an association</p>
<dt>association.main</p>
<dd> whether the route table is the main route table for its VPC route-table-id route.destination-cidr-block</p>
<dt>CIDR address block specified in one of the</p>
<dd> table&#8217;s routes</p>
<dt>route.gateway-id</p>
<dd> ID of a gateway specified by a route in the table</p>
<dt>route.instance-id</p>
<dd> ID of an instance specified by a route in the table</p>
<dt>route.nat-gateway-id</p>
<dd> ID of a NAT gateway specified by a route in the table route.vpc-peering-connection-id ID of a VPC peering connection specified by a route in the table</p>
<dt>route.origin</p>
<dd> which operation created a route in the table</p>
<dt>route.state</p>
<dd> whether a route in the table has state &quot;active&quot; or &quot;blackhole&quot;</p>
<dt>tag-key</p>
<dd> key of a tag assigned to the route table</p>
<dt>tag-value</p>
<dd> value of a tag assigned to the route table</p>
<dt>tag:KEY</p>
<dd> specific tag key/value combination</p>
<dt>vpc-id</p>
<dd> the associated VPC&#8217;s ID </p>
</dl>
<h2>Index</h2>
