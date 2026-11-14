---
title: "nsswitch-conf(5)"
name: "nsswitch-conf"
section: "5"
letter: "n"
url: "/docs/linux/man/5-nsswitch-conf/"
description: "nsswitch.conf – Name Service Switch configuration file"
---

<p>nsswitch.conf &#8211; Name Service Switch configuration file</p>
<h2>Description</h2>
<p>The Name Service Switch (NSS) configuration file, <i>/etc/nsswitch.conf</i>, is used by the GNU C Library and certain other applications to determine the sources from which to obtain name-service information in a range of categories, and in what order. Each category of information is identified by a database name. The file is plain ASCII text, with columns separated by spaces or tab characters. The first column specifies the database name. The remaining columns describe the order of sources to query and a limited set of actions that can be performed by lookup result. The following databases are understood by the GNU C Library:</p>
<dl>
<dt><code>aliases</code></p>
<dd>Mail aliases, used by <code><a href="/docs/linux/man/3-getaliasent/">getaliasent</a></code>(3) and related functions.</p>
<dt><code>ethers</code></p>
<dd>Ethernet numbers.</p>
<dt><code>group</code></p>
<dd>Groups of users, used by <code><a href="/docs/linux/man/3-getgrent/">getgrent</a></code>(3) and related functions.</p>
<dt><code>hosts</code></p>
<dd>Host names and numbers, used by <code><a href="/docs/linux/man/3-gethostbyname/">gethostbyname</a></code>(3) and related functions.</p>
<dt><code>initgroups</code></p>
<dd>Supplementary group access list, used by <code><a href="/docs/linux/man/3-getgrouplist/">getgrouplist</a></code>(3) function.</p>
<dt><code>netgroup</code></p>
<dd>Network-wide list of hosts and users, used for access rules. C libraries before glibc 2.1 supported netgroups only over NIS.</p>
<dt><code>networks</code></p>
<dd>Network names and numbers, used by <code><a href="/docs/linux/man/3-getnetent/">getnetent</a></code>(3) and related functions.</p>
<dt><code>passwd</code></p>
<dd>User passwords, used by <code><a href="/docs/linux/man/3-getpwent/">getpwent</a></code>(3) and related functions.</p>
<dt><code>protocols</code></p>
<dd>Network protocols, used by <code><a href="/docs/linux/man/3-getprotoent/">getprotoent</a></code>(3) and related functions.</p>
<dt><code>publickey</code></p>
<dd>Public and secret keys for Secure_RPC used by NFS and NIS+.</p>
<dt><code>rpc</code></p>
<dd>Remote procedure call names and numbers, used by <code><a href="/docs/linux/man/3-getrpcbyname/">getrpcbyname</a></code>(3) and related functions.</p>
<dt><code>services</code></p>
<dd>Network services, used by <code><a href="/docs/linux/man/3-getservent/">getservent</a></code>(3) and related functions.</p>
<dt><code>shadow</code></p>
<dd>Shadow user passwords, used by <code><a href="/docs/linux/man/3-getspnam/">getspnam</a></code>(3) and related functions.</dl>
<p> The GNU C Library ignores databases with unknown names. Some applications use this to implement special handling for their own databases. For example, <code><a href="/docs/linux/man/8-sudo/">sudo</a></code>(8) consults the <code>sudoers</code> database. Here is an example <i>/etc/nsswitch.conf</i> file: passwd: compat group: compat shadow: compat </p>
<pre><code>hosts:          dns [!UNAVAIL=return] files
networks:       nis [NOTFOUND=return] files
ethers:         nis [NOTFOUND=return] files
protocols:      nis [NOTFOUND=return] files
rpc:            nis [NOTFOUND=return] files
services:       nis [NOTFOUND=return] files</code></pre>
<p> The first column is the database name. The remaining columns specify:</p>
<dl>
<dt>*</p>
<dd>One or more service specifications, for example, &quot;files&quot;, &quot;db&quot;, or &quot;nis&quot;. The order of the services on the line determines the order in which those services will be queried, in turn, until a result is found.</p>
<dt>*</p>
<dd>Optional actions to perform if a particular result is obtained from the preceding service, for example, &quot;[NOTFOUND=return]&quot;.</dl>
<p> The service specifications supported on your system depend on the presence of shared libraries, and are therefore extensible. Libraries called <i>/lib/libnss_SERVICE.so.</i><code>X</code> will provide the named <i>SERVICE</i>. On a standard installation, you can use &quot;files&quot;, &quot;db&quot;, &quot;nis&quot;, and &quot;nisplus&quot;. For the <code>hosts</code> database, you can additionally specify &quot;dns&quot;. For the <code>passwd</code>, <code>group</code>, and <code>shadow</code> databases, you can additionally specify &quot;compat&quot; (see <code>Compatibility mode</code> below). The version number <code>X</code> may be 1 for glibc 2.0, or 2 for glibc 2.1 and later. On systems with additional libraries installed, you may have access to further services such as &quot;hesiod&quot;, &quot;ldap&quot;, &quot;winbind&quot; and &quot;wins&quot;. An action may also be specified following a service specification. The action modifies the behavior following a result obtained from the preceding data source. Action items take the general form:</p>
<dl>
<dd>[<i>STATUS</i>=<i>ACTION</i>]<br />
 [!<i>STATUS</i>=<i>ACTION</i>]</dl>
