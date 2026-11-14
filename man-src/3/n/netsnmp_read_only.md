---
title: "netsnmp_read_only(3)"
name: "netsnmp_read_only"
section: "3"
letter: "n"
url: "/docs/linux/man/3-netsnmp_read_only/"
description: "read_only – Make your handler read_only automatically The only purpose of this handler is to return an appropriate error for any requests passed to it in a SET mode."
---

<p>read_only &#8211; Make your handler read_only automatically The only purpose of this handler is to return an appropriate error for any requests passed to it in a SET mode.</p>
<h3>Functions</h3>
<p><code>netsnmp_mib_handler</code> * <code>netsnmp_get_read_only_handler</code> (void)<br />
 <i>returns a read_only handler that can be injected into a given handler chain. </i><br />
 int <code>netsnmp_read_only_helper</code> (<code>netsnmp_mib_handler</code> *handler, <code>netsnmp_handler_registration</code> *reginfo, <code>netsnmp_agent_request_info</code> *reqinfo, <code>netsnmp_request_info</code> *requests) </p>
<p> void <code>netsnmp_init_read_only_helper</code> (void)<br />
 <i>initializes the read_only helper which then registers a read_only handler as a run-time injectable handler for configuration file use. </i></p>
<h2>Detailed Description</h2>
<p>Make your handler read_only automatically The only purpose of this handler is to return an appropriate error for any requests passed to it in a SET mode. </p>
<p> Inserting it into your handler chain will ensure you&#8217;re never asked to perform a SET request so you can ignore those error conditions.</p>
<h2>Function Documentation</h2>
<h3><code>netsnmp_mib_handler</code>* netsnmp_get_read_only_handler (void)</h3>
<p>returns a read_only handler that can be injected into a given handler chain. </p>
<p> Definition at line 29 of file read_only.c. </p>
<p> References netsnmp_mib_handler_s::flags, MIB_HANDLER_AUTO_NEXT, netsnmp_create_handler(), netsnmp_read_only_helper(), and NULL. </p>
<p> Referenced by netsnmp_init_read_only_helper(), netsnmp_register_read_only_instance(), netsnmp_register_read_only_scalar(), and netsnmp_register_read_only_table_data().</p>
<h3>void netsnmp_init_read_only_helper (void)</h3>
<p>initializes the read_only helper which then registers a read_only handler as a run-time injectable handler for configuration file use. </p>
<p> Definition at line 81 of file read_only.c. </p>
<p> References netsnmp_get_read_only_handler(), and netsnmp_register_handler_by_name().</p>
