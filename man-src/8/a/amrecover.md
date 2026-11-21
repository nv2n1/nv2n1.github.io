---
title: "amrecover(8)"
name: "amrecover"
section: "8"
letter: "a"
url: "/docs/linux/man/8-amrecover/"
description: "amrecover – Amanda index database browser"
---
<p>amrecover &#8211; Amanda index database browser </p>
<h2>SYNOPSIS</h2>
<dl>
<dt><code>amrecover</code> [-s&nbsp;<wbr><i>index-server</i>] [-t&nbsp;<wbr><i>tape-server</i>] [-d&nbsp;<wbr><i>tape-device</i>] [-h&nbsp;<wbr><i>hostname</i>] [<code>-o</code>&nbsp;<wbr><i>configoption</i>...] [-C&nbsp;<wbr><i>config</i>] </dt>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>Amrecover</code> </p>
<dd> <p> browses the database of Amanda index files to determine which tapes contain files to recover. Furthermore, it is able to recover files. </p>
<p>In order to restore files in place, you must invoke <code>amrecover</code> from the root of the backed up filesystem, or use <code>lcd</code> to move into that directory, otherwise a directory tree that resembles the backed up filesystem will be created in the current directory. See the examples below for details. </p>
<p>Amrecover will read the <code>amanda-client.conf</code> file and the <i>config</i><code>/amanda-client.conf</code> file. If no configuration name is supplied on the command line, Amrecover will try the compiled-in default configuration ,usually <code>DailySet1</code>. </p>
<p>See the <code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8) man page for more details about Amanda.  </p>
<h2>OPTIONS</h2>
 </dd>
<dl>
<dd> <p> <br />
 <font SIZE="+1"> <code>Note</code> </font> <br />
 </p>
<p>The Default values are those set at compile-time. Use <code>amrestore</code> to recover client-encrypted or client-custom-compressed tapes. </p>
 </dd></dl>
<p> <code>[ -C ] config</code> </p>
<dl>
<dd> <p> Amanda configuration. </p>
 </dd></dl>
<p> <code>-s index-server</code> </p>
<dl>
<dd> <p> Host that runs the index daemon. </p>
 </dd></dl>
<p> <code>-t tape-server</code> </p>
<dl>
<dd> <p> Host that runs the tape server daemon. </p>
 </dd></dl>
<p> <code>-d tape-device</code> </p>
<dl>
<dd> <p> Tape device to use on the tape server host. </p>
 </dd></dl>
<p> <code>-h hostname</code> </p>
<dl>
<dd> <p> Hostname to begin restoring; defaults to the system&#8217;s hostname. </p>
 </dd></dl>
<p> <code>-o</code> <i>clientconfigoption</i> </p>
<dl>
<dd> <p> See the &quot;<code>CONFIGURATION OVERRIDE</code>&quot; section in <code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8). </p>
 </dd></dl>
<h2>AUTH</h2>
<p>The default <code>auth</code> is &#8216;BSDTCP&#8217;, you can set a different auth in the <code>amanda-client.conf</code> file or by specifying the &#8216;-oauth=bsd&#8217; command line argument.  </p>
<h2>COMMANDS</h2>
<p> <code>Amrecover</code> connects to the index server and then presents a command line prompt. Usage is similar to an ftp client. The GNU readline library is used to provide command line history and editing if it was built in to <code>amrecover</code>. </p>
<p>The purpose of browsing the database is to build up a <i>restore list</i> of files to be extracted from the backup system. The following commands are available: </p>
<p> <code>sethost hostname</code> </p>
<dl>
<dd> <p> Specifies which host to look at backup files for (default: the local host). </p>
 </dd></dl>
<p> <code>setdate YYYY-MM-DD-HH-MM[-SS] | YYYY-MM-DD</code> </p>
<dl>
<dd> <p> Set the restore time (default: now). File listing commands only return information on backup images for this day, for the day before with the next lower dump level, and so on, until the most recent level 0 backup on or before the specified date is encountered. </p>
<p>For example, if: </p>
 </dd>
<dl>
<dd> <pre><code>1996-07-01 was a level 0 backup
1996-07-02 through 1996-07-05 were level 1 backups
1996-07-06 through 1997-07-08 were level 2 backups
</code></pre>
 </dd></dl>
<p>then the command <code>setdate 1997-07-08-00</code> would yield files from the following days: </p>
<dl>
<dd> <pre><code>1997-07-08 (the latest level 2 backup)
1997-07-05 (the latest level 1 backup)
1997-07-01 (the latest level 0 backup)
</code></pre>
 </dd></dl>
