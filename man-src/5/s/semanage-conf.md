---
title: "semanage-conf(5)"
name: "semanage-conf"
section: "5"
letter: "s"
url: "/docs/linux/man/5-semanage-conf/"
description: "semanage.conf – global configuration file for the SELinux Management library"
---

<p>semanage.conf &#8211; global configuration file for the SELinux Management library</p>
<h2>Description</h2>
<p>The <code>semanage.conf</code> file is usually located under the directory /etc/selinux and it is used for run-time configuration of the behavior of the SELinux Management library. Each line should contain a configuration parameter followed by the equal sign (&quot;=&quot;) and then followed by the configuration value for that parameter. Anything after the &quot;#&quot; symbol is ignored similarly to empty lines. The following parameters are allowed:</p>
<dl>
<dd>
<dl>
<dt><code>module-store </code></p>
<dd>Specify how the SELinux Management library should interact with the SELinux policy store. When set to &quot;direct&quot;, the SELinux Management library writes to the SELinux policy module store directly (this is the default setting). Otherwise a socket path or a server name can be used for the argument. If the argument begins with &quot;/&quot; (as in &quot;/foo/bar&quot;), it represents the path to a named socket that should be used to connect the policy management server. If the argument does not begin with a &quot;/&quot; (as in &quot;foo.com:4242&quot;), it should be interpreted as the name of a remote policy management server to be used through a TCP connection (default port is 4242 unless a different one is specified after the server name using the colon to separate the two fields).</p>
<dt><code>root</code></p>
<dd>Specify an alternative root path to use for the store. The default is &quot;/&quot;</p>
<dt><code>store-root</code></p>
<dd>Specify an alternative store_root path to use. The default is &quot;/var/lib/selinux&quot;</p>
<dt><code>compiler-directory</code></p>
<dd>Specify an alternative directory that contains HLL to CIL compilers. The default value is &quot;/usr/libexec/selinux/hll&quot;.</p>
<dt><code>ignore-module-cache</code></p>
<dd>Whether or not to ignore the cache of CIL modules compiled from HLL. It can be set to either &quot;true&quot; or &quot;false&quot; and is set to &quot;false&quot; by default. If the cache is ignored, then all CIL modules are recompiled from their HLL modules.</p>
<dt><code>policy-version </code></p>
<dd>When generating the policy, by default <code>semanage</code> will set the policy version to POLICYDB_VERSION_MAX, as defined in &lt;sepol/policydb/policydb.h&gt;. Change this setting if a different version needs to be set for the policy.</p>
<dt><code>target-platform</code></p>
<dd>The target platform to generate policies for. Valid values are &quot;selinux&quot; and &quot;xen&quot;, and is set to &quot;selinux&quot; by default.</p>
<dt><code>expand-check</code></p>
<dd>Whether or not to check &quot;neverallow&quot; rules when executing all <code>semanage</code> command. It can be set to either &quot;0&quot; (disabled) or &quot;1&quot; (enabled) and by default it is enabled. There might be a large penalty in execution time if this option is enabled.</p>
<dt><code>file-mode</code></p>
<dd>By default the permission mode for the run-time policy files is set to 0644.</p>
<dt><code>save-previous</code></p>
<dd>It controls whether the previous module directory is saved after a successful commit to the policy store and it can be set to either &quot;true&quot; or &quot;false&quot;. By default it is set to &quot;false&quot; (the previous version is deleted).</p>
<dt><code>save-linked</code></p>
<dd>It controls whether the previously linked module is saved (with name &quot;base.linked&quot;) after a successful commit to the policy store. It can be set to either &quot;true&quot; or &quot;false&quot; and by default it is set to &quot;false&quot; (the previous module is deleted).</p>
<dt><code>ignoredirs</code></p>
<dd>List, separated by &quot;;&quot;, of directories to ignore when setting up users homedirs. Some distributions use this to stop labeling /root as a homedir.</p>
<dt><code>usepasswd </code></p>
<dd>Whether or not to enable the use getpwent() to obtain a list of home directories to label. It can be set to either &quot;true&quot; or &quot;false&quot;. By default it is set to &quot;true&quot;.</p>
<dt><code>disable-genhomedircon</code></p>
<dd>It controls whether or not the genhomedircon function is executed when using the <code>semanage</code> command and it can be set to either &quot;false&quot; or &quot;true&quot;. By default the genhomedircon functionality is enabled (equivalent to this option set to &quot;false&quot;).</p>
<dt><code>handle-unknown</code></p>
<dd>This option overrides the kernel behavior for handling permissions defined in the kernel but missing from the actual policy. It can be set to &quot;deny&quot;, &quot;reject&quot; or &quot;allow&quot;. By default the setting from the policy is taken.</p>
<dt><code>bzip-blocksize</code></p>
<dd>It should be in the range 0-9. A value of 0 means no compression. By default the bzip block size is set to 9 (actual block size value is obtained after multiplication by 100000).</p>
<dt><code>bzip-small</code></p>
<dd>When set to &quot;true&quot;, the bzip algorithm shall try to reduce its system memory usage. It can be set to either &quot;true&quot; or &quot;false&quot; and by default it is set to &quot;false&quot;.</p>
<dt><code>remove-hll</code></p>
<dd>When set to &quot;true&quot;, HLL files will be removed after compilation into CIL. In order to delete HLL files already compiled into CIL, modules will need to be recompiled with the <code>ignore-module-cache</code> option set to &#8216;true&#8217; or using the <code>ignore-module-cache</code> option with semodule. The remove-hll option can be set to either &quot;true&quot; or &quot;false&quot; and by default it is set to &quot;false&quot;. Please note that since this option deletes all HLL files, an updated HLL compiler will not be able to recompile the original HLL file into CIL. In order to compile the original HLL file into CIL, the same HLL file will need to be reinstalled.</p>
<dt><code>optimize-policy</code></p>
<dd>When set to &quot;true&quot;, the kernel policy will be optimized upon rebuilds. It can be set to either &quot;true&quot; or &quot;false&quot; and by default it is set to &quot;false&quot;. </p>
<h2>See Also</h2>
<dl>
<dt><a href="/docs/linux/man/8-semanage/">semanage</a>(8)</p>
<dd></dl>
<h2>Author</h2>
<p>This manual page was written by Guido Trentalancia &lt;guido [at] trentalancia.com&gt;. </p>
<p> The SELinux management library was written by Tresys Technology LLC and Red Hat Inc.</p>
