---
title: "perlfork(1)"
name: "perlfork"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlfork/"
description: "perlfork – Perl’s fork() emulation"
---

<h2 class="name">NAME</h2>
<p> perlfork &#8211; Perl&#8217;s fork() emulation </p>
<h2>SYNOPSIS</h2>
<pre>
    NOTE:  As of the 5.8.0 release, fork() emulation has considerably
    matured.  However, there are still a few known bugs and differences
    from real fork() that might affect you.  See the &quot;BUGS&quot; and
    &quot;CAVEATS AND LIMITATIONS&quot; sections below.
</pre>
<p> Perl provides a <code>fork()</code> keyword that corresponds to the Unix system call of the same name. On most Unix-like platforms where the <code>fork()</code> system call is available, Perl&#8217;s <code>fork()</code> simply calls it. </p>
<p> On some platforms such as Windows where the <code>fork()</code> system call is not available, Perl can be built to emulate <code>fork()</code> at the interpreter level. While the emulation is designed to be as compatible as possible with the real <code>fork()</code> at the level of the Perl program, there are certain important differences that stem from the fact that all the pseudo child &#8220;processes&#8221; created this way live in the same real process as far as the operating system is concerned. </p>
<p> This document provides a general overview of the capabilities and limitations of the <code>fork()</code> emulation. Note that the issues discussed here are not applicable to platforms where a real <code>fork()</code> is available and Perl has been configured to use it.</p>
<h2>DESCRIPTION</h2>
<p> The <code>fork()</code> emulation is implemented at the level of the Perl interpreter. What this means in general is that running <code>fork()</code> will actually clone the running interpreter and all its state, and run the cloned interpreter in a separate thread, beginning execution in the new thread just after the point where the <code>fork()</code> was called in the parent. We will refer to the thread that implements this child &#8220;process&#8221; as the pseudo-process. </p>
<p> To the Perl program that called <code>fork()</code>, all this is designed to be transparent. The parent returns from the <code>fork()</code> with a pseudo-process <font SIZE="-1">ID</font> that can be subsequently used in any process-manipulation functions; the child returns from the <code>fork()</code> with a value of <tt>0</tt> to signify that it is the child pseudo-process.</p>
<h3>Behavior of other Perl features in forked pseudo-processes</h3>
<p> Most Perl features behave in a natural way within pseudo-processes.</p>
<dl>
<dt>$$ or $PROCESS_ID</p>
<dd> This special variable is correctly set to the pseudo-process <font SIZE="-1">ID.</font> It can be used to identify pseudo-processes within a particular session. Note that this value is subject to recycling if any pseudo-processes are launched after others have been <code>wait()</code>-ed on.</p>
<dt>%ENV</p>
<dd> Each pseudo-process maintains its own virtual environment. Modifications to <tt>%ENV</tt> affect the virtual environment, and are only visible within that pseudo-process, and in any processes (or pseudo-processes) launched from it.</p>
<dt><code>chdir()</code> and all other builtins that accept filenames</p>
<dd> Each pseudo-process maintains its own virtual idea of the current directory. Modifications to the current directory using <code>chdir()</code> are only visible within that pseudo-process, and in any processes (or pseudo-processes) launched from it. All file and directory accesses from the pseudo-process will correctly map the virtual working directory to the real working directory appropriately.</p>
<dt><code>wait()</code> and <code>waitpid()</code></p>
<dd> <code>wait()</code> and <code>waitpid()</code> can be passed a pseudo-process <font SIZE="-1">ID</font> returned by <code>fork()</code>. These calls will properly wait for the termination of the pseudo-process and return its status.</p>
<dt><code>kill()</code></p>
<dd> <tt>&quot;kill('KILL', ...)&quot;</tt> can be used to terminate a pseudo-process by passing it the <font SIZE="-1">ID</font> returned by <code>fork()</code>. The outcome of kill on a pseudo-process is unpredictable and it should not be used except under dire circumstances, because the operating system may not guarantee integrity of the process resources when a running thread is terminated. The process which implements the pseudo-processes can be blocked and the Perl interpreter hangs. Note that using <tt>&quot;kill('KILL', ...)&quot;</tt> on a pseudo-<code>process()</code> may typically cause memory leaks, because the thread that implements the pseudo-process does not get a chance to clean up its resources. </p>
<p> <tt>&quot;kill('TERM', ...)&quot;</tt> can also be used on pseudo-processes, but the signal will not be delivered while the pseudo-process is blocked by a system call, e.g. waiting for a socket to connect, or trying to read from a socket with no data available. Starting in Perl 5.14 the parent process will not wait for children to exit once they have been signalled with <tt>&quot;kill('TERM', ...)&quot;</tt> to avoid deadlock during process exit. You will have to explicitly call <code>waitpid()</code> to make sure the child has time to clean-up itself, but you are then also responsible that the child is not blocking on I/O either.</p>
<dt><code>exec()</code></p>
<dd> Calling <code>exec()</code> within a pseudo-process actually spawns the requested executable in a separate process and waits for it to complete before exiting with the same exit status as that process. This means that the process <font SIZE="-1">ID</font> reported within the running executable will be different from what the earlier Perl <code>fork()</code> might have returned. Similarly, any process manipulation functions applied to the <font SIZE="-1">ID</font> returned by <code>fork()</code> will affect the waiting pseudo-process that called <code>exec()</code>, not the real process it is waiting for after the <code>exec()</code>. </p>
<p> When <code>exec()</code> is called inside a pseudo-process then <font SIZE="-1">DESTROY</font> methods and <font SIZE="-1">END</font> blocks will still be called after the external process returns.</p>
<dt><code>exit()</code></p>
<dd> <code>exit()</code> always exits just the executing pseudo-process, after automatically <code>wait()</code>-ing for any outstanding child pseudo-processes. Note that this means that the process as a whole will not exit unless all running pseudo-processes have exited. See below for some limitations with open filehandles.</p>
<dt>Open handles to files, directories and network sockets</p>
<dd> All open handles are <code>dup()</code>-ed in pseudo-processes, so that closing any handles in one process does not affect the others. See below for some limitations.</dl>
<h3>Resource limits</h3>
<p> In the eyes of the operating system, pseudo-processes created via the <code>fork()</code> emulation are simply threads in the same process. This means that any process-level limits imposed by the operating system apply to all pseudo-processes taken together. This includes any limits imposed by the operating system on the number of open file, directory and socket handles, limits on disk space usage, limits on memory size, limits on <font SIZE="-1">CPU</font> utilization etc.</p>
<h3>Killing the parent process</h3>
<p> If the parent process is killed (either using Perl&#8217;s <code>kill()</code> builtin, or using some external means) all the pseudo-processes are killed as well, and the whole process exits.</p>
<h3>Lifetime of the parent process and pseudo-processes</h3>
<p> During the normal course of events, the parent process and every pseudo-process started by it will wait for their respective pseudo-children to complete before they exit. This means that the parent and every pseudo-child created by it that is also a pseudo-parent will only exit after their pseudo-children have exited. </p>
<p> Starting with Perl 5.14 a parent will not <code>wait()</code> automatically for any child that has been signalled with <tt>&quot;kill('TERM', ...)&quot;</tt> to avoid a deadlock in case the child is blocking on I/O and never receives the signal.</p>
<h2>CAVEATS AND LIMITATIONS</h2>
<dl>
<dt><font SIZE="-1">BEGIN</font> blocks</p>
<dd> The <code>fork()</code> emulation will not work entirely correctly when called from within a <font SIZE="-1">BEGIN</font> block. The forked copy will run the contents of the <font SIZE="-1">BEGIN</font> block, but will not continue parsing the source stream after the <font SIZE="-1">BEGIN</font> block. For example, consider the following code: </p>
<pre><code>
BEGIN
{
    fork and exit;
#fork child and exit the parent
        print "inner
";
}
print "outer
";
</code></pre>
<p> This will print: </p>
<pre>
    inner
</pre>
<p> rather than the expected: </p>
<pre>
    inner
    outer
</pre>
<p> This limitation arises from fundamental technical difficulties in cloning and restarting the stacks used by the Perl parser in the middle of a parse.</p>
<dt>Open filehandles</p>
<dd> Any filehandles open at the time of the <code>fork()</code> will be <code>dup()</code>-ed. Thus, the files can be closed independently in the parent and child, but beware that the <code>dup()</code>-ed handles will still share the same seek pointer. Changing the seek position in the parent will change it in the child and vice-versa. One can avoid this by opening files that need distinct seek pointers separately in the child. </p>
<p> On some operating systems, notably Solaris and Unixware, calling <tt>&quot;exit()&quot;</tt> from a child process will flush and close open filehandles in the parent, thereby corrupting the filehandles. On these systems, calling <tt>&quot;_exit()&quot;</tt> is suggested instead. <tt>&quot;_exit()&quot;</tt> is available in Perl through the <tt>&quot;POSIX&quot;</tt> module. Please consult your system&#8217;s manpages for more information on this.</p>
<dt>Open directory handles</p>
<dd> Perl will completely read from all open directory handles until they reach the end of the stream. It will then <code>seekdir()</code> back to the original location and all future <code>readdir()</code> requests will be fulfilled from the cache buffer. That means that neither the directory handle held by the parent process nor the one held by the child process will see any changes made to the directory after the <code>fork()</code> call. </p>
<p> Note that <code>rewinddir()</code> has a similar limitation on Windows and will not force <code>readdir()</code> to read the directory again either. Only a newly opened directory handle will reflect changes to the directory.</p>
<dt>Forking pipe <code>open()</code> not yet implemented</p>
<dd> The <tt>&quot;open(FOO, &quot;|-&quot;)&quot;</tt> and <tt>&quot;open(BAR, &quot;-|&quot;)&quot;</tt> constructs are not yet implemented. This limitation can be easily worked around in new code by creating a pipe explicitly. The following example shows how to write to a forked child: </p>
<p>#simulate open(FOO, &#8220;|-&#8220;)<br />
sub pipe_to_fork($)<br />
{<br />
    my $parent = shift;<br />
    pipe my $child, $parent or die;<br />
    my $pid = fork();<br />
    die &#8220;fork() failed: $!&#8221; unless defined $pid;<br />
    if ($pid) {<br />
        close $child;<br />
    } else {<br />
        close $parent;<br />
        open(STDIN, &#8220;&lt;&amp;=&#8221;.fileno($child)) or die;<br />
    }<br />
    $pid;<br />
}<br />
if (pipe_to_fork(&#8216;FOO&#8217;)) {<br />
#parent<br />
    print FOO &#8220;pipe_to_fork
&#8221;;<br />
    close FOO;<br />
} else {<br />
#child<br />
    while (&lt;STDIN&gt;) {<br />
        print;<br />
    }<br />
    exit(0);<br />
}</p>
<p> And this one reads from the child: </p>
<pre><code>
#simulate open(FOO, "-|")
sub pipe_from_fork($)
{
    my $parent = shift;
    pipe $parent, my $child or die;
    my $pid = fork();
    die "fork() failed: $!" unless defined $pid;
    if ($pid) {
        close $child;
    } else {
        close $parent;
        open(STDOUT, "&gt;&amp;=".fileno($child)) or die;
    }
    $pid;
}
if (pipe_from_fork('BAR')) {
#parent
    while (&lt;BAR&gt;) {
        print;
    }
    close BAR;
} else {
#child
    print "pipe_from_fork
";
    exit(0);
}
</code></pre>
<p> Forking pipe <code>open()</code> constructs will be supported in future.</p>
<dt>Global state maintained by XSUBs</p>
<dd> External subroutines (XSUBs) that maintain their own global state may not work correctly. Such XSUBs will either need to maintain locks to protect simultaneous access to global data from different pseudo-processes, or maintain all their state on the Perl symbol table, which is copied naturally when <code>fork()</code> is called. A callback mechanism that provides extensions an opportunity to clone their state will be provided in the near future.</p>
<dt>Interpreter embedded in larger application</p>
<dd> The <code>fork()</code> emulation may not behave as expected when it is executed in an application which embeds a Perl interpreter and calls Perl APIs that can evaluate bits of Perl code. This stems from the fact that the emulation only has knowledge about the Perl interpreter&#8217;s own data structures and knows nothing about the containing application&#8217;s state. For example, any state carried on the application&#8217;s own call stack is out of reach.</p>
<dt>Thread-safety of extensions</p>
<dd> Since the <code>fork()</code> emulation runs code in multiple threads, extensions calling into non-thread-safe libraries may not work reliably when calling <code>fork()</code>. As Perl&#8217;s threading support gradually becomes more widely adopted even on platforms with a native <code>fork()</code>, such extensions are expected to be fixed for thread-safety.</dl>
<h2>PORTABILITY CAVEATS</h2>
<p> In portable Perl code, <tt>&quot;kill(9, $child)&quot;</tt> must not be used on forked processes. Killing a forked process is unsafe and has unpredictable results. See &#8220;<code>kill()</code>&#8221;, above.</p>
<h2>BUGS</h2>
<dl>
<dt>&bull;</p>
<dd> Having pseudo-process IDs be negative integers breaks down for the integer <tt>&quot;-1&quot;</tt> because the <code>wait()</code> and <code>waitpid()</code> functions treat this number as being special. The tacit assumption in the current implementation is that the system never allocates a thread <font SIZE="-1">ID</font> of <tt>1</tt> for user threads. A better representation for pseudo-process IDs will be implemented in future.</p>
<dt>&bull;</p>
<dd> In certain cases, the OS-level handles created by the <code>pipe()</code>, <code>socket()</code>, and <code>accept()</code> operators are apparently not duplicated accurately in pseudo-processes. This only happens in some situations, but where it does happen, it may result in deadlocks between the read and write ends of pipe handles, or inability to send or receive data across socket handles.</p>
<dt>&bull;</p>
<dd> This document may be incomplete in some respects.</dl>
<h2>AUTHOR</h2>
<p> Support for concurrent interpreters and the <code>fork()</code> emulation was implemented by ActiveState, with funding from Microsoft Corporation. </p>
<p> This document is authored and maintained by Gurusamy Sarathy &lt;gsar [at] activestate.com&gt;.</p>
<h2>SEE ALSO</h2>
<p> &#8220;fork&#8221; in perlfunc, perlipc </p>
<h2>Index</h2>
