---
title: "globus_gram_job_manager_job_execution_environment(3)"
name: "globus_gram_job_manager_job_execution_environment"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gram_job_manager_job_execution_environment/"
description: "globus_gram_job_manager_job_execution_environment – Job Execution Environment"
---

<h2>Environment Variables</h2>
<p> The GRAM Job Manager provides a minimal environment for user&#8217;s jobs. The following environment variables will be set by the job manager. Variables marked with an asterisk (*) will only be set if a related job manager configuration option or RSL attribute is provided. Local schedulers may set additional environment variables. </p>
<p> <code>HOME</code></p>
<dl>
<dt>
</dt><dd> The user&#8217;s home directory.</dd></dl>
<p> <code>LOGNAME</code></p>
<dl>
<dt>
</dt><dd> The user&#8217;s login name.</dd></dl>
<p> <code>X509_USER_PROXY</code></p>
<dl>
<dt>
</dt><dd> The path to the job manager&#8217;s delegated credential. (GSI only).</dd></dl>
<p> <code>GLOBUS_GRAM_JOB_CONTACT</code></p>
<dl>
<dt>
</dt><dd> The job manager&#8217;s contact string for this job.</dd></dl>
<p> <code>GLOBUS_LOCATION</code></p>
<dl>
<dt>
</dt><dd> The path to the Globus installation on the job manager host.</dd></dl>
<p> <code>X509_CERT_DIR*</code></p>
<dl>
<dt>
</dt><dd> The path to a trusted certificate directory. This variable will only be set if the -x509-cert-dir argument is given to the job manager.</dd></dl>
<p> <code>GLOBUS_GASS_CACHE_DEFAULT*</code></p>
<dl>
<dt>
</dt><dd> The path to the job&#8217;s GASS cache (if the gass_cache RSL attribute is present).</dd></dl>
<p> <code>GLOBUS_TCP_PORT_RANGE*</code></p>
<dl>
<dt>
</dt><dd> A system-specific range of TCP ports which may be used by the job. Globus I/O will automatically honor this range. Only present if the related configuration option is present in the job manager configuration file.</dd></dl>
<p> <code>GLOBUS_REMOTE_IO_URL*</code></p>
<dl>
<dt>
</dt><dd> The path to a file containing a URL string of a GASS server which the job may access (if the remote_io_url attribute is present).</dd></dl>
<p> <code>GLOBUS_NEXUS_NO_GSI</code></p>
<dl>
<dt>
</dt><dd> Disables GSI in Nexus&#8217;s TCP protocol, for compatibility with Nexus 4.6 and earlier.</dd></dl>
<h2>RSL Substitions</h2>
<p> In addition to the environment variables described above, a number of RSL substitutions are made available by the job manager. These substitions may be added to the environment by the job RSL if needed. </p>
<p> <code>HOME</code></p>
<dl>
<dt>
</dt><dd> The user&#8217;s home directory.</dd></dl>
<p> <code>LOGNAME</code></p>
<dl>
<dt>
</dt><dd> The user&#8217;s login name.</dd></dl>
<p> <code>GLOBUS_ID</code></p>
<dl>
<dt>
</dt><dd> The subject name of the security credentials under which the job is running.</dd></dl>
<p> <code>GLOBUS_GRAM_JOB_CONTACT</code></p>
<dl>
<dt>
</dt><dd> The job manager&#8217;s contact string for this job.</dd></dl>
<p> <code>GLOBUS_HOST_MANUFACTURER</code></p>
<dl>
<dt>
</dt><dd> The manufacturer part of the host configuration string (derived from config.guess)</dd></dl>
<p> <code>GLOBUS_HOST_CPUTYPE</code></p>
<dl>
<dt>
</dt><dd> The CPU type part of the host configuration string (derived from config.guess)</dd></dl>
<p> <code>GLOBUS_HOST_OSNAME</code></p>
<dl>
<dt>
</dt><dd> The operating system name part of the host configuration string (derived from config.guess)</dd></dl>
<p> <code>GLOBUS_HOST_OSVERSION</code></p>
<dl>
<dt>
</dt><dd> The operating system version number part of the host configuration string (derived from config.guess)</dd></dl>
<p> <code>GLOBUS_GATEKEEPER_HOST</code></p>
<dl>
<dt>
</dt><dd> The name of the host on which the gatekeeper is running.</dd></dl>
<p> <code>GLOBUS_GATEKEEPER_PORT</code></p>
<dl>
<dt>
</dt><dd> The TCP port which on which the gatekeeper is accepting connections.</dd></dl>
<p> <code>GLOBUS_GATEKEEPER_SUBJECT</code></p>
<dl>
<dt>
</dt><dd> The subject name of the security credentials under which the gatekeeper is running.</dd></dl>
<p> <code>GLOBUS_LOCATION</code></p>
<dl>
<dt>
</dt><dd> The path to the Globus installation on the job manager host.</dd></dl>
<p> <code>GLOBUS_CACHED_STDOUT</code></p>
<dl>
<dt>
</dt><dd> The name of the local file in the cache where stdout is being stored. This may be used as the value of the stdout RSL attribute to cause one copy of output to be stored in the cache. A stdio_update signal may be used to retrieve the output when the job is finishing.</dd></dl>
<p> <code>GLOBUS_CACHED_STDERR</code></p>
<dl>
<dt>
</dt><dd> The name of the local file in the cache where stderr is being stored. This may be used as the value of the stderr RSL attribute to cause one copy of output to be stored in the cache. A stdio_update signal may be used to retrieve the output when the job is finishing.</dd></dl>
<p> <code>SCRATCH_DIRECTORY</code></p>
<dl>
<dt>
</dt><dd> The path of the scratch directory for this job. (Only set if the scratch_dir RSL attribute is used).</dd></dl>
<p> <code>GLOBUS_CONDOR_ARCH</code></p>
<dl>
<dt>
</dt><dd> The condor name of the architecture which the job manager is handling jobs for.</dd></dl>
<p> <code>GLOBUS_CONDOR_OS</code></p>
<dl>
<dt>
</dt><dd> The condor name of the operating system which the job manager is handling jobs for.</dd></dl>
