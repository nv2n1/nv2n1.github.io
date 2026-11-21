---

title: "ifdata(1)"
name: "ifdata"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ifdata/"
description: "ifdata – get network interface info without parsing ifconfig output"
---

<dl>
<dt> <code>ifdata</code> [options] {<i>iface</i>}</dt></dl>
<p> <code>ifdata</code></p>
<dd>can be used to check for the existence of a network interface, or to get information about the interface, such as its IP address. Unlike <code>ifconfig</code> or <code>ip</code>, <code>ifdata</code> has simple to parse output that is designed to be easily used by a shell script.</dd>
<h2>OPTIONS</h2>
<p> <code>-h</code></p>
<dl>
<dt>
</dt><dd> Print out a help summary.</dd></dl>
<p> <code>-e</code></p>
<dl>
<dt>
</dt><dd> Test to see if the interface exists, exit nonzero if it does not.</dd></dl>
<p> <code>-p</code></p>
<dl>
<dt>
</dt><dd> Prints out the whole configuration of the interface.</dd></dl>
<p> <code>-pe</code></p>
<dl>
<dt>
</dt><dd> Prints &quot;yes&quot; or &quot;no&quot; if the interface exists or not.</dd></dl>
<p> <code>-pa</code></p>
<dl>
<dt>
</dt><dd> Prints the IPv4 address of the interface.</dd></dl>
<p> <code>-pn</code></p>
<dl>
<dt>
</dt><dd> Prints the netmask of the interface.</dd></dl>
<p> <code>-pN</code></p>
<dl>
<dt>
</dt><dd> Prints the network address of the interface.</dd></dl>
<p> <code>-pb</code></p>
<dl>
<dt>
</dt><dd> Prints the broadcast address of the interface.</dd></dl>
<p> <code>-pm</code></p>
<dl>
<dt>
</dt><dd> Prints the MTU of the interface.</dd></dl>
<p> Following options are Linux only. </p>
<p> <code>-ph</code></p>
<dl>
<dt>
</dt><dd> Prints the hardware address of the interface. Exit with a failure exit code if there is not hardware address for the given network interface.</dd></dl>
<p> <code>-pf</code></p>
<dl>
<dt>
</dt><dd> Prints the flags of the interface.</dd></dl>
<p> <code>-si</code></p>
<dl>
<dt>
</dt><dd> Prints out all the input statistics of the interface.</dd></dl>
<p> <code>-sip</code></p>
<dl>
<dt>
</dt><dd> Prints the number of input packets.</dd></dl>
<p> <code>-sib</code></p>
<dl>
<dt>
</dt><dd> Prints the number of input bytes.</dd></dl>
<p> <code>-sie</code></p>
<dl>
<dt>
</dt><dd> Prints the number of input errors.</dd></dl>
<p> <code>-sid</code></p>
<dl>
<dt>
</dt><dd> Prints the number of dropped input packets.</dd></dl>
<p> <code>-sif</code></p>
<dl>
<dt>
</dt><dd> Prints the number of input fifo overruns.</dd></dl>
<p> <code>-sic</code></p>
<dl>
<dt>
</dt><dd> Print the number of compressed input packets.</dd></dl>
<p> <code>-sim</code></p>
<dl>
<dt>
</dt><dd> Prints the number of input multicast packets.</dd></dl>
<p> <code>-so</code></p>
<dl>
<dt>
</dt><dd> Prints out all the output statistics of the interface.</dd></dl>
<p> <code>-sop</code></p>
<dl>
<dt>
</dt><dd> Prints the number of output packets.</dd></dl>
<p> <code>-sob</code></p>
<dl>
<dt>
</dt><dd> Prints the number of output bytes.</dd></dl>
<p> <code>-soe</code></p>
<dl>
<dt>
</dt><dd> Prints the number of output errors.</dd></dl>
<p> <code>-sod</code></p>
<dl>
<dt>
</dt><dd> Prints the number of dropped output packets.</dd></dl>
<p> <code>-sof</code></p>
<dl>
<dt>
</dt><dd> Prints the number of output fifo overruns.</dd></dl>
<p> <code>-sox</code></p>
<dl>
<dt>
</dt><dd> Print the number of output collisions.</dd></dl>
<p> <code>-soc</code></p>
<dl>
<dt>
</dt><dd> Prints the number of output carrier losses.</dd></dl>
<p> <code>-som</code></p>
<dl>
<dt>
</dt><dd> Prints the number of output multicast packets.</dd></dl>
<p> <code>-bips</code></p>
<dl>
<dt>
</dt><dd> Prints the number of bytes of incoming traffic measured in one second.</dd></dl>
<p> <code>-bops</code></p>
<dl>
<dt>
</dt><dd> Prints the number of bytes of outgoing traffic measured in one second.</dd></dl>
<h2>AUTHOR</h2>
<p> Benjamin BAYART </p>
