---
title: "ipv4calc(1)"
name: "ipv4calc"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipv4calc/"
description: "ipv4calc - Calculates IPv4 elements from an address. SYNOPSIS ipv4calc[--network | --broadcast | --netmask | --address | --cidr] addr DESCRIPTION If an option is specified ipv4calc calculates the r..."
---

<h2 class="name">NAME</h2>
<pre>
  ipv4calc - Calculates IPv4 elements from an address.
</pre>
<h2>SYNOPSIS</h2>
<pre><code>
ipv4calc[--network | --broadcast | --netmask |
         --address | --cidr] addr
</code></pre>
<h2>DESCRIPTION</h2>
<p> If an option is specified <code>ipv4calc</code> calculates the requested element from the address and prints it on stdout. </p>
<p> If multiple options are specified, only the first one is printed. </p>
<p> If no options are specified, the program prints the host part of the address, the network and the broadcast address as deduced from the given address. </p>
<p> If address doesn&#8217;t contains a netmask or mask length, the default one is assumed.</p>
<h2>AUTHOR</h2>
<p> Francis J. Lacoste &lt;francis.lacoste [at] iNsu.COM&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 1999,2000 iNsu Innovations Inc. All rights reserved. </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms as perl itself.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/3-network--ipv4addr/">Network::IPv4Addr</a></i>(3). </p>
<h2>Index</h2>
