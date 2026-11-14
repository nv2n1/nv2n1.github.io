---
title: "aio(7)"
name: "aio"
section: "7"
letter: "a"
url: "/docs/linux/man/7-aio/"
description: "aio – POSIX asynchronous I/O overview"
---

<p>aio &#8211; POSIX asynchronous I/O overview</p>
<h2>Description</h2>
<p>The POSIX asynchronous I/O (AIO) interface allows applications to initiate one or more I/O operations that are performed asynchronously (i.e., in the background). The application can elect to be notified of completion of the I/O operation in a variety of ways: by delivery of a signal, by instantiation of a thread, or no notification at all. The POSIX AIO interface consists of the following functions:</p>
<dl>
<dt><code><a href="/docs/linux/man/3-aio_read/">aio_read</a></code>(3)</p>
<dd>Enqueue a read request. This is the asynchronous analog of <code><a href="/docs/linux/man/2-read/">read</a></code>(2).</p>
<dt><code><a href="/docs/linux/man/3-aio_write/">aio_write</a></code>(3)</p>
<dd>Enqueue a write request. This is the asynchronous analog of <code><a href="/docs/linux/man/2-write/">write</a></code>(2).</p>
<dt><code><a href="/docs/linux/man/3-aio_fsync/">aio_fsync</a></code>(3)</p>
<dd>Enqueue a sync request for the I/O operations on a file descriptor. This is the asynchronous analog of <code><a href="/docs/linux/man/2-fsync/">fsync</a></code>(2) and <code><a href="/docs/linux/man/2-fdatasync/">fdatasync</a></code>(2).</p>
<dt><code><a href="/docs/linux/man/3-aio_error/">aio_error</a></code>(3)</p>
<dd>Obtain the error status of an enqueued I/O request.</p>
<dt><code><a href="/docs/linux/man/3-aio_return/">aio_return</a></code>(3)</p>
<dd>Obtain the return status of a completed I/O request.</p>
<dt><code><a href="/docs/linux/man/3-aio_suspend/">aio_suspend</a></code>(3)</p>
<dd>Suspend the caller until one or more of a specified set of I/O requests completes.</p>
<dt><code><a href="/docs/linux/man/3-aio_cancel/">aio_cancel</a></code>(3)</p>
<dd>Attempt to cancel outstanding I/O requests on a specified file descriptor.</p>
<dt><code><a href="/docs/linux/man/3-lio_listio/">lio_listio</a></code>(3)</p>
<dd>Enqueue multiple I/O requests using a single function call.</dl>
<p> The <i>aiocb</i> (&quot;asynchronous I/O control block&quot;) structure defines parameters that control an I/O operation. An argument of this type is employed with all of the functions listed above. This structure has the following form: </p>
<pre><code>#include &lt;aiocb.h&gt;</code></pre>
<p> struct aiocb {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;The order of these fields is implementation-dependent&nbsp;*/ int aio_fildes;               /* File descriptor */<br />
off_t aio_offset;             /* File offset */<br />
volatile void *aio_buf;       /* Location of buffer */<br />
size_t aio_nbytes;            /* Length of transfer */<br />
int aio_reqprio;              /* Request priority */<br />
struct sigevent aio_sigevent; /* Notification method */<br />
int aio_lio_opcode;           /* Operation to be performed;<br />
                                 lio_listio() only */<br />
/* Various implementation-internal fields not shown */<br />
}<br />
;<br />
/* Operation codes for &#8216;aio_lio_opcode&#8217;: */ enum { LIO_READ, LIO_WRITE, LIO_NOP }; The fields of this structure are as follows:</p>
<dl>
<dt><i>aio_fildes</i></p>
<dd>The file descriptor on which the I/O operation is to be performed.</p>
<dt><i>aio_offset</i></p>
<dd>This is the file offset at which the I/O operation is to be performed.</p>
<dt><i>aio_buf</i></p>
<dd>This is the buffer used to transfer data for a read or write operation.</p>
<dt><i>aio_nbytes</i></p>
<dd>This is the size of the buffer pointed to by <i>aio_buf</i>.</p>
<dt><i>aio_reqprio</i></p>
<dd>This field specifies a value that is subtracted from the calling thread&#8217;s real-time priority in order to determine the priority for execution of this I/O request (see <code><a href="/docs/linux/man/3-pthread_setschedparam/">pthread_setschedparam</a></code>(3)). The specified value must be between 0 and the value returned by <i>sysconf(_SC_AIO_PRIO_DELTA_MAX)</i>. This field is ignored for file synchronization operations.</p>
<dt><i>aio_sigevent</i></p>
<dd>This field is a structure that specifies how the caller is to be notified when the asynchronous I/O operation completes. Possible values for <i>aio_sigevent.sigev_notify</i> are <code>SIGEV_NONE</code>, <code>SIGEV_SIGNAL</code>, and <code>SIGEV_THREAD</code>. See <code><a href="/docs/linux/man/7-sigevent/">sigevent</a></code>(7) for further details.</p>
<dt><i>aio_lio_opcode</i></p>
<dd>The type of operation to be performed; used only for <code><a href="/docs/linux/man/3-lio_listio/">lio_listio</a></code>(3).</dl>
<p> In addition to the standard functions listed above, the GNU C library provides the following extension to the POSIX AIO API:</p>
<dl>
<dt><code><a href="/docs/linux/man/3-aio_init/">aio_init</a></code>(3)</p>
<dd>Set parameters for tuning the behavior of the glibc POSIX AIO implementation.</dl>
<h2>Errors</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd>The <i>aio_reqprio</i> field of the <i>aiocb</i> structure was less than 0, or was greater than the limit returned by the call <i>sysconf(_SC_AIO_PRIO_DELTA_MAX)</i>.</dl>
<h2>Versions</h2>
<p>The POSIX AIO interfaces are provided by glibc since version 2.1.</p>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008.</p>
<h2>Notes</h2>
<p>It is a good idea to zero out the control block buffer before use (see <code><a href="/docs/linux/man/3-memset/">memset</a></code>(3)). The control block buffer and the buffer pointed to by <i>aio_buf</i> must not be changed while the I/O operation is in progress. These buffers must remain valid until the I/O operation completes. </p>
<p> Simultaneous asynchronous read or write operations using the same <i>aiocb</i> structure yield undefined results. </p>
<p> The current Linux POSIX AIO implementation is provided in user space by glibc. This has a number of limitations, most notably that maintaining multiple threads to perform I/O operations is expensive and scales poorly. Work has been in progress for some time on a kernel state-machine-based implementation of asynchronous I/O (see <code><a href="/docs/linux/man/2-io_submit/">io_submit</a></code>(2), <code><a href="/docs/linux/man/2-io_setup/">io_setup</a></code>(2), <code><a href="/docs/linux/man/2-io_cancel/">io_cancel</a></code>(2), <code><a href="/docs/linux/man/2-io_destroy/">io_destroy</a></code>(2), <code><a href="/docs/linux/man/2-io_getevents/">io_getevents</a></code>(2)), but this implementation hasn&#8217;t yet matured to the point where the POSIX AIO implementation can be completely reimplemented using the kernel system calls.</p>
<h2>Examples</h2>
<p>The program below opens each of the files named in its command-line arguments and queues a request on the resulting file descriptor using <code><a href="/docs/linux/man/3-aio_read/">aio_read</a></code>(3). The program then loops, periodically monitoring each of the I/O operations that is still in progress using <code><a href="/docs/linux/man/3-aio_error/">aio_error</a></code>(3). Each of the I/O requests is set up to provide notification by delivery of a signal. After all I/O requests have completed, the program retrieves their status using <code><a href="/docs/linux/man/3-aio_return/">aio_return</a></code>(3). The <code>SIGQUIT</code> signal (generated by typing control-\) causes the program to request cancellation of each of the outstanding requests using <code><a href="/docs/linux/man/3-aio_cancel/">aio_cancel</a></code>(3). Here is an example of what we might see when running this program. In this example, the program queues two requests to standard input, and these are satisfied by two lines of input containing &quot;abc&quot; and &quot;x&quot;. for (int j = 0; j &lt; numReqs; j++) {<br />
    ioList[j].reqNum = j;<br />
    ioList[j].status = EINPROGRESS;<br />
    ioList[j].aiocbp = &amp;aiocbList[j];<br />
    ioList[j].aiocbp-&gt;aio_fildes = open(argv[j + 1], O_RDONLY);<br />
    if (ioList[j].aiocbp-&gt;aio_fildes == -1)<br />
        errExit(&quot;open&quot;);<br />
    printf(&quot;opened %s on descriptor %d
&quot;, argv[j + 1],<br />
           ioList[j].aiocbp-&gt;aio_fildes);<br />
    ioList[j].aiocbp-&gt;aio_buf = malloc(BUF_SIZE);<br />
    if (ioList[j].aiocbp-&gt;aio_buf == NULL)<br />
        errExit(&quot;malloc&quot;);<br />
    ioList[j].aiocbp-&gt;aio_nbytes = BUF_SIZE;<br />
    ioList[j].aiocbp-&gt;aio_reqprio = 0;<br />
    ioList[j].aiocbp-&gt;aio_offset = 0;<br />
    ioList[j].aiocbp-&gt;aio_sigevent.sigev_notify = SIGEV_SIGNAL;<br />
    ioList[j].aiocbp-&gt;aio_sigevent.sigev_signo = IO_SIGNAL;<br />
    ioList[j].aiocbp-&gt;aio_sigevent.sigev_value.sival_ptr =<br />
        &amp;ioList[j];<br />
    s = aio_read(ioList[j].aiocbp);<br />
    if (s == -1)<br />
        errExit(&quot;aio_read&quot;);<br />
}<br />
openReqs = numReqs;<br />
/* Loop, monitoring status of I/O requests */<br />
while (openReqs &gt; 0) {<br />
    sleep(3); /* Delay between each monitoring step */<br />
    if (gotSIGQUIT) {<br />
        /* On receipt of SIGQUIT, attempt to cancel each of the<br />
                       outstanding I/O requests, and display status returned<br />
                       from the cancellation requests */<br />
        printf(&quot;got SIGQUIT; canceling I/O requests: 
&quot;);<br />
        for (int j = 0; j &lt; numReqs; j++) {<br />
            if (ioList[j].status == EINPROGRESS) {<br />
                printf(&quot;    Request %d on descriptor %d:&quot;, j,<br />
                       ioList[j].aiocbp-&gt;aio_fildes);<br />
                s = aio_cancel(ioList[j].aiocbp-&gt;aio_fildes,<br />
                               ioList[j].aiocbp);<br />
                if (s == AIO_CANCELED)<br />
                    printf(&quot;I/O canceled
&quot;);<br />
                else if (s == AIO_NOTCANCELED)<br />
                    printf(&quot;I/O not canceled
&quot;);<br />
                else if (s == AIO_ALLDONE)<br />
                    printf(&quot;I/O all done
&quot;);<br />
                else<br />
                    perror(&quot;aio_cancel&quot;);<br />
            }<br />
        }<br />
        gotSIGQUIT = 0;<br />
    }<br />
    /* Check the status of each I/O request that is still<br />
               in progress */<br />
    printf(&quot;aio_error():
&quot;);<br />
    for (int j = 0; j &lt; numReqs; j++) {<br />
        if (ioList[j].status == EINPROGRESS) {<br />
            printf(&quot;    for request %d (descriptor %d): &quot;,<br />
                   j, ioList[j].aiocbp-&gt;aio_fildes);<br />
            ioList[j].status = aio_error(ioList[j].aiocbp);<br />
            switch (ioList[j].status) {<br />
            case 0:<br />
                printf(&quot;I/O succeeded
&quot;);<br />
                break;<br />
            case EINPROGRESS:<br />
                printf(&quot;In progress
&quot;);<br />
                break;<br />
            case ECANCELED:<br />
                printf(&quot;Canceled
&quot;);<br />
                break;<br />
            default:<br />
                perror(&quot;aio_error&quot;);<br />
                break;<br />
            }<br />
            if (ioList[j].status != EINPROGRESS)<br />
                openReqs&#8211;;<br />
        }<br />
    }<br />
}<br />
printf(&quot;All I/O requests completed
&quot;);<br />
/* Check status return of all I/O requests */<br />
printf(&quot;aio_return():
&quot;);<br />
for (int j = 0; j &lt; numReqs; j++) {<br />
    ssize_t s;<br />
    s = aio_return(ioList[j].aiocbp);<br />
    printf(&quot;    for request %d (descriptor %d): %zd
&quot;,<br />
           j, ioList[j].aiocbp-&gt;aio_fildes, s);<br />
}<br />
exit(EXIT_SUCCESS);<br />
} int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct sigaction sa;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int s;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int numReqs;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Total number of queued I/O requests&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int openReqs;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Number of I/O requests still in progress&nbsp;*/ if (argc &lt; 2) {<br />
    fprintf(stderr, &quot;Usage: %s &lt;pathname&gt; &lt;pathname&gt;&#8230;
&quot;,<br />
            argv[0]);<br />
    exit(EXIT_FAILURE);<br />
}<br />
numReqs = argc &#8211; 1;<br />
/* Allocate our arrays */<br />
struct ioRequest *ioList = calloc(numReqs, sizeof(*ioList));<br />
if (ioList == NULL)<br />
    errExit(&quot;calloc&quot;);<br />
