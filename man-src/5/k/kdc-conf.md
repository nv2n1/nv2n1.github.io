---
title: "kdc-conf(5)"
name: "kdc-conf"
section: "5"
letter: "k"
url: "/docs/linux/man/5-kdc-conf/"
description: "kdc.conf – Kerberos V5 KDC configuration file"
---

<p>kdc.conf &#8211; Kerberos V5 KDC configuration file </p>
<p> The kdc.conf file supplements <i><a href="/docs/linux/man/5-krb5-conf/">krb5.conf</a>(5)</i> for programs which are typically only used on a KDC, such as the <i><a href="/docs/linux/man/8-krb5kdc/">krb5kdc</a>(8)</i> and <i><a href="/docs/linux/man/8-kadmind/">kadmind</a>(8)</i> daemons and the <i><a href="/docs/linux/man/8-kdb5_util/">kdb5_util</a>(8)</i> program. Relations documented here may also be specified in krb5.conf; for the KDC programs mentioned, krb5.conf and kdc.conf will be merged into a single configuration profile. </p>
<p> Normally, the kdc.conf file is found in the KDC state directory, <code>/var/kerberos</code><code>/krb5kdc</code>. You can override the default location by setting the environment variable <code>KRB5_KDC_PROFILE</code>. </p>
<p> Please note that you need to restart the KDC daemon for any configuration changes to take effect.</p>
<h2>Structure</h2>
<p>The kdc.conf file is set up in the same format as the <i><a href="/docs/linux/man/5-krb5-conf/">krb5.conf</a>(5)</i> file.</p>
<h2>Sections</h2>
<p>The kdc.conf file may contain the following sections: <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <i>[kdcdefaults]</i> </td>
<td> Default values for KDC behavior
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <i>[realms]</i> </td>
<td> Realm-specific database configuration and settings
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <i>[dbdefaults]</i> </td>
<td> Default database settings
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <i>[dbmodules]</i> </td>
<td> Per-database settings
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <i>[logging]</i> </td>
<td> Controls how Kerberos daemons perform logging
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center></p>
<h3>[kdcdefaults]</h3>
<p>With one exception, relations in the [kdcdefaults] section specify default values for realm variables, to be used if the [realms] subsection does not contain a relation for the tag. See the <i>[realms]</i> section for the definitions of these relations.</p>
<dl>
<dt>&bull;</p>
<dd><code>host_based_services</code></p>
<dt>&bull;</p>
<dd><code>kdc_ports</code></p>
<dt>&bull;</p>
<dd><code>kdc_tcp_ports</code></p>
<dt>&bull;</p>
<dd><code>no_host_referral</code></p>
<dt>&bull;</p>
<dd><code>restrict_anonymous_to_tgt</code></p>
<dt><code>kdc_max_dgram_reply_size</code></p>
<dd>Specifies the maximum packet size that can be sent over UDP. The default value is 4096 bytes.</dl>
<h3>[realms]</h3>
<p>Each tag in the [realms] section is the name of a Kerberos realm. The value of the tag is a subsection where the relations define KDC parameters for that particular realm. The following example shows how to define one parameter for the ATHENA.MIT.EDU realm: </p>
<pre>[realms]
 ATHENA.MIT.EDU = {
 max_renewable_life = 7d 0h 0m 0s
 }</pre>
