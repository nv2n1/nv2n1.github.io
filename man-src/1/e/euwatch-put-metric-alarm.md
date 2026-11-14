---
title: "euwatch-put-metric-alarm(1)"
name: "euwatch-put-metric-alarm"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euwatch-put-metric-alarm/"
description: "euwatch-put-metric-alarm – Create or update an alarm"
---

<h2>NAME</h2>
<p> euwatch-put-metric-alarm &#8211; Create or update an alarm</p>
<h2>SYNOPSIS</h2>
<p> euwatch-put-metric-alarm <code>&#8211;comparison-operator</code></p>
<dl>
<dt>{GreaterThanOrEqualToThreshold,GreaterThanThreshold,LessThanThreshold,LessThanOrEqualToThreshold}</p>
<dd> <code>&#8211;evaluation-periods</code> COUNT <code>&#8211;metric-name</code> METRIC <code>&#8211;namespace</code> NAMESPACE <code>&#8211;period</code> SECONDS <code>&#8211;statistic</code> {Average,Maximum,Minimum,SampleCount,Sum} <code>&#8211;threshold</code> FLOAT [&#8211;actions-enabled {true,false}] [&#8211;alarm-actions ARN1,ARN2,&#8230;] [&#8211;alarm-description DESCRIPTION] [-d KEY1=VALUE1,KEY2=VALUE2,&#8230;] [&#8211;insufficient-data-actions ARN1,ARN2,&#8230;] [&#8211;ok-actions ARN1,ARN2,&#8230;] [&#8211;unit UNIT] [&#8211;show-empty-fields] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] ALARM</dl>
<h2>DESCRIPTION</h2>
<p> Create or update an alarm</p>
<h3>positional arguments:</h3>
<dl>
<dt>ALARM</p>
<dd> name of the alarm (required)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>&#8211;comparison-operator</code> {GreaterThanOrEqualToThreshold,GreaterThanThreshold,LessThanThreshold,LessThanOrEqualToThreshold}</p>
<dd> arithmetic operator with which the comparison with the threshold will be made (required)</p>
<dt><code>&#8211;evaluation-periods</code> COUNT</p>
<dd> number of consecutive periods for which the value of the metric needs to be compared to the threshold (required)</p>
<dt><code>&#8211;metric-name</code> METRIC</p>
<dd> name for the alarm&#8217;s associated metric (required)</p>
<dt><code>&#8211;namespace</code> NAMESPACE</p>
<dd> namespace for the alarm&#8217;s associated metric (required)</p>
<dt><code>&#8211;period</code> SECONDS</p>
<dd> period over which the specified statistic is applied (required)</p>
<dt><code>&#8211;statistic</code> {Average,Maximum,Minimum,SampleCount,Sum}</p>
<dd> statistic on which to alarm (required)</p>
<dt><code>&#8211;threshold</code> FLOAT</p>
<dd> value to compare the statistic against (required)</p>
<dt><code>&#8211;actions-enabled</code> {true,false}</p>
<dd> whether this alarm&#8217;s actions should be executed when it changes state</p>
<dt><code>&#8211;alarm-actions</code> ARN1,ARN2,&#8230;</p>
<dd> ARNs of SNS topics to publish to when the alarm changes to the ALARM state</p>
<dt><code>&#8211;alarm-description</code> DESCRIPTION</p>
<dd> description of the alarm</p>
<dt><code>-d</code> KEY1=VALUE1,KEY2=VALUE2,&#8230;, <code>&#8211;dimensions</code> KEY1=VALUE1,KEY2=VALUE2,&#8230;</p>
<dd> dimensions for the alarm&#8217;s associated metric</p>
<dt><code>&#8211;insufficient-data-actions</code> ARN1,ARN2,&#8230;</p>
<dd> ARNs of SNS topics to publish to when the alarm changes to the INSUFFICIENT_DATA state</p>
<dt><code>&#8211;ok-actions</code> ARN1,ARN2,&#8230;</p>
<dd> ARNs of SNS topics to publish to when the alarm changes to the OK state</p>
<dt><code>&#8211;unit</code> UNIT</p>
<dd> unit for the alarm&#8217;s associated metric</p>
<dt><code>&#8211;show-empty-fields</code></p>
<dd> show empty values as &quot;(nil)&quot;</p>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</p>
<dd> instance monitoring service endpoint URL</p>
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
