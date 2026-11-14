---
title: "dlm_dispatch(3)"
name: "dlm_dispatch"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlm_dispatch/"
description: "libdlm – dlm_get_fd, dlm_dispatch, dlm_pthread_init, dlm_ls_pthread_init, dlm_cleanup"
---

<h2>NAME</h2>
<p> libdlm &#8211; dlm_get_fd, dlm_dispatch, dlm_pthread_init, dlm_ls_pthread_init, dlm_cleanup</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;libdlm.h&gt;
int dlm_pthread_init();
int dlm_ls_pthread_init(dlm_lshandle_t lockspace);
int dlm_pthread_cleanup();
int dlm_get_fd(void);
int dlm_dispatch(int fd);
link with - ldlm
</code></pre>
<h2>DESCRIPTION</h2>
<p> libdlm provides the programmatic userspace interface to the Distributed Lock manager. It provides all the calls you need to manipulate locks &amp; lockspaces<br />
 libdlm can be used in pthread or non-pthread applications. For pthread applications simply call the following function before doing any lock operations. If you&#8217;re using pthreads, remember to define _REENTRANT at the top of the program or using -D_REENTRANT on the compile line.<br />
 pthreads is the normal way of using the DLM. This way you simply initialize the DLM&#8217;s thread and all the AST routines will be delivered in that thread. You just call the dlm_lock() etc routines in the main line of your program.<br />
 If you don&#8217;t want to use pthreads or you want to handle the dlm callback ASTs yourself then you can get an FD handle to the DLM device and call <code>dlm_dispatch()</code> on it whenever it becomes active. That was ASTs will be delivered in the context of the thread/process that called <code>dlm_dispatch().</code> </p>
<h3>int dlm_pthread_init()</h3>
<p> Creates a thread to receive all lock ASTs. The AST callback function for lock operations will be called in the context of this thread. If there is a potential for local resource access conflicts you must provide your own pthread-based locking in the AST routine. </p>
<h3>int dlm_ls_pthread_init(dlm_lshandle_t lockspace)</h3>
<p> As dlm_pthread_init but initializes a thread for the specified lockspace. </p>
<h3>int dlm_pthread_cleanup()</h3>
<p> Cleans up the default lockspace threads after use. Normally you don&#8217;t need to call this, but if the locking code is in a dynamically loadable shared library this will probably be necessary.<br />
 For non-pthread based applications the DLM provides a file descriptor that the program can feed into poll/select. If activity is detected on that FD then a dispatch function should be called: </p>
<h3>int dlm_get_fd()</h3>
<p> Returns a file-descriptor for the DLM suitable for passing in to poll() or select(). </p>
<h3>int dlm_dispatch(int fd)</h3>
<p> Reads from the DLM and calls any AST routines that may be needed. This routine runs in the context of the caller so no extra locking is needed to protect local resources. </p>
<h2>libdlm_lt</h2>
<p> There also exists a &quot;light&quot; version of the libdlm library called libdlm_lt. This is provided for those applications that do not want to use pthread functions. If you use this library it is important that your application is NOT compiled with -D_REENTRANT or linked with libpthread. </p>
<h2>EXAMPLES</h2>
<p> Create a lockspace and start a thread to deliver its callbacks:<br />
dlm_lshandle_t ls;<br />
ls = dlm_create_lockspace(&#8220;myLS&#8221;, 0660);<br />
dlm_ls_pthread_init(ls);<br />
&#8230; status = dlm_ls_lock(ls,<br />
                         &#8230;);</p>
<p>&nbsp;<wbr>Using&nbsp;<wbr><a href="/docs/linux/man/2-poll/">poll</a>(2)&nbsp;<wbr>to wait for and dispatch ASTs </p>
<pre><code>
static int poll_for_ast(dlm_lshandle_t ls)
{
    struct pollfd pfd;
    pfd.fd = dlm_ls_get_fd(ls);
    pfd.events = POLLIN;
    while (!ast_called) {
        if (poll(&amp;pfd, 1, 0) &lt; 0) {
            perror("poll");
            return -1;
        }
        dlm_dispatch(dlm_ls_get_fd(ls));
    }
    ast_called = 0;
    return 0;
}
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libdlm/">libdlm</a></code>(3), <code><a href="/docs/linux/man/3-dlm_lock/">dlm_lock</a></code>(3), <code><a href="/docs/linux/man/3-dlm_unlock/">dlm_unlock</a></code>(3), <code><a href="/docs/linux/man/3-dlm_open_lockspace/">dlm_open_lockspace</a></code>(3), <code><a href="/docs/linux/man/3-dlm_create_lockspace/">dlm_create_lockspace</a></code>(3), <code><a href="/docs/linux/man/3-dlm_close_lockspace/">dlm_close_lockspace</a></code>(3), <code><a href="/docs/linux/man/3-dlm_release_lockspace/">dlm_release_lockspace</a></code>(3) </p>
<h2>Index</h2>
