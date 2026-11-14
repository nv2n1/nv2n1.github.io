---
title: "authconfig(8)"
name: "authconfig"
section: "8"
letter: "a"
url: "/docs/linux/man/8-authconfig/"
description: "authconfig, authconfig-tui – an interface for configuring system authentication resources"
---

<p>authconfig, authconfig-tui &#8211; an interface for configuring system authentication resources</p>
<h2>Synopsis</h2>
<p><code>authconfig</code> [options] {&#8211;update|&#8211;updateall|&#8211;test|&#8211;probe|&#8211;restorebackup &lt;name&gt;|&#8211;savebackup &lt;name&gt;|&#8211;restorelastbackup}</p>
<h2>Description</h2>
<p><code>authconfig</code> provides a simple method of configuring /etc/sysconfig/network to handle NIS, as well as /etc/passwd and /etc/shadow, the files used for shadow password support. Basic LDAP, Kerberos 5, and Winbind client configuration is also provided. </p>
<p> If <code>&#8211;test</code> action is specified, the <code>authconfig</code> just reads the current settings from the various configuration files and prints their values. If <code>&#8211;update</code> action is specified, <code>authconfig</code> must be run by root (or through console helper), and configuration changes are saved. Only the files affected by the configuration changes are overwritten. If <code>&#8211;updateall</code> action is specified, <code>authconfig</code> must be run by root (or through console helper), and all configuration files are written. The <code>&#8211;probe</code> action instructs <code>authconfig</code> to use DNS and other means to guess at configuration information for the current host, print its guesses if it finds them, to standard output, and exit. </p>
<p> The <code>&#8211;restorebackup</code>, <code>&#8211;savebackup</code>, and <code>&#8211;restorelastbackup</code> actions provide a possibility to save and later restore a backup of configuration files which authconfig modifies. Authconfig also saves an automatic backup of configuration files before every configuration change. This special backup can be restored by the <code>&#8211;restorelastbackup</code> action. </p>
<p> If <code>&#8211;nostart</code> is specified (which is what the install program does), ypbind or other daemons will not be started or stopped immediately following program execution, but only enabled to start or stop at boot time. </p>
<p> The <code>&#8211;enablenis</code>, <code>&#8211;enableldap</code>, <code>&#8211;enablewinbind</code>, and <code>&#8211;enablehesiod</code> options are used to configure user information services in <code>/etc/nsswitch.conf</code>, the <code>&#8211;enablecache</code> option is used to configure naming services caching, and the <code>&#8211;enableshadow</code>, <code>&#8211;enableldapauth</code>, <code>&#8211;enablekrb5</code>, and <code>&#8211;enablewinbindauth</code> options are used to configure authentication functions via <code>/etc/pam.d/system-auth</code>. Each <code>&#8211;enable</code> has a matching <code>&#8211;disable</code> option that disables the service if it is already enabled. The respective services have parameters which configure their server names etc. </p>
<p> The algorithm used for storing new password hashes can be specified by the <code>&#8211;passalgo</code> option which takes one of the following possible values as a parameter: <code>descrypt</code>, <code>bigcrypt</code>, <code>md5</code>, <code>sha256</code>, and <code>sha512</code>. </p>
<p> The <code>&#8211;enablelocauthorize</code> option allows to bypass checking network authentication services for authorization and the <code>&#8211;enablesysnetauth</code> allows authentication of system accounts (with uid &lt; 500) by these services. </p>
<p> When the configuration settings allow use of <i>SSSD</i> for user information services and authentication, <i>SSSD</i> will be automatically used instead of the legacy services and the <i>SSSD</i> configuration will be set up so there is a default domain populated with the settings required to connect the services. The <code>&#8211;enablesssd</code> and <code>&#8211;enablesssdauth</code> options force adding <i>SSSD</i> to <code>/etc/nsswitch.conf</code> and <code>/etc/pam.d/system-auth</code>, but they do not set up the domain in the <i>SSSD</i> configuration files. The <i>SSSD</i> configuration has to be set up manually. The allowed configuration of services for <i>SSSD</i> are: LDAP for user information (<code>&#8211;enableldap</code>) and either LDAP (<code>&#8211;enableldapauth</code>), or Kerberos (<code>&#8211;enablekrb5</code>) for authentication. Please note that even though these options alone do not trigger any change in SSSD configuration files this may not be true if any of these options is used in conjunction with other options such as <code>&#8211;enableldap</code> or <code>&#8211;updateall</code>. </p>
<p> In case <i>SSSD</i> does not support some feature of the legacy services that are required for the site configuration, the use of the legacy services can be forced by setting FORCELEGACY=yes in <code>/etc/sysconfig/authconfig</code>. </p>
<p> The list of options mentioned here in the manual page is not exhaustive, please refer to <code>authconfig &#8211;help</code> for the complete list of the options. </p>
<p> The <code>authconfig-tui</code> supports all options of authconfig but it implies <code>&#8211;update</code> as the default action. Its window contains a <code>Cancel</code> button by default. If <code>&#8211;back</code> option is specified at run time, a <code>Back</code> button is presented instead. If <code>&#8211;kickstart</code> is specified, no interactive screens will be seen. The values the program will use will be those specified by the other options (<code>&#8211;passalgo</code>, <code>&#8211;enableshadow</code>, etc.). </p>
<p> For <i>namelist</i> you may substitute either a single name or a comma-separated list of names.</p>
<h2>Notes</h2>
<p>The <code>authconfig-tui</code> is deprecated. No new configuration settings will be supported by its text user interface. Use <code>system-config-authentication</code> GUI application or the command line options instead. </p>
<p> The <code>/usr/bin/authconfig</code> uses the <code>consolehelper</code> to authenticate as the system user before it starts up. If you want to run it directly without the authentication as the system user, run the <code>/usr/sbin/authconfig</code> command. </p>
<p> The SSSD service is enabled and possibly started by authconfig when at least two of the following three conditions are met:<br />
 1) /etc/sssd/sssd.conf file exists (or is configured via the implicit SSSD support)<br />
 2) SSSD authentication is enabled (pam_sss.so is used in PAM configuration)<br />
 3) SSSD is enabled for user identity (nsswitch.conf contains sss) </p>
