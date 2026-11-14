---
title: "globusrun(1)"
name: "globusrun"
section: "1"
letter: "g"
url: "/docs/linux/man/1-globusrun/"
description: "globusrun – Execute and manage jobs via GRAM"
---

<h2 class="name">NAME</h2>
<p> globusrun &#8211; Execute and manage jobs via GRAM </p>
<h2>SYNOPSIS</h2>
<p> <code>globusrun</code> [-help | -usage | -version -versions ] </p>
<p> <code>globusrun</code> [-p | -parse] { -f <i>FILENAME</i> | -file <i>FILENAME</i> | <i>RSL</i> } </p>
<p> <code>globusrun</code> [OPTIONS] {-r <i>RESOURCE</i>| -resource <i>RESOURCE</i>} { -a | -authenticate-only } </p>
<p> <code>globusrun</code> [OPTIONS] {-r <i>RESOURCE</i>| -resource <i>RESOURCE</i>} { -j | -jobmanager-version } </p>
<p> <code>globusrun</code> [OPTIONS] {-k | -kill } <i>JOBID</i> </p>
<p> <code>globusrun</code> [OPTIONS] [ -full-proxy | -D ] { -y | -refresh-proxy } <i>JOBID</i> </p>
<p> <code>globusrun</code> [OPTIONS] -status <i>JOBID</i> </p>
<p> <code>globusrun</code> [OPTIONS] { -r <i>RESOURCE</i> | -resource <i>RESOURCE</i> } { -f <i>FILENAME</i> | -file <i>FILENAME</i> | <i>RSL</i>}</p>
<h2>DESCRIPTION</h2>
<p> The <code>globusrun</code> program for submits and manages jobs run on a local or remote job host. The jobs are controlled by the <code>globus-job-manager</code> program which interfaces with a local resource manager that schedules and executes the job. </p>
<p> The <code>globusrun</code> program can be run in a number of different modes chosen by command-line options. </p>
<p> When <i>-help</i>, <i>-usage</i>, <i>-version</i>, or <i>-versions</i> command-line options are used, <code>globusrun</code> will print out diagnostic information and then exit. </p>
<p> When the <i>-p</i> or <i>-parse</i> command-line option is present, <code>globusrun</code> will verify the syntax of the RSL specification and then terminate. If the syntax is valid, <code>globusrun</code> will print out the string RSL Parsed Successfully&#8230; and exit with a zero exit code; otherwise, it will print an error message and terminate with a non-zero exit code. </p>
<p> When the <i>-a</i> or <i>-authenticate-only</i> command-line option is present, <code>globusrun</code> will verify that the service named by <i>RESOURCE</i> exists and the client&#8217;s credentials are granted permission to access that service. If authentication is successful, <code>globusrun</code> will display the string GRAM Authentication test successful and exit with a zero exit code; otherwise it will print an explanation of the problem and will with a non-zero exit code. </p>
<p> When the <i>-j</i> or <i>-jobmanager-version</i> command-line option is present, <code>globusrun</code> will attempt to determine the software version that the service named by <i>RESOURCE</i> is running. If successful, it will display both the Toolkit version and the Job Manager package version and exit with a zero exit code; otherwise, it will print an explanation of the problem and exit with a non-zero exit code. </p>
<p> When the <i>-k</i> or <i>-kill</i> command-line option is present, <code>globusrun</code> will attempt to terminate the job named by <i>JOB_ID</i>. If successful, <code>globusrun</code> will exit with zero; otherwise it will display an explanation of the problem and exit with a non-zero exit code. </p>
<p> When the <i>-y</i> or <i>-refresh-proxy</i> command-line option is present, <code>globusrun</code> will attempt to delegate a new X.509 proxy to the job manager which is managing the job named by <i>JOBID</i>. If successful, <code>globusrun</code> will exit with zero; otherwise it will display an explanation of the problem and exit with a non-zero exit code. This behavior can be modified by the <i>-full-proxy</i> or <i>-D</i> command-line options to enable full proxy delegation. The default is limited proxy delegation. </p>
<p> When the <i>-status</i> command-line option is present, <code>globusrun</code> will attempt to determine the current state of the job. If successful, the state will be printed to standard output and <code>globusrun</code> will exit with a zero exit code; otherwise, a description of the error will be displayed and it will exit with a non-zero exit code. </p>
<p> Otherwise, <code>globusrun</code> will submit the job to a GRAM service. By default, <code>globusrun</code> waits until the job has terminated or failed before exiting, displaying information about job state changes and at exit time, the job exit code if it is provided by the GRAM service. </p>
<p> The <code>globusrun</code> program can also function as a <code>GASS</code> file server to allow the <code>globus-job-manager</code> program to stage files to and from the machine on which <code>globusrun</code> is executed to the GRAM service node. This behavior is controlled by the <i>-s</i>, <i>-o</i>, and <i>-w</i> command-line options. </p>
<p> Jobs submitted by <code>globusrun</code> can be monitored interactively or detached. To have <code>globusrun</code> detach from the GRAM service after submitting the job, use the <i>-b</i> or <i>-F</i> command-line options.</p>
<h2>OPTIONS</h2>
<p> <code>-help</code></p>
<dl>
<dt>
<dd> Display a help message to standard error and exit.</dl>
<p> <code>-usage</code></p>
<dl>
<dt>
<dd> Display a one-line usage summary to standard error and exit.</dl>
<p> <code>-version</code></p>
<dl>
<dt>
<dd> Display the software version of <code>globusrun</code> to standard error and exit.</dl>
<p> <code>-versions</code></p>
<dl>
<dt>
<dd> Display the software version of all modules used by <code>globusrun</code> (including DiRT information) to standard error and then exit.</dl>
<p> <code>-p, -parse</code></p>
<dl>
<dt>
<dd> Do a parse check on the job specification and print diagnostics. If a parse error occurs, <code>globusrun</code> exits with a non-zero exit code.</dl>
<p> <code>-f FILENAME, -file FILENAME</code></p>
<dl>
<dt>
<dd> Read job specification from the file named by <i>FILENAME</i></dl>
<p> <code>-n, -no-interrupt</code></p>
<dl>
<dt>
<dd> Disable handling of the SIGINT signal, so that the interrupt character (typically Control-C causes <code>globusrun</code> to terminate without canceling the job.</dl>
<p> <code>-r RESOURCE</code></p>
<dl>
<dt>
<dd> Submit the request to the resource specified by <i>RESOURCE</i>. A resource may be specified in the following ways: </p>
<dl>
<dt>
<dd> &bull; <i>HOST</i></dl>
<dl>
<dt>
<dd> &bull; <i>HOST</i>:<i>PORT</i></dl>
<dl>
<dt>
<dd> &bull; <i>HOST</i>:<i>PORT</i>/<i>SERVICE</i></dl>
<dl>
<dt>
<dd> &bull; <i>HOST</i>/<i>SERVICE</i></dl>
<dl>
<dt>
<dd> &bull; <i>HOST</i>:/<i>SERVICE</i></dl>
<dl>
<dt>
<dd> &bull; <i>HOST</i>::<i>SUBJECT</i></dl>
<dl>
<dt>
<dd> &bull; <i>HOST</i>:<i>PORT</i>:<i>SUBJECT</i></dl>
<dl>
<dt>
<dd> &bull; <i>HOST</i>/<i>SERVICE</i>:<i>SUBJECT</i></dl>
<dl>
<dt>
<dd> &bull; <i>HOST</i>:/<i>SERVICE</i>:<i>SUBJECT</i></dl>
<dl>
<dt>
<dd> &bull; <i>HOST</i>:<i>PORT</i>/<i>SERVICE</i>:<i>SUBJECT</i> If any of <i>PORT</i>, <i>SERVICE</i>, or <i>SUBJECT</i> is omitted, the defaults of 2811, jobmanager, and host@<i>HOST</i> are used respectively.</dl>
</dl>
<p> <code>-j, -jobmanager-version</code></p>
<dl>
<dt>
<dd> Print the software version being run by the service running at <i>RESOURCE</i>.</dl>
<p> <code>-k </code><i>JOBID</i><code>, -kill </code><i>JOBID</i></p>
<dl>
<dt>
<dd> Kill the job named by <i>JOBID</i>.</dl>
<p> <code>-D, -full-proxy</code></p>
<dl>
<dt>
<dd> Delegate a full impersonation proxy to the service. By default, a limited proxy is delegated when needed.</dl>
<p> <code>-y, -refresh-proxy</code>: Delegate a new proxy to the service processing JOBID. </p>
<p> <code>-status</code></p>
<dl>
<dt>
<dd> Display the current status of the job named by JOBID.</dl>
<p> <code>-q, -quiet</code></p>
<dl>
<dt>
<dd> Do not display job state change or exit code information.</dl>
<p> <code>-o, -output-enable</code></p>
<dl>
<dt>
<dd> Start a GASS server within the <code>globusrun</code> application that allows access to its standard output and standard error streams only. Also, augment the <i>RSL</i> with a definition of the GLOBUSRUN_GASS_URL RSL substitution and add stdout and stderr clauses which redirect the output and error streams of the job to the output and error streams of the interactive <code>globusrun</code> command. If this is specified, then <code>globusrun</code> acts as though the <i>-q</i> were also specified.</dl>
<p> <code>-s, -server</code></p>
<dl>
<dt>
<dd> Start a GASS server within the <code>globusrun</code> application that allows access to its standard output and standard error streams for writing and any file local the the <code>globusrun</code> invocation for reading. Also, augment the <i>RSL</i> with a definition of the GLOBUSRUN_GASS_URL RSL substitution and add stdout and stderr clauses which redirect the output and error streams of the job to the output and error streams of the interactive <code>globusrun</code> command. If this is specified, then <code>globusrun</code> acts as though the <i>-q</i> were also specified.</dl>
<p> <code>-w, -write-allow</code></p>
<dl>
<dt>
<dd> Start a GASS server within the <code>globusrun</code> application that allows access to its standard output and standard error streams for writing and any file local the the <code>globusrun</code> invocation for reading or writing. Also, augment the <i>RSL</i> with a definition of the GLOBUSRUN_GASS_URL RSL substitution and add stdout and stderr clauses which redirect the output and error streams of the job to the output and error streams of the interactive <code>globusrun</code> command. If this is specified, then <code>globusrun</code> acts as though the <i>-q</i> were also specified.</dl>
<p> <code>-b, -batch</code></p>
<dl>
<dt>
<dd> Terminate after submitting the job to the GRAM service. The GASS-related options can be used to stage input files, but standard output, standard error, and file staging after the job completes will not be processed. The <code>globusrun</code> program will exit after the job hits any of the following states: </p>
<dl>
<dt>
<dd> &bull; PENDING</dl>
<dl>
<dt>
<dd> &bull; ACTIVE</dl>
<dl>
<dt>
<dd> &bull; FAILED</dl>
<dl>
<dt>
<dd> &bull; DONE</dl>
</dl>
<p> <code>-F, -fast-batch</code></p>
<dl>
<dt>
<dd> Terminate after submitting the job to the GRAM service. The <code>globusrun</code> program will exit after it receives a reply from the service. The <i>JOBID</i> will be displayed to standard output before terminating so that the job can be checked with the <i>-status</i> command-line option or modified by the <i>-refresh-proxy</i> or <i>-kill</i> command-line options.</dl>
<p> <code>-d, -dryrun</code></p>
<dl>
<dt>
<dd> Submit the job with the dryrun attribute set to true. When this is done, the job manager will prepare to start the job but start short of submitting it to the service. This can be used to detect problems with the <i>RSL</i>.</dl>
<h2>ENVIRONMENT</h2>
<p> The following variables affect the execution of <code>globusrun</code> </p>
<p> <code>X509_USER_PROXY</code></p>
<dl>
<dt>
<dd> Path to proxy credential.</dl>
<p> <code>X509_CERT_DIR</code></p>
<dl>
<dt>
<dd> Path to trusted certificate directory.</dl>
<h2>BUGS</h2>
<p> The <code>globusrun</code> program assumes any failure to contact the job means the job has terminated. In fact, this may be due to the <code>globus-job-manager</code> program exiting after all jobs it is managing have reached the DONE or FAILED states. In order to reliably detect job termination, the two_phase RSL attribute should be used.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-globus-job-submit/">globus-job-submit</a></code>(1), <code><a href="/docs/linux/man/1-globus-job-run/">globus-job-run</a></code>(1), <code><a href="/docs/linux/man/1-globus-job-clean/">globus-job-clean</a></code>(1), <code><a href="/docs/linux/man/1-globus-job-get-output/">globus-job-get-output</a></code>(1), <code><a href="/docs/linux/man/1-globus-job-cancel/">globus-job-cancel</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> Copyright &#169; 1999-2014 University of Chicago </p>
<h2>Index</h2>
