---
title: "libnodeupdown(3)"
name: "libnodeupdown"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libnodeupdown/"
description: "libnodeupdown – a library of functions to determine if a node is up or down"
---

<h2>NAME</h2>
<p> libnodeupdown &#8211; a library of functions to determine if a node is up or down</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;nodeupdown.h&gt;</code> </p>
<p> <code>nodeupdown_t nodeupdown_handle_create(void);</code> </p>
<p> <code>int nodeupdown_handle_destroy(nodeupdown_t handle);</code> </p>
<p> <code>int nodeupdown_load_data(nodeupdown_t handle, const char *hostname, int port, int timeout_len, char *module);</code> </p>
<p> <code>int nodeupdown_errnum(nodeupdown_t handle);</code> </p>
<p> <code>char *nodeupdown_strerror(int errnum);</code> </p>
<p> <code>char *nodeupdown_errormsg(int errnum);</code> </p>
<p> <code>void nodeupdown_perror(nodeupdown_t handle, const char *msg);</code> </p>
<p> <code>int nodeupdown_get_up_nodes_string(nodeupdown_t handle, char *buf, int buflen);</code> </p>
<p> <code>int nodeupdown_get_down_nodes_string(nodeupdown_t handle, char *buf, int buflen);</code> </p>
<p> <code>int nodeupdown_get_up_nodes_list(nodeupdown_t handle, char **list, int len);</code> </p>
<p> <code>int nodeupdown_get_down_nodes_list(nodeupdown_t handle, char **list, int len);</code> </p>
<p> <code>int nodeupdown_is_node_up(nodeupdown_t handle, const char *node);</code> </p>
<p> <code>int nodeupdown_is_node_down(nodeupdown_t handle, const char *node);</code> </p>
<p> <code>int nodeupdown_up_count(nodeupdown_t handle);</code> </p>
<p> <code>int nodeupdown_down_count(nodeupdown_t handle);</code> </p>
<p> <code>int nodeupdown_last_up_time(nodeupdown_t handle, const char *node, unsigned int *last_up_time);</code> </p>
<p> <code>int nodeupdown_nodelist_create(nodeupdown_t handle, char ***list);</code> </p>
<p> <code>int nodeupdown_nodelist_clear(nodeupdown_t handle, char **list);</code> </p>
<p> <code>int nodeupdown_nodelist_destroy(nodeupdown_t handle, char **list);</code> </p>
<h2>DESCRIPTION</h2>
<p> The nodeupdown library functions are a set of functions that interacts with a particular backend tool and a clusterlist database to determine if the nodes of a cluster are up or down. See below for additional information on backend modules and clusterlist modules to learn about which backend tool and clusterlist database format is used. </p>
<p> For API information, please see the individual manpages for each of the functions above, or read the comments written in /usr/include/nodeupdown.h. Please see the <code><a href="/docs/linux/man/5-nodeupdown-conf/">nodeupdown.conf</a></code>(5) manpage for information about the nodeupdown configuration file. </p>
<h2>BACKEND MODULES</h2>
<p> The nodeupdown library loads a backend module, which uses a particular backend tool, to gather up/down info for the nodeupdown library. By default, the following backend tools are searched for by nodeupdown in the following order: </p>
<p> cerebro &#8211; See <a rel="nofollow" href="http://cerebro.sourceforge.net">http://cerebro.sourceforge.net</a> for more information. </p>
<p> ganglia &#8211; See <a rel="nofollow" href="http://ganglia.sourceforge.net">http://ganglia.sourceforge.net</a> for more information. </p>
<p> pingd &#8211; Simple pingd daemon. See <code><a href="/docs/linux/man/8-pingd/">pingd</a>(8)</code> </p>
<p> openib &#8211; See <a rel="nofollow" href="http://openib.org/">http://openib.org/</a> </p>
<p> If none of the above are found, the nodeupdown library will search for a backend module in /usr/lib64/nodeupdown until one is found. </p>
<h2>CLUSTERLIST MODULES</h2>
<p> The nodeupdown library loads a clusterlist module to obtain a list of all cluster nodes. There are several possible clusterlist formats that can be parsed. By default, the following clusterlist modules are searched for by nodeupdown in the following order: </p>
<p> genders &#8211; Uses a genders database and the genders library to determine all nodes in the cluster. See <a rel="nofollow" href="http://genders.sourceforge.net.">http://genders.sourceforge.net.</a><br />
 hostsfile &#8211; Uses a file that lists the hostname of every node in the cluster on a separate line. The default hostsfile is /etc/hostsfile. </p>
