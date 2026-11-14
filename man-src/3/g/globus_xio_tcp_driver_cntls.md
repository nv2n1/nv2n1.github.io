---
title: "globus_xio_tcp_driver_cntls(3)"
name: "globus_xio_tcp_driver_cntls"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_xio_tcp_driver_cntls/"
description: "Attributes and Cntls –"
---

<h2 class="name">NAME</h2>
<p> Attributes and Cntls &#8211; </p>
<h3>Enumerations</h3>
<p> enum <code>globus_xio_tcp_cmd_t</code> { <code>GLOBUS_XIO_TCP_SET_SERVICE</code>, <code>GLOBUS_XIO_TCP_GET_SERVICE</code>, <code>GLOBUS_XIO_TCP_SET_PORT</code>, <code>GLOBUS_XIO_TCP_GET_PORT</code>, <code>GLOBUS_XIO_TCP_SET_BACKLOG</code>, <code>GLOBUS_XIO_TCP_GET_BACKLOG</code>, <code>GLOBUS_XIO_TCP_SET_LISTEN_RANGE</code>, <code>GLOBUS_XIO_TCP_GET_LISTEN_RANGE</code>, <code>GLOBUS_XIO_TCP_GET_HANDLE</code>, <code>GLOBUS_XIO_TCP_SET_HANDLE</code>, <code>GLOBUS_XIO_TCP_SET_INTERFACE</code>, <code>GLOBUS_XIO_TCP_GET_INTERFACE</code>, <code>GLOBUS_XIO_TCP_SET_RESTRICT_PORT</code>, <code>GLOBUS_XIO_TCP_GET_RESTRICT_PORT</code>, <code>GLOBUS_XIO_TCP_SET_REUSEADDR</code>, <code>GLOBUS_XIO_TCP_GET_REUSEADDR</code>, <code>GLOBUS_XIO_TCP_SET_NO_IPV6</code>, <code>GLOBUS_XIO_TCP_GET_NO_IPV6</code>, <code>GLOBUS_XIO_TCP_SET_CONNECT_RANGE</code>, <code>GLOBUS_XIO_TCP_GET_CONNECT_RANGE</code>, <code>GLOBUS_XIO_TCP_SET_KEEPALIVE</code>, <code>GLOBUS_XIO_TCP_GET_KEEPALIVE</code>, <code>GLOBUS_XIO_TCP_SET_LINGER</code>, <code>GLOBUS_XIO_TCP_GET_LINGER</code>, <code>GLOBUS_XIO_TCP_SET_OOBINLINE</code>, <code>GLOBUS_XIO_TCP_GET_OOBINLINE</code>, <code>GLOBUS_XIO_TCP_SET_SNDBUF</code>, <code>GLOBUS_XIO_TCP_GET_SNDBUF</code>, <code>GLOBUS_XIO_TCP_SET_RCVBUF</code>, <code>GLOBUS_XIO_TCP_GET_RCVBUF</code>, <code>GLOBUS_XIO_TCP_SET_NODELAY</code>, <code>GLOBUS_XIO_TCP_GET_NODELAY</code>, <code>GLOBUS_XIO_TCP_SET_SEND_FLAGS</code>, <code>GLOBUS_XIO_TCP_GET_SEND_FLAGS</code>, <code>GLOBUS_XIO_TCP_GET_LOCAL_CONTACT</code>, <code>GLOBUS_XIO_TCP_GET_LOCAL_NUMERIC_CONTACT</code>, <code>GLOBUS_XIO_TCP_GET_REMOTE_CONTACT</code>, <code>GLOBUS_XIO_TCP_GET_REMOTE_NUMERIC_CONTACT</code>, <code>GLOBUS_XIO_TCP_AFFECT_ATTR_DEFAULTS</code>, <code>GLOBUS_XIO_TCP_SET_BLOCKING_IO</code>, <code>GLOBUS_XIO_TCP_GET_BLOCKING_IO</code> } </p>
<h3>Functions</h3>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_TCP_SET_SERVICE</code>, const char *service_name) </p>
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
<p> Tcp driver specific attrs and cntls. </p>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_xio_attr_cntl()</code> </p>
<p> <code>globus_xio_handle_cntl()</code> </p>
<p> <code>globus_xio_server_cntl()</code> </p>
<p> <code>globus_xio_data_descriptor_cntl()</code></dl>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>globus_xio_tcp_cmd_t</code></h3>
<p> doxygen varargs filter stuff TCP driver specific cntls </p>
<p> <code>Enumerator</code></p>
<dl>
<dt><i>GLOBUS_XIO_TCP_SET_SERVICE </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_TCP_GET_SERVICE </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_TCP_SET_PORT </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_TCP_GET_PORT </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_TCP_SET_BACKLOG </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_TCP_GET_BACKLOG </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_TCP_SET_LISTEN_RANGE </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_TCP_GET_LISTEN_RANGE </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_TCP_GET_HANDLE </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code>, <code>globus_xio_handle_cntl </code>, <code>globus_xio_server_cntl </code></p>
<dt><i>GLOBUS_XIO_TCP_SET_HANDLE </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_TCP_SET_INTERFACE </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_TCP_GET_INTERFACE </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_TCP_SET_RESTRICT_PORT </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_TCP_GET_RESTRICT_PORT </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_TCP_SET_REUSEADDR </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_TCP_GET_REUSEADDR </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_TCP_SET_NO_IPV6 </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_TCP_GET_NO_IPV6 </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_TCP_SET_CONNECT_RANGE </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_TCP_GET_CONNECT_RANGE </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_TCP_SET_KEEPALIVE </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code>, <code>globus_xio_handle_cntl </code></p>
<dt><i>GLOBUS_XIO_TCP_GET_KEEPALIVE </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code>, <code>globus_xio_handle_cntl </code></p>
<dt><i>GLOBUS_XIO_TCP_SET_LINGER </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code>, <code>globus_xio_handle_cntl </code></p>
<dt><i>GLOBUS_XIO_TCP_GET_LINGER </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code>, <code>globus_xio_handle_cntl </code></p>
<dt><i>GLOBUS_XIO_TCP_SET_OOBINLINE </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code>, <code>globus_xio_handle_cntl </code></p>
<dt><i>GLOBUS_XIO_TCP_GET_OOBINLINE </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code>, <code>globus_xio_handle_cntl </code></p>
<dt><i>GLOBUS_XIO_TCP_SET_SNDBUF </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code>, <code>globus_xio_handle_cntl </code></p>
<dt><i>GLOBUS_XIO_TCP_GET_SNDBUF </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code>, <code>globus_xio_handle_cntl </code></p>
<dt><i>GLOBUS_XIO_TCP_SET_RCVBUF </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code>, <code>globus_xio_handle_cntl </code></p>
<dt><i>GLOBUS_XIO_TCP_GET_RCVBUF </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code>, <code>globus_xio_handle_cntl </code></p>
<dt><i>GLOBUS_XIO_TCP_SET_NODELAY </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code>, <code>globus_xio_handle_cntl </code></p>
<dt><i>GLOBUS_XIO_TCP_GET_NODELAY </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code>, <code>globus_xio_handle_cntl </code></p>
<dt><i>GLOBUS_XIO_TCP_SET_SEND_FLAGS </i></p>
<dd> See usage for: <code>globus_xio_data_descriptor_cntl </code></p>
<dt><i>GLOBUS_XIO_TCP_GET_SEND_FLAGS </i></p>
<dd> See usage for: <code>globus_xio_data_descriptor_cntl </code></p>
<dt><i>GLOBUS_XIO_TCP_GET_LOCAL_CONTACT </i></p>
<dd> See usage for: <code>globus_xio_handle_cntl </code>, <code>globus_xio_server_cntl </code></p>
<dt><i>GLOBUS_XIO_TCP_GET_LOCAL_NUMERIC_CONTACT </i></p>
<dd> See usage for: <code>globus_xio_handle_cntl </code>, <code>globus_xio_server_cntl </code></p>
<dt><i>GLOBUS_XIO_TCP_GET_REMOTE_CONTACT </i></p>
<dd> See usage for: <code>globus_xio_handle_cntl </code></p>
<dt><i>GLOBUS_XIO_TCP_GET_REMOTE_NUMERIC_CONTACT </i></p>
<dd> See usage for: <code>globus_xio_handle_cntl </code></p>
<dt><i>GLOBUS_XIO_TCP_AFFECT_ATTR_DEFAULTS </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_TCP_SET_BLOCKING_IO </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code>, <code>globus_xio_handle_cntl </code></p>
<dt><i>GLOBUS_XIO_TCP_GET_BLOCKING_IO </i></p>
<dd> See usage for: <code>globus_xio_attr_cntl </code>, <code>globus_xio_handle_cntl </code></dl>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_TCP_SET_SERVICE</code>, const char *service_name)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the tcp service name to bind to. </p>
<p> Used only on attrs for <code>globus_xio_server_create()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>service_name</i> The service name to use when setting up the listener. If the service name cannot be resolved, the port (if one is set) will be used instead.</dl>
<p> string opt: port=<i>string</i></p>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_TCP_GET_SERVICE</code>, char **service_name_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the tcp service name to bind to. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>service_name_out</i> A pointer to the service name will be stored here If none is set, NULL will be passed back. Otherwise, the name will be duplicated with strdup() and the user should call free() on it.</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_TCP_SET_PORT</code>, intlistener_port)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the tcp port number to bind to. </p>
<p> Used only on attrs for <code>globus_xio_server_create()</code>. The default port number is 0 (system assigned) </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>listener_port</i> The port number to use when setting up the listener. If the service name is also set, this will only be used if that can&#8217;t be resolved.</dl>
<p> string opt: port=<i>int</i></p>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_TCP_GET_PORT</code>, int *listener_port_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the tcp port number to bind to. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>listener_port_out</i> The port will be stored here.</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_TCP_SET_BACKLOG</code>, intlistener_backlog)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the listener backlog on a server. </p>
<p> Used only on attrs for <code>globus_xio_server_create()</code>. The default backlog is -1 (system maximum) </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>listener_backlog</i> This indicates the maximum length of the system&#8217;s queue of pending connections. Any connection attempts when the queue is full will fail. If backlog is equal to -1, then the system-specific maximum queue length will be used.</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_TCP_GET_BACKLOG</code>, int *listener_backlog_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the listener backlog on an attr. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>listener_backlog_out</i> The backlog will be stored here.</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_TCP_SET_LISTEN_RANGE</code>, intlistener_min_port, intlistener_max_port)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the tcp port range to confine the server to. </p>
<p> Used only on attrs for <code>globus_xio_server_create()</code> where no specific service or port has been set. It overrides the range set in the GLOBUS_TCP_PORT_RANGE env variable. If &#8216;restrict port&#8217; is true, the server&#8217;s listening port will be constrained to the range specified. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>listener_min_port</i> The lower bound on the listener port. (default 0 &#8212; no bound)<br />
 <i>listener_max_port</i> The upper bound on the listener port. (default 0 &#8212; no bound)</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>GLOBUS_XIO_TCP_SET_RESTRICT_PORT</code></dl>
<p> string opt: listen_range=<i>int</i>,<i>int</i></p>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_TCP_GET_LISTEN_RANGE</code>, int *listener_min_port_out, int *listener_max_port_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the tcp port range on an attr. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>listener_min_port_out</i> The lower bound will be stored here.<br />
 <i>listener_max_port_out</i> The upper bound will be stored here.</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_TCP_GET_HANDLE</code>, globus_xio_system_socket_t *handle_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the tcp socket handle on an attr, handle, or server. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle_out</i> The tcp socket will be stored here. If none is set, GLOBUS_XIO_TCP_INVALID_HANDLE will be set.</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_TCP_SET_HANDLE</code>, globus_xio_system_socket_thandle)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the tcp socket to use for a handle or server. </p>
