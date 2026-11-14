---
title: "sss_cache(8)"
name: "sss_cache"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sss_cache/"
description: "sss_cache – perform cache cleanup"
---

<p>sss_cache &#8211; perform cache cleanup</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>sss_cache</code> [<i>options</i>]</dl>
<h2>Description</h2>
<p><code>sss_cache</code></p>
<dd>invalidates records in SSSD cache. Invalidated records are forced to be reloaded from server as soon as related SSSD backend is online. Options that invalidate a single object only accept a single provided argument.</p>
<h2>Options</h2>
<p><code>-E</code>,<code>&#8211;everything</code></p>
<dl>
<dd>Invalidate all cached entries.</dl>
<p> <code>-u</code>,<code>&#8211;user</code> <i>login</i></p>
<dl>
<dd>Invalidate specific user.</dl>
<p> <code>-U</code>,<code>&#8211;users</code></p>
<dl>
<dd>Invalidate all user records. This option overrides invalidation of specific user if it was also set.</dl>
<p> <code>-g</code>,<code>&#8211;group</code> <i>group</i></p>
<dl>
<dd>Invalidate specific group.</dl>
<p> <code>-G</code>,<code>&#8211;groups</code></p>
<dl>
<dd>Invalidate all group records. This option overrides invalidation of specific group if it was also set.</dl>
<p> <code>-n</code>,<code>&#8211;netgroup</code> <i>netgroup</i></p>
<dl>
<dd>Invalidate specific netgroup.</dl>
<p> <code>-N</code>,<code>&#8211;netgroups</code></p>
<dl>
<dd>Invalidate all netgroup records. This option overrides invalidation of specific netgroup if it was also set.</dl>
<p> <code>-s</code>,<code>&#8211;service</code> <i>service</i></p>
<dl>
<dd>Invalidate specific service.</dl>
<p> <code>-S</code>,<code>&#8211;services</code></p>
<dl>
<dd>Invalidate all service records. This option overrides invalidation of specific service if it was also set.</dl>
<p> <code>-a</code>,<code>&#8211;autofs-map</code> <i>autofs-map</i></p>
<dl>
<dd>Invalidate specific autofs maps.</dl>
<p> <code>-A</code>,<code>&#8211;autofs-maps</code></p>
<dl>
<dd>Invalidate all autofs maps. This option overrides invalidation of specific map if it was also set.</dl>
<p> <code>-h</code>,<code>&#8211;ssh-host</code> <i>hostname</i></p>
<dl>
<dd>Invalidate SSH public keys of a specific host.</dl>
<p> <code>-H</code>,<code>&#8211;ssh-hosts</code></p>
<dl>
<dd>Invalidate SSH public keys of all hosts. This option overrides invalidation of SSH public keys of specific host if it was also set.</dl>
<p> <code>-r</code>,<code>&#8211;sudo-rule</code> <i>rule</i></p>
<dl>
<dd>Invalidate particular sudo rule.</dl>
<p> <code>-R</code>,<code>&#8211;sudo-rules</code></p>
<dl>
<dd>Invalidate all cached sudo rules. This option overrides invalidation of specific sudo rule if it was also set.</dl>
<p> <code>-d</code>,<code>&#8211;domain</code> <i>domain</i></p>
<dl>
<dd>Restrict invalidation process only to a particular domain.</dl>
<p> <code>-?</code>,<code>&#8211;help</code></p>
<dl>
<dd>Display help message and exit.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-sssd/">sssd</a></code>(8), <code><a href="/docs/linux/man/5-sssd-conf/">sssd.conf</a></code>(5), <code><a href="/docs/linux/man/5-sssd-ldap/">sssd-ldap</a></code>(5), <code><a href="/docs/linux/man/5-sssd-krb5/">sssd-krb5</a></code>(5), <code><a href="/docs/linux/man/5-sssd-simple/">sssd-simple</a></code>(5), <code><a href="/docs/linux/man/5-sssd-ipa/">sssd-ipa</a></code>(5), <code><a href="/docs/linux/man/5-sssd-ad/">sssd-ad</a></code>(5), <code><a href="/docs/linux/man/5-sssd-sudo/">sssd-sudo</a></code>(5),<code><a href="/docs/linux/man/5-sssd-secrets/">sssd-secrets</a></code>(5),<code><a href="/docs/linux/man/8-sss_cache/">sss_cache</a></code>(8), <code><a href="/docs/linux/man/8-sss_debuglevel/">sss_debuglevel</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupadd/">sss_groupadd</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupdel/">sss_groupdel</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupshow/">sss_groupshow</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupmod/">sss_groupmod</a></code>(8), <code><a href="/docs/linux/man/8-sss_useradd/">sss_useradd</a></code>(8), <code><a href="/docs/linux/man/8-sss_userdel/">sss_userdel</a></code>(8), <code><a href="/docs/linux/man/8-sss_usermod/">sss_usermod</a></code>(8), <code><a href="/docs/linux/man/8-sss_obfuscate/">sss_obfuscate</a></code>(8), <code><a href="/docs/linux/man/8-sss_seed/">sss_seed</a></code>(8), <code><a href="/docs/linux/man/8-sssd_krb5_locator_plugin/">sssd_krb5_locator_plugin</a></code>(8), <code><a href="/docs/linux/man/8-sss_ssh_authorizedkeys/">sss_ssh_authorizedkeys</a></code>(8), <code><a href="/docs/linux/man/8-sss_ssh_knownhostsproxy/">sss_ssh_knownhostsproxy</a></code>(8),<code><a href="/docs/linux/man/5-sssd-ifp/">sssd-ifp</a></code>(5),<code><a href="/docs/linux/man/8-pam_sss/">pam_sss</a></code>(8). <code><a href="/docs/linux/man/5-sss_rpcidmapd/">sss_rpcidmapd</a></code>(5)</p>
<h2>Authors</h2>
<p><code>The SSSD upstream &#8211; <a rel="nofollow" href="https://pagure.io/SSSD/sssd/">https://pagure.io/SSSD/sssd/</a></code></p>
