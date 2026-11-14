---
title: "esddsp(1)"
name: "esddsp"
section: "1"
letter: "e"
url: "/docs/linux/man/1-esddsp/"
---

<h2 class="name">NAME</h2>
 

 esddsp - attempt to reroute audio device to esd 

<h2>DESCRIPTION</h2>

 esddsp can allow non-esd applications to be routed through esd.

<h2>USAGE</h2>

 esddsp [options] player arguments 

 options: 

 <pre><code>
 -h, --help                show brief help
 -s, --server=HOST:PORT    contact esd server on host at port
 -m, --mixer               enable mixer support
 -n, --name=NAME           use name to identify player to esd
 -v, --verbose             show parameters
 --mmap                    use memory mapping emulation
                             (useful for games like quake)
</code></pre>

<h2>SEE ALSO</h2>

 <i><a HREF="/docs/linux/man/1-esd/">esd</a></i>(1), <i><a HREF="/docs/linux/man/1-esdcat/">esdcat</a></i>(1), <i><a HREF="/docs/linux/man/1-esdloop/">esdloop</a></i>(1), <i><a HREF="/docs/linux/man/1-esdplay/">esdplay</a></i>(1), <i><a HREF="/docs/linux/man/1-esdsample/">esdsample</a></i>(1), <i><a HREF="/docs/linux/man/1-esd-config/">esd-config</a></i>(1), <i><a HREF="/docs/linux/man/1-esdctl/">esdctl</a></i>(1), <i><a HREF="/docs/linux/man/1-esdfilt/">esdfilt</a></i>(1), <i><a HREF="/docs/linux/man/1-esdmon/">esdmon</a></i>(1), <i><a HREF="/docs/linux/man/1-esdrec/">esdrec</a></i>(1) 

<h2>Index</h2>


