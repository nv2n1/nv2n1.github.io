---
title: "keystone(1)"
name: "keystone"
section: "1"
letter: "k"
url: "/docs/linux/man/1-keystone/"
description: "keystone – Client for OpenStack Identity API"
---

<h2>NAME</h2>
<p> keystone &#8211; Client for OpenStack Identity API</p>
<h2>SYNOPSIS</h2>
<p> <code>keystone</code> [options] &lt;command&gt; [command-options] </p>
<p> <code>keystone help</code> </p>
<p> <code>keystone help</code> &lt;command&gt;</p>
<h2>DESCRIPTION</h2>
<p> <code>WARNING:</code> The <code>keystone</code> command line utility is pending deprecation. The <i>OpenStackClient unified command line utility</i> should be used instead. The <code>keystone</code> command line utility only supports V2 of the Identity API whereas the OSC program supports both V2 and V3. </p>
<p> The <code>keystone</code> command line utility interacts with services providing OpenStack Identity API (e.g. Keystone). </p>
<p> To communicate with the API, you will need to be authenticated &#8211; and the <code>keystone</code> provides multiple options for this. </p>
<p> While bootstrapping Keystone the authentication is accomplished with a shared secret token and the location of the Identity API endpoint. The shared secret token is configured in keystone.conf as &quot;admin_token&quot;. </p>
<p> You can specify those values on the command line with <i>&#8211;os-token</i> and <i>&#8211;os-endpoint</i>, or set them in environment variables:</p>
<dl>
<dt><code>OS_SERVICE_TOKEN</code></p>
<dd> Your Keystone administrative token</p>
<dt><code>OS_SERVICE_ENDPOINT</code></p>
<dd> Your Identity API endpoint </p>
<p> The command line options will override any environment variables set. </p>
<p> If you already have accounts, you can use your OpenStack username and password. You can do this with the <i>&#8211;os-username</i>, <i>&#8211;os-password</i>. </p>
<p> Keystone allows a user to be associated with one or more projects which are historically called tenants. To specify the project for which you want to authorize against, you may optionally specify a <i>&#8211;os-tenant-id</i> or <i>&#8211;os-tenant-name</i>. </p>
<p> Instead of using options, it is easier to just set them as environment variables:</p>
<dt><code>OS_USERNAME</code></p>
<dd> Your Keystone username.</p>
<dt><code>OS_PASSWORD</code></p>
<dd> Your Keystone password.</p>
<dt><code>OS_TENANT_NAME</code></p>
<dd> Name of Keystone project.</p>
<dt><code>OS_TENANT_ID</code></p>
<dd> ID of Keystone Tenant.</p>
<dt><code>OS_AUTH_URL</code></p>
<dd> The OpenStack API server URL.</p>
<dt><code>OS_IDENTITY_API_VERSION</code></p>
<dd> The OpenStack Identity API version.</p>
<dt><code>OS_CACERT</code></p>
<dd> The location for the CA truststore (PEM formatted) for this client.</p>
<dt><code>OS_CERT</code></p>
<dd> The location for the keystore (PEM formatted) containing the public key of this client. This keystore can also optionally contain the private key of this client.</p>
<dt><code>OS_KEY</code></p>
<dd> The location for the keystore (PEM formatted) containing the private key of this client. This value can be empty if the private key is included in the OS_CERT file. </p>
<p> For example, in Bash you&#8217;d use: </p>
<pre>
export OS_USERNAME=yourname
export OS_PASSWORD=yadayadayada
export OS_TENANT_NAME=myproject
export OS_AUTH_URL=http(s)://example.com:5000/v2.0/
export OS_IDENTITY_API_VERSION=2.0
export OS_CACERT=/etc/keystone/yourca.pem
export OS_CERT=/etc/keystone/yourpublickey.pem
export OS_KEY=/etc/keystone/yourprivatekey.pem
</pre>
</dl>
<h2>OPTIONS</h2>
<p> To get a list of available commands and options run: </p>
<pre>
keystone help
</pre>
<p> To get usage and options of a command: </p>
<pre>
keystone help &lt;command&gt;
</pre>
<h2>EXAMPLES</h2>
<p> Get information about endpoint-create command: </p>
<pre>
keystone help endpoint-create
</pre>
<p> View endpoints of OpenStack services: </p>
<pre>
keystone catalog
</pre>
<p> Create a &#8216;service&#8217; project: </p>
<pre>
keystone tenant-create --name=service
</pre>
<p> Create service user for nova: </p>
<pre><code>
keystone user - create-- name = nova-- tenant_id = &lt;project ID&gt; --email = nova[at] nothing.com
</code></pre>
<p> View roles: </p>
<pre>
keystone role-list
</pre>
<h2>BUGS</h2>
<p> Keystone client is hosted in Launchpad so you can view current bugs at <i><a rel="nofollow" href="https://bugs.launchpad.net/python-keystoneclient/">https://bugs.launchpad.net/python-keystoneclient/</a></i>.</p>
<h2>AUTHOR</h2>
<p> OpenStack Contributors</p>
<h2>COPYRIGHT</h2>
<p> OpenStack Contributors </p>
<h2>Index</h2>
