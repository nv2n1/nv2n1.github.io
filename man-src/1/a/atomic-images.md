---
title: "atomic-images(1)"
name: "atomic-images"
section: "1"
letter: "a"
url: "/docs/linux/man/1-atomic-images/"
description: "atomic-images – operations on container images"
---

<h2 class="name">NAME</h2>
<p> atomic-images &#8211; operations on container images </p>
<h2>SYNOPSIS</h2>
<p> <code>atomic images COMMAND [OPTIONS] [IMAGES&#8230;]</code> </p>
<p> atomic images allows the user to view and operate on container images in a docker registry. </p>
<h2>COMMANDS</h2>
<p> <code>delete</code> </p>
<p> Delete the specified container image(s). If you use the <code>&#8211;remote option</code> remote disk space will not be freed until the <code>registry garbage-collection</code> command is invoked for the remote registry. </p>
<p> <code>generate</code><br />
&nbsp;<wbr>&nbsp;<wbr>Generates a gomtree validation manifest for all images. Gomtree is required for this feature to be available. </p>
<p> <code>help</code> </p>
<p> Displays a help file associated with a container or image. </p>
<p> If a container or image has a help file (in man format) embedded in itself, atomic help will display the help file in a pager similar to man. The default location for a help file is /image_help.1 but the location of the help can be overridden with the HELP LABEL. If you choose to override the default location, ensure the path provided is a fully-qualified path that includes the help file itself. </p>
<p> The help file can be written using the middleman markup and the converted using the go-md2man utility as follows: </p>
<dl>
<dt>
<dd>
<pre>
go-md2man -in image_help.1.md -out image_help.1
</pre>
</dl>
<p> You can also use any of the many options to create the help file including using native man tagging. </p>
<p> <code>info</code> </p>
<p> Displays the LABEL fields within an image. By default, it will check first for a local image and then all configured registries. </p>
<p> For a system container image, this will also display the environment variables a user can set. </p>
<p> <code>list</code> </p>
<p> List all installed container images on your system. </p>
<p> A <code>&gt;</code> preceding the image name indicates that the image is used by a container. </p>
<p> A * in the first column indicates a dangling image. <code>Dangling</code> images are images with no name/tag and which are not used by any other images. Since they are not used, they waste system space. Dangling images can be caused by using &#8216;docker build&#8217; to update an image without removing the older version of the image. </p>
<p> <code>prune</code> </p>
<p> Prune/delete all <code>dangling</code> images, freeing wasted disk space. </p>
<p> <code>update</code> </p>
<p> Pulls the latest update of the image from the repository. If a container based on this image exists, the container will continue to use the old image. Use &#8211;force to remove the container. </p>
<p> <code>verify</code> </p>
<p> Checks whether there is a newer image available. If the image differs, it will capture any of its relevant information like version (where applicable).<br />
&nbsp;<wbr>&nbsp;<wbr>Verify will always attempt to use the&nbsp;<wbr><code>Version</code>&nbsp;<wbr>and&nbsp;<wbr><code>Release</code>&nbsp;<wbr>labels to determine if there is a newer version.&nbsp;<wbr>&nbsp;<wbr>If that information is not<br />
&nbsp;<wbr>&nbsp;<wbr>available, then for&nbsp;<wbr>&#8216;ostree&#8217;&nbsp;<wbr>images, verify will compare using the manifest digests.&nbsp;<wbr>&nbsp;<wbr>In the case of docker images, it will use the image&#8217;s ID<br />
&nbsp;<wbr>&nbsp;<wbr>for comparison. </p>
<p> <code>version</code> </p>
<p> Display image &#8216;Id Name:Version:Release RepoTag&#8217; label </p>
<h2>delete OPTIONS</h2>
<p> [<code>-h|&#8211;help</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>Print usage statement </p>
<p> [<code>-f|&#8211;force</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>Force the deletion of specified local images, even if they are in use. </p>
<p> [<code>&#8211;remote</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>Delete images in remote registry.&nbsp;<wbr>&nbsp;<wbr><i>&#8211;force</i>&nbsp;<wbr>is not supported with this option. </p>
<p> [<code>&#8211;storage=[ostree|docker]</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>Optionally specify the storage from which to delete the image from. Will prompt user to specify if the same image name exists in both ostree and docker, and the user did not specify. </p>
<h2>Note:</h2>
<p> Atomic &#8211;assumeyes option can be used </p>
<p> [<code>-y|&#8211;assumeyes</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>Delete image(s)&nbsp;<wbr>without conformation from the user </p>
<h2>info OPTIONS</h2>
<p> [<code>-h|&#8211;help</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>Print usage statement </p>
<p> [<code>&#8211;remote</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>Ignore all local images, only search configured registries. </p>
<p> [<code>&#8211;storage=[ostree|docker]</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>Optionally specify the storage of the image. Will prompt user to specify if the same image name exists in both ostree and docker, and the user did not specify. </p>
<h2>list OPTIONS</h2>
<p> [<code>-h|&#8211;help</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>Print usage statement </p>
<p> [<code>-a|&#8211;all</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>Show all images, including intermediate images </p>
<p> [<code>-f|&#8211;filter</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>Filter output based on given filters, example usage:&nbsp;<wbr>&#8216;&#8211;filter repo=foo&#8217; will list all images that has &quot;foo&quot; as part of their repository name. </p>
<p> [<code>-n|&#8211;noheading</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>Do not print heading when listing the images </p>
<p> [<code>&#8211;no-trunc</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>Do not truncate output </p>
<p> [<code>-q|&#8211;quiet</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>Only display image IDs </p>
<p> [<code>&#8211;json</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>Output in the form of JSON. </p>
<h2>update OPTIONS</h2>
<p> [<code>-f</code>|<code>&#8211;force</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>Remove all containers based on this image </p>
<p> [<code>-h</code>|<code>&#8211;help</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>Print usage statement </p>
<p> [<code>&#8211;storage=[ostree|docker]</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>Optionally specify the storage of the image. Defaults to docker. </p>
<h2>verify OPTIONS</h2>
<p> [<code>-h|&#8211;help</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>Print usage statement </p>
<p> [<code>&#8211;no-validate</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>Skip validation of the files contained inside the image. </p>
<p> [<code>&#8211;storage=[ostree|docker]</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>Optionally specify the storage of the image. Will prompt user to specify if the same image name exists in both ostree and docker, and the user did not specify. </p>
<p> [<code>-v|&#8211;verbose</code>]<br />
Will output the status of each base image that makes up the image being verified. </p>
<h2>version OPTIONS</h2>
<p> [<code>-h|&#8211;help</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>Print usage statement </p>
<p> [<code>-r|&#8211;recurse</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>Recurse through all layers of the specified image. </p>
<p> [<code>&#8211;storage=[ostree|docker]</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>Optionally specify the storage of the image. Will prompt user to specify if the same image name exists in both ostree and docker, and the user did not specify. </p>
<h2>EXAMPLES</h2>
<p> Verify the Red Hat rsyslog image </p>
<dl>
<dt>
<dd>
<pre>
# atomic images verify registry.access.redhat.com/rhel7/rsyslog
#
</pre>
</dl>
<p> Verify the Red Hat rsyslog image and show status of each image layer </p>
<dl>
<dt>
<dd>
<pre>
# atomic images verify -v registry.access.redhat.com/rhel7/rsyslog
registry.access.redhat.com/rhel7/rsyslog contains the following images:
 rhel7/rsyslog-7.1-29           rhel7/rsyslog-7.1-29
 redhat/rhel7-7.1-24            redhat/rhel7-7.1-24
 * = version difference
</pre>
</dl>
<p> Verify a system image </p>
<dl>
<dt>
<dd>
<pre><code>
#sudo atomic images verify busybox
validation output for layer a3ed95caeb02ffe68cdd9fd84406680ae93d633cb16422d00e8a7c22955b46d4:
(no changes detected)
validation output for layer 8ddc19f16526912237dd8af81971d5e4dd0587907234be2b83e249518d5b673f:
"etc/shadow": keyword "size": expected 243;
got 268 "etc/shadow" : keyword "sha256digest" : expected 22d9cee21ee808c52af44ac...;
got 7a07ac69054c2a3533569874c2...
</code></pre>
</dl>
<h2>HISTORY</h2>
<p> July 2015, Originally compiled by Daniel Walsh (dwalsh at redhat dot com) July 2016, Updated to reflect images sub-command changes (jhonce at redhat dot com) July 2016, Added sub-commands all, filter and quiet to list (jerzhang at redhat dot com) </p>
<h2>Index</h2>
