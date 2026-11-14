---
title: "esdctl(1)"
name: "esdctl"
section: "1"
letter: "e"
url: "/docs/linux/man/1-esdctl/"
---

<h2 class="name">NAME</h2>
 

 esdctl - The Enlightened Sound Daemon 

<h2>DESCRIPTION</h2>

 Command-line control program for EsounD

<h2>USAGE</h2>

 esdctl [options] [command] 

 options: <tt>&quot;-s&quot;</tt>, --server=host:port contact esd server on host at port 

 commands: 

 <pre><code>
 lock                          foreign clients may not use the server
 unlock                        foreign clients may use the server
 standby, off                  suspend sound output for other programs
 resume, on                    resume sound output
 cache sample                  cache a sample in the server
 getid name                    retrieve a sample id from its name
 free name                     uncache a sample in the server
 play name                     play a cached sample once
 loop name                     make a cached sample loop
 stop name                     stop the looping sample at end
 serverinfo                    get server info from server
 allinfo                       get player and sample info from server
 panstream id left right set   panning for a stream
 pansample id left right set   default panning for a sample
                               - left/right pan values scaled to 256.
 standbymode                   see if server's on standby, etc.
</code></pre>

<h2>SEE ALSO</h2>

 <i><a HREF="/docs/linux/man/1-esd/">esd</a></i>(1), <i><a HREF="/docs/linux/man/1-esdcat/">esdcat</a></i>(1), <i><a HREF="/docs/linux/man/1-esddsp/">esddsp</a></i>(1), <i><a HREF="/docs/linux/man/1-esdloop/">esdloop</a></i>(1), <i><a HREF="/docs/linux/man/1-esdplay/">esdplay</a></i>(1), <i><a HREF="/docs/linux/man/1-esdsample/">esdsample</a></i>(1), <i><a HREF="/docs/linux/man/1-esd-config/">esd-config</a></i>(1), <i><a HREF="/docs/linux/man/1-esdfilt/">esdfilt</a></i>(1), <i><a HREF="/docs/linux/man/1-esdmon/">esdmon</a></i>(1), <i><a HREF="/docs/linux/man/1-esdrec/">esdrec</a></i>(1) 

<h2>Index</h2>


