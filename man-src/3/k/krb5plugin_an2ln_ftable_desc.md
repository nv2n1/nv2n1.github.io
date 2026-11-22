---

title: "krb5plugin_an2ln_ftable_desc(3)"
name: "krb5plugin_an2ln_ftable_desc"
section: "3"
letter: "k"
url: "/docs/linux/man/3-krb5plugin_an2ln_ftable_desc/"
description: "krb5plugin_an2ln_ftable_desc –"
---

<p> krb5plugin_an2ln_ftable_desc &#8211; </p>
<p> Description of the </p>
<p>krb5_aname_to_lname(3) plugin facility. </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;an2ln_plugin.h&gt;</p>
<h2>Detailed Description</h2>
<p> Description of the krb5_aname_to_lname(3) plugin facility. </p>
<p> The krb5_aname_to_lname(3) function is pluggable. The plugin is named KRB5_PLUGIN_AN2LN (&#8216;an2ln&#8217;), with a single minor version, KRB5_PLUGIN_AN2LN_VERSION_0 (0). </p>
<p> The plugin for krb5_aname_to_lname(3) consists of a data symbol referencing a structure of type krb5plugin_an2ln_ftable, with four fields: </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
</dt><dd> <i>init</i> Plugin initialization function (see <a href="/docs/linux/man/7-krb5-plugin/">krb5-plugin</a>(7))<br/>
 <i>minor_version</i> The plugin minor version number (0)<br/>
 <i>fini</i> Plugin finalization function<br/>
 <i>an2ln</i> Plugin aname_to_lname function</dd></dl>
<p> The an2ln field is the plugin entry point that performs the traditional aname_to_lname operation however the plugin desires. It is invoked in no particular order relative to other an2ln plugins, but it has a &#8216;rule&#8217; argument that indicates which plugin is intended to act on the rule. The plugin an2ln function must return KRB5_PLUGIN_NO_HANDLE if the rule is not applicable to it. </p>
<p> The plugin an2ln function has the following arguments, in this order: </p>
<dl>
<dt>1.</dt>
<dd> plug_ctx, the context value output by the plugin&#8217;s init function</dd>
<dt>2.</dt>
<dd> context, a krb5_context</dd>
<dt>3.</dt>
<dd> rule, the aname_to_lname rule being evaluated (from <a href="/docs/linux/man/5-krb5-conf/">krb5.conf</a>(5))</dd>
<dt>4.</dt>
<dd> aname, the krb5_principal to be mapped to an lname</dd>
<dt>5.</dt>
<dd> set_res_f, a function the plugin must call to set its result</dd>
<dt>6.</dt>
<dd> set_res_ctx, the first argument to set_res_f (the second is the result lname string)</dd></dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for HeimdalKerberos5library from the source code. </p>
