---
title: "kdb5_ldap_util(8)"
name: "kdb5_ldap_util"
section: "8"
letter: "k"
url: "/docs/linux/man/8-kdb5_ldap_util/"
description: "kdb5_ldap_util – Kerberos configuration utility"
---

<p>kdb5_ldap_util &#8211; Kerberos configuration utility</p>
<h2>Synopsis</h2>
<p><code>kdb5_ldap_util</code> [<code>-D</code> <i>user_dn</i> [<code>-w</code> <i>passwd</i>]] [<code>-H</code> <i>ldapuri</i>] <code>command</code> [<i>command_options</i>]</p>
<h2>Description</h2>
<p>kdb5_ldap_util allows an administrator to manage realms, Kerberos services and ticket policies.</p>
<h2>Command-Line Options</h2>
<dl>
<dt><code>-D</code> <i>user_dn</i></p>
<dd>Specifies the Distinguished Name (DN) of the user who has sufficient rights to perform the operation on the LDAP server.</p>
<dt><code>-w</code> <i>passwd</i></p>
<dd>Specifies the password of <i>user_dn</i>. This option is not recommended.</p>
<dt><code>-H</code> <i>ldapuri</i></p>
<dd>Specifies the URI of the LDAP server. It is recommended to use <code>ldapi://</code> or <code>ldaps://</code> to connect to the LDAP server.</dl>
<h2>Commands</h2>
<h3>create</h3>
<p><code>create</code> [<code>-subtrees</code> <i>subtree_dn_list</i>] [<code>-sscope</code> <i>search_scope</i>] [<code>-containerref</code> <i>container_reference_dn</i>] [<code>-k</code> <i>mkeytype</i>] [<code>-kv</code> <i>mkeyVNO</i>] [<code>-m|-P</code> <i>password</i>|<code>-sf</code> <i>stashfilename</i>] [<code>-s</code>] [<code>-r</code> <i>realm</i>] [<code>-maxtktlife</code> <i>max_ticket_life</i>] [<code>-maxrenewlife</code> <i>max_renewable_ticket_life</i>] [<i>ticket_flags</i>] </p>
<p> Creates realm in directory. Options:</p>
<dl>
<dt><code>-subtrees</code> <i>subtree_dn_list</i></p>
<dd>Specifies the list of subtrees containing the principals of a realm. The list contains the DNs of the subtree objects separated by colon (<code>:</code>).</p>
<dt><code>-sscope</code> <i>search_scope</i></p>
<dd>Specifies the scope for searching the principals under the subtree. The possible values are 1 or one (one level), 2 or sub (subtrees).</p>
<dt><code>-containerref</code> <i>container_reference_dn</i></p>
<dd>Specifies the DN of the container object in which the principals of a realm will be created. If the container reference is not configured for a realm, the principals will be created in the realm container.</p>
<dt><code>-k</code> <i>mkeytype</i></p>
<dd>Specifies the key type of the master key in the database. The default is given by the <code>master_key_type</code> variable in <i><a href="/docs/linux/man/5-kdc-conf/">kdc.conf</a>(5)</i>.</p>
<dt><code>-kv</code> <i>mkeyVNO</i></p>
<dd>Specifies the version number of the master key in the database; the default is 1. Note that 0 is not allowed.</p>
<dt><code>-m</code></p>
<dd>Specifies that the master database password should be read from the TTY rather than fetched from a file on the disk.</p>
<dt><code>-P</code> <i>password</i></p>
<dd>Specifies the master database password. This option is not recommended.</p>
<dt><code>-r</code> <i>realm</i></p>
<dd>Specifies the Kerberos realm of the database.</p>
<dt><code>-sf</code> <i>stashfilename</i></p>
<dd>Specifies the stash file of the master database password.</p>
<dt><code>-s</code></p>
<dd>Specifies that the stash file is to be created.</p>
<dt><code>-maxtktlife</code> <i>max_ticket_life</i></p>
<dd>(<i>getdate</i> string) Specifies maximum ticket life for principals in this realm.</p>
<dt><code>-maxrenewlife</code> <i>max_renewable_ticket_life</i></p>
<dd>(<i>getdate</i> string) Specifies maximum renewable life of tickets for principals in this realm.</p>
<dt><i>ticket_flags</i></p>
<dd>Specifies global ticket flags for the realm. Allowable flags are documented in the description of the <code>add_principal</code> command in <i><a href="/docs/linux/man/1-kadmin/">kadmin</a>(1)</i>. </p>
<p> Example: </p>
<pre>kdb5_ldap_util -D cn=admin,o=org -H <a href="ldaps://ldap-server1.mit.edu">ldaps://ldap-server1.mit.edu</a>
 create -subtrees o=org -sscope SUB -r ATHENA.MIT.EDU
