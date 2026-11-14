---
title: "globus_xio_tcp_driver-h(3)"
name: "globus_xio_tcp_driver-h"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_xio_tcp_driver-h/"
description: "builtins/tcp/globus_xio_tcp_driver.h –"
---

<p>builtins/tcp/globus_xio_tcp_driver.h &#8211; </p>
<p> Header file for XIO TCP Driver.</p>
<h2>Synopsis</h2>
<p>#include &#8216;globus_xio_system.h&#8217; </p>
<h3>Macros</h3>
<p>#define <code>GLOBUS_XIO_TCP_INVALID_HANDLE</code> </p>
<h3>Enumerations</h3>
<p>enum <code>globus_xio_tcp_error_type_t</code> { <code>GLOBUS_XIO_TCP_ERROR_NO_ADDRS</code> } </p>
<p> enum <code>globus_xio_tcp_cmd_t</code> { <code>GLOBUS_XIO_TCP_SET_SERVICE</code>, <code>GLOBUS_XIO_TCP_GET_SERVICE</code>, <code>GLOBUS_XIO_TCP_SET_PORT</code>, <code>GLOBUS_XIO_TCP_GET_PORT</code>, <code>GLOBUS_XIO_TCP_SET_BACKLOG</code>, <code>GLOBUS_XIO_TCP_GET_BACKLOG</code>, <code>GLOBUS_XIO_TCP_SET_LISTEN_RANGE</code>, <code>GLOBUS_XIO_TCP_GET_LISTEN_RANGE</code>, <code>GLOBUS_XIO_TCP_GET_HANDLE</code>, <code>GLOBUS_XIO_TCP_SET_HANDLE</code>, <code>GLOBUS_XIO_TCP_SET_INTERFACE</code>, <code>GLOBUS_XIO_TCP_GET_INTERFACE</code>, <code>GLOBUS_XIO_TCP_SET_RESTRICT_PORT</code>, <code>GLOBUS_XIO_TCP_GET_RESTRICT_PORT</code>, <code>GLOBUS_XIO_TCP_SET_REUSEADDR</code>, <code>GLOBUS_XIO_TCP_GET_REUSEADDR</code>, <code>GLOBUS_XIO_TCP_SET_NO_IPV6</code>, <code>GLOBUS_XIO_TCP_GET_NO_IPV6</code>, <code>GLOBUS_XIO_TCP_SET_CONNECT_RANGE</code>, <code>GLOBUS_XIO_TCP_GET_CONNECT_RANGE</code>, <code>GLOBUS_XIO_TCP_SET_KEEPALIVE</code>, <code>GLOBUS_XIO_TCP_GET_KEEPALIVE</code>, <code>GLOBUS_XIO_TCP_SET_LINGER</code>, <code>GLOBUS_XIO_TCP_GET_LINGER</code>, <code>GLOBUS_XIO_TCP_SET_OOBINLINE</code>, <code>GLOBUS_XIO_TCP_GET_OOBINLINE</code>, <code>GLOBUS_XIO_TCP_SET_SNDBUF</code>, <code>GLOBUS_XIO_TCP_GET_SNDBUF</code>, <code>GLOBUS_XIO_TCP_SET_RCVBUF</code>, <code>GLOBUS_XIO_TCP_GET_RCVBUF</code>, <code>GLOBUS_XIO_TCP_SET_NODELAY</code>, <code>GLOBUS_XIO_TCP_GET_NODELAY</code>, <code>GLOBUS_XIO_TCP_SET_SEND_FLAGS</code>, <code>GLOBUS_XIO_TCP_GET_SEND_FLAGS</code>, <code>GLOBUS_XIO_TCP_GET_LOCAL_CONTACT</code>, <code>GLOBUS_XIO_TCP_GET_LOCAL_NUMERIC_CONTACT</code>, <code>GLOBUS_XIO_TCP_GET_REMOTE_CONTACT</code>, <code>GLOBUS_XIO_TCP_GET_REMOTE_NUMERIC_CONTACT</code>, <code>GLOBUS_XIO_TCP_AFFECT_ATTR_DEFAULTS</code>, <code>GLOBUS_XIO_TCP_SET_BLOCKING_IO</code>, <code>GLOBUS_XIO_TCP_GET_BLOCKING_IO</code> } </p>
<p> enum <code>globus_xio_tcp_send_flags_t</code> { <code>GLOBUS_XIO_TCP_SEND_OOB</code> = MSG_OOB } </p>
<h3>Functions</h3>
<p>globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_TCP_SET_SERVICE</code>, const char *service_name) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_TCP_GET_SERVICE</code>, char **service_name_out) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_TCP_SET_PORT</code>, int listener_port) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_TCP_GET_PORT</code>, int *listener_port_out) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_TCP_SET_BACKLOG</code>, int listener_backlog) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_TCP_GET_BACKLOG</code>, int *listener_backlog_out) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_TCP_SET_LISTEN_RANGE</code>, int listener_min_port, int listener_max_port) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_TCP_GET_LISTEN_RANGE</code>, int *listener_min_port_out, int *listener_max_port_out) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_TCP_GET_HANDLE</code>, globus_xio_system_socket_t *handle_out) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_TCP_GET_HANDLE</code>, globus_xio_system_socket_t *handle_out) </p>
<p> globus_result_t <code>globus_xio_server_cntl</code> (server, driver, <code>GLOBUS_XIO_TCP_GET_HANDLE</code>, globus_xio_system_socket_t *handle_out) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_TCP_SET_HANDLE</code>, globus_xio_system_socket_t handle) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_TCP_SET_INTERFACE</code>, const char *interface) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_TCP_GET_INTERFACE</code>, char **interface_out) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_TCP_SET_RESTRICT_PORT</code>, globus_bool_t restrict_port) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_TCP_GET_RESTRICT_PORT</code>, globus_bool_t *restrict_port_out) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_TCP_SET_REUSEADDR</code>, globus_bool_t resuseaddr) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_TCP_GET_REUSEADDR</code>, globus_bool_t *resuseaddr_out) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_TCP_SET_NO_IPV6</code>, globus_bool_t no_ipv6) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_TCP_GET_NO_IPV6</code>, globus_bool_t *no_ipv6_out) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_TCP_SET_CONNECT_RANGE</code>, int connector_min_port, int connector_max_port) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_TCP_GET_CONNECT_RANGE</code>, int *connector_min_port_out, int *connector_max_port_out) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_TCP_SET_KEEPALIVE</code>, globus_bool_t keepalive) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_TCP_SET_KEEPALIVE</code>, globus_bool_t keepalive) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_TCP_GET_KEEPALIVE</code>, globus_bool_t *keepalive_out) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_TCP_GET_KEEPALIVE</code>, globus_bool_t *keepalive_out) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_TCP_SET_LINGER</code>, globus_bool_t linger, int linger_time) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_TCP_SET_LINGER</code>, globus_bool_t linger, int linger_time) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_TCP_GET_LINGER</code>, globus_bool_t *linger_out, int *linger_time_out) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_TCP_GET_LINGER</code>, globus_bool_t *linger_out, int *linger_time_out) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_TCP_SET_OOBINLINE</code>, globus_bool_t oobinline) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_TCP_SET_OOBINLINE</code>, globus_bool_t oobinline) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_TCP_GET_OOBINLINE</code>, globus_bool_t *oobinline_out) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_TCP_GET_OOBINLINE</code>, globus_bool_t *oobinline_out) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_TCP_SET_SNDBUF</code>, int sndbuf) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_TCP_SET_SNDBUF</code>, int sndbuf) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_TCP_GET_SNDBUF</code>, int *sndbuf_out) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_TCP_GET_SNDBUF</code>, int *sndbuf_out) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_TCP_SET_RCVBUF</code>, int rcvbuf) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_TCP_SET_RCVBUF</code>, int rcvbuf) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_TCP_GET_RCVBUF</code>, int *rcvbuf_out) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_TCP_GET_RCVBUF</code>, int *rcvbuf_out) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_TCP_SET_NODELAY</code>, globus_bool_t nodelay) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_TCP_SET_NODELAY</code>, globus_bool_t nodelay) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_TCP_GET_NODELAY</code>, globus_bool_t *nodelay_out) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_TCP_GET_NODELAY</code>, globus_bool_t *nodelay_out) </p>
<p> globus_result_t <code>globus_xio_data_descriptor_cntl</code> (dd, driver, <code>GLOBUS_XIO_TCP_SET_SEND_FLAGS</code>, int send_flags) </p>
<p> globus_result_t <code>globus_xio_data_descriptor_cntl</code> (dd, driver, <code>GLOBUS_XIO_TCP_GET_SEND_FLAGS</code>, int *send_flags_out) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_TCP_GET_LOCAL_CONTACT</code>, char **contact_string_out) </p>
<p> globus_result_t <code>globus_xio_server_cntl</code> (server, driver, <code>GLOBUS_XIO_TCP_GET_LOCAL_CONTACT</code>, char **contact_string_out) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_TCP_GET_LOCAL_NUMERIC_CONTACT</code>, char **contact_string_out) </p>
<p> globus_result_t <code>globus_xio_server_cntl</code> (server, driver, <code>GLOBUS_XIO_TCP_GET_LOCAL_NUMERIC_CONTACT</code>, char **contact_string_out) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_TCP_GET_REMOTE_CONTACT</code>, char **contact_string_out) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_TCP_GET_REMOTE_NUMERIC_CONTACT</code>, char **contact_string_out) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_TCP_AFFECT_ATTR_DEFAULTS</code>, globus_bool_t affect_global) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_TCP_SET_BLOCKING_IO</code>, globus_bool_t use_blocking_io) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_TCP_SET_BLOCKING_IO</code>, globus_bool_t use_blocking_io) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_TCP_GET_BLOCKING_IO</code>, globus_bool_t *use_blocking_io_out) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_TCP_GET_BLOCKING_IO</code>, globus_bool_t *use_blocking_io_out) </p>
<h2>Detailed Description</h2>
<p>Header file for XIO TCP Driver. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_xio from the source code.</p>