<p> Used only on attrs for <code>globus_xio_server_create()</code> or <code>globus_xio_register_open()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> Use this handle (fd or SOCKET) for the listener or connection. Note: close() will not be called on this handle.</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_TCP_SET_INTERFACE</code>, const char *interface)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the interface to bind a listener or connection to. </p>
<p> Used only on attrs for <code>globus_xio_server_create()</code> or <code>globus_xio_register_open</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>interface</i> The interface to use. Can be a hostname or numeric IP</dl>
<p> string opt: iface=<i>string</i></p>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_TCP_GET_INTERFACE</code>, char **interface_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the interface on the attr. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>interface_out</i> A pointer to the interface will be stored here If one is set, NULL will be passed back. Otherwise, the interface will be duplicated with strdup() and the user should call free() on it.</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_TCP_SET_RESTRICT_PORT</code>, globus_bool_trestrict_port)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Enable or disable the listener or connector range constraints. </p>
<p> Used only on attrs for <code>globus_xio_server_create()</code> or <code>globus_xio_register_open()</code>. This enables or ignores the port range found in the attr or in then env. By default, those ranges are enabled. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>restrict_port</i> GLOBUS_TRUE to enable (default), GLOBUS_FALSE to disable.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>GLOBUS_XIO_TCP_SET_LISTEN_RANGE</code> </p>
<p> <code>GLOBUS_XIO_TCP_SET_CONNECT_RANGE</code></dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_TCP_GET_RESTRICT_PORT</code>, globus_bool_t *restrict_port_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the restrict port flag. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>restrict_port_out</i> The restrict port flag will be stored here.</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_TCP_SET_REUSEADDR</code>, globus_bool_tresuseaddr)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Reuse addr when binding. </p>
<p> Used only on attrs for <code>globus_xio_server_create()</code> or <code>globus_xio_register_open()</code> to determine whether or not to allow reuse of addresses when binding a socket to a port number. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>resuseaddr</i> GLOBUS_TRUE to allow, GLOBUS_FALSE to disallow (default)</dl>
<p> string opt: reuse=<i>bool</i></p>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_TCP_GET_REUSEADDR</code>, globus_bool_t *resuseaddr_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the reuseaddr flag on an attr. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>resuseaddr_out</i> The reuseaddr flag will be stored here.</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_TCP_SET_NO_IPV6</code>, globus_bool_tno_ipv6)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Restrict to IPV4 only. </p>
<p> Used only on attrs for <code>globus_xio_server_create()</code> or <code>globus_xio_register_open()</code>. Disallow IPV6 sockets from being used (default is to use either ipv4 or ipv6) </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>no_ipv6</i> GLOBUS_TRUE to disallow ipv6, GLOBUS_FALSE to allow (default)</dl>
<p> string opt: noipv6=<i>bool</i></p>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_TCP_GET_NO_IPV6</code>, globus_bool_t *no_ipv6_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the no ipv6 flag on an attr. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>no_ipv6_out</i> The no ipv6 flag will be stored here.</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_TCP_SET_CONNECT_RANGE</code>, intconnector_min_port, intconnector_max_port)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the tcp port range to confine the server to. </p>
<p> Used only on attrs for <code>globus_xio_register_open()</code>. It overrides the range set in the GLOBUS_TCP_SOURCE_RANGE env variable. If &#8216;restrict port&#8217; is true, the connecting socket&#8217;s local port will be constrained to the range specified. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>connector_min_port</i> The lower bound on the listener port. (default 0 &#8212; no bound)<br />
 <i>connector_max_port</i> The upper bound on the listener port. (default 0 &#8212; no bound)</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>GLOBUS_XIO_TCP_SET_RESTRICT_PORT</code></dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_TCP_GET_CONNECT_RANGE</code>, int *connector_min_port_out, int *connector_max_port_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the tcp source port range on an attr. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>connector_min_port_out</i> The lower bound will be stored here.<br />
 <i>connector_max_port_out</i> The upper bound will be stored here.</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_TCP_SET_KEEPALIVE</code>, globus_bool_tkeepalive)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Enable tcp keepalive. </p>