Password for &quot;cn=admin,o=org&quot;:
Initializing database for realm 'ATHENA.MIT.EDU'
You will be prompted for the database Master Password.
It is important that you NOT FORGET this password.
Enter KDC database master key:
Re-enter KDC database master key to verify:</pre>
</dl>
<h3>modify</h3>
<p><code>modify</code> [<code>-subtrees</code> <i>subtree_dn_list</i>] [<code>-sscope</code> <i>search_scope</i>] [<code>-containerref</code> <i>container_reference_dn</i>] [<code>-r</code> <i>realm</i>] [<code>-maxtktlife</code> <i>max_ticket_life</i>] [<code>-maxrenewlife</code> <i>max_renewable_ticket_life</i>] [<i>ticket_flags</i>] </p>
<p> Modifies the attributes of a realm. Options:</p>
<dl>
<dt><code>-subtrees</code> <i>subtree_dn_list</i></p>
<dd>Specifies the list of subtrees containing the principals of a realm. The list contains the DNs of the subtree objects separated by colon (<code>:</code>). This list replaces the existing list.</p>
<dt><code>-sscope</code> <i>search_scope</i></p>
<dd>Specifies the scope for searching the principals under the subtrees. The possible values are 1 or one (one level), 2 or sub (subtrees).</p>
<dt><code>-containerref</code> <i>container_reference_dn</i> Specifies the DN of the</p>
<dd>container object in which the principals of a realm will be created.</p>
<dt><code>-r</code> <i>realm</i></p>
<dd>Specifies the Kerberos realm of the database.</p>
<dt><code>-maxtktlife</code> <i>max_ticket_life</i></p>
<dd>(<i>getdate</i> string) Specifies maximum ticket life for principals in this realm.</p>
<dt><code>-maxrenewlife</code> <i>max_renewable_ticket_life</i></p>
<dd>(<i>getdate</i> string) Specifies maximum renewable life of tickets for principals in this realm.</p>
<dt><i>ticket_flags</i></p>
<dd>Specifies global ticket flags for the realm. Allowable flags are documented in the description of the <code>add_principal</code> command in <i><a href="/docs/linux/man/1-kadmin/">kadmin</a>(1)</i>. </p>
<p> Example: </p>
<pre>shell% kdb5_ldap_util -D cn=admin,o=org -H
 <a href="ldaps://ldap-server1.mit.edu">ldaps://ldap-server1.mit.edu</a> modify +requires_preauth -r
 ATHENA.MIT.EDU
Password for &quot;cn=admin,o=org&quot;:
shell%</pre>
</dl>
<h3>view</h3>
<p><code>view</code> [<code>-r</code> <i>realm</i>] </p>
<p> Displays the attributes of a realm. Options:</p>
<dl>
<dt><code>-r</code> <i>realm</i></p>
<dd>Specifies the Kerberos realm of the database. </p>
<p> Example: </p>
<pre>kdb5_ldap_util -D cn=admin,o=org -H <a href="ldaps://ldap-server1.mit.edu">ldaps://ldap-server1.mit.edu</a>
 view -r ATHENA.MIT.EDU
Password for &quot;cn=admin,o=org&quot;:
Realm Name: ATHENA.MIT.EDU
Subtree: ou=users,o=org
Subtree: ou=servers,o=org
SearchScope: ONE
Maximum ticket life: 0 days 01:00:00
Maximum renewable life: 0 days 10:00:00
Ticket flags: DISALLOW_FORWARDABLE REQUIRES_PWCHANGE</pre>
</dl>
<h3>destroy</h3>
<p><code>destroy</code> [<code>-f</code>] [<code>-r</code> <i>realm</i>] </p>
<p> Destroys an existing realm. Options:</p>
<dl>
<dt><code>-f</code></p>
<dd>If specified, will not prompt the user for confirmation.</p>
<dt><code>-r</code> <i>realm</i></p>
<dd>Specifies the Kerberos realm of the database. </p>
<p> Example: </p>
<pre>shell% kdb5_ldap_util -D cn=admin,o=org -H
 <a href="ldaps://ldap-server1.mit.edu">ldaps://ldap-server1.mit.edu</a> destroy -r ATHENA.MIT.EDU
