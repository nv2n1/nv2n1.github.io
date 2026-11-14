---
title: "arcresub(1)"
name: "arcresub"
section: "1"
letter: "a"
url: "/docs/linux/man/1-arcresub/"
description: "arcresub – ARC Resubmission"
---

<h2 class="name">NAME</h2>
<p> arcresub &#8211; ARC Resubmission</p>
<h2>DESCRIPTION</h2>
<p> The <code>arcresub</code> command is used for resubmitting jobs to grid enabled computing resources. </p>
<h2>SYNOPSIS</h2>
<p> <code>arcresub [options] [jobid &#8230;]</code> </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code>, <code>&#8211;all</code></p>
<dd> all jobs</p>
<dt><code>-j</code>, <code>&#8211;joblist</code>=<i>filename</i></p>
<dd> the file storing information about active jobs (default ~/.arc/jobs.xml)</p>
<dt><code>-i</code>, <code>&#8211;jobids-from-file</code>=<i>filename</i></p>
<dd> a file containing a list of job IDs</p>
<dt><code>-o</code>, <code>&#8211;jobids-to-file</code>=<i>filename</i></p>
<dd> the IDs of the submitted jobs will be appended to this file</p>
<dt><code>-c</code>, <code>&#8211;cluster</code>=<i>name</i></p>
<dd> select one or more computing elements: <i>name</i> can be an alias for a single CE, a group of CEs or a URL</p>
<dt><code>-q</code>, <code>&#8211;qluster</code>=<i>name</i></p>
<dd> select one or more computing elements for the new jobs: <i>name</i> can be an alias for a single CE, a group of CEs or a URL</p>
<dt><code>-g</code>, <code>&#8211;index</code>=<i>name</i></p>
<dd> select one or more registries: <i>name</i> can be an alias for a single registry, a group of registries or a URL</p>
<dt><code>-r</code>, <code>&#8211;rejectmanagement</code>=<i>URL</i></p>
<dd> skip jobs which are on a computing element with a given URL</p>
<dt><code>-R</code>, <code>&#8211;rejectdiscovery</code>=<i>URL</i></p>
<dd> skip the service with the given URL during service discovery</p>
<dt><code>-S</code>, <code>&#8211;submissioninterface</code>=<i>InterfaceName</i></p>
<dd> only use this interface for submitting (e.g. org.nordugrid.gridftpjob, org.ogf.glue.emies.activitycreation, org.ogf.bes)</p>
<dt><code>-I</code>, <code>&#8211;infointerface</code>=<i>InterfaceName</i></p>
<dd> the computing element specified by URL at the command line should be queried using this information interface (possible options: org.nordugrid.ldapng, org.nordugrid.ldapglue2, org.nordugrid.wsrfglue2, org.ogf.glue.emies.resourceinfo)</p>
<dt><code>-k</code>, <code>&#8211;keep</code></p>
<dd> keep the files on the server (do not clean)</p>
<dt><code>-m</code>, <code>&#8211;same</code></p>
<dd> resubmit to the same cluster</p>
<dt><code>-M</code>, <code>&#8211;not-same</code></p>
<dd> do not resubmit to the same cluster</p>
<dt><code>-s</code>, <code>&#8211;status</code>=<i>statusstr</i></p>
<dd> only select jobs whose status is statusstr</p>
<dt><code>-P</code>, <code>&#8211;listplugins</code></p>
<dd> list the available plugins</p>
<dt><code>-t</code>, <code>&#8211;timeout</code>=<i>seconds</i></p>
<dd> timeout in seconds (default 20)</p>
<dt><code>-z</code>, <code>&#8211;conffile</code>=<i>filename</i></p>
<dd> configuration file (default ~/.arc/client.conf)</p>
<dt><code>-d</code>, <code>&#8211;debug</code>=<i>debuglevel</i></p>
<dd> FATAL, ERROR, WARNING, INFO, VERBOSE or DEBUG</p>
<dt><code>-b</code>, <code>&#8211;broker</code>=<i>broker</i></p>
<dd> selected broker: Random (default), FastestQueue or custom</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> print version information</p>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd> print help</dl>
<h2>ARGUMENTS</h2>
<dl>
<dt><code>jobid</code> &#8230;</p>
<dd> job ID or job name of jobs to be resubmitted</dl>
<h2>EXTENDED DESCRIPTION</h2>
<p> The <code>arcresub</code> command is used for resubmitting jobs on grid enabled computing resources. The job can be referred to either by the job ID that was returned by <code><a href="/docs/linux/man/1-arcsub/">arcsub</a></code>(1) at submission time or by its jobname if the job description that was submitted contained a jobname attribute. </p>
<p> More than one job ID and/or jobname can be given. If several jobs were submitted with the same jobname all those jobs will be resubmitted. </p>
<p> If the job description of a job to be resubmitted, contained any local input files, checksums of these was calculated and stored in the job list, and those will be used to check whether the files has changed. If local input files has changed the job will not be resubmitted. </p>
<p> In case the job description is not found in the job list, it will be retrieved from the cluster holding the job. This description however might differ from the one originally used to submit the job, since both the submission client and the cluster can have made modifications to the job description. </p>
<p> Upon resubmision the job will receive a new job ID, and the old job ID will be stored in the local job list file, enabling future back tracing of the resubmitted job. </p>
<p> The name of the local job list file can used specified by the <code>&#8211;joblist</code> option. By specifying the <code>&#8211;all</code> option, all active jobs appearing the in job list file will be resubmitted. </p>
<p> The <code>&#8211;cluster</code> option can be used to select or reject jobs at specific clusters to be resubmitted. See <code><a href="/docs/linux/man/1-arcsub/">arcsub</a></code>(1) for a discussion of the format of arguments to this option. The <code>&#8211;qluster</code> option can be used to force the jobs to be resubmitted to a particular cluster, or to reject resubmission to a particular cluster. Again see <code><a href="/docs/linux/man/1-arcsub/">arcsub</a></code>(1) for a discussion of the format of arguments to this option. The <code>&#8211;status</code> option can be used to select jobs in a specific state. These options can be repeated several times. See <code><a href="/docs/linux/man/1-arstat/">arstat</a></code>(1) for possible state values. Which servers to query can be specified by giving the <code>&#8211;index</code> option to the command. See <code><a href="/docs/linux/man/1-arcsub/">arcsub</a></code>(1) for a discussion of the format of arguments to this option. </p>
<p> The default behaviour of <code>arcresub</code> is to resubmit to any cluster. This behaviour can be changed by specifying the <code>&#8211;same</code> or <code>&#8211;not-same</code> options. The former will resubmit a job to the same cluster as the job resides, and thus the <code>&#8211;qluster</code> and <code>&#8211;index</code> options is ignored. The latter will resubmit a job to any cluster except to the cluster it resides. Note the <code>&#8211;same</code> and <code>&#8211;not-same</code> options cannot be specified together. </p>
<p> If the old job was successfully killed the job will be removed from the remote cluster unless the <code>&#8211;keep</code> option was specified. </p>
<h2>FILES</h2>
<dl>
<dt><code>~/.arc/client.conf</code></p>
<dd> Some options can be given default values by specifying them in the ARC client configuration file. By using the <code>&#8211;conffile</code> option a different configuration file can be used than the default. </p>
<dt><code>~/.arc/jobs.xml</code></p>
<dd> This a local list of the user&#8217;s active jobs. When a job is successfully submitted it is added to this list and when it is removed from the remote cluster it is removed from this list. This list is used as the list of all active jobs when the user specifies the </p>
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
<p> <code><a href="/docs/linux/man/1-arccat/">arccat</a></code>(1), <code><a href="/docs/linux/man/1-arcclean/">arcclean</a></code>(1), <code><a href="/docs/linux/man/1-arccp/">arccp</a></code>(1), <code><a href="/docs/linux/man/1-arcget/">arcget</a></code>(1), <code><a href="/docs/linux/man/1-arcinfo/">arcinfo</a></code>(1), <code><a href="/docs/linux/man/1-arckill/">arckill</a></code>(1), <code><a href="/docs/linux/man/1-arcls/">arcls</a></code>(1), <code><a href="/docs/linux/man/1-arcmkdir/">arcmkdir</a></code>(1), <code><a href="/docs/linux/man/1-arcproxy/">arcproxy</a></code>(1), <code><a href="/docs/linux/man/1-arcrenew/">arcrenew</a></code>(1), <code><a href="/docs/linux/man/1-arcresume/">arcresume</a></code>(1), <code><a href="/docs/linux/man/1-arcrm/">arcrm</a></code>(1), <code><a href="/docs/linux/man/1-arcstat/">arcstat</a></code>(1), <code><a href="/docs/linux/man/1-arcsub/">arcsub</a></code>(1), <code><a href="/docs/linux/man/1-arcsync/">arcsync</a></code>(1), <code><a href="/docs/linux/man/1-arctest/">arctest</a></code>(1) </p>
<h2>Index</h2>
