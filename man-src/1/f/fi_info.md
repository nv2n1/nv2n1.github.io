---
title: "fi_info(1)"
name: "fi_info"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fi_info/"
---

<h2 class="name">NAME</h2>
 

 

 fi_info - Simple utility to query for fabric interfaces 

<h2>SYNOPSIS</h2>

<dl>
<dt>
<dd> <pre><code>
&amp;nbsp;
fi_info &amp;nbsp;
[OPTIONS]
</code></pre></dl>

<h2>DESCRIPTION</h2>

 

 The fi_info utility can be used to query for available fabric interfaces. The utility supports filtering based on a number of options such as endpoint type, provider name, or supported modes. Additionally, fi_info can also be used to discover the environment variables that can be used to tune provider specific parameters. If no filters are specified, then all available fabric interfaces for all providers and endpoint types will be returned.

<h2>OPTIONS</h2>

<h3>Filtering</h3>

 

 -n, --node=&lt;NAME&gt; : Node name or address used to filter interfaces. Only interfaces which can reach the given node or address will respond. 

 -P, --port=&lt;PORT&gt; : Port number used to filter interfaces. 

 -c, --caps=&lt;CAP1|CAP2&gt;.. : Pipe separated list of capabilities used to filter interfaces. Only interfaces supporting all of the given capabilities will respond. For more information on capabilities, see <a HREF="/docs/linux/man/3-fi_getinfo/">fi_getinfo</a>(3). 

 -m, --mode=&lt;MOD1|MOD2&gt;.. : Pipe separated list of modes used to filter interfaces. Only interfaces supporting all of the given modes will respond. For more information on, modes see <a HREF="/docs/linux/man/3-fi_getinfo/">fi_getinfo</a>(3). 

 -t, --ep_type=&lt;EPTYPE&gt; : Specifies the type of fabric interface communication desired. For example, specifying FI_EP_DGRAM would return only interfaces which support unreliable datagram. For more information on endpoint types, see <a HREF="/docs/linux/man/3-fi_endpoint/">fi_endpoint</a>(3). 

 -a, --addr_format=&lt;FMT&gt; : Filter fabric interfaces by their address format. For example, specifying FI_SOCKADDR_IN would return only interfaces which use sockaddr_in structures for addressing. For more information on address formats, see <a HREF="/docs/linux/man/3-fi_getinfo/">fi_getinfo</a>(3). 

 -p, --provider=&lt;PROV&gt; : Filter fabric interfaces by the provider implementation. For a list of providers, see the --list option. 

 -d, --domain=&lt;DOMAIN&gt; : Filter interfaces to only those with the given domain name. 

 -f, --fabric=&lt;FABRIC&gt; : Filter interfaces to only those with the given fabric name.

<h3>Discovery</h3>

 

 -e, --env : List libfabric related environment levels which can be used to enable extra configuration or tuning. 

 -l, --list : List available libfabric providers. 

 -v, --verbose : By default, fi_info will display a summary of each of the interfaces discovered. If the verbose option is enabled, then all of the contents of the fi_info structure are displayed. For more information on the data contained in the fi_info structure, see <a HREF="/docs/linux/man/3-fi_getinfo/">fi_getinfo</a>(3). 

 --version : Display versioning information.

<h2>USAGE EXAMPLES</h2>

<dl>
<dt>
<dd> <pre>
$&nbsp;fi_info -n 30.0.11.1 -p usnic -t FI_EP_DGRAM
</pre></dl>
 

 This will respond with all fabric interfaces that can reach address 30.0.11.1 using endpoint type FI_EP_DGRAM with the usNIC provider.

<h2>OUTPUT</h2>

 

 By default fi_info will output a summary of the fabric interfaces discovered:
<dl>
<dt>
<dd> <pre><code>
$ &amp;nbsp;
./ fi_info - n 30.0.11.1 - p usnic - t FI_EP_DGRAM provider : usnic &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
fabric : 30.0.11.0 / 24 &amp; nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
domain : usnic_2
             &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
version : 1.0 &amp; nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
type : FI_EP_DGRAM
           &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
protocol : FI_PROTO_UDP
</code></pre></dl>
 

 To see the full fi_info structure, specify the -v option.

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/3-fi_getinfo/">fi_getinfo</a>(3), <a HREF="/docs/linux/man/3-fi_endpoint/">fi_endpoint</a>(3)

<h2>AUTHORS</h2>

 OpenFabrics. 

<h2>Index</h2>