<p>Only the most recent version of a file will be presented. </p>
<p>The following abbreviated date specifications are accepted: </p>
<p> <code>--MM-DD</code> </p>
<dl>
<dd> <p> dates in the current year </p>
 </dd></dl>
<p> <code>---DD</code> </p>
<dl>
<dd> <p> dates in the current month of the current year </p>
 </dd></dl>
</dl>
<p> <code>setdisk</code> <i>diskname</i> [<i>mountpoint</i>] </p>
<dl>
<dd> <p> Specifies which disk to consider (default: the disk holding the working directory where <code>amrecover</code> is started). It can only be set after the host is set with <code>sethost</code>. <i>Diskname</i> is the device name specified in the <i>amanda.conf</i> or <code><a href="/docs/linux/man/5-disklist/">disklist</a></code>(5). The disk must be local to the host. If <i>mountpoint</i> is not specified, all pathnames will be relative to the (unknown) mount point instead of full pathnames. </p>
 </dd></dl>
<p> <code>listhost</code> [<i>diskdevice</i>] </p>
<dl>
<dd> <p> List all <code>host</code> </p>
 </dd></dl>
<p> <code>listdisk</code> [<i>diskdevice</i>] </p>
<dl>
<dd> <p> List all <code>diskname</code> </p>
 </dd></dl>
<p> <code>listproperty</code> </p>
<dl>
<dd> <p> List all <code>property</code> </p>
 </dd></dl>
<p> <code>setproperty</code> [<code>append</code>] [<code>priority</code>] <i>name</i> [<i>value</i> ...] </p>
<dl>
<dd> <p> Set the property <i>name</i> to the value <i>value</i>. The <code>append</code> keyword appends the <i>value</i> to the values already set for this property. Without <i>value</i>, the property is unset. The <code>priority</code> keyword is unused, it is present for ease of copy/paste from application definition. </p>
 </dd></dl>
<p> <code>setdevice</code> [[-h <i>tape-server</i>] <i>tapedev</i>] </p>
<dl>
<dd> <p> Specifies the host to use as the tape server, and which of its tape devices to use. If the server is omitted, the server name reverts to the configure-time default. If the tape device is omitted, the default is used. </p>
<p>If you want amrecover to use your changer, the <i>tapedev</i> must be equal to the <code>amrecover-changer</code> setting on the server. </p>
<p>Since device names contain colons, you must always specify the hostname. </p>
<pre><code>settape 192.168.0.10:file:/file1
</code></pre>
<p> You can change the tape device when amrecover ask you to load the tape: </p>
<pre><code>Load tape DMP014 now
Continue? [Y/n/t]: t
Tape device: server2:/dev/nst2
Continue? [Y/n/t]: Y
Using tape /dev/nst2 from server server2.
</code></pre>
 </dd></dl>
<p> <code>setmode</code> <i>mode</i> </p>
<dl>
<dd> <p> Set the extraction mode for Samba shares. If <i>mode</i> is <code>smb</code>, shares are sent to the Samba server to be restored back onto the PC. If <i>mode</i> is <code>tar</code>, they are extracted on the local machine the same way tar volumes are extracted. </p>
 </dd></dl>
