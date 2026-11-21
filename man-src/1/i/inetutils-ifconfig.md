---

title: "inetutils-ifconfig(1)"
name: "inetutils-ifconfig"
section: "1"
letter: "i"
url: "/docs/linux/man/1-inetutils-ifconfig/"
description: "ifconfig – configure network interfaces"
---

<p>GNU Network Utilities</p>
<p> <code>ifconfig</code> &#8211; configure network interfaces </p>
<p> <code>ifconfig</code> [<i>option &#8230;</i> ] <i>name</i> [<i>addr</i> ] [<code>broadcast </code><i>brdaddr</i> ] [<code>{ pointopoint | dstaddr } </code><i>dstaddr</i> ] [<code>netmask </code><i>mask</i> ] [<code>{ ether | hwaddr | lladdr } </code><i>macaddr</i> ] [<code>metric </code><i>n</i> ] [<code>mtu </code><i>n</i> ] [<code>txqueuelen </code><i>n</i> ] [<code>up | down</code> ] [<i>flags</i> ]</p>
<p> Configure network interfaces. </p>
<p> Mandatory or optional arguments to long options are also mandatory or optional for any corresponding short options. </p>
<p> Known flags are: <code>allmulti , arp , automedia , broadcast , debug , dynamic , master</code> <code>multicast , pointopoint , portsel , promisc , slave , trailers , up</code> Prepending <code>no</code> to any of these flags will negate their effect.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a , -all</code></dt>
<dd> Display all available interfaces.</dd>
<dt><code>-A , -address </code><i>addr</i></dt>
<dd> Set the interface address to <i>addr</i></dd>
<dt><code>-B , -broadcast </code><i>addr</i></dt>
<dd>
</dd><dt><code>-b , -brdaddr </code><i>addr</i></dt>
<dd> Set the broadcast address to <i>addr</i></dd>
<dt><code>-d , -dstaddr </code><i>addr</i></dt>
<dd>
</dd><dt><code>-p , -peer </code><i>addr</i></dt>
<dd> Set the destination (peer) address to <i>addr</i></dd>
<dt><code>&#8211;up</code></dt>
<dd> Activate the interface (default if address is given).</dd>
<dt><code>&#8211;down</code></dt>
<dd> Shut the interface down.</dd>
<dt><code>-F , -flags </code><i>flag , </i>[<i>flag &#8230;</i> ]</dt>
<dd> Set the interface flags.</dd>
<dt><code>-i , -interface </code><i>name</i></dt>
<dd> Configure the network interface <i>name</i></dd>
<dt><code>-l , -list</code></dt>
<dd> List the available or selected interfaces.</dd>
<dt><code>-m , -netmask </code><i>mask</i></dt>
<dd> Set the netmask to <i>mask</i></dd>
<dt><code>&#8211;metric </code><i>n</i></dt>
<dd> Set the interface metric to <i>n</i></dd>
<dt><code>-M , -mtu </code><i>n</i></dt>
<dd> Set the interface MTU to <i>n</i></dd>
<dt><code>&#8211;format </code><i>format</i></dt>
<dd> Select the output format; set to <code>help</code> for information.</dd>
<dt><code>-s , -short</code></dt>
<dd> Short output format.</dd>
<dt><code>-v , -verbose</code></dt>
<dd> Output information when configuring the interface.</dd>
<dt><code>-? , -help</code></dt>
<dd> Give this help list.</dd>
<dt><code>&#8211;usage</code></dt>
<dd> Give a short usage message.</dd>
<dt><code>-V , -version</code></dt>
<dd> Print program version.</dd></dl>
<p> Linux-specific options:</p>
<dl>
<dt><code>-T , -txqlen </code><i>n</i></dt>
<dd> Set the transmit queue length to <i>n</i></dd></dl>
