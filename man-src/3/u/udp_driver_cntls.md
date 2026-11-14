---
title: "udp_driver_cntls(3)"
name: "udp_driver_cntls"
section: "3"
letter: "u"
url: "/docs/linux/man/3-udp_driver_cntls/"
description: "Attributes and Cntls –"
---

<p>Attributes and Cntls &#8211; </p>
<p> UDP driver specific attrs and cntls.</p>
<h3>Enumerations</h3>
<p>enum <code>globus_xio_udp_cmd_t</code> { <code>GLOBUS_XIO_UDP_SET_HANDLE</code>, <code>GLOBUS_XIO_UDP_SET_SERVICE</code>, <code>GLOBUS_XIO_UDP_GET_SERVICE</code>, <code>GLOBUS_XIO_UDP_SET_PORT</code>, <code>GLOBUS_XIO_UDP_GET_PORT</code>, <code>GLOBUS_XIO_UDP_SET_LISTEN_RANGE</code>, <code>GLOBUS_XIO_UDP_GET_LISTEN_RANGE</code>, <code>GLOBUS_XIO_UDP_SET_INTERFACE</code>, <code>GLOBUS_XIO_UDP_GET_INTERFACE</code>, <code>GLOBUS_XIO_UDP_SET_RESTRICT_PORT</code>, <code>GLOBUS_XIO_UDP_GET_RESTRICT_PORT</code>, <code>GLOBUS_XIO_UDP_SET_REUSEADDR</code>, <code>GLOBUS_XIO_UDP_GET_REUSEADDR</code>, <code>GLOBUS_XIO_UDP_SET_NO_IPV6</code>, <code>GLOBUS_XIO_UDP_GET_NO_IPV6</code>, <code>GLOBUS_XIO_UDP_GET_HANDLE</code>, <code>GLOBUS_XIO_UDP_SET_SNDBUF</code>, <code>GLOBUS_XIO_UDP_GET_SNDBUF</code>, <code>GLOBUS_XIO_UDP_SET_RCVBUF</code>, <code>GLOBUS_XIO_UDP_GET_RCVBUF</code>, <code>GLOBUS_XIO_UDP_GET_CONTACT</code>, <code>GLOBUS_XIO_UDP_GET_NUMERIC_CONTACT</code>, <code>GLOBUS_XIO_UDP_SET_CONTACT</code>, <code>GLOBUS_XIO_UDP_CONNECT</code>, <code>GLOBUS_XIO_UDP_SET_MULTICAST</code> }</p>
<h3>Functions</h3>
<p>globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, GLOBUS_XIO_UDP_SET_HANDLE, globus_xio_system_socket_t handle) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, GLOBUS_XIO_UDP_SET_SERVICE, const char *service_name) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, GLOBUS_XIO_UDP_GET_SERVICE, char **service_name_out) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, GLOBUS_XIO_UDP_SET_PORT, int listener_port) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, GLOBUS_XIO_UDP_GET_PORT, int *listener_port_out) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, GLOBUS_XIO_UDP_SET_LISTEN_RANGE, int listener_min_port, int listener_max_port) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, GLOBUS_XIO_UDP_GET_LISTEN_RANGE, int *listener_min_port_out, int *listener_max_port_out) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, GLOBUS_XIO_UDP_SET_INTERFACE, const char *interface) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, GLOBUS_XIO_UDP_GET_INTERFACE, char **interface_out) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, GLOBUS_XIO_UDP_SET_RESTRICT_PORT, globus_bool_t restrict_port) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, GLOBUS_XIO_UDP_GET_RESTRICT_PORT, globus_bool_t *restrict_port_out) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, GLOBUS_XIO_UDP_SET_REUSEADDR, globus_bool_t resuseaddr) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, GLOBUS_XIO_UDP_GET_REUSEADDR, globus_bool_t *resuseaddr_out) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, GLOBUS_XIO_UDP_SET_NO_IPV6, globus_bool_t no_ipv6) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, GLOBUS_XIO_UDP_GET_NO_IPV6, globus_bool_t *no_ipv6_out) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, GLOBUS_XIO_UDP_GET_HANDLE, globus_xio_system_socket_t *handle_out) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, GLOBUS_XIO_UDP_GET_HANDLE, globus_xio_system_socket_t *handle_out) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, GLOBUS_XIO_UDP_SET_SNDBUF, int sndbuf) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, GLOBUS_XIO_UDP_SET_SNDBUF, int sndbuf) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, GLOBUS_XIO_UDP_GET_SNDBUF, int *sndbuf_out) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, GLOBUS_XIO_UDP_GET_SNDBUF, int *sndbuf_out) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, GLOBUS_XIO_UDP_SET_RCVBUF, int rcvbuf) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, GLOBUS_XIO_UDP_SET_RCVBUF, int rcvbuf) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, GLOBUS_XIO_UDP_GET_RCVBUF, int *rcvbuf_out) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, GLOBUS_XIO_UDP_GET_RCVBUF, int *rcvbuf_out) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, GLOBUS_XIO_UDP_GET_CONTACT, char **contact_string_out) </p>
<p> globus_result_t <code>globus_xio_data_descriptor_cntl</code> (dd, driver, GLOBUS_XIO_UDP_GET_CONTACT, char **contact_string_out) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, GLOBUS_XIO_UDP_GET_NUMERIC_CONTACT, char **contact_string_out) </p>
<p> globus_result_t <code>globus_xio_data_descriptor_cntl</code> (dd, driver, GLOBUS_XIO_UDP_GET_NUMERIC_CONTACT, char **contact_string_out) </p>
<p> globus_result_t <code>globus_xio_data_descriptor_cntl</code> (dd, driver, GLOBUS_XIO_UDP_SET_CONTACT, char *contact_string) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, GLOBUS_XIO_UDP_CONNECT, char *contact_string) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, GLOBUS_XIO_UDP_SET_MULTICAST, char *contact_string)</p>
<h2>Detailed Description</h2>
<p>UDP driver specific attrs and cntls. </p>
<p> <code>See also:</code></p>
<dl>
<dd><code>globus_xio_attr_cntl()</code> </p>
<p> <code>globus_xio_handle_cntl()</code> </p>
<p> <code>globus_xio_data_descriptor_cntl()</code></dl>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>globus_xio_udp_cmd_t</code></h3>
<p>doxygen varargs filter stuff UDP driver specific cntls </p>
<p> <code>Enumerator: </code></p>
<dl>
<dt><i>GLOBUS_XIO_UDP_SET_HANDLE </i></p>
<dd>See usage for: <code>globus_xio_attr_cntl </code>.</p>
<dt><i>GLOBUS_XIO_UDP_SET_SERVICE </i></p>
<dd>See usage for: <code>globus_xio_attr_cntl </code>.</p>
<dt><i>GLOBUS_XIO_UDP_GET_SERVICE </i></p>
<dd>See usage for: <code>globus_xio_attr_cntl </code>.</p>
<dt><i>GLOBUS_XIO_UDP_SET_PORT </i></p>
<dd>See usage for: <code>globus_xio_attr_cntl </code>.</p>
<dt><i>GLOBUS_XIO_UDP_GET_PORT </i></p>
<dd>See usage for: <code>globus_xio_attr_cntl </code>.</p>
<dt><i>GLOBUS_XIO_UDP_SET_LISTEN_RANGE </i></p>
<dd>See usage for: <code>globus_xio_attr_cntl </code>.</p>
<dt><i>GLOBUS_XIO_UDP_GET_LISTEN_RANGE </i></p>
<dd>See usage for: <code>globus_xio_attr_cntl </code>.</p>
<dt><i>GLOBUS_XIO_UDP_SET_INTERFACE </i></p>
<dd>See usage for: <code>globus_xio_attr_cntl </code>.</p>
<dt><i>GLOBUS_XIO_UDP_GET_INTERFACE </i></p>
<dd>See usage for: <code>globus_xio_attr_cntl </code>.</p>
<dt><i>GLOBUS_XIO_UDP_SET_RESTRICT_PORT </i></p>
<dd>See usage for: <code>globus_xio_attr_cntl </code>.</p>
<dt><i>GLOBUS_XIO_UDP_GET_RESTRICT_PORT </i></p>
<dd>See usage for: <code>globus_xio_attr_cntl </code>.</p>
<dt><i>GLOBUS_XIO_UDP_SET_REUSEADDR </i></p>
<dd>See usage for: <code>globus_xio_attr_cntl </code>.</p>
<dt><i>GLOBUS_XIO_UDP_GET_REUSEADDR </i></p>
<dd>See usage for: <code>globus_xio_attr_cntl </code>.</p>
<dt><i>GLOBUS_XIO_UDP_SET_NO_IPV6 </i></p>
<dd>See usage for: <code>globus_xio_attr_cntl </code>.</p>
<dt><i>GLOBUS_XIO_UDP_GET_NO_IPV6 </i></p>
<dd>See usage for: <code>globus_xio_attr_cntl </code>.</p>
<dt><i>GLOBUS_XIO_UDP_GET_HANDLE </i></p>
<dd>See usage for: <code>globus_xio_attr_cntl </code>, <code>globus_xio_handle_cntl </code>.</p>
<dt><i>GLOBUS_XIO_UDP_SET_SNDBUF </i></p>
<dd>See usage for: <code>globus_xio_attr_cntl </code>, <code>globus_xio_handle_cntl </code>.</p>
<dt><i>GLOBUS_XIO_UDP_GET_SNDBUF </i></p>
<dd>See usage for: <code>globus_xio_attr_cntl </code>, <code>globus_xio_handle_cntl </code>.</p>
<dt><i>GLOBUS_XIO_UDP_SET_RCVBUF </i></p>
<dd>See usage for: <code>globus_xio_attr_cntl </code>, <code>globus_xio_handle_cntl </code>.</p>
<dt><i>GLOBUS_XIO_UDP_GET_RCVBUF </i></p>
<dd>See usage for: <code>globus_xio_attr_cntl </code>, <code>globus_xio_handle_cntl </code>.</p>
<dt><i>GLOBUS_XIO_UDP_GET_CONTACT </i></p>
<dd>See usage for: <code>globus_xio_handle_cntl </code>, <code>globus_xio_data_descriptor_cntl </code>.</p>
<dt><i>GLOBUS_XIO_UDP_GET_NUMERIC_CONTACT </i></p>
<dd>See usage for: <code>globus_xio_handle_cntl </code>, <code>globus_xio_data_descriptor_cntl </code>.</p>
<dt><i>GLOBUS_XIO_UDP_SET_CONTACT </i></p>
<dd>See usage for: <code>globus_xio_data_descriptor_cntl </code>.</p>
<dt><i>GLOBUS_XIO_UDP_CONNECT </i></p>
<dd>See usage for: <code>globus_xio_handle_cntl </code>.</p>
<dt><i>GLOBUS_XIO_UDP_SET_MULTICAST </i></p>
<dd>See usage for: <code>globus_xio_attr_cntl </code>.</dl>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, GLOBUS_XIO_UDP_SET_HANDLE, globus_xio_system_socket_t handle)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the udp socket to use. <code>Parameters:</code></p>
<dl>
<dd><i>handle</i> Use this handle (fd or SOCKET). Note: close() will not be called on this handle.</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, GLOBUS_XIO_UDP_SET_SERVICE, const char * service_name)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the udp service name to listen on. <code>Parameters:</code></p>
<dl>
<dd><i>service_name</i> The service name to use when setting up the listener. If the service name cannot be resolved, the port (if one is set) will be used instead.</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, GLOBUS_XIO_UDP_GET_SERVICE, char ** service_name_out)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the service name to listen on. <code>Parameters:</code></p>
<dl>
<dd><i>service_name_out</i> A pointer to the service name will be stored here If none is set, NULL will be passed back. Otherwise, the name will be duplicated with strdup() and the user should call free() on it.</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, GLOBUS_XIO_UDP_SET_PORT, int listener_port)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the port number to listen on. The default is 0 (system assigned) </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>listener_port</i> The port number to use when setting up the listener. If the service name is also set, this will only be used if that can&#8217;t be resolved.</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, GLOBUS_XIO_UDP_GET_PORT, int * listener_port_out)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. the port number to listen on. <code>Parameters:</code></p>
<dl>
<dd><i>listener_port_out</i> The port will be stored here.</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, GLOBUS_XIO_UDP_SET_LISTEN_RANGE, int listener_min_port, int listener_max_port)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the port range to confine the listener to. Used only where no specific service or port has been set. It overrides the range set in the GLOBUS_UDP_PORT_RANGE env variable. If &#8216;restrict port&#8217; is true, the listening port will be constrained to the range specified. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>listener_min_port</i> The lower bound on the listener port. (default 0 &#8212; no bound)<br />
 <i>listener_max_port</i> The upper bound on the listener port. (default 0 &#8212; no bound)</dl>
<p> <code>See also:</code></p>
<dl>
<dd><code>GLOBUS_XIO_UDP_SET_RESTRICT_PORT</code></dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, GLOBUS_XIO_UDP_GET_LISTEN_RANGE, int * listener_min_port_out, int * listener_max_port_out)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the udp port range on an attr. <code>Parameters:</code></p>
<dl>
<dd><i>listener_min_port_out</i> The lower bound will be stored here.<br />
 <i>listener_max_port_out</i> The upper bound will be stored here.</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, GLOBUS_XIO_UDP_SET_INTERFACE, const char * interface)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the interface to bind the socket to. <code>Parameters:</code></p>
