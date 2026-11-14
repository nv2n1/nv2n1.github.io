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
<h2>SYNOPSIS</h2>
<p> euca-bundle-instance <code>-b</code> BUCKET <code>-p</code> PREFIX [-o KEY-ID] [-c POLICY]</p>
<dl>
<dt>[-s SIGNATURE] [-w KEY] [-x HOURS]</p>
<dd> [&#8211;show-empty-fields] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] INSTANCE</dl>
<h2>DESCRIPTION</h2>
<p> Bundle an S3-backed Windows instance</p>
<h3>positional arguments:</h3>
<dl>
<dt>INSTANCE</p>
<dd> ID of the instance to bundle (required)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-b</code> BUCKET, <code>&#8211;bucket</code> BUCKET</p>
<dd> bucket in which to store the new machine image (required)</p>
<dt><code>-p</code> PREFIX, <code>&#8211;prefix</code> PREFIX</p>
<dd> beginning of the machine image bundle name (required)</p>
<dt><code>-o</code> KEY-ID, <code>&#8211;owner-akid</code> KEY-ID, <code>&#8211;user-access-key</code> KEY-ID</p>
<dd> bucket owner&#8217;s access key ID (required if not specified in configuration)</p>
<dt><code>-c</code> POLICY, <code>&#8211;policy</code> POLICY</p>
<dd> Base64-encoded upload policy that allows the server to upload a bundle on your behalf. If unused, a secret key is required.</p>
<dt><code>-s</code> SIGNATURE, <code>&#8211;policy-signature</code> SIGNATURE</p>
<dd> signature of the Base64-encoded upload policy. If unused, a secret key is required.</p>
<dt><code>-w</code> KEY, <code>&#8211;owner-sak</code> KEY, <code>&#8211;user-secret-key</code> KEY</p>
<dd> bucket owner&#8217;s secret access key, used to sign upload policies. This is required unless both <code>-c</code> and <code>-s</code> are used or if a secret key is specified in a configuration file.</p>
<dt><code>-x</code> HOURS, <code>&#8211;expires</code> HOURS</p>
<dd> generated upload policy expiration time (default: 24)</p>
<dt><code>&#8211;show-empty-fields</code></p>
<dd> show empty values as &quot;(nil)&quot;</p>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</p>
<dd> compute service endpoint URL</p>
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
