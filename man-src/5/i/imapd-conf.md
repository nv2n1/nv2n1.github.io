---
title: "imapd-conf(5)"
name: "imapd-conf"
section: "5"
letter: "i"
url: "/docs/linux/man/5-imapd-conf/"
description: "imapd.conf – IMAP configuration file"
---

<p>*</p>
<h2>Name</h2>
<p>imapd.conf &#8211; IMAP configuration file</p>
<h2>Description</h2>
<p><code>/etc/imapd.conf</code> is the configuration file for the Cyrus IMAP server. It defines local parameters for IMAP. </p>
<p> Each line of the <code>/etc/imapd.conf</code> file has the form</p>
<dl>
<dd><i>option</i>: <i>value</i></dd></dl>
<p> where <i>option</i> is the name of the configuration option being set and <i>value</i> is the value that the configuration option is being set to. </p>
<p> Although there is no limit to the length of a line, a &#8220;\&#8221; (backslash) character may be used as the last character on a line to force it to continue on the next one. No additional whitespace is inserted before or after the &#8220;\&#8221;. Note that a line that is split using &#8220;\&#8221; character(s) is still considered a single line. For example</p>
<dl>
<dd><i>option</i>:\<br />
 <i>value</i>1 <i>value</i>2 \<br />
 <i>value</i>3</dd></dl>
