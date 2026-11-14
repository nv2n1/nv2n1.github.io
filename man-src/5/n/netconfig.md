---
title: "netconfig(5)"
name: "netconfig"
section: "5"
letter: "n"
url: "/docs/linux/man/5-netconfig/"
description: "netconfig – network configuration data base"
---

<p><code>netconfig</code> &#8211; network configuration data base</p>
<h2>Synopsis</h2>
<p>/etc/netconfig</p>
<h2>Description</h2>
<p>The <code>netconfig</code> file defines a list of &#8220;transport names&#8221; describing their semantics and protocol. In Fx , this file is only used by the RPC library code. Entries have the following format: <i>network_id semantics flags family protoname device libraries</i> Entries consist of the following fields:</p>
<dl>
<dt><i>network_id</i></p>
<dd>The name of the transport described.</p>
<dt><i>semantics</i></p>
<dd>Describes the semantics of the transport. This can be one of:</p>
<dl>
<dt><code>tpi_clts</code></p>
<dd>Connectionless transport.</p>
<dt><code>tpi_cots</code></p>
<dd>Connection-oriented transport</p>
<dt><code>tpi_cots_ord</code></p>
<dd>Connection-oriented, ordered transport.</p>
<dt><code>tpi_raw</code></p>
<dd>A raw connection.</dl>
<dt><i>flags</i></p>
<dd>This field is either blank (specified by &#8220;<code>&#8211;</code> &#8221; or contains a &#8220;<code>v</code> &#8221; meaning visible to the <a href="/docs/linux/man/3-getnetconfig/">getnetconfig</a>(3) function.</p>
<dt><i>family</i></p>
<dd>The protocol family of the transport. This is currently one of:</p>
<dl>
<dt><code>inet6</code></p>
<dd>The IPv6 (<code>PF_INET6</code> ) family of protocols.</p>
<dt><code>inet</code></p>
<dd>The IPv4 (<code>PF_INET</code> ) family of protocols.</p>
<dt><code>loopback</code></p>
<dd>The <code>PF_LOCAL</code> protocol family.</dl>
<dt><i>protoname</i></p>
<dd>The name of the protocol used for this transport. Can currently be either <code>udp</code> <code>tcp</code> or empty.</p>
<dt><i>device</i></p>
<dd>This field is always empty in Fx .</p>
<dt><i>libraries</i></p>
<dd>This field is always empty in Fx .</dl>
<p> The order of entries in this file will determine which transport will be preferred by the RPC library code, given a match on a specified network type. For example, if a sample network config file would look like this: </p>
<blockquote>
<pre>udp6 tpi_clts v inet6 udp - -
tcp6 tpi_cots_ord v inet6 tcp - -
udp tpi_clts v inet udp - -
tcp tpi_cots_ord v inet tcp - -
rawip tpi_raw - inet - - -
local tpi_cots_ord - loopback - - -</pre>
</blockquote>
<p> then using the network type <code>udp</code> in calls to the RPC library function (see <a href="/docs/linux/man/3-rpc/">rpc</a>(3)) will make the code first try <code>udp6</code> and then <code>udp</code> </p>
<pre><code>getnetconfig(3)

    and associated functions will parse this file and return structures of
    the following format :

    struct netconfig {
    char *nc_netid;             /* Network ID */
    unsigned long nc_semantics; /* Semantics (see below) */
    unsigned long nc_flag;      /* Flags (see below) */
    char *nc_protofmly;         /* Protocol family */
    char *nc_proto;             /* Protocol name */
    char *nc_device;            /* Network device pathname (unused) */
    unsigned long nc_nlookups;  /* Number of lookup libs (unused) */
    char **nc_lookups;          /* Names of the libraries (unused) */
    unsigned long nc_unused[9]; /* reserved */
};</code></pre>
<h2>Files</h2>
<dl>
<dt><code>/etc/netconfig </code></p>
<dd></dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-getnetconfig/">getnetconfig</a>(3), <a href="/docs/linux/man/3-getnetpath/">getnetpath</a>(3) </p>
