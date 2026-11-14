---
title: "pam_krb5(8)"
name: "pam_krb5"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_krb5/"
description: "pam_krb5 – Kerberos 5 authentication"
---

<p>pam_krb5 &#8211; Kerberos 5 authentication</p>
<h2>Synopsis</h2>
<p><code>auth required //usr/$LIB/security/pam_krb5.so</code><br />
 <code>session optional //usr/$LIB/security/pam_krb5.so</code><br />
 <code>account sufficient //usr/$LIB/security/pam_krb5.so</code><br />
 <code>password sufficient //usr/$LIB/security/pam_krb5.so</code> </p>
<h2>Description</h2>
<p>The pam_krb5.so module is designed to allow smooth integration of Kerberos 5 password-checking for applications which use PAM. It creates session-specific credential caches. If the system is an AFS client, it will also attempt to obtain tokens for the local cell, the cell which contains the user&#8217;s home directory, and any explicitly-configured cells. When a user logs in, the module&#8217;s authentication function performs a simple password check and, if possible, obtains Kerberos 5 credentials, caching them for later use. When the application requests initialization of credentials (or opens a session), the usual ticket files are created. When the application subsequently requests deletion of credentials or closing of the session, the module deletes the ticket files. When the application requests account management, if the module did not participate in authenticating the user, it will signal libpam to ignore the module. If the module did participate in authenticating the user, it will check for an expired user password and verify the user&#8217;s authorization using the .k5login file of the user being authenticated, which is expected to be accessible to the module. </p>
<h2>Arguments</h2>
<dl>
<dt>debug</p>
<dd>turns on debugging via <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3). Debugging messages are logged with priority <i>LOG_DEBUG</i>. </p>
<dt>debug_sensitive</p>
<dd>turns on debugging of sensitive information via <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3). Debug messages are logged with priority <i>LOG_DEBUG</i>. </p>
<dt>afs_cells=<i>cell.example.com[,&#8230;]</i></p>
<dd>tells pam_krb5.so to obtain tokens for the named cells, in addition to the local cell, for the user. The module will guess the principal name of the AFS service for the named cells, or it can be specified by giving cell in the form <i>cellname</i><code>=principalname</code>. </p>
<dt>always_allow_localname</p>
<dd>tells pam_krb5.so, when performing an authorization check using the target user&#8217;s .k5login file, to always allow access when the principal name being authenticated maps to the local user&#8217;s name (as configured using the <i>auth_to_local_names</i> and <i>auth_to_local</i> settings in <code><a href="/docs/linux/man/5-krb5-conf/">krb5.conf</a></code>(5), if your implementation provides those settings). Otherwise, if the file exists and can be read, but the principal is not explicitly listed, access is typically denied. This setting is disabled by default. </p>
<dt>armor = <i>true</i>|<i>false</i>|<i>service [&#8230;]</i></p>
<dd>attempt to use armoring when communicating with the KDC. This option is currently mainly only useful for testing, as the <i>keytab</i> method should not be expected to work when the module is called from an unprivileged process, and the <i>pkinit</i> method requires that the KDC is properly configured to offer anonymous PKINIT, and that the client is also properly configured to trust the KDC&#8217;s CA. The default is <code>false</code>. </p>
<dt>armor_strategy = <i>keytab,pkinit</i></p>
<dd>controls how the module will attempt to obtain tickets for use as armor. The value should be a comma-separated list of methods. Supported methods include <i>ketyab</i> and <i>pkinit</i>. The default is <code>keytab,pkinit</code>. </p>
<dt>banner=<i>Kerberos 5</i></p>
<dd>tells pam_krb5.so how to identify itself when users attempt to change their passwords. The default setting is &quot;Kerberos 5&quot;. </p>
<dt>ccache_dir=<i>/tmp</i></p>
<dd>tells pam_krb5.so which directory to use for storing credential caches. The default setting is <i>/tmp</i>. </p>
<dt>ccname_template=<i>FILE:%d/krb5cc_%U_XXXXXX</i></p>
<dd>specifies the location in which to place the user&#8217;s session-specific credential cache. This value is treated as a template, and these sequences are substituted:<br />
&nbsp;<wbr>&nbsp;<wbr>%u<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>login name</p>
<p>&nbsp;<wbr>&nbsp;<wbr>%U<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>login UID</p>
<p>&nbsp;<wbr>&nbsp;<wbr>%p<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>principal name</p>
<p>&nbsp;<wbr>&nbsp;<wbr>%r<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>principal&#8217;s realm name</p>
<p>&nbsp;<wbr>&nbsp;<wbr>%h<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>home directory</p>
<p>&nbsp;<wbr>&nbsp;<wbr>%d<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>the default ccache directory&nbsp;<wbr>(as set with&nbsp;<wbr><i>ccache_dir</i>)</p>
<p>&nbsp;<wbr>&nbsp;<wbr>%P<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>the current process ID</p>
<p>&nbsp;<wbr>&nbsp;<wbr>%%<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>literal&nbsp;<wbr>&#8216;%&#8217;</p>
<p> If the resulting template does not end with &quot;XXXXXX&quot;, a suffix will be added to the configured value. If not set, the module attempts to read the default used by libkrb5 from <code><a href="/docs/linux/man/5-krb5-conf/">krb5.conf</a></code>(5), and if one is not found, the default is <i>FILE:%d/krb5cc_%U_XXXXXX</i>&quot;. </p>
<dt>chpw_prompt</p>
<dd>tells pam_krb5.so to allow expired passwords to be changed during authentication attempts. While this is the traditional behavior exhibited by &quot;kinit&quot;, it is inconsistent with the behavior expected by PAM, which expects authentication to (appear to) succeed, only to have password expiration be flagged by a subsequent call to the account management function. Some applications which don&#8217;t handle password expiration correctly will fail unconditionally if the user&#8217;s password is expired, and this flag can be used to attempt to work around this bug in those applications. The default is <code>false</code>. </p>
<dt>cred_session</p>
<dd>specifies that pam_krb5 should create and destroy credential caches, as it does when the calling application opens and closes a PAM session, when the calling application establishes and deletes PAM credentials. This is done to compensate for applications which expect to create a credential cache but which don&#8217;t use PAM session management. It is usually a harmless redundancy in applications which don&#8217;t require it, so this option is enabled by default except for these services: &quot;<i>sshd</i>&quot;. </p>
<dt>external</p>
<dd>
<dt>external=<i>sshd</i></p>
<dd>tells pam_krb5.so to use Kerberos credentials provided by the calling application during session setup. This is most often useful for obtaining AFS tokens. </p>
<dt>ignore_afs=<i>true</i>|<i>false</i>|<i>service [&#8230;]</i></p>
<dd>tells pam_krb5.so to completely ignore the presence of AFS, preventing any attempts to obtain new tokens on behalf of the calling application. </p>
<dt>ignore_k5login</p>
<dd>specifies that pam_krb5 should skip checking the user&#8217;s .k5login file to verify that the principal name of the client being authenticated is authorized to access the user account. (Actually, the check is performed by a function offered by the Kerberos library, which controls which files it will consult.) The default is to perform the check. </p>
<dt>ignore_unknown_principals</p>
<dd>
<dt>ignore_unknown_spn</p>
<dd>
<dt>ignore_unknown_upn</p>
<dd>specifies that not pam_krb5 should return a PAM_IGNORE code to libpam instead of PAM_USER_UNKNOWN for users for whom the determined principal name is expired or does not exist. </p>
<dt>keytab=<i>FILE:/etc/krb5.keytab</i></p>
<dd>tells pam_krb5.so the location of a keytab to use when validating credentials obtained from KDCs. </p>
<dt>minimum_uid=<i>0</i></p>
<dd>tells pam_krb5.so to ignore authentication attempts by users with UIDs below the specified number. </p>
<dt>multiple_ccaches</p>
<dd>specifies that pam_krb5 should maintain multiple credential caches for this service, because it both sets credentials and opens a PAM session, but it sets the KRB5CCNAME variable after doing only one of the two. This option is usually not necessary for most services. </p>
<dt>no_initial_prompt</p>
<dd>tells pam_krb5.so to not ask for a password before attempting authentication, and to instead allow the Kerberos library to trigger a request for a password only in cases where one is needed. </p>
<dt>no_subsequent_prompt</p>
<dd>tells pam_krb5.so to only provide the previously-entered password in response to any request for a password which the Kerberos library might make. If the calling application does not properly support PAM conversations (possibly due to limitations of a network protocol which it is serving), this may be need to be used to prevent the application from supplying the user&#8217;s current password in a password-changing situations when a new password is called for. </p>
<dt>no_user_check</p>
<dd>tells pam_krb5.so to not check if a user exists on the local system, to skip authorization checks using the user&#8217;s .k5login file, and to create ccaches owned by the current process&#8217;s UID. This is useful for situations where a non-privileged server process needs to use Kerberized services on behalf of remote users who may not have local access. Note that such a server should have an encrypted connection with its client in order to avoid allowing the user&#8217;s password to be eavesdropped. </p>
<dt>no_validate</p>
<dd>
<dt>no_validate=<i>vlock</i></p>
<dd>tells pam_krb5.so to not attempt to use the local keytab to verify that the TGT obtained from the realm&#8217;s servers has not been spoofed. The <code>libdefaults</code> <code>verify_ap_req_nofail</code> setting can affect whether or not errors reading the keytab which are encountered during validation will be suppressed. </p>
<dt>null_afs</p>
<dd>tells pam_krb5.so, when it attempts to set tokens, to try to get credentials for services with names which resemble afs@<i>REALM</i> before attempting to get credentials for services with names resembling afs/<i>cell</i>@<i>REALM</i>. The default is to assume that the cell&#8217;s name is the instance in the AFS service&#8217;s Kerberos principal name. </p>
<dt>preauth_options=[]</p>
<dd>controls the preauthentication options which pam_krb5 passes to libkrb5, if the system-defaults need to be overridden. The list is treated as a template, and these sequences are substituted: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>%u<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>login name</p>
<p>&nbsp;<wbr>&nbsp;<wbr>%U<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>login UID</p>
<p>&nbsp;<wbr>&nbsp;<wbr>%p<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>principal name</p>
<p>&nbsp;<wbr>&nbsp;<wbr>%r<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>principal&#8217;s realm name</p>
<p>&nbsp;<wbr>&nbsp;<wbr>%h<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>home directory</p>
<p>&nbsp;<wbr>&nbsp;<wbr>%d<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>the default ccache directory</p>
<p>&nbsp;<wbr>&nbsp;<wbr>%P<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>the current process ID</p>
<p>&nbsp;<wbr>&nbsp;<wbr>%%<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>literal&nbsp;<wbr>&#8216;%&#8217;</p>
<p> A list of recognized values should be listed in the <a href="/docs/linux/man/1-kinit/">kinit</a>(1) manual page as parameters for its -X option. </p>
<dt>pwhelp=<i>filename</i></p>
<dd>specifies the name of a text file whose contents will be displayed to clients who attempt to change their passwords. There is no default. </p>
<dt>realm=<i>realm</i></p>
<dd>overrides the default realm set in <i>/etc/krb5.conf</i>, which pam_krb5.so will attempt to authenticate users to. </p>
<dt>tokens</p>
<dd>
<dt>tokens=<i>imap</i></p>
<dd>signals that pam_krb5.so should create a new AFS PAG and obtain AFS tokens during authentication in addition to session setup. This is primarily useful in server applications which need to access a user&#8217;s files but which do not open PAM sessions before doing so. A properly-written server will not need this flag set in order to function correctly. </p>
<dt>trace</p>
<dd>turns on libkrb5&#8217;s library tracing. Trace messages are logged to <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) with priority <i>LOG_DEBUG</i>. </p>
<dt>try_first_pass</p>
<dd>tells pam_krb5.so to check the previously-entered password as with <code>use_first_pass</code>, but to prompt the user for another one if the previously-entered one fails. This is the default mode of operation. </p>
<dt>use_first_pass</p>
<dd>tells pam_krb5.so to get the user&#8217;s entered password as it was stored by a module listed earlier in the stack, usually <code>pam_unix</code> or <code>pam_pwdb</code>, instead of prompting the user for it. </p>
<dt>use_authtok</p>
<dd>tells pam_krb5.so to never prompt for new passwords when changing passwords. This is useful if you are using <code>pam_cracklib</code> or <code>pam_passwdqc</code> to try to enforce use of less-easy-to-guess passwords. </p>
<dt>use_shmem</p>
<dd>
<dt>use_shmem=<i>sshd</i></p>
<dd>tells pam_krb5.so to pass credentials from the authentication service function to the session management service function using shared memory, or to do so for specific services. </p>
<dt>validate_user_user</p>
<dd>
<dt>validate_user_user=<i>gnome-screensaver</i></p>
<dd>specifies that, when attempting validation of the TGT, the module should attempt user-to-user authentication using a previously-obtainted TGT in the default ccache if validation can&#8217;t be performed using a keytab. </p>
</dl>
<h2>Files</h2>
<p><i>/etc/krb5.conf</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-pam_krb5/">pam_krb5</a></code>(5) <code><a href="/docs/linux/man/5-krb5-conf/">krb5.conf</a></code>(5) </p>
<h2>Bugs</h2>
<p>Probably, but let&#8217;s hope not. If you find any, please file them in the bug database at <a rel="nofollow" href="http://bugzilla.redhat.com/">http://bugzilla.redhat.com/</a> against the &quot;pam_krb5&quot; component. </p>
<h2>Author</h2>
<p>Nalin Dahyabhai &lt;nalin [at] redhat.com&gt;</p>
