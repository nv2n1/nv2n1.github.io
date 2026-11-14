---
title: "posix_spawnp(3)"
name: "posix_spawnp"
section: "3"
letter: "p"
url: "/docs/linux/man/3-posix_spawnp/"
description: "posix_spawn, posix_spawnp – spawn a process"
---

<p>posix_spawn, posix_spawnp &#8211; spawn a process</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;spawn.h&gt;

int posix_spawn(pid_t *pid, const char *path,
                const posix_spawn_file_actions_t *file_actions,
                const posix_spawnattr_t *attrp,
                char *const argv[], char *const envp[]);

int posix_spawnp(pid_t *pid, const char *file,
                 const posix_spawn_file_actions_t *file_actions,
                 const posix_spawnattr_t *attrp,
                 char *const argv[], char *const envp[]);</code></pre>
<h2>Description</h2>
<p>The <code>posix_spawn</code>() and <code>posix_spawnp</code>() functions are used to create a new child process that executes a specified file. These functions were specified by POSIX to provide a standardized method of creating new processes on machines that lack the capability to support the <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) system call. These machines are generally small, embedded systems lacking MMU support. </p>
<p> The <code>posix_spawn</code>() and <code>posix_spawnp</code>() functions provide the functionality of a combined <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) and <code><a href="/docs/linux/man/3-exec/">exec</a></code>(3), with some optional housekeeping steps in the child process before the <code><a href="/docs/linux/man/3-exec/">exec</a></code>(3). These functions are not meant to replace the <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) and <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) system calls. In fact, they provide only a subset of the functionality that can be achieved by using the system calls. </p>
<p> The only difference between <code>posix_spawn</code>() and <code>posix_spawnp</code>() is the manner in which they specify the file to be executed by the child process. With <code>posix_spawn</code>(), the executable file is specified as a pathname (which can be absolute or relative). With <code>posix_spawnp</code>(), the executable file is specified as a simple filename; the system searches for this file in the list of directories specified by <code>PATH</code> (in the same way as for <code><a href="/docs/linux/man/3-execvp/">execvp</a></code>(3)). For the remainder of this page, the discussion is phrased in terms of <code>posix_spawn</code>(), with the understanding that <code>posix_spawnp</code>() differs only on the point just described. </p>
<p> The remaining arguments to these two functions are as follows:</p>
<dl>
<dt>*</p>
<dd>The <i>pid</i> argument points to a buffer that is used to return the process ID of the new child process.</p>
<dt>*</p>
<dd>The <i>file_actions</i> argument points to a <i>spawn file actions object</i> that specifies file-related actions to be performed in the child between the <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) and <code><a href="/docs/linux/man/3-exec/">exec</a></code>(3) steps. This object is initialized and populated before the <code>posix_spawn</code>() call using <code><a href="/docs/linux/man/3-posix_spawn_file_actions_init/">posix_spawn_file_actions_init</a></code>(3) and the <code>posix_spawn_file_actions_*</code>() functions.</p>
<dt>*</p>
<dd>The <i>attrp</i> argument points to an <i>attributes objects</i> that specifies various attributes of the created child process. This object is initialized and populated before the <code>posix_spawn</code>() call using <code><a href="/docs/linux/man/3-posix_spawnattr_init/">posix_spawnattr_init</a></code>(3) and the <code>posix_spawnattr_*</code>() functions.</p>
<dt>*</p>
<dd>The <i>argv</i> and <i>envp</i> arguments specify the argument list and environment for the program that is executed in the child process, as for <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2).</dl>
<p> Below, the functions are described in terms of a three-step process: the <code>fork</code>() step, the pre-<code>exec</code>() step (executed in the child), and the <code>exec</code>() step (executed in the child).</p>
<h3>fork() step</h3>
<p>Since glibc 2.24, the <code>posix_spawn</code>() function commences by calling <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) with <code>CLONE_VM</code> and <code>CLONE_VFORK</code> flags. Older implementations use <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), or possibly <code><a href="/docs/linux/man/2-vfork/">vfork</a></code>(2) (see below). </p>
<p> The PID of the new child process is placed in <i>*pid</i>. The <code>posix_spawn</code>() function then returns control to the parent process. </p>
<p> Subsequently, the parent can use one of the system calls described in <code><a href="/docs/linux/man/2-wait/">wait</a></code>(2) to check the status of the child process. If the child fails in any of the housekeeping steps described below, or fails to execute the desired file, it exits with a status of 127. </p>
<p> Before glibc 2.24, the child process is created using <code><a href="/docs/linux/man/2-vfork/">vfork</a></code>(2) instead of <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) when either of the following is true:</p>
<dl>
<dt>*</p>
<dd>the <i>spawn-flags</i> element of the attributes object pointed to by <i>attrp</i> contains the GNU-specific flag <code>POSIX_SPAWN_USEVFORK</code>; or</p>
<dt>*</p>
<dd><i>file_actions</i> is NULL and the <i>spawn-flags</i> element of the attributes object pointed to by <i>attrp</i> does <i>not</i> contain <code>POSIX_SPAWN_SETSIGMASK</code>, <code>POSIX_SPAWN_SETSIGDEF</code>, <code>POSIX_SPAWN_SETSCHEDPARAM</code>, <code>POSIX_SPAWN_SETSCHEDULER</code>, <code>POSIX_SPAWN_SETPGROUP</code>, or <code>POSIX_SPAWN_RESETIDS</code>.</dl>
<p> In other words, <code><a href="/docs/linux/man/2-vfork/">vfork</a></code>(2) is used if the caller requests it, or if there is no cleanup expected in the child before it <code><a href="/docs/linux/man/3-exec/">exec</a></code>(3)s the requested file.</p>
<h3>pre-exec() step: housekeeping</h3>
<p>In between the <code>fork()</code> and the <code>exec()</code> steps, a child process may need to perform a set of housekeeping actions. The <code>posix_spawn</code>() and <code>posix_spawnp</code>() functions support a small, well-defined set of system tasks that the child process can accomplish before it executes the executable file. These operations are controlled by the attributes object pointed to by <i>attrp</i> and the file actions object pointed to by <i>file_actions</i>. In the child, processing is done in the following sequence:</p>
<dl>
<dt>1.</p>
<dd>Process attribute actions: signal mask, signal default handlers, scheduling algorithm and parameters, process group, and effective user and group IDs are changed as specified by the attributes object pointed to by <i>attrp</i>.</p>
<dt>2.</p>
<dd>File actions, as specified in the <i>file_actions</i> argument, are performed in the order that they were specified using calls to the <code>posix_spawn_file_actions_add*</code>() functions.</p>
<dt>3.</p>
<dd>File descriptors with the <code>FD_CLOEXEC</code> flag set are closed.</dl>
<p> All process attributes in the child, other than those affected by attributes specified in the object pointed to by <i>attrp</i> and the file actions in the object pointed to by <i>file_actions</i>, will be affected as though the child was created with <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) and it executed the program with <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). </p>
<p> The process attributes actions are defined by the attributes object pointed to by <i>attrp</i>. The <i>spawn-flags</i> attribute (set using <code><a href="/docs/linux/man/3-posix_spawnattr_setflags/">posix_spawnattr_setflags</a></code>(3)) controls the general actions that occur, and other attributes in the object specify values to be used during those actions. </p>
<p> The effects of the flags that may be specified in <i>spawn-flags</i> are as follows:</p>
<dl>
<dt><code>POSIX_SPAWN_SETSIGMASK</code></p>
<dd>Set the signal mask to the signal set specified in the <i>spawn-sigmask</i> attribute of the object pointed to by <i>attrp</i>. If the <code>POSIX_SPAWN_SETSIGMASK</code> flag is not set, then the child inherits the parent&#8217;s signal mask.</p>
<dt><code>POSIX_SPAWN_SETSIGDEF</code></p>
<dd>Reset the disposition of all signals in the set specified in the <i>spawn-sigdefault</i> attribute of the object pointed to by <i>attrp</i> to the default. For the treatment of the dispositions of signals not specified in the <i>spawn-sigdefault</i> attribute, or the treatment when <code>POSIX_SPAWN_SETSIGDEF</code> is not specified, see <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2).</p>
<dt><code>POSIX_SPAWN_SETSCHEDPARAM</code></p>
<dd>If this flag is set, and the <code>POSIX_SPAWN_SETSCHEDULER</code> flag is not set, then set the scheduling parameters to the parameters specified in the <i>spawn-schedparam</i> attribute of the object pointed to by <i>attrp</i>.</p>
<dt><code>POSIX_SPAWN_SETSCHEDULER</code></p>
<dd>Set the scheduling policy algorithm and parameters of the child, as follows:</p>
<dl>
<dd>
<dl>
<dt>*</p>
<dd>The scheduling policy is set to the value specified in the <i>spawn-schedpolicy</i> attribute of the object pointed to by <i>attrp</i>.</p>
<dt>*</p>
<dd>The scheduling parameters are set to the value specified in the <i>spawn-schedparam</i> attribute of the object pointed to by <i>attrp</i> (but see BUGS).</dl>
<p> If the <code>POSIX_SPAWN_SETSCHEDPARAM</code> and <code>POSIX_SPAWN_SETSCHEDPOLICY</code> flags are not specified, the child inherits the corresponding scheduling attributes from the parent.</dl>
<dt><code>POSIX_SPAWN_RESETIDS</code></p>
<dd>If this flag is set, reset the effective UID and GID to the real UID and GID of the parent process. If this flag is not set, then the child retains the effective UID and GID of the parent. In either case, if the set-user-ID and set-group-ID permission bits are enabled on the executable file, their effect will override the setting of the effective UID and GID (se <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2)).</p>
<dt><code>POSIX_SPAWN_SETPGROUP</code></p>
<dd>Set the process group to the value specified in the <i>spawn-pgroup</i> attribute of the object pointed to by <i>attrp</i>. If the <i>spawn-pgroup</i> attribute has the value 0, the child&#8217;s process group ID is made the same as its process ID. If the <code>POSIX_SPAWN_SETPGROUP</code> flag is not set, the child inherits the parent&#8217;s process group ID.</p>
<dt><code>POSIX_SPAWN_USEVFORK</code></p>
<dd>Since glibc 2.24, this flag has no effect. On older implementations, setting this flag forces the <code>fork()</code> step to use <code><a href="/docs/linux/man/2-vfork/">vfork</a></code>(2) instead of <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2). The <code>_GNU_SOURCE</code> feature test macro must be defined to obtain the definition of this constant.</p>
<dt><code>POSIX_SPAWN_SETSID</code> (since glibc 2.26)</p>
<dd>If this flag is set, the child process shall create a new session and become the session leader. The child process shall also become the process group leader of the new process group in the session (see <code><a href="/docs/linux/man/2-setsid/">setsid</a></code>(2)). The <code>_GNU_SOURCE</code> feature test macro must be defined to obtain the definition of this constant.</dl>
<p> If <i>attrp</i> is NULL, then the default behaviors described above for each flag apply. </p>
<p> The <i>file_actions</i> argument specifies a sequence of file operations that are performed in the child process after the general processing described above, and before it performs the <code><a href="/docs/linux/man/3-exec/">exec</a></code>(3). If <i>file_actions</i> is NULL, then no special action is taken, and standard <code><a href="/docs/linux/man/3-exec/">exec</a></code>(3) semantics apply&#8212;file descriptors open before the exec remain open in the new process, except those for which the <code>FD_CLOEXEC</code> flag has been set. File locks remain in place. </p>
<p> If <i>file_actions</i> is not NULL, then it contains an ordered set of requests to <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/2-close/">close</a></code>(2), and <code><a href="/docs/linux/man/2-dup2/">dup2</a></code>(2) files. These requests are added to the <i>file_actions</i> by <code><a href="/docs/linux/man/3-posix_spawn_file_actions_addopen/">posix_spawn_file_actions_addopen</a></code>(3), <code><a href="/docs/linux/man/3-posix_spawn_file_actions_addclose/">posix_spawn_file_actions_addclose</a></code>(3), and <code><a href="/docs/linux/man/3-posix_spawn_file_actions_adddup2/">posix_spawn_file_actions_adddup2</a></code>(3). The requested operations are performed in the order they were added to <i>file_actions</i>. </p>
<p> If any of the housekeeping actions fails (due to bogus values being passed or other reasons why signal handling, process scheduling, process group ID functions, and file descriptor operations might fail), the child process exits with exit value 127.</p>
<h3>exec() step</h3>
<p>Once the child has successfully forked and performed all requested pre-exec steps, the child runs the requested executable. </p>
<p> The child process takes its environment from the <i>envp</i> argument, which is interpreted as if it had been passed to <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). The arguments to the created process come from the <i>argv</i> argument, which is processed as for <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2).</p>
<h2>Return Value</h2>
<p>Upon successful completion, <code>posix_spawn</code>() and <code>posix_spawnp</code>() place the PID of the child process in <i>pid</i>, and return 0. If there is an error during the <code>fork()</code> step, then no child is created, the contents of <i>*pid</i> are unspecified, and these functions return an error number as described below. </p>
<p> Even when these functions return a success status, the child process may still fail for a plethora of reasons related to its pre-<code>exec</code>() initialization. In addition, the <code><a href="/docs/linux/man/3-exec/">exec</a></code>(3) may fail. In all of these cases, the child process will exit with the exit value of 127.</p>
<h2>Errors</h2>
<p>The <code>posix_spawn</code>() and <code>posix_spawnp</code>() functions fail only in the case where the underlying <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), <code><a href="/docs/linux/man/2-vfork/">vfork</a></code>(2) or <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) call fails; in these cases, these functions return an error number, which will be one of the errors described for <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), <code><a href="/docs/linux/man/2-vfork/">vfork</a></code>(2) or <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2). </p>
<p> In addition, these functions fail if:</p>
<dl>
<dt><code>ENOSYS</code></p>
<dd>Function not supported on this system.</dl>
<h2>Versions</h2>
<p>The <code>posix_spawn</code>() and <code>posix_spawnp</code>() functions are available since glibc 2.2.</p>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008.</p>
<h2>Notes</h2>
<p>The housekeeping activities in the child are controlled by the objects pointed to by <i>attrp</i> (for non-file actions) and <i>file_actions</i> In POSIX parlance, the <i>posix_spawnattr_t</i> and <i>posix_spawn_file_actions_t</i> data types are referred to as objects, and their elements are not specified by name. Portable programs should initialize these objects using only the POSIX-specified functions. (In other words, although these objects may be implemented as structures containing fields, portable programs must avoid dependence on such implementation details.) </p>
<p> According to POSIX, it is unspecified whether fork handlers established with <code><a href="/docs/linux/man/3-pthread_atfork/">pthread_atfork</a></code>(3) are called when <code>posix_spawn</code>() is invoked. Since glibc 2.24, the fork handlers are not executed in any case. On older implementations, fork handlers are called only if the child is created using <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2). </p>
<p> There is no &quot;posix_fspawn&quot; function (i.e., a function that is to <code>posix_spawn</code>() as <code><a href="/docs/linux/man/3-fexecve/">fexecve</a></code>(3) is to <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2)). However, this functionality can be obtained by specifying the <i>path</i> argument as one of the files in the caller&#8217;s <i>/proc/self/fd</i> directory.</p>
<h2>Bugs</h2>
<p>POSIX.1 says that when <code>POSIX_SPAWN_SETSCHEDULER</code> is specified in <i>spawn-flags</i>, then the <code>POSIX_SPAWN_SETSCHEDPARAM</code> (if present) is ignored. However, before glibc 2.14, calls to <code>posix_spawn</code>() failed with an error if <code>POSIX_SPAWN_SETSCHEDULER</code> was specified without also specifying <code>POSIX_SPAWN_SETSCHEDPARAM</code>.</p>
<h2>Examples</h2>
<p>The program below demonstrates the use of various functions in the POSIX spawn API. The program accepts command-line attributes that can be used to create file actions and attributes objects. The remaining command-line arguments are used as the executable name and command-line arguments of the program that is executed in the child. In the first run, the <code><a href="/docs/linux/man/1-date/">date</a></code>(1) command is executed in the child, and the <code>posix_spawn</code>() call employs no file actions or attributes objects. $ <code>./a.out date</code> PID of child: 7634 Tue Feb 1 19:47:50 CEST 2011 Child status: exited, status=0 In the next run, the <i>-c</i> command-line option is used to create a file actions object that closes standard output in the child. Consequently, <code><a href="/docs/linux/man/1-date/">date</a></code>(1) fails when trying to perform output and exits with a status of 1. $ <code>./a.out -c date</code> PID of child: 7636 date: write error: Bad file descriptor Child status: exited, status=1 In the next run, the <i>-s</i> command-line option is used to create an attributes object that specifies that all (blockable) signals in the child should be blocked. Consequently, trying to kill child with the default signal sent by <code><a href="/docs/linux/man/1-kill/">kill</a></code>(1) (i.e., <code>SIGTERM</code>) fails, because that signal is blocked. Therefore, to kill the child, <code>SIGKILL</code> is necessary (<code>SIGKILL</code> can&#8217;t be blocked). $ <code>./a.out -s sleep 60 &amp;</code> [1] 7637 $ PID of child: 7638 $ <code>kill 7638</code> $ <code>kill -KILL 7638</code> $ Child status: killed by signal 9 [1]+ Done ./a.out -s sleep 60 When we try to execute a nonexistent command in the child, the <code><a href="/docs/linux/man/3-exec/">exec</a></code>(3) fails and the child exits with a status of 127. </p>
<pre><code>$ ./a.out xxxxx
PID of child: 10190
Child status: exited, status=127



Program source



#include &lt;spawn.h&gt;
#include &lt;stdint.h&gt;
#include &lt;stdio.h&gt;
#include &lt;unistd.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;string.h&gt;
#include &lt;wait.h&gt;
#include &lt;errno.h&gt;
#define errExit(msg)    do { perror(msg); \
exit(EXIT_FAILURE); } while (0)
#define errExitEN(en, msg) \
do { errno = en; perror(msg); \
    exit(EXIT_FAILURE); } while (0)
