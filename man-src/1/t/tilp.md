---
title: "tilp(1)"
name: "tilp"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tilp/"
description: "TiLP2 – a communication program for TI calculators (‘Tilp Is a Linking Program’)"
---

<h2 class="name">NAME</h2>
<p> TiLP2 &#8211; a communication program for TI calculators (&#8216;Tilp Is a Linking Program&#8217;)</p>
<h2>SYNOPSYS</h2>
<p> <code>tilp</code> [-h / &#8211;help] [-v / &#8211;version] [&#8211;calc=] [&#8211;cable=] [&#8211;port=] [&#8211;timeout=] [&#8211;delay=] [&#8211;silent] [&#8211;no-gui] [filename] </p>
<h2>DESCRIPTION</h2>
<p> The <code>TiLP</code> program allows you to backup, restore and archive variables and/or applications for your Texas Instruments calculator on your computer. It has also additional features such as screen dump, remote control, ROM dump, FLASHing. TiLP is a very complete program. Moreover, you have the same program for all calculator models. </p>
<h2>OPTIONS</h2>
<p> The command line of tilp can be used for sending files like variables, backup, FLASH apps, OS, TiGroup, etc. You cannot do any other operations. If you want more operations, you have to use the GUI. For sending one or more files, simply pass the filename(s) on the command line. If you want to use TiLP from console, use the &#8211;no-gui switch. </p>
<p> Take care: options must be passed before the filename! </p>
<p> <code>tilp</code> accepts the following options: </p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Display a list of all command line options. </p>
<dt><code>-v, &#8211;version</code></p>
<dd> Output the version info. </p>
<dt><code>&#8211;no-gui</code>, <code>-n</code></p>
<dd> Send file(s) without launching any Graphical User Interface. All information is displayed in the console. Beware: using this switch disables any overwrite check. Use it with care! </p>
<dt><code>&#8211;silent</code>, <code>-s</code></p>
<dd> Skip questions in no GUI mode. Should be used with &#8211;no-gui switch. </p>
<dt><code>&#8211;calc=</code><i>CALC</i>, <i>CALC</i></p>
<dd> Select a calculator type: v200, ti92+, ti92, ti89t, ti89, ti86, ti85, ti84+, ti83+, ti83, ti82, ti73 or nspire. </p>
<dt><code>&#8211;cable=</code><i>CABLE</i>, <i>CABLE</i></p>
<dd> Select a link cable type: GrayLink, BlackLink, Parallel, SilverLink, DirectLink, VTi, TiEmu. </p>
<dt><code>&#8211;port=</code><i>PORT</i>, <code>-p</code><i>PORT</i></p>
<dd> Specify on which port the link cable is plugged on. Can be null, 1, 2, 3 or 4. </p>
<dt><code>&#8211;timeout=</code><i>TIMEOUT</i>, <code>-t</code><i>TIMEOUT</i></p>
<dd> in tenth of seconds (0.1 s). The program waits for a response of the calculator during that amount of time. Once this delay is elapsed, the program sends a timeout error. The default value is 1 second. </p>
<dt><code>&#8211;delay=</code><i>DELAY</i>, <code>-d</code><i>DELAY</i></p>
<dd> in microseconds. This is the time which separates the transmission of 2 bytes (in the old cables). The default value is 5 microseconds. Decreasing this value increases the transfer speed but decreases the reliability of the transmission. </p>
</dl>
<h2>EXAMPLE</h2>
<p> Quickly send (no GUI) a file to a TI-89 through a BlackLink cable on the second serial port (/dev/ttyS1 or COM2), setting the timeout to 2s: </p>
<dl>
<dt>tilp &#8211;calc=ti89 &#8211;cable=BlackLink &#8211;port=2 &#8211;timeout=20 &#8211;no-gui group.89g</p>
<dd>
<dt>Starting at version 1.13, a new and shorter syntax can be used:</p>
<dd>
<dt>tilp ti89 blacklink -p2 -t20 -n group.89g</p>
<dd>
</dl>
<h2>CONFIG FILE FORMAT</h2>
<p> This section describes the format of the .tilp config file which is in the home directory of the user (*nix, Win32), or the old tilp.ini file formerly stored alongside the program (Win32). The file is separated into several sections (hardware, gui, calc, external programs, fonts, screen, misc). A line preceded by the &#8216;#&#8217; symbol is a comment. Each line has the following format: option=something. Every line can be put in any order. Beware: any comment added to the file will be overwritten! Here&#8217;s a description of the options and their possible values: </p>
<p> <code>version=</code> Which version of TiLP has written the config file. Used to display the Release the file and to keep compatibility. </p>
<p> <code>calc_model=</code> Defines the calculator type. Choose one of the following values (case insensitive): ti73, ti82, ti83, ti83+, ti84+, ti85, ti86, ti89, ti92, ti92+, v200, nspire. </p>
<p> <code>cable_model=</code> Define the link cable type (case sensitive). Choose one of the following value: GrayLink, BlackLink, Parallel, SilverLink, DirectLink, VTi or TiEmu. </p>
<p> <code>cable_port=</code> Define the port to use. You have to choose one of the following value depending on your link cable type and the port you want use: parallel port #[1-3], serial port #[1-4], virtual port #[1-2], USB port #[1-4]. </p>
<p> <code>cable_timeout=</code> with the timeout value to use in tenth of seconds. Default value: 20. </p>
<p> <code>cable_delay=</code> with the delay value to use in micro-seconds for home-made cables. Default value: 10 </p>
<p> <code>pane_x_size=</code> and <code>pane_y_size=</code> Gives the width and height values of the remote view. </p>
<p> <code>wnd_x_size1=</code> and <code>wnd_y_size1=</code> Gives the width and height of the windows in full view. </p>
<p> <code>wnd_x_size2=</code> and <code>wnd_y_size2=</code> Gives the width and height of the windows in simplified view (no right frame). </p>
<p> <code>local_sort=</code> Define the sorting method for the right window. Choose one of the following value: name, date, size, user, group, attrib </p>
<p> <code>local_sort_order=</code> Define the sorting order for the right window. Choose either &#8216;up&#8217; or &#8216;down&#8217;. </p>
<p> <code>remote_sort=</code> Define the sorting method for the left window. Choose one of the following value: name, info, type, size </p>
<p> <code>remote_sort_order=</code> Define the sorting order for the left window. Choose either &#8216;up&#8217; or &#8216;down&#8217;. </p>
<p> <code>filesel_type=</code> File selector type (1: gtk, 2: native, 3: kde). </p>
<p> <code>full_gui=</code> Display the right frame (local view). </p>
<p> <code>local_path=</code> Use full path when sending variables. </p>
<p> <code>show_all=</code> Show all files (1) or only TI files (0). </p>
<p> <code>overwrite=</code> Defines whether TiLP should ask for confirmation when you attempt to delete files/variables. Use with care! </p>
<p> <code>recv_as_group=</code> Receive set of files as a grouped file if enabled. </p>
<p> <code>working_dir=</code> Contains the directory that TiLP will list at startup. Can be changed from the popup menu. </p>
<p> <code>remote_font_name=</code> Define the font to use in the left window (calc files). The font is described by its XFLD (X-Font Logical Description) name. </p>
<p> <code>local_font_name=</code> Define the font to use in the right window (computer files). The font is described by its XFLD name, such as: -adobe-courier-medium-r-*-*-*-125-*-*-*-*-*-* </p>
<p> <code>screen_format=</code> Define the image format to use for saving screen captures. It can be: xpm (1), jpg, bmp, tif, png, pdf and eps (7). </p>
<p> <code>screen_scaling=</code> Unused. </p>
<p> <code>screen_clipping=</code> If enabled, display only the LCD area. Otherwise, displays the full area (the hidden part is only usable via ASM programming on TI89). </p>
<p> <code>screen_blurry=</code> Define whether the image is saved in B&amp;W or saved like a VTi image (dark &amp; light gray). </p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1999-2006, Romain Lievin. Permission to use, copy, modify, and distribute this software and its documentation for any purpose and without fee is hereby granted, provided that the above copyright notice appear in all copies and that both that copyright notice and this permission notice appear in supporting documentation. </p>
<p> This program and its source code is distributed under the terms of the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA. </p>
<h2>SUGGESTIONS AND BUG REPORTS</h2>
<p> The canonical place to find TiLP2 and some miscellaneous information is at <a rel="nofollow" href="http://www.tilp.info">http://www.tilp.info</a> (redirected to <a href="http://lpg.ticalc.org/prj_tilp/index.php)">http://lpg.ticalc.org/prj_tilp/index.php)</a> You can also look at <a rel="nofollow" href="http://lpg.ticalc.org">http://lpg.ticalc.org</a> and <a href="http://www.ticalc.org">http://www.ticalc.org</a> for others TI related programs for Linux. French people can also look at <a href="http://www.ti-fr.org">http://www.ti-fr.org</a> and <a href="http://tiplanet.org.">http://tiplanet.org.</a> </p>
<h2>AUTHOR</h2>
<p> Original author (Linux &amp; Win32): Romain Lievin. </p>
<p> Mac OS-X port by Julien Blache. </p>
<p> FreeBSD port by Tijl Coosemans. </p>
<h2>THANKS</h2>
<p> Thanks to these people for having lent me their calculator: Jean-Pierre and Thomas (TI92+), Benoit, Philippe and Florence (TI89), Louis (TI86), Luc (TI85), Nicolas (TI83), Jean-Philippe and Francois (TI82). Special thanks to Guillaume for his Grey/Gray TIGL link cable. Thanks to many others (patches, suggestions, &#8230;) </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-tilp/">tilp</a>(1) <a href="/docs/linux/man/1-tiemu/">tiemu</a>(1) </p>
<h2>Index</h2>
