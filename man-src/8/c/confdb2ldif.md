---
title: "confdb2ldif(8)"
name: "confdb2ldif"
section: "8"
letter: "c"
url: "/docs/linux/man/8-confdb2ldif/"
description: "confdb2ldif – Create an LDIF file from a cluster configuration"
---

<p>confdb2ldif &#8211; Create an LDIF file from a cluster configuration</p>
<h2>Synopsis</h2>
<p><code>confdb2ldap &lt;basedn&gt; [&lt;config object base&gt;]</code> </p>
<h2>Description</h2>
<p><code>confdb2ldif</code> reads the cluster configuration from the openais object database and generates an LDIF file suitable for importing into an LDAP database. The LDIF file is written to standard output. </p>
<h2>Options</h2>
<dl>
<dt><code>&lt;basedn&gt;</code></p>
<dd>This is the base DN of the LDAP server into which the configuration will be imported. confdb2ldif will create a &quot;cn=cluster&quot; object below this to contain the cluster configuration. The base DN is usually derived from the host&#8217;s domain name. So if the host is ldapsrv.mycorp.com then the base DN could be dc=mycorp,dc=com.</p>
<dt><code>[&lt;config object base&gt;]</code></p>
<dd>Configuration object in the objdb to start from. This defaults to &quot;cluster&quot; and there should rarely be any need to change it. </p>
</dl>
<h2>Comments</h2>
<p><code>confdb2ldif</code> uses the openais libconfdb to read the configuration. The default way to do this is run against a running aisexec to read the live configuration. It is possible to generate an LDIF file from a non-running system by using the standalone feature of openais&#8217;s libconfdb.<br />
 eg to read the configuration from /etc/cluster/cluster.conf, use the following command: </p>
<pre>OPENAIS_DEFAULT_CONFIG_IFACE=xmlconfig:cmanpreconfig confdb2ldif dc=mycompany,dc=com</pre>
<p>or to do it from CCS </p>
<pre>OPENAIS_DEFAULT_CONFIG_IFACE=ccsconfig:cmanpreconfig confdb2ldif dc=mycompany,dc=com</pre>
<p>The LDIF file is written to stdout and so can be saved or piped straight into ldapmodify if required. </p>
<p> It&#8217;s important that the 99cluster.ldif schema file has been loaded into the LDAP server before adding the contents of this generated LDIF file.</p>
<h2>Example</h2>
<pre>confdb2ldif dc=mycorp,dc=com | ldapmodify -x -a -D&quot;cn=Directory Manager&quot; -c -v -W</pre>
<h2>Bugs</h2>
<p><code>confdb2ldif</code> parses the cluster configuration without checking it against the loaded schema. So if there are attributes in the config file that are not known to the schema, parts of the load will fail. It is important to check the results of feeding the output into ldapmodify. In particular aisexec logging operations will not convert into LDIF because they rely on duplicate keys. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-libconfdb/">libconfdb</a>(3), <a href="/docs/linux/man/8-openais/">openais</a>(8), <a href="/docs/linux/man/5-cluster-conf/">cluster.conf</a>(5) </p>