struct aiocb *aiocbList = calloc(numReqs, sizeof(*aiocbList));<br />
if (aiocbList == NULL)<br />
    errExit(&quot;calloc&quot;);<br />
/* Establish handlers for SIGQUIT and the I/O completion signal */<br />
sa.sa_flags = SA_RESTART;<br />
sigemptyset(&amp;sa.sa_mask);<br />
sa.sa_handler = quitHandler;<br />
if (sigaction(SIGQUIT, &amp;sa, NULL) == -1)<br />
    errExit(&quot;sigaction&quot;);<br />
sa.sa_flags = SA_RESTART | SA_SIGINFO;<br />
sa.sa_sigaction = aioSigHandler;<br />
if (sigaction(IO_SIGNAL, &amp;sa, NULL) == -1)<br />
    errExit(&quot;sigaction&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Open each file specified on the command line, and queue<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;a read request on the resulting file descriptor&nbsp;*/ </p>
<pre><code>for (int j = 0; j &lt; numReqs; j++) {
    ioList[j].reqNum = j;
    ioList[j].status = EINPROGRESS;
    ioList[j].aiocbp = &amp;aiocbList[j];
    ioList[j].aiocbp-&gt;aio_fildes = open(argv[j + 1], O_RDONLY);
    if (ioList[j].aiocbp-&gt;aio_fildes == -1)
        errExit(&quot;open&quot;);
    printf(&quot;opened %s on descriptor %d
&quot;, argv[j + 1],
           ioList[j].aiocbp-&gt;aio_fildes);
    ioList[j].aiocbp-&gt;aio_buf = malloc(BUF_SIZE);
    if (ioList[j].aiocbp-&gt;aio_buf == NULL)
        errExit(&quot;malloc&quot;);
    ioList[j].aiocbp-&gt;aio_nbytes = BUF_SIZE;
    ioList[j].aiocbp-&gt;aio_reqprio = 0;
    ioList[j].aiocbp-&gt;aio_offset = 0;
    ioList[j].aiocbp-&gt;aio_sigevent.sigev_notify = SIGEV_SIGNAL;
    ioList[j].aiocbp-&gt;aio_sigevent.sigev_signo = IO_SIGNAL;
    ioList[j].aiocbp-&gt;aio_sigevent.sigev_value.sival_ptr =
        &amp;ioList[j];
    s = aio_read(ioList[j].aiocbp);
    if (s == -1)
        errExit(&quot;aio_read&quot;);
}
openReqs = numReqs;
/* Loop, monitoring status of I/O requests */
while (openReqs &gt; 0) {
    sleep(3); /* Delay between each monitoring step */
    if (gotSIGQUIT) {
        /* On receipt of SIGQUIT, attempt to cancel each of the
                       outstanding I/O requests, and display status returned
                       from the cancellation requests */
        printf(&quot;got SIGQUIT; canceling I/O requests: 
&quot;);
        for (int j = 0; j &lt; numReqs; j++) {
            if (ioList[j].status == EINPROGRESS) {
                printf(&quot;    Request %d on descriptor %d:&quot;, j,
                       ioList[j].aiocbp-&gt;aio_fildes);
                s = aio_cancel(ioList[j].aiocbp-&gt;aio_fildes,
                               ioList[j].aiocbp);
                if (s == AIO_CANCELED)
                    printf(&quot;I/O canceled
&quot;);
                else if (s == AIO_NOTCANCELED)
                    printf(&quot;I/O not canceled
&quot;);
                else if (s == AIO_ALLDONE)
                    printf(&quot;I/O all done
&quot;);
                else
                    perror(&quot;aio_cancel&quot;);
            }
        }
        gotSIGQUIT = 0;
    }
    /* Check the status of each I/O request that is still
               in progress */
    printf(&quot;aio_error():
&quot;);
    for (int j = 0; j &lt; numReqs; j++) {
        if (ioList[j].status == EINPROGRESS) {
            printf(&quot;    for request %d (descriptor %d): &quot;,
                   j, ioList[j].aiocbp-&gt;aio_fildes);
            ioList[j].status = aio_error(ioList[j].aiocbp);
            switch (ioList[j].status) {
            case 0:
                printf(&quot;I/O succeeded
&quot;);
                break;
            case EINPROGRESS:
                printf(&quot;In progress
&quot;);
                break;
            case ECANCELED:
                printf(&quot;Canceled
&quot;);
                break;
            default:
                perror(&quot;aio_error&quot;);
                break;
            }
            if (ioList[j].status != EINPROGRESS)
                openReqs--;
        }
    }
}
printf(&quot;All I/O requests completed
&quot;);
/* Check status return of all I/O requests */
printf(&quot;aio_return():
&quot;);
for (int j = 0; j &lt; numReqs; j++) {
    ssize_t s;
    s = aio_return(ioList[j].aiocbp);
    printf(&quot;    for request %d (descriptor %d): %zd
&quot;,
           j, ioList[j].aiocbp-&gt;aio_fildes, s);
}
exit(EXIT_SUCCESS);
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-io_cancel/">io_cancel</a></code>(2), <code><a href="/docs/linux/man/2-io_destroy/">io_destroy</a></code>(2), <code><a href="/docs/linux/man/2-io_getevents/">io_getevents</a></code>(2), <code><a href="/docs/linux/man/2-io_setup/">io_setup</a></code>(2), <code><a href="/docs/linux/man/2-io_submit/">io_submit</a></code>(2), <code><a href="/docs/linux/man/3-aio_cancel/">aio_cancel</a></code>(3), <code><a href="/docs/linux/man/3-aio_error/">aio_error</a></code>(3), <code><a href="/docs/linux/man/3-aio_init/">aio_init</a></code>(3), <code><a href="/docs/linux/man/3-aio_read/">aio_read</a></code>(3), <code><a href="/docs/linux/man/3-aio_return/">aio_return</a></code>(3), <code><a href="/docs/linux/man/3-aio_write/">aio_write</a></code>(3), <code><a href="/docs/linux/man/3-lio_listio/">lio_listio</a></code>(3) </p>
<p> &quot;Asynchronous I/O Support in Linux 2.5&quot;, Bhattacharya, Pratt, Pulavarty, and Morgan, Proceedings of the Linux Symposium, 2003,</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
