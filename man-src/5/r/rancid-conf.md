---
title: "rancid-conf(5)"
name: "rancid-conf"
section: "5"
letter: "r"
url: "/docs/linux/man/5-rancid-conf/"
description: "rancid.conf – rancid environment configuration file"
---

<p>rancid.conf &#8211; rancid environment configuration file</p>
<h2>Description</h2>
<p><code>rancid.conf</code> contains environment configuration information for <code><a href="/docs/linux/man/1-rancid-run/">rancid-run</a></code>(1) and <code><a href="/docs/linux/man/1-rancid-cvs/">rancid-cvs</a></code>(1), including shell PATH, list of rancid groups, etc. It is read by several scripts at run-time and others inherit the configration from a parent process which has read it. The syntax of <code>rancid.conf</code> is that of <i><a href="/docs/linux/man/1-sh/">sh</a></i>(1). <code>rancid.conf</code> is used to set environment variables used by other rancid scripts to effect their run-time behavior or to enable them to find their resources. </p>
<h2>Variables</h2>
<p>The following variables are used (listed alphabetically): </p>
<dl>
<dt><code>ACLSORT</code></p>
<dd>Permits disabling of access-list sorting, which could alter statement order that had been cleverly crafted by the administrator for optimal performance, thus making recovery and comparsion more difficult. </p>
<p> Default: YES</p>
<dt><code>BASEDIR</code></p>
<dd>BASEDIR is the directory where <code>rancid-run&#8217;s</code> log directory, the revision control system&#8217;s repository, and rancid group directories will be placed. </p>
<p> Its value is configure&#8217;s localstatedir and should be modified if rancid is moved to a new location in the file system without re-installing from the distribution. </p>
<p> Default: /var</p>
<dt><code>CVSROOT</code></p>
<dd><i><a href="/docs/linux/man/1-cvs/">cvs</a></i>(1) and <i><a href="/docs/linux/man/1-rancid-cvs/">rancid-cvs</a></i>(1) use this environment variable to locate the CVS repository. In some cases, particularly for Subversion and git, it is used as an argument to commands. In general, it should not be necessary to alter it, but it could be set to a remote location if the the RCS system supports it. If it is a remote location, any necessary authentication must be handled separately from RANCiD, which provides no means of interacting with the remote. </p>
<p> Default: $BASEDIR/CVS</p>
<dt><code>DIFFSCRIPT</code></p>
<dd>Defines an alternate filter for the output of the RCS diff. The filter should read from stdin and write to stdout. The default is defined in control_rancid and only improves readability. </p>
<p> Example: DIFFSCRIPT=&quot;sed -e &#8216;/^=/d&#8217; | expand&quot;; export DIFFSCRIPT</p>
<dt><code>FILTER_PWDS</code></p>
<dd>Determines which passwords will be filtered from configs. The value may be &quot;NO&quot;, &quot;YES&quot;, or &quot;ALL&quot; to filter none of the passwords, only those which are reversable or plain-text, or all (plus ssh keys, etc), respectively. </p>
<p> Default: YES </p>
<p> Note: a value of &quot;NO&quot; could be a security issue since diffs are sent via e-mail. A value of &quot;ALL&quot; is encouraged. </p>
<p> Note: <code>FILTER_PWDS</code> does not affect the handling of SNMP community strings. see <code>NOCOMMSTR</code> below. </p>
<p> Note: passwords whose value cycles and would produce erroneous diffs are always filtered (e.g.: Alteon passwords).</p>
<dt><code>LIST_OF_GROUPS</code></p>
<dd>Defines a list of group names of routers separated by white-space. These names become the directory names in $BASEDIR which contain the data for that set of devices. <code><a href="/docs/linux/man/1-rancid-run/">rancid-run</a></code>(1) also uses this variable to determine which device groups it should collect. Choose these names to be descriptive of the set of devices and do not use spaces, unprintable characters, etc. </p>
<p> Example: LIST_OF_GROUPS=&quot;UofO USFS&quot; </p>
<p> Two groups are defined; UofO (University of Oregon) and USFS (US Forest Service). Each will have a directory created (see <i><a href="/docs/linux/man/1-rancid-cvs/">rancid-cvs</a></i>(1)) $BASEDIR/UofO and $BASEDIR/USFS respectively, which will contain their data. </p>
<p> Each group must also have aliases for the administrative and diff recipients set-up in <i>/etc/aliases</i>. For example: </p>
<pre>rancid-uofo: frank
rancid-admin-uofo: joe,bob
rancid-usfs: frank
rancid-admin-usfs: joe,bob</pre>
<dt><code>LOCKTIME</code></p>
<dd>Defines the number of hours a group&#8217;s lock file may age before rancid starts to complain about a hung collection. The default is 4 hours.</p>
<dt><code>LOGDIR</code></p>
<dd>Directory where <code>rancid-run</code> places log files. </p>
<p> Default: $BASEDIR/logs</p>
<dt><code>MAILDOMAIN</code></p>
<dd>Define the domain part of addresses for administrative and diff e-mail. The value of this variable is simply appended to the normal mail addresses. For example rancid-usfs [at] example.com, if <code>MAILDOMAIN</code> had been set to &quot;@example.com&quot;.</p>
<dt><code>MAILHEADERS</code></p>
<dd>Define additional mail headers to be added to rancid mail, such as Precedence or X- style headers. Individual headers must be separated by a 
 (new line). </p>
