---
title: "vfstest(1)"
name: "vfstest"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vfstest/"
description: "vfstest – tool for testing samba VFS modules"
---

<h2 class="name">NAME</h2>
<p> vfstest &#8211; tool for testing samba VFS modules </p>
<h2>SYNOPSIS</h2>
<dl>
<dt>
<dd>vfstest [-d debuglevel] [-c command] [-l logdir] [-h]</dl>
<h2>DESCRIPTION</h2>
<p> This tool is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> vfstest is a small command line utility that has the ability to test dso samba VFS modules. It gives the user the ability to call the various VFS functions manually and supports cascaded VFS modules.</p>
<h2>OPTIONS</h2>
<p> -c|&#8211;command=command</p>
<dl>
<dt>
<dd> Execute the specified (<code>semicolon</code>-separated) commands. See below for the commands that are available.</dl>
<p> -?|&#8211;help</p>
<dl>
<dt>
<dd> Print a summary of command line options.</dl>
<p> -l|&#8211;logfile=logbasename</p>
<dl>
<dt>
<dd> File name for log/debug files. The extension <code>&#8216;.client&#8217;</code> will be appended. The log file is never removed by the client.</dl>
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
<h2>COMMANDS</h2>
<p> <i>VFS COMMANDS</i> </p>
<dl>
<dt>
<dd> &bull; load &lt;module.so&gt; &#8211; Load specified VFS module</dl>
<dl>
<dt>
<dd> &bull; populate &lt;char&gt; &lt;size&gt; &#8211; Populate a data buffer with the specified data</dl>
<dl>
<dt>
<dd> &bull; showdata [&lt;offset&gt; &lt;len&gt;] &#8211; Show data currently in data buffer</dl>
<dl>
<dt>
<dd> &bull; connect &#8211; VFS connect()</dl>
<dl>
<dt>
<dd> &bull; disconnect &#8211; VFS disconnect()</dl>
<dl>
<dt>
<dd> &bull; disk_free &#8211; VFS disk_free()</dl>
<dl>
<dt>
<dd> &bull; opendir &#8211; VFS opendir()</dl>
<dl>
<dt>
<dd> &bull; readdir &#8211; VFS readdir()</dl>
<dl>
<dt>
<dd> &bull; mkdir &#8211; VFS mkdir()</dl>
<dl>
<dt>
<dd> &bull; rmdir &#8211; VFS rmdir()</dl>
<dl>
<dt>
<dd> &bull; closedir &#8211; VFS closedir()</dl>
<dl>
<dt>
<dd> &bull; open &#8211; VFS open()</dl>
<dl>
<dt>
<dd> &bull; close &#8211; VFS close()</dl>
<dl>
<dt>
<dd> &bull; read &#8211; VFS read()</dl>
<dl>
<dt>
<dd> &bull; write &#8211; VFS write()</dl>
<dl>
<dt>
<dd> &bull; lseek &#8211; VFS lseek()</dl>
<dl>
<dt>
<dd> &bull; rename &#8211; VFS rename()</dl>
<dl>
<dt>
<dd> &bull; fsync &#8211; VFS fsync()</dl>
<dl>
<dt>
<dd> &bull; stat &#8211; VFS stat()</dl>
<dl>
<dt>
<dd> &bull; fstat &#8211; VFS fstat()</dl>
<dl>
<dt>
<dd> &bull; lstat &#8211; VFS lstat()</dl>
<dl>
<dt>
<dd> &bull; unlink &#8211; VFS unlink()</dl>
<dl>
<dt>
<dd> &bull; chmod &#8211; VFS chmod()</dl>
<dl>
<dt>
<dd> &bull; fchmod &#8211; VFS fchmod()</dl>
<dl>
<dt>
<dd> &bull; chown &#8211; VFS chown()</dl>
<dl>
<dt>
<dd> &bull; fchown &#8211; VFS fchown()</dl>
<dl>
<dt>
<dd> &bull; chdir &#8211; VFS chdir()</dl>
<dl>
<dt>
<dd> &bull; getwd &#8211; VFS getwd()</dl>
<dl>
<dt>
<dd> &bull; utime &#8211; VFS utime()</dl>
<dl>
<dt>
<dd> &bull; ftruncate &#8211; VFS ftruncate()</dl>
<dl>
<dt>
<dd> &bull; lock &#8211; VFS lock()</dl>
<dl>
<dt>
<dd> &bull; symlink &#8211; VFS symlink()</dl>
<dl>
<dt>
<dd> &bull; readlink &#8211; VFS readlink()</dl>
<dl>
<dt>
<dd> &bull; link &#8211; VFS link()</dl>
<dl>
<dt>
<dd> &bull; mknod &#8211; VFS mknod()</dl>
<dl>
<dt>
<dd> &bull; realpath &#8211; VFS realpath()</dl>
<dl>
<dt>
<dd> &bull; getxattr &#8211; VFS getxattr()</dl>
<dl>
<dt>
<dd> &bull; listxattr &#8211; VFS listxattr()</dl>
<dl>
<dt>
<dd> &bull; setxattr &#8211; VFS setxattr()</dl>
<dl>
<dt>
<dd> &bull; removexattr &#8211; VFS removexattr()</dl>
<dl>
<dt>
<dd> &bull; fget_nt_acl &#8211; VFS fget_nt_acl()</dl>
<dl>
<dt>
<dd> &bull; get_nt_acl &#8211; VFS get_nt_acl()</dl>
<dl>
<dt>
<dd> &bull; fset_nt_acl &#8211; VFS fset_nt_acl()</dl>
<dl>
<dt>
<dd> &bull; set_nt_acl &#8211; VFS open() and fset_nt_acl()</dl>
<dl>
<dt>
<dd> &bull; fchmod_acl &#8211; VFS fchmod_acl()</dl>
<dl>
<dt>
<dd> &bull; chmod_acl &#8211; VFS chmod_acl()</dl>
<dl>
<dt>
<dd> &bull; sys_acl_get_file &#8211; VFS sys_acl_get_file()</dl>
<dl>
<dt>
<dd> &bull; sys_acl_get_fd &#8211; VFS sys_acl_get_fd()</dl>
<dl>
<dt>
<dd> &bull; sys_acl_blob_get_file &#8211; VFS sys_acl_blob_get_file()</dl>
<dl>
<dt>
<dd> &bull; sys_acl_blob_get_fd &#8211; VFS sys_acl_blob_get_fd()</dl>
<dl>
<dt>
<dd> &bull; sys_acl_delete_def_file &#8211; VFS sys_acl_delete_def_file()</dl>
<dl>
<dt>
<dd> &bull; test_chain &#8211; test chain code</dl>
<dl>
<dt>
<dd> &bull; translate_name &#8211; VFS translate_name()</dl>
<p> <i>GENERAL COMMANDS</i> </p>
<dl>
<dt>
<dd> &bull; conf &lt;smb.conf&gt; &#8211; Load a different configuration file</dl>
<dl>
<dt>
<dd> &bull; help [&lt;command&gt;] &#8211; Get list of commands or info about specified command</dl>
<dl>
<dt>
<dd> &bull; debuglevel &lt;level&gt; &#8211; Set debug level</dl>
<dl>
<dt>
<dd> &bull; freemem &#8211; Free memory currently in use</dl>
<dl>
<dt>
<dd> &bull; exit &#8211; Exit vfstest</dl>
<h2>VERSION</h2>
<p> This man page is correct for version 3 and 4 of the Samba suite.</p>
<h2>AUTHOR</h2>
<p> The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed. </p>
<p> The vfstest man page was written by Jelmer Vernooij. Updated version by Guenter Kukkukk. </p>
<h2>Index</h2>