<p> <code>settranslate</code> [<code>on</code>|<code>off</code>] </p>
<dl>
<dd> <p> Default: on. Translate escaped octal value (&#8216;\000&#8217;) in the index file to their corespondig characters, it improve the interface if amrecover is run in the same charset as the filename. Set it to <code>off</code> if the charset of some filename is not compatible with the amrecover charset. </p>
 </dd></dl>
<p> <code>mode</code> </p>
<dl>
<dd> <p> Displays the extracting mode for Samba shares. </p>
 </dd></dl>
<p> <code>history</code> </p>
<dl>
<dd> <p> Show the backup history of the current host and disk. Dates, levels, tapes and file position on tape of each backup are displayed. </p>
 </dd></dl>
<p> <code>pwd</code> </p>
<dl>
<dd> <p> Display the name of the current backup working directory. </p>
 </dd></dl>
<p> <code>cd</code> <i>dir</i> </p>
<dl>
<dd> <p> Change the backup working directory to <i>dir.</i> If the mount point was specified with <code>setdisk</code>, this can be a full pathname or it can be relative to the current backup working directory. If the mount point was not specified, paths are relative to the mount point if they start with &quot;/&quot;, otherwise they are relative to the current backup working directory. The <i>dir</i> can be a shell style wildcards. </p>
 </dd></dl>
<p> <code>cdx</code> <i>dir</i> </p>
<dl>
<dd> <p> Like the <code>cd</code> command but allow regular expression. </p>
 </dd></dl>
<p> <code>lpwd</code> </p>
<dl>
<dd> <p> Display the <code>amrecover</code> working directory. Files will be restored under this directory, relative to the backed up filesystem. </p>
 </dd></dl>
<p> <code>lcd</code> <i>path</i> </p>
<dl>
<dd> <p> Change the <code>amrecover</code> working directory to <i>path</i>. </p>
 </dd></dl>
<p> <code>ls</code> </p>
<dl>
<dd> <p> List the contents of the current backup working directory. See the description of the <code>setdate</code> command for how the view of the directory is built up. The backup date is shown for each file. </p>
 </dd></dl>
<p> <code>add</code> <i>item1 item2 ...</i> </p>
<dl>
<dd> <p> Add the specified files or directories to the restore list. Each item may have shell style wildcards. </p>
 </dd></dl>
<p> <code>addx</code> <i>item1 item2 ...</i> </p>
<dl>
<dd> <p> Add the specified files or directories to the restore list. Each item may be a regular expression. </p>
 </dd></dl>
<p> <code>delete</code> <i>item1 item2 ...</i> </p>
<dl>
<dd> <p> Delete the specified files or directories from the restore list. Each item may have shell style wildcards. </p>
 </dd></dl>
<p> <code>deletex</code> <i>item1 item2 ...</i> </p>
<dl>
<dd> <p> Delete the specified files or directories from the restore list. Each item may be a regular expression. </p>
 </dd></dl>
<p> <code>list</code> <i>file</i> </p>
<dl>
<dd> <p> Display the contents of the restore list. If a file name is specified, the restore list is written to that file. This can be used to manually extract the files from the Amanda tapes with <code>amrestore</code>. </p>
 </dd></dl>
<p> <code>clear</code> </p>
<dl>
<dd> <p> Clear the restore list. </p>
 </dd></dl>
<p> <code>quit</code> </p>
<dl>
<dd> <p> Close the connection to the index server and exit. </p>
 </dd></dl>
<p> <code>exit</code> </p>
<dl>
<dd> <p> Close the connection to the index server and exit. </p>
 </dd></dl>
<p> <code>extract</code> </p>
<dl>
<dd> <p> Start the extract sequence (see the examples below). Make sure the local working directory is the root of the backed up filesystem, or another directory that will behave like that. Use <code>lpwd</code> to display the local working directory, and <code>lcd</code> to change it. </p>
 </dd></dl>
<p> <code>help</code> </p>
<dl>
<dd> <p> Display a brief list of these commands. </p>
 </dd></dl>
<h2>EXAMPLES</h2>
<p>The following shows the recovery of an old <i>syslog</i> file. </p>
<pre><code># cd /var/log
# ls -l syslog.7
syslog.7: No such file or directory
# amrecover MyConfig
AMRECOVER Version 2.4.2. Contacting server on oops ...
220 oops Amanda index server (2.4.2) ready.
Setting restore date to today (1997-12-09)
200 Working date set to 1997-12-09.
200 Config set to MyConfig.
200 Dump host set to this-host.some.org.
$CWD '/var/log' is on disk '/var' mounted at '/var'.
200 Disk set to /var.
/var/log
WARNING: not on root of selected filesystem, check man-page!
amrecover&gt; ls
1997-12-09 daemon.log
1997-12-09 syslog
1997-12-08 authlog
1997-12-08 sysidconfig.log
1997-12-08 syslog.0
1997-12-08 syslog.1
1997-12-08 syslog.2
1997-12-08 syslog.3
1997-12-08 syslog.4
1997-12-08 syslog.5
1997-12-08 syslog.6
1997-12-08 syslog.7
amrecover&gt; add syslog.7
Added /log/syslog.7
amrecover&gt; lpwd
/var/log
amrecover&gt; lcd ..
/var
amrecover&gt; extract
Extracting files using tape drive /dev/nst0 on host 192.168.0.10
The following tapes are needed: DMP014
Restoring files into directory /var
Continue? [Y/n]: y
Load tape DMP014 now
Continue? [Y/n/t]: y
set owner/mode for '.'? [yn] n
amrecover&gt; quit
200 Good bye.
# ls -l syslog.7
total 26
-rw-r--r-- 1 root other 12678 Oct 14 16:36 syslog.7
</code></pre>
<p>If you do not want to overwrite existing files, create a subdirectory to run <code>amrecover</code> from and then move the restored files afterward. </p>
<pre><code># cd /var
# (umask 077 ; mkdir .restore)
# cd .restore
# amrecover
AMRECOVER Version 2.4.2. Contacting server on oops ...
...
amrecover&gt; cd log
/var/log
amrecover&gt; ls
...
amrecover&gt; add syslog.7
Added /log/syslog.7
amrecover&gt; lpwd
/var/.restore
amrecover&gt; extract
Extracting files using tape drive /dev/nst0 on host 192.168.0.10
...
amrecover&gt; quit
200 Good bye.
# mv -i log/syslog.7 ../log/syslog.7-restored
# cd ..
# rm -fr .restore
</code></pre>
<p>If you need to run <code>amrestore</code> by hand instead of letting <code>amrecover</code> control it, use the <code>list</code> command after browsing to display the needed tapes. </p>
<pre><code># cd /var/log
# amrecover
AMRECOVER Version 2.4.2. Contacting server on oops ...
...
amrecover&gt; ls
...
amrecover&gt; add syslog syslog.6 syslog.7
Added /log/syslog
Added /log/syslog.6
Added /log/syslog.7
amrecover&gt; list
TAPE DMP014 LEVEL 0 DATE 1997-12-08
        /log/syslog.7
        /log/syslog.6
TAPE DMP015 LEVEL 1 DATE 1997-12-09
        /log/syslog
amrecover&gt; quit
</code></pre>
<p>The <code>history</code> command shows each tape that has a backup of the current disk along with the date of the backup, the level, the tape label and the file position on the tape. All active tapes are listed, not just back to the most recent full dump. </p>
<p>Tape file position zero is a label. The first backup image is in file position one. </p>
<pre><code># cd /var/log
# amrecover
AMRECOVER Version 2.4.2. Contacting server on oops ...
...
amrecover&gt; history
200- Dump history for config &quot;MyConfig&quot; host &quot;this-host.some.org&quot; disk &quot;/var&quot;
201- 1997-12-09 1 DMP015 9
201- 1997-12-08 1 DMP014 11
201- 1997-12-07 0 DMP013 22
201- 1997-12-06 1 DMP012 16
201- 1997-12-05 1 DMP011 9
201- 1997-12-04 0 DMP010 11
201- 1997-12-03 1 DMP009 7
201- 1997-12-02 1 DMP008 7
201- 1997-12-01 1 DMP007 9
201- 1997-11-30 1 DMP006 6
...
amrecover&gt; quit
</code></pre>
<h2>ENVIRONMENT</h2>
<p> <code>PAGER</code> The <code>ls</code> and <code>list</code> commands will use $PAGER to display the file lists. Defaults to <i>more</i> if PAGER is not set. </p>
<p> <code>AMANDA_SERVER</code> If set, $AMANDA_SERVER will be used as index-server. The value will take precedence over the compiled default, but will be overridden by the -s switch. </p>
<p> <code>AMANDA_TAPE_SERVER</code> If set, $AMANDA_TAPE_SERVER will be used as tape-server. The value will take precedence over the compiled default, but will be overridden by the -t switch.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code>amanda-client.conf</code>(5), <code><a href="/docs/linux/man/8-amrestore/">amrestore</a></code>(8), <code><a href="/docs/linux/man/8-amfetchdump/">amfetchdump</a></code>(8), <code><a href="/docs/linux/man/3-readline/">readline</a></code>(3) </p>
<p>The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a>  </p>
<h2>AUTHORS</h2>
<p> <code>Alan M. McIvor</code> &lt;alan [at] kauri.auck.irl.cri.nz&gt; </p>
<p> <code>Stefan G. Weichinger</code> &lt;sgw [at] amanda.org&gt; </p>
<h2>Index</h2>
<dl>
<dt><a href="#lbAB">NAME</a></dt>
<dd>  </dd>
<dt><a href="#lbAC">SYNOPSIS</a></dt>
<dd>  </dd>
<dt><a href="#lbAD">DESCRIPTION</a></dt>
<dd>  </dd>
<dt><a href="#lbAE">OPTIONS</a></dt>
<dd>  </dd>
<dt><a href="#lbAF">AUTH</a></dt>
<dd>  </dd>
<dt><a href="#lbAG">COMMANDS</a></dt>
<dd>  </dd>
<dt><a href="#lbAH">EXAMPLES</a></dt>
<dd>  </dd>
<dt><a href="#lbAI">ENVIRONMENT</a></dt>
<dd>  </dd>
<dt><a href="#lbAJ">SEE ALSO</a></dt>
<dd>  </dd>
<dt><a href="#lbAK">AUTHORS</a></dt>
<dd>  </dd></dl>
