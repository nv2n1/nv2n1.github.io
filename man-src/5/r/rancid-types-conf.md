---
title: "rancid-types-conf(5)"
name: "rancid-types-conf"
section: "5"
letter: "r"
url: "/docs/linux/man/5-rancid-types-conf/"
description: "rancid.types.conf – rancid device type configuration file"
---

<p>rancid.types.conf &#8211; rancid device type configuration file</p>
<h2>Description</h2>
<p><code>rancid.types.conf</code> contains formatted configuration lines that define the device types that are available for use in the &lt;device_type&gt; field of the <code><a href="/docs/linux/man/5-router-db/">router.db</a></code>(5) configuration file. </p>
<p> The <code>rancid.types.base</code> configuration file follows the same format but defines the base types described in <i><a href="/docs/linux/man/5-router-db/">router.db</a>(5).</i> </p>
<p> Users are <code>STRONGLY</code> discouraged from altering this file or overriding the base types in <code>rancid.types.conf.</code> Instead, copy the type definition to be altered from <code>rancid.types.base</code> to <code>rancid.types.conf</code> using a different &lt;device_type&gt;.</p>
<h2>Syntax</h2>
<p>One directive is listed per-line, where the syntax is one of: </p>
<pre>&lt;device_type&gt;;command;&lt;filter_function&gt;;&lt;device_command_string&gt;
&lt;device_type&gt;;inloop;&lt;input_loop_function&gt;
&lt;device_type&gt;;login;&lt;login_program&gt;
&lt;device_type&gt;;module;&lt;perl_module_name&gt;
&lt;device_type&gt;;prescript;&lt;rancid_script&gt; XXX temporary knob? add this?
&lt;device_type&gt;;postscript;&lt;rancid_script&gt; XXX temporary knob? add this?
&lt;device_type&gt;;script;&lt;rancid_script&gt;</pre>
<p>For example: </p>
<pre>cisco;login;clogin
cisco;module;rancid::ios
cisco;inloop;ios::inloop
cisco;command;ShowVersion;show version
juniper;login;/usr/local/bin/jlogin
juniper;module;rancid::junos
juniper;inloop;junos::inloop
juniper;command;ShowVersion;show version</pre>
<p>&lt;device_type&gt; is a lower case name used in the <i><a href="/docs/linux/man/5-router-db/">router.db</a>(5)</i> file. Its case is forced to lower case when reading the configuration files. </p>
<p> Each &lt;device_type&gt; may have the following directives defined. The login and script directives are required.</p>
<dl>
<dt><code>command</code></p>
<dd>Defines commands to run for the &lt;device_type&gt; and the function that will process the input.</p>
<dt><code>inloop</code></p>
<dd>Intended for <i><a href="/docs/linux/man/1-rancid/">rancid</a>(1),</i> <code>inloop</code> defines a function to loop over the input from the device.</p>
<dt><code>login</code></p>
<dd>Defines the login script used for the &lt;device_type&gt;, which does not need to be an FQPN, but then must be found in the path.</p>
<dt><code>module</code></p>
<dd>Loads a rancid perl module to supply functions used in the <code>command</code> directives for the &lt;device_type&gt;. Multiple module lines may exist for a device type, they are loaded in the order they appear.</p>
<dt><code>script</code></p>
<dd>Defines the rancid script used for the &lt;device_type&gt;, which does not need to be an FQPN, but then must be found in the path.</dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/rancid/rancid.types.conf</code></p>
<dd>Configuration file described here.</p>
<dt><code>/etc/rancid/rancid.types.base</code></p>
<dd>Configuration file described here.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-control_rancid/">control_rancid</a></code>(1), <code><a href="/docs/linux/man/1-rancid/">rancid</a></code>(1), <code><a href="/docs/linux/man/1-rancid-run/">rancid-run</a></code>(1), <code><a href="/docs/linux/man/5-router-db/">router.db</a></code>(5), <code><a href="/docs/linux/man/3-rancid/">rancid</a></code>(3) </p>
