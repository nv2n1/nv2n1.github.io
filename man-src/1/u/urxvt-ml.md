---
title: "urxvt-ml(1)"
name: "urxvt-ml"
section: "1"
letter: "u"
url: "/docs/linux/man/1-urxvt-ml/"
description: "rxvt-unicode (ouR XVT, unicode) – (a VT102 emulator for the X window system)"
---

<h2 class="name">NAME</h2>
<p> rxvt-unicode (ouR XVT, unicode) &#8211; (a VT102 emulator for the X window system) </p>
<h2>SYNOPSIS</h2>
<p> <code>urxvt-ml</code> [options] [-e command [ args ]]</p>
<h2>DESCRIPTION</h2>
<p> <code>rxvt-unicode</code>, version <code>9.21</code>, is a colour vt102 terminal emulator intended as an <i><a href="/docs/linux/man/1-xterm/">xterm</a></i>(1) replacement for users who do not require features such as Tektronix 4014 emulation and toolkit-style configurability. As a result, <code>rxvt-unicode</code> uses much less swap space &#8212; a significant advantage on a machine serving many X sessions. </p>
<p> This document is also available on the World-Wide-Web at &lt;<a rel="nofollow" href="http://pod.tst.eu/http://cvs.schmorp.de/rxvt-unicode/doc/rxvt.1.pod">http://pod.tst.eu/http://cvs.schmorp.de/rxvt-unicode/doc/rxvt.1.pod</a>&gt;.</p>
<h2>FREQUENTLY ASKED QUESTIONS</h2>
<p> See <a href="/docs/linux/man/7-urxvt-ml/">urxvt-ml</a>(7) (try <tt>&quot;man 7 urxvt-ml&quot;</tt>) for a list of frequently asked questions and answer to them and some common problems. That document is also accessible on the World-Wide-Web at &lt;<a rel="nofollow" href="http://pod.tst.eu/http://cvs.schmorp.de/rxvt-unicode/doc/rxvt.7.pod">http://pod.tst.eu/http://cvs.schmorp.de/rxvt-unicode/doc/rxvt.7.pod</a>&gt;.</p>
<h2>RXVT-UNICODE VS. RXVT</h2>
<p> Unlike the original rxvt, <code>rxvt-unicode</code> stores all text in Unicode internally. That means it can store and display most scripts in the world. Being a terminal emulator, however, some things are very difficult, especially cursive scripts such as arabic, vertically written scripts like mongolian or scripts requiring extremely complex combining rules, like tibetan or devanagari. Don&#8217;t expect pretty output when using these scripts. Most other scripts, latin, cyrillic, kanji, thai etc. should work fine, though. A somewhat difficult case are right-to-left scripts, such as hebrew: <code>rxvt-unicode</code> adopts the view that bidirectional algorithms belong in the application, not the terminal emulator (too many things &#8212; such as cursor-movement while editing &#8212; break otherwise), but that might change. </p>
<p> If you are looking for a terminal that supports more exotic scripts, let me recommend <tt>&quot;mlterm&quot;</tt>, which is a very user friendly, lean and clean terminal emulator. In fact, the reason rxvt-unicode was born was solely because the author couldn&#8217;t get <tt>&quot;mlterm&quot;</tt> to use one font for latin1 and another for japanese. </p>
<p> Therefore another design rationale was the use of multiple fonts to display characters: The idea of a single unicode font which many other programs force onto its users never made sense to me: You should be able to choose any font for any script freely. </p>
<p> Apart from that, rxvt-unicode is also much better internationalised than its predecessor, supports things such as <font SIZE="-1">XFT</font> and <font SIZE="-1">ISO 14755</font> that are handy in i18n-environments, is faster, and has a lot bugs less than the original rxvt. This all in addition to dozens of other small improvements. </p>
<p> It is still faithfully following the original rxvt idea of being lean and nice on resources: for example, you can still configure rxvt-unicode without most of its features to get a lean binary. It also comes with a client/daemon pair that lets you open any number of terminal windows from within a single process, which makes startup time very fast and drastically reduces memory usage. See <a href="/docs/linux/man/1-urxvt-mld/">urxvt-mld</a>(1) (daemon) and <a href="/docs/linux/man/1-urxvt-mlc/">urxvt-mlc</a>(1) (client). </p>
<p> It also makes technical information about escape sequences (which have been extended) more accessible: see <a href="/docs/linux/man/7-urxvt-ml/">urxvt-ml</a>(7) for technical reference documentation (escape sequences etc.).</p>
<h2>OPTIONS</h2>
<p> The <code>urxvt-ml</code> options (mostly a subset of <i>xterm</i>&#8216;s) are listed below. In keeping with the smaller-is-better philosophy, options may be eliminated or default values chosen at compile-time, so options and defaults listed may not accurately reflect the version installed on your system. `urxvt-ml -h&#8217; gives a list of major compile-time options on the <i>Options</i> line. Option descriptions may be prefixed with which compile option each is dependent upon. e.g. `Compile <i></i><font SIZE="-1"><i>XIM</i></font><i></i>:&#8217; requires <i></i><font SIZE="-1"><i>XIM</i></font><i></i> on the <i>Options</i> line. Note: `urxvt-ml -help&#8217; gives a list of all command-line options compiled into your version. </p>
<p> Note that <code>urxvt-ml</code> permits the resource name to be used as a long-option (&#8211;/++ option) so the potential command-line options are far greater than those listed. For example: `urxvt-ml &#8211;loginShell &#8211;color1 Orange&#8217;. </p>
<p> The following options are available:</p>
<dl>
<dt><code>-help</code>, <code>&#8211;help</code></p>
<dd> Print out a message describing available options.</p>
<dt><code>-display</code> <i>displayname</i></p>
<dd> Attempt to open a window on the named X display (the older form <code>-d</code> is still respected. but deprecated). In the absence of this option, the display specified by the <font SIZE="-1"><code>DISPLAY</code></font> environment variable is used.</p>
<dt><code>-depth</code> <i>bitdepth</i></p>
<dd> Compile <i>frills</i>: Attempt to find a visual with the given bit depth; resource <code>depth</code>. </p>
<p> [Please note that many X servers (and libXft) are buggy with respect to <tt>&quot;-depth 32&quot;</tt> and/or alpha channels, and will cause all sorts of graphical corruption. This is harmless, but we can&#8217;t do anything about this, so watch out]</p>
<dt><code>-visual</code> <i>visualID</i></p>
<dd> Compile <i>frills</i>: Use the given visual (see e.g. <tt>&quot;xdpyinfo&quot;</tt> for possible visual ids) instead of the default, and also allocate a private colormap. All visual types except for DirectColor are supported.</p>
<dt><code>-geometry</code> <i>geom</i></p>
<dd> Window geometry (<code>-g</code> still respected); resource <code>geometry</code>.</p>
<dt><code>-rv</code>|<code>+rv</code></p>
<dd> Turn on/off simulated reverse video; resource <code>reverseVideo</code>.</p>
<dt><code>-j</code>|<code>+j</code></p>
<dd> Turn on/off jump scrolling (allow multiple lines per refresh); resource <code>jumpScroll</code>.</p>
<dt><code>-ss</code>|<code>+ss</code></p>
<dd> Turn on/off skip scrolling (allow multiple screens per refresh); resource <code>skipScroll</code>.</p>
<dt><code>-fade</code> <i>number</i></p>
<dd> Fade the text by the given percentage when focus is lost. Small values fade a little only, 100 completely replaces all colours by the fade colour; resource <code>fading</code>.</p>
<dt><code>-fadecolor</code> <i>colour</i></p>
<dd> Fade to this colour when fading is used (see <code>-fade</code>). The default colour is opaque black. resource <code>fadeColor</code>.</p>
<dt><code>-icon</code> <i>file</i></p>
<dd> Compile <i>pixbuf</i>: Use the specified image as application icon. This is used by many window managers, taskbars and pagers to represent the application window; resource <i>iconFile</i>.</p>
<dt><code>-bg</code> <i>colour</i></p>
<dd> Window background colour; resource <code>background</code>.</p>
<dt><code>-fg</code> <i>colour</i></p>
<dd> Window foreground colour; resource <code>foreground</code>.</p>
<dt><code>-cr</code> <i>colour</i></p>
<dd> The cursor colour; resource <code>cursorColor</code>.</p>
<dt><code>-pr</code> <i>colour</i></p>
<dd> The mouse pointer foreground colour; resource <code>pointerColor</code>.</p>
<dt><code>-pr2</code> <i>colour</i></p>
<dd> The mouse pointer background colour; resource <code>pointerColor2</code>.</p>
<dt><code>-bd</code> <i>colour</i></p>
<dd> The colour of the border around the text area and between the scrollbar and the text; resource <code>borderColor</code>.</p>
<dt><code>-fn</code> <i>fontlist</i></p>
<dd> Select the fonts to be used. This is a comma separated list of font names that are checked in order when trying to find glyphs for characters. The first font defines the cell size for characters; other fonts might be smaller, but not (in general) larger. A (hopefully) reasonable default font list is always appended to it. See resource <code>font</code> for more details. </p>
<p> In short, to specify an X11 core font, just specify its name or prefix it with <tt>&quot;x:&quot;</tt>. To specify an XFT-font, you need to prefix it with <tt>&quot;xft:&quot;</tt>, e.g.: </p>
<pre>
   urxvt-ml -fn &quot;xft:Bitstream Vera Sans Mono:pixelsize=15&quot;
   urxvt-ml -fn &quot;9x15bold,xft:Bitstream Vera Sans Mono&quot;
</pre>
<p> See also the question &#8220;How does rxvt-unicode choose fonts?&#8221; in the <font SIZE="-1">FAQ</font> section of <a href="/docs/linux/man/7-urxvt-ml/">urxvt-ml</a>(7).</p>
<dt><code>-fb</code> <i>fontlist</i></p>
<dd> Compile <i>font-styles</i>: The bold font list to use when <code>bold</code> characters are to be printed. See resource <code>boldFont</code> for details.</p>
<dt><code>-fi</code> <i>fontlist</i></p>
<dd> Compile <i>font-styles</i>: The italic font list to use when <i>italic</i> characters are to be printed. See resource <code>italicFont</code> for details.</p>
<dt><code>-fbi</code> <i>fontlist</i></p>
<dd> Compile <i>font-styles</i>: The bold italic font list to use when bold italic characters are to be printed. See resource <code>boldItalicFont</code> for details.</p>
<dt><code>-is</code>|<code>+is</code></p>
<dd> Compile <i>font-styles</i>: Bold/Blink font styles imply high intensity foreground/background (default). See resource <code>intensityStyles</code> for details.</p>
<dt><code>-name</code> <i>name</i></p>
<dd> Specify the application name under which resources are to be obtained, rather than the default executable file name. Name should not contain `.&#8217; or `*&#8217; characters. Also sets the icon and title name.</p>
<dt><code>-ls</code>|<code>+ls</code></p>
<dd> Start as a login-shell/sub-shell; resource <code>loginShell</code>.</p>
<dt><code>-mc</code> <i>milliseconds</i></p>
<dd> Specify the maximum time between multi-click selections.</p>
<dt><code>-ut</code>|<code>+ut</code></p>
<dd> Compile <i>utmp</i>: Inhibit/enable writing a utmp entry; resource <code>utmpInhibit</code>.</p>
<dt><code>-vb</code>|<code>+vb</code></p>
<dd> Turn on/off visual bell on receipt of a bell character; resource <code>visualBell</code>.</p>
<dt><code>-sb</code>|<code>+sb</code></p>
<dd> Turn on/off scrollbar; resource <code>scrollBar</code>.</p>
<dt><code>-sr</code>|<code>+sr</code></p>
<dd> Put scrollbar on right/left; resource <code>scrollBar_right</code>.</p>
<dt><code>-st</code>|<code>+st</code></p>
<dd> Display rxvt (non XTerm/NeXT) scrollbar without/with a trough; resource <code>scrollBar_floating</code>.</p>
<dt><code>-si</code>|<code>+si</code></p>
<dd> Turn on/off scroll-to-bottom on <font SIZE="-1">TTY</font> output inhibit; resource <code>scrollTtyOutput</code> has opposite effect.</p>
<dt><code>-sk</code>|<code>+sk</code></p>
<dd> Turn on/off scroll-to-bottom on keypress; resource <code>scrollTtyKeypress</code>.</p>
<dt><code>-sw</code>|<code>+sw</code></p>
<dd> Turn on/off scrolling with the scrollback buffer as new lines appear. This only takes effect if <code>-si</code> is also given; resource <code>scrollWithBuffer</code>.</p>
<dt><code>-ptab</code>|<code>+ptab</code></p>
<dd> If enabled (default), &#8220;Horizontal Tab&#8221; characters are being stored as actual wide characters in the screen buffer, which makes it possible to select and paste them. Since a horizontal tab is a cursor movement and not an actual glyph, this can sometimes be visually annoying as the cursor on a tab character is displayed as a wide cursor; resource <code>pastableTabs</code>.</p>
<dt><code>-bc</code>|<code>+bc</code></p>
<dd> Blink the cursor; resource <code>cursorBlink</code>.</p>
<dt><code>-uc</code>|<code>+uc</code></p>
<dd> Make the cursor underlined; resource <code>cursorUnderline</code>.</p>
<dt><code>-iconic</code></p>
<dd> Start iconified, if the window manager supports that option. Alternative form is <code>-ic</code>.</p>
<dt><code>-sl</code> <i>number</i></p>
<dd> Save <i>number</i> lines in the scrollback buffer. See resource entry for limits; resource <code>saveLines</code>.</p>
<dt><code>-b</code> <i>number</i></p>
<dd> Compile <i>frills</i>: Internal border of <i>number</i> pixels. See resource entry for limits; resource <code>internalBorder</code>.</p>
<dt><code>-w</code> <i>number</i></p>
<dd> Compile <i>frills</i>: External border of <i>number</i> pixels. Also, <code>-bw</code> and <code>-borderwidth</code>. See resource entry for limits; resource <code>externalBorder</code>.</p>
<dt><code>-bl</code></p>
<dd> Compile <i>frills</i>: Set <font SIZE="-1">MWM</font> hints to request a borderless window, i.e. if honoured by the <font SIZE="-1">WM,</font> the rxvt-unicode window will not have window decorations; resource <code>borderLess</code>. If the window manager does not support <font SIZE="-1">MWM</font> hints (e.g. kwin), enables override-redirect mode.</p>
<dt><code>-override-redirect</code></p>
<dd> Compile <i>frills</i>: Sets override-redirect on the window; resource <code>override-redirect</code>.</p>
<dt><code>-dockapp</code></p>
<dd> Sets the initial state of the window to WithdrawnState, which makes window managers that support this extension treat it as a dockapp.</p>
<dt><code>-sbg</code></p>
<dd> Compile <i>frills</i>: Disable the usage of the built-in block graphics/line drawing characters and just rely on what the specified fonts provide. Use this if you have a good font and want to use its block graphic glyphs; resource <code>skipBuiltinGlyphs</code>.</p>
<dt><code>-lsp</code> <i>number</i></p>
<dd> Compile <i>frills</i>: Lines (pixel height) to insert between each row of the display. Useful to work around font rendering problems; resource <code>lineSpace</code>.</p>
<dt><code>-letsp</code> <i>number</i></p>
<dd> Compile <i>frills</i>: Amount to adjust the computed character width by to control overall letter spacing. Negative values will tighten up the letter spacing, positive values will space letters out more. Useful to work around odd font metrics; resource <code>letterSpace</code>.</p>
<dt><code>-tn</code> <i>termname</i></p>
<dd> This option specifies the name of the terminal type to be set in the <font SIZE="-1"><code>TERM</code></font> environment variable. This terminal type must exist in the <i><a href="/docs/linux/man/5-termcap/">termcap</a>(5)</i> database and should have <i>li#</i> and <i>co#</i> entries; resource <code>termName</code>.</p>
<dt><code>-e</code> <i>command [arguments]</i></p>
<dd> Run the command with its command-line arguments in the <code>urxvt-ml</code> window; also sets the window title and icon name to be the basename of the program being executed if neither <i>-title</i> (<i>-T</i>) nor <i>-n</i> are given on the command line. If this option is used, it must be the last on the command-line. If there is no <code>-e</code> option then the default is to run the program specified by the <font SIZE="-1"><code>SHELL</code></font> environment variable or, failing that, <i><a href="/docs/linux/man/1-sh/">sh</a>(1)</i>. </p>
<p> Please note that you must specify a program with arguments. If you want to run shell commands, you have to specify the shell, like this: </p>
<pre>
  urxvt-ml -e sh -c &quot;shell commands&quot;
</pre>
<dt><code>-title</code> <i>text</i></p>
<dd> Window title (<code>-T</code> still respected); the default title is the basename of the program specified after the <code>-e</code> option, if any, otherwise the application name; resource <code>title</code>.</p>
<dt><code>-n</code> <i>text</i></p>
<dd> Icon name; the default name is the basename of the program specified after the <code>-e</code> option, if any, otherwise the application name; resource <code>iconName</code>.</p>
<dt><code>-C</code></p>
<dd> Capture system console messages.</p>
<dt><code>-pt</code> <i>style</i></p>
<dd> Compile <i></i><font SIZE="-1"><i>XIM</i></font><i></i>: input style for input method; <code>OverTheSpot</code>, <code>OffTheSpot</code>, <code>Root</code>; resource <code>preeditType</code>.</p>
<dt><code>-im</code> <i>text</i></p>
<dd> Compile <i></i><font SIZE="-1"><i>XIM</i></font><i></i>: input method name. resource <code>inputMethod</code>.</p>
<dt><code>-imlocale</code> <i>string</i></p>
<dd> The locale to use for opening the <font SIZE="-1">IM.</font> You can use an <tt>&quot;LC_CTYPE&quot;</tt> of e.g. <tt>&quot;de_DE.UTF-8&quot;</tt> for normal text processing but <tt>&quot;ja_JP.EUC-JP&quot;</tt> for the input extension to be able to input japanese characters while staying in another locale. resource <code>imLocale</code>.</p>
<dt><code>-imfont</code> <i>fontset</i></p>
<dd> Set the font set to use for the X Input Method, see resource <code>imFont</code> for more info.</p>
<dt><code>-tcw</code></p>
<dd> Change the meaning of triple-click selection with the left mouse button. Only effective when the original (non-perl) selection code is in-use. Instead of selecting a full line it will extend the selection to the end of the logical line only. resource <code>tripleclickwords</code>.</p>
<dt><code>-insecure</code></p>
<dd> Enable &#8220;insecure&#8221; mode, which currently enables most of the escape sequences that echo strings. See the resource <code>insecure</code> for more info.</p>
<dt><code>-mod</code> <i>modifier</i></p>
<dd> Override detection of Meta modifier with specified key: <code>alt</code>, <code>meta</code>, <code>hyper</code>, <code>super</code>, <code>mod1</code>, <code>mod2</code>, <code>mod3</code>, <code>mod4</code>, <code>mod5</code>; resource <i>modifier</i>.</p>
<dt><code>-ssc</code>|<code>+ssc</code></p>
<dd> Turn on/off secondary screen (default enabled); resource <code>secondaryScreen</code>.</p>
<dt><code>-ssr</code>|<code>+ssr</code></p>
<dd> Turn on/off secondary screen scroll (default enabled); resource <code>secondaryScroll</code>.</p>
<dt><code>-hold</code>|<code>+hold</code></p>
<dd> Turn on/off hold window after exit support. If enabled, urxvt-ml will not immediately destroy its window when the program executed within it exits. Instead, it will wait till it is being killed or closed by the user; resource <code>hold</code>.</p>
<dt><code>-cd</code> <i>path</i></p>
<dd> Sets the working directory for the shell (or the command specified via <code>-e</code>). The <i>path</i> must be an absolute path and it must exist for urxvt-ml to start; resource <code>chdir</code>.</p>
<dt><code>-xrm</code> <i>string</i></p>
<dd> Works like the X Toolkit option of the same name, by adding the <i>string</i> as if it were specified in a resource file. Resource values specified this way take precedence over all other resource specifications. </p>
<p> Note that you need to use the <i>same</i> syntax as in the .Xdefaults file, e.g. <tt>&quot;*.background: black&quot;</tt>. Also note that all urxvt-ml-specific options can be specified as long-options on the commandline, so use of <code>-xrm</code> is mostly limited to cases where you want to specify other resources (e.g. for input methods) or for compatibility with other programs.</p>
<dt><code>-keysym.</code><i>sym</i> <i>string</i></p>
<dd> Remap a key symbol. See resource <code>keysym</code>.</p>
<dt><code>-embed</code> <i>windowid</i></p>
<dd> Tells urxvt-ml to embed its windows into an already-existing window, which enables applications to easily embed a terminal. </p>
<p> Right now, urxvt-ml will first unmap/map the specified window, so it shouldn&#8217;t be a top-level window. urxvt-ml will also reconfigure it quite a bit, so don&#8217;t expect it to keep some specific state. It&#8217;s best to create an extra subwindow for urxvt-ml and leave it alone. </p>
<p> The window will not be destroyed when urxvt-ml exits. </p>
<p> It might be useful to know that urxvt-ml will not close file descriptors passed to it (except for stdin/out/err, of course), so you can use file descriptors to communicate with the programs within the terminal. This works regardless of whether the <tt>&quot;-embed&quot;</tt> option was used or not. </p>
<p> Here is a short Gtk2-perl snippet that illustrates how this option can be used (a longer example is in <i>doc/embed</i>): </p>
<pre><code>
my $rxvt = new Gtk2::Socket;
$rxvt-&gt;signal_connect_after(realize = &gt; sub {
    my $xid = $_[0]-&gt;window-&gt;get_xid;
    system "urxvt-ml -embed $xid &amp;";
});
</code></pre>
<dt><code>-pty-fd</code> <i>file descriptor</i></p>
<dd> Tells urxvt-ml <font SIZE="-1">NOT</font> to execute any commands or create a new pty/tty pair but instead use the given file descriptor as the tty master. This is useful if you want to drive urxvt-ml as a generic terminal emulator without having to run a program within it. </p>
<p> If this switch is given, urxvt-ml will not create any utmp/wtmp entries and will not tinker with pty/tty permissions &#8211; you have to do that yourself if you want that. </p>
<p> As an extremely special case, specifying <tt>&quot;-1&quot;</tt> will completely suppress pty/tty operations, which is probably only useful in conjunction with some perl extension that manages the terminal. </p>
<p> Here is a example in perl that illustrates how this option can be used (a longer example is in <i>doc/pty-fd</i>): </p>
<p>use IO::Pty;<br />
use Fcntl;<br />
my $pty = new IO::Pty;<br />
fcntl $pty, F_SETFD, 0;<br />
#clear close &#8211; on &#8211; exec system &#8220;urxvt-ml -pty-fd &#8220;.(fileno $pty).&#8221;&amp;&#8221;;<br />
close $pty;<br />
#now communicate with rxvt<br />
my $slave = $pty-&gt;slave;<br />
while (&lt;$slave&gt;) {<br />
    print $slave &#8220;got &lt;$_&gt;
&#8221;<br />
}</p>
<dt><code>-pe</code> <i>string</i></p>
<dd> Comma-separated list of perl extension scripts to use (or not to use) in this terminal instance. See resource <code>perl-ext</code> for details.</dl>
<h2>RESOURCES</h2>
<p> Note: `urxvt-ml &#8211;help&#8217; gives a list of all resources (long options) compiled into your version. All resources are also available as long-options. </p>
<p> You can set and change the resources using X11 tools like <code>xrdb</code>. Many distribution do also load settings from the <code>~/.Xresources</code> file when X starts. urxvt-ml will consult the following files/resources in order, with later settings overwriting earlier ones: </p>
<pre>
  1. app-defaults file in $XAPPLRESDIR
  2. $HOME/.Xdefaults
  3. RESOURCE_MANAGER property on root-window of screen 0
  4. SCREEN_RESOURCES property on root-window of the current screen
  5. $XENVIRONMENT file OR $HOME/.Xdefaults-&lt;nodename&gt;
  6. resources specified via -xrm on the commandline
</pre>
<p> Note that when reading X resources, <code>urxvt-ml</code> recognizes two class names: <code>Rxvt</code> and <code>URxvt</code>. The class name <code>Rxvt</code> allows resources common to both <code>urxvt-ml</code> and the original <i>rxvt</i> to be easily configured, while the class name <code>URxvt</code> allows resources unique to <code>urxvt-ml</code>, to be shared between different <code>urxvt-ml</code> configurations. If no resources are specified, suitable defaults will be used. Command-line arguments can be used to override resource settings. The following resources are supported (you might want to check the urxvt-ml<i><a href="/docs/linux/man/3-perl/">perl</a></i>(3) manpage for additional settings by perl extensions not documented here):</p>
<dl>
<dt><code>depth:</code> <i>bitdepth</i></p>
<dd> Compile <i>xft</i>: Attempt to find a visual with the given bit depth; option <code>-depth</code>.</p>
<dt><code>buffered:</code> <i>boolean</i></p>
<dd> Compile <i>xft</i>: Turn on/off double-buffering for xft (default enabled). On some card/driver combination enabling it slightly decreases performance, on most it greatly helps it. The slowdown is small, so it should normally be enabled.</p>
<dt><code>geometry:</code> <i>geom</i></p>
<dd> Create the window with the specified X window geometry [default 80&#215;24]; option <code>-geometry</code>.</p>
<dt><code>background:</code> <i>colour</i></p>
<dd> Use the specified colour as the window&#8217;s background colour [default White]; option <code>-bg</code>.</p>
<dt><code>foreground:</code> <i>colour</i></p>
<dd> Use the specified colour as the window&#8217;s foreground colour [default Black]; option <code>-fg</code>.</p>
<dt><code>color</code><i>n</i><code>:</code> <i>colour</i></p>
<dd> Use the specified colour for the colour value <i>n</i>, where 0-7 corresponds to low-intensity (normal) colours and 8-15 corresponds to high-intensity (bold = bright foreground, blink = bright background) colours. The canonical names are as follows: 0=black, 1=red, 2=green, 3=yellow, 4=blue, 5=magenta, 6=cyan, 7=white, but the actual colour names used are listed in the <font SIZE="-1"><code>COLOURS AND GRAPHICS</code></font> section. </p>
<p> Colours higher than 15 cannot be set using resources (yet), but can be changed using an escape command (see <a href="/docs/linux/man/7-urxvt-ml/">urxvt-ml</a>(7)). </p>
<p> Colours 16-79 form a standard 4x4x4 colour cube (the same as xterm with 88 colour support). Colours 80-87 are evenly spaces grey steps.</p>
<dt><code>colorBD:</code> <i>colour</i></p>
<dd>
<dt><code>colorIT:</code> <i>colour</i></p>
<dd> Use the specified colour to display bold or italic characters when the foreground colour is the default. If font styles are not available (Compile <i>styles</i>) and this option is unset, reverse video is used instead.</p>
<dt><code>colorUL:</code> <i>colour</i></p>
<dd> Use the specified colour to display underlined characters when the foreground colour is the default.</p>
<dt><code>underlineColor:</code> <i>colour</i></p>
<dd> If set, use the specified colour as the colour for the underline itself. If unset, use the foreground colour.</p>
<dt><code>highlightColor:</code> <i>colour</i></p>
<dd> If set, use the specified colour as the background for highlighted characters. If unset, use reverse video.</p>
<dt><code>highlightTextColor:</code> <i>colour</i></p>
<dd> If set and highlightColor is set, use the specified colour as the foreground for highlighted characters.</p>
<dt><code>cursorColor:</code> <i>colour</i></p>
<dd> Use the specified colour for the cursor. The default is to use the foreground colour; option <code>-cr</code>.</p>
<dt><code>cursorColor2:</code> <i>colour</i></p>
<dd> Use the specified colour for the colour of the cursor text. For this to take effect, <code>cursorColor</code> must also be specified. The default is to use the background colour.</p>
<dt><code>reverseVideo:</code> <i>boolean</i></p>
<dd> <code>True</code>: simulate reverse video by foreground and background colours; option <code>-rv</code>. <code>False</code>: regular screen colours [default]; option <code>+rv</code>. See note in <font SIZE="-1"><code>COLOURS AND GRAPHICS</code></font> section.</p>
<dt><code>jumpScroll:</code> <i>boolean</i></p>
<dd> <code>True</code>: specify that jump scrolling should be used. When receiving lots of lines, urxvt-ml will only scroll once a whole screen height of lines has been read, resulting in fewer updates while still displaying every received line; option <code>-j</code>. </p>
<p> <code>False</code>: specify that smooth scrolling should be used. urxvt-ml will force a screen refresh on each new line it received; option <code>+j</code>.</p>
<dt><code>skipScroll:</code> <i>boolean</i></p>
<dd> <code>True</code>: (the default) specify that skip scrolling should be used. When receiving lots of lines, urxvt-ml will only scroll once in a while (around 60 times per second), resulting in far fewer updates. This can result in urxvt-ml not ever displaying some of the lines it receives; option <code>-ss</code>. </p>
<p> <code>False</code>: specify that everything is to be displayed, even if the refresh is too fast for the human eye to read anything (or the monitor to display anything); option <code>+ss</code>.</p>
<dt><code>fading:</code> <i>number</i></p>
<dd> Fade the text by the given percentage when focus is lost; option <code>-fade</code>.</p>
<dt><code>fadeColor:</code> <i>colour</i></p>
<dd> Fade to this colour, when fading is used (see <code>fading:</code>). The default colour is black; option <code>-fadecolor</code>.</p>
<dt><code>iconFile:</code> <i>file</i></p>
<dd> Set the application icon pixmap; option <code>-icon</code>.</p>
<dt><code>scrollColor:</code> <i>colour</i></p>
<dd> Use the specified colour for the scrollbar [default #B2B2B2].</p>
<dt><code>troughColor:</code> <i>colour</i></p>
<dd> Use the specified colour for the scrollbar&#8217;s trough area [default #969696]. Only relevant for rxvt (non XTerm/NeXT) scrollbar.</p>
<dt><code>borderColor:</code> <i>colour</i></p>
<dd> The colour of the border around the text area and between the scrollbar and the text.</p>
<dt><code>font:</code> <i>fontlist</i></p>
<dd> Select the fonts to be used. This is a comma separated list of font names that are checked in order when trying to find glyphs for characters. The first font defines the cell size for characters; other fonts might be smaller, but not (in general) larger. A (hopefully) reasonable default font list is always appended to it; option <code>-fn</code>. </p>
<p> Each font can either be a standard X11 core font (<font SIZE="-1">XLFD</font>) name, with optional prefix <tt>&quot;x:&quot;</tt> or a Xft font (Compile <i>xft</i>), prefixed with <tt>&quot;xft:&quot;</tt>. </p>
<p> In addition, each font can be prefixed with additional hints and specifications enclosed in square brackets (<tt>&quot;[]&quot;</tt>). The only available hint currently is <tt>&quot;codeset=codeset-name&quot;</tt>, and this is only used for Xft fonts. </p>
<p> For example, this font resource </p>
<p>URxvt.font : 9x15bold,<br />
    -misc &#8211; fixed &#8211; bold &#8211; r &#8211; normal&#8211; 15 &#8211; 140 &#8211; 75 &#8211; 75 &#8211; c &#8211; 90 &#8211; iso10646 &#8211; 1,<br />
    -misc &#8211; fixed &#8211; medium &#8211; r &#8211; normal&#8211; 15 &#8211; 140 &#8211; 75 &#8211; 75 &#8211; c &#8211; 90 &#8211; iso10646 &#8211; 1,<br />
    [codeset = JISX0208] xft : Kochi Gothic : antialias = false,<br />
                                              xft : Code2000 : antialias = false</p>
<p> specifies five fonts to be used. The first one is <tt>&quot;9x15bold&quot;</tt> (actually the iso8859-1 version of the second font), which is the base font (because it is named first) and thus defines the character cell grid to be 9 pixels wide and 15 pixels high. </p>
<p> The second font is just used to add additional unicode characters not in the base font, likewise the third, which is unfortunately non-bold, but the bold version of the font does contain fewer characters, so this is a useful supplement. </p>
<p> The third font is an Xft font with aliasing turned off, and the characters are limited to the <font SIZE="-1"><code>JIS 0208</code></font> codeset (i.e. japanese kanji). The font contains other characters, but we are not interested in them. </p>
<p> The last font is a useful catch-all font that supplies most of the remaining unicode characters.</p>
<dt><code>boldFont:</code> <i>fontlist</i></p>
<dd>
<dt><code>italicFont:</code> <i>fontlist</i></p>
<dd>
<dt><code>boldItalicFont:</code> <i>fontlist</i></p>
<dd> The font list to use for displaying <code>bold</code>, <i>italic</i> or bold italic characters, respectively. </p>
<p> If specified and non-empty, then the syntax is the same as for the <code>font</code>-resource, and the given font list will be used as is, which makes it possible to substitute completely different font styles for bold and italic. </p>
<p> If unset (the default), a suitable font list will be synthesized by &#8220;morphing&#8221; the normal text font list into the desired shape. If that is not possible, replacement fonts of the desired shape will be tried. </p>
<p> If set, but empty, then this specific style is disabled and the normal text font will being used for the given style.</p>
<dt><code>intensityStyles:</code> <i>boolean</i></p>
<dd> When font styles are not enabled, or this option is enabled (<code>True</code>, option <code>-is</code>, the default), bold/blink font styles imply high intensity foreground/background colours. Disabling this option (<code>False</code>, option <code>+is</code>) disables this behaviour, the high intensity colours are not reachable.</p>
<dt><code>title:</code> <i>string</i></p>
<dd> Set window title string, the default title is the command-line specified after the <code>-e</code> option, if any, otherwise the application name; option <code>-title</code>.</p>
<dt><code>iconName:</code> <i>string</i></p>
<dd> Set the name used to label the window&#8217;s icon or displayed in an icon manager window, it also sets the window&#8217;s title unless it is explicitly set; option <code>-n</code>.</p>
<dt><code>mapAlert:</code> <i>boolean</i></p>
<dd> <code>True</code>: de-iconify (map) on receipt of a bell character. <code>False</code>: no de-iconify (map) on receipt of a bell character [default].</p>
<dt><code>urgentOnBell:</code> <i>boolean</i></p>
<dd> <code>True</code>: set the urgency hint for the wm on receipt of a bell character. <code>False</code>: do not set the urgency hint [default]. </p>
<p> urxvt-ml resets the urgency hint on every focus change.</p>
<dt><code>visualBell:</code> <i>boolean</i></p>
<dd> <code>True</code>: use visual bell on receipt of a bell character; option <code>-vb</code>. <code>False</code>: no visual bell [default]; option <code>+vb</code>.</p>
<dt><code>loginShell:</code> <i>boolean</i></p>
<dd> <code>True</code>: start as a login shell by prepending a `-&#8216; to <code>argv[0]</code> of the shell; option <code>-ls</code>. <code>False</code>: start as a normal sub-shell [default]; option <code>+ls</code>.</p>
<dt><code>multiClickTime:</code> <i>number</i></p>
<dd> Specify the maximum time in milliseconds between multi-click select events. The default is 500 milliseconds; option <code>-mc</code>.</p>
<dt><code>utmpInhibit:</code> <i>boolean</i></p>
<dd> <code>True</code>: inhibit writing record into the system log file <code>utmp</code>; option <code>-ut</code>. <code>False</code>: write record into the system log file <code>utmp</code> [default]; option <code>+ut</code>.</p>
<dt><code>print-pipe:</code> <i>string</i></p>
<dd> Specify a command pipe for vt100 printer [default <i><a href="/docs/linux/man/1-lpr/">lpr</a>(1)</i>]. Use <code>Print</code> to initiate a screen dump to the printer and <code>Ctrl-Print</code> or <code>Shift-Print</code> to include the scrollback as well. </p>
<p> The string will be interpreted as if typed into the shell as-is. </p>
<p> Example: </p>
<pre>
   URxvt.print-pipe: cat &gt; $(TMPDIR=$HOME mktemp urxvt.XXXXXX)
</pre>
<p> This creates a new file in your home directory with the screen contents every time you hit <tt>&quot;Print&quot;</tt>.</p>
<dt><code>scrollstyle:</code> <i>mode</i></p>
<dd> Set scrollbar style to <code>rxvt</code>, <code>plain</code>, <code>next</code> or <code>xterm</code>. <code>plain</code> is the author&#8217;s favourite.</p>
<dt><code>thickness:</code> <i>number</i></p>
<dd> Set the scrollbar width in pixels.</p>
<dt><code>scrollBar:</code> <i>boolean</i></p>
<dd> <code>True</code>: enable the scrollbar [default]; option <code>-sb</code>. <code>False</code>: disable the scrollbar; option <code>+sb</code>.</p>
<dt><code>scrollBar_right:</code> <i>boolean</i></p>
<dd> <code>True</code>: place the scrollbar on the right of the window; option <code>-sr</code>. <code>False</code>: place the scrollbar on the left of the window; option <code>+sr</code>.</p>
<dt><code>scrollBar_floating:</code> <i>boolean</i></p>
<dd> <code>True</code>: display an rxvt scrollbar without a trough; option <code>-st</code>. <code>False</code>: display an rxvt scrollbar with a trough; option <code>+st</code>.</p>
<dt><code>scrollBar_align:</code> <i>mode</i></p>
<dd> Align the <code>top</code>, <code>bottom</code> or <code>centre</code> [default] of the scrollbar thumb with the pointer on middle button press/drag.</p>
<dt><code>scrollTtyOutput:</code> <i>boolean</i></p>
<dd> <code>True</code>: scroll to bottom when tty receives output; option <code>-si</code>. <code>False</code>: do not scroll to bottom when tty receives output; option <code>+si</code>.</p>
<dt><code>scrollWithBuffer:</code> <i>boolean</i></p>
<dd> <code>True</code>: scroll with scrollback buffer when tty receives new lines (i.e. try to show the same lines) and <code>scrollTtyOutput</code> is False; option <code>-sw</code>. <code>False</code>: do not scroll with scrollback buffer when tty receives new lines; option <code>+sw</code>.</p>
<dt><code>scrollTtyKeypress:</code> <i>boolean</i></p>
<dd> <code>True</code>: scroll to bottom when a non-special key is pressed. Special keys are those which are intercepted by rxvt-unicode for special handling and are not passed onto the shell; option <code>-sk</code>. <code>False</code>: do not scroll to bottom when a non-special key is pressed; option <code>+sk</code>.</p>
<dt><code>saveLines:</code> <i>number</i></p>
<dd> Save <i>number</i> lines in the scrollback buffer [default 64]. This resource is limited on most machines to 65535; option <code>-sl</code>.</p>
<dt><code>internalBorder:</code> <i>number</i></p>
<dd> Internal border of <i>number</i> pixels. This resource is limited to 100; option <code>-b</code>.</p>
<dt><code>externalBorder:</code> <i>number</i></p>
<dd> External border of <i>number</i> pixels. This resource is limited to 100; option <code>-w</code>, <code>-bw</code>, <code>-borderwidth</code>.</p>
<dt><code>borderLess:</code> <i>boolean</i></p>
<dd> Set <font SIZE="-1">MWM</font> hints to request a borderless window, i.e. if honoured by the <font SIZE="-1">WM,</font> the rxvt-unicode window will not have window decorations; option <code>-bl</code>.</p>
<dt><code>skipBuiltinGlyphs:</code> <i>boolean</i></p>
<dd> Compile <i>frills</i>: Disable the usage of the built-in block graphics/line drawing characters and just rely on what the specified fonts provide. Use this if you have a good font and want to use its block graphic glyphs; option <code>-sbg</code>.</p>
<dt><code>termName:</code> <i>termname</i></p>
<dd> Specifies the terminal type name to be set in the <font SIZE="-1"><code>TERM</code></font> environment variable; option <code>-tn</code>.</p>
<dt><code>lineSpace:</code> <i>number</i></p>
<dd> Specifies number of lines (pixel height) to insert between each row of the display [default 0]; option <code>-lsp</code>.</p>
<dt><code>meta8:</code> <i>boolean</i></p>
<dd> <code>True</code>: handle Meta (Alt) + keypress to set the 8th bit. <code>False</code>: handle Meta (Alt) + keypress as an escape prefix [default].</p>
<dt><code>mouseWheelScrollPage:</code> <i>boolean</i></p>
<dd> <code>True</code>: the mouse wheel scrolls a page full. <code>False</code>: the mouse wheel scrolls five lines [default].</p>
<dt><code>pastableTabs:</code> <i>boolean</i></p>
<dd> <code>True</code>: store tabs as wide characters. <code>False</code>: interpret tabs as cursor movement only; option <tt>&quot;-ptab&quot;</tt>.</p>
<dt><code>cursorBlink:</code> <i>boolean</i></p>
<dd> <code>True</code>: blink the cursor. <code>False</code>: do not blink the cursor [default]; option <code>-bc</code>.</p>
<dt><code>cursorUnderline:</code> <i>boolean</i></p>
<dd> <code>True</code>: Make the cursor underlined. <code>False</code>: Make the cursor a box [default]; option <code>-uc</code>.</p>
<dt><code>pointerBlank:</code> <i>boolean</i></p>
<dd> <code>True</code>: blank the pointer when a key is pressed or after a set number of seconds of inactivity. <code>False</code>: the pointer is always visible [default].</p>
<dt><code>pointerColor:</code> <i>colour</i></p>
<dd> Mouse pointer foreground colour.</p>
<dt><code>pointerColor2:</code> <i>colour</i></p>
<dd> Mouse pointer background colour.</p>
<dt><code>pointerBlankDelay:</code> <i>number</i></p>
<dd> Specifies number of seconds before blanking the pointer [default 2]. Use a large number (e.g. <tt>987654321</tt>) to effectively disable the timeout.</p>
<dt><code>backspacekey:</code> <i>string</i></p>
<dd> The string to send when the backspace key is pressed. If set to <font SIZE="-1"><code>DEC</code></font> or unset it will send <code>Delete</code> (code 127) or, with control, <code>Backspace</code> (code 8) &#8211; which can be reversed with the appropriate <font SIZE="-1">DEC</font> private mode escape sequence.</p>
<dt><code>deletekey:</code> <i>string</i></p>
<dd> The string to send when the delete key (not the keypad delete key) is pressed. If unset it will send the sequence traditionally associated with the <code>Execute</code> key.</p>
<dt><code>cutchars:</code> <i>string</i></p>
<dd> The characters used as delimiters for double-click word selection (whitespace delimiting is added automatically if resource is given). </p>
<p> When the perl selection extension is in use (the default if compiled in, see the urxvt-ml<i><a href="/docs/linux/man/3-perl/">perl</a></i>(3) manpage), a suitable regex using these characters will be created (if the resource exists, otherwise, no regex will be created). In this mode, characters outside <font SIZE="-1">ISO-8859-1</font> can be used. </p>
<p> When the selection extension is not used, only <font SIZE="-1">ISO-8859-1</font> characters can be used. If not specified, the built-in default is used: </p>
<p> <font SIZE="-1"><code>BACKSLASH</code></font><code> `&quot;&#8217;&amp;()*,;&lt;=&gt;?@[]^{|}</code></p>
<dt><code>preeditType:</code> <i>style</i></p>
<dd> <code>OverTheSpot</code>, <code>OffTheSpot</code>, <code>Root</code>; option <code>-pt</code>.</p>
<dt><code>inputMethod:</code> <i>name</i></p>
<dd> <i>name</i> of inputMethod to use; option <code>-im</code>.</p>
<dt><code>imLocale:</code> <i>name</i></p>
<dd> The locale to use for opening the <font SIZE="-1">IM.</font> You can use an <tt>&quot;LC_CTYPE&quot;</tt> of e.g. <tt>&quot;de_DE.UTF-8&quot;</tt> for normal text processing but <tt>&quot;ja_JP.EUC-JP&quot;</tt> for the input extension to be able to input japanese characters while staying in another locale; option <code>-imlocale</code>.</p>
<dt><code>imFont:</code> <i>fontset</i></p>
<dd> Specify the font-set used for <font SIZE="-1">XIM</font> styles <tt>&quot;OverTheSpot&quot;</tt> or <tt>&quot;OffTheSpot&quot;</tt>. It must be a standard X font set (<font SIZE="-1">XLFD</font> patterns separated by commas), i.e. it&#8217;s not in the same format as the other font lists used in urxvt-ml. The default will be set-up to chose *any* suitable found found, preferably one or two pixels differing in size to the base font. option <code>-imfont</code>.</p>
<dt><code>tripleclickwords:</code> <i>boolean</i></p>
<dd> Change the meaning of triple-click selection with the left mouse button. Instead of selecting a full line it will extend the selection to the end of the logical line only; option <code>-tcw</code>.</p>
<dt><code>insecure:</code> <i>boolean</i></p>
<dd> Enables &#8220;insecure&#8221; mode. Rxvt-unicode offers some escape sequences that echo arbitrary strings like the icon name or the locale. This could be abused if somebody gets 8-bit-clean access to your display, whether through a mail client displaying mail bodies unfiltered or through <i><a href="/docs/linux/man/1-write/">write</a></i>(1) or any other means. Therefore, these sequences are disabled by default. (Note that many other terminals, including xterm, have these sequences enabled by default, which doesn&#8217;t make it safer, though). </p>
<p> You can enable them by setting this boolean resource or specifying <code>-insecure</code> as an option. At the moment, this enables display-answer, locale, findfont, icon label and window title requests.</p>
<dt><code>modifier:</code> <i>modifier</i></p>
<dd> Set the key to be interpreted as the Meta key to: <code>alt</code>, <code>meta</code>, <code>hyper</code>, <code>super</code>, <code>mod1</code>, <code>mod2</code>, <code>mod3</code>, <code>mod4</code>, <code>mod5</code>; option <code>-mod</code>.</p>
<dt><code>answerbackString:</code> <i>string</i></p>
<dd> Specify the reply rxvt-unicode sends to the shell when an <font SIZE="-1">ENQ </font>(control-E) character is passed through. It may contain escape values as described in the entry on <code>keysym</code> following.</p>
<dt><code>secondaryScreen:</code> <i>boolean</i></p>
<dd> Turn on/off secondary screen (default enabled).</p>
<dt><code>secondaryScroll:</code> <i>boolean</i></p>
<dd> Turn on/off secondary screen scroll (default enabled). If this option is enabled, scrolls on the secondary screen will change the scrollback buffer and, when secondaryScreen is off, switching to/from the secondary screen will instead scroll the screen up.</p>
<dt><code>hold</code>: <i>boolean</i></p>
<dd> Turn on/off hold window after exit support. If enabled, urxvt-ml will not immediately destroy its window when the program executed within it exits. Instead, it will wait till it is being killed or closed by the user.</p>
<dt><code>chdir</code>: <i>path</i></p>
<dd> Sets the working directory for the shell (or the command specified via <code>-e</code>). The <i>path</i> must be an absolute path and it must exist for urxvt-ml to start. If it isn&#8217;t specified then the current working directory will be used; option <code>-cd</code>.</p>
<dt><code>keysym.</code><i>sym</i>: <i>action</i></p>
<dd> Compile <i>frills</i>: Associate <i>action</i> with keysym <i>sym</i>. The intervening resource name <code>keysym.</code> cannot be omitted. </p>
<p> Using this resource, you can map key combinations such as <tt>&quot;Ctrl-Shift-BackSpace&quot;</tt> to various actions, such as outputting a different string than would normally result from that combination, making the terminal scroll up or down the way you want it, or any other thing an extension might provide. </p>
<p> The key combination that triggers the action, <i>sym</i>, has the following format: </p>
<pre>
   (modifiers-)key
</pre>
<p> Where <i>modifiers</i> can be any combination of <code>ISOLevel3</code>, <code>AppKeypad</code>, <code>Control</code>, <code>NumLock</code>, <code>Shift</code>, <code>Meta</code>, <code>Lock</code>, <code>Mod1</code>, <code>Mod2</code>, <code>Mod3</code>, <code>Mod4</code>, <code>Mod5</code>, and the abbreviated <code>I</code>, <code>K</code>, <code>C</code>, <code>N</code>, <code>S</code>, <code>M</code>, <code>A</code>, <code>L</code>, <code>1</code>, <code>2</code>, <code>3</code>, <code>4</code>, <code>5</code>. </p>
<p> The <code>NumLock</code>, <code>Meta</code> and <code>ISOLevel3</code> modifiers are usually aliased to whatever modifier the NumLock key, Meta/Alt keys or <font SIZE="-1">ISO</font> Level3 Shift/AltGr keys are being mapped. <code>AppKeypad</code> is a synthetic modifier mapped to the current application keymap mode state. </p>
<p> Due the the large number of modifier combinations, a key mapping will match if <i>at least</i> the specified identifiers are being set, and no other key mappings with those and more bits are being defined. That means that defining a mapping for <tt>&quot;a&quot;</tt> will automatically provide definitions for <tt>&quot;Meta-a&quot;</tt>, <tt>&quot;Shift-a&quot;</tt> and so on, unless some of those are defined mappings themselves. See the <tt>&quot;builtin:&quot;</tt> action, below, for a way to work around this when this is a problem. </p>
<p> The spelling of <i>key</i> depends on your implementation of X. An easy way to find a key name is to use the <code><a href="/docs/linux/man/1-xev/">xev</a></code>(1) command. You can find a list by looking for the <tt>&quot;XK_&quot;</tt> macros in the <code>X11/keysymdef.h</code> include file (omit the <tt>&quot;XK_&quot;</tt> prefix). Alternatively you can specify <i>key</i> by its hex keysym value (<code>0x0000 &#8211; 0xFFFF</code>). </p>
<p> As with any resource value, the <i>action</i> string may contain backslash escape sequences (<tt>&quot;
&quot;</tt>: newline, <tt>&quot;\&quot;</tt>: backslash, <tt>&quot;
