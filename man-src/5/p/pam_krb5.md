---
title: "pam_krb5(5)"
name: "pam_krb5"
section: "5"
letter: "p"
url: "/docs/linux/man/5-pam_krb5/"
description: "pam_krb5 – Kerberos 5 authentication"
---

<p>pam_krb5 &#8211; Kerberos 5 authentication</p>
<h2>Description</h2>
<p>pam_krb5.so reads its configuration information from the <code>appdefaults</code> section of <code><a href="/docs/linux/man/5-krb5-conf/">krb5.conf</a></code>(5). You should read the <code><a href="/docs/linux/man/5-krb5-conf/">krb5.conf</a></code>(5) man page before continuing here. The module expects its configuration information to be in the <code>pam</code> subsection of the <code>appdefaults</code> section. </p>
<h2>Directives</h2>
<p>Directives which take a <i>true</i>, <i>false</i>, or a PAM service name can also be selectively disabled for specific PAM services using the related &quot;no_&quot; option (exceptions to &quot;debug = true&quot; can be made using &quot;no_debug&quot;, for example). </p>
<dl>
<dt>debug = <i>true</i>|<i>false</i>|<i>service [&#8230;]</i></p>
<dd>turns on debugging via <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3). Debug messages are logged with priority <i>LOG_DEBUG</i>. </p>
<dt>debug_sensitive = <i>true</i>|<i>false</i>|<i>service [&#8230;]</i></p>
<dd>turns on debugging of sensitive information via <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3). Debug messages are logged with priority <i>LOG_DEBUG</i>. </p>
<dt>afs_cells = <i>cell.example.com [&#8230;]</i></p>
<dd>tells pam_krb5.so to obtain tokens for the listed cells, in addition to the local cell and the cell which contains the user&#8217;s home directory, for the user. The module will guess the principal name of the AFS service for the listed cells, or it can be specified by listing cells in the form <i>cellname</i><code>=principalname</code>. </p>
<dt>always_allow_localname = <i>true</i>|<i>false</i>|<i>service [&#8230;]</i></p>
<dd>tells pam_krb5.so, when performing an authorization check using the target user&#8217;s .k5login file, to always allow access when the principal name being authenticated maps to the local user&#8217;s name (as configured using the <i>auth_to_local_names</i> and <i>auth_to_local</i> settings in <code><a href="/docs/linux/man/5-krb5-conf/">krb5.conf</a></code>(5), if your implementation provides those settings). Otherwise, if the file exists and can be read, but the principal is not explicitly listed, access is typically denied. This setting is disabled by default. </p>
<dt>armor = <i>true</i>|<i>false</i>|<i>service [&#8230;]</i></p>
<dd>attempt to use armoring when communicating with the KDC. This option is currently mainly only useful for testing, as the <i>keytab</i> method should not be expected to work when the module is called from an unprivileged process, and the <i>pkinit</i> method requires that the KDC is properly configured to offer anonymous PKINIT, and that the client is also properly configured to trust the KDC&#8217;s CA. The default is <code>false</code>. </p>
<dt>armor_strategy = <i>keytab,pkinit</i></p>
<dd>controls how the module will attempt to obtain tickets for use as armor. The value should be a comma-separated list of methods. Supported methods include <i>ketyab</i> and <i>pkinit</i>. The default is <code>keytab,pkinit</code>. </p>
<dt>banner = <i>Kerberos 5</i></p>
<dd>specifies what sort of password the module claims to be changing whenever it is called upon to change passwords. The default is <code>Kerberos 5</code>. </p>
<dt>ccache_dir = <i>/var/tmp</i></p>
<dd>specifies the directory in which to place credential cache files. The default is <i>/tmp</i>. </p>
<dt>ccname_template = <i>KEYRING:krb5cc_%U_%P</i></p>
<dd>
<dt>ccname_template = <i>FILE:%d/krb5cc_%U_XXXXXX</i></p>
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
<dt>chpw_prompt = <i>true</i>|<i>false</i>|<i>service [&#8230;]</i></p>
<dd>tells pam_krb5.so to allow expired passwords to be changed during authentication attempts. While this is the traditional behavior exhibited by &quot;kinit&quot;, it is inconsistent with the behavior expected by PAM, which expects authentication to (appear to) succeed, only to have password expiration be flagged by a subsequent call to the account management function. Some applications which don&#8217;t handle password expiration correctly will fail unconditionally if the user&#8217;s password is expired, and this flag can be used to attempt to work around this bug in those applications. The default is <code>false</code>. </p>
<dt>cred_session=<i>true</i>|<i>false</i>|<i>service [&#8230;]</i></p>
<dd>specifies that pam_krb5 should create and destroy credential caches, as it does when the calling application opens and closes a PAM session, when the calling application establishes and deletes PAM credentials. This is done to compensate for applications which expect to create a credential cache but which don&#8217;t use PAM session management. It is usually a harmless redundancy in applications which don&#8217;t require it, so this option is enabled by default except for this list of services: &quot;<i>sshd</i>&quot;. </p>
<dt>external = <i>true</i>|<i>false</i>|<i>sshd ftp [&#8230;]</i></p>
<dd>tells pam_krb5.so to use Kerberos credentials provided by the calling application during session setup. This is most often useful for obtaining AFS tokens. The default is &quot;<i>sshd sshd-rekey gssftp</i>&quot;. </p>
<dt>ignore_afs=<i>true</i>|<i>false</i>|<i>service [&#8230;]</i></p>
<dd>tells pam_krb5.so to completely ignore the presence of AFS, preventing any attempts to obtain new tokens on behalf of the calling application. </p>
<dt>ignore_k5login=<i>true</i>|<i>false</i>|<i>service [&#8230;]</i></p>
<dd>specifies which other not pam_krb5 should skip checking the user&#8217;s .k5login file to verify that the principal name of the client being authenticated is authorized to access the user account. (Actually, the check is performed by a function offered by the Kerberos library, which controls which files it will consult.) The default is <i>false</i>, which causes pam_krb5 to perform the check. </p>
<dt>ignore_unknown_principals=<i>true</i>|<i>false</i>|<i>service [&#8230;]</i></p>
<dd>
<dt>ignore_unknown_spn=<i>true</i>|<i>false</i>|<i>service [&#8230;]</i></p>
<dd>
<dt>ignore_unknown_upn=<i>true</i>|<i>false</i>|<i>service [&#8230;]</i></p>
<dd>specifies which other not pam_krb5 should return a PAM_IGNORE code to libpam instead of PAM_USER_UNKNOWN for users for whom the determined principal name is expired or does not exist. </p>
<dt>initial_prompt=<i>true</i>|<i>false</i>|<i>service [&#8230;]</i></p>
<dd>tells pam_krb5.so whether or not to ask for a password before attempting authentication. If one is needed and pam_krb5.so has not prompted for it, the Kerberos library should trigger a request for a password. </p>
<dt>keytab = <i>FILE:/etc/krb5.keytab</i></p>
<dd>
<dt>keytab = <i>FILE:/etc/krb5.keytab imap=FILE:/etc/imap.keytab</i></p>
<dd>specifies the name of a keytab file to search for a service key for use in validating TGTs. The location can be specified on a per-service basis by specifying a list of locations in the form <i>pam_service</i>=<i>location</i>. The default is <i>FILE:/etc/krb5.keytab</i>. </p>
<dt>mappings = <i>regex1 regex2 [&#8230;]</i></p>
<dd>specifies that pam_krb5 should derive the user&#8217;s principal name from the Unix user name by first checking if the user name matches <code>regex1</code>, and formulating a principal name using <code>regex2</code>. For example, <code>&quot;mappings = ^EXAMPLE\(.*)$ $1@EXAMPLE.COM</code>&quot; would map any user with a name of the form &quot;EXAMPLE\whatever&quot; to a principal name of &quot;whatever [at] EXAMPLE.COM&quot;. This is primarily targeted at allowing pam_krb5 to be used to authenticate users whose user information is provided by <code><a href="/docs/linux/man/8-winbindd/">winbindd</a></code>(8). This will frequently require the reverse to be configured by setting up an auth_to_local rule elsewhere in <code><a href="/docs/linux/man/5-krb5-conf/">krb5.conf</a></code>(5). </p>
<dt>minimum_uid = <i>0</i></p>
<dd>specifies the minimum UID of users being authenticated. If a user with a UID less than this value attempts authentication, the request will be ignored. </p>
<dt>multiple_ccaches=<i>true</i>|<i>false</i>|<i>service [&#8230;]</i></p>
<dd>specifies that pam_krb5 should maintain multiple credential caches for applications that both set credentials and open a PAM session, but which set the KRB5CCNAME variable after doing only one of the two. This option is usually not necessary for most services. </p>
<dt>preauth_options = <i></i></p>
<dd>controls the preauthentication options which pam_krb5 passes to libkrb5, if the system-defaults need to be overridden. The list is treated as a template, and these sequences are substituted: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>%u<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>login name</p>
<p>&nbsp;<wbr>&nbsp;<wbr>%U<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>login UID</p>
<p>&nbsp;<wbr>&nbsp;<wbr>%p<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>principal name</p>
<p>&nbsp;<wbr>&nbsp;<wbr>%r<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>principal&#8217;s realm name</p>
<p>&nbsp;<wbr>&nbsp;<wbr>%h<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>home directory</p>
<p>&nbsp;<wbr>&nbsp;<wbr>%d<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>the default ccache directory&nbsp;<wbr>(as set with&nbsp;<wbr><i>ccache_dir</i>)</p>
<p>&nbsp;<wbr>&nbsp;<wbr>%P<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>the current process ID</p>
<p>&nbsp;<wbr>&nbsp;<wbr>%%<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>literal&nbsp;<wbr>&#8216;%&#8217;</p>
<p> A list of recognized values should be listed in the <a href="/docs/linux/man/1-kinit/">kinit</a>(1) manual page as parameters for its -X option. </p>
<dt>null_afs=<i>true</i>|<i>false</i>|<i>service [&#8230;]</i></p>
<dd>tells pam_krb5.so, when it attempts to set tokens, to try to get credentials for services with names which resemble afs@<i>REALM</i> before attempting to get credentials for services with names resembling afs/<i>cell</i>@<i>REALM</i>. The default is to assume that the cell&#8217;s name is the instance in the AFS service&#8217;s Kerberos principal name. </p>
<dt>pwhelp = <i>filename</i></p>
<dd>specifies the name of a text file whose contents will be displayed to clients who attempt to change their passwords. There is no default. </p>
<dt>subsequent_prompt = <i>true</i>|<i>false</i>|<i>service&nbsp;<wbr>[&#8230;]</i></p>
<dd>controls whether or not pam_krb5.so will allow the Kerberos library to ask the user for a password or other information, if the previously-entered password is somehow insufficient for authenticating the user. This is commonly needed to allow a user to log in when that user&#8217;s password has expired. The default is <code>false</code> during password changes, and <code>true</code> otherwise. </p>
<p> If the calling application does not properly support PAM conversations (possibly due to limitations of a network protocol which it is serving), this may be need to be disabled for that application to prevent it from supplying the user&#8217;s current password in a password-changing situation when a new password is called for. </p>
<dt>tokens = <i>true</i>|<i>false</i>|<i>service&nbsp;<wbr>[&#8230;]</i></p>
<dd>signals that pam_krb5.so should create an AFS PAG and obtain tokens during authentication in addition to session setup. This is primarily useful in server applications which need to access a user&#8217;s files but which do not open PAM sessions before doing so. For correctly-written applications, this flag is not necessary. </p>
<dt>token_strategy = <i>rxk5,2b[,&#8230;]</i></p>
<dd>controls how, and using which format, pam_krb5.so should attempt to set AFS tokens for the user&#8217;s session. By default, the module is configured with &quot;token_strategy = <i>2b</i>&quot;. Recognized strategy names include:<br />
&nbsp;<wbr><i>rxk5</i>&nbsp;<wbr>&nbsp;<wbr>rxk5&nbsp;<wbr>(requires OpenAFS 1.6 or later)<br />
&nbsp;<wbr><i>2b</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rxkad&nbsp;<wbr>&quot;2b&quot;&nbsp;<wbr>(requires OpenAFS 1.2.8 or later) </p>
<dt>trace = <i>true</i>|<i>false</i>|<i>service [&#8230;]</i></p>
<dd>turns on libkrb5&#8217;s library tracing. Trace messages are logged to <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) with priority <i>LOG_DEBUG</i>. </p>
<dt>use_shmem = <i>true</i>|<i>false</i>|<i>service&nbsp;<wbr>[&#8230;]</i></p>
<dd>tells pam_krb5.so to pass credentials from the authentication service function to the session management service function using shared memory for specific services. By default, the module is configured with &quot;use_shmem = <i>sshd</i>&quot;. </p>
<dt>validate = <i>true</i>|<i>false</i>|<i>service&nbsp;<wbr>[&#8230;]</i></p>
<dd>specifies whether or not to attempt validation of the TGT using the local keytab. The default is <code>true</code>. The <code>libdefaults</code> <code>verify_ap_req_nofail</code> setting can affect whether or not errors reading the keytab which are encountered during validation will be suppressed. </p>
<dt>validate_user_user = <i>true</i>|<i>false</i>|<i>service&nbsp;<wbr>[&#8230;]</i></p>
<dd>specifies whether or not, when attempting validation of the TGT, to attempt user-to-user authentication using a previously-obtainted TGT in the default ccache if validation can&#8217;t be performed using a keytab. The default is <code>false</code>. </p>
</dl>
<h2>Example</h2>
<pre><code>[appdefaults]
pam = {

    validate = true

    ccache_dir = /var/tmp

    external = sshd

    tokens = imap ftpd

    TEST.EXAMPLE.COM = {

        debug = true

        afs_cells = testcell.example.com othercell.example.com

        keytab = FILE:/etc/krb5.keytab httpd=FILE:/etc/httpd.keytab

    }
}
</code></pre>
<h2>Files</h2>
<p><i>/etc/krb5.conf</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-pam_krb5/">pam_krb5</a></code>(8)</p>
<h2>Bugs</h2>
<p>Probably, but let&#8217;s hope not. If you find any, please file them in the bug database at <a rel="nofollow" href="http://bugzilla.redhat.com/">http://bugzilla.redhat.com/</a> against the &quot;pam_krb5&quot; component. </p>
<h2>Author</h2>
<p>Nalin Dahyabhai &lt;nalin [at] redhat.com&gt;</p>
