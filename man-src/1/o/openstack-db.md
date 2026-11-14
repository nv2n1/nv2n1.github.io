---
title: "openstack-db(1)"
name: "openstack-db"
section: "1"
letter: "o"
url: "/docs/linux/man/1-openstack-db/"
description: "openstack-db – Set up a local database for use with an OpenStack service"
---

<h2>NAME</h2>
<p> openstack-db &#8211; Set up a local database for use with an OpenStack service</p>
<h2>SYNOPSIS</h2>
<p> <code>openstack-db</code> <i>&#8211;service &lt;service&gt; &#8211;init|&#8211;drop </i>[<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> Set up a local database (MySQL) for use with openstack-&lt;service&gt;. This script will create a &#8216;&lt;service&gt;&#8217; database that is accessible only on localhost by user &#8216;&lt;service&gt;&#8217; with password &#8216;&lt;service&gt;&#8217;. The setup of a database with a multi-server OpenStack installation is outside of the scope of this simple helper script.</p>
<h2>OPTIONS</h2>
<dl>
<dt> <code>&#8211;help</code> | <code>-h</code></p>
<dt>
<dd>
<dd>Print usage information.</p>
<dt> <code>&#8211;drop</code></p>
<dt>
<dd>
<dd>Drop the database.</p>
<dt> <code>&#8211;init</code></p>
<dt>
<dd>
<dd>Initialise the database.</p>
<dt> <code>&#8211;update</code></p>
<dt>
<dd>
<dd>Update an initialised database.</p>
<dt> <code>&#8211;password</code> &lt;pw&gt; | <code>-p</code> &lt;pw&gt;</p>
<dt>
<dd>
<dd>Specify the password for user that will be used to connect database for the service. By default the &lt;service&gt; parameter is used for the password.</p>
<dt> <code>&#8211;rootpw</code> &lt;pw&gt; | <code>-r</code> &lt;pw&gt;</p>
<dt>
<dd>
<dd>Specify the root database password. If the script installs the database server, it will set the root password to this value instead of prompting for a password. If the database server is already installed, this password will be used to connect to the database instead of having to prompt for it.</p>
<dt> <code>&#8211;service</code> &lt;service&gt;</p>
<dt>
<dd>
<dd>Specify the openstack service to manipulate the database for. This option is mandatory.</p>
<dt> <code>&#8211;yes</code> | <code>-y</code></p>
<dt>
<dd>
<dd>In cases where the script would normally ask for confirmation before doing something, such as installing the database server, just assume yes. This is useful if you want to run the script non-interactively. </p>
</dl>
<h2>Index</h2>
