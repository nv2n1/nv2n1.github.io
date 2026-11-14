---
title: "ipa-adtrust-install(1)"
name: "ipa-adtrust-install"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipa-adtrust-install/"
description: "ipa-adtrust-install – Prepare an IPA server to be able to establish trust relationships with AD domains"
---

<h2>NAME</h2>
<p> ipa-adtrust-install &#8211; Prepare an IPA server to be able to establish trust relationships with AD domains</p>
<h2>SYNOPSIS</h2>
<p> ipa-adtrust-install [<i>OPTION</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Adds all necessary objects and configuration to allow an IPA server to create a trust to an Active Directory domain. This requires that the IPA server is already installed and configured. </p>
<p> Please note you will not be able to estabilish an trust to an Active Directory domain unless the realm name of the IPA server matches its domain name. </p>
<p> ipa-adtrust-install can be run multiple times to reinstall deleted objects or broken configuration files. E.g. a fresh samba configuration (smb.conf file and registry based configuration can be created. Other items like e.g. the configuration of the local range cannot be changed by running ipa-adtrust-install a second time because with changes here other objects might be affected as well. </p>
<h3>Firewall Requirements</h3>
<p> In addition to the IPA server firewall requirements, ipa-adtrust-install requires the following ports to be open to allow IPA and Active Directory to communicate together: </p>
<p> <code>TCP Ports</code></p>
<dl>
<dt>
<dd> &bull; 135/tcp EPMAP</p>
<dt>
<dd> &bull; 138/tcp NetBIOS-DGM</p>
<dt>
<dd> &bull; 139/tcp NetBIOS-SSN</p>
<dt>
<dd> &bull; 445/tcp Microsoft-DS</p>
<dt>
<dd> &bull; 1024/tcp through 1300/tcp to allow EPMAP on port 135/tcp to create a TCP listener based on an incoming request.</p>
<dt><code>UDP Ports</code></p>
<dd>
<dt>
<dd> &bull; 138/udp NetBIOS-DGM</p>
<dt>
<dd> &bull; 139/udp NetBIOS-SSN</p>
<dt>
<dd> &bull; 389/udp LDAP </p>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd> Enable debug logging when more verbose output is needed</p>
<dt><code>&#8211;netbios-name</code>=<i>NETBIOS_NAME</i></p>
<dd> The NetBIOS name for the IPA domain. If not provided then this is determined based on the leading component of the DNS domain name. Running ipa-adtrust-install for a second time with a different NetBIOS name will change the name. Please note that changing the NetBIOS name might break existing trust relationships to other domains.</p>
<dt><code>&#8211;no-msdcs</code></p>
<dd> Do not create DNS service records for Windows in managed DNS server. Since those DNS service records are the only way to discover domain controllers of other domains they must be added manually to a different DNS server to allow trust realationships work properly. All needed service records are listed when ipa-adtrust-install finishes and either &#8211;no-msdcs was given or no IPA DNS service is configured. Typically service records for the following service names are needed for the IPA domain which should point to all IPA servers:</p>
<dt>
<dd> &bull; _ldap._tcp</p>
<dt>
<dd> &bull; _kerberos._tcp</p>
<dt>
<dd> &bull; _kerberos._udp</p>
<dt>
<dd> &bull; _ldap._tcp.dc._msdcs</p>
<dt>
<dd> &bull; _kerberos._tcp.dc._msdcs</p>
<dt>
<dd> &bull; _kerberos._udp.dc._msdcs</p>
<dt>
<dd> &bull; _ldap._tcp.Default-First-Site-Name._sites.dc._msdcs</p>
<dt>
<dd> &bull; _kerberos._tcp.Default-First-Site-Name._sites.dc._msdcs</p>
<dt>
<dd> &bull; _kerberos._udp.Default-First-Site-Name._sites.dc._msdcs</p>
<dt><code>&#8211;add-sids</code></p>
<dd> Add SIDs to existing users and groups as on of final steps of the ipa-adtrust-install run. If there a many existing users and groups and a couple of replicas in the environment this operation might lead to a high replication traffic and a performance degradation of all IPA servers in the environment. To avoid this the SID generation can be run after ipa-adtrust-install is run and scheduled independently. To start this task you have to load an edited version of ipa-sidgen-task-run.ldif with the ldapmodify command info the directory server.</p>
<dt><code>&#8211;add-agents</code></p>
<dd> Add IPA masters to the list that allows to serve information about users from trusted forests. Starting with FreeIPA 4.2, a regular IPA master can provide this information to SSSD clients. IPA masters aren&#8217;t added to the list automatically as restart of the LDAP service on each of them is required. The host where ipa-adtrust-install is being run is added automatically.</p>
<dt>
<dd> Note that IPA masters where ipa-adtrust-install wasn&#8217;t run, can serve information about users from trusted forests only if they are enabled via ipa-adtrust-install run on any other IPA master. At least SSSD version 1.13 on IPA master is required to be able to perform as a trust agent.</p>
<dt><code>-U</code>, <code>&#8211;unattended</code></p>
<dd> An unattended installation that will never prompt for user input</p>
<dt><code>-U</code>, <code>&#8211;rid-base</code>=<i>RID_BASE</i></p>
<dd> First RID value of the local domain. The first Posix ID of the local domain will be assigned to this RID, the second to RID+1 etc. See the online help of the idrange CLI for details.</p>
<dt><code>-U</code>, <code>&#8211;secondary-rid-base</code>=<i>SECONDARY_RID_BASE</i></p>
<dd> Start value of the secondary RID range, which is only used in the case a user and a group share numerically the same Posix ID. See the online help of the idrange CLI for details.</p>
<dt><code>-A</code>, <code>&#8211;admin-name</code>=<i>ADMIN_NAME</i></p>
<dd> The name of the user with administrative privileges for this IPA server. Defaults to &#8216;admin&#8217;.</p>
<dt><code>-a</code>, <code>&#8211;admin-password</code>=<i>password</i></p>
<dd> The password of the user with administrative privileges for this IPA server. Will be asked interactively if <code>-U</code> is not specified.</p>
<dt>The credentials of the admin user will be used to obtain Kerberos ticket before configuring cross-realm trusts support and afterwards, to ensure that the ticket contains MS-PAC information required to actually add a trust with Active Directory domain via &#8216;ipa trust-add &#8211;type=ad&#8217; command.</p>
<dd>
<dt><code>&#8211;enable-compat</code></p>
<dd> Enables support for trusted domains users for old clients through Schema Compatibility plugin. SSSD supports trusted domains natively starting with version 1.9. For platforms that lack SSSD or run older SSSD version one needs to use this option. When enabled, slapi-nis package needs to be installed and schema-compat-plugin will be configured to provide lookup of users and groups from trusted domains via SSSD on IPA server. These users and groups will be available under <code>cn=users,cn=compat,$SUFFIX</code> and <code>cn=groups,cn=compat,$SUFFIX</code> trees. SSSD will normalize names of users and groups to lower case.</p>
<dt>
<dd> In addition to providing these users and groups through the compat tree, this option enables authentication over LDAP for trusted domain users with DN under compat tree, i.e. using bind DN <code>uid=administrator [at] ad.domain,cn=users,cn=compat,$SUFFIX</code>.</p>
<dt>
<dd> LDAP authentication performed by the compat tree is done via PAM &#8216;<code>system-auth</code>&#8216; service. This service exists by default on Linux systems and is provided by pam package as /etc/pam.d/system-auth. If your IPA install does not have default HBAC rule &#8216;allow_all&#8217; enabled, then make sure to define in IPA special service called &#8216;<code>system-auth</code>&#8216; and create an HBAC rule to allow access to anyone to this rule on IPA masters.</p>
<dt>
<dd> As &#8216;<code>system-auth</code>&#8216; PAM service is not used directly by any other application, it is safe to use it for trusted domain users via compatibility path.</p>
<dt></dl>
<h2>EXIT STATUS</h2>
<dd> 0 if the installation was successful </p>
<p> 1 if an error occurred </p>
<h2>Index</h2>
