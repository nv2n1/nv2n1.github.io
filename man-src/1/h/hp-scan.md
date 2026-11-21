---
title: "hp-scan(1)"
name: "hp-scan"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hp-scan/"
description: "hp-scan – Scan Utility"
---

<h2>DESCRIPTION</h2>
<p> SANE-based scan utility for HPLIP supported all-in-one/mfp devices.</p>
<h2>SYNOPSIS</h2>
<p> <code>hp-scan [DEVICE_URI|PRINTER_NAME] [MODE] [OPTIONS]</code></p>
<h2>PRINTER|DEVICE-URI</h2>
<dl>
<dt>To specify a device-URI:</dt>
<dd> -d&lt;device-uri&gt; or &#8211;device=&lt;device-uri&gt;</dd>
<dt>To specify a CUPS printer:</dt>
<dd> -p&lt;printer&gt; or &#8211;printer=&lt;printer&gt;</dd></dl>
<h2>MODE</h2>
<dl>
<dt>Run in interactive mode:</dt>
<dd> -i or &#8211;interactive</dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt>Set the logging level:</dt>
<dd> -l&lt;level&gt; or &#8211;logging=&lt;level&gt; &lt;level&gt;: none, info*, error, warn, debug (*default)</dd>
<dt>Run in debug mode:</dt>
<dd> -g (same as option: -ldebug)</dd>
<dt>This help information:</dt>
<dd> -h or &#8211;help</dd></dl>
<h2>OPTIONS (GENERAL)</h2>
<dl>
<dt>Scan destinations:</dt>
<dd> -s&lt;dest_list&gt; or &#8211;dest=&lt;dest_list&gt; where &lt;dest_list&gt; is a comma separated list containing one or more of: &#8216;file&#8217; , &#8216;viewer&#8217;, &#8216;editor&#8217;, &#8216;pdf&#8217;, or &#8216;print&#8217;. Use only commas between values, no spaces.</dd>
<dt>Scan mode:</dt>
<dd> -m&lt;mode&gt; or &#8211;mode=&lt;mode&gt;. Where &lt;mode&gt; is &#8216;gray&#8217;*, &#8216;color&#8217; or &#8216;lineart&#8217;.</dd>
<dt>Scanning resolution:</dt>
<dd> -r&lt;resolution_in_dpi&gt; or &#8211;res=&lt;resolution_in_dpi&gt; or &#8211;resolution=&lt;resolution_in_dpi&gt; where 300 is default.</dd>
<dt>Image resize:</dt>
<dd> &#8211;resize=&lt;scale_in_%&gt; (min=1%, max=400%, default=100%)</dd>
<dt>Color Dropout Red :</dt>
<dd> -color_dropout_red_value=&lt;color_dropout_red_value&gt; or &#8211;color_dropout_red_value=&lt;color_dropout_red_value&gt;</dd>
<dt>Color Dropout Green :</dt>
<dd> -color_dropout_green_value=&lt;color_dropout_green_value&gt; or &#8211;color_dropout_green_value=&lt;color_dropout_green_value&gt;</dd>
<dt>Color Dropout Blue :</dt>
<dd> -color_dropout_blue_value=&lt;color_dropout_blue_value&gt; or &#8211;color_dropout_blue_value=&lt;color_dropout_blue_value&gt;</dd>
<dt>Color Dropout Range :</dt>
<dd> -color_range=&lt;color_range&gt; or &#8211;color_range=&lt;color_range&gt;</dd>
<dt>Image contrast:</dt>
<dd> -c=&lt;contrast&gt; or &#8211;contrast=&lt;contrast&gt; The contrast range varies from device to device.</dd>
<dt>Image brightness:</dt>
<dd> -b=&lt;brightness&gt; or &#8211;brightness=&lt;brightness&gt; The brightness range varies from device to device.</dd>
<dt>ADF mode:</dt>
<dd> &#8211;adf (Note, only PDF output is supported when using the ADF) &#8211;duplex or &#8211;dup for duplex scanning using ADF.</dd></dl>
<h2>OPTIONS (SCAN AREA)</h2>
<dl>
<dt>Specify the units for area/box measurements:</dt>
<dd> -t&lt;units&gt; or &#8211;units=&lt;units&gt; where &lt;units&gt; is &#8216;mm&#8217;*, &#8216;cm&#8217;, &#8216;in&#8217;, &#8216;px&#8217;, or &#8216;pt&#8217; (&#8216;mm&#8217; is default).</dd>
<dt>Scan area:</dt>
<dd> -a&lt;tlx&gt;,&lt;tly&gt;,&lt;brx&gt;,&lt;bry&gt; or &#8211;area=&lt;tlx&gt;,&lt;tly&gt;,&lt;brx&gt;,&lt;bry&gt; Coordinates are relative to the upper left corner of the scan area. Units for tlx, tly, brx, and bry are specified by -t/&#8211;units (default is &#8216;mm&#8217;). Use only commas between values, no spaces.</dd>
<dt>Scan box:</dt>
<dd> &#8211;box=&lt;tlx&gt;,&lt;tly&gt;,&lt;width&gt;,&lt;height&gt; tlx and tly coordinates are relative to the upper left corner of the scan area. Units for tlx, tly, width, and height are specified by -t/&#8211;units (default is &#8216;mm&#8217;). Use only commas between values, no spaces.</dd>
<dt>Top left x of the scan area:</dt>
<dd> &#8211;tlx=&lt;tlx&gt; Coordinates are relative to the upper left corner of the scan area. Units are specified by -t/&#8211;units (default is &#8216;mm&#8217;).</dd>
<dt>Top left y of the scan area:</dt>
<dd> &#8211;tly=&lt;tly&gt; Coordinates are relative to the upper left corner of the scan area. Units are specified by -t/&#8211;units (default is &#8216;mm&#8217;).</dd>
<dt>Bottom right x of the scan area:</dt>
<dd> &#8211;brx=&lt;brx&gt; Coordinates are relative to the upper left corner of the scan area. Units are specified by -t/&#8211;units (default is &#8216;mm&#8217;).</dd>
<dt>Bottom right y of the scan area:</dt>
<dd> &#8211;bry=&lt;bry&gt; Coordinates are relative to the upper left corner of the scan area. Units are specified by -t/&#8211;units (default is &#8216;mm&#8217;).</dd>
<dt>Specify the scan area based on a paper size:</dt>
<dd> &#8211;size=&lt;paper size name&gt; where &lt;paper size name&gt; is one of: 3&#215;5, 4&#215;6, 5&#215;7, a2_env, a3, a4, a5, a6, b4, b5, c6_env, dl_env, exec, flsa, higaki, japan_env_3, japan_env_4, legal, letter, no_10_env, oufufu-hagaki, photo, super_b</dd></dl>
<h2>OPTIONS (&#8216;FILE&#8217; DEST)</h2>
<dl>
<dt>Filename for &#8216;file&#8217; destination:</dt>
<dd> -o&lt;file&gt; or -f&lt;file&gt; or &#8211;file=&lt;file&gt; or &#8211;output=&lt;file&gt;</dd></dl>
<h2>OPTIONS (&#8216;PDF&#8217; DEST)</h2>
<dl>
<dt>PDF viewer application:</dt>
<dd> &#8211;pdf=&lt;pdf_viewer&gt;</dd></dl>
<h2>OPTIONS (&#8216;VIEWER&#8217; DEST)</h2>
<dl>
<dt>Image viewer application:</dt>
<dd> -v&lt;viewer&gt; or &#8211;viewer=&lt;viewer&gt;</dd></dl>
<h2>OPTIONS (&#8216;EDITOR&#8217; DEST)</h2>
<dl>
<dt>Image editor application:</dt>
<dd> -e&lt;editor&gt; or &#8211;editor=&lt;editor&gt;</dd></dl>
<h2>OPTIONS (&#8216;EMAIL&#8217; DEST)</h2>
<dl>
<dt>From: address for &#8217;email&#8217; dest:</dt>
<dd> &#8211;email-from=&lt;email_from_address&gt; (required for &#8217;email&#8217; dest.)</dd>
<dt>To: address for &#8217;email&#8217; dest:</dt>
<dd> &#8211;email-to=&lt;email__to_address&gt; (required for &#8217;email&#8217; dest.)</dd>
<dt>Email subject for &#8217;email&#8217; dest:</dt>
<dd> &#8211;email-subject=&quot;&lt;subject&gt;&quot; or &#8211;subject=&quot;&lt;subject&gt;&quot; Use double quotes (&quot;) around the subject if it contains space characters.</dd>
<dt>Note or message for the &#8217;email&#8217; dest:</dt>
<dd> &#8211;email-msg=&quot;&lt;msg&gt;&quot; or &#8211;email-note=&quot;&lt;note&gt;&quot; Use double quotes (&quot;) around the note/message if it contains space characters.</dd></dl>
<h2>OPTIONS (&#8216;PRINTER&#8217; DEST)</h2>
<dl>
<dt>Printer queue/printer dest:</dt>
<dd> &#8211;dp=&lt;printer_name&gt; or &#8211;dest-printer=&lt;printer_name&gt;</dd>
<dt>Printer device-URI dest:</dt>
<dd> &#8211;dd=&lt;device-uri&gt; or &#8211;dest-device=&lt;device-uri&gt;</dd></dl>
<h2>OPTIONS (ADVANCED)</h2>
<dl>
<dt>Set the scanner compression mode:</dt>
<dd> -x&lt;mode&gt; or &#8211;compression=&lt;mode&gt;, &lt;mode&gt;=&#8217;raw&#8217;, &#8216;none&#8217; or &#8216;jpeg&#8217; (&#8216;jpeg&#8217; is default) (&#8216;raw&#8217; and &#8216;none&#8217; are equivalent)</dd></dl>
<h2>SEE ALSO</h2>
<h2>AUTHOR</h2>
<p> HPLIP (HP Linux Imaging and Printing) is an HP developed solution for printing, scanning, and faxing with HP inkjet and laser based printers in Linux.</p>
<h2>REPORTING BUGS</h2>
<p> The HPLIP Launchpad.net site <code><a rel="nofollow" href="https://launchpad.net/hplip">https://launchpad.net/hplip</a></code> is available to get help, report bugs, make suggestions, discuss the HPLIP project or otherwise contact the HPLIP Team.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2001-18 HP Development Company, L.P. </p>
<p> This software comes with ABSOLUTELY NO WARRANTY. This is free software, and you are welcome to distribute it under certain conditions. See COPYING file for more details. </p>
