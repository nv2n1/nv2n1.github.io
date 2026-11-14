---
title: "pva-dbschema-update(1)"
name: "pva-dbschema-update"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pva-dbschema-update/"
description: "pva-dbschema-update – PHP VOMS-Admin(PVA) tool to update database schema to the latest version"
---

<h2 class="name">NAME</h2>
<p> pva-dbschema-update &#8211; PHP VOMS-Admin(PVA) tool to update database schema to the latest version</p>
<h2>DESCRIPTION</h2>
<p> The <code>pva-dbschema-update</code> command update database schema to the latest version required for PHP VOMS-Admin operation. </p>
<h2>SYNOPSIS</h2>
<p> <code>pva-dbschema-update [-f] [-h &lt;host&gt;] -d &lt;database&gt; -u &lt;user&gt; -p &lt;password&gt;</code> </p>
<h2>ARGUMENTS</h2>
<dl>
<dt><code>-f</code></p>
<dd> force database schema update invocation (assuming database version is oldest)</dl>
<dl>
<dt><code>-h &lt;host&gt;</code></p>
<dd> database server host (localhost is used by default)</dl>
<dl>
<dt><code>-d &lt;database&gt;</code></p>
<dd> target database name for schema update</dl>
<dl>
<dt><code>-u &lt;user&gt;</code></p>
<dd> username to access database on server</dl>
<dl>
<dt><code>-p &lt;password&gt;</code></p>
<dd> passwoed to access database on server</dl>
<h2>EXTENDED DESCRIPTION</h2>
<p> The <code>pva-dbschema-update </code> command designed to be called within package post-install script to authomatically update all served VO databases on PHP VOMS-Admin update. </p>
<p> In case database migration from another server that runs older version of PHP VOMS-Admin it is required to update database schema manually. </p>
<h2>EXAMPLE</h2>
<p> pva-dbschema-update -d voms_testbed -u voms_user -p P@ssw0rd </p>
<h2>COPYRIGHT</h2>
<p> APACHE LICENSE Version 2.0 </p>
<h2>AUTHOR</h2>
<p> Andrii Salnikov &lt;manf [at] grid.org.ua&gt; </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pva-addvo/">pva-addvo</a></code>(1), <code><a href="/docs/linux/man/5-pva-config/">pva-config</a></code>(5), <code><a href="/docs/linux/man/8-voms/">voms</a></code>(8) </p>
<h2>Index</h2>
