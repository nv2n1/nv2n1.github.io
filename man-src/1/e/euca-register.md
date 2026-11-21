---
title: "euca-register(1)"
name: "euca-register"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-register/"
description: "euca-register – Register a new image"
---

<h2>NAME</h2>
<p> euca-register &#8211; Register a new image</p>
<h2>SYNOPSIS</h2>
<p> euca-register <code>-n</code> NAME [-d DESCRIPTION] [-a {i386,x86_64,armhf}]</p>
<dl>
<dt>[&#8211;kernel KERNEL] [&#8211;ramdisk RAMDISK]</dt>
<dd> [&#8211;root-device-name DEVICE] [-s SNAPSHOT] [-b DEVICE=MAPPED] [&#8211;virtualization-type {paravirtual,hvm}] [&#8211;platform windows] [&#8211;show-empty-fields] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] [MANIFEST]</dd></dl>
<h2>DESCRIPTION</h2>
<p> Register a new image</p>
<h3>positional arguments:</h3>
<dl>
<dt>MANIFEST</dt>
<dd> location of the image manifest in S3 storage (required for instance-store images)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-n</code> NAME, <code>&#8211;name</code> NAME</dt>
<dd> name of the new image (required)</dd>
<dt><code>-d</code> DESCRIPTION, <code>&#8211;description</code> DESCRIPTION</dt>
<dd> description of the new image</dd>
<dt><code>-a</code> {i386,x86_64,armhf}, <code>&#8211;architecture</code> {i386,x86_64,armhf}</dt>
<dd> CPU architecture of the new image</dd>
<dt><code>&#8211;kernel</code> KERNEL</dt>
<dd> ID of the kernel to associate with the new image</dd>
<dt><code>&#8211;ramdisk</code> RAMDISK</dt>
<dd> ID of the ramdisk to associate with the new image</dd>
<dt><code>&#8211;root-device-name</code> DEVICE</dt>
<dd> root device name (default: <i>,/dev/sda1/</i>)</dd>
<dt><code>-s</code> SNAPSHOT, <code>&#8211;snapshot</code> SNAPSHOT</dt>
<dd> snapshot to use for the root device</dd>
<dt><code>-b</code> DEVICE=MAPPED, <code>&#8211;block-device-mapping</code> DEVICE=MAPPED</dt>
<dd> define a block device mapping for the image, in the form DEVICE=MAPPED, where &quot;MAPPED&quot; is &quot;none&quot;, &quot;ephemeral(0-3)&quot;, or &quot;[SNAPID]:[GiB]:[true|false]:[standard|VOLTYPE[:IOPS]]&quot;</dd>
<dt><code>&#8211;virtualization-type</code> {paravirtual,hvm}</dt>
<dd> virtualization type for the new image</dd>
<dt><code>&#8211;platform</code> windows</dt>
<dd> [Privileged] the new image&#8217;s platform (windows)</dd>
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
