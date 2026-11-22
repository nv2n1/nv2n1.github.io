---
title: "realmd(5)"
name: "realmd"
section: "5"
letter: "r"
url: "/docs/linux/man/5-realmd/"
description: "realmd.conf – Tweak behavior of realmd"
---
<p>realmd.conf &#8211; Tweak behavior of realmd </p>
<h2>CONFIGURATION FILE</h2>
<p> <code>realmd</code> can be tweaked by network administrators to act in specific ways. This is done by placing settings in a /etc/realmd.conf. This file does not exist by default. The syntax of this file is the same as an INI file or Desktop Entry file. </p>
<p>In general, settings in this file only apply at the point of joining a domain or realm. Once the realm has been setup the settings have no effect. You may choose to configure m[blue]<code>SSSD</code>m[][1] or m[blue]<code>Winbind</code>m[][2] directly. </p>
<p>Only specify the settings you wish to override in the /etc/realmd.conf file. Settings not specified will be loaded from their packaged defaults. Only override the settings below. You may find other settings if you look through the <code>realmd</code> source code. However these are not guaranteed to remain stable. </p>
<p>There are various sections in the config file. Some sections are global topic sections, and are listed below. Other sections are specific to a given realm. These realm specific sections should always contain the domain name in lower case as their section header. </p>
<p>Examples of each setting is found below, including the header of the section it should be placed in. However in the resulting file only include each section once, and combine the various section setting together as lines underneath the section. For example </p>
<dl>
<dd> <pre><code>[users]
default-home = /home/%U
default-shell = /bin/bash
</code></pre>
 </dd></dl>
<h2>ACTIVE-DIRECTORY</h2>
<p>These options should go in an <code>[active-directory]</code> section of the /etc/realmd.conf file. Only specify the settings you wish to override. </p>
<p> <code>default-client</code> </p>
<dl>
<dd> <p> Specify the <code>default-client</code> setting in order to control which client software is the preferred default for use with Active Directory. </p>
 </dd>
<dl>
<dd> <pre><code>[active-directory]
default-client = sssd
# default-client = winbind
</code></pre>
 </dd></dl>
<p> The default setting for this is <code>sssd</code> which uses m[blue]<code>SSSD</code>m[][1] as the Active Directory client. You can also specify <code>winbind</code> to use m[blue]<code>Samba Winbind</code>m[][2]. </p>
<p>Some callers of <code>realmd</code> such as the <code>realm</code> command line tool allow specifying which client software should be used. Others, such as GNOME Control Center, simplify choose the default. </p>
<p>You can verify the preferred default client softawre by running the following command. The realm with the preferred client software will be listed first. </p>
<dl>
<dd> <pre><code>$ realm discover domain.example.com domain.example.com
  configured: no
  server-software: active-directory
  client-software: sssd
  type: kerberos
  realm-name: AD.THEWALTER.LAN
  domain-name: ad.thewalter.lan
domain.example.com
  configured: no
  server-software: active-directory
  client-software: winbind
  type: kerberos
  realm-name: AD.THEWALTER.LAN
  domain-name: ad.thewalter.lan
</code></pre>
 </dd></dl>
</dl>
<p> <code>os-name</code> </p>
<dl>
<dd> <p> (see below) </p>
 </dd></dl>
<p> <code>os-version</code> </p>
<dl>
<dd> <p> Specify the <code>os-name</code> and/or <code>os-version</code> settings to control the values that are placed in the computer account <code>operatingSystem</code> and <code>operatingSystemVersion</code> attributes. </p>
<p>This is an Active Directory specific option. </p>
 </dd>
<dl>
<dd> <pre><code>[active-directory]
os-name = Gentoo Linux
os-version = 9.9.9.9.9
</code></pre>
 </dd></dl>
</dl>
<h2>SERVICE</h2>
<p>These options should go in an <code>[service]</code> section of the /etc/realmd.conf file. Only specify the settings you wish to override. </p>
<p> <code>automatic-install</code> </p>
<dl>
<dd> <p> Set this to <i>no</i> to disable automatic installation of packages via package-kit. </p>
 </dd>
<dl>
<dd> <pre><code>[service]
automatic-install = no
# automatic-install = yes
</code></pre>
 </dd></dl>
</dl>
<h2>USERS</h2>
<p>These options should go in an <code>[users]</code> section of the /etc/realmd.conf file. Only specify the settings you wish to override. </p>
<p> <code>default-home</code> </p>
<dl>
<dd> <p> Specify the <code>default-home</code> setting in order to control how to set the home directory for accounts that have no home directory explicitly set. </p>
 </dd>
<dl>
<dd> <pre><code>[users]
default-home = /home/%D/%U
# default-home = /nfs/home/%D-%U
</code></pre>
 </dd></dl>
<p> The default setting for this is <code>/home/%D/%U</code>. The <code>%D</code> format is replaced by the domain name. The <code>%U</code> format is replaced by the user name. </p>
<p>You can verify the home directory for a user by running the following command. </p>
<dl>
<dd> <pre><code>$ getent passwd 'DOMAIN/User' DOMAIN\user:*:13445:13446:Name:/home/DOMAIN/user:/bin/bash
</code></pre>
 </dd></dl>
