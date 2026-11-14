---
title: "globus_net_manager_tutorial(3)"
name: "globus_net_manager_tutorial"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_net_manager_tutorial/"
description: "globus_net_manager_tutorial – Net Manager Implementation Tutorial This example uses functionality from globus_common and globus_net_manager modules, so the headers for those must be included:"
---

<h2 class="name">NAME</h2>
<p> globus_net_manager_tutorial &#8211; Net Manager Implementation Tutorial This example uses functionality from globus_common and globus_net_manager modules, so the headers for those must be included: </p>
<pre><code>
#include "globus_common.h"
#include "globus_net_manager.h"
</code></pre>
<p>&nbsp;<wbr>To implement a network manager, define a struct&nbsp;<wbr><code>globus_net_manager_s</code>&nbsp;<wbr>containing pointers to the functions in your code that you want invoked during network events, and pass that to&nbsp;<wbr><code>globus_net_manager_register()</code>. Applications which use the&nbsp;<wbr><code>Context</code>&nbsp;<wbr>functions or the&nbsp;<wbr><code>Globus XIO Net Manager Driver</code>&nbsp;<wbr>will invoke your functions as network operations occur. For this example&nbsp;<wbr>(and I would imagine most real implementations), the globus_net_manager_t is statically initialized, like this: </p>
<p>static globus_net_manager_t globus_l_net_manager_logging = {<br />
    &#8220;logging&#8221;,<br />
    globus_l_net_manager_logging_pre_listen,<br />
    globus_l_net_manager_logging_post_listen,<br />
    globus_l_net_manager_logging_end_listen,<br />
    globus_l_net_manager_logging_pre_accept,<br />
    globus_l_net_manager_logging_post_accept,<br />
    globus_l_net_manager_logging_pre_connect,<br />
    globus_l_net_manager_logging_post_connect,<br />
    globus_l_net_manager_logging_pre_close,<br />
    globus_l_net_manager_logging_post_close};</p>
<p>&nbsp;<wbr>For the examples provided in this library, the&nbsp;<wbr><code>globus_net_manager_s</code>&nbsp;<wbr>is registered during module activation in a globus_extension module. This method makes it easy to use network managers in a shared library environment. This is also a good place to initialize any state that you need to retain between calls to the network manager. </p>
<p> To implement this, do the following: </p>
<p>static int<br />
globus_l_net_manager_logging_activate(void)<br />
{<br />
    globus_hashtable_init(<br />
        &amp;globus_l_nm_logging_logfiles,<br />
        7,<br />
        globus_hashtable_string_hash,<br />
        globus_hashtable_string_keyeq);<br />
    int rc = globus_module_activate(GLOBUS_NET_MANAGER_MODULE);<br />
    if (rc == 0) {<br />
        rc = globus_net_manager_register(<br />
            &amp;globus_l_net_manager_logging,<br />
            GlobusExtensionMyModule(globus_net_manager_logging));<br />
    }<br />
    return rc;<br />
}<br />
static void<br />
globus_l_logging_logfiles_destroy(void *datum)<br />
{<br />
    globus_l_nm_logging_logref_t *logref = datum;<br />
    if (logref) {<br />
        free(logref-&gt;key);<br />
        fclose(logref-&gt;handle);<br />
        free(logref);<br />
    }<br />
}<br />
static int<br />
globus_l_net_manager_logging_deactivate(void)<br />
{<br />
    globus_hashtable_destroy_all(<br />
        &amp;globus_l_nm_logging_logfiles,<br />
        globus_l_logging_logfiles_destroy);<br />
    int rc = globus_net_manager_unregister(&amp;globus_l_net_manager_logging);<br />
    if (rc == 0) {<br />
        rc = globus_module_deactivate(GLOBUS_NET_MANAGER_MODULE);<br />
    }<br />
    return rc;<br />
}</p>
<p> Finally, the real work of the manager is done in the functions registered in the <code>globus_net_manager_s</code>. For brevity, I&#8217;ll just include the pre_listen function in this tutorial. This function is passed the task-id associated with the operation, the transport (&#8216;tcp&#8217;, &#8216;udp&#8217;, &#8216;udt&#8217;, etc) used by the network, and whatever attributes are associated with the operation. If we wanted to modify things before they were processed by the network, we could create a modified copy of the attributes in the pre_listen function and return them via the attr_array_out parameter. In this case, we simply print out the information we&#8217;ve received from the network stack. </p>
<pre><code>
static globus_result_t
globus_l_net_manager_logging_pre_listen(
    struct globus_net_manager_s *manager,
    const globus_net_manager_attr_t *manager_attr_array,
    const char *task_id,
    const char *transport,
    const globus_net_manager_attr_t *attr_array,
    globus_net_manager_attr_t **attr_array_out)
{
    FILE *logfile;
    logfile = globus_l_net_manager_logging_get_logfile(manager_attr_array);
    globus_l_net_manager_logging_log_header(logfile, manager, task_id, transport, "pre_listen");
    globus_l_net_manager_logging_log_attrs(logfile, attr_array);
    globus_l_net_manager_logging_log_footer(logfile);
    return GLOBUS_SUCCESS;
}
/* globus_l_net_manager_logging_pre_listen() */
</code></pre>
<hr>
<h2>Index</h2>
