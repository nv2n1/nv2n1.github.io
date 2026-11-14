---
title: "host(5)"
name: "host"
section: "5"
letter: "h"
url: "/docs/linux/man/5-host/"
description: "host.conf – resolver configuration file"
---

<p>host.conf &#8211; resolver configuration file</p>
<h2>Description</h2>
<p>The file <i>/etc/host.conf</i> contains configuration information specific to the resolver library. It should contain one configuration keyword per line, followed by appropriate configuration information. The keywords recognized are <i>trim</i>, <i>multi</i>, <i>nospoof</i>, <i>spoof</i>, and <i>reorder</i>. These keywords are described below.</p>
<dl>
<dt><i>trim</i></p>
<dd>This keyword may be listed more than once. Each time it should be followed by a list of domains, separated by colons (&#8216;:&#8217;), semicolons (&#8216;;&#8217;) or commas (&#8216;,&#8217;), with the leading dot. When set, the resolv+ library will automatically trim the given domain name from the end of any hostname resolved via DNS. This is intended for use with local hosts and domains. (Related note: trim will not affect hostnames gathered via NIS or the hosts file. Care should be taken to ensure that the first hostname for each entry in the hosts file is fully qualified or unqualified, as appropriate for the local installation.)</p>
<dt><i>multi</i></p>
<dd>Valid values are <i>on</i> and <i>off</i>. If set to <i>on</i>, the resolv+ library will return all valid addresses for a host that appears in the <i>/etc/hosts</i> file, instead of only the first. This is <i>off</i> by default, as it may cause a substantial performance loss at sites with large hosts files.</p>
<dt><i>nospoof</i></p>
<dd>Valid values are <i>on</i> and <i>off</i>. If set to <i>on</i>, the resolv+ library will attempt to prevent hostname spoofing to enhance the security of <code>rlogin</code> and <code>rsh</code>. It works as follows: after performing a host address lookup, resolv+ will perform a hostname lookup for that address. If the two hostnames do not match, the query will fail. The default value is <i>off</i>.</p>
<dt><i>spoofalert</i></p>
<dd>Valid values are <i>on</i> and <i>off</i>. If this option is set to <i>on</i> and the <i>nospoof</i> option is also set, resolv+ will log a warning of the error via the syslog facility. The default value is <i>off</i>.</p>
<dt><i>spoof</i></p>
<dd>Valid values are <i>off</i>, <i>nowarn</i> and <i>warn</i>. If this option is set to <i>off</i>, spoofed addresses are permitted and no warnings will be emitted via the syslog facility. If this option is set to <i>warn</i>, resolv+ will attempt to prevent hostname spoofing to enhance the security and log a warning of the error via the syslog facility. If this option is set to <i>nowarn</i>, the resolv+ library will attempt to prevent hostname spoofing to enhance the security but not emit warnings via the syslog facility. Setting this option to anything else is equal to setting it to <i>nowarn</i>.</p>
<dt><i>reorder</i></p>
<dd>Valid values are <i>on</i> and <i>off</i>. If set to <i>on</i>, resolv+ will attempt to reorder host addresses so that local addresses (i.e., on the same subnet) are listed first when a <code><a href="/docs/linux/man/3-gethostbyname/">gethostbyname</a></code>(3) is performed. Reordering is done for all lookup methods. The default value is <i>off</i>.</dl>
<h2>Environment</h2>
<p>There are six environment variables that can be used to allow users to override the behavior which is configured in <i>/etc/host.conf</i>.</p>
<dl>
<dt><code>RESOLV_HOST_CONF</code></p>
<dd>If set, this variable points to a file that should be read instead of <i>/etc/host.conf</i>.</p>
<dt><code>RESOLV_SPOOF_CHECK</code></p>
<dd>Overrides the <i>nospoof</i>, <i>spoofalert</i> and <i>spoof</i> commands in the same way as the <i>spoof</i> command is parsed. Valid values are <i>off</i>, <i>nowarn</i> and <i>warn</i>.</p>
<dt><code>RESOLV_MULTI</code></p>
<dd>Overrides the <i>multi</i> command.</p>
<dt><code>RESOLV_REORDER</code></p>
<dd>Overrides the <i>reorder</i> command.</p>
<dt><code>RESOLV_ADD_TRIM_DOMAINS</code></p>
<dd>A list of domains, separated by colons (&#8216;:&#8217;), semicolons (&#8216;;&#8217;) or commas (&#8216;,&#8217;), with the leading dot, which will be added to the list of domains that should be trimmed.</p>
<dt><code>RESOLV_OVERRIDE_TRIM_DOMAINS</code></p>
<dd>A list of domains, separated by colons (&#8216;:&#8217;), semicolons (&#8216;;&#8217;) or commas (&#8216;,&#8217;), with the leading dot, which will replace the list of domains that should be trimmed. Overrides the <i>trim</i> command.</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/host.conf</i></p>
<dd>Resolver configuration file</p>
<dt><i>/etc/resolv.conf</i></p>
<dd>Resolver configuration file</p>
<dt><i>/etc/hosts</i></p>
<dd>Local hosts database</dl>
<h2>Notes</h2>
<p>The following differences exist compared to the original implementation. A new command <i>spoof</i> and a new environment variable <code>RESOLV_SPOOF_CHECK</code> can take arguments like <i>off</i>, <i>nowarn</i> and <i>warn</i>. Line comments can appear anywhere and not only at the beginning of a line.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-gethostbyname/">gethostbyname</a></code>(3), <code><a href="/docs/linux/man/7-hostname/">hostname</a></code>(7), <code><a href="/docs/linux/man/8-named/">named</a></code>(8), <code>resolv+</code>(8)</p>
<h2>Colophon</h2>
<p>This page is part of release 3.69 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="http://www.kernel.org/doc/man-pages/.">http://www.kernel.org/doc/man-pages/.</a> </p>
