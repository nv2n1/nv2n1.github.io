---
title: "statgrab(3)"
name: "statgrab"
section: "3"
letter: "s"
url: "/docs/linux/man/3-statgrab/"
description: "statgrab, libstatgrab – get system statistics"
---

<p>statgrab, libstatgrab &#8211; get system statistics</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;statgrab.h&gt;
</code></pre>
<p> sg_error <code>sg_init</code> (int <i>ignore_init_errors</i>); sg_error <code>sg_shutdown</code> (void); sg_error <code>sg_drop_privileges</code> (void); sg_error <code>sg_get_error</code> (void); const char *sg_get_error_arg</p>
<p>    (void);<br />
int sg_get_error_errno</p>
<p>    (void);<br />
const char *sg_str_error</p>
<p>    (sg_error code); sg_error <code>sg_get_error_details</code> (sg_error_details *<i>err_details</i>); char *sg_strperror</p>
<p>    (char **buf, const sg_error_details *const err_details);<br />
size_t sg_get_nelements</p>
<p>    (const void *data); sg_error <code>sg_free_stats_buf</code> (void *<i>data</i>); sg_error <code>sg_lock_mutex</code> (const char *<i>mutex_name</i>); sg_error <code>sg_unlock_mutex</code> (const char *<i>mutex_name</i>); sg_cpu_percents *<code>sg_get_cpu_percents</code> (void); sg_cpu_percents *<code>sg_get_cpu_percents_of</code> (sg_cpu_percent_source <i>cps</i>); sg_cpu_percents *<code>sg_get_cpu_percents_r</code> (const sg_cpu_stats *<i>whereof</i>); void sg_free_cpu_percents</p>
<p>    (sg_cpu_percents *data); sg_cpu_stats *<code>sg_get_cpu_stats</code> (void); sg_cpu_stats *<code>sg_get_cpu_stats_diff</code> (void); sg_cpu_stats *<code>sg_get_cpu_stats_r</code> (void); sg_cpu_stats *<code>sg_get_cpu_stats_diff_between</code> (const sg_cpu_stats *<i>cpu_now</i>, const sg_cpu_stats *<i>cpu_last</i>); sg_error <code>sg_free_cpu_stats</code> (sg_cpu_stats *<i>data</i>); sg_disk_io_stats *<code>sg_get_disk_io_stats</code> (size_t *<i>entries</i>); sg_disk_io_stats *<code>sg_get_disk_io_stats_r</code> (size_t *<i>entries</i>); sg_disk_io_stats *<code>sg_get_disk_io_stats_diff</code> (size_t *<i>entries</i>); sg_disk_io_stats *<code>sg_get_disk_io_stats_diff_between</code> (const sg_disk_io_stats *<i>cur</i>, const sg_disk_io_stats *<i>last</i>, size_t *<i>entries</i>); sg_error <code>sg_free_disk_io_stats</code> (sg_disk_io_stats *<i>data</i>); sg_fs_stats *<code>sg_get_fs_stats</code> (size_t *<i>entries</i>); sg_fs_stats *<code>sg_get_fs_stats_r</code> (size_t *<i>entries</i>); sg_error <code>sg_free_fs_stats</code> (sg_fs_stats *<i>data</i>); </p>
<pre><code>const char **sg_get_valid_filesystems

    (size_t *entries);</code></pre>
