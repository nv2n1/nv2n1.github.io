---
title: "skopeo(1)"
name: "skopeo"
section: "1"
letter: "s"
url: "/docs/linux/man/1-skopeo/"
description: "skopeo — Various operations with container images images and container image registries"
---

<h2 class="name">NAME</h2>
<p> skopeo &#8212; Various operations with container images images and container image registries </p>
<h2>SYNOPSIS</h2>
<p> <code>skopeo</code> [<i>global options</i>] <i>command</i> [<i>command options</i>] </p>
<h2>DESCRIPTION</h2>
<p> skopeo is a command line utility providing various operations with container images and container image registries. For example, it is able to inspect a repository on a Docker registry and fetch image. It fetches the repository&#8217;s manifest and it is able to show you a docker inspect-like json output about a whole repository or a tag. This tool, in contrast to docker inspect, helps you gather useful information about a repository or a tag without requiring you to run docker pull &#8211; e.g. &#8211; which tags are available for the given repository? which labels the image has? </p>
<p> It also allows you to copy container images between various registries, possibly converting them as necessary, and to sign and verify images. </p>
<h2>IMAGE NAMES</h2>
<p> Most commands refer to container images, using a <i>transport</i>:<i>details</i> format. The following formats are supported: </p>
<p> <code>atomic:</code><i>namespace</i><code>/</code><i>stream</i><code>:</code><i>tag</i><br />
&nbsp;<wbr>&nbsp;<wbr>An image in the current project of the current default Atomic<br />
&nbsp;<wbr>&nbsp;<wbr>Registry. The current project and Atomic Registry instance are by<br />
&nbsp;<wbr>&nbsp;<wbr>default read from&nbsp;<wbr>$HOME/.kube/config, which is set e.g. using<br />
&nbsp;<wbr>&nbsp;<wbr>(oc login). </p>
<p> <code>dir:</code><i>path</i><br />
&nbsp;<wbr>&nbsp;<wbr>An existing local directory&nbsp;<wbr><i>path</i>&nbsp;<wbr>storing the manifest, layer<br />
&nbsp;<wbr>&nbsp;<wbr>tarballs and signatures as individual files. This is a<br />
&nbsp;<wbr>&nbsp;<wbr>non-standardized format, primarily useful for debugging or<br />
&nbsp;<wbr>&nbsp;<wbr>noninvasive container inspection. </p>
<p> <code>docker://</code><i>docker-reference</i><br />
&nbsp;<wbr>&nbsp;<wbr>An image in a registry implementing the&nbsp;<wbr>&quot;Docker Registry HTTP API V2&quot;.<br />
&nbsp;<wbr>&nbsp;<wbr>By default, uses the authorization state in&nbsp;<wbr>$HOME/.docker/config.json,<br />
&nbsp;<wbr>&nbsp;<wbr>which is set e.g. using&nbsp;<wbr>(docker login). </p>
<p> <code>oci:</code><i>path</i><code>:</code><i>tag</i><br />
&nbsp;<wbr>&nbsp;<wbr>An image&nbsp;<wbr><i>tag</i>&nbsp;<wbr>in a directory compliant with&nbsp;<wbr>&quot;Open Container Image<br />
&nbsp;<wbr>&nbsp;<wbr>Layout Specification&quot;&nbsp;<wbr>at&nbsp;<wbr><i>path</i>. </p>
<h2>OPTIONS</h2>
<p> <code>&#8211;debug</code> enable debug output </p>
<p> <code>&#8211;policy</code> <i>path-to-policy</i> Path to a policy.json file to use for verifying signatures and deciding whether an image is trusted, overriding the default trust policy file. </p>
<p> <code>&#8211;insecure-policy</code> Adopt an insecure, permissive policy that allows anything. This obviates the need for a policy file. </p>
<p> <code>&#8211;registries.d</code> <i>dir</i> use registry configuration files in <i>dir</i> (e.g. for docker signature storage), overriding the default path. </p>
<p> <code>&#8211;help</code>|<code>-h</code> Show help </p>
<p> <code>&#8211;version</code>|<code>-v</code> print the version number </p>
<h2>COMMANDS</h2>
<h2>skopeo copy</h2>
<p> <code>skopeo copy</code> [<code>&#8211;sign-by=</code><i>key-ID</i>] <i>source-image destination-image</i> </p>
<p> Copy an image (manifest, filesystem layers, signatures) from one location to another. </p>
<p> Uses the system&#8217;s trust policy to validate images, rejects images not trusted by the policy. </p>
<p> <i>source-image</i> use the &quot;image name&quot; format described above </p>
<p> <i>destination-image</i> use the &quot;image name&quot; format described above </p>
<p> <code>&#8211;remove-signatures</code> do not copy signatures, if any, from <i>source-image</i>. Necessary when copying a signed image to a destination which does not support signatures. </p>
<p> <code>&#8211;sign-by=</code><i>key-id</i> add a signature using that key ID for an image name corresponding to <i>destination-image</i> </p>
<p> <code>&#8211;src-creds</code> <i>username[:password]</i> for accessing the source registry </p>
<p> <code>&#8211;dest-creds</code> <i>username[:password]</i> for accessing the destination registry </p>
<p> <code>&#8211;src-cert-dir</code> <i>path</i> Use certificates at <i>path</i> (*.crt, *.cert, *.key) to connect to the source registry </p>
<p> <code>&#8211;src-tls-verify</code> <i>bool-value</i> Require HTTPS and verify certificates when talking to docker source registry (defaults to true) </p>
<p> <code>&#8211;dest-cert-dir</code> <i>path</i> Use certificates at <i>path</i> (*.crt, *.cert, *.key) to connect to the destination registry </p>
<p> <code>&#8211;dest-ostree-tmp-dir</code> <i>path</i> Directory to use for OSTree temporary files. </p>
<p> <code>&#8211;dest-tls-verify</code> <i>bool-value</i> Require HTTPS and verify certificates when talking to docker destination registry (defaults to true) </p>
<p> Existing signatures, if any, are preserved as well. </p>
<h2>skopeo delete</h2>
<p> <code>skopeo delete</code> <i>image-name</i> </p>
<p> Mark <i>image-name</i> for deletion. To release the allocated disk space, you need to execute the docker registry garabage collector. E.g., </p>
<dl>
<dt>
<dd>
<pre>
$ docker exec -it registry bin/registry garbage-collect /etc/docker/registry/config.yml
</pre>
</dl>
<p> <code>&#8211;creds</code> <i>username[:password]</i> for accessing the registry </p>
<p> <code>&#8211;cert-dir</code> <i>path</i> Use certificates at <i>path</i> (*.crt, *.cert, *.key) to connect to the registry </p>
<p> <code>&#8211;tls-verify</code> <i>bool-value</i> Require HTTPS and verify certificates when talking to docker registries (defaults to true) </p>
<p> Additionally, the registry must allow deletions by setting REGISTRY_STORAGE_DELETE_ENABLED=true for the registry daemon. </p>
<h2>skopeo inspect</h2>
<p> <code>skopeo inspect</code> [<code>&#8211;raw</code>] <i>image-name</i> </p>
<p> Return low-level information about <i>image-name</i> in a registry </p>
<p> <code>&#8211;raw</code> output raw manifest, default is to format in JSON </p>
<p> <i>image-name</i> name of image to retrieve information about </p>
<p> <code>&#8211;creds</code> <i>username[:password]</i> for accessing the registry </p>
<p> <code>&#8211;cert-dir</code> <i>path</i> Use certificates at <i>path</i> (*.crt, *.cert, *.key) to connect to the registry </p>
<p> <code>&#8211;tls-verify</code> <i>bool-value</i> Require HTTPS and verify certificates when talking to docker registries (defaults to true) </p>
<h2>skopeo manifest-digest</h2>
<p> <code>skopeo manifest-digest</code> <i>manifest-file</i> </p>
<p> Compute a manifest digest of <i>manifest-file</i> and write it to standard output. </p>
<h2>skopeo standalone-sign</h2>
<p> <code>skopeo standalone-sign</code> <i>manifest docker-reference key-fingerprint</i> <code>&#8211;output</code>|<code>-o</code> <i>signature</i> </p>
<p> This is primarily a debugging tool, or useful for special cases, and usually should not be a part of your normal operational workflow; use skopeo copy &#8211;sign-by instead to publish and sign an image in one step. </p>
<p> <i>manifest</i> Path to a file containing the image manifest </p>
<p> <i>docker-reference</i> A docker reference to identify the image with </p>
<p> <i>key-fingerprint</i> Key identity to use for signing </p>
<p> <code>&#8211;output</code>|<code>-o</code> output file </p>
<h2>skopeo standalone-verify</h2>
<p> <code>skopeo standalone-verify</code> <i>manifest docker-reference key-fingerprint signature</i> </p>
<p> Verify a signature using local files, digest will be printed on success. </p>
<p> <i>manifest</i> Path to a file containing the image manifest </p>
<p> <i>docker-reference</i> A docker reference expected to identify the image in the signature </p>
<p> <i>key-fingerprint</i> Expected identity of the signing key </p>
<p> <i>signature</i> Path to signature file </p>
<p> <code>Note:</code> If you do use this, make sure that the image can not be changed at the source location between the times of its verification and use. </p>
<h2>skopeo help</h2>
<p> show help for skopeo </p>
<h2>FILES</h2>
<p> <code>/etc/containers/policy.json</code><br />
&nbsp;<wbr>&nbsp;<wbr>Default trust policy file, if&nbsp;<wbr><code>&#8211;policy</code>&nbsp;<wbr>is not specified.<br />
&nbsp;<wbr>&nbsp;<wbr>The policy format is documented in&nbsp;<wbr> &lt;<a rel="nofollow" href="https://github.com/containers/image/blob/master/docs/policy.json.md">https://github.com/containers/image/blob/master/docs/policy.json.md</a>&gt; . </p>
<p> <code>/etc/containers/registries.d</code><br />
&nbsp;<wbr>&nbsp;<wbr>Default directory containing registry configuration, if&nbsp;<wbr><code>&#8211;registries.d</code>&nbsp;<wbr>is not specified.<br />
&nbsp;<wbr>&nbsp;<wbr>The contents of this directory are documented in&nbsp;<wbr> &lt;<a rel="nofollow" href="https://github.com/containers/image/blob/master/docs/registries.d.md">https://github.com/containers/image/blob/master/docs/registries.d.md</a>&gt; . </p>
<h2>EXAMPLES</h2>
<h2>skopeo copy</h2>
<p> To copy the layers of the docker.io busybox image to a local directory: </p>
<dl>
<dt>
<dd>
<pre>
$ mkdir -p /var/lib/images/busybox
$ skopeo copy <a href="docker://busybox:latest">docker://busybox:latest</a> dir:/var/lib/images/busybox
$ ls /var/lib/images/busybox/*
  /tmp/busybox/2b8fd9751c4c0f5dd266fcae00707e67a2545ef34f9a29354585f93dac906749.tar
  /tmp/busybox/manifest.json
  /tmp/busybox/8ddc19f16526912237dd8af81971d5e4dd0587907234be2b83e249518d5b673f.tar
</pre>
</dl>
<p> To copy and sign an image: </p>
<dl>
<dt>
<dd>
<pre>
$ skopeo copy --sign-by dev [at] example.com atomic:example/busybox:streaming atomic:example/busybox:gold
</pre>
</dl>
<h2>skopeo delete</h2>
<p> Mark image example/pause for deletion from the registry.example.com registry: </p>
<dl>
<dt>
<dd>
<pre>
$ skopeo delete --force <a href="docker://registry.example.com/example/pause:latest">docker://registry.example.com/example/pause:latest</a>
</pre>
</dl>
<p> See above for additional details on using the command <code>delete</code>. </p>
<h2>skopeo inspect</h2>
<p> To review information for the image fedora from the docker.io registry: </p>
<dl>
<dt>
<dd>
<pre><code>
$ skopeo inspect docker: // docker.io/fedora
{
    "Name" : "docker.io/library/fedora",
             "Digest" : "sha256:a97914edb6ba15deb5c5acf87bd6bd5b6b0408c96f48a5cbd450b5b04509bb7d",
                        "RepoTags" : [
                            "20",
                            "21",
                            "22",
                            "23",
                            "24",
                            "heisenbug",
                            "latest",
                            "rawhide"
                        ],
                                     "Created" : "2016-06-20T19:33:43.220526898Z",
                                                 "DockerVersion" : "1.10.3",
                                                                   "Labels" : {},
                                                                              "Architecture" : "amd64",
                                                                                               "Os" : "linux",
                                                                                                      "Layers" : ["sha256:7c91a140e7a1025c3bc3aace4c80c0d9933ac4ee24b8630a6b0b5d8b9ce6b9d4"]
}
</code></pre>
</dl>
<h2>skopeo layers</h2>
<p> Another method to retrieve the layers for the busybox image from the docker.io registry: </p>
<dl>
<dt>
<dd>
<pre>
$ skopeo layers <a href="docker://busybox">docker://busybox</a>
$ ls layers-500650331/
  8ddc19f16526912237dd8af81971d5e4dd0587907234be2b83e249518d5b673f.tar
  manifest.json
  a3ed95caeb02ffe68cdd9fd84406680ae93d633cb16422d00e8a7c22955b46d4.tar
</pre>
</dl>
<h2>skopeo manifest-digest</h2>
<dl>
<dt>
<dd>
<pre>
$ skopeo manifest-digest manifest.json
sha256:a59906e33509d14c036c8678d687bd4eec81ed7c4b8ce907b888c607f6a1e0e6
</pre>
</dl>
<h2>skopeo standalone-sign</h2>
<dl>
<dt>
<dd>
<pre>
$ skopeo standalone-sign busybox-manifest.json registry.example.com/example/busybox 1D8230F6CDB6A06716E414C1DB72F2188BB46CC8 --output busybox.signature
$
</pre>
</dl>
<p> See skopeo copy above for the preferred method of signing images. </p>
<h2>skopeo standalone-verify</h2>
<dl>
<dt>
<dd>
<pre>
$ skopeo standalone-verify busybox-manifest.json registry.example.com/example/busybox 1D8230F6CDB6A06716E414C1DB72F2188BB46CC8  busybox.signature
Signature verified, digest sha256:20bf21ed457b390829cdbeec8795a7bea1626991fda603e0d01b4e7f60427e55
</pre>
</dl>
<h2>AUTHORS</h2>
<p> Antonio Murdaca &lt;runcom [at] redhat.com&gt;, Miloslav Trmac &lt;mitr [at] redhat.com&gt;, Jhon Honce &lt;jhonce [at] redhat.com&gt; </p>
<h2>Index</h2>
