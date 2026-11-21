---

title: "euwatch-put-metric-alarm(1)"
name: "euwatch-put-metric-alarm"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euwatch-put-metric-alarm/"
description: "euwatch-put-metric-alarm – Create or update an alarm"
---

<p> euwatch-put-metric-alarm &#8211; Create or update an alarm</p>
<h2>SYNOPSIS</h2>
<p> euwatch-put-metric-alarm <code>&#8211;comparison-operator</code></p>
<dl>
<dt>{GreaterThanOrEqualToThreshold,GreaterThanThreshold,LessThanThreshold,LessThanOrEqualToThreshold}</dt>
<dd> <code>&#8211;evaluation-periods</code> COUNT <code>&#8211;metric-name</code> METRIC <code>&#8211;namespace</code> NAMESPACE <code>&#8211;period</code> SECONDS <code>&#8211;statistic</code> {Average,Maximum,Minimum,SampleCount,Sum} <code>&#8211;threshold</code> FLOAT [&#8211;actions-enabled {true,false}] [&#8211;alarm-actions ARN1,ARN2,&#8230;] [&#8211;alarm-description DESCRIPTION] [-d KEY1=VALUE1,KEY2=VALUE2,&#8230;] [&#8211;insufficient-data-actions ARN1,ARN2,&#8230;] [&#8211;ok-actions ARN1,ARN2,&#8230;] [&#8211;unit UNIT] [&#8211;show-empty-fields] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] ALARM</dd></dl>
<h2>DESCRIPTION</h2>
<p> Create or update an alarm</p>
<h3>positional arguments:</h3>
<dl>
<dt>ALARM</dt>
<dd> name of the alarm (required)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>&#8211;comparison-operator</code> {GreaterThanOrEqualToThreshold,GreaterThanThreshold,LessThanThreshold,LessThanOrEqualToThreshold}</dt>
<dd> arithmetic operator with which the comparison with the threshold will be made (required)</dd>
<dt><code>&#8211;evaluation-periods</code> COUNT</dt>
<dd> number of consecutive periods for which the value of the metric needs to be compared to the threshold (required)</dd>
<dt><code>&#8211;metric-name</code> METRIC</dt>
<dd> name for the alarm&#8217;s associated metric (required)</dd>
<dt><code>&#8211;namespace</code> NAMESPACE</dt>
<dd> namespace for the alarm&#8217;s associated metric (required)</dd>
<dt><code>&#8211;period</code> SECONDS</dt>
<dd> period over which the specified statistic is applied (required)</dd>
<dt><code>&#8211;statistic</code> {Average,Maximum,Minimum,SampleCount,Sum}</dt>
<dd> statistic on which to alarm (required)</dd>
<dt><code>&#8211;threshold</code> FLOAT</dt>
<dd> value to compare the statistic against (required)</dd>
<dt><code>&#8211;actions-enabled</code> {true,false}</dt>
<dd> whether this alarm&#8217;s actions should be executed when it changes state</dd>
<dt><code>&#8211;alarm-actions</code> ARN1,ARN2,&#8230;</dt>
<dd> ARNs of SNS topics to publish to when the alarm changes to the ALARM state</dd>
<dt><code>&#8211;alarm-description</code> DESCRIPTION</dt>
<dd> description of the alarm</dd>
<dt><code>-d</code> KEY1=VALUE1,KEY2=VALUE2,&#8230;, <code>&#8211;dimensions</code> KEY1=VALUE1,KEY2=VALUE2,&#8230;</dt>
<dd> dimensions for the alarm&#8217;s associated metric</dd>
<dt><code>&#8211;insufficient-data-actions</code> ARN1,ARN2,&#8230;</dt>
<dd> ARNs of SNS topics to publish to when the alarm changes to the INSUFFICIENT_DATA state</dd>
<dt><code>&#8211;ok-actions</code> ARN1,ARN2,&#8230;</dt>
<dd> ARNs of SNS topics to publish to when the alarm changes to the OK state</dd>
<dt><code>&#8211;unit</code> UNIT</dt>
<dd> unit for the alarm&#8217;s associated metric</dd>
<dt><code>&#8211;show-empty-fields</code></dt>
<dd> show empty values as &quot;(nil)&quot;</dd>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</dt>
<dd> instance monitoring service endpoint URL</dd>
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
