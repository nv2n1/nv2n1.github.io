---
title: "globus_xio_mode_e_get_stack(3)"
name: "globus_xio_mode_e_get_stack"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_xio_mode_e_get_stack/"
description: "Attributes and Cntls –"
---

<p>Attributes and Cntls &#8211; </p>
<h3>Enumerations</h3>
<p>enum <code>globus_xio_mode_e_cmd_t</code> { <code>GLOBUS_XIO_MODE_E_SET_STACK</code>, <code>GLOBUS_XIO_MODE_E_GET_STACK</code>, <code>GLOBUS_XIO_MODE_E_SET_NUM_STREAMS</code>, <code>GLOBUS_XIO_MODE_E_GET_NUM_STREAMS</code>, <code>GLOBUS_XIO_MODE_E_SET_OFFSET_READS</code>, <code>GLOBUS_XIO_MODE_E_GET_OFFSET_READS</code>, <code>GLOBUS_XIO_MODE_E_SET_MANUAL_EODC</code>, <code>GLOBUS_XIO_MODE_E_GET_MANUAL_EODC</code>, <code>GLOBUS_XIO_MODE_E_SEND_EOD</code>, <code>GLOBUS_XIO_MODE_E_SET_EODC</code>, <code>GLOBUS_XIO_MODE_E_DD_GET_OFFSET</code>, <code>GLOBUS_XIO_MODE_E_SET_STACK_ATTR</code>, <code>GLOBUS_XIO_MODE_E_GET_STACK_ATTR</code> } </p>
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
<p>Mode_e driver specific attrs and cntls. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>globus_xio_attr_cntl()</code> </p>
<p> <code>globus_xio_handle_cntl()</code> </p>
<p> <code>globus_xio_server_cntl()</code> </p>
<p> <code>globus_xio_data_descriptor_cntl()</code></dl>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>globus_xio_mode_e_cmd_t</code></h3>
<p>doxygen varargs filter stuff MODE_E driver specific cntls </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>GLOBUS_XIO_MODE_E_SET_STACK </i></p>
<dd>See usage for: <code>globus_xio_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_MODE_E_GET_STACK </i></p>
<dd>See usage for: <code>globus_xio_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_MODE_E_SET_NUM_STREAMS </i></p>
<dd>See usage for: <code>globus_xio_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_MODE_E_GET_NUM_STREAMS </i></p>
<dd>See usage for: <code>globus_xio_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_MODE_E_SET_OFFSET_READS </i></p>
<dd>See usage for: <code>globus_xio_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_MODE_E_GET_OFFSET_READS </i></p>
<dd>See usage for: <code>globus_xio_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_MODE_E_SET_MANUAL_EODC </i></p>
<dd>See usage for: <code>globus_xio_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_MODE_E_GET_MANUAL_EODC </i></p>
<dd>See usage for: <code>globus_xio_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_MODE_E_SEND_EOD </i></p>
<dd>See usage for: <code>globus_xio_data_descriptor_cntl </code></p>
<dt><i>GLOBUS_XIO_MODE_E_SET_EODC </i></p>
<dd>See usage for: <code>globus_xio_handle_cntl </code></p>
<dt><i>GLOBUS_XIO_MODE_E_DD_GET_OFFSET </i></p>
<dd>See usage for: <code>globus_xio_data_descriptor_cntl </code></p>
<dt><i>GLOBUS_XIO_MODE_E_SET_STACK_ATTR </i></p>
<dd>See usage for: <code>globus_xio_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_MODE_E_GET_STACK_ATTR </i></p>
<dd>See usage for: <code>globus_xio_attr_cntl </code></dl>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_MODE_E_SET_STACK</code>, globus_xio_stack_tstack)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the stack (of xio drivers) to be used for the connection(s). </p>
<p> Do not create a new ftp client handle, use this handle instead. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>stack</i> Specifies the stack to use for the connection(s). Note: this stack will not be destroyed.</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_MODE_E_GET_STACK</code>, globus_xio_stack_t *stack_out)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the stack on the attr. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>stack_out</i> The stack will be stored here. If none is set, GLOBUS_NULL will be set.</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_MODE_E_SET_NUM_STREAMS</code>, intnum_streams)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the number of streams to be used between the client and the server. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>num_streams</i> Specifies the number of streams to use.</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_MODE_E_GET_NUM_STREAMS</code>, int *num_streams_out)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the number of streams on the attr. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>num_streams_out</i> The stream count will be stored here.</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_MODE_E_SET_OFFSET_READS</code>, globus_bool_toffset_reads)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set flag to indicate whether the data read from user would always be preceded by an offset read or not. The user can do a read with wait_for_bytes set to zero, to find the offset of the data that he is going to get in his next read operation </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>offset_reads</i> GLOBUS_TRUE to enable offset reads, GLOBUS_FALSE to disable offset reads (default).</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_MODE_E_GET_OFFSET_READS</code>, globus_bool_t *offset_reads_out)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get OFFSET_READS flag on the attr. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>offset_reads_out</i> The OFFSET_READS flag will be stored here.</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_MODE_E_SET_MANUAL_EODC</code>, globus_bool_tmanual_eodc)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set flag to indicate whether EODC will be set manually by the user on a data_desc or the driver has to calculate the EODC </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>manual_eodc</i> GLOBUS_TRUE to set EODC manually, GLOBUS_FALSE to not set EODC manually (default).</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_MODE_E_GET_MANUAL_EODC</code>, globus_bool_t *manual_eodc_out)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get MANUAL_EODC flag on the attr. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>manual_eodc_out</i> The MANUAL_EODC flag will be stored here.</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_MODE_E_SET_STACK_ATTR</code>, globus_xio_stack_tstack)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the attr to be used with the stack set from GLOBUS_XIO_MODE_E_SET_STACK. </p>
<p> Do not create a new ftp client handle, use this handle instead. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>stack</i> Specifies the stack to use for the connection(s). Note: this stack will not be destroyed.</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_MODE_E_GET_STACK_ATTR</code>, globus_xio_attr_t *stack_out)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the attr that will be used with the stack. This is intended for use with GLOBUS_XIO_MODE_E_SET_STACK. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>stack_out</i> The stack will be stored here. If none is set, GLOBUS_NULL will be set.</dl>
<h3>globus_result_t globus_xio_data_descriptor_cntl (dd, driver, <code>GLOBUS_XIO_MODE_E_SEND_EOD</code>, globus_bool_tsend_eod)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set SEND_EOD flag </p>
<p> Used only for data descriptors to write calls. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>send_eod</i> GLOBUS_TRUE to send EOD, GLOBUS_FALSE to not send EOD (default).</dl>
<h3>globus_result_t globus_xio_data_descriptor_cntl (dd, driver, <code>GLOBUS_XIO_MODE_E_DD_GET_OFFSET</code>, globus_off_t *offset_out)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get offset of the next available data </p>
<p> Used only if OFFSET_READS is enabled. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>offset_out</i> offset will be stored here</dl>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, <code>GLOBUS_XIO_MODE_E_SET_EODC</code>, inteod_count)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set EOD count </p>
<p> Used only if MANUAL_EODC flag is set to GLOBUS_TRUE. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>eod_count</i> specifies the eod count</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_xio from the source code.</p>
