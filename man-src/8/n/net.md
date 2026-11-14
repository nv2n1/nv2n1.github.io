---
title: "net(8)"
name: "net"
section: "8"
letter: "n"
url: "/docs/linux/man/8-net/"
description: "net – Tool for administration of Samba and remote CIFS servers."
---

<p>net &#8211; Tool for administration of Samba and remote CIFS servers.</p>
<h2>Synopsis</h2>
<dl>
<dd>net {&lt;ads|rap|rpc&gt;} [-h|&#8211;help] [-w|&#8211;workgroup workgroup] [-W|&#8211;myworkgroup myworkgroup] [-U|&#8211;user user] [-I|&#8211;ipaddress ip-address] [-p|&#8211;port port] [-n myname] [-s conffile] [-S|&#8211;server server] [-l|&#8211;long] [-v|&#8211;verbose] [-f|&#8211;force] [-P|&#8211;machine-pass] [-d debuglevel] [-V] [&#8211;request-timeout seconds] [-t|&#8211;timeout seconds] [-i|&#8211;stdin] [&#8211;tallocreport]</dl>
<h2>Description</h2>
<p>This tool is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> The Samba net utility is meant to work just like the net utility available for windows and DOS. The first argument should be used to specify the protocol to use when executing a certain command. ADS is used for ActiveDirectory, RAP is using for old (Win9x/NT3) clients and RPC can be used for NT4 and Windows 2000. If this argument is omitted, net will try to determine it automatically. Not all commands are available on all protocols.</p>
<h2>Options</h2>
<p>-?|&#8211;help</p>
<dl>
<dd>Print a summary of command line options.</dl>
<p> -k|&#8211;kerberos</p>
<dl>
<dd>Try to authenticate with kerberos. Only useful in an Active Directory environment.</dl>
<p> -w|&#8211;workgroup target-workgroup</p>
<dl>
<dd>Sets target workgroup or domain. You have to specify either this option or the IP address or the name of a server.</dl>
<p> -W|&#8211;myworkgroup workgroup</p>
<dl>
<dd>Sets client workgroup or domain</dl>
<p> -U|&#8211;user user</p>
<dl>
<dd>User name to use</dl>
<p> -I|&#8211;ipaddress ip-address</p>
<dl>
<dd>IP address of target server to use. You have to specify either this option or a target workgroup or a target server.</dl>
<p> -p|&#8211;port port</p>
<dl>
<dd>Port on the target server to connect to (usually 139 or 445). Defaults to trying 445 first, then 139.</dl>
<p> -n|&#8211;netbiosname &lt;primary NetBIOS name&gt;</p>
<dl>
<dd>This option allows you to override the NetBIOS name that Samba uses for itself. This is identical to setting the m[blue]<code>netbios name</code>m[] parameter in the smb.conf file. However, a command line setting will take precedence over settings in smb.conf.</dl>
<p> -S|&#8211;server server</p>
<dl>
<dd>Name of target server. You should specify either this option or a target workgroup or a target IP address.</dl>
<p> -l|&#8211;long</p>
<dl>
<dd>When listing data, give more information on each item.</dl>
<p> -v|&#8211;verbose</p>
<dl>
<dd>When listing data, give more verbose information on each item.</dl>
<p> -f|&#8211;force</p>
<dl>
<dd>Enforcing a net command.</dl>
<p> -P|&#8211;machine-pass</p>
<dl>
<dd>Make queries to the external server using the machine account of the local server.</dl>
<p> &#8211;request-timeout 30</p>
<dl>
<dd>Let client requests timeout after 30 seconds the default is 10 seconds.</dl>
<p> -t|&#8211;timeout 30</p>
<dl>
<dd>Set timeout for client operations to 30 seconds.</dl>
<p> &#8211;use-ccache</p>
<dl>
<dd>Try to use the credentials cached by winbind.</dl>
<p> -i|&#8211;stdin</p>
<dl>
<dd>Take input for net commands from standard input.</dl>
<p> &#8211;tallocreport</p>
<dl>
<dd>Generate a talloc report while processing a net command.</dl>
<p> -T|&#8211;test</p>
<dl>
<dd>Only test command sequence, dry-run.</dl>
<p> -F|&#8211;flags FLAGS</p>
<dl>
<dd>Pass down integer flags to a net subcommand.</dl>
<p> -C|&#8211;comment COMMENT</p>
<dl>
<dd>Pass down a comment string to a net subcommand.</dl>
<p> -n|&#8211;myname MYNAME</p>
<dl>
<dd>Use MYNAME as a requester name for a net subcommand.</dl>
<p> -c|&#8211;container CONTAINER</p>
<dl>
<dd>Use a specific AD container for net ads operations.</dl>
<p> -M|&#8211;maxusers MAXUSERS</p>
<dl>
<dd>Fill in the maxusers field in net rpc share operations.</dl>
<p> -r|&#8211;reboot</p>
<dl>
<dd>Reboot a remote machine after a command has been successfully executed (e.g. in remote join operations).</dl>
<p> &#8211;force-full-repl</p>
<dl>
<dd>When calling &quot;net rpc vampire keytab&quot; this option enforces a full re-creation of the generated keytab file.</dl>
<p> &#8211;single-obj-repl</p>
<dl>
<dd>When calling &quot;net rpc vampire keytab&quot; this option allows one to replicate just a single object to the generated keytab file.</dl>
<p> &#8211;clean-old-entries</p>
<dl>
<dd>When calling &quot;net rpc vampire keytab&quot; this option allows one to cleanup old entries from the generated keytab file.</dl>
<p> &#8211;db</p>
<dl>
<dd>Define dbfile for &quot;net idmap&quot; commands.</dl>
<p> &#8211;lock</p>
<dl>
<dd>Activates locking of the dbfile for &quot;net idmap check&quot; command.</dl>
<p> -a|&#8211;auto</p>
<dl>
<dd>Activates noninteractive mode in &quot;net idmap check&quot;.</dl>
<p> &#8211;repair</p>
<dl>
<dd>Activates repair mode in &quot;net idmap check&quot;.</dl>
<p> &#8211;acls</p>
<dl>
<dd>Includes ACLs to be copied in &quot;net rpc share migrate&quot;.</dl>
<p> &#8211;attrs</p>
<dl>
<dd>Includes file attributes to be copied in &quot;net rpc share migrate&quot;.</dl>
<p> &#8211;timestamps</p>
<dl>
<dd>Includes timestamps to be copied in &quot;net rpc share migrate&quot;.</dl>
<p> -X|&#8211;exclude DIRECTORY</p>
<dl>
<dd>Allows one to exclude directories when copying with &quot;net rpc share migrate&quot;.</dl>
<p> &#8211;destination SERVERNAME</p>
<dl>
<dd>Defines the target servername of migration process (defaults to localhost).</dl>
<p> -L|&#8211;local</p>
<dl>
<dd>Sets the type of group mapping to local (used in &quot;net groupmap set&quot;).</dl>
<p> -D|&#8211;domain</p>
<dl>
<dd>Sets the type of group mapping to domain (used in &quot;net groupmap set&quot;).</dl>
<p> -N|&#8211;ntname NTNAME</p>
<dl>
<dd>Sets the ntname of a group mapping (used in &quot;net groupmap set&quot;).</dl>
<p> -R|&#8211;rid RID</p>
<dl>
<dd>Sets the rid of a group mapping (used in &quot;net groupmap set&quot;).</dl>
<p> &#8211;reg-version REG_VERSION</p>
<dl>
<dd>Assume database version {n|1,2,3} (used in &quot;net registry check&quot;).</dl>
<p> -o|&#8211;output FILENAME</p>
<dl>
<dd>Output database file (used in &quot;net registry check&quot;).</dl>
<p> &#8211;wipe</p>
<dl>
<dd>Create a new database from scratch (used in &quot;net registry check&quot;).</dl>
<p> &#8211;precheck PRECHECK_DB_FILENAME</p>
<dl>
<dd>Defines filename for database prechecking (used in &quot;net registry import&quot;).</dl>
<p> &#8211;no-dns-updates</p>
<dl>
<dd>Do not perform DNS updates as part of &quot;net ads join&quot;.</dl>
<p> -e|&#8211;encrypt</p>
<dl>
<dd>This command line parameter requires the remote server support the UNIX extensions or that the SMB3 protocol has been selected. Requests that the connection be encrypted. Negotiates SMB encryption using either SMB3 or POSIX extensions via GSSAPI. Uses the given credentials for the encryption negotiation (either kerberos or NTLMv1/v2 if given domain/username/password triple. Fails the connection if encryption cannot be negotiated.</dl>
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
<h3>Changesecretpw</h3>
<p>This command allows the Samba machine account password to be set from an external application to a machine account password that has already been stored in Active Directory. DO NOT USE this command unless you know exactly what you are doing. The use of this command requires that the force flag (-f) be used also. There will be NO command prompt. Whatever information is piped into stdin, either by typing at the command line or otherwise, will be stored as the literal machine password. Do NOT use this without care and attention as it will overwrite a legitimate machine password without warning. YOU HAVE BEEN WARNED.</p>
<h3>Time</h3>
<p>The NET TIME command allows you to view the time on a remote server or synchronise the time on the local server with the time on the remote server.</p>
<h3>Time</h3>
<p>Without any options, the NET TIME command displays the time on the remote server. The remote server must be specified with the -S option.</p>
<h3>Time System</h3>
<p>Displays the time on the remote server in a format ready for /bin/date. The remote server must be specified with the -S option.</p>
<h3>Time Set</h3>
<p>Tries to set the date and time of the local server to that on the remote server using /bin/date. The remote server must be specified with the -S option.</p>
<h3>Time Zone</h3>
<p>Displays the timezone in hours from GMT on the remote server. The remote server must be specified with the -S option.</p>
<h3>[RPC|ADS] JOIN [TYPE] [&#8211;no-dns-updates] [-U username[%password]] [createupn=UPN] [createcomputer=OU] [machinepass=PASS] [osName=string osVer=string] [options]</h3>
<p>Join a domain. If the account already exists on the server, and [TYPE] is MEMBER, the machine will attempt to join automatically. (Assuming that the machine has been created in server manager) Otherwise, a password will be prompted for, and a new account may be created. </p>
<p> [TYPE] may be PDC, BDC or MEMBER to specify the type of server joining the domain. </p>
<p> [UPN] (ADS only) set the principalname attribute during the join. The default format is host/netbiosname [at] REALM. </p>
<p> [OU] (ADS only) Precreate the computer account in a specific OU. The OU string reads from top to bottom without RDNs, and is delimited by a &#8216;/&#8217;. Please note that &#8216;\&#8217; is used for escape by both the shell and ldap, so it may need to be doubled or quadrupled to pass through, and it is not used as a delimiter. </p>
<p> [PASS] (ADS only) Set a specific password on the computer account being created by the join. </p>
<p> [osName=string osVer=String] (ADS only) Set the operatingSystem and operatingSystemVersion attribute during the join. Both parameters must be specified for either to take effect.</p>
<h3>[RPC] OLDJOIN [options]</h3>
<p>Join a domain. Use the OLDJOIN option to join the domain using the old style of domain joining &#8211; you need to create a trust account in server manager first.</p>
<h3>[Rpc|Ads] User</h3>
<h3>[Rpc|Ads] User</h3>
<p>List all users</p>
<h3>[RPC|ADS] USER DELETE target</h3>
<p>Delete specified user</p>
<h3>[RPC|ADS] USER INFO target</h3>
<p>List the domain groups of the specified user.</p>
<h3>[RPC|ADS] USER RENAME oldname newname</h3>
<p>Rename specified user.</p>
<h3>[RPC|ADS] USER ADD name [password] [-F user flags] [-C comment]</h3>
<p>Add specified user.</p>
<h3>[Rpc|Ads] Group</h3>
<h3>[RPC|ADS] GROUP [misc options] [targets]</h3>
<p>List user groups.</p>
<h3>[RPC|ADS] GROUP DELETE name [misc. options]</h3>
<p>Delete specified group.</p>
<h3>[RPC|ADS] GROUP ADD name [-C comment]</h3>
<p>Create specified group.</p>
<h3>[Rap|Rpc] Share</h3>
<h3>[RAP|RPC] SHARE [misc. options] [targets]</h3>
<p>Enumerates all exported resources (network shares) on target server.</p>
<h3>[RAP|RPC] SHARE ADD name=serverpath [-C comment] [-M maxusers] [targets]</h3>
<p>Adds a share from a server (makes the export active). Maxusers specifies the number of users that can be connected to the share simultaneously.</p>
<h3>SHARE DELETE sharename</h3>
<p>Delete specified share.</p>
<h3>[Rpc|Rap] File</h3>
<h3>[Rpc|Rap] File</h3>
<p>List all open files on remote server.</p>
<h3>[RPC|RAP] FILE CLOSE fileid</h3>
<p>Close file with specified <i>fileid</i> on remote server.</p>
<h3>[RPC|RAP] FILE INFO fileid</h3>
<p>Print information on specified <i>fileid</i>. Currently listed are: file-id, username, locks, path, permissions.</p>
<h3>[RAP|RPC] FILE USER user</h3>
<p>List files opened by specified <i>user</i>. Please note that net rap file user does not work against Samba servers.</p>
<h3>Session</h3>
<h3>Rap Session</h3>
<p>Without any other options, SESSION enumerates all active SMB/CIFS sessions on the target server.</p>
<h3>Rap Session Delete|Close Client_Name</h3>
<p>Close the specified sessions.</p>
<h3>Rap Session Info Client_Name</h3>
<p>Give a list with all the open files in specified session.</p>
<h3>RAP SERVER <i>DOMAIN</i></h3>
<p>List all servers in specified domain or workgroup. Defaults to local domain.</p>
<h3>Rap Domain</h3>
<p>Lists all domains and workgroups visible on the current network.</p>
<h3>Rap Printq</h3>
<h3>Rap Printq Info Queue_Name</h3>
<p>Lists the specified print queue and print jobs on the server. If the <i>QUEUE_NAME</i> is omitted, all queues are listed.</p>
<h3>Rap Printq Delete Jobid</h3>
<p>Delete job with specified id.</p>
<h3>RAP VALIDATE <i>user</i> [<i>password</i>]</h3>
<p>Validate whether the specified user can log in to the remote server. If the password is not specified on the commandline, it will be prompted. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> Currently NOT implemented. </p>
</dl>
<h3>Rap Groupmember</h3>
<h3>Rap Groupmember List Group</h3>
<p>List all members of the specified group.</p>
<h3>Rap Groupmember Delete Group User</h3>
<p>Delete member from group.</p>
<h3>Rap Groupmember Add Group User</h3>
<p>Add member to group.</p>
<h3>RAP ADMIN <i>command</i></h3>
<p>Execute the specified <i>command</i> on the remote server. Only works with OS/2 servers. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> Currently NOT implemented. </p>
</dl>
<h3>Rap Service</h3>
<h3>RAP SERVICE START NAME [arguments&#8230;]</h3>
<p>Start the specified service on the remote server. Not implemented yet. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> Currently NOT implemented. </p>
</dl>
<h3>Rap Service Stop</h3>
<p>Stop the specified service on the remote server. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> Currently NOT implemented. </p>
</dl>
<h3>RAP PASSWORD <i>USER</i> <i>OLDPASS</i> <i>NEWPASS</i></h3>
<p>Change password of <i>USER</i> from <i>OLDPASS</i> to <i>NEWPASS</i>.</p>
<h3>Lookup</h3>
<h3>Lookup Host Hostname [Type]</h3>
<p>Lookup the IP address of the given host with the specified type (netbios suffix). The type defaults to 0x20 (workstation).</p>
<h3>Lookup Ldap [Domain]</h3>
<p>Give IP address of LDAP server of specified <i>DOMAIN</i>. Defaults to local domain.</p>
<h3>Lookup Kdc [Realm]</h3>
<p>Give IP address of KDC for the specified <i>REALM</i>. Defaults to local realm.</p>
<h3>Lookup Dc [Domain]</h3>
<p>Give IP&#8217;s of Domain Controllers for specified <i> DOMAIN</i>. Defaults to local domain.</p>
<h3>Lookup Master Domain</h3>
<p>Give IP of master browser for specified <i>DOMAIN</i> or workgroup. Defaults to local domain.</p>
<h3>Cache</h3>
<p>Samba uses a general caching interface called &#8216;gencache&#8217;. It can be controlled using &#8216;NET CACHE&#8217;. </p>
<p> All the timeout parameters support the suffixes:</p>
<dl>
<dd>s &#8211; Seconds</dl>
<dl>
<dd>m &#8211; Minutes</dl>
<dl>
<dd>h &#8211; Hours</dl>
<dl>
<dd>d &#8211; Days</dl>
<dl>
<dd>w &#8211; Weeks</dl>
<h3>CACHE ADD key data time-out</h3>
<p>Add specified key+data to the cache with the given timeout.</p>
<h3>CACHE DEL key</h3>
<p>Delete key from the cache.</p>
<h3>CACHE SET key data time-out</h3>
<p>Update data of existing cache entry.</p>
<h3>Cache Search Pattern</h3>
<p>Search for the specified pattern in the cache data.</p>
<h3>Cache List</h3>
<p>List all current items in the cache.</p>
<h3>Cache Flush</h3>
<p>Remove all the current items from the cache.</p>
<h3>Getlocalsid [Domain]</h3>
<p>Prints the SID of the specified domain, or if the parameter is omitted, the SID of the local server.</p>
<h3>SETLOCALSID S-1-5-21-x-y-z</h3>
<p>Sets SID for the local server to the specified SID.</p>
<h3>Getdomainsid</h3>
<p>Prints the local machine SID and the SID of the current domain.</p>
<h3>Setdomainsid</h3>
<p>Sets the SID of the current domain.</p>
<h3>Groupmap</h3>
<p>Manage the mappings between Windows group SIDs and UNIX groups. Common options include:</p>
<dl>
<dd>
<dl>
<dd>&bull; unixgroup &#8211; Name of the UNIX group</dl>
<dl>
<dd>&bull; ntgroup &#8211; Name of the Windows NT group (must be resolvable to a SID</dl>
<dl>
<dd>&bull; rid &#8211; Unsigned 32-bit integer</dl>
<dl>
<dd>&bull; sid &#8211; Full SID in the form of &quot;S-1-&#8230;&quot;</dl>
<dl>
<dd>&bull; type &#8211; Type of the group; either &#8216;domain&#8217;, &#8216;local&#8217;, or &#8216;builtin&#8217;</dl>
<dl>
<dd>&bull; comment &#8211; Freeform text description of the group</dl>
</dl>
<h3>Groupmap Add</h3>
<p>Add a new group mapping entry: </p>
<dl>
<dd>
<pre>net groupmap add {rid=int|sid=string} unixgroup=string \
 [type={domain|local}] [ntgroup=string] [comment=string]</pre>
</dl>
<h3>Groupmap Delete</h3>
<p>Delete a group mapping entry. If more than one group name matches, the first entry found is deleted. </p>
<p> net groupmap delete {ntgroup=string|sid=SID}</p>
<h3>Groupmap Modify</h3>
<p>Update an existing group entry. </p>
<dl>
<dd>
<pre>net groupmap modify {ntgroup=string|sid=SID} [unixgroup=string] \
 [comment=string] [type={domain|local}]</pre>
</dl>
<h3>Groupmap List</h3>
<p>List existing group mapping entries. </p>
<p> net groupmap list [verbose] [ntgroup=string] [sid=SID]</p>
<h3>Maxrid</h3>
<p>Prints out the highest RID currently in use on the local server (by the active &#8216;passdb backend&#8217;).</p>
<h3>Rpc Info</h3>
<p>Print information about the domain of the remote server, such as domain name, domain sid and number of users and groups.</p>
<h3>[Rpc|Ads] Testjoin</h3>
<p>Check whether participation in a domain is still valid.</p>
<h3>[Rpc|Ads] Changetrustpw</h3>
<p>Force change of domain trust password.</p>
<h3>Rpc Trustdom</h3>
<h3>Rpc Trustdom Add Domain</h3>
<p>Add a interdomain trust account for <i>DOMAIN</i>. This is in fact a Samba account named <i>DOMAIN$</i> with the account flag <code>&#8216;I&#8217;</code> (interdomain trust account). This is required for incoming trusts to work. It makes Samba be a trusted domain of the foreign (trusting) domain. Users of the Samba domain will be made available in the foreign domain. If the command is used against localhost it has the same effect as smbpasswd -a -i DOMAIN. Please note that both commands expect a appropriate UNIX account.</p>
<h3>Rpc Trustdom Del Domain</h3>
<p>Remove interdomain trust account for <i>DOMAIN</i>. If it is used against localhost it has the same effect as smbpasswd -x DOMAIN$.</p>
<h3>Rpc Trustdom Establish Domain</h3>
<p>Establish a trust relationship to a trusted domain. Interdomain account must already be created on the remote PDC. This is required for outgoing trusts to work. It makes Samba be a trusting domain of a foreign (trusted) domain. Users of the foreign domain will be made available in our domain. You&#8217;ll need winbind and a working idmap config to make them appear in your system.</p>
<h3>Rpc Trustdom Revoke Domain</h3>
<p>Abandon relationship to trusted domain</p>
<h3>Rpc Trustdom List</h3>
<p>List all interdomain trust relationships.</p>
<h3>Rpc Trust</h3>
<h3>Rpc Trust Create</h3>
<p>Create a trust object by calling lsaCreateTrustedDomainEx2. The can be done on a single server or on two servers at once with the possibility to use a random trust password. </p>
<p> <code>Options:</code> </p>
<p> otherserver</p>
<dl>
<dd>Domain controller of the second domain</dl>
<p> otheruser</p>
<dl>
<dd>Admin user in the second domain</dl>
<p> otherdomainsid</p>
<dl>
<dd>SID of the second domain</dl>
<p> other_netbios_domain</p>
<dl>
<dd>NetBIOS (short) name of the second domain</dl>
<p> otherdomain</p>
<dl>
<dd>DNS (full) name of the second domain</dl>
<p> trustpw</p>
<dl>
<dd>Trust password</dl>
<p> <code>Examples:</code> </p>
<p> Create a trust object on srv1.dom1.dom for the domain dom2</p>
<dl>
<dd>
<dl>
<dd>
<pre>net rpc trust create \
 otherdomainsid=S-x-x-xx-xxxxxxxxxx-xxxxxxxxxx-xxxxxxxxx \
 other_netbios_domain=dom2 \
 otherdomain=dom2.dom \
 trustpw=12345678 \
 -S srv1.dom1.dom</pre>
</dl>
</dl>
<p> Create a trust relationship between dom1 and dom2</p>
<dl>
<dd>
<dl>
<dd>
<pre>net rpc trust create \
 otherserver=srv2.dom2.test \
 otheruser=dom2adm \
 -S srv1.dom1.dom</pre>
</dl>
</dl>
<h3>Rpc Trust Delete</h3>
<p>Delete a trust object by calling lsaDeleteTrustedDomain. The can be done on a single server or on two servers at once. </p>
<p> <code>Options:</code> </p>
<p> otherserver</p>
<dl>
<dd>Domain controller of the second domain</dl>
<p> otheruser</p>
<dl>
<dd>Admin user in the second domain</dl>
<p> otherdomainsid</p>
<dl>
<dd>SID of the second domain</dl>
<p> <code>Examples:</code> </p>
<p> Delete a trust object on srv1.dom1.dom for the domain dom2</p>
<dl>
<dd>
<dl>
<dd>
<pre>net rpc trust delete \
 otherdomainsid=S-x-x-xx-xxxxxxxxxx-xxxxxxxxxx-xxxxxxxxx \
 -S srv1.dom1.dom</pre>
</dl>
</dl>
<p> Delete a trust relationship between dom1 and dom2</p>
<dl>
<dd>
<dl>
<dd>
<pre>net rpc trust delete \
 otherserver=srv2.dom2.test \
 otheruser=dom2adm \
 -S srv1.dom1.dom</pre>
</dl>
</dl>
<h3></h3>
<h3>Rpc Rights</h3>
<p>This subcommand is used to view and manage Samba&#8217;s rights assignments (also referred to as privileges). There are three options currently available: <i>list</i>, <i>grant</i>, and <i>revoke</i>. More details on Samba&#8217;s privilege model and its use can be found in the Samba-HOWTO-Collection.</p>
<h3>Rpc Abortshutdown</h3>
<p>Abort the shutdown of a remote server.</p>
<h3>RPC SHUTDOWN [-t timeout] [-r] [-f] [-C message]</h3>
<p>Shut down the remote server. </p>
<p> -r</p>
<dl>
<dd>Reboot after shutdown.</dl>
<p> -f</p>
<dl>
<dd>Force shutting down all applications.</dl>
<p> -t timeout</p>
<dl>
<dd>Timeout before system will be shut down. An interactive user of the system can use this time to cancel the shutdown.</dl>
<p> -C message</p>
<dl>
<dd>Display the specified message on the screen to announce the shutdown.</dl>
<h3>Rpc Samdump</h3>
<p>Print out sam database of remote server. You need to run this against the PDC, from a Samba machine joined as a BDC.</p>
<h3>Rpc Vampire</h3>
<p>Export users, aliases and groups from remote server to local server. You need to run this against the PDC, from a Samba machine joined as a BDC. This vampire command cannot be used against an Active Directory, only against an NT4 Domain Controller.</p>
<h3>Rpc Vampire Keytab</h3>
<p>Dump remote SAM database to local Kerberos keytab file.</p>
<h3>Rpc Vampire Ldif</h3>
<p>Dump remote SAM database to local LDIF file or standard output.</p>
<h3>Rpc Getsid</h3>
<p>Fetch domain SID and store it in the local secrets.tdb.</p>
<h3>Ads Leave</h3>
<p>Make the remote host leave the domain it is part of.</p>
<h3>Ads Status</h3>
<p>Print out status of machine account of the local machine in ADS. Prints out quite some debug info. Aimed at developers, regular users should use NET ADS TESTJOIN.</p>
<h3>Ads Printer</h3>
<h3>Ads Printer Info [Printer] [Server]</h3>
<p>Lookup info for <i>PRINTER</i> on <i>SERVER</i>. The printer name defaults to &quot;*&quot;, the server name defaults to the local host.</p>
<h3>Ads Printer Publish Printer</h3>
<p>Publish specified printer using ADS.</p>
<h3>Ads Printer Remove Printer</h3>
<p>Remove specified printer from ADS directory.</p>
<h3>ADS SEARCH <i>EXPRESSION</i> <i>ATTRIBUTES&#8230;</i></h3>
<p>Perform a raw LDAP search on a ADS server and dump the results. The expression is a standard LDAP search expression, and the attributes are a list of LDAP fields to show in the results. </p>
<p> Example: <code>net ads search &#8216;(objectCategory=group)&#8217; sAMAccountName</code></p>
<h3>ADS DN <i>DN</i> <i>(attributes)</i></h3>
<p>Perform a raw LDAP search on a ADS server and dump the results. The DN standard LDAP DN, and the attributes are a list of LDAP fields to show in the result. </p>
<p> Example: <code>net ads dn &#8216;CN=administrator,CN=Users,DC=my,DC=domain&#8217; SAMAccountName</code></p>
<h3>Ads Workgroup</h3>
<p>Print out workgroup name for specified kerberos realm.</p>
<h3>Ads Enctypes</h3>
<p>List, modify or delete the value of the &quot;msDS-SupportedEncryptionTypes&quot; attribute of an account in AD. </p>
<p> This attribute allows one to control which Kerberos encryption types are used for the generation of initial and service tickets. The value consists of an integer bitmask with the following values: </p>
<p> 0x00000001 DES-CBC-CRC </p>
<p> 0x00000002 DES-CBC-MD5 </p>
<p> 0x00000004 RC4-HMAC </p>
<p> 0x00000008 AES128-CTS-HMAC-SHA1-96 </p>
<p> 0x00000010 AES256-CTS-HMAC-SHA1-96</p>
<h3>ADS ENCTYPES LIST <i>&lt;ACCOUNTNAME&gt;</i></h3>
<p>List the value of the &quot;msDS-SupportedEncryptionTypes&quot; attribute of a given account. </p>
<p> Example: <code>net ads enctypes list Computername</code></p>
<h3>ADS ENCTYPES SET <i>&lt;ACCOUNTNAME&gt;</i> <i>[enctypes]</i></h3>
<p>Set the value of the &quot;msDS-SupportedEncryptionTypes&quot; attribute of the LDAP object of ACCOUNTNAME to a given value. If the value is omitted, the value is set to 31 which enables all the currently supported encryption types. </p>
<p> Example: <code>net ads enctypes set Computername 24</code></p>
<h3>ADS ENCTYPES DELETE <i>&lt;ACCOUNTNAME&gt;</i></h3>
<p>Deletes the &quot;msDS-SupportedEncryptionTypes&quot; attribute of the LDAP object of ACCOUNTNAME. </p>
<p> Example: <code>net ads enctypes set Computername 24</code></p>
<h3>SAM CREATEBUILTINGROUP &lt;NAME&gt;</h3>
<p>(Re)Create a BUILTIN group. Only a wellknown set of BUILTIN groups can be created with this command. This is the list of currently recognized group names: Administrators, Users, Guests, Power Users, Account Operators, Server Operators, Print Operators, Backup Operators, Replicator, RAS Servers, Pre-Windows 2000 compatible Access. This command requires a running Winbindd with idmap allocation properly configured. The group gid will be allocated out of the winbindd range.</p>
<h3>SAM CREATELOCALGROUP &lt;NAME&gt;</h3>
<p>Create a LOCAL group (also known as Alias). This command requires a running Winbindd with idmap allocation properly configured. The group gid will be allocated out of the winbindd range.</p>
<h3>SAM DELETELOCALGROUP &lt;NAME&gt;</h3>
<p>Delete an existing LOCAL group (also known as Alias).</p>
<h3>SAM MAPUNIXGROUP &lt;NAME&gt;</h3>
<p>Map an existing Unix group and make it a Domain Group, the domain group will have the same name.</p>
<h3>SAM UNMAPUNIXGROUP &lt;NAME&gt;</h3>
<p>Remove an existing group mapping entry.</p>
<h3>SAM ADDMEM &lt;GROUP&gt; &lt;MEMBER&gt;</h3>
<p>Add a member to a Local group. The group can be specified only by name, the member can be specified by name or SID.</p>
<h3>SAM DELMEM &lt;GROUP&gt; &lt;MEMBER&gt;</h3>
<p>Remove a member from a Local group. The group and the member must be specified by name.</p>
<h3>SAM LISTMEM &lt;GROUP&gt;</h3>
<p>List Local group members. The group must be specified by name.</p>
<h3>SAM LIST &lt;users|groups|localgroups|builtin|workstations&gt; [verbose]</h3>
<p>List the specified set of accounts by name. If verbose is specified, the rid and description is also provided for each account.</p>
<h3>Sam Rights List</h3>
<p>List all available privileges.</p>
<h3>SAM RIGHTS GRANT &lt;NAME&gt; &lt;PRIVILEGE&gt;</h3>
<p>Grant one or more privileges to a user.</p>
<h3>SAM RIGHTS REVOKE &lt;NAME&gt; &lt;PRIVILEGE&gt;</h3>
<p>Revoke one or more privileges from a user.</p>
<h3>SAM SHOW &lt;NAME&gt;</h3>
<p>Show the full DOMAIN\NAME the SID and the type for the corresponding account.</p>
<h3>SAM SET HOMEDIR &lt;NAME&gt; &lt;DIRECTORY&gt;</h3>
<p>Set the home directory for a user account.</p>
<h3>SAM SET PROFILEPATH &lt;NAME&gt; &lt;PATH&gt;</h3>
<p>Set the profile path for a user account.</p>
<h3>SAM SET COMMENT &lt;NAME&gt; &lt;COMMENT&gt;</h3>
<p>Set the comment for a user or group account.</p>
<h3>SAM SET FULLNAME &lt;NAME&gt; &lt;FULL NAME&gt;</h3>
<p>Set the full name for a user account.</p>
<h3>SAM SET LOGONSCRIPT &lt;NAME&gt; &lt;SCRIPT&gt;</h3>
<p>Set the logon script for a user account.</p>
<h3>SAM SET HOMEDRIVE &lt;NAME&gt; &lt;DRIVE&gt;</h3>
<p>Set the home drive for a user account.</p>
<h3>SAM SET WORKSTATIONS &lt;NAME&gt; &lt;WORKSTATIONS&gt;</h3>
<p>Set the workstations a user account is allowed to log in from.</p>
<h3>SAM SET DISABLE &lt;NAME&gt;</h3>
<p>Set the &quot;disabled&quot; flag for a user account.</p>
<h3>SAM SET PWNOTREQ &lt;NAME&gt;</h3>
<p>Set the &quot;password not required&quot; flag for a user account.</p>
<h3>SAM SET AUTOLOCK &lt;NAME&gt;</h3>
<p>Set the &quot;autolock&quot; flag for a user account.</p>
<h3>SAM SET PWNOEXP &lt;NAME&gt;</h3>
<p>Set the &quot;password do not expire&quot; flag for a user account.</p>
<h3>SAM SET PWDMUSTCHANGENOW &lt;NAME&gt; [yes|no]</h3>
<p>Set or unset the &quot;password must change&quot; flag for a user account.</p>
<h3>Sam Policy List</h3>
<p>List the available account policies.</p>
<h3>SAM POLICY SHOW &lt;account policy&gt;</h3>
<p>Show the account policy value.</p>
<h3>SAM POLICY SET &lt;account policy&gt; &lt;value&gt;</h3>
<p>Set a value for the account policy. Valid values can be: &quot;forever&quot;, &quot;never&quot;, &quot;off&quot;, or a number.</p>
<h3>Sam Provision</h3>
<p>Only available if ldapsam:editposix is set and winbindd is running. Properly populates the ldap tree with the basic accounts (Administrator) and groups (Domain Users, Domain Admins, Domain Guests) on the ldap tree.</p>
<h3>IDMAP DUMP &lt;local tdb file name&gt;</h3>
<p>Dumps the mappings contained in the local tdb file specified. This command is useful to dump only the mappings produced by the idmap_tdb backend.</p>
<h3>IDMAP RESTORE [input file]</h3>
<p>Restore the mappings from the specified file or stdin.</p>
<h3>IDMAP SET SECRET &lt;DOMAIN&gt; &lt;secret&gt;</h3>
<p>Store a secret for the specified domain, used primarily for domains that use idmap_ldap as a backend. In this case the secret is used as the password for the user DN used to bind to the ldap server.</p>
<h3>IDMAP SET RANGE &lt;RANGE&gt; &lt;SID&gt; [index] [&#8211;db=&lt;DB&gt;]</h3>
<p>Store a domain-range mapping for a given domain (and index) in autorid database.</p>
<h3>IDMAP SET CONFIG &lt;config&gt; [&#8211;db=&lt;DB&gt;]</h3>
<p>Update CONFIG entry in autorid database.</p>
<h3>IDMAP GET RANGE &lt;SID&gt; [index] [&#8211;db=&lt;DB&gt;]</h3>
<p>Get the range for a given domain and index from autorid database.</p>
<h3>IDMAP GET RANGES [&lt;SID&gt;] [&#8211;db=&lt;DB&gt;]</h3>
<p>Get ranges for all domains or for one identified by given SID.</p>
<h3>IDMAP GET CONFIG [&#8211;db=&lt;DB&gt;]</h3>
<p>Get CONFIG entry from autorid database.</p>
<h3>IDMAP DELETE MAPPING [-f] [&#8211;db=&lt;DB&gt;] &lt;ID&gt;</h3>
<p>Delete a mapping sid &lt;-&gt; gid or sid &lt;-&gt; uid from the IDMAP database. The mapping is given by &lt;ID&gt; which may either be a sid: S-x-&#8230;, a gid: &quot;GID number&quot; or a uid: &quot;UID number&quot;. Use -f to delete an invalid partial mapping &lt;ID&gt; -&gt; xx </p>
<p> Use &quot;smbcontrol all idmap &#8230;&quot; to notify running smbd instances. See the <code><a href="/docs/linux/man/1-smbcontrol/">smbcontrol</a></code>(1) manpage for details.</p>
<h3>IDMAP DELETE RANGE [-f] [&#8211;db=&lt;TDB&gt;] &lt;RANGE&gt;|(&lt;SID&gt; [&lt;INDEX&gt;])</h3>
<p>Delete a domain range mapping identified by &#8216;RANGE&#8217; or &quot;domain SID and INDEX&quot; from autorid database. Use -f to delete invalid mappings.</p>
<h3>IDMAP DELETE RANGES [-f] [&#8211;db=&lt;TDB&gt;] &lt;SID&gt;</h3>
<p>Delete all domain range mappings for a domain identified by SID. Use -f to delete invalid mappings.</p>
<h3>IDMAP CHECK [-v] [-r] [-a] [-T] [-f] [-l] [&#8211;db=&lt;DB&gt;]</h3>
<p>Check and repair the IDMAP database. If no option is given a read only check of the database is done. Among others an interactive or automatic repair mode may be chosen with one of the following options: </p>
<p> -r|&#8211;repair</p>
<dl>
<dd>Interactive repair mode, ask a lot of questions.</dl>
<p> -a|&#8211;auto</p>
<dl>
<dd>Noninteractive repair mode, use default answers.</dl>
<p> -v|&#8211;verbose</p>
<dl>
<dd>Produce more output.</dl>
<p> -f|&#8211;force</p>
<dl>
<dd>Try to apply changes, even if they do not apply cleanly.</dl>
<p> -T|&#8211;test</p>
<dl>
<dd>Dry run, show what changes would be made but don&#8217;t touch anything.</dl>
<p> -l|&#8211;lock</p>
<dl>
<dd>Lock the database while doing the check.</dl>
<p> &#8211;db &lt;DB&gt;</p>
<dl>
<dd>Check the specified database.</dl>
<dl>
<dd></dl>
<p> It reports about the finding of the following errors: </p>
<p> Missing reverse mapping:</p>
<dl>
<dd>A record with mapping A-&gt;B where there is no B-&gt;A. Default action in repair mode is to &quot;fix&quot; this by adding the reverse mapping.</dl>
<p> Invalid mapping:</p>
<dl>
<dd>A record with mapping A-&gt;B where B-&gt;C. Default action is to &quot;delete&quot; this record.</dl>
<p> Missing or invalid HWM:</p>
<dl>
<dd>A high water mark is not at least equal to the largest ID in the database. Default action is to &quot;fix&quot; this by setting it to the largest ID found +1.</dl>
<p> Invalid record:</p>
<dl>
<dd>Something we failed to parse. Default action is to &quot;edit&quot; it in interactive and &quot;delete&quot; it in automatic mode.</dl>
<h3>Usershare</h3>
<p>Starting with version 3.0.23, a Samba server now supports the ability for non-root users to add user defined shares to be exported using the &quot;net usershare&quot; commands. </p>
<p> To set this up, first set up your smb.conf by adding to the [global] section: usershare path = /usr/local/samba/lib/usershares Next create the directory /usr/local/samba/lib/usershares, change the owner to root and set the group owner to the UNIX group who should have the ability to create usershares, for example a group called &quot;serverops&quot;. Set the permissions on /usr/local/samba/lib/usershares to 01770. (Owner and group all access, no access for others, plus the sticky bit, which means that a file in that directory can be renamed or deleted only by the owner of the file). Finally, tell smbd how many usershares you will allow by adding to the [global] section of smb.conf a line such as : usershare max shares = 100. To allow 100 usershare definitions. Now, members of the UNIX group &quot;serverops&quot; can create user defined shares on demand using the commands below. </p>
<p> The usershare commands are:</p>
<dl>
<dd>net usershare add sharename path [comment [acl] [guest_ok=[y|n]]] &#8211; to add or change a user defined share.</dl>
<dl>
<dd>net usershare delete sharename &#8211; to delete a user defined share.</dl>
<dl>
<dd>net usershare info [-l|&#8211;long] [wildcard sharename] &#8211; to print info about a user defined share.</dl>
<dl>
<dd>net usershare list [-l|&#8211;long] [wildcard sharename] &#8211; to list user defined shares.</dl>
<h3>USERSHARE ADD sharename path [comment] [acl] [guest_ok=[y|n]]</h3>
<p>Add or replace a new user defined share, with name &quot;sharename&quot;. </p>
<p> &quot;path&quot; specifies the absolute pathname on the system to be exported. Restrictions may be put on this, see the global smb.conf parameters: &quot;usershare owner only&quot;, &quot;usershare prefix allow list&quot;, and &quot;usershare prefix deny list&quot;. </p>
<p> The optional &quot;comment&quot; parameter is the comment that will appear on the share when browsed to by a client. </p>
<p> The optional &quot;acl&quot; field specifies which users have read and write access to the entire share. Note that guest connections are not allowed unless the smb.conf parameter &quot;usershare allow guests&quot; has been set. The definition of a user defined share acl is: &quot;user:permission&quot;, where user is a valid username on the system and permission can be &quot;F&quot;, &quot;R&quot;, or &quot;D&quot;. &quot;F&quot; stands for &quot;full permissions&quot;, ie. read and write permissions. &quot;D&quot; stands for &quot;deny&quot; for a user, ie. prevent this user from accessing this share. &quot;R&quot; stands for &quot;read only&quot;, ie. only allow read access to this share (no creation of new files or directories or writing to files). </p>
<p> The default if no &quot;acl&quot; is given is &quot;Everyone:R&quot;, which means any authenticated user has read-only access. </p>
<p> The optional &quot;guest_ok&quot; has the same effect as the parameter of the same name in smb.conf, in that it allows guest access to this user defined share. This parameter is only allowed if the global parameter &quot;usershare allow guests&quot; has been set to true in the smb.conf. </p>
<p> There is no separate command to modify an existing user defined share, just use the &quot;net usershare add [sharename]&quot; command using the same sharename as the one you wish to modify and specify the new options you wish. The Samba smbd daemon notices user defined share modifications at connect time so will see the change immediately, there is no need to restart smbd on adding, deleting or changing a user defined share.</p>
<h3>USERSHARE DELETE sharename</h3>
<p>Deletes the user defined share by name. The Samba smbd daemon immediately notices this change, although it will not disconnect any users currently connected to the deleted share.</p>
<h3>USERSHARE INFO [-l|&#8211;long] [wildcard sharename]</h3>
<p>Get info on user defined shares owned by the current user matching the given pattern, or all users. </p>
<p> net usershare info on its own dumps out info on the user defined shares that were created by the current user, or restricts them to share names that match the given wildcard pattern (&#8216;*&#8217; matches one or more characters, &#8216;?&#8217; matches only one character). If the &#8216;-l&#8217; or &#8216;&#8211;long&#8217; option is also given, it prints out info on user defined shares created by other users. </p>
<p> The information given about a share looks like: [foobar] path=/home/jeremy comment=testme usershare_acl=Everyone:F guest_ok=n And is a list of the current settings of the user defined share that can be modified by the &quot;net usershare add&quot; command.</p>
<h3>USERSHARE LIST [-l|&#8211;long] wildcard sharename</h3>
<p>List all the user defined shares owned by the current user matching the given pattern, or all users. </p>
<p> net usershare list on its own list out the names of the user defined shares that were created by the current user, or restricts the list to share names that match the given wildcard pattern (&#8216;*&#8217; matches one or more characters, &#8216;?&#8217; matches only one character). If the &#8216;-l&#8217; or &#8216;&#8211;long&#8217; option is also given, it includes the names of user defined shares created by other users.</p>
<h3>[Rpc] Conf</h3>
<p>Starting with version 3.2.0, a Samba server can be configured by data stored in registry. This configuration data can be edited with the new &quot;net conf&quot; commands. There is also the possibility to configure a remote Samba server by enabling the RPC conf mode and specifying the address of the remote server. </p>
<p> The deployment of this configuration data can be activated in two levels from the <i>smb.conf</i> file: Share definitions from registry are activated by setting <i>registry shares</i> to &#8220;yes&#8221; in the [global] section and global configuration options are activated by setting m[blue]<code>include = registry</code>m[] in the [global] section for a mixed configuration or by setting m[blue]<code>config backend = registry</code>m[] in the [global] section for a registry-only configuration. See the <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5) manpage for details. </p>
<p> The conf commands are:</p>
<dl>
<dd>net [rpc] conf list &#8211; Dump the complete configuration in smb.conf like format.</dl>
<dl>
<dd>net [rpc] conf import &#8211; Import configuration from file in smb.conf format.</dl>
<dl>
<dd>net [rpc] conf listshares &#8211; List the registry shares.</dl>
<dl>
<dd>net [rpc] conf drop &#8211; Delete the complete configuration from registry.</dl>
<dl>
<dd>net [rpc] conf showshare &#8211; Show the definition of a registry share.</dl>
<dl>
<dd>net [rpc] conf addshare &#8211; Create a new registry share.</dl>
<dl>
<dd>net [rpc] conf delshare &#8211; Delete a registry share.</dl>
<dl>
<dd>net [rpc] conf setparm &#8211; Store a parameter.</dl>
<dl>
<dd>net [rpc] conf getparm &#8211; Retrieve the value of a parameter.</dl>
<dl>
<dd>net [rpc] conf delparm &#8211; Delete a parameter.</dl>
<dl>
<dd>net [rpc] conf getincludes &#8211; Show the includes of a share definition.</dl>
<dl>
<dd>net [rpc] conf setincludes &#8211; Set includes for a share.</dl>
<dl>
<dd>net [rpc] conf delincludes &#8211; Delete includes from a share definition.</dl>
<h3>[Rpc] Conf List</h3>
<p>Print the configuration data stored in the registry in a smb.conf-like format to standard output.</p>
<h3>[RPC] CONF IMPORT [&#8211;test|-T] filename [section]</h3>
<p>This command imports configuration from a file in smb.conf format. If a section encountered in the input file is present in registry, its contents is replaced. Sections of registry configuration that have no counterpart in the input file are not affected. If you want to delete these, you will have to use the &quot;net conf drop&quot; or &quot;net conf delshare&quot; commands. Optionally, a section may be specified to restrict the effect of the import command to that specific section. A test mode is enabled by specifying the parameter &quot;-T&quot; on the commandline. In test mode, no changes are made to the registry, and the resulting configuration is printed to standard output instead.</p>
<h3>[Rpc] Conf Listshares</h3>
<p>List the names of the shares defined in registry.</p>
<h3>[Rpc] Conf Drop</h3>
<p>Delete the complete configuration data from registry.</p>
<h3>[RPC] CONF SHOWSHARE sharename</h3>
<p>Show the definition of the share or section specified. It is valid to specify &quot;global&quot; as sharename to retrieve the global configuration options from registry.</p>
<h3>[RPC] CONF ADDSHARE sharename path [writeable={y|N} [guest_ok={y|N} [comment]]]</h3>
<p>Create a new share definition in registry. The sharename and path have to be given. The share name may <i>not</i> be &quot;global&quot;. Optionally, values for the very common options &quot;writeable&quot;, &quot;guest ok&quot; and a &quot;comment&quot; may be specified. The same result may be obtained by a sequence of &quot;net conf setparm&quot; commands.</p>
<h3>[RPC] CONF DELSHARE sharename</h3>
<p>Delete a share definition from registry.</p>
<h3>[RPC] CONF SETPARM section parameter value</h3>
<p>Store a parameter in registry. The section may be global or a sharename. The section is created if it does not exist yet.</p>
<h3>[RPC] CONF GETPARM section parameter</h3>
<p>Show a parameter stored in registry.</p>
<h3>[RPC] CONF DELPARM section parameter</h3>
<p>Delete a parameter stored in registry.</p>
<h3>[RPC] CONF GETINCLUDES section</h3>
<p>Get the list of includes for the provided section (global or share). </p>
<p> Note that due to the nature of the registry database and the nature of include directives, the includes need special treatment: Parameters are stored in registry by the parameter name as valuename, so there is only ever one instance of a parameter per share. Also, a specific order like in a text file is not guaranteed. For all real parameters, this is perfectly ok, but the include directive is rather a meta parameter, for which, in the smb.conf text file, the place where it is specified between the other parameters is very important. This can not be achieved by the simple registry smbconf data model, so there is one ordered list of includes per share, and this list is evaluated after all the parameters of the share. </p>
<p> Further note that currently, only files can be included from registry configuration. In the future, there will be the ability to include configuration data from other registry keys.</p>
<h3>[RPC] CONF SETINCLUDES section [filename]+</h3>
<p>Set the list of includes for the provided section (global or share) to the given list of one or more filenames. The filenames may contain the usual smb.conf macros like %I.</p>
<h3>[RPC] CONF DELINCLUDES section</h3>
<p>Delete the list of includes from the provided section (global or share).</p>
<h3>Registry</h3>
<p>Manipulate Samba&#8217;s registry. </p>
<p> The registry commands are:</p>
<dl>
<dd>net registry enumerate &#8211; Enumerate registry keys and values.</dl>
<dl>
<dd>net registry enumerate_recursive &#8211; Enumerate registry key and its subkeys.</dl>
<dl>
<dd>net registry createkey &#8211; Create a new registry key.</dl>
<dl>
<dd>net registry deletekey &#8211; Delete a registry key.</dl>
<dl>
<dd>net registry deletekey_recursive &#8211; Delete a registry key with subkeys.</dl>
<dl>
<dd>net registry getvalue &#8211; Print a registry value.</dl>
<dl>
<dd>net registry getvalueraw &#8211; Print a registry value (raw format).</dl>
<dl>
<dd>net registry setvalue &#8211; Set a new registry value.</dl>
<dl>
<dd>net registry increment &#8211; Increment a DWORD registry value under a lock.</dl>
<dl>
<dd>net registry deletevalue &#8211; Delete a registry value.</dl>
<dl>
<dd>net registry getsd &#8211; Get security descriptor.</dl>
<dl>
<dd>net registry getsd_sdd1 &#8211; Get security descriptor in sddl format.</dl>
<dl>
<dd>net registry setsd_sdd1 &#8211; Set security descriptor from sddl format string.</dl>
<dl>
<dd>net registry import &#8211; Import a registration entries (.reg) file.</dl>
<dl>
<dd>net registry export &#8211; Export a registration entries (.reg) file.</dl>
<dl>
<dd>net registry convert &#8211; Convert a registration entries (.reg) file.</dl>
<dl>
<dd>net registry check &#8211; Check and repair a registry database.</dl>
<h3>REGISTRY ENUMERATE key</h3>
<p>Enumerate subkeys and values of <i>key</i>.</p>
<h3>REGISTRY ENUMERATE_RECURSIVE key</h3>
<p>Enumerate values of <i>key</i> and its subkeys.</p>
<h3>REGISTRY CREATEKEY key</h3>
<p>Create a new <i>key</i> if not yet existing.</p>
<h3>REGISTRY DELETEKEY key</h3>
<p>Delete the given <i>key</i> and its values from the registry, if it has no subkeys.</p>
<h3>REGISTRY DELETEKEY_RECURSIVE key</h3>
<p>Delete the given <i>key</i> and all of its subkeys and values from the registry.</p>
<h3>REGISTRY GETVALUE key name</h3>
<p>Output type and actual value of the value <i>name</i> of the given <i>key</i>.</p>
<h3>REGISTRY GETVALUERAW key name</h3>
<p>Output the actual value of the value <i>name</i> of the given <i>key</i>.</p>
<h3>REGISTRY SETVALUE key name type value &#8230;</h3>
<p>Set the value <i>name</i> of an existing <i>key</i>. <i>type</i> may be one of <i>sz</i>, <i>multi_sz</i> or <i>dword</i>. In case of <i>multi_sz</i> <i>value</i> may be given multiple times.</p>
<h3>REGISTRY INCREMENT key name [inc]</h3>
<p>Increment the DWORD value <i>name</i> of <i>key</i> by <i>inc</i> while holding a g_lock. <i>inc</i> defaults to 1.</p>
<h3>REGISTRY DELETEVALUE key name</h3>
<p>Delete the value <i>name</i> of the given <i>key</i>.</p>
<h3>REGISTRY GETSD key</h3>
<p>Get the security descriptor of the given <i>key</i>.</p>
<h3>REGISTRY GETSD_SDDL key</h3>
<p>Get the security descriptor of the given <i>key</i> as a Security Descriptor Definition Language (SDDL) string.</p>
<h3>REGISTRY SETSD_SDDL keysd</h3>
<p>Set the security descriptor of the given <i>key</i> from a Security Descriptor Definition Language (SDDL) string <i>sd</i>.</p>
<h3>REGISTRY IMPORT file [&#8211;precheck &lt;check-file&gt;] [opt]</h3>
<p>Import a registration entries (.reg) <i>file</i>. </p>
<p> The following options are available: </p>
<p> &#8211;precheck <i>check-file</i></p>
<dl>
<dd>This is a mechanism to check the existence or non-existence of certain keys or values specified in a precheck file before applying the import file. The import file will only be applied if the precheck succeeds. </p>
<p> The check-file follows the normal registry file syntax with the following semantics:</p>
<dl>
<dd>
<dl>
<dd>&bull; &lt;value name&gt;=&lt;value&gt; checks whether the value exists and has the given value.</dl>
<dl>
<dd>&bull; &lt;value name&gt;=- checks whether the value does not exist.</dl>
<dl>
<dd>&bull; [key] checks whether the key exists.</dl>
<dl>
<dd>&bull; [-key] checks whether the key does not exist.</dl>
</dl>
</dl>
<h3>REGISTRY EXPORT keyfile[opt]</h3>
<p>Export a <i>key</i> to a registration entries (.reg) <i>file</i>.</p>
<h3>REGISTRY CONVERT in out [[inopt] outopt]</h3>
<p>Convert a registration entries (.reg) file <i>in</i>.</p>
<h3>REGISTRY CHECK [-ravTl] [-o &lt;ODB&gt;] [&#8211;wipe] [&lt;DB&gt;]</h3>
<p>Check and repair the registry database. If no option is given a read only check of the database is done. Among others an interactive or automatic repair mode may be chosen with one of the following options </p>
<p> -r|&#8211;repair</p>
<dl>
<dd>Interactive repair mode, ask a lot of questions.</dl>
<p> -a|&#8211;auto</p>
<dl>
<dd>Noninteractive repair mode, use default answers.</dl>
<p> -v|&#8211;verbose</p>
<dl>
<dd>Produce more output.</dl>
<p> -T|&#8211;test</p>
<dl>
<dd>Dry run, show what changes would be made but don&#8217;t touch anything.</dl>
<p> -l|&#8211;lock</p>
<dl>
<dd>Lock the database while doing the check.</dl>
<p> &#8211;reg-version={1,2,3}</p>
<dl>
<dd>Specify the format of the registry database. If not given it defaults to the value of the binary or, if an registry.tdb is explizitly stated at the commandline, to the value found in the INFO/version record.</dl>
<p> [&#8211;db] &lt;DB&gt;</p>
<dl>
<dd>Check the specified database.</dl>
<p> -o|&#8211;output &lt;ODB&gt;</p>
<dl>
<dd>Create a new registry database &lt;ODB&gt; instead of modifying the input. If &lt;ODB&gt; is already existing &#8211;wipe may be used to overwrite it.</dl>
<p> &#8211;wipe</p>
<dl>
<dd>Replace the registry database instead of modifying the input or overwrite an existing output database.</dl>
<dl>
<dd></dl>
<h3>Eventlog</h3>
<p>Starting with version 3.4.0 net can read, dump, import and export native win32 eventlog files (usually *.evt). evt files are used by the native Windows eventviewer tools. </p>
<p> The import and export of evt files can only succeed when <i>eventlog list</i> is used in <i>smb.conf</i> file. See the <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5) manpage for details. </p>
<p> The eventlog commands are:</p>
<dl>
<dd>net eventlog dump &#8211; Dump a eventlog *.evt file on the screen.</dl>
<dl>
<dd>net eventlog import &#8211; Import a eventlog *.evt into the samba internal tdb based representation of eventlogs.</dl>
<dl>
<dd>net eventlog export &#8211; Export the samba internal tdb based representation of eventlogs into an eventlog *.evt file.</dl>
<h3>EVENTLOG DUMP filename</h3>
<p>Prints a eventlog *.evt file to standard output.</p>
<h3>EVENTLOG IMPORT filename eventlog</h3>
<p>Imports a eventlog *.evt file defined by <i>filename</i> into the samba internal tdb representation of eventlog defined by <i>eventlog</i>. <i>eventlog</i> needs to part of the <i>eventlog list</i> defined in smb.conf. See the <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5) manpage for details.</p>
<h3>EVENTLOG EXPORT filename eventlog</h3>
<p>Exports the samba internal tdb representation of eventlog defined by <i>eventlog</i> to a eventlog *.evt file defined by <i>filename</i>. <i>eventlog</i> needs to part of the <i>eventlog list</i> defined in smb.conf. See the <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5) manpage for details.</p>
<h3>Dom</h3>
<p>Starting with version 3.2.0 Samba has support for remote join and unjoin APIs, both client and server-side. Windows supports remote join capabilities since Windows 2000. </p>
<p> In order for Samba to be joined or unjoined remotely an account must be used that is either member of the Domain Admins group, a member of the local Administrators group or a user that is granted the SeMachineAccountPrivilege privilege. </p>
<p> The client side support for remote join is implemented in the net dom commands which are:</p>
<dl>
<dd>net dom join &#8211; Join a remote computer into a domain.</dl>
<dl>
<dd>net dom unjoin &#8211; Unjoin a remote computer from a domain.</dl>
<dl>
<dd>net dom renamecomputer &#8211; Renames a remote computer joined to a domain.</dl>
<h3>DOM JOIN<tt>&nbsp;<wbr>&nbsp;</tt>domain=DOMAIN ou=OU account=ACCOUNT password=PASSWORD reboot</h3>
<p>Joins a computer into a domain. This command supports the following additional parameters:</p>
<dl>
<dd>
<dl>
<dd>&bull; <i>DOMAIN</i> can be a NetBIOS domain name (also known as short domain name) or a DNS domain name for Active Directory Domains. As in Windows, it is also possible to control which Domain Controller to use. This can be achieved by appending the DC name using the \ separator character. Example: MYDOM\MYDC. The <i>DOMAIN</i> parameter cannot be NULL.</dl>
<dl>
<dd>&bull; <i>OU</i> can be set to a RFC 1779 LDAP DN, like <i>ou=mymachines,cn=Users,dc=example,dc=com</i> in order to create the machine account in a non-default LDAP container. This optional parameter is only supported when joining Active Directory Domains.</dl>
<dl>
<dd>&bull; <i>ACCOUNT</i> defines a domain account that will be used to join the machine to the domain. This domain account needs to have sufficient privileges to join machines.</dl>
<dl>
<dd>&bull; <i>PASSWORD</i> defines the password for the domain account defined with <i>ACCOUNT</i>.</dl>
<dl>
<dd>&bull; <i>REBOOT</i> is an optional parameter that can be set to reboot the remote machine after successful join to the domain.</dl>
</dl>
<p> Note that you also need to use standard net parameters to connect and authenticate to the remote machine that you want to join. These additional parameters include: -S computer and -U user. </p>
<p> Example: net dom join -S xp -U XP\administrator%secret domain=MYDOM account=MYDOM\administrator password=topsecret reboot. </p>
<p> This example would connect to a computer named XP as the local administrator using password secret, and join the computer into a domain called MYDOM using the MYDOM domain administrator account and password topsecret. After successful join, the computer would reboot.</p>
<h3>DOM UNJOIN account=ACCOUNT password=PASSWORD reboot</h3>
<p>Unjoins a computer from a domain. This command supports the following additional parameters:</p>
<dl>
<dd>
<dl>
<dd>&bull; <i>ACCOUNT</i> defines a domain account that will be used to unjoin the machine from the domain. This domain account needs to have sufficient privileges to unjoin machines.</dl>
<dl>
<dd>&bull; <i>PASSWORD</i> defines the password for the domain account defined with <i>ACCOUNT</i>.</dl>
<dl>
<dd>&bull; <i>REBOOT</i> is an optional parameter that can be set to reboot the remote machine after successful unjoin from the domain.</dl>
</dl>
<p> Note that you also need to use standard net parameters to connect and authenticate to the remote machine that you want to unjoin. These additional parameters include: -S computer and -U user. </p>
<p> Example: net dom unjoin -S xp -U XP\administrator%secret account=MYDOM\administrator password=topsecret reboot. </p>
<p> This example would connect to a computer named XP as the local administrator using password secret, and unjoin the computer from the domain using the MYDOM domain administrator account and password topsecret. After successful unjoin, the computer would reboot.</p>
<h3>DOM RENAMECOMPUTER newname=NEWNAME account=ACCOUNT password=PASSWORD reboot</h3>
<p>Renames a computer that is joined to a domain. This command supports the following additional parameters:</p>
<dl>
<dd>
<dl>
<dd>&bull; <i>NEWNAME</i> defines the new name of the machine in the domain.</dl>
<dl>
<dd>&bull; <i>ACCOUNT</i> defines a domain account that will be used to rename the machine in the domain. This domain account needs to have sufficient privileges to rename machines.</dl>
<dl>
<dd>&bull; <i>PASSWORD</i> defines the password for the domain account defined with <i>ACCOUNT</i>.</dl>
<dl>
<dd>&bull; <i>REBOOT</i> is an optional parameter that can be set to reboot the remote machine after successful rename in the domain.</dl>
</dl>
<p> Note that you also need to use standard net parameters to connect and authenticate to the remote machine that you want to rename in the domain. These additional parameters include: -S computer and -U user. </p>
<p> Example: net dom renamecomputer -S xp -U XP\administrator%secret newname=XPNEW account=MYDOM\administrator password=topsecret reboot. </p>
<p> This example would connect to a computer named XP as the local administrator using password secret, and rename the joined computer to XPNEW using the MYDOM domain administrator account and password topsecret. After successful rename, the computer would reboot.</p>
<h3>G_Lock</h3>
<p>Manage global locks.</p>
<h3>G_LOCK DO lockname timeout command</h3>
<p>Execute a shell command under a global lock. This might be useful to define the order in which several shell commands will be executed. The locking information is stored in a file called g_lock.tdb. In setups with CTDB running, the locking information will be available on all cluster nodes.</p>
<dl>
<dd>
<dl>
<dd>&bull; <i>LOCKNAME</i> defines the name of the global lock.</dl>
<dl>
<dd>&bull; <i>TIMEOUT</i> defines the timeout.</dl>
<dl>
<dd>&bull; <i>COMMAND</i> defines the shell command to execute.</dl>
</dl>
<h3>G_Lock Locks</h3>
<p>Print a list of all currently existing locknames.</p>
<h3>G_LOCK DUMP lockname</h3>
<p>Dump the locking table of a certain global lock.</p>
<h3>Tdb</h3>
<p>Print information from tdb records.</p>
<h3>TDB LOCKING key [DUMP]</h3>
<p>List sharename, filename and number of share modes for a record from locking.tdb. With the optional DUMP options, dump the complete record.</p>
<dl>
<dd>
<dl>
<dd>&bull; <i>KEY</i> Key of the tdb record as hex string.</dl>
</dl>
<h3>Help [Command]</h3>
<p>Gives usage information for the specified command.</p>
<h2>Version</h2>
<p>This man page is complete for version 3 of the Samba suite.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed. </p>
<p> The net manpage was written by Jelmer Vernooij.</p>
