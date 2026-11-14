---
title: "x(7)"
name: "x"
section: "7"
letter: "x"
url: "/docs/linux/man/7-x/"
description: "X – a portable, network-transparent window system"
---

<p>X &#8211; a portable, network-transparent window system</p>
<h2>Overview</h2>
<p>The X Window System is a network transparent window system which runs on a wide range of computing and graphics machines. It should be relatively straightforward to build the X.Org Foundation software distribution on most ANSI C and POSIX compliant systems. Commercial implementations are also available for a wide range of platforms. </p>
<p> The X.Org Foundation requests that the following names be used when referring to this software: </p>
<p> <center></p>
<table>
<tr VALIGN=top>
<td ALIGN=center>X
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>X Window System
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>X Version 11
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>X Window System, Version 11
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>X11
</td>
</tr>
</table>
<p></center> </p>
<p> <i>X Window System</i> is a trademark of The Open Group.</p>
<h2>Description</h2>
<p>X Window System servers run on computers with bitmap displays. The server distributes user input to and accepts output requests from various client programs through a variety of different interprocess communication channels. Although the most common case is for the client programs to be running on the same machine as the server, clients can be run transparently from other machines (including machines with different architectures and operating systems) as well. </p>
<p> X supports overlapping hierarchical subwindows and text and graphics operations, on both monochrome and color displays. For a full explanation of the functions that are available, see the <i>Xlib &#8211; C Language X Interface</i> manual, the <i>X Window System Protocol</i> specification, the <i>X Toolkit Intrinsics &#8211; C Language Interface</i> manual, and various toolkit documents. </p>
<p> The number of programs that use <i>X</i> is quite large. Programs provided in the core X.Org Foundation distribution include: a terminal emulator, <i>xterm</i>; a window manager, <i>twm</i>; a display manager, <i>xdm</i>; a console redirect program, <i>xconsole</i>; a mail interface, <i>xmh</i>; a bitmap editor, <i>bitmap</i>; resource listing/manipulation tools, <i>appres</i>, <i>editres</i>; access control programs, <i>xauth</i>, <i>xhost</i>, and <i>iceauth</i>; user preference setting programs, <i>xrdb</i>, <i>xcmsdb</i>, <i>xset</i>, <i>xsetroot</i>, <i>xstdcmap</i>, and <i>xmodmap</i>; clocks, <i>xclock</i> and <i>oclock</i>; a font displayer, <i>xfd</i>; utilities for listing information about fonts, windows, and displays, <i>xlsfonts</i>, <i>xwininfo</i>, <i>xlsclients</i>, <i>xdpyinfo</i>, <i>xlsatoms</i>, and <i>xprop</i>; screen image manipulation utilities, <i>xwd</i>, <i>xwud</i>, and <i>xmag</i>; a performance measurement utility, <i>x11perf</i>; a font compiler, <i>bdftopcf</i>; a font server and related utilities, <i>xfs</i>, <i>fsinfo</i>, <i>fslsfonts</i>, <i>fstobdf</i>; a display server and related utilities, <i>Xserver</i>, <i>rgb</i>, <i>mkfontdir</i>; a clipboard manager, <i>xclipboard</i>; keyboard description compiler and related utilities, <i>xkbcomp</i>, <i>setxkbmap</i> <i>xkbprint</i>, <i>xkbbell</i>, <i>xkbevd</i>, <i>xkbvleds</i>, and <i>xkbwatch</i>; a utility to terminate clients, <i>xkill</i>; a firewall security proxy, <i>xfwp</i>; a proxy manager to control them, <i>proxymngr</i>; a utility to find proxies, <i>xfindproxy</i>; web browser plug-ins, <i>libxrx.so</i> and <i>libxrxnest.so</i>; an RX MIME-type helper program, <i>xrx</i>; and a utility to cause part or all of the screen to be redrawn, <i>xrefresh</i>. </p>
<p> Many other utilities, window managers, games, toolkits, etc. are included as user-contributed software in the X.Org Foundation distribution, or are available on the Internet. See your site administrator for details.</p>
<h2>Starting Up</h2>
<p>There are two main ways of getting the X server and an initial set of client applications started. The particular method used depends on what operating system you are running and whether or not you use other window systems in addition to X.</p>
<dl>
<dt><code>Display Manager</code></p>
<dd>If you want to always have X running on your display, your site administrator can set your machine up to use a Display Manager such as <i>xdm</i>, <i>gdm</i>, or <i>kdm</i>. This program is typically started by the system at boot time and takes care of keeping the server running and getting users logged in. If you are running one of these display managers, you will normally see a window on the screen welcoming you to the system and asking for your login information. Simply type them in as you would at a normal terminal. If you make a mistake, the display manager will display an error message and ask you to try again. After you have successfully logged in, the display manager will start up your X environment. The documentation for the display manager you use can provide more details.</p>
<dt><i>xinit</i> (run manually from the shell)</p>
<dd>Sites that support more than one window system might choose to use the <i>xinit</i> program for starting X manually. If this is true for your machine, your site administrator will probably have provided a program named &quot;x11&quot;, &quot;startx&quot;, or &quot;xstart&quot; that will do site-specific initialization (such as loading convenient default resources, running a window manager, displaying a clock, and starting several terminal emulators) in a nice way. If not, you can build such a script using the <i>xinit</i> program. This utility simply runs one user-specified program to start the server, runs another to start up any desired clients, and then waits for either to finish. Since either or both of the user-specified programs may be a shell script, this gives substantial flexibility at the expense of a nice interface. For this reason, <i>xinit</i> is not intended for end users.</dl>
<h2>Display Names</h2>
<p>From the user&#8217;s perspective, every X server has a <i>display name</i> of the form: </p>
<dl>
<dd><i>hostname:displaynumber.screennumber</i></dl>
<p> This information is used by the application to determine how it should connect to the server and which screen it should use by default (on displays with multiple monitors):</p>
<dl>
<dt><i>hostname</i></p>
<dd>The <i>hostname</i> specifies the name of the machine to which the display is physically connected. If the hostname is not given, the most efficient way of communicating to a server on the same machine will be used.</p>
<dt><i>displaynumber</i></p>
<dd>The phrase &quot;display&quot; is usually used to refer to a collection of monitors that share a common set of input devices (keyboard, mouse, tablet, etc.). Most workstations tend to only have one display. Larger, multi-user systems, however, frequently have several displays so that more than one person can be doing graphics work at once. To avoid confusion, each display on a machine is assigned a <i>display number</i> (beginning at 0) when the X server for that display is started. The display number must always be given in a display name.</p>
<dt><i>screennumber</i></p>
<dd>Some displays share their input devices among two or more monitors. These may be configured as a single logical screen, which allows windows to move across screens, or as individual screens, each with their own set of windows. If configured such that each monitor has its own set of windows, each screen is assigned a <i>screen number</i> (beginning at 0) when the X server for that display is started. If the screen number is not given, screen 0 will be used.</dl>
<p> On POSIX systems, the default display name is stored in your DISPLAY environment variable. This variable is set automatically by the <i>xterm</i> terminal emulator. However, when you log into another machine on a network, you may need to set DISPLAY by hand to point to your display. For example, </p>
<pre> % setenv DISPLAY myws:0
 $ DISPLAY=myws:0; export DISPLAY</pre>
