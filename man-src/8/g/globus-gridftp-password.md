---
title: "globus-gridftp-password(8)"
name: "globus-gridftp-password"
section: "8"
letter: "g"
url: "/docs/linux/man/8-globus-gridftp-password/"
description: "globus-gridftp-password – creates an encrypted password to be used for an user of the Globus GridFTP server"
---

<p>globus-gridftp-password &#8211; creates an encrypted password to be used for an user of the Globus GridFTP server</p>
<h2>Synopsys</h2>
<p><code>globus-gridftp-password </code></p>
<h2>Description</h2>
<p>Create encrypted user passwords to be used with the GridFTP server in case it is configured to use clear text password. However, this type of functionality is not recommended, unless the network is trusted. The <code>globus-gridftp-password</code> command asks for a password and generates a line in the same format as the standard password file (see file <code>/etc/passwd</code>). Such a line can be appended to the password file used by the GridFTP server. </p>
<h2>Example</h2>
<pre><code>% gridftp-password.pl &gt;&gt; pwfile</code>
<code> Password:</code></pre>
<p>Generates a password line for the current user and append it to file &quot;pwfile&quot;. <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<h2>Author</h2>
<p>Initiative for Globus in Europe (IGE), <a rel="nofollow" href="http://www.ige-project.eu">http://www.ige-project.eu</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2012 Initiative for Globus in Europe (IGE)</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-globus-gridftp-server/">globus-gridftp-server</a>(8) </p>
