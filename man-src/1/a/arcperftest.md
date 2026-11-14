---
title: "arcperftest(1)"
name: "arcperftest"
section: "1"
letter: "a"
url: "/docs/linux/man/1-arcperftest/"
description: "arcperftest – ARC service performance tester"
---

<h2 class="name">NAME</h2>
<p> arcperftest &#8211; ARC service performance tester</p>
<h2>SYNOPSIS</h2>
<p> <code>arcperftest</code> [ <code>-c</code> <i>config</i> ] [ <code>-d</code> <i>debug</i> ] [ <code>-r</code> ] <i>url threads duration</i> </p>
<h2>DESCRIPTION</h2>
<p> The <code>arcperftest</code> command test the performance of an ARC service specified by its <i>url</i> sending <i>threads</i> number of concurrent requests for a duration of <i>duration</i> seconds. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code> <i>config</i></p>
<dd> The file containing client chain XML configuration with &#8216;soap&#8217; entry point and HOSTNAME, PORTNUMBER and PATH keyword for hostname, port and HTTP path of &#8216;echo&#8217; service. </p>
<dt><code>-d</code> <i>debuglevel</i></p>
<dd> FATAL, ERROR, WARNING, INFO, VERBOSE or DEBUG</p>
<dt><code>-r</code></p>
<dd> If specified close connection and reconnect after every request. </p>
</dl>
<h2>EXAMPLES</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>Axis2C:<br />
&nbsp;<wbr>with TLS:<br />
arcperftest&nbsp;<wbr><a rel="nofollow" href="https://glueball.uio.no:50443/axis2/services/echo">https://glueball.uio.no:50443/axis2/services/echo</a>&nbsp;<wbr>&nbsp;<wbr>10 30<br />
&nbsp;<wbr>without TLS:<br />
arcperftest&nbsp;<wbr><a rel="nofollow" href="http://glueball.uio.no:50000/axis2/services/echo">http://glueball.uio.no:50000/axis2/services/echo</a>&nbsp;<wbr>&nbsp;<wbr>10 30 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>HED:<br />
&nbsp;<wbr>with TLS:<br />
arcperftest&nbsp;<wbr><a rel="nofollow" href="https://glueball.uio.no:60000/echo">https://glueball.uio.no:60000/echo</a>&nbsp;<wbr>10 30<br />
&nbsp;<wbr>without TLS:<br />
arcperftest&nbsp;<wbr><a rel="nofollow" href="http://glueball.uio.no:60010/echo">http://glueball.uio.no:60010/echo</a>&nbsp;<wbr>10 30 </p>
<h2>COPYRIGHT</h2>
<p> APACHE LICENSE Version 2.0 </p>
<h2>AUTHOR</h2>
<p> ARC software is developed by the NorduGrid Collaboration (<a rel="nofollow" href="http://www.nordugrid.org">http://www.nordugrid.org</a>), please consult the AUTHORS file distributed with ARC. Please report bugs and feature requests to <a rel="nofollow" href="http://bugzilla.nordugrid.org">http://bugzilla.nordugrid.org</a> </p>
<h2>Index</h2>
