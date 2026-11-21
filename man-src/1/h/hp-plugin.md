---

title: "hp-plugin(1)"
name: "hp-plugin"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hp-plugin/"
description: "hp-plugin – Plugin Download and Install Utility"
---

<p> HP Proprietary Plugin Download and Install Utility</p>
<p> <code>hp-plugin [MODE] [OPTIONS]</code></p>
<h2>MODE</h2>
<dl>
<dt>Run in graphical UI mode:</dt>
<dd> -u or &#8211;gui (Default)</dd>
<dt>Run in interactive mode:</dt>
<dd> -i or &#8211;interactive</dd>
<dt>Installation for required printer mode:</dt>
<dd> &#8211;required (Qt4 only)</dd>
<dt>Installation for optional printer mode:</dt>
<dd> &#8211;optional (Qt4 only)</dd>
<dt>Set the language:</dt>
<dd> &#8211;loc=&lt;lang&gt; or &#8211;lang=&lt;lang&gt;. Use &#8211;loc=? or &#8211;lang=? to see a list of available language codes.</dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt>Specify the path to the plugin file:</dt>
<dd> -p &lt;path&gt; or &#8211;path=&lt;path&gt; or &#8211;plugin=&lt;path&gt;</dd>
<dt>Set the logging level:</dt>
<dd> -l&lt;level&gt; or &#8211;logging=&lt;level&gt; &lt;level&gt;: none, info*, error, warn, debug (*default)</dd>
<dt>Run in debug mode:</dt>
<dd> -g (same as option: -ldebug)</dd>
<dt>This help information:</dt>
<dd> -h or &#8211;help</dd></dl>
<h2>SEE ALSO</h2>
<p> hp-setup hp-firmware</p>
<h2>AUTHOR</h2>
<p> HPLIP (HP Linux Imaging and Printing) is an HP developed solution for printing, scanning, and faxing with HP inkjet and laser based printers in Linux.</p>
<h2>REPORTING BUGS</h2>
<p> The HPLIP Launchpad.net site <code><a rel="nofollow" href="https://launchpad.net/hplip">https://launchpad.net/hplip</a></code> is available to get help, report bugs, make suggestions, discuss the HPLIP project or otherwise contact the HPLIP Team.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2001-18 HP Development Company, L.P. </p>
<p> This software comes with ABSOLUTELY NO WARRANTY. This is free software, and you are welcome to distribute it under certain conditions. See COPYING file for more details. </p>
