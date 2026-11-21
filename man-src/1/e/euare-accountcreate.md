---

title: "euare-accountcreate(1)"
name: "euare-accountcreate"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euare-accountcreate/"
description: "euare-accountcreate – [Eucalyptus cloud admin only] Create a new account"
---

<h2>NAME</h2>
<p> euare-accountcreate &#8211; [Eucalyptus cloud admin only] Create a new account</p>
<p> euare-accountcreate [-k] [-w] [-d DOMAIN] [-l] [&#8211;show-empty-fields]</p>
<dl>
<dt>[-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID]</dt>
<dd> [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] [ACCOUNT]</dd></dl>
<p> [Eucalyptus cloud admin only] Create a new account</p>
<h3>positional arguments:</h3>
<dl>
<dt>ACCOUNT</dt>
<dd> also add an alias (name) to the new account (required on eucalyptus &lt; 4.2)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-k</code>, <code>&#8211;create-accesskey</code></dt>
<dd> also create an access key for the new account&#8217;s administrator and show it</dd>
<dt><code>-w</code>, <code>&#8211;write-config</code></dt>
<dd> output access keys and region information in the form of a euca2ools.ini(5) configuration file instead of by themselves (implies <code>-k</code>)</dd>
<dt><code>-d</code> DOMAIN, <code>&#8211;domain</code> DOMAIN</dt>
<dd> the DNS domain to use for region information in configuration file output (default: based on IAM URL)</dd>
<dt><code>-l</code>, <code>&#8211;set-default-user</code></dt>
<dd> set this user as the default user for the region in euca2ools.ini(5) configuration file output. This option is only useful when used with <code>-w</code>.</dd>
<dt><code>&#8211;show-empty-fields</code></dt>
<dd> show empty values as &quot;(nil)&quot;</dd>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</dt>
<dd> identity service endpoint URL</dd>
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
