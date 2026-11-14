---
title: "msktutil(1)"
name: "msktutil"
section: "1"
letter: "m"
url: "/docs/linux/man/1-msktutil/"
description: "msktutil – fetches and manages kerberos keytabs in an Active Directory environment"
---

<h2>NAME</h2>
<p> msktutil &#8211; fetches and manages kerberos keytabs in an Active Directory environment</p>
<h2>SYNOPSIS</h2>
<p> <code>msktutil</code> [command 1] [command 2] [command 3] &#8230;</p>
<h2>DESCRIPTION</h2>
<p> msktutil is a Unix/Linux keytab client for Microsoft Active Directory environments. This program is capable of creating accounts in Active Directory, adding service principals to those accounts, and creating local keytab files so that kerberizied services can utilize Active directory as a Kerberos realm. msktutil will create and manage machine accounts by default. The &#8211;use-service-account option lets msktutil operate on service accounts. msktutil requires that the Kerberos client libraries are properly installed and configured to use Active Directory as a realm. </p>
<p> Whenever a principal is added or a keytab is updated, the secret password for the corresponding account is changed. By default, the password is not stored, so it needs to be reset each time msktutil is executed. All entries in the keytab will be automatically updated whenever the password is reset. The previous entries will be left in the keytab, so sessions using the older key versions will not break. This behavior is similar to the way Windows hosts handle machine password changes.</p>
<h2>CREDENTIALS</h2>
<p> There are two common methods of using this program. The first is to &quot;kinit&quot; with Administrator-like credentials which have permission to create computer objects in your Active Directory server. If you invoke the program with such credentials, you can create a new computer account or service account from scratch. </p>
<p> The second is to pre-create the accounts with such credentials, and then invoke msktutil on a machine without any special permissions. When the computer account or service account exists already, msktutil will attempt to authenticate as that account using either the existing keytab, or if that fails, a default password. When that default password is not specified with the option &#8211;old-account-password, msktutil will use the default machine password. It will then change the password and update the keytab appropriately. This is usually the more convenient option when joining many computers to the domain. </p>
<p> To pre-create a computer account, you may use the Active Directory Users and Computers GUI, select &quot;new computer&quot; from the right click menu, and type the short DNS name, then right click on the newly created object and select &quot;Reset account&quot; to set the password to the default value. Another alternative is to invoke msktutil with the &#8211;precreate argument. Both methods accomplish the same thing. </p>
<p> To pre-create a service account, you may use the Active Directory Users and Computers GUI, select &quot;new user&quot; from the right click menu, fill in all required data, set the password to a specific value and use setspn.exe to set the desired servicePrincipalName(s). You may also select &quot;must change password at next logon&quot;.</p>
<h2>PASSWORD EXPIRY</h2>
<p> Be aware that Windows machines will, by default, automatically change their account password every 30 days, and thus many domains have a 90-day password expiry window, after which your keytab will stop working. There are two ways to deal with this: </p>
<p> a) (Preferred): Make sure you&#8217;re running a daily cron job to run msktutil &#8211;auto-update, which will change the password automatically 30 days after it was last changed and update the keytab. </p>
<p> b) (Not preferred): disable password expiry for the account via the &#8211;dont-expire-password option (or otherwise setting DONT_EXPIRE_PASSWORD flag in userAccountControl in AD).</p>
<h2>PASSWORD POLICY ISSUES</h2>
<p> This section only applies to msktutil &#8211;use-service-account. </p>
<p> While machine account passwords may be changed at any time, service accounts are user accounts and your Active Directory domain may have special password policies for those user accounts. E.g., &quot;minimum password age&quot; is typically set to 1 day, which means that you will have to wait for that time to pass until you may invoke msktutil &#8211;update &#8211;use-service-account.</p>
<h2>OTHER NOTES</h2>
<p> Unlike other kerberos implementations, Active Directory has only a single key for all of the principals associated with an account. So, if you create a HTTP/hostname service principal, it will share the same key as the host/hostname principal. If you want to isolate (security-wise) different service principals, you may want to create a dedicated service account for them (with &#8211;use-service-account) and a separate keytab file (with &#8211;keytab). </p>
<p> Also note: kinit -k &#8216;host/computername&#8217; *will not work*, by default, even when that is a valid service principal existing in your keytab. Active Directory does not allow you to authenticate as a service principal, so do not use that as a test of whether the service principal is working. If you actually want to authenticate as the computer account user, kinit -k &#8216;computername$&#8217; instead. </p>
<p> If you really need to be able to authenticate as &#8216;host/computername&#8217;, you can also use the &#8211;upn argument to set the userPrincipalName attribute (generally requires administrator credentials, not computer account credentials). Both &#8216;computername$&#8217; and the value of userPrincipalName are treated as valid account names to kinit as. </p>
<p> msktutil will use kerberized LDAP operations to talk to domain controllers. To obtain a LDAP service ticket, the DNS service will be used to construct the domain controllers LDAP principal name. If DNS is mis-configured, this construction may fail. To work around this issue, you may specify the fully qualified DNS name of your domain controller with the &#8211;server option and additionally use the &#8211;no-reverse-lookups option. </p>
<p> Samba (<a rel="nofollow" href="http://www.samba.org">www.samba.org</a>) provides the net command that can be used to manage kerberos keytabs as well. Using msktutil and commands like &quot;net ads join&quot; or &quot;net ads keytab&quot; together can lead to trouble. With the &#8211;set-samba-secret option, msktutil can be used as a replacement for net. </p>
<p> Active Directory includes authorization data (e.g. information about group memberships) in Kerberos tickets. This information is called PAC and may lead to very large ticket sizes. Especially HTTP services are known to produce failures if that size exceeds the HTTP header size. If your service does not make use of that PAC information (which is true for most Unix/Linux-services) you may just disable it with the &#8211;no-pac option.</p>
<h2>MODES</h2>
<dl>
<dt>-v, &#8211;version</p>
<dd> Displays version information</p>
<dt>&#8211;help</p>
<dd> Displays a help message</p>
<dt>-c, &#8211;create</p>
<dd> Creates a keytab for the current host or a given service account. Equivalent to &#8211;update &#8211;service host.</p>
<dt>-f, &#8211;flush</p>
<dd> Flushes out all principals for the current accountname from the keytab, and makes corresponding changes to the machine or service account.</p>
<dt>-u, &#8211;update</p>
<dd> Forces a password change and updates all related service principal entries from the servicePrincipalName and userPrincipalName attributes. Updates dNSDomainName for machine accounts and always updates msDS-supportedEncryptionTypes attributes with current values, and applies other changes as specified.</p>
<dt>&#8211;auto-update</p>
<dd> Checks if the password is at least 30 days old (from pwdLastSet attribute), and that the account does not have password expiry disabled. If those conditions are met, acts just like &#8211;update. Will also update if the keytab failed to authenticate but the default password did work (e.g. after resetting the account in AD). Otherwise, exits without doing anything (even if attribute modifying options are given). This option is intended for use from a daily crontab to ensure that the password is rotated regularly.</p>
<dt>&#8211;precreate</p>
<dd> Pre-create (or update) an account for the given host with default password. Does not use or update local keytab. Requires -h or &#8211;computer-name argument. Implies &#8211;user-creds-only. Generally requires administrator credentials.</dl>
<h2>CONNECTION/SETUP OPTIONS</h2>
<dl>
<dt>-b, &#8211;base &lt;base&gt;</p>
<dd> Specifies a relative LDAP base when creating a new account. For example, specifying &#8216;-b OU=Unix&#8217; for a computer named SERVER in an Active Directory domain example.com would create a computer account in the LDAP path: CN=SERVER,OU=Unix,DC=EXAMPLE,DC=COM. This option can also be specified by setting the MSKTUTIL_LDAP_BASE environment variable to the desired value. </p>
<p> If not specified, the default value is read from AD (and the default there, unless modified by an admin, is CN=Computers for machine accounts and CN=Users for service accounts).</p>
<dt>&#8211;computer-name &lt;name&gt;</p>
<dd> Specifies that the new account should use &lt;name&gt; for the computer account name and the SAM Account Name. Note that a &#8216;$&#8217; will be automatically appended to the SAM Account Name. Defaults to the machine&#8217;s hostname, excluding the realm, with dots replaced with dashes. </p>
<p> That is: if the realm is EXAMPLE.COM, and the hostname is FOO.EXAMPLE.COM, the default computer name is FOO. If the hostname is FOO.BAR.EXAMPLE.COM, the default computer name is FOO-BAR.</p>
<dt>&#8211;account-name &lt;name&gt;</p>
<dd> An alias for &#8211;computer-name that can be used when operating on service accounts. Note that a &#8216;$&#8217; will not be automatically appended to the SAM Account Name when using service accounts.</p>
<dt>&#8211;old-account-password &lt;password&gt;</p>
<dd> Use supplied account password for authentication. This is useful if the keytab does not yet exist but the password of the computer account is known. This password will be changed by msktutil in order to create or update the keytab</p>
<dt>-h, &#8211;hostname &lt;name&gt;</p>
<dd> Overrides the current hostname to be used to be &lt;name&gt;. If this is not specified, the local host name will be used. Note that the local name lookup service will be to qualify and resolve names into fully-qualified names, including a domain extension. This affects the default hostname for other arguments, and the default computer-name. The hostname is also used to set the dNSDomainName attribute.</p>
<dt>-k, &#8211;keytab &lt;file&gt;</p>
<dd> Specifies to use &lt;file&gt; for the keytab. This option can also be specified by setting the MSKTUTIL_KEYTAB environment variable to the name of the desired keytab file. This keytab is both read from, in order to authenticate as the given account, and written to, after updating the account password. Default: /etc/krb5.keytab &#8211;keytab-auth-as &lt;name&gt; Specifies which principal name we should try to use, when we authenticate from a keytab. Normally, msktutil will try to use the account name or the host principal for the current host. If this option is specified, instead msktutil will try to use the given principal name first, and only fall back to the default behavior if we fail to authenticate with the given name. This option can be useful if you do not know the current password for the relevant account, do not have a keytab with the account principal, but you do have a keytab with a service principal associated with that account.</p>
<dt>&#8211;server &lt;server&gt;</p>
<dd> Specifies to use &lt;server&gt; as the domain controller. This affects both kerberos and ldap operations. The server can also be specified by setting the MSKTUTIL_SERVER environment variable. Default: looked up in DNS from the realm name.</p>
<dt>&#8211;server-behind-nat</p>
<dd> When the server is behind a firewall that performs Network Address Translation, KRB-PRIV messages fail validation. This is because the IP adddress in the encrypted part of the message cannot be rewritten in the NAT process. This option ignores the resulting error for the password change process, allowing systems outside the NAT firewall to join the domain managed by servers inside the NAT firewall.</p>
<dt>&#8211;realm &lt;realm&gt;</p>
<dd> Specifies to use &lt;realm&gt; as kerberos realm. Default: use the default_realm from [libdefaults] section of krb5.conf.</p>
<dt>&#8211;site &lt;site&gt;</p>
<dd> Find and use domain controller in specific AD site. This option is ignored if option &#8211;server is used.</p>
<dt>-N, &#8211;no-reverse-lookup</p>
<dd> Do not attempt to canonicalize the name of the domain controller via DNS reverse lookups. You may need to do this if your client cannot resolve the PTR records for a domain controller or your DNS servers store incorrect PTR records. Default: Use DNS reverse lookups to canonicalize DC names.</p>
<dt>&#8211;user-creds-only</p>
<dd> Don&#8217;t attempt to authenticate with a keytab: only use user&#8217;s credentials (from e.g. kinit). You may need to do this to modify certain attributes that require Administrator credentials (description, userAccountControl, userPrincipalName, in a default AD setup).</p>
<dt>&#8211;verbose</p>
<dd> Enables verbose status messages. May be specified more then once to get LDAP debugging. </p>
</dl>
<h2>OBJECT TYPE/ATTRIBUTE-SETTING OPTIONS</h2>
<dl>
<dt>&#8211;use-service-account</p>
<dd> Create and maintain service accounts instead of machine accounts.</p>
<dt>&#8211;delegation</p>
<dd> Enables the account to be trusted for delegation. This option can also be enabled by setting the MSKTUTIL_DELEGATION environment variable. This modifies the userAccountControl attribute. Generally requires administrator credentials.</p>
<dt>&#8211;description &lt;text&gt;</p>
<dd> Sets the account&#8217;s description attribute to the given text (or removes if text is &#8221;). Generally requires administrator credentials.</p>
<dt>&#8211;disable-delegation</p>
<dd> Disables the account from being trusted for delegation. This modifies the userAccountControl attribute. Generally requires administrator credentials.</p>
<dt>&#8211;disable-no-pac</p>
<dd> Unsets the flag that disables the KDC&#8217;s including of a PAC in the machine&#8217;s service tickets. This modifies the userAccountControl attribute. Generally requires administrator credentials.</p>
<dt>&#8211;dont-expire-password</p>
<dd> Sets the DONT_EXPIRE_PASSSWORD bit in the userAccountControl attribute, which disables password expiry for this account. If you don&#8217;t run a cron job to periodically rotate the keytab, you will want to set this flag. Generally requires administrator credentials.</p>
<dt>&#8211;do-expire-password</p>
<dd> Unsets the DONT_EXPIRE_PASSWORD flag in the userAccountControl attribute. Generally requires administrator credentials.</p>
<dt>&#8211;enctypes &lt;integer&gt;</p>
<dd> Sets the supported encryption types in the msDs-supportedEncryptionTypes field. </p>
<p> You may OR together the following values:<br />
&nbsp;<wbr>&nbsp;<wbr>0x1=des-cbc-crc<br />
&nbsp;<wbr>&nbsp;<wbr>0x2=des-cbc-md5<br />
&nbsp;<wbr>&nbsp;<wbr>0x4=rc4-hmac-md5<br />
&nbsp;<wbr>&nbsp;<wbr>0x8=aes128-cts-hmac-sha1<br />
&nbsp;<wbr>&nbsp;<wbr>0x10=aes256-cts-hmac-sha1 </p>
<p> This value is used to determine which encryption types AD will offer to use, and which encryption types to put in the keytab. </p>
<p> If the value is set to 0x3 (that is: only the two DES types), it also attempts to set the DES-only flag in userAccountControl. </p>
<p> Note: Windows 2008R2 refuses to use DES by default; you thus cannot use DES-only keys unless you have enabled DES encryption for your domain first. Recent versions of MIT kerberos clients similarly refuse to use DES by default. </p>
<p> Default: sets the value to 0x1C: that is, use anything but DES.</p>
<dt>&#8211;allow-weak-crypto</p>
<dd> Enables the usage of DES keys for authentication. This is equivalent to MIT&#8217;s krb5.conf parameter allow_weak_crypto.</p>
<dt>&#8211;no-pac</p>
<dd> Specifies that service tickets for this account should not contain a PAC. This modifies the userAccountControl attribute. See Microsoft Knowledge Base article #832575 for details. This option can also be specified by setting the MSKTUTIL_NO_PAC environment variable. Generally requires administrator credentials.</p>
<dt>-s, &#8211;service &lt;principal&gt;</p>
<dd> Specifies a service principal to add to the account (and thus keytab, if appropriate). The service is of the form &lt;service&gt;/&lt;hostname&gt;. If the hostname is omitted, assumes current hostname. May be specified multiple times.</p>
<dt>&#8211;remove-service &lt;principal&gt;</p>
<dd> Specifies a service principal to remove from the account (and keytab if appropriate).</p>
<dt>&#8211;upn &lt;principal&gt;</p>
<dd> Sets the userPrincipalName on the computer account or service account to be &lt;principal&gt;. Note that the realm will automatically be appended to the value given. The userPrincipalName is an additional name which can be used to kinit. This is generally unnecessary, since you can always authenticate as the name given by &#8211;accountname (i.e. computername$ for computer accounts) whether or not userPrincipalName is set. Generally requires administrator credentials.</p>
<dt>&#8211;set-samba-secret</p>
<dd> Use Samba&#8217;s net changesecretpw command to locally set the machine account password in Samba&#8217;s secrets.tdb. $PATH need to include Samba&#8217;s net command. Samba needs to be configured appropriately.</dl>
<h2>EXAMPLES</h2>
<p> For unprivileged users the most common invocations are: </p>
<pre>
msktutil --update --service host --service HTTP
</pre>
<p> This will update a computer account in Active Directory with a new password, write out a new keytab, and ensure that it has both &quot;host&quot; and &quot;HTTP&quot; service principals are on it for the hostname. </p>
<pre>
msktutil --auto-update
</pre>
<p> This is useful in a daily cron job to check and rotate the password automatically when it&#8217;s 30 days old. </p>
<p> For users with admin privileges in AD, some common uses: </p>
<pre>
msktutil --create --service host --service HTTP
</pre>
<p> This will create a computer account in Active Directory with a new password, write out a new keytab, and ensure that it has both &quot;host&quot; and &quot;HTTP&quot; service principals are on it for the hostname. </p>
<pre>
msktutil --precreate --host computer1.example.com
</pre>
<p> This will pre-create an account for computer1 with the default password using your credentials. This can be done on a central host, e.g. to script the addition of many hosts. You can then use msktutil &#8211;create on the hosts themselves (without special credentials) to join them to the domain. </p>
<pre>
msktutil --host afs --service afs --enctypes 0x03
</pre>
<p> This will create an afs/cell.name [at] REALM principal, and associate that principal with a computer account called &#8216;afs&#8217;. The principal will be marked as DES-only, which is required for AFS. </p>
<pre><code>
msktutil-- create-- use - service - account-- service HTTP / hostname.example.com-- keytab / etc / apache / krb5.keytab-- accountname srv - http-- no - pac
</code></pre>
<p> This will create an HTTP/hostname.example.com [at] REALM principal, and associate that principal with a service account called &#8216;srv-http&#8217;. Corresponding Kerberos keys will be written to the keytab file /etc/apache/krb5.keytab. The size of Kerberos tickets for that service will stay small because no PAC information will be included. </p>
<pre><code>
msktutil-- create-- service host / hostname-- service host / hostname.example.com-- set - samba - secret-- enctypes 0x4
</code></pre>
<p> This will create a computer account in Active Directory that is compatible with Samba. The command creates a new password, write out a new keytab, and ensure that it includes both &quot;host/hostname&quot; and &quot;host/hostname.example.com&quot; as service principals (which is equivalent to what setspn.exe -R would do on windows). The new computer password will be stored in Samba&#8217;s secrets.tdb database to provide interoperability with Samba. As Samba (version 3) only supports arcfour-encrypted Kerberos tickets the &#8211;enctypes option must be used to select only that encryption type.</p>
<h2>AUTHOR</h2>
<p> Ken Dreyer, Mark Pröhl, Olaf Flebbe </p>
<h2>Index</h2>
