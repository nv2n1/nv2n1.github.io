---

title: "euform-create-stack(1)"
name: "euform-create-stack"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euform-create-stack/"
description: "euform-create-stack – Create a new stack"
---

<h2>NAME</h2>
<p> euform-create-stack &#8211; Create a new stack</p>
<p> euform-create-stack (<code>&#8211;template-file</code> FILE | <code>&#8211;template-url</code> URL) [-d]</p>
<dl>
<dt>[-n ARN[,&#8230;]] [&#8211;capabilities CAP[,&#8230;]]</dt>
<dd> [-p KEY=VALUE] [-t MINUTES] [&#8211;tag KEY[=VALUE]] [&#8211;show-empty-fields] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] STACK</dd></dl>
<p> Create a new stack</p>
<h3>positional arguments:</h3>
<dl>
<dt>STACK</dt>
<dd> name of the new stack (required)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>&#8211;template-file</code> FILE</dt>
<dd> file containing the new stack&#8217;s JSON template</dd>
<dt><code>&#8211;template-url</code> URL</dt>
<dd> URL pointing to the new stack&#8217;s JSON template</dd>
<dt><code>-d</code>, <code>&#8211;disable-rollback</code></dt>
<dd> disable rollback on failure</dd>
<dt><code>-n</code> ARN[,&#8230;], <code>&#8211;notification-arns</code> ARN[,&#8230;]</dt>
<dd> SNS ARNs to publish stack actions to</dd>
<dt><code>&#8211;capabilities</code> CAP[,&#8230;]</dt>
<dd> capabilities needed to create the stack</dd>
<dt><code>-p</code> KEY=VALUE, <code>&#8211;parameter</code> KEY=VALUE</dt>
<dd> key and value of the parameters to use with the new stack&#8217;s template, separated by an &quot;=&quot; character</dd>
<dt><code>-t</code> MINUTES, <code>&#8211;timeout</code> MINUTES</dt>
<dd> timeout for stack creation</dd>
<dt><code>&#8211;tag</code> KEY[=VALUE]</dt>
<dd> key and optional value of the tag to create, separated by an &quot;=&quot; character. If no value is given the tag&#8217;s value is set to an empty string.</dd>
<dt><code>&#8211;show-empty-fields</code></dt>
<dd> show empty values as &quot;(nil)&quot;</dd>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</dt>
<dd> deployment templating service endpoint URL</dd>
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
