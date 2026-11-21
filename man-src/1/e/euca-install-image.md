---

title: "euca-install-image(1)"
name: "euca-install-image"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-install-image/"
description: "euca-install-image – Bundle, upload and register an image into the cloud"
---

<h2>NAME</h2>
<p> euca-install-image &#8211; Bundle, upload and register an image into the cloud</p>
<p> euca-install-image <code>-n</code> NAME [&#8211;description DESCRIPTION]</p>
<dl>
<dt>[&#8211;max-pending-parts MAX_PENDING_PARTS]</dt>
<dd> [&#8211;virtualization-type {paravirtual,hvm}] [&#8211;platform windows] [&#8211;ec2-url EC2_URL] <code>-i</code> FILE [-p PREFIX] [-d DIR] <code>-r</code> {i386,x86_64,armhf,ppc,ppc64,ppc64le} [-k FILE] [-c FILE] [&#8211;ec2cert FILE] [-u ACCOUNT] [&#8211;kernel IMAGE] [&#8211;ramdisk IMAGE] [&#8211;bootstrap-url BOOTSTRAP_URL] [-B VIRTUAL1=DEVICE1,VIRTUAL2=DEVICE2,&#8230;] [&#8211;productcodes CODE1,CODE2,&#8230;] [&#8211;image-size IMAGE_SIZE] <code>-b</code> BUCKET[/PREFIX] [&#8211;acl {public-read,aws-exec-read,ec2-bundle-read}] [&#8211;upload-policy POLICY | <code>&#8211;upload-policy-file</code> FILE] [&#8211;upload-policy-signature SIGNATURE] [&#8211;location LOCATION] [&#8211;retry] [&#8211;progress | <code>&#8211;no-progress]</code> [&#8211;show-empty-fields] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h]</dd></dl>
<p> Bundle, upload and register an image into the cloud</p>
<h3>optional arguments:</h3>
<dl>
<dt><code>-n</code> NAME, <code>&#8211;name</code> NAME</dt>
<dd> name of the new image (required)</dd>
<dt><code>&#8211;description</code> DESCRIPTION</dt>
<dd> description of the new image</dd>
<dt><code>&#8211;max-pending-parts</code> MAX_PENDING_PARTS</dt>
<dd> pause the bundling process when more than this number of parts are waiting to be uploaded (default: 2)</dd>
<dt><code>&#8211;virtualization-type</code> {paravirtual,hvm}</dt>
<dd> virtualization type for the new image</dd>
<dt><code>&#8211;platform</code> windows</dt>
<dd> [Privileged] the new image&#8217;s platform (windows)</dd>
<dt><code>&#8211;ec2-url</code> EC2_URL</dt>
<dd> compute service endpoint URL</dd>
<dt><code>-i</code> FILE, <code>&#8211;image</code> FILE</dt>
<dd> file containing the image to bundle (required)</dd>
<dt><code>-p</code> PREFIX, <code>&#8211;prefix</code> PREFIX</dt>
<dd> the file name prefix to give the bundle&#8217;s files (required when bundling stdin; otherwise defaults to the image&#8217;s file name)</dd>
<dt><code>-d</code> DIR, <code>&#8211;destination</code> DIR</dt>
<dd> location to place the bundle&#8217;s files (default: dir named by TMPDIR, TEMP, or TMP environment variables, or otherwise <i>,/var/tmp/</i>)</dd>
<dt><code>-r</code> {i386,x86_64,armhf,ppc,ppc64,ppc64le}, <code>&#8211;arch</code> {i386,x86_64,armhf,ppc,ppc64,ppc64le}</dt>
<dd> the image&#8217;s architecture (required)</dd>
<dt><code>-k</code> FILE, <code>&#8211;privatekey</code> FILE</dt>
<dd> file containing your private key to sign the bundle&#8217;s manifest with. If one is not available the bundle will not be signed.</dd>
<dt><code>-c</code> FILE, <code>&#8211;cert</code> FILE</dt>
<dd> file containing your X.509 certificate. If one is not available it will not be possible to unbundle the bundle without cloud administrator assistance.</dd>
<dt><code>&#8211;ec2cert</code> FILE</dt>
<dd> file containing the cloud&#8217;s X.509 certificate. If one is not available locally it must be available from the bootstrap service.</dd>
<dt><code>-u</code> ACCOUNT, <code>&#8211;user</code> ACCOUNT</dt>
<dd> your account ID</dd>
<dt><code>&#8211;kernel</code> IMAGE</dt>
<dd> ID of the kernel image to associate with this machine image</dd>
<dt><code>&#8211;ramdisk</code> IMAGE</dt>
<dd> ID of the ramdisk image to associate with this machine image</dd>
<dt><code>&#8211;bootstrap-url</code> BOOTSTRAP_URL</dt>
<dd> [Eucalyptus only] bootstrap service endpoint URL (used for obtaining <code>&#8211;ec2cert</code> automatically</dd>
<dt><code>-B</code> VIRTUAL1=DEVICE1,VIRTUAL2=DEVICE2,&#8230;, <code>&#8211;block-device-mappings</code> VIRTUAL1=DEVICE1,VIRTUAL2=DEVICE2,&#8230;</dt>
<dd> block device mapping scheme with which to launch instances of this machine image</dd>
<dt><code>&#8211;productcodes</code> CODE1,CODE2,&#8230;</dt>
<dd> comma-separated list of product codes for the image</dd>
<dt><code>&#8211;image-size</code> IMAGE_SIZE</dt>
<dd> the image&#8217;s size (required when bundling stdin)</dd>
<dt><code>-b</code> BUCKET[/PREFIX], <code>&#8211;bucket</code> BUCKET[/PREFIX]</dt>
<dd> bucket to upload the bundle to (required)</dd>
<dt><code>&#8211;acl</code> {public-read,aws-exec-read,ec2-bundle-read}</dt>
<dd> canned ACL policy to apply to the bundle (default: aws-exec-read)</dd>
<dt><code>&#8211;upload-policy</code> POLICY</dt>
<dd> upload policy to use for authorization</dd>
<dt><code>&#8211;upload-policy-file</code> FILE</dt>
<dd> file containing an upload policy to use for authorization</dd>
<dt><code>&#8211;upload-policy-signature</code> SIGNATURE</dt>
<dd> signature for the upload policy (required when an &#8216;upload policy is used)</dd>
<dt><code>&#8211;location</code> LOCATION</dt>
<dd> location constraint of the destination bucket (default: inferred from s3-location-constraint in configuration, or otherwise none)</dd>
<dt><code>&#8211;retry</code></dt>
<dd> retry failed uploads up to 5 times</dd>
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
