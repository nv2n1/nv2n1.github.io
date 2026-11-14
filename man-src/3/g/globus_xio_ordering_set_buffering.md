---
title: "globus_xio_ordering_set_buffering(3)"
name: "globus_xio_ordering_set_buffering"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_xio_ordering_set_buffering/"
description: "Attributes and Cntls –"
---

<p>Attributes and Cntls &#8211; </p>
<h3>Enumerations</h3>
<p>enum <code>globus_xio_ordering_cmd_t</code> { <code>GLOBUS_XIO_ORDERING_SET_OFFSET</code>, <code>GLOBUS_XIO_ORDERING_SET_MAX_READ_COUNT</code>, <code>GLOBUS_XIO_ORDERING_GET_MAX_READ_COUNT</code>, <code>GLOBUS_XIO_ORDERING_SET_BUFFERING</code>, <code>GLOBUS_XIO_ORDERING_GET_BUFFERING</code>, <code>GLOBUS_XIO_ORDERING_SET_BUF_SIZE</code>, <code>GLOBUS_XIO_ORDERING_GET_BUF_SIZE</code>, <code>GLOBUS_XIO_ORDERING_SET_MAX_BUF_COUNT</code>, <code>GLOBUS_XIO_ORDERING_GET_MAX_BUF_COUNT</code> } </p>
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
<p>Ordering driver specific attrs and cntls. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>globus_xio_attr_cntl()</code> </p>
<p> <code>globus_xio_handle_cntl()</code></dl>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>globus_xio_ordering_cmd_t</code></h3>
<p>ORDERING driver specific cntls </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>GLOBUS_XIO_ORDERING_SET_OFFSET </i></p>
<dd>See usage for: <code>globus_xio_handle_cntl </code></p>
<dt><i>GLOBUS_XIO_ORDERING_SET_MAX_READ_COUNT </i></p>
<dd>See usage for: <code>globus_xio_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_ORDERING_GET_MAX_READ_COUNT </i></p>
<dd>See usage for: <code>globus_xio_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_ORDERING_SET_BUFFERING </i></p>
<dd>See usage for: <code>globus_xio_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_ORDERING_GET_BUFFERING </i></p>
<dd>See usage for: <code>globus_xio_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_ORDERING_SET_BUF_SIZE </i></p>
<dd>See usage for: <code>globus_xio_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_ORDERING_GET_BUF_SIZE </i></p>
<dd>See usage for: <code>globus_xio_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_ORDERING_SET_MAX_BUF_COUNT </i></p>
<dd>See usage for: <code>globus_xio_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_ORDERING_GET_MAX_BUF_COUNT </i></p>
<dd>See usage for: <code>globus_xio_attr_cntl </code></dl>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_ORDERING_SET_MAX_READ_COUNT</code>, intmax_read_count)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the maximum number of reads that ordering driver can have outstanding on driver(s) below. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>max_read_count</i> Specifies the maximum number of parallel reads (default is 1).</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_ORDERING_GET_MAX_READ_COUNT</code>, int *max_read_count_out)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the maximum number of parallel reads set on the attr. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>max_read_count_out</i> The maximum number of parallel reads allowed will be stored here.</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_ORDERING_SET_BUFFERING</code>, globus_bool_tbuffering)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. This driver can be used in 2 modes; ordering (care about offsets of the data read &#8211; underlying transport driver may deliver data out of order &#8211; this driver will rearrange data based on the offset and deliver inorder to user) and buffering (do not care about offsets &#8211; just buffer the data read abd deliver it when requested). This attribute control can be used to enable buffering. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>buffering</i> GLOBUS_TRUE to enable buffering, GLOBUS_FALSE (default) to disable buffering.</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_ORDERING_GET_BUFFERING</code>, globus_bool_t *buffering_out)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the buffering flag on the attr. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>buffering_out</i> Buffering flag will be stored in here.</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_ORDERING_SET_BUF_SIZE</code>, intbuf_size)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the size of the buffer that ordering driver creates to use for reading data from the driver below it. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>buf_size</i> Specifies the buffer size for internal reads (default is 100 KB).</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_ORDERING_GET_BUF_SIZE</code>, int *buf_size_out)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the size of the buffer used for the internal reads. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>buf_size_out</i> The buffer size will be stored in here.</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_ORDERING_SET_MAX_BUF_COUNT</code>, intmax_buf_count)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the maximum number of buffers that this driver can create for reading data from the driver below it. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>max_buf_count</i> Specifies the max buffer count for internal reads (default is 100).</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_ORDERING_GET_MAX_BUF_COUNT</code>, int *max_buf_count_out)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get the maximum buffer count set on the attr. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>max_buf_count_out</i> The maximun buffer count will be stored in here.</dl>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, <code>GLOBUS_XIO_ORDERING_SET_OFFSET</code>, globus_off_toffset)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set offset for the next IO operation. This is not allowed when there is an outstanding IO operation. This operation clears all the buffered data. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>offset</i> Specifies the offset to use in the next IO operation.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_xio from the source code.</p>
