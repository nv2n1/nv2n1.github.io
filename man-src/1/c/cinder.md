---
title: "cinder(1)"
name: "cinder"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cinder/"
description: "cinder – Client for OpenStack Block Storage API"
---

<h2>NAME</h2>
<p> cinder &#8211; Client for OpenStack Block Storage API</p>
<h2>SYNOPSIS</h2>
<p> <code>cinder</code> [options] &lt;command&gt; [command-options] </p>
<p> <code>cinder help</code> </p>
<p> <code>cinder help</code> &lt;command&gt;</p>
<h2>DESCRIPTION</h2>
<p> The <code>cinder</code> command line utility interacts with OpenStack Block Storage Service (Cinder). </p>
<p> In order to use the CLI, you must provide your OpenStack username, password, project (historically called tenant), and auth endpoint. You can use configuration options <i>&#8211;os-username</i>, <i>&#8211;os-password</i>, <i>&#8211;os-tenant-name</i> or <i>&#8211;os-tenant-id</i>, and <i>&#8211;os-auth-url</i> or set corresponding environment variables: </p>
<pre>
export OS_USERNAME=user
export OS_PASSWORD=pass
export OS_TENANT_NAME=myproject
export OS_AUTH_URL=<a rel="nofollow" href="http://auth.example.com:5000/v2.0">http://auth.example.com:5000/v2.0</a>
</pre>
<p> You can select an API version to use by <i>&#8211;os-volume-api-version</i> option or by setting corresponding environment variable: </p>
<pre>
export OS_VOLUME_API_VERSION=2
</pre>
<h2>OPTIONS</h2>
<p> To get a list of available commands and options run: </p>
<pre>
cinder help
</pre>
<p> To get usage and options of a command: </p>
<pre>
cinder help &lt;command&gt;
</pre>
<h2>BUGS</h2>
<p> Cinder client is hosted in Launchpad so you can view current bugs at <i><a rel="nofollow" href="https://bugs.launchpad.net/python-cinderclient/">https://bugs.launchpad.net/python-cinderclient/</a></i>.</p>
<h2>AUTHOR</h2>
<p> OpenStack Contributors</p>
<h2>COPYRIGHT</h2>
<p> OpenStack Contributors </p>
<h2>Index</h2>
