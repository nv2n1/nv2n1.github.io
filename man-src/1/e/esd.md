---
title: "esd(1)"
name: "esd"
section: "1"
letter: "e"
url: "/docs/linux/man/1-esd/"
---

<h2 class="name">NAME</h2>
 

 esd - The Enlightened Sound Daemon 

<h2>DESCRIPTION</h2>

 Starts up EsounD, which provides a sound mixing server.

<h2>USAGE</h2>

 esd [options] 

 <pre><code>
  -d DEVICE     force esd to use sound device DEVICE
  -b            run server in 8 bit sound mode
  -r RATE       run server at sample rate of RATE
  -as SECS      free audio device after SECS of inactivity (-1 to disable)
  -unix         use unix domain sockets instead of tcp/ip
  -tcp          use tcp/ip sockets instead of unix domain
  -public       make tcp/ip access public (other than localhost)
  -promiscuous  start unlocked and owned (disable authenticaton) NOT RECOMMENDED
  -terminate    terminate esd daemon after last client exits
  -noterminate  do not terminate esd daemon after last client exits
  -nobeeps      disable startup beeps
  -beeps        enable startup beeps
  -trust        start esd even if use of /tmp/.esd can be insecure
  -port PORT    listen for connections at PORT (only for tcp/ip)
  -bind ADDRESS binds to ADDRESS (only for tcp/ip)
  -v --version  print version information
</code></pre> Possible devices are: /dev/dsp, /dev/dsp2, etc.

<h2>FILES /etc/esd.conf<tt>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>daemon configuration file</h2>

<h2>SEE ALSO</h2>

 <i><a HREF="/docs/linux/man/1-esdcat/">esdcat</a></i>(1), <i><a HREF="/docs/linux/man/1-esddsp/">esddsp</a></i>(1), <i><a HREF="/docs/linux/man/1-esdloop/">esdloop</a></i>(1), <i><a HREF="/docs/linux/man/1-esdplay/">esdplay</a></i>(1), <i><a HREF="/docs/linux/man/1-esdsample/">esdsample</a></i>(1),
 <i><a HREF="/docs/linux/man/1-esd-config/">esd-config</a></i>(1), <i><a HREF="/docs/linux/man/1-esdctl/">esdctl</a></i>(1), <i><a HREF="/docs/linux/man/1-esdfilt/">esdfilt</a></i>(1), <i><a HREF="/docs/linux/man/1-esdmon/">esdmon</a></i>(1), <i><a HREF="/docs/linux/man/1-esdrec/">esdrec</a></i>(1) 

<h2>Index</h2>