<p> When <code>&#8211;update</code> action is used the enablement or disablement and possible restart of services happens only in case the changed configuration options affect the service to be restarted. This means that if for example the ypbind service is enabled with <code>authconfig &#8211;update &#8211;nostart &#8211;enablenis</code> but not started and you run the same command without the <code>&#8211;nostart</code> later the ypbind service will not be started because no configuration change affecting ypbind happened.</p>
<h2>Return Codes</h2>
<p><code>authconfig</code> returns 0 on success, 1 on backup operation errors, 2 if not running with sufficient privileges, 3 if unknown password hash algorithm is specified or incorrect values are set for password strength checking (this error is non fatal), 4 if download of CA certificate fails, 5 if writing configuration files fails on <code>&#8211;updateall</code> action, 6 if writing fails on <code>&#8211;update</code> action, 7 if Winbind or IPA domain join fails. </p>
<p> <code>authconfig-tui</code> returns 0 on success, 2 on error, and 1 if the user cancelled the program (by using either the <code>Cancel</code> or <code>Back</code> button). It can also return the same codes as <code>authconfig</code>.</p>
<h2>Files</h2>
<dl>
<dt>
<dt> <i>/etc/sysconfig/authconfig</i></p>
<dd>
<dd>Used to track whether or not particular authentication mechanisms are enabled. Currently includes variables named USESHADOW, USEMD5, USEKERBEROS, USELDAPAUTH, USESMBAUTH, USEWINBIND, USEWINBINDAUTH, USEHESIOD, USENIS, USELDAP, and others.</p>
<dt> <i>/etc/passwd</i></p>
<dd>
<dt> <i>/etc/shadow</i></p>
<dd>Used for shadow password support.</p>
<dt> <i>/etc/yp.conf</i></p>
<dd>Configuration file for NIS support.</p>
<dt> <i>/etc/sysconfig/network</i></p>
<dd>Another configuration file for NIS support.</p>
<dt> <i>/etc/ldap.conf</i></p>
<dd>
<dt> <i>/etc/nss_ldap.conf</i></p>
<dd>
<dt> <i>/etc/pam_ldap.conf</i></p>
<dd>
<dt> <i>/etc/nslcd.conf</i></p>
<dd>
<dt> <i>/etc/openldap/ldap.conf</i></p>
<dd>Used to configure nss_ldap, pam_ldap, nslcd, and the OpenLDAP library. Only the files already existing on the system are modified.</p>
<dt> <i>/etc/krb5.conf</i></p>
<dd>Used to configure Kerberos 5.</p>
<dt> <i>/etc/hesiod.conf</i></p>
<dd>Used to configure Hesiod.</p>
<dt> <i>/etc/samba/smb.conf</i></p>
<dd>Used to configure winbind authentication.</p>
<dt> <i>/etc/nsswitch.conf</i></p>
<dd>Used to configure user information services.</p>
<dt> <i>/etc/login.defs</i></p>
<dd>Used to configure parameters of user accounts (minimum UID of a regular user, password hashing algorithm).</p>
<dt> <i>/etc/pam.d/system-auth</i></p>
<dd>Common PAM configuration for system services which include it using the <code>include</code> directive. It is created as symlink and not relinked if it points to another file.</p>
<dt> <i>/etc/pam.d/system-auth-ac</i></p>
<dd>Contains the actual PAM configuration for system services and is the default target of the <code>/etc/pam.d/system-auth</code> symlink. If a local configuration of PAM is created (and symlinked from <code>system-auth</code> file) this file can be <code>include</code>d there. </p>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-authconfig-gtk/">authconfig-gtk</a>(8), <a href="/docs/linux/man/5-system-auth-ac/">system-auth-ac</a>(5), <a href="/docs/linux/man/5-passwd/">passwd</a>(5), <a href="/docs/linux/man/5-shadow/">shadow</a>(5), <a href="/docs/linux/man/1-pwconv/">pwconv</a>(1), <a href="/docs/linux/man/1-domainname/">domainname</a>(1), <a href="/docs/linux/man/8-ypbind/">ypbind</a>(8), <a href="/docs/linux/man/5-nsswitch-conf/">nsswitch.conf</a>(5), <a href="/docs/linux/man/5-smb-conf/">smb.conf</a>(5), <a href="/docs/linux/man/8-sssd/">sssd</a>(8) </p>
<h2>Authors</h2>
<pre>Nalin Dahyabhai &lt;nalin [at] redhat.com&gt;, Preston Brown &lt;pbrown [at] redhat.com&gt;,
Matt Wilson &lt;msw [at] redhat.com&gt;, Tomas Mraz &lt;tmraz [at] redhat.com&gt;</pre>
