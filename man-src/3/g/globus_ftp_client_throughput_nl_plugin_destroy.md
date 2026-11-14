---
title: "globus_ftp_client_throughput_nl_plugin_destroy(3)"
name: "globus_ftp_client_throughput_nl_plugin_destroy"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_ftp_client_throughput_nl_plugin_destroy/"
description: "Netlogger Throughput Plugin –"
---

<h2 class="name">NAME</h2>
<p> Netlogger Throughput Plugin &#8211; </p>
<h3>Macros</h3>
<p> #define <code>GLOBUS_FTP_CLIENT_THROUGHPUT_NL_PLUGIN_MODULE</code> (&amp;globus_i_ftp_client_throughput_nl_plugin_module) </p>
<h3>Functions</h3>
<p> globus_result_t <code>globus_ftp_client_throughput_nl_plugin_init</code> (<code>globus_ftp_client_plugin_t</code> *plugin, const char *nl_url, const char *prog_name, const char *opaque_string) </p>
<p> globus_result_t <code>globus_ftp_client_throughput_nl_plugin_init_with_handle</code> (<code>globus_ftp_client_plugin_t</code> *plugin, NLhandle *nl_handle, const char *opaque_string) </p>
<p> globus_result_t <code>globus_ftp_client_throughput_nl_plugin_destroy</code> (<code>globus_ftp_client_plugin_t</code> *plugin) </p>
<p> globus_result_t <code>globus_ftp_client_throughput_nl_plugin_set_callbacks</code> (<code>globus_ftp_client_plugin_t</code> *plugin, <code>globus_ftp_client_throughput_plugin_begin_cb_t</code> begin_cb, <code>globus_ftp_client_throughput_plugin_stripe_cb_t</code> per_stripe_cb, <code>globus_ftp_client_throughput_plugin_total_cb_t</code> total_cb, <code>globus_ftp_client_throughput_plugin_complete_cb_t</code> complete_cb, void *user_specific) </p>
<h2>Detailed Description</h2>
<p> This plugin allows a user to easily use the throughput plugin to log performance data vi Netlogger. </p>
<p> The plugin will log the following Event Types with its coressponding info </p>
<p> TransferPerfTotal : This event type will be sent everytime a throughput plugin total callback is received. </p>
<dl>
<dt>&bull;</p>
<dd> URL.SOURCE &lt;string&gt; Source url of transfer</p>
<dt>&bull;</p>
<dd> URL.DEST &lt;string&gt; Dest url of transfer</p>
<dt>&bull;</p>
<dd> BYTES &lt;int&gt; Total bytes transferred thus far</p>
<dt>&bull;</p>
<dd> BW.CURRENT &lt;float&gt; Current (instantaneous) bandwidth</p>
<dt>&bull;</p>
<dd> BW.AVG &lt;float&gt; Average (instantaneous) bandwidth</dl>
<p> TransferPerfStripe : This event type will be sent everytime a throughput plugin stripe callback is received. </p>
<dl>
<dt>&bull;</p>
<dd> URL.SOURCE &lt;string&gt; Source url of transfer</p>
<dt>&bull;</p>
<dd> URL.DEST &lt;string&gt; Dest url of transfer</p>
<dt>&bull;</p>
<dd> INDEX &lt;int&gt; The stripe index the event applies to</p>
<dt>&bull;</p>
<dd> BYTES &lt;int&gt; Total bytes transferred thus far on this stripe</p>
<dt>&bull;</p>
<dd> BW.CURRENT &lt;float&gt; Current (instantaneous) bandwidth on this stripe</p>
<dt>&bull;</p>
<dd> BW.AVG &lt;float&gt; Average (instantaneous) bandwidth on this stripe</dl>
<p> TransferBegin : This event type will be sent everytime a throughput plugin begin callback is received. </p>
<dl>
<dt>&bull;</p>
<dd> URL.SOURCE &lt;string&gt; Source url of transfer</p>
<dt>&bull;</p>
<dd> URL.DEST &lt;string&gt; Dest url of transfer</dl>
<p> TransferEnd : This event type will be sent everytime a throughput plugin complete callback is received. </p>
<dl>
<dt>&bull;</p>
<dd> SUCCESS &lt;bool&gt; Completion status</dl>
<h2>Macro Definition Documentation</h2>
<h3>#define GLOBUS_FTP_CLIENT_THROUGHPUT_NL_PLUGIN_MODULE (&amp;globus_i_ftp_client_throughput_nl_plugin_module)</h3>
<p> Module descriptor</p>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_ftp_client_throughput_nl_plugin_destroy (<code>globus_ftp_client_plugin_t</code> *plugin)</h3>
<p> Destroy netlogger wrapped throughput plugin </p>
<p> Frees up memory associated with plugin </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>plugin</i> plugin previously initialized with init (above)</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> GLOBUS_SUCCESS</p>
<dt>&bull;</p>
<dd> Error on NULL plugin</dl>
</dl>
<h3>globus_result_t globus_ftp_client_throughput_nl_plugin_init (<code>globus_ftp_client_plugin_t</code> *plugin, const char *nl_url, const char *prog_name, const char *opaque_string)</h3>
<p> Initialize netlogger wrapped throughput plugin </p>
<p> This will initialize a netlogger wrapped throughput plugin. Note that the nl_url may be NULL. Regardless of what nl_host is set to, if the env variable NL_DEST_ENV is set, logging will always occur to that location. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>plugin</i> a plugin to be initialized<br />
 <i>nl_url</i> the url to log to (May be NULL) Valid urls are: file://tmp/netlog.log x-<a href="netlog://host[:port]">netlog://host[:port]</a> x-<a href="syslog://localhost">syslog://localhost</a><br />
 <i>prog_name</i> This is used as the prog name in the NetLoggerOpen call<br />
 <i>opaque_string</i> this is an opaque string that will be inserted into all logged statements. (may be NULL)</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Error on NULL plugin or failure to init throughput plugin</p>
