---
title: "krb5plugin_kuserok_ftable_desc(3)"
name: "krb5plugin_kuserok_ftable_desc"
section: "3"
letter: "k"
url: "/docs/linux/man/3-krb5plugin_kuserok_ftable_desc/"
description: "krb5plugin_kuserok_ftable_desc –"
---

<h2 class="name">NAME</h2>
<p> krb5plugin_kuserok_ftable_desc &#8211; </p>
<p> Description of the </p>
<p><a href="/docs/linux/man/3-krb5_kuserok/">krb5_kuserok</a>(3) plugin facility. </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;kuserok_plugin.h&gt;</p>
<h2>Detailed Description</h2>
<p> Description of the <a href="/docs/linux/man/3-krb5_kuserok/">krb5_kuserok</a>(3) plugin facility. </p>
<p> The <a href="/docs/linux/man/3-krb5_kuserok/">krb5_kuserok</a>(3) function is pluggable. The plugin is named KRB5_PLUGIN_KUSEROK (&#8216;krb5_plugin_kuserok&#8217;), with a single minor version, KRB5_PLUGIN_KUSEROK_VERSION_0 (0). </p>
<p> The plugin for <a href="/docs/linux/man/3-krb5_kuserok/">krb5_kuserok</a>(3) consists of a data symbol referencing a structure of type krb5plugin_kuserok_ftable, with four fields: </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>init</i> Plugin initialization function (see <a href="/docs/linux/man/7-krb5-plugin/">krb5-plugin</a>(7))<br />
 <i>minor_version</i> The plugin minor version number (0)<br />
 <i>fini</i> Plugin finalization function<br />
 <i>kuserok</i> Plugin kuserok function</dl>
<p> The kuserok field is the plugin entry point that performs the traditional kuserok operation however the plugin desires. It is invoked in no particular order relative to other kuserok plugins, but it has a &#8216;rule&#8217; argument that indicates which plugin is intended to act on the rule. The plugin kuserok function must return KRB5_PLUGIN_NO_HANDLE if the rule is not applicable to it. </p>
<p> The plugin kuserok function has the following arguments, in this order: </p>
<dl>
<dt>1.</p>
<dd> plug_ctx, the context value output by the plugin&#8217;s init function</p>
<dt>2.</p>
<dd> context, a krb5_context</p>
<dt>3.</p>
<dd> rule, the kuserok rule being evaluated (from <a href="/docs/linux/man/5-krb5-conf/">krb5.conf</a>(5))</p>
<dt>4.</p>
<dd> flags</p>
<dt>5.</p>
<dd> k5login_dir, configured location of k5login per-user files if any</p>
<dt>6.</p>
<dd> luser, name of the local user account to which principal is attempting to access.</p>
<dt>7.</p>
<dd> principal, the krb5_principal trying to access the luser account</p>
<dt>8.</p>
<dd> result, a krb5_boolean pointer where the plugin will output its result</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for HeimdalKerberos5library from the source code. </p>
<h2>Index</h2>
