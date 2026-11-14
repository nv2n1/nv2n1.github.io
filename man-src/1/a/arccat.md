---
title: "arccat(1)"
name: "arccat"
section: "1"
letter: "a"
url: "/docs/linux/man/1-arccat/"
description: "arccat – ARC Catenate"
---

<h2 class="name">NAME</h2>
<p> arccat &#8211; ARC Catenate</p>
<h2>DESCRIPTION</h2>
<p> The <code>arccat</code> command can be used to view the stdout or stderr of a running job. It can also be used to show A-REX&#8217;s error log of a job. </p>
<h2>SYNOPSIS</h2>
<p> <code>arccat [options] [job &#8230;]</code> </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code>, <code>&#8211;all</code></p>
<dd> all jobs</p>
<dt><code>-j</code>, <code>&#8211;joblist</code>=<i>filename</i></p>
<dd> the file storing information about active jobs (default ~/.arc/jobs.xml)</p>
<dt><code>-i</code>, <code>&#8211;jobids-from-file</code>=<i>filename</i></p>
<dd> a file containing a list of jobIDs</p>
<dt><code>-c</code>, <code>&#8211;cluster</code>=<i>name</i></p>
<dd> select one or more computing elements: <i>name</i> can be an alias for a single CE, a group of CEs or a URL</p>
<dt><code>-r</code>, <code>&#8211;rejectmanagement</code>=<i>URL</i></p>
<dd> skip jobs which are on a computing element with a given URL</p>
<dt><code>-s</code>, <code>&#8211;status</code>=<i>statusstr</i></p>
<dd> only select jobs whose status is statusstr</p>
<dt><code>-o</code>, <code>&#8211;stdout</code></p>
<dd> show the stdout of the job (default)</p>
<dt><code>-e</code>, <code>&#8211;stderr</code></p>
<dd> show the stderr of the job</p>
<dt><code>-l</code>, <code>&#8211;joblog</code></p>
<dd> show A-REX&#8217;s error log of the job</p>
<dt><code>-P</code>, <code>&#8211;listplugins</code></p>
<dd> list the available plugins</p>
<dt><code>-t</code>, <code>&#8211;timeout</code>=<i>seconds</i></p>
<dd> timeout in seconds (default 20)</p>
<dt><code>-z</code>, <code>&#8211;conffile</code>=<i>filename</i></p>
<dd> configuration file (default ~/.arc/client.conf)</p>
<dt><code>-d</code>, <code>&#8211;debug</code>=<i>debuglevel</i></p>
<dd> FATAL, ERROR, WARNING, INFO, VERBOSE or DEBUG</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> print version information</p>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd> print help</dl>
<h2>ARGUMENTS</h2>
<dl>
<dt><code>job</code> &#8230;</p>
<dd> list of jobids and/or jobnames</dl>
<h2>EXTENDED DESCRIPTION</h2>
<p> The <code>arccat</code> command displays the stdout or stderr of running jobs. It can also display A-REX&#8217;s error log of a job. The job can be referred to either by the jobid that was returned by <code><a href="/docs/linux/man/1-arcsub/">arcsub</a></code>(1) at submission time or by its jobname if the job description that was submitted contained a jobname attribute. </p>
<p> More than one jobid and/or jobname can be given. If several jobs were submitted with the same jobname the stdout, stderr or A-REX error log of all those jobs are shown. If the <code>&#8211;joblist</code> option is used the list of jobs is read from a file with the specified filename. By specifying the <code>&#8211;all</code> option, the stdout, stderr or A-REX error log of all active jobs will be shown. </p>
<p> The <code>&#8211;cluster</code> option can be used to select or reject jobs at specific clusters. See <code><a href="/docs/linux/man/1-arcsub/">arcsub</a></code>(1) for a discussion of the format of arguments to this option. The <code>&#8211;status</code> option can be used to select jobs in a specific state. These options can be repeated several times. See <code><a href="/docs/linux/man/1-arstat/">arstat</a></code>(1) for possible state values. </p>
<p> Only jobs where the stdout or stderr argument was given in the job description can display the contents of those files. </p>
<h2>FILES</h2>
<dl>
<dt><code>~/.arc/client.conf</code></p>
<dd> Some options can be given default values by specifying them in the ARC client configuration file. By using the <code>&#8211;conffile</code> option a different configuration file can be used than the default. </p>
<dt><code>~/.arc/jobs.xml</code></p>
<dd> This a local list of the user&#8217;s active jobs. When a job is successfully submitted it is added to this list and when it is removed from the remote cluster it is removed from this list. This list is used as the list of all active jobs when the user specifies the <code>&#8211;all</code> option to the various NorduGrid ARC user interface commands. By using the <code>&#8211;joblist</code> option a different file can be used than the default. </p>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>X509_USER_PROXY</code></p>
<dd> The location of the user&#8217;s Grid proxy file. Shouldn&#8217;t be set unless the proxy is in a non-standard location. </p>
<dt><code>ARC_LOCATION</code></p>
<dd> The location where ARC is installed can be specified by this variable. If not specified the install location will be determined from the path to the command being executed, and if this fails a WARNING will be given stating the location which will be used. </p>
<dt><code>ARC_PLUGIN_PATH</code></p>
<dd> The location of ARC plugins can be specified by this variable. Multiple locations can be specified by separating them by : (; in Windows). The default location is <code>$ARC_LOCATION</code>/lib/arc (\ in Windows). </p>
</dl>
<h2>COPYRIGHT</h2>
<p> APACHE LICENSE Version 2.0 </p>
<h2>AUTHOR</h2>
<p> ARC software is developed by the NorduGrid Collaboration (<a rel="nofollow" href="http://www.nordugrid.org">http://www.nordugrid.org</a>), please consult the AUTHORS file distributed with ARC. Please report bugs and feature requests to <a rel="nofollow" href="http://bugzilla.nordugrid.org">http://bugzilla.nordugrid.org</a> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-arcclean/">arcclean</a></code>(1), <code><a href="/docs/linux/man/1-arccp/">arccp</a></code>(1), <code><a href="/docs/linux/man/1-arcget/">arcget</a></code>(1), <code><a href="/docs/linux/man/1-arcinfo/">arcinfo</a></code>(1), <code><a href="/docs/linux/man/1-arckill/">arckill</a></code>(1), <code><a href="/docs/linux/man/1-arcls/">arcls</a></code>(1), <code><a href="/docs/linux/man/1-arcmkdir/">arcmkdir</a></code>(1), <code><a href="/docs/linux/man/1-arcproxy/">arcproxy</a></code>(1), <code><a href="/docs/linux/man/1-arcrenew/">arcrenew</a></code>(1), <code><a href="/docs/linux/man/1-arcresub/">arcresub</a></code>(1), <code><a href="/docs/linux/man/1-arcresume/">arcresume</a></code>(1), <code><a href="/docs/linux/man/1-arcrm/">arcrm</a></code>(1), <code><a href="/docs/linux/man/1-arcstat/">arcstat</a></code>(1), <code><a href="/docs/linux/man/1-arcsub/">arcsub</a></code>(1), <code><a href="/docs/linux/man/1-arcsync/">arcsync</a></code>(1), <code><a href="/docs/linux/man/1-arctest/">arctest</a></code>(1) </p>
<h2>Index</h2>