<p> where </p>
<pre><code>STATUS

=&gt;
success

|
notfound

|
unavail

|
tryagain


ACTION

=&gt;
return

|
continue

|
merge</code></pre>
<p> The ! negates the test, matching all possible results except the one specified. The case of the keywords is not significant. The <i>STATUS</i> value is matched against the result of the lookup function called by the preceding service specification, and can be one of:</p>
<dl>
<dd>
<dl>
<dt><code>success</code></p>
<dd>No error occurred and the requested entry is returned. The default action for this condition is &quot;return&quot;.</p>
<dt><code>notfound</code></p>
<dd>The lookup succeeded, but the requested entry was not found. The default action for this condition is &quot;continue&quot;.</p>
<dt><code>unavail</code></p>
<dd>The service is permanently unavailable. This can mean either that the required file cannot be read, or, for network services, that the server is not available or does not allow queries. The default action for this condition is &quot;continue&quot;.</p>
<dt><code>tryagain</code></p>
<dd>The service is temporarily unavailable. This could mean a file is locked or a server currently cannot accept more connections. The default action for this condition is &quot;continue&quot;.</dl>
</dl>
<p> The <i>ACTION</i> value can be one of:</p>
<dl>
<dd>
<dl>
<dt><code>return</code></p>
<dd>Return a result now. Do not call any further lookup functions. However, for compatibility reasons, if this is the selected action for the <code>group</code> database and the <code>notfound</code> status, and the configuration file does not contain the <code>initgroups</code> line, the next lookup function is always called, without affecting the search result.</p>
<dt><code>continue</code></p>
<dd>Call the next lookup function.</p>
<dt><code>merge</code></p>
<dd><i>[SUCCESS=merge]</i> is used between two database entries. When a group is located in the first of the two group entries, processing will continue on to the next one. If the group is also found in the next entry (and the group name and GID are an exact match), the member list of the second entry will be added to the group object to be returned. Available since glibc 2.24. Note that merging will not be done for <code><a href="/docs/linux/man/3-getgrent/">getgrent</a></code>(3) nor will duplicate members be pruned when they occur in both entries being merged.</dl>
</dl>
<h3>Compatibility mode (compat)</h3>
<p>The NSS &quot;compat&quot; service is similar to &quot;files&quot; except that it additionally permits special entries in corresponding files for granting users or members of netgroups access to the system. The following entries are valid in this mode:</p>
<dl>
<dd>For <code>passwd</code> and <code>shadow</code> databases:</p>
<dl>
<dd>
<dl>
<dt><code>+</code><i>user</i></p>
<dd>Include the specified <i>user</i> from the NIS passwd/shadow map.</p>
<dt><code>+</code><i>user::::::</i></p>
<dd>Include the specified <i>user</i> from the NIS passwd map, but override with non-empty passwd fields.</p>
<dt><code>+@</code><i>netgroup</i></p>
<dd>Include all users in the given <i>netgroup</i>.</p>
<dt><code>&#8211;</code><i>user</i></p>
<dd>Exclude the specified <i>user</i> from the NIS passwd/shadow map.</p>
<dt><code>-@</code><i>netgroup</i></p>
<dd>Exclude all users in the given <i>netgroup</i>.</p>
<dt><code>+</code></p>
<dd>Include every user, except previously excluded ones, from the NIS passwd/shadow map.</dl>
</dl>
<p> For <code>group</code> database:</p>
<dl>
<dd>
<dl>
<dt><code>+</code><i>group</i></p>
<dd>Include the specified <i>group</i> from the NIS group map.</p>
<dt><code>&#8211;</code><i>group</i></p>
<dd>Exclude the specified <i>group</i> from the NIS group map.</p>
<dt><code>+</code></p>
<dd>Include every group, except previously excluded ones, from the NIS group map.</dl>
</dl>
</dl>
<p> By default, the source is &quot;nis&quot;, but this may be overridden by specifying any NSS service except &quot;compat&quot; itself as the source for the pseudo-databases <code>passwd_compat</code>, <code>group_compat</code>, and <code>shadow_compat</code>.</p>
<h2>Files</h2>
<p>A service named <i>SERVICE</i> is implemented by a shared object library named <i>libnss_SERVICE.so.</i><code>X</code> that resides in <i>/lib</i>.</p>
<dl>
<dd>
<dl>
<dd><i>/etc/nsswitch.conf</i> NSS configuration file.</p>
<dt><i>/lib/libnss_compat.so.</i><code>X</code></p>
<dd>implements &quot;compat&quot; source.</p>
<dt><i>/lib/libnss_db.so.</i><code>X</code></p>
<dd>implements &quot;db&quot; source.</p>
<dt><i>/lib/libnss_dns.so.</i><code>X</code></p>
<dd>implements &quot;dns&quot; source.</p>
<dt><i>/lib/libnss_files.so.</i><code>X</code></p>
<dd>implements &quot;files&quot; source.</p>
<dt><i>/lib/libnss_hesiod.so.</i><code>X</code></p>
<dd>implements &quot;hesiod&quot; source.</p>
<dt><i>/lib/libnss_nis.so.</i><code>X</code></p>
<dd>implements &quot;nis&quot; source.</p>
<dt><i>/lib/libnss_nisplus.so.</i><code>X</code></p>
<dd>implements &quot;nisplus&quot; source.</dl>
</dl>
<p> The following files are read when &quot;files&quot; source is specified for respective databases:</p>
<dl>
<dd>
<dl>
<dt><code>aliases</code></p>
<dd><i>/etc/aliases</i></p>
<dt><code>ethers</code></p>
<dd><i>/etc/ethers</i></p>
<dt><code>group</code></p>
<dd><i>/etc/group</i></p>
<dt><code>hosts</code></p>
<dd><i>/etc/hosts</i></p>
<dt><code>initgroups</code></p>
<dd><i>/etc/group</i></p>
<dt><code>netgroup</code></p>
<dd><i>/etc/netgroup</i></p>
<dt><code>networks</code></p>
<dd><i>/etc/networks</i></p>
<dt><code>passwd</code></p>
<dd><i>/etc/passwd</i></p>
<dt><code>protocols</code></p>
<dd><i>/etc/protocols</i></p>
<dt><code>publickey</code></p>
<dd><i>/etc/publickey</i></p>
<dt><code>rpc</code></p>
<dd><i>/etc/rpc</i></p>
<dt><code>services</code></p>
<dd><i>/etc/services</i></p>
<dt><code>shadow</code></p>
<dd><i>/etc/shadow</i></dl>
</dl>
<h2>Notes</h2>
<p>Within each process that uses <code>nsswitch.conf</code>, the entire file is read only once. If the file is later changed, the process will continue using the old configuration. </p>
<p> Traditionally, there was only a single source for service information, often in the form of a single configuration file (e.g., <i>/etc/passwd</i>). However, as other name services, such as the Network Information Service (NIS) and the Domain Name Service (DNS), became popular, a method was needed that would be more flexible than fixed search orders coded into the C library. The Name Service Switch mechanism, which was based on the mechanism used by Sun Microsystems in the Solaris 2 C library, introduced a cleaner solution to the problem.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-getent/">getent</a></code>(1), <code><a href="/docs/linux/man/5-nss/">nss</a></code>(5)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
