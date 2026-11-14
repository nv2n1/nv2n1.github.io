---
title: "sd_listen_fds_start(3)"
name: "sd_listen_fds_start"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sd_listen_fds_start/"
---

sd_listen_fds, SD_LISTEN_FDS_START - Check for file descriptors passed by the system manager 

<h2>Synopsis</h2><pre>#include &lt;systemd/sd-daemon.h&gt;</pre><pre>#define SD_LISTEN_FDS_START 3</pre><dl COMPACT><dt> <b>int sd_listen_fds(int&nbsp;<wbr></b><i>unset_environment</i><b>);</b></dl><h2>Description</h2><b>sd_listen_fds()</b>
<dd>shall be called by a daemon to check for file descriptors passed by the init system as part of the socket-based activation logic. 

 If the <i>unset_environment</i> parameter is non-zero, <b>sd_listen_fds()</b> will unset the <i>$LISTEN_FDS</i> and <i>$LISTEN_PID</i> environment variables before returning (regardless of whether the function call itself succeeded or not). Further calls to <b>sd_listen_fds()</b> will then fail, but the variables are no longer inherited by child processes. 

 If a daemon receives more than one file descriptor, they will be passed in the same order as configured in the systemd socket unit file (see <b><a HREF="/docs/linux/man/5-systemd-socket/">systemd.socket</a></b>(5) for details). Nonetheless, it is recommended to verify the correct socket types before using them. To simplify this checking, the functions <b><a HREF="/docs/linux/man/3-sd_is_fifo/">sd_is_fifo</a></b>(3), <b><a HREF="/docs/linux/man/3-sd_is_socket/">sd_is_socket</a></b>(3), <b><a HREF="/docs/linux/man/3-sd_is_socket_inet/">sd_is_socket_inet</a></b>(3), <b><a HREF="/docs/linux/man/3-sd_is_socket_unix/">sd_is_socket_unix</a></b>(3) are provided. In order to maximize flexibility, it is recommended to make these checks as loose as possible without allowing incorrect setups. i.e. often, the actual port number a socket is bound to matters little for the service to work, hence it should not be verified. On the other hand, whether a socket is a datagram or stream socket matters a lot for the most common program logics and should be checked. 

 This function call will set the FD_CLOEXEC flag for all passed file descriptors to avoid further inheritance to children of the calling process. 

 If multiple socket units activate the same service the order of the file descriptors passed to its main process is undefined. If additional file descriptors have been passed to the service manager using <b><a HREF="/docs/linux/man/3-sd_pid_notify_with_fds/">sd_pid_notify_with_fds</a></b>(3)'s &quot;FDSTORE=1&quot; messages, these file descriptors are passed last, in arbitrary order, and with duplicates removed.
<h2>Return Value</h2>On failure, this call returns a negative errno-style error code. If <i>$LISTEN_FDS</i>/<i>$LISTEN_PID</i> was not set or was not correctly set for this daemon and hence no file descriptors were received, 0 is returned. Otherwise, the number of file descriptors passed is returned. The application may find them starting with file descriptor SD_LISTEN_FDS_START, i.e. file descriptor 3.
<h2>Notes</h2>These APIs are implemented as a shared library, which can be compiled and linked to with the <b>libsystemd</b>&nbsp;<wbr><b><a HREF="/docs/linux/man/1-pkg-config/">pkg-config</a></b>(1) file. 

 Internally, this function checks whether the <i>$LISTEN_PID</i> environment variable equals the daemon PID. If not, it returns immediately. Otherwise, it parses the number passed in the <i>$LISTEN_FDS</i> environment variable, then sets the FD_CLOEXEC flag for the parsed number of file descriptors starting from SD_LISTEN_FDS_START. Finally, it returns the parsed number.
<h2>Environment</h2><i>$LISTEN_PID</i>, <i>$LISTEN_FDS</i>
<dl COMPACT><dd>Set by the init system for supervised processes that use socket-based activation. This environment variable specifies the data <b>sd_listen_fds()</b> parses. See above for details.</dl><h2>See Also</h2><b><a HREF="/docs/linux/man/1-systemd/">systemd</a></b>(1), <b><a HREF="/docs/linux/man/3-sd-daemon/">sd-daemon</a></b>(3), <b><a HREF="/docs/linux/man/3-sd_is_fifo/">sd_is_fifo</a></b>(3), <b><a HREF="/docs/linux/man/3-sd_is_socket/">sd_is_socket</a></b>(3), <b><a HREF="/docs/linux/man/3-sd_is_socket_inet/">sd_is_socket_inet</a></b>(3), <b><a HREF="/docs/linux/man/3-sd_is_socket_unix/">sd_is_socket_unix</a></b>(3), <b><a HREF="/docs/linux/man/7-daemon/">daemon</a></b>(7), <b><a HREF="/docs/linux/man/5-systemd-service/">systemd.service</a></b>(5), <b><a HREF="/docs/linux/man/5-systemd-socket/">systemd.socket</a></b>(5)
