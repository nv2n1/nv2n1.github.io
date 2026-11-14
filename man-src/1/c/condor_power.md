---
title: "condor_power(1)"
name: "condor_power"
section: "1"
letter: "c"
url: "/docs/linux/man/1-condor_power/"
description: "condor_power send packet intended to wake a machine from a low power state"
---

<h2>Name</h2>
<p> <i>condor_power</i> send packet intended to wake a machine from a low power state </p>
<h2>Synopsis</h2>
<p> <i>condor_power</i> [ <code>-h</code> ] </p>
<p> <i>condor_power</i> [ <code>-d</code> ] [ <code>-i</code> ] [ <code>-m </code> <i>MACaddress</i> ] [ <code>-s </code> <i>subnet</i> ] [ <i>ClassAdFile</i> ] </p>
<h2>Description</h2>
<p> <i>condor_power</i> sends one UDP Wake on LAN (WOL) packet to a machine specified either by command line arguments or by the contents of a machine ClassAd. The machine ClassAd may be in a file, where the file name specified by the optional argument <i>ClassAdFile</i> is given on the command line. With no command line arguments to specify the machine, and no file specified, <i>condor_power</i> quietly presumes that standard input is the file source which will specify the machine ClassAd that includes the public IP address and subnet of the machine. </p>
<p> <i>condor_power</i> needs a complete specification of the machine to be successful. If a MAC address is provided on the command line, but no subnet is given, then the default value for the subnet is used. If a subnet is provided on the command line, but no MAC address is given, then <i>condor_power</i> falls back to taking its information in the form of the machine ClassAd as provided in a file or on standard input. Note that this case implies that the command line specification of the subnet is ignored. </p>
<p> <i>condor_power</i> relies on the router receiving the WOL packet to correctly broadcast the request. Since routers are often configured to ignore requests to broadcast messages on a different subnet than the sender, the send of a WOL packet to a machine on a different subnet may fail. </p>
<h2>Options</h2>
<p> <code>-h</code></p>
<dl>
<dt>
<dd> Print usage information and exit.</p>
<dt>
<dd></dl>
<p> <code>-d</code></p>
<dl>
<dt>
<dd> Enable debugging messages.</p>
<dt>
<dd></dl>
<p> <code>-i</code></p>
<dl>
<dt>
<dd> Read a ClassAd that is piped in through standard input.</p>
<dt>
<dd></dl>
<p> <code>-m </code> <i>MACaddress</i></p>
<dl>
<dt>
<dd> Specify the MAC address in the standard format of six groups of two hexadecimal digits separated by colons.</p>
<dt>
<dd></dl>
<p> <code>-s </code> <i>subnet</i></p>
<dl>
<dt>
<dd> Specify the subnet in the standard form of a mask for an IPv4 address. Without this option, a global broadcast will be sent.</p>
<dt>
<dd>
<dt>
<dd></dl>
<h2>Exit Status</h2>
<p> <i>condor_power</i> will exit with a status value of 0 (zero) upon success, and it will exit with the value 1 (one) upon failure. </p>
<h2>Author</h2>
<p> Center for High Throughput Computing, University of Wisconsin-Madison</p>
<h2>Copyright</h2>
<p> Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. </p>
<h2>Index</h2>
