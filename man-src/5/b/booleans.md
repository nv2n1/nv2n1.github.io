---
title: "booleans(5)"
name: "booleans"
section: "5"
letter: "b"
url: "/docs/linux/man/5-booleans/"
description: "booleans – The SELinux booleans configuration files"
---

<p>booleans &#8211; The SELinux booleans configuration files</p>
<h2>Description</h2>
<p>The <i>booleans</i> file, if present contains booleans to support a specific distribution. </p>
<p> The <i>booleans.local</i> file, if present contains locally generated booleans. </p>
<p> Both files contain a list of boolean names and their associated values. </p>
<p> Generally the <i>booleans</i> and/or <i>booleans.local</i> files are not present (they have been deprecated). However if there is an SELinux-aware application that uses the libselinux functions listed below, then these files may be present: </p>
<dl>
<dd><code><a href="/docs/linux/man/3-security_set_boolean_list/">security_set_boolean_list</a></code>(3)</p>
<dl>
<dd>Writes a <i>booleans.local</i> file if flag <i>permanent</i> = <i>1</i>. </p>
</dl>
</dl>
<dl>
<dd><code><a href="/docs/linux/man/3-security_load_booleans/">security_load_booleans</a></code>(3)</p>
<dl>
<dd>Looks for a <i>booleans</i> and/or <i>booleans.local</i> file at <code><a href="/docs/linux/man/3-selinux_booleans_path/">selinux_booleans_path</a></code>(3) unless a specific path is specified as a parameter.</dl>
</dl>
<p> <code><a href="/docs/linux/man/8-booleans/">booleans</a></code>(8) has details on booleans and <code><a href="/docs/linux/man/8-setsebool/">setsebool</a></code>(8) describes how booleans can now be set persistent across reboots. </p>
<p> <code><a href="/docs/linux/man/3-selinux_booleans_path/">selinux_booleans_path</a></code>(3) will return the active policy path to these files. The default boolean files are:</p>
<dl>
<dd><i>/etc/selinux/{SELINUXTYPE}/booleans</i><br />
 <i>/etc/selinux/{SELINUXTYPE}/booleans.local</i></dl>
<p> Where <i>{SELINUXTYPE}</i> is the entry from the selinux configuration file <i>config</i> (see <code><a href="/docs/linux/man/5-selinux_config/">selinux_config</a></code>(5)).</p>
<h2>File Format</h2>
<p>Both boolean files have the same format and contain one or more boolean names and their value. </p>
<p> The format is:</p>
<dl>
<dd><i>boolean_name</i> <i>value</i> </p>
</dl>
<p> Where:</p>
<dl>
<dd><i>boolean_name</i></p>
<dl>
<dd>The name of the boolean.</dl>
<p> <i>value</i></p>
<dl>
<dd>The default setting for the boolean. This can be one of the following:</p>
<dl>
<dd><i>true</i> | <i>false</i> | <i>1</i> | <i>0</i></dl>
</dl>
</dl>
<p> Note that if <code>SETLOCALDEFS</code> is set in the SELinux <i>config</i> file (see <code><a href="/docs/linux/man/5-selinux_config/">selinux_config</a></code>(5)), then <code><a href="/docs/linux/man/3-selinux_mkload_policy/">selinux_mkload_policy</a></code>(3) will check for a <i>booleans.local</i> file in the <code><a href="/docs/linux/man/3-selinux_booleans_path/">selinux_booleans_path</a></code>(3) and also a <i>local.users</i> file (see <code><a href="/docs/linux/man/5-local-users/">local.users</a></code>(5)) in the <code><a href="/docs/linux/man/3-selinux_users_path/">selinux_users_path</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8), <code><a href="/docs/linux/man/8-booleans/">booleans</a></code>(8), <code><a href="/docs/linux/man/8-setsebool/">setsebool</a></code>(8), <code><a href="/docs/linux/man/8-semanage/">semanage</a></code>(8), <code><a href="/docs/linux/man/3-selinux_booleans_path/">selinux_booleans_path</a></code>(3), <code><a href="/docs/linux/man/3-security_set_boolean_list/">security_set_boolean_list</a></code>(3), <code><a href="/docs/linux/man/3-security_load_booleans/">security_load_booleans</a></code>(3), <code><a href="/docs/linux/man/3-selinux_mkload_policy/">selinux_mkload_policy</a></code>(3), <code><a href="/docs/linux/man/3-selinux_users_path/">selinux_users_path</a></code>(3), <code><a href="/docs/linux/man/5-selinux_config/">selinux_config</a></code>(5), <code><a href="/docs/linux/man/5-local-users/">local.users</a></code>(5) </p>
