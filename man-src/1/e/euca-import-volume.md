---

title: "euca-import-volume(1)"
name: "euca-import-volume"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-import-volume/"
description: "euca-import-volume – Import a file to a volume in the cloud"
---

<p> euca-import-volume &#8211; Import a file to a volume in the cloud</p>
<h2>SYNOPSIS</h2>
<p> euca-import-volume <code>-f</code> FORMAT <code>-z</code> ZONE [-s GiB] [&#8211;image-size BYTES]</p>
<dl>
<dt>(<code>-b</code> BUCKET | <code>&#8211;manifest-url</code> URL) [&#8211;prefix PREFIX]</dt>
<dd> [-x DAYS] [&#8211;no-upload] [-d DESCRIPTION] [&#8211;show-empty-fields] [&#8211;s3-url URL] [-o KEY_ID] [-w KEY] [&#8211;progress | <code>&#8211;no-progress]</code> [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] FILE</dd></dl>
<h2>DESCRIPTION</h2>
<p> Import a file to a volume in the cloud</p>
<h3>positional arguments:</h3>
<dl>
<dt>FILE</dt>
<dd> file containing the disk image to import (required)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-f</code> FORMAT, <code>&#8211;format</code> FORMAT</dt>
<dd> the image&#8217;s format (&quot;vmdk&quot;, &quot;raw&quot;, or &quot;vhd&quot;) (required)</dd>
<dt><code>-z</code> ZONE, <code>&#8211;availability-zone</code> ZONE</dt>
<dd> the zone in which to create the volume (required)</dd>
<dt><code>-s</code> GiB, <code>&#8211;volume-size</code> GiB</dt>
<dd> size of the volume to import to, in GiB</dd>
<dt><code>&#8211;image-size</code> BYTES</dt>
<dd> size of the image (required for non-raw files</dd>
<dt><code>-b</code> BUCKET, <code>&#8211;bucket</code> BUCKET</dt>
<dd> the bucket to upload the volume to</dd>
<dt><code>&#8211;manifest-url</code> URL</dt>
<dd> a pre-signed URL that points to the import manifest to use</dd>
<dt><code>&#8211;prefix</code> PREFIX</dt>
<dd> a prefix to add to the names of the volume parts as they are uploaded</dd>
<dt><code>-x</code> DAYS, <code>&#8211;expires</code> DAYS</dt>
<dd> how long the import manifest should remain valid, in days (default: 30 days)</dd>
<dt><code>&#8211;no-upload</code></dt>
<dd> start the import process, but do not actually upload the volume (see euca-resume-import)</dd>
<dt><code>-d</code> DESCRIPTION, <code>&#8211;description</code> DESCRIPTION</dt>
<dd> a description for the import task (not the volume)</dd>
<dt><code>&#8211;show-empty-fields</code></dt>
<dd> show empty values as &quot;(nil)&quot;</dd>
<dt><code>&#8211;s3-url</code> URL</dt>
<dd> object storage service endpoint URL</dd>
<dt><code>-o</code> KEY_ID, <code>&#8211;owner-akid</code> KEY_ID</dt>
<dd> access key to use for the object storage service (default: same as that for the compute service)</dd>
<dt><code>-w</code> KEY, <code>&#8211;owner-sak</code> KEY</dt>
<dd> secret key to use for the object storage service (default: same as that for the compute service)</dd>
<dt><code>&#8211;progress</code></dt>
<dd> show progress (the default when run interactively)</dd>
<dt><code>&#8211;no-progress</code></dt>
<dd> do not show progress (the default when run noninteractively)</dd>
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
