---
title: "krb5plugin_db_ftable_desc(3)"
name: "krb5plugin_db_ftable_desc"
section: "3"
letter: "k"
url: "/docs/linux/man/3-krb5plugin_db_ftable_desc/"
description: "krb5plugin_db_ftable_desc –"
---

<h2 class="name">NAME</h2>
<p> krb5plugin_db_ftable_desc &#8211; </p>
<p> Description of the krb5 DB plugin facility.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;db_plugin.h&gt;</p>
<h2>Detailed Description</h2>
<p> Description of the krb5 DB plugin facility. </p>
<p> The <a href="/docs/linux/man/3-krb5_aname_to_lname/">krb5_aname_to_lname</a>(3) function&#8217;s DB rule is pluggable. The plugin is named KRB5_PLUGIN_DB (&#8216;krb5_db_plug&#8217;), with a single minor version, KRB5_PLUGIN_DB_VERSION_0 (0). </p>
<p> The plugin consists of a data symbol referencing a structure of type <code>krb5plugin_db_ftable_desc</code>, with three fields: </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>init</i> Plugin initialization function (see <a href="/docs/linux/man/7-krb5-plugin/">krb5-plugin</a>(7))<br />
 <i>minor_version</i> The plugin minor version number (0)<br />
 <i>fini</i> Plugin finalization function</dl>
<p> The init entry point is expected to call heim_db_register(). The fini entry point is expected to do nothing. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for HeimdalKerberos5library from the source code. </p>
<h2>Index</h2>
