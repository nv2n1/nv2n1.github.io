---
title: "ib_acme(1)"
name: "ib_acme"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ib_acme/"
---

<h2>NAME</h2>

 ib_acme - test and configuration utility for the IB ACM

<h2>SYNOPSIS</h2>

 

 <pre><code>
ib_acme[-f addr_format][-s src_addr] - d dest_addr[-v][-c][-e][-P][-S svc_addr][-C repetitions]
</code></pre> <pre><code>
ib_acme[-A[addr_file]][-O[opt_file]][-D dest_dir][-V]
</code></pre>

<h2>DESCRIPTION</h2>

 ib_acme provides assistance configuring and testing the ibacm service. The first usage of the service will test that the ibacm is running and operating correctly. The second usage model will automatically create address and configuration files for the ibacm service.

<h2>OPTIONS</h2>

<dl>
<dt>-f addr_format
<dd> Specifies the format of the src_addr and dest_addr parameters. Valid address formats are: 'i' ip address, 'n' host name, 'l' lid, 'g' gid, and 'u' unspecified. If the -f option is omitted, an unspecified address format is assumed. ib_acme will use getaddrinfo or other mechanisms to determine which format the address uses.
<dt>-s src_addr
<dd> Specifies the local source address of the path to resolve. The source address can be an IP address, system network name, or LID, as indicated by the addr_format option.
<dt>-d dest_addr
<dd> Specifies the destination address of the path to resolve. The destination address can be an IP address, system network name, or LID, as indicated by the addr_format option.
<dt>-v
<dd> Indicates that the resolved path information should be verified with the active IB SA. Use of the -v option provides a sanity check that resolved path information is usable given the current cluster configuration.
<dt>-c
<dd> Instructs the ACM service to only returned information that currently resides in its local cache.
<dt>-e [N]
<dd> Displays one (N = 1, 2, ...) or all endpoints (N = 0 or not present).
<dt>-P [opt]
<dd> Queries performance data from the destination service. Valid options are: &quot;col&quot; for outputting combined data in column format, &quot;N&quot; (N = 1, 2, ...) for outputing data for a specific endpoint N, &quot;all&quot; for outputting data for all endpoints, and &quot;s&quot; for outputting data for a specific endpoint with the address given by the -s option.
<dt>-S svc_addr
<dd> address of ACM service, default: local service
<dt>-C repetitions
<dd> number of repetitions to perform resolution. Used to measure performance of ACM cache lookups. Defaults to 1.
<dt>-A [addr_file]
<dd> With this option, the ib_acme utility automatically generates the address configuration file ibacm_addr.cfg. The generated file is constructed using the system host name.
<dt>-O [opt_file]
<dd> With this option, the ib_acme utility automatically generates the option configuration file ibacm_opts.cfg. The generated file is currently generated using static information.
<dt>-D dest_dir
<dd> Specify the destination directory for the output files.
<dt>-V
<dd> Enables verbose output. When combined with -A or -O options, ib_acme will display additional details, such as generated address information saved to the ibacm_addr.cfg file.</dl>

<h2>NOTES</h2>

 The ib_acme utility performs two main functions. With the -A and -O options, it automatically generates address or options configuration files. The generated files are text based and may be edited. These options are intended to provide a simple way to configure address and option information on all nodes on a cluster. 

 The other function of the ib_acme utility is to test the ibacm service, including helping to verify that the service is usable given the current cluster configuration. The ib_acme utility can resolve IP addresses, network names, or IB LIDs into a path record. It can then compare that path record against one obtained by the SA. When used to test the ibacm service, the ib_acme utility has the side effect of loading the ibacm caches. 

 Multiple, numerical destinations can be specified by adding brackets [] to the end of a base destination name or address. Users may specify a list of numerical ranges inside the brackets using the following example as a guide: node[1-3,5,7-8]. This will result in testing node1, node2, node3, node5, node7, and node8.

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/7-ibacm/">ibacm</a>(7), <a HREF="/docs/linux/man/1-ibacm/">ibacm</a>(1) 

<h2>Index</h2>


