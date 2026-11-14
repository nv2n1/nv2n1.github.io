---
title: "iv_examples(3)"
name: "iv_examples"
section: "3"
letter: "i"
url: "/docs/linux/man/3-iv_examples/"
description: "iv_examples – ivykis examples"
---

<h2>NAME</h2>
<p> iv_examples &#8211; ivykis examples</p>
<h2>EXAMPLE</h2>
<p> ivykis is initialised by calling <code><a href="/docs/linux/man/3-iv_init/">iv_init</a></code>(3). This function is the first function to call when dealing with ivykis &#8212; it has to be called before registering file descriptors or timers. </p>
<p> The ivykis main event loop is started by calling <code><a href="/docs/linux/man/3-iv_main/">iv_main</a></code>(3). This function generally does not return, except when <code><a href="/docs/linux/man/3-iv_quit/">iv_quit</a></code>(3) is called somewhere during execution of the program. </p>
<p> An application asks ivykis to monitor a certain file descriptor by filling out a structure of type &#8216;struct iv_fd&#8217; with a file descriptor number and a callback function, and calling the function iv_fd_register. </p>
<p> The first example program waits for data from standard input, and writes a message to standard out whenever something is received: </p>
<pre><code>
#include &lt;iv.h&gt;
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
struct iv_fd fd_stdin;
static void callback(void *dummy)
{
    char buf[1024];
    int len;
    len = read(fd_stdin.fd, buf, sizeof(buf));
    if (len &lt;= 0) {
        if (len &lt; 0) {
            if (errno == EAGAIN)
                return;
            perror("read");
        }
        exit(1);
    }
    printf("read %d bytes of data from stdin
", len);
}
int main()
{
    iv_init();
    IV_FD_INIT(&amp;fd_stdin);
    fd_stdin.fd = 0;
    fd_stdin.handler_in = callback;
    iv_fd_register(&amp;fd_stdin);
    iv_main();
    iv_deinit();
    return 0;
}
</code></pre>
<p> The application is responsible for memory management of &#8216;struct iv_fd&#8217;s passed to ivykis. For example, it should not free memory that contains such structures that are still registered with ivykis (i.e. haven&#8217;t had iv_fd_unregister called on them). </p>
<p> iv_fd_register transparently sets the passed file descriptor to nonblocking mode, in anticipation of its future usage. </p>
<p> File descriptor callbacks are called in a level-triggered fashion. Therefore, the way of dealing with fd_stdin in the example callback function is safe. In case there arrives data between read and detecting EAGAIN, ivykis will re-call the callback function after it returns. Also, if there are more than 1024 bytes waiting in the input buffer, ivykis will re-call the callback function until all data from stdin have been drained.</p>
<h2>EXAMPLE 2</h2>
<p> The second example accepts connections on TCP port 6667, and waits on each of the connections for data. When data is received on any connection, a message is printed to standard out. </p>
<p>#include &lt;iv.h&gt;<br />
#include &lt;netinet/in.h&gt;<br />
#include &lt;stdio.h&gt;<br />
#include &lt;stdlib.h&gt;<br />
struct connection {<br />
    struct iv_fd fd;<br />
    /* other per-connection data goes here */<br />
};<br />
struct listening_socket {<br />
    struct iv_fd fd;<br />
    /* other per-listening socket data goes here */<br />
};<br />
static void connection_handler(void *_conn)<br />
{<br />
    struct connection *conn = (struct connection *)_conn;<br />
    char buf[1024];<br />
    int len;<br />
    len = read(conn-&gt;fd.fd, buf, sizeof(buf));<br />
    if (len &lt;= 0) {<br />
        if (len &lt; 0 &amp;&amp; errno == EAGAIN)<br />
            return;<br />
        iv_fd_unregister(&amp;conn-&gt;fd);<br />
        close(conn-&gt;fd.fd);<br />
        free(conn);<br />
        return;<br />
    }<br />
    printf(&#8220;got %d bytes of data from %p
&#8221;, len, conn);<br />
}<br />
static void listening_socket_handler(void *_sock)<br />
{<br />
    struct listening_socket *sock = (struct listening_socket *)_sock;<br />
    struct sockaddr_in addr;<br />
    socklen_t addrlen;<br />
    struct connection *conn;<br />
    int fd;<br />
    addrlen = sizeof(addr);<br />
    fd = accept(sock-&gt;fd.fd, (struct sockaddr *)&amp;addr, &amp;addrlen);<br />
    if (fd &lt; 0) {<br />
        if (errno == EAGAIN)<br />
            return;<br />
        perror(&#8220;accept&#8221;);<br />
        exit(1);<br />
    }<br />
    conn = malloc(sizeof(*conn));<br />
    if (conn == NULL) {<br />
        fprintf(stderr, &#8220;listening_socket_handler: memory allocation error, dropping connection&#8221;);<br />
        close(fd);<br />
        return;<br />
    }<br />
    IV_FD_INIT(&amp;conn-&gt;fd);<br />
    conn-&gt;fd.fd = fd;<br />
    conn-&gt;fd.cookie = (void *)conn;<br />
    conn-&gt;fd.handler_in = connection_handler;<br />
    iv_fd_register(&amp;conn-&gt;fd);<br />
}<br />
int main()<br />
{<br />
    struct listening_socket s;<br />
    struct sockaddr_in addr;<br />
    int fd;<br />
    fd = socket(AF_INET, SOCK_STREAM, 0);<br />
    if (fd &lt; 0) {<br />
        perror(&#8220;socket&#8221;);<br />
        exit(1);<br />
    }<br />
    addr.sin_family = AF_INET;<br />
    addr.sin_addr.s_addr = htonl(INADDR_ANY);<br />
    addr.sin_port = htons(6667);<br />
    if (bind(fd, (struct sockaddr *)&amp;addr, sizeof(addr)) &lt; 0) {<br />
        perror(&#8220;bind&#8221;);<br />
        exit(1);<br />
    }<br />
    if (listen(fd, 4) &lt; 0) {<br />
        perror(&#8220;listen&#8221;);<br />
        exit(1);<br />
    }<br />
    iv_init();<br />
    IV_FD_INIT(&amp;s.fd);<br />
    s.fd.fd = fd;<br />
    s.fd.cookie = (void *)&amp;s;<br />
    s.fd.handler_in = listening_socket_handler;<br />
    iv_fd_register(&amp;s.fd);<br />
    iv_main();<br />
    iv_deinit();<br />
    return 0;<br />
}</p>
<p> As illustrated, it is possible to pass cookies into callback functions. This is useful for conveying information on which higher-level entity (such as &#8216;connection&#8217; or &#8216;listening socket&#8217;) generated the event for which the callback was called. </p>
<p> Note how it is possible to unregister and even free a &#8216;struct iv_fd&#8217; in its own callback function. There is logic in ivykis to deal with this case.</p>
<h2>EXAMPLE 3</h2>
<p> This example extends the previous example by a per-connection timer that disconnects the client after too long a period of inactivity. Lines not present in example 2 or different than in example 2 are indicated by &#8216;//XXXX&#8217; in the right-hand margin. </p>
<p>#include &lt;iv.h&gt;<br />
#include &lt;netinet/in.h&gt;<br />
#include &lt;stdio.h&gt;<br />
#include &lt;stdlib.h&gt;<br />
#define CONNECTION_TIMEOUT (10)<br />
struct connection {<br />
    struct iv_fd fd;<br />
    struct iv_timer disconnect_timeout; // XXXX<br />
    /* other per-connection data goes here */<br />
};<br />
struct listening_socket {<br />
    struct iv_fd fd;<br />
    /* other per-listening socket data goes here */<br />
};<br />
static void connection_handler(void *_conn)<br />
{<br />
    struct connection *conn = (struct connection *)_conn;<br />
    char buf[1024];<br />
    int len;<br />
    len = read(conn-&gt;fd.fd, buf, sizeof(buf));<br />
    if (len &lt;= 0) {<br />
        if (len &lt; 0 &amp;&amp; errno == EAGAIN)<br />
            return;<br />
        iv_timer_unregister(&amp;conn-&gt;disconnect_timeout); // XXXX<br />
        iv_fd_unregister(&amp;conn-&gt;fd);<br />
        close(conn-&gt;fd.fd);<br />
        free(conn);<br />
        return;<br />
    }<br />
    printf(&#8220;got %d bytes of data from %p
&#8221;, len, conn);<br />
    iv_timer_unregister(&amp;conn-&gt;disconnect_timeout);                // XXXX<br />
    iv_validate_now();                                             // XXXX<br />
    conn-&gt;disconnect_timeout.expires = iv_now;                     // XXXX<br />
    conn-&gt;disconnect_timeout.expires.tv_sec += CONNECTION_TIMEOUT; // XXXX<br />
    iv_timer_register(&amp;conn-&gt;disconnect_timeout);                  // XXXX<br />
}<br />
static void disconnect_timeout_expired(void *_conn)       // XXXX<br />
{                                                         // XXXX<br />
    struct connection *conn = (struct connection *)_conn; // XXXX<br />
    iv_fd_unregister(&amp;conn-&gt;fd);                          // XXXX<br />
    close(conn-&gt;fd.fd);                                   // XXXX<br />
    free(conn);                                           // XXXX<br />
} // XXXX<br />
static void listening_socket_handler(void *_sock)<br />
{<br />
    struct listening_socket *sock = (struct listening_socket *)_sock;<br />
    struct sockaddr_in addr;<br />
    socklen_t addrlen;<br />
    struct connection *conn;<br />
    int fd;<br />
    addrlen = sizeof(addr);<br />
    fd = accept(sock-&gt;fd.fd, (struct sockaddr *)&amp;addr, &amp;addrlen);<br />
    if (fd &lt; 0) {<br />
        if (errno == EAGAIN)<br />
            return;<br />
        perror(&#8220;accept&#8221;);<br />
        exit(1);<br />
    }<br />
    conn = malloc(sizeof(*conn));<br />
    if (conn == NULL) {<br />
        fprintf(stderr, &#8220;listening_socket_handler: memory allocation error, dropping connection&#8221;);<br />
        close(fd);<br />
        return;<br />
    }<br />
    IV_FD_INIT(&amp;conn-&gt;fd);<br />
    conn-&gt;fd.fd = fd;<br />
    conn-&gt;fd.cookie = (void *)conn;<br />
    conn-&gt;fd.handler_in = connection_handler;<br />
    iv_fd_register(&amp;conn-&gt;fd);<br />
    IV_TIMER_INIT(&amp;conn-&gt;disconnect_timeout);                      // XXXX<br />
    iv_validate_now();                                             // XXXX<br />
    conn-&gt;disconnect_timeout.cookie = (void *)conn;                // XXXX<br />
    conn-&gt;disconnect_timeout.handler = disconnect_timeout_expired; // XXXX<br />
    conn-&gt;disconnect_timeout.expires = iv_now;                     // XXXX<br />
    conn-&gt;disconnect_timeout.expires.tv_sec += CONNECTION_TIMEOUT; // XXXX<br />
    iv_timer_register(&amp;conn-&gt;disconnect_timeout);                  // XXXX<br />
}<br />
int main()<br />
{<br />
    struct listening_socket s;<br />
    struct sockaddr_in addr;<br />
    int fd;<br />
    fd = socket(AF_INET, SOCK_STREAM, 0);<br />
    if (fd &lt; 0) {<br />
        perror(&#8220;socket&#8221;);<br />
        exit(1);<br />
    }<br />
    addr.sin_family = AF_INET;<br />
    addr.sin_addr.s_addr = htonl(INADDR_ANY);<br />
    addr.sin_port = htons(6667);<br />
    if (bind(fd, (struct sockaddr *)&amp;addr, sizeof(addr)) &lt; 0) {<br />
        perror(&#8220;bind&#8221;);<br />
        exit(1);<br />
    }<br />
    if (listen(fd, 4) &lt; 0) {<br />
        perror(&#8220;listen&#8221;);<br />
        exit(1);<br />
    }<br />
    iv_init();<br />
    IV_FD_INIT(&amp;s.fd);<br />
    s.fd.fd = fd;<br />
    s.fd.cookie = (void *)&amp;s;<br />
    s.fd.handler_in = listening_socket_handler;<br />
    iv_fd_register(&amp;s.fd);<br />
    iv_main();<br />
    iv_deinit();<br />
    return 0;<br />
}</p>
<p> The global variable &#8216;iv_now&#8217; contains the current time-of-day. However, it is updated lazily, and its contents might be stale at any given time. Before using it, <code><a href="/docs/linux/man/3-iv_validate_now/">iv_validate_now</a></code>(3) must be called.</p>
<h2>EXAMPLE 4</h2>
<p> The fourth example demonstrates how to use a custom fatal error handler that does not write the message to syslog. </p>
<pre><code>
#include &lt;iv.h&gt;
#include &lt;stdio.h&gt;
static void fatal_error(const char *msg)
{
    fprintf(stderr, "ivykis: FATAL ERROR: %s
", msg);
}
int main()
{
    iv_init();
    iv_set_fatal_msg_handler(fatal_error);
    iv_fatal("Programmatically triggered fatal error %d.", 42);
    printf("This code is never reached.
");
    iv_deinit();
    return 0;
}
</code></pre>
<p> This program will abort immediately, with the error message printed to the standard error stream.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ivykis/">ivykis</a></code>(3), <code><a href="/docs/linux/man/3-iv_fatal/">iv_fatal</a></code>(3), <code><a href="/docs/linux/man/3-iv_fd/">iv_fd</a></code>(3), <code><a href="/docs/linux/man/3-iv_timer/">iv_timer</a></code>(3), <code><a href="/docs/linux/man/3-iv_task/">iv_task</a></code>(3), <code><a href="/docs/linux/man/3-iv_init/">iv_init</a></code>(3), <code><a href="/docs/linux/man/3-iv_time/">iv_time</a></code>(3) </p>
<h2>Index</h2>
