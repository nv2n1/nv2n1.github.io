---
title: "gutenprint-foomaticppdupdate(8)"
name: "gutenprint-foomaticppdupdate"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gutenprint-foomaticppdupdate/"
description: "gutenprint-foomaticppdupdate – update Gutenprint Foomatic PPD files"
---

<p>gutenprint-foomaticppdupdate &#8211; update Gutenprint Foomatic PPD files</p>
<h2>Synopsis</h2>
<p><code>gutenprint-foomaticppdupdate VERSION</code></p>
<h2>Description</h2>
<p><code>gutenprint-foomaticppdupdate</code> regenerates the <i>Gutenprint</i> Foomatic PPD files in use by CUPS, using freshly generated Foomatic PPD files as templates. The new PPD file replaces the old PPD file under <i>/etc/cups/ppd</i>, but all the options set in the old PPD will be merged into the new PPD, provided that they are still valid in the new file. </p>
<p> <code>gutenprint-foomaticppdupdate</code> does <code>not</code> restart cupsd. cupsd will need manual reloading (or send SIGHUP) once <code>gutenprint-foomaticppdupdate</code> has completed. </p>
<p> This is not intended to be used directly but instead is run automatically on package upgrade.</p>
<h2>Options</h2>
<p><code>VERSION</code> The version number of the Gutenprint package just installed.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-cups-genppdupdate/">cups-genppdupdate</a></code>(8) This program is free software; you can redistribute it and/or modify it under the terms fo the GNU General Public License, version 2, or (at your option) any later version. </p>