<p> is equivalent to</p>
<dl>
<dd><i>option</i>: <i>value</i>1 <i>value</i>2 <i>value</i>3</dd></dl>
<p> Blank lines and lines beginning with &#8220;#&#8221; are ignored. </p>
<p> For boolean and enumerated options, the values &#8220;yes&#8221;, &#8220;on&#8221;, &#8220;t&#8221;, &#8220;true&#8221; and &#8220;1&#8221; turn the option on, the values &#8220;no&#8221;, &#8220;off&#8221;, &#8220;f&#8221;, &#8220;false&#8221; and &#8220;0&#8221; turn the option off.</p>
<h2>Field Descriptions</h2>
<p>The sections below detail options that can be placed in the <code>/etc/imapd.conf</code> file, and show each option&#8217;s default value. Some options have no default value, these are listed with &#8220;&lt;no default&gt;&#8221;. Some options default to the empty string, these are listed with &#8220;&lt;none&gt;&#8221;. </p>
<dl>
<dt><code>admins:</code> &lt;empty string&gt;</dt>
<dd>The list of userids with administrative rights. Separate each userid with a space. Sites using Kerberos authentication may use separate &quot;admin&quot; instances.</dd></dl>
<p> Note that accounts used by users should not be administrators. Administrative accounts should not receive mail. That is, if user &quot;jbRo&quot; is a user reading mail, he should not also be in the admins line. Some problems may occur otherwise, most notably the ability of administrators to create top-level mailboxes visible to users, but not writable by users.</p>
<dl>
<dt><code>afspts_localrealms:</code> &lt;none&gt;</dt>
<dd>The list of realms which are to be treated as local, and thus stripped during identifier canonicalization (for the AFSPTS ptloader module). This is different from loginrealms in that it occurs later in the authorization process (as the user id is canonified for PTS lookup)</dd>
<dt><code>afspts_mycell:</code> &lt;none&gt;</dt>
<dd>Cell to use for AFS PTS lookups. Defaults to the local cell.</dd>
<dt><code>allowallsubscribe:</code> 0</dt>
<dd>Allow subscription to nonexistent mailboxes. This option is typically used on backend servers in a Murder so that users can subscribe to mailboxes that don&#8217;t reside on their &quot;home&quot; server. This option can also be used as a workaround for IMAP clients which don&#8217;t play well with nonexistent or unselectable mailboxes (e.g., Microsoft Outlook).</dd>
<dt><code>allowanonymouslogin:</code> 0</dt>
<dd>Permit logins by the user &quot;anonymous&quot; using any password. Also allows use of the SASL ANONYMOUS mechanism.</dd>
<dt><code>allowapop:</code> 1</dt>
<dd>Allow use of the POP3 APOP authentication command.</dd></dl>
<p> Note that this command requires that SASL is compiled with APOP support, that the plaintext passwords are available in a SASL auxprop backend (e.g., sasldb), and that the system can provide enough entropy (e.g., from /dev/urandom) to create a challenge in the banner.</p>
<dl>
<dt><code>allownewnews:</code> 0</dt>
<dd>Allow use of the NNTP NEWNEWS command.</dd></dl>
<p> Note that this is a very expensive command and should only be enabled when absolutely necessary.</p>
<dl>
<dt><code>allowplaintext:</code> 0</dt>
<dd>Allow the use of cleartext passwords on the wire.</dd>
<dt><code>allowusermoves:</code> 0</dt>
<dd>Allow moving user accounts (with associated meta-data) via RENAME or XFER.</dd></dl>
<p> Note that measures should be taken to make sure that the user being moved is not logged in, and cannot login during the move. Failure to do so may result in the user&#8217;s meta-data (seen state, subscriptions, etc) being corrupted or out of date.</p>
<dl>
<dt><code>altnamespace:</code> 0</dt>
<dd>Use the alternate IMAP namespace, where personal folders reside at the same level in the hierarchy as INBOX.</dd></dl>
<p> This option ONLY applies where interaction takes place with the client/user. Currently this is limited to the IMAP protocol (imapd) and Sieve scripts (lmtpd). This option does NOT apply to admin tools such as cyradm (admins ONLY), reconstruct, quota, etc., NOR does it affect LMTP delivery of messages directly to mailboxes via plus-addressing.</p>
<dl>
<dt><code>annotation_db:</code> skiplist</dt>
<dd>The cyrusdb backend to use for mailbox annotations. </dd>
<p> Allowed values: <i>berkeley</i>, <i>berkeley-hash</i>, <i>skiplist</i></p>
<dt><code>annotation_db_path:</code> &lt;none&gt;</dt>
<dd>The absolute path to the annotations db file. If not specified, will be confdir/annotations.db</dd>
<dt><code>anyoneuseracl:</code> 1</dt>
<dd>Should non-admin users be allowed to set ACLs for the &#8216;anyone&#8217; user on their mailboxes? In a large organization this can cause support problems, but it&#8217;s enabled by default.</dd>
<dt><code>annotation_definitions:</code> &lt;none&gt;</dt>
<dd>File containing external (third-party) annotation definitions.</dd></dl>
<p> Each line of the file specifies the properties of an annotation and has the following form:</p>
<dl>
<dd><i>name</i>, <i>scope</i>, <i>attrib-type</i>, <i>proxy-type</i>, <i>attrib-names</i>, <i>acl</i></dd>
<dt><i>name</i></dt>
<dd>is the hierarchical name as in the draft standard, typically of the form /vendor/acme/blurdybloop</dd>
<dt><i>scope</i></dt>
<dd>specifies whether the annotation is for the <code>server</code> or a <code>mailbox</code></dd>
<dt><i>attrib-type</i></dt>
<dd>specifies the attribute data type which is one of: <code>string</code>, <code>boolean</code>, <code>int</code>, <code>uint</code>, or <code>content-type</code></dd>
<dt><i>proxy-type</i></dt>
<dd>specifies whether this attribute is for the <code>backend</code> or <code>proxy</code> servers or both (<code>proxy_and_backend</code>)</dd>
<dt><i>attrib-names</i></dt>
<dd>is the space-separated list of available attributes for the annotation. Possible attribute names are (where the suffixless <code>foo</code> permits both <code>foo.priv</code> and <code>foo.shared</code>): <code>alue</code>, <code>value.shared</code>, <code>value.priv</code>, <code>size</code>, <code>size.shared</code>, <code>size.priv</code>, <code>modifiedsince</code>, <code>modifiedsince.shared</code>, <code>modifiedsince.priv</code>, <code>content-type</code>, <code>content-type.shared</code>, <code>content-type.priv</code></dd>
<dt><i>acl</i></dt>
<dd>is the extra ACL requirements for setting annotations. This is the standard IMAP ACL permission bit string format. Particularly useful is the <code>a</code> right to require admin privileges. Note that some ACL requirements (read and write on the mailbox) are hard-wired in the server</dd></dl>
<p> Blank lines and lines beginning with &#8220;#&#8221; are ignored. </p>
<dl>
<dt><code>auditlog:</code> 0</dt>
<dd>Should cyrus output log entries for every action taken on a message file or mailboxes list entry? It&#8217;s noisy so disabled by default, but can be very useful for tracking down what happened if things look strange</dd>
<dt><code>auth_mech:</code> unix</dt>
<dd>The authorization mechanism to use. </dd>
<p> Allowed values: <i>unix</i>, <i>pts</i>, <i>krb</i>, <i>krb5</i></p>
<dt><code>autocreatequota:</code> 0</dt>
<dd>If nonzero, normal users may create their own IMAP accounts by creating the mailbox INBOX. The user&#8217;s quota is set to the value if it is positive, otherwise the user has unlimited quota.</dd>
<dt><code>berkeley_cachesize:</code> 512</dt>
<dd>Size (in kilobytes) of the shared memory buffer pool (cache) used by the berkeley environment. The minimum allowed value is 20. The maximum allowed value is 4194303 (4GB).</dd>
<dt><code>berkeley_locks_max:</code> 50000</dt>
<dd>Maximum number of locks to be held or requested in the berkeley environment.</dd>
<dt><code>berkeley_txns_max:</code> 100</dt>
<dd>Maximum number of transactions to be supported in the berkeley environment.</dd>
<dt><code>boundary_limit:</code> 1000</dt>
<dd>messages are parsed recursively and a deep enough MIME structure can cause a stack overflow. Do not parse deeper than this many layers of MIME structure. The default of 1000 is much higher than any sane message should have.</dd>
<dt><code>client_timeout:</code> 10</dt>
<dd>Number of seconds to wait before returning a timeout failure when performing a client connection (e.g., in a murder environment)</dd>
<dt><code>commandmintimer:</code> &lt;none&gt;</dt>
<dd>Time in seconds. Any imap command that takes longer than this time is logged.</dd>
<dt><code>configdirectory:</code> &lt;none&gt;</dt>
<dd>The pathname of the IMAP configuration directory. This field is required.</dd>
<dt><code>debug_command:</code> &lt;none&gt;</dt>
<dd>Debug command to be used by processes started with -D option. The string is a C format string that gets 3 options: the first is the name of the executable (without path). The second is the pid (integer) and the third is the service ID. Example: /usr/local/bin/gdb /usr/cyrus/bin/%s %d</dd>
<dt><code>defaultacl:</code> anyone lrs</dt>
<dd>The Access Control List (ACL) placed on a newly-created (non-user) mailbox that does not have a parent mailbox.</dd>
<dt><code>defaultdomain:</code> &lt;none&gt;</dt>
<dd>The default domain for virtual domain support</dd>
<dt><code>defaultpartition:</code> &lt;none&gt;</dt>
<dd>The partition name used by default for new mailboxes. If not specified, the partition with the most free space will be used for new mailboxes.</dd>
<dt><code>defaultserver:</code> &lt;none&gt;</dt>
<dd>The backend server name used by default for new mailboxes. If not specified, the server with the most free space will be used for new mailboxes.</dd>
<dt><code>deletedprefix:</code> DELETED</dt>
<dd>If &quot;delete_mode&quot; set to be &quot;delayed&quot;, the prefix for the deleted mailboxes hierarchy. The hierarchy delimiter will be automatically appended.</dd>
<dt><code>delete_mode:</code> immediate</dt>
<dd>The manner in which mailboxes are deleted. &quot;immediate&quot; mode is the default behavior in which mailboxes are removed immediately. In &quot;delayed&quot; mode, mailboxes are renamed to a special hiearchy defined by the &quot;deletedprefix&quot; option to be removed later by cyr_expire. </dd>
<p> Allowed values: <i>immediate</i>, <i>delayed</i></p>
<dt><code>deleteright:</code> c</dt>
<dd>Deprecated &#8211; only used for backwards compatibility with existing installations. Lists the old RFC 2086 right which was used to grant the user the ability to delete a mailbox. If a user has this right, they will automatically be given the new &#8216;x&#8217; right.</dd>
<dt><code>disable_user_namespace:</code> 0</dt>
<dd>Preclude list command on user namespace. If set to &#8216;yes&#8217;, the LIST response will never include any other user&#8217;s mailbox. Admin users will always see all mailboxes. The default is &#8216;no&#8217;</dd>
<dt><code>disable_shared_namespace:</code> 0</dt>
<dd>Preclude list command on user namespace. If set to &#8216;yes&#8217;, the LIST response will never include any non-user mailboxes. Admin users will always see all mailboxes. The default is &#8216;no&#8217;</dd>
<dt><code>disconnect_on_vanished_mailbox:</code> 0</dt>
<dd>If enabled, IMAP/POP3/NNTP clients will be disconnected by the server if the currently selected mailbox is (re)moved by another session. Otherwise, the missing mailbox is treated as empty while in use by the client.</dd>
<dt><code>duplicate_db:</code> skiplist</dt>
<dd>The cyrusdb backend to use for the duplicate delivery suppression and sieve. </dd>
<p> Allowed values: <i>berkeley</i>, <i>berkeley-nosync</i>, <i>berkeley-hash</i>, <i>berkeley-hash-nosync</i>, <i>skiplist</i>, <i>sql</i></p>
<dt><code>duplicate_db_path:</code> &lt;none&gt;</dt>
<dd>The absolute path to the duplicate db file. If not specified, will be confdir/deliver.db</dd>
<dt><code>duplicatesuppression:</code> 1</dt>
<dd>If enabled, lmtpd will suppress delivery of a message to a mailbox if a message with the same message-id (or resent-message-id) is recorded as having already been delivered to the mailbox. Records the mailbox and message-id/resent-message-id of all successful deliveries.</dd>
<dt><code>expunge_mode:</code> default</dt>
<dd>The mode in which messages (and their corresponding cache entries) are expunged. &quot;default&quot; mode is the default behavior in which the message files are purged at the time of the EXPUNGE, but index and cache records are retained to facilitate QRESYNC. In &quot;delayed&quot; mode, the message files are also retained, allowing unexpunge to rescue them. In &quot;immediate&quot; mode, both the message files and the index records are removed as soon as possible. In all cases, nothing will be finally purged until all other processes have closed the mailbox to ensure they never see data disappear under them. In &quot;default&quot; or &quot;delayed&quot; mode, a later run of &quot;cyr_expire&quot; will clean out the retained records (and possibly message files). This reduces the amount of I/O that takes place at the time of EXPUNGE and should result in greater responsiveness for the client, especially when expunging a large number of messages. </dd>
<p> Allowed values: <i>default</i>, <i>immediate</i>, <i>delayed</i></p>
<dt><code>expunge_days:</code> 7</dt>
<dd>Number of days to retain expunged messages before cleaning up their index records. The default is 7. This is necessary for QRESYNC to work correctly. If combined with delayed expunge (above) you will also be able to unexpunge messages during this time.</dd>
<dt><code>failedloginpause:</code> 3</dt>
<dd>Number of seconds to pause after a failed login.</dd>
<dt><code>flushseenstate:</code> 0</dt>
<dd>If enabled, changes to the seen state will be flushed to disk immediately, otherwise changes will be cached and flushed when the mailbox is closed. This option may be used to fix the problem of previously read messages being marked as unread in Microsoft Outlook, at the expense of a loss of performance/scalability.</dd>
<dt><code>foolstupidclients:</code> 0</dt>
<dd>If enabled, only list the personal namespace when a LIST &quot;*&quot; is performed (it changes the request to a LIST &quot;INBOX*&quot;).</dd>
<dt><code>force_sasl_client_mech:</code> &lt;none&gt;</dt>
<dd>Force preference of a given SASL mechanism for client side operations (e.g., murder environments). This is separate from (and overridden by) the ability to use the &lt;host shortname&gt;_mechs option to set preferred mechanisms for a specific host</dd>
<dt><code>fulldirhash:</code> 0</dt>
<dd>If enabled, uses an improved directory hashing scheme which hashes on the entire username instead of using just the first letter as the hash. This changes hash algorithm used for quota and user directories and if <i>hashimapspool</i> is enabled, the entire mail spool.</dd></dl>
<p> Note that this option CANNOT be changed on a live system. The server must be quiesced and then the directories moved with the <code>rehash</code> utility.</p>
<dl>
<dt><code>hashimapspool:</code> 0</dt>
<dd>If enabled, the partitions will also be hashed, in addition to the hashing done on configuration directories. This is recommended if one partition has a very bushy mailbox tree.</dd>
<dt><code>debug:</code> 0</dt>
<dd>If enabled, allow syslog() to pass LOG_DEBUG messages.</dd>
<dt><code>hostname_mechs:</code> &lt;none&gt;</dt>
<dd>Force a particular list of SASL mechanisms to be used when authenticating to the backend server hostname (where hostname is the short hostname of the server in question). If it is not specified it will query the server for available mechanisms and pick one to use. &#8211; Cyrus Murder</dd>
<dt><code>hostname_password:</code> &lt;none&gt;</dt>
<dd>The password to use for authentication to the backend server hostname (where hostname is the short hostname of the server) &#8211; Cyrus Murder</dd>
<dt><code>idlesocket:</code> {configdirectory}/socket/idle</dt>
<dd>Unix domain socket that idled listens on.</dd>
<dt><code>ignorereference:</code> 0</dt>
<dd>For backwards compatibility with Cyrus 1.5.10 and earlier &#8212; ignore the reference argument in LIST or LSUB commands.</dd>
<dt><code>imapidlepoll:</code> 60</dt>
<dd>The interval (in seconds) for polling for mailbox changes and ALERTs while running the IDLE command. This option is used when idled is not enabled or cannot be contacted. The minimum value is 1. A value of 0 will disable IDLE.</dd>
<dt><code>imapidresponse:</code> 1</dt>
<dd>If enabled, the server responds to an ID command with a parameter list containing: version, vendor, support-url, os, os-version, command, arguments, environment. Otherwise the server returns NIL.</dd>
<dt><code>imapmagicplus:</code> 0</dt>
<dd>Only list a restricted set of mailboxes via IMAP by using userid+namespace syntax as the authentication/authorization id. Using userid+ (with an empty namespace) will list only subscribed mailboxes.</dd>
<dt><code>implicit_owner_rights:</code> lkxa</dt>
<dd>The implicit Access Control List (ACL) for the owner of a mailbox.</dd>
<dt><code>@include:</code> &lt;none&gt;</dt>
<dd>Directive which includes the specified file as part of the configuration. If the path to the file is not absolute, CYRUS_PATH is prepended.</dd>
<dt><code>improved_mboxlist_sort:</code> 0</dt>
<dd>If enabled, a special comparator will be used which will correctly sort mailbox names that contain characters such as &#8216; &#8216; and &#8216;-&#8216;.</dd></dl>
<p> Note that this option SHOULD NOT be changed on a live system. The mailboxes database should be dumped (ctl_mboxlist) before the option is changed, removed, and then undumped after changing the option. When not using flat files for the subscriptions databases the same has to be done (cyr_dbtool) for each subscription database See improved_mboxlist_sort.html.</p>
<dl>
<dt><code>internaldate_heuristic:</code> standard</dt>
<dd>Mechanism to determine email internaldates on delivery/reconstruct. &quot;standard&quot; uses time() when delivering a message, mtime on reconstruct. &quot;receivedheader&quot; looks at the top most Received header or time/mtime otherwise </dd>
<p> Allowed values: <i>standard</i>, <i>receivedheader</i></p>
<dt><code>ldap_authz:</code> &lt;none&gt;</dt>
<dd>SASL authorization ID for the LDAP server</dd>
<dt><code>ldap_base:</code> &lt;empty string&gt;</dt>
<dd>Contains the LDAP base dn for the LDAP ptloader module</dd>
<dt><code>ldap_bind_dn:</code> &lt;none&gt;</dt>
<dd>Bind DN for the connection to the LDAP server (simple bind). Do not use for anonymous simple binds</dd>
<dt><code>ldap_deref:</code> never</dt>
<dd>Specify how aliases dereferencing is handled during search. </dd>
<p> Allowed values: <i>search</i>, <i>find</i>, <i>always</i>, <i>never</i></p>
<dt><code>ldap_filter:</code> (uid=%u)</dt>
<dd>Specify a filter that searches user identifiers. The following tokens can be used in the filter string: </dd>
<p> %% = % %u = user %U = user portion of %u (%U = test when %u = test [at] domain.tld) %d = domain portion of %u if available (%d = domain.tld when %u = %test [at] domain.tld), otherwise same as %r %D = user dn. (use when ldap_member_method: filter) %1-9 = domain tokens (%1 = tld, %2 = domain when %d = domain.tld) </p>
<p> ldap_filter is not used when ldap_sasl is enabled.</p>
<dt><code>ldap_group_base:</code> &lt;empty string&gt;</dt>
<dd>LDAP base dn for ldap_group_filter.</dd>
<dt><code>ldap_group_filter:</code> (cn=%u)</dt>
<dd>Specify a filter that searches for group identifiers. See ldap_filter for more options.</dd>
<dt><code>ldap_group_scope:</code> sub</dt>
<dd>Specify search scope for ldap_group_filter. </dd>
<p> Allowed values: <i>sub</i>, <i>one</i>, <i>base</i></p>
<dt><code>ldap_id:</code> &lt;none&gt;</dt>
<dd>SASL authentication ID for the LDAP server</dd>
<dt><code>ldap_mech:</code> &lt;none&gt;</dt>
<dd>SASL mechanism for LDAP authentication</dd>
<dt><code>ldap_member_attribute:</code> &lt;none&gt;</dt>
<dd>See ldap_member_method.</dd>
<dt><code>ldap_member_base:</code> &lt;empty string&gt;</dt>
<dd>LDAP base dn for ldap_member_filter.</dd>
<dt><code>ldap_member_filter:</code> (member=%D)</dt>
<dd>Specify a filter for &quot;ldap_member_method: filter&quot;. See ldap_filter for more options.</dd>
<dt><code>ldap_member_method:</code> attribute</dt>
<dd>Specify a group method. The &quot;attribute&quot; method retrieves groups from a multi-valued attribute specified in ldap_member_attribute. </dd>
<p> The &quot;filter&quot; method uses a filter, specified by ldap_member_filter, to find groups; ldap_member_attribute is a single-value attribute group name. </p>
<p> Allowed values: <i>attribute</i>, <i>filter</i></p>
<dt><code>ldap_member_scope:</code> sub</dt>
<dd>Specify search scope for ldap_member_filter. </dd>
<p> Allowed values: <i>sub</i>, <i>one</i>, <i>base</i></p>
<dt><code>ldap_password:</code> &lt;none&gt;</dt>
<dd>Password for the connection to the LDAP server (SASL and simple bind). Do not use for anonymous simple binds</dd>
<dt><code>ldap_realm:</code> &lt;none&gt;</dt>
<dd>SASL realm for LDAP authentication</dd>
<dt><code>ldap_referrals:</code> 0</dt>
<dd>Specify whether or not the client should follow referrals.</dd>
<dt><code>ldap_restart:</code> 1</dt>
<dd>Specify whether or not LDAP I/O operations are automatically restarted if they abort prematurely.</dd>
<dt><code>ldap_sasl:</code> 1</dt>
<dd>Use SASL for LDAP binds in the LDAP PTS module.</dd>
<dt><code>ldap_sasl_authc:</code> &lt;none&gt;</dt>
<dd>Deprecated. Use ldap_id</dd>
<dt><code>ldap_sasl_authz:</code> &lt;none&gt;</dt>
<dd>Deprecated. Use ldap_authz</dd>
<dt><code>ldap_sasl_mech:</code> &lt;none&gt;</dt>
<dd>Deprecated. Use ldap_mech</dd>
<dt><code>ldap_sasl_password:</code> &lt;none&gt;</dt>
<dd>Deprecated. User ldap_password</dd>
<dt><code>ldap_sasl_realm:</code> &lt;none&gt;</dt>
<dd>Deprecated. Use ldap_realm</dd>
<dt><code>ldap_scope:</code> sub</dt>
<dd>Specify search scope. </dd>
<p> Allowed values: <i>sub</i>, <i>one</i>, <i>base</i></p>
<dt><code>ldap_servers:</code> <a href="ldap://localhost/">ldap://localhost/</a></dt>
<dd>Deprecated. Use ldap_uri</dd>
<dt><code>ldap_size_limit:</code> 1</dt>
<dd>Specify a number of entries for a search request to return.</dd>
<dt><code>ldap_start_tls:</code> 0</dt>
<dd>Use StartTLS extended operation. Do not use ldaps: ldap_uri when this option is enabled.</dd>
<dt><code>ldap_time_limit:</code> 5</dt>
<dd>Specify a number of seconds for a search request to complete.</dd>
<dt><code>ldap_timeout:</code> 5</dt>
<dd>Specify a number of seconds a search can take before timing out.</dd>
<dt><code>ldap_tls_cacert_dir:</code> &lt;none&gt;</dt>
<dd>Path to directory with CA (Certificate Authority) certificates.</dd>
<dt><code>ldap_tls_cacert_file:</code> &lt;none&gt;</dt>
<dd>File containing CA (Certificate Authority) certificate(s).</dd>
<dt><code>ldap_tls_cert:</code> &lt;none&gt;</dt>
<dd>File containing the client certificate.</dd>
<dt><code>ldap_tls_check_peer:</code> 0</dt>
<dd>Require and verify server certificate. If this option is yes, you must specify ldap_tls_cacert_file or ldap_tls_cacert_dir.</dd>
<dt><code>ldap_tls_ciphers:</code> &lt;none&gt;</dt>
<dd>List of SSL/TLS ciphers to allow. The format of the string is described in ciphers(1).</dd>
<dt><code>ldap_tls_key:</code> &lt;none&gt;</dt>
<dd>File containing the private client key.</dd>
<dt><code>ldap_uri:</code> &lt;none&gt;</dt>
<dd>Contains a list of the URLs of all the LDAP servers when using the LDAP PTS module.</dd>
<dt><code>ldap_version:</code> 3</dt>
<dd>Specify the LDAP protocol version. If ldap_start_tls and/or ldap_use_sasl are enabled, ldap_version will be automatically set to 3.</dd>
<dt><code>lmtp_downcase_rcpt:</code> 0</dt>
<dd>If enabled, lmtpd will convert the recipient addresses to lowercase (up to a &#8216;+&#8217; character, if present).</dd>
<dt><code>lmtp_fuzzy_mailbox_match:</code> 0</dt>
<dd>If enabled, and the mailbox specified in the detail part of the recipient (everything after the &#8216;+&#8217;) does not exist, lmtpd will try to find the closest match (ignoring case, ignoring whitespace, falling back to parent) to the specified mailbox name.</dd>
<dt><code>lmtp_over_quota_perm_failure:</code> 0</dt>
<dd>If enabled, lmtpd returns a permanent failure code when a user&#8217;s mailbox is over quota. By default, the failure is temporary, causing the MTA to queue the message and retry later.</dd>
<dt><code>lmtp_strict_quota:</code> 0</dt>
<dd>If enabled, lmtpd returns a failure code when the incoming message will cause the user&#8217;s mailbox to exceed its quota. By default, the failure won&#8217;t occur until the mailbox is already over quota.</dd>
<dt><code>lmtp_strict_rfc2821:</code> 1</dt>
<dd>By default, lmtpd will be strict (per RFC 2821) with regards to which envelope addresses are allowed. If this option is set to false, 8bit characters in the local-part of envelope addresses are changed to &#8216;X&#8217; instead. This is useful to avoid generating backscatter with certain MTAs like Postfix or Exim which accept such messages.</dd>
<dt><code>lmtpsocket:</code> {configdirectory}/socket/lmtp</dt>
<dd>Unix domain socket that lmtpd listens on, used by <a href="/docs/linux/man/8-deliver/">deliver</a>(8). This should match the path specified in <a href="/docs/linux/man/5-cyrus-conf/">cyrus.conf</a>(5).</dd>
<dt><code>lmtptxn_timeout:</code> 300</dt>
<dd>Timeout (in seconds) used during a lmtp transaction to a remote backend (e.g. in a murder environment). Can be used to prevent hung lmtpds on proxy hosts when a backend server becomes unresponsive during a lmtp transaction. The default is 300 &#8211; change to zero for infinite.</dd>
<dt><code>loginrealms:</code> &lt;empty string&gt;</dt>
<dd>The list of remote realms whose users may authenticate using cross-realm authentication identifiers. Separate each realm name by a space. (A cross-realm identity is considered any identity returned by SASL with an &quot;@&quot; in it.).</dd>
<dt><code>loginuseacl:</code> 0</dt>
<dd>If enabled, any authentication identity which has <code>a</code> rights on a user&#8217;s INBOX may log in as that user.</dd>
<dt><code>logtimestamps:</code> 0</dt>
<dd>Include notations in the protocol telemetry logs indicating the number of seconds since the last command or response.</dd>
<dt><code>mailbox_default_options:</code> 0</dt>
<dd>Default &quot;options&quot; field for the mailbox on create. You&#8217;ll want to know what you&#8217;re doing before setting this, but it can apply some default annotations like duplicate supression</dd>
<dt><code>mailnotifier:</code> &lt;none&gt;</dt>
<dd><a href="/docs/linux/man/8-notifyd/">Notifyd</a>(8) method to use for &quot;MAIL&quot; notifications. If not set, &quot;MAIL&quot; notifications are disabled.</dd>
<dt><code>maxheaderlines:</code> 1000</dt>
<dd>Maximum number of lines of header that will be processed into cache records. Default 1000. If set to zero, it is unlimited. If a message hits the limit, an error will be logged and the rest of the lines in the header will be skipped. This is to avoid malformed messages causing giant cache records</dd>
<dt><code>maxmessagesize:</code> 0</dt>
<dd>Maximum incoming LMTP message size. If non-zero, lmtpd will reject messages larger than <i>maxmessagesize</i> bytes. If set to 0, this will allow messages of any size (the default).</dd>
<dt><code>maxquoted:</code> 131072</dt>
<dd>Maximum size of a single quoted string for the parser. Default 128k</dd>
<dt><code>maxword:</code> 131072</dt>
<dd>Maximum size of a single word for the parser. Default 128k</dd>
<dt><code>mboxkey_db:</code> skiplist</dt>
<dd>The cyrusdb backend to use for mailbox keys. </dd>
<p> Allowed values: <i>berkeley</i>, <i>skiplist</i></p>
<dt><code>mboxlist_db:</code> skiplist</dt>
<dd>The cyrusdb backend to use for the mailbox list. </dd>
<p> Allowed values: <i>flat</i>, <i>berkeley</i>, <i>berkeley-hash</i>, <i>skiplist</i></p>
<dt><code>mboxlist_db_path:</code> &lt;none&gt;</dt>
<dd>The absolute path to the mailboxes db file. If not specified will be confdir/mailboxes.db</dd>
<dt><code>mboxname_lockpath:</code> &lt;none&gt;</dt>
<dd>Path to mailbox name lock files (default $conf/lock)</dd>
<dt><code>metapartition_files:</code> &lt;empty string&gt;</dt>
<dd>Space-separated list of metadata files to be stored on a <i>metapartition</i> rather than in the mailbox directory on a spool partition. </dd>
<p> Allowed values: <i>header</i>, <i>index</i>, <i>cache</i>, <i>expunge</i>, <i>squat</i></p>
<dt><code>metapartition-name:</code> &lt;none&gt;</dt>
<dd>The pathname of the metadata partition <i>name</i>, corresponding to spool partition <code>partition-name</code>. For any mailbox residing in a directory on <code>partition-name</code>, the metadata files listed in <i>metapartition_files</i> will be stored in a corresponding directory on <code>metapartition-name</code>. Note that not every <code>partition-name</code> option is required to have a corresponding <code>metapartition-name</code> option, so that you can selectively choose which spool partitions will have separate metadata partitions.</dd>
<dt><code>mupdate_authname:</code> &lt;none&gt;</dt>
<dd>The SASL username (Authentication Name) to use when authenticating to the mupdate server (if needed).</dd>
<dt><code>mupdate_config:</code> standard</dt>
<dd>The configuration of the mupdate servers in the Cyrus Murder. The &quot;standard&quot; config is one in which there are discreet frontend (proxy) and backend servers. The &quot;unified&quot; config is one in which a server can be both a frontend and backend. The &quot;replicated&quot; config is one in which multiple backend servers all share the same mailspool, but each have their own &quot;replicated&quot; copy of mailboxes.db. </dd>
<p> Allowed values: <i>standard</i>, <i>unified</i>, <i>replicated</i></p>
<dt><code>munge8bit:</code> 1</dt>
<dd>If enabled, lmtpd munges messages with 8-bit characters in the headers. The 8-bit characters are changed to `X&#8217;. If <code>reject8bit</code> is enabled, setting <code>munge8bit</code> has no effect. (A proper solution to non-ASCII characters in headers is offered by RFC 2047 and its predecessors.)</dd>
<dt><code>mupdate_connections_max:</code> 128</dt>
<dd>The max number of connections that a mupdate process will allow, this is related to the number of file descriptors in the mupdate process. Beyond this number connections will be immediately issued a BYE response.</dd>
<dt><code>mupdate_password:</code> &lt;none&gt;</dt>
<dd>The SASL password (if needed) to use when authenticating to the mupdate server.</dd>
<dt><code>mupdate_port:</code> 3905</dt>
<dd>The port of the mupdate server for the Cyrus Murder</dd>
<dt><code>mupdate_realm:</code> &lt;none&gt;</dt>
<dd>The SASL realm (if needed) to use when authenticating to the mupdate server.</dd>
<dt><code>mupdate_retry_delay:</code> 20</dt>
<dd>The base time to wait between connection retries to the mupdate server.</dd>
<dt><code>mupdate_server:</code> &lt;none&gt;</dt>
<dd>The mupdate server for the Cyrus Murder</dd>
<dt><code>mupdate_username:</code> &lt;empty string&gt;</dt>
<dd>The SASL username (Authorization Name) to use when authenticating to the mupdate server</dd>
<dt><code>mupdate_workers_max:</code> 50</dt>
<dd>The maximum number of mupdate worker threads (overall)</dd>
<dt><code>mupdate_workers_maxspare:</code> 10</dt>
<dd>The maximum number of idle mupdate worker threads</dd>
<dt><code>mupdate_workers_minspare:</code> 2</dt>
<dd>The minimum number of idle mupdate worker threads</dd>
<dt><code>mupdate_workers_start:</code> 5</dt>
<dd>The number of mupdate worker threads to start</dd>
<dt><code>netscapeurl:</code> &lt;none&gt;</dt>
<dd>If enabled at compile time, this specifies a URL to reply when Netscape asks the server where the mail administration HTTP server is. Administrators should set this to a local resource.</dd>
<dt><code>newsaddheaders:</code> to</dt>
<dd>Space-separated list of headers to be added to incoming usenet articles. Added <i>To:</i> headers will contain email delivery addresses corresponding to each newsgroup in the <i>Newsgroups:</i> header. Added <i>Reply-To:</i> headers will contain email delivery addresses corresponding to each newsgroup in the <i>Followup-To:</i> or <i>Newsgroups:</i> header. If the specified header(s) already exist in an article, the email delivery addresses will be appended to the original header body(s). </dd>
<p> This option applies if and only if the <code>newspostuser</code> option is set. </p>
<p> Allowed values: <i>to</i>, <i>replyto</i></p>
<dt><code>newsgroups:</code> *</dt>
<dd>A wildmat pattern specifying which mailbox hierarchies should be treated as newsgroups. Only mailboxes matching the wildmat will accept and/or serve articles via NNTP. If not set, a default wildmat of &quot;*&quot; (ALL shared mailboxes) will be used. If the <i>newsprefix</i> option is also set, the default wildmat will be translated to &quot;&lt;newsprefix&gt;.*&quot;</dd>
<dt><code>newsmaster:</code> news</dt>
<dd>Userid that is used for checking access controls when executing Usenet control messages. For instance, to allow articles to be automatically deleted by cancel messages, give the &quot;news&quot; user the &#8216;d&#8217; right on the desired mailboxes. To allow newsgroups to be automatically created, deleted and renamed by the corresponding control messages, give the &quot;news&quot; user the &#8216;c&#8217; right on the desired mailbox hierarchies.</dd>
<dt><code>newspeer:</code> &lt;none&gt;</dt>
<dd>A list of whitespace-separated news server specifications to which articles should be fed. Each server specification is a string of the form [user[:pass]@]host[:port][/wildmat] where &#8216;host&#8217; is the fully qualified hostname of the server, &#8216;port&#8217; is the port on which the server is listening, &#8216;user&#8217; and &#8216;pass&#8217; are the authentication credentials and &#8216;wildmat&#8217; is a pattern that specifies which groups should be fed. If no &#8216;port&#8217; is specified, port 119 is used. If no &#8216;wildmat&#8217; is specified, all groups are fed. If &#8216;user&#8217; is specified (even if empty), then the NNTP POST command will be used to feed the article to the server, otherwise the IHAVE command will be used. </dd>
<p> A &#8216;@&#8217; may be used in place of &#8216;!&#8217; in the wildmat to prevent feeding articles cross-posted to the given group, otherwise cross-posted articles are fed if any part of the wildmat matches. For example, the string &quot;peer.example.com:*,!control.*,@local.*&quot; would feed all groups except control messages and local groups to peer.example.com. In the case of cross-posting to local groups, these articles would not be fed.</p>
<dt><code>newspostuser:</code> &lt;none&gt;</dt>
<dd>Userid used to deliver usenet articles to newsgroup folders (usually via lmtp2nntp). For example, if set to &quot;post&quot;, email sent to &quot;post+comp.mail.imap&quot; would be delivered to the &quot;comp.mail.imap&quot; folder. </dd>
<p> When set, the Cyrus NNTP server will add the header(s) specified in the <code>newsaddheaders</code> option to each incoming usenet article. The added header(s) will contain email delivery addresses corresponding to each relevent newsgroup. If not set, no headers are added to usenet articles.</p>
<dt><code>newsprefix:</code> &lt;none&gt;</dt>
<dd>Prefix to be prepended to newsgroup names to make the corresponding IMAP mailbox names.</dd>
<dt><code>newsrc_db_path:</code> &lt;none&gt;</dt>
<dd>The absolute path to the newsrc db file. If not specified, will be confdir/fetchnews.db</dd>
<dt><code>nntptimeout:</code> 3</dt>
<dd>Set the length of the NNTP server&#8217;s inactivity autologout timer, in minutes. The minimum value is 3, the default.</dd>
<dt><code>normalizeuid:</code> 0</dt>
<dd>Lowercase uid and strip leading and trailing blanks. It is recommended to set this to yes, especially if OpenLDAP is used as authentication source.</dd>
<dt><code>notifysocket:</code> {configdirectory}/socket/notify</dt>
<dd>Unix domain socket that the mail notification daemon listens on.</dd>
<dt><code>notify_external:</code> &lt;none&gt;</dt>
<dd>Path to the external program that <a href="/docs/linux/man/8-notifyd/">notifyd</a>(8) will call to send mail notifications.</dd></dl>
<p> The external program will be called with the following command line options:</p>
<dl>
<dt><code>-c</code><i> class</i></dt>
<dd>
</dd><dt><code>-p</code><i> priority</i></dt>
<dd>
</dd><dt><code>-u</code><i> user</i></dt>
<dd>
</dd><dt><code>-m</code><i> mailbox</i></dt>
<dd></dd></dl>
<p> And the notification message will be available on <i>stdin</i>. </p>
<dl>
<dt><code>partition-name:</code> &lt;none&gt;</dt>
<dd>The pathname of the partition <i>name</i>. At least one partition pathname MUST be specified. If the <code>defaultpartition</code> option is used, then its pathname MUST be specified. For example, if the value of the <code>defaultpartion</code> option is <code>default</code>, then the <code>partition-default</code> field is required.</dd>
<dt><code>plaintextloginpause:</code> 0</dt>
<dd>Number of seconds to pause after a successful plaintext login. For systems that support strong authentication, this permits users to perceive a cost of using plaintext passwords. (This does not affect the use of PLAIN in SASL authentications.)</dd>
<dt><code>plaintextloginalert:</code> &lt;none&gt;</dt>
<dd>Message to send to client after a successful plaintext login.</dd>
<dt><code>popexpiretime:</code> -1</dt>
<dd>The number of days advertised as being the minimum a message may be left on the POP server before it is deleted (via the CAPA command, defined in the POP3 Extension Mechanism, which some clients may support). &quot;NEVER&quot;, the default, may be specified with a negative number. The Cyrus POP3 server never deletes mail, no matter what the value of this parameter is. However, if a site implements a less liberal policy, it needs to change this parameter accordingly.</dd>
<dt><code>popminpoll:</code> 0</dt>
<dd>Set the minimum amount of time the server forces users to wait between successive POP logins, in minutes.</dd>
<dt><code>popsubfolders:</code> 0</dt>
<dd>Allow access to subfolders of INBOX via POP3 by using userid+subfolder syntax as the authentication/authorization id.</dd>
<dt><code>poppollpadding:</code> 1</dt>
<dd>Create a softer minimum poll restriction. Allows <i>poppollpadding</i> connections before the minpoll restriction is triggered. Additionally, one padding entry is recovered every <i>popminpoll</i> minutes. This allows for the occasional polling rate faster than popminpoll, (i.e., for clients that require a send/receive to send mail) but still enforces the rate long-term. Default is 1 (disabled). </dd>
<p> The easiest way to think of it is a queue of past connections, with one slot being filled for every connection, and one slot being cleared every <i>popminpoll</i> minutes. When the queue is full, the user will not be able to check mail again until a slot is cleared. If the user waits a sufficient amount of time, they will get back many or all of the slots.</p>
<dt><code>poptimeout:</code> 10</dt>
<dd>Set the length of the POP server&#8217;s inactivity autologout timer, in minutes. The minimum value is 10, the default.</dd>
<dt><code>popuseacl:</code> 0</dt>
<dd>Enforce IMAP ACLs in the pop server. Due to the nature of the POP3 protocol, the only rights which are used by the pop server are &#8216;r&#8217;, user to open the mailbox and list/retrieve messages. The &#8216;t&#8217; right allows the user to delete messages. The &#8216;s&#8217; right allows messages retrieved by the user to have the \Seen flag set (only if <i>popuseimapflags</i> is also enabled).</dd>
<dt><code>popuseimapflags:</code> 0</dt>
<dd>If enabled, the pop server will set and obey IMAP flags. Messages having the \Deleted flag are ignored as if they do not exist. Messages that are retrieved by the client will have the \Seen flag set. All messages will have the \Recent flag unset.</dd>
<dt><code>postmaster:</code> postmaster</dt>
<dd>Username that is used as the &#8216;From&#8217; address in rejection MDNs produced by sieve.</dd>
<dt><code>postuser:</code> &lt;empty string&gt;</dt>
<dd>Userid used to deliver messages to shared folders. For example, if set to &quot;bb&quot;, email sent to &quot;bb+shared.blah&quot; would be delivered to the &quot;shared.blah&quot; folder. By default, an email address of &quot;+shared.blah&quot; would be used.</dd>
<dt><code>proc_path:</code> &lt;none&gt;</dt>
<dd>Path to proc directory. Default is NULL &#8211; must be an absolute path if specified. If not specified, the path $confdir/proc/ will be used.</dd>
<dt><code>proxy_authname:</code> proxy</dt>
<dd>The authentication name to use when authenticating to a backend server in the Cyrus Murder.</dd>
<dt><code>proxy_compress:</code> 0</dt>
<dd>Try to enable protocol-specific compression when performing a client connection to a backend server in the Cyrus Murder.</dd></dl>
<p> Note that this should only be necessary over slow network connections. Also note that currently only IMAP and MUPDATE support compression.</p>
<dl>
<dt><code>proxy_password:</code> &lt;none&gt;</dt>
<dd>The default password to use when authenticating to a backend server in the Cyrus Murder. May be overridden on a host-specific basis using the hostname_password option.</dd>
<dt><code>proxy_realm:</code> &lt;none&gt;</dt>
<dd>The authentication realm to use when authenticating to a backend server in the Cyrus Murder</dd>
<dt><code>proxyd_allow_status_referral:</code> 0</dt>
<dd>Set to true to allow proxyd to issue referrals to clients that support it when answering the STATUS command. This is disabled by default since some clients issue many STATUS commands in a row, and do not cache the connections that these referrals would cause, thus resulting in a higher authentication load on the respective backend server.</dd>
<dt><code>proxyd_disable_mailbox_referrals:</code> 0</dt>
<dd>Set to true to disable the use of mailbox-referrals on the proxy servers.</dd>
<dt><code>proxyservers:</code> &lt;none&gt;</dt>
<dd>A list of users and groups that are allowed to proxy for other users, separated by spaces. Any user listed in this will be allowed to login for any other user: use with caution. In a standard murder this option should ONLY be set on backends. DO NOT SET on frontends or things won&#8217;t work properly.</dd>
<dt><code>pts_module:</code> afskrb</dt>
<dd>The PTS module to use. </dd>
<p> Allowed values: <i>afskrb</i>, <i>ldap</i></p>
<dt><code>ptloader_sock:</code> &lt;none&gt;</dt>
<dd>Unix domain socket that ptloader listens on. (defaults to configdir/ptclient/ptsock)</dd>
<dt><code>ptscache_db:</code> skiplist</dt>
<dd>The cyrusdb backend to use for the pts cache. </dd>
<p> Allowed values: <i>berkeley</i>, <i>berkeley-hash</i>, <i>skiplist</i></p>
<dt><code>ptscache_db_path:</code> &lt;none&gt;</dt>
<dd>The absolute path to the ptscache db file. If not specified, will be confdir/ptscache.db</dd>
<dt><code>ptscache_timeout:</code> 10800</dt>
<dd>The timeout (in seconds) for the PTS cache database when using the auth_krb_pts authorization method (default: 3 hours).</dd>
<dt><code>ptskrb5_convert524:</code> 1</dt>
<dd>When using the AFSKRB ptloader module with Kerberos 5 canonicalization, do the final 524 conversion to get a n AFS style name (using &#8216;.&#8217; instead of &#8216;/&#8217;, and using short names</dd>
<dt><code>ptskrb5_strip_default_realm:</code> 1</dt>
<dd>When using the AFSKRB ptloader module with Kerberos 5 canonicalization, strip the default realm from the userid (this does not affect the stripping of realms specified by the afspts_localrealms option)</dd>
<dt><code>qosmarking:</code> cs0</dt>
<dd>This specifies the Class Selector or Differentiated Services Code Point designation on IP headers (in the ToS field). </dd>
<p> Allowed values: <i>cs0</i>, <i>cs1</i>, <i>cs2</i>, <i>cs3</i>, <i>cs4</i>, <i>cs5</i>, <i>cs6</i>, <i>cs7</i>, <i>af11</i>, <i>af12</i>, <i>af13</i>, <i>af21</i>, <i>af22</i>, <i>af23</i>, <i>af31</i>, <i>af32</i>, <i>af33</i>, <i>af41</i>, <i>af42</i>, <i>af43</i>, <i>ef</i></p>
<dt><code>quota_db:</code> quotalegacy</dt>
<dd>The cyrusdb backend to use for quotas. </dd>
<p> Allowed values: <i>flat</i>, <i>berkeley</i>, <i>berkeley-hash</i>, <i>skiplist</i>, <i>sql</i>, <i>quotalegacy</i></p>
<dt><code>quota_db_path:</code> &lt;none&gt;</dt>
<dd>The absolute path for the quota database (if you choose a single-file quota DB type &#8211; or the base path if you choose quotalegacy). If not specified will be confdir/quota.db or confdir/quota/</dd>
<dt><code>quotawarn:</code> 90</dt>
<dd>The percent of quota utilization over which the server generates warnings.</dd>
<dt><code>quotawarnkb:</code> 0</dt>
<dd>The maximum amount of free space (in kB) at which to give a quota warning (if this value is 0, or if the quota is smaller than this amount, than warnings are always given).</dd>
<dt><code>reject8bit:</code> 0</dt>
<dd>If enabled, lmtpd rejects messages with 8-bit characters in the headers.</dd>
<dt><code>rfc2046_strict:</code> 0</dt>
<dd>If enabled, imapd will be strict (per RFC 2046) when matching MIME boundary strings. This means that boundaries containing other boundaries as substrings will be treated as identical. Since enabling this option will break some messages created by Eudora 5.1 (and earlier), it is recommended that it be left disabled unless there is good reason to do otherwise.</dd>
<dt><code>rfc3028_strict:</code> 1</dt>
<dd>If enabled, Sieve will be strict (per RFC 3028) with regards to which headers are allowed to be used in address and envelope tests. This means that only those headers which are defined to contain addresses will be allowed in address tests and only &quot;to&quot; and &quot;from&quot; will be allowed in envelope tests. When disabled, ANY grammatically correct header will be allowed.</dd>
<dt><code>sasl_auto_transition:</code> 0</dt>
<dd>If enabled, the SASL library will automatically create authentication secrets when given a plaintext password. See the SASL documentation.</dd>
<dt><code>sasl_maximum_layer:</code> 256</dt>
<dd>Maximum SSF (security strength factor) that the server will allow a client to negotiate.</dd>
<dt><code>sasl_minimum_layer:</code> 0</dt>
<dd>The minimum SSF that the server will allow a client to negotiate. A value of 1 requires integrity protection; any higher value requires some amount of encryption.</dd>
<dt><code>sasl_option:</code> 0</dt>
<dd>Any SASL option can be set by preceding it with &quot;sasl_&quot;. This file overrides the SASL configuration file.</dd>
<dt><code>sasl_pwcheck_method:</code> &lt;none&gt;</dt>
<dd>The mechanism used by the server to verify plaintext passwords. Possible values include &quot;auxprop&quot;, &quot;saslauthd&quot;, and &quot;pwcheck&quot;.</dd>
<dt><code>seenstate_db:</code> skiplist</dt>
<dd>The cyrusdb backend to use for the seen state. </dd>
<p> Allowed values: <i>flat</i>, <i>berkeley</i>, <i>berkeley-hash</i>, <i>skiplist</i></p>
<dt><code>sendmail:</code> /usr/lib/sendmail</dt>
<dd>The pathname of the sendmail executable. Sieve invokes sendmail for sending rejections, redirects and vacation responses.</dd>
<dt><code>serverlist:</code> &lt;none&gt;</dt>
<dd>Whitespace separated list of backend server names. Used for finding server with the most available free space for proxying CREATE.</dd>
<dt><code>servername:</code> &lt;none&gt;</dt>
<dd>This is the hostname visible in the greeting messages of the POP, IMAP and LMTP daemons. If it is unset, then the result returned from <a href="/docs/linux/man/2-gethostname/">gethostname</a>(2) is used.</dd>
<dt><code>serverinfo:</code> on</dt>
<dd>The server information to display in the greeting and capability responses. Information is displayed as follows:</dd>
<dd>&quot;off&quot; = no server information in the greeting or capabilities<br />
 &quot;min&quot; = <i>servername</i> in the greeting; no server information in the capabilities<br />
 &quot;on&quot; = <i>servername</i> and product version in the greeting; product version in the capabilities </dd>
<p> Allowed values: <i>off</i>, <i>min</i>, <i>on</i></p>
<dt><code>sharedprefix:</code> Shared Folders</dt>
<dd>If using the alternate IMAP namespace, the prefix for the shared namespace. The hierarchy delimiter will be automatically appended.</dd>
<dt><code>sieve_allowreferrals:</code> 1</dt>
<dd>If enabled, timsieved will issue referrals to clients when the user&#8217;s scripts reside on a remote server (in a Murder). Otherwise, timsieved will proxy traffic to the remote server.</dd>
<dt><code>sieve_extensions:</code> fileinto reject vacation imapflags notify envelope relational regex subaddress copy</dt>
<dd>Space-separated list of Sieve extensions allowed to be used in sieve scripts, enforced at submission by <a href="/docs/linux/man/8-timsieved/">timsieved</a>(8). Any previously installed script will be unaffected by this option and will continue to execute regardless of the extensions used. This option has no effect on options that are disabled at compile time (e.g., &quot;regex&quot;). </dd>
<p> Allowed values: <i>fileinto</i>, <i>reject</i>, <i>vacation</i>, <i>imapflags</i>, <i>notify</i>, <i>include</i>, <i>envelope</i>, <i>body</i>, <i>relational</i>, <i>regex</i>, <i>subaddress</i>, <i>copy</i></p>
<dt><code>sieve_maxscriptsize:</code> 32</dt>
<dd>Maximum size (in kilobytes) any sieve script can be, enforced at submission by <a href="/docs/linux/man/8-timsieved/">timsieved</a>(8).</dd>
<dt><code>sieve_maxscripts:</code> 5</dt>
<dd>Maximum number of sieve scripts any user may have, enforced at submission by <a href="/docs/linux/man/8-timsieved/">timsieved</a>(8).</dd>
<dt><code>sieve_utf8fileinto:</code> 0</dt>
<dd>If enabled, the sieve engine expects folder names for the <i>fileinto</i> action in scripts to use UTF8 encoding. Otherwise, modified UTF7 encoding should be used.</dd>
<dt><code>sieve_sasl_send_unsolicited_capability:</code> 0</dt>
<dd>If enabled, timsieved will emit a capability response after a successful SASL authentication, per draft-martin-managesieve-12.txt .</dd>
<dt><code>sievedir:</code> /usr/sieve</dt>
<dd>If sieveusehomedir is false, this directory is searched for Sieve scripts.</dd>
<dt><code>sievenotifier:</code> &lt;none&gt;</dt>
<dd><a href="/docs/linux/man/8-notifyd/">Notifyd</a>(8) method to use for &quot;SIEVE&quot; notifications. If not set, &quot;SIEVE&quot; notifications are disabled.</dd></dl>
<p> This method is only used when no method is specified in the script.</p>
<dl>
<dt><code>sieveusehomedir:</code> 0</dt>
<dd>If enabled, lmtpd will look for Sieve scripts in user&#8217;s home directories: ~user/.sieve.</dd>
<dt><code>singleinstancestore:</code> 1</dt>
<dd>If enabled, imapd, lmtpd and nntpd attempt to only write one copy of a message per partition and create hard links, resulting in a potentially large disk savings.</dd>
<dt><code>skiplist_always_checkpoint:</code> 1</dt>
<dd>If enabled, this option forces the skiplist cyrusdb backend to always checkpoint when doing a recovery. This causes slightly more IO, but on the other hand leads to more efficient databases, and the entire file is already &quot;hot&quot;.</dd>
<dt><code>skiplist_unsafe:</code> 0</dt>
<dd>If enabled, this option forces the skiplist cyrusdb backend to not sync writes to the disk. Enabling this option is NOT RECOMMENDED.</dd>
<dt><code>soft_noauth:</code> 1</dt>
<dd>If enabled, lmtpd returns temporary failures if the client does not successfully authenticate. Otherwise lmtpd returns permanent failures (causing the mail to bounce immediately).</dd>
<dt><code>specialusealways:</code> 0</dt>
<dd>If enabled, this option causes LIST and LSUB output to always include the XLIST &quot;special-use&quot; flags. See &quot;xlist-*&#8217;&quot;</dd>
<dt><code>sql_database:</code> &lt;none&gt;</dt>
<dd>Name of the database which contains the cyrusdb table(s).</dd>
<dt><code>sql_engine:</code> &lt;none&gt;</dt>
<dd>Name of the SQL engine to use. </dd>
<p> Allowed values: <i>mysql</i>, <i>pgsql</i>, <i>sqlite</i></p>
<dt><code>sql_hostnames:</code> &lt;empty string&gt;</dt>
<dd>Comma separated list of SQL servers (in host[:port] format).</dd>
<dt><code>sql_passwd:</code> &lt;none&gt;</dt>
<dd>Password to use for authentication to the SQL server.</dd>
<dt><code>sql_user:</code> &lt;none&gt;</dt>
<dd>Username to use for authentication to the SQL server.</dd>
<dt><code>sql_usessl:</code> 0</dt>
<dd>If enabled, a secure connection will be made to the SQL server.</dd>
<dt><code>srvtab:</code> &lt;empty string&gt;</dt>
<dd>The pathname of <i>srvtab</i> file containing the server&#8217;s private key. This option is passed to the SASL library and overrides its default setting.</dd>
<dt><code>submitservers:</code> &lt;none&gt;</dt>
<dd>A list of users and groups that are allowed to resolve &quot;urlauth=submit+&quot; IMAP URLs, separated by spaces. Any user listed in this will be allowed to fetch the contents of any valid &quot;urlauth=submit+&quot; IMAP URL: use with caution.</dd>
<dt><code>subscription_db:</code> flat</dt>
<dd>The cyrusdb backend to use for the subscriptions list. </dd>
<p> Allowed values: <i>flat</i>, <i>berkeley</i>, <i>berkeley-hash</i>, <i>skiplist</i></p>
<dt><code>suppress_capabilities:</code> &lt;none&gt;</dt>
<dd>Suppress the named capabilities from any capability response. Use the exact case as it appears in the response, e.g. &quot;suppress_capabilities: ESEARCH QRESYNC WITHIN XLIST LIST-EXTENDED&quot; if you have a murder with 2.3.x backends and don&#8217;t want clients being confused by new capabilities that some backends don&#8217;t support.</dd>
<dt><code>statuscache:</code> 0</dt>
<dd>Enable/disable the imap status cache.</dd>
<dt><code>statuscache_db:</code> skiplist</dt>
<dd>The cyrusdb backend to use for the imap status cache. </dd>
<p> Allowed values: <i>berkeley</i>, <i>berkeley-nosync</i>, <i>berkeley-hash</i>, <i>berkeley-hash-nosync</i>, <i>skiplist</i></p>
<dt><code>statuscache_db_path:</code> &lt;none&gt;</dt>
<dd>The absolute path to the statuscache db file. If not specified, will be confdir/statuscache.db</dd>
<dt><code>sync_authname:</code> &lt;none&gt;</dt>
<dd>The authentication name to use when authenticating to a sync server. Prefix with a channel name to only apply for that channel</dd>
<dt><code>sync_compress:</code> 0</dt>
<dd>Enable compression on replication traffic. Prefix with a channel name to only apply for that channel</dd>
<dt><code>sync_host:</code> &lt;none&gt;</dt>
<dd>Name of the host (replica running <a href="/docs/linux/man/8-sync_server/">sync_server</a>(8)) to which replication actions will be sent by <a href="/docs/linux/man/8-sync_client/">sync_client</a>(8). Prefix with a channel name to only apply for that channel</dd>
<dt><code>sync_log:</code> 0</dt>
<dd>Enable replication action logging by <a href="/docs/linux/man/8-lmtpd/">lmtpd</a>(8), imapd(8), pop3d(8), and <a href="/docs/linux/man/8-nntpd/">nntpd</a>(8). The log {configdirectory}/sync/log is used by <a href="/docs/linux/man/8-sync_client/">sync_client</a>(8) for &quot;rolling&quot; replication.</dd>
<dt><code>sync_log_chain:</code> 0</dt>
<dd>Enable replication action logging by sync_server as well, allowing chaining of replicas. Use this on &#8216;B&#8217; for A =&gt; B =&gt; C replication layout</dd>
<dt><code>sync_log_channels:</code> &lt;none&gt;</dt>
<dd>If specified, log all events to multiple log files in directories specified by each &quot;channel&quot;. To run these log files, you need to pass the -n option to sync_client -r with the channel name. Use this for a mesh style replication layout &#8211; every machine replicating to every other machine.</dd>
<dt><code>sync_password:</code> &lt;none&gt;</dt>
<dd>The default password to use when authenticating to a sync server. Prefix with a channel name to only apply for that channel</dd>
<dt><code>sync_port:</code> csync</dt>
<dd>Name of the service (or port number) of the replication service on replica host. The default is &quot;csync&quot; which is usally port 2005, but any service name or numeric port can be specified. Prefix with a channel name to only apply for that channel</dd>
<dt><code>sync_realm:</code> &lt;none&gt;</dt>
<dd>The authentication realm to use when authenticating to a sync server. Prefix with a channel name to only apply for that channel</dd>
<dt><code>sync_repeat_interval:</code> 1</dt>
<dd>Minimum interval (in seconds) between replication runs in rolling replication mode. If a replication run takes longer than this time, we repeat immediately. Prefix with a channel name to only apply for that channel</dd>
<dt><code>sync_shutdown_file:</code> &lt;none&gt;</dt>
<dd>Simple latch used to tell <a href="/docs/linux/man/8-sync_client/">sync_client</a>(8) that it should shut down at the next opportunity. Safer than sending signals to running processes. Prefix with a channel name to only apply for that channel</dd>
<dt><code>syslog_prefix:</code> &lt;none&gt;</dt>
<dd>String to be prepended to the process name in syslog entries.</dd>
<dt><code>tcp_keepalive:</code> 0</dt>
<dd>Enable keepalive on TCP connections</dd>
<dt><code>tcp_keepalive_cnt:</code> 0</dt>
<dd>Number of TCP keepalive probes to send before declaring the connection dead (0 == system default)</dd>
<dt><code>tcp_keepalive_idle:</code> 0</dt>
<dd>Number of seconds a connection must be idle before keepalive probes are sent (0 == system default)</dd>
<dt><code>tcp_keepalive_intvl:</code> 0</dt>
<dd>Number of seconds between keepalive probes (0 == system default)</dd>
<dt><code>temp_path:</code> /tmp</dt>
<dd>The pathname to store temporary files in</dd>
<dt><code>timeout:</code> 30</dt>
<dd>The length of the IMAP server&#8217;s inactivity autologout timer, in minutes. The minimum value is 30, the default.</dd>
<dt><code>tls_ca_file:</code> &lt;none&gt;</dt>
<dd>File containing one or more Certificate Authority (CA) certificates.</dd>
<dt><code>tls_ca_path:</code> &lt;none&gt;</dt>
<dd>Path to directory with certificates of CAs. This directory must have filenames with the hashed value of the certificates (see openssl(XXX)).</dd>
<dt><code>tlscache_db:</code> skiplist</dt>
<dd>The cyrusdb backend to use for the TLS cache. </dd>
<p> Allowed values: <i>berkeley</i>, <i>berkeley-nosync</i>, <i>berkeley-hash</i>, <i>berkeley-hash-nosync</i>, <i>skiplist</i>, <i>sql</i></p>
<dt><code>tlscache_db_path:</code> &lt;none&gt;</dt>
<dd>The absolute path to the tlscache db file. If not specified, will be confdir/tls_sessions.db</dd>
<dt><code>tls_cert_file:</code> &lt;none&gt;</dt>
<dd>File containing the certificate presented for server authentication during STARTTLS. A value of &quot;disabled&quot; will disable SSL/TLS.</dd>
<dt><code>tls_cipher_list:</code> DEFAULT</dt>
<dd>The list of SSL/TLS ciphers to allow. The format of the string is described in ciphers(1).</dd>
<dt><code>tls_key_file:</code> &lt;none&gt;</dt>
<dd>File containing the private key belonging to the server certificate. A value of &quot;disabled&quot; will disable SSL/TLS.</dd>
<dt><code>tls_require_cert:</code> 0</dt>
<dd>Require a client certificate for ALL services (imap, pop3, lmtp, sieve).</dd>
<dt><code>tls_session_timeout:</code> 1440</dt>
<dd>The length of time (in minutes) that a TLS session will be cached for later reuse. The maximum value is 1440 (24 hours), the default. A value of 0 will disable session caching.</dd>
<dt><code>umask:</code> 077</dt>
<dd>The umask value used by various Cyrus IMAP programs.</dd>
<dt><code>userdeny_db:</code> flat</dt>
<dd>The cyrusdb backend to use for the user access list. </dd>
<p> Allowed values: <i>flat</i>, <i>berkeley</i>, <i>berkeley-hash</i>, <i>skiplist</i>, <i>sql</i></p>
<dt><code>userdeny_db_path:</code> &lt;none&gt;</dt>
<dd>The absolute path to the userdeny db file. If not specified, will be confdir/user_deny.db</dd>
<dt><code>user_folder_limit:</code> 0</dt>
<dd>Limit the number of folders a user can create in their INBOX. Set to 0 (default) for no limit. Only affects folders in user.</dd>
<dt><code>username_tolower:</code> 1</dt>
<dd>Convert usernames to all lowercase before login/authentication. This is useful with authentication backends which ignore case during username lookups (such as LDAP).</dd>
<dt><code>userprefix:</code> Other Users</dt>
<dd>If using the alternate IMAP namespace, the prefix for the other users namespace. The hierarchy delimiter will be automatically appended.</dd>
<dt><code>unix_group_enable:</code> 1</dt>
<dd>Should we look up groups when using auth_unix (disable this if you are not using groups in ACLs for your IMAP server, and you are using auth_unix with a backend (such as LDAP) that can make getgrent() calls very slow)</dd>
<dt><code>unixhierarchysep:</code> 0</dt>
<dd>Use the UNIX separator character &#8216;/&#8217; for delimiting levels of mailbox hierarchy. The default is to use the netnews separator character &#8216;.&#8217;.</dd>
<dt><code>virtdomains:</code> off</dt>
<dd>Enable virtual domain support. If enabled, the user&#8217;s domain will be determined by splitting a fully qualified userid at the last &#8216;@&#8217; or &#8216;%&#8217; symbol. If the userid is unqualified, and the virtdomains option is set to &quot;on&quot;, then the domain will be determined by doing a reverse lookup on the IP address of the incoming network interface, otherwise the user is assumed to be in the default domain (if set). </dd>
<p> Allowed values: <i>off</i>, <i>userid</i>, <i>on</i></p>
<dt><code>xlist-*:</code> &lt;none&gt;</dt>
<dd>Cyrus 2.4 ONLY &#8211; enable special use flags. The valid names can be taken from GMail&#8217;s XLIST documents or RFC 6154. Attribute name in the configuration key should be defined in lowercase. The attribute value is case sensitive, may contain whitespace and must be valid UTF7-IMAP string. It must exactly match the name of the subfolder of a user&#8217;s INBOX. </dd>
<p> Example: xlist-drafts: My Drafts </p>
<p> Every user on your server with a &#8216;INBOX.My Drafts&#8217; folder will get the special use flag &quot;Drafts&quot; added. Later versions of Cyrus have a much more flexible RFC 6154 compatible system.</p>
<dt><code>tls_prefer_server_ciphers:</code> 0</dt>
<dd>Prefer the ciphers on the server side instead of client side</dd>
<dt><code>tls_versions:</code> ssl2 ssl3 tls1_0 tls1_1 tls1_2</dt>
<dd>A list of SSL/TLS versions to not disable. Cyrus IMAP SSL/TLS starts with all protocols, and substracts protocols not in this list. Newer versions of SSL/TLS will need to be added here to allow them to get disabled. </dd>
</dl>
<h2>See Also</h2>
<p><code>imapd(8)</code>, <code>pop3d(8)</code>, <code><a href="/docs/linux/man/8-nntpd/">nntpd</a>(8)</code>, <code><a href="/docs/linux/man/8-lmtpd/">lmtpd</a>(8)</code>, <code><a href="/docs/linux/man/8-timsieved/">timsieved</a>(8)</code>, <code><a href="/docs/linux/man/8-idled/">idled</a>(8)</code>, <code><a href="/docs/linux/man/8-notifyd/">notifyd</a>(8)</code>, <code><a href="/docs/linux/man/8-deliver/">deliver</a>(8)</code>, <code><a href="/docs/linux/man/8-cyrus-master/">cyrus-master</a>(8)</code>, <code>ciphers(1)</code> </p>
