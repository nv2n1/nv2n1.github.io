---
title: "euca-upload-bundle(1)"
name: "euca-upload-bundle"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-upload-bundle/"
description: "euca-upload-bundle – Upload a bundle prepared by euca-bundle-image to the cloud"
---

<h2>NAME</h2>
<p> euca-upload-bundle &#8211; Upload a bundle prepared by euca-bundle-image to the cloud</p>
<h2>SYNOPSIS</h2>
<p> euca-upload-bundle <code>-m</code> FILE [-d DIR] [&#8211;skipmanifest] <code>-b</code> BUCKET[/PREFIX]</p>
<dl>
<dt>[&#8211;acl {public-read,aws-exec-read,ec2-bundle-read}]</p>
<dd> [&#8211;upload-policy POLICY | <code>&#8211;upload-policy-file</code> FILE] [&#8211;upload-policy-signature SIGNATURE] [&#8211;location LOCATION] [&#8211;retry] [&#8211;progress | <code>&#8211;no-progress]</code> [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h]</dl>
<h2>DESCRIPTION</h2>
<p> Upload a bundle prepared by euca-bundle-image to the cloud</p>
<h3>optional arguments:</h3>
<dl>
<dt><code>-m</code> FILE, <code>&#8211;manifest</code> FILE</p>
<dd> manifest for the bundle to upload (required)</p>
<dt><code>-d</code> DIR, <code>&#8211;directory</code> DIR</p>
<dd> directory that contains the bundle parts (default: directory that contains the manifest)</p>
<dt><code>&#8211;skipmanifest</code></p>
<dd> do not upload the manifest</p>
<dt><code>-b</code> BUCKET[/PREFIX], <code>&#8211;bucket</code> BUCKET[/PREFIX]</p>
<dd> bucket to upload the bundle to (required)</p>
<dt><code>&#8211;acl</code> {public-read,aws-exec-read,ec2-bundle-read}</p>
<dd> canned ACL policy to apply to the bundle (default: aws-exec-read)</p>
<dt><code>&#8211;upload-policy</code> POLICY</p>
<dd> upload policy to use for authorization</p>
<dt><code>&#8211;upload-policy-file</code> FILE</p>
<dd> file containing an upload policy to use for authorization</p>
<dt><code>&#8211;upload-policy-signature</code> SIGNATURE</p>
<dd> signature for the upload policy (required when an &#8216;upload policy is used)</p>
<dt><code>&#8211;location</code> LOCATION</p>
<dd> location constraint of the destination bucket (default: inferred from s3-location-constraint in configuration, or otherwise none)</p>
<dt><code>&#8211;retry</code></p>
<dd> retry failed uploads up to 5 times</p>
<dt><code>&#8211;progress</code></p>
<dd> show progress (the default when run interactively)</p>
<dt><code>&#8211;no-progress</code></p>
<dd> do not show progress (the default when run noninteractively)</p>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</p>
<dd> object storage service endpoint URL</p>
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