<p> Note that in the case of IPA domains, most users already have a home directory configured in the domain. Therefore this configuration setting may rarely show through. </dl>
 </p>
<p> <code>default-shell</code> </p>
<dl>
<dd> <p> Specify the <code>default-shell</code> setting in order to control how to set the Unix shell for accounts that have no shell explicitly set. </p>
 </dd>
<dl>
<dd> <pre><code>[users]
default-shell = /bin/bash
# default-shell = /bin/sh
</code></pre>
 </dd></dl>
<p> The default setting for this is <code>/bin/bash</code> shell. The shell should be a valid shell if you expect the domain users be able to log in. For example it should exist in the /etc/shells file. </p>
<p>You can verify the shell for a user by running the following command. </p>
<dl>
<dd> <pre><code>$ getent passwd 'DOMAIN/User' DOMAIN\user:*:13445:13446:Name:/home/DOMAIN/user:/bin/bash
</code></pre>
 </dd></dl>
<p> Note that in the case of IPA domains, most users already have a shell configured in the domain. Therefore this configuration setting may rarely show through. </dl>
  </p>
<h2>REALM SPECIFIC SETTINGS</h2>
<p>These options should go in an section with the same name as the realm in the /etc/realmd.conf file. For example for the <code>domain.example.com</code> domain the section would be called <code>[domain.example.com]</code>. To figure out the canonical name for a realm use the <code>realm</code> command: </p>
<dl>
<dd> <pre><code>$ realm discover --name DOMAIN.example.com domain.example.com
...
</code></pre>
 </dd></dl>
<p>Only specify the settings you wish to override. </p>
<p> <code>computer-ou</code> </p>
<dl>
<dd> <p> Specify this option to create directory computer accounts in a location other than the default. This currently only works with Active Directory domains. </p>
 </dd>
<dl>
<dd> <pre><code>[domain.example.com]
computer-ou = OU=Linux Computers,DC=domain,DC=example,DC=com
# computer-ou = OU=Linux Computers,
</code></pre>
 </dd></dl>
<p> Specify the OU as an LDAP DN. It can be relative to the Root DSE, or a complete LDAP DN. Obviously the OU must exist in the directory. </p>
<p>It is also possible to use the <code>--computer-ou</code> argument of the <code>realm</code> command to create a computer account at a specific OU. </dl>
 </p>
<p> <code>user-prinicpal</code> </p>
<dl>
<dd> <p> Set the <code>user-prinicpal</code> to yes to create <code>userPrincipalName</code> attributes for the computer account in the realm, in the form host/computer [at] REALM </p>
 </dd>
<dl>
<dd> <pre><code>[domain.example.com]
user-principal = yes
</code></pre>
 </dd></dl>
</dl>
<p> <code>automatic-id-mapping</code> </p>
<dl>
<dd> <p> This option is on by default for Active Directory realms. Turn it off to use UID and GID information stored in the directory (as-per RFC2307) rather than automatically generating UID and GID numbers. </p>
<p>This option only makes sense for Active Directory realms. </p>
 </dd>
<dl>
<dd> <pre><code>[domain.example.com]
automatic-id-mapping = no
# automatic-id-mapping = yes
</code></pre>
 </dd></dl>
</dl>
<p> <code>manage-system</code> </p>
<dl>
<dd> <p> This option is on by default. Normally joining a realm affects many aspects of the configuration and management of the system. Turning this off limits the interaction with the realm or domain to authentication and identity. </p>
 </dd>
<dl>
<dd> <pre><code>[domain.example.com]
manage-system = no
# manage-system = yes
</code></pre>
 </dd></dl>
<p> When this option is turned on <code>realmd</code> defaults to using domain policy to control who can log into this machine. Further adjustments to login policy can be made with the <code>realm permit</code> command. </dl>
 </p>
<p> <code>fully-qualified-names</code> </p>
<dl>
<dd> <p> This option is on by default. If turned off then realm user and group names are not qualified their name. This may cause them to conflict with local user and group names. </p>
 </dd>
<dl>
<dd> <pre><code>[domain.example.com]
fully-qualified-names = no
# fully-qualified-names = yes
</code></pre>
 </dd></dl>
</dl>
<h2>AUTHOR</h2>
<p> <code>Stef Walter</code> &lt;stef [at] thewalter.net&gt; </p>
<dl>
<dd> <p> Maintainer </p>
 </dd></dl>
<h2>NOTES</h2>
<dl>
<dt> 1.</dt>
<dd> <p> SSSD </p>
 </dd>
<dl>
<dd> <p> <a rel="nofollow" href="https://fedorahosted.org/sssd/">https://fedorahosted.org/sssd/</a> </p>
 </dd></dl>
<dt> 2.</dt>
<dd> <p> Winbind </p>
 </dd>
<dl>
<dd> <p> <a rel="nofollow" href="http://www.samba.org/samba/docs/man/Samba-HOWTO-Collection/winbind.html">http://www.samba.org/samba/docs/man/Samba-HOWTO-Collection/winbind.html</a> </p>
 </dd></dl>