char **environ;
int
main(int argc, char *argv[])
{
    pid_t child_pid;
    int s, opt, status;
    sigset_t mask;
    posix_spawnattr_t attr;
    posix_spawnattr_t *attrp;
    posix_spawn_file_actions_t file_actions;
    posix_spawn_file_actions_t *file_actionsp;
    /* Parse command-line options, which can be used to specify an
    attributes object and file actions object for the child. */
    attrp = NULL;
    file_actionsp = NULL;
    while ((opt = getopt(argc, argv, &quot;sc&quot;)) != -1) {
        switch (opt) {
            case 'c':       /* -c: close standard output in child */
            /* Create a file actions object and add a &quot;close&quot;
            action to it */
            s = posix_spawn_file_actions_init(&amp;file_actions);
            if (s != 0)
            errExitEN(s, &quot;posix_spawn_file_actions_init&quot;);
            s = posix_spawn_file_actions_addclose(&amp;file_actions,
            STDOUT_FILENO);
            if (s != 0)
            errExitEN(s, &quot;posix_spawn_file_actions_addclose&quot;);
            file_actionsp = &amp;file_actions;
            break;
            case 's':       /* -s: block all signals in child */
            /* Create an attributes object and add a &quot;set signal mask&quot;
            action to it */
            s = posix_spawnattr_init(&amp;attr);
            if (s != 0)
            errExitEN(s, &quot;posix_spawnattr_init&quot;);
            s = posix_spawnattr_setflags(&amp;attr, POSIX_SPAWN_SETSIGMASK);
            if (s != 0)
            errExitEN(s, &quot;posix_spawnattr_setflags&quot;);
            sigfillset(&amp;mask);
            s = posix_spawnattr_setsigmask(&amp;attr, &amp;mask);
            if (s != 0)
            errExitEN(s, &quot;posix_spawnattr_setsigmask&quot;);
            attrp = &amp;attr;
            break;
        }
    }
    /* Spawn the child. The name of the program to execute and the
    command-line arguments are taken from the command-line arguments
    of this program. The environment of the program execed in the
    child is made the same as the parent's environment. */
    s = posix_spawnp(&amp;child_pid, argv[optind], file_actionsp, attrp,
    &amp;argv[optind], environ);
    if (s != 0)
    errExitEN(s, &quot;posix_spawn&quot;);
    /* Destroy any objects that we created earlier */
    if (attrp != NULL) {
        s = posix_spawnattr_destroy(attrp);
        if (s != 0)
        errExitEN(s, &quot;posix_spawnattr_destroy&quot;);
    }
    if (file_actionsp != NULL) {
        s = posix_spawn_file_actions_destroy(file_actionsp);
        if (s != 0)
        errExitEN(s, &quot;posix_spawn_file_actions_destroy&quot;);
    }
    printf(&quot;PID of child: %jd
&quot;, (intmax_t) child_pid);
    /* Monitor status of the child until it terminates */
    do {
        s = waitpid(child_pid, &amp;status, WUNTRACED | WCONTINUED);
        if (s == -1)
        errExit(&quot;waitpid&quot;);
        printf(&quot;Child status: &quot;);
        if (WIFEXITED(status)) {
            printf(&quot;exited, status=%d
&quot;, WEXITSTATUS(status));
        } else if (WIFSIGNALED(status)) {
            printf(&quot;killed by signal %d
&quot;, WTERMSIG(status));
        } else if (WIFSTOPPED(status)) {
            printf(&quot;stopped by signal %d
&quot;, WSTOPSIG(status));
        } else if (WIFCONTINUED(status)) {
            printf(&quot;continued
&quot;);
        }
    } while (!WIFEXITED(status) &amp;&amp; !WIFSIGNALED(status));
    exit(EXIT_SUCCESS);
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-close/">close</a></code>(2), <code><a href="/docs/linux/man/2-dup2/">dup2</a></code>(2), <code><a href="/docs/linux/man/2-execl/">execl</a></code>(2), <code><a href="/docs/linux/man/2-execlp/">execlp</a></code>(2), <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/2-sched_setparam/">sched_setparam</a></code>(2), <code><a href="/docs/linux/man/2-sched_setscheduler/">sched_setscheduler</a></code>(2), <code><a href="/docs/linux/man/2-setpgid/">setpgid</a></code>(2), <code><a href="/docs/linux/man/2-setuid/">setuid</a></code>(2), <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2), <code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2), <code><a href="/docs/linux/man/3-posix_spawn_file_actions_addclose/">posix_spawn_file_actions_addclose</a></code>(3), <code><a href="/docs/linux/man/3-posix_spawn_file_actions_adddup2/">posix_spawn_file_actions_adddup2</a></code>(3), <code><a href="/docs/linux/man/3-posix_spawn_file_actions_addopen/">posix_spawn_file_actions_addopen</a></code>(3), <code><a href="/docs/linux/man/3-posix_spawn_file_actions_destroy/">posix_spawn_file_actions_destroy</a></code>(3), <code><a href="/docs/linux/man/3-posix_spawn_file_actions_init/">posix_spawn_file_actions_init</a></code>(3), <code><a href="/docs/linux/man/3-posix_spawnattr_destroy/">posix_spawnattr_destroy</a></code>(3), <code><a href="/docs/linux/man/3-posix_spawnattr_getflags/">posix_spawnattr_getflags</a></code>(3), <code><a href="/docs/linux/man/3-posix_spawnattr_getpgroup/">posix_spawnattr_getpgroup</a></code>(3), <code><a href="/docs/linux/man/3-posix_spawnattr_getschedparam/">posix_spawnattr_getschedparam</a></code>(3), <code><a href="/docs/linux/man/3-posix_spawnattr_getschedpolicy/">posix_spawnattr_getschedpolicy</a></code>(3), <code><a href="/docs/linux/man/3-posix_spawnattr_getsigdefault/">posix_spawnattr_getsigdefault</a></code>(3), <code><a href="/docs/linux/man/3-posix_spawnattr_getsigmask/">posix_spawnattr_getsigmask</a></code>(3), <code><a href="/docs/linux/man/3-posix_spawnattr_init/">posix_spawnattr_init</a></code>(3), <code><a href="/docs/linux/man/3-posix_spawnattr_setflags/">posix_spawnattr_setflags</a></code>(3), <code><a href="/docs/linux/man/3-posix_spawnattr_setpgroup/">posix_spawnattr_setpgroup</a></code>(3), <code><a href="/docs/linux/man/3-posix_spawnattr_setschedparam/">posix_spawnattr_setschedparam</a></code>(3), <code><a href="/docs/linux/man/3-posix_spawnattr_setschedpolicy/">posix_spawnattr_setschedpolicy</a></code>(3), <code><a href="/docs/linux/man/3-posix_spawnattr_setsigdefault/">posix_spawnattr_setsigdefault</a></code>(3), <code><a href="/docs/linux/man/3-posix_spawnattr_setsigmask/">posix_spawnattr_setsigmask</a></code>(3), <code><a href="/docs/linux/man/3-pthread_atfork/">pthread_atfork</a></code>(3), <i>&lt;spawn.h&gt;</i>, Base Definitions volume of POSIX.1-2001, <i><a rel="nofollow" href="http://www.opengroup.org/unix/online.html">http://www.opengroup.org/unix/online.html</a></i></p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
