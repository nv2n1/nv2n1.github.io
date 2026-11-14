---
title: "kadmin(1)"
name: "kadmin"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kadmin/"
description: "kadmin – Kerberos V5 database administration program"
---

<h2>NAME</h2>
<p> kadmin &#8211; Kerberos V5 database administration program</p>
<h2>SYNOPSIS</h2>
<p> <code>kadmin</code> [<code>-O</code>|<code>-N</code>] [<code>-r</code> <i>realm</i>] [<code>-p</code> <i>principal</i>] [<code>-q</code> <i>query</i>] [[<code>-c</code> <i>cache_name</i>]|[<code>-k</code> [<code>-t</code> <i>keytab</i>]]|<code>-n</code>] [<code>-w</code> <i>password</i>] [<code>-s</code> <i>admin_server</i>[:<i>port</i>]] [command args&#8230;] </p>
<p> <code>kadmin.local</code> [<code>-r</code> <i>realm</i>] [<code>-p</code> <i>principal</i>] [<code>-q</code> <i>query</i>] [<code>-d</code> <i>dbname</i>] [<code>-e</code> <i>enc</i>:<i>salt</i> &#8230;] [<code>-m</code>] [<code>-x</code> <i>db_args</i>] [command args&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> kadmin and kadmin.local are command-line interfaces to the Kerberos V5 administration system. They provide nearly identical functionalities; the difference is that kadmin.local directly accesses the KDC database, while kadmin performs operations using <i><a href="/docs/linux/man/8-kadmind/">kadmind</a>(8)</i>. Except as explicitly noted otherwise, this man page will use &quot;kadmin&quot; to refer to both versions. kadmin provides for the maintenance of Kerberos principals, password policies, and service key tables (keytabs). </p>
<p> The remote kadmin client uses Kerberos to authenticate to kadmind using the service principal <code>kadmin/ADMINHOST</code> (where <i>ADMINHOST</i> is the fully-qualified hostname of the admin server) or <code>kadmin/admin</code>. If the credentials cache contains a ticket for one of these principals, and the <code>-c</code> credentials_cache option is specified, that ticket is used to authenticate to kadmind. Otherwise, the <code>-p</code> and <code>-k</code> options are used to specify the client Kerberos principal name used to authenticate. Once kadmin has determined the principal name, it requests a service ticket from the KDC, and uses that service ticket to authenticate to kadmind. </p>
<p> Since kadmin.local directly accesses the KDC database, it usually must be run directly on the master KDC with sufficient permissions to read the KDC database. If the KDC database uses the LDAP database module, kadmin.local can be run on any host which can access the LDAP server.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-r</code> <i>realm</i></p>
<dd> Use <i>realm</i> as the default database realm.</p>
<dt><code>-p</code> <i>principal</i></p>
<dd> Use <i>principal</i> to authenticate. Otherwise, kadmin will append <code>/admin</code> to the primary principal name of the default ccache, the value of the <code>USER</code> environment variable, or the username as obtained with getpwuid, in order of preference.</p>
<dt><code>-k</code></p>
<dd> Use a keytab to decrypt the KDC response instead of prompting for a password. In this case, the default principal will be <code>host/hostname</code>. If there is no keytab specified with the <code>-t</code> option, then the default keytab will be used.</p>
<dt><code>-t</code> <i>keytab</i></p>
<dd> Use <i>keytab</i> to decrypt the KDC response. This can only be used with the <code>-k</code> option.</p>
<dt><code>-n</code></p>
<dd> Requests anonymous processing. Two types of anonymous principals are supported. For fully anonymous Kerberos, configure PKINIT on the KDC and configure <code>pkinit_anchors</code> in the client&#8217;s <i><a href="/docs/linux/man/5-krb5-conf/">krb5.conf</a>(5)</i>. Then use the <code>-n</code> option with a principal of the form <code>@REALM</code> (an empty principal name followed by the at-sign and a realm name). If permitted by the KDC, an anonymous ticket will be returned. A second form of anonymous tickets is supported; these realm-exposed tickets hide the identity of the client but not the client&#8217;s realm. For this mode, use <code>kinit -n</code> with a normal principal name. If supported by the KDC, the principal (but not realm) will be replaced by the anonymous principal. As of release 1.8, the MIT Kerberos KDC only supports fully anonymous operation.</p>
<dt><code>-c</code> <i>credentials_cache</i></p>
<dd> Use <i>credentials_cache</i> as the credentials cache. The cache should contain a service ticket for the <code>kadmin/ADMINHOST</code> (where <i>ADMINHOST</i> is the fully-qualified hostname of the admin server) or <code>kadmin/admin</code> service; it can be acquired with the <i><a href="/docs/linux/man/1-kinit/">kinit</a>(1)</i> program. If this option is not specified, kadmin requests a new service ticket from the KDC, and stores it in its own temporary ccache.</p>
<dt><code>-w</code> <i>password</i></p>
<dd> Use <i>password</i> instead of prompting for one. Use this option with care, as it may expose the password to other users on the system via the process list.</p>
<dt><code>-q</code> <i>query</i></p>
<dd> Perform the specified query and then exit.</p>
<dt><code>-d</code> <i>dbname</i></p>
<dd> Specifies the name of the KDC database. This option does not apply to the LDAP database module.</p>
<dt><code>-s</code> <i>admin_server</i>[:<i>port</i>]</p>
<dd> Specifies the admin server which kadmin should contact.</p>
<dt><code>-m</code></p>
<dd> If using kadmin.local, prompt for the database master password instead of reading it from a stash file.</p>
<dt><code>-e</code> <i>enc</i>:<i>salt</i> &#8230;</p>
<dd> Sets the keysalt list to be used for any new keys created. See <i>Keysalt_lists</i> in <i><a href="/docs/linux/man/5-kdc-conf/">kdc.conf</a>(5)</i> for a list of possible values.</p>
<dt><code>-O</code></p>
<dd> Force use of old AUTH_GSSAPI authentication flavor.</p>
<dt><code>-N</code></p>
<dd> Prevent fallback to AUTH_GSSAPI authentication flavor.</p>
<dt><code>-x</code> <i>db_args</i></p>
<dd> Specifies the database specific arguments. See the next section for supported options. </p>
<p> Starting with release 1.14, if any command-line arguments remain after the options, they will be treated as a single query to be executed. This mode of operation is intended for scripts and behaves differently from the interactive mode in several respects:</p>
<dt>&bull;</p>
<dd> Query arguments are split by the shell, not by kadmin.</p>
<dt>&bull;</p>
<dd> Informational and warning messages are suppressed. Error messages and query output (e.g. for <code>get_principal</code>) will still be displayed.</p>
<dt>&bull;</p>
<dd> Confirmation prompts are disabled (as if <code>-force</code> was given). Password prompts will still be issued as required.</p>
<dt>&bull;</p>
<dd> The exit status will be non-zero if the query fails. </p>
<p> The <code>-q</code> option does not carry these behavior differences; the query will be processed as if it was entered interactively. The <code>-q</code> option cannot be used in combination with a query in the remaining arguments.</dl>
<h2>DATABASE OPTIONS</h2>
<p> Database options can be used to override database-specific defaults. Supported options for the DB2 module are:</p>
<dl>
<dt><code>-x dbname=</code>*filename*</p>
<dd> Specifies the base filename of the DB2 database.</p>
<dt><code>-x lockiter</code></p>
<dd> Make iteration operations hold the lock for the duration of the entire operation, rather than temporarily releasing the lock while handling each principal. This is the default behavior, but this option exists to allow command line override of a [dbmodules] setting. First introduced in release 1.13.</p>
<dt><code>-x unlockiter</code></p>
<dd> Make iteration operations unlock the database for each principal, instead of holding the lock for the duration of the entire operation. First introduced in release 1.13. </p>
<p> Supported options for the LDAP module are:</p>
<dt><code>-x host=</code><i>ldapuri</i></p>
<dd> Specifies the LDAP server to connect to by a LDAP URI.</p>
<dt><code>-x binddn=</code><i>bind_dn</i></p>
<dd> Specifies the DN used to bind to the LDAP server.</p>
<dt><code>-x bindpwd=</code><i>password</i></p>
<dd> Specifies the password or SASL secret used to bind to the LDAP server. Using this option may expose the password to other users on the system via the process list; to avoid this, instead stash the password using the <code>stashsrvpw</code> command of <i><a href="/docs/linux/man/8-kdb5_ldap_util/">kdb5_ldap_util</a>(8)</i>.</p>
<dt><code>-x sasl_mech=</code><i>mechanism</i></p>
<dd> Specifies the SASL mechanism used to bind to the LDAP server. The bind DN is ignored if a SASL mechanism is used. New in release 1.13.</p>
<dt><code>-x sasl_authcid=</code><i>name</i></p>
<dd> Specifies the authentication name used when binding to the LDAP server with a SASL mechanism, if the mechanism requires one. New in release 1.13.</p>
<dt><code>-x sasl_authzid=</code><i>name</i></p>
<dd> Specifies the authorization name used when binding to the LDAP server with a SASL mechanism. New in release 1.13.</p>
<dt><code>-x sasl_realm=</code><i>realm</i></p>
<dd> Specifies the realm used when binding to the LDAP server with a SASL mechanism, if the mechanism uses one. New in release 1.13.</p>
<dt><code>-x debug=</code><i>level</i></p>
<dd> sets the OpenLDAP client library debug level. <i>level</i> is an integer to be interpreted by the library. Debugging messages are printed to standard error. New in release 1.12.</dl>
<h2>COMMANDS</h2>
<p> When using the remote client, available commands may be restricted according to the privileges specified in the <i><a href="/docs/linux/man/5-kadm5-acl/">kadm5.acl</a>(5)</i> file on the admin server.</p>
<h3>add_principal</h3>
<p> <code>add_principal</code> [<i>options</i>] <i>newprinc</i> </p>
<p> Creates the principal <i>newprinc</i>, prompting twice for a password. If no password policy is specified with the <code>-policy</code> option, and the policy named <code>default</code> is assigned to the principal if it exists. However, creating a policy named <code>default</code> will not automatically assign this policy to previously existing principals. This policy assignment can be suppressed with the <code>-clearpolicy</code> option. </p>
<p> This command requires the <code>add</code> privilege. </p>
<p> Aliases: <code>addprinc</code>, <code>ank</code> </p>
<p> Options:</p>
<dl>
<dt><code>-expire</code> <i>expdate</i></p>
<dd> (<i>getdate</i> string) The expiration date of the principal.</p>
<dt><code>-pwexpire</code> <i>pwexpdate</i></p>
<dd> (<i>getdate</i> string) The password expiration date.</p>
<dt><code>-maxlife</code> <i>maxlife</i></p>
<dd> (<i>duration</i> or <i>getdate</i> string) The maximum ticket life for the principal.</p>
<dt><code>-maxrenewlife</code> <i>maxrenewlife</i></p>
<dd> (<i>duration</i> or <i>getdate</i> string) The maximum renewable life of tickets for the principal.</p>
<dt><code>-kvno</code> <i>kvno</i></p>
<dd> The initial key version number.</p>
<dt><code>-policy</code> <i>policy</i></p>
<dd> The password policy used by this principal. If not specified, the policy <code>default</code> is used if it exists (unless <code>-clearpolicy</code> is specified).</p>
<dt><code>-clearpolicy</code></p>
<dd> Prevents any policy from being assigned when <code>-policy</code> is not specified.</p>
<dt><code>{-|+}allow_postdated</code></p>
<dd> <code>-allow_postdated</code> prohibits this principal from obtaining postdated tickets. <code>+allow_postdated</code> clears this flag.</p>
<dt><code>{-|+}allow_forwardable</code></p>
<dd> <code>-allow_forwardable</code> prohibits this principal from obtaining forwardable tickets. <code>+allow_forwardable</code> clears this flag.</p>
<dt><code>{-|+}allow_renewable</code></p>
<dd> <code>-allow_renewable</code> prohibits this principal from obtaining renewable tickets. <code>+allow_renewable</code> clears this flag.</p>
<dt><code>{-|+}allow_proxiable</code></p>
<dd> <code>-allow_proxiable</code> prohibits this principal from obtaining proxiable tickets. <code>+allow_proxiable</code> clears this flag.</p>
<dt><code>{-|+}allow_dup_skey</code></p>
<dd> <code>-allow_dup_skey</code> disables user-to-user authentication for this principal by prohibiting this principal from obtaining a session key for another user. <code>+allow_dup_skey</code> clears this flag.</p>
<dt><code>{-|+}requires_preauth</code></p>
<dd> <code>+requires_preauth</code> requires this principal to preauthenticate before being allowed to kinit. <code>-requires_preauth</code> clears this flag. When <code>+requires_preauth</code> is set on a service principal, the KDC will only issue service tickets for that service principal if the client&#8217;s initial authentication was performed using preauthentication.</p>
<dt><code>{-|+}requires_hwauth</code></p>
<dd> <code>+requires_hwauth</code> requires this principal to preauthenticate using a hardware device before being allowed to kinit. <code>-requires_hwauth</code> clears this flag. When <code>+requires_hwauth</code> is set on a service principal, the KDC will only issue service tickets for that service principal if the client&#8217;s initial authentication was performed using a hardware device to preauthenticate.</p>
<dt><code>{-|+}ok_as_delegate</code></p>
<dd> <code>+ok_as_delegate</code> sets the <code>okay as delegate</code> flag on tickets issued with this principal as the service. Clients may use this flag as a hint that credentials should be delegated when authenticating to the service. <code>-ok_as_delegate</code> clears this flag.</p>
<dt><code>{-|+}allow_svr</code></p>
<dd> <code>-allow_svr</code> prohibits the issuance of service tickets for this principal. <code>+allow_svr</code> clears this flag.</p>
<dt><code>{-|+}allow_tgs_req</code></p>
<dd> <code>-allow_tgs_req</code> specifies that a Ticket-Granting Service (TGS) request for a service ticket for this principal is not permitted. <code>+allow_tgs_req</code> clears this flag.</p>
<dt><code>{-|+}allow_tix</code></p>
<dd> <code>-allow_tix</code> forbids the issuance of any tickets for this principal. <code>+allow_tix</code> clears this flag.</p>
<dt><code>{-|+}needchange</code></p>
<dd> <code>+needchange</code> forces a password change on the next initial authentication to this principal. <code>-needchange</code> clears this flag.</p>
<dt><code>{-|+}password_changing_service</code></p>
<dd> <code>+password_changing_service</code> marks this principal as a password change service principal.</p>
<dt><code>{-|+}ok_to_auth_as_delegate</code></p>
<dd> <code>+ok_to_auth_as_delegate</code> allows this principal to acquire forwardable tickets to itself from arbitrary users, for use with constrained delegation.</p>
<dt><code>{-|+}no_auth_data_required</code></p>
<dd> <code>+no_auth_data_required</code> prevents PAC or AD-SIGNEDPATH data from being added to service tickets for the principal.</p>
<dt><code>{-|+}lockdown_keys</code></p>
<dd> <code>+lockdown_keys</code> prevents keys for this principal from leaving the KDC via kadmind. The chpass and extract operations are denied for a principal with this attribute. The chrand operation is allowed, but will not return the new keys. The delete and rename operations are also denied if this attribute is set, in order to prevent a malicious administrator from replacing principals like krbtgt/* or kadmin/* with new principals without the attribute. This attribute can be set via the network protocol, but can only be removed using kadmin.local.</p>
<dt><code>-randkey</code></p>
<dd> Sets the key of the principal to a random value.</p>
<dt><code>-nokey</code></p>
<dd> Causes the principal to be created with no key. New in release 1.12.</p>
<dt><code>-pw</code> <i>password</i></p>
<dd> Sets the password of the principal to the specified string and does not prompt for a password. Note: using this option in a shell script may expose the password to other users on the system via the process list.</p>
<dt><code>-e</code> <i>enc</i>:<i>salt</i>,&#8230;</p>
<dd> Uses the specified keysalt list for setting the keys of the principal. See <i>Keysalt_lists</i> in <i><a href="/docs/linux/man/5-kdc-conf/">kdc.conf</a>(5)</i> for a list of possible values.</p>
<dt><code>-x</code> <i>db_princ_args</i></p>
<dd> Indicates database-specific options. The options for the LDAP database module are:</p>
<dt><code>-x dn=</code><i>dn</i></p>
<dd> Specifies the LDAP object that will contain the Kerberos principal being created.</p>
<dt><code>-x linkdn=</code><i>dn</i></p>
<dd> Specifies the LDAP object to which the newly created Kerberos principal object will point.</p>
<dt><code>-x containerdn=</code><i>container_dn</i></p>
<dd> Specifies the container object under which the Kerberos principal is to be created.</p>
<dt><code>-x tktpolicy=</code><i>policy</i></p>
<dd> Associates a ticket policy to the Kerberos principal. </p>
<p> <code>NOTE:</code></p>
<dt>&bull;</p>
<dd> The <code>containerdn</code> and <code>linkdn</code> options cannot be specified with the <code>dn</code> option.</p>
<dt>&bull;</p>
<dd> If the <i>dn</i> or <i>containerdn</i> options are not specified while adding the principal, the principals are created under the principal container configured in the realm or the realm container.</p>
<dt>&bull;</p>
<dd> <i>dn</i> and <i>containerdn</i> should be within the subtrees or principal container configured in the realm. </p>
<p> Example: </p>
<pre><code>
kadmin: addprinc jennifer
WARNING: no policy specified for "jennifer [at] ATHENA.MIT.EDU";
defaulting to no policy.
Enter password for principal jennifer [at] ATHENA.MIT.EDU:
Re-enter password for principal jennifer [at] ATHENA.MIT.EDU:
Principal "jennifer [at] ATHENA.MIT.EDU" created.
kadmin:
</code></pre>
</dl>
<h3>modify_principal</h3>
<p> <code>modify_principal</code> [<i>options</i>] <i>principal</i> </p>
<p> Modifies the specified principal, changing the fields as specified. The options to <code>add_principal</code> also apply to this command, except for the <code>-randkey</code>, <code>-pw</code>, and <code>-e</code> options. In addition, the option <code>-clearpolicy</code> will clear the current policy of a principal. </p>
<p> This command requires the <i>modify</i> privilege. </p>
<p> Alias: <code>modprinc</code> </p>
<p> Options (in addition to the <code>addprinc</code> options):</p>
<dl>
<dt><code>-unlock</code></p>
<dd> Unlocks a locked principal (one which has received too many failed authentication attempts without enough time between them according to its password policy) so that it can successfully authenticate.</dl>
<h3>rename_principal</h3>
<p> <code>rename_principal</code> [<code>-force</code>] <i>old_principal</i> <i>new_principal</i> </p>
<p> Renames the specified <i>old_principal</i> to <i>new_principal</i>. This command prompts for confirmation, unless the <code>-force</code> option is given. </p>
<p> This command requires the <code>add</code> and <code>delete</code> privileges. </p>
<p> Alias: <code>renprinc</code></p>
<h3>delete_principal</h3>
<p> <code>delete_principal</code> [<code>-force</code>] <i>principal</i> </p>
<p> Deletes the specified <i>principal</i> from the database. This command prompts for deletion, unless the <code>-force</code> option is given. </p>
<p> This command requires the <code>delete</code> privilege. </p>
<p> Alias: <code>delprinc</code></p>
<h3>change_password</h3>
<p> <code>change_password</code> [<i>options</i>] <i>principal</i> </p>
<p> Changes the password of <i>principal</i>. Prompts for a new password if neither <code>-randkey</code> or <code>-pw</code> is specified. </p>
<p> This command requires the <code>changepw</code> privilege, or that the principal running the program is the same as the principal being changed. </p>
<p> Alias: <code>cpw</code> </p>
<p> The following options are available:</p>
<dl>
<dt><code>-randkey</code></p>
<dd> Sets the key of the principal to a random value.</p>
<dt><code>-pw</code> <i>password</i></p>
<dd> Set the password to the specified string. Using this option in a script may expose the password to other users on the system via the process list.</p>
<dt><code>-e</code> <i>enc</i>:<i>salt</i>,&#8230;</p>
<dd> Uses the specified keysalt list for setting the keys of the principal. See <i>Keysalt_lists</i> in <i><a href="/docs/linux/man/5-kdc-conf/">kdc.conf</a>(5)</i> for a list of possible values.</p>
<dt><code>-keepold</code></p>
<dd> Keeps the existing keys in the database. This flag is usually not necessary except perhaps for <code>krbtgt</code> principals. </p>
<p> Example: </p>
<p>kadmin: cpw systest<br />
Enter password for principal systest [at] BLEEP.COM:<br />
Re-enter password for principal systest [at] BLEEP.COM:<br />
Password for systest [at] BLEEP.COM changed.<br />
kadmin:
</dl>
<h3>purgekeys</h3>
<p> <code>purgekeys</code> [<code>-all</code>|<code>-keepkvno</code> <i>oldest_kvno_to_keep</i>] <i>principal</i> </p>
<p> Purges previously retained old keys (e.g., from <code>change_password -keepold</code>) from <i>principal</i>. If <code>-keepkvno</code> is specified, then only purges keys with kvnos lower than <i>oldest_kvno_to_keep</i>. If <code>-all</code> is specified, then all keys are purged. The <code>-all</code> option is new in release 1.12. </p>
<p> This command requires the <code>modify</code> privilege.</p>
<h3>get_principal</h3>
<p> <code>get_principal</code> [<code>-terse</code>] <i>principal</i> </p>
<p> Gets the attributes of principal. With the <code>-terse</code> option, outputs fields as quoted tab-separated strings. </p>
<p> This command requires the <code>inquire</code> privilege, or that the principal running the the program to be the same as the one being listed. </p>
<p> Alias: <code>getprinc</code> </p>
<p> Examples: </p>
<p>kadmin : getprinc tlyu / admin Principal : tlyu / admin[at] BLEEP.COM Expiration date : [never] Last password change : Mon Aug 12 14 : 16 : 47 EDT 1996 Password expiration date : [none] Maximum ticket life : 0 days 10 : 00 : 00 Maximum renewable life : 7 days 00 : 00 : 00 Last modified : Mon Aug 12 14 : 16 : 47 EDT 1996(bjaspan / admin[at] BLEEP.COM) Last successful authentication : [never] Last failed authentication : [never] Failed password attempts : 0 Number of keys : 2 Key : vno 1, des &#8211; cbc &#8211; crc Key : vno 1, des &#8211; cbc &#8211; crc : v4 Attributes : Policy : [none] kadmin : getprinc &#8211; terse systest systest[at] BLEEP.COM 3 86400 604800 1 785926535 753241234 785900000 tlyu / admin[at] BLEEP.COM 786100034 0 0 kadmin:</p>
<h3>list_principals</h3>
<p> <code>list_principals</code> [<i>expression</i>] </p>
<p> Retrieves all or some principal names. <i>expression</i> is a shell-style glob expression that can contain the wild-card characters <code>?</code>, <code>*</code>, and <code>[]</code>. All principal names matching the expression are printed. If no expression is provided, all principal names are printed. If the expression does not contain an <code>@</code> character, an <code>@</code> character followed by the local realm is appended to the expression. </p>
<p> This command requires the <code>list</code> privilege. </p>
<p> Alias: <code>listprincs</code>, <code>get_principals</code>, <code>get_princs</code> </p>
<p> Example: </p>
<p>kadmin : listprincs test *<br />
             test3[at] SECURE &#8211;<br />
         TEST.OV.COM<br />
             test2[at] SECURE &#8211;<br />
         TEST.OV.COM<br />
             test1[at] SECURE &#8211;<br />
         TEST.OV.COM<br />
             testuser[at] SECURE &#8211;<br />
         TEST.OV.COM<br />
             kadmin:</p>
<h3>get_strings</h3>
<p> <code>get_strings</code> <i>principal</i> </p>
<p> Displays string attributes on <i>principal</i>. </p>
<p> This command requires the <code>inquire</code> privilege. </p>
<p> Alias: <code>getstr</code></p>
<h3>set_string</h3>
<p> <code>set_string</code> <i>principal</i> <i>name</i> <i>value</i> </p>
<p> Sets a string attribute on <i>principal</i>. String attributes are used to supply per-principal configuration to the KDC and some KDC plugin modules. The following string attribute names are recognized by the KDC:</p>
<dl>
<dt><code>require_auth</code></p>
<dd> Specifies an authentication indicator which is required to authenticate to the principal as a service. Multiple indicators can be specified, separated by spaces; in this case any of the specified indicators will be accepted. (New in release 1.14.)</p>
<dt><code>session_enctypes</code></p>
<dd> Specifies the encryption types supported for session keys when the principal is authenticated to as a server. See <i>Encryption_types</i> in <i><a href="/docs/linux/man/5-kdc-conf/">kdc.conf</a>(5)</i> for a list of the accepted values.</p>
<dt><code>otp</code></p>
<dd> Enables One Time Passwords (OTP) preauthentication for a client <i>principal</i>. The <i>value</i> is a JSON string representing an array of objects, each having optional <code>type</code> and <code>username</code> fields. </p>
<p> This command requires the <code>modify</code> privilege. </p>
<p> Alias: <code>setstr</code> </p>
<p> Example: </p>
<p>set_string host / foo.mit.edu session_enctypes aes128 &#8211; cts<br />
                                                            set_string user[at] FOO.COM otp &#8220;[{&#8221;<br />
                                                                                            &#8220;type&#8221;<br />
                                                                                            &#8220;:&#8221;<br />
                                                                                            &#8220;hotp&#8221;<br />
                                                                                            &#8220;,&#8221;<br />
                                                                                            &#8220;username&#8221;<br />
                                                                                            &#8220;:&#8221;<br />
                                                                                            &#8220;al&#8221;<br />
                                                                                            &#8220;}]&#8221;
</dl>
<h3>del_string</h3>
<p> <code>del_string</code> <i>principal</i> <i>key</i> </p>
<p> Deletes a string attribute from <i>principal</i>. </p>
<p> This command requires the <code>delete</code> privilege. </p>
<p> Alias: <code>delstr</code></p>
<h3>add_policy</h3>
<p> <code>add_policy</code> [<i>options</i>] <i>policy</i> </p>
<p> Adds a password policy named <i>policy</i> to the database. </p>
<p> This command requires the <code>add</code> privilege. </p>
<p> Alias: <code>addpol</code> </p>
<p> The following options are available:</p>
<dl>
<dt><code>-maxlife</code> <i>time</i></p>
<dd> (<i>duration</i> or <i>getdate</i> string) Sets the maximum lifetime of a password.</p>
<dt><code>-minlife</code> <i>time</i></p>
<dd> (<i>duration</i> or <i>getdate</i> string) Sets the minimum lifetime of a password.</p>
<dt><code>-minlength</code> <i>length</i></p>
<dd> Sets the minimum length of a password.</p>
<dt><code>-minclasses</code> <i>number</i></p>
<dd> Sets the minimum number of character classes required in a password. The five character classes are lower case, upper case, numbers, punctuation, and whitespace/unprintable characters.</p>
<dt><code>-history</code> <i>number</i></p>
<dd> Sets the number of past keys kept for a principal. This option is not supported with the LDAP KDC database module.</p>
<dt><code>-maxfailure</code> <i>maxnumber</i></p>
<dd> Sets the number of authentication failures before the principal is locked. Authentication failures are only tracked for principals which require preauthentication. The counter of failed attempts resets to 0 after a successful attempt to authenticate. A <i>maxnumber</i> value of 0 (the default) disables lockout.</p>
<dt><code>-failurecountinterval</code> <i>failuretime</i></p>
<dd> (<i>duration</i> or <i>getdate</i> string) Sets the allowable time between authentication failures. If an authentication failure happens after <i>failuretime</i> has elapsed since the previous failure, the number of authentication failures is reset to 1. A <i>failuretime</i> value of 0 (the default) means forever.</p>
<dt><code>-lockoutduration</code> <i>lockouttime</i></p>
<dd> (<i>duration</i> or <i>getdate</i> string) Sets the duration for which the principal is locked from authenticating if too many authentication failures occur without the specified failure count interval elapsing. A duration of 0 (the default) means the principal remains locked out until it is administratively unlocked with <code>modprinc -unlock</code>.</p>
<dt><code>-allowedkeysalts</code></p>
<dd> Specifies the key/salt tuples supported for long-term keys when setting or changing a principal&#8217;s password/keys. See <i>Keysalt_lists</i> in <i><a href="/docs/linux/man/5-kdc-conf/">kdc.conf</a>(5)</i> for a list of the accepted values, but note that key/salt tuples must be separated with commas (&#8216;,&#8217;) only. To clear the allowed key/salt policy use a value of &#8216;-&#8216;. </p>
<p> Example: </p>
<pre>
kadmin: add_policy -maxlife &quot;2 days&quot; -minlength 5 guests
kadmin:
</pre>
</dl>
<h3>modify_policy</h3>
<p> <code>modify_policy</code> [<i>options</i>] <i>policy</i> </p>
<p> Modifies the password policy named <i>policy</i>. Options are as described for <code>add_policy</code>. </p>
<p> This command requires the <code>modify</code> privilege. </p>
<p> Alias: <code>modpol</code></p>
<h3>delete_policy</h3>
<p> <code>delete_policy</code> [<code>-force</code>] <i>policy</i> </p>
<p> Deletes the password policy named <i>policy</i>. Prompts for confirmation before deletion. The command will fail if the policy is in use by any principals. </p>
<p> This command requires the <code>delete</code> privilege. </p>
<p> Alias: <code>delpol</code> </p>
<p> Example: </p>
<pre>
kadmin: del_policy guests
Are you sure you want to delete the policy &quot;guests&quot;?
(yes/no): yes
kadmin:
</pre>
<h3>get_policy</h3>
<p> <code>get_policy</code> [ <code>-terse</code> ] <i>policy</i> </p>
<p> Displays the values of the password policy named <i>policy</i>. With the <code>-terse</code> flag, outputs the fields as quoted strings separated by tabs. </p>
<p> This command requires the <code>inquire</code> privilege. </p>
<p> Alias: getpol </p>
<p> Examples: </p>
<pre>
kadmin: get_policy admin
Policy: admin
Maximum password life: 180 days 00:00:00
Minimum password life: 00:00:00
Minimum password length: 6
Minimum number of password character classes: 2
Number of old keys kept: 5
Reference count: 17
kadmin: get_policy -terse admin
admin     15552000  0    6    2    5    17
kadmin:
</pre>
<p> The &quot;Reference count&quot; is the number of principals using that policy. With the LDAP KDC database module, the reference count field is not meaningful.</p>
<h3>list_policies</h3>
<p> <code>list_policies</code> [<i>expression</i>] </p>
<p> Retrieves all or some policy names. <i>expression</i> is a shell-style glob expression that can contain the wild-card characters <code>?</code>, <code>*</code>, and <code>[]</code>. All policy names matching the expression are printed. If no expression is provided, all existing policy names are printed. </p>
<p> This command requires the <code>list</code> privilege. </p>
<p> Aliases: <code>listpols</code>, <code>get_policies</code>, <code>getpols</code>. </p>
<p> Examples: </p>
<pre>
kadmin:  listpols
test-pol
dict-only
once-a-min
test-pol-nopw
kadmin:  listpols t*
test-pol
test-pol-nopw
kadmin:
</pre>
<h3>ktadd</h3>
<pre><code>
ktadd[options] principal
        ktadd[options] -
    glob princ - exp
</code></pre>
<p> Adds a <i>principal</i>, or all principals matching <i>princ-exp</i>, to a keytab file. Each principal&#8217;s keys are randomized in the process. The rules for <i>princ-exp</i> are described in the <code>list_principals</code> command. </p>
<p> This command requires the <code>inquire</code> and <code>changepw</code> privileges. With the <code>-glob</code> form, it also requires the <code>list</code> privilege. </p>
<p> The options are:</p>
<dl>
<dt><code>-k[eytab]</code> <i>keytab</i></p>
<dd> Use <i>keytab</i> as the keytab file. Otherwise, the default keytab is used.</p>
<dt><code>-e</code> <i>enc</i>:<i>salt</i>,&#8230;</p>
<dd> Uses the specified keysalt list for setting the new keys of the principal. See <i>Keysalt_lists</i> in <i><a href="/docs/linux/man/5-kdc-conf/">kdc.conf</a>(5)</i> for a list of possible values.</p>
<dt><code>-q</code></p>
<dd> Display less verbose information.</p>
<dt><code>-norandkey</code></p>
<dd> Do not randomize the keys. The keys and their version numbers stay unchanged. This option cannot be specified in combination with the <code>-e</code> option. </p>
<p> An entry for each of the principal&#8217;s unique encryption types is added, ignoring multiple keys with the same encryption type but different salt types. </p>
<p> Example: </p>
<pre>
kadmin: ktadd -k /tmp/foo-new-keytab host/foo.mit.edu
Entry for principal host/foo.mit.edu [at] ATHENA.MIT.EDU with kvno 3,
     encryption type aes256-cts-hmac-sha1-96 added to keytab
     FILE:/tmp/foo-new-keytab
kadmin:
</pre>
</dl>
<h3>ktremove</h3>
<p> <code>ktremove</code> [options] <i>principal</i> [<i>kvno</i> | <i>all</i> | <i>old</i>] </p>
<p> Removes entries for the specified <i>principal</i> from a keytab. Requires no permissions, since this does not require database access. </p>
<p> If the string &quot;all&quot; is specified, all entries for that principal are removed; if the string &quot;old&quot; is specified, all entries for that principal except those with the highest kvno are removed. Otherwise, the value specified is parsed as an integer, and all entries whose kvno match that integer are removed. </p>
<p> The options are:</p>
<dl>
<dt><code>-k[eytab]</code> <i>keytab</i></p>
<dd> Use <i>keytab</i> as the keytab file. Otherwise, the default keytab is used.</p>
<dt><code>-q</code></p>
<dd> Display less verbose information. </p>
<p> Example: </p>
<pre>
kadmin: ktremove kadmin/admin all
Entry for principal kadmin/admin with kvno 3 removed from keytab
     FILE:/etc/krb5.keytab
kadmin:
</pre>
</dl>
<h3>lock</h3>
<p> Lock database exclusively. Use with extreme caution! This command only works with the DB2 KDC database module.</p>
<h3>unlock</h3>
<p> Release the exclusive database lock.</p>
<h3>list_requests</h3>
<p> Lists available for kadmin requests. </p>
<p> Aliases: <code>lr</code>, <code>?</code></p>
<h3>quit</h3>
<p> Exit program. If the database was locked, the lock is released. </p>
<p> Aliases: <code>exit</code>, <code>q</code></p>
<h2>HISTORY</h2>
<p> The kadmin program was originally written by Tom Yu at MIT, as an interface to the OpenVision Kerberos administration program.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-kpasswd/">kpasswd</a>(1)</i>, <i><a href="/docs/linux/man/8-kadmind/">kadmind</a>(8)</i></p>
<h2>AUTHOR</h2>
<p> MIT</p>
<h2>COPYRIGHT</h2>
<p> 1985-2017, MIT </p>
<h2>Index</h2>
