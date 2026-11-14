---
title: "pam_winbind(8)"
name: "pam_winbind"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_winbind/"
description: "pam_winbind – PAM module for Winbind"
---

<p>pam_winbind &#8211; PAM module for Winbind</p>
<h2>Description</h2>
<p>This tool is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> pam_winbind is a PAM module that can authenticate users against the local domain by talking to the Winbind daemon.</p>
<h2>Synopsis</h2>
<p>Edit the PAM system config /etc/pam.d/service and modify it as the following example shows: </p>
<dl>
<dd>
<pre> ...
 auth required pam_env.so
 auth sufficient pam_unix2.so
 +++ auth required pam_winbind.so use_first_pass
 account requisite pam_unix2.so
 +++ account required pam_winbind.so use_first_pass
 +++ password sufficient pam_winbind.so
 password requisite pam_pwcheck.so cracklib
 password required pam_unix2.so use_authtok
 session required pam_unix2.so
 +++ session required pam_winbind.so
 ...</pre>
</dl>
<p> Make sure that pam_winbind is one of the first modules in the session part. It may retrieve kerberos tickets which are needed by other modules.</p>
<h2>Options</h2>
<p>pam_winbind supports several options which can either be set in the PAM configuration files or in the pam_winbind configuration file situated at /etc/security/pam_winbind.conf. Options from the PAM configuration file take precedence to those from the configuration file. See <code><a href="/docs/linux/man/5-pam_winbind-conf/">pam_winbind.conf</a></code>(5) for further details. </p>
<p> debug</p>
<dl>
<dd>Gives debugging output to syslog.</dl>
<p> debug_state</p>
<dl>
<dd>Gives detailed PAM state debugging output to syslog.</dl>
<p> require_membership_of=[SID or NAME]</p>
<dl>
<dd>If this option is set, pam_winbind will only succeed if the user is a member of the given SID or NAME. A SID can be either a group-SID, an alias-SID or even an user-SID. It is also possible to give a NAME instead of the SID. That name must have the form: <i>MYDOMAIN\mygroup</i> or <i>MYDOMAIN\myuser</i>. pam_winbind will, in that case, lookup the SID internally. Note that NAME may not contain any spaces. It is thus recommended to only use SIDs. You can verify the list of SIDs a user is a member of with wbinfo &#8211;user-sids=SID. </p>
<p> This option must only be specified on a auth module declaration, as it only operates in conjunction with password authentication.</dl>
<p> use_first_pass</p>
<dl>
<dd>By default, pam_winbind tries to get the authentication token from a previous module. If no token is available it asks the user for the old password. With this option, pam_winbind aborts with an error if no authentication token from a previous module is available.</dl>
<p> try_first_pass</p>
<dl>
<dd>Same as the use_first_pass option (previous item), except that if the primary password is not valid, PAM will prompt for a password.</dl>
<p> use_authtok</p>
<dl>
<dd>Set the new password to the one provided by the previously stacked password module. If this option is not set pam_winbind will ask the user for the new password.</dl>
<p> krb5_auth</p>
<dl>
<dd>pam_winbind can authenticate using Kerberos when winbindd is talking to an Active Directory domain controller. Kerberos authentication must be enabled with this parameter. When Kerberos authentication can not succeed (e.g. due to clock skew), winbindd will fallback to samlogon authentication over MSRPC. When this parameter is used in conjunction with <i>winbind refresh tickets</i>, winbind will keep your Ticket Granting Ticket (TGT) uptodate by refreshing it whenever necessary.</dl>
<p> krb5_ccache_type=[type]</p>
<dl>
<dd>When pam_winbind is configured to try kerberos authentication by enabling the <i>krb5_auth</i> option, it can store the retrieved Ticket Granting Ticket (TGT) in a credential cache. The type of credential cache can be set with this option. Currently the only supported value is: <i>FILE</i>. In that case a credential cache in the form of /tmp/krb5cc_UID will be created, where UID is replaced with the numeric user id. Leave empty to just do kerberos authentication without having a ticket cache after the logon has succeeded.</dl>
<p> cached_login</p>
<dl>
<dd>Winbind allows one to logon using cached credentials when <i>winbind offline logon</i> is enabled. To use this feature from the PAM module this option must be set.</dl>
<p> silent</p>
<dl>
<dd>Do not emit any messages.</dl>
<p> mkhomedir</p>
<dl>
<dd>Create homedirectory for a user on-the-fly, option is valid in PAM session block.</dl>
<p> warn_pwd_expire</p>
<dl>
<dd>Defines number of days before pam_winbind starts to warn about passwords that are going to expire. Defaults to 14 days.</dl>
<h2>Pam Data Exports</h2>
<p>This section describes the data exported in the PAM stack which could be used in other PAM modules. </p>
<p> PAM_WINBIND_HOMEDIR</p>
<dl>
<dd>This is the Windows Home Directory set in the profile tab in the user settings on the Active Directory Server. This could be a local path or a directory on a share mapped to a drive.</dl>
<p> PAM_WINBIND_LOGONSCRIPT</p>
<dl>
<dd>The path to the logon script which should be executed if a user logs in. This is normally a relative path to the script stored on the server.</dl>
<p> PAM_WINBIND_LOGONSERVER</p>
<dl>
<dd>This exports the Active Directory server we are authenticating against. This can be used as a variable later.</dl>
<p> PAM_WINBIND_PROFILEPATH</p>
<dl>
<dd>This is the profile path set in the profile tab in the user settings. Normally the home directory is synced with this directory on a share.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-pam_winbind-conf/">pam_winbind.conf</a></code>(5), <code><a href="/docs/linux/man/1-wbinfo/">wbinfo</a></code>(1), <code><a href="/docs/linux/man/8-winbindd/">winbindd</a></code>(8), <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5)</p>
<h2>Version</h2>
<p>This man page is correct for version 3 of Samba.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed. </p>
<p> This manpage was written by Jelmer Vernooij and Guenther Deschner.</p>
