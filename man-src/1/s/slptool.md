---

title: "slptool(1)"
name: "slptool"
section: "1"
letter: "s"
url: "/docs/linux/man/1-slptool/"
description: "slptool – SLP command line tool"
---

<p> slptool &#8211; SLP command line tool</p>
<h2>SYNOPSIS</h2>
<p> <code>slptool</code> [<i>options</i>] <i>command-and-arguments</i></p>
<h2>OPTIONS</h2>
<dl>
<dt>
</dt><dd> options may be:</dd>
<dt> <code>-v</code> (or <code>&#8211;version</code>) displays the versions of slptool and OpenSLP.</dt>
<dt> <code>-s</code> (or <code>&#8211;scope</code>) followed by a comma-separated list of scopes.</dt>
<dt> <code>-l</code> (or <code>&#8211;language</code>) followed by a language tag.</dt>
<dt> <code>-t</code> (or <code>&#8211;time</code>) followed by a lifetime tag.</dt>
<dt> <code>-i</code> (or <code>&#8211;interfaces</code>) followed by a comma-separated list of interfaces.</dt>
<dt> <code>-u</code> (or <code>&#8211;unicastifc</code>) followed by a single interface.</dt>
<dd>command-and-arguments may be:</dd>
<dt>
</dt><dd>findsrvs service-type [filter]</dd>
<dt>
</dt><dd>findattrs url [attrids]</dd>
<dt>
</dt><dd>findsrvtypes [authority]</dd>
<dt>
</dt><dd>findscopes</dd>
<dt>
</dt><dd>register url [attrs]</dd>
<dt>
</dt><dd>deregister url</dd>
<dt>
</dt><dd>getproperty propertyname</dd></dl>
<h2>EXAMPLES</h2>
<dl>
<dt>
</dt><dd>slptool register service:myserv.x://myhost.com &quot;(attr1=val1),(attr2=val2)&quot;</dd>
<dt>
</dt><dd>slptool findsrvs service:myserv.x</dd>
<dt>
</dt><dd>slptool findsrvs service:myserv.x &quot;(attr1=val1)&quot;</dd>
<dt>
</dt><dd>slptool <code>-i</code> 10.77.13.240,192.168.250.240 findsrvs service:myserv.x</dd>
<dt>
</dt><dd>slptool <code>-u</code> 10.77.13.237 findsrvs service:myserv.x &quot;(attr1=val1)&quot;</dd>
<dt>
</dt><dd>slptool findattrs service:myserv.x://myhost.com</dd>
<dt>
</dt><dd>slptool findattrs service:myserv.x://myhost.com attr1</dd>
<dt>
</dt><dd>slptool <code>-i</code> 10.77.13.243 findattrs service:myserv.x://myhost.com attr1</dd>
<dt>
</dt><dd>slptool <code>-u</code> 10.77.13.237 findattrs service:myserv.x://myhost.com attr1</dd>
<dt>
</dt><dd>slptool deregister service:myserv.x://myhost.com</dd>
<dt>
</dt><dd>slptool getproperty net.slp.useScopes</dd></dl>