<p> Default: Precedence: bulk </p>
<p> Example: Precedence: bulk
X-clamation: beef cake</p>
<dt><code>MAILOPTS</code></p>
<dd>Define additional options used to invoke <code><a href="/docs/linux/man/8-sendmail/">sendmail</a></code>(8). By default, this is not set. </p>
<p> Example: MAILOPTS=&quot;-f bounces.go.here [at] example.com&quot;</p>
<dt><code>MAILSPLIT</code></p>
<dd>Defines the maximum BODY size of diffs in kilobytes, such that diffs are split clunks no larger than N kbytes. The minimum is 0, which disables splitting. </p>
<p> Default: 0.</p>
<dt><code>MAX_ROUNDS</code></p>
<dd>Defines how many times rancid should retry collection of devices that fail. The minimum is 0. </p>
<p> Default: 4.</p>
<dt><code>NOCOMMSTR</code></p>
<dd>If set, <i><a href="/docs/linux/man/1-rancid/">rancid</a></i>(1) will filter SNMP community strings from configs. Otherwise, they will be retained and may appear in clear-text in e-mail diffs. By default, this is not set.</p>
<dt><code>NOPIPE</code></p>
<dd>If set, <i><a href="/docs/linux/man/1-rancid/">rancid</a></i>(1) will use temporary files to save the output from the router and then read these to build the file which will be saved in CVS (or Subversion or git). Otherwise, an IPC pipe will be used. We have found that the buffering mechanisms used in perl and expect are heinous. Using temporary files may result in a noticeable improvement in speed. By default, this is not set.</p>
<dt><code>OLDTIME</code></p>
<dd>Specified as a number of hours, OLDTIME defines how many hours should pass since a successful collection of a device&#8217;s configuration and when <i><a href="/docs/linux/man/1-control_rancid/">control_rancid</a></i>(1) should start complaining about failures. The value should be greater than the number of hours between <code>rancid-run</code> cron runs. </p>
<p> Default: 24</p>
<dt><code>PAR_COUNT</code></p>
<dd>Defines the number of rancid processes that <i><a href="/docs/linux/man/1-par/">par</a></i>(1) will start simultaneously as <i><a href="/docs/linux/man/1-control_rancid/">control_rancid</a></i>(1) attempts to perform collections. Raising this value will decrease the amount of time necessary for a complete collection of a (or all) rancid groups at the expense of system load. The default is relatively cautious. If collections are not completing quickly enough for users, use trial and error of speed versus system load to find a suitable value. </p>
<p> Default: 5</p>
<dt><code>PATH</code></p>
<dd>Is a colon separate list of directory pathnames in the the file system where rancid&#8217;s <i><a href="/docs/linux/man/1-sh/">sh</a></i>(1) and <i><a href="/docs/linux/man/1-perl/">perl</a></i>(1) scripts should look for the programs that it needs, such as <i><a href="/docs/linux/man/1-telnet/">telnet</a></i>(1). Its value is set by configure. Should it be necessary to modify PATH, note that it must include /usr/libexec/rancid.</p>
<dt><code>RCSSYS</code></p>
<dd>Sets which revision control system is in use. Valid values are <code>cvs</code> for CVS, <code>git</code> for Git or <code>svn</code> for Subversion. </p>
<p> Default: cvs</p>
<dt><code>TERM</code></p>
<dd>Some Unix utilities require TERM, the terminal type, to be set to a sane value. Some clients, such as <i><a href="/docs/linux/man/1-telnet/">telnet</a></i>(1) and <i><a href="/docs/linux/man/1-ssh/">ssh</a></i>(1)<i>,</i> communicate this to the server (i.e.: the remote device), thus this can affect the behavior of login sessions on a device. The default should suffice. </p>
<p> Default: network</p>
<dt><code>TMPDIR</code></p>
<dd>Some Unix utilities recognize TMPDIR as a directory where temporary files can be stored. In some cases, rancid utilizes this directory for lock files and other temporary files. </p>
<p> Default: /tmp</dl>
<p> Each of these are simply environment variables. In order for them to be present in the environment of child processes, each must be exported. See <i><a href="/docs/linux/man/1-sh/">sh</a></i>(1) for more information on the built-in command export.</dl>
<h2>Errors</h2>
<p><code>rancid.conf</code> is interpreted directly by <i><a href="/docs/linux/man/1-sh/">sh</a></i>(1), so its syntax follows that of the bourne shell. Errors may produce quite unexpected results.</p>
<h2>Files</h2>
<dl>
<dt><code>/etc/rancid/rancid.conf</code></p>
<dd>Configuration file described here.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-control_rancid/">control_rancid</a></code>(1), <code><a href="/docs/linux/man/1-rancid/">rancid</a></code>(1), <code><a href="/docs/linux/man/1-rancid-cvs/">rancid-cvs</a></code>(1), <code><a href="/docs/linux/man/1-rancid-run/">rancid-run</a></code>(1)</p>
<h2>History</h2>
<p>In RANCID releases prior to 2.3, <code>rancid.conf</code> was named <code>env</code> and located in the bin directory. This was changed to be more consistent with common file location practices.</p>
