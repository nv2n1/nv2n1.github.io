---
title: "sss_seed(8)"
name: "sss_seed"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sss_seed/"
description: "sss_seed – seed the SSSD cache with a user"
---

<p>sss_seed &#8211; seed the SSSD cache with a user</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>sss_seed</code> [<i>options</i>] -D&nbsp;<wbr><i>DOMAIN</i> -n&nbsp;<wbr><i>USER</i></dl>
<h2>Description</h2>
<p><code>sss_seed</code></p>
<dd>seeds the SSSD cache with a user entry and temporary password. If a user entry is already present in the SSSD cache then the entry is updated with the temporary password. </p>
<h2>Options</h2>
<p><code>-D</code>,<code>&#8211;domain</code> <i>DOMAIN</i></p>
<dl>
<dd>Provide the name of the domain in which the user is a member of. The domain is also used to retrieve user information. The domain must be configured in sssd.conf. The <i>DOMAIN</i> option must be provided. Information retrieved from the domain overrides what is provided in the options.</dl>
<p> <code>-n</code>,<code>&#8211;username</code> <i>USER</i></p>
<dl>
<dd>The username of the entry to be created or modified in the cache. The <i>USER</i> option must be provided.</dl>
<p> <code>-u</code>,<code>&#8211;uid</code> <i>UID</i></p>
<dl>
<dd>Set the UID of the user to <i>UID</i>.</dl>
<p> <code>-g</code>,<code>&#8211;gid</code> <i>GID</i></p>
<dl>
<dd>Set the GID of the user to <i>GID</i>.</dl>
<p> <code>-c</code>,<code>&#8211;gecos</code> <i>COMMENT</i></p>
<dl>
<dd>Any text string describing the user. Often used as the field for the user&#8217;s full name.</dl>
<p> <code>-h</code>,<code>&#8211;home</code> <i>HOME_DIR</i></p>
<dl>
<dd>Set the home directory of the user to <i>HOME_DIR</i>.</dl>
<p> <code>-s</code>,<code>&#8211;shell</code> <i>SHELL</i></p>
<dl>
<dd>Set the login shell of the user to <i>SHELL</i>.</dl>
<p> <code>-i</code>,<code>&#8211;interactive</code></p>
<dl>
<dd>Interactive mode for entering user information. This option will only prompt for information not provided in the options or retrieved from the domain.</dl>
<p> <code>-p</code>,<code>&#8211;password-file</code> <i>PASS_FILE</i></p>
<dl>
<dd>Specify file to read user&#8217;s password from. (if not specified password is prompted for)</dl>
<p> <code>-?</code>,<code>&#8211;help</code></p>
<dl>
<dd>Display help message and exit.</dl>
<h2>Notes</h2>
<p>The length of the password (or the size of file specified with -p or &#8211;password-file option) must be less than or equal to PASS_MAX bytes (64 bytes on systems with no globally-defined PASS_MAX value). </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-sssd/">sssd</a></code>(8), <code><a href="/docs/linux/man/5-sssd-conf/">sssd.conf</a></code>(5), <code><a href="/docs/linux/man/5-sssd-ldap/">sssd-ldap</a></code>(5), <code><a href="/docs/linux/man/5-sssd-krb5/">sssd-krb5</a></code>(5), <code><a href="/docs/linux/man/5-sssd-simple/">sssd-simple</a></code>(5), <code><a href="/docs/linux/man/5-sssd-ipa/">sssd-ipa</a></code>(5), <code><a href="/docs/linux/man/5-sssd-ad/">sssd-ad</a></code>(5), <code><a href="/docs/linux/man/5-sssd-sudo/">sssd-sudo</a></code>(5),<code><a href="/docs/linux/man/8-sss_cache/">sss_cache</a></code>(8), <code><a href="/docs/linux/man/8-sss_debuglevel/">sss_debuglevel</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupadd/">sss_groupadd</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupdel/">sss_groupdel</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupshow/">sss_groupshow</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupmod/">sss_groupmod</a></code>(8), <code><a href="/docs/linux/man/8-sss_useradd/">sss_useradd</a></code>(8), <code><a href="/docs/linux/man/8-sss_userdel/">sss_userdel</a></code>(8), <code><a href="/docs/linux/man/8-sss_usermod/">sss_usermod</a></code>(8), <code><a href="/docs/linux/man/8-sss_obfuscate/">sss_obfuscate</a></code>(8), <code><a href="/docs/linux/man/8-sss_seed/">sss_seed</a></code>(8), <code><a href="/docs/linux/man/8-sssd_krb5_locator_plugin/">sssd_krb5_locator_plugin</a></code>(8), <code><a href="/docs/linux/man/8-sss_ssh_authorizedkeys/">sss_ssh_authorizedkeys</a></code>(8), <code><a href="/docs/linux/man/8-sss_ssh_knownhostsproxy/">sss_ssh_knownhostsproxy</a></code>(8),<code><a href="/docs/linux/man/5-sssd-ifp/">sssd-ifp</a></code>(5),<code><a href="/docs/linux/man/8-pam_sss/">pam_sss</a></code>(8). <code><a href="/docs/linux/man/5-sss_rpcidmapd/">sss_rpcidmapd</a></code>(5)</p>
<h2>Authors</h2>
<p><code>The SSSD upstream &#8211; <a rel="nofollow" href="http://fedorahosted.org/sssd">http://fedorahosted.org/sssd</a></code></p>
