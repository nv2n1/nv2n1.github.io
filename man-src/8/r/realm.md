---
title: "realm(8)"
name: "realm"
section: "8"
letter: "r"
url: "/docs/linux/man/8-realm/"
description: "realm – Manage enrollment in realms"
---

<p>realm &#8211; Manage enrollment in realms</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>realm discover</code> [realm-name]</p>
<dt> <code>realm join</code> [-U user] [realm-name]</p>
<dt> <code>realm leave</code> [-U user] [realm-name]</p>
<dt> <code>realm list</code></p>
<dt> <code>realm permit</code> [-ax] [-R realm] {user [at] domain&#8230;}</p>
<dt> <code>realm deny</code> -a [-R realm]</dl>
<h2>Description</h2>
<p><code>realm</code></p>
<dd>is a command line tool that can be used to manage enrollment in kerberos realms, like Active Directory domains or IPA domains. </p>
<p> See the various sub commands below. The following global options can be used: </p>
<p> <code>&#8211;install=/path</code></p>
<dl>
<dd>Run in install mode. This makes realmd chroot into the specified directory and place files in appropriate locations for use during an installer. No packages will be installed or services will be started when running in this mode.</dl>
<p> <code>&#8211;unattended</code></p>
<dl>
<dd>Run in unattended mode without prompting for input.</dl>
<p> <code>&#8211;verbose, -v</code></p>
<dl>
<dd>Display verbose diagnostics while doing running commands.</dl>
<h2>Discover</h2>
<p>Discover a realm and its capabilities. </p>
<dl>
<dd>
<pre>$ realm discover</pre>
</dl>
<dl>
<dd>
<pre>$ realm discover domain.example.com</pre>
</dl>
<p> After discovering a realm, its name, type and capabilities are displayed. </p>
<p> If no domain is specified, then the domain assigned through DHCP is used as a default. </p>
<p> The following options can be used: </p>
<p> <code>&#8211;all</code></p>
<dl>
<dd>Show all discovered realms (in various configurations).</dl>
<p> <code>&#8211;client-software=xxx</code></p>
<dl>
<dd>Only discover realms for which we can use the given client software. Possible values include <i>sssd</i> or <i>winbind</i>.</dl>
<p> <code>&#8211;server-software=xxx</code></p>
<dl>
<dd>Only discover realms which run the given server software. Possible values include <i>active-directory</i> or <i>ipa</i>.</dl>
<p> <code>&#8211;membership-software=xxx</code></p>
<dl>
<dd>Only discover realms for which the given membership software can be used to subsequently perform enrollment. Possible values include <i>samba</i> or <i>adcli</i>.</dl>
<h2>Join</h2>
<p>Configure the local machine for use with a realm. </p>
<dl>
<dd>
<pre>$ realm join domain.example.com</pre>
</dl>
<dl>
<dd>
<pre>$ realm join --user=admin --computer-ou=OU=Special domain.example.com</pre>
</dl>
<p> The realm is first discovered, as we would with the <code>discover</code> command. If no domain is specified, then the domain assigned through DHCP is used as a default. </p>
<p> After a successful join, the computer will be in a state where it is able to resolve remote user and group names from the realm. For kerberos realms, a computer account and host keytab is created. </p>
<p> Joining arbitrary kerberos realms is not supported. The realm must have a supported mechanism for joining from a client machine, such as Active Directory or IPA. </p>
<p> If the domain has been preconfigured, and unless &#8211;user is explicitly specified, an automatic join is attempted first. </p>
<p> Note that the &#8211;user, &#8211;no-password, and &#8211;one-time-password options are mutually exclusive. At most one of them can be specified. </p>
<p> It is generally possible to use kerberos credentials to perform a join operation. Use the <code>kinit</code> command to acquire credentials prior to starting the join. Do not specify the <code>&#8211;user</code> argument, the user will be selected automatically from the credential cache. The <code>realm</code> respects the KRB5_CCACHE environment variable, but uses the default kerberos credential cache if it&#8217;s not present. Not all types of servers can be joined using kerberos credentials, some (like IPA) insist on prompting for a password. </p>
<p> The following options can be used: </p>
<p> <code>&#8211;automatic-id-mapping=no</code></p>
<dl>
<dd>Do not perform UID/GID mapping for users and groups, but expect these identifiers to be present in the domain already.</dl>
<p> <code>&#8211;user=xxx</code></p>
<dl>
<dd>The user name to be used to authenticate with when joining the machine to the realm. You will be prompted for a password.</dl>
<p> <code>&#8211;computer-ou=OU=xxx</code></p>
<dl>
<dd>The distinguished name of an organizational unit to create the computer account. The exact format of the distinguished name depends on the client software and membership software. You can usually omit the root DSE portion of distinguished name. This is an Active Directory specific option.</dl>
<p> <code>&#8211;computer-name=xxx</code></p>
<dl>
<dd>This option only applies to Active Directory realms. Specify this option to override the default name used when creating the computer account. The system&#8217;s FQDN will still be saved in the dNSHostName attribute. </p>
<p> Specify the name as a string of 15 or fewer characters that is a valid NetBIOS computer name.</dl>
<p> <code>&#8211;no-password</code></p>
<dl>
<dd>Perform the join automatically without a password.</dl>
<p> <code>&#8211;one-time-password=xxxx</code></p>
<dl>
<dd>Perform the join using a one time password specified on the command line. This is not possible with all types of realms.</dl>
<p> <code>&#8211;client-software=xxx</code></p>
<dl>
<dd>Only join realms for which we can use the given client software. Possible values include <i>sssd</i> or <i>winbind</i>. Not all values are supported for all realms. By default the client software is automatically selected.</dl>
<p> <code>&#8211;server-software=xxx</code></p>
<dl>
<dd>Only join realms for run the given server software. Possible values include <i>active-directory</i> or <i>ipa</i>.</dl>
<p> <code>&#8211;membership-software=xxx</code></p>
<dl>
<dd>The software to use when joining to the realm. Possible values include <i>samba</i> or <i>adcli</i>. Not all values are supported for all realms. By default the membership software is automatically selected.</dl>
<p> <code>&#8211;user-principal=</code><i>host/name [at] REALM</i></p>
<dl>
<dd>Set the userPrincipalName field of the computer account to this kerberos principal. If you omit the value for this option, then a principal will be set in the form of host/shortname [at] REALM</dl>
<p> <code>&#8211;os-name=xxx</code></p>
<dl>
<dd>The name of the operation system of the client. When joining an AD domain the value is store in the matching AD attribute.</dl>
<p> <code>&#8211;os-version=xxx</code></p>
<dl>
<dd>The version of the operation system of the client. When joining an AD domain the value is store in the matching AD attribute.</dl>
<h2>Leave</h2>
<p>Deconfigure the local machine for use with a realm. </p>
<dl>
<dd>
<pre>$ realm leave</pre>
</dl>
<dl>
<dd>
<pre>$ realm leave domain.example.com</pre>
</dl>
<p> If no realm name is specified, then the first configured realm will be used. </p>
<p> The following options can be used: </p>
<p> <code>&#8211;client-software=xxx</code></p>
<dl>
<dd>Only leave the realm which is using the given client software. Possible values include <i>sssd</i> or <i>winbind</i>.</dl>
<p> <code>&#8211;server-software=xxx</code></p>
<dl>
<dd>Only leave the realm which is using the given server software. Possible values include <i>active-directory</i> or <i>ipa</i>.</dl>
<p> <code>&#8211;remove</code></p>
<dl>
<dd>Remove or disable computer account from the directory while leaving the realm. This will usually prompt for a pasword.</dl>
<p> <code>&#8211;user</code></p>
<dl>
<dd>The user name to be used to authenticate with when leaving the realm. You will be prompted for a password. Implies <code>&#8211;remove</code>.</dl>
<h2>List</h2>
<p>List all the discovered and configured realms. </p>
<dl>
<dd>
<pre>$ realm list</pre>
</dl>
<p> By default, realms that have been discovered, but not configured (using the <code>join</code> command), are not displayed. Also, by default, the list of realm details displayed is verbose. The options below can be used to change this default behavior </p>
<p> The following options can be used: </p>
<p> <code>&#8211;all</code></p>
<dl>
<dd>Show all discovered realms (whether or not they have been configured).</dl>
<p> <code>&#8211;name-only</code></p>
<dl>
<dd>Display only realm names (as opposed to verbose output).</dl>
<h2>Permit</h2>
<p>Permit local login by users of the realm. </p>
<dl>
<dd>
<pre>$ realm permit --all
$ realm permit user [at] example.com
$ realm permit DOMAIN\User2
$ realm permit --withdraw user [at] example.com</pre>
</dl>
<p> The current login policy and format of the user names can be seen by using the <code>realm list</code> command. </p>
<p> The following options can be used: </p>
<p> <code>&#8211;all, -a</code></p>
<dl>
<dd>Permit logins using realm accounts on the local machine according to the realm policy.This usually defaults to allowing any realm user to log in.</dl>
<p> <code>&#8211;groups, -g</code></p>
<dl>
<dd>Treat the specified names as groups rather than user login names. Permit login by users in the specified groups.</dl>
<p> <code>&#8211;realm, -R</code></p>
<dl>
<dd>Specify the of the realm to change login policy for.</dl>
<p> <code>&#8211;withdraw, -x</code></p>
<dl>
<dd>Remove a login from the list of realm accounts permitted to log into the machine.</dl>
<h2>Deny</h2>
<p>Deny local login by realm accounts. </p>
<dl>
<dd>
<pre>$ realm deny --all</pre>
</dl>
<p> This command prevents realm accounts from logging into the local machine. Use <code>realm permit</code> to restrict logins to specific accounts. </p>
<p> The following options can be used: </p>
<p> <code>&#8211;all, -a</code></p>
<dl>
<dd>This option should be specified</dl>
<p> <code>&#8211;realm, -R</code></p>
<dl>
<dd>Specify the name of the realm to deny users login to.</dl>
<h2>Author</h2>
<p><code>Stef Walter</code> &lt;stef [at] thewalter.net&gt;</p>
<dl>
<dd>Maintainer</dl>