<p> Used on attrs for <code>globus_xio_server_create()</code>, <code>globus_xio_register_open()</code> and with <code>globus_xio_handle_cntl()</code> to determine whether or not to periodically send &#8216;keepalive&#8217; messages on a connected socket handle. This may enable earlier detection of broken connections. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>keepalive</i> GLOBUS_TRUE to enable, GLOBUS_FALSE to disable (default)</dl>
<p> string opt: keepalive=<i>bool</i></p>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_TCP_GET_KEEPALIVE</code>, globus_bool_t *keepalive_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the tcp keepalive flag. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>keepalive_out</i> The tcp keepalive flag will be stored here.</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_TCP_SET_LINGER</code>, globus_bool_tlinger, intlinger_time)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set tcp linger. </p>
<p> Used on attrs for <code>globus_xio_server_create()</code>, <code>globus_xio_register_open()</code> and with <code>globus_xio_handle_cntl()</code> to determine what to do when data is in the socket&#8217;s buffer when the socket is closed. If linger is set to true, then the close operation will block until the socket buffers are empty, or the linger_time has expired. If this is enabled, any data remaining after the linger time has expired, will be discarded. If this is disabled, close finishes immediately, but the OS will still attempt to transmit the remaining data. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>linger</i> GLOBUS_TRUE to enable, GLOBUS_FALSE to disable (default)<br />
 <i>linger_time</i> The time (in seconds) to block at close time if linger is true and data is queued in the socket buffer.</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_TCP_GET_LINGER</code>, globus_bool_t *linger_out, int *linger_time_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the tcp linger flag and time. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>linger_out</i> The linger flag will be stored here.<br />
 <i>linger_time_out</i> The linger time will be set here.</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_TCP_SET_OOBINLINE</code>, globus_bool_toobinline)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Receive out of band data (tcp urgent data) in normal stream. </p>
