---
title: "deb-triggers(5)"
name: "deb-triggers"
section: "5"
letter: "d"
url: "/docs/linux/man/5-deb-triggers/"
description: "deb-triggers – package triggers"
---

<p>deb-triggers &#8211; package triggers</p>
<h2>Synopsis</h2>
<p><code>debian/triggers</code>, <code>debian/</code><i>binary-package</i><code>.triggers</code>, <code>DEBIAN/triggers</code></p>
<h2>Description</h2>
<p>A package declares its relationship to some trigger(s) by including a <i>triggers</i> file in its control archive (i.e. <i>DEBIAN/triggers</i> during package creation). </p>
<p> This file contains directives, one per line. Leading and trailing whitespace and everything after the first <code>#</code> on any line will be trimmed, and empty lines will be ignored. </p>
<p> The trigger control directives currently supported are:</p>
<dl>
<dt><code>interest</code> <i>trigger-name</i></p>
<dd>
<dt><code>interest-await</code> <i>trigger-name</i></p>
<dd>
<dt><code>interest-noawait</code> <i>trigger-name</i></p>
<dd>Specifies that the package is interested in the named trigger. All triggers in which a package is interested must be listed using this directive in the triggers control file. </p>
<p> The &#8220;await&#8221; variants put the triggering package in triggers-awaited state depending on how the trigger was activated. The &#8220;noawait&#8221; variant does not put the triggering packages in triggers-awaited state, even if the triggering package declared an &#8220;await&#8221; activation (either with an <code>activate-await</code> or <code>activate</code> directive, or by using the <code>dpkg-trigger</code> <code>&#8211;no-await</code> command-line option). The &#8220;noawait&#8221; variant should be used when the functionality provided by the trigger is not crucial.</p>
<dt><code>activate</code> <i>trigger-name</i></p>
<dd>
<dt><code>activate-await</code> <i>trigger-name</i></p>
<dd>
<dt><code>activate-noawait</code> <i>trigger-name</i></p>
<dd>Arranges that changes to this package&#8217;s state will activate the specified trigger. The trigger will be activated at the start of the following operations: unpack, configure, remove (including for the benefit of a conflicting package), purge and deconfigure. </p>
<p> The &#8220;await&#8221; variants only put the triggering package in triggers-awaited state if the interest directive is also &#8220;await&#8221;. The &#8220;noawait&#8221; variant never puts the triggering packages in triggers-awaited state. The &#8220;noawait&#8221; variant should be used when the functionality provided by the trigger is not crucial. </p>
<p> If this package disappears during the unpacking of another package the trigger will be activated when the disappearance is noted towards the end of the unpack. Trigger processing, and transition from triggers-awaited to installed, does not cause activations. In the case of unpack, triggers mentioned in both the old and new versions of the package will be activated.</dl>
<p> Unknown directives are an error which will prevent installation of the package. </p>
<p> The &#8220;-noawait&#8221; variants should always be favored when possible since triggering packages are not put in triggers-awaited state and can thus be immediately configured without requiring the processing of the trigger. If the triggering packages are dependencies of other upgraded packages, it will avoid an early trigger processing run and make it possible to run the trigger only once as one of the last steps of the upgrade. </p>
<p> The &#8220;-noawait&#8221; variants are supported since dpkg 1.16.1, and will lead to errors if used with an older dpkg. </p>
<p> The &#8220;-await&#8221; alias variants are supported since dpkg 1.17.21, and will lead to errors if used with an older dpkg. </p>
<p> When a package provides an <code>interest-noawait</code> directive, any activation will set the triggering package into &#8220;noawait&#8221; mode, regardless of the awaiting mode requested by the activation (either &#8220;await&#8221; or &#8220;noawait&#8221;). When a package provides an <code>interest</code> or <code>interest-await</code> directive, any activation will set the triggering package into &#8220;await&#8221; or &#8220;noawait&#8221; depending on how it was activated.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-dpkg-trigger/">dpkg-trigger</a></code>(1), <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1), <code>/usr/share/doc/dpkg/triggers.txt.gz</code>. </p>
