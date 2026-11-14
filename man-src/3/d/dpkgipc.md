---
title: "dpkgipc(3)"
name: "dpkgipc"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dpkgipc/"
---

Dpkg::IPC - helper functions for IPC 

<h2>Description</h2>Dpkg::IPC offers helper functions to allow you to execute other programs in an easy, yet flexible way, while hiding all the gory details of <font SIZE="-1">IPC </font>(Inter-Process Communication) from you.
<h2>Methods</h2><dl COMPACT><dt>spawn
<dd>Creates a child process and executes another program in it. The arguments are interpreted as a hash of options, specifying how to handle the in and output of the program to execute. Returns the pid of the child process (unless the wait_child option was given). 

 Any error will cause the function to exit with one of the Dpkg::ErrorHandling functions. 

 Options:
<dl COMPACT><dd><dl COMPACT><dt>exec
<dd>Can be either a scalar, i.e. the name of the program to be executed, or an array reference, i.e. the name of the program plus additional arguments. Note that the program will never be executed via the shell, so you can't specify additional arguments in the scalar string and you can't use any shell facilities like globbing. 

 Mandatory Option.
<dt>from_file, to_file, error_to_file
<dd>Filename as scalar. Standard input/output/error of the child process will be redirected to the file specified.
<dt>from_handle, to_handle, error_to_handle
<dd>Filehandle. Standard input/output/error of the child process will be dup'ed from the handle.
<dt>from_pipe, to_pipe, error_to_pipe
<dd>Scalar reference or object based on IO::Handle. A pipe will be opened for each of the two options and either the reading (<tt>&quot;to_pipe&quot;</tt> and <tt>&quot;error_to_pipe&quot;</tt>) or the writing end (<tt>&quot;from_pipe&quot;</tt>) will be returned in the referenced scalar. Standard input/output/error of the child process will be dup'ed to the other ends of the pipes.
<dt>from_string, to_string, error_to_string
<dd>Scalar reference. Standard input/output/error of the child process will be redirected to the string given as reference. Note that it wouldn't be strictly necessary to use a scalar reference for <tt>&quot;from_string&quot;</tt>, as the string is not modified in any way. This was chosen only for reasons of symmetry with <tt>&quot;to_string&quot;</tt> and <tt>&quot;error_to_string&quot;</tt>. <tt>&quot;to_string&quot;</tt> and <tt>&quot;error_to_string&quot;</tt> imply the <tt>&quot;wait_child&quot;</tt> option.
<dt>wait_child
<dd>Scalar. If containing a true value, <i>wait_child()</i> will be called before returning. The return value of <i>spawn()</i> will be a true value, not the pid.
<dt>nocheck
<dd>Scalar. Option of the <i>wait_child()</i> call.
<dt>timeout
<dd>Scalar. Option of the <i>wait_child()</i> call.
<dt>chdir
<dd>Scalar. The child process will chdir in the indicated directory before calling exec.
<dt>env
<dd>Hash reference. The child process will populate <tt>%ENV</tt> with the items of the hash before calling exec. This allows exporting environment variables.
<dt>delete_env
<dd>Array reference. The child process will remove all environment variables listed in the array before calling exec.
<dt>sig
<dd>Hash reference. The child process will populate <tt>%SIG</tt> with the items of the hash before calling exec. This allows setting signal dispositions.
<dt>delete_sig
<dd>Array reference. The child process will reset all signals listed in the array to their default dispositions before calling exec.</dl></dl><dl COMPACT><dd></dl><dt>wait_child
<dd>Takes as first argument the pid of the process to wait for. Remaining arguments are taken as a hash of options. Returns nothing. Fails if the child has been ended by a signal or if it exited non-zero. 

 Options:
<dl COMPACT><dd><dl COMPACT><dt>cmdline
<dd>String to identify the child process in error messages. Defaults to ``child process''.
<dt>nocheck
<dd>If true do not check the return status of the child (and thus do not fail it it has been killed or if it exited with a non-zero return code).
<dt>timeout
<dd>Set a maximum time to wait for the process, after that fail with an error message.</dl></dl><dl COMPACT><dd></dl></dl><h2>Changes</h2><h3>Version 1.01</h3>New options: <i>spawn()</i> now accepts 'sig' and 'delete_sig'.
<h3>Version 1.00</h3>Mark the module as public.
<h2>Authors</h2>Written by Raphaël Hertzog &lt;hertzog [at] debian.org&gt; and Frank Lichtenheld &lt;djpig [at] debian.org&gt;.
<h2>See Also</h2>Dpkg, Dpkg::ErrorHandling
