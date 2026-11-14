---
title: "arctest(1)"
name: "arctest"
section: "1"
letter: "a"
url: "/docs/linux/man/1-arctest/"
description: "arctest – ARC Test Suite"
---

<h2 class="name">NAME</h2>
<p> arctest &#8211; ARC Test Suite</p>
<h2>DESCRIPTION</h2>
<p> The <code>arctest</code> command tests basic ARC client and server setup. </p>
<h2>SYNOPSIS</h2>
<p> <code>arctest [options]</code> </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code>, <code>&#8211;cluster</code>=<i>name</i></p>
<dd> select one or more computing elements: <i>name</i> can be an alias for a single CE, a group of CEs or a URL</p>
<dt><code>-g</code>, <code>&#8211;index</code>=<i>name</i></p>
<dd> select one or more registries: <i>name</i> can be an alias for a single registry, a group of registries or a URL</p>
<dt><code>-R</code>, <code>&#8211;rejectdiscovery</code>=<i>URL</i></p>
<dd> skip the service with the given URL during service discovery</p>
<dt><code>-S</code>, <code>&#8211;submissioninterface</code>=<i>InterfaceName</i></p>
<dd> only use this interface for submitting (e.g. org.nordugrid.gridftpjob, org.ogf.glue.emies.activitycreation, org.ogf.bes)</p>
<dt><code>-I</code>, <code>&#8211;infointerface</code>=<i>InterfaceName</i></p>
<dd> the computing element specified by URL at the command line should be queried using this information interface (possible options: org.nordugrid.ldapng, org.nordugrid.ldapglue2, org.nordugrid.wsrfglue2, org.ogf.glue.emies.resourceinfo)</p>
<dt><code>-J</code> <i>jobid</i>, <code>&#8211;jobid</code>=<i>jobid</i></p>
<dd> submits testjob given by the jobid.</p>
<dt><code>-r</code> <i>time</i>, <code>&#8211;runtime</code>=<i>time</i></p>
<dd> test job runtime specified in case of the 1st test job.</p>
<dt><code>-j</code>, <code>&#8211;joblist</code>=<i>filename</i></p>
<dd> the file storing information about active jobs (default ~/.arc/jobs.xml)</p>
<dt><code>-o</code>, <code>&#8211;jobids-to-file</code>=<i>filename</i></p>
<dd> the IDs of the submitted jobs will be appended to this file</p>
<dt><code>-D</code>, <code>&#8211;dryrun</code></p>
<dd> submit jobs as dry run (no submission to batch system)</p>
<dt><code> &#8211;direct</code></p>
<dd> submit directly &#8211; no resource discovery or matchmaking</p>
<dt><code>-x</code>, <code>&#8211;dumpdescription</code></p>
<dd> do not submit &#8211; dump job description in the language accepted by the target</p>
<dt><code>-E</code>, <code>&#8211;certificate</code></p>
<dd> prints information about installed user- and CA-certificates</p>
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
<dt><code>-v</code>, <code>-version</code></p>
<dd> print version information</p>
<dt><code>-h</code>, <code>-help</code></p>
<dd> print usage information</dl>
<h2>EXTENDED DESCRIPTION</h2>
<p> The <code>arctest</code> command is used for basic testing of ARC client and server installation through submitting various test jobs. It can also print basic information about user&#8217;s certificate. The command is complementary to <code>arcinfo</code> and <code>arcproxy -I</code> </p>
<p> The test jobs available in this version of arctest are: </p>
<p> Test job 1: This test-job calculates prime-numbers for a number of minutes given by <code>-r</code> (default 5) and outputs the list to stderr. The source-code for the prime-number program, the Makefile and the executable are downloaded to the cluster from HTTP and FTP servers and the program is compiled before running. In this way, the test job constitutes a fairly comprehensive test of the basic setup of a grid cluster. </p>
<p> Test job 2: attempts to list all environment variables at the remote site </p>
<p> Test job 3: copies a remote file from an HTTP server into a local file </p>
<h2>EXAMPLES</h2>
<p> arctest -J 1 -c &lt;clustername&gt; </p>
<p> will submit test job number 1 to the specified cluster belonging to the flavor of it. </p>
<p> arctest &#8211;certificate </p>
<p> will print basic information about the user&#8217;s certificate. </p>
<h2>COPYRIGHT</h2>
<p> APACHE LICENSE Version 2.0 </p>
<h2>AUTHOR</h2>
<p> ARC software is developed by the NorduGrid Collaboration (<a rel="nofollow" href="http://www.nordugrid.org">http://www.nordugrid.org</a>), please consult the AUTHORS file distributed with ARC. Please report bugs and feature requests to <a rel="nofollow" href="http://bugzilla.nordugrid.org">http://bugzilla.nordugrid.org</a> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-arccat/">arccat</a></code>(1), <code><a href="/docs/linux/man/1-arcclean/">arcclean</a></code>(1), <code><a href="/docs/linux/man/1-arccp/">arccp</a></code>(1), <code><a href="/docs/linux/man/1-arcget/">arcget</a></code>(1), <code><a href="/docs/linux/man/1-arcinfo/">arcinfo</a></code>(1), <code><a href="/docs/linux/man/1-arckill/">arckill</a></code>(1), <code><a href="/docs/linux/man/1-arcls/">arcls</a></code>(1), <code><a href="/docs/linux/man/1-arcmkdir/">arcmkdir</a></code>(1), <code><a href="/docs/linux/man/1-arcproxy/">arcproxy</a></code>(1), <code><a href="/docs/linux/man/1-arcrenew/">arcrenew</a></code>(1), <code><a href="/docs/linux/man/1-arcresub/">arcresub</a></code>(1), <code><a href="/docs/linux/man/1-arcresume/">arcresume</a></code>(1), <code><a href="/docs/linux/man/1-arcrm/">arcrm</a></code>(1), <code><a href="/docs/linux/man/1-arcstat/">arcstat</a></code>(1), <code><a href="/docs/linux/man/1-arcsub/">arcsub</a></code>(1), <code><a href="/docs/linux/man/1-arcsync/">arcsync</a></code>(1) </p>
<h2>Index</h2>
