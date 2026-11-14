---
title: "rkhunter(8)"
name: "rkhunter"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rkhunter/"
description: "rkhunter – RootKit Hunter"
---

<p>rkhunter &#8211; RootKit Hunter</p>
<h2>Synopsis</h2>
<p><code>rkhunter</code> {&#8211;check | &#8211;unlock | &#8211;update | &#8211;versioncheck |<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;propupd&nbsp;<wbr>[{filename | directory | package name},&#8230;]&nbsp;<wbr>|<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;list&nbsp;<wbr>[tests |&nbsp;<wbr>{lang | languages}&nbsp;<wbr>| rootkits | perl |<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>propfiles]&nbsp;<wbr>|<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;config-check | &#8211;version | &#8211;help}&nbsp;<wbr>[options] </p>
<h2>Description</h2>
<p><code>rkhunter</code> is a shell script which carries out various checks on the local system to try and detect known rootkits and malware. It also performs checks to see if commands have been modified, if the system startup files have been modified, and various checks on the network interfaces, including checks for listening applications. <code>rkhunter</code> has been written to be as generic as possible, and so should run on most Linux and UNIX systems. It is provided with some support scripts should certain commands be missing from the system, and some of these are perl scripts. <code>rkhunter</code> does require certain commands to be present for it to be able to execute. Additionally, some tests require specific commands, but if these are not present then the test will be skipped. <code>rkhunter</code> needs to be run under a Bourne-type shell, typically <code>bash</code> or <code>ksh</code>. <code>rkhunter</code> can be run as a cron job or from the command-line. </p>
<h2>Command Options</h2>
<p>If no command option is given, then <code>&#8211;help</code> is assumed. <code>rkhunter</code> will return a non-zero exit code if any error or warning occurs. </p>
<dl>
<dt><code>-c, &#8211;check</code></p>
<dd>This command option tells <code>rkhunter</code> to perform various checks on the local system. The result of each test will be displayed on stdout. If anything suspicious is found, then a warning will be displayed. A log file of the tests and the results will be automatically produced. </p>
<p> It is suggested that this command option is run regularly in order to ensure that the system has not been compromised. </p>
<dd>
<dt><code>&#8211;unlock</code></p>
<dd>This command option simply unlocks (removes) the lock file. If this option is used on its own, then no log file is created. </p>
<dd>
<dt><code>&#8211;update</code></p>
<dd>This command option causes <code>rkhunter</code> to check if there is a later version of any of its text data files. A command-line web browser, for example <code>wget</code> or <code>lynx</code>, must be present on the system when using this option. </p>
<p> It is suggested that this command option is run regularly in order to ensure that the data files are kept up to date. </p>
<p> If this option is used via cron, then it is recommended that the <code>&#8211;nocolors</code> option is also used. </p>
<p> An exit code of zero for this command option means that no updates were available. An exit code of one means that a download error occurred, and a code of two means that no error occurred but updates were available and have been installed. </p>
<dd>
<dt><code>&#8211;propupd [{filename | directory | package name},&#8230;]</code></p>
<dd>One of the checks <code>rkhunter</code> performs is to compare various current file properties of various commands, against those it has previously stored. This command option causes <code>rkhunter</code> to update its data file of stored values with the current values. </p>
<p> If the <i>filename</i> option is used, then it must either be a full pathname, or a plain file name (for example, &#8216;awk&#8217;). When used, then only the entry in the file properties database for that file will be updated. If the <i>directory</i> option is used, then only those files listed in the database that are in the given directory will be updated. Similarly, if the <i>package name</i> option is used, then only those files in the database which are part of the specified package will be updated. The package name must be the base part of the name, no version numbers should be included &#8211; for example, &#8216;coreutils&#8217;. Package names will, of course, only be stored in the file properties database if a package manager is being used. If a package name is the same as a file name &#8211; for example, &#8216;file&#8217; could refer to the &#8216;file&#8217; command or to the RPM &#8216;file&#8217; package (which contains the &#8216;file&#8217; command) &#8211; the package name will be used. If no specific option is given, then the entire database is updated. </p>
<p> <i>WARNING:</i> It is the users responsibility to ensure that the files on the system are genuine and from a reliable source. <code>rkhunter</code> can only report if a file has changed, but not on what has caused the change. Hence, if a file has changed, and the <code>&#8211;propupd</code> command option is used, then <code>rkhunter</code> will assume that the file is genuine. </p>
<dd>
<dt><code>&#8211;versioncheck</code></p>
<dd>This command option causes <code>rkhunter</code> to check if there is a later version of the program. A command-line web browser must be present on the system when using this option. </p>
<p> If this option is used via cron, then it is recommended that the <code>&#8211;nocolors</code> option is also used. </p>
<p> An exit code of zero for this command option means that no new version was available. An exit code of one means that an error occurred downloading the latest version number, and a code of two means that no error occurred but a new version is available. </p>
<dd>
<dt><code>&#8211;list [tests | {lang | languages} | rootkits | perl | propfiles]</code></p>
<dd>This command option will list some of the supported capabilities of the program, and then exit. The <i>tests</i> option lists the currently available test names (see the README file for more details about test names). The <i>languages</i> option lists the currently available languages, and the <i>rootkits</i> option lists the rootkits that are searched for by <code>rkhunter</code>. The <i>perl</i> option lists the installation status of the perl command and perl modules that may be used by some of the tests. Note that it is not <i>required</i> to install these modules. However, if <code>rkhunter</code> is forced to use perl to execute a test then the module must be present. The <i>propfiles</i> option will list the file names that are used to generate the file properties database. If no specific option is given, then all the lists, except for the file properties database, are displayed. </p>
<dd>
<dt><code>-C, &#8211;config-check</code></p>
<dd>This command option causes <code>rkhunter</code> to check its configuration file(s), and then exit. The program will run through its normal configuration checks as specified by the enable and disable options on the command-line and in the configuration files. That is, only the configuration options for tests which would normally run are checked. In order to check all the configured options, then use the <code>&#8211;enable all &#8211;disable none</code> options on the command line. Additionally, the program will check to see if there are any unrecognised configuration options. If any configuration problems are found, then they will be displayed and the return code will be set to 1. </p>
<p> It is suggested that this option is used whenever the configuration file(s) have been changed. </p>
<dd>
<dt><code>-V, &#8211;version</code></p>
<dd>This command option causes <code>rkhunter</code> to display its version number, and then exit. </p>
<dd>
<dt><code>-h, &#8211;help</code></p>
<dd>This command option displays the help screen menu, and then exits. </p>
<dd></dl>
<h2>Options</h2>
<p><code>rkhunter</code> uses a configuration file, named <i>rkhunter.conf</i>, for many of its configuration options. It will also use a local configuration file, named <i>rkhunter.conf.local</i>, if it is present. However, some options can also be specified on the command-line, and these will override the configuration file options. The configuration file options are well documented within the main configuration file itself. The following are the command-line options. The defaults mentioned here are the program defaults, unless explicitly stated as the configuration file default. </p>
<dl>
<dt><code>&#8211;appendlog</code></p>
<dd>By default a new log file will be created when <code>rkhunter</code> runs, and the previous log file will be renamed by having <i>.old</i> appended to its name. This option tells <code>rkhunter</code> to append to the existing log file. If the log file does not exist, then it will be created. </p>
<dt><code>&#8211;bindir &lt;directory&gt;&#8230;</code></p>
<dd>This option modifies which directories <code>rkhunter</code> looks in to find the various commands it requires (that is, its PATH). The default is the root PATH, and an internal list of some common command directories. By default a specified directory will be appended to the default list. However, if the directory name begins with the &#8216;+&#8217; character, then it will be prepended to the list (that is, it will be put at the start of the list). </p>
<dt><code>&#8211;cs2, &#8211;color-set2</code></p>
<dd>By default <code>rkhunter</code> will display its test results in color. The colors used are green for successful tests, red for failed tests (warnings), and yellow for skipped tests. These colors are visible when a black background is used, but are difficult to see on a white background. This option tells <code>rkhunter</code> to use a different color set which is more suited to a white background. </p>
<dt><code>&#8211;configfile &lt;file&gt;</code></p>
<dd>The installation process will automatically tell <code>rkhunter</code> where its configuration file is located. However, if necessary, this option can be used to specify a different pathname. </p>
<p> If a local configuration file is to be used, then it must reside in the same directory as the configuration file specified by this option. </p>
<dt><code>&#8211;cronjob</code></p>
<dd>This is similar to the <code>&#8211;check</code> command option, but it disables several of the interactive options. When this option is used <code>&#8211;check</code>, <code>&#8211;nocolors</code> and <code>&#8211;skip-keypress</code> are assumed. By default no output is sent to stdout, so the <code>&#8211;report-warnings-only</code> option may be useful with this option. </p>
<dt><code>&#8211;dbdir &lt;directory&gt;</code></p>
<dd>The installation process will automatically configure where the data files are stored for <code>rkhunter</code>. However, if necessary, this option can be used to specify a different directory. The directory can be read-only, after installation, provided that neither of the <code>&#8211;update</code> or <code>&#8211;propupd</code> options are specified, and that the <code>&#8211;versioncheck</code> option is not specified if ROTATE_MIRRORS is set to 1 in the configuration file. </p>
<dt><code>&#8211;debug</code></p>
<dd>This is a special option mainly for the developers. It produces no output on stdout. Regular logging will continue as per default or as specified by the <code>&#8211;logfile</code> option, and the debug output will be in a randomly generated filename which starts with <i>/tmp/rkhunter-debug</i>. </p>
<dt><code>&#8211;disable &lt;test&gt;[,&lt;test&gt;&#8230;]</code></p>
<dd>This option tells <code>rkhunter</code> not to run the specified tests. Read the README file for more information about test names. By default no tests are disabled. </p>
<dt><code>&#8211;display-logfile</code></p>
<dd>This option will cause the logfile to be displayed on the screen once <code>rkhunter</code> has finished. </p>
<dt><code>&#8211;enable &lt;test&gt;[,&lt;test&gt;&#8230;]</code></p>
<dd>This option tells <code>rkhunter</code> to only run the specified tests. If only one test name, other than <i>all</i>, is given, then the <code>&#8211;skip-keypress</code> option is assumed. Read the README file for more information about test names. By default all tests are enabled. All the test names are listed below under TESTS. </p>
<dt><code>&#8211;hash {MD5 | SHA1 | SHA224 | SHA256 | SHA384 | SHA512 |</code></p>
<dd><code> NONE | &lt;command&gt;}</code><br />
 Both the file properties check and the <code>&#8211;propupd</code> command option will use a hash function to determine a files current hash value. This option tells <code>rkhunter</code> which hash function to use. The <i>MD5</i> and <i>SHA</i> options will look for the relevant command, and, if not found, a perl support script will then be used to see if a perl module supporting the function has been installed. Alternatively, a specific <i>command</i> may be specified. A value of <i>NONE</i> can be used to indicate that the hash values should not be obtained or used as part of the file properties check. The default is <i>SHA1</i>, or <i>MD5</i> if no SHA1 command can be found. </p>
<p> Systems using prelinking must use either MD5, SHA1 or NONE. </p>
<dt><code>&#8211;lang, &#8211;language &lt;language&gt;</code></p>
<dd>This option specifies which language to use for the displayed tests and results. The currently supported languages can be seen by the <code>&#8211;list</code> command option. The default is <i>en</i> (English). If a message to be displayed cannot be found in the language file, then the English version will be used. As such, the English language file must always be present. The <code>&#8211;update</code> command option will update the language files when new versions are available. </p>
<dt><code>-l, &#8211;logfile [file]</code></p>
<dd>By default <code>rkhunter</code> will write out a log file. The default location of the file is <i>/var/log/rkhunter.log</i>. However, this location can be changed by using this option. If <i>/dev/null</i> is specified as the log file, then no log file will be written. If no specific <i>file</i> is given, then the default will be used. By default <code>rkhunter</code> will create a new log file each time it is run. Any previously existing logfile is moved out of the way, and has <i>.old</i> appended to it. </p>
<dt><code>&#8211;noappend-log</code></p>
<dd>This option reverts <code>rkhunter</code> to its default behaviour of creating a new log file rather than appending to it. </p>
<dt><code>&#8211;nocf</code></p>
<dd>This option is only valid when the command-line <code>&#8211;disable</code> option is used. When the <code>&#8211;disable</code> option is used, by default, the configuration file option to disable tests is also used to determine which tests to run. If only the <code>&#8211;disable</code> option is to be used to determine which tests to run, then <code>&#8211;nocf</code> must be given. </p>
<dt><code>&#8211;nocolors</code></p>
<dd>This option causes the result of each test to not be displayed in a specific color. The default color, usually the reverse of the background color, will be used (typically this is just black and white). </p>
<dt><code>&#8211;nolog</code></p>
<dd>This option tells <code>rkhunter</code> not to write anything to a log file. </p>
<dt><code>&#8211;nomow, &#8211;no-mail-on-warning</code></p>
<dd>The configuration file has an option which will cause a simple email message to be sent to a user should <code>rkhunter</code> detect any warnings during system checks. This command-line option overrides the configuration file option, and prevents an email message from being sent. The configuration file default is not to email a message. </p>
<dt><code>&#8211;ns, &#8211;nosummary</code></p>
<dd>When the <code>&#8211;check</code> command option is used, by default a short summary of results is displayed at the end. This option prevents the summary from being displayed. </p>
<dt><code>&#8211;novl, &#8211;no-verbose-logging</code></p>
<dd>During some tests <code>rkhunter</code> will log a lot of information. Use of this option reduces the amount of logging, and so can improve the performance of <code>rkhunter</code>. However, the log file will contain less information should any warnings occur. By default verbose logging is enabled. </p>
<dt><code>&#8211;pkgmgr {RPM | DPKG | BSD | SOLARIS | NONE}</code></p>
<dd>This option is used during the file properties check or when the <code>&#8211;propupd</code> command option is given. It tells <code>rkhunter</code> that the current file property values should be obtained from the relevant package manager. See the README file for more details of this option. The default is <i>NONE</i>, which means not to use a package manager. </p>
<dt><code>-q, &#8211;quiet</code></p>
<dd>This option tells <code>rkhunter</code> not to display any output. It can be useful when only the exit code is going to be checked. Other options may be used with this one, to force only specific items to be displayed. </p>
<dt><code>&#8211;rwo, &#8211;report-warnings-only</code></p>
<dd>This option causes only warning messages to be displayed. This can be useful when <code>rkhunter</code> is run via cron. Other options may be used to force other items of information to be displayed. </p>
<dt><code>&#8211;sk, &#8211;skip-keypress</code></p>
<dd>When the <code>&#8211;check</code> command option is used, after certain sections of tests, the user will be prompted to press the <i>return</i> key in order to continue. This option disables that feature, and <code>rkhunter</code> will run until all the tests have completed. </p>
<p> If this option has not been given, and the user is prompted to press the <i>return</i> key, a single &#8216;<i>s</i>&#8216; character, in upper- or lowercase, may be given followed by the <i>return</i> key. <code>rkhunter</code> will then continue the tests without prompting the user again (as if this option had been given). </p>
<dt><code>&#8211;summary</code></p>
<dd>This option will cause the summary of test results to be displayed. This is the default. </p>
<dt><code>&#8211;syslog [facility.priority]</code></p>
<dd>When the <code>&#8211;check</code> command option is used, this option will cause the start and finish times to be logged to syslog. The default is not to log anything to syslog, but if the option is used, then the default level is <i>authpriv.notice</i>. </p>
<dt><code>&#8211;tmpdir &lt;directory&gt;</code></p>
<dd>The installation process will automatically configure where temporary files are to be created. However, if necessary, this option can be used to specify a different directory. The directory must not be a symbolic link, and must be secure (root access only). </p>
<dt><code>&#8211;vl, &#8211;verbose-logging</code></p>
<dd>This option tells <code>rkhunter</code> that when it runs some tests, it should log as much information as possible. This can be useful when trying to diagnose why a warning has occurred, but it obviously also takes more time. The default is to use verbose logging. </p>
<dt><code>-x, &#8211;autox</code></p>
<dd>When this option is used, <code>rkhunter</code> will try and detect if the X Window system is in use. If it is in use, then the second color set will automatically be used (see the <code>&#8211;color-set2</code> option). This allows <code>rkhunter</code> to be run on, for example, a server console (where X is not present, so the default color set should be used), and on a users terminal (where X is in use, so the second color set should be used). In both cases <code>rkhunter</code> will use the correct color set. The configuration file default is to try and detect X. </p>
<dt><code>-X, &#8211;no-autox</code></p>
<dd>This option prevents <code>rkhunter</code> from automatically detecting if the X Window system is being used. See the <code>&#8211;autox</code> option. </p>
</dl>
<h2>Tests</h2>
<p>[This section to be written] </p>
<dl>
<dt><code>additional_rkts</code></p>
<dd>This test is for SHORT_EXPLANATION. It works as part of GROUP. Corresponding configuration file entries: ONE=one, TWO=two and for white-listing THREE=three,three. Simple globbing (/dev/shm/file-*) works. </p>
<dt><code>all</code></p>
<dd>
<dt><code>apps</code></p>
<dd>
<dt><code>attributes</code></p>
<dd>
<dt><code>avail_modules</code></p>
<dd>
<dt><code>deleted_files</code></p>
<dd>
<dt><code>filesystem</code></p>
<dd>
<dt><code>group_accounts</code></p>
<dd>
<dt><code>group_changes</code></p>
<dd>
<dt><code>hashes</code></p>
<dd>
<dt><code>hidden_ports</code></p>
<dd>
<dt><code>hidden_procs</code></p>
<dd>
<dt><code>immutable</code></p>
<dd>
<dt><code>known_rkts</code></p>
<dd>
<dt><code>loaded_modules</code></p>
<dd>
<dt><code>local_host</code></p>
<dd>
<dt><code>malware</code></p>
<dd>
<dt><code>network</code></p>
<dd>
<dt><code>none</code></p>
<dd>
<dt><code>os_specific</code></p>
<dd>
<dt><code>other_malware</code></p>
<dd>
<dt><code>packet_cap_apps</code></p>
<dd>
<dt><code>passwd_changes</code></p>
<dd>
<dt><code>ports</code></p>
<dd>
<dt><code>possible_rkt_files</code></p>
<dd>
<dt><code>possible_rkt_strings</code></p>
<dd>
<dt><code>promisc</code></p>
<dd>
<dt><code>properties</code></p>
<dd>
<dt><code>rootkits</code></p>
<dd>
<dt><code>running_procs</code></p>
<dd>
<dt><code>scripts</code></p>
<dd>
<dt><code>shared_libs</code></p>
<dd>
<dt><code>shared_libs_path</code></p>
<dd>
<dt><code>startup_files</code></p>
<dd>
<dt><code>startup_malware</code></p>
<dd>
<dt><code>strings</code></p>
<dd>
<dt><code>suspscan</code></p>
<dd>
<dt><code>system_commands</code></p>
<dd>
<dt><code>system_configs</code></p>
<dd>
<dt><code>trojans</code></p>
<dd></dl>
<h2>Files</h2>
<p>(For a default installation)<br />
 /etc/rkhunter.conf<br />
 /var/log/rkhunter.log</p>
<h2>See Also</h2>
<p>See the CHANGELOG file for recent changes.<br />
 The README file has information about installing <code>rkhunter</code>, as well as specific sections on test names and using package managers.<br />
 The FAQ file should also answer some questions. </p>
<h2>Licensing</h2>
<p>RootKit Hunter is licensed under the GPL, copyright Michael Boelen. See the LICENSE file for details of GPL licensing.</p>
<h2>Contact Information</h2>
<p>RootKit Hunter is under active development by the RootKit Hunter project team. For reporting bugs, updates, patches, comments and questions, please go to <a rel="nofollow" href="http://rkhunter.sourceforge.net/">http://rkhunter.sourceforge.net/</a></p>
