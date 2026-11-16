---
title: "euimage-install-pack(1)"
name: "euimage-install-pack"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euimage-install-pack/"
description: "euimage-install-pack – ***TECH PREVIEW***"
---

<h2>NAME</h2>
<p> euimage-install-pack &#8211; ***TECH PREVIEW***</p>
<h2>SYNOPSIS</h2>
<p> euimage-install-pack [&#8211;profile PROFILE] [-b BUCKET[/PREFIX]]</p>
<dl>
<dt>[&#8211;location LOCATION] [&#8211;privatekey FILE]</dt>
<dd> [&#8211;cert FILE] [&#8211;ec2cert FILE] [&#8211;user ACCOUNT] [&#8211;kernel IMAGE] [&#8211;ramdisk IMAGE] [&#8211;ec2-url EC2_URL] [&#8211;progress | <code>&#8211;no-progress]</code> [&#8211;show-empty-fields] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] FILE</dd></dl>
<h2>DESCRIPTION</h2>
<p> ***TECH PREVIEW***</p>
<h2>DESCRIPTION</h2>
<p> Install a packed image into the cloud</p>
<h3>positional arguments:</h3>
<dl>
<dt>FILE</dt>
<dd> the pack to install (required)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>&#8211;profile</code> PROFILE</dt>
<dd> which of the image&#8217;s profiles to install (default: &quot;default&quot;)</dd>
<dt><code>-b</code> BUCKET[/PREFIX], <code>&#8211;bucket</code> BUCKET[/PREFIX]</dt>
<dd> bucket to upload the image to (required)</dd>
<dt><code>&#8211;location</code> LOCATION</dt>
<dd> location constraint of the destination bucket (default: inferred from s3-location-constraint in configuration, or otherwise none</dd>
<dt><code>&#8211;privatekey</code> FILE</dt>
<dd> file containing your private key to sign the bundle&#8217;s manifest with. This private key will also be required to unbundle the bundle in the future. (instance-store only)</dd>
<dt><code>&#8211;cert</code> FILE</dt>
<dd> file containing your X.509 certificate (instance-store only)</dd>
<dt><code>&#8211;ec2cert</code> FILE</dt>
<dd> file containing the cloud&#8217;s X.509 certificate (instance-store only)</dd>
<dt><code>&#8211;user</code> ACCOUNT</dt>
<dd> your account ID (instance-store only)</dd>
<dt><code>&#8211;kernel</code> IMAGE</dt>
<dd> ID of the kernel image to associate with this machine image (paravirtual only)</dd>
<dt><code>&#8211;ramdisk</code> IMAGE</dt>
<dd> ID of the ramdisk image to associate with this machine image (paravirtual only)</dd>
<dt><code>&#8211;ec2-url</code> EC2_URL</dt>
<dd> compute service endpoint URL</dd>
<dt><code>&#8211;progress</code></dt>
<dd> show progress (the default when run interactively)</dd>
<dt><code>&#8211;no-progress</code></dt>
<dd> do not show progress (the default when run noninteractively)</dd>
<dt><code>&#8211;show-empty-fields</code></dt>
<dd> show empty values as &quot;(nil)&quot;</dd>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</dt>
<dd> object storage service endpoint URL</dd>
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
<h2>Index</h2>
