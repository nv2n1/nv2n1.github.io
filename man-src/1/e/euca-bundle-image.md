---
title: "euca-bundle-image(1)"
name: "euca-bundle-image"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-bundle-image/"
description: "euca-bundle-image – Prepare an image for use in the cloud"
---

<h2>NAME</h2>
<p> euca-bundle-image &#8211; Prepare an image for use in the cloud</p>
<h2>SYNOPSIS</h2>
<p> euca-bundle-image [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] <code>-i</code> FILE</p>
<dl>
<dt>[-p PREFIX] [-d DIR] <code>-r</code></dt>
<dd> {i386,x86_64,armhf,ppc,ppc64,ppc64le} [-k FILE] [-c FILE] [&#8211;ec2cert FILE] [-u ACCOUNT] [&#8211;kernel IMAGE] [&#8211;ramdisk IMAGE] [&#8211;bootstrap-url BOOTSTRAP_URL] [-B VIRTUAL1=DEVICE1,VIRTUAL2=DEVICE2,&#8230;] [&#8211;productcodes CODE1,CODE2,&#8230;] [&#8211;image-size IMAGE_SIZE] [&#8211;progress | <code>&#8211;no-progress]</code> [&#8211;region USER [at] REGION] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h]</dd></dl>
<h2>DESCRIPTION</h2>
<p> Prepare an image for use in the cloud</p>
<h3>optional arguments:</h3>
<dl>
<dt> <code>-I</code> KEY_ID, <code>&#8211;access-key-id</code> KEY_ID</dt>
<dt> <code>-S</code> KEY, <code>&#8211;secret-key</code> KEY</dt>
<dt> <code>&#8211;security-token</code> TOKEN</dt>
<dt><code>-i</code> FILE, <code>&#8211;image</code> FILE</dt>
<dd>
</dd><dd>file containing the image to bundle (required)</dd>
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
<dt><code>&#8211;progress</code></dt>
<dd> show progress (the default when run interactively)</dd>
<dt><code>&#8211;no-progress</code></dt>
<dd> do not show progress (the default when run noninteractively)</dd>
<dt><code>&#8211;region</code> USER [at] REGION</dt>
<dd> region and/or user names to search when looking up config file data</dd>
<dt><code>&#8211;debug</code></dt>
<dd> show debugging output</dd>
<dt><code>&#8211;debugger</code></dt>
<dd> launch interactive debugger on error</dd>
<dt><code>&#8211;version</code></dt>
<dd> show the program&#8217;s version and exit</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> show this help message and exit </dd>
</dl>
<h2>Index</h2>
