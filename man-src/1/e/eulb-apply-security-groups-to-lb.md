---

title: "eulb-apply-security-groups-to-lb(1)"
name: "eulb-apply-security-groups-to-lb"
section: "1"
letter: "e"
url: "/docs/linux/man/1-eulb-apply-security-groups-to-lb/"
description: "eulb-apply-security-groups-to-lb – [VPC only] Associate one or more security groups with a load balancer. All previous associations with security groups will be replaced."
---

<h2>NAME</h2>
<p> eulb-apply-security-groups-to-lb &#8211; [VPC only] Associate one or more security groups with a load balancer. All previous associations with security groups will be replaced.</p>
<p> eulb-apply-security-groups-to-lb <code>-g</code> GROUP1,GROUP2,&#8230;</p>
<dl>
<dt>[&#8211;show-empty-fields] [-U URL]</dt>
<dd> [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] ELB</dd></dl>
<p> [VPC only] Associate one or more security groups with a load balancer. All previous associations with security groups will be replaced.</p>
<h3>positional arguments:</h3>
<dl>
<dt>ELB</dt>
<dd> name of the load balancer to modify (required)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-g</code> GROUP1,GROUP2,&#8230;, <code>&#8211;security-groups</code> GROUP1,GROUP2,&#8230;</dt>
<dd> security groups to associate the load balancer with (required)</dd>
<dt><code>&#8211;show-empty-fields</code></dt>
<dd> show empty values as &quot;(nil)&quot;</dd>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</dt>
<dd> load balancing service endpoint URL</dd>
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
