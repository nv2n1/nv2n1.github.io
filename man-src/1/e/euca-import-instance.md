---
title: "euca-import-instance(1)"
name: "euca-import-instance"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-import-instance/"
description: "euca-import-instance – Import an instance into the cloud"
---

<h2>NAME</h2>
<p> euca-import-instance &#8211; Import an instance into the cloud</p>
<h2>SYNOPSIS</h2>
<p> euca-import-instance <code>-t</code> INSTANCETYPE <code>-f</code> FORMAT <code>-a</code> ARCH <code>-p</code></p>
<dl>
<dt>{Windows,Linux} (<code>-b</code> BUCKET | <code>&#8211;manifest-url</code> URL)</p>
<dd> [&#8211;prefix PREFIX] [-x DAYS] [&#8211;no-upload] [-d DESCRIPTION] [-g GROUP] [-z ZONE] [-s GiB] [&#8211;image-size BYTES] [&#8211;user-data DATA | <code>&#8211;user-data-file</code> FILE] [&#8211;subnet SUBNET] [&#8211;private-ip-address ADDRESS] [&#8211;monitor] [&#8211;instance-initiated-shutdown-behavior {stop,terminate}] [&#8211;key KEYPAIR] [&#8211;show-empty-fields] [&#8211;s3-url URL] [-o KEY_ID] [-w KEY] [&#8211;progress | <code>&#8211;no-progress]</code> [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] FILE</dl>
<h2>DESCRIPTION</h2>
<p> Import an instance into the cloud</p>
<h3>positional arguments:</h3>
<dl>
<dt>FILE</p>
<dd> file containing the disk image to import (required)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-t</code> INSTANCETYPE, <code>&#8211;instance-type</code> INSTANCETYPE</p>
<dd> the type of instance to import to (required)</p>
<dt><code>-f</code> FORMAT, <code>&#8211;format</code> FORMAT</p>
<dd> the image&#8217;s format (&quot;vmdk&quot;, &quot;raw&quot;, or &quot;vhd&quot;) (required)</p>
<dt><code>-a</code> ARCH, <code>&#8211;architecture</code> ARCH</p>
<dd> the instance&#8217;s processor architecture (required)</p>
<dt><code>-p</code> {Windows,Linux}, <code>&#8211;platform</code> {Windows,Linux}</p>
<dd> the instance&#8217;s operating system (required)</p>
<dt><code>-b</code> BUCKET, <code>&#8211;bucket</code> BUCKET</p>
<dd> the bucket to upload the volume to</p>
<dt><code>&#8211;manifest-url</code> URL</p>
<dd> a pre-signed URL that points to the import manifest to use</p>
<dt><code>&#8211;prefix</code> PREFIX</p>
<dd> a prefix to add to the names of the volume parts as they are uploaded</p>
<dt><code>-x</code> DAYS, <code>&#8211;expires</code> DAYS</p>
<dd> how long the import manifest should remain valid, in days (default: 30 days)</p>
<dt><code>&#8211;no-upload</code></p>
<dd> start the import process, but do not actually upload the volume (see euca-resume-import)</p>
<dt><code>-d</code> DESCRIPTION, <code>&#8211;description</code> DESCRIPTION</p>
<dd> a description for the import task (not the volume)</p>
<dt><code>-g</code> GROUP, <code>&#8211;group</code> GROUP</p>
<dd> name of the security group to create the instance in</p>
<dt><code>-z</code> ZONE, <code>&#8211;availability-zone</code> ZONE</p>
<dd> the zone in which to create the instance</p>
<dt><code>-s</code> GiB, <code>&#8211;volume-size</code> GiB</p>
<dd> size of the volume to import to, in GiB</p>
<dt><code>&#8211;image-size</code> BYTES</p>
<dd> size of the image (required for non-raw files</p>
<dt><code>&#8211;user-data</code> DATA</p>
<dd> user data to supply to the instance</p>
<dt><code>&#8211;user-data-file</code> FILE</p>
<dd> file containing user data to supply to the instance</p>
<dt><code>&#8211;subnet</code> SUBNET</p>
<dd> [VPC only] subnet to create the instance&#8217;s network interface in</p>
<dt><code>&#8211;private-ip-address</code> ADDRESS</p>
<dd> [VPC only] assign a specific primary private IP address to the instance&#8217;s interface</p>
<dt><code>&#8211;monitor</code></p>
<dd> enable detailed monitoring for the instance</p>
<dt><code>&#8211;instance-initiated-shutdown-behavior</code> {stop,terminate}</p>
<dd> whether to &quot;stop&quot; (default) or terminate the instance when it shuts down</p>
<dt><code>&#8211;key</code> KEYPAIR</p>
<dd> [Eucalyptus only] name of the key pair to use when running the instance</p>
<dt><code>&#8211;show-empty-fields</code></p>
<dd> show empty values as &quot;(nil)&quot;</p>
<dt><code>&#8211;s3-url</code> URL</p>
<dd> object storage service endpoint URL</p>
<dt><code>-o</code> KEY_ID, <code>&#8211;owner-akid</code> KEY_ID</p>
<dd> access key to use for the object storage service (default: same as that for the compute service)</p>
<dt><code>-w</code> KEY, <code>&#8211;owner-sak</code> KEY</p>
<dd> secret key to use for the object storage service (default: same as that for the compute service)</p>
<dt><code>&#8211;progress</code></p>
<dd> show progress (the default when run interactively)</p>
<dt><code>&#8211;no-progress</code></p>
<dd> do not show progress (the default when run noninteractively)</p>
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