<p>The <i>ssh</i> program can be used to start an X program on a remote machine; it automatically sets the DISPLAY variable correctly. </p>
<p> Finally, most X programs accept a command line option of <code>-display </code><i>displayname</i> to temporarily override the contents of DISPLAY. This is most commonly used to pop windows on another person&#8217;s screen or as part of a &quot;remote shell&quot; command to start an xterm pointing back to your display. For example, </p>
<pre> % xeyes -display joesws:0 -geometry 1000x1000+0+0
 % rsh big xterm -display myws:0 -ls &lt;/dev/null &amp;</pre>
<p>X servers listen for connections on a variety of different communications channels (network byte streams, shared memory, etc.). Since there can be more than one way of contacting a given server, The <i>hostname</i> part of the display name is used to determine the type of channel (also called a transport layer) to be used. X servers generally support the following types of connections:</p>
<dl>
<dt><i>local</i></p>
<dd>The hostname part of the display name should be the empty string. For example: <i>:0</i>, <i>:1</i>, and <i>:0.1</i>. The most efficient local transport will be chosen.</p>
<dt><i>TCP/IP</i></p>
<dd>The hostname part of the display name should be the server machine&#8217;s hostname or IP address. Full Internet names, abbreviated names, IPv4 addresses, and IPv6 addresses are all allowed. For example: <i>x.org:0</i>, <i>expo:0</i>, <i>[::1]:0</i>, <i>198.112.45.11:0</i>, <i>bigmachine:1</i>, and <i>hydra:0.1</i>.</dl>
<h2>Access Control</h2>
<p>An X server can use several types of access control. Mechanisms provided in Release 7 are: </p>
<table>
<tr VALIGN=top>
<td>Host Access </td>
<td>Simple host-based access control.
</td>
</tr>
<tr VALIGN=top>
<td>MIT-MAGIC-COOKIE-1</td>
<td>Shared plain-text &quot;cookies&quot;.
</td>
</tr>
<tr VALIGN=top>
<td>XDM-AUTHORIZATION-1</td>
<td>Secure DES based private-keys.
</td>
</tr>
<tr VALIGN=top>
<td>SUN-DES-1 </td>
<td>Based on Sun&#8217;s secure rpc system.
</td>
</tr>
<tr VALIGN=top>
<td>Server Interpreted</td>
<td>Server-dependent methods of access control
</td>
</tr>
</table>
<p> <i>Xdm</i> initializes access control for the server and also places authorization information in a file accessible to the user. </p>
<p> Normally, the list of hosts from which connections are always accepted should be empty, so that only clients with are explicitly authorized can connect to the display. When you add entries to the host list (with <i>xhost</i>), the server no longer performs any authorization on connections from those machines. Be careful with this. </p>
<p> The file from which <i>Xlib</i> extracts authorization data can be specified with the environment variable <code>XAUTHORITY</code>, and defaults to the file <code>.Xauthority</code> in the home directory. <i>Xdm</i> uses <code>$HOME/.Xauthority</code> and will create it or merge in authorization records if it already exists when a user logs in. </p>
<p> If you use several machines and share a common home directory across all of the machines by means of a network file system, you never really have to worry about authorization files, the system should work correctly by default. Otherwise, as the authorization files are machine-independent, you can simply copy the files to share them. To manage authorization files, use <i>xauth</i>. This program allows you to extract records and insert them into other files. Using this, you can send authorization to remote machines when you login, if the remote machine does not share a common home directory with your local machine. Note that authorization information transmitted &#8220;in the clear&#8221; through a network file system or using <i>ftp</i> or <i>rcp</i> can be &#8220;stolen&#8221; by a network eavesdropper, and as such may enable unauthorized access. In many environments, this level of security is not a concern, but if it is, you need to know the exact semantics of the particular authorization data to know if this is actually a problem. </p>
<p> For more information on access control, see the <i><a href="/docs/linux/man/7-xsecurity/">Xsecurity</a></i>(7) manual page.</p>
<h2>Geometry Specifications</h2>
<p>One of the advantages of using window systems instead of hardwired terminals is that applications don&#8217;t have to be restricted to a particular size or location on the screen. Although the layout of windows on a display is controlled by the window manager that the user is running (described below), most X programs accept a command line argument of the form <code>-geometry </code><i>WIDTHxHEIGHT+XOFF+YOFF</i> (where <i>WIDTH</i>, <i>HEIGHT</i>, <i>XOFF</i>, and <i>YOFF</i> are numbers) for specifying a preferred size and location for this application&#8217;s main window. </p>
<p> The <i>WIDTH</i> and <i>HEIGHT</i> parts of the geometry specification are usually measured in either pixels or characters, depending on the application. The <i>XOFF</i> and <i>YOFF</i> parts are measured in pixels and are used to specify the distance of the window from the left or right and top and bottom edges of the screen, respectively. Both types of offsets are measured from the indicated edge of the screen to the corresponding edge of the window. The X offset may be specified in the following ways:</p>
<dl>
<dt><i>+XOFF</i></p>
<dd>The left edge of the window is to be placed <i>XOFF</i> pixels in from the left edge of the screen (i.e., the X coordinate of the window&#8217;s origin will be <i>XOFF</i>). <i>XOFF</i> may be negative, in which case the window&#8217;s left edge will be off the screen.</p>
<dt><i>-XOFF</i></p>
<dd>The right edge of the window is to be placed <i>XOFF</i> pixels in from the right edge of the screen. <i>XOFF</i> may be negative, in which case the window&#8217;s right edge will be off the screen.</dl>
<p> The Y offset has similar meanings:</p>
<dl>
<dt><i>+YOFF</i></p>
<dd>The top edge of the window is to be <i>YOFF</i> pixels below the top edge of the screen (i.e., the Y coordinate of the window&#8217;s origin will be <i>YOFF</i>). <i>YOFF</i> may be negative, in which case the window&#8217;s top edge will be off the screen.</p>
<dt><i>-YOFF</i></p>
<dd>The bottom edge of the window is to be <i>YOFF</i> pixels above the bottom edge of the screen. <i>YOFF</i> may be negative, in which case the window&#8217;s bottom edge will be off the screen.</dl>
<p> Offsets must be given as pairs; in other words, in order to specify either <i>XOFF</i> or <i>YOFF</i> both must be present. Windows can be placed in the four corners of the screen using the following specifications:</p>
<dl>
<dt><i>+0+0</i></p>
<dd>upper left hand corner.</p>
<dt><i>-0+0</i></p>
<dd>upper right hand corner.</p>
<dt><i>-0-0</i></p>
<dd>lower right hand corner.</p>
<dt><i>+0-0</i></p>
<dd>lower left hand corner.</dl>
<p> In the following examples, a terminal emulator is placed in roughly the center of the screen and a load average monitor, mailbox, and clock are placed in the upper right hand corner: </p>
<pre> xterm -fn 6x10 -geometry 80x24+30+200 &amp;
 xclock -geometry 48x48-0+0 &amp;
 xload -geometry 48x48-96+0 &amp;
 xbiff -geometry 48x48-48+0 &amp;</pre>
<h2>Window Managers</h2>
<p>The layout of windows on the screen is controlled by special programs called <i>window managers</i>. Although many window managers will honor geometry specifications as given, others may choose to ignore them (requiring the user to explicitly draw the window&#8217;s region on the screen with the pointer, for example). </p>
<p> Since window managers are regular (albeit complex) client programs, a variety of different user interfaces can be built. The X.Org Foundation distribution comes with a window manager named <i>twm</i> which supports overlapping windows, popup menus, point-and-click or click-to-type input models, title bars, nice icons (and an icon manager for those who don&#8217;t like separate icon windows). </p>
<p> See the user-contributed software in the X.Org Foundation distribution for other popular window managers.</p>
<h2>Font Names</h2>
<p>Collections of characters for displaying text and symbols in X are known as <i>fonts</i>. A font typically contains images that share a common appearance and look nice together (for example, a single size, boldness, slant, and character set). Similarly, collections of fonts that are based on a common type face (the variations are usually called roman, bold, italic, bold italic, oblique, and bold oblique) are called <i>families</i>. </p>
<p> Fonts come in various sizes. The X server supports <i>scalable</i> fonts, meaning it is possible to create a font of arbitrary size from a single source for the font. The server supports scaling from <i>outline</i> fonts and <i>bitmap</i> fonts. Scaling from outline fonts usually produces significantly better results than scaling from bitmap fonts. </p>
<p> An X server can obtain fonts from individual files stored in directories in the file system, or from one or more font servers, or from a mixtures of directories and font servers. The list of places the server looks when trying to find a font is controlled by its <i>font path</i>. Although most installations will choose to have the server start up with all of the commonly used font directories in the font path, the font path can be changed at any time with the <i>xset</i> program. However, it is important to remember that the directory names are on the <code>server</code>&#8216;s machine, not on the application&#8217;s. </p>
<p> Bitmap font files are usually created by compiling a textual font description into binary form, using <i>bdftopcf</i>. Font databases are created by running the <i>mkfontdir</i> program in the directory containing the source or compiled versions of the fonts. Whenever fonts are added to a directory, <i>mkfontdir</i> should be rerun so that the server can find the new fonts. To make the server reread the font database, reset the font path with the <i>xset</i> program. For example, to add a font to a private directory, the following commands could be used: </p>
<pre> % cp newfont.pcf ~/myfonts
 % mkfontdir ~/myfonts
 % xset fp rehash</pre>
<p>The <i>xfontsel</i> and <i>xlsfonts</i> programs can be used to browse through the fonts available on a server. Font names tend to be fairly long as they contain all of the information needed to uniquely identify individual fonts. However, the X server supports wildcarding of font names, so the full specification </p>
<pre> <i>-adobe-courier-medium-r-normal--10-100-75-75-m-60-iso8859-1</i></pre>
<p>might be abbreviated as: </p>
<pre> <i>-*-courier-medium-r-normal--*-100-*-*-*-*-iso8859-1</i></pre>
<p>Because the shell also has special meanings for <i>*</i> and <i>?</i>, wildcarded font names should be quoted: </p>
<pre> % xlsfonts -fn '-*-courier-medium-r-normal--*-100-*-*-*-*-*-*'</pre>
<p>The <i>xlsfonts</i> program can be used to list all of the fonts that match a given pattern. With no arguments, it lists all available fonts. This will usually list the same font at many different sizes. To see just the base scalable font names, try using one of the following patterns: </p>
<pre> <i>-*-*-*-*-*-*-0-0-0-0-*-0-*-*</i>
 <i>-*-*-*-*-*-*-0-0-75-75-*-0-*-*</i>
 <i>-*-*-*-*-*-*-0-0-100-100-*-0-*-*</i></pre>
<p>To convert one of the resulting names into a font at a specific size, replace one of the first two zeros with a nonzero value. The field containing the first zero is for the pixel size; replace it with a specific height in pixels to name a font at that size. Alternatively, the field containing the second zero is for the point size; replace it with a specific size in decipoints (there are 722.7 decipoints to the inch) to name a font at that size. The last zero is an average width field, measured in tenths of pixels; some servers will anamorphically scale if this value is specified.</p>
<h2>Font Server Names</h2>
<p>One of the following forms can be used to name a font server that accepts TCP connections: </p>
<pre> tcp/<i>hostname</i>:<i>port</i>
 tcp/<i>hostname</i>:<i>port</i>/<i>cataloguelist</i></pre>
<p>The <i>hostname</i> specifies the name (or decimal numeric address) of the machine on which the font server is running. The <i>port</i> is the decimal TCP port on which the font server is listening for connections. The <i>cataloguelist</i> specifies a list of catalogue names, with &#8216;+&#8217; as a separator. </p>
<p> Examples: <i>tcp/x.org:7100</i>, <i>tcp/198.112.45.11:7100/all</i>.</p>
<h2>Color Names</h2>
<p>Most applications provide ways of tailoring (usually through resources or command line arguments) the colors of various elements in the text and graphics they display. A color can be specified either by an abstract color name, or by a numerical color specification. The numerical specification can identify a color in either device-dependent (RGB) or device-independent terms. Color strings are case-insensitive. </p>
<p> X supports the use of abstract color names, for example, &quot;red&quot;, &quot;blue&quot;. A value for this abstract name is obtained by searching one or more color name databases. <i>Xlib</i> first searches zero or more client-side databases; the number, location, and content of these databases is implementation dependent. If the name is not found, the color is looked up in the X server&#8217;s database. The text form of this database is commonly stored in the file <i>/usr/share/X11/rgb.txt</i>. </p>
<p> A numerical color specification consists of a color space name and a set of values in the following syntax: </p>
<pre> <i>&lt;color_space_name&gt;</i>:<i>&lt;value&gt;/.../&lt;value&gt;</i></pre>
<p>An RGB Device specification is identified by the prefix &quot;rgb:&quot; and has the following syntax: </p>
<pre> rgb:<i>&lt;red&gt;/&lt;green&gt;/&lt;blue&gt;</i>
 <i>&lt;red&gt;</i>, <i>&lt;green&gt;</i>, <i>&lt;blue&gt;</i> := <i>h</i> | <i>hh</i> | <i>hhh</i> | <i>hhhh</i>
 <i>h</i> := single hexadecimal digits</pre>
<p>Note that <i>h</i> indicates the value scaled in 4 bits, <i>hh</i> the value scaled in 8 bits, <i>hhh</i> the value scaled in 12 bits, and <i>hhhh</i> the value scaled in 16 bits, respectively. These values are passed directly to the X server, and are assumed to be gamma corrected. </p>
<p> The eight primary colors can be represented as: </p>
<p> <center></p>
<table>
<tr VALIGN=top>
<td>black</td>
<td>rgb:0/0/0
</td>
</tr>
<tr VALIGN=top>
<td>red</td>
<td>rgb:ffff/0/0
</td>
</tr>
<tr VALIGN=top>
<td>green</td>
<td>rgb:0/ffff/0
</td>
</tr>
<tr VALIGN=top>
<td>blue</td>
<td>rgb:0/0/ffff
</td>
</tr>
<tr VALIGN=top>
<td>yellow</td>
<td>rgb:ffff/ffff/0
</td>
</tr>
<tr VALIGN=top>
<td>magenta</td>
<td>rgb:ffff/0/ffff
</td>
</tr>
<tr VALIGN=top>
<td>cyan</td>
<td>rgb:0/ffff/ffff
</td>
</tr>
<tr VALIGN=top>
<td>white</td>
<td>rgb:ffff/ffff/ffff
</td>
</tr>
</table>
<p></center> </p>
<p> For backward compatibility, an older syntax for RGB Device is supported, but its continued use is not encouraged. The syntax is an initial sharp sign character followed by a numeric specification, in one of the following formats: </p>
<p> <center></p>
<table>
<tr VALIGN=top>
<td>#RGB </td>
<td>(4 bits each)
</td>
</tr>
<tr VALIGN=top>
<td>#RRGGBB </td>
<td>(8 bits each)
</td>
</tr>
<tr VALIGN=top>
<td>#RRRGGGBBB</td>
<td>(12 bits each)
</td>
</tr>
<tr VALIGN=top>
<td>#RRRRGGGGBBBB</td>
<td>(16 bits each)
</td>
</tr>
</table>
<p></center> </p>
<p> The R, G, and B represent single hexadecimal digits. When fewer than 16 bits each are specified, they represent the most-significant bits of the value (unlike the &quot;rgb:&quot; syntax, in which values are scaled). For example, #3a7 is the same as #3000a0007000. </p>
<p> An RGB intensity specification is identified by the prefix &quot;rgbi:&quot; and has the following syntax: </p>
<pre> rgbi:<i>&lt;red&gt;/&lt;green&gt;/&lt;blue&gt;</i></pre>
<p>The red, green, and blue are floating point values between 0.0 and 1.0, inclusive. They represent linear intensity values, with 1.0 indicating full intensity, 0.5 half intensity, and so on. These values will be gamma corrected by <i>Xlib</i> before being sent to the X server. The input format for these values is an optional sign, a string of numbers possibly containing a decimal point, and an optional exponent field containing an E or e followed by a possibly signed integer string. </p>
<p> The standard device-independent string specifications have the following syntax: </p>
<p> <center></p>
<table>
<tr VALIGN=top>
<td>CIEXYZ:<i>&lt;X&gt;/&lt;Y&gt;/&lt;Z&gt;</i></td>
<td>(<i>none</i>, 1, <i>none</i>)
</td>
</tr>
<tr VALIGN=top>
<td>CIEuvY:<i>&lt;u&gt;/&lt;v&gt;/&lt;Y&gt;</i></td>
<td>(~.6, ~.6, 1)
</td>
</tr>
<tr VALIGN=top>
<td>CIExyY:<i>&lt;x&gt;/&lt;y&gt;/&lt;Y&gt;</i></td>
<td>(~.75, ~.85, 1)
</td>
</tr>
<tr VALIGN=top>
<td>CIELab:<i>&lt;L&gt;/&lt;a&gt;/&lt;b&gt;</i></td>
<td>(100, <i>none</i>, <i>none</i>)
</td>
</tr>
<tr VALIGN=top>
<td>CIELuv:<i>&lt;L&gt;/&lt;u&gt;/&lt;v&gt;</i></td>
<td>(100, <i>none</i>, <i>none</i>)
</td>
</tr>
<tr VALIGN=top>
<td>TekHVC:<i>&lt;H&gt;/&lt;V&gt;/&lt;C&gt;</i></td>
<td>(360, 100, 100)
</td>
</tr>
</table>
<p></center> </p>
<p> All of the values (C, H, V, X, Y, Z, a, b, u, v, y, x) are floating point values. Some of the values are constrained to be between zero and some upper bound; the upper bounds are given in parentheses above. The syntax for these values is an optional &#8216;+&#8217; or &#8216;-&#8216; sign, a string of digits possibly containing a decimal point, and an optional exponent field consisting of an &#8216;E&#8217; or &#8216;e&#8217; followed by an optional &#8216;+&#8217; or &#8216;-&#8216; followed by a string of digits. </p>
<p> For more information on device independent color, see the <i>Xlib</i> reference manual.</p>
<h2>Keyboards</h2>
<p>The X keyboard model is broken into two layers: server-specific codes (called <i>keycodes</i>) which represent the physical keys, and server-independent symbols (called <i>keysyms</i>) which represent the letters or words that appear on the keys. Two tables are kept in the server for converting keycodes to keysyms:</p>
<dl>
<dt><i>modifier list</i></p>
<dd>Some keys (such as Shift, Control, and Caps Lock) are known as <i>modifier</i> and are used to select different symbols that are attached to a single key (such as Shift-a generates a capital A, and Control-l generates a control character ^L). The server keeps a list of keycodes corresponding to the various modifier keys. Whenever a key is pressed or released, the server generates an <i>event</i> that contains the keycode of the indicated key as well as a mask that specifies which of the modifier keys are currently pressed. Most servers set up this list to initially contain the various shift, control, and shift lock keys on the keyboard.</p>
<dt><i>keymap table</i></p>
<dd>Applications translate event keycodes and modifier masks into keysyms using a <i>keysym table</i> which contains one row for each keycode and one column for various modifier states. This table is initialized by the server to correspond to normal typewriter conventions. The exact semantics of how the table is interpreted to produce keysyms depends on the particular program, libraries, and language input method used, but the following conventions for the first four keysyms in each row are generally adhered to:</dl>
<p> The first four elements of the list are split into two groups of keysyms. Group 1 contains the first and second keysyms; Group 2 contains the third and fourth keysyms. Within each group, if the first element is alphabetic and the the second element is the special keysym <i>NoSymbol</i>, then the group is treated as equivalent to a group in which the first element is the lowercase letter and the second element is the uppercase letter. </p>
<p> Switching between groups is controlled by the keysym named MODE SWITCH, by attaching that keysym to some key and attaching that key to any one of the modifiers Mod1 through Mod5. This modifier is called the &#8220;group modifier.&#8221; Group 1 is used when the group modifier is off, and Group 2 is used when the group modifier is on. </p>
<p> Within a group, the modifier state determines which keysym to use. The first keysym is used when the Shift and Lock modifiers are off. The second keysym is used when the Shift modifier is on, when the Lock modifier is on and the second keysym is uppercase alphabetic, or when the Lock modifier is on and is interpreted as ShiftLock. Otherwise, when the Lock modifier is on and is interpreted as CapsLock, the state of the Shift modifier is applied first to select a keysym; but if that keysym is lowercase alphabetic, then the corresponding uppercase keysym is used instead.</p>
<h2>Options</h2>
<p>Most X programs attempt to use the same names for command line options and arguments. All applications written with the X Toolkit Intrinsics automatically accept the following options:</p>
<dl>
<dt><code>-display </code><i>display</i></p>
<dd>This option specifies the name of the X server to use.</p>
<dt><code>-geometry </code><i>geometry</i></p>
<dd>This option specifies the initial size and location of the window.</p>
<dt><code>-bg </code><i>color</i>, <code>-background </code><i>color</i></p>
<dd>Either option specifies the color to use for the window background.</p>
<dt><code>-bd </code><i>color</i>, <code>-bordercolor </code><i>color</i></p>
<dd>Either option specifies the color to use for the window border.</p>
<dt><code>-bw </code><i>number</i>, <code>-borderwidth </code><i>number</i></p>
<dd>Either option specifies the width in pixels of the window border.</p>
<dt><code>-fg </code><i>color</i>, <code>-foreground </code><i>color</i></p>
<dd>Either option specifies the color to use for text or graphics.</p>
<dt><code>-fn </code><i>font</i>, <code>-font </code><i>font</i></p>
<dd>Either option specifies the font to use for displaying text.</p>
<dt><code>-iconic</code></p>
<dd>This option indicates that the user would prefer that the application&#8217;s windows initially not be visible as if the windows had be immediately iconified by the user. Window managers may choose not to honor the application&#8217;s request.</p>
<dt><code>-name</code></p>
<dd>This option specifies the name under which resources for the application should be found. This option is useful in shell aliases to distinguish between invocations of an application, without resorting to creating links to alter the executable file name.</p>
<dt><code>-rv</code>, <code>-reverse</code></p>
<dd>Either option indicates that the program should simulate reverse video if possible, often by swapping the foreground and background colors. Not all programs honor this or implement it correctly. It is usually only used on monochrome displays.</p>
<dt><code>+rv</code></p>
<dd>This option indicates that the program should not simulate reverse video. This is used to override any defaults since reverse video doesn&#8217;t always work properly.</p>
<dt><code>-selectionTimeout</code></p>
<dd>This option specifies the timeout in milliseconds within which two communicating applications must respond to one another for a selection request.</p>
<dt><code>-synchronous</code></p>
<dd>This option indicates that requests to the X server should be sent synchronously, instead of asynchronously. Since <i>Xlib</i> normally buffers requests to the server, errors do not necessarily get reported immediately after they occur. This option turns off the buffering so that the application can be debugged. It should never be used with a working program.</p>
<dt><code>-title </code><i>string</i></p>
<dd>This option specifies the title to be used for this window. This information is sometimes used by a window manager to provide some sort of header identifying the window.</p>
<dt><code>-xnllanguage </code><i>language[_territory][.codeset]</i></p>
<dd>This option specifies the language, territory, and codeset for use in resolving resource and other filenames.</p>
<dt><code>-xrm </code><i>resourcestring</i></p>
<dd>This option specifies a resource name and value to override any defaults. It is also very useful for setting resources that don&#8217;t have explicit command line arguments.</dl>
<h2>Resources</h2>
<p>To make the tailoring of applications to personal preferences easier, X provides a mechanism for storing default values for program resources (e.g. background color, window title, etc.) that is used by programs that use toolkits based on the X Toolkit Intrinsics library libXt. (Programs using the common Gtk+ and Qt toolkits use other configuration mechanisms.) Resources are specified as strings that are read in from various places when an application is run. Program components are named in a hierarchical fashion, with each node in the hierarchy identified by a class and an instance name. At the top level is the class and instance name of the application itself. By convention, the class name of the application is the same as the program name, but with the first letter capitalized (e.g. <i>Bitmap</i> or <i>Emacs</i>) although some programs that begin with the letter &#8220;x&#8221; also capitalize the second letter for historical reasons. </p>
<p> The precise syntax for resources is: </p>
<pre>ResourceLine = Comment | IncludeFile | ResourceSpec | &lt;empty line&gt;
Comment = &quot;!&quot; {&lt;any character except null or newline&gt;}
IncludeFile = &quot;#&quot; WhiteSpace &quot;include&quot; WhiteSpace FileName WhiteSpace
FileName = &lt;valid filename for operating system&gt;
ResourceSpec = WhiteSpace ResourceName WhiteSpace &quot;:&quot; WhiteSpace Value
ResourceName = [Binding] {Component Binding} ComponentName
Binding = &quot;.&quot; | &quot;*&quot;
WhiteSpace = {&lt;space&gt; | &lt;horizontal tab&gt;}
Component = &quot;?&quot; | ComponentName
ComponentName = NameChar {NameChar}
NameChar = &quot;a&quot;-&quot;z&quot; | &quot;A&quot;-&quot;Z&quot; | &quot;0&quot;-&quot;9&quot; | &quot;_&quot; | &quot;-&quot;
Value = {&lt;any character except null or unescaped newline&gt;}</pre>
<p>Elements separated by vertical bar (|) are alternatives. Curly braces ({&#8230;}) indicate zero or more repetitions of the enclosed elements. Square brackets ([&#8230;]) indicate that the enclosed element is optional. Quotes (&quot;&#8230;&quot;) are used around literal characters. </p>
<p> IncludeFile lines are interpreted by replacing the line with the contents of the specified file. The word &quot;include&quot; must be in lowercase. The filename is interpreted relative to the directory of the file in which the line occurs (for example, if the filename contains no directory or contains a relative directory specification). </p>
<p> If a ResourceName contains a contiguous sequence of two or more Binding characters, the sequence will be replaced with single &quot;.&quot; character if the sequence contains only &quot;.&quot; characters, otherwise the sequence will be replaced with a single &quot;*&quot; character. </p>
<p> A resource database never contains more than one entry for a given ResourceName. If a resource file contains multiple lines with the same ResourceName, the last line in the file is used. </p>
<p> Any whitespace character before or after the name or colon in a ResourceSpec are ignored. To allow a Value to begin with whitespace, the two-character sequence &#8220;\<i>space</i>&#8221; (backslash followed by space) is recognized and replaced by a space character, and the two-character sequence &#8220;\<i>tab</i>&#8221; (backslash followed by horizontal tab) is recognized and replaced by a horizontal tab character. To allow a Value to contain embedded newline characters, the two-character sequence &#8220;
&#8221; is recognized and replaced by a newline character. To allow a Value to be broken across multiple lines in a text file, the two-character sequence &#8220;\<i>newline</i>&#8221; (backslash followed by newline) is recognized and removed from the value. To allow a Value to contain arbitrary character codes, the four-character sequence &#8220;\<i>nnn</i>&#8221;, where each <i>n</i> is a digit character in the range of &#8220;0&#8221;-&#8220;7&#8221;, is recognized and replaced with a single byte that contains the octal value specified by the sequence. Finally, the two-character sequence &#8220;\&#8221; is recognized and replaced with a single backslash. </p>
<p> When an application looks for the value of a resource, it specifies a complete path in the hierarchy, with both class and instance names. However, resource values are usually given with only partially specified names and classes, using pattern matching constructs. An asterisk (*) is a loose binding and is used to represent any number of intervening components, including none. A period (.) is a tight binding and is used to separate immediately adjacent components. A question mark (?) is used to match any single component name or class. A database entry cannot end in a loose binding; the final component (which cannot be &quot;?&quot;) must be specified. The lookup algorithm searches the resource database for the entry that most closely matches (is most specific for) the full name and class being queried. When more than one database entry matches the full name and class, precedence rules are used to select just one. </p>
<p> The full name and class are scanned from left to right (from highest level in the hierarchy to lowest), one component at a time. At each level, the corresponding component and/or binding of each matching entry is determined, and these matching components and bindings are compared according to precedence rules. Each of the rules is applied at each level, before moving to the next level, until a rule selects a single entry over all others. The rules (in order of precedence) are:</p>
<dl>
<dt>1.</p>
<dd>An entry that contains a matching component (whether name, class, or &quot;?&quot;) takes precedence over entries that elide the level (that is, entries that match the level in a loose binding).</p>
<dt>2.</p>
<dd>An entry with a matching name takes precedence over both entries with a matching class and entries that match using &quot;?&quot;. An entry with a matching class takes precedence over entries that match using &quot;?&quot;.</p>
<dt>3.</p>
<dd>An entry preceded by a tight binding takes precedence over entries preceded by a loose binding.</dl>
<p> Programs based on the X Toolkit Intrinsics obtain resources from the following sources (other programs usually support some subset of these sources):</p>
<dl>
<dt><code>RESOURCE_MANAGER root window property</code></p>
<dd>Any global resources that should be available to clients on all machines should be stored in the RESOURCE_MANAGER property on the root window of the first screen using the <i>xrdb</i> program. This is frequently taken care of when the user starts up X through the display manager or <i>xinit</i>.</p>
<dt><code>SCREEN_RESOURCES root window property</code></p>
<dd>Any resources specific to a given screen (e.g. colors) that should be available to clients on all machines should be stored in the SCREEN_RESOURCES property on the root window of that screen. The <i>xrdb</i> program will sort resources automatically and place them in RESOURCE_MANAGER or SCREEN_RESOURCES, as appropriate.</p>
<dt><code>application-specific files</code></p>
<dd>Directories named by the environment variable XUSERFILESEARCHPATH or the environment variable XAPPLRESDIR (which names a single directory and should end with a &#8216;/&#8217; on POSIX systems), plus directories in a standard place (usually under /usr/share/X11/, but this can be overridden with the XFILESEARCHPATH environment variable) are searched for for application-specific resources. For example, application default resources are usually kept in /usr/share/X11/app-defaults/. See the <i>X Toolkit Intrinsics &#8211; C Language Interface</i> manual for details.</p>
<dt><code>XENVIRONMENT</code></p>
<dd>Any user- and machine-specific resources may be specified by setting the XENVIRONMENT environment variable to the name of a resource file to be loaded by all applications. If this variable is not defined, a file named <i>$HOME</i>/.Xdefaults-<i>hostname</i> is looked for instead, where <i>hostname</i> is the name of the host where the application is executing.</p>
<dt><code>-xrm </code><i>resourcestring</i></p>
<dd>Resources can also be specified from the command line. The <i>resourcestring</i> is a single resource name and value as shown above. Note that if the string contains characters interpreted by the shell (e.g., asterisk), they must be quoted. Any number of <code>-xrm</code> arguments may be given on the command line.</dl>
<p> Program resources are organized into groups called <i>classes</i>, so that collections of individual resources (each of which are called <i>instances</i>) can be set all at once. By convention, the instance name of a resource begins with a lowercase letter and class name with an upper case letter. Multiple word resources are concatenated with the first letter of the succeeding words capitalized. Applications written with the X Toolkit Intrinsics will have at least the following resources: </p>
<dl>
<dt><code>background (</code>class<code> Background)</code></p>
<dd>This resource specifies the color to use for the window background.</dl>
<dl>
<dt><code>borderWidth (</code>class<code> BorderWidth)</code></p>
<dd>This resource specifies the width in pixels of the window border.</dl>
<dl>
<dt><code>borderColor (</code>class<code> BorderColor)</code></p>
<dd>This resource specifies the color to use for the window border.</dl>
<p> Most applications using the X Toolkit Intrinsics also have the resource <code>foreground</code> (class <code>Foreground</code>), specifying the color to use for text and graphics within the window. </p>
<p> By combining class and instance specifications, application preferences can be set quickly and easily. Users of color displays will frequently want to set Background and Foreground classes to particular defaults. Specific color instances such as text cursors can then be overridden without having to define all of the related resources. For example, </p>
<pre> bitmap*Dashed: off
 XTerm*cursorColor: gold
 XTerm*multiScroll: on
 XTerm*jumpScroll: on
 XTerm*reverseWrap: on
 XTerm*curses: on
 XTerm*Font: 6x10
 XTerm*scrollBar: on
 XTerm*scrollbar*thickness: 5
 XTerm*multiClickTime: 500
 XTerm*charClass: 33:48,37:48,45-47:48,64:48
 XTerm*cutNewline: off
 XTerm*cutToBeginningOfLine: off
 XTerm*titeInhibit: on
 XTerm*ttyModes: intr ^c erase ^? kill ^u
 XLoad*Background: gold
 XLoad*Foreground: red
 XLoad*highlight: black
 XLoad*borderWidth: 0
 emacs*Geometry: 80x65-0-0
 emacs*Background: rgb:5b/76/86
 emacs*Foreground: white
 emacs*Cursor: white
 emacs*BorderColor: white
 emacs*Font: 6x10
 xmag*geometry: -0-0
 xmag*borderColor: white</pre>
<p>If these resources were stored in a file called <i>.Xresources</i> in your home directory, they could be added to any existing resources in the server with the following command: </p>
<pre> % xrdb -merge $HOME/.Xresources</pre>
<p>This is frequently how user-friendly startup scripts merge user-specific defaults into any site-wide defaults. All sites are encouraged to set up convenient ways of automatically loading resources. See the <i>Xlib</i> manual section <i>Resource Manager Functions</i> for more information.</p>
<h2>Environment</h2>
<dl>
<dt><code>DISPLAY</code></p>
<dd>This is the only mandatory environment variable. It must point to an X server. See section &quot;Display Names&quot; above.</p>
<dt><code>XAUTHORITY</code></p>
<dd>This must point to a file that contains authorization data. The default is <i>$HOME/.Xauthority</i>. See <code><a href="/docs/linux/man/7-xsecurity/">Xsecurity</a></code>(7), <code><a href="/docs/linux/man/1-xauth/">xauth</a></code>(1), <code><a href="/docs/linux/man/1-xdm/">xdm</a></code>(1), <code><a href="/docs/linux/man/3-xau/">Xau</a></code>(3).</p>
<dt><code>ICEAUTHORITY</code></p>
<dd>This must point to a file that contains authorization data. The default is <i>$HOME/.ICEauthority</i>.</p>
<dt><code>LC_ALL</code>, <code>LC_CTYPE</code>, <code>LANG</code></p>
<dd>The first non-empty value among these three determines the current locale&#8217;s facet for character handling, and in particular the default text encoding. See <code><a href="/docs/linux/man/7-locale/">locale</a></code>(7), <code><a href="/docs/linux/man/3-setlocale/">setlocale</a></code>(3), <code><a href="/docs/linux/man/1-locale/">locale</a></code>(1).</p>
<dt><code>XMODIFIERS</code></p>
<dd>This variable can be set to contain additional information important for the current locale setting. Typically set to <i>@im=&lt;input-method&gt;</i> to enable a particular input method. See <code><a href="/docs/linux/man/3-xsetlocalemodifiers/">XSetLocaleModifiers</a></code>(3).</p>
<dt><code>XLOCALEDIR</code></p>
<dd>This must point to a directory containing the locale.alias file and Compose and XLC_LOCALE file hierarchies for all locales. The default value is<i> /usr/share/X11/locale</i>.</p>
<dt><code>XENVIRONMENT</code></p>
<dd>This must point to a file containing X resources. The default is <i>$HOME/.Xdefaults-&lt;hostname&gt;</i>. Unlike <i>$HOME/.Xresources</i>, it is consulted each time an X application starts.</p>
<dt><code>XFILESEARCHPATH</code></p>
<dd>This must contain a colon separated list of path templates, where libXt will search for resource files. The default value consists of </p>
<pre> /etc/X11/%L/%T/%N%C%S:\
 /etc/X11/%l/%T/%N%C%S:\
 /etc/X11/%T/%N%C%S:\
 /etc/X11/%L/%T/%N%S:\
 /etc/X11/%l/%T/%N%S:\
 /etc/X11/%T/%N%S:\
 /usr/share/X11/%L/%T/%N%C%S:\
 /usr/share/X11/%l/%T/%N%C%S:\
 /usr/share/X11/%T/%N%C%S:\
 /usr/share/X11/%L/%T/%N%S:\
 /usr/share/X11/%l/%T/%N%S:\
 /usr/share/X11/%T/%N%S:\
 /usr/lib/x86_64-linux-gnu/X11/%L/%T/%N%C%S:\
 /usr/lib/x86_64-linux-gnu/X11/%l/%T/%N%C%S:\
 /usr/lib/x86_64-linux-gnu/X11/%T/%N%C%S:\
 /usr/lib/x86_64-linux-gnu/X11/%L/%T/%N%S:\
 /usr/lib/x86_64-linux-gnu/X11/%l/%T/%N%S:\
 /usr/lib/x86_64-linux-gnu/X11/%T/%N%S</pre>
<p>A path template is transformed to a pathname by substituting: </p>
<pre> %D =&gt; the implementation-specific default path
 %N =&gt; name (basename) being searched for
 %T =&gt; type (dirname) being searched for
 %S =&gt; suffix being searched for
 %C =&gt; value of the resource &quot;customization&quot;
 (class &quot;Customization&quot;)
 %L =&gt; the locale name
 %l =&gt; the locale's language (part before '_')
 %t =&gt; the locale's territory (part after '_` but before '.')
 %c =&gt; the locale's encoding (part after '.')</pre>
<dt><code>XUSERFILESEARCHPATH</code></p>
<dd>This must contain a colon separated list of path templates, where libXt will search for user dependent resource files. The default value is: </p>
<pre> $XAPPLRESDIR/%L/%N%C:\
 $XAPPLRESDIR/%l/%N%C:\
 $XAPPLRESDIR/%N%C:\
 $HOME/%N%C:\
 $XAPPLRESDIR/%L/%N:\
 $XAPPLRESDIR/%l/%N:\
 $XAPPLRESDIR/%N:\
 $HOME/%N</pre>
<p>$XAPPLRESDIR defaults to <i>$HOME</i>, see below. </p>
<p> A path template is transformed to a pathname by substituting: </p>
<pre> %D =&gt; the implementation-specific default path
 %N =&gt; name (basename) being searched for
 %T =&gt; type (dirname) being searched for
 %S =&gt; suffix being searched for
 %C =&gt; value of the resource &quot;customization&quot;
 (class &quot;Customization&quot;)
 %L =&gt; the locale name
 %l =&gt; the locale's language (part before '_')
 %t =&gt; the locale's territory (part after '_` but before '.')
 %c =&gt; the locale's encoding (part after '.')</pre>
<dt><code>XAPPLRESDIR</code></p>
<dd>This must point to a base directory where the user stores the application dependent resource files. The default value is <i>$HOME</i>. Only used if XUSERFILESEARCHPATH is not set.</p>
<dt><code>XKEYSYMDB</code></p>
<dd>This must point to a file containing nonstandard keysym definitions. The default value is<i> /usr/share/X11/XKeysymDB</i>.</p>
<dt><code>XCMSDB</code></p>
<dd>This must point to a color name database file. The default value is <i> /usr/lib/x86_64-linux-gnu/X11/Xcms.txt</i>.</p>
<dt><code>RESOURCE_NAME</code></p>
<dd>This serves as main identifier for resources belonging to the program being executed. It defaults to the basename of pathname of the program.</p>
<dt><code>SESSION_MANAGER</code></p>
<dd>Denotes the session manager to which the application should connect. See <code><a href="/docs/linux/man/1-xsm/">xsm</a></code>(1), <code><a href="/docs/linux/man/1-rstart/">rstart</a></code>(1).</p>
<dt><code>XF86BIGFONT_DISABLE</code></p>
<dd>Setting this variable to a non-empty value disables the XFree86-Bigfont extension. This extension is a mechanism to reduce the memory consumption of big fonts by use of shared memory.</dl>
<p> <code>XKB_FORCE</code><br />
 <code>XKB_DISABLE</code><br />
 <code>XKB_DEBUG</code><br />
 <code>_XKB_CHARSET</code><br />
 <code>_XKB_LOCALE_CHARSETS</code><br />
 <code>_XKB_OPTIONS_ENABLE</code><br />
 <code>_XKB_LATIN1_LOOKUP</code><br />
 <code>_XKB_CONSUME_LOOKUP_MODS</code><br />
 <code>_XKB_CONSUME_SHIFT_AND_LOCK</code><br />
 <code>_XKB_IGNORE_NEW_KEYBOARDS</code><br />
 <code>_XKB_CONTROL_FALLBACK</code><br />
 <code>_XKB_COMP_LED</code> <code>_XKB_COMP_FAIL_BEEP</code> </p>
<p> These variables influence the X Keyboard Extension.</p>
<h2>Examples</h2>
<p>The following is a collection of sample command lines for some of the more frequently used commands. For more information on a particular command, please refer to that command&#8217;s manual page. </p>
<pre> % xrdb $HOME/.Xresources
 % xmodmap -e &quot;keysym BackSpace = Delete&quot;
 % mkfontdir /usr/local/lib/X11/otherfonts
 % xset fp+ /usr/local/lib/X11/otherfonts
 % xmodmap $HOME/.keymap.km
 % xsetroot -solid 'rgbi:.8/.8/.8'
 % xset b 100 400 c 50 s 1800 r on
 % xset q
 % twm
 % xmag
 % xclock -geometry 48x48-0+0 -bg blue -fg white
 % xeyes -geometry 48x48-48+0
 % xbiff -update 20
 % xlsfonts '*helvetica*'
 % xwininfo -root
 % xdpyinfo -display joesworkstation:0
 % xhost -joesworkstation
 % xrefresh
 % xwd | xwud
 % bitmap companylogo.bm 32x32
 % xcalc -bg blue -fg magenta
 % xterm -geometry 80x66-0-0 -name myxterm $*</pre>
<h2>Diagnostics</h2>
<p>A wide variety of error messages are generated from various programs. The default error handler in <i>Xlib</i> (also used by many toolkits) uses standard resources to construct diagnostic messages when errors occur. The defaults for these messages are usually stored in <i>/usr/share/X11/XErrorDB</i>. If this file is not present, error messages will be rather terse and cryptic. </p>
<p> When the X Toolkit Intrinsics encounter errors converting resource strings to the appropriate internal format, no error messages are usually printed. This is convenient when it is desirable to have one set of resources across a variety of displays (e.g. color vs. monochrome, lots of fonts vs. very few, etc.), although it can pose problems for trying to determine why an application might be failing. This behavior can be overridden by the setting the <i>StringConversionWarnings</i> resource. </p>
<p> To force the X Toolkit Intrinsics to always print string conversion error messages, the following resource should be placed in the file that gets loaded onto the RESOURCE_MANAGER property using the <i>xrdb</i> program (frequently called <i>.Xresources</i> or <i>.Xres</i> in the user&#8217;s home directory): </p>
<pre> *StringConversionWarnings: on</pre>
<p>To have conversion messages printed for just a particular application, the appropriate instance name can be placed before the asterisk: </p>
<pre> xterm*StringConversionWarnings: on</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-xorgfoundation/">XOrgFoundation</a></code>(7), <code><a href="/docs/linux/man/7-xstandards/">XStandards</a></code>(7), <code><a href="/docs/linux/man/7-xsecurity/">Xsecurity</a></code>(7), <code><a href="/docs/linux/man/1-appres/">appres</a></code>(1), <code><a href="/docs/linux/man/1-bdftopcf/">bdftopcf</a></code>(1), <code><a href="/docs/linux/man/1-bitmap/">bitmap</a></code>(1), <code><a href="/docs/linux/man/1-editres/">editres</a></code>(1), <code><a href="/docs/linux/man/1-fsinfo/">fsinfo</a></code>(1), <code><a href="/docs/linux/man/1-fslsfonts/">fslsfonts</a></code>(1), <code><a href="/docs/linux/man/1-fstobdf/">fstobdf</a></code>(1), <code><a href="/docs/linux/man/1-iceauth/">iceauth</a></code>(1), <code><a href="/docs/linux/man/1-imake/">imake</a></code>(1), <code><a href="/docs/linux/man/1-makedepend/">makedepend</a></code>(1), <code><a href="/docs/linux/man/1-mkfontdir/">mkfontdir</a></code>(1), <code><a href="/docs/linux/man/1-oclock/">oclock</a></code>(1), <code><a href="/docs/linux/man/1-proxymngr/">proxymngr</a></code>(1), <code><a href="/docs/linux/man/1-rgb/">rgb</a></code>(1), <code><a href="/docs/linux/man/1-resize/">resize</a></code>(1), <code><a href="/docs/linux/man/1-rstart/">rstart</a></code>(1), <code><a href="/docs/linux/man/1-smproxy/">smproxy</a></code>(1), <code><a href="/docs/linux/man/1-twm/">twm</a></code>(1), <code><a href="/docs/linux/man/1-x11perf/">x11perf</a></code>(1), <code><a href="/docs/linux/man/1-x11perfcomp/">x11perfcomp</a></code>(1), <code><a href="/docs/linux/man/1-xauth/">xauth</a></code>(1), <code><a href="/docs/linux/man/1-xclipboard/">xclipboard</a></code>(1), <code><a href="/docs/linux/man/1-xclock/">xclock</a></code>(1), <code><a href="/docs/linux/man/1-xcmsdb/">xcmsdb</a></code>(1), <code><a href="/docs/linux/man/1-xconsole/">xconsole</a></code>(1), <code><a href="/docs/linux/man/1-xdm/">xdm</a></code>(1), <code><a href="/docs/linux/man/1-xdpyinfo/">xdpyinfo</a></code>(1), <code><a href="/docs/linux/man/1-xfd/">xfd</a></code>(1), <code><a href="/docs/linux/man/1-xfindproxy/">xfindproxy</a></code>(1), <code><a href="/docs/linux/man/1-xfs/">xfs</a></code>(1), <code><a href="/docs/linux/man/1-xfwp/">xfwp</a></code>(1), <code><a href="/docs/linux/man/1-xhost/">xhost</a></code>(1), <code><a href="/docs/linux/man/1-xinit/">xinit</a></code>(1), <code><a href="/docs/linux/man/1-xkbbell/">xkbbell</a></code>(1), <code><a href="/docs/linux/man/1-xkbcomp/">xkbcomp</a></code>(1), <code><a href="/docs/linux/man/1-xkbevd/">xkbevd</a></code>(1), <code><a href="/docs/linux/man/1-xkbprint/">xkbprint</a></code>(1), <code><a href="/docs/linux/man/1-xkbvleds/">xkbvleds</a></code>(1), <code><a href="/docs/linux/man/1-xkbwatch/">xkbwatch</a></code>(1), <code><a href="/docs/linux/man/1-xkill/">xkill</a></code>(1), <code><a href="/docs/linux/man/1-xlogo/">xlogo</a></code>(1), <code><a href="/docs/linux/man/1-xlsatoms/">xlsatoms</a></code>(1), <code><a href="/docs/linux/man/1-xlsclients/">xlsclients</a></code>(1), <code><a href="/docs/linux/man/1-xlsfonts/">xlsfonts</a></code>(1), <code><a href="/docs/linux/man/1-xmag/">xmag</a></code>(1), <code><a href="/docs/linux/man/1-xmh/">xmh</a></code>(1), <code><a href="/docs/linux/man/1-xmodmap/">xmodmap</a></code>(1), <code><a href="/docs/linux/man/1-xprop/">xprop</a></code>(1), <code><a href="/docs/linux/man/1-xrdb/">xrdb</a></code>(1), <code><a href="/docs/linux/man/1-xrefresh/">xrefresh</a></code>(1), <code><a href="/docs/linux/man/1-xrx/">xrx</a></code>(1), <code><a href="/docs/linux/man/1-xset/">xset</a></code>(1), <code><a href="/docs/linux/man/1-xsetroot/">xsetroot</a></code>(1), <code><a href="/docs/linux/man/1-xsm/">xsm</a></code>(1), <code><a href="/docs/linux/man/1-xstdcmap/">xstdcmap</a></code>(1), <code><a href="/docs/linux/man/1-xterm/">xterm</a></code>(1), <code><a href="/docs/linux/man/1-xwd/">xwd</a></code>(1), <code><a href="/docs/linux/man/1-xwininfo/">xwininfo</a></code>(1), <code><a href="/docs/linux/man/1-xwud/">xwud</a></code>(1). <code><a href="/docs/linux/man/1-xserver/">Xserver</a></code>(1), <code><a href="/docs/linux/man/1-xorg/">Xorg</a></code>(1), <code><a href="/docs/linux/man/1-xdmx/">Xdmx</a></code>(1), <code><a href="/docs/linux/man/1-xephyr/">Xephyr</a></code>(1), <code><a href="/docs/linux/man/1-xnest/">Xnest</a></code>(1), <code><a href="/docs/linux/man/1-xquartz/">Xquartz</a></code>(1), <code><a href="/docs/linux/man/1-xvfb/">Xvfb</a></code>(1), <code><a href="/docs/linux/man/1-xvnc/">Xvnc</a></code>(1), <code><a href="/docs/linux/man/1-xwin/">XWin</a></code>(1). <i>Xlib &#8211; C Language X Interface</i>, and <i>X Toolkit Intrinsics &#8211; C Language Interface</i></p>
<h2>Trademarks</h2>
<p>X Window System is a trademark of The Open Group.</p>
<h2>Authors</h2>
<p>A cast of thousands, literally. Releases 6.7 and later are brought to you by the X.Org Foundation. The names of all people who made it a reality will be found in the individual documents and source files. </p>
<p> Releases 6.6 and 6.5 were done by The X.Org Group. Release 6.4 was done by The X Project Team. The Release 6.3 distribution was from The X Consortium, Inc. The staff members at the X Consortium responsible for that release were: Donna Converse (emeritus), Stephen Gildea (emeritus), Kaleb Keithley, Matt Landau (emeritus), Ralph Mor (emeritus), Janet O&#8217;Halloran, Bob Scheifler, Ralph Swick, Dave Wiggins (emeritus), and Reed Augliere. </p>
<p> The X Window System standard was originally developed at the Laboratory for Computer Science at the Massachusetts Institute of Technology, and all rights thereto were assigned to the X Consortium on January 1, 1994. X Consortium, Inc. closed its doors on December 31, 1996. All rights to the X Window System have been assigned to The Open Group.</p>
