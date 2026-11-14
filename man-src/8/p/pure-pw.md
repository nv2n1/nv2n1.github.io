---
title: "pure-pw(8)"
name: "pure-pw"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pure-pw/"
description: "pure-pw – Manage virtual users files for Pure-FTPd"
---

<p>pure-pw &#8211; Manage virtual users files for Pure-FTPd</p>
<h2>Syntax</h2>
<p>pure-pw useradd login [-f passwd_file] [-F puredb_file] -u uid [-g gid]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-D/-d home_directory&nbsp;<wbr>[-c gecos]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[-t download_bandwidth]&nbsp;<wbr>[-T upload_bandwidth]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[-n max number_of_files]&nbsp;<wbr>[-N max_Mbytes]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[-q upload_ratio]&nbsp;<wbr>[-Q download_ratio]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[-r&nbsp;<wbr>&lt;allow client host&gt;/&lt;mask&gt;[,&lt;ip&gt;/&lt;mask&gt;]&#8230;]&nbsp;<wbr>[-R&nbsp;<wbr>&lt;deny client host&gt;/&lt;mask&gt;[,&lt;ip&gt;/&lt;mask&gt;]&#8230;]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[-i&nbsp;<wbr>&lt;allow local host&gt;/&lt;mask&gt;[,&lt;ip&gt;/&lt;mask&gt;]&#8230;]&nbsp;<wbr>[-I&nbsp;<wbr>&lt;deny local host&gt;/&lt;mask&gt;[,&lt;ip&gt;/&lt;mask&gt;]&#8230;]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[-y&nbsp;<wbr>&lt;max number of concurrent sessions&gt;]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[-z&nbsp;<wbr>&lt;hhmm&gt;-&lt;hhmm&gt;]&nbsp;<wbr>[-m]<br />
 pure-pw usermod login [-f passwd_file] [-F puredb_file] [-u uid] [-g gid]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-D/-d home_directory -[c gecos]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[-t download_bandwidth]&nbsp;<wbr>[-T upload_bandwidth]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[-n max_number_of_files]&nbsp;<wbr>[-N max_Mbytes]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[-q upload_ratio]&nbsp;<wbr>[-Q download_ratio]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[-r&nbsp;<wbr>&lt;allow client host&gt;/&lt;mask&gt;[,&lt;ip&gt;/&lt;mask&gt;]&#8230;]&nbsp;<wbr>[-R&nbsp;<wbr>&lt;deny client host&gt;/&lt;mask&gt;[,&lt;ip&gt;/&lt;mask&gt;]&#8230;]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[-i&nbsp;<wbr>&lt;allow local host&gt;/&lt;mask&gt;[,&lt;ip&gt;/&lt;mask&gt;]&#8230;]&nbsp;<wbr>[-I&nbsp;<wbr>&lt;deny local host&gt;/&lt;mask&gt;[,&lt;ip&gt;/&lt;mask&gt;]&#8230;]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[-y&nbsp;<wbr>&lt;max number of concurrent sessions&gt;]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[-z&nbsp;<wbr>&lt;hhmm&gt;-&lt;hhmm&gt;]&nbsp;<wbr>[-m]<br />
 pure-pw userdel login [-f passwd_file] [-F puredb_file] [-m]<br />
 pure-pw passwd login [-f passwd_file] [-F puredb_file] [-m]<br />
 pure-pw show login [-f passwd_file] [-m]<br />
 pure-pw mkdb [&lt;puredb_database_file&gt; [-f passwd_file]] [-F puredb_file]<br />
 pure-pw list [-f passwd_file]</p>
<h2>Description</h2>
<p>Virtual users is a simple mechanism to store a list of users, with their password, name, uid, directory, etc. It&#8217;s just like /etc/passwd. But it&#8217;s not /etc/passwd. It&#8217;s a different file, only for FTP.<br />
 It means that you can easily create FTP-only accounts without messing your system accounts.<br />
 Additionnaly, virtual users files can store individual quotas, ratios, bandwidth, etc. System accounts can&#8217;t do this.<br />
 Thousands of virtual users can share the same system user, as long as they all are chrooted, and they have their own home directory.</p>
<h2>Files</h2>
<p><i>/etc/pure-ftpd/pureftpd.passwd</i><br />
 <i>/etc/pure-ftpd/pureftpd.pdb</i></p>
<h2>Environment Variables</h2>
<p><i>PURE_PASSWDFILE</i> If this variable is defined, this is the default value for the text password file. Without this variable, /etc/pure-ftpd/pureftpd.passwd is assumed.<br />
 <i>PURE_DBFILE</i> If this variable is defined, this is the default value for the PureDB password file. Without this variable, /etc/pure-ftpd/pureftpd.pdb is assumed.</p>
<h2>Examples</h2>
<p>Please read <a rel="nofollow" href="http://download.pureftpd.org/pub/pure-ftpd/doc/README.Virtual-Users">http://download.pureftpd.org/pub/pure-ftpd/doc/README.Virtual-Users</a></p>
<h2>Authors</h2>
<p>Frank DENIS &lt;j at pureftpd dot org&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-ftp/">ftp</a>(1)</code>, <code><a href="/docs/linux/man/8-pure-ftpd/">pure-ftpd</a>(8)</code> <code><a href="/docs/linux/man/8-pure-ftpwho/">pure-ftpwho</a>(8)</code> <code><a href="/docs/linux/man/8-pure-mrtginfo/">pure-mrtginfo</a>(8)</code> <code><a href="/docs/linux/man/8-pure-uploadscript/">pure-uploadscript</a>(8)</code> <code><a href="/docs/linux/man/8-pure-statsdecode/">pure-statsdecode</a>(8)</code> <code><a href="/docs/linux/man/8-pure-pw/">pure-pw</a>(8)</code> <code><a href="/docs/linux/man/8-pure-quotacheck/">pure-quotacheck</a>(8)</code> <code><a href="/docs/linux/man/8-pure-authd/">pure-authd</a>(8)</code> <code>RFC 959</code>, <code>RFC 2228,</code> <code>RFC 2389</code> and <code>RFC 2428</code>. </p>
