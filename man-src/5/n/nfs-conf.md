---
title: "nfs-conf(5)"
name: "nfs-conf"
section: "5"
letter: "n"
url: "/docs/linux/man/5-nfs-conf/"
description: "nfs.conf – general configuration for NFS daemons and tools"
---

<p>nfs.conf &#8211; general configuration for NFS daemons and tools</p>
<h2>Synopsis</h2>
<p><i>/etc/nfs.conf</i></p>
<h2>Description</h2>
<p>This file contains site-specific configuration for various NFS daemons and other processes. Most configuration can also be passed to processes via command line arguments, but it can be more convenient to have a central file. In particular, this encourages consistent configuration across different processes. When command line options are provided, they override values set in this file. When this file does not specify a particular parameter, and no command line option is provided, each tool provides its own default values. The file format supports multiple sections, each of which can contain multiple value assignments. A section is introduced by a line containing the section name enclosed in square brackets, so</p>
<dl>
<dd><code>[global]</code></dl>
<p> would introduce a section called <code>global</code>. A value assignment is a single line that has the name of the value, an equals sign, and a setting for the value, so</p>
<dl>
<dd><code>threads = 4</code></dl>
<p> would set the value named <code>threads</code> in the current section to <code>4</code>. Leading and trailing spaces and tab are ignored, as are spaces and tabs surrounding the equals sign. Single and double quotes surrounding the assigned value are also removed. If the resulting string is empty, the whole assignment is ignored. Any line starting with &#8220;<code>#</code>&#8221; or &#8220;<code>;</code>&#8221; is ignored, as is any blank line. If the assigned value started with a &#8220;<code>$</code>&#8221; then the remainder is treated as a name and looked for in the section <code>[environment]</code> or in the processes environment (see <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7)). The value found is used for this value. The value name <code>include</code> is special. If a section contains</p>
<dl>
<dd><code>include = /some/file/name</code></dl>
<p> then the named file will be read, and any value assignments found there-in will be added to the current section. If the file contains section headers, then new sections will be created just as if the included file appeared in place of the <code>include</code> line. Lookup of section and value names is case-insensitive. Where a Boolean value is expected, any of <code>true</code>, <code>t</code>, <code>yes</code>, <code>y</code>, <code>on</code>, or <code>1</code> can be used for &quot;true&quot;, while <code>false</code>, <code>f</code>, <code>no</code>, <code>n</code>, <code>off</code>, or <code>0</code> can be used for &quot;false&quot;. Comparisons are case-insensitive. </p>
<h2>Sections</h2>
<p>The following sections are known to various programs, and can contain the given named values. Most sections can also contain a <code>debug</code> value, which can be one or more from the list <code>general</code>, <code>call</code>, <code>auth</code>, <code>parse</code>, <code>all</code>. When a list is given, the members should be comma-separated.</p>
<dl>
<dt><code>nfsdcltrack</code></p>
<dd>Recognized values: <code>storagedir</code>. </p>
<p> The <code>nfsdcltrack</code> program is run directly by the Linux kernel and there is no opportunity to provide command line arguments, so the configuration file is the only way to configure this program. See <code><a href="/docs/linux/man/8-nfsdcltrack/">nfsdcltrack</a></code>(8) for details. </p>
<dt><code>nfsd</code></p>
<dd>Recognized values: <code>threads</code>, <code>host</code>, <code>port</code>, <code>grace-time</code>, <code>lease-time</code>, <code>udp</code>, <code>tcp</code>, <code>vers2</code>, <code>vers3</code>, <code>vers4</code>, <code>vers4.0</code>, <code>vers4.1</code>, <code>vers4.2</code>, <code>rdma</code>. </p>
<p> Version and protocol values are Boolean values as described above, and are also used by <code>rpc.mountd</code>. Threads and the two times are integers. <code>port</code> and <code>rdma</code> are service names or numbers. See <code><a href="/docs/linux/man/8-rpc-nfsd/">rpc.nfsd</a></code>(8) for details. </p>
<dt><code>mountd</code></p>
<dd>Recognized values: <code>manage-gids</code>, <code>descriptors</code>, <code>port</code>, <code>threads</code>, <code>reverse-lookup</code>, <code>state-directory-path</code>, <code>ha-callout</code>. </p>
<p> These, together with the protocol and version values in the <code>[nfsd]</code> section, are used to configure mountd. See <code><a href="/docs/linux/man/8-rpc-mountd/">rpc.mountd</a></code>(8) for details. </p>
<dt><code>statd</code></p>
<dd>Recognized values: <code>port</code>, <code>outgoing-port</code>, <code>name</code>, <code>state-directory-path</code>, <code>ha-callout</code>. </p>
<p> See <code><a href="/docs/linux/man/8-rpc-statd/">rpc.statd</a></code>(8) for details. </p>
<dt><code>lockd</code></p>
<dd>Recognized values: <code>port</code> and <code>udp-port</code>. </p>
<p> See <code><a href="/docs/linux/man/8-rpc-statd/">rpc.statd</a></code>(8) for details. </p>
<dt><code>sm-notify</code></p>
<dd>Recognized values: <code>retry-time</code>, <code>outgoing-port</code>, and <code>outgoing-addr</code>. </p>
<p> See <code><a href="/docs/linux/man/8-sm-notify/">sm-notify</a></code>(8) for details. </p>
<dt><code>gssd</code></p>
<dd>Recognized values: <code>use-memcache</code>, <code>use-machine-creds</code>, <code>avoid-dns</code>, <code>limit-to-legacy-enctypes</code>, <code>context-timeout</code>, <code>rpc-timeout</code>, <code>pipefs-directory</code>, <code>keytab-file</code>, <code>cred-cache-directory</code>, <code>preferred-realm</code>. </p>
<p> See <code><a href="/docs/linux/man/8-rpc-gssd/">rpc.gssd</a></code>(8) for details. </p>
<dt><code>exportfs</code></p>
<dd>Only <code>debug=</code> is recognized. </p>
</dl>
<h2>Files</h2>
<p><i>/etc/nfs.conf</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-nfsdcltrack/">nfsdcltrack</a></code>(8), <code><a href="/docs/linux/man/8-rpc-nfsd/">rpc.nfsd</a></code>(8), <code><a href="/docs/linux/man/8-rpc-mountd/">rpc.mountd</a></code>(8), <code><a href="/docs/linux/man/5-nfsmount-conf/">nfsmount.conf</a></code>(5). </p>
