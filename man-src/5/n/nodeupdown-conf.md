---
title: "nodeupdown-conf(5)"
name: "nodeupdown-conf"
section: "5"
letter: "n"
url: "/docs/linux/man/5-nodeupdown-conf/"
description: "nodeupdown.conf – specify alternate default values for the nodeupdown library"
---

<p>nodeupdown.conf &#8211; specify alternate default values for the nodeupdown library</p>
<h2>Description</h2>
<p>Through a configuration file, system administrators may override the default values used in the <code><a href="/docs/linux/man/3-nodeupdown_load_data/">nodeupdown_load_data</a>(3)</code> API function. The configuration specified in this file takes precedence over any configuration values found in a configuration module. The configuration file is stored at /etc/nodeupdown.conf. </p>
<h2>Configuration Options</h2>
<p>The following are a list of configuration options that can be specified in the configuration file. Each configuration option must be listed on a separate line. Arguments for an option are separated by any amount of whitespace. Multiple arguments are also separated by whitespace. Comments can be marked by using the pound sign (&quot;#&quot;) character, and lines can be continued on the next using backslash (&quot;\&quot;). </p>
<dl>
<dt><i>hostnames host1 host2 host3 &#8230;</i></p>
<dd>Specify the hostname of the server to reach. Multiple hostnames can be listed up to a maximum of 8.</p>
<dt><i>port num</i></p>
<dd>Specify the port.</p>
<dt><i>timeout_len seconds</i></p>
<dd>Specify the timeout length in seconds.</dl>
<h2>Files</h2>
<p>/etc/nodeupdown.conf</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-whatsup/">whatsup</a>(1), <a href="/docs/linux/man/3-libnodeupdown/">libnodeupdown</a>(3), <a href="/docs/linux/man/3-nodeupdown_load_data/">nodeupdown_load_data</a>(3) </p>
