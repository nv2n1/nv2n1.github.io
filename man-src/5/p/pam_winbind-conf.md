---
title: "pam_winbind-conf(5)"
name: "pam_winbind-conf"
section: "5"
letter: "p"
url: "/docs/linux/man/5-pam_winbind-conf/"
description: "pam_winbind.conf – Configuration file of PAM module for Winbind"
---

<p>pam_winbind.conf &#8211; Configuration file of PAM module for Winbind</p>
<h2>Description</h2>
<p>This configuration file is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> pam_winbind.conf is the configuration file for the pam_winbind PAM module. See <code><a href="/docs/linux/man/8-pam_winbind/">pam_winbind</a></code>(8) for further details.</p>
<h2>Synopsis</h2>
<p>The pam_winbind.conf configuration file is a classic ini-style configuration file. There is only one section (global) where various options are defined.</p>
<h2>Options</h2>
<p>pam_winbind supports several options which can either be set in the PAM configuration files or in the pam_winbind configuration file situated at /etc/security/pam_winbind.conf. Options from the PAM configuration file take precedence to those from the pam_winbind.conf configuration file. </p>
<p> debug = yes|no</p>
<dl>
<dd>Gives debugging output to syslog. Defaults to &quot;no&quot;.</dl>
<p> debug_state = yes|no</p>
<dl>
<dd>Gives detailed PAM state debugging output to syslog. Defaults to &quot;no&quot;.</dl>
<p> require_membership_of = [SID or NAME]</p>
<dl>
<dd>If this option is set, pam_winbind will only succeed if the user is a member of the given SID or NAME. A SID can be either a group-SID, an alias-SID or even an user-SID. It is also possible to give a NAME instead of the SID. That name must have the form: <i>MYDOMAIN\mygroup</i> or <i>MYDOMAIN\myuser</i>. pam_winbind will, in that case, lookup the SID internally. Note that NAME may not contain any spaces. It is thus recommended to only use SIDs. You can verify the list of SIDs a user is a member of with wbinfo &#8211;user-sids=SID. This setting is empty by default. </p>
<p> This option only operates during password authentication, and will not restrict access if a password is not required for any reason (such as SSH key-based login).</dl>
<p> try_first_pass = yes|no</p>
<dl>
<dd>By default, pam_winbind tries to get the authentication token from a previous module. If no token is available it asks the user for the old password. With this option, pam_winbind aborts with an error if no authentication token from a previous module is available. If a primary password is not valid, PAM will prompt for a password. Default to &quot;no&quot;.</dl>
<p> krb5_auth = yes|no</p>
<dl>
<dd>pam_winbind can authenticate using Kerberos when winbindd is talking to an Active Directory domain controller. Kerberos authentication must be enabled with this parameter. When Kerberos authentication can not succeed (e.g. due to clock skew), winbindd will fallback to samlogon authentication over MSRPC. When this parameter is used in conjunction with <i>winbind refresh tickets</i>, winbind will keep your Ticket Granting Ticket (TGT) uptodate by refreshing it whenever necessary. Defaults to &quot;no&quot;.</dl>
<p> krb5_ccache_type = [type]</p>
<dl>
<dd>When pam_winbind is configured to try kerberos authentication by enabling the <i>krb5_auth</i> option, it can store the retrieved Ticket Granting Ticket (TGT) in a credential cache. The type of credential cache can be controlled with this option. The supported values are: <i>KEYRING</i> (when supported by the system&#8217;s Kerberos library and Kernel), <i>FILE</i> and <i>DIR</i> (when the DIR type is supported by the system&#8217;s Kerberos library). In case of FILE a credential cache in the form of /tmp/krb5cc_UID will be created &#8211; in case of DIR you NEED to specify a directory. UID is replaced with the numeric user id. </p>
<p> When using the KEYRING type, the supported mechanism is &#8220;KEYRING:persistent:UID&#8221;, which uses the Linux kernel keyring to store credentials on a per-UID basis. This is the recommended choice on latest Linux distributions, as it is the most secure and predictable method. </p>
<p> It is also possible to define custom filepaths and use the &quot;%u&quot; pattern in order to substitue the numeric user id. Examples: </p>
<p> krb5_ccache_type = DIR:/run/user/%u/krb5cc</p>
<dl>
<dd>This will create a credential cache file in the specified directory.</dl>
<p> krb5_ccache_type = FILE:/tmp/krb5cc_%u</p>
<dl>
<dd>This will create a credential cache file.</dl>
<p> Leave empty to just do kerberos authentication without having a ticket cache after the logon has succeeded. This setting is empty by default.</dl>
<p> cached_login = yes|no</p>
<dl>
<dd>Winbind allows one to logon using cached credentials when <i>winbind offline logon</i> is enabled. To use this feature from the PAM module this option must be set. Defaults to &quot;no&quot;.</dl>
<p> silent = yes|no</p>
<dl>
<dd>Do not emit any messages. Defaults to &quot;no&quot;.</dl>
<p> mkhomedir = yes|no</p>
<dl>
<dd>Create homedirectory for a user on-the-fly, option is valid in PAM session block. Defaults to &quot;no&quot;.</dl>
<p> warn_pwd_expire = days</p>
<dl>
<dd>Defines number of days before pam_winbind starts to warn about passwords that are going to expire. Defaults to 14 days.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-pam_winbind/">pam_winbind</a></code>(8), <code><a href="/docs/linux/man/1-wbinfo/">wbinfo</a></code>(1), <code><a href="/docs/linux/man/8-winbindd/">winbindd</a></code>(8), <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5)</p>
<h2>Version</h2>
<p>This man page is correct for version 3 of Samba.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed. </p>
<p> This manpage was written by Jelmer Vernooij and Guenther Deschner.</p>
