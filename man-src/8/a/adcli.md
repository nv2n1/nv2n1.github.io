---
title: "adcli(8)"
name: "adcli"
section: "8"
letter: "a"
url: "/docs/linux/man/8-adcli/"
description: "adcli – Tool for performing actions on an Active Directory domain"
---

<p>adcli &#8211; Tool for performing actions on an Active Directory domain</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>adcli info</code> domain.example.com</p>
<dt> <code>adcli join</code> domain.example.com</p>
<dt> <code>adcli update</code></p>
<dt> <code>adcli create-user</code> [&#8211;domain=domain.example.com] user</p>
<dt> <code>adcli delete-user</code> [&#8211;domain=domain.example.com] user</p>
<dt> <code>adcli create-group</code> [&#8211;domain=domain.example.com] user</p>
<dt> <code>adcli delete-group</code> [&#8211;domain=domain.example.com] user</p>
<dt> <code>adcli add-member</code> [&#8211;domain=domain.example.com] group user&#8230;</p>
<dt> <code>adcli remove-member</code> [&#8211;domain=domain.example.com] group user&#8230;</p>
<dt> <code>adcli preset-computer</code> [&#8211;domain=domain.example.com] computer&#8230;</p>
<dt> <code>adcli reset-computer</code> [&#8211;domain=domain.example.com] computer</p>
<dt> <code>adcli delete-computer</code> [&#8211;domain=domain.example.com] computer</dl>
<h2>General Overview</h2>
<p><code>adcli</code></p>
<dd>is a command line tool that can perform actions in an Active Directory domain. Among other things it can be used to join a computer to a domain. </p>
<p> See the various sub commands below. The following global options can be used: </p>
<p> <code>-D, &#8211;domain=</code><i>domain</i></p>
<dl>
<dd>The domain to connect to. If a domain is not specified then the domain part of the local computer&#8217;s host name is used.</dl>
<p> <code>-R, &#8211;domain-realm=</code><i>REALM</i></p>
<dl>
<dd>Kerberos realm for the domain. If not specified then the upper cased domain name is used.</dl>
<p> <code>-S, &#8211;domain-controller=</code><i>server</i></p>
<dl>
<dd>Connect to a specific domain controller. If not specified then an appropriate domain controller is automatically discovered.</dl>
<p> <code>-C, &#8211;login-ccache=</code><i>/path/to/file</i></p>
<dl>
<dd>Use the specified kerberos credential cache to authenticate with the domain.</dl>
<p> <code>-U, &#8211;login-user=</code><i>User</i></p>
<dl>
<dd>Use the specified user account to authenticate with the domain. If not specified then the name &#8216;Administrator&#8217; will be used.</dl>
<p> <code>&#8211;no-password</code></p>
<dl>
<dd>Don&#8217;t show prompts for or read a password from input.</dl>
<p> <code>-W, &#8211;prompt-password</code></p>
<dl>
<dd>Prompt for a password if necessary. This is the default.</dl>
<p> <code>&#8211;stdin-password</code></p>
<dl>
<dd>Read a password from stdin input instead of prompting for a password.</dl>
<p> <code>-v, &#8211;verbose</code></p>
<dl>
<dd>Run in verbose mode with debug output.</dl>
<h2>Querying Domain Information</h2>
<p><code>adcli info</code> displays discovered information about an Active Directory domain or an Active Directory domain controller. </p>
<dl>
<dd>
<pre>$ adcli info domain.example.com
...</pre>
</dl>
<dl>
<dd>
<pre>$ adcli info --domain-controller=dc.domain.example.com
...</pre>
</dl>
<p> <code>adcli info</code> will output as much information as it can about the domain. The information is designed to be both machine and human readable. The command will exit with a non-zero exit code if the domain does note exist or cannot be reached. </p>
<p> To show domain info for a specific domain controller use the <code>&#8211;domain-controller</code> option to specify which domain controller to query. </p>
<p> Use the <code>&#8211;verbose</code> option to show details of how the domain is discovered and queried. Many of the global options, in particular authentication options, are not usable with the <code>adcli info</code> command.</p>
<h2>Joining The Local Machine To A Domain</h2>
<p><code>adcli join</code> creates a computer account in the domain for the local machine, and sets up a keytab for the machine. It does not configure an authentication service (such as <code>sssd</code>). </p>
<dl>
<dd>
<pre>$ adcli join domain.example.com
Password for Administrator:</pre>
</dl>
<p> In addition to the global options, you can specify the following options to control how this operation is done. </p>
<p> <code>-N, &#8211;computer-name=</code><i>computer</i></p>
<dl>
<dd>The short non-dotted name of the computer account that will be created in the domain. If not specified then the first portion of the <code>&#8211;host-fqdn</code> is used.</dl>
<p> <code>-O, &#8211;domain-ou=</code><i>OU=xxx</i></p>
<dl>
<dd>The full distinguished name of the OU in which to create the computer account. If not specified then the computer account will be created in a default location.</dl>
<p> <code>-H, &#8211;host-fqdn=</code><i>host</i></p>
<dl>
<dd>Override the local machine&#8217;s fully qualified domain name. If not specified the local machine&#8217;s hostname will be retrieved via <code>gethostname()</code>.</dl>
<p> <code>-K, &#8211;host-keytab=</code><i>/path/to/keytab</i></p>
<dl>
<dd>Specify the path to the host keytab where host credentials will be written after a successful join operation. If not specified the default location will be used, usually /etc/krb5.keytab.</dl>
<p> <code>&#8211;login-type=</code><i>{computer|user}</i></p>
<dl>
<dd>Specify the type of authentication that will be performed before creating the machine account in the domain. If set to &#8216;computer&#8217; then the computer must already have a preset account in the domain. If not specified and none of the other <code>&#8211;login-xxx</code> arguments have been specified, then will try both &#8216;computer&#8217; and &#8216;user&#8217; authentication.</dl>
<p> <code>&#8211;os-name=</code><i>name</i></p>
<dl>
<dd>Set the operating system name on the computer account. The default depends on where adcli was built, but is usually something like &#8216;linux-gnu&#8217;.</dl>
<p> <code>&#8211;os-service-pack=</code><i>pack</i></p>
<dl>
<dd>Set the operating system service pack on the computer account. Not set by default.</dl>
<p> <code>&#8211;os-version=</code><i>version</i></p>
<dl>
<dd>Set the operating system version on the computer account. Not set by default.</dl>
<p> <code>&#8211;service-name=</code><i>service</i></p>
<dl>
<dd>Additional service name for a kerberos principal to be created on the computer account. This option may be specified multiple times.</dl>
<p> <code>&#8211;user-principal=</code><i>host/name [at] REALM</i></p>
<dl>
<dd>Set the userPrincipalName field of the computer account to this kerberos principal. If you omit the value for this option, then a principal will be set in the form of host/host.example.com [at] REALM</dl>
<p> <code>&#8211;one-time-password</code></p>
<dl>
<dd>Specify a one time password for a preset computer account. This is equivalent to using <code>&#8211;login-type=computer</code> and providing a password as input.</dl>
<p> <code>&#8211;show-details</code></p>
<dl>
<dd>After a successful join print out information about join operation. This is output in a format that should be both human and machine readable.</dl>
<p> <code>&#8211;show-password</code></p>
<dl>
<dd>After a successful join print out the computer machine account password. This is output in a format that should be both human and machine readable.</dl>
<h2>Updating The Machine Account Password And Other Attributes</h2>
<p><code>adcli update</code> updates the password of the computer account on the domain controller for the local machine, write the new keys to the keytab and removes older keys. It keeps the previous key on purpose because AD will need some time to replicate the new key to all DCs hence the previous key might still be used. </p>
<dl>
<dd>
<pre>$ adcli update</pre>
</dl>
<p> If used with a credential cache other attributes of the computer account can be changed as well if the principal has sufficient privileges. </p>
<dl>
<dd>
<pre>$ kinit Administrator
$ adcli update --login-ccache=/tmp/krbcc_123</pre>
</dl>
<p> In addition to the global options, you can specify the following options to control how this operation is done. </p>
<p> <code>-N, &#8211;computer-name=</code><i>computer</i></p>
<dl>
<dd>The short non-dotted name of the computer account that will be created in the domain. If not specified it will be retrieved from the keytab entries.</dl>
<p> <code>-H, &#8211;host-fqdn=</code><i>host</i></p>
<dl>
<dd>The local machine&#8217;s fully qualified domain name. If not specified the local machine&#8217;s hostname will be retrieved from the keytab entries.</dl>
<p> <code>-K, &#8211;host-keytab=</code><i>/path/to/keytab</i></p>
<dl>
<dd>Specify the path to the host keytab where current host credentials are stored and the new ones will be written to. If not specified the default location will be used, usually /etc/krb5.keytab.</dl>
<p> <code>&#8211;os-name=</code><i>name</i></p>
<dl>
<dd>Set the operating system name on the computer account. Not set by default.</dl>
<p> <code>&#8211;os-service-pack=</code><i>pack</i></p>
<dl>
<dd>Set the operating system service pack on the computer account. Not set by default.</dl>
<p> <code>&#8211;os-version=</code><i>version</i></p>
<dl>
<dd>Set the operating system version on the computer account. Not set by default.</dl>
<p> <code>&#8211;service-name=</code><i>service</i></p>
<dl>
<dd>Additional service name for a Kerberos principal to be created on the computer account. This option may be specified multiple times.</dl>
<p> <code>&#8211;user-principal=</code><i>host/name [at] REALM</i></p>
<dl>
<dd>Set the userPrincipalName field of the computer account to this Kerberos principal.</dl>
<p> <code>&#8211;computer-password-lifetime=</code><i>lifetime</i></p>
<dl>
<dd>Only update the password of the computer account if it is older than the lifetime given in days. By default the password is updated if it is older than 30 days.</dl>
<p> <code>&#8211;show-details</code></p>
<dl>
<dd>After a successful join print out information about join operation. This is output in a format that should be both human and machine readable.</dl>
<h2>Creating A User</h2>
<p><code>adcli create-user</code> creates a new user account in the domain. </p>
<dl>
<dd>
<pre>$ adcli create-user Fry --domain=domain.example.com \
 --display-name=&quot;Philip J. Fry&quot; --mail=fry [at] domain.example.com</pre>
</dl>
<p> In addition to the global options, you can specify the following options to control how the user is created. </p>
<p> <code>&#8211;display-name=</code><i>&quot;Name&quot;</i></p>
<dl>
<dd>Set the displayName attribute of the new created user account.</dl>
<p> <code>-O, &#8211;domain-ou=</code><i>OU=xxx</i></p>
<dl>
<dd>The full distinguished name of the OU in which to create the user account. If not specified then the computer account will be created in a default location.</dl>
<p> <code>&#8211;mail=</code><i>email [at] domain.com</i></p>
<dl>
<dd>Set the mail attribute of the new created user account. This attribute may be specified multiple times.</dl>
<p> <code>&#8211;unix-home=</code><i>/home/user</i></p>
<dl>
<dd>Set the unixHomeDirectory attribute of the new created user account, which should be an absolute path to the user&#8217;s home directory.</dl>
<p> <code>&#8211;unix-gid=</code><i>111</i></p>
<dl>
<dd>Set the gidNumber attribute of the new created user account, which should be the user&#8217;s numeric primary group id.</dl>
<p> <code>&#8211;unix-shell=</code><i>/bin/shell</i></p>
<dl>
<dd>Set the loginShell attribute of the new created user account, which should be a path to a valid shell.</dl>
<p> <code>&#8211;unix-uid=</code><i>111</i></p>
<dl>
<dd>Set the uidNumber attribute of the new created user account, which should be the user&#8217;s numeric primary user id.</dl>
<h2>Deleting A User</h2>
<p><code>adcli delete-user</code> deletes a user account from the domain. </p>
<dl>
<dd>
<pre>$ adcli delete-user Fry --domain=domain.example.com</pre>
</dl>
<p> The various global options can be used.</p>
<h2>Creating A Group</h2>
<p><code>adcli create-group</code> creates a new group in the domain. </p>
<dl>
<dd>
<pre>$ adcli create-group Pilots --domain=domain.example.com \
 --description=&quot;Group for all pilots&quot;</pre>
</dl>
<p> In addition to the global options, you can specify the following options to control how the group is created. </p>
<p> <code>&#8211;description=</code><i>&quot;text&quot;</i></p>
<dl>
<dd>Set the description attribute of the new created group.</dl>
<p> <code>-O, &#8211;domain-ou=</code><i>OU=xxx</i></p>
<dl>
<dd>The full distinguished name of the OU in which to create the group. If not specified then the group will be created in a default location.</dl>
<h2>Deleting A Group</h2>
<p><code>adcli delete-group</code> deletes a group from the domain. </p>
<dl>
<dd>
<pre>$ adcli delete-group Pilots --domain=domain.example.com</pre>
</dl>
<p> The various global options can be used.</p>
<h2>Adding A Member To A Group</h2>
<p><code>adcli add-member</code> adds one or more users to a group in the domain. The group is specified first, and then the various users to be added. </p>
<dl>
<dd>
<pre>$ adcli add-member --domain=domain.example.com Pilots Leela Scruffy</pre>
</dl>
<p> The various global options can be used.</p>
<h2>Removing A Member From A Group</h2>
<p><code>adcli remove-member</code> removes a user from a group in the domain. The group is specified first, and then the various users to be removed. </p>
<dl>
<dd>
<pre>$ adcli remove-member --domain=domain.example.com Pilots Scruffy</pre>
</dl>
<p> The various global options can be used.</p>
<h2>Preset Computer Accounts</h2>
<p><code>adcli preset-computer</code> pre-creates one or more computer accounts in the domain for machines to later use when joining the domain. By doing this machines can join using a one time password or automatically without a password. </p>
<dl>
<dd>
<pre>$ adcli preset-computer --domain=domain.example.com \
 host1.example.com host2
Password for Administrator:</pre>
</dl>
<p> If the computer names specified contain dots, then they are treated as fully qualified host names, otherwise they are treated as short computer names. The computer accounts must not already exist. </p>
<p> In addition to the global options, you can specify the following options to control how this operation is done. </p>
<p> <code>-O, &#8211;domain-ou=</code><i>OU=xxx</i></p>
<dl>
<dd>The full distinguished name of the OU in which to create the computer accounts. If not specified then the computer account will be created in a default location.</dl>
<p> <code>&#8211;one-time-password</code></p>
<dl>
<dd>Specify a one time password to use when presetting the computer accounts. If not specified then a default password will be used, which allows for later automatic joins.</dl>
<p> <code>&#8211;os-name=</code><i>name</i></p>
<dl>
<dd>Set the operating system name on the computer account. The default depends on where adcli was built, but is usually something like &#8216;linux-gnu&#8217;.</dl>
<p> <code>&#8211;os-service-pack=</code><i>pack</i></p>
<dl>
<dd>Set the operating system service pack on the computer account. Not set by default.</dl>
<p> <code>&#8211;os-version=</code><i>version</i></p>
<dl>
<dd>Set the operating system version on the computer account. Not set by default.</dl>
<p> <code>&#8211;service-name=</code><i>service</i></p>
<dl>
<dd>Additional service name for a kerberos principal to be created on the computer account. This option may be specified multiple times.</dl>
<p> <code>&#8211;user-principal</code></p>
<dl>
<dd>Set the userPrincipalName field of the computer account to this kerberos principal in the form of host/host.example.com [at] REALM</dl>
<h2>Reset Computer Account</h2>
<p><code>adcli reset-computer</code> resets a computer account in the domain. If a the appropriate machine is currently joined to the domain, then its membership will be broken. The account must already exist. </p>
<dl>
<dd>
<pre>$ adcli reset-computer --domain=domain.example.com host2</pre>
</dl>
<p> If the computer names specified contain dots, then they are treated as fully qualified host names, otherwise they are treated as short computer names. </p>
<p> In addition to the global options, you can specify the following options to control how this operation is done. </p>
<p> <code>&#8211;login-type=</code><i>{computer|user}</i></p>
<dl>
<dd>Specify the type of authentication that will be performed before creating the machine account in the domain. If set to &#8216;computer&#8217; then the computer must already have a preset account in the domain. If not specified and none of the other <code>&#8211;login-xxx</code> arguments have been specified, then will try both &#8216;computer&#8217; and &#8216;user&#8217; authentication.</dl>
<h2>Delete Computer Account</h2>
<p><code>adcli delete-computer</code> deletes a computer account in the domain. The account must already exist. </p>
<dl>
<dd>
<pre>$ adcli delete-computer --domain=domain.example.com host2
Password for Administrator:</pre>
</dl>
<p> If the computer name contains a dot, then it is treated as fully qualified host name, otherwise it is treated as short computer name. </p>
<p> If no computer name is specified, then the host name of the computer adcli is running on is used, as returned by gethostname(). </p>
<p> The various global options can be used.</p>
<h2>Bugs</h2>
<p>Please send bug reports to either the distribution bug tracker or the upstream bug tracker at m[blue]<code><a rel="nofollow" href="https://bugs.freedesktop.org/enter_bug.cgi?product=realmd">https://bugs.freedesktop.org/enter_bug.cgi?product=realmd</a>&amp;component=adcli</code>m[]</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-realmd/">realmd</a></code>(8), <code><a href="/docs/linux/man/8-net/">net</a></code>(8), <code><a href="/docs/linux/man/8-sssd/">sssd</a></code>(8) Further details available in the realmd online documentation at m[blue]<code><a rel="nofollow" href="http://www.freedesktop.org/software/realmd/">http://www.freedesktop.org/software/realmd/</a></code>m[] </p>
