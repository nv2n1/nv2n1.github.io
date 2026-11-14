---
title: "fcinitbringuptodate(3)"
name: "fcinitbringuptodate"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcinitbringuptodate/"
description: "FcInitBringUptoDate – reload configuration files if needed"
---

<p>FcInitBringUptoDate &#8211; reload configuration files if needed </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcBool FcInitBringUptoDate (void</code><i></i><code>); </code></p>
<h2>Description</h2>
<p>Checks the rescan interval in the default configuration, checking the configuration if the interval has passed and reloading the configuration if when any changes are detected. Returns FcFalse if the configuration cannot be reloaded (see FcInitReinitialize). Otherwise returns FcTrue.</p>
