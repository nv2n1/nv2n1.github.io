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
<dt>[&#8211;show-empty-fields] [-U URL]</p>
<dd> [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;filter NAME=VALUE] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] [IMAGE [IMAGE &#8230;]]</dl>
<h2>DESCRIPTION</h2>
<p> Show information about images</p>
<h2>DESCRIPTION</h2>
<p> By default, only images your account owns and images for which your account has explicit launch permissions are shown.</p>
<h3>positional arguments:</h3>
<dl>
<dt>IMAGE</p>
<dd> limit results to specific images</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-a</code>, <code>&#8211;all</code></p>
<dd> describe all images</p>
<dt><code>-o</code> ACCOUNT, <code>&#8211;owner</code> ACCOUNT</p>
<dd> describe images owned by the specified owner</p>
<dt><code>-x</code> ACCOUNT, <code>&#8211;executable-by</code> ACCOUNT</p>
<dd> describe images for which the specified account has explicit launch permissions</p>
<dt><code>&#8211;show-empty-fields</code></p>
<dd> show empty values as &quot;(nil)&quot;</p>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</p>
<dd> compute service endpoint URL</p>
<dt><code>&#8211;region</code> USER [at] REGION</p>
<dd> region and/or user names to search when looking up config file data</p>
<dt> <code>-I</code> KEY_ID, <code>&#8211;access-key-id</code> KEY_ID</p>
<dt> <code>-S</code> KEY, <code>&#8211;secret-key</code> KEY</p>
<dt> <code>&#8211;security-token</code> TOKEN</p>
<dt><code>&#8211;filter</code> NAME=VALUE</p>
<dd>
<dd>restrict results to those that meet criteria</p>
<dt><code>&#8211;debug</code></p>
<dd> show debugging output</p>
<dt><code>&#8211;debugger</code></p>
<dd> launch interactive debugger on error</p>
<dt><code>&#8211;version</code></p>
<dd> show the program&#8217;s version and exit</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> show this help message and exit</dl>
<h3>allowed filter names:</h3>
<dl>
<dt>architecture</p>
<dd> CPU architecture</p>
<dt>block-device-mapping.delete-on-termination</p>
<dd> whether a volume is deleted upon instance termination</p>
<dt>block-device-mapping.device-name</p>
<dd> device name for a volume mapped to the image</p>
<dt>block-device-mapping.snapshot-id</p>
<dd> snapshot ID for a volume mapped to the image</p>
<dt>block-device-mapping.volume-size</p>
<dd> volume size for a volume mapped to the image</p>
<dt>block-device-mapping.volume-type</p>
<dd> volume type for a volume mapped to the image</p>
<dt>description</p>
<dd> image description</p>
<dt>hypervisor</p>
<dd> image&#8217;s hypervisor type image-id image-type image type (&quot;machine&quot;, &quot;kernel&quot;, or &quot;ramdisk&quot;) is-public whether the image is public kernel-id manifest-location name owner-alias image owner&#8217;s account alias owner-id image owner&#8217;s account ID platform &quot;windows&quot; for Windows images product-code product code associated with the image product-code.type type of product code associated with the image (&quot;devpay&quot;, &quot;marketplace&quot;) ramdisk-id root-device-name root-device-type root device type (&quot;ebs&quot; or &quot;instance-store&quot;) state image state (&quot;available&quot;, &quot;pending&quot;, or &quot;failed&quot;)</p>
<dt>state-reason-code</p>
<dd> reason code for the most recent state change</p>
<dt>state-reason-message</p>
<dd> message for the most recent state change</p>
<dt>tag-key</p>
<dd> key of a tag assigned to the image</p>
<dt>tag-value</p>
<dd> value of a tag assigned to the image</p>
<dt>tag:KEY</p>
<dd> specific tag key/value combination</p>
<dt>virtualization-type</p>
<dd> virtualization type (&quot;paravirtual&quot; or &quot;hvm&quot;) </p>
</dl>
<h2>Index</h2>
