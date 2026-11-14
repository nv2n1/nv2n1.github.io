---
title: "wbinfo(1)"
name: "wbinfo"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wbinfo/"
description: "wbinfo – Query information from winbind daemon"
---

<h2 class="name">NAME</h2>
<p> wbinfo &#8211; Query information from winbind daemon </p>
<h2>SYNOPSIS</h2>
<dl>
<dt>
<dd>wbinfo [-a user%password] [&#8211;all-domains] [&#8211;allocate-gid] [&#8211;allocate-uid] [-c] [&#8211;ccache-save] [&#8211;change-user-password] [-D domain] [&#8211;dc-info domain] [&#8211;domain domain] [&#8211;dsgetdcname domain] [-g] [&#8211;getdcname domain] [&#8211;get-auth-user] [-G gid] [&#8211;gid-info gid] [&#8211;group-info group] [&#8211;help|-?] [-i user] [-I ip] [-K user%password] [&#8211;krb5ccname cctype] [&#8211;lanman] [&#8211;logoff] [&#8211;logoff-uid uid] [&#8211;logoff-user username] [&#8211;lookup-sids] [-m] [-n name] [-N netbios-name] [&#8211;ntlmv1] [&#8211;ntlmv2] [&#8211;online-status] [&#8211;own-domain] [-p] [-P|&#8211;ping-dc] [&#8211;pam-logon user%password] [-r user] [-R|&#8211;lookup-rids] [&#8211;remove-gid-mapping gid,sid] [&#8211;remove-uid-mapping uid,sid] [-s sid] [&#8211;separator] [&#8211;sequence] [&#8211;set-auth-user user%password] [&#8211;set-gid-mapping gid,sid] [&#8211;set-uid-mapping uid,sid] [-S sid] [&#8211;sid-aliases sid] [&#8211;sid-to-fullname sid] [&#8211;sids-to-unix-ids sidlist] [-t] [-u] [&#8211;uid-info uid] [&#8211;usage] [&#8211;user-domgroups sid] [&#8211;user-sidinfo sid] [&#8211;user-sids sid] [-U uid] [-V] [&#8211;verbose] [-Y sid]</dl>
<h2>DESCRIPTION</h2>
<p> This tool is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> The wbinfo program queries and returns information created and used by the <code><a href="/docs/linux/man/8-winbindd/">winbindd</a></code>(8) daemon. </p>
<p> The <code><a href="/docs/linux/man/8-winbindd/">winbindd</a></code>(8) daemon must be configured and running for the wbinfo program to be able to return information.</p>
<h2>OPTIONS</h2>
<p> -a|&#8211;authenticate <i>username%password</i></p>
<dl>
<dt>
<dd> Attempt to authenticate a user via <code><a href="/docs/linux/man/8-winbindd/">winbindd</a></code>(8). This checks both authentication methods and reports its results. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font><br />
 Do not be tempted to use this functionality for authentication in third-party applications. Instead use <code><a href="/docs/linux/man/1-ntlm_auth/">ntlm_auth</a></code>(1). </p>
</dl>
</dl>
<p> &#8211;allocate-gid</p>
<dl>
<dt>
<dd> Get a new GID out of idmap</dl>
<p> &#8211;allocate-uid</p>
<dl>
<dt>
<dd> Get a new UID out of idmap</dl>
<p> &#8211;all-domains</p>
<dl>
<dt>
<dd> List all domains (trusted and own domain).</dl>
<p> -c|&#8211;change-secret</p>
<dl>
<dt>
<dd> Change the trust account password. May be used in conjunction with <code>domain</code> in order to change interdomain trust account passwords.</dl>
<p> &#8211;ccache-save <i>username%password</i></p>
<dl>
<dt>
<dd> Store user and password for ccache.</dl>
<p> &#8211;change-user-password <i>username</i></p>
<dl>
<dt>
<dd> Change the password of a user. The old and new password will be prompted.</dl>
<p> &#8211;dc-info <i>domain</i></p>
<dl>
<dt>
<dd> Displays information about the current domain controller for a domain.</dl>
<p> &#8211;domain <i>name</i></p>
<dl>
<dt>
<dd> This parameter sets the domain on which any specified operations will performed. If special domain name &#8216;.&#8217; is used to represent the current domain to which <code><a href="/docs/linux/man/8-winbindd/">winbindd</a></code>(8) belongs. A &#8216;*&#8217; as the domain name means to enumerate over all domains (NOTE: This can take a long time and use a lot of memory).</dl>
<p> -D|&#8211;domain-info <i>domain</i></p>
<dl>
<dt>
<dd> Show most of the info we have about the specified domain.</dl>
<p> &#8211;dsgetdcname <i>domain</i></p>
<dl>
<dt>
<dd> Find a DC for a domain.</dl>
<p> &#8211;gid-info <i>gid</i></p>
<dl>
<dt>
<dd> Get group info from gid.</dl>
<p> &#8211;group-info <i>group</i></p>
<dl>
<dt>
<dd> Get group info from group name.</dl>
<p> -g|&#8211;domain-groups</p>
<dl>
<dt>
<dd> This option will list all groups available in the Windows NT domain for which the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) daemon is operating in. Groups in all trusted domains can be listed with the &#8211;domain=&#8217;*&#8217; option. Note that this operation does not assign group ids to any groups that have not already been seen by <code><a href="/docs/linux/man/8-winbindd/">winbindd</a></code>(8).</dl>
<p> &#8211;get-auth-user</p>
<dl>
<dt>
<dd> Print username and password used by <code><a href="/docs/linux/man/8-winbindd/">winbindd</a></code>(8) during session setup to a domain controller. Username and password can be set using <code>&#8211;set-auth-user</code>. Only available for root.</dl>
<p> &#8211;getdcname <i>domain</i></p>
<dl>
<dt>
<dd> Get the DC name for the specified domain.</dl>
<p> -G|&#8211;gid-to-sid <i>gid</i></p>
<dl>
<dt>
<dd> Try to convert a UNIX group id to a Windows NT SID. If the gid specified does not refer to one within the idmap gid range then the operation will fail.</dl>
<p> -?</p>
<dl>
<dt>
<dd> Print brief help overview.</dl>
<p> -i|&#8211;user-info <i>user</i></p>
<dl>
<dt>
<dd> Get user info.</dl>
<p> -I|&#8211;WINS-by-ip <i>ip</i></p>
<dl>
<dt>
<dd> The <i>-I</i> option queries <code><a href="/docs/linux/man/8-winbindd/">winbindd</a></code>(8) to send a node status request to get the NetBIOS name associated with the IP address specified by the <i>ip</i> parameter.</dl>
<p> -K|&#8211;krb5auth <i>username%password</i></p>
<dl>
<dt>
<dd> Attempt to authenticate a user via Kerberos.</dl>
<p> &#8211;krb5ccname <i>KRB5CCNAME</i></p>
<dl>
<dt>
<dd> Allows one to request a sepcific kerberos credential cache type used for authentication.</dl>
<p> &#8211;lanman</p>
<dl>
<dt>
<dd> Use lanman cryptography for user authentication.</dl>
<p> &#8211;logoff</p>
<dl>
<dt>
<dd> Logoff a user.</dl>
<p> &#8211;logoff-uid <i>UID</i></p>
<dl>
<dt>
<dd> Define user uid used during logoff request.</dl>
<p> &#8211;logoff-user <i>USERNAME</i></p>
<dl>
<dt>
<dd> Define username used during logoff request.</dl>
<p> &#8211;lookup-sids <i>SID1,SID2&#8230;</i></p>
<dl>
<dt>
<dd> Looks up SIDs. SIDs must be specified as ASCII strings in the traditional Microsoft format. For example, S-1-5-21-1455342024-3071081365-2475485837-500.</dl>
<p> -m|&#8211;trusted-domains</p>
<dl>
<dt>
<dd> Produce a list of domains trusted by the Windows NT server <code><a href="/docs/linux/man/8-winbindd/">winbindd</a></code>(8) contacts when resolving names. This list does not include the Windows NT domain the server is a Primary Domain Controller for.</dl>
<p> -n|&#8211;name-to-sid <i>name</i></p>
<dl>
<dt>
<dd> The <i>-n</i> option queries <code><a href="/docs/linux/man/8-winbindd/">winbindd</a></code>(8) for the SID associated with the name specified. Domain names can be specified before the user name by using the winbind separator character. For example CWDOM1/Administrator refers to the Administrator user in the domain CWDOM1. If no domain is specified then the domain used is the one specified in the <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5)<i>workgroup </i> parameter.</dl>
<p> -N|&#8211;WINS-by-name <i>name</i></p>
<dl>
<dt>
<dd> The <i>-N</i> option queries <code><a href="/docs/linux/man/8-winbindd/">winbindd</a></code>(8) to query the WINS server for the IP address associated with the NetBIOS name specified by the <i>name</i> parameter.</dl>
<p> &#8211;ntlmv1</p>
<dl>
<dt>
<dd> Use NTLMv1 cryptography for user authentication.</dl>
<p> &#8211;ntlmv2</p>
<dl>
<dt>
<dd> Use NTLMv2 cryptography for user authentication. NTLMv2 is the default method, this option is only maintained for compatibility.</dl>
<p> &#8211;online-status <i>domain</i></p>
<dl>
<dt>
<dd> Show whether domains are marked as online or offline. An optional domain argument limits the output to the online status of a given domain.</dl>
<p> &#8211;own-domain</p>
<dl>
<dt>
<dd> List own domain.</dl>
<p> &#8211;pam-logon <i>username%password</i></p>
<dl>
<dt>
<dd> Attempt to authenticate a user in the same way pam_winbind would do.</dl>
<p> -p|&#8211;ping</p>
<dl>
<dt>
<dd> Check whether <code><a href="/docs/linux/man/8-winbindd/">winbindd</a></code>(8) is still alive. Prints out either &#8216;succeeded&#8217; or &#8216;failed&#8217;.</dl>
<p> -P|&#8211;ping-dc</p>
<dl>
<dt>
<dd> Issue a no-effect command to our DC. This checks if our secure channel connection to our domain controller is still alive. It has much less impact than wbinfo -t.</dl>
<p> -r|&#8211;user-groups <i>username</i></p>
<dl>
<dt>
<dd> Try to obtain the list of UNIX group ids to which the user belongs. This only works for users defined on a Domain Controller.</dl>
<p> -R|&#8211;lookup-rids <i>rid1, rid2, rid3&#8230;</i></p>
<dl>
<dt>
<dd> Converts RIDs to names. Uses a comma separated list of rids.</dl>
<p> &#8211;remove-gid-mapping <i>GID,SID</i></p>
<dl>
<dt>
<dd> Removes an existing GID to SID mapping from the database.</dl>
<p> &#8211;remove-uid-mapping <i>UID,SID</i></p>
<dl>
<dt>
<dd> Removes an existing UID to SID mapping from the database.</dl>
<p> -s|&#8211;sid-to-name <i>sid</i></p>
<dl>
<dt>
<dd> Use <i>-s</i> to resolve a SID to a name. This is the inverse of the <i>-n </i> option above. SIDs must be specified as ASCII strings in the traditional Microsoft format. For example, S-1-5-21-1455342024-3071081365-2475485837-500.</dl>
<p> &#8211;separator</p>
<dl>
<dt>
<dd> Get the active winbind separator.</dl>
<p> &#8211;sequence</p>
<dl>
<dt>
<dd> This command has been deprecated. Please use the &#8211;online-status option instead.</dl>
<p> &#8211;set-auth-user <i>username%password</i></p>
<dl>
<dt>
<dd> Store username and password used by <code><a href="/docs/linux/man/8-winbindd/">winbindd</a></code>(8) during session setup to a domain controller. This enables winbindd to operate in a Windows 2000 domain with Restrict Anonymous turned on (a.k.a. Permissions compatible with Windows 2000 servers only).</dl>
<p> &#8211;set-gid-mapping <i>GID,SID</i></p>
<dl>
<dt>
<dd> Create a GID to SID mapping in the database.</dl>
<p> &#8211;set-uid-mapping <i>UID,SID</i></p>
<dl>
<dt>
<dd> Create a UID to SID mapping in the database.</dl>
<p> -S|&#8211;sid-to-uid <i>sid</i></p>
<dl>
<dt>
<dd> Convert a SID to a UNIX user id. If the SID does not correspond to a UNIX user mapped by <code><a href="/docs/linux/man/8-winbindd/">winbindd</a></code>(8) then the operation will fail.</dl>
<p> &#8211;sid-aliases <i>sid</i></p>
<dl>
<dt>
<dd> Get SID aliases for a given SID.</dl>
<p> &#8211;sid-to-fullname <i>sid</i></p>
<dl>
<dt>
<dd> Converts a SID to a full username (DOMAIN
