---
title: "pmrecordaddhost(3)"
name: "pmrecordaddhost"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmrecordaddhost/"
description: "pmafm, pmRecordSetup, pmRecordAddHost, pmRecordControl – record mode support for PMAPI clients"
---

<p><code>pmafm</code>, <code>pmRecordSetup</code>, <code>pmRecordAddHost</code>, <code>pmRecordControl</code> &#8211; record mode support for PMAPI clients</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmafm.h&gt; </p>
<p> FILE *pmRecordSetup(const char *</code><i>folio</i>, const char *<i>creator</i>, int&nbsp;<wbr><i>replay</i>); </p>
<p> int pmRecordAddHost(const char *<i>host</i>, int <i>isdefault</i>, pmRecordHost&nbsp;<wbr>**<i>rhp</i>); </p>
<p> int pmRecordControl(pmRecordHost *<i>rhp</i>, int <i>request</i>, const char&nbsp;<wbr>*<i>options</i>); </p>
<p> cc &#8230; -lpcp_gui</p>
<h2>Description</h2>
<p>These routines may be used to create a Performance Co-Pilot (PCP) archive &#8220;on the fly&#8221; to support &#8220;record mode&#8221; services for PMAPI client applications. </p>
<p> Each record mode &#8220;session&#8221; involves one or more PCP archive logs each created using a dedicated <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) process, with an overall Archive Folio format as understood by <code><a href="/docs/linux/man/1-pmafm/">pmafm</a></code>(1), to name and collect all of the archive logs associated with a single recording session. </p>
<p> The <i>pmRecordHost</i> structure is used to maintain state information between the creator of the recording session and the associated <code>pmlogger</code> process(es). The structure is defined as: </p>
<pre>typedef struct {
 FILE *f_config; /* caller writes pmlogger configuration here */
 int fd_ipc; /* IPC channel to pmlogger */
 char *logfile; /* full pathname for pmlogger error logfile */
 pid_t pid; /* process id for pmlogger */
 int status; /* exit status, -1 if unknown */
} pmRecordHost;</pre>
<p>The routines are used in combination to create a recording session as follows.</p>
<dl>
<dt>1.</p>
<dd>Call <code>pmRecordSetup</code> to establish a new recording session. A new Archive Folio will be created using the name <i>folio</i>; if the file or directory <i>folio</i> already exists, or the file <i>folio</i> cannot be created, this is an error. The application that is creating the session is identified by <i>creator</i> (most often this would be the same as the global PMAPI application name, <i>pmProgname</i>). If the application knows how to create its own configuration file to replay the recorded session, then <i>replay</i> should be non-zero.</p>
<dl>
<dd><code>pmRecordSetup</code> returns a <i>stdio</i> stream onto which the application should write the text of the required replay configuration file, if any.</dl>
<dt>2.</p>
<dd>For each <i>host</i> that is to be included in the recording session, call <code>pmRecordAddHost</code>. A new <i>pmRecordHost</i> structure is returned via <i>rhp</i>. It is assumed that <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) is running on <i>host</i> as this is how <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) will retrieve the required performance metrics.</p>
<dl>
<dd>If this <i>host</i> is the default host for this recording session, then <i>isdefault</i> should be non-zero. This will ensure that the corresponding archive appears first in the PCP archive folio, and hence the tools used to replay the archive folio will make the correct determination of the archive associated with the default host. At most one <i>host</i> per recording session may be nominated as the default host. </p>
<p> The calling application should write the desired <code>pmlogger</code> configuration onto the <i>stdio</i> stream returned via the <i>f_config</i> field in the <i>pmRecordHost</i> structure.</dl>
<dt>3.</p>
<dd>Optionally add arguments to the command line that will be used to launch <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) by calling <code>pmRecordControl</code> with a <i>request</i> of <code>PM_REC_SETARG</code>. The argument is passed via <i>options</i> and one call to <code>pmRecordControl</code> is required for each distinct argument.</p>
<dl>
<dd>An argument may be added for a particular <code>pmlogger</code> instance identified by <i>rhp</i>, or if the <i>rhp</i> argument is NULL the argument is added for all <code>pmlogger</code> instances that will be launched in the current recording session. </p>
<p> Independent of any calls to <code>pmRecordControl</code> with a <i>request</i> of <code>PM_REC_SETARG</code>, each <code>pmlogger</code> instance will automatically be launched with the following arguments: <code>-c</code>, <code>-h</code>, <code>-l</code>, <code>-x</code> and the basename for the PCP archive log.</dl>
<dt>4.</p>
<dd>To commence the recording session, call <code>pmRecordControl</code> with a <i>request</i> of <code>PM_REC_ON</code>, and <i>rhp</i> must be NULL. This will launch one <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) process for each host in the recording session, and initialize the <i>fd_ipc</i>, <i>logfile</i>, <i>pid</i> and <i>status</i> fields in the associated <i>pmRecordHost</i> structure(s).</p>
<dt>5.</p>
<dd>To terminate a <code>pmlogger</code> instance identified by <i>rhp</i>, call <code>pmRecordControl</code> with a <i>request</i> of <code>PM_REC_OFF</code>. If the <i>rhp</i> argument to <code>pmRecordControl</code> is NULL, the termination request is broadcast to all <code>pmlogger</code> processes in the current recording session.</p>
<dl>
<dd>An informative dialog is generated directly by each <code>pmlogger</code> process and hence note the comments on the disposition of output from <code>pmlogger</code> below. </p>
<p> Alternatively, <code>pmlogger</code> can be started with options to limit the duration of logging, e.g. the <code>-T</code> or <code>-s</code> arguments, in which case there is no need to call <code>pmRecordControl</code> with a <i>request</i> of <code>PM_REC_OFF</code> and no dialog is generated.</dl>
<dt>6.</p>
<dd>To display the current status of the <code>pmlogger</code> instance identified by <i>rhp</i>, call <code>pmRecordControl</code> with a <i>request</i> of <code>PM_REC_STATUS</code>. If the <i>rhp</i> argument to <code>pmRecordControl</code> is NULL, the status request is broadcast to all <code>pmlogger</code> processes in the current recording session.</p>
<dl>
<dd>The display is generated directly by each <code>pmlogger</code> process and hence note the comments on the disposition of output from <code>pmlogger</code> below.</dl>
<dt>7.</p>
<dd>To detach a <code>pmlogger</code> instance identified by <i>rhp</i> and allow it to continue independent of the application that launched the recording session, call <code>pmRecordControl</code> with a <i>request</i> of <code>PM_REC_DETACH</code>. If the <i>rhp</i> argument to <code>pmRecordControl</code> is NULL, the detach request is broadcast to all <code>pmlogger</code> processes in the current recording session.</p>
<dl>
<dd>An informative dialog is generated directly by each <code>pmlogger</code> process and hence note the comments on the disposition of output from <code>pmlogger</code> below.</dl>
</dl>
<p> The calling application should not close any of the returned <i>stdio</i> streams; this will be done by <code>pmRecordControl</code> when recording is commenced. </p>
<p> Once <code>pmlogger</code> has been started for a recording session, then <code>pmlogger</code> will assume responsibility for any dialog with the user in the event that the application that launched the recording session should exit, particularly without terminating the recording session. </p>
<p> By default, information and dialogs from <code>pmlogger</code> will be displayed using <code><a href="/docs/linux/man/1-pmquery/">pmquery</a></code>(1) on the assumption that most applications wishing to launch a recording session are GUI-based. In the event that <code>pmquery</code> fails to display the information (for example, because the <code>DISPLAY</code> environment variable is not set), <code>pmlogger</code> will write on its own <i>stderr</i> stream (<code>not</code> the <i>stderr</i> stream of the launching process); the output will be assigned to the <i>XXXXXX.host.</i><code>log</code> file described in the FILES section below. For convenience, the full pathname to this file is provided via the <i>logfile</i> field in the <i>pmRecordHost</i> structure. </p>
<p> If the <i>options</i> argument to <code>pmRecordControl</code> is not NULL, this string may be used to pass additional arguments to <code><a href="/docs/linux/man/1-pmquery/">pmquery</a></code>(1) in those cases where a dialog is to be displayed. One use of this capability would be to provide a <code>-geometry</code> string to control the placement of the dialog. </p>
<p> Premature termination of a launched <code>pmlogger</code> process may be determined using the <i>pmRecordHost</i> structure, by calling <code><a href="/docs/linux/man/2-select/">select</a></code>(2) on the <i>fd_ipc</i> field or polling the <i>status</i> field that will contain the termination status from <code><a href="/docs/linux/man/2-waitpid/">waitpid</a></code>(2) if known, else -1.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-pmafm/">pmafm</a></code>(1), <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1), <code><a href="/docs/linux/man/1-pmquery/">pmquery</a></code>(1) and <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3).</p>
<h2>Files</h2>
<p>These routines create a number of files in the <code>same directory</code> as the <i>folio</i> file named in the call to <code>pmRecordSetup</code>. In all cases, the &#8220;XXXXXX&#8221; component is the result of calling <code><a href="/docs/linux/man/3-mktemp/">mktemp</a></code>(3).</p>
<dl>
<dt><i>XXXXXX</i></p>
<dd>If <i>replay</i> is non-zero, this is the creator&#8217;s replay configuration file, else an empty control file, used to guarantee uniqueness.</p>
<dt><i>folio</i></p>
<dd>The PCP Archive Folio, suitable for use with <code><a href="/docs/linux/man/1-pmafm/">pmafm</a></code>(1).</p>
<dt><i>XXXXXX.host.</i><code>config</code></p>
<dd>The <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) configuration for each <i>host</i> &#8211; if the same <i>host</i> is used in different calls to <code>pmRecordAddHost</code> within the same recording session then one of the letters &#8220;a&#8221; through &#8220;z&#8221; will be appended to the &#8220;XXXXXX&#8221; part of all associated file names to ensure uniqueness.</p>
<dt><i>XXXXXX.host.</i><code>log</code></p>
<dd><i>stdout</i> and <i>stderr</i> for the <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) instance for each <i>host</i>.</p>
<dt><i>XXXXXX.host.</i>{<code>0</code>,<code>meta</code>,<code>index</code>}</p>
<dd>The files comprising a single PCP archive for each <i>host</i>.</dl>
<h2>Diagnostics</h2>
<p><code>pmRecordSetup</code> may return <code>NULL</code> in the event of an error. Check <i>errno</i> for the real cause, but the value <code>EINVAL</code> typically means that the order of calls to these routines is not correct (there is obvious state associated with the current recording session that is maintained across calls to these routines). For example the following calls would produce this <code>EINVAL</code> error; calling <code>pmRecordControl</code> before calling <code>pmRecordAddHost</code> at least once, or calling <code>pmRecordAddHost</code> before calling <code>pmRecordSetup</code>. </p>
<p> <code>pmRecordControl</code> and <code>pmRecordAddHost</code> both return 0 on success, else a value less than 0 suitable for decoding with <code><a href="/docs/linux/man/3-pmerrstr/">pmErrStr</a></code>(3) on failure. The value <code>-EINVAL</code> has the same interpretation as <i>errno</i> being set to <code>EINVAL</code> as described above. </p>
<p> <code>pmRecordControl</code> will return <code>PM_ERR_IPC</code> if the associated <code>pmlogger</code> process has already exited.</p>
