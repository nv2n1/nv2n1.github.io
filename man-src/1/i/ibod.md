---
title: "ibod(1)"
name: "ibod"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ibod/"
description: "ibod – ISDN MPPP bandwidth on demand daemon"
---

<h2>NAME</h2>
<p> ibod &#8211; ISDN MPPP bandwidth on demand daemon</p>
<h2>SYNOPSIS</h2>
<p> <code>ibod</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>Ibod</code> is a ISDN MPPP bandwidth on demand daemon designed to operate in conjunction with <code>isdn4linux.</code> It is normally started at boot time, but can be started and stopped at any time. The program monitors inbound and outbound traffic on the ISDN interface. When the required bandwidth exceeds the capacity for one IDSN B-channel (64kbps) a second (slave) channel is connected according to the MPPP protocol. When the traffic decreases below one channel capacity, the slave channel is disconnected. </p>
<p> A configuration file <i>/etc/ppp/ibod.cf</i> is read initially. The device <i>/dev/isdninfo</i> is monitored for the current state and throughput of the ISDN interface. All operation on the ISDN interface is made through the <i>/dev/isdnctrl</i> interface. </p>
<p> <code>Ibod</code> is also listening on TCP port 6050 for eventual connection from control panel BSD <a href="/docs/linux/man/1-ibod/">ibod</a>(1). </p>
<h2>SIGNALS</h2>
<p> Upon receiving SIGHUP, the configuration file is re-read. A SIGPIPE closes an eventual socket connection with <code>xibod.</code> </p>
<h2>ENVIRONMENT</h2>
<p> Variable <i>IBOD_HOME</i> specifies the directory where to look for the configuration file <i>ibod.cf.</i> </p>
<h2>DIAGNOSTICS</h2>
<p> All logging is made to syslog with the identity tag <i>ibod.</i> </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/4-ibod-cf/">ibod.cf</a>(4) and <a href="/docs/linux/man/1-xibod/">xibod</a>(1) </p>
<h2>AUTHOR</h2>
<p> Bjoern Smith, Smith [at] Compound.SE </p>
<h2>Index</h2>
