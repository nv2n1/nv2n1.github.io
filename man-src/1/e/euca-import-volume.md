---
title: "euca-import-volume(1)"
name: "euca-import-volume"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-import-volume/"
description: "euca-import-volume – Import a file to a volume in the cloud"
---

<h2>NAME</h2>
<p> euca-import-volume &#8211; Import a file to a volume in the cloud</p>
<h2>SYNOPSIS</h2>
<p> euca-import-volume <code>-f</code> FORMAT <code>-z</code> ZONE [-s GiB] [&#8211;image-size BYTES]</p>
<dl>
<dt>(<code>-b</code> BUCKET | <code>&#8211;manifest-url</code> URL) [&#8211;prefix PREFIX]</p>
<dd> [-x DAYS] [&#8211;no-upload] [-d DESCRIPTION] [&#8211;show-empty-fields] [&#8211;s3-url URL] [-o KEY_ID] [-w KEY] [&#8211;progress | <code>&#8211;no-progress]</code> [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] FILE</dl>
<h2>DESCRIPTION</h2>
<p> Import a file to a volume in the cloud</p>
<h3>positional arguments:</h3>
<dl>
<dt>FILE</p>
<dd> file containing the disk image to import (required)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-f</code> FORMAT, <code>&#8211;format</code> FORMAT</p>
<dd> the image&#8217;s format (&quot;vmdk&quot;, &quot;raw&quot;, or &quot;vhd&quot;) (required)</p>
<dt><code>-z</code> ZONE, <code>&#8211;availability-zone</code> ZONE</p>
<dd> the zone in which to create the volume (required)</p>
<dt><code>-s</code> GiB, <code>&#8211;volume-size</code> GiB</p>
<dd> size of the volume to import to, in GiB</p>
<dt><code>&#8211;image-size</code> BYTES</p>
<dd> size of the image (required for non-raw files</p>
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
