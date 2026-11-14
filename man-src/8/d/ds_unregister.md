---
title: "ds_unregister(8)"
name: "ds_unregister"
section: "8"
letter: "d"
url: "/docs/linux/man/8-ds_unregister/"
description: "ds_unregister – Un-register a directory server instance from the console"
---

<p>ds_unregister &#8211; Un-register a directory server instance from the console</p>
<h2>Synopsis</h2>
<p><code>ds_unregister</code> -s <i>server_id</i> -w <i>admin_password</i></p>
<h2>Description</h2>
<p>Un-registers the specified directory server instance from the console. </p>
<h2>Options</h2>
<p>A summary of options is included below:</p>
<dl>
<dt><code>-s server_id</code></p>
<dd>Required &#8211; server_id &#8211; the directory server identifier &#8211; slapd-<i>server_id</i></p>
<dt><code>-w password</code></p>
<dd>Required &#8211; password &#8211; the password for the console admin user. If password is &#8216;-&#8216;, prompt for the password.
</dl>
<h2>Author</h2>
<p>ds_unregister was written by the 389 Project.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to <a rel="nofollow" href="http://bugzilla.redhat.com.">http://bugzilla.redhat.com.</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2011 Red Hat, Inc.<br />
 This is free software. You may redistribute copies of it under the terms of the Directory Server license found in the LICENSE file of this software distribution. This license is essentially the GNU General Public License version 2 with an exception for plug-in distribution.</p>