Password for &quot;cn=admin,o=org&quot;:
Deleting KDC database of 'ATHENA.MIT.EDU', are you sure?
(type 'yes' to confirm)? yes
OK, deleting database of 'ATHENA.MIT.EDU'...
shell%</pre>
</dl>
<h3>list</h3>
<p><code>list</code> </p>
<p> Lists the name of realms. </p>
<p> Example: </p>
<pre>shell% kdb5_ldap_util -D cn=admin,o=org -H
 <a href="ldaps://ldap-server1.mit.edu">ldaps://ldap-server1.mit.edu</a> list
Password for &quot;cn=admin,o=org&quot;:
ATHENA.MIT.EDU
OPENLDAP.MIT.EDU
MEDIA-LAB.MIT.EDU
shell%</pre>
<h3>stashsrvpw</h3>
<p><code>stashsrvpw</code> [<code>-f</code> <i>filename</i>] <i>name</i> </p>
<p> Allows an administrator to store the password for service object in a file so that KDC and Administration server can use it to authenticate to the LDAP server. Options:</p>
<dl>
<dt><code>-f</code> <i>filename</i></p>
<dd>Specifies the complete path of the service password file. By default, <code>/usr/local/var/service_passwd</code> is used.</p>
<dt><i>name</i></p>
<dd>Specifies the name of the object whose password is to be stored. If <i><a href="/docs/linux/man/8-krb5kdc/">krb5kdc</a>(8)</i> or <i><a href="/docs/linux/man/8-kadmind/">kadmind</a>(8)</i> are configured for simple binding, this should be the distinguished name it will use as given by the <code>ldap_kdc_dn</code> or <code>ldap_kadmind_dn</code> variable in <i><a href="/docs/linux/man/5-kdc-conf/">kdc.conf</a>(5)</i>. If the KDC or kadmind is configured for SASL binding, this should be the authentication name it will use as given by the <code>ldap_kdc_sasl_authcid</code> or <code>ldap_kadmind_sasl_authcid</code> variable. </p>
<p> Example: </p>
<pre>kdb5_ldap_util stashsrvpw -f /home/andrew/conf_keyfile
 cn=service-kdc,o=org
Password for &quot;cn=service-kdc,o=org&quot;:
Re-enter password for &quot;cn=service-kdc,o=org&quot;:</pre>
</dl>
<h3>create_policy</h3>
<p><code>create_policy</code> [<code>-r</code> <i>realm</i>] [<code>-maxtktlife</code> <i>max_ticket_life</i>] [<code>-maxrenewlife</code> <i>max_renewable_ticket_life</i>] [<i>ticket_flags</i>] <i>policy_name</i> </p>
<p> Creates a ticket policy in the directory. Options:</p>
<dl>
<dt><code>-r</code> <i>realm</i></p>
<dd>Specifies the Kerberos realm of the database.</p>
<dt><code>-maxtktlife</code> <i>max_ticket_life</i></p>
<dd>(<i>getdate</i> string) Specifies maximum ticket life for principals.</p>
<dt><code>-maxrenewlife</code> <i>max_renewable_ticket_life</i></p>
<dd>(<i>getdate</i> string) Specifies maximum renewable life of tickets for principals.</p>
<dt><i>ticket_flags</i></p>
<dd>Specifies the ticket flags. If this option is not specified, by default, no restriction will be set by the policy. Allowable flags are documented in the description of the <code>add_principal</code> command in <i><a href="/docs/linux/man/1-kadmin/">kadmin</a>(1)</i>.</p>
<dt><i>policy_name</i></p>
<dd>Specifies the name of the ticket policy. </p>
<p> Example: </p>
<pre>kdb5_ldap_util -D cn=admin,o=org -H <a href="ldaps://ldap-server1.mit.edu">ldaps://ldap-server1.mit.edu</a>
 create_policy -r ATHENA.MIT.EDU -maxtktlife &quot;1 day&quot;
 -maxrenewlife &quot;1 week&quot; -allow_postdated +needchange
 -allow_forwardable tktpolicy
