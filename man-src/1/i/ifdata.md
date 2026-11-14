---
title: "ifdata(1)"
name: "ifdata"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ifdata/"
description: "ifdata – get network interface info without parsing ifconfig output"
---

<h2 class="name">NAME</h2>
<p> ifdata &#8211; get network interface info without parsing ifconfig output </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>ifdata</code> [options] {<i>iface</i>}</dl>
<h2>DESCRIPTION</h2>
<p> <code>ifdata</code></p>
<dd>can be used to check for the existence of a network interface, or to get information about the interface, such as its IP address. Unlike <code>ifconfig</code> or <code>ip</code>, <code>ifdata</code> has simple to parse output that is designed to be easily used by a shell script.</p>
<h2>OPTIONS</h2>
<p> <code>-h</code></p>
<dl>
<dt>
<dd> Print out a help summary.</dl>
<p> <code>-e</code></p>
<dl>
<dt>
<dd> Test to see if the interface exists, exit nonzero if it does not.</dl>
<p> <code>-p</code></p>
<dl>
<dt>
<dd> Prints out the whole configuration of the interface.</dl>
<p> <code>-pe</code></p>
<dl>
<dt>
<dd> Prints &quot;yes&quot; or &quot;no&quot; if the interface exists or not.</dl>
<p> <code>-pa</code></p>
<dl>
<dt>
<dd> Prints the IPv4 address of the interface.</dl>
<p> <code>-pn</code></p>
<dl>
<dt>
<dd> Prints the netmask of the interface.</dl>
<p> <code>-pN</code></p>
<dl>
<dt>
<dd> Prints the network address of the interface.</dl>
<p> <code>-pb</code></p>
<dl>
<dt>
<dd> Prints the broadcast address of the interface.</dl>
<p> <code>-pm</code></p>
<dl>
<dt>
<dd> Prints the MTU of the interface.</dl>
<p> Following options are Linux only. </p>
<p> <code>-ph</code></p>
<dl>
<dt>
<dd> Prints the hardware address of the interface. Exit with a failure exit code if there is not hardware address for the given network interface.</dl>
<p> <code>-pf</code></p>
<dl>
<dt>
<dd> Prints the flags of the interface.</dl>
<p> <code>-si</code></p>
<dl>
<dt>
<dd> Prints out all the input statistics of the interface.</dl>
<p> <code>-sip</code></p>
<dl>
<dt>
<dd> Prints the number of input packets.</dl>
<p> <code>-sib</code></p>
<dl>
<dt>
<dd> Prints the number of input bytes.</dl>
<p> <code>-sie</code></p>
<dl>
<dt>
<dd> Prints the number of input errors.</dl>
<p> <code>-sid</code></p>
<dl>
<dt>
<dd> Prints the number of dropped input packets.</dl>
<p> <code>-sif</code></p>
<dl>
<dt>
<dd> Prints the number of input fifo overruns.</dl>
<p> <code>-sic</code></p>
<dl>
<dt>
<dd> Print the number of compressed input packets.</dl>
<p> <code>-sim</code></p>
<dl>
<dt>
<dd> Prints the number of input multicast packets.</dl>
<p> <code>-so</code></p>
<dl>
<dt>
<dd> Prints out all the output statistics of the interface.</dl>
<p> <code>-sop</code></p>
<dl>
<dt>
<dd> Prints the number of output packets.</dl>
<p> <code>-sob</code></p>
<dl>
<dt>
<dd> Prints the number of output bytes.</dl>
<p> <code>-soe</code></p>
<dl>
<dt>
<dd> Prints the number of output errors.</dl>
<p> <code>-sod</code></p>
<dl>
<dt>
<dd> Prints the number of dropped output packets.</dl>
<p> <code>-sof</code></p>
<dl>
<dt>
<dd> Prints the number of output fifo overruns.</dl>
<p> <code>-sox</code></p>
<dl>
<dt>
<dd> Print the number of output collisions.</dl>
<p> <code>-soc</code></p>
<dl>
<dt>
<dd> Prints the number of output carrier losses.</dl>
<p> <code>-som</code></p>
<dl>
<dt>
<dd> Prints the number of output multicast packets.</dl>
<p> <code>-bips</code></p>
<dl>
<dt>
<dd> Prints the number of bytes of incoming traffic measured in one second.</dl>
<p> <code>-bops</code></p>
<dl>
<dt>
<dd> Prints the number of bytes of outgoing traffic measured in one second.</dl>
<h2>AUTHOR</h2>
<p> Benjamin BAYART </p>
<h2>Index</h2>