<p> If none of the above are found, the nodeupdown library will search for a clusterlist module in /usr/lib64/nodeupdown. If none are found, a default behavior will be implemented by the nodeupdown library. </p>
<h2>CONFIG MODULES</h2>
<p> The nodeupdown library optionally loads a configuration module, which can be used to define the default values used in <code><a href="/docs/linux/man/3-nodeupdown_load_data/">nodeupdown_load_data</a>(3).</code> The configuration module is primarily used for ease of configuring a large cluster of nodes, rather than writing and distributing multiple configuration files throughout a cluster. By default, the following configuration modules are searched for by nodeupdown in the following order: </p>
<p> None built by default </p>
<p> If none of the above are found, the nodeupdown library will search for a config module in /usr/lib64/nodeupdown. The nodeupdown configuration file takes precedence over the configuration module. When neither are in use, defaults are supplied by the backend tool. </p>
<h2>FILES</h2>
<p> /usr/include/nodeupdown.h</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-nodeupdown_handle_create/">nodeupdown_handle_create</a>(3), <a href="/docs/linux/man/3-nodeupdown_load_data/">nodeupdown_load_data</a>(3), <a href="/docs/linux/man/3-nodeupdown_handle_destroy/">nodeupdown_handle_destroy</a>(3), <a href="/docs/linux/man/3-nodeupdown_errnum/">nodeupdown_errnum</a>(3), <a href="/docs/linux/man/3-nodeupdown_strerror/">nodeupdown_strerror</a>(3), <a href="/docs/linux/man/3-nodeupdown_errormsg/">nodeupdown_errormsg</a>(3), <a href="/docs/linux/man/3-nodeupdown_perror/">nodeupdown_perror</a>(3), <a href="/docs/linux/man/3-nodeupdown_get_up_nodes_string/">nodeupdown_get_up_nodes_string</a>(3), <a href="/docs/linux/man/3-nodeupdown_get_down_nodes_string/">nodeupdown_get_down_nodes_string</a>(3), <a href="/docs/linux/man/3-nodeupdown_get_up_nodes_list/">nodeupdown_get_up_nodes_list</a>(3), <a href="/docs/linux/man/3-nodeupdown_get_down_nodes_list/">nodeupdown_get_down_nodes_list</a>(3), <a href="/docs/linux/man/3-nodeupdown_is_node_up/">nodeupdown_is_node_up</a>(3), <a href="/docs/linux/man/3-nodeupdown_is_node_down/">nodeupdown_is_node_down</a>(3), <a href="/docs/linux/man/3-nodeupdown_up_count/">nodeupdown_up_count</a>(3), <a href="/docs/linux/man/3-nodeupdown_down_count/">nodeupdown_down_count</a>(3), <a href="/docs/linux/man/3-nodeupdown_last_up_time/">nodeupdown_last_up_time</a>(3), <a href="/docs/linux/man/3-nodeupdown_nodelist_create/">nodeupdown_nodelist_create</a>(3), <a href="/docs/linux/man/3-nodeupdown_nodelist_clear/">nodeupdown_nodelist_clear</a>(3), <a href="/docs/linux/man/3-nodeupdown_nodelist_destroy/">nodeupdown_nodelist_destroy</a>(3), <a href="/docs/linux/man/5-nodeupdown-conf/">nodeupdown.conf</a>(5) </p>
<h2>Index</h2>
