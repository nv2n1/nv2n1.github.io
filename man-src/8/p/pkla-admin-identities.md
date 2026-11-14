---
title: "pkla-admin-identities(8)"
name: "pkla-admin-identities"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pkla-admin-identities/"
description: "pkla-admin-identities – List pklocalauthority-configured polkit administrators"
---

<p>pkla-admin-identities &#8211; List pklocalauthority-configured polkit administrators</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pkla-admin-identities</code> [<code>&#8211;help</code>]</p>
<dt> <code>pkla-admin-identities</code> [<code>&#8211;config-path</code>&nbsp;<wbr><i>config-path</i>]</dl>
<h2>Description</h2>
<p><code>pkla-admin-identities</code></p>
<dd>interprets configuration files described below to determine which users <code><a href="/docs/linux/man/8-polkit/">polkit</a></code>(8) considers administrators, using a non-JavaScript configuration file format described below. </p>
<p> <i>Note:</i> Determining which users are considered administrators is driven by JavaScript rules as described in <code><a href="/docs/linux/man/8-polkit/">polkit</a></code>(8). <code>pkla-admin-identities</code> is called by a JavaScript rule file named 49-polkit-pkla-compat.rules; other JavaScript rules with a higher priority may exist, so the <code>pkla-admin-identities</code> configuration may not necessarily govern the final decision by <code><a href="/docs/linux/man/8-polkit/">polkit</a></code>(8). </p>
<p> The ordering of the JavaScript rule files and the ordering of <code>pkla-admin-identities</code> configuration files is not integrated and uses different rules; the <code>pkla-admin-identities</code> configuration evaluation is happens at a single point within the JavaScript rule evaluation order. </p>
<p> <code>pkla-admin-identities</code> is an internal helper program of pkla-polkit-compat. You shouldn&#8217;t need to run it directly, except for debugging purposes. </p>
<p> Configuration is read from files with a .conf extension in the /etc/polkit-1/localauthority.conf.d directory. All files are read in lexicographical order (using the C locale), meaning that later files can override earlier ones. The file 50-localauthority.conf contains the settings provided by the OS vendor. Users and 3rd party packages can drop configuration files with a priority higher than 60 to change the defaults. The configuration file format is simple. Each configuration file is a <i>key file</i> (also commonly known as a <i>ini file</i>) with a single group called [Configuration]. Only a single key, AdminIdentities is read. The value of this key is a semi-colon separated list of identities that can be used when administrator authentication is required. Users are specified by prefixing the user name with unix-user:, groups of users are specified by prefixing with unix-group:, and netgroups of users are specified with unix-netgroup:. See the section called &#8220;EXAMPLE&#8221; for an example of a configuration file. </p>
<p> <code>pkla-admin-identities</code> outputs the resulting configuration of administrator identities, one identity per line, using the same format (including e.g. the unix-user: prefix). If no administrator identities are configured in the above-described configuration files, the output will be empty.</p>
<h2>Options</h2>
<p><code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Write a summary of the available options to standard output and exit successfully.</dl>
<p> <code>-c</code>, <code>&#8211;config-path</code>=<i>config-path</i></p>
<dl>
<dd>Search for configuration files in <i>config-path</i> instead of the default /etc/polkit-1/localauthority.conf.d.</dl>
<h2>Exit Status</h2>
<p><code>pkla-admin-identities</code> exits with 0 on success (even if there are no administrator identities), and a non-zero status on error.</p>
<h2>Files</h2>
<p>/etc/polkit-1/localauthority.conf.d</p>
<dl>
<dd>Default directory containing configuration files.</dl>
<h2>Example</h2>
<p>The following .conf file </p>
<dl>
<dd>
<pre>[Configuration]
AdminIdentities=unix-group:staff</pre>
</dl>
<p> specifies that any user in the staff UNIX group can be used for authentication when administrator authentication is needed. This file would typically be installed in the /etc/polkit-1/localauthority.conf.d directory and given the name 60-desktop-policy.conf to ensure that it is evaluated after the 50-localauthority.conf file shipped with pkla-polkit-compat. If the local administrator wants to override this (suppose 60-desktop-policy.conf was shipped as part of the OS) he can simply create a file 99-my-admin-configuration.conf with the following content </p>
<dl>
<dd>
<pre>[Configuration]
AdminIdentities=unix-user:lisa;unix-user:marge</pre>
</dl>
<p> to specify that only the users lisa and marge can authenticate when administrator authentication is needed.</p>
<h2>Author</h2>
<p>Written by David Zeuthen &lt;davidz [at] redhat.com&gt; with a lot of help from many others. Adapted by Miloslav Trmač &lt;mitr [at] redhat.com&gt;.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-polkit/">polkit</a></code>(8) </p>
