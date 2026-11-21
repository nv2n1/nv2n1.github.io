---

title: "euform-update-stack(1)"
name: "euform-update-stack"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euform-update-stack/"
description: "euform-update-stack – Update a stack’s template, parameters, or capabilities"
---

<h2>NAME</h2>
<p> euform-update-stack &#8211; Update a stack&#8217;s template, parameters, or capabilities</p>
<p> euform-update-stack [&#8211;template-file FILE | <code>&#8211;template-url</code> URL]</p>
<dl>
<dt>[&#8211;capabilities CAP[,&#8230;]] [-p KEY=VALUE]</dt>
<dd> [&#8211;tag KEY[=VALUE] | <code>&#8211;delete-tags]</code> [&#8211;show-empty-fields] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] STACK</dd></dl>
<p> Update a stack&#8217;s template, parameters, or capabilities</p>
<h3>positional arguments:</h3>
<dl>
<dt>STACK</dt>
<dd> name of the stack to update (required)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>&#8211;template-file</code> FILE</dt>
<dd> file containing a new JSON template for the stack</dd>
<dt><code>&#8211;template-url</code> URL</dt>
<dd> URL pointing to a new JSON template for the stack</dd>
<dt><code>&#8211;capabilities</code> CAP[,&#8230;]</dt>
<dd> capabilities needed to update the stack</dd>
<dt><code>-p</code> KEY=VALUE, <code>&#8211;parameter</code> KEY=VALUE</dt>
<dd> key and value of the parameters to use with the stack&#8217;s template, separated by an &quot;=&quot; character</dd>
<dt><code>&#8211;tag</code> KEY[=VALUE]</dt>
<dd> key and optional value of a tag to add, separated by an &quot;=&quot; character. If no value is given the tag&#8217;s value is set to an empty string.</dd>
<dt><code>&#8211;delete-tags</code></dt>
<dd> remove all tags associated with the stack</dd>
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
