---
title: "remctl_output(3)"
name: "remctl_output"
section: "3"
letter: "r"
url: "/docs/linux/man/3-remctl_output/"
---

remctl_output - Retrieve the results of a remctl command

<h2>Synopsis</h2>

<pre><code>#include &lt;remctl.h&gt;
struct remctl_output *remctl_output(struct remctl *r);</code></pre>

<h2>Description</h2>

<i>remctl_output()</i> retrieves the next output token from the remote remctl server. <i>r</i> is a remctl client object created with <i>remctl_new()</i>, which should have previously been used as the argument to <i>remctl_open()</i> and then either <i>remctl_command()</i> or <i>remctl_commandv()</i>. The returned remctl_output struct has the following members: <pre><code>struct remctl_output {
    enum remctl_output_type type;
    char *data;
    size_t length;
    int stream; /* 1 == stdout, 2 == stderr */
    int status; /* Exit status of remote command. */
    int error;  /* Remote error code. */
};</code></pre> where the type field will have one of the following values: <pre> REMCTL_OUT_OUTPUT
 REMCTL_OUT_STATUS
 REMCTL_OUT_ERROR
 REMCTL_OUT_DONE</pre>A command rejected by the remctl server will return a single output token of type <font SIZE="-1">REMCTL_OUT_ERROR. A</font> successful command will return zero or more <font SIZE="-1">REMCTL_OUT_OUTPUT</font> tokens representing the output of the command followed by a <font SIZE="-1">REMCTL_OUT_STATUS</font> token giving the exit status of the command. Therefore, for each command issued, the caller should call <i>remctl_command()</i> or <i>remctl_commandv()</i> and then call <i>remctl_output()</i> repeatedly to retrieve each output token until <i>remctl_output()</i> returns a token of type <font SIZE="-1">REMCTL_OUT_ERROR</font> or <font SIZE="-1">REMCTL_OUT_STATUS.</font> A <font SIZE="-1">REMCTL_OUT_OUTPUT</font> token will have data in the data field, whose length is given by the length field. The output stream will be given by the stream field, with a value of 1 indicating standard output and a value of 2 indicating standard error. All other stream values are reserved for future use. A <font SIZE="-1">REMCTL_OUT_STATUS</font> token will hold the exit status of the remote command in the status field. Following the standard Unix convention, a 0 status should normally be considered success and any non-zero status should normally be considered failure, although a given command may have its own exit status conventions. A <font SIZE="-1">REMCTL_OUT_ERROR</font> token will have the error message from the server in the data field (with length stored in length) and the protocol error code in the error field. The latter is the most reliable indicator of the error; the message stored in the error field is free-form text, may or may not be localized, and should not be used for programmatic comparisons. For the possible error code values and their meanings, see the remctl protocol specification. If <i>remctl_output()</i> is called when there is no pending output from the remote server (after a <font SIZE="-1">REMCTL_OUT_ERROR</font> or <font SIZE="-1">REMCTL_OUT_STATUS</font> token has already been returned, for example), a token of type <font SIZE="-1">REMCTL_OUT_DONE</font> will be returned. <font SIZE="-1">REMCTL_OUT_DONE</font> tokens do not use any of the other fields of the remctl_output struct. The returned remctl_output struct must not be freed by the caller. It will be invalidated on any subsequent call to any other remctl <font SIZE="-1">API</font> function other than <i>remctl_error()</i> on the same remctl client object; the caller should therefore copy out of the remctl_output struct any data it wishes to preserve before making any subsequent remctl <font SIZE="-1">API</font> calls.

<h2>Return Value</h2>

<i>remctl_output()</i> returns a pointer to a remctl_output struct on success and <font SIZE="-1">NULL</font> on failure. On failure, the caller should call <i>remctl_error()</i> to retrieve the error message.

<h2>See Also</h2>

<i><a HREF="/docs/linux/man/3-remctl_new/">remctl_new</a></i>(3), <i><a HREF="/docs/linux/man/3-remctl_open/">remctl_open</a></i>(3), <i><a HREF="/docs/linux/man/3-remctl_command/">remctl_command</a></i>(3), <i><a HREF="/docs/linux/man/3-remctl_commandv/">remctl_commandv</a></i>(3), <i><a HREF="/docs/linux/man/3-remctl_error/">remctl_error</a></i>(3) 

 The current version of the remctl library and complete details of the remctl protocol are available from its web page at &lt;<a rel="nofollow" HREF="http://www.eyrie.org/~eagle/software/remctl/">http://www.eyrie.org/~eagle/software/remctl/</a>&gt;.

<h2>Author</h2>

Russ Allbery &lt;eagle [at] eyrie.org&gt;

<h2>Copyright And License</h2>

Copyright 2007, 2009 The Board of Trustees of the Leland Stanford Junior University 

 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved. This file is offered as-is, without any warranty.
