---
title: "ipa-join(1)"
name: "ipa-join"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipa-join/"
description: "ipa-join – Join a machine to an IPA realm and get a keytab for the host service principal"
---

<h2>NAME</h2>
<p> ipa-join &#8211; Join a machine to an IPA realm and get a keytab for the host service principal</p>
<h2>SYNOPSIS</h2>
<p> ipa-join [<code>-d</code>|<code>&#8211;debug</code>] [<code>-q</code>|<code>&#8211;quiet</code>] [<code>-u</code>|<code>&#8211;unenroll</code>] [<code>-h</code>|<code>&#8211;hostname</code> hostname] [<code>-s</code>|<code>&#8211;server</code> hostname] [<code>-k</code>|<code>&#8211;keytab</code> filename] [<code>-w</code>|<code>&#8211;bindpw</code> password] [<code>-b</code>|&#8211;<code>basedn basedn</code>] [<code>-?</code>|<code>&#8211;help</code>] [<code>&#8211;usage</code>] </p>
<h2>DESCRIPTION</h2>
<p> Joins a host to an IPA realm and retrieves a kerberos <i>keytab</i> for the host service principal, or unenrolls an enrolled host from an IPA server. </p>
<p> Kerberos keytabs are used for services (like sshd) to perform kerberos authentication. A keytab is a file with one or more secrets (or keys) for a kerberos principal. </p>
<p> The ipa-join command will create and retrieve a service principal for host/foo.example.com [at] EXAMPLE.COM and place it by default into /etc/krb5.keytab. The location can be overridden with the -k option. </p>
<p> The IPA server to contact is set in /etc/ipa/default.conf by default and can be overridden using the -s,&#8211;server option. </p>
<p> In order to join the machine needs to be authenticated. This can happen in one of two ways: </p>
<p> * Authenticate using the current kerberos principal </p>
<p> * Provide a password to authenticate with </p>
<p> If a client host has already been joined to the IPA realm the ipa-join command will fail. The host will need to be removed from the server using `ipa host-del FQDN` in order to join the client to the realm. </p>
<p> This command is normally executed by the ipa-client-install command as part of the enrollment process. </p>
<p> The reverse is unenrollment. Unenrolling a host removes the Kerberos key on the IPA server. This prepares the host to be re-enrolled. This uses the host principal stored in /etc/krb5.conf to authenticate to the IPA server to perform the unenrollment. </p>
<p> Please note, that while the ipa-join option removes the client from the domain, it does not actually uninstall the client or properly remove all of the IPA-related configuration. The only way to uninstall a client completely is to use ipa-client-install &#8211;uninstall (see <code><a href="/docs/linux/man/1-ipa-client-install/">ipa-client-install</a></code>(1)). </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h,&#8211;hostname hostname</code></p>
<dd> The hostname of this server (FQDN). By default of nodename from <a href="/docs/linux/man/2-uname/">uname</a>(2) is used.</p>
<dt><code>-s,&#8211;server server</code></p>
<dd> The hostname of the IPA server (FQDN). Note that by default there is no /etc/ipa/default.conf, in most cases it needs to be supplied.</p>
<dt><code>-k,&#8211;keytab keytab-file</code></p>
<dd> The keytab file where to append the new key (will be created if it does not exist). Default: /etc/krb5.keytab</p>
<dt><code>-w,&#8211;bindpw password</code></p>
<dd> The password to use if not using Kerberos to authenticate. Use a password of this particular host (one time password created on IPA server)</p>
<dt><code>-b,&#8211;basedn basedn</code></p>
<dd> The basedn of the IPA server (of the form dc=example,dc=com). This is only needed when not using Kerberos to authenticate and anonymous binds are disallowed in the IPA LDAP server.</p>
<dt><code>-f,&#8211;force</code></p>
<dd> Force enrolling the host even if host entry exists.</p>
<dt><code>-u,&#8211;unenroll</code></p>
<dd> Unenroll this host from the IPA server. No keytab entry is removed in the process (see <code><a href="/docs/linux/man/1-ipa-rmkeytab/">ipa-rmkeytab</a></code>(1)).</p>
<dt><code>-q,&#8211;quiet</code></p>
<dd> Quiet mode. Only errors are displayed.</p>
<dt><code>-d,&#8211;debug</code></p>
<dd> Print the raw XML-RPC output in GSSAPI mode.</dl>
<h2>EXAMPLES</h2>
<p> Join IPA domain and retrieve a keytab with kerberos credentials. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>kinit admin<br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>ipa-join </p>
<p> Join IPA domain and retrieve a keytab using a one-time password. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>ipa-join -w secret123 </p>
<p> Join IPA domain and save the keytab in another location. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>ipa-join -k&nbsp;<wbr>/tmp/host.keytab</p>
<h2>EXIT STATUS</h2>
<p> The exit status is 0 on success, nonzero on error. </p>
<p> 0 Success </p>
<p> 1 Kerberos context initialization failed </p>
<p> 2 Incorrect usage </p>
<p> 3 Out of memory </p>
<p> 4 Invalid service principal name </p>
<p> 5 No Kerberos credentials cache </p>
<p> 6 No Kerberos principal and no bind DN and password </p>
<p> 7 Failed to open keytab </p>
<p> 8 Failed to create key material </p>
<p> 9 Setting keytab failed </p>
<p> 10 Bind password required when using a bind DN </p>
<p> 11 Failed to add key to keytab </p>
<p> 12 Failed to close keytab </p>
<p> 13 Host is already enrolled </p>
<p> 14 LDAP failure </p>
<p> 15 Incorrect bulk password </p>
<p> 16 Host name must be fully-qualified </p>
<p> 17 XML-RPC fault </p>
<p> 18 Principal not found in host entry </p>
<p> 19 Unable to generate Kerberos credentials cache </p>
<p> 20 Unenrollment result not in XML-RPC response </p>
<p> 21 Failed to get default Kerberos realm </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ipa-rmkeytab/">ipa-rmkeytab</a></code>(1) <code><a href="/docs/linux/man/1-ipa-client-install/">ipa-client-install</a></code>(1) </p>
<h2>Index</h2>
