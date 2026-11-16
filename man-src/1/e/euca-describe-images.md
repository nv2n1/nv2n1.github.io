---
title: "euca-describe-images(1)"
name: "euca-describe-images"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-describe-images/"
description: "euca-describe-images – Show information about images"
---

<h2>NAME</h2>
<p> euca-describe-images &#8211; Show information about images</p>
<h2>SYNOPSIS</h2>
<p> euca-describe-images [-a] [-o ACCOUNT] [-x ACCOUNT]</p>
<dl>
<dt>[&#8211;show-empty-fields] [-U URL]</dt>
<dd> [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;filter NAME=VALUE] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] [IMAGE [IMAGE &#8230;]]</dd></dl>
<h2>DESCRIPTION</h2>
<p> Show information about images</p>
<h2>DESCRIPTION</h2>
<p> By default, only images your account owns and images for which your account has explicit launch permissions are shown.</p>
<h3>positional arguments:</h3>
<dl>
<dt>IMAGE</dt>
<dd> limit results to specific images</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-a</code>, <code>&#8211;all</code></dt>
<dd> describe all images</dd>
<dt><code>-o</code> ACCOUNT, <code>&#8211;owner</code> ACCOUNT</dt>
<dd> describe images owned by the specified owner</dd>
<dt><code>-x</code> ACCOUNT, <code>&#8211;executable-by</code> ACCOUNT</dt>
<dd> describe images for which the specified account has explicit launch permissions</dd>
<dt><code>&#8211;show-empty-fields</code></dt>
<dd> show empty values as &quot;(nil)&quot;</dd>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</dt>
<dd> compute service endpoint URL</dd>
<dt><code>&#8211;region</code> USER [at] REGION</dt>
<dd> region and/or user names to search when looking up config file data</dd>
<dt> <code>-I</code> KEY_ID, <code>&#8211;access-key-id</code> KEY_ID</dt>
<dt> <code>-S</code> KEY, <code>&#8211;secret-key</code> KEY</dt>
<dt> <code>&#8211;security-token</code> TOKEN</dt>
<dt><code>&#8211;filter</code> NAME=VALUE</dt>
<dd>
</dd><dd>restrict results to those that meet criteria</dd>
<dt><code>&#8211;debug</code></dt>
<dd> show debugging output</dd>
<dt><code>&#8211;debugger</code></dt>
<dd> launch interactive debugger on error</dd>
<dt><code>&#8211;version</code></dt>
<dd> show the program&#8217;s version and exit</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> show this help message and exit</dd></dl>
<h3>allowed filter names:</h3>
<dl>
<dt>architecture</dt>
<dd> CPU architecture</dd>
<dt>block-device-mapping.delete-on-termination</dt>
<dd> whether a volume is deleted upon instance termination</dd>
<dt>block-device-mapping.device-name</dt>
<dd> device name for a volume mapped to the image</dd>
<dt>block-device-mapping.snapshot-id</dt>
<dd> snapshot ID for a volume mapped to the image</dd>
<dt>block-device-mapping.volume-size</dt>
<dd> volume size for a volume mapped to the image</dd>
<dt>block-device-mapping.volume-type</dt>
<dd> volume type for a volume mapped to the image</dd>
<dt>description</dt>
<dd> image description</dd>
<dt>hypervisor</dt>
<dd> image&#8217;s hypervisor type image-id image-type image type (&quot;machine&quot;, &quot;kernel&quot;, or &quot;ramdisk&quot;) is-public whether the image is public kernel-id manifest-location name owner-alias image owner&#8217;s account alias owner-id image owner&#8217;s account ID platform &quot;windows&quot; for Windows images product-code product code associated with the image product-code.type type of product code associated with the image (&quot;devpay&quot;, &quot;marketplace&quot;) ramdisk-id root-device-name root-device-type root device type (&quot;ebs&quot; or &quot;instance-store&quot;) state image state (&quot;available&quot;, &quot;pending&quot;, or &quot;failed&quot;)</dd>
<dt>state-reason-code</dt>
<dd> reason code for the most recent state change</dd>
<dt>state-reason-message</dt>
<dd> message for the most recent state change</dd>
<dt>tag-key</dt>
<dd> key of a tag assigned to the image</dd>
<dt>tag-value</dt>
<dd> value of a tag assigned to the image</dd>
<dt>tag:KEY</dt>
<dd> specific tag key/value combination</dd>
<dt>virtualization-type</dt>
<dd> virtualization type (&quot;paravirtual&quot; or &quot;hvm&quot;) </dd>
</dl>
<h2>Index</h2>
