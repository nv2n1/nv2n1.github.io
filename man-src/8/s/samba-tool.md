---
title: "samba-tool(8)"
name: "samba-tool"
section: "8"
letter: "s"
url: "/docs/linux/man/8-samba-tool/"
description: "samba-tool – Main Samba administration tool."
---

<p>samba-tool &#8211; Main Samba administration tool.</p>
<h2>Synopsis</h2>
<dl>
<dd>samba-tool [-h] [-W myworkgroup] [-U user] [-d debuglevel] [&#8211;v]</dl>
<h2>Description</h2>
<p>This tool is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite.</p>
<h2>Options</h2>
<p>-h|&#8211;help</p>
<dl>
<dd>Show this help message and exit</dl>
<p> &#8211;realm=REALM</p>
<dl>
<dd>Set the realm name</dl>
<p> &#8211;simple-bind-dn=DN</p>
<dl>
<dd>DN to use for a simple bind</dl>
<p> &#8211;password=PASSWORD</p>
<dl>
<dd>Password</dl>
<p> -U USERNAME|&#8211;username=USERNAME</p>
<dl>
<dd>Username</dl>
<p> -W WORKGROUP|&#8211;workgroup=WORKGROUP</p>
<dl>
<dd>Workgroup</dl>
<p> -N|&#8211;no-pass</p>
<dl>
<dd>Don&#8217;t ask for a password</dl>
<p> -k KERBEROS|&#8211;kerberos=KERBEROS</p>
<dl>
<dd>Use Kerberos</dl>
<p> &#8211;ipaddress=IPADDRESS</p>
<dl>
<dd>IP address of the server</dl>
<p> -d|&#8211;debuglevel=level</p>
<dl>
<dd><i>level</i> is an integer from 0 to 10. The default value if this parameter is not specified is 1. </p>
<p> The higher this value, the more detail will be logged to the log files about the activities of the server. At level 0, only critical errors and serious warnings will be logged. Level 1 is a reasonable level for day-to-day running &#8211; it generates a small amount of information about operations carried out. </p>
<p> Levels above 1 will generate considerable amounts of log data, and should only be used when investigating a problem. Levels above 3 are designed for use only by developers and generate HUGE amounts of log data, most of which is extremely cryptic. </p>
<p> Note that specifying this parameter here will override the m[blue]<code>log level</code>m[] parameter in the smb.conf file.</dl>
<p> -V|&#8211;version</p>
<dl>
<dd>Prints the program version number.</dl>
<p> -s|&#8211;configfile=&lt;configuration file&gt;</p>
<dl>
<dd>The file specified contains the configuration details required by the server. The information in this file includes server-specific information such as what printcap file to use, as well as descriptions of all the services that the server is to provide. See smb.conf for more information. The default configuration file name is determined at compile time.</dl>
<p> -l|&#8211;log-basename=logdirectory</p>
<dl>
<dd>Base directory name for log/debug files. The extension <code>&quot;.progname&quot;</code> will be appended (e.g. log.smbclient, log.smbd, etc&#8230;). The log file is never removed by the client.</dl>
<p> &#8211;option=&lt;name&gt;=&lt;value&gt;</p>
<dl>
<dd>Set the <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5) option &quot;&lt;name&gt;&quot; to value &quot;&lt;value&gt;&quot; from the command line. This overrides compiled-in defaults and options read from the configuration file.</dl>
<h2>Commands</h2>
<h3>dbcheck</h3>
<p>Check the local AD database for errors.</p>
<h3>delegation</h3>
<p>Manage Delegations.</p>
<h3>delegation add-service accountname principal [options]</h3>
<p>Add a service principal as msDS-AllowedToDelegateTo.</p>
<h3>delegation del-service accountname principal [options]</h3>
<p>Delete a service principal as msDS-AllowedToDelegateTo.</p>
<h3>delegation for-any-protocol accountname [(on|off)] [options]</h3>
<p>Set/unset UF_TRUSTED_TO_AUTHENTICATE_FOR_DELEGATION (S4U2Proxy) for an account.</p>
<h3>delegation for-any-service accountname [(on|off)] [options]</h3>
<p>Set/unset UF_TRUSTED_FOR_DELEGATION for an account.</p>
<h3>delegation show accountname [options]<tt>&nbsp;</tt></h3>
<p>Show the delegation setting of an account.</p>
<h3>dns</h3>
<p>Manage Domain Name Service (DNS).</p>
<h3>dns add server zone name A|AAAA|PTR|CNAME|NS|MX|SRV|TXT data</h3>
<p>Add a DNS record.</p>
<h3>dns delete server zone name A|AAAA|PTR|CNAME|NS|MX|SRV|TXT data</h3>
<p>Delete a DNS record.</p>
<h3>dns query server zone name A|AAAA|PTR|CNAME|NS|MX|SRV|TXT|ALL [options] data</h3>
<p>Query a name.</p>
<h3>dns roothints server [name] [options]</h3>
<p>Query root hints.</p>
<h3>dns serverinfo server [options]</h3>
<p>Query server information.</p>
<h3>dns update server zone name A|AAAA|PTR|CNAME|NS|MX|SRV|TXT olddata newdata</h3>
<p>Update a DNS record.</p>
<h3>dns zonecreate server zone [options]</h3>
<p>Create a zone.</p>
<h3>dns zonedelete server zone [options]</h3>
<p>Delete a zone.</p>
<h3>dns zoneinfo server zone [options]</h3>
<p>Query zone information.</p>
<h3>dns zonelist server [options]</h3>
<p>List zones.</p>
<h3>domain</h3>
<p>Manage Domain.</p>
<h3>domain classicupgrade [options] classic_smb_conf</h3>
<p>Upgrade from Samba classic (NT4-like) database to Samba AD DC database.</p>
<h3>domain dcpromo dnsdomain [DC|RODC] [options]</h3>
<p>Promote an existing domain member or NT4 PDC to an AD DC.</p>
<h3>domain demote</h3>
<p>Demote ourselves from the role of domain controller.</p>
<h3>domain exportkeytab keytab [options]</h3>
<p>Dumps Kerberos keys of the domain into a keytab.</p>
<h3>domain info ip_address [options]</h3>
<p>Print basic info about a domain and the specified DC.</p>
<h3>domain join dnsdomain [DC|RODC|MEMBER|SUBDOMAIN] [options]</h3>
<p>Join a domain as either member or backup domain controller.</p>
<h3>domain level show|raise options [options]</h3>
<p>Show/raise domain and forest function levels.</p>
<h3>domain passwordsettings show|set options [options]</h3>
<p>Show/set password settings.</p>
<h3>domain provision</h3>
<p>Promote an existing domain member or NT4 PDC to an AD DC.</p>
<h3>domain trust</h3>
<p>Domain and forest trust management.</p>
<h3>domain trust create DOMAIN options [options]</h3>
<p>Create a domain or forest trust.</p>
<h3>domain trust delete DOMAIN options [options]</h3>
<p>Delete a domain trust.</p>
<h3>domain trust list options [options]</h3>
<p>List domain trusts.</p>
<h3>domain trust namespaces [DOMAIN] options [options]</h3>
<p>Manage forest trust namespaces.</p>
<h3>domain trust show DOMAIN options [options]</h3>
<p>Show trusted domain details.</p>
<h3>domain trust validate DOMAIN options [options]</h3>
<p>Validate a domain trust.</p>
<h3>drs</h3>
<p>Manage Directory Replication Services (DRS).</p>
<h3>drs bind</h3>
<p>Show DRS capabilities of a server.</p>
<h3>drs kcc</h3>
<p>Trigger knowledge consistency center run.</p>
<h3>drs options</h3>
<p>Query or change <i>options</i> for NTDS Settings object of a domain controller.</p>
<h3>drs replicate destination_DC source_DC NC [options]</h3>
<p>Replicate a naming context between two DCs.</p>
<h3>drs showrepl</h3>
<p>Show replication status.</p>
<h3>dsacl</h3>
<p>Administer DS ACLs</p>
<h3>dsacl set</h3>
<p>Modify access list on a directory object.</p>
<h3>fsmo</h3>
<p>Manage Flexible Single Master Operations (FSMO).</p>
<h3>fsmo seize [options]</h3>
<p>Seize the role.</p>
<h3>fsmo show</h3>
<p>Show the roles.</p>
<h3>fsmo transfer [options]</h3>
<p>Transfer the role.</p>
<h3>gpo</h3>
<p>Manage Group Policy Objects (GPO).</p>
<h3>gpo create displayname [options]</h3>
<p>Create an empty GPO.</p>
<h3>gpo del gpo [options]</h3>
<p>Delete GPO.</p>
<h3>gpo dellink container_dn gpo [options]</h3>
<p>Delete GPO link from a container.</p>
<h3>gpo fetch gpo [options]</h3>
<p>Download a GPO.</p>
<h3>gpo getinheritance container_dn [options]</h3>
<p>Get inheritance flag for a container.</p>
<h3>gpo getlink container_dn [options]</h3>
<p>List GPO Links for a container.</p>
<h3>gpo list username [options]</h3>
<p>List GPOs for an account.</p>
<h3>gpo listall</h3>
<p>List all GPOs.</p>
<h3>gpo listcontainers gpo [options]</h3>
<p>List all linked containers for a GPO.</p>
<h3>gpo setinheritance container_dn block|inherit [options]</h3>
<p>Set inheritance flag on a container.</p>
<h3>gpo setlink container_dn gpo [options]</h3>
<p>Add or Update a GPO link to a container.</p>
<h3>gpo show gpo [options]</h3>
<p>Show information for a GPO.</p>
<h3>group</h3>
<p>Manage groups.</p>
<h3>group add groupname [options]</h3>
<p>Create a new AD group.</p>
<h3>group addmembers groupname members [options]</h3>
<p>Add members to an AD group.</p>
<h3>group delete groupname [options]</h3>
<p>Delete an AD group.</p>
<h3>group list</h3>
<p>List all groups.</p>
<h3>group listmembers groupname [options]</h3>
<p>List all members of the specified AD group.</p>
<h3>group removemembers groupname members [options]</h3>
<p>Remove members from the specified AD group.</p>
<h3>ldapcmp <i>URL1</i> <i>URL2</i> <i>domain|configuration|schema|dnsdomain|dnsforest</i> [options]</h3>
<p>Compare two LDAP databases.</p>
<h3>ntacl</h3>
<p>Manage NT ACLs.</p>
<h3>ntacl get file [options]</h3>
<p>Get ACLs on a file.</p>
<h3>ntacl set acl file [options]</h3>
<p>Set ACLs on a file.</p>
<h3>ntacl sysvolcheck</h3>
<p>Check sysvol ACLs match defaults (including correct ACLs on GPOs).</p>
<h3>ntacl sysvolreset</h3>
<p>Reset sysvol ACLs to defaults (including correct ACLs on GPOs).</p>
<h3>rodc</h3>
<p>Manage Read-Only Domain Controller (RODC).</p>
<h3>rodc preload SID|DN|accountname [options]</h3>
<p>Preload one account for an RODC.</p>
<h3>sites</h3>
<p>Manage sites.</p>
<h3>sites create site [options]</h3>
<p>Create a new site.</p>
<h3>sites remove site [options]</h3>
<p>Delete an existing site.</p>
<h3>spn</h3>
<p>Manage Service Principal Names (SPN).</p>
<h3>spn add name user [options]</h3>
<p>Create a new SPN.</p>
<h3>spn delete name [user] [options]</h3>
<p>Delete an existing SPN.</p>
<h3>spn list user [options]</h3>
<p>List SPNs of a given user.</p>
<h3>testparm</h3>
<p>Check the syntax of the configuration file.</p>
<h3>time</h3>
<p>Retrieve the time on a server.</p>
<h3>user</h3>
<p>Manage users.</p>
<h3>user add username [password]</h3>
<p>Create a new user. Please note that this subcommand is deprecated and available for compatibility reasons only. Please use samba-tool user create instead.</p>
<h3>user create username [password]</h3>
<p>Create a new user in the Active Directory Domain.</p>
<h3>user delete username [options]</h3>
<p>Delete an existing user account.</p>
<h3>user disable username</h3>
<p>Disable an user account.</p>
<h3>user enable username</h3>
<p>Enable an user account.</p>
<h3>user list</h3>
<p>List all users.</p>
<h3>user password [options]</h3>
<p>Change password for an user account (the one provided in authentication).</p>
<h3>user setexpiry username [options]</h3>
<p>Set the expiration of an user account.</p>
<h3>user setpassword username [options]</h3>
<p>Sets or resets the password of an user account.</p>
<h3>user getpassword username [options]</h3>
<p>Gets the password of an user account.</p>
<h3>user syncpasswords &#8211;cache-ldb-initialize [options]</h3>
<p>Syncs the passwords of all user accounts, using an optional script. </p>
<p> Note that this command should run on a single domain controller only (typically the PDC-emulator).</p>
<h3>vampire [options] <i>domain</i></h3>
<p>Join and synchronise a remote AD domain to the local server. Please note that samba-tool vampire is deprecated, please use samba-tool domain join instead.</p>
<h3>help</h3>
<p>Gives usage information.</p>
<h2>Version</h2>
<p>This man page is complete for version 4 of the Samba suite.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed. </p>
<p> The samba-tool manpage was written by Karolin Seeger.</p>