<dt>&bull;</p>
<dd> Error on NetLogger open</p>
<dt>&bull;</p>
<dd> GLOBUS_SUCCESS</dl>
</dl>
<h3>globus_result_t globus_ftp_client_throughput_nl_plugin_init_with_handle (<code>globus_ftp_client_plugin_t</code> *plugin, NLhandle *nl_handle, const char *opaque_string)</h3>
<p> Initialize netlogger wrapped throughput plugin </p>
<p> This will initialize a netlogger wrapped throughput plugin. Instead of passing a NetLogger url as in the plain init func, you can pass in a previously &#8216;Open&#8217;ed NLhandle. This handle will not be destroyed by this plugin. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>plugin</i> a plugin to be initialized<br />
 <i>nl_handle</i> a previously opened NetLogger handle<br />
 <i>opaque_string</i> this is an opaque string that will be inserted into all logged statements. (may be NULL)</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Error on NULL plugin or failure to init throughput plugin</p>
<dt>&bull;</p>
<dd> Error on NetLogger open</p>
<dt>&bull;</p>
<dd> GLOBUS_SUCCESS</dl>
</dl>
<h3>globus_result_t globus_ftp_client_throughput_nl_plugin_set_callbacks (<code>globus_ftp_client_plugin_t</code> *plugin, <code>globus_ftp_client_throughput_plugin_begin_cb_t</code>begin_cb, <code>globus_ftp_client_throughput_plugin_stripe_cb_t</code>per_stripe_cb, <code>globus_ftp_client_throughput_plugin_total_cb_t</code>total_cb, <code>globus_ftp_client_throughput_plugin_complete_cb_t</code>complete_cb, void *user_specific)</h3>
<p> Receive throughput callbacks </p>
<p> You can still get the automatic netlogging of throughput along with receiving the same throughput callbacks that the throughput plugin provides by using this function to set these callbacks. Note that the callbacks are defined the same as in the throughput plugin </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>plugin</i><br />
 <i>begin_cb</i> the callback to be called upon the start of a transfer<br />
 <i>per_stripe_cb</i> the callback to be called every time updated throughput info is available for a given stripe<br />
 <i>total_cb</i> the callback to be called every time updated throughput info is available for any stripe<br />
 <i>complete_cb</i> the callback to be called to indicate transfer completion<br />
 <i>user_specific</i> a pointer to some user specific data that will be provided to all callbacks</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Error on NULL or invalid plugin</p>
<dt>&bull;</p>
<dd> GLOBUS_SUCCESS</dl>
</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>Throughput Performance Plugin</code></dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_ftp_client from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAM">Author</a></p>
<dd></dl>
