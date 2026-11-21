---

title: "ldns-zsplit(1)"
name: "ldns-zsplit"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ldns-zsplit/"
description: "ldns-zsplit – split up a zone file"
---

<p> ldns-zsplit &#8211; split up a zone file</p>
<h2>SYNOPSIS</h2>
<p> <code>ldns-zsplit</code> [ <i>OPTIONS</i> ] <i>zonefile</i> </p>
<h2>DESCRIPTION</h2>
<h2>OPTIONS</h2>
<dl>
<dt><code>-n NUMBER</code></dt>
<dd> Split after NUMBER RRs, <code>ldns-zsplit</code> will not split in the middle of an RRs.</dd></dl>
<p> Each part is saved with a numerical suffix, starting with .000. The largest suffix is thus .999. </p>
<dl>
<dt><code>-o ORIGIN</code></dt>
<dd> use ORIGIN as origin when reading the zonefile. </dd>
<dt><code>-z</code></dt>
<dd> Sort the zone before splitting. </dd>
<dt><code>-v</code></dt>
<dd> Show version number and exit. </dd>
</dl>
<h2>AUTHOR</h2>
<p> Written by the ldns team as an example for ldns usage. </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;ldns-team [at] nlnetlabs.nl&gt;. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2005, 2006 NLnet Labs. This is free software. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
