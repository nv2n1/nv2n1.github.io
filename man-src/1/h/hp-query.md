---
title: "hp-query(1)"
name: "hp-query"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hp-query/"
description: "hp-query – Model Query Utility"
---

<h2 class="name">NAME</h2>
<p> hp-query &#8211; Model Query Utility </p>
<h2>DESCRIPTION</h2>
<p> Query a printer model for static model information. Designed to be called from other processes.</p>
<h2>SYNOPSIS</h2>
<p> <code>hp-query [MODE] [OPTIONS]</code></p>
<h2>MODE</h2>
<dl>
<dt>Run in non-interactive mode:</p>
<dd> -n or &#8211;non-interactive</dl>
<h2>OPTIONS</h2>
<dl>
<dt>Set the logging level:</p>
<dd> -l&lt;level&gt; or &#8211;logging=&lt;level&gt; &lt;level&gt;: none, info*, error, warn, debug (*default)</p>
<dt>Run in debug mode:</p>
<dd> -g (same as option: -ldebug)</p>
<dt>This help information:</p>
<dd> -h or &#8211;help</p>
<dt>Specify model by device URI:</p>
<dd> -d&lt;device_uri&gt; or &#8211;device=&lt;device_uri&gt;</p>
<dt>Specify normalized model name:</p>
<dd> -m&lt;model_name&gt; or &#8211;model=&lt;model_name&gt; (normalized models.dat format)</p>
<dt>Specify raw model name:</p>
<dd> -r&lt;model_name&gt; or &#8211;raw=&lt;model_name&gt; (raw model name from MDL: field of device ID)</p>
<dt>Specify key to query:</p>
<dd> -k&lt;key&gt; or &#8211;key=&lt;key&gt; (or, use -a/&#8211;all to return all keys)</p>
<dt>Query all keys:</p>
<dd> -a or &#8211;all (default separator is a LF)</p>
<dt>Specify the separator when multiple keys are queried:</p>
<dd> -s&lt;sep&gt; &#8211;sep=&lt;sep&gt; (character or &#8216;tab&#8217;, &#8216;newline&#8217;, &#8216;cr&#8217;, &#8216;lf&#8217;, &#8216;crlf&#8217;)(only valid when used with -a/&#8211;all)</p>
<dt>Suppress trailing linefeed:</p>
<dd> -x</dl>
<h2>SEE ALSO</h2>
<p> hp-info</p>
<h2>AUTHOR</h2>
<p> HPLIP (HP Linux Imaging and Printing) is an HP developed solution for printing, scanning, and faxing with HP inkjet and laser based printers in Linux.</p>
<h2>REPORTING BUGS</h2>
<p> The HPLIP Launchpad.net site <code><a rel="nofollow" href="https://launchpad.net/hplip">https://launchpad.net/hplip</a></code> is available to get help, report bugs, make suggestions, discuss the HPLIP project or otherwise contact the HPLIP Team.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2001-18 HP Development Company, L.P. </p>
<p> This software comes with ABSOLUTELY NO WARRANTY. This is free software, and you are welcome to distribute it under certain conditions. See COPYING file for more details. </p>
<h2>Index</h2>
