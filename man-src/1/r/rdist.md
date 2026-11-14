---
title: "rdist(1)"
name: "rdist"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rdist/"
description: "rdist – remote file distribution client program"
---

<h2 class="name">NAME</h2>
<p> rdist &#8211; remote file distribution client program </p>
<h2>SYNOPSIS</h2>
<p> <code>rdist</code> [ <code>-DFn</code> ] [ <code>-A </code> <i>num</i> ] [ <code>-a </code> <i>num </i> ] [ <code>-d </code> <i>var=value </i> ] [ <code>-l</code> <i>&lt;local logopts&gt;</i> ] [ <code>-L</code> <i>&lt;remote logopts&gt;</i> ] [ <code>-f </code> <i>distfile </i> ] [ <code>-M </code> <i>maxproc</i> ] [ <code>-m </code> <i>host </i> ] [ <code>-o</code> <i>distopts</i> ] [ <code>-t </code> <i>timeout </i> ] [ <code>-p</code> <i>&lt;rdistd-path&gt;</i> ] [ <code>-P</code> <i>&lt;transport-path&gt;</i> ] [ <i>name &#8230;</i> ] </p>
<p> <code>rdist</code> <code>-DFn</code> <code>-c </code> <i>name &#8230; </i> <i>[login@]host[:dest]</i> </p>
<p> <code>rdist</code> <code>-Server</code> </p>
<p> <code>rdist</code> <code>-V</code></p>
<h2>DESCRIPTION</h2>
<p> <i>Rdist</i> is a program to maintain identical copies of files over multiple hosts. It preserves the owner, group, mode, and mtime of files if possible and can update programs that are executing. <i>Rdist</i> reads commands from <i>distfile</i> to direct the updating of files and/or directories. If <i>distfile</i> is `-&#8216;, the standard input is used. If no <code>-f</code> option is present, the program looks first for `distfile&#8217;, then `Distfile&#8217; to use as the input. If no names are specified on the command line, <i>rdist</i> will update all of the files and directories listed in <i>distfile</i>. Otherwise, the argument is taken to be the name of a file to be updated or the label of a command to execute. If label and file names conflict, it is assumed to be a label. These may be used together to update specific files using specific commands. </p>
<p> The <code>-c</code> option forces <i>rdist</i> to interpret the remaining arguments as a small <i>distfile</i>. The equivalent distfile is as follows. </p>
<pre><code>

&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
(name...)-&gt;[login @] host

    &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
install[dest];
</code></pre>
<p> The <code>-Server</code> option is recognized to provide partial backward compatible support for older versions of <i>rdist</i> which used this option to put <i>rdist</i> into server mode. If <i>rdist</i> is started with the <code>-Server</code> command line option, it will attempt to exec (run) the old version of <i>rdist.</i> This option will only work if <i>rdist</i> was compiled with the location of the old rdist (the path <i>/usr/bin/oldrdist</i> is used on Red Hat linux) and that program is available at run time. </p>
<p> <i>Rdist</i> can use either the <i><a href="/docs/linux/man/3-rcmd/">rcmd</a>(3)</i> function call or run an arbitrary transport program such as <i><a href="//www.systutorials.com/docs/linux/man/1c-rsh/">rsh</a>(1c)</i> to access each target host. The method used is selected at compile-time. However, if the later method is used, the transport program can be specified at run-time on the command line with the default being <i><a href="//www.systutorials.com/docs/linux/man/1c-rsh/">rsh</a>(1c).</i> If the <i><a href="//www.systutorials.com/docs/linux/man/1c-rsh/">rsh</a>(1c)</i> method is used and the target host is the string <code>localhost</code> and the remote user name is the same as the local user name, <i>rdist</i> will run the command </p>
<pre>
<dl><dt><dd><code>/bin/sh -c rdistd -S</code>
</dl>
</pre>
<p> Otherwise <i>rdist</i> run will run the command </p>
<pre>
<dl><dt><dd><code>rsh </code><i>host</i><code> -l </code><i>remuser </i><code>rdistd -S</code>
</dl>
</pre>
<p> where <i>host</i> is the name of the target host, <i>remuser</i> is the name of the user to make the connection as and, <i>rdistd</i> is the rdist server command on the target host as shown below. To use a transport program other than <i><a href="//www.systutorials.com/docs/linux/man/1c-rsh/">rsh</a>(1c)</i> use the <code>-P</code> option. Whatever transport program is used, must be compatible with the above specified syntax for <i><a href="//www.systutorials.com/docs/linux/man/1c-rsh/">rsh</a>(1c).</i> If the transport program is not, it should be <i>wrapped</i> in a shell script which does understand this command line syntax and which then executes the real transport program. </p>
<p> Here&#8217;s an example which uses <i><a href="/docs/linux/man/1-ssh/">ssh</a>(1)</i> as the transport: </p>
<pre>
<dl><dt><dd><code>rdist -P /usr/local/bin/ssh -f myDistfile</code>
</dl>
</pre>
<p> If the <i><a href="/docs/linux/man/3-rcmd/">rcmd</a>(3) </i> method is used, then <i>rdist</i> makes the connection to the target host itself and runs the <i>rdistd</i> server program as shown below. The default, and preferred method, is to use <i><a href="//www.systutorials.com/docs/linux/man/1c-rsh/">rsh</a>(1c)</i> to make the connection to target hosts. This allows <i>rdist</i> to be run without being setuid to &#8220;root&#8221;. </p>
<p> On each target host <i>Rdist</i> will attempt to run the command </p>
<pre>
<dl><dt><dd><i>rdistd -S</i>
</dl>
</pre>
<p> or </p>
<pre>
<dl><dt><dd><i>&lt;rdistd path&gt; -S</i>
</dl>
</pre>
<p> if the <i>-p</i> option was specified. If no <code>-p </code> option is included, or the <i>&lt;rdistd path&gt;</i> is a simple filename, <i>rdistd</i> or <i>&lt;rdistd path&gt;</i> must be somewhere in the <code>$PATH</code> of the user running <code>rdist</code> on the remote (target) host.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-A </code><i>num</i></p>
<dd> Set the minimum number of free files (inodes) on a filesystem that must exist for <i>rdist</i> to update or install a file.</p>
<dt><code>-a </code><i>num</i></p>
<dd> Set the minimum amount of free space (in bytes) on a filesystem that must exist for <i>rdist</i> to update or install a file.</p>
<dt><code>-D</code></p>
<dd> Enable copious debugging messages.</p>
<dt><code>-d </code><i>var=value</i></p>
<dd> Define <i>var</i> to have <i>value</i>. This option is used to define or override variable definitions in the <i>distfile</i>. <i>Value</i> can be the empty string, one name, or a list of names surrounded by parentheses and separated by tabs and/or spaces.</p>
<dt><code>-F</code></p>
<dd> Do not fork any child <i>rdist</i> processes. All clients are updated sequentially.</p>
<dt><code>-f </code><i>distfile</i></p>
<dd> Set the name of the distfile to use to be <i>distfile .</i> If <i>distfile</i> is specified as &#8220;-&#8221; (dash) then read from standard input (stdin).</p>
<dt><code>-l </code><i>logopts</i></p>
<dd> Set local logging options. See the section <code>MESSAGE LOGGING</code> for details on the syntax for <i>logopts.</i></p>
<dt><code>-L </code><i>logopts</i></p>
<dd> Set remote logging options. <i>logopts</i> is the same as for local logging except the values are passed to the remote server (<i>rdistd</i>). See the section <code>MESSAGE LOGGING</code> for details on the syntax for <i>logopts.</i></p>
<dt><code>-M </code><i>num</i></p>
<dd> Set the maximum number of simultaneously running child <i>rdist</i> processes to <i>num.</i> The default is 4.</p>
<dt><code>-m </code><i>machine</i></p>
<dd> Limit which machines are to be updated. Multiple <code>-m</code> arguments can be given to limit updates to a subset of the hosts listed in the <i>distfile</i>.</p>
<dt><code>-n</code></p>
<dd> Print the commands without executing them. This option is useful for debugging <i>distfile</i>.</p>
<dt><code>-o</code><i>distopts</i></p>
<dd> Specify the dist options to enable. <i>distopts</i> is a comma separated list of options which are listed below. The valid values for <i>distopts</i> are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>verify</code></p>
<dd> Verify that the files are up to date on all the hosts. Any files that are out of date will be displayed but no files will be changed nor any mail sent.</p>
<dt><code>whole</code></p>
<dd> Whole mode. The whole file name is appended to the destination directory name. Normally, only the last component of a name is used when renaming files. This will preserve the directory structure of the files being copied instead of flattening the directory structure. For example, rdisting a list of files such as <i>/path/dir1/f1 </i> and <i>/path/dir2/f2 </i> to <i>/tmp/dir </i> would create files <i>/tmp/dir/path/dir1/f1 </i> and <i>/tmp/dir/path/dir2/f2 </i> instead of <i>/tmp/dir/dir1/f1 </i> and <i>/tmp/dir/dir2/f2.</i></p>
<dt><code>noexec</code></p>
<dd> Automatically exclude executable files that are in <i><a href="/docs/linux/man/5-a-out/">a.out</a>(5)</i> format from being checked or updated.</p>
<dt><code>younger</code></p>
<dd> Younger mode. Files are normally updated if their <i>mtime</i> and <i>size</i> (see <i><a href="/docs/linux/man/2-stat/">stat</a></i>(2)) disagree. This option causes <i>rdist</i> not to update files that are younger than the master copy. This can be used to prevent newer copies on other hosts from being replaced. A warning message is printed for files which are newer than the master copy.</p>
<dt><code>compare</code></p>
<dd> Binary comparison. Perform a binary comparison and update files if they differ rather than comparing dates and sizes.</p>
<dt><code>follow</code></p>
<dd> Follow symbolic links. Copy the file that the link points to rather than the link itself.</p>
<dt><code>ignlnks</code></p>
<dd> Ignore unresolved links. <i>Rdist</i> will normally try to maintain the link structure of files being transferred and warn the user if all the links cannot be found.</p>
<dt><code>chknfs</code></p>
<dd> Do not check or update files on target host that reside on NFS filesystems.</p>
<dt><code>chkreadonly</code></p>
<dd> Enable check on target host to see if a file resides on a read-only filesystem. If a file does, then no checking or updating of the file is attempted.</p>
<dt><code>chksym</code></p>
<dd> If the target on the remote host is a symbolic link, but is not on the master host, the remote target will be left a symbolic link. This behavior is generally considered a bug in the original version of <i>rdist,</i> but is present to allow compatibility with older versions.</p>
<dt><code>quiet</code></p>
<dd> Quiet mode. Files that are being modified are normally printed on standard output. This option suppresses this.</p>
<dt><code>remove</code></p>
<dd> Remove extraneous files. If a directory is being updated, any files that exist on the remote host that do not exist in the master directory are removed. This is useful for maintaining truly identical copies of directories.</p>
<dt><code>nochkowner</code></p>
<dd> Do not check user ownership of files that already exist. The file ownership is only set when the file is updated.</p>
<dt><code>nochkgroup</code></p>
<dd> Do not check group ownership of files that already exist. The file ownership is only set when the file is updated.</p>
<dt><code>nochkmode</code></p>
<dd> Do not check file and directory permission modes. The permission mode is only set when the file is updated.</p>
<dt><code>nodescend</code></p>
<dd> Do not descend into a directory. Normally <i>rdist</i> will recursively check directories. If this option is enabled, then any files listed in the file list in the distfile that are directories are not recursively scanned. Only the existence, ownership, and mode of the directory are checked.</p>
<dt><code>numchkgroup</code></p>
<dd> Use the numeric group id (gid) to check group ownership instead of the group name.</p>
<dt><code>numchkowner</code></p>
<dd> Use the numeric user id (uid) to check user ownership instead of the user name.</p>
<dt><code>savetargets</code></p>
<dd> Save files that are updated instead of removing them. Any target file that is updates is first rename from <code>file</code> to <code>file.OLD.</code></p>
<dt><code>sparse</code></p>
<dd> Enable checking for sparse (aka <i>wholely</i>) files. One of the most common types of sparse files are those produced by <code><a href="/docs/linux/man/3-ndbm/">ndbm</a>(3).</code> This option adds some additional processing overhead so it should only be enabled for targets likely to contain sparse files.</dl>
</dl>
<dt><code>-p </code><i>&lt;rdistd-path&gt;</i></p>
<dd> Set the path where the rdistd server is searched for on the target host.</p>
<dt><code>-P </code><i>&lt;transport-path&gt;</i></p>
<dd> Set the path to the transport command to be used. This is normally <i><a href="//www.systutorials.com/docs/linux/man/1c-rsh/">rsh</a>(1c)</i> but can be any other program &#8211; such as <i><a href="/docs/linux/man/1-ssh/">ssh</a>(1) &#8211;</i> which understands <i><a href="//www.systutorials.com/docs/linux/man/1c-rsh/">rsh</a>(1c)</i> command line syntax and which provides an appropriate connection to the remote host. The <i>transport-path</i> may be a colon seperated list of possible pathnames. In this case, the first component of the path to exist is used. i.e. <code>/usr/ucb/rsh:/usr/bin/remsh,</code> <code>/usr/bsd/rsh.</code></p>
<dt><code>-t </code><i>timeout</i></p>
<dd> Set the timeout period (in seconds) for waiting for responses from the remote <i>rdist</i> server. The default is 900 seconds.</p>
<dt><code>-V</code></p>
<dd> Print version information and exit.</dl>
<h2>MESSAGE LOGGING</h2>
<p> <i>Rdist</i> uses a collection of predefined message <code>facilities</code> that each contain a list of message <code>types</code> specifying which types of messages to send to that <i>facility.</i> The local client (<i>rdist</i>) and the remote server (<i>rdistd</i>) each maintain their own copy of what types of messages to log to what facilities. </p>
<p> The <code>-l</code> <i>logopts</i> option to <i>rdist</i> tells <i>rdist</i> what logging options to use locally. The <code>-L</code> <i>logopts</i> option to <i>rdist</i> tells <i>rdist</i> what logging options to pass to the remote <i>rdistd</i> server. </p>
<p> The form of <i>logopts</i> should be of form </p>
<dl>
<dt>
<dd> <i>facility</i><code>=</code><i>types</i><code>:</code><i>facility</i><code>=</code><i>types&#8230;</i></dl>
<p> The valid facility names are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>stdout</code></p>
<dd> Messages to standard output.</p>
<dt><code>file</code></p>
<dd> Log to a file. To specify the file name, use the format &#8220;<code>file=</code><i>filename</i><code>=</code><i>types</i>&#8221;. e.g. <code>&#8220;file=/tmp/rdist.log=all,debug&#8221;.</code></p>
<dt><code>syslog</code></p>
<dd> Use the <i><a href="/docs/linux/man/8-syslogd/">syslogd</a>(8)</i> facility.</p>
<dt><code>notify</code></p>
<dd> Use the internal <i>rdist</i> <code>notify</code> facility. This facility is used in conjunction with the <code>notify</code> keyword in a <i>distfile</i> to specify what messages are mailed to the <code>notify</code> address.</dl>
</dl>
<p> <i>types</i> should be a comma separated list of message types. Each message type specified enables that message level. This is unlike the <i><a href="/docs/linux/man/3-syslog/">syslog</a>(3)</i> system facility which uses an ascending order scheme. The following are the valid <i>types:</i></p>
<dl>
<dt>
<dd>
<dl>
<dt><code>change</code></p>
<dd> Things that change. This includes files that are installed or updated in some way.</p>
<dt><code>info</code></p>
<dd> General information.</p>
<dt><code>notice</code></p>
<dd> General info about things that change. This includes things like making directories which are needed in order to install a specific target, but which are not explicitly specified in the <i>distfile.</i></p>
<dt><code>nerror</code></p>
<dd> Normal errors that are not fatal.</p>
<dt><code>ferror</code></p>
<dd> Fatal errors.</p>
<dt><code>warning</code></p>
<dd> Warnings about errors which are not as serious as <code>nerror</code> type messages.</p>
<dt><code>debug</code></p>
<dd> Debugging information.</p>
<dt><code>all</code></p>
<dd> All but debug messages.</dl>
</dl>
<p> Here is a sample command line option: </p>
<pre>
<dl><dt><dd>-l stdout=all:syslog=change,notice:file=/tmp/rdist.log=all
</dl>
</pre>
<p> This entry will set local message logging to have all but debug messages sent to standard output, change and notice messages will be sent to <i><a href="/docs/linux/man/3-syslog/">syslog</a>(3),</i> and all messages will be written to the file <code>/tmp/rdist.log.</code></p>
<h2>DISTFILES</h2>
<p> The <i>distfile</i> contains a sequence of entries that specify the files to be copied, the destination hosts, and what operations to perform to do the updating. Each entry has one of the following formats.<br />
&lt;variable name&gt; `=&#8217; &lt;name list&gt;<br />
[ label: ] &lt;source list&gt; `-&gt;&#8217; &lt;destination list&gt; &lt;command list&gt;<br />
[ label: ] &lt;source list&gt; `::&#8217; &lt;time_stamp file&gt; &lt;command list&gt;</p>
<p> The first format is used for defining variables. The second format is used for distributing files to other hosts. The third format is used for making lists of files that have been changed since some given date. The <i>source list</i> specifies a list of files and/or directories on the local host which are to be used as the master copy for distribution. The <i>destination list</i> is the list of hosts to which these files are to be copied. Each file in the source list is added to a list of changes if the file is out of date on the host which is being updated (second format) or the file is newer than the time stamp file (third format). </p>
<p> Labels are optional. They are used to identify a command for partial updates. </p>
<p> Newlines, tabs, and blanks are only used as separators and are otherwise ignored. Comments begin with `#&#8217; and end with a newline. </p>
<p> Variables to be expanded begin with `$&#8217; followed by one character or a name enclosed in curly braces (see the examples at the end). </p>
<p> The source and destination lists have the following format: </p>
<p>&amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
&lt;name&gt; or</p>
<p>    &amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;`(&#8216; &lt;zero or more names separated by white-space&gt; `)&#8217;<br />
 These simple lists can be modified by using one level of set addition, subtraction, or intersection like this: </p>
<p>&amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
list &#8216;-&#8216; list or</p>
<p>    &amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
list &#8216;+&#8217; list or</p>
<p>    &amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
list &#8216;&amp;&#8217; list<br />
 If additional modifications are needed (e.g., &#8220;all servers and client machines except for the OSF/1 machines&#8221;) then the list will have to be explicitly constructed in steps using &quot;temporary&quot; variables. </p>
<p> The shell meta-characters `[&#8216;, `]&#8217;, `{&#8216;, `}&#8217;, `*&#8217;, and `?&#8217; are recognized and expanded (on the local host only) in the same way as <i><a href="/docs/linux/man/1-csh/">csh</a></i>(1). They can be escaped with a backslash. The `~&#8217; character is also expanded in the same way as <i>csh</i> but is expanded separately on the local and destination hosts. When the <code>-o</code><i>whole</i> option is used with a file name that begins with `~&#8217;, everything except the home directory is appended to the destination name. File names which do not begin with `/&#8217; or `~&#8217; use the destination user&#8217;s home directory as the root directory for the rest of the file name. </p>
<p> The command list consists of zero or more commands of the following format. </p>
<p>`install &#8216;     &lt;options&gt;    opt_dest_name `;&#8217;<br />
`notify &#8216;      &lt;name list&gt;  `;&#8217;<br />
`except &#8216;      &lt;name list&gt;  `;&#8217;<br />
`except_pat &#8216;  &lt;pattern list&gt;`;&#8217;<br />
`special &#8216;     &lt;name list&gt;  string `;&#8217;<br />
`cmdspecial &#8216;  &lt;name list&gt;  string `;&#8217;</p>
<p> The <i>install</i> command is used to copy out of date files and/or directories. Each source file is copied to each host in the destination list. Directories are recursively copied in the same way. <i>Opt_dest_name</i> is an optional parameter to rename files. If no <i>install</i> command appears in the command list or the destination name is not specified, the source file name is used. Directories in the path name will be created if they do not exist on the remote host. The <code>-o </code><i>distopts</i> option as specified above under <code>OPTIONS,</code> has the same semantics as on the command line except they only apply to the files in the source list. The login name used on the destination host is the same as the local host unless the destination name is of the format &#8220;login [at] host&quot;. </p>
<p> The <i>notify</i> command is used to mail the list of files updated (and any errors that may have occurred) to the listed names. If no `@&#8217; appears in the name, the destination host is appended to the name (e.g., name1 [at] host, name2 [at] host, &#8230;). </p>
<p> The <i>except</i> command is used to update all of the files in the source list <code>except</code> for the files listed in <i>name list</i>. This is usually used to copy everything in a directory except certain files. </p>
<p> The <i>except_pat</i> command is like the <i>except</i> command except that <i>pattern list</i> is a list of regular expressions (see <i><a href="/docs/linux/man/1-ed/">ed</a></i>(1) for details). If one of the patterns matches some string within a file name, that file will be ignored. Note that since `\&#8217; is a quote character, it must be doubled to become part of the regular expression. Variables are expanded in <i>pattern list</i> but not shell file pattern matching characters. To include a `$&#8217;, it must be escaped with `\&#8217;. </p>
<p> The <i>special</i> command is used to specify <i><a href="/docs/linux/man/1-sh/">sh</a></i>(1) commands that are to be executed on the remote host after the file in <i>name list</i> is updated or installed. If the <i>name list</i> is omitted then the shell commands will be executed for every file updated or installed. <i>String</i> starts and ends with `&quot;&#8217; and can cross multiple lines in <i>distfile.</i> Multiple commands to the shell should be separated by `;&#8217;. Commands are executed in the user&#8217;s home directory on the host being updated. The <i>special</i> command can be used to rebuild private databases, etc. after a program has been updated. The following environment variables are set for each <i>special</i> command:</p>
<dl>
<dt><code>FILE</code></p>
<dd> The full pathname of the local file that was just updated.</p>
<dt><code>REMFILE</code></p>
<dd> The full pathname of the remote file that was just updated.</p>
<dt><code>BASEFILE</code></p>
<dd> The basename of the remote file that was just updated.</dl>
<p> The <i>cmdspecial</i> command is similar to the <i>special</i> command, except it is executed only when the entire command is completed instead of after each file is updated. The list of files is placed in the environment variable <code>$FILES.</code> Each file name in <code>$FILES</code> is separated by a `:&#8217; (colon). </p>
<p> If a hostname ends in a &#8220;+&#8221; (plus sign), then the plus is stripped off and NFS checks are disabled. This is equivalent to disabling the <code>-o</code><i>chknfs</i> option just for this one host. </p>
<p> The following is a small example. </p>
<pre><code>
HOSTS = ( matisse root [at] arpa)
FILES = ( /bin /lib /usr/bin /usr/games
              /usr/include/{
    *.h,
    {
        stand, sys, vax *, pascal, machine
    }
/*.h}
              /usr/lib /usr/man/man? /usr/ucb /usr/local/rdist )
EXLIB = ( Mail.rc aliases aliases.dir aliases.pag crontab dshrc
              sendmail.cf sendmail.fc sendmail.hf sendmail.st uucp vfont )
${FILES} -&gt; ${HOSTS}
              install -oremove,chknfs ;
              except /usr/lib/${EXLIB} ;
              except /usr/games/lib ;
              special /usr/lib/sendmail "/usr/lib/sendmail -bz" ;
srcs:
/usr/src/bin -&gt; arpa
              except_pat ( \.o\$ /SCCS\$ ) ;
IMAGEN = (ips dviimp catdvi)
imagen:
/usr/local/${IMAGEN} -&gt; arpa
              install /usr/local/lib ;
              notify ralph ;
${FILES} :: stamp.cory
              notify root [at] cory ;

</code></pre>
<h2>ENVIRONMENT</h2>
<dl>
<dt>TMPDIR</p>
<dd> Name of temporary directory to use. Default is <code>/tmp.</code></dl>
<h2>FILES</h2>
<pre>
distfile       - input command file
$TMPDIR/rdist* - temporary file for update lists
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-sh/">sh</a>(1),</code> <code><a href="/docs/linux/man/1-csh/">csh</a>(1),</code> <code><a href="/docs/linux/man/2-stat/">stat</a>(2),</code> <code><a href="//www.systutorials.com/docs/linux/man/1c-rsh/">rsh</a>(1c),</code> <code><a href="/docs/linux/man/3-rcmd/">rcmd</a>(3)</code></p>
<h2>DIAGNOSTICS</h2>
<h2>NOTES</h2>
<p> If the basename of a file (the last component in the pathname) is &quot;.&quot;, then <code>rdist </code> assumes the remote (destination) name is a directory. i.e. <code>/tmp/.</code> means that <code>/tmp</code> should be a directory on the remote host. </p>
<p> The following options are still recognized for backwards compatibility: </p>
<dl>
<dt>
<dd> -v -N -O -q -b -r -R -s -w -y -h -i -x</dl>
<h2>BUGS</h2>
<p> Source files must reside on the local host where rdist is executed. </p>
<p> Variable expansion only works for name lists; there should be a general macro facility. </p>
<p> <i>Rdist</i> aborts on files which have a negative mtime (before Jan 1, 1970). </p>
<p> If a hardlinked file is listed more than once in the same target, then <i>rdist </i> will report missing links. Only one instance of a link should be listed in each target. </p>
<h2>Index</h2>
