---
title: "globus-job-manager(8)"
name: "globus-job-manager"
section: "8"
letter: "g"
url: "/docs/linux/man/8-globus-job-manager/"
description: "globus-job-manager – Execute and monitor jobs"
---

<p>globus-job-manager &#8211; Execute and monitor jobs</p>
<h2>Synopsis</h2>
<p><code>globus-job-manager</code> -type <i>LRM</i> [-conf <i>CONFIG_PATH</i>] [-help ] [-globus-host-manufacturer <i>MANUFACTURER</i>] [-globus-host-cputype <i>CPUTYPE</i>] [-globus-host-osname <i>OSNAME</i>] [-globus-host-osversion <i>OSVERSION</i>] [-globus-gatekeeper-host <i>HOST</i>] [-globus-gatekeeper-port <i>PORT</i>] [-globus-gatekeeper-subject <i>SUBJECT</i>] [-home <i>GLOBUS_LOCATION</i>] [-target-globus-location <i>TARGET_GLOBUS_LOCATION</i>] [-condor-arch <i>ARCH</i>] [-condor-os <i>OS</i>] [-history <i>HISTORY_DIRECTORY</i>] [-scratch-dir-base <i>SCRATCH_DIRECTORY</i>] [-enable-syslog ] [-stdio-log <i>LOG_DIRECTORY</i>] [-log-pattern <i>PATTERN</i>] [-log-levels <i>LEVELS</i>] [-state-file-dir <i>STATE_DIRECTORY</i>] [-globus-tcp-port-range <i>PORT_RANGE</i>] [-globus-tcp-source-range <i>SOURCE_RANGE</i>] [-x509-cert-dir <i>TRUSTED_CERTIFICATE_DIRECTORY</i>] [-cache-location <i>GASS_CACHE_DIRECTORY</i>] [-k ] [-extra-envvars <i>VAR=VAL,&#8230;</i>] [-seg-module <i>SEG_MODULE</i>] [-audit-directory <i>AUDIT_DIRECTORY</i>] [-globus-toolkit-version <i>TOOLKIT_VERSION</i>] [-disable-streaming ] [-disable-usagestats ] [-usagestats-targets <i>TARGET</i>] [-service-tag <i>SERVICE_TAG</i>]</p>
<h2>Description</h2>
<p>The <code>globus-job-manager</code> program is a servivce which starts and controls GRAM jobs which are executed by a local resource management system, such as LSF or Condor. The <code>globus-job-manager</code> program is typically started by the <code>globus-gatekeeper</code> program and not directly by a user. It runs until all jobs it is managing have terminated or its delegated credentials have expired. </p>
<p> Typically, users interact with the <code>globus-job-manager</code> program via client applications such as <code>globusrun</code>, <code>globus-job-submit</code>, or tools such as CoG jglobus or Condor-G. </p>
<p> The full set of command-line options to <code>globus-job-manager</code> consists of: </p>
<p> <code>-help</code></p>
<dl>
<dd>Display a help message to standard error and exit</dl>
<p> <code>-type </code><i>LRM</i></p>
<dl>
<dd>Execute jobs using the local resource manager named <i>LRM</i>.</dl>
<p> <code>-conf </code><i>CONFIG_PATH</i></p>
<dl>
<dd>Read additional command-line arguments from the file <i>CONFIG_PATH</i>. If present, this must be the first command-line argument to the <code>globus-job-manager</code> program.</dl>
<p> <code>-globus-host-manufacturer </code><i>MANUFACTURER</i>:: Indicate the manufacturer of the system which the jobs will execute on. This parameter sets the value of the $(GLOBUS_HOST_MANUFACTURER) RSL substitution to <i>MANUFACTURER</i> </p>
<p> <code>-globus-host-cputype </code><i>CPUTYPE</i></p>
<dl>
<dd>Indicate the CPU type of the system which the jobs will execute on. This parameter sets the value of the $(GLOBUS_HOST_CPUTYPE) RSL substitution to <i>CPUTYPE</i></dl>
<p> <code>-globus-host-osname </code><i>OSNAME</i></p>
<dl>
<dd>Indicate the operating system type of the system which the jobs will execute on. This parameter sets the value of the $(GLOBUS_HOST_OSNAME) RSL substitution to <i>OSNAME</i></dl>
<p> <code>-globus-host-osversion </code><i>OSVERSION</i></p>
<dl>
<dd>Indicate the operating system version of the system which the jobs will execute on. This parameter sets the value of the $(GLOBUS_HOST_OSVERSION) RSL substitution to <i>OSVERSION</i></dl>
<p> <code>-globus-gatekeeper-host </code><i>HOST</i></p>
<dl>
<dd>Indicate the host name of the machine which the job was submitted to. This parameter sets the value of the $(GLOBUS_GATEKEEPER_HOST) RSL substitution to <i>HOST</i></dl>
<p> <code>-globus-gatekeeper-port </code><i>PORT</i></p>
<dl>
<dd>Indicate the TCP port number of gatekeeper to which jobs are submitted to. This parameter sets the value of the $(GLOBUS_GATEKEEPER_PORT) RSL substitution to <i>PORT</i></dl>
<p> <code>-globus-gatekeeper-subject </code><i>SUBJECT</i></p>
<dl>
<dd>Indicate the X.509 identity of the gatekeeper to which jobs are submitted to. This parameter sets the value of the $(GLOBUS_GATEKEEPER_SUBJECT) RSL substitution to <i>SUBJECT</i></dl>
<p> <code>-home </code><i>GLOBUS_LOCATION</i></p>
<dl>
<dd>Indicate the path where the Globus Toolkit(r) is installed on the service node. This is used by the job manager to locate its support and configuration files.</dl>
<p> <code>-target-globus-location </code><i>TARGET_GLOBUS_LOCATION</i></p>
<dl>
<dd>Indicate the path where the Globus Toolkit(r) is installed on the execution host. If this is omitted, the value specified as a parameter to <i>-home</i> is used. This parameter sets the value of the $(GLOBUS_LOCATION) RSL substitution to <i>TARGET_GLOBUS_LOCATION</i></dl>
<p> <code>-history </code><i>HISTORY_DIRECTORY</i></p>
<dl>
<dd>Configure the job manager to write job history files to <i>HISTORY_DIRECTORY</i>. These files are described in the FILES section below.</dl>
<p> <code>-scratch-dir-base </code><i>SCRATCH_DIRECTORY</i></p>
<dl>
<dd>Configure the job manager to use <i>SCRATCH_DIRECTORY</i> as the default scratch directory root if a relative path is specified in the job RSL&#8217;s scratch_dir attribute.</dl>
<p> <code>-enable-syslog</code></p>
<dl>
<dd>Configure the job manager to write log messages via syslog. Logging is further controlled by the argument to the <i>-log-levels</i> parameter described below.</dl>
<p> <code>-log-pattern </code><i>PATTERN</i></p>
<dl>
<dd>Configure the job manager to write log messages to files named by the string <i>PATTERN</i>. The <i>PATTERN</i> string may contain job-independent RSL substitutions such as $(HOME), $(LOGNAME), etc, as well as the special RSL substition $(DATE) which will be resolved at log time to the date in YYYYMMDD form.</dl>
<p> <code>-stdio-log </code><i>LOG_DIRECTORY</i></p>
<dl>
<dd>Configure the job manager to write log messages to files in the <i>LOG_DIRECTORY</i> directory. This is a backward-compatible parameter, equivalent to &#8216;-log-pattern &#8216;.</dl>
<p> <code>-log-levels </code><i>LEVELS</i></p>
<dl>
<dd>Configure the job manager to write log messages of certain levels to syslog and/or log files. The available log levels are FATAL, ERROR, WARN, INFO, DEBUG, and TRACE. Multiple values can be combined with the | character. The default value of logging when enabled is FATAL|ERROR.</dl>
<p> <code>-state-file-dir </code><i>STATE_DIRECTORY</i></p>
<dl>
<dd>Configure the job manager to write state files to <i>STATE_DIRECTORY</i>. If not specified, the job manager uses the default of $GLOBUS_LOCATION/tmp/gram_job_state/. This directory must be writable by all users and be on a file system which supports POSIX advisory file locks. . This directory must be writable by all users and be on a file system which supports POSIX advisory file locks.</dl>
<p> <code>-globus-tcp-port-range </code><i>PORT_RANGE</i></p>
<dl>
<dd>Configure the job manager to restrict its TCP/IP communication to use ports in the range described by <i>PORT_RANGE</i>. This value is also made available in the job environment via the GLOBUS_TCP_PORT_RANGE environment variable.</dl>
<p> <code>-globus-tcp-source-range </code><i>SOURCE_RANGE</i></p>
<dl>
<dd>Configure the job manager to restrict its TCP/IP communication to use source ports in the range described by <i>SOURCE_RANGE</i>. This value is also made available in the job environment via the GLOBUS_TCP_SOURCE_RANGE environment variable.</dl>
<p> <code>-x509-cert-dir </code><i>TRUSTED_CERTIFICATE_DIRECTORY</i></p>
<dl>
<dd>Configure the job manager to search <i>TRUSTED_CERTIFICATE_DIRECTORY</i> for its list of trusted CA certificates and their signing policies. This value is also made available in the job environment via the X509_CERT_DIR environment variable.</dl>
<p> <code>-cache-location </code><i>GASS_CACHE_DIRECTORY</i></p>
<dl>
<dd>Configure the job manager to use the path <i>GASS_CACHE_DIRECTORY</i> for its temporary GASS-cache files. This value is also made available in the job environment via the GLOBUS_GASS_CACHE_DEFAULT environment variable.</dl>
<p> <code>-k</code></p>
<dl>
<dd>Configure the job manager to assume it is using Kerberos for authentication instead of X.509 certificates. This disables some certificate-specific processing in the job manager.</dl>
<p> <code>-extra-envvars </code><i>VAR=VAL,&#8230;</i></p>
<dl>
<dd>Configure the job manager to define a set of environment variables in the job environment beyond those defined in the base job environment. The format of the parameter to this argument is a comma-separated sequence of VAR=VAL pairs, where VAR is the variable name and VAL is the variable&#8217;s value. If the value is not specified, then the value of the variable in the job manager&#8217;s environment is used. This option may be present multiple times on the command-line or the job manager configuration file to append multiple environment settings.</dl>
<p> <code>-seg-module </code><i>SEG_MODULE</i></p>
<dl>
<dd>Configure the job manager to use the schedule event generator module named by <i>SEG_MODULE</i> to detect job state changes events from the local resource manager, in place of the less efficient polling operations used in GT2. To use this, one instance of the <code>globus-job-manager-event-generator</code> must be running to process events for the LRM into a generic format that the job manager can parse.</dl>
<p> <code>-audit-directory </code><i>AUDIT_DIRECTORY</i></p>
<dl>
<dd>Configure the job manager to write audit records to the directory named by <i>AUDIT_DIRECTORY</i>. This records can be loaded into a database using the <code>globus-gram-audit</code> program.</dl>
<p> <code>-globus-toolkit-version </code><i>TOOLKIT_VERSION</i></p>
<dl>
<dd>Configure the job manager to use <i>TOOLKIT_VERSION</i> as the version for audit and usage stats records.</dl>
<p> <code>-service-tag </code><i>SERVICE_TAG</i></p>
<dl>
<dd>Configure the job manager to use <i>SERVICE_TAG</i> as a unique identifier to allow multiple GRAM instances to use the same job state directories without interfering with each other&#8217;s jobs. If not set, the value untagged will be used.</dl>
<p> <code>-disable-streaming</code></p>
<dl>
<dd>Configure the job manager to disable file streaming. This is propagated to the LRM script interface but has no effect in GRAM5.</dl>
<p> <code>-disable-usagestats</code></p>
<dl>
<dd>Disable sending of any usage stats data, even if <i>-usagestats-targets</i> is present in the configuration.</dl>
<p> <code>-usagestats-targets </code><i>TARGET</i></p>
<dl>
<dd>Send usage packets to a data collection service for analysis. The <i>TARGET</i> string consists of a comma-separated list of HOST:PORT combinations, each contaiing an optional list of data to send. See Usage Stats Packets for more information about the tags. Special tag strings of all (which enables all tags) and default may be used, or a sequence of characters for the various tags. If this option is not present in the configuration, then the default of usage-stats.globus.org:4810 is used.</dl>
<p> <code>-condor-arch </code><i>ARCH</i></p>
<dl>
<dd>Set the architecture specification for condor jobs to be <i>ARCH</i> in job classified ads generated by the GRAM5 codnor LRM script. This is required for the condor LRM but ignored for all others.</dl>
<p> <code>-condor-os </code><i>OS</i></p>
<dl>
<dd>Set the operating system specification for condor jobs to be <i>OS</i> in job classified ads generated by the GRAM5 codnor LRM script. This is required for the condor LRM but ignored for all others.</dl>
<h2>Environment</h2>
<p>If the following variables affect the execution of <code>globus-job-manager</code> </p>
<p> <code>HOME</code></p>
<dl>
<dd>User&#8217;s home directory.</dl>
<p> <code>LOGNAME</code></p>
<dl>
<dd>User&#8217;s name.</dl>
<p> <code>JOBMANAGER_SYSLOG_ID</code></p>
<dl>
<dd>String to prepend to syslog audit messages.</dl>
<p> <code>JOBMANAGER_SYSLOG_FAC</code></p>
<dl>
<dd>Facility to log syslog audit messages as.</dl>
<p> <code>JOBMANAGER_SYSLOG_LVL</code></p>
<dl>
<dd>Priority level to use for syslog audit messages.</dl>
<p> <code>GATEKEEPER_JM_ID</code></p>
<dl>
<dd>Job manager ID to be used in syslog audit records.</dl>
<p> <code>GATEKEEPER_PEER</code></p>
<dl>
<dd>Peer information to be used in syslog audit records</dl>
<p> <code>GLOBUS_ID</code></p>
<dl>
<dd>Credential information to be used in syslog audit records</dl>
<p> <code>GLOBUS_JOB_MANAGER_SLEEP</code></p>
<dl>
<dd>Time (in seconds) to sleep when the job manager is started. [For debugging purposes only]</dl>
<p> <code>GRID_SECURITY_HTTP_BODY_FD</code></p>
<dl>
<dd>File descriptor of an open file which contains the initial job request and to which the initial job reply should be sent. This file descriptor is inherited from the <code>globus-gatekeeper</code>.</dl>
<p> <code>X509_USER_PROXY</code></p>
<dl>
<dd>Path to the X.509 user proxy which was delegated by the client to the <code>globus-gatekeeper</code> program to be used by the job manager.</dl>
<p> <code>GRID_SECURITY_CONTEXT_FD</code></p>
<dl>
<dd>File descriptor containing an exported security context that the job manager should use to reply to the client which submitted the job.</dl>
<p> <code>GLOBUS_USAGE_TARGETS</code></p>
<dl>
<dd>Default list of usagestats services to send usage packets to.</dl>
<p> <code>GLOBUS_TCP_PORT_RANGE</code></p>
<dl>
<dd>Default range of allowed TCP ports to listen on. The <i>-globus-tcp-port-range</i> command-line option overrides this.</dl>
<p> <code>GLOBUS_TCP_SOURCE_RANGE</code></p>
<dl>
<dd>Default range of allowed TCP ports to bind to. The <i>-globus-tcp-source-range</i> command-line option overrides this.</dl>
<h2>Files</h2>
<p><code>$HOME/.globus/job/HOSTNAME/LRM.TAG.red</code></p>
<dl>
<dd>Job manager delegated user credential.</dl>
<p> <code>$HOME/.globus/job/HOSTNAME/LRM.TAG.lock</code></p>
<dl>
<dd>Job manager state lock file.</dl>
<p> <code>$HOME/.globus/job/HOSTNAME/LRM.TAG.pid</code></p>
<dl>
<dd>Job manager pid file.</dl>
<p> <code>$HOME/.globus/job/HOSTNAME/LRM.TAG.sock</code></p>
<dl>
<dd>Job manager socket for inter-job manager communications.</dl>
<p> <code>$HOME/.globus/job/HOSTNAME/JOB_ID/</code></p>
<dl>
<dd>Job-specific state directory.</dl>
<p> <code>$HOME/.globus/job/HOSTNAME/JOB_ID/stdin</code></p>
<dl>
<dd>Standard input which has been staged from a remote URL.</dl>
<p> <code>$HOME/.globus/job/HOSTNAME/JOB_ID/stdout</code></p>
<dl>
<dd>Standard output which will be staged from a remote URL.</dl>
<p> <code>$HOME/.globus/job/HOSTNAME/JOB_ID/stderr</code></p>
<dl>
<dd>Standard error which will be staged from a remote URL.</dl>
<p> <code>$HOME/.globus/job/HOSTNAME/JOB_ID/x509_user_proxy</code></p>
<dl>
<dd>Job-specific delegated credential.</dl>
<p> <code>$GLOBUS_LOCATION/tmp/gram_job_state/job.HOSTNAME.JOB_ID</code></p>
<dl>
<dd>Job state file.</dl>
<p> <code>$GLOBUS_LOCATION/tmp/gram_job_state/job.HOSTNAME.JOB_ID.lock</code></p>
<dl>
<dd>Job state lock file. In most cases this will be a symlink to the job manager lock file.</dl>
<p> <code>$GLOBUS_LOCATION/etc/globus-job-manager.conf</code></p>
<dl>
<dd>Default location of the global job manager configuration file.</dl>
<p> <code>$GLOBUS_LOCATION/etc/grid-services/jobmanager-LRM</code></p>
<dl>
<dd>Default location of the LRM-specific gatekeeper configuration file.</dl>
<p> <code>$GLOBUS_LOCATION/etc/globus/gram/job&#8212;manager.rvf</code></p>
<dl>
<dd>Default location of the site-specific job manager RSL validation file.</dl>
<p> <code>$GLOBUS_LOCATION/etc/globus/gram/lrm.rvf</code></p>
<dl>
<dd>Default location of the site-specific job manager RSL validation file for the named lrm.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-globusrun/">globusrun</a>(1), <a href="/docs/linux/man/8-globus-gatekeeper/">globus-gatekeeper</a>(8), <a href="/docs/linux/man/1-globus-personal-gatekeeper/">globus-personal-gatekeeper</a>(1), <a href="/docs/linux/man/8-globus-gram-audit/">globus-gram-audit</a>(8)</p>
<h2>Author</h2>
<p>Copyright &#169; 1999-2016 University of Chicago</p>
