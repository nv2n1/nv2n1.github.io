---

title: "vfstest(1)"
name: "vfstest"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vfstest/"
description: "vfstest – tool for testing samba VFS modules"
---

<p> vfstest &#8211; tool for testing samba VFS modules </p>
<h2>SYNOPSIS</h2>
<dl>
<dt>
</dt><dd>vfstest [-d debuglevel] [-c command] [-l logdir] [-h]</dd></dl>
<h2>DESCRIPTION</h2>
<p> This tool is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> vfstest is a small command line utility that has the ability to test dso samba VFS modules. It gives the user the ability to call the various VFS functions manually and supports cascaded VFS modules.</p>
<h2>OPTIONS</h2>
<p> -c|&#8211;command=command</p>
<dl>
<dt>
</dt><dd> Execute the specified (<code>semicolon</code>-separated) commands. See below for the commands that are available.</dd></dl>
<p> -?|&#8211;help</p>
<dl>
<dt>
</dt><dd> Print a summary of command line options.</dd></dl>
<p> -l|&#8211;logfile=logbasename</p>
<dl>
<dt>
</dt><dd> File name for log/debug files. The extension <code>&#8216;.client&#8217;</code> will be appended. The log file is never removed by the client.</dd></dl>
<p> -d|&#8211;debuglevel=level</p>
<dl>
<dt>
</dt><dd> <i>level</i> is an integer from 0 to 10. The default value if this parameter is not specified is 0. </dd>
<p> The higher this value, the more detail will be logged to the log files about the activities of the server. At level 0, only critical errors and serious warnings will be logged. Level 1 is a reasonable level for day-to-day running &#8211; it generates a small amount of information about operations carried out. </p>
<p> Levels above 1 will generate considerable amounts of log data, and should only be used when investigating a problem. Levels above 3 are designed for use only by developers and generate HUGE amounts of log data, most of which is extremely cryptic. </p>
<p> Note that specifying this parameter here will override the m[blue]<code>log level</code>m[] parameter in the smb.conf file.</dl>
<p> -V|&#8211;version</p>
<dl>
<dt>
</dt><dd> Prints the program version number.</dd></dl>
<p> -s|&#8211;configfile=&lt;configuration file&gt;</p>
<dl>
<dt>
</dt><dd> The file specified contains the configuration details required by the server. The information in this file includes server-specific information such as what printcap file to use, as well as descriptions of all the services that the server is to provide. See smb.conf for more information. The default configuration file name is determined at compile time.</dd></dl>
<p> -l|&#8211;log-basename=logdirectory</p>
<dl>
<dt>
</dt><dd> Base directory name for log/debug files. The extension <code>&quot;.progname&quot;</code> will be appended (e.g. log.smbclient, log.smbd, etc&#8230;). The log file is never removed by the client.</dd></dl>
<p> &#8211;option=&lt;name&gt;=&lt;value&gt;</p>
<dl>
<dt>
</dt><dd> Set the <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5) option &quot;&lt;name&gt;&quot; to value &quot;&lt;value&gt;&quot; from the command line. This overrides compiled-in defaults and options read from the configuration file.</dd></dl>
<h2>COMMANDS</h2>
<p> <i>VFS COMMANDS</i> </p>
<dl>
<dt>
</dt><dd> &bull; load &lt;module.so&gt; &#8211; Load specified VFS module</dd></dl>
<dl>
<dt>
</dt><dd> &bull; populate &lt;char&gt; &lt;size&gt; &#8211; Populate a data buffer with the specified data</dd></dl>
<dl>
<dt>
</dt><dd> &bull; showdata [&lt;offset&gt; &lt;len&gt;] &#8211; Show data currently in data buffer</dd></dl>
<dl>
<dt>
</dt><dd> &bull; connect &#8211; VFS connect()</dd></dl>
<dl>
<dt>
</dt><dd> &bull; disconnect &#8211; VFS disconnect()</dd></dl>
<dl>
<dt>
</dt><dd> &bull; disk_free &#8211; VFS disk_free()</dd></dl>
<dl>
<dt>
</dt><dd> &bull; opendir &#8211; VFS opendir()</dd></dl>
<dl>
<dt>
</dt><dd> &bull; readdir &#8211; VFS readdir()</dd></dl>
<dl>
<dt>
</dt><dd> &bull; mkdir &#8211; VFS mkdir()</dd></dl>
<dl>
<dt>
</dt><dd> &bull; rmdir &#8211; VFS rmdir()</dd></dl>
<dl>
<dt>
</dt><dd> &bull; closedir &#8211; VFS closedir()</dd></dl>
<dl>
<dt>
</dt><dd> &bull; open &#8211; VFS open()</dd></dl>
<dl>
<dt>
</dt><dd> &bull; close &#8211; VFS close()</dd></dl>
<dl>
<dt>
</dt><dd> &bull; read &#8211; VFS read()</dd></dl>
<dl>
<dt>
</dt><dd> &bull; write &#8211; VFS write()</dd></dl>
<dl>
<dt>
</dt><dd> &bull; lseek &#8211; VFS lseek()</dd></dl>
<dl>
<dt>
</dt><dd> &bull; rename &#8211; VFS rename()</dd></dl>
<dl>
<dt>
</dt><dd> &bull; fsync &#8211; VFS fsync()</dd></dl>
<dl>
<dt>
</dt><dd> &bull; stat &#8211; VFS stat()</dd></dl>
<dl>
<dt>
</dt><dd> &bull; fstat &#8211; VFS fstat()</dd></dl>
<dl>
<dt>
</dt><dd> &bull; lstat &#8211; VFS lstat()</dd></dl>
<dl>
<dt>
</dt><dd> &bull; unlink &#8211; VFS unlink()</dd></dl>
<dl>
<dt>
</dt><dd> &bull; chmod &#8211; VFS chmod()</dd></dl>
<dl>
<dt>
</dt><dd> &bull; fchmod &#8211; VFS fchmod()</dd></dl>
<dl>
<dt>
</dt><dd> &bull; chown &#8211; VFS chown()</dd></dl>
<dl>
<dt>
</dt><dd> &bull; fchown &#8211; VFS fchown()</dd></dl>
<dl>
<dt>
</dt><dd> &bull; chdir &#8211; VFS chdir()</dd></dl>
<dl>
<dt>
</dt><dd> &bull; getwd &#8211; VFS getwd()</dd></dl>
<dl>
<dt>
</dt><dd> &bull; utime &#8211; VFS utime()</dd></dl>
<dl>
<dt>
</dt><dd> &bull; ftruncate &#8211; VFS ftruncate()</dd></dl>
<dl>
<dt>
</dt><dd> &bull; lock &#8211; VFS lock()</dd></dl>
<dl>
<dt>
</dt><dd> &bull; symlink &#8211; VFS symlink()</dd></dl>
<dl>
<dt>
</dt><dd> &bull; readlink &#8211; VFS readlink()</dd></dl>
<dl>
<dt>
</dt><dd> &bull; link &#8211; VFS link()</dd></dl>
<dl>
<dt>
</dt><dd> &bull; mknod &#8211; VFS mknod()</dd></dl>
<dl>
<dt>
</dt><dd> &bull; realpath &#8211; VFS realpath()</dd></dl>
<dl>
<dt>
</dt><dd> &bull; getxattr &#8211; VFS getxattr()</dd></dl>
<dl>
<dt>
</dt><dd> &bull; listxattr &#8211; VFS listxattr()</dd></dl>
<dl>
<dt>
</dt><dd> &bull; setxattr &#8211; VFS setxattr()</dd></dl>
<dl>
<dt>
</dt><dd> &bull; removexattr &#8211; VFS removexattr()</dd></dl>
<dl>
<dt>
</dt><dd> &bull; fget_nt_acl &#8211; VFS fget_nt_acl()</dd></dl>
<dl>
<dt>
</dt><dd> &bull; get_nt_acl &#8211; VFS get_nt_acl()</dd></dl>
<dl>
<dt>
</dt><dd> &bull; fset_nt_acl &#8211; VFS fset_nt_acl()</dd></dl>
<dl>
<dt>
</dt><dd> &bull; set_nt_acl &#8211; VFS open() and fset_nt_acl()</dd></dl>
<dl>
<dt>
</dt><dd> &bull; fchmod_acl &#8211; VFS fchmod_acl()</dd></dl>
<dl>
<dt>
</dt><dd> &bull; chmod_acl &#8211; VFS chmod_acl()</dd></dl>
<dl>
<dt>
</dt><dd> &bull; sys_acl_get_file &#8211; VFS sys_acl_get_file()</dd></dl>
<dl>
<dt>
</dt><dd> &bull; sys_acl_get_fd &#8211; VFS sys_acl_get_fd()</dd></dl>
<dl>
<dt>
</dt><dd> &bull; sys_acl_blob_get_file &#8211; VFS sys_acl_blob_get_file()</dd></dl>
<dl>
<dt>
</dt><dd> &bull; sys_acl_blob_get_fd &#8211; VFS sys_acl_blob_get_fd()</dd></dl>
<dl>
<dt>
</dt><dd> &bull; sys_acl_delete_def_file &#8211; VFS sys_acl_delete_def_file()</dd></dl>
<dl>
<dt>
</dt><dd> &bull; test_chain &#8211; test chain code</dd></dl>
<dl>
<dt>
</dt><dd> &bull; translate_name &#8211; VFS translate_name()</dd></dl>
<p> <i>GENERAL COMMANDS</i> </p>
<dl>
<dt>
</dt><dd> &bull; conf &lt;smb.conf&gt; &#8211; Load a different configuration file</dd></dl>
<dl>
<dt>
</dt><dd> &bull; help [&lt;command&gt;] &#8211; Get list of commands or info about specified command</dd></dl>
<dl>
<dt>
</dt><dd> &bull; debuglevel &lt;level&gt; &#8211; Set debug level</dd></dl>
<dl>
<dt>
</dt><dd> &bull; freemem &#8211; Free memory currently in use</dd></dl>
<dl>
<dt>
</dt><dd> &bull; exit &#8211; Exit vfstest</dd></dl>
<h2>VERSION</h2>
<p> This man page is correct for version 3 and 4 of the Samba suite.</p>
<h2>AUTHOR</h2>
<p> The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed. </p>
<p> The vfstest man page was written by Jelmer Vernooij. Updated version by Guenter Kukkukk. </p>
