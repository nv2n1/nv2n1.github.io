---
title: "softhsm2-conf(5)"
name: "softhsm2-conf"
section: "5"
letter: "s"
url: "/docs/linux/man/5-softhsm2-conf/"
description: "softhsm2.conf – SoftHSM configuration file"
---

<p>softhsm2.conf &#8211; SoftHSM configuration file</p>
<h2>Synopsis</h2>
<p><code>softhsm2.conf</code></p>
<h2>Description</h2>
<p>This is the configuration file for SoftHSM. It can be found on a default location, but can also be relocated by using the environment variable. Any configuration must be done according to the file format found in this document.</p>
<h2>File Format</h2>
<p>Each configuration option is a pair of name and value separated by a equality sign. The configuration option must be located on a single line. </p>
<dl>
<dd>
<pre>&lt;name&gt; = &lt;value&gt;</pre>
</dl>
<p> It is also possible to add comments in the file by using the hash sign. Anything after the hash sign will be ignored. </p>
<dl>
<dd>
<pre># A comment
</dl>
Any empty lines or lines that does not have the correct format will be ignored.</pre>
<h2>Directories.Tokendir</h2>
<p>The location where SoftHSM can store the tokens. </p>
<dl>
<dd>
<pre>directories.tokendir = /var/lib/softhsm/tokens/</pre>
</dl>
<h2>Objectstore.Backend</h2>
<p>The backend to use by SoftHSM to store token objects. Either &quot;file&quot; or &quot;db&quot; is supported. In order to use the &quot;db&quot; backend, the SoftHSM build needs to be configured with &quot;configure &#8211;with-objectstore-backend-db&quot; </p>
<dl>
<dd>
<pre>objectstore.backend = file</pre>
</dl>
<h2>Log.Level</h2>
<p>The log level which can be set to ERROR, WARNING, INFO or DEBUG. </p>
<dl>
<dd>
<pre>log.level = INFO</pre>
</dl>
<h2>Slots.Removable</h2>
<p>If set to true CKF_REMOVABLE_DEVICE is set in the flags returned by C_GetSlotInfo. Default is false. </p>
<dl>
<dd>
<pre>slots.removable = true</pre>
</dl>
<h2>Environment</h2>
<dl>
<dt>SOFTHSM2_CONF</p>
<dd>When defined, the value will be used as path to the configuration file.</dl>
<h2>Files</h2>
<dl>
<dt><i>~/.config/softhsm2/softhsm2.conf</i></p>
<dd>default user-specific location of the SoftHSM configuration file; if it exists it will override the system wide configuration</p>
<dt><i>/etc/softhsm2.conf</i></p>
<dd>default system-wide location of the SoftHSM configuration file</p>
<dt><i>/etc/softhsm2.conf.sample</i></p>
<dd>an example of a SoftHSM configuration file</dl>
<h2>Author</h2>
<p>Written by Rickard Bellgrim, Francis Dupont, René Post, and Roland van Rijswijk.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-softhsm2-keyconv/">softhsm2-keyconv</a></i>(1), <i><a href="/docs/linux/man/1-softhsm2-migrate/">softhsm2-migrate</a></i>(1), <i><a href="/docs/linux/man/1-softhsm2-util/">softhsm2-util</a></i>(1) </p>
