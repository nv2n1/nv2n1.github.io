---

title: "arcresume(1)"
name: "arcresume"
section: "1"
letter: "a"
url: "/docs/linux/man/1-arcresume/"
description: "arcresume – ARC Resume"
---

<p> The <code>arcresume</code> command is used for resuming a job that was submitted to grid enabled resources and then subsequently failed. The job will be resumed at the last ok state reported by the cluster. </p>
<p> <code>arcresume [options] [job &#8230;]</code> </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code>, <code>&#8211;all</code></dt>
<dd> all jobs</dd>
<dt><code>-j</code>, <code>&#8211;joblist</code>=<i>filename</i></dt>
<dd> the file storing information about active jobs (default ~/.arc/jobs.xml)</dd>
<dt><code>-i</code>, <code>&#8211;jobids-from-file</code>=<i>filename</i></dt>
<dd> a file containing a list of jobIDs</dd>
<dt><code>-c</code>, <code>&#8211;cluster</code>=<i>name</i></dt>
<dd> select one or more computing elements: <i>name</i> can be an alias for a single CE, a group of CEs or a URL</dd>
<dt><code>-r</code>, <code>&#8211;rejectmanagement</code>=<i>URL</i></dt>
<dd> skip jobs which are on a computing element with a given URL</dd>
<dt><code>-s</code>, <code>&#8211;status</code>=<i>statusstr</i></dt>
<dd> only select jobs whose status is statusstr</dd>
<dt><code>-P</code>, <code>&#8211;listplugins</code></dt>
<dd> list the available plugins</dd>
<dt><code>-t</code>, <code>&#8211;timeout</code>=<i>seconds</i></dt>
<dd> timeout in seconds (default 20)</dd>
<dt><code>-z</code>, <code>&#8211;conffile</code>=<i>filename</i></dt>
<dd> configuration file (default ~/.arc/client.conf)</dd>
<dt><code>-d</code>, <code>&#8211;debug</code>=<i>debuglevel</i></dt>
<dd> FATAL, ERROR, WARNING, INFO, VERBOSE or DEBUG</dd>
<dt><code>-v</code>, <code>&#8211;version</code></dt>
<dd> print version information</dd>
<dt><code>-?</code>, <code>&#8211;help</code></dt>
<dd> print help</dd></dl>
<h2>ARGUMENTS</h2>
<dl>
<dt><code>job</code> &#8230;</dt>
<dd> list of jobids and/or jobnames</dd></dl>
<h2>EXTENDED DESCRIPTION</h2>
<p> The <code>arcresume</code> command resumes a job submitted an ARC enabled resource. The job can be referred to either by the jobid that was returned by <code><a href="/docs/linux/man/1-arcsub/">arcsub</a></code>(1) at submission time or by its jobname if the job description that was submitted contained a jobname attribute. </p>
<p> More than one jobid and/or jobname can be given. If several jobs were submitted with the same jobname all those jobs are resumed. If the <code>&#8211;joblist</code> option is used the list of jobs is read from a file with the specified filename. By specifying the <code>&#8211;all</code> option, all active jobs will be resumed. </p>
<p> The <code>&#8211;cluster</code> option can be used to select or reject jobs at specific clusters. See <code><a href="/docs/linux/man/1-arcsub/">arcsub</a></code>(1) for a discussion of the format of arguments to this option. The <code>&#8211;status</code> option can be used to select jobs in a specific state. These options can be repeated several times. See <code><a href="/docs/linux/man/1-arcstat/">arcstat</a></code>(1) for possible states values. </p>
<h2>FILES</h2>
<dl>
<dt><code>~/.arc/client.conf</code></dt>
<dd> Some options can be given default values by specifying them in the ARC client configuration file. By using the <code>&#8211;conffile</code> option a different configuration file can be used than the default. </dd>
<dt><code>~/.arc/jobs.xml</code></dt>
<dd> This a local list of the user&#8217;s active jobs. When a job is successfully submitted it is added to this list and when it is removed from the remote cluster it is removed from this list. This list is used as the list of all active jobs when the user specifies the <code>&#8211;all</code> option to the various NorduGrid ARC user interface commands. By using the <code>&#8211;joblist</code> option a different file can be used than the default. </dd>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>X509_USER_PROXY</code></dt>
<dd> The location of the user&#8217;s Grid proxy file. Shouldn&#8217;t be set unless the proxy is in a non-standard location. </dd>
<dt><code>ARC_LOCATION</code></dt>
<dd> The location where ARC is installed can be specified by this variable. If not specified the install location will be determined from the path to the command being executed, and if this fails a WARNING will be given stating the location which will be used. </dd>
<dt><code>ARC_PLUGIN_PATH</code></dt>
<dd> The location of ARC plugins can be specified by this variable. Multiple locations can be specified by separating them by : (; in Windows). The default location is <code>$ARC_LOCATION</code>/lib/arc (\ in Windows). </dd>
</dl>
<h2>COPYRIGHT</h2>
<p> APACHE LICENSE Version 2.0 </p>
<h2>AUTHOR</h2>
<p> ARC software is developed by the NorduGrid Collaboration (<a rel="nofollow" href="http://www.nordugrid.org">http://www.nordugrid.org</a>), please consult the AUTHORS file distributed with ARC. Please report bugs and feature requests to <a rel="nofollow" href="http://bugzilla.nordugrid.org">http://bugzilla.nordugrid.org</a> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-arccat/">arccat</a></code>(1), <code><a href="/docs/linux/man/1-arcclean/">arcclean</a></code>(1), <code><a href="/docs/linux/man/1-arccp/">arccp</a></code>(1), <code><a href="/docs/linux/man/1-arcget/">arcget</a></code>(1), <code><a href="/docs/linux/man/1-arcinfo/">arcinfo</a></code>(1), <code><a href="/docs/linux/man/1-arckill/">arckill</a></code>(1), <code><a href="/docs/linux/man/1-arcls/">arcls</a></code>(1), <code><a href="/docs/linux/man/1-arcmkdir/">arcmkdir</a></code>(1), <code><a href="/docs/linux/man/1-arcproxy/">arcproxy</a></code>(1), <code><a href="/docs/linux/man/1-arcrenew/">arcrenew</a></code>(1), <code><a href="/docs/linux/man/1-arcresub/">arcresub</a></code>(1), <code><a href="/docs/linux/man/1-arcrm/">arcrm</a></code>(1), <code><a href="/docs/linux/man/1-arcstat/">arcstat</a></code>(1), <code><a href="/docs/linux/man/1-arcsub/">arcsub</a></code>(1), <code><a href="/docs/linux/man/1-arcsync/">arcsync</a></code>(1), <code><a href="/docs/linux/man/1-arctest/">arctest</a></code>(1) </p>
