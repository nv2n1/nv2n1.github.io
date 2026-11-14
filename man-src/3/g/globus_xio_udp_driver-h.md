---
title: "globus_xio_udp_driver-h(3)"
name: "globus_xio_udp_driver-h"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_xio_udp_driver-h/"
description: "builtins/udp/globus_xio_udp_driver.h –"
---

<p>builtins/udp/globus_xio_udp_driver.h &#8211; </p>
<p> XIO UDP Driver.</p>
<h2>Synopsis</h2>
<p>#include &#8216;globus_xio_system.h&#8217; </p>
<h3>Macros</h3>
<p>#define <code>GLOBUS_XIO_UDP_INVALID_HANDLE</code> </p>
<h3>Enumerations</h3>
<p>enum <code>globus_xio_udp_error_type_t</code> { <code>GLOBUS_XIO_UDP_ERROR_NO_ADDRS</code>, <code>GLOBUS_XIO_UDP_ERROR_SHORT_WRITE</code> } </p>
<p> enum <code>globus_xio_udp_cmd_t</code> { <code>GLOBUS_XIO_UDP_SET_HANDLE</code>, <code>GLOBUS_XIO_UDP_SET_SERVICE</code>, <code>GLOBUS_XIO_UDP_GET_SERVICE</code>, <code>GLOBUS_XIO_UDP_SET_PORT</code>, <code>GLOBUS_XIO_UDP_GET_PORT</code>, <code>GLOBUS_XIO_UDP_SET_LISTEN_RANGE</code>, <code>GLOBUS_XIO_UDP_GET_LISTEN_RANGE</code>, <code>GLOBUS_XIO_UDP_SET_INTERFACE</code>, <code>GLOBUS_XIO_UDP_GET_INTERFACE</code>, <code>GLOBUS_XIO_UDP_SET_RESTRICT_PORT</code>, <code>GLOBUS_XIO_UDP_GET_RESTRICT_PORT</code>, <code>GLOBUS_XIO_UDP_SET_REUSEADDR</code>, <code>GLOBUS_XIO_UDP_GET_REUSEADDR</code>, <code>GLOBUS_XIO_UDP_SET_NO_IPV6</code>, <code>GLOBUS_XIO_UDP_GET_NO_IPV6</code>, <code>GLOBUS_XIO_UDP_GET_HANDLE</code>, <code>GLOBUS_XIO_UDP_SET_SNDBUF</code>, <code>GLOBUS_XIO_UDP_GET_SNDBUF</code>, <code>GLOBUS_XIO_UDP_SET_RCVBUF</code>, <code>GLOBUS_XIO_UDP_GET_RCVBUF</code>, <code>GLOBUS_XIO_UDP_GET_CONTACT</code>, <code>GLOBUS_XIO_UDP_GET_NUMERIC_CONTACT</code>, <code>GLOBUS_XIO_UDP_SET_CONTACT</code>, <code>GLOBUS_XIO_UDP_CONNECT</code>, <code>GLOBUS_XIO_UDP_SET_MULTICAST</code> } </p>
<h3>Functions</h3>
<p>globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_UDP_SET_HANDLE</code>, globus_xio_system_socket_t handle) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_UDP_SET_SERVICE</code>, const char *service_name) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_UDP_GET_SERVICE</code>, char **service_name_out) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_UDP_SET_PORT</code>, int listener_port) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_UDP_GET_PORT</code>, int *listener_port_out) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_UDP_SET_LISTEN_RANGE</code>, int listener_min_port, int listener_max_port) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_UDP_GET_LISTEN_RANGE</code>, int *listener_min_port_out, int *listener_max_port_out) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_UDP_SET_INTERFACE</code>, const char *interface) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_UDP_GET_INTERFACE</code>, char **interface_out) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_UDP_SET_RESTRICT_PORT</code>, globus_bool_t restrict_port) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_UDP_GET_RESTRICT_PORT</code>, globus_bool_t *restrict_port_out) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_UDP_SET_REUSEADDR</code>, globus_bool_t resuseaddr) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_UDP_GET_REUSEADDR</code>, globus_bool_t *resuseaddr_out) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_UDP_SET_NO_IPV6</code>, globus_bool_t no_ipv6) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_UDP_GET_NO_IPV6</code>, globus_bool_t *no_ipv6_out) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_UDP_GET_HANDLE</code>, globus_xio_system_socket_t *handle_out) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_UDP_GET_HANDLE</code>, globus_xio_system_socket_t *handle_out) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_UDP_SET_SNDBUF</code>, int sndbuf) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_UDP_SET_SNDBUF</code>, int sndbuf) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_UDP_GET_SNDBUF</code>, int *sndbuf_out) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_UDP_GET_SNDBUF</code>, int *sndbuf_out) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_UDP_SET_RCVBUF</code>, int rcvbuf) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_UDP_SET_RCVBUF</code>, int rcvbuf) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_UDP_GET_RCVBUF</code>, int *rcvbuf_out) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_UDP_GET_RCVBUF</code>, int *rcvbuf_out) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_UDP_GET_CONTACT</code>, char **contact_string_out) </p>
<p> globus_result_t <code>globus_xio_data_descriptor_cntl</code> (dd, driver, <code>GLOBUS_XIO_UDP_GET_CONTACT</code>, char **contact_string_out) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_UDP_GET_NUMERIC_CONTACT</code>, char **contact_string_out) </p>
<p> globus_result_t <code>globus_xio_data_descriptor_cntl</code> (dd, driver, <code>GLOBUS_XIO_UDP_GET_NUMERIC_CONTACT</code>, char **contact_string_out) </p>
<p> globus_result_t <code>globus_xio_data_descriptor_cntl</code> (dd, driver, <code>GLOBUS_XIO_UDP_SET_CONTACT</code>, char *contact_string) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_UDP_CONNECT</code>, char *contact_string) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_UDP_SET_MULTICAST</code>, char *contact_string) </p>
<h2>Detailed Description</h2>
<p>XIO UDP Driver. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_xio from the source code.</p>
