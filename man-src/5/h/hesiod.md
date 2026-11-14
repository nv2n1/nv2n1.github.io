---
title: "hesiod(5)"
name: "hesiod"
section: "5"
letter: "h"
url: "/docs/linux/man/5-hesiod/"
description: "hesiod.conf – Configuration file for the Hesiod library"
---

<p>hesiod.conf &#8211; Configuration file for the Hesiod library</p>
<h2>Description</h2>
<p>The file hesiod.conf determines the behavior of the Hesiod library. Blank lines and lines beginning with a `#&#8217; character are ignored. All other lines should be of the form <i>variable</i> = <i>value</i>, where the value should be a single word. Possible variables and values are:</p>
<dl>
<dt>lhs</p>
<dd>Specifies the domain prefix used for Hesiod queries. In almost all cases, you should specify &#8220;lhs=.ns&#8221;. The default value if you do not specify an lhs value is no domain prefix, which is not compatible with most Hesiod domains.</p>
<dt>rhs</p>
<dd>Specifies the default Hesiod domain; this value may be overridden by the <code>HES_DOMAIN</code> environment variable. You must specify an rhs line for the Hesiod library to work properly.</p>
<dt>classes</p>
<dd>Specifies which DNS classes Hesiod should do lookups in. Possible values are IN (the preferred class) and HS (the deprecated class, still used by some sites). You may specify both classes separated by a comma to try one class first and then the other if no entry is available in the first class. The default value of the classes variable is &#8220;IN,HS&#8221;.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-hesiod/">hesiod</a>(3)</p>
<h2>Bugs</h2>
<p>There default value for &#8220;lhs&#8221; should probably be more reasonable. </p>
