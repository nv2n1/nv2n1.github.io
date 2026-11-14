---
title: "slptool(1)"
name: "slptool"
section: "1"
letter: "s"
url: "/docs/linux/man/1-slptool/"
description: "slptool – SLP command line tool"
---

<h2>NAME</h2>
<p> slptool &#8211; SLP command line tool</p>
<h2>SYNOPSIS</h2>
<p> <code>slptool</code> [<i>options</i>] <i>command-and-arguments</i></p>
<h2>OPTIONS</h2>
<dl>
<dt>
<dd> options may be:</p>
<dt> <code>-v</code> (or <code>&#8211;version</code>) displays the versions of slptool and OpenSLP.</p>
<dt> <code>-s</code> (or <code>&#8211;scope</code>) followed by a comma-separated list of scopes.</p>
<dt> <code>-l</code> (or <code>&#8211;language</code>) followed by a language tag.</p>
<dt> <code>-t</code> (or <code>&#8211;time</code>) followed by a lifetime tag.</p>
<dt> <code>-i</code> (or <code>&#8211;interfaces</code>) followed by a comma-separated list of interfaces.</p>
<dt> <code>-u</code> (or <code>&#8211;unicastifc</code>) followed by a single interface.</p>
<dt>
<dd>
<dd>command-and-arguments may be:</p>
<dt>
<dd>
<dt>
<dd>findsrvs service-type [filter]</p>
<dt>
<dd>findattrs url [attrids]</p>
<dt>
<dd>findsrvtypes [authority]</p>
<dt>
<dd>findscopes</p>
<dt>
<dd>register url [attrs]</p>
<dt>
<dd>deregister url</p>
<dt>
<dd>getproperty propertyname</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd>
<dt>
<dd>slptool register service:myserv.x://myhost.com &quot;(attr1=val1),(attr2=val2)&quot;</p>
<dt>
<dd>slptool findsrvs service:myserv.x</p>
<dt>
<dd>slptool findsrvs service:myserv.x &quot;(attr1=val1)&quot;</p>
<dt>
<dd>slptool <code>-i</code> 10.77.13.240,192.168.250.240 findsrvs service:myserv.x</p>
<dt>
<dd>slptool <code>-u</code> 10.77.13.237 findsrvs service:myserv.x &quot;(attr1=val1)&quot;</p>
<dt>
<dd>slptool findattrs service:myserv.x://myhost.com</p>
<dt>
<dd>slptool findattrs service:myserv.x://myhost.com attr1</p>
<dt>
<dd>slptool <code>-i</code> 10.77.13.243 findattrs service:myserv.x://myhost.com attr1</p>
<dt>
<dd>slptool <code>-u</code> 10.77.13.237 findattrs service:myserv.x://myhost.com attr1</p>
<dt>
<dd>slptool deregister service:myserv.x://myhost.com</p>
<dt>
<dd>slptool getproperty net.slp.useScopes</dl>
<h2>Index</h2>
