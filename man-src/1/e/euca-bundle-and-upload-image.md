---
title: "euca-bundle-and-upload-image(1)"
name: "euca-bundle-and-upload-image"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-bundle-and-upload-image/"
description: "euca-bundle-and-upload-image – Prepare and upload an image for use in the cloud"
---

<h2>NAME</h2>
<p> euca-bundle-and-upload-image &#8211; Prepare and upload an image for use in the cloud</p>
<h2>SYNOPSIS</h2>
<p> euca-bundle-and-upload-image [&#8211;preserve-bundle]</p>
<dl>
<dt>[&#8211;max-pending-parts MAX_PENDING_PARTS] <code>-i</code></p>
<dd> FILE [-p PREFIX] [-d DIR] <code>-r</code> {i386,x86_64,armhf,ppc,ppc64,ppc64le} [-k FILE] [-c FILE] [&#8211;ec2cert FILE] [-u ACCOUNT] [&#8211;kernel IMAGE] [&#8211;ramdisk IMAGE] [&#8211;bootstrap-url BOOTSTRAP_URL] [-B VIRTUAL1=DEVICE1,VIRTUAL2=DEVICE2,&#8230;] [&#8211;productcodes CODE1,CODE2,&#8230;] [&#8211;image-size IMAGE_SIZE] <code>-b</code> BUCKET[/PREFIX] [&#8211;acl {public-read,aws-exec-read,ec2-bundle-read}] [&#8211;upload-policy POLICY | <code>&#8211;upload-policy-file</code> FILE] [&#8211;upload-policy-signature SIGNATURE] [&#8211;location LOCATION] [&#8211;retry] [&#8211;progress | <code>&#8211;no-progress]</code> [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h]</dl>
<h2>DESCRIPTION</h2>
<p> Prepare and upload an image for use in the cloud</p>
<h3>optional arguments:</h3>
<dl>
<dt><code>&#8211;preserve-bundle</code></p>
<dd> do not delete the bundle as it is being uploaded</p>
<dt><code>&#8211;max-pending-parts</code> MAX_PENDING_PARTS</p>
<dd> pause the bundling process when more than this number of parts are waiting to be uploaded (default: 2)</p>
<dt><code>-i</code> FILE, <code>&#8211;image</code> FILE</p>
<dd> file containing the image to bundle (required)</p>
<dt><code>-p</code> PREFIX, <code>&#8211;prefix</code> PREFIX</p>
<dd> the file name prefix to give the bundle&#8217;s files (required when bundling stdin; otherwise defaults to the image&#8217;s file name)</p>
<dt><code>-d</code> DIR, <code>&#8211;destination</code> DIR</p>
<dd> location to place the bundle&#8217;s files (default: dir named by TMPDIR, TEMP, or TMP environment variables, or otherwise <i>,/var/tmp/</i>)</p>
<dt><code>-r</code> {i386,x86_64,armhf,ppc,ppc64,ppc64le}, <code>&#8211;arch</code> {i386,x86_64,armhf,ppc,ppc64,ppc64le}</p>
<dd> the image&#8217;s architecture (required)</p>
<dt><code>-k</code> FILE, <code>&#8211;privatekey</code> FILE</p>
<dd> file containing your private key to sign the bundle&#8217;s manifest with. If one is not available the bundle will not be signed.</p>
<dt><code>-c</code> FILE, <code>&#8211;cert</code> FILE</p>
<dd> file containing your X.509 certificate. If one is not available it will not be possible to unbundle the bundle without cloud administrator assistance.</p>
<dt><code>&#8211;ec2cert</code> FILE</p>
<dd> file containing the cloud&#8217;s X.509 certificate. If one is not available locally it must be available from the bootstrap service.</p>
<dt><code>-u</code> ACCOUNT, <code>&#8211;user</code> ACCOUNT</p>
<dd> your account ID</p>
<dt><code>&#8211;kernel</code> IMAGE</p>
<dd> ID of the kernel image to associate with this machine image</p>
<dt><code>&#8211;ramdisk</code> IMAGE</p>
<dd> ID of the ramdisk image to associate with this machine image</p>
<dt><code>&#8211;bootstrap-url</code> BOOTSTRAP_URL</p>
<dd> [Eucalyptus only] bootstrap service endpoint URL (used for obtaining <code>&#8211;ec2cert</code> automatically</p>
<dt><code>-B</code> VIRTUAL1=DEVICE1,VIRTUAL2=DEVICE2,&#8230;, <code>&#8211;block-device-mappings</code> VIRTUAL1=DEVICE1,VIRTUAL2=DEVICE2,&#8230;</p>
<dd> block device mapping scheme with which to launch instances of this machine image</p>
<dt><code>&#8211;productcodes</code> CODE1,CODE2,&#8230;</p>
<dd> comma-separated list of product codes for the image</p>
<dt><code>&#8211;image-size</code> IMAGE_SIZE</p>
<dd> the image&#8217;s size (required when bundling stdin)</p>
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