Password for &quot;cn=admin,o=org&quot;:</pre>
</dl>
<h3>modify_policy</h3>
<p><code>modify_policy</code> [<code>-r</code> <i>realm</i>] [<code>-maxtktlife</code> <i>max_ticket_life</i>] [<code>-maxrenewlife</code> <i>max_renewable_ticket_life</i>] [<i>ticket_flags</i>] <i>policy_name</i> </p>
<p> Modifies the attributes of a ticket policy. Options are same as for <code>create_policy</code>. </p>
<p> Example: </p>
<pre>kdb5_ldap_util -D cn=admin,o=org -H
 <a href="ldaps://ldap-server1.mit.edu">ldaps://ldap-server1.mit.edu</a> modify_policy -r ATHENA.MIT.EDU
 -maxtktlife &quot;60 minutes&quot; -maxrenewlife &quot;10 hours&quot;
 +allow_postdated -requires_preauth tktpolicy
Password for &quot;cn=admin,o=org&quot;:</pre>
<h3>view_policy</h3>
<p><code>view_policy</code> [<code>-r</code> <i>realm</i>] <i>policy_name</i> </p>
<p> Displays the attributes of a ticket policy. Options:</p>
<dl>
<dt><i>policy_name</i></p>
<dd>Specifies the name of the ticket policy. </p>
<p> Example: </p>
<pre>kdb5_ldap_util -D cn=admin,o=org -H <a href="ldaps://ldap-server1.mit.edu">ldaps://ldap-server1.mit.edu</a>
 view_policy -r ATHENA.MIT.EDU tktpolicy
Password for &quot;cn=admin,o=org&quot;:
Ticket policy: tktpolicy
Maximum ticket life: 0 days 01:00:00
Maximum renewable life: 0 days 10:00:00
Ticket flags: DISALLOW_FORWARDABLE REQUIRES_PWCHANGE</pre>
</dl>
<h3>destroy_policy</h3>
<p><code>destroy_policy</code> [<code>-r</code> <i>realm</i>] [<code>-force</code>] <i>policy_name</i> </p>
<p> Destroys an existing ticket policy. Options:</p>
<dl>
<dt><code>-r</code> <i>realm</i></p>
<dd>Specifies the Kerberos realm of the database.</p>
<dt><code>-force</code></p>
<dd>Forces the deletion of the policy object. If not specified, the user will be prompted for confirmation before deleting the policy.</p>
<dt><i>policy_name</i></p>
<dd>Specifies the name of the ticket policy. </p>
<p> Example: </p>
<pre>kdb5_ldap_util -D cn=admin,o=org -H <a href="ldaps://ldap-server1.mit.edu">ldaps://ldap-server1.mit.edu</a>
 destroy_policy -r ATHENA.MIT.EDU tktpolicy
Password for &quot;cn=admin,o=org&quot;:
This will delete the policy object 'tktpolicy', are you sure?
(type 'yes' to confirm)? yes
** policy object 'tktpolicy' deleted.</pre>
</dl>
<h3>list_policy</h3>
<p><code>list_policy</code> [<code>-r</code> <i>realm</i>] </p>
<p> Lists the ticket policies in realm if specified or in the default realm. Options:</p>
<dl>
<dt><code>-r</code> <i>realm</i></p>
<dd>Specifies the Kerberos realm of the database. </p>
<p> Example: </p>
<pre>kdb5_ldap_util -D cn=admin,o=org -H <a href="ldaps://ldap-server1.mit.edu">ldaps://ldap-server1.mit.edu</a>
 list_policy -r ATHENA.MIT.EDU
Password for &quot;cn=admin,o=org&quot;:
tktpolicy
tmppolicy
userpolicy</pre>
</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-kadmin/">kadmin</a>(1)</i></p>
<h2>Author</h2>
<p>MIT</p>
<h2>Copyright</h2>
<p>1985-2016, MIT</p>