<p> Used on attrs for <code>globus_xio_server_create()</code>, <code>globus_xio_register_open()</code> and with <code>globus_xio_handle_cntl()</code> to choose whether out-of-band data is received in the normal data queue. (Currently, there is no other way to receive OOB data) </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>oobinline</i> GLOBUS_TRUE to enable, GLOBUS_FALSE to disable (default)</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_TCP_GET_OOBINLINE</code>, globus_bool_t *oobinline_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the oobinline flag. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>oobinline_out</i> The oobinline flag will be stored here.</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_TCP_SET_SNDBUF</code>, intsndbuf)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the tcp socket send buffer size. </p>
<p> Used on attrs for <code>globus_xio_server_create()</code>, <code>globus_xio_register_open()</code> and with <code>globus_xio_handle_cntl()</code> to set the size of the send buffer used on the socket. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sndbuf</i> The send buffer size in bytes to use. (default is system specific)</dl>
<p> string opt: sndbuf=<i>formatted int</i></p>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_TCP_GET_SNDBUF</code>, int *sndbuf_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the tcp send buffer size on the attr or handle. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sndbuf_out</i> The send buffer size will be stored here.</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_TCP_SET_RCVBUF</code>, intrcvbuf)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the tcp socket receive buffer size. </p>
<p> Used on attrs for <code>globus_xio_server_create()</code>, <code>globus_xio_register_open()</code> and with <code>globus_xio_handle_cntl()</code> to set the size of the receive buffer used on the socket. The receive buffer size is often used by the operating system to choose the appropriate TCP window size. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>rcvbuf</i> The receive buffer size in bytes. (default is system specific)</dl>
<p> string opt: rcvbuf=<i>formatted int</i></p>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_TCP_GET_RCVBUF</code>, int *rcvbuf_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the tcp receive buffer size on the attr or handle. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>rcvbuf_out</i> The receive buffer size will be stored here.</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_TCP_SET_NODELAY</code>, globus_bool_tnodelay)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Disable Nagle&#8217;s algorithm. </p>
<p> Used on attrs for <code>globus_xio_server_create()</code>, <code>globus_xio_register_open()</code> and with <code>globus_xio_handle_cntl()</code> to determine whether or not to disable Nagle&#8217;s algorithm. If set to GLOBUS_TRUE, the socket will send packets as soon as possible with no unnecessary delays introduced. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>nodelay</i> GLOBUS_TRUE to disable nagle, GLOBUS_FALSE to enable (default)</dl>
<p> string opt: nodelay=<i>bool</i></p>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_TCP_GET_NODELAY</code>, globus_bool_t *nodelay_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the tcp nodelay flag. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>nodelay_out</i> The no delay flag will be stored here.</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_TCP_AFFECT_ATTR_DEFAULTS</code>, globus_bool_taffect_global)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Change the default attr values. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>affect_global</i> If GLOBUS_TRUE, any future cntls on this attr will access the global default attr (which all new attrs are initialized from) The default is GLOBUS_FALSE. Note: this should only be used at the application level and there should only be one. There is no mutex protecting the global attr. This feature should not be abused. There are some attrs that make no sense to change globally. Attrs that do include the tcp port range stuff, socket buffer sizes, etc.</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_TCP_SET_BLOCKING_IO</code>, globus_bool_tuse_blocking_io)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Enable true blocking io when making globus_xio_read/write() calls. Note: use with caution. you can deadlock an entire app with this. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>use_blocking_io</i> If GLOBUS_TRUE, true blocking io will be enabled. GLOBUS_FALSE will disable it (default);</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_TCP_GET_BLOCKING_IO</code>, globus_bool_t *use_blocking_io_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the blocking io status in use or in attr. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>use_blocking_io_out</i> The flag will be set here. GLOBUS_TRUE for enabled.</dl>
<h3>globus_result_t globus_xio_data_descriptor_cntl (dd, driver, <code>GLOBUS_XIO_TCP_SET_SEND_FLAGS</code>, intsend_flags)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set tcp send flags. </p>
<p> Used only for data descriptors to write calls. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>send_flags</i> The flags to use when sending data.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_xio_tcp_send_flags_t</code></dl>
<h3>globus_result_t globus_xio_data_descriptor_cntl (dd, driver, <code>GLOBUS_XIO_TCP_GET_SEND_FLAGS</code>, int *send_flags_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get tcp send flags. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>send_flags_out</i> The flags to use will be stored here.</dl>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, <code>GLOBUS_XIO_TCP_GET_HANDLE</code>, globus_xio_system_socket_t *handle_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the tcp socket handle on an attr, handle, or server. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle_out</i> The tcp socket will be stored here. If none is set, GLOBUS_XIO_TCP_INVALID_HANDLE will be set.</dl>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, <code>GLOBUS_XIO_TCP_SET_KEEPALIVE</code>, globus_bool_tkeepalive)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Enable tcp keepalive. </p>
<p> Used on attrs for <code>globus_xio_server_create()</code>, <code>globus_xio_register_open()</code> and with <code>globus_xio_handle_cntl()</code> to determine whether or not to periodically send &#8216;keepalive&#8217; messages on a connected socket handle. This may enable earlier detection of broken connections. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>keepalive</i> GLOBUS_TRUE to enable, GLOBUS_FALSE to disable (default)</dl>
<p> string opt: keepalive=<i>bool</i></p>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, <code>GLOBUS_XIO_TCP_GET_KEEPALIVE</code>, globus_bool_t *keepalive_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the tcp keepalive flag. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>keepalive_out</i> The tcp keepalive flag will be stored here.</dl>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, <code>GLOBUS_XIO_TCP_SET_LINGER</code>, globus_bool_tlinger, intlinger_time)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set tcp linger. </p>
<p> Used on attrs for <code>globus_xio_server_create()</code>, <code>globus_xio_register_open()</code> and with <code>globus_xio_handle_cntl()</code> to determine what to do when data is in the socket&#8217;s buffer when the socket is closed. If linger is set to true, then the close operation will block until the socket buffers are empty, or the linger_time has expired. If this is enabled, any data remaining after the linger time has expired, will be discarded. If this is disabled, close finishes immediately, but the OS will still attempt to transmit the remaining data. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>linger</i> GLOBUS_TRUE to enable, GLOBUS_FALSE to disable (default)<br />
 <i>linger_time</i> The time (in seconds) to block at close time if linger is true and data is queued in the socket buffer.</dl>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, <code>GLOBUS_XIO_TCP_GET_LINGER</code>, globus_bool_t *linger_out, int *linger_time_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the tcp linger flag and time. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>linger_out</i> The linger flag will be stored here.<br />
 <i>linger_time_out</i> The linger time will be set here.</dl>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, <code>GLOBUS_XIO_TCP_SET_OOBINLINE</code>, globus_bool_toobinline)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Receive out of band data (tcp urgent data) in normal stream. </p>
