---
title: "beakerlib-synchronisation(1)"
name: "beakerlib-synchronisation"
section: "1"
letter: "b"
url: "/docs/linux/man/1-beakerlib-synchronisation/"
---

<h2 class="name">NAME</h2>
 

 BeakerLib - synchronisation - Process synchronisation routines 

<h2>DESCRIPTION</h2>

 This is a library of helpers for process synchronisation of applications. 

 <font SIZE="-1">NOTE:</font> none of this commands will cause the test proper to fail, even in case of critical errors during their invocation. If you want your test to fail if those test fail, use their return codes and <i>rlFail()</i>.

<h2>FUNCTIONS</h2>

<h3>Process Synchronisation</h3>

 <i>rlWaitForCmd</i> 

 Pauses script execution until command exit status is the expeced value. Logs a <font SIZE="-1">WARNING</font> and returns 1 if the command didn't exit successfully before timeout elapsed or a maximum number of invocations has been reached. 

 <pre><code>
rlWaitForCmd command[-p PID][-t time][-m count][-d delay][-r retval]
</code></pre>
<dl>
<dt>command
</dt><dd> Command that will be executed until its return code is equal 0 or value speciefied as option to `-r'.
</dd><dt>-t time
</dt><dd> Timeout in seconds, default=120. If the command doesn't return 0 before time elapses, the command will be killed.
</dd><dt>-p <font SIZE="-1">PID</font>
</dt><dd> <font SIZE="-1">PID</font> of the process to check before running command. If the process exits before the socket is opened, the command will log a <font SIZE="-1">WARNING.</font>
</dd><dt>-m count
</dt><dd> Maximum number of `command' executions before continuing anyway. Default is infite. Returns 1 if the maximum was reached.
</dd><dt>-d delay
</dt><dd> Delay between `command' invocations. Default 1.
</dd><dt>-r retval
</dt><dd> Expected return value of command. Default 0.</dd></dl>
 

 <i>rlWaitForFile</i> 

 Pauses script execution until specified file or directory starts existing. Returns 0 if file started existing, 1 if timeout was reached or <font SIZE="-1">PID</font> exited. Return code is greater than 1 in case of error. 

 
rlWaitForFile path[-p PID][-t time][-d delay]

<dl>
<dt>path
</dt><dd> Path to file that should start existing.
</dd><dt>-t time
</dt><dd> Timeout in seconds (optional, default=120). If the file isn't opened before the time elapses the command returns 1.
</dd><dt>-p <font SIZE="-1">PID</font>
</dt><dd> <font SIZE="-1">PID</font> of the process that should also be running. If the process exits before the file is created, the command returns with status code of 1.
</dd><dt>-d delay
</dt><dd> Delay between subsequent checks for existence of file. Default 1.</dd></dl>
 

 <i>rlWaitForSocket</i> 

 Pauses script execution until socket starts listening. Returns 0 if socket started listening, 1 if timeout was reached or <font SIZE="-1">PID</font> exited. Return code is greater than 1 in case of error. 

 
rlWaitForSocket{port | path}[-p PID][-t time][-d delay][--close]

<dl>
<dt>port|path
</dt><dd> Network port to wait for opening or a path to <font SIZE="-1">UNIX</font> socket. Regular expressions are also supported.
</dd><dt>-t time
</dt><dd> Timeout in seconds (optional, default=120). If the socket isn't opened before the time elapses the command returns 1.
</dd><dt>-p <font SIZE="-1">PID</font>
</dt><dd> <font SIZE="-1">PID</font> of the process that should also be running. If the process exits before the socket is opened, the command returns with status code of 1.
</dd><dt>-d delay
</dt><dd> Delay between subsequent checks for availability of socket. Default 1.
</dd><dt>--close
</dt><dd> Wait for the socket to stop listening.</dd></dl>
 

 <i>rlWait</i> 

 Wrapper around bash builtin `wait' command. See <i>bash_builtins</i>(1) man page. Kills the process and all its children if the timeout elapses. 

 <pre><code>
rlWaitFor[n...][-s SIGNAL][-t time]
</code></pre>
<dl>
<dt>n
</dt><dd> List of PIDs to wait for. They need to be background tasks of current shell. See <i>bash_builtins</i>(1) section for `wait' command/
</dd><dt>-t time
</dt><dd> Timeout in seconds (optional, default=30). If the wait isn't successful before the time elapses then all specified tasks are killed.
</dd><dt>-s <font SIZE="-1">SIGNAL</font>
</dt><dd> Signal used to kill the process, optional <font SIZE="-1">SIGTERM</font> by default.</dd></dl>

<h2>AUTHORS</h2>

<dl>
<dt>&bull;
</dt><dd> Hubert Kario &lt;hkario [at] redhat.com&gt; 
</dd></dl>

<h2>Index</h2>