<p>The following tags may be specified in a [realms] subsection:</p>
<dl>
<dt><code>acl_file</code></p>
<dd>(String.) Location of the access control list file that <i><a href="/docs/linux/man/8-kadmind/">kadmind</a>(8)</i> uses to determine which principals are allowed which permissions on the Kerberos database. The default value is <code>/var/kerberos</code><code>/krb5kdc</code><code>/kadm5.acl</code>. For more information on Kerberos ACL file see <i><a href="/docs/linux/man/5-kadm5-acl/">kadm5.acl</a>(5)</i>.</p>
<dt><code>database_module</code></p>
<dd>(String.) This relation indicates the name of the configuration section under <i>[dbmodules]</i> for database-specific parameters used by the loadable database library. The default value is the realm name. If this configuration section does not exist, default values will be used for all database parameters.</p>
<dt><code>database_name</code></p>
<dd>(String, deprecated.) This relation specifies the location of the Kerberos database for this realm, if the DB2 module is being used and the <i>[dbmodules]</i> configuration section does not specify a database name. The default value is <code>/var/kerberos</code><code>/krb5kdc</code><code>/principal</code>.</p>
<dt><code>default_principal_expiration</code></p>
<dd>(<i>abstime</i> string.) Specifies the default expiration date of principals created in this realm. The default value is 0, which means no expiration date.</p>
<dt><code>default_principal_flags</code></p>
<dd>(Flag string.) Specifies the default attributes of principals created in this realm. The format for this string is a comma-separated list of flags, with &#8216;+&#8217; before each flag that should be enabled and &#8216;-&#8216; before each flag that should be disabled. The <code>postdateable</code>, <code>forwardable</code>, <code>tgt-based</code>, <code>renewable</code>, <code>proxiable</code>, <code>dup-skey</code>, <code>allow-tickets</code>, and <code>service</code> flags default to enabled. </p>
<p> There are a number of possible flags:</p>
<dt><code>allow-tickets</code></p>
<dd>Enabling this flag means that the KDC will issue tickets for this principal. Disabling this flag essentially deactivates the principal within this realm.</p>
<dt><code>dup-skey</code></p>
<dd>Enabling this flag allows the principal to obtain a session key for another user, permitting user-to-user authentication for this principal.</p>
<dt><code>forwardable</code></p>
<dd>Enabling this flag allows the principal to obtain forwardable tickets.</p>
<dt><code>hwauth</code></p>
<dd>If this flag is enabled, then the principal is required to preauthenticate using a hardware device before receiving any tickets.</p>
<dt><code>no-auth-data-required</code></p>
<dd>Enabling this flag prevents PAC or AD-SIGNEDPATH data from being added to service tickets for the principal.</p>
<dt><code>ok-as-delegate</code></p>
<dd>If this flag is enabled, it hints the client that credentials can and should be delegated when authenticating to the service.</p>
<dt><code>ok-to-auth-as-delegate</code></p>
<dd>Enabling this flag allows the principal to use S4USelf tickets.</p>
<dt><code>postdateable</code></p>
<dd>Enabling this flag allows the principal to obtain postdateable tickets.</p>
<dt><code>preauth</code></p>
<dd>If this flag is enabled on a client principal, then that principal is required to preauthenticate to the KDC before receiving any tickets. On a service principal, enabling this flag means that service tickets for this principal will only be issued to clients with a TGT that has the preauthenticated bit set.</p>
<dt><code>proxiable</code></p>
<dd>Enabling this flag allows the principal to obtain proxy tickets.</p>
<dt><code>pwchange</code></p>
<dd>Enabling this flag forces a password change for this principal.</p>
<dt><code>pwservice</code></p>
<dd>If this flag is enabled, it marks this principal as a password change service. This should only be used in special cases, for example, if a user&#8217;s password has expired, then the user has to get tickets for that principal without going through the normal password authentication in order to be able to change the password.</p>
<dt><code>renewable</code></p>
<dd>Enabling this flag allows the principal to obtain renewable tickets.</p>
<dt><code>service</code></p>
<dd>Enabling this flag allows the the KDC to issue service tickets for this principal.</p>
<dt><code>tgt-based</code></p>
<dd>Enabling this flag allows a principal to obtain tickets based on a ticket-granting-ticket, rather than repeating the authentication process that was used to obtain the TGT.</p>
<dt><code>dict_file</code></p>
<dd>(String.) Location of the dictionary file containing strings that are not allowed as passwords. The file should contain one string per line, with no additional whitespace. If none is specified or if there is no policy assigned to the principal, no dictionary checks of passwords will be performed.</p>
<dt><code>host_based_services</code></p>
<dd>(Whitespace- or comma-separated list.) Lists services which will get host-based referral processing even if the server principal is not marked as host-based by the client.</p>
<dt><code>iprop_enable</code></p>
<dd>(Boolean value.) Specifies whether incremental database propagation is enabled. The default value is false.</p>
<dt><code>iprop_master_ulogsize</code></p>
<dd>(Integer.) Specifies the maximum number of log entries to be retained for incremental propagation. The default value is 1000. Prior to release 1.11, the maximum value was 2500.</p>
<dt><code>iprop_slave_poll</code></p>
<dd>(Delta time string.) Specifies how often the slave KDC polls for new updates from the master. The default value is <code>2m</code> (that is, two minutes).</p>
<dt><code>iprop_port</code></p>
<dd>(Port number.) Specifies the port number to be used for incremental propagation. This is required in both master and slave configuration files.</p>
<dt><code>iprop_resync_timeout</code></p>
<dd>(Delta time string.) Specifies the amount of time to wait for a full propagation to complete. This is optional in configuration files, and is used by slave KDCs only. The default value is 5 minutes (<code>5m</code>). New in release 1.11.</p>
<dt><code>iprop_logfile</code></p>
<dd>(File name.) Specifies where the update log file for the realm database is to be stored. The default is to use the <code>database_name</code> entry from the realms section of the krb5 config file, with <code>.ulog</code> appended. (NOTE: If <code>database_name</code> isn&#8217;t specified in the realms section, perhaps because the LDAP database back end is being used, or the file name is specified in the [dbmodules] section, then the hard-coded default for <code>database_name</code> is used. Determination of the <code>iprop_logfile</code> default value will not use values from the [dbmodules] section.)</p>
<dt><code>kadmind_port</code></p>
<dd>(Port number.) Specifies the port on which the <i><a href="/docs/linux/man/8-kadmind/">kadmind</a>(8)</i> daemon is to listen for this realm. The assigned port for kadmind is 749, which is used by default.</p>
<dt><code>key_stash_file</code></p>
<dd>(String.) Specifies the location where the master key has been stored (via kdb5_util stash). The default is <code>/var/kerberos</code><code>/krb5kdc</code><code>/.k5.REALM</code>, where <i>REALM</i> is the Kerberos realm.</p>
<dt><code>kdc_ports</code></p>
<dd>(Whitespace- or comma-separated list.) Lists the ports on which the Kerberos server should listen for UDP requests, as a comma-separated list of integers. The default value is <code>88,750</code>, which are the assigned Kerberos port and the port historically used by Kerberos V4.</p>
<dt><code>kdc_tcp_ports</code></p>
<dd>(Whitespace- or comma-separated list.) Lists the ports on which the Kerberos server should listen for TCP connections, as a comma-separated list of integers. To disable listening on TCP, set this relation to the empty string with <code>kdc_tcp_ports = &quot;&quot;</code>. If this relation is not specified, the default is to listen on TCP port 88 (the standard port). Prior to release 1.13, the default was not to listen for TCP connections at all.</p>
<dt><code>master_key_name</code></p>
<dd>(String.) Specifies the name of the principal associated with the master key. The default is <code>K/M</code>.</p>
<dt><code>master_key_type</code></p>
<dd>(Key type string.) Specifies the master key&#8217;s key type. The default value for this is <code>aes256-cts-hmac-sha1-96</code>. For a list of all possible values, see <i>Encryption types</i>.</p>
<dt><code>max_life</code></p>
<dd>(<i>duration</i> string.) Specifies the maximum time period for which a ticket may be valid in this realm. The default value is 24 hours.</p>
<dt><code>max_renewable_life</code></p>
<dd>(<i>duration</i> string.) Specifies the maximum time period during which a valid ticket may be renewed in this realm. The default value is 0.</p>
<dt><code>no_host_referral</code></p>
<dd>(Whitespace- or comma-separated list.) Lists services to block from getting host-based referral processing, even if the client marks the server principal as host-based or the service is also listed in <code>host_based_services</code>. <code>no_host_referral = *</code> will disable referral processing altogether.</p>
<dt><code>des_crc_session_supported</code></p>
<dd>(Boolean value). If set to true, the KDC will assume that service principals support des-cbc-crc for session key enctype negotiation purposes. If <code>allow_weak_crypto</code> in <i>libdefaults</i> is false, or if des-cbc-crc is not a permitted enctype, then this variable has no effect. Defaults to true. New in release 1.11.</p>
<dt><code>reject_bad_transit</code></p>
<dd>(Boolean value.) If set to true, the KDC will check the list of transited realms for cross-realm tickets against the transit path computed from the realm names and the capaths section of its <i><a href="/docs/linux/man/5-krb5-conf/">krb5.conf</a>(5)</i> file; if the path in the ticket to be issued contains any realms not in the computed path, the ticket will not be issued, and an error will be returned to the client instead. If this value is set to false, such tickets will be issued anyways, and it will be left up to the application server to validate the realm transit path. </p>
<p> If the disable-transited-check flag is set in the incoming request, this check is not performed at all. Having the <code>reject_bad_transit</code> option will cause such ticket requests to be rejected always. </p>
<p> This transit path checking and config file option currently apply only to TGS requests. </p>
<p> The default value is true.</p>
<dt><code>restrict_anonymous_to_tgt</code></p>
<dd>(Boolean value.) If set to true, the KDC will reject ticket requests from anonymous principals to service principals other than the realm&#8217;s ticket-granting service. This option allows anonymous PKINIT to be enabled for use as FAST armor tickets without allowing anonymous authentication to services. The default value is false. New in release 1.9.</p>
<dt><code>supported_enctypes</code></p>
<dd>(List of <i>key</i>:<i>salt</i> strings.) Specifies the default key/salt combinations of principals for this realm. Any principals created through <i><a href="/docs/linux/man/1-kadmin/">kadmin</a>(1)</i> will have keys of these types. The default value for this tag is <code>aes256-cts-hmac-sha1-96:normal aes128-cts-hmac-sha1-96:normal des3-cbc-sha1:normal arcfour-hmac-md5:normal</code>. For lists of possible values, see <i>Keysalt lists</i>.</dl>
<h3>[dbdefaults]</h3>
<p>The [dbdefaults] section specifies default values for some database parameters, to be used if the [dbmodules] subsection does not contain a relation for the tag. See the <i>[dbmodules]</i> section for the definitions of these relations.</p>
<dl>
<dt>&bull;</p>
<dd><code>ldap_kerberos_container_dn</code></p>
<dt>&bull;</p>
<dd><code>ldap_kdc_dn</code></p>
<dt>&bull;</p>
<dd><code>ldap_kdc_sasl_authcid</code></p>
<dt>&bull;</p>
<dd><code>ldap_kdc_sasl_authzid</code></p>
<dt>&bull;</p>
<dd><code>ldap_kdc_sasl_mech</code></p>
<dt>&bull;</p>
<dd><code>ldap_kdc_sasl_realm</code></p>
<dt>&bull;</p>
<dd><code>ldap_kadmind_dn</code></p>
<dt>&bull;</p>
<dd><code>ldap_kadmind_sasl_authcid</code></p>
<dt>&bull;</p>
<dd><code>ldap_kadmind_sasl_authzid</code></p>
<dt>&bull;</p>
<dd><code>ldap_kadmind_sasl_mech</code></p>
<dt>&bull;</p>
<dd><code>ldap_kadmind_sasl_realm</code></p>
<dt>&bull;</p>
<dd><code>ldap_service_password_file</code></p>
<dt>&bull;</p>
<dd><code>ldap_servers</code></p>
<dt>&bull;</p>
<dd><code>ldap_conns_per_server</code></dl>
<h3>[dbmodules]</h3>
<p>The [dbmodules] section contains parameters used by the KDC database library and database modules. Each tag in the [dbmodules] section is the name of a Kerberos realm or a section name specified by a realm&#8217;s <code>database_module</code> parameter. The following example shows how to define one database parameter for the ATHENA.MIT.EDU realm: </p>
<pre>[dbmodules]
 ATHENA.MIT.EDU = {
 disable_last_success = true
 }</pre>
<p>The following tags may be specified in a [dbmodules] subsection:</p>
<dl>
<dt><code>database_name</code></p>
<dd>This DB2-specific tag indicates the location of the database in the filesystem. The default is <code>/var/kerberos</code><code>/krb5kdc</code><code>/principal</code>.</p>
<dt><code>db_library</code></p>
<dd>This tag indicates the name of the loadable database module. The value should be <code>db2</code> for the DB2 module and <code>kldap</code> for the LDAP module.</p>
<dt><code>disable_last_success</code></p>
<dd>If set to <code>true</code>, suppresses KDC updates to the &quot;Last successful authentication&quot; field of principal entries requiring preauthentication. Setting this flag may improve performance. (Principal entries which do not require preauthentication never update the &quot;Last successful authentication&quot; field.). First introduced in release 1.9.</p>
<dt><code>disable_lockout</code></p>
<dd>If set to <code>true</code>, suppresses KDC updates to the &quot;Last failed authentication&quot; and &quot;Failed password attempts&quot; fields of principal entries requiring preauthentication. Setting this flag may improve performance, but also disables account lockout. First introduced in release 1.9.</p>
<dt><code>ldap_conns_per_server</code></p>
<dd>This LDAP-specific tag indicates the number of connections to be maintained per LDAP server.</p>
<dt><code>ldap_kdc_dn</code> and <code>ldap_kadmind_dn</code></p>
<dd>These LDAP-specific tags indicate the default DN for binding to the LDAP server. The <i><a href="/docs/linux/man/8-krb5kdc/">krb5kdc</a>(8)</i> daemon uses <code>ldap_kdc_dn</code>, while the <i><a href="/docs/linux/man/8-kadmind/">kadmind</a>(8)</i> daemon and other administrative programs use <code>ldap_kadmind_dn</code>. The kadmind DN must have the rights to read and write the Kerberos data in the LDAP database. The KDC DN must have the same rights, unless <code>disable_lockout</code> and <code>disable_last_success</code> are true, in which case it only needs to have rights to read the Kerberos data. These tags are ignored if a SASL mechanism is set with <code>ldap_kdc_sasl_mech</code> or <code>ldap_kadmind_sasl_mech</code>.</p>
<dt><code>ldap_kdc_sasl_mech</code> and <code>ldap_kadmind_sasl_mech</code></p>
<dd>These LDAP-specific tags specify the SASL mechanism (such as <code>EXTERNAL</code>) to use when binding to the LDAP server. New in release 1.13.</p>
<dt><code>ldap_kdc_sasl_authcid</code> and <code>ldap_kadmind_sasl_authcid</code></p>
<dd>These LDAP-specific tags specify the SASL authentication identity to use when binding to the LDAP server. Not all SASL mechanisms require an authentication identity. If the SASL mechanism requires a secret (such as the password for <code>DIGEST-MD5</code>), these tags also determine the name within the <code>ldap_service_password_file</code> where the secret is stashed. New in release 1.13.</p>
<dt><code>ldap_kdc_sasl_authzid</code> and <code>ldap_kadmind_sasl_authzid</code></p>
<dd>These LDAP-specific tags specify the SASL authorization identity to use when binding to the LDAP server. In most circumstances they do not need to be specified. New in release 1.13.</p>
<dt><code>ldap_kdc_sasl_realm</code> and <code>ldap_kadmind_sasl_realm</code></p>
<dd>These LDAP-specific tags specify the SASL realm to use when binding to the LDAP server. In most circumstances they do not need to be set. New in release 1.13.</p>
<dt><code>ldap_kerberos_container_dn</code></p>
<dd>This LDAP-specific tag indicates the DN of the container object where the realm objects will be located.</p>
<dt><code>ldap_servers</code></p>
<dd>This LDAP-specific tag indicates the list of LDAP servers that the Kerberos servers can connect to. The list of LDAP servers is whitespace-separated. The LDAP server is specified by a LDAP URI. It is recommended to use <code>ldapi:</code> or <code>ldaps:</code> URLs to connect to the LDAP server.</p>
<dt><code>ldap_service_password_file</code></p>
<dd>This LDAP-specific tag indicates the file containing the stashed passwords (created by <code>kdb5_ldap_util stashsrvpw</code>) for the <code>ldap_kdc_dn</code> and <code>ldap_kadmind_dn</code> objects, or for the <code>ldap_kdc_sasl_authcid</code> or <code>ldap_kadmind_sasl_authcid</code> names for SASL authentication. This file must be kept secure.</p>
<dt><code>unlockiter</code></p>
<dd>If set to <code>true</code>, this DB2-specific tag causes iteration operations to release the database lock while processing each principal. Setting this flag to <code>true</code> can prevent extended blocking of KDC or kadmin operations when dumps of large databases are in progress. First introduced in release 1.13. </p>
<p> The following tag may be specified directly in the [dbmodules] section to control where database modules are loaded from:</p>
<dt><code>db_module_dir</code></p>
<dd>This tag controls where the plugin system looks for database modules. The value should be an absolute path.</dl>
<h3>[logging]</h3>
<p>The [logging] section indicates how <i><a href="/docs/linux/man/8-krb5kdc/">krb5kdc</a>(8)</i> and <i><a href="/docs/linux/man/8-kadmind/">kadmind</a>(8)</i> perform logging. The keys in this section are daemon names, which may be one of:</p>
<dl>
<dt><code>admin_server</code></p>
<dd>Specifies how <i><a href="/docs/linux/man/8-kadmind/">kadmind</a>(8)</i> performs logging.</p>
<dt><code>kdc</code></p>
<dd>Specifies how <i><a href="/docs/linux/man/8-krb5kdc/">krb5kdc</a>(8)</i> performs logging.</p>
<dt><code>default</code></p>
<dd>Specifies how either daemon performs logging in the absence of relations specific to the daemon. </p>
<p> Values are of the following forms:</p>
<dt><code>FILE=</code><i>filename</i> or <code>FILE:</code><i>filename</i></p>
<dd>This value causes the daemon&#8217;s logging messages to go to the <i>filename</i>. If the <code>=</code> form is used, the file is overwritten. If the <code>:</code> form is used, the file is appended to.</p>
<dt><code>STDERR</code></p>
<dd>This value causes the daemon&#8217;s logging messages to go to its standard error stream.</p>
<dt><code>CONSOLE</code></p>
<dd>This value causes the daemon&#8217;s logging messages to go to the console, if the system supports it.</p>
<dt><code>DEVICE=</code><i>&lt;devicename&gt;</i></p>
<dd>This causes the daemon&#8217;s logging messages to go to the specified device.</p>
<dt><code>SYSLOG</code>[<code>:</code><i>severity</i>[<code>:</code><i>facility</i>]]</p>
<dd>This causes the daemon&#8217;s logging messages to go to the system log. </p>
<p> The severity argument specifies the default severity of system log messages. This may be any of the following severities supported by the <a href="/docs/linux/man/3-syslog/">syslog</a>(3) call, minus the <code>LOG_</code> prefix: <code>EMERG</code>, <code>ALERT</code>, <code>CRIT</code>, <code>ERR</code>, <code>WARNING</code>, <code>NOTICE</code>, <code>INFO</code>, and <code>DEBUG</code>. </p>
<p> The facility argument specifies the facility under which the messages are logged. This may be any of the following facilities supported by the <a href="/docs/linux/man/3-syslog/">syslog</a>(3) call minus the LOG_ prefix: <code>KERN</code>, <code>USER</code>, <code>MAIL</code>, <code>DAEMON</code>, <code>AUTH</code>, <code>LPR</code>, <code>NEWS</code>, <code>UUCP</code>, <code>CRON</code>, and <code>LOCAL0</code> through <code>LOCAL7</code>. </p>
<p> If no severity is specified, the default is <code>ERR</code>. If no facility is specified, the default is <code>AUTH</code>. </p>
<p> In the following example, the logging messages from the KDC will go to the console and to the system log under the facility LOG_DAEMON with default severity of LOG_INFO; and the logging messages from the administrative server will be appended to the file <code>/var/adm/kadmin.log</code> and sent to the device <code>/dev/tty04</code>. </p>
<pre>[logging]
 kdc = CONSOLE
 kdc = SYSLOG:INFO:DAEMON
 admin_server = FILE:/var/adm/kadmin.log
 admin_server = DEVICE=/dev/tty04</pre>
</dl>
<h3>[otp]</h3>
<p>Each subsection of [otp] is the name of an OTP token type. The tags within the subsection define the configuration required to forward a One Time Password request to a RADIUS server. </p>
<p> For each token type, the following tags may be specified:</p>
<dl>
<dt><code>server</code></p>
<dd>This is the server to send the RADIUS request to. It can be a hostname with optional port, an ip address with optional port, or a Unix domain socket address. The default is <code>/var/kerberos</code><code>/krb5kdc</code><code>/&lt;name&gt;.socket</code>.</p>
<dt><code>secret</code></p>
<dd>This tag indicates a filename (which may be relative to <code>/var/kerberos</code><code>/krb5kdc</code>) containing the secret used to encrypt the RADIUS packets. The secret should appear in the first line of the file by itself; leading and trailing whitespace on the line will be removed. If the value of <code>server</code> is a Unix domain socket address, this tag is optional, and an empty secret will be used if it is not specified. Otherwise, this tag is required.</p>
<dt><code>timeout</code></p>
<dd>An integer which specifies the time in seconds during which the KDC should attempt to contact the RADIUS server. This tag is the total time across all retries and should be less than the time which an OTP value remains valid for. The default is 5 seconds.</p>
<dt><code>retries</code></p>
<dd>This tag specifies the number of retries to make to the RADIUS server. The default is 3 retries (4 tries).</p>
<dt><code>strip_realm</code></p>
<dd>If this tag is <code>true</code>, the principal without the realm will be passed to the RADIUS server. Otherwise, the realm will be included. The default value is <code>true</code>.</p>
<dt><code>indicator</code></p>
<dd>This tag specifies an authentication indicator to be included in the ticket if this token type is used to authenticate. This option may be specified multiple times. (New in release 1.14.) </p>
<p> In the following example, requests are sent to a remote server via UDP: </p>
<pre>[otp]
 MyRemoteTokenType = {
 server = radius.mydomain.com:1812
 secret = SEmfiajf42$
 timeout = 15
 retries = 5
 strip_realm = true
 }</pre>
<p>An implicit default token type named <code>DEFAULT</code> is defined for when the per-principal configuration does not specify a token type. Its configuration is shown below. You may override this token type to something applicable for your situation: </p>
<pre>[otp]
 DEFAULT = {
 strip_realm = false
 }</pre>
</dl>
<h2>Pkinit Options</h2>
<p><code>NOTE:</code> The following are pkinit-specific options. These values may be specified in [kdcdefaults] as global defaults, or within a realm-specific subsection of [realms]. Also note that a realm-specific value over-rides, does not add to, a generic [kdcdefaults] specification. The search order is:</p>
<dl>
<dt>1.</p>
<dd>realm-specific subsection of [realms]: </p>
<pre>[realms]
 EXAMPLE.COM = {
 pkinit_anchors = FILE:/usr/local/example.com.crt
 }</pre>
<dt>2.</p>
<dd>generic value in the [kdcdefaults] section: </p>
<pre>[kdcdefaults]
 pkinit_anchors = DIR:/usr/local/generic_trusted_cas/</pre>
<p>For information about the syntax of some of these options, see <i>Specifying PKINIT identity information</i> in <i><a href="/docs/linux/man/5-krb5-conf/">krb5.conf</a>(5)</i>.</p>
<dt><code>pkinit_anchors</code></p>
<dd>Specifies the location of trusted anchor (root) certificates which the KDC trusts to sign client certificates. This option is required if pkinit is to be supported by the KDC. This option may be specified multiple times.</p>
<dt><code>pkinit_dh_min_bits</code></p>
<dd>Specifies the minimum number of bits the KDC is willing to accept for a client&#8217;s Diffie-Hellman key. The default is 2048.</p>
<dt><code>pkinit_allow_upn</code></p>
<dd>Specifies that the KDC is willing to accept client certificates with the Microsoft UserPrincipalName (UPN) Subject Alternative Name (SAN). This means the KDC accepts the binding of the UPN in the certificate to the Kerberos principal name. The default value is false. </p>
<p> Without this option, the KDC will only accept certificates with the id-pkinit-san as defined in <i>RFC 4556</i>. There is currently no option to disable SAN checking in the KDC.</p>
<dt><code>pkinit_eku_checking</code></p>
<dd>This option specifies what Extended Key Usage (EKU) values the KDC is willing to accept in client certificates. The values recognized in the kdc.conf file are:</p>
<dt><code>kpClientAuth</code></p>
<dd>This is the default value and specifies that client certificates must have the id-pkinit-KPClientAuth EKU as defined in <i>RFC 4556</i>.</p>
<dt><code>scLogin</code></p>
<dd>If scLogin is specified, client certificates with the Microsoft Smart Card Login EKU (id-ms-kp-sc-logon) will be accepted.</p>
<dt><code>none</code></p>
<dd>If none is specified, then client certificates will not be checked to verify they have an acceptable EKU. The use of this option is not recommended.</p>
<dt><code>pkinit_identity</code></p>
<dd>Specifies the location of the KDC&#8217;s X.509 identity information. This option is required if pkinit is to be supported by the KDC.</p>
<dt><code>pkinit_indicator</code></p>
<dd>Specifies an authentication indicator to include in the ticket if pkinit is used to authenticate. This option may be specified multiple times. (New in release 1.14.)</p>
<dt><code>pkinit_kdc_ocsp</code></p>
<dd>Specifies the location of the KDC&#8217;s OCSP.</p>
<dt><code>pkinit_pool</code></p>
<dd>Specifies the location of intermediate certificates which may be used by the KDC to complete the trust chain between a client&#8217;s certificate and a trusted anchor. This option may be specified multiple times.</p>
<dt><code>pkinit_revoke</code></p>
<dd>Specifies the location of Certificate Revocation List (CRL) information to be used by the KDC when verifying the validity of client certificates. This option may be specified multiple times.</p>
<dt><code>pkinit_require_crl_checking</code></p>
<dd>The default certificate verification process will always check the available revocation information to see if a certificate has been revoked. If a match is found for the certificate in a CRL, verification fails. If the certificate being verified is not listed in a CRL, or there is no CRL present for its issuing CA, and <code>pkinit_require_crl_checking</code> is false, then verification succeeds. </p>
<p> However, if <code>pkinit_require_crl_checking</code> is true and there is no CRL information available for the issuing CA, then verification fails. </p>
<p> <code>pkinit_require_crl_checking</code> should be set to true if the policy is such that up-to-date CRLs must be present for every CA.</dl>
<h2>Encryption Types</h2>
<p>Any tag in the configuration files which requires a list of encryption types can be set to some combination of the following strings. Encryption types marked as &quot;weak&quot; are available for compatibility but not recommended for use. <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> des-cbc-crc </td>
<td> DES cbc mode with CRC-32 (weak)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> des-cbc-md4 </td>
<td> DES cbc mode with RSA-MD4 (weak)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> des-cbc-md5 </td>
<td> DES cbc mode with RSA-MD5 (weak)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> des-cbc-raw </td>
<td> DES cbc mode raw (weak)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> des3-cbc-raw </td>
<td> Triple DES cbc mode raw (weak)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> des3-cbc-sha1 des3-hmac-sha1 des3-cbc-sha1-kd </td>
<td> Triple DES cbc mode with HMAC/sha1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> des-hmac-sha1 </td>
<td> DES with HMAC/sha1 (weak)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> aes256-cts-hmac-sha1-96 aes256-cts AES-256 </td>
<td> CTS mode with 96-bit SHA-1 HMAC
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> aes128-cts-hmac-sha1-96 aes128-cts AES-128 </td>
<td> CTS mode with 96-bit SHA-1 HMAC
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> arcfour-hmac rc4-hmac arcfour-hmac-md5 </td>
<td> RC4 with HMAC/MD5
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> arcfour-hmac-exp rc4-hmac-exp arcfour-hmac-md5-exp </td>
<td> Exportable RC4 with HMAC/MD5 (weak)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> camellia256-cts-cmac camellia256-cts </td>
<td> Camellia-256 CTS mode with CMAC
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> camellia128-cts-cmac camellia128-cts </td>
<td> Camellia-128 CTS mode with CMAC
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> des </td>
<td> The DES family: des-cbc-crc, des-cbc-md5, and des-cbc-md4 (weak)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> des3 </td>
<td> The triple DES family: des3-cbc-sha1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> aes </td>
<td> The AES family: aes256-cts-hmac-sha1-96 and aes128-cts-hmac-sha1-96
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> rc4 </td>
<td> The RC4 family: arcfour-hmac
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> camellia </td>
<td> The Camellia family: camellia256-cts-cmac and camellia128-cts-cmac
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center> </p>
<p> The string <code>DEFAULT</code> can be used to refer to the default set of types for the variable in question. Types or families can be removed from the current list by prefixing them with a minus sign (&quot;-&quot;). Types or families can be prefixed with a plus sign (&quot;+&quot;) for symmetry; it has the same meaning as just listing the type or family. For example, &quot;<code>DEFAULT -des</code>&quot; would be the default set of encryption types with DES types removed, and &quot;<code>des3 DEFAULT</code>&quot; would be the default set of encryption types with triple DES types moved to the front. </p>
<p> While <code>aes128-cts</code> and <code>aes256-cts</code> are supported for all Kerberos operations, they are not supported by very old versions of our GSSAPI implementation (krb5-1.3.1 and earlier). Services running versions of krb5 without AES support must not be given AES keys in the KDC database.</p>
<h2>Keysalt Lists</h2>
<p>Kerberos keys for users are usually derived from passwords. Kerberos commands and configuration parameters that affect generation of keys take lists of enctype-salttype (&quot;keysalt&quot;) pairs, known as <i>keysalt lists</i>. Each keysalt pair is an enctype name followed by a salttype name, in the format <i>enc</i>:<i>salt</i>. Individual keysalt list members are separated by comma (&quot;,&quot;) characters or space characters. For example: </p>
<pre>kadmin -e aes256-cts:normal,aes128-cts:normal</pre>
<p>would start up kadmin so that by default it would generate password-derived keys for the <code>aes256-cts</code> and <code>aes128-cts</code> encryption types, using a <code>normal</code> salt. </p>
<p> To ensure that people who happen to pick the same password do not have the same key, Kerberos 5 incorporates more information into the key using something called a salt. The supported salt types are as follows: <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> normal </td>
<td> default for Kerberos Version 5
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> v4 </td>
<td> the only type used by Kerberos Version 4 (no salt)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> norealm </td>
<td> same as the default, without using realm information
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> onlyrealm </td>
<td> uses only realm information as the salt
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> afs3 </td>
<td> AFS version 3, only used for compatibility with Kerberos 4 in AFS
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> special </td>
<td> generate a random salt
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center></p>
<h2>Sample Kdc.Conf File</h2>
<p>Here&#8217;s an example of a kdc.conf file: </p>
<pre>[kdcdefaults]
 kdc_ports = 88
[realms]
 ATHENA.MIT.EDU = {
 kadmind_port = 749
 max_life = 12h 0m 0s
 max_renewable_life = 7d 0h 0m 0s
 master_key_type = aes256-cts-hmac-sha1-96
 supported_enctypes = aes256-cts-hmac-sha1-96:normal aes128-cts-hmac-sha1-96:normal
 database_module = openldap_ldapconf
 }
[logging]
 kdc = FILE:/usr/local/var/krb5kdc/kdc.log
 admin_server = FILE:/usr/local/var/krb5kdc/kadmin.log
[dbdefaults]
 ldap_kerberos_container_dn = cn=krbcontainer,dc=mit,dc=edu
[dbmodules]
 openldap_ldapconf = {
 db_library = kldap
 disable_last_success = true
 ldap_kdc_dn = &quot;cn=krbadmin,dc=mit,dc=edu&quot;
 # this object needs to have read rights on
 # the realm container and principal subtrees
 ldap_kadmind_dn = &quot;cn=krbadmin,dc=mit,dc=edu&quot;
 # this object needs to have read and write rights on
 # the realm container and principal subtrees
 ldap_service_password_file = /etc/kerberos/service.keyfile
 ldap_servers = <a href="ldaps://kerberos.mit.edu">ldaps://kerberos.mit.edu</a>
 ldap_conns_per_server = 5
 }</pre>
<h2>Files</h2>
<p><code>/var/kerberos</code><code>/krb5kdc</code><code>/kdc.conf</code></p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-krb5-conf/">krb5.conf</a>(5)</i>, <i><a href="/docs/linux/man/8-krb5kdc/">krb5kdc</a>(8)</i>, <i><a href="/docs/linux/man/5-kadm5-acl/">kadm5.acl</a>(5)</i></p>
<h2>Author</h2>
<p>MIT</p>
<h2>Copyright</h2>
<p>1985-2016, MIT</p>
