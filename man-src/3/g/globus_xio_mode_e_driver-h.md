---
title: "globus_xio_mode_e_driver-h(3)"
name: "globus_xio_mode_e_driver-h"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_xio_mode_e_driver-h/"
description: "builtins/mode_e/globus_xio_mode_e_driver.h –"
---

<p>builtins/mode_e/globus_xio_mode_e_driver.h &#8211; </p>
<p> XIO MODE_E Driver.</p>
<h2>Synopsis</h2>
<p>#include &#8216;globus_common.h&#8217; </p>
<h3>Enumerations</h3>
<p>enum <code>globus_xio_mode_e_error_type_t</code> { <code>GLOBUS_XIO_MODE_E_HEADER_ERROR</code> } </p>
<p> enum <code>globus_xio_mode_e_cmd_t</code> { <code>GLOBUS_XIO_MODE_E_SET_STACK</code>, <code>GLOBUS_XIO_MODE_E_GET_STACK</code>, <code>GLOBUS_XIO_MODE_E_SET_NUM_STREAMS</code>, <code>GLOBUS_XIO_MODE_E_GET_NUM_STREAMS</code>, <code>GLOBUS_XIO_MODE_E_SET_OFFSET_READS</code>, <code>GLOBUS_XIO_MODE_E_GET_OFFSET_READS</code>, <code>GLOBUS_XIO_MODE_E_SET_MANUAL_EODC</code>, <code>GLOBUS_XIO_MODE_E_GET_MANUAL_EODC</code>, <code>GLOBUS_XIO_MODE_E_SEND_EOD</code>, <code>GLOBUS_XIO_MODE_E_SET_EODC</code>, <code>GLOBUS_XIO_MODE_E_DD_GET_OFFSET</code>, <code>GLOBUS_XIO_MODE_E_SET_STACK_ATTR</code>, <code>GLOBUS_XIO_MODE_E_GET_STACK_ATTR</code> } </p>
<h3>Functions</h3>
<p>globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_MODE_E_SET_STACK</code>, globus_xio_stack_t stack) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_MODE_E_GET_STACK</code>, globus_xio_stack_t *stack_out) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_MODE_E_SET_NUM_STREAMS</code>, int num_streams) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_MODE_E_GET_NUM_STREAMS</code>, int *num_streams_out) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_MODE_E_SET_OFFSET_READS</code>, globus_bool_t offset_reads) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_MODE_E_GET_OFFSET_READS</code>, globus_bool_t *offset_reads_out) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_MODE_E_SET_MANUAL_EODC</code>, globus_bool_t manual_eodc) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_MODE_E_GET_MANUAL_EODC</code>, globus_bool_t *manual_eodc_out) </p>
<p> globus_result_t <code>globus_xio_data_descriptor_cntl</code> (dd, driver, <code>GLOBUS_XIO_MODE_E_SEND_EOD</code>, globus_bool_t send_eod) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_MODE_E_SET_EODC</code>, int eod_count) </p>
<p> globus_result_t <code>globus_xio_data_descriptor_cntl</code> (dd, driver, <code>GLOBUS_XIO_MODE_E_DD_GET_OFFSET</code>, globus_off_t *offset_out) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_MODE_E_SET_STACK_ATTR</code>, globus_xio_stack_t stack) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_MODE_E_GET_STACK_ATTR</code>, globus_xio_attr_t *stack_out) </p>
<h2>Detailed Description</h2>
<p>XIO MODE_E Driver. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_xio from the source code.</p>