<p> Used on attrs for <code>globus_xio_server_create()</code>, <code>globus_xio_register_open()</code> and with <code>globus_xio_handle_cntl()</code> to choose whether out-of-band data is received in the normal data queue. (Currently, there is no other way to receive OOB data) </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>oobinline</i> GLOBUS_TRUE to enable, GLOBUS_FALSE to disable (default)</dl>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, <code>GLOBUS_XIO_TCP_GET_OOBINLINE</code>, globus_bool_t *oobinline_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the oobinline flag. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>oobinline_out</i> The oobinline flag will be stored here.</dl>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, <code>GLOBUS_XIO_TCP_SET_SNDBUF</code>, intsndbuf)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the tcp socket send buffer size. </p>
<p> Used on attrs for <code>globus_xio_server_create()</code>, <code>globus_xio_register_open()</code> and with <code>globus_xio_handle_cntl()</code> to set the size of the send buffer used on the socket. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sndbuf</i> The send buffer size in bytes to use. (default is system specific)</dl>
<p> string opt: sndbuf=<i>formatted int</i></p>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, <code>GLOBUS_XIO_TCP_GET_SNDBUF</code>, int *sndbuf_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the tcp send buffer size on the attr or handle. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sndbuf_out</i> The send buffer size will be stored here.</dl>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, <code>GLOBUS_XIO_TCP_SET_RCVBUF</code>, intrcvbuf)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the tcp socket receive buffer size. </p>
<p> Used on attrs for <code>globus_xio_server_create()</code>, <code>globus_xio_register_open()</code> and with <code>globus_xio_handle_cntl()</code> to set the size of the receive buffer used on the socket. The receive buffer size is often used by the operating system to choose the appropriate TCP window size. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>rcvbuf</i> The receive buffer size in bytes. (default is system specific)</dl>
<p> string opt: rcvbuf=<i>formatted int</i></p>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, <code>GLOBUS_XIO_TCP_GET_RCVBUF</code>, int *rcvbuf_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the tcp receive buffer size on the attr or handle. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>rcvbuf_out</i> The receive buffer size will be stored here.</dl>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, <code>GLOBUS_XIO_TCP_SET_NODELAY</code>, globus_bool_tnodelay)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Disable Nagle&#8217;s algorithm. </p>
<p> Used on attrs for <code>globus_xio_server_create()</code>, <code>globus_xio_register_open()</code> and with <code>globus_xio_handle_cntl()</code> to determine whether or not to disable Nagle&#8217;s algorithm. If set to GLOBUS_TRUE, the socket will send packets as soon as possible with no unnecessary delays introduced. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>nodelay</i> GLOBUS_TRUE to disable nagle, GLOBUS_FALSE to enable (default)</dl>
<p> string opt: nodelay=<i>bool</i></p>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, <code>GLOBUS_XIO_TCP_GET_NODELAY</code>, globus_bool_t *nodelay_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the tcp nodelay flag. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>nodelay_out</i> The no delay flag will be stored here.</dl>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, <code>GLOBUS_XIO_TCP_GET_LOCAL_CONTACT</code>, char **contact_string_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get local socket info. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>contact_string_out</i> A pointer to a contact string for the local end of a connected socket or listener will be stored here. The user should free() it when done with it. It will be in the format: &lt;hostname&gt;:&lt;port&gt;</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_xio_server_get_contact_string()</code> </p>
<p> <code>GLOBUS_XIO_GET_LOCAL_CONTACT</code></dl>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, <code>GLOBUS_XIO_TCP_GET_LOCAL_NUMERIC_CONTACT</code>, char **contact_string_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get local socket info. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>contact_string_out</i> A pointer to a contact string for the local end of a connected socket or listener will be stored here. The user should free() it when done with it. It will be in the format: &lt;ip&gt;:&lt;port&gt;</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>GLOBUS_XIO_GET_LOCAL_NUMERIC_CONTACT</code></dl>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, <code>GLOBUS_XIO_TCP_GET_REMOTE_CONTACT</code>, char **contact_string_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get remote socket info. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>contact_string_out</i> A pointer to a contact string for the remote end of a connected socket will be stored here. The user should free() it when done with it. It will be in the format: &lt;hostname&gt;:&lt;port&gt;</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>GLOBUS_XIO_GET_REMOTE_CONTACT</code></dl>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, <code>GLOBUS_XIO_TCP_GET_REMOTE_NUMERIC_CONTACT</code>, char **contact_string_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get remote socket info. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>contact_string_out</i> A pointer to a contact string for the remote end of a connected socket will be stored here. The user should free() it when done with it. It will be in the format: &lt;ip&gt;:&lt;port&gt;</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>GLOBUS_XIO_GET_REMOTE_NUMERIC_CONTACT</code></dl>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, <code>GLOBUS_XIO_TCP_SET_BLOCKING_IO</code>, globus_bool_tuse_blocking_io)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Enable true blocking io when making globus_xio_read/write() calls. Note: use with caution. you can deadlock an entire app with this. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>use_blocking_io</i> If GLOBUS_TRUE, true blocking io will be enabled. GLOBUS_FALSE will disable it (default);</dl>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, <code>GLOBUS_XIO_TCP_GET_BLOCKING_IO</code>, globus_bool_t *use_blocking_io_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the blocking io status in use or in attr. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>use_blocking_io_out</i> The flag will be set here. GLOBUS_TRUE for enabled.</dl>
<h3>globus_result_t globus_xio_server_cntl (server, driver, <code>GLOBUS_XIO_TCP_GET_HANDLE</code>, globus_xio_system_socket_t *handle_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the tcp socket handle on an attr, handle, or server. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle_out</i> The tcp socket will be stored here. If none is set, GLOBUS_XIO_TCP_INVALID_HANDLE will be set.</dl>
<h3>globus_result_t globus_xio_server_cntl (server, driver, <code>GLOBUS_XIO_TCP_GET_LOCAL_CONTACT</code>, char **contact_string_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get local socket info. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>contact_string_out</i> A pointer to a contact string for the local end of a connected socket or listener will be stored here. The user should free() it when done with it. It will be in the format: &lt;hostname&gt;:&lt;port&gt;</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_xio_server_get_contact_string()</code> </p>
<p> <code>GLOBUS_XIO_GET_LOCAL_CONTACT</code></dl>
<h3>globus_result_t globus_xio_server_cntl (server, driver, <code>GLOBUS_XIO_TCP_GET_LOCAL_NUMERIC_CONTACT</code>, char **contact_string_out)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get local socket info. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>contact_string_out</i> A pointer to a contact string for the local end of a connected socket or listener will be stored here. The user should free() it when done with it. It will be in the format: &lt;ip&gt;:&lt;port&gt;</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>GLOBUS_XIO_GET_LOCAL_NUMERIC_CONTACT</code></dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_xio from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAH">Function Documentation</a></p>
<dd>
<dt><a href="#lbCP">Author</a></p>
<dd></dl>
