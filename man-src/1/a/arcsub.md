---
title: "arcsub(1)"
name: "arcsub"
section: "1"
letter: "a"
url: "/docs/linux/man/1-arcsub/"
description: "arcsub – ARC Submission"
---

<h2 class="name">NAME</h2>
<p> arcsub &#8211; ARC Submission</p>
<h2>DESCRIPTION</h2>
<p> The <code>arcsub</code> command is used for submitting jobs to Grid enabled computing resources. </p>
<h2>SYNOPSIS</h2>
<p> <code>arcsub [options] [filename &#8230;]</code> </p>
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
<dt><code>-e</code>, <code>&#8211;jobdescrstring=</code><i>String</p>
<dd> jobdescription string describing the job to be submitted</p>
<dt></i><code>-f</code>, <code>&#8211;jobdescrfile=</code><i>filename</p>
<dd> jobdescription file describing the job to be submitted</p>
<dt></i><code>-j</code>, <code>&#8211;joblist</code>=<i>filename</i></p>
<dd> the file storing information about active jobs (default ~/.arc/jobs.xml)</p>
<dt><code>-o</code>, <code>&#8211;jobids-to-file</code>=<i>filename</i></p>
<dd> the IDs of the submitted jobs will be appended to this file</p>
<dt><code>-D</code>, <code>&#8211;dryrun</code></p>
<dd> submit jobs as dry run (no submission to batch system)</p>
<dt><code> &#8211;direct</code></p>
<dd> submit directly &#8211; no resource discovery or matchmaking</p>
<dt><code>-x</code>, <code>&#8211;dumpdescription</code></p>
<dd> do not submit &#8211; dump job description in the language accepted by the target</p>
<dt><code>-P</code>, <code>&#8211;listplugins</code></p>
<dd> list the available plugins</p>
<dt><code>-t</code>, <code>&#8211;timeout</code>=<i>seconds</i></p>
<dd> timeout in seconds (default 20)</p>
<dt><code>-z</code>, <code>&#8211;conffile</code>=<i>filename</i></p>
<dd> configuration file (default ~/.arc/client.conf)</p>
<dt><code>-d</code>, <code>&#8211;debug</code>=<i>debuglevel</i></p>
<dd> FATAL, ERROR, WARNING, INFO, VERBOSE or DEBUG</p>
<dt><code>-b</code>, <code>&#8211;broker</code>=<i>broker</i></p>
<dd> selected broker: Random (default), FastestQueue or custom. Use -P to find possible options.</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> print version information</p>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd> print help</dl>
<h2>ARGUMENTS</h2>
<dl>
<dt><code>filename</code> &#8230;</p>
<dd> job description files describing the jobs to be submitted</dl>
<h2>EXTENDED DESCRIPTION</h2>
<p> <code>arcsub</code> is the key command when submitting jobs to Grid enabled computing resources with the ARC client. As default <code>arcsub</code> is able to submit jobs to A-REX, CREAM and EMI ES enabled computing elements (CEs), and as always for successful submission you need to be authenticated at the targeted computing services. Since <code>arcsub</code> is build on a modular library, modules can be installed which enables submission to other targets, e.g. the classic ARC CE Grid-Manager. </p>
<p> Job submission can be accomplished by specifying a job description file to submit as an argument. <code>arcsub</code> will then by default perform resource discovery on the Grid and then the discovered resources will be matched to the job description and ranked according to the chosen broker (<code>&#8211;broker</code> option). If no Grid environment has been configured, please contact your system administrator, or setup one yourself in the client configuration file (see files section). Another option is to explicitly specify a registry service (or multiple) to <code>arcsub</code> using the <code>&#8211;index</code> option, which accepts an URL, alias or group. Alternatively a specific CE (or multiple) can be targeted by using the <code>&#8211;cluster</code> option. If such a scenario is the most common, it is worthwhile to specify those CEs in the client configuration as default services, which makes it superfluous to specify them as argument. In the same manner aliases and groups, defined in the configuration file, can be utilized, and can be used as argument to the <code>&#8211;cluster</code> or <code>&#8211;index</code> options. In all of the above scenarios <code>arcsub</code> obtains resource information from the services which is then used for matchmaking against the job description, however that step can be avoided by specifying the <code>&#8211;direct</code> option, in which case the job description is submitted directly to first specified endpoint. </p>
<p> The format of a classic GRIDFTP-based cluster URLs:<br />
 <code>[<a href="ldap://]">ldap://]</a>&lt;hostname&gt;[:2135/nordugrid-cluster-name=&lt;hostname&gt;,Mds-Vo-name=local,o=grid]</code><br />
 Only the <code>hostname</code> part has to be specified, the rest of the URL is automatically generated. </p>
<p> The format of an A-REX URL is:<br />
 <code>[<a rel="nofollow" href="https://]">https://]</a>&lt;hostname&gt;[:&lt;port&gt;][/&lt;path&gt;]</code><br />
 Here the port is 443 by default, but the path cannot be guessed, so if it is not specified, then the service is assumed to live on the root path. </p>
<p> Job descriptions can also be specified using the <code>&#8211;jobdescrfile</code> option which expect the file name of the description as argument, or the <code>&#8211;jobdescrstring</code> option which expect as argument the job description as a string, and both options can be specified multiple times and one does not exclude the other. The default supported job description languages are xRSL, JSDL and JDL. </p>
<p> If the job description is successfully submitted a job-ID is returned and printed. This job-ID uniquely identifies the job while it is being executed. On the other hand it is also possible that no CEs matches the constraints defined in the description in which case no submission will be done. Upon successful submission, the job-ID along with more technical job information is stored in the job-list file (described below). The stored information enables the job management commands of the ARC client to manage jobs easily, and thus the job-ID need not to be saved manually. By default the job-list file is stored in the .arc directory in the home directory of the user, however another location can be specified using the <code>&#8211;joblist</code> option taking the location of this file as argument. If the <code>&#8211;joblist</code> option was used during submission, it should also be specified in the consecutive commands when managing the job. If a Computing Element has multiple job submission interfaces (e.g. gridftp, EMI-ES, BES), then the brokering algorithm will choose one of them. With the <code>&#8211;submissioninterface</code> option the requested interface can be specified, and in that case only those Computing Elements will be considered which has that specific interface, and only that interface will be used to submit the jobs. </p>
<p> As mentioned above registry or index services can be specified with the <code>&#8211;index</code> option. Specifying one or multiple index servers instructs the <code>arcsub</code> command to query the servers for registered CEs, the returned CEs will then be matched against the job description and those matching will be ranked by the chosen broker (see below) and submission will be tried in order until successful or reaching the end. From the returned list of CEs it might happen that a troublesome or undesirable CE is selected for submission, in that case it possible to reject that cluster using the <code>&#8211;rejectdiscovery</code> option and providing the URL (or just the hostname) of the CE, which will disregard that CE as a target for submission. </p>
<p> When multiple CEs are targeted for submission, the resource broker will be used to filter out CEs which do not match the job description requirements and then rank the remaining CEs. The broker used by default will rank the CEs randomly, however a different broker can be chosen by using the <code>&#8211;broker</code> option, which takes the name of the broker as argument. The broker type can also be specified in client.conf. The brokers available can be seen using <code>arcsub -P.</code> By default the following brokers are available:</p>
<dl>
<dt>Random (default)</p>
<dd> Chooses a random CE matching the job requirements.</p>
<dt>FastestQueue</p>
<dd> Ranks matching CEs according to the length of the job queue at the CEs, ranking those with shortest queue first/highest.</p>
<dt>Benchmark</p>
<dd> Ranks matching CEs according to a specified benchmark, which should be specified by appending the broker name with &#8216;:&#8217; and then the name of the benchmark. If no option is given to the Benchmark broker then CEs will be ranked according to the &#8216;specint2000&#8217; benchmark.</p>
<dt>Data</p>
<dd> Ranks matching CEs according to the amount of input data cached by each CE, by querying the CE. Only CEs with the A-REX BES interface support this operation.</p>
<dt>Null</p>
<dd> Choose a random CE with no filtering at all of CEs.</p>
<dt>PythonBroker</p>
<dd> User-defined custom brokers can be created in Python. See the example broker SampleBroker.py or ACIXBroker.py (like Data broker but uses the ARC Cache Index) that come installed with ARC for more details of how to write your own broker. A PythonBroker is specified by <code>&#8211;broker PythonBroker:Filename.Class:args</code>, where Filename is the file containing the class Class which implements the broker interface. The directory containing this file must be in the PYTHONPATH. args is optional and allows specifying arguments to the broker.</dl>
<p> Before submission, <code>arcsub</code> performs an intelligent modification of the job description (adding or modifying attributes, even converting the description language to fit the needs of the CE) ensuring that it is valid. The modified job description can be printed by specifying the <code>&#8211;dumpdescription</code> option. The format, i.e. job description language, of the printed job description cannot be specified, and will be that which will be sent to and accepted by the chosen target. Further information from <code>arcsub</code> can be obtained by increasing the verbosity, which is done with the <code>&#8211;debug</code> option where the default verbosity level is WARNING. Setting the level to DEBUG will show all messages, while setting it to FATAL will only show fatal log messages. </p>
<p> To <code>validate</code> your job description without actually submitting a job, use the <code>&#8211;dryrun</code> option: it will capture possible syntax or other errors, but will instruct the site not to submit the job for execution. Only the grid-manager (ARC0) and A-REX (ARC1) CEs support this feature. </p>
<h2>EXAMPLES</h2>
<p> Submission of a job description file &quot;helloworld.jsdl&quot; to the Grid<br />
 <code>arcsub helloworld.jsdl</code> </p>
<p> A information index server (registry) can also be queried for CEs to submit to:<br />
 <code>arcsub -g registry.example.com helloworld.jsdl</code> </p>
<p> Submission of a job description file &quot;helloworld.jsdl&quot; to ce.example.com:<br />
 <code>arcsub -c ce.example.com helloworld.jsdl</code> </p>
<p> Direct submission to a CE is done as:<br />
 <code>arcsub &#8211;direct -c cd.example.com helloworld.jsdl</code> </p>
<p> The job description can also be specified directly on the command line as shown in the example, using the XRSL job description language:<br />
 <code>arcsub -c example.com/arex -e \<br />
 &#8216;&amp;(executable=&quot;/bin/echo&quot;)(arguments=&quot;Hello World!&quot;)&#8217;</code> </p>
<p> When submitting against CEs retrieved from information index servers it might be useful to do resource brokering:<br />
 <code>arcsub -g registry.example.com -b FastestQueue helloworld.jsdl</code> </p>
<p> If the job has a large input data set, it can be useful to send it to a CE where those files are already cached. The ACIX broker can be used for this:<br />
 <code>arcsub -g registry.example.com -b PythonBroker:ACIXBroker.ACIXBroker:<a rel="nofollow" href="https://cacheindex.ndgf.org:6443/data/index">https://cacheindex.ndgf.org:6443/data/index</a> helloworld.jsdl</code> </p>
<p> Disregarding a specific CE for submission submitting against an information index server:<br />
 <code>arcsub -g registry.example.com -R badcomputingelement.com/arex helloworld.jsdl</code> </p>
<p> Dumping the job description is done as follows:<br />
 <code>arcsub -c example.com/arex -x helloworld.jsdl</code> </p>
<h2>FILES</h2>
<dl>
<dt><code>~/.arc/client.conf</code></p>
<dd> Some options can be given default values by specifying them in the ARC client configuration file. Registry and computing element services can be specified in separate sections of the config. The default services can be specified by adding &#8216;default=yes&#8217; attribute to the section of the service, thus when no <code>&#8211;cluster</code> or <code>&#8211;index</code> options are given these will be used for submission. Each service has an alias, and can be member of any number of groups. Then specifying the alias or the name of the group with the <code>&#8211;cluster</code> or <code>&#8211;index</code> options will select the given services. By using the <code>&#8211;conffile</code> option a different configuration file can be used than the default. Note that some installations also have a system client configuration file, however attributes in the client one takes precedence, and then command line options takes precedence over configuration file attributes. </p>
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
<p> <code><a href="/docs/linux/man/1-arccat/">arccat</a></code>(1), <code><a href="/docs/linux/man/1-arcclean/">arcclean</a></code>(1), <code><a href="/docs/linux/man/1-arccp/">arccp</a></code>(1), <code><a href="/docs/linux/man/1-arcget/">arcget</a></code>(1), <code><a href="/docs/linux/man/1-arcinfo/">arcinfo</a></code>(1), <code><a href="/docs/linux/man/1-arckill/">arckill</a></code>(1), <code><a href="/docs/linux/man/1-arcls/">arcls</a></code>(1), <code><a href="/docs/linux/man/1-arcmkdir/">arcmkdir</a></code>(1), <code><a href="/docs/linux/man/1-arcproxy/">arcproxy</a></code>(1), <code><a href="/docs/linux/man/1-arcrenew/">arcrenew</a></code>(1), <code><a href="/docs/linux/man/1-arcresub/">arcresub</a></code>(1), <code><a href="/docs/linux/man/1-arcresume/">arcresume</a></code>(1), <code><a href="/docs/linux/man/1-arcrm/">arcrm</a></code>(1), <code><a href="/docs/linux/man/1-arcstat/">arcstat</a></code>(1), <code><a href="/docs/linux/man/1-arcsync/">arcsync</a></code>(1), <code><a href="/docs/linux/man/1-arctest/">arctest</a></code>(1) </p>
<h2>Index</h2>