<dl>
<dd><i>interface</i> The interface to use. Can be a hostname or numeric IP</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, GLOBUS_XIO_UDP_GET_INTERFACE, char ** interface_out)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the interface on the attr. <code>Parameters:</code></p>
<dl>
<dd><i>interface_out</i> A pointer to the interface will be stored here If one is set, NULL will be passed back. Otherwise, the interface will be duplicated with strdup() and the user should call free() on it.</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, GLOBUS_XIO_UDP_SET_RESTRICT_PORT, globus_bool_t restrict_port)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Enable or disable the listener range constraints. This enables or ignores the port range found in the attr or in then env. By default, those ranges are enabled. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>restrict_port</i> GLOBUS_TRUE to enable (default), GLOBUS_FALSE to disable.</dl>
<p> <code>See also:</code></p>
<dl>
<dd><code>GLOBUS_XIO_UDP_SET_LISTEN_RANGE</code></dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, GLOBUS_XIO_UDP_GET_RESTRICT_PORT, globus_bool_t * restrict_port_out)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the restrict port flag. <code>Parameters:</code></p>
<dl>
<dd><i>restrict_port_out</i> The restrict port flag will be stored here.</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, GLOBUS_XIO_UDP_SET_REUSEADDR, globus_bool_t resuseaddr)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Reuse addr when binding. Used to determine whether or not to allow reuse of addresses when binding a socket to a port number. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>resuseaddr</i> GLOBUS_TRUE to allow, GLOBUS_FALSE to disallow (default)</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, GLOBUS_XIO_UDP_GET_REUSEADDR, globus_bool_t * resuseaddr_out)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the reuseaddr flag on an attr. <code>Parameters:</code></p>
<dl>
<dd><i>resuseaddr_out</i> The reuseaddr flag will be stored here.</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, GLOBUS_XIO_UDP_SET_NO_IPV6, globus_bool_t no_ipv6)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Restrict to IPV4 only. Disallow IPV6 sockets from being used (default is to use either ipv4 or ipv6) </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>no_ipv6</i> GLOBUS_TRUE to disallow ipv6, GLOBUS_FALSE to allow (default)</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, GLOBUS_XIO_UDP_GET_NO_IPV6, globus_bool_t * no_ipv6_out)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the no ipv6 flag on an attr. <code>Parameters:</code></p>
<dl>
<dd><i>no_ipv6_out</i> The no ipv6 flag will be stored here.</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, GLOBUS_XIO_UDP_GET_HANDLE, globus_xio_system_socket_t * handle_out)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the socket handle on an attr or handle. <code>Parameters:</code></p>
<dl>
<dd><i>handle_out</i> The udp socket will be stored here. If none is set, GLOBUS_XIO_UDP_INVALID_HANDLE will be set.</dl>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, GLOBUS_XIO_UDP_GET_HANDLE, globus_xio_system_socket_t * handle_out)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the socket handle on an attr or handle. <code>Parameters:</code></p>
<dl>
<dd><i>handle_out</i> The udp socket will be stored here. If none is set, GLOBUS_XIO_UDP_INVALID_HANDLE will be set.</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, GLOBUS_XIO_UDP_SET_SNDBUF, int sndbuf)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the socket send buffer size. Used to set the size of the send buffer used on the socket. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>sndbuf</i> The send buffer size in bytes to use. (default is system specific)</dl>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, GLOBUS_XIO_UDP_SET_SNDBUF, int sndbuf)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the socket send buffer size. Used to set the size of the send buffer used on the socket. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>sndbuf</i> The send buffer size in bytes to use. (default is system specific)</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, GLOBUS_XIO_UDP_GET_SNDBUF, int * sndbuf_out)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the send buffer size on the attr or handle. <code>Parameters:</code></p>
<dl>
<dd><i>sndbuf_out</i> The send buffer size will be stored here.</dl>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, GLOBUS_XIO_UDP_GET_SNDBUF, int * sndbuf_out)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the send buffer size on the attr or handle. <code>Parameters:</code></p>
<dl>
<dd><i>sndbuf_out</i> The send buffer size will be stored here.</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, GLOBUS_XIO_UDP_SET_RCVBUF, int rcvbuf)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the socket receive buffer size. Used to set the size of the receive buffer used on the socket. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>rcvbuf</i> The receive buffer size in bytes. (default is system specific)</dl>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, GLOBUS_XIO_UDP_SET_RCVBUF, int rcvbuf)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the socket receive buffer size. Used to set the size of the receive buffer used on the socket. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>rcvbuf</i> The receive buffer size in bytes. (default is system specific)</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, GLOBUS_XIO_UDP_GET_RCVBUF, int * rcvbuf_out)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the receive buffer size on the attr or handle. <code>Parameters:</code></p>
<dl>
<dd><i>rcvbuf_out</i> The receive buffer size will be stored here.</dl>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, GLOBUS_XIO_UDP_GET_RCVBUF, int * rcvbuf_out)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the receive buffer size on the attr or handle. <code>Parameters:</code></p>
<dl>
<dd><i>rcvbuf_out</i> The receive buffer size will be stored here.</dl>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, GLOBUS_XIO_UDP_GET_CONTACT, char ** contact_string_out)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the contact string associated with a handle or data descriptor. Use with <code>globus_xio_handle_cntl()</code> to get a contact string for the udp listener. Use with <code>globus_xio_data_descriptor_cntl()</code> to get the sender&#8217;s contact string from a data descriptor passed to <code>globus_xio_register_read()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>contact_string_out</i> A pointer to a contact string will be stored here. The user should free() it when done with it. It will be in the format: &lt;hostname&gt;:&lt;port&gt;</dl>
<p> <code>See also:</code></p>
<dl>
<dd><code>GLOBUS_XIO_GET_LOCAL_CONTACT</code></dl>
<h3>globus_result_t globus_xio_data_descriptor_cntl (dd, driver, GLOBUS_XIO_UDP_GET_CONTACT, char ** contact_string_out)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the contact string associated with a handle or data descriptor. Use with <code>globus_xio_handle_cntl()</code> to get a contact string for the udp listener. Use with <code>globus_xio_data_descriptor_cntl()</code> to get the sender&#8217;s contact string from a data descriptor passed to <code>globus_xio_register_read()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>contact_string_out</i> A pointer to a contact string will be stored here. The user should free() it when done with it. It will be in the format: &lt;hostname&gt;:&lt;port&gt;</dl>
<p> <code>See also:</code></p>
<dl>
<dd><code>GLOBUS_XIO_GET_LOCAL_CONTACT</code></dl>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, GLOBUS_XIO_UDP_GET_NUMERIC_CONTACT, char ** contact_string_out)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the contact string associated with a handle or data descriptor. Use with <code>globus_xio_handle_cntl()</code> to get a contact string for the udp listener. Use with <code>globus_xio_data_descriptor_cntl()</code> to get the sender&#8217;s contact string from a data descriptor passed to <code>globus_xio_register_read()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>contact_string_out</i> A pointer to a contact string will be stored here. The user should free() it when done with it. It will be in the format: &lt;ip&gt;:&lt;port&gt;</dl>
<p> <code>See also:</code></p>
<dl>
<dd><code>GLOBUS_XIO_GET_LOCAL_NUMERIC_CONTACT</code></dl>
<h3>globus_result_t globus_xio_data_descriptor_cntl (dd, driver, GLOBUS_XIO_UDP_GET_NUMERIC_CONTACT, char ** contact_string_out)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the contact string associated with a handle or data descriptor. Use with <code>globus_xio_handle_cntl()</code> to get a contact string for the udp listener. Use with <code>globus_xio_data_descriptor_cntl()</code> to get the sender&#8217;s contact string from a data descriptor passed to <code>globus_xio_register_read()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>contact_string_out</i> A pointer to a contact string will be stored here. The user should free() it when done with it. It will be in the format: &lt;ip&gt;:&lt;port&gt;</dl>
<p> <code>See also:</code></p>
<dl>
<dd><code>GLOBUS_XIO_GET_LOCAL_NUMERIC_CONTACT</code></dl>
<h3>globus_result_t globus_xio_data_descriptor_cntl (dd, driver, GLOBUS_XIO_UDP_SET_CONTACT, char * contact_string)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the destination contact. Use on a data descriptor passed to <code>globus_xio_register_write()</code> to specify the recipient of the data. This is necessary with unconnected handles or to send to recipients other than the connected one. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>contact_string</i> A pointer to a contact string of the format &lt;hostname/ip&gt;:&lt;port/service&gt;</dl>
<p> <code>See also:</code></p>
<dl>
<dd><code>GLOBUS_XIO_UDP_CONNECT</code></dl>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, GLOBUS_XIO_UDP_CONNECT, char * contact_string)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the default destination contact. Connecting a handle to a specific contact blocks packets from any other contact. It also sets the default destination of all outgoing packets so, using <code>GLOBUS_XIO_UDP_SET_CONTACT</code> is unnecessary. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>contact_string</i> A pointer to a contact string of the format &lt;hostname/ip&gt;:&lt;port/service&gt;</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, GLOBUS_XIO_UDP_SET_MULTICAST, char * contact_string)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Join a multicast group. Specifiy a multicast group to join. All packets received will be to the specified multicast address. Do not use <code>GLOBUS_XIO_UDP_CONNECT</code>, <code>GLOBUS_XIO_UDP_SET_PORT</code>, or pass a contact string on the open. Consider using <code>GLOBUS_XIO_UDP_SET_REUSEADDR</code> to allow other apps to join this group. Use <code>GLOBUS_XIO_UDP_SET_INTERFACE</code> to specify the interface to use. Will not affect handles set with <code>GLOBUS_XIO_UDP_SET_HANDLE</code>. <code>GLOBUS_XIO_UDP_SET_RESTRICT_PORT</code> is ignored. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>contact_string</i> A pointer to a contact string of the multicast group to join with the format: &lt;hostname/ip&gt;:&lt;port/service&gt;</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus xio from the source code.</p>
