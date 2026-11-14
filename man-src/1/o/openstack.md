---
title: "openstack(1)"
name: "openstack"
section: "1"
letter: "o"
url: "/docs/linux/man/1-openstack/"
description: "openstack – OpenStack Command Line Client"
---

<h2>NAME</h2>
<p> openstack &#8211; OpenStack Command Line Client </p>
<p> OpenStack Command Line</p>
<h2>SYNOPSIS</h2>
<p> <code>openstack</code> [&lt;global-options&gt;] &lt;command&gt; [&lt;command-arguments&gt;] </p>
<p> <code>openstack help</code> &lt;command&gt; </p>
<p> <code>openstack</code> &#8211;help</p>
<h2>DESCRIPTION</h2>
<p> <code>openstack</code> provides a common command-line interface to OpenStack APIs. It is generally equivalent to the CLIs provided by the OpenStack project client libraries, but with a distinct and consistent command structure.</p>
<h2>AUTHENTICATION METHODS</h2>
<p> <code>openstack</code> uses a similar authentication scheme as the OpenStack project CLIs, with the credential information supplied either as environment variables or as options on the command line. The primary difference is the use of &#8216;project&#8217; in the name of the options <code>OS_PROJECT_NAME</code>/<code>OS_PROJECT_ID</code> over the old tenant-based names. </p>
<pre>
export OS_AUTH_URL=&lt;url-to-openstack-identity&gt;
export OS_PROJECT_NAME=&lt;project-name&gt;
export OS_USERNAME=&lt;user-name&gt;
export OS_PASSWORD=&lt;password&gt;  # (optional)
</pre>
<p> <code>openstack</code> can use different types of authentication plugins provided by the keystoneclient library. The following default plugins are available:</p>
<dl>
<dt>&bull;</p>
<dd> <code>token</code>: Authentication with a token</p>
<dt>&bull;</p>
<dd> <code>password</code>: Authentication with a username and a password </p>
<p> Refer to the keystoneclient library documentation for more details about these plugins and their options, and for a complete list of available plugins. Please bear in mind that some plugins might not support all of the functionalities of <code>openstack</code>; for example the v3unscopedsaml plugin can deliver only unscoped tokens, some commands might not be available through this authentication method. </p>
<p> Additionally, it is possible to use Keystone&#8217;s service token to authenticate, by setting the options <i>&#8211;os-token</i> and <i>&#8211;os-url</i> (or the environment variables <code>OS_TOKEN</code> and <code>OS_URL</code> respectively). This method takes precedence over authentication plugins. </p>
<p> <code>NOTE:</code> To use the <code>v3unscopedsaml</code> method, the lxml package will need to be installed.</dl>
<h2>OPTIONS</h2>
<p> <code>openstack</code> takes global options that control overall behaviour and command-specific options that control the command operation. Most global options have a corresponding environment variable that may also be used to set the value. If both are present, the command-line option takes priority. The environment variable names are derived from the option name by dropping the leading dashes (&#8216;&#8211;&#8216;), converting each embedded dash (&#8216;-&#8216;) to an underscore (&#8216;_&#8217;), and converting to upper case. </p>
<p> <code>openstack</code> recognizes the following global options:</p>
<dl>
<dt><i>&#8211;os-auth-plugin</i> &lt;auth-plugin&gt;</p>
<dd> The authentication plugin to use when connecting to the Identity service. If this option is not set, <code>openstack</code> will attempt to guess the authentication method to use based on the other options. If this option is set, its version must match <i>&#8211;os-identity-api-version</i></p>
<dt><i>&#8211;os-auth-url</i> &lt;auth-url&gt;</p>
<dd> Authentication URL</p>
<dt><i>&#8211;os-url</i> &lt;service-url&gt;</p>
<dd> Service URL, when using a service token for authentication</p>
<dt><i>&#8211;os-domain-name</i> &lt;auth-domain-name&gt; | <i>&#8211;os-domain-id</i> &lt;auth-domain-id&gt;</p>
<dd> Domain-level authorization scope (name or ID)</p>
<dt><i>&#8211;os-project-name</i> &lt;auth-project-name&gt; | <i>&#8211;os-project-id</i> &lt;auth-project-id&gt;</p>
<dd> Project-level authentication scope (name or ID)</p>
<dt><i>&#8211;os-project-domain-name</i> &lt;auth-project-domain-name&gt; | <i>&#8211;os-project-domain-id</i> &lt;auth-project-domain-id&gt;</p>
<dd> Domain name or id containing project</p>
<dt><i>&#8211;os-username</i> &lt;auth-username&gt;</p>
<dd> Authentication username</p>
<dt><i>&#8211;os-password</i> &lt;auth-password&gt;</p>
<dd> Authentication password</p>
<dt><i>&#8211;os-token</i> &lt;token&gt;</p>
<dd> Authenticated token or service token</p>
<dt><i>&#8211;os-user-domain-name</i> &lt;auth-user-domain-name&gt; | <i>&#8211;os-user-domain-id</i> &lt;auth-user-domain-id&gt;</p>
<dd> Domain name or id containing user</p>
<dt><i>&#8211;os-user-domain-name</i> &lt;auth-user-domain-name&gt; | <i>&#8211;os-user-domain-id</i> &lt;auth-user-domain-id&gt;</p>
<dd> Domain name or ID containing user</p>
<dt><i>&#8211;os-trust-id</i> &lt;trust-id&gt;</p>
<dd> id of the trust to use as a trustee user</p>
<dt><i>&#8211;os-default-domain</i> &lt;auth-domain&gt;</p>
<dd> Default domain ID (Default: &#8216;default&#8217;)</p>
<dt><i>&#8211;os-region-name</i> &lt;auth-region-name&gt;</p>
<dd> Authentication region name</p>
<dt><i>&#8211;os-cacert</i> &lt;ca-bundle-file&gt;</p>
<dd> CA certificate bundle file</p>
<dt><i>&#8211;verify</i> | <i>&#8211;insecure</i></p>
<dd> Verify or ignore server certificate (default: verify)</p>
<dt><i>&#8211;os-identity-api-version</i> &lt;identity-api-version&gt;</p>
<dd> Identity API version (Default: 2.0)</p>
<dt><i>&#8211;os-XXXX-api-version</i> &lt;XXXX-api-version&gt;</p>
<dd> Additional API version options will be available depending on the installed API libraries.</dl>
<h2>COMMANDS</h2>
<p> To get a list of the available commands: </p>
<pre>
openstack --help
</pre>
<p> To get a description of a specific command: </p>
<pre>
openstack help &lt;command&gt;
</pre>
<p> Note that the set of commands shown will vary depending on the API versions that are in effect at that time. For example, to force the display of the Identity v3 commands: openstack &#8211;os-identity-api-version 3 &#8211;help</p>
<dl>
<dt><i>complete</i></p>
<dd> Print the bash completion functions for the current command set.</p>
<dt><i>help</i></p>
<dd> Print help for an individual command </p>
<p> Additional information on the OpenStackClient command structure and arguments is available in the <i>OpenStackClient Commands</i> wiki page.</dl>
<h3>Command Objects</h3>
<p> The list of command objects is growing longer with the addition of OpenStack project support. The object names may consist of multiple words to compose a unique name. Occasionally when multiple APIs have a common name with common overlapping purposes there will be options to select which object to use, or the API resources will be merged, as in the <code>quota</code> object that has options referring to both Compute and Volume quotas.</p>
<h3>Command Actions</h3>
<p> The actions used by OpenStackClient are defined with specific meaning to provide a consistent behavior for each object. Some actions have logical opposite actions, and those pairs will always match for any object that uses them.</p>
<h2>NOTES</h2>
<p> The command list displayed in help output reflects the API versions selected. For example, to see Identity v3 commands <code>OS_IDENTITY_API_VERSION</code> must be set to <code>3</code>.</p>
<h2>EXAMPLES</h2>
<p> Show the detailed information for server <code>appweb01</code>: </p>
<pre><code>
openstack-- os - project - name ExampleCo-- os - username demo-- os - password secrete-- os - auth - url http: //localhost:5000:/v2.0 \
    server show appweb01
</code></pre>
<p> The same command if the auth environment variables (<code>OS_AUTH_URL</code>, <code>OS_PROJECT_NAME</code>, <code>OS_USERNAME</code>, <code>OS_PASSWORD</code>) are set: </p>
<pre>
openstack server show appweb01
</pre>
<p> Create a new image: </p>
<pre><code>
openstack image create-- disk - format = qcow2-- container - format = bare-- public --copy - from http: //somewhere.net/foo.img \
    foo
</code></pre>
<h2>FILES</h2>
<dl>
<dt><code>~/.openstack</code></p>
<dd> Placeholder for future local state directory. This directory is intended to be shared among multiple OpenStack-related applications; contents are namespaced with an identifier for the app that owns it. Shared contents (such as <code>~/.openstack/cache</code>) have no prefix and the contents must be portable.</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> The following environment variables can be set to alter the behaviour of <code>openstack</code>. Most of them have corresponding command-line options that take precedence if set.</p>
<dl>
<dt><code>OS_AUTH_PLUGIN</code></p>
<dd> The authentication plugin to use when connecting to the Identity service, its version must match the Identity API version</p>
<dt><code>OS_AUTH_URL</code></p>
<dd> Authentication URL</p>
<dt><code>OS_URL</code></p>
<dd> Service URL (when using the service token)</p>
<dt><code>OS_DOMAIN_NAME</code></p>
<dd> Domain-level authorization scope (name or ID)</p>
<dt><code>OS_PROJECT_NAME</code></p>
<dd> Project-level authentication scope (name or ID)</p>
<dt><code>OS_PROJECT_DOMAIN_NAME</code></p>
<dd> Domain name or id containing project</p>
<dt><code>OS_USERNAME</code></p>
<dd> Authentication username</p>
<dt><code>OS_TOKEN</code></p>
<dd> Authenticated or service token</p>
<dt><code>OS_PASSWORD</code></p>
<dd> Authentication password</p>
<dt><code>OS_USER_DOMAIN_NAME</code></p>
<dd> Domain name or id containing user</p>
<dt><code>OS_TRUST_ID</code></p>
<dd> id of the trust to use as a trustee user</p>
<dt><code>OS_DEFAULT_DOMAIN</code></p>
<dd> Default domain ID (Default: &#8216;default&#8217;)</p>
<dt><code>OS_REGION_NAME</code></p>
<dd> Authentication region name</p>
<dt><code>OS_CACERT</code></p>
<dd> CA certificate bundle file</p>
<dt><code>OS_IDENTITY_API_VERSION</code></p>
<dd> Identity API version (Default: 2.0)</p>
<dt><code>OS_XXXX_API_VERSION</code></p>
<dd> Additional API version options will be available depending on the installed API libraries.</dl>
<h2>BUGS</h2>
<p> Bug reports are accepted at the python-openstackclient LaunchPad project &quot;<i><a rel="nofollow" href="https://bugs.launchpad.net/python-openstackclient/+bugs">https://bugs.launchpad.net/python-openstackclient/+bugs</a></i>&quot;.</p>
<h2>AUTHORS</h2>
<p> Please refer to the AUTHORS file distributed with OpenStackClient.</p>
<h2>COPYRIGHT</h2>
<p> Copyright 2011-2014 OpenStack Foundation and the authors listed in the AUTHORS file.</p>
<h2>LICENSE</h2>
<p> <i><a rel="nofollow" href="http://www.apache.org/licenses/LICENSE-2.0">http://www.apache.org/licenses/LICENSE-2.0</a></i></p>
<h2>SEE ALSO</h2>
<p> The <i>OpenStackClient page</i> in the <i>OpenStack Wiki</i> contains further documentation. </p>
<p> The individual OpenStack project CLIs, the OpenStack API references.</p>
<h2>AUTHOR</h2>
<p> OpenStack contributors</p>
<h2>COPYRIGHT</h2>
<p> 2012-2013 OpenStack Foundation </p>
<h2>Index</h2>
