---
title: "rsl(5)"
name: "rsl"
section: "5"
letter: "r"
url: "/docs/linux/man/5-rsl/"
description: "rsl – GRAM5 RSL Attributes"
---

<p>rsl &#8211; GRAM5 RSL Attributes</p>
<h2>Description</h2>
<p><code>arguments</code></p>
<dl>
<dd>The command line arguments for the executable. Use quotes, if a space is required in a single argument.</dl>
<p> <code>count</code></p>
<dl>
<dd>The number of executions of the executable. [Default: &lt;literal&gt;1&lt;/literal&gt;]</dl>
<p> <code>directory</code></p>
<dl>
<dd>Specifies the path of the directory the jobmanager will use as the default directory for the requested job. [Default: &lt;literal&gt;$(HOME)&lt;/literal&gt;]</dl>
<p> <code>dry_run</code></p>
<dl>
<dd>If dryrun = yes then the jobmanager will not submit the job for execution and will return success. [Default: &lt;literal&gt;no&lt;/literal&gt;]</dl>
<p> <code>environment</code></p>
<dl>
<dd>The environment variables that will be defined for the executable in addition to default set that is given to the job by the jobmanager.</dl>
<p> <code>executable</code></p>
<dl>
<dd>The name of the executable file to run on the remote machine. If the value is a GASS URL, the file is transferred to the remote gass cache before executing the job and removed after the job has terminated.</dl>
<p> <code>expiration</code></p>
<dl>
<dd>Time (in seconds) after a a job fails to receive a two-phase commit end signal before it is cleaned up. [Default: &lt;literal&gt;14400&lt;/literal&gt;]</dl>
<p> <code>file_clean_up</code></p>
<dl>
<dd>Specifies a list of files which will be removed after the job is completed.</dl>
<p> <code>file_stage_in</code></p>
<dl>
<dd>Specifies a list of (&quot;remote URL&quot; &quot;local file&quot;) pairs which indicate files to be staged to the nodes which will run the job.</dl>
<p> <code>file_stage_in_shared</code></p>
<dl>
<dd>Specifies a list of (&quot;remote URL&quot; &quot;local file&quot;) pairs which indicate files to be staged into the cache. A symlink from the cache to the &quot;local file&quot; path will be made.</dl>
<p> <code>file_stage_out</code></p>
<dl>
<dd>Specifies a list of (&quot;local file&quot; &quot;remote URL&quot;) pairs which indicate files to be staged from the job to a GASS-compatible file server.</dl>
<p> <code>gass_cache</code></p>
<dl>
<dd>Specifies location to override the GASS cache location.</dl>
<p> <code>gram_my_job</code></p>
<dl>
<dd>Obsolete and ignored. [Default: &lt;literal&gt;collective&lt;/literal&gt;]</dl>
<p> <code>host_count</code></p>
<dl>
<dd>Only applies to clusters of SMP computers, such as newer IBM SP systems. Defines the number of nodes (&quot;pizza boxes&quot;) to distribute the &quot;count&quot; processes across.</dl>
<p> <code>job_type</code></p>
<dl>
<dd>This specifies how the jobmanager should start the job. Possible values are single (even if the count &gt; 1, only start 1 process or thread), multiple (start count processes or threads), mpi (use the appropriate method (e.g. mpirun) to start a program compiled with a vendor-provided MPI library. Program is started with count nodes), and condor (starts condor jobs in the &quot;condor&quot; universe.) [Default: &lt;literal&gt;multiple&lt;/literal&gt;]</dl>
<p> <code>library_path</code></p>
<dl>
<dd>Specifies a list of paths to be appended to the system-specific library path environment variables. [Default: &lt;literal&gt;$(GLOBUS_LOCATION)/lib&lt;/literal&gt;]</dl>
<p> <code>loglevel</code></p>
<dl>
<dd>Override the default log level for this job. The value of this attribute consists of a combination of the strings FATAL, ERROR, WARN, INFO, DEBUG, TRACE joined by the | character</dl>
<p> <code>logpattern</code></p>
<dl>
<dd>Override the default log path pattern for this job. The value of this attribute is a string (potentially containing RSL substitutions) that is evaluated to the path to write the log to. If the resulting string contains the string $(DATE) (or any other RSL substitution), it will be reevaluated at log time.</dl>
<p> <code>max_cpu_time</code></p>
<dl>
<dd>Explicitly set the maximum cputime for a single execution of the executable. The units is in minutes. The value will go through an atoi() conversion in order to get an integer. If the GRAM scheduler cannot set cputime, then an error will be returned.</dl>
<p> <code>max_memory</code></p>
<dl>
<dd>Explicitly set the maximum amount of memory for a single execution of the executable. The units is in Megabytes. The value will go through an atoi() conversion in order to get an integer. If the GRAM scheduler cannot set maxMemory, then an error will be returned.</dl>
<p> <code>max_time</code></p>
<dl>
<dd>The maximum walltime or cputime for a single execution of the executable. Walltime or cputime is selected by the GRAM scheduler being interfaced. The units is in minutes. The value will go through an atoi() conversion in order to get an integer.</dl>
<p> <code>max_wall_time</code></p>
<dl>
<dd>Explicitly set the maximum walltime for a single execution of the executable. The units is in minutes. The value will go through an atoi() conversion in order to get an integer. If the GRAM scheduler cannot set walltime, then an error will be returned.</dl>
<p> <code>min_memory</code></p>
<dl>
<dd>Explicitly set the minimum amount of memory for a single execution of the executable. The units is in Megabytes. The value will go through an atoi() conversion in order to get an integer. If the GRAM scheduler cannot set minMemory, then an error will be returned.</dl>
<p> <code>project</code></p>
<dl>
<dd>Target the job to be allocated to a project account as defined by the scheduler at the defined (remote) resource.</dl>
<p> <code>proxy_timeout</code></p>
<dl>
<dd>Obsolete and ignored. Now a job-manager-wide setting.</dl>
<p> <code>queue</code></p>
<dl>
<dd>Target the job to a queue (class) name as defined by the scheduler at the defined (remote) resource.</dl>
<p> <code>remote_io_url</code></p>
<dl>
<dd>Writes the given value (a URL base string) to a file, and adds the path to that file to the environment through the GLOBUS_REMOTE_IO_URL environment variable. If this is specified as part of a job restart RSL, the job manager will update the file&#8217;s contents. This is intended for jobs that want to access files via GASS, but the URL of the GASS server has changed due to a GASS server restart.</dl>
<p> <code>restart</code></p>
<dl>
<dd>Start a new job manager, but instead of submitting a new job, start managing an existing job. The job manager will search for the job state file created by the original job manager. If it finds the file and successfully reads it, it will become the new manager of the job, sending callbacks on status and streaming stdout/err if appropriate. It will fail if it detects that the old jobmanager is still alive (via a timestamp in the state file). If stdout or stderr was being streamed over the network, new stdout and stderr attributes can be specified in the restart RSL and the jobmanager will stream to the new locations (useful when output is going to a GASS server started by the client that&#8217;s listening on a dynamic port, and the client was restarted). The new job manager will return a new contact string that should be used to communicate with it. If a jobmanager is restarted multiple times, any of the previous contact strings can be given for the restart attribute.</dl>
<p> <code>rsl_substitution</code></p>
<dl>
<dd>Specifies a list of values which can be substituted into other rsl attributes&#8217; values through the $(SUBSTITUTION) mechanism.</dl>
<p> <code>save_state</code></p>
<dl>
<dd>Causes the jobmanager to save it&#8217;s job state information to a persistent file on disk. If the job manager exits or is suspended, the client can later start up a new job manager which can continue monitoring the job.</dl>
<p> <code>savejobdescription</code></p>
<dl>
<dd>Save a copy of the job description to $HOME [Default: &lt;literal&gt;no&lt;/literal&gt;]</dl>
<p> <code>scratch_dir</code></p>
<dl>
<dd>Specifies the location to create a scratch subdirectory in. A SCRATCH_DIRECTORY RSL substitution will be filled with the name of the directory which is created.</dl>
<p> <code>stderr</code></p>
<dl>
<dd>The name of the remote file to store the standard error from the job. If the value is a GASS URL, the standard error from the job is transferred dynamically during the execution of the job. There are two accepted forms of this value. It can consist of a single destination: stderr = URL, or a sequence of destinations: stderr = (DESTINATION) (DESTINATION). In the latter case, the DESTINATION may itself be a URL or a sequence of an x-gass-cache URL followed by a cache tag. [Default: &lt;literal&gt;/dev/null&lt;/literal&gt;]</dl>
<p> <code>stderr_position</code></p>
<dl>
<dd>Specifies where in the file remote standard error streaming should be restarted from. Must be 0.</dl>
<p> <code>stdin</code></p>
<dl>
<dd>The name of the file to be used as standard input for the executable on the remote machine. If the value is a GASS URL, the file is transferred to the remote gass cache before executing the job and removed after the job has terminated. [Default: &lt;literal&gt;/dev/null&lt;/literal&gt;]</dl>
<p> <code>stdout</code></p>
<dl>
<dd>The name of the remote file to store the standard output from the job. If the value is a GASS URL, the standard output from the job is transferred dynamically during the execution of the job. There are two accepted forms of this value. It can consist of a single destination: stdout = URL, or a sequence of destinations: stdout = (DESTINATION) (DESTINATION). In the latter case, the DESTINATION may itself be a URL or a sequence of an x-gass-cache URL followed by a cache tag. [Default: &lt;literal&gt;/dev/null&lt;/literal&gt;]</dl>
<p> <code>stdout_position</code></p>
<dl>
<dd>Specifies where in the file remote output streaming should be restarted from. Must be 0.</dl>
<p> <code>two_phase</code></p>
<dl>
<dd>Use a two-phase commit for job submission and completion. The job manager will respond to the initial job request with a WAITING_FOR_COMMIT error. It will then wait for a signal from the client before doing the actual job submission. The integer supplied is the number of seconds the job manager should wait before timing out. If the job manager times out before receiving the commit signal, or if a client issues a cancel signal, the job manager will clean up the job&#8217;s files and exit, sending a callback with the job status as GLOBUS_GRAM_PROTOCOL_JOB_STATE_FAILED. After the job manager sends a DONE or FAILED callback, it will wait for a commit signal from the client. If it receives one, it cleans up and exits as usual. If it times out and save_state was enabled, it will leave all of the job&#8217;s files in place and exit (assuming the client is down and will attempt a job restart later). The timeoutvalue can be extended via a signal. When one of the following errors occurs, the job manager does not delete the job state file when it exits: GLOBUS_GRAM_PROTOCOL_ERROR_COMMIT_TIMED_OUT, GLOBUS_GRAM_PROTOCOL_ERROR_TTL_EXPIRED, GLOBUS_GRAM_PROTOCOL_ERROR_JM_STOPPED, GLOBUS_GRAM_PROTOCOL_ERROR_USER_PROXY_EXPIRED. In these cases, it can not be restarted, so the job manager will not wait for the commit signal after sending the FAILED callback</dl>
<p> <code>username</code></p>
<dl>
<dd>Verify that the job is running as this user.</dl>
<h2>Author</h2>
<p>Copyright &#169; 1999-2016 University of Chicago</p>
