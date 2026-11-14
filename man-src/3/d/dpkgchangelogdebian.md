---
title: "dpkgchangelogdebian(3)"
name: "dpkgchangelogdebian"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dpkgchangelogdebian/"
---

Dpkg::Changelog::Debian - parse Debian changelogs 

<h2>Description</h2>Dpkg::Changelog::Debian parses Debian changelogs as described in the Debian policy (version 3.6.2.1 at the time of this writing). See section ``<font SIZE="-1">SEE ALSO''</font> for locations where to find this definition. 

 The parser tries to ignore most cruft like # or /* */ style comments, <font SIZE="-1">CVS</font> comments, vim variables, emacs local variables and stuff from older changelogs with other formats at the end of the file. <font SIZE="-1">NOTE:</font> most of these are ignored silently currently, there is no parser error issued for them. This should become configurable in the future.
<h3><font SIZE="-1">METHODS</font></h3><dl COMPACT><dt>$c-&gt;parse($fh, $description)
<dd>Read the filehandle and parse a Debian changelog in it. Returns the number of changelog entries that have been parsed with success.</dl><h2>See Also</h2>Dpkg::Changelog 

 Description of the Debian changelog format in the Debian policy: &lt;<a rel="nofollow" HREF="https://www.debian.org/doc/debian-policy/ch-source.html#s-dpkgchangelog">https://www.debian.org/doc/debian-policy/ch-source.html#s-dpkgchangelog</a>&gt;.
<h2>Changes</h2><h3>Version 1.00</h3>Mark the module as public.
<h2>Authors</h2>Frank Lichtenheld, &lt;frank [at] lichtenheld.de&gt; Raphaël Hertzog, &lt;hertzog [at] debian.org&gt;
