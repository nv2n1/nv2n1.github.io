---
title: "dahdi_cfg(8)"
name: "dahdi_cfg"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dahdi_cfg/"
description: "dahdi_cfg – configures DAHDI kernel modules from /etc/dahdi/system.conf"
---

<p>dahdi_cfg &#8211; configures DAHDI kernel modules from /etc/dahdi/system.conf</p>
<h2>Synopsis</h2>
<p><code>dahdi_cfg [-c </code><i>CFG_FILE</i><code>] [-s] [-f] [-t] [-v [-v &#8230; ] ]</code> <code>dahdi_cfg -h</code> </p>
<h2>Description</h2>
<p><code>dahdi_cfg </code> configures DAHDI interface cards from a config file. You generally need to run it with a valid configurations in order for DAHDI modules to work properly. It must be run to configure every DAHDI span. Normally it is run from the DAHDI init script. </p>
<h2>Options</h2>
<p><code>-c </code><i>CFG_FILE</i></p>
<dl>
<dd>Use an alternative configuration file instead of <i>/etc/dahdi/system.conf</i></dl>
<p> <code>-s</code></p>
<dl>
<dd>Only shutdown spans.</dl>
<p> <code>-f</code></p>
<dl>
<dd>Always configure every channel, even if it appears not to have changed.</dl>
<p> <code>-t</code></p>
<dl>
<dd>Test mode. Don&#8217;t do anything, just report what you wanted to do.</dl>
<p> <code>-v</code></p>
<dl>
<dd>Be more verbose. Add extra v-s for extra verbosity.</dl>
<p> <code>-h</code></p>
<dl>
<dd>Display a brief help message.</dl>
<h2>Files</h2>
<p><i>/etc/dahdi/system.conf</i></p>
<dl>
<dd>The default location for the configuration file.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-dahdi_tool/">dahdi_tool</a>(8), <a href="/docs/linux/man/8-dahdi_monitor/">dahdi_monitor</a>(8), <a href="/docs/linux/man/8-asterisk/">asterisk</a>(8). </p>
<h2>Author</h2>
<p>This manual page was written by Santiago Ruano Rinc[&#8216;o]n &lt;santiago [at] unicauca.edu.co&gt; for the Debian system (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 any later version published by the Free Software Foundation.</p>
