---
title: "inetutils-ifconfig(1)"
name: "inetutils-ifconfig"
section: "1"
letter: "i"
url: "/docs/linux/man/1-inetutils-ifconfig/"
description: "ifconfig – configure network interfaces"
---

<p>GNU Network Utilities</p>
<h2 class="name">NAME</h2>
<p> <code>ifconfig</code> &#8211; configure network interfaces </p>
<h2>SYNOPSIS</h2>
<p> <code>ifconfig</code> [<i>option &#8230;</i> ] <i>name</i> [<i>addr</i> ] [<code>broadcast </code><i>brdaddr</i> ] [<code>{ pointopoint | dstaddr } </code><i>dstaddr</i> ] [<code>netmask </code><i>mask</i> ] [<code>{ ether | hwaddr | lladdr } </code><i>macaddr</i> ] [<code>metric </code><i>n</i> ] [<code>mtu </code><i>n</i> ] [<code>txqueuelen </code><i>n</i> ] [<code>up | down</code> ] [<i>flags</i> ]</p>
<h2>DESCRIPTION</h2>
<p> Configure network interfaces. </p>
<p> Mandatory or optional arguments to long options are also mandatory or optional for any corresponding short options. </p>
<p> Known flags are: <code>allmulti , arp , automedia , broadcast , debug , dynamic , master</code> <code>multicast , pointopoint , portsel , promisc , slave , trailers , up</code> Prepending <code>no</code> to any of these flags will negate their effect.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a , -all</code></p>
<dd> Display all available interfaces.</p>
<dt><code>-A , -address </code><i>addr</i></p>
<dd> Set the interface address to <i>addr</i></p>
<dt><code>-B , -broadcast </code><i>addr</i></p>
<dd>
<dt><code>-b , -brdaddr </code><i>addr</i></p>
<dd> Set the broadcast address to <i>addr</i></p>
<dt><code>-d , -dstaddr </code><i>addr</i></p>
<dd>
<dt><code>-p , -peer </code><i>addr</i></p>
<dd> Set the destination (peer) address to <i>addr</i></p>
<dt><code>&#8211;up</code></p>
<dd> Activate the interface (default if address is given).</p>
<dt><code>&#8211;down</code></p>
<dd> Shut the interface down.</p>
<dt><code>-F , -flags </code><i>flag , </i>[<i>flag &#8230;</i> ]</p>
<dd> Set the interface flags.</p>
<dt><code>-i , -interface </code><i>name</i></p>
<dd> Configure the network interface <i>name</i></p>
<dt><code>-l , -list</code></p>
<dd> List the available or selected interfaces.</p>
<dt><code>-m , -netmask </code><i>mask</i></p>
<dd> Set the netmask to <i>mask</i></p>
<dt><code>&#8211;metric </code><i>n</i></p>
<dd> Set the interface metric to <i>n</i></p>
<dt><code>-M , -mtu </code><i>n</i></p>
<dd> Set the interface MTU to <i>n</i></p>
<dt><code>&#8211;format </code><i>format</i></p>
<dd> Select the output format; set to <code>help</code> for information.</p>
<dt><code>-s , -short</code></p>
<dd> Short output format.</p>
<dt><code>-v , -verbose</code></p>
<dd> Output information when configuring the interface.</p>
<dt><code>-? , -help</code></p>
<dd> Give this help list.</p>
<dt><code>&#8211;usage</code></p>
<dd> Give a short usage message.</p>
<dt><code>-V , -version</code></p>
<dd> Print program version.</dl>
<p> Linux-specific options:</p>
<dl>
<dt><code>-T , -txqlen </code><i>n</i></p>
<dd> Set the transmit queue length to <i>n</i></dl>
<h2>Index</h2>
