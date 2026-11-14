---
title: "globus_xio_net_manager_driver-h(3)"
name: "globus_xio_net_manager_driver-h"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_xio_net_manager_driver-h/"
description: "xio_driver/globus_xio_net_manager_driver.h –"
---

<p>xio_driver/globus_xio_net_manager_driver.h &#8211; </p>
<p> Network Manager XIO Driver.</p>
<h2>Synopsis</h2>
<p>#include &#8216;globus_common.h&#8217;<br />
 #include &#8216;globus_net_manager_attr.h&#8217; </p>
<h3>Enumerations</h3>
<p>enum <code>globus_xio_net_manager_cntl_t</code> { <code>GLOBUS_XIO_NET_MANAGER_SET_TASK_ID</code>, <code>GLOBUS_XIO_NET_MANAGER_GET_TASK_ID</code> } </p>
<h3>Functions</h3>
<p>globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_NET_MANAGER_SET_TASK_ID</code>, const char *task_id) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_NET_MANAGER_GET_TASK_ID</code>, const char **task_id) </p>
<h2>Detailed Description</h2>
<p>Network Manager XIO Driver. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_net_manager from the source code.</p>
