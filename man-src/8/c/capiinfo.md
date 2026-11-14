---
title: "capiinfo(8)"
name: "capiinfo"
section: "8"
letter: "c"
url: "/docs/linux/man/8-capiinfo/"
description: "capiinfo – Show supported features of all installed CAPI2.0 controllers"
---

<p>capiinfo &#8211; Show supported features of all installed CAPI2.0 controllers</p>
<h2>Synopsis</h2>
<p><code>capiinfo</code></p>
<h2>Description</h2>
<p>The capiinfo program checks how many controllers are installed and calls CAPI_GET_PROFILE for each of them. Also it sends a FACILITY_REQ capi message to get the information for the facilities supported by each controller. The information is shown on STDOUT. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-capiinit/">capiinit</a>(8)<br />
 <a rel="nofollow" href="http://www.capi.org/">http://www.capi.org/</a> (CAPI 2.0 specification) </p>
<h2>Authors</h2>
<p>Carsten Paeth (calle [at] calle.in-berlin.de)</p>
