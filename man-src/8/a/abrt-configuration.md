---
title: "abrt-configuration(8)"
name: "abrt-configuration"
section: "8"
letter: "a"
url: "/docs/linux/man/8-abrt-configuration/"
---

abrt-configuration - dbus server for reading/writing ABRT configuration

<h2>Synopsis</h2>

<i>abrt-configuration</i> [-v[v]...] [-t NUM]

<h2>Description</h2>

<i>abrt-configuration</i> allows other programs to read/write ABRT configuration over D-Bus. Normally <i>abrt-configuration</i> is started by D-Bus daemon on demand, and terminates after a timeout. The server listens on <i>com.redhat.problem.configuration</i> address on the system bus and exports the configuration as D-Bus objects identified by D-Bus path and D-Bus interface. The configuration objects are created from D-BUS Object Introspection XML files placed in /usr/share/problems/config/interfaces directory. Each file must contain exactly one <i>node</i> element with one <i>interface</i> element and the interface must contain only <i>property</i> elements. The node element must also have both <i>com.redhat.problems.configuration.ConfFile</i> and <i>com.rehdat.problems.configuration.DefaultConfFile</i> annotations elements which provide path to the working configuration file, where the changes are written, and to the default configuration file. <i>property</i> elements can also have the path annotations but they must be specified both or neither. 'propety's name must be equal to some option from the configuration files and its type must be one of the following D-Bus types: b,i,s,as. The server allows all users to read the configuration, but modifications are authorized over PolicyKit with <i>com.redhat.problem.configuration.update</i> policy.

<h3>Example of the configuration XML file:</h3>

<pre><code>&lt;node name=&quot;/com/redhat/problems/configuration/ccpp&quot;&gt;
&lt;annotation name=&quot;com.redhat.problems.ConfFile&quot; value=&quot;/etc/abrt/plugins/CCpp.conf&quot; /&gt;
&lt;annotation name=&quot;com.redhat.problems.DefaultConfFile&quot; value=&quot;/usr/share/abrt/conf.d/plugins/CCpp.conf&quot; /&gt;

&lt;interface name=&quot;com.redhat.problems.configuration.ccpp&quot;&gt;
&lt;property name=&quot;MakeCompatCore&quot; type=&quot;b&quot; access=&quot;readwrite&quot;/&gt;
&lt;property name=&quot;SaveBinaryImage&quot; type=&quot;b&quot; access=&quot;readwrite&quot;/&gt;
&lt;property name=&quot;VerboseLog&quot; type=&quot;i&quot; access=&quot;readwrite&quot;/&gt;
&lt;property name=&quot;DebuginfoLocation&quot; type=&quot;s&quot; access=&quot;readwrite&quot;/&gt;
&lt;/interface&gt;
&lt;/node&gt;</code></pre>

<h2>Options</h2>

-v
<dl><dd>Log more detailed debugging information.</dl>
 

 -t NUM
<dl><dd>Exit after NUM seconds of inactivity.</dl>

<h2>Authors</h2>

<dl><dd>&bull; ABRT team</dl>

<h2>See Also</h2>

<a HREF="/docs/linux/man/5-abrt-conf/">abrt.conf</a>(5) 
