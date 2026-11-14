---
title: "sharesec(1)"
name: "sharesec"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sharesec/"
description: "sharesec – Set or get share ACLs"
---

<h2 class="name">NAME</h2>
<p> sharesec &#8211; Set or get share ACLs </p>
<h2>SYNOPSIS</h2>
<dl>
<dt>
<dd>sharesec {sharename} [-r, &#8211;remove=ACL] [-m, &#8211;modify=ACL] [-a, &#8211;add=ACL] [-R, &#8211;replace=ACLs] [-D, &#8211;delete] [-v, &#8211;view] [&#8211;view-all] [-M, &#8211;machine-sid] [-F, &#8211;force] [-d, &#8211;debuglevel=DEBUGLEVEL] [-s, &#8211;configfile=CONFIGFILE] [-l, &#8211;log-basename=LOGFILEBASE] [&#8211;version] [-?, &#8211;help] [&#8211;usage] [-S, &#8211;setsddl=STRING] [-V, &#8211;viewsddl]</dl>
<h2>DESCRIPTION</h2>
<p> This tool is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> The sharesec program manipulates share permissions on SMB file shares.</p>
<h2>OPTIONS</h2>
<p> The following options are available to the sharesec program. The format of ACLs is described in the section ACL FORMAT </p>
<p> -a|&#8211;add=ACL</p>
<dl>
<dt>
<dd> Add the ACEs specified to the ACL list.</dl>
<p> -D|&#8211;delete</p>
<dl>
<dt>
<dd> Delete the entire security descriptor.</dl>
<p> -F|&#8211;force</p>
<dl>
<dt>
<dd> Force storing the ACL.</dl>
<p> -m|&#8211;modify=ACL</p>
<dl>
<dt>
<dd> Modify existing ACEs.</dl>
<p> -M|&#8211;machine-sid</p>
<dl>
<dt>
<dd> Initialize the machine SID.</dl>
<p> -r|&#8211;remove=ACL</p>
<dl>
<dt>
<dd> Remove ACEs.</dl>
<p> -R|&#8211;replace=ACLS</p>
<dl>
<dt>
<dd> Overwrite an existing share permission ACL.</dl>
<p> -v|&#8211;view</p>
<dl>
<dt>
<dd> List a share acl</dl>
<p> &#8211;view-all</p>
<dl>
<dt>
<dd> List all share acls</dl>
<p> -S|&#8211;setsddl=STRING</p>
<dl>
<dt>
<dd> Set security descriptor by providing ACL in SDDL format.</dl>
<p> -V|&#8211;viewsddl</p>
<dl>
<dt>
<dd> List a share acl in SDDL format.</dl>
<p> -?|&#8211;help</p>
<dl>
<dt>
<dd> Print a summary of command line options.</dl>
<p> -d|&#8211;debuglevel=level</p>
<dl>
<dt>
<dd> <i>level</i> is an integer from 0 to 10. The default value if this parameter is not specified is 0. </p>
<p> The higher this value, the more detail will be logged to the log files about the activities of the server. At level 0, only critical errors and serious warnings will be logged. Level 1 is a reasonable level for day-to-day running &#8211; it generates a small amount of information about operations carried out. </p>
<p> Levels above 1 will generate considerable amounts of log data, and should only be used when investigating a problem. Levels above 3 are designed for use only by developers and generate HUGE amounts of log data, most of which is extremely cryptic. </p>
<p> Note that specifying this parameter here will override the m[blue]<code>log level</code>m[] parameter in the smb.conf file.</dl>
<p> -V|&#8211;version</p>
<dl>
<dt>
<dd> Prints the program version number.</dl>
<p> -s|&#8211;configfile=&lt;configuration file&gt;</p>
<dl>
<dt>
<dd> The file specified contains the configuration details required by the server. The information in this file includes server-specific information such as what printcap file to use, as well as descriptions of all the services that the server is to provide. See smb.conf for more information. The default configuration file name is determined at compile time.</dl>
<p> -l|&#8211;log-basename=logdirectory</p>
<dl>
<dt>
<dd> Base directory name for log/debug files. The extension <code>&quot;.progname&quot;</code> will be appended (e.g. log.smbclient, log.smbd, etc&#8230;). The log file is never removed by the client.</dl>
<p> &#8211;option=&lt;name&gt;=&lt;value&gt;</p>
<dl>
<dt>
<dd> Set the <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5) option &quot;&lt;name&gt;&quot; to value &quot;&lt;value&gt;&quot; from the command line. This overrides compiled-in defaults and options read from the configuration file.</dl>
<h2>ACL FORMAT</h2>
<p> The format of an ACL is one or more ACL entries separated by either commas or newlines. An ACL entry is one of the following: </p>
<dl>
<dt>
<dd>
<pre>
        REVISION:&lt;revision number&gt;
        OWNER:&lt;sid or name&gt;
        GROUP:&lt;sid or name&gt;
        ACL:&lt;sid or name&gt;:&lt;type&gt;/&lt;flags&gt;/&lt;mask&gt;
        
</pre>
</dl>
<p> The revision of the ACL specifies the internal Windows NT ACL revision for the security descriptor. If not specified it defaults to 1. Using values other than 1 may cause strange behaviour. </p>
<p> The owner and group specify the owner and group SIDs for the object. Share ACLs do not specify an owner or a group, so these fields are empty. </p>
<p> ACLs specify permissions granted to the SID. This SID can be specified in S-1-x-y-z format or as a name in which case it is resolved against the server on which the file or directory resides. The type, flags and mask values determine the type of access granted to the SID. </p>
<p> The type can be either ALLOWED or DENIED to allow/deny access to the SID. The flags values are generally zero for share ACLs. </p>
<p> The mask is a value which expresses the access right granted to the SID. It can be given as a decimal or hexadecimal value, or by using one of the following text strings which map to the NT file permissions of the same name. </p>
<dl>
<dt>
<dd> &bull; <i>R</i> &#8211; Allow read access</dl>
<dl>
<dt>
<dd> &bull; <i>W</i> &#8211; Allow write access</dl>
<dl>
<dt>
<dd> &bull; <i>X</i> &#8211; Execute permission on the object</dl>
<dl>
<dt>
<dd> &bull; <i>D</i> &#8211; Delete the object</dl>
<dl>
<dt>
<dd> &bull; <i>P</i> &#8211; Change permissions</dl>
<dl>
<dt>
<dd> &bull; <i>O</i> &#8211; Take ownership</dl>
<p> The following combined permissions can be specified: </p>
<dl>
<dt>
<dd> &bull; <i>READ</i> &#8211; Equivalent to &#8216;RX&#8217; permissions</dl>
<dl>
<dt>
<dd> &bull; <i>CHANGE</i> &#8211; Equivalent to &#8216;RXWD&#8217; permissions</dl>
<dl>
<dt>
<dd> &bull; <i>FULL</i> &#8211; Equivalent to &#8216;RWXDPO&#8217; permissions</dl>
<h2>EXIT STATUS</h2>
<p> The sharesec program sets the exit status depending on the success or otherwise of the operations performed. The exit status may be one of the following values. </p>
<p> If the operation succeeded, sharesec returns and exit status of 0. If sharesec couldn&#8217;t connect to the specified server, or there was an error getting or setting the ACLs, an exit status of 1 is returned. If there was an error parsing any command line arguments, an exit status of 2 is returned.</p>
<h2>EXAMPLES</h2>
<p> Add full access for SID <i>S-1-5-21-1866488690-1365729215-3963860297-17724</i> on <i>share</i>: </p>
<dl>
<dt>
<dd>
<pre>
        host:~ # sharesec share -a S-1-5-21-1866488690-1365729215-3963860297-17724:ALLOWED/0/FULL
        
</pre>
</dl>
<p> List all ACEs for <i>share</i>: </p>
<dl>
<dt>
<dd>
<pre>
        host:~ # sharesec share -v
        REVISION:1
        CONTROL:SR|DP
        OWNER:
        GROUP:
        ACL:S-1-1-0:ALLOWED/0x0/FULL
        ACL:S-1-5-21-1866488690-1365729215-3963860297-17724:ALLOWED/0x0/FULL
        
</pre>
</dl>
<h2>VERSION</h2>
<p> This man page is correct for version 3 of the Samba suite.</p>
<h2>AUTHOR</h2>
<p> The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed. </p>
<h2>Index</h2>
