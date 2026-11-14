---
title: "atomic-pull(1)"
name: "atomic-pull"
section: "1"
letter: "a"
url: "/docs/linux/man/1-atomic-pull/"
description: "atomic-pull – fetch an image locally"
---

<h2 class="name">NAME</h2>
<p> atomic-pull &#8211; fetch an image locally </p>
<h2>SYNOPSIS</h2>
<p> <code>atomic pull</code> [<code>-h|&#8211;help</code>] [<code>&#8211;storage=[ostree|docker]</code>] [<code>-t</code>|<code>&#8211;type</code> atomic] IMAGE </p>
<h2>DESCRIPTION</h2>
<p> <code>atomic pull</code>, will fetch a remote image and store it locally. </p>
<p> You can pull an image from a docker registry (like docker.io) to your local docker daemon with atomic pull. </p>
<p> atomic pull docker.io/busybox:latest </p>
<p> Use the &#8211;storage ostree option to store it into the OSTree repository. You can define a default storage type in <code>/etc/atomic.conf</code> with the key of <code>default_storage</code>. </p>
<p> IMAGE has the form SOURCE:IMAGE-NAME, where SOURCE can be one of then &#8216;oci&#8217; is assumed. </p>
<p> An &#8216;oci&#8217; image is fetched via Skopeo from a Docker registry. These two commands are equivalent: </p>
<p> atomic pull etcd<br />
 atomic pull oci:etcd </p>
<p> A &#8216;docker&#8217; image is imported from the local Docker engine, thus not accessing the network. It is equivalent to saving the image from docker (docker save IMAGE) and importing it into the OSTree repository: </p>
<p> atomic pull &#8211;storage ostree docker:fedora </p>
<p> A &#8216;dockertar&#8217; image works in a similar way to &#8216;docker&#8217; images, except that the saved tarball is specified: </p>
<p> atomic pull &#8211;storage ostree dockertar:/path/to/the/image.tar </p>
<p> An &#8216;ostree&#8217; image refers to an image which is fetched from a remote OSTree repository. The remote has to be already configured in the local OSTree repository: </p>
<p> atomic pull &#8211;storage ostree ostree:REMOTE/branch </p>
<p> If the user is not privileged, the image will be stored in the user specific repository. </p>
<p> If your /etc/containers/policy.json requires signature verification, the pulled image is verified prior to being made available to the local docker daemon. When interacting with a docker registry, Atomic uses the policy and YAML configuration files /etc/containers/ to determine:</p>
<dl>
<dt>step]</p>
<dd>
<p> item if the image should be verified with a signature item and where to get the signature</dl>
<p> If you use the &#8211;type atomic switch to interact with an atomic registry, Atomic will still use the policy to determine if verification is needed. The signature itself will be obtained from the atomic registry. An example of pulling from an atomic registry could be: </p>
<p> atomic pull &#8211;type atomic my-atomic-registry:images/foobar </p>
<h2>OPTIONS:</h2>
<p> <code>-h</code> <code>&#8211;help</code> Print usage statement </p>
<p> <code>&#8211;storage=[ostree|docker]</code> Define the destination storage for the pulled image. </p>
<p> <code>-t</code> <code>&#8211;type atomic</code> Define an alternate registry type. The only valid option is <code>atomic</code> for when you want to take advantage of advanced atomic registry options. </p>
<h2>HISTORY</h2>
<p> April 2016, Originally compiled by Giuseppe Scrivano (gscrivan at redhat dot com) </p>
<h2>Index</h2>
