---
title: "realmd(5)"
name: "realmd"
section: "5"
letter: "r"
url: "/docs/linux/man/5-realmd/"
description: "realmd.conf – Tweak behavior of realmd"
---

<p>realmd.conf &#8211; Tweak behavior of realmd</p>
<h2>Configuration File</h2>
<p><code>realmd</code> can be tweaked by network administrators to act in specific ways. This is done by placing settings in a /etc/realmd.conf. This file does not exist by default. The syntax of this file is the same as an INI file or Desktop Entry file. </p>
<p> In general, settings in this file only apply at the point of joining a domain or realm. Once the realm has been setup the settings have no effect. You may choose to configure m[blue]<code>SSSD</code>m[]<font SIZE="-2">[1]</font> or m[blue]<code>Winbind</code>m[]<font SIZE="-2">[2]</font> directly. </p>
<p> Only specify the settings you wish to override in the /etc/realmd.conf file. Settings not specified will be loaded from their packaged defaults. Only override the settings below. You may find other settings if you look through the <code>realmd</code> source code. However these are not guaranteed to remain stable. </p>
<p> There are various sections in the config file. Some sections are global topic sections, and are listed below. Other sections are specific to a given realm. These realm specific sections should always contain the domain name in lower case as their section header. </p>
<p> Examples of each setting is found below, including the header of the section it should be placed in. However in the resulting file only include each section once, and combine the various section setting together as lines underneath the section. For example </p>
<dl>
<dd>
<pre>[users]
default-home = /home/%U
default-shell = /bin/bash</pre>
</dl>
<h2>Active-Directory</h2>
<p>These options should go in an <code>[active-directory]</code> section of the /etc/realmd.conf file. Only specify the settings you wish to override. </p>
<p> <code>default-client</code></p>
<dl>
<dd>Specify the <code>default-client</code> setting in order to control which client software is the preferred default for use with Active Directory. </p>
<dl>
<dd>
<pre>[active-directory]
default-client = sssd
# default-client = winbind</pre>
</dl>
<p> The default setting for this is <code>sssd</code> which uses m[blue]<code>SSSD</code>m[]<font SIZE="-2">[1]</font> as the Active Directory client. You can also specify <code>winbind</code> to use m[blue]<code>Samba Winbind</code>m[]<font SIZE="-2">[2]</font>. </p>
<p> Some callers of <code>realmd</code> such as the <code>realm</code> command line tool allow specifying which client software should be used. Others, such as GNOME Control Center, simplify choose the default. </p>
<p> You can verify the preferred default client softawre by running the following command. The realm with the preferred client software will be listed first. </p>
<dl>
<dd>
<pre>$ <code>realm discover domain.example.com</code>
domain.example.com
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
 domain-name: ad.thewalter.lan</pre>
</dl>
</dl>
<p> <code>os-name</code></p>
<dl>
<dd>(see below)</dl>
<p> <code>os-version</code></p>
<dl>
<dd>Specify the <code>os-name</code> and/or <code>os-version</code> settings to control the values that are placed in the computer account <code>operatingSystem</code> and <code>operatingSystemVersion</code> attributes. </p>
<p> This is an Active Directory specific option. </p>
<dl>
<dd>
<pre>[active-directory]
os-name = Gentoo Linux
os-version = 9.9.9.9.9</pre>
</dl>
</dl>
<h2>Service</h2>
<p>These options should go in an <code>[service]</code> section of the /etc/realmd.conf file. Only specify the settings you wish to override. </p>
<p> <code>automatic-install</code></p>
<dl>
<dd>Set this to <i>no</i> to disable automatic installation of packages via package-kit. </p>
<dl>
<dd>
<pre>[service]
automatic-install = no
# automatic-install = yes</pre>
</dl>
</dl>
<h2>Users</h2>
<p>These options should go in an <code>[users]</code> section of the /etc/realmd.conf file. Only specify the settings you wish to override. </p>
<p> <code>default-home</code></p>
<dl>
<dd>Specify the <code>default-home</code> setting in order to control how to set the home directory for accounts that have no home directory explicitly set. </p>
<dl>
<dd>
<pre>[users]
default-home = /home/%D/%U
# default-home = /nfs/home/%D-%U</pre>
</dl>
<p> The default setting for this is <code>/home/%D/%U</code>. The <code>%D</code> format is replaced by the domain name. The <code>%U</code> format is replaced by the user name. </p>
<p> You can verify the home directory for a user by running the following command. </p>
<dl>
<dd>
<pre>$ <code>getent passwd 'DOMAIN/User'</code>
DOMAIN
