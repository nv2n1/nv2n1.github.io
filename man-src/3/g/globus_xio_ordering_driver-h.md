---
title: "globus_xio_ordering_driver-h(3)"
name: "globus_xio_ordering_driver-h"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_xio_ordering_driver-h/"
description: "builtins/ordering/globus_xio_ordering_driver.h –"
---

<p>builtins/ordering/globus_xio_ordering_driver.h &#8211; </p>
<p> XIO ORDERING Driver.</p>
<h2>Synopsis</h2>
<p>#include &#8216;globus_common.h&#8217; </p>
<h3>Enumerations</h3>
<p>enum <code>globus_xio_ordering_error_type_t</code> { <code>GLOBUS_XIO_ORDERING_ERROR_READ</code>, <code>GLOBUS_XIO_ORDERING_ERROR_CANCEL</code> } </p>
<p> enum <code>globus_xio_ordering_cmd_t</code> { <code>GLOBUS_XIO_ORDERING_SET_OFFSET</code>, <code>GLOBUS_XIO_ORDERING_SET_MAX_READ_COUNT</code>, <code>GLOBUS_XIO_ORDERING_GET_MAX_READ_COUNT</code>, <code>GLOBUS_XIO_ORDERING_SET_BUFFERING</code>, <code>GLOBUS_XIO_ORDERING_GET_BUFFERING</code>, <code>GLOBUS_XIO_ORDERING_SET_BUF_SIZE</code>, <code>GLOBUS_XIO_ORDERING_GET_BUF_SIZE</code>, <code>GLOBUS_XIO_ORDERING_SET_MAX_BUF_COUNT</code>, <code>GLOBUS_XIO_ORDERING_GET_MAX_BUF_COUNT</code> } </p>
<h3>Functions</h3>
<p>globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_ORDERING_SET_OFFSET</code>, globus_off_t offset) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_ORDERING_SET_MAX_READ_COUNT</code>, int max_read_count) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_ORDERING_GET_MAX_READ_COUNT</code>, int *max_read_count_out) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_ORDERING_SET_BUFFERING</code>, globus_bool_t buffering) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_ORDERING_GET_BUFFERING</code>, globus_bool_t *buffering_out) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_ORDERING_SET_BUF_SIZE</code>, int buf_size) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_ORDERING_GET_BUF_SIZE</code>, int *buf_size_out) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_ORDERING_SET_MAX_BUF_COUNT</code>, int max_buf_count) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_ORDERING_GET_MAX_BUF_COUNT</code>, int *max_buf_count_out) </p>
<h2>Detailed Description</h2>
<p>XIO ORDERING Driver. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_xio from the source code.</p>
