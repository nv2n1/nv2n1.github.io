---
title: "globus_gram_job_manager_configuration(3)"
name: "globus_gram_job_manager_configuration"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gram_job_manager_configuration/"
description: "globus_gram_job_manager_configuration – Job Manager Configuration The Job Manager is generally configured using the setup-globus-gram-job-manager setup script."
---

<h2 class="name">NAME</h2>
<p> globus_gram_job_manager_configuration &#8211; Job Manager Configuration The Job Manager is generally configured using the setup-globus-gram-job-manager setup script. </p>
<p> This section of the Job Manager manual describes all options which may be passed to the GRAM Job Manager in the configuration file $GLOBUS_LOCATION/etc/globus-job-manager.conf. </p>
<h2>Configuration File Options</h2>
<p> <code>-save-logfile always|on-error|never</code></p>
<dl>
<dt>
<dd> Create a file to store Job Manager log messages. This file will be created in the user&#8217;s home directory. If the argument to this option is <i>on-error</i> , then the file will be removed if the job manager completes successfully. If the argument to this optionis <i>always</i> , the file will not be deleted by the job manager.</dl>
<p> <code>-k</code></p>
<dl>
<dt>
<dd> Indicate that the job manager was built with the kerberos GSSAPI instead of GSI. This disables checks for a delegated GSI credential.</dl>
<p> <code>-home GLOBUS_LOCATION</code></p>
<dl>
<dt>
<dd> Set the GLOBUS_LOCATION environment variable to the specified Globus-Location.</dl>
<p> <code>-type JOB_MANAGER_TYPE</code></p>
<dl>
<dt>
<dd> Set the type of scheduler interface to use for this job manager. A similarly named Perl module in the $GLOBUS_LOCATION/lib/perl/Globus/GRAM/JobManager/ directory is needed.</dl>
<p> <code>-history PATH</code></p>
<dl>
<dt>
<dd> Set the path to the directory to store job history files.</dl>
<p> <code>-cache-location PATH</code></p>
<dl>
<dt>
<dd> Set the path for the GASS cache. This path must be unique for each user. RSL substitutions (such as /builddir and mockbuild) may be used in this path. See <code>RSL Substitions</code> for a list of available RSL substitutions.</dl>
<p> <code>-extra-envvars VAR1,VAR2,&#8230;</code></p>
<dl>
<dt>
<dd> The Job manager will attempt to get the listed VARs from its environment and set them the same for the job&#8217;s environment. For example, -extra-envvars LD_LIBRARY_PATH,GLOBUS_TCP_PORT_RANGE</dl>
<p> <code>-scratch-dir-base PATH</code></p>
<dl>
<dt>
<dd> Set the default scratch directory root for the job manager. Job-specific scratch directories will be created as a subdirectory of this directory. RSL substitutions (such as /builddir and mockbuild) may be used in this path. See <code>RSL Substitions</code> for a list of available RSL substitutions. If this option is not present in the configuration file, then the job manager will create scratch directories as subdirectories of the user&#8217;s home directory.</dl>
<p> <code>-condor-arch ARCH</code></p>
<dl>
<dt>
<dd> Set the condor architecture for this job manager to be the specified ARCH. This is required when the job manager type is <i>condor</i>.</dl>
<p> <code>-condor-os OSNAME</code></p>
<dl>
<dt>
<dd> Set the condor operating system name for this job manager to be the specified OSNAME. This is required when the job manager type is <i>condor</i>.</dl>
<p> <code>-globus-gatekeeper-host HOST</code></p>
<dl>
<dt>
<dd> Set the name of the gatekeeper host. This will be made available in the GLOBUS_GATEKEEPER_HOST RSL substitution.</dl>
<p> <code>-globus-gatekeeper-port PORT</code></p>
<dl>
<dt>
<dd> Set the TCP port of the gatekeeper. This will be made available in the GLOBUS_GATEKEEPER_PORT RSL substitution.</dl>
<p> <code>-globus-gatekeeper-subject SUBJECT</code></p>
<dl>
<dt>
<dd> Set the GSI subject name of the gatekeeper. This will be made available in the GLOBUS_GATEKEEPER_SUBJECT RSL substitution.</dl>
<p> <code>-globus-host-manufacturer MANUFACTURER</code></p>
<dl>
<dt>
<dd> Set the manufacturer name of the host machine. This will be made available in the GLOBUS_HOST_MANUFACTURER RSL substitution.</dl>
<p> <code>-globus-host-cputype CPUTYPE</code></p>
<dl>
<dt>
<dd> Set the cpu type of the host machine. This will be made available in the GLOBUS_HOST_CPUTYPE RSL substitution.</dl>
<p> <code>-globus-host-osname OSNAME</code></p>
<dl>
<dt>
<dd> Set the operating system name of the host machine. This will be made available in the GLOBUS_HOST_OSNAME RSL substitution.</dl>
<p> <code>-globus-host-osversion OSVERSION</code></p>
<dl>
<dt>
<dd> Set the operating system version of the host machine. This will be made available in the GLOBUS_HOST_OSVERSION RSL substitution.</dl>
<p> <code>-globus-tcp-port-range RANGE</code></p>
<dl>
<dt>
<dd> Set the range of TCP port numbers which the job manager will use. This will also be made available in the GLOBUS_TCP_PORT_RANGE environment variable and RSL substitution.</dl>
<p> <code>-state-file-dir PATH</code></p>
<dl>
<dt>
<dd> Set the path to store job manager state files (used for restarting a job manager which fails). If this is not set, then job state files will be stored in the $GLOBUS_LOCATION/tmp/gram_job_state directory.</dl>
<p> <code>-x509-cert-dir PATH</code></p>
<dl>
<dt>
<dd> Set the path to the X.509 trusted certificate directory on the job execution hosts. If not present, then the trusted certificate directory used by the job manager (usually set by the Gatekeeper) will be used</dl>
<p> <code>-seg-module MODULE</code></p>
<dl>
<dt>
<dd> Use the named module as a way to interact with the scheduler instead of polling for job status.</dl>
<p> <code>-audit-directory DIRECTORY</code></p>
<dl>
<dt>
<dd> Store job auditing records in DIRECTORY. This directory should be sticky and group writable but not group readable. Audit records can be uploaded to a database by using the globus-gram-audit command.</dl>
<p> <code>-globus-toolkit-version VERSION-STRING</code></p>
<dl>
<dt>
<dd> Use the string VERSION-STRING as the toolkit version in audit records.</dl>
<p> <code>-single</code></p>
<dl>
<dt>
<dd> Use the single job manager per user/jobmanager type feature</dl>
<h2>Index</h2>
