---
title: "slapd(5)"
name: "slapd"
section: "5"
letter: "s"
url: "/docs/linux/man/5-slapd/"
description: "slapd.plugin – plugin configuration for slapd, the stand-alone LDAP daemon"
---

<p>slapd.plugin &#8211; plugin configuration for slapd, the stand-alone LDAP daemon</p>
<h2>Synopsis</h2>
<p>/etc/openldap/slapd.conf</p>
<h2>Description</h2>
<p>The <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5) file contains configuration information for the <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) daemon. This configuration file is also used by the SLAPD tools <code><a href="/docs/linux/man/8-slapadd/">slapadd</a></code>(8), <code><a href="/docs/linux/man/8-slapcat/">slapcat</a></code>(8), and <code><a href="/docs/linux/man/8-slapindex/">slapindex</a></code>(8). </p>
<p> The <code>slapd.conf</code> file consists of a series of global configuration options that apply to <code>slapd</code> as a whole (including all backends), followed by zero or more database backend definitions that contain information specific to a backend instance. </p>
<p> The general format of <code>slapd.conf</code> is as follows: </p>
<pre> # comment - these options apply to every database
 &lt;global configuration options&gt;
 # first database definition &amp; configuration options
 database &lt;backend 1 type&gt;
 &lt;configuration options specific to backend 1&gt;
 # subsequent database definitions &amp; configuration options
 ...</pre>
<p>If slapd is compiled with <i>&#8211;enable-slapi</i>, support for plugins according to <i>Netscape&#8217;s Directory Server Plug-Ins</i>. Version 4 of the API is currently implemented, with some extensions from version 5. </p>
<p> Both global and database specific data may contain plugin information. Plugins associated with a specific database are called before global plugins. This manpage details the <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) configuration statements that affect the loading of SLAPI <i>plugins</i>. </p>
<p> Arguments that should be replaced by actual text are shown in brackets &lt;&gt;. </p>
<p> The structure of the plugin directives is</p>
<dl>
<dt><code>plugin &lt;type&gt; &lt;lib_path&gt; &lt;init_function&gt; [&lt;arguments&gt;]</code></p>
<dd>Load a plugin of the specified type for the current database.</dl>
<p> The <code>&lt;type&gt;</code> can be one of <code>preoperation</code>, that is executed before processing the operation for the specified database, <code>postoperation</code>, that is executed after the operation for the specified database has been processed, <code>extendedop</code>, that is used when executing an extended operation, or <code>object</code>. The latter is used for miscellaneous types such as ACL, computed attribute and search filter rewriter plugins. </p>
<p> The <code>&lt;libpath&gt;</code> argument specifies the path to the plugin loadable object; if a relative path is given, the object is looked for according to the underlying dynamic loading package (libtool&#8217;s ltdl is used). </p>
<p> The <code>&lt;init_function&gt;</code> argument specifies what symbol must be called when the plugin is first loaded. This function should register the functions provided by the plugin for the desired operations. It should be noted that it is this init function, not the plugin type specified as the first argument, that determines when and for what operations the plugin will be invoked. The optional <code>&lt;arguments&gt;</code> list is passed to the init function.</p>
<dl>
<dt><code>pluginlog &lt;file&gt;</code></p>
<dd>Specify an alternative path for the plugin log file (default is /var/errors).</p>
<dt><code>modulepath &lt;pathspec&gt;</code></p>
<dd>This statement sets the module load path for dynamically loadable backends, as described in <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5); however, since both the dynamically loadable backends and the SLAPI plugins use the same underlying library (libtool&#8217;s ltdl) its value also affects the plugin search path. In general the search path is made of colon-separated paths; usually the user-defined path is searched first; then the value of the <i>LTDL_LIBRARY_PATH</i> environment variable, if defined, is used; finally, the system-specific dynamic load path is attempted (e.g. on Linux the value of the environment variable <i>LD_LIBRARY_PATH</i>). Please carefully read the documentation of ltdl because its behavior is very platform dependent.</dl>
<h2>Files</h2>
<dl>
<dt>/etc/openldap/slapd.conf</p>
<dd>default slapd configuration file</p>
<dt>/var/errors</p>
<dd>default plugin log file</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8), </p>
<p> &quot;OpenLDAP Administrator&#8217;s Guide&quot; (<a rel="nofollow" href="http://www.OpenLDAP.org/doc/admin/)">http://www.OpenLDAP.org/doc/admin/)</a></p>
<h2>Acknowledgements</h2>
<p><code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release.</p>