<p> sg_error <code>sg_set_valid_filesystems</code> (const char *<i>valid_fs</i>[]); sg_host_info *<code>sg_get_host_info</code> (void); sg_host_info *<code>sg_get_host_info_r</code> (void); sg_error <code>sg_free_host_info</code> (sg_host_info *<i>data</i>); sg_load_stats *<code>sg_get_load_stats</code> (void); sg_load_stats *<code>sg_get_load_stats</code> (void); sg_error <code>sg_free_load_stats</code> (sg_load_stats *<i>data</i>); sg_mem_stats *<code>sg_get_mem_stats</code> (void); sg_mem_stats *<code>sg_get_mem_stats_r</code> (void); sg_error <code>sg_free_mem_stats</code> (sg_mem_stats *<i>data</i>); sg_swap_stats *<code>sg_get_swap_stats</code> (void); sg_swap_stats *<code>sg_get_swap_stats_r</code> (void); sg_error <code>sg_free_swap_stats</code> (sg_swap_stats *<i>data</i>); sg_network_iface_stats *<code>sg_get_network_iface_stats</code> (size_t *<i>entries</i>); sg_network_iface_stats *<code>sg_get_network_iface_stats_r</code> (size_t *<i>entries</i>); sg_error <code>sg_free_network_iface_stats</code> (sg_network_iface_stats *<i>data</i>); sg_network_io_stats *<code>sg_get_network_io_stats</code> (size_t *<i>entries</i>); sg_network_io_stats *<code>sg_get_network_io_stats_r</code> (size_t *<i>entries</i>); sg_network_io_stats *<code>sg_get_network_io_stats_diff</code> (size_t *<i>entries</i>); sg_network_io_stats *<code>sg_get_network_io_stats_diff_between</code> (const sg_network_io_stats *<i>cur</i>, const sg_network_io_stats *<i>last</i>, size_t *<i>entries</i>); sg_error <code>sg_free_network_io_stats</code> (sg_network_iface_stats *<i>data</i>); sg_page_stats *<code>sg_get_page_stats</code> (void); sg_page_stats *<code>sg_get_page_stats_r</code> (void); sg_page_stats *<code>sg_get_page_stats_diff</code> (void); sg_page_stats *<code>sg_get_page_stats_diff_between</code> (const sg_page_stats *<i>cur</i>, const sg_page_stats *<i>last</i>); sg_error <code>sg_free_page_stats</code> (sg_page_stats *<i>data</i>); sg_process_stats *<code>sg_get_process_stats</code> (size_t *<i>entries</i>); sg_process_stats *<code>sg_get_process_stats_r</code> (size_t *<i>entries</i>); sg_error <code>sg_free_process_stats</code> (sg_process_stats *<i>data</i>); sg_process_count *<code>sg_get_process_count</code> (void); sg_process_count *<code>sg_get_process_count_of</code> (sg_process_count_source <i>pcs</i>); sg_process_count *<code>sg_get_process_count_r</code> (sg_process_stats const *<i>whereof</i>); sg_error <code>sg_free_process_count</code> (sg_process_count *<i>data</i>); sg_user_stats *<code>sg_get_user_stats</code> (size_t *<i>entries</i>); sg_user_stats *<code>sg_get_user_stats_r</code> (size_t *<i>entries</i>); sg_error <code>sg_free_user_stats</code> (sg_user_stats *<i>data</i>);</p>
<h2>Description</h2>
<p>The statgrab library provides a cross-platform interface to get several system statistics. System statistics aren&#8217;t standardised, so the statgrab library tries to choose the most important values over all supported operating systems. This implies that some values might not be available on every OS while some specific values are missing when there are no counterparts on any other OS. </p>
<p> The libstatgrab is organised in components, each for interrelated statistics. </p>
<table BORDER>
<tr VALIGN=top>
<td> component </td>
<td> statistics
</td>
</tr>
<tr VALIGN=top>
<td> cpu </td>
<td> sg_cpu_stats, sg_cpu_percents
</td>
</tr>
<tr VALIGN=top>
<td> disk </td>
<td> sg_disk_io_stats, sg_fs_stats
</td>
</tr>
<tr VALIGN=top>
<td> load </td>
<td> sg_load_stats
</td>
</tr>
<tr VALIGN=top>
<td> mem </td>
<td> sg_mem_stats
</td>
</tr>
<tr VALIGN=top>
<td> network </td>
<td> sg_network_io_stats, sg_network_iface_stats
</td>
</tr>
<tr VALIGN=top>
<td> os </td>
<td> sg_host_info
</td>
</tr>
<tr VALIGN=top>
<td> page </td>
<td> sg_page_stats
</td>
</tr>
<tr VALIGN=top>
<td> process </td>
<td> sg_process_stats, sg_process_count
</td>
</tr>
<tr VALIGN=top>
<td> swap </td>
<td> sg_swap_stats
</td>
</tr>
<tr VALIGN=top>
<td> user </td>
<td> sg_user_stats
</td>
</tr>
</table>
<p> The library was originally written to support the i-scream central monitoring system, but has since become a standalone package. It has been ported to work on Linux, NetBSD, FreeBSD, OpenBSD, DragonFly BSD, Solaris, HP-UX, AIX and Cygwin.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-sg_intro/">sg_intro</a></code>(3) <code><a href="/docs/linux/man/3-sg_get_cpu_stats/">sg_get_cpu_stats</a></code>(3) <code><a href="/docs/linux/man/3-sg_get_disk_io_stats/">sg_get_disk_io_stats</a></code>(3) <code><a href="/docs/linux/man/3-sg_get_fs_stats/">sg_get_fs_stats</a></code>(3) <code><a href="/docs/linux/man/3-sg_get_host_info/">sg_get_host_info</a></code>(3) <code><a href="/docs/linux/man/3-sg_get_load_stats/">sg_get_load_stats</a></code>(3) <code><a href="/docs/linux/man/3-sg_get_mem_stats/">sg_get_mem_stats</a></code>(3) <code><a href="/docs/linux/man/3-sg_get_network_io_stats/">sg_get_network_io_stats</a></code>(3) <code><a href="/docs/linux/man/3-sg_get_network_iface_stats/">sg_get_network_iface_stats</a></code>(3) <code><a href="/docs/linux/man/3-sg_get_page_stats/">sg_get_page_stats</a></code>(3) <code><a href="/docs/linux/man/3-sg_get_process_stats/">sg_get_process_stats</a></code>(3) <code><a href="/docs/linux/man/3-sg_get_swap_stats/">sg_get_swap_stats</a></code>(3) <code><a href="/docs/linux/man/3-sg_get_user_stats/">sg_get_user_stats</a></code>(3) <code><a href="/docs/linux/man/3-sg_get_error/">sg_get_error</a></code>(3) <code><a href="/docs/linux/man/3-sg_internal-intro/">sg_internal-intro</a></code>(3)</p>
<h2>Website</h2>
<p>&lt;<a rel="nofollow" href="http://www.i-scream.org/libstatgrab/">http://www.i-scream.org/libstatgrab/</a>&gt;</p>
