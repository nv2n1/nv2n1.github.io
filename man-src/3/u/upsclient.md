---
title: "upsclient(3)"
name: "upsclient"
section: "3"
letter: "u"
url: "/docs/linux/man/3-upsclient/"
description: "upsclient – Network UPS Tools client access library"
---

<p>upsclient &#8211; Network UPS Tools client access library</p>
<h2>Description</h2>
<p>The Network UPS Tools (NUT) <code>upsclient</code> library provides a number of useful functions for programs to use when communicating with <code><a href="/docs/linux/man/8-upsd/">upsd</a></code>(8). Many of the low-level socket and protocol details are handled automatically when using this interface. </p>
<p> State is maintained across calls in an opaque structure called UPSCONN_t. Callers are expected to create one per connection. These will be provided to most of the <code>upsclient</code> functions. The format of this structure is subject to change, and client programs must not reference elements within it directly.</p>
<h2>Initialization And Cleanup</h2>
<p>Before creating any connection, and in general using any upscli function, you must call <code><a href="/docs/linux/man/3-upscli_init/">upscli_init</a></code>(3) with proper parameters to initialize upscli module. </p>
<p> To register specific host security policy, you must call <code><a href="/docs/linux/man/3-upscli_add_host_cert/">upscli_add_host_cert</a></code>(3) before initialize connection to it. </p>
<p> In the same way, just before exiting, and after all upscli usage, you must call <code><a href="/docs/linux/man/3-upscli_cleanup/">upscli_cleanup</a></code>(3) to flush cache files and perform other cleanup.</p>
<h2>Network Functions</h2>
<p>To create a new connection, use <code><a href="/docs/linux/man/3-upscli_connect/">upscli_connect</a></code>(3). This will also initialize the UPSCONN_t structure. To verify that a connection has been established later, <code><a href="/docs/linux/man/3-upscli_fd/">upscli_fd</a></code>(3) can be used to return the file descriptor. Clients wishing to check for the presence and operation of SSL on a connection may call <code><a href="/docs/linux/man/3-upscli_ssl/">upscli_ssl</a></code>(3). </p>
<p> The majority of clients will use <code><a href="/docs/linux/man/3-upscli_get/">upscli_get</a></code>(3) to retrieve single items from the server. To retrieve a list, use <code><a href="/docs/linux/man/3-upscli_list_start/">upscli_list_start</a></code>(3) to get it started, then call <code><a href="/docs/linux/man/3-upscli_list_next/">upscli_list_next</a></code>(3) for each element. </p>
<p> Raw lines of text may be sent to <code><a href="/docs/linux/man/8-upsd/">upsd</a></code>(8) with <code><a href="/docs/linux/man/3-upscli_sendline/">upscli_sendline</a></code>(3). Reading raw lines is possible with <code><a href="/docs/linux/man/3-upscli_readline/">upscli_readline</a></code>(3). Client programs are expected to format these lines according to the protocol, as no checking will be performed before transmission. </p>
<p> At the end of a connection, you must call <code><a href="/docs/linux/man/3-upsclient_disconnect/">upsclient_disconnect</a></code>(3) to disconnect from <code>upsd</code> and release any dynamic memory associated with the UPSCONN_t structure. Failure to call this function will result in memory and file descriptor leaks in your program.</p>
<h2>Error Handling</h2>
<p>In the event of an error, <code><a href="/docs/linux/man/3-upscli_strerror/">upscli_strerror</a></code>(3) will provide human-readable details on what happened. <code><a href="/docs/linux/man/3-upscli_upserror/">upscli_upserror</a></code>(3) may also be used to retrieve the error number. These numbers are defined in <code>upsclient.h</code> as <i>UPSCLI_ERR_*</i>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-libupsclient-config/">libupsclient-config</a></code>(1), <code><a href="/docs/linux/man/3-upscli_init/">upscli_init</a></code>(3), <code><a href="/docs/linux/man/3-upscli_cleanup/">upscli_cleanup</a></code>(3), <code><a href="/docs/linux/man/3-upscli_add_host_cert/">upscli_add_host_cert</a></code>(3), <code><a href="/docs/linux/man/3-upscli_connect/">upscli_connect</a></code>(3), <code><a href="/docs/linux/man/3-upscli_disconnect/">upscli_disconnect</a></code>(3), <code><a href="/docs/linux/man/3-upscli_fd/">upscli_fd</a></code>(3), <code><a href="/docs/linux/man/3-upscli_getvar/">upscli_getvar</a></code>(3), <code><a href="/docs/linux/man/3-upscli_list_next/">upscli_list_next</a></code>(3), <code><a href="/docs/linux/man/3-upscli_list_start/">upscli_list_start</a></code>(3), <code><a href="/docs/linux/man/3-upscli_readline/">upscli_readline</a></code>(3), <code><a href="/docs/linux/man/3-upscli_sendline/">upscli_sendline</a></code>(3), <code><a href="/docs/linux/man/3-upscli_splitaddr/">upscli_splitaddr</a></code>(3), <code><a href="/docs/linux/man/3-upscli_splitname/">upscli_splitname</a></code>(3), <code><a href="/docs/linux/man/3-upscli_ssl/">upscli_ssl</a></code>(3), <code><a href="/docs/linux/man/3-upscli_strerror/">upscli_strerror</a></code>(3), <code><a href="/docs/linux/man/3-upscli_upserror/">upscli_upserror</a></code>(3) </p>
