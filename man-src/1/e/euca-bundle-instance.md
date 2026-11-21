---

title: "euca-bundle-instance(1)"
name: "euca-bundle-instance"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-bundle-instance/"
description: "euca-bundle-instance – Bundle an S3-backed Windows instance"
---

<h2>NAME</h2>
<p> euca-bundle-instance &#8211; Bundle an S3-backed Windows instance</p>
<p> euca-bundle-instance <code>-b</code> BUCKET <code>-p</code> PREFIX [-o KEY-ID] [-c POLICY]</p>
<dl>
<dt>[-s SIGNATURE] [-w KEY] [-x HOURS]</dt>
<dd> [&#8211;show-empty-fields] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] INSTANCE</dd></dl>
<p> Bundle an S3-backed Windows instance</p>
<h3>positional arguments:</h3>
<dl>
<dt>INSTANCE</dt>
<dd> ID of the instance to bundle (required)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-b</code> BUCKET, <code>&#8211;bucket</code> BUCKET</dt>
<dd> bucket in which to store the new machine image (required)</dd>
<dt><code>-p</code> PREFIX, <code>&#8211;prefix</code> PREFIX</dt>
<dd> beginning of the machine image bundle name (required)</dd>
<dt><code>-o</code> KEY-ID, <code>&#8211;owner-akid</code> KEY-ID, <code>&#8211;user-access-key</code> KEY-ID</dt>
<dd> bucket owner&#8217;s access key ID (required if not specified in configuration)</dd>
<dt><code>-c</code> POLICY, <code>&#8211;policy</code> POLICY</dt>
<dd> Base64-encoded upload policy that allows the server to upload a bundle on your behalf. If unused, a secret key is required.</dd>
<dt><code>-s</code> SIGNATURE, <code>&#8211;policy-signature</code> SIGNATURE</dt>
<dd> signature of the Base64-encoded upload policy. If unused, a secret key is required.</dd>
<dt><code>-w</code> KEY, <code>&#8211;owner-sak</code> KEY, <code>&#8211;user-secret-key</code> KEY</dt>
<dd> bucket owner&#8217;s secret access key, used to sign upload policies. This is required unless both <code>-c</code> and <code>-s</code> are used or if a secret key is specified in a configuration file.</dd>
<dt><code>-x</code> HOURS, <code>&#8211;expires</code> HOURS</dt>
<dd> generated upload policy expiration time (default: 24)</dd>
<dt><code>&#8211;show-empty-fields</code></dt>
<dd> show empty values as &quot;(nil)&quot;</dd>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</dt>
<dd> compute service endpoint URL</dd>
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
