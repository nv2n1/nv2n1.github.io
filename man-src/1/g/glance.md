---
title: "glance(1)"
name: "glance"
section: "1"
letter: "g"
url: "/docs/linux/man/1-glance/"
description: "glance – Client for OpenStack Images API"
---

<h2>NAME</h2>
<p> glance &#8211; Client for OpenStack Images API</p>
<h2>SYNOPSIS</h2>
<p> <code>glance</code> [options] &lt;command&gt; [command-options] </p>
<p> <code>glance help</code> </p>
<p> <code>glance help</code> &lt;command&gt;</p>
<h2>DESCRIPTION</h2>
<p> The <code>glance</code> command line utility interacts with OpenStack Images Service (Glance). </p>
<p> In order to use the CLI, you must provide your OpenStack username, password, project (historically called tenant), and auth endpoint. You can use configuration options <i>&#8211;os-username</i>, <i>&#8211;os-password</i>, <i>&#8211;os-tenant-id</i>, and <i>&#8211;os-auth-url</i> or set corresponding environment variables: </p>
<pre>
export OS_USERNAME=user
export OS_PASSWORD=pass
export OS_TENANT_ID=b363706f891f48019483f8bd6503c54b
export OS_AUTH_URL=<a rel="nofollow" href="http://auth.example.com:5000/v2.0">http://auth.example.com:5000/v2.0</a>
</pre>
<p> The command line tool will attempt to reauthenticate using provided credentials for every request. You can override this behavior by manually supplying an auth token using <i>&#8211;os-image-url</i> and <i>&#8211;os-auth-token</i> or by setting corresponding environment variables: </p>
<pre>
export OS_IMAGE_URL=<a rel="nofollow" href="http://glance.example.org:9292/">http://glance.example.org:9292/</a>
export OS_AUTH_TOKEN=3bcc3d3a03f44e3d8377f9247b0ad155
</pre>
<p> You can select an API version to use by <i>&#8211;os-image-api-version</i> option or by setting corresponding environment variable: </p>
<pre>
export OS_IMAGE_API_VERSION=2
</pre>
<h2>OPTIONS</h2>
<p> To get a list of available commands and options run: </p>
<pre>
glance help
</pre>
<p> To get usage and options of a command: </p>
<pre>
glance help &lt;command&gt;
</pre>
<h2>EXAMPLES</h2>
<p> Get information about image-create command: </p>
<pre>
glance help image-create
</pre>
<p> See available images: </p>
<pre>
glance image-list
</pre>
<p> Create new image: </p>
<pre><code>
glance image - create-- name foo-- disk - format = qcow2-- container - format = bare-- is - public = True-- copy - from http: // somewhere.net/foo.img
</code></pre>
<p> Describe a specific image: </p>
<pre>
glance image-show foo
</pre>
<h2>BUGS</h2>
<p> Glance client is hosted in Launchpad so you can view current bugs at <i><a rel="nofollow" href="https://bugs.launchpad.net/python-glanceclient/">https://bugs.launchpad.net/python-glanceclient/</a></i>.</p>
<h2>AUTHOR</h2>
<p> OpenStack Foundation</p>
<h2>COPYRIGHT</h2>
<p> OpenStack Foundation </p>
<h2>Index</h2>
