---
title: "ccs_config_dump(8)"
name: "ccs_config_dump"
section: "8"
letter: "c"
url: "/docs/linux/man/8-ccs_config_dump/"
description: "ccs_config_dump – Tool to generate XML output of running configuration."
---

<p>ccs_config_dump &#8211; Tool to generate XML output of running configuration. </p>
<h2>Synopsis</h2>
<p><code>ccs_config_dump</code> [<i>OPTION</i>].. </p>
<h2>Description</h2>
<p><code>ccs_config_dump</code> is part of the Cluster Configuration System (CCS). It is used to dump the current running configuration in XML format. The running configuration is, sometimes, different from the stored configuration on file or ldap because some subsystems store or set some default information into the configuration. Those values are generally not present on the on-disk version of the configuration but are required at runtime for the cluster to work properly. </p>
<h2>Options</h2>
<dl>
<dt><code>-h</code></p>
<dd>Help. Print out the usage.</p>
<dt><code>-V</code></p>
<dd>Print the version information.</p>
<dt><code>-r</code></p>
<dd>Force config dump from running cluster. This option is only for expert users and debugging sessions. Don&#8217;t use it for random purposes. ccs_config_dump can be configured to use different configuration sources via environment variables. This option will clear them to use the default and use only the runtime configuration. </p>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ccs_config_validate/">ccs_config_validate</a>(8), <a href="/docs/linux/man/5-cluster-conf/">cluster.conf</a>(5) </p>
