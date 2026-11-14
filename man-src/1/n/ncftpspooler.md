---
title: "ncftpspooler(1)"
name: "ncftpspooler"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ncftpspooler/"
description: "ncftpspooler – Global batch FTP job processor daemon"
---

<h2>NAME</h2>
<p> ncftpspooler &#8211; Global batch FTP job processor daemon</p>
<h2>SYNOPSIS</h2>
<p> <code>ncftpspooler</code> -d [<i>options</i>] </p>
<p> <code>ncftpspooler</code> -l [<i>options</i>]</p>
<h2>OPTIONS</h2>
<h3>Command line flags:</h3>
<dl>
<dt><code>-d</code></p>
<dd> Begin background processing of FTP jobs in the designated FTP job queue directory.</p>
<dt><code>-q</code><i> XX</i></p>
<dd> Use this option to specify a directory to use as the FTP job queue instead of the default directory, /var/spool/ncftp.</p>
<dt><code>-o</code><i> XX</i></p>
<dd> Use this option to specify a filename to use as the log file. By default, (and rather inappropriately) the program simply uses a file called <i>log</i> in the job queue directory. If you don&#8217;t want a log, use this option to specify /dev/null.</p>
<dt><code>-l</code></p>
<dd> Lists the contents of the job queue directory.</p>
<dt><code>-s</code><i> XX</i></p>
<dd> When the job queue is empty, the program sleeps 120 seconds and then checks again to see if a new job has been submitted. Use this option to change the number of seconds used for this delay.</dl>
<h2>DESCRIPTION</h2>
<p> The <i>ncftpspooler</i> program evolved from the <i>ncftpbatch</i> program. The <i>ncftpbatch</i> program was originally designed as a &#8220;personal FTP spooler&#8221; which would process a single background job a particular user and exit when it finished; the <i>ncftpspooler</i> program is a &#8220;global FTP spooler&#8221; which stays running and processes background jobs as they are submitted. </p>
<p> The job queue directory is monitored for specially-named and formatted text files. Each file serves as a single FTP job. The name of the job file contains the type of FTP job (<i>get</i> or <i>put</i>), a timestamp indicating the earliest the job should be processed, and optionally some additional information to make it easier to create unique job files (i.e. a sequence number). The contents of the job files have information such as the remote server machine to FTP to, username, password, remote pathname, etc. </p>
<p> Your job queue directory must be readable and writable by the user that you plan to run <i>ncftpspooler</i> as, so that jobs can be removed or renamed within the queue. </p>
<p> More importantly, the user that is running the program will need adequate privileges to access the local files that are involved in the FTPing. I.e., if your spooler is going to be processing jobs which upload files to remote servers, then the user will need read permission on the local files that will be uploaded (and directory access permission the parent directories). Likewise, if your spooler is going to be processing jobs which download files, then the user would need to be able to write to the local directories. </p>
<p> Once you have created your spool directory with appropriate permissions and ownerships, you can run <i>ncftpspooler -d</i> to launch the spooler daemon. You can run additional spoolers if you want to process more than FTP job from the same job queue directory simultaneously. You can then monitor the log file (i.e., using <i>tail -f</i> ) to track the progress of the spooler. Most of the time it won&#8217;t be doing anything, unless job files have appeared in the job queue directory.</p>
<h2>JOB FILE NAMES</h2>
<p> When the <i>ncftpspooler</i> program monitors the job queue directory, it ignores any files that do not follow the naming convention for job files. The job files must be prefixed in the format of <i>X-YYYYMMDD-hhmmss</i> where <i>X</i> denotes a job type, <i>YYYY</i> is the four-digit year, <i>MM</i> is the two-digit month number, <i>DD</i> is the two-digit day of the month, <i>hh</i> is the two-digit hour of the day (00-23), <i>mm</i> is the two-digit minute, and <i>ss</i> is the two-digit second. The date and time represent the earliest time you want the job to be run. </p>
<p> The job type can be <i>g</i> for a get (download from remote host), or <i>p</i> for aput (upload to remote host). </p>
<p> As an example, if you wanted to schedule an upload to occur at 11:45 PM on December 7, 2001, a job file could be named</p>
<dl>
<dt>
<dd>
<p> p-20011207-234500
</dl>
<p> In practice, the job files include additional information such as a sequence number or process ID. This makes it easier to create unique job file names. Here is the same example, with a process ID and a sequence number:</p>
<dl>
<dt>
<dd>
<p> p-20011207-234500-1234-2
</dl>
<p> When submitting job files to the queue directory, be sure to use a dash character after the <i>hhmmss</i> field if you choose to append any additional data to the job file name.</p>
<h2>JOB FILE CONTENTS</h2>
<p> Job files are ordinary text files, so that they can be created by hand. Each line of the file is a key-pair in the format <i>variable</i>=<i>value</i>, or is a comment line beginning with an octothorpe character (<i>#</i>), or is a blank line. Here is an example job file:</p>
<dl>
<dt>
<dd>
<p> # This is a NcFTP spool file entry.<br />
 job-name=g-20011016-100656-008299-1<br />
 op=get<br />
 hostname=<a href="ftp://ftp.freebsd.org">ftp.freebsd.org</a><br />
 xtype=I<br />
 passive=1<br />
 remote-dir=pub/FreeBSD<br />
 local-dir=/tmp<br />
 remote-file=README.TXT<br />
 local-file=readme.txt
</dl>
<p> Job files are flexible since they follow an easy-to-use format and do not have many requirements, but there are a few mandatory parameters that must appear for the spooler to be able to process the job.</p>
<dl>
<dt><i>op</i></p>
<dd> The operation (job type) to perform. Valid values are <i>get</i> and <i>put</i>.</p>
<dt><i>hostname</i></p>
<dd> The remote host to FTP to. This may be an IP address or a DNS name (i.e. <a href="ftp://ftp.example.com">ftp.example.com</a>).</dl>
<p> For a regular <i>get</i> job, these parameters are required:</p>
<dl>
<dt><i>remote-file</i></p>
<dd> The pathname of the file to download from the remote server.</p>
<dt><i>local-file</i></p>
<dd> The pathname to use on the local server for the downloaded file.</dl>
<p> For a regular <i>put</i> job, these parameters are required:</p>
<dl>
<dt><i>local-file</i></p>
<dd> The pathname of the file to upload to the remote server.</p>
<dt><i>remote-file</i></p>
<dd> The pathname to use on the remote server for the uploaded file.</dl>
<p> For a recursive <i>get</i> job, these parameters are required:</p>
<dl>
<dt><i>remote-file</i></p>
<dd> The pathname of the file or directory to download from the remote server.</p>
<dt><i>local-dir</i></p>
<dd> The directory pathname to use on the local server to contain the downloaded items.</dl>
<p> For a recursive <i>put</i> job, these parameters are required:</p>
<dl>
<dt><i>local-file</i></p>
<dd> The pathname of the file or directory to upload to the remote server.</p>
<dt><i>remote-dir</i></p>
<dd> The directory pathname to use on the remote server to contain the uploaded items.</dl>
<p> The rest of the parameters are optional. The spooler will attempt to use reasonable defaults for these parameters if necessary.</p>
<dl>
<dt><i>user</i></p>
<dd> The username to use to login to the remote server. Defaults to &#8220;anonymous&#8221; for guest access.</p>
<dt><i>pass</i></p>
<dd> The password to use in conjunction with the username to login to the remote server.</p>
<dt><i>acct</i></p>
<dd> The account to use in conjunction with the username to login to the remote server. The need to specify this parameter is extremely rare.</p>
<dt><i>port</i></p>
<dd> The port number to use in conjunction with the remote hostname to connect to the remote server. Defaults to the standard FTP port number, 21.</p>
<dt><i>host-ip</i></p>
<dd> The IP address to use in conjunction with the remote hostname to connect to the remote server. This parameter can be used in place of the <i>hostname</i> parameter, but one or the other must be used. This parameter is commonly included along with the <i>hostname</i> parameter as supplemental information.</p>
<dt><i>xtype</i></p>
<dd> The transfer type to use. Defaults to binary transfer type (TYPE I). Valid values are <i>I</i> for binary, <i>A</i> for ASCII text.</p>
<dt><i>passive</i></p>
<dd> Whether to use FTP passive data connections (PASV) or FTP active data connections (PORT). Valid values are <i>0</i> for active, <i>1</i> for passive, or <i>2</i> to try passive, then fallback to active. The default is <i>2</i>.</p>
<dt><i>recursive</i></p>
<dd> This can be used to transfer entire directory trees. By default, only a single file is transferred. Valid values are <i>yes</i> or <i>no</i>.</p>
<dt><i>delete</i></p>
<dd> This can be used to delete the source file on the source machine after successfully transferring the file to the destination machine. By default, source files are not deleted. Valid values are <i>yes</i> or <i>no</i>.</p>
<dt><i>job-name</i></p>
<dd> This isn&#8217;t used by the program, but can be used by an entity which is automatically generating job files. As an example, when using the <i>-bbb</i> flag with <i>ncftpput</i>, it creates a job file on stdout with a <i>job-name</i> parameter so you can easily copy the file to the job queue directory with the suggested job name as the job file name.</p>
<dt><i>pre-ftp-command</i></p>
<dd>
<dt><i>post-ftp-command</i></p>
<dd> These parameters correspond to the <i>-W</i>, and <i>-Y</i> options of <i>ncftpget</i> and <i>ncftpput</i>. It is important to note that these refer to RFC959 File Transfer Protocol commands and <code>not</code> shell commands, nor commands used from within /usr/bin/ftp or ncftp.</p>
<dt><i>pre-shell-command</i></p>
<dd>
<dt><i>post-shell-command</i></p>
<dd> These parameters provide hooks so you can run a custom program when an item is processed by the spooler. Valid values are pathnames to scripts or executable programs. Note that the value must not contain any command-line arguments &#8212; if you want to do that, create a shell script and have it run your program with the command-line arguments it requires.</dl>
<p> Generally speaking, <i>post-shell-command</i> is much more useful than <i>pre-shell-command</i> since if you need to use these options you&#8217;re more likely to want to do something after the FTP transfer has completed rather than before. For example, you might want to run a shell script which pages an administrator to notify her that her 37 gigabyte file download has completed. </p>
<p> When your custom program is run, it receives on standard input the contents of the job file (i.e. several lines of <i>variable</i>=<i>value</i> key-pairs), as well as additional data the spooler may provide, such as a <i>result</i> key-pair with a textual description of the job&#8217;s completion status. </p>
<p> <i>post-shell-command</i> update a log file named /var/log/ncftp_spooler.</p>
<dl>
<dt>
<dd>
<p> #!/usr/bin/perl -w </p>
<p> my ($line);<br />
 my (%params) = (); </p>
<p> while (defined($line = &lt;STDIN&gt;)) {<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>$params{$1}&nbsp;<wbr>=&nbsp;<wbr>$2</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>if&nbsp;<wbr>($line&nbsp;<wbr>=~&nbsp;<wbr>/^([^=\#\s]+)=(.*)/);</p>
<p> } </p>
<p> if ((defined($params{&quot;result&quot;})) &amp;&amp; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>($params{&quot;result&quot;}&nbsp;<wbr>=~&nbsp;<wbr>/^Succeeded/))<br />
 {<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>open(LOG, &quot;&gt;&gt; /var/log/ncftp_spooler.log&quot;)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>or <a href="/docs/linux/man/1-exit/">exit</a>(1);</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>print LOG &quot;DOWNLOAD&quot; if ($params{&quot;op&quot;} eq &quot;get&quot;);</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>print LOG &quot;UPLOAD&quot; if ($params{&quot;op&quot;} eq &quot;put&quot;);</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>print LOG &quot; &quot;, $params{&quot;local-file&quot;}, &quot;
&quot;;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>close(LOG);</p>
<p> }
</dl>
<h2>DIAGNOSTICS</h2>
<p> The log file should be examined to determine if any <i>ncftpspooler</i> processes are actively working on jobs. The log contains copious amounts of useful information, including the entire FTP control connection conversation between the FTP client and server.</p>
<h2>BUGS</h2>
<p> The <i>recursive</i> option may not be reliable since <i>ncftpspooler</i> depends on functionality which may or may not be present in the remote server software. Additionally, even if the functionality is available, <i>ncftpspooler</i> may need to use heuristics which cannot be considered 100% accurate. Therefore it is best to create individual jobs for each file in the directory tree, rather than a single recursive directory job. </p>
<p> For resumption of downloads to work, the remote server must support the FTP <i>SIZE</i> and <i>MDTM</i> primitives. Most modern FTP server software can do this, but there are still a number of bare-bones <i>ftpd</i> implementations which do not. In these cases, <i>ncftpspooler</i> will re-download the file in entirety each time until the download succeeds. </p>
<p> The program needs to be improved to detect jobs that have no chance of ever completing successfully. There are still a number of cases where jobs can get spooled but get retried over and over again until a vigilant sysadmin manually removes the jobs. </p>
<p> The spool files may contain usernames and passwords stored in cleartext. These files should not be readable by any user except the user running the program!</p>
<h2>AUTHOR</h2>
<p> Mike Gleason, NcFTP Software (<a rel="nofollow" href="http://www.ncftp.com">http://www.ncftp.com</a>).</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-ncftpbatch/">ncftpbatch</a>(1),</i> <i><a href="/docs/linux/man/1-ncftp/">ncftp</a></i>(1), <i><a href="/docs/linux/man/1-ncftpput/">ncftpput</a></i>(1), <i><a href="/docs/linux/man/1-ncftpget/">ncftpget</a></i>(1), <i><a href="/docs/linux/man/1-uucp/">uucp</a></i>(1). </p>
<h2>Index</h2>
