---

title: "urxvt256c-ml(1)"
name: "urxvt256c-ml"
section: "1"
letter: "u"
url: "/docs/linux/man/1-urxvt256c-ml/"
description: "rxvt-unicode (ouR XVT, unicode) – (a VT102 emulator for the X window system)"
---

<p> <code>urxvt256c-ml</code> [options] [-e command [ args ]]  </p>
<p> <code>rxvt-unicode</code>, version <code>9.21</code>, is a colour vt102 terminal emulator intended as an <i><a href="/docs/linux/man/1-xterm/">xterm</a></i>(1) replacement for users who do not require features such as Tektronix 4014 emulation and toolkit-style configurability. As a result, <code>rxvt-unicode</code> uses much less swap space --- a significant advantage on a machine serving many X sessions. </p>
<p> This document is also available on the World-Wide-Web at &lt;<a rel="nofollow" href="http://pod.tst.eu/http://cvs.schmorp.de/rxvt-unicode/doc/rxvt.1.pod">http://pod.tst.eu/http://cvs.schmorp.de/rxvt-unicode/doc/rxvt.1.pod</a>&gt;.  </p>
<h2>FREQUENTLY ASKED QUESTIONS</h2>
<p> See <a href="/docs/linux/man/7-urxvt256c-ml/">urxvt256c-ml</a>(7) (try <code>&quot;man 7 urxvt256c-ml&quot;</code>) for a list of frequently asked questions and answer to them and some common problems. That document is also accessible on the World-Wide-Web at &lt;<a rel="nofollow" href="http://pod.tst.eu/http://cvs.schmorp.de/rxvt-unicode/doc/rxvt.7.pod">http://pod.tst.eu/http://cvs.schmorp.de/rxvt-unicode/doc/rxvt.7.pod</a>&gt;.  </p>
<h2>RXVT-UNICODE VS. RXVT</h2>
<p> Unlike the original rxvt, <code>rxvt-unicode</code> stores all text in Unicode internally. That means it can store and display most scripts in the world. Being a terminal emulator, however, some things are very difficult, especially cursive scripts such as arabic, vertically written scripts like mongolian or scripts requiring extremely complex combining rules, like tibetan or devanagari. Don&#8217;t expect pretty output when using these scripts. Most other scripts, latin, cyrillic, kanji, thai etc. should work fine, though. A somewhat difficult case are right-to-left scripts, such as hebrew: <code>rxvt-unicode</code> adopts the view that bidirectional algorithms belong in the application, not the terminal emulator (too many things --- such as cursor-movement while editing --- break otherwise), but that might change. </p>
<p> If you are looking for a terminal that supports more exotic scripts, let me recommend <code>&quot;mlterm&quot;</code>, which is a very user friendly, lean and clean terminal emulator. In fact, the reason rxvt-unicode was born was solely because the author couldn&#8217;t get <code>&quot;mlterm&quot;</code> to use one font for latin1 and another for japanese. </p>
<p> Therefore another design rationale was the use of multiple fonts to display characters: The idea of a single unicode font which many other programs force onto its users never made sense to me: You should be able to choose any font for any script freely. </p>
<p> Apart from that, rxvt-unicode is also much better internationalised than its predecessor, supports things such as <font SIZE="-1">XFT</font> and <font SIZE="-1">ISO 14755</font> that are handy in i18n-environments, is faster, and has a lot bugs less than the original rxvt. This all in addition to dozens of other small improvements. </p>
<p> It is still faithfully following the original rxvt idea of being lean and nice on resources: for example, you can still configure rxvt-unicode without most of its features to get a lean binary. It also comes with a client/daemon pair that lets you open any number of terminal windows from within a single process, which makes startup time very fast and drastically reduces memory usage. See <a href="/docs/linux/man/1-urxvt256c-mld/">urxvt256c-mld</a>(1) (daemon) and <a href="/docs/linux/man/1-urxvt256c-mlc/">urxvt256c-mlc</a>(1) (client). </p>
<p> It also makes technical information about escape sequences (which have been extended) more accessible: see <a href="/docs/linux/man/7-urxvt256c-ml/">urxvt256c-ml</a>(7) for technical reference documentation (escape sequences etc.).  </p>
<h2>OPTIONS</h2>
<p> The <code>urxvt256c-ml</code> options (mostly a subset of <i>xterm</i>&#8216;s) are listed below. In keeping with the smaller-is-better philosophy, options may be eliminated or default values chosen at compile-time, so options and defaults listed may not accurately reflect the version installed on your system. `urxvt256c-ml -h&#8217; gives a list of major compile-time options on the <i>Options</i> line. Option descriptions may be prefixed with which compile option each is dependent upon. e.g. `Compile <i></i><font SIZE="-1"><i>XIM</i></font><i></i>:&#8216; requires <i></i><font SIZE="-1"><i>XIM</i></font><i></i> on the <i>Options</i> line. Note: `urxvt256c-ml -help&#8217; gives a list of all command-line options compiled into your version. </p>
<p> Note that <code>urxvt256c-ml</code> permits the resource name to be used as a long-option (--/++ option) so the potential command-line options are far greater than those listed. For example: `urxvt256c-ml --loginShell --color1 Orange&#8217;. </p>
<p> The following options are available: </p>
<dl>
<dt><code>-help</code>, <code>--help</code></dt>
<dd> <p> Print out a message describing available options. </p>
 </dd>
<dt><code>-display</code><i>displayname</i></dt>
<dd> <p> Attempt to open a window on the named X display (the older form <code>-d</code> is still respected. but deprecated). In the absence of this option, the display specified by the <font SIZE="-1"><code>DISPLAY</code></font> environment variable is used. </p>
 </dd>
<dt><code>-depth</code><i>bitdepth</i></dt>
<dd> <p> Compile <i>frills</i>: Attempt to find a visual with the given bit depth; resource <code>depth</code>. </p>
<p> [Please note that many X servers (and libXft) are buggy with respect to <code>&quot;-depth 32&quot;</code> and/or alpha channels, and will cause all sorts of graphical corruption. This is harmless, but we can&#8217;t do anything about this, so watch out] </p>
 </dd>
<dt><code>-visual</code><i>visualID</i></dt>
<dd> <p> Compile <i>frills</i>: Use the given visual (see e.g. <code>&quot;xdpyinfo&quot;</code> for possible visual ids) instead of the default, and also allocate a private colormap. All visual types except for DirectColor are supported. </p>
 </dd>
<dt><code>-geometry</code><i>geom</i></dt>
<dd> <p> Window geometry (<code>-g</code> still respected); resource <code>geometry</code>. </p>
 </dd>
<dt><code>-rv</code>|<code>+rv</code></dt>
<dd> <p> Turn on/off simulated reverse video; resource <code>reverseVideo</code>. </p>
 </dd>
<dt><code>-j</code>|<code>+j</code></dt>
<dd> <p> Turn on/off jump scrolling (allow multiple lines per refresh); resource <code>jumpScroll</code>. </p>
 </dd>
<dt><code>-ss</code>|<code>+ss</code></dt>
<dd> <p> Turn on/off skip scrolling (allow multiple screens per refresh); resource <code>skipScroll</code>. </p>
 </dd>
<dt><code>-fade</code><i>number</i></dt>
<dd> <p> Fade the text by the given percentage when focus is lost. Small values fade a little only, 100 completely replaces all colours by the fade colour; resource <code>fading</code>. </p>
 </dd>
<dt><code>-fadecolor</code><i>colour</i></dt>
<dd> <p> Fade to this colour when fading is used (see <code>-fade</code>). The default colour is opaque black. resource <code>fadeColor</code>. </p>
 </dd>
<dt><code>-icon</code><i>file</i></dt>
<dd> <p> Compile <i>pixbuf</i>: Use the specified image as application icon. This is used by many window managers, taskbars and pagers to represent the application window; resource <i>iconFile</i>. </p>
 </dd>
<dt><code>-bg</code><i>colour</i></dt>
<dd> <p> Window background colour; resource <code>background</code>. </p>
 </dd>
<dt><code>-fg</code><i>colour</i></dt>
<dd> <p> Window foreground colour; resource <code>foreground</code>. </p>
 </dd>
<dt><code>-cr</code><i>colour</i></dt>
<dd> <p> The cursor colour; resource <code>cursorColor</code>. </p>
 </dd>
<dt><code>-pr</code><i>colour</i></dt>
<dd> <p> The mouse pointer foreground colour; resource <code>pointerColor</code>. </p>
 </dd>
<dt><code>-pr2</code><i>colour</i></dt>
<dd> <p> The mouse pointer background colour; resource <code>pointerColor2</code>. </p>
 </dd>
<dt><code>-bd</code><i>colour</i></dt>
<dd> <p> The colour of the border around the text area and between the scrollbar and the text; resource <code>borderColor</code>. </p>
 </dd>
<dt><code>-fn</code><i>fontlist</i></dt>
<dd> <p> Select the fonts to be used. This is a comma separated list of font names that are checked in order when trying to find glyphs for characters. The first font defines the cell size for characters; other fonts might be smaller, but not (in general) larger. A (hopefully) reasonable default font list is always appended to it. See resource <code>font</code> for more details. </p>
<p> In short, to specify an X11 core font, just specify its name or prefix it with <code>&quot;x:&quot;</code>. To specify an XFT-font, you need to prefix it with <code>&quot;xft:&quot;</code>, e.g.: </p>
<pre><code>   urxvt256c-ml -fn &quot;xft:Bitstream Vera Sans Mono:pixelsize=15&quot;
   urxvt256c-ml -fn &quot;9x15bold,xft:Bitstream Vera Sans Mono&quot;
</code></pre>
<p> See also the question ``How does rxvt-unicode choose fonts?&#8216;&#8216; in the <font SIZE="-1">FAQ</font> section of <a href="/docs/linux/man/7-urxvt256c-ml/">urxvt256c-ml</a>(7). </p>
 </dd>
<dt><code>-fb</code><i>fontlist</i></dt>
<dd> <p> Compile <i>font-styles</i>: The bold font list to use when <code>bold</code> characters are to be printed. See resource <code>boldFont</code> for details. </p>
 </dd>
<dt><code>-fi</code><i>fontlist</i></dt>
<dd> <p> Compile <i>font-styles</i>: The italic font list to use when <i>italic</i> characters are to be printed. See resource <code>italicFont</code> for details. </p>
 </dd>
<dt><code>-fbi</code><i>fontlist</i></dt>
<dd> <p> Compile <i>font-styles</i>: The bold italic font list to use when bold italic characters are to be printed. See resource <code>boldItalicFont</code> for details. </p>
 </dd>
<dt><code>-is</code>|<code>+is</code></dt>
<dd> <p> Compile <i>font-styles</i>: Bold/Blink font styles imply high intensity foreground/background (default). See resource <code>intensityStyles</code> for details. </p>
 </dd>
<dt><code>-name</code><i>name</i></dt>
<dd> <p> Specify the application name under which resources are to be obtained, rather than the default executable file name. Name should not contain `.&#8216; or `*&#8216; characters. Also sets the icon and title name. </p>
 </dd>
<dt><code>-ls</code>|<code>+ls</code></dt>
<dd> <p> Start as a login-shell/sub-shell; resource <code>loginShell</code>. </p>
 </dd>
<dt><code>-mc</code><i>milliseconds</i></dt>
<dd> <p> Specify the maximum time between multi-click selections. </p>
 </dd>
<dt><code>-ut</code>|<code>+ut</code></dt>
<dd> <p> Compile <i>utmp</i>: Inhibit/enable writing a utmp entry; resource <code>utmpInhibit</code>. </p>
 </dd>
<dt><code>-vb</code>|<code>+vb</code></dt>
<dd> <p> Turn on/off visual bell on receipt of a bell character; resource <code>visualBell</code>. </p>
 </dd>
<dt><code>-sb</code>|<code>+sb</code></dt>
<dd> <p> Turn on/off scrollbar; resource <code>scrollBar</code>. </p>
 </dd>
<dt><code>-sr</code>|<code>+sr</code></dt>
<dd> <p> Put scrollbar on right/left; resource <code>scrollBar_right</code>. </p>
 </dd>
<dt><code>-st</code>|<code>+st</code></dt>
<dd> <p> Display rxvt (non XTerm/NeXT) scrollbar without/with a trough; resource <code>scrollBar_floating</code>. </p>
 </dd>
<dt><code>-si</code>|<code>+si</code></dt>
<dd> <p> Turn on/off scroll-to-bottom on <font SIZE="-1">TTY</font> output inhibit; resource <code>scrollTtyOutput</code> has opposite effect. </p>
 </dd>
<dt><code>-sk</code>|<code>+sk</code></dt>
<dd> <p> Turn on/off scroll-to-bottom on keypress; resource <code>scrollTtyKeypress</code>. </p>
 </dd>
<dt><code>-sw</code>|<code>+sw</code></dt>
<dd> <p> Turn on/off scrolling with the scrollback buffer as new lines appear. This only takes effect if <code>-si</code> is also given; resource <code>scrollWithBuffer</code>. </p>
 </dd>
<dt><code>-ptab</code>|<code>+ptab</code></dt>
<dd> <p> If enabled (default), ``Horizontal Tab&#8217;&#8216; characters are being stored as actual wide characters in the screen buffer, which makes it possible to select and paste them. Since a horizontal tab is a cursor movement and not an actual glyph, this can sometimes be visually annoying as the cursor on a tab character is displayed as a wide cursor; resource <code>pastableTabs</code>. </p>
 </dd>
<dt><code>-bc</code>|<code>+bc</code></dt>
<dd> <p> Blink the cursor; resource <code>cursorBlink</code>. </p>
 </dd>
<dt><code>-uc</code>|<code>+uc</code></dt>
<dd> <p> Make the cursor underlined; resource <code>cursorUnderline</code>. </p>
 </dd>
<dt><code>-iconic</code></dt>
<dd> <p> Start iconified, if the window manager supports that option. Alternative form is <code>-ic</code>. </p>
 </dd>
<dt><code>-sl</code><i>number</i></dt>
<dd> <p> Save <i>number</i> lines in the scrollback buffer. See resource entry for limits; resource <code>saveLines</code>. </p>
 </dd>
<dt><code>-b</code><i>number</i></dt>
<dd> <p> Compile <i>frills</i>: Internal border of <i>number</i> pixels. See resource entry for limits; resource <code>internalBorder</code>. </p>
 </dd>
<dt><code>-w</code><i>number</i></dt>
<dd> <p> Compile <i>frills</i>: External border of <i>number</i> pixels. Also, <code>-bw</code> and <code>-borderwidth</code>. See resource entry for limits; resource <code>externalBorder</code>. </p>
 </dd>
<dt><code>-bl</code></dt>
<dd> <p> Compile <i>frills</i>: Set <font SIZE="-1">MWM</font> hints to request a borderless window, i.e. if honoured by the <font SIZE="-1">WM,</font> the rxvt-unicode window will not have window decorations; resource <code>borderLess</code>. If the window manager does not support <font SIZE="-1">MWM</font> hints (e.g. kwin), enables override-redirect mode. </p>
 </dd>
<dt><code>-override-redirect</code></dt>
<dd> <p> Compile <i>frills</i>: Sets override-redirect on the window; resource <code>override-redirect</code>. </p>
 </dd>
<dt><code>-dockapp</code></dt>
<dd> <p> Sets the initial state of the window to WithdrawnState, which makes window managers that support this extension treat it as a dockapp. </p>
 </dd>
<dt><code>-sbg</code></dt>
<dd> <p> Compile <i>frills</i>: Disable the usage of the built-in block graphics/line drawing characters and just rely on what the specified fonts provide. Use this if you have a good font and want to use its block graphic glyphs; resource <code>skipBuiltinGlyphs</code>. </p>
 </dd>
<dt><code>-lsp</code><i>number</i></dt>
<dd> <p> Compile <i>frills</i>: Lines (pixel height) to insert between each row of the display. Useful to work around font rendering problems; resource <code>lineSpace</code>. </p>
 </dd>
<dt><code>-letsp</code><i>number</i></dt>
<dd> <p> Compile <i>frills</i>: Amount to adjust the computed character width by to control overall letter spacing. Negative values will tighten up the letter spacing, positive values will space letters out more. Useful to work around odd font metrics; resource <code>letterSpace</code>. </p>
 </dd>
<dt><code>-tn</code><i>termname</i></dt>
<dd> <p> This option specifies the name of the terminal type to be set in the <font SIZE="-1"><code>TERM</code></font> environment variable. This terminal type must exist in the <i><a href="/docs/linux/man/5-termcap/">termcap</a>(5)</i> database and should have <i>li#</i> and <i>co#</i> entries; resource <code>termName</code>. </p>
 </dd>
<dt><code>-e</code><i>command [arguments]</i></dt>
<dd> <p> Run the command with its command-line arguments in the <code>urxvt256c-ml</code> window; also sets the window title and icon name to be the basename of the program being executed if neither <i>-title</i> (<i>-T</i>) nor <i>-n</i> are given on the command line. If this option is used, it must be the last on the command-line. If there is no <code>-e</code> option then the default is to run the program specified by the <font SIZE="-1"><code>SHELL</code></font> environment variable or, failing that, <i><a href="/docs/linux/man/1-sh/">sh</a>(1)</i>. </p>
<p> Please note that you must specify a program with arguments. If you want to run shell commands, you have to specify the shell, like this: </p>
<pre><code>  urxvt256c-ml -e sh -c &quot;shell commands&quot;
</code></pre>
 </dd>
<dt><code>-title</code><i>text</i></dt>
<dd> <p> Window title (<code>-T</code> still respected); the default title is the basename of the program specified after the <code>-e</code> option, if any, otherwise the application name; resource <code>title</code>. </p>
 </dd>
<dt><code>-n</code><i>text</i></dt>
<dd> <p> Icon name; the default name is the basename of the program specified after the <code>-e</code> option, if any, otherwise the application name; resource <code>iconName</code>. </p>
 </dd>
<dt><code>-C</code></dt>
<dd> <p> Capture system console messages. </p>
 </dd>
<dt><code>-pt</code><i>style</i></dt>
<dd> <p> Compile <i></i><font SIZE="-1"><i>XIM</i></font><i></i>: input style for input method; <code>OverTheSpot</code>, <code>OffTheSpot</code>, <code>Root</code>; resource <code>preeditType</code>. </p>
 </dd>
<dt><code>-im</code><i>text</i></dt>
<dd> <p> Compile <i></i><font SIZE="-1"><i>XIM</i></font><i></i>: input method name. resource <code>inputMethod</code>. </p>
 </dd>
<dt><code>-imlocale</code><i>string</i></dt>
<dd> <p> The locale to use for opening the <font SIZE="-1">IM.</font> You can use an <code>&quot;LC_CTYPE&quot;</code> of e.g. <code>&quot;de_DE.UTF-8&quot;</code> for normal text processing but <code>&quot;ja_JP.EUC-JP&quot;</code> for the input extension to be able to input japanese characters while staying in another locale. resource <code>imLocale</code>. </p>
 </dd>
<dt><code>-imfont</code><i>fontset</i></dt>
<dd> <p> Set the font set to use for the X Input Method, see resource <code>imFont</code> for more info. </p>
 </dd>
<dt><code>-tcw</code></dt>
<dd> <p> Change the meaning of triple-click selection with the left mouse button. Only effective when the original (non-perl) selection code is in-use. Instead of selecting a full line it will extend the selection to the end of the logical line only. resource <code>tripleclickwords</code>. </p>
 </dd>
<dt><code>-insecure</code></dt>
<dd> <p> Enable ``insecure&#8217;&#8216; mode, which currently enables most of the escape sequences that echo strings. See the resource <code>insecure</code> for more info. </p>
 </dd>
<dt><code>-mod</code><i>modifier</i></dt>
<dd> <p> Override detection of Meta modifier with specified key: <code>alt</code>, <code>meta</code>, <code>hyper</code>, <code>super</code>, <code>mod1</code>, <code>mod2</code>, <code>mod3</code>, <code>mod4</code>, <code>mod5</code>; resource <i>modifier</i>. </p>
 </dd>
<dt><code>-ssc</code>|<code>+ssc</code></dt>
<dd> <p> Turn on/off secondary screen (default enabled); resource <code>secondaryScreen</code>. </p>
 </dd>
<dt><code>-ssr</code>|<code>+ssr</code></dt>
<dd> <p> Turn on/off secondary screen scroll (default enabled); resource <code>secondaryScroll</code>. </p>
 </dd>
<dt><code>-hold</code>|<code>+hold</code></dt>
<dd> <p> Turn on/off hold window after exit support. If enabled, urxvt256c-ml will not immediately destroy its window when the program executed within it exits. Instead, it will wait till it is being killed or closed by the user; resource <code>hold</code>. </p>
 </dd>
<dt><code>-cd</code><i>path</i></dt>
<dd> <p> Sets the working directory for the shell (or the command specified via <code>-e</code>). The <i>path</i> must be an absolute path and it must exist for urxvt256c-ml to start; resource <code>chdir</code>. </p>
 </dd>
<dt><code>-xrm</code><i>string</i></dt>
<dd> <p> Works like the X Toolkit option of the same name, by adding the <i>string</i> as if it were specified in a resource file. Resource values specified this way take precedence over all other resource specifications. </p>
<p> Note that you need to use the <i>same</i> syntax as in the .Xdefaults file, e.g. <code>&quot;*.background: black&quot;</code>. Also note that all urxvt256c-ml-specific options can be specified as long-options on the commandline, so use of <code>-xrm</code> is mostly limited to cases where you want to specify other resources (e.g. for input methods) or for compatibility with other programs. </p>
 </dd>
<dt><code>-keysym.</code><i>sym</i><i>string</i></dt>
<dd> <p> Remap a key symbol. See resource <code>keysym</code>. </p>
 </dd>
<dt><code>-embed</code><i>windowid</i></dt>
<dd> <p> Tells urxvt256c-ml to embed its windows into an already-existing window, which enables applications to easily embed a terminal. </p>
<p> Right now, urxvt256c-ml will first unmap/map the specified window, so it shouldn&#8217;t be a top-level window. urxvt256c-ml will also reconfigure it quite a bit, so don&#8217;t expect it to keep some specific state. It&#8217;s best to create an extra subwindow for urxvt256c-ml and leave it alone. </p>
<p> The window will not be destroyed when urxvt256c-ml exits. </p>
<p> It might be useful to know that urxvt256c-ml will not close file descriptors passed to it (except for stdin/out/err, of course), so you can use file descriptors to communicate with the programs within the terminal. This works regardless of whether the <code>&quot;-embed&quot;</code> option was used or not. </p>
<p> Here is a short Gtk2-perl snippet that illustrates how this option can be used (a longer example is in <i>doc/embed</i>): </p>
<pre><code>   my $rxvt = new Gtk2::Socket;
   $rxvt-&gt;signal_connect_after (realize =&gt; sub {
      my $xid = $_[0]-&gt;window-&gt;get_xid;
      system &quot;urxvt256c-ml -embed $xid &amp;&quot;;
   });
</code></pre>
 </dd>
<dt><code>-pty-fd</code><i>file descriptor</i></dt>
<dd> <p> Tells urxvt256c-ml <font SIZE="-1">NOT</font> to execute any commands or create a new pty/tty pair but instead use the given file descriptor as the tty master. This is useful if you want to drive urxvt256c-ml as a generic terminal emulator without having to run a program within it. </p>
<p> If this switch is given, urxvt256c-ml will not create any utmp/wtmp entries and will not tinker with pty/tty permissions - you have to do that yourself if you want that. </p>
<p> As an extremely special case, specifying <code>&quot;-1&quot;</code> will completely suppress pty/tty operations, which is probably only useful in conjunction with some perl extension that manages the terminal. </p>
<p> Here is a example in perl that illustrates how this option can be used (a longer example is in <i>doc/pty-fd</i>): </p>
<pre><code>   use IO::Pty;
   use Fcntl;
   my $pty = new IO::Pty;
   fcntl $pty, F_SETFD, 0; # clear close-on-exec
   system &quot;urxvt256c-ml -pty-fd &quot; . (fileno $pty) . &quot;&amp;&quot;;
   close $pty;
   # now communicate with rxvt
   my $slave = $pty-&gt;slave;
   while (&lt;$slave&gt;) { print $slave &quot;got &lt;$_&gt;\n&quot; }
</code></pre>
 </dd>
<dt><code>-pe</code><i>string</i></dt>
<dd> <p> Comma-separated list of perl extension scripts to use (or not to use) in this terminal instance. See resource <code>perl-ext</code> for details. </p>
 </dd></dl>
<h2>RESOURCES</h2>
<p> Note: `urxvt256c-ml --help&#8217; gives a list of all resources (long options) compiled into your version. All resources are also available as long-options. </p>
<p> You can set and change the resources using X11 tools like <code>xrdb</code>. Many distribution do also load settings from the <code>~/.Xresources</code> file when X starts. urxvt256c-ml will consult the following files/resources in order, with later settings overwriting earlier ones: </p>
<pre><code>  1. app-defaults file in $XAPPLRESDIR
  2. $HOME/.Xdefaults
  3. RESOURCE_MANAGER property on root-window of screen 0
  4. SCREEN_RESOURCES property on root-window of the current screen
  5. $XENVIRONMENT file OR $HOME/.Xdefaults-&lt;nodename&gt;
  6. resources specified via -xrm on the commandline
</code></pre>
<p> Note that when reading X resources, <code>urxvt256c-ml</code> recognizes two class names: <code>Rxvt</code> and <code>URxvt</code>. The class name <code>Rxvt</code> allows resources common to both <code>urxvt256c-ml</code> and the original <i>rxvt</i> to be easily configured, while the class name <code>URxvt</code> allows resources unique to <code>urxvt256c-ml</code>, to be shared between different <code>urxvt256c-ml</code> configurations. If no resources are specified, suitable defaults will be used. Command-line arguments can be used to override resource settings. The following resources are supported (you might want to check the urxvt256c-ml <i>perl</i>(3) manpage for additional settings by perl extensions not documented here): </p>
<dl>
<dt><code>depth:</code><i>bitdepth</i></dt>
<dd> <p> Compile <i>xft</i>: Attempt to find a visual with the given bit depth; option <code>-depth</code>. </p>
 </dd>
<dt><code>buffered:</code><i>boolean</i></dt>
<dd> <p> Compile <i>xft</i>: Turn on/off double-buffering for xft (default enabled). On some card/driver combination enabling it slightly decreases performance, on most it greatly helps it. The slowdown is small, so it should normally be enabled. </p>
 </dd>
<dt><code>geometry:</code><i>geom</i></dt>
<dd> <p> Create the window with the specified X window geometry [default 80x24]; option <code>-geometry</code>. </p>
 </dd>
<dt><code>background:</code><i>colour</i></dt>
<dd> <p> Use the specified colour as the window&#8217;s background colour [default White]; option <code>-bg</code>. </p>
 </dd>
<dt><code>foreground:</code><i>colour</i></dt>
<dd> <p> Use the specified colour as the window&#8217;s foreground colour [default Black]; option <code>-fg</code>. </p>
 </dd>
<dt><code>color</code><i>n</i><code>:</code><i>colour</i></dt>
<dd> <p> Use the specified colour for the colour value <i>n</i>, where 0-7 corresponds to low-intensity (normal) colours and 8-15 corresponds to high-intensity (bold = bright foreground, blink = bright background) colours. The canonical names are as follows: 0=black, 1=red, 2=green, 3=yellow, 4=blue, 5=magenta, 6=cyan, 7=white, but the actual colour names used are listed in the <font SIZE="-1"><code>COLOURS AND GRAPHICS</code></font> section. </p>
<p> Colours higher than 15 cannot be set using resources (yet), but can be changed using an escape command (see <a href="/docs/linux/man/7-urxvt256c-ml/">urxvt256c-ml</a>(7)). </p>
<p> Colours 16-79 form a standard 4x4x4 colour cube (the same as xterm with 88 colour support). Colours 80-87 are evenly spaces grey steps. </p>
 </dd>
<dt><code>colorBD:</code><i>colour</i></dt>
<dd>  </dd>
<dt><code>colorIT:</code><i>colour</i></dt>
<dd> <p> Use the specified colour to display bold or italic characters when the foreground colour is the default. If font styles are not available (Compile <i>styles</i>) and this option is unset, reverse video is used instead. </p>
 </dd>
<dt><code>colorUL:</code><i>colour</i></dt>
<dd> <p> Use the specified colour to display underlined characters when the foreground colour is the default. </p>
 </dd>
<dt><code>underlineColor:</code><i>colour</i></dt>
<dd> <p> If set, use the specified colour as the colour for the underline itself. If unset, use the foreground colour. </p>
 </dd>
<dt><code>highlightColor:</code><i>colour</i></dt>
<dd> <p> If set, use the specified colour as the background for highlighted characters. If unset, use reverse video. </p>
 </dd>
<dt><code>highlightTextColor:</code><i>colour</i></dt>
<dd> <p> If set and highlightColor is set, use the specified colour as the foreground for highlighted characters. </p>
 </dd>
<dt><code>cursorColor:</code><i>colour</i></dt>
<dd> <p> Use the specified colour for the cursor. The default is to use the foreground colour; option <code>-cr</code>. </p>
 </dd>
<dt><code>cursorColor2:</code><i>colour</i></dt>
<dd> <p> Use the specified colour for the colour of the cursor text. For this to take effect, <code>cursorColor</code> must also be specified. The default is to use the background colour. </p>
 </dd>
<dt><code>reverseVideo:</code><i>boolean</i></dt>
<dd> <p> <code>True</code>: simulate reverse video by foreground and background colours; option <code>-rv</code>. <code>False</code>: regular screen colours [default]; option <code>+rv</code>. See note in <font SIZE="-1"><code>COLOURS AND GRAPHICS</code></font> section. </p>
 </dd>
<dt><code>jumpScroll:</code><i>boolean</i></dt>
<dd> <p> <code>True</code>: specify that jump scrolling should be used. When receiving lots of lines, urxvt256c-ml will only scroll once a whole screen height of lines has been read, resulting in fewer updates while still displaying every received line; option <code>-j</code>. </p>
<p> <code>False</code>: specify that smooth scrolling should be used. urxvt256c-ml will force a screen refresh on each new line it received; option <code>+j</code>. </p>
 </dd>
<dt><code>skipScroll:</code><i>boolean</i></dt>
<dd> <p> <code>True</code>: (the default) specify that skip scrolling should be used. When receiving lots of lines, urxvt256c-ml will only scroll once in a while (around 60 times per second), resulting in far fewer updates. This can result in urxvt256c-ml not ever displaying some of the lines it receives; option <code>-ss</code>. </p>
<p> <code>False</code>: specify that everything is to be displayed, even if the refresh is too fast for the human eye to read anything (or the monitor to display anything); option <code>+ss</code>. </p>
 </dd>
<dt><code>fading:</code><i>number</i></dt>
<dd> <p> Fade the text by the given percentage when focus is lost; option <code>-fade</code>. </p>
 </dd>
<dt><code>fadeColor:</code><i>colour</i></dt>
<dd> <p> Fade to this colour, when fading is used (see <code>fading:</code>). The default colour is black; option <code>-fadecolor</code>. </p>
 </dd>
<dt><code>iconFile:</code><i>file</i></dt>
<dd> <p> Set the application icon pixmap; option <code>-icon</code>. </p>
 </dd>
<dt><code>scrollColor:</code><i>colour</i></dt>
<dd> <p> Use the specified colour for the scrollbar [default #B2B2B2]. </p>
 </dd>
<dt><code>troughColor:</code><i>colour</i></dt>
<dd> <p> Use the specified colour for the scrollbar&#8217;s trough area [default #969696]. Only relevant for rxvt (non XTerm/NeXT) scrollbar. </p>
 </dd>
<dt><code>borderColor:</code><i>colour</i></dt>
<dd> <p> The colour of the border around the text area and between the scrollbar and the text. </p>
 </dd>
<dt><code>font:</code><i>fontlist</i></dt>
<dd> <p> Select the fonts to be used. This is a comma separated list of font names that are checked in order when trying to find glyphs for characters. The first font defines the cell size for characters; other fonts might be smaller, but not (in general) larger. A (hopefully) reasonable default font list is always appended to it; option <code>-fn</code>. </p>
<p> Each font can either be a standard X11 core font (<font SIZE="-1">XLFD</font>) name, with optional prefix <code>&quot;x:&quot;</code> or a Xft font (Compile <i>xft</i>), prefixed with <code>&quot;xft:&quot;</code>. </p>
<p> In addition, each font can be prefixed with additional hints and specifications enclosed in square brackets (<code>&quot;[]&quot;</code>). The only available hint currently is <code>&quot;codeset=codeset-name&quot;</code>, and this is only used for Xft fonts. </p>
<p> For example, this font resource </p>
<pre><code>   URxvt.font: 9x15bold,\
               -misc-fixed-bold-r-normal--15-140-75-75-c-90-iso10646-1,\
               -misc-fixed-medium-r-normal--15-140-75-75-c-90-iso10646-1, \
               [codeset=JISX0208]xft:Kochi Gothic:antialias=false, \
               xft:Code2000:antialias=false
</code></pre>
<p> specifies five fonts to be used. The first one is <code>&quot;9x15bold&quot;</code> (actually the iso8859-1 version of the second font), which is the base font (because it is named first) and thus defines the character cell grid to be 9 pixels wide and 15 pixels high. </p>
<p> The second font is just used to add additional unicode characters not in the base font, likewise the third, which is unfortunately non-bold, but the bold version of the font does contain fewer characters, so this is a useful supplement. </p>
<p> The third font is an Xft font with aliasing turned off, and the characters are limited to the <font SIZE="-1"><code>JIS 0208</code></font> codeset (i.e. japanese kanji). The font contains other characters, but we are not interested in them. </p>
<p> The last font is a useful catch-all font that supplies most of the remaining unicode characters. </p>
 </dd>
<dt><code>boldFont:</code><i>fontlist</i></dt>
<dd>  </dd>
<dt><code>italicFont:</code><i>fontlist</i></dt>
<dd>  </dd>
<dt><code>boldItalicFont:</code><i>fontlist</i></dt>
<dd> <p> The font list to use for displaying <code>bold</code>, <i>italic</i> or bold italic characters, respectively. </p>
<p> If specified and non-empty, then the syntax is the same as for the <code>font</code>-resource, and the given font list will be used as is, which makes it possible to substitute completely different font styles for bold and italic. </p>
<p> If unset (the default), a suitable font list will be synthesized by ``morphing&#8217;&#8216; the normal text font list into the desired shape. If that is not possible, replacement fonts of the desired shape will be tried. </p>
<p> If set, but empty, then this specific style is disabled and the normal text font will being used for the given style. </p>
 </dd>
<dt><code>intensityStyles:</code><i>boolean</i></dt>
<dd> <p> When font styles are not enabled, or this option is enabled (<code>True</code>, option <code>-is</code>, the default), bold/blink font styles imply high intensity foreground/background colours. Disabling this option (<code>False</code>, option <code>+is</code>) disables this behaviour, the high intensity colours are not reachable. </p>
 </dd>
<dt><code>title:</code><i>string</i></dt>
<dd> <p> Set window title string, the default title is the command-line specified after the <code>-e</code> option, if any, otherwise the application name; option <code>-title</code>. </p>
 </dd>
<dt><code>iconName:</code><i>string</i></dt>
<dd> <p> Set the name used to label the window&#8217;s icon or displayed in an icon manager window, it also sets the window&#8217;s title unless it is explicitly set; option <code>-n</code>. </p>
 </dd>
<dt><code>mapAlert:</code><i>boolean</i></dt>
<dd> <p> <code>True</code>: de-iconify (map) on receipt of a bell character. <code>False</code>: no de-iconify (map) on receipt of a bell character [default]. </p>
 </dd>
<dt><code>urgentOnBell:</code><i>boolean</i></dt>
<dd> <p> <code>True</code>: set the urgency hint for the wm on receipt of a bell character. <code>False</code>: do not set the urgency hint [default]. </p>
<p> urxvt256c-ml resets the urgency hint on every focus change. </p>
 </dd>
<dt><code>visualBell:</code><i>boolean</i></dt>
<dd> <p> <code>True</code>: use visual bell on receipt of a bell character; option <code>-vb</code>. <code>False</code>: no visual bell [default]; option <code>+vb</code>. </p>
 </dd>
<dt><code>loginShell:</code><i>boolean</i></dt>
<dd> <p> <code>True</code>: start as a login shell by prepending a `-&#8216; to <code>argv[0]</code> of the shell; option <code>-ls</code>. <code>False</code>: start as a normal sub-shell [default]; option <code>+ls</code>. </p>
 </dd>
<dt><code>multiClickTime:</code><i>number</i></dt>
<dd> <p> Specify the maximum time in milliseconds between multi-click select events. The default is 500 milliseconds; option <code>-mc</code>. </p>
 </dd>
<dt><code>utmpInhibit:</code><i>boolean</i></dt>
<dd> <p> <code>True</code>: inhibit writing record into the system log file <code>utmp</code>; option <code>-ut</code>. <code>False</code>: write record into the system log file <code>utmp</code> [default]; option <code>+ut</code>. </p>
 </dd>
<dt><code>print-pipe:</code><i>string</i></dt>
<dd> <p> Specify a command pipe for vt100 printer [default <i><a href="/docs/linux/man/1-lpr/">lpr</a>(1)</i>]. Use <code>Print</code> to initiate a screen dump to the printer and <code>Ctrl-Print</code> or <code>Shift-Print</code> to include the scrollback as well. </p>
<p> The string will be interpreted as if typed into the shell as-is. </p>
<p> Example: </p>
<pre><code>   URxvt.print-pipe: cat &gt; $(TMPDIR=$HOME mktemp urxvt.XXXXXX)
</code></pre>
<p> This creates a new file in your home directory with the screen contents every time you hit <code>&quot;Print&quot;</code>. </p>
 </dd>
<dt><code>scrollstyle:</code><i>mode</i></dt>
<dd> <p> Set scrollbar style to <code>rxvt</code>, <code>plain</code>, <code>next</code> or <code>xterm</code>. <code>plain</code> is the author&#8217;s favourite. </p>
 </dd>
<dt><code>thickness:</code><i>number</i></dt>
<dd> <p> Set the scrollbar width in pixels. </p>
 </dd>
<dt><code>scrollBar:</code><i>boolean</i></dt>
<dd> <p> <code>True</code>: enable the scrollbar [default]; option <code>-sb</code>. <code>False</code>: disable the scrollbar; option <code>+sb</code>. </p>
 </dd>
<dt><code>scrollBar_right:</code><i>boolean</i></dt>
<dd> <p> <code>True</code>: place the scrollbar on the right of the window; option <code>-sr</code>. <code>False</code>: place the scrollbar on the left of the window; option <code>+sr</code>. </p>
 </dd>
<dt><code>scrollBar_floating:</code><i>boolean</i></dt>
<dd> <p> <code>True</code>: display an rxvt scrollbar without a trough; option <code>-st</code>. <code>False</code>: display an rxvt scrollbar with a trough; option <code>+st</code>. </p>
 </dd>
<dt><code>scrollBar_align:</code><i>mode</i></dt>
<dd> <p> Align the <code>top</code>, <code>bottom</code> or <code>centre</code> [default] of the scrollbar thumb with the pointer on middle button press/drag. </p>
 </dd>
<dt><code>scrollTtyOutput:</code><i>boolean</i></dt>
<dd> <p> <code>True</code>: scroll to bottom when tty receives output; option <code>-si</code>. <code>False</code>: do not scroll to bottom when tty receives output; option <code>+si</code>. </p>
 </dd>
<dt><code>scrollWithBuffer:</code><i>boolean</i></dt>
<dd> <p> <code>True</code>: scroll with scrollback buffer when tty receives new lines (i.e. try to show the same lines) and <code>scrollTtyOutput</code> is False; option <code>-sw</code>. <code>False</code>: do not scroll with scrollback buffer when tty receives new lines; option <code>+sw</code>. </p>
 </dd>
<dt><code>scrollTtyKeypress:</code><i>boolean</i></dt>
<dd> <p> <code>True</code>: scroll to bottom when a non-special key is pressed. Special keys are those which are intercepted by rxvt-unicode for special handling and are not passed onto the shell; option <code>-sk</code>. <code>False</code>: do not scroll to bottom when a non-special key is pressed; option <code>+sk</code>. </p>
 </dd>
<dt><code>saveLines:</code><i>number</i></dt>
<dd> <p> Save <i>number</i> lines in the scrollback buffer [default 64]. This resource is limited on most machines to 65535; option <code>-sl</code>. </p>
 </dd>
<dt><code>internalBorder:</code><i>number</i></dt>
<dd> <p> Internal border of <i>number</i> pixels. This resource is limited to 100; option <code>-b</code>. </p>
 </dd>
<dt><code>externalBorder:</code><i>number</i></dt>
<dd> <p> External border of <i>number</i> pixels. This resource is limited to 100; option <code>-w</code>, <code>-bw</code>, <code>-borderwidth</code>. </p>
 </dd>
<dt><code>borderLess:</code><i>boolean</i></dt>
<dd> <p> Set <font SIZE="-1">MWM</font> hints to request a borderless window, i.e. if honoured by the <font SIZE="-1">WM,</font> the rxvt-unicode window will not have window decorations; option <code>-bl</code>. </p>
 </dd>
<dt><code>skipBuiltinGlyphs:</code><i>boolean</i></dt>
<dd> <p> Compile <i>frills</i>: Disable the usage of the built-in block graphics/line drawing characters and just rely on what the specified fonts provide. Use this if you have a good font and want to use its block graphic glyphs; option <code>-sbg</code>. </p>
 </dd>
<dt><code>termName:</code><i>termname</i></dt>
<dd> <p> Specifies the terminal type name to be set in the <font SIZE="-1"><code>TERM</code></font> environment variable; option <code>-tn</code>. </p>
 </dd>
<dt><code>lineSpace:</code><i>number</i></dt>
<dd> <p> Specifies number of lines (pixel height) to insert between each row of the display [default 0]; option <code>-lsp</code>. </p>
 </dd>
<dt><code>meta8:</code><i>boolean</i></dt>
<dd> <p> <code>True</code>: handle Meta (Alt) + keypress to set the 8th bit. <code>False</code>: handle Meta (Alt) + keypress as an escape prefix [default]. </p>
 </dd>
<dt><code>mouseWheelScrollPage:</code><i>boolean</i></dt>
<dd> <p> <code>True</code>: the mouse wheel scrolls a page full. <code>False</code>: the mouse wheel scrolls five lines [default]. </p>
 </dd>
<dt><code>pastableTabs:</code><i>boolean</i></dt>
<dd> <p> <code>True</code>: store tabs as wide characters. <code>False</code>: interpret tabs as cursor movement only; option <code>&quot;-ptab&quot;</code>. </p>
 </dd>
<dt><code>cursorBlink:</code><i>boolean</i></dt>
<dd> <p> <code>True</code>: blink the cursor. <code>False</code>: do not blink the cursor [default]; option <code>-bc</code>. </p>
 </dd>
<dt><code>cursorUnderline:</code><i>boolean</i></dt>
<dd> <p> <code>True</code>: Make the cursor underlined. <code>False</code>: Make the cursor a box [default]; option <code>-uc</code>. </p>
 </dd>
<dt><code>pointerBlank:</code><i>boolean</i></dt>
<dd> <p> <code>True</code>: blank the pointer when a key is pressed or after a set number of seconds of inactivity. <code>False</code>: the pointer is always visible [default]. </p>
 </dd>
<dt><code>pointerColor:</code><i>colour</i></dt>
<dd> <p> Mouse pointer foreground colour. </p>
 </dd>
<dt><code>pointerColor2:</code><i>colour</i></dt>
<dd> <p> Mouse pointer background colour. </p>
 </dd>
<dt><code>pointerBlankDelay:</code><i>number</i></dt>
<dd> <p> Specifies number of seconds before blanking the pointer [default 2]. Use a large number (e.g. <code>987654321</code>) to effectively disable the timeout. </p>
 </dd>
<dt><code>backspacekey:</code><i>string</i></dt>
<dd> <p> The string to send when the backspace key is pressed. If set to <font SIZE="-1"><code>DEC</code></font> or unset it will send <code>Delete</code> (code 127) or, with control, <code>Backspace</code> (code 8) - which can be reversed with the appropriate <font SIZE="-1">DEC</font> private mode escape sequence. </p>
 </dd>
<dt><code>deletekey:</code><i>string</i></dt>
<dd> <p> The string to send when the delete key (not the keypad delete key) is pressed. If unset it will send the sequence traditionally associated with the <code>Execute</code> key. </p>
 </dd>
<dt><code>cutchars:</code><i>string</i></dt>
<dd> <p> The characters used as delimiters for double-click word selection (whitespace delimiting is added automatically if resource is given). </p>
<p> When the perl selection extension is in use (the default if compiled in, see the urxvt256c-ml <i>perl</i>(3) manpage), a suitable regex using these characters will be created (if the resource exists, otherwise, no regex will be created). In this mode, characters outside <font SIZE="-1">ISO-8859-1</font> can be used. </p>
<p> When the selection extension is not used, only <font SIZE="-1">ISO-8859-1</font> characters can be used. If not specified, the built-in default is used: </p>
<p> <font SIZE="-1"><code>BACKSLASH</code></font><code> `&quot;&#8216;&amp;()*,;&lt;=&gt;?@[]^{|}</code> </p>
 </dd>
<dt><code>preeditType:</code><i>style</i></dt>
<dd> <p> <code>OverTheSpot</code>, <code>OffTheSpot</code>, <code>Root</code>; option <code>-pt</code>. </p>
 </dd>
<dt><code>inputMethod:</code><i>name</i></dt>
<dd> <p> <i>name</i> of inputMethod to use; option <code>-im</code>. </p>
 </dd>
<dt><code>imLocale:</code><i>name</i></dt>
<dd> <p> The locale to use for opening the <font SIZE="-1">IM.</font> You can use an <code>&quot;LC_CTYPE&quot;</code> of e.g. <code>&quot;de_DE.UTF-8&quot;</code> for normal text processing but <code>&quot;ja_JP.EUC-JP&quot;</code> for the input extension to be able to input japanese characters while staying in another locale; option <code>-imlocale</code>. </p>
 </dd>
<dt><code>imFont:</code><i>fontset</i></dt>
<dd> <p> Specify the font-set used for <font SIZE="-1">XIM</font> styles <code>&quot;OverTheSpot&quot;</code> or <code>&quot;OffTheSpot&quot;</code>. It must be a standard X font set (<font SIZE="-1">XLFD</font> patterns separated by commas), i.e. it&#8217;s not in the same format as the other font lists used in urxvt256c-ml. The default will be set-up to chose *any* suitable found found, preferably one or two pixels differing in size to the base font. option <code>-imfont</code>. </p>
 </dd>
<dt><code>tripleclickwords:</code><i>boolean</i></dt>
<dd> <p> Change the meaning of triple-click selection with the left mouse button. Instead of selecting a full line it will extend the selection to the end of the logical line only; option <code>-tcw</code>. </p>
 </dd>
<dt><code>insecure:</code><i>boolean</i></dt>
<dd> <p> Enables ``insecure&#8217;&#8216; mode. Rxvt-unicode offers some escape sequences that echo arbitrary strings like the icon name or the locale. This could be abused if somebody gets 8-bit-clean access to your display, whether through a mail client displaying mail bodies unfiltered or through <i><a href="/docs/linux/man/1-write/">write</a></i>(1) or any other means. Therefore, these sequences are disabled by default. (Note that many other terminals, including xterm, have these sequences enabled by default, which doesn&#8217;t make it safer, though). </p>
<p> You can enable them by setting this boolean resource or specifying <code>-insecure</code> as an option. At the moment, this enables display-answer, locale, findfont, icon label and window title requests. </p>
 </dd>
<dt><code>modifier:</code><i>modifier</i></dt>
<dd> <p> Set the key to be interpreted as the Meta key to: <code>alt</code>, <code>meta</code>, <code>hyper</code>, <code>super</code>, <code>mod1</code>, <code>mod2</code>, <code>mod3</code>, <code>mod4</code>, <code>mod5</code>; option <code>-mod</code>. </p>
 </dd>
<dt><code>answerbackString:</code><i>string</i></dt>
<dd> <p> Specify the reply rxvt-unicode sends to the shell when an <font SIZE="-1">ENQ </font>(control-E) character is passed through. It may contain escape values as described in the entry on <code>keysym</code> following. </p>
 </dd>
<dt><code>secondaryScreen:</code><i>boolean</i></dt>
<dd> <p> Turn on/off secondary screen (default enabled). </p>
 </dd>
<dt><code>secondaryScroll:</code><i>boolean</i></dt>
<dd> <p> Turn on/off secondary screen scroll (default enabled). If this option is enabled, scrolls on the secondary screen will change the scrollback buffer and, when secondaryScreen is off, switching to/from the secondary screen will instead scroll the screen up. </p>
 </dd>
<dt><code>hold</code>: <i>boolean</i></dt>
<dd> <p> Turn on/off hold window after exit support. If enabled, urxvt256c-ml will not immediately destroy its window when the program executed within it exits. Instead, it will wait till it is being killed or closed by the user. </p>
 </dd>
<dt><code>chdir</code>: <i>path</i></dt>
<dd> <p> Sets the working directory for the shell (or the command specified via <code>-e</code>). The <i>path</i> must be an absolute path and it must exist for urxvt256c-ml to start. If it isn&#8217;t specified then the current working directory will be used; option <code>-cd</code>. </p>
 </dd>
<dt><code>keysym.</code><i>sym</i>: <i>action</i></dt>
<dd> <p> Compile <i>frills</i>: Associate <i>action</i> with keysym <i>sym</i>. The intervening resource name <code>keysym.</code> cannot be omitted. </p>
<p> Using this resource, you can map key combinations such as <code>&quot;Ctrl-Shift-BackSpace&quot;</code> to various actions, such as outputting a different string than would normally result from that combination, making the terminal scroll up or down the way you want it, or any other thing an extension might provide. </p>
<p> The key combination that triggers the action, <i>sym</i>, has the following format: </p>
<pre><code>   (modifiers-)key
</code></pre>
<p> Where <i>modifiers</i> can be any combination of <code>ISOLevel3</code>, <code>AppKeypad</code>, <code>Control</code>, <code>NumLock</code>, <code>Shift</code>, <code>Meta</code>, <code>Lock</code>, <code>Mod1</code>, <code>Mod2</code>, <code>Mod3</code>, <code>Mod4</code>, <code>Mod5</code>, and the abbreviated <code>I</code>, <code>K</code>, <code>C</code>, <code>N</code>, <code>S</code>, <code>M</code>, <code>A</code>, <code>L</code>, <code>1</code>, <code>2</code>, <code>3</code>, <code>4</code>, <code>5</code>. </p>
<p> The <code>NumLock</code>, <code>Meta</code> and <code>ISOLevel3</code> modifiers are usually aliased to whatever modifier the NumLock key, Meta/Alt keys or <font SIZE="-1">ISO</font> Level3 Shift/AltGr keys are being mapped. <code>AppKeypad</code> is a synthetic modifier mapped to the current application keymap mode state. </p>
<p> Due the the large number of modifier combinations, a key mapping will match if <i>at least</i> the specified identifiers are being set, and no other key mappings with those and more bits are being defined. That means that defining a mapping for <code>&quot;a&quot;</code> will automatically provide definitions for <code>&quot;Meta-a&quot;</code>, <code>&quot;Shift-a&quot;</code> and so on, unless some of those are defined mappings themselves. See the <code>&quot;builtin:&quot;</code> action, below, for a way to work around this when this is a problem. </p>
<p> The spelling of <i>key</i> depends on your implementation of X. An easy way to find a key name is to use the <code><a href="/docs/linux/man/1-xev/">xev</a></code>(1) command. You can find a list by looking for the <code>&quot;XK_&quot;</code> macros in the <code>X11/keysymdef.h</code> include file (omit the <code>&quot;XK_&quot;</code> prefix). Alternatively you can specify <i>key</i> by its hex keysym value (<code>0x0000 - 0xFFFF</code>). </p>
<p> As with any resource value, the <i>action</i> string may contain backslash escape sequences (<code>&quot;\n&quot;</code>: newline, <code>&quot;\\&quot;</code>: backslash, <code>&quot;\000&quot;</code>: octal number), see <font SIZE="-1">RESOURCES</font> in <code>&quot;man 7 X&quot;</code> for further details. </p>
<p> An action starts with an action prefix that selects a certain type of action, followed by a colon. An action string without colons is interpreted as a literal string to pass to the tty (as if it was prefixed with <code>&quot;string:&quot;</code>). </p>
<p> The following action prefixes are known - extensions can provide additional prefixes: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>string:STRING</dt>
<dd> <p> If the <i>action</i> starts with <code>&quot;string:&quot;</code> (or otherwise contains no colons), then the remaining <code>&quot;STRING&quot;</code> will be passed to the program running in the terminal. For example, you could replace whatever Shift-Tab outputs by the string <code>&quot;echo rm -rf /&quot;</code> followed by a newline: </p>
<pre><code>   URxvt.keysym.Shift-Tab: string:echo rm -rf /\n
</code></pre>
<p> This could in theory be used to completely redefine your keymap. </p>
<p> In addition, for actions of this type, you can define a range of keysyms in one shot by loading the <code>&quot;keysym-list&quot;</code> perl extension and providing an <i>action</i> with pattern <code>list/PREFIX/MIDDLE/SUFFIX</code>, where the delimiter `/&#8216; should be a character not used by the strings. </p>
<p> Its usage can be demonstrated by an example: </p>
<pre><code>  URxvt.keysym.M-C-0x61: list|\033&lt;|abc|&gt;
</code></pre>
<p> The above line is equivalent to the following three lines: </p>
<pre><code>  URxvt.keysym.Meta-Control-0x61: string:\033&lt;a&gt;
  URxvt.keysym.Meta-Control-0x62: string:\033&lt;b&gt;
  URxvt.keysym.Meta-Control-0x63: string:\033&lt;c&gt;
</code></pre>
 </dd>
<dt>command:STRING</dt>
<dd> <p> If <i>action</i> takes the form of <code>&quot;command:STRING&quot;</code>, the specified <font SIZE="-1"><code>STRING</code></font> is interpreted and executed as urxvt256c-ml&#8217;s control sequence (basically the opposite of <code>&quot;string:&quot;</code> - instead of sending it to the program running in the terminal, it will be treated as if it were program output). This is most useful to feed command sequences into urxvt256c-ml. </p>
<p> For example the following means &quot;change the current locale to <code>&quot;zh_CN.GBK&quot;</code> when Control-Meta-c is being pressed&quot;: </p>
<pre><code>  URxvt.keysym.M-C-c: command:\033]701;zh_CN.GBK\007
</code></pre>
<p> The following example will map Control-Meta-1 and Control-Meta-2 to the fonts <code>&quot;suxuseuro&quot;</code> and <code>&quot;9x15bold&quot;</code>, so you can have some limited font-switching at runtime: </p>
<pre><code>  URxvt.keysym.M-C-1: command:\033]50;suxuseuro\007
  URxvt.keysym.M-C-2: command:\033]50;9x15bold\007
</code></pre>
<p> Other things are possible, e.g. resizing (see <a href="/docs/linux/man/7-urxvt256c-ml/">urxvt256c-ml</a>(7) for more info): </p>
<pre><code>  URxvt.keysym.M-C-3: command:\033[8;25;80t
  URxvt.keysym.M-C-4: command:\033[8;48;110t
</code></pre>
 </dd>
<dt>builtin:</dt>
<dd> <p> The builtin action is the action that urxvt256c-ml would execute if no key binding existed for the key combination. The obvious use is to undo the effect of existing bindings. The not so obvious use is to reinstate bindings when another binding overrides too many modifiers. </p>
<p> For example if you overwrite the <code>&quot;Insert&quot;</code> key you will disable urxvt256c-ml&#8217;s <code>&quot;Shift-Insert&quot;</code> mapping. To re-enable that, you can poke ``holes&#8217;&#8216; into the user-defined keymap using the <code>&quot;builtin:&quot;</code> replacement: </p>
<pre><code>  URxvt.keysym.Insert: &lt;my insert key sequence&gt;
  URxvt.keysym.S-Insert: builtin:
</code></pre>
<p> The first line defines a mapping for <code>&quot;Insert&quot;</code> and <i>any</i> combination of modifiers. The second line re-establishes the default mapping for <code>&quot;Shift-Insert&quot;</code>. </p>
 </dd>
<dt>builtin-string:</dt>
<dd> <p> This action is mainly useful to restore string mappings for keys that have predefined actions in urxvt256c-ml. The exact semantics are a bit difficult to explain - basically, this action will send the string to the application that would be sent if urxvt256c-ml wouldn&#8217;t have a built-in action for it. </p>
<p> An example might make it clearer: urxvt256c-ml normally pastes the selection when you press <code>&quot;Shift-Insert&quot;</code>. With the following bindings, it would instead emit the (undocumented, but what applications running in the terminal might expect) sequence <code>&quot;ESC [ 2 $&quot;</code> instead: </p>
<pre><code>   URxvt.keysym.S-Insert: builtin-string:
   URxvt.keysym.C-S-Insert: builtin:
</code></pre>
<p> The first line disables the paste functionality for that key combination, and the second reinstates the default behaviour for <code>&quot;Control-Shift-Insert&quot;</code>, which would otherwise be overridden. </p>
<p> Similarly, to let applications gain access to the <code>&quot;C-M-c&quot;</code> (copy to clipboard) and <code>&quot;C-M-v&quot;</code> (paste clipboard) key combination, you can do this: </p>
<pre><code>   URxvt.keysym.C-M-c: builtin-string:
   URxvt.keysym.C-M-v: builtin-string:
</code></pre>
 </dd>
<dt><font SIZE="-1">EXTENSION:STRING</font></dt>
<dd> <p> An action of this form invokes the action <font SIZE="-1"><code>STRING</code></font>, if any, provided by the urxvt256c-ml <i>perl</i>(3) extension <font SIZE="-1"><code>EXTENSION</code></font>. The extension will be loaded automatically if necessary. </p>
<p> Not all extensions define actions, but popular extensions that do include the <i>selection</i> and <i>matcher</i> extensions (documented in their own manpages, urxvt256c-ml-<i>selection</i>(1) and urxvt256c-ml-<i>matcher</i>(1), respectively). </p>
<p> From the silly examples department, this will rot13-``encrypt&#8217;&#8216; urxvt256c-ml&#8217;s selection when Alt-Control-c is pressed on typical <font SIZE="-1">PC</font> keyboards: </p>
<pre><code>  URxvt.keysym.M-C-c: selection:rot13
</code></pre>
 </dd>
<dt>perl:STRING *DEPRECATED*</dt>
<dd> <p> This is a deprecated way of invoking commands provided by perl extensions. It is still supported, but should not be used anymore. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt><code>perl-ext-common</code>: <i>string</i></dt>
<dd>  </dd>
<dt><code>perl-ext</code>: <i>string</i></dt>
<dd> <p> Comma-separated list(s) of perl extension scripts (default: <code>&quot;default&quot;</code>) to use in this terminal instance; option <code>-pe</code>. </p>
<p> Extension names can be prefixed with a <code>&quot;-&quot;</code> sign to prohibit using them. This can be useful to selectively disable some extensions loaded by default, or specified via the <code>&quot;perl-ext-common&quot;</code> resource. For example, <code>&quot;default,-selection&quot;</code> will use all the default extensions except <code>&quot;selection&quot;</code>. </p>
<p> The default set includes the <code>&quot;selection&quot;</code>, <code>&quot;option-popup&quot;</code>, <code>&quot;selection-popup&quot;</code>, <code>&quot;readline&quot;</code> and <code>&quot;searchable-scrollback&quot;</code> extensions, and extensions which are mentioned in <code>keysym</code> resources. </p>
<p> Any extension such that a corresponding resource is given on the command line is automatically appended to <code>perl-ext</code>. </p>
<p> Each extension is looked up in the library directories, loaded if necessary, and bound to the current terminal instance. When the library search path contains multiple extension files of the same name, then the first one found will be used. </p>
<p> If both of these resources are the empty string, then the perl interpreter will not be initialized. The rationale for having two options is that <code>perl-ext-common</code> will be used for extensions that should be available to all instances, while <code>perl-ext</code> is used for specific instances. </p>
 </dd>
<dt><code>perl-eval</code>: <i>string</i></dt>
<dd> <p> Perl code to be evaluated when all extensions have been registered. See the urxvt256c-ml <i>perl</i>(3) manpage. </p>
 </dd>
<dt><code>perl-lib</code>: <i>path</i></dt>
<dd> <p> Colon-separated list of additional directories that hold extension scripts. When looking for perl extensions, urxvt256c-ml will first look in these directories, then in <code>$URXVT_PERL_LIB</code>, <i></i>$HOME <i>/.urxvt/ext</i> and lastly in <i>/usr/lib64/urxvt/perl/</i>. </p>
<p> See the urxvt256c-ml <i>perl</i>(3) manpage. </p>
 </dd>
<dt><code>selection.pattern-</code>idx: <i>perl-regex</i></dt>
<dd> <p> Additional selection patterns, see the urxvt256c-ml <i>perl</i>(3) manpage for details. </p>
 </dd>
<dt><code>selection-autotransform.</code>idx: <i>perl-transform</i></dt>
<dd> <p> Selection auto-transform patterns, see the urxvt256c-ml <i>perl</i>(3) manpage for details. </p>
 </dd>
<dt><code>searchable-scrollback:</code><i>keysym</i> *DEPRECATED*</dt>
<dd> <p> This resource is deprecated and will be removed. Use a <code>keysym</code> resource instead, e.g.: </p>
<pre><code>   URxvt.keysym.M-s: searchable-scrollback:start
</code></pre>
 </dd>
<dt><code>url-launcher</code>: <i>string</i></dt>
<dd> <p> Specifies the program to be started with a <font SIZE="-1">URL</font> argument. Used by the <code>&quot;selection-popup&quot;</code> and <code>&quot;matcher&quot;</code> perl extensions. </p>
 </dd>
<dt><code>transient-for</code>: <i>windowid</i></dt>
<dd> <p> Compile <i>frills</i>: Sets the <font SIZE="-1">WM_TRANSIENT_FOR</font> property to the given window id. </p>
 </dd>
<dt><code>override-redirect</code>: <i>boolean</i></dt>
<dd> <p> Compile <i>frills</i>: Sets override-redirect for the terminal window, making it almost invisible to window managers; option <code>-override-redirect</code>. </p>
 </dd>
<dt><code>iso14755:</code><i>boolean</i></dt>
<dd> <p> Turn on/off <font SIZE="-1">ISO 14755 </font>(default enabled). </p>
 </dd>
<dt><code>iso14755_52:</code><i>boolean</i></dt>
<dd> <p> Turn on/off <font SIZE="-1">ISO 14755 5.2</font> mode (default enabled). </p>
 </dd></dl>
<h2>BACKGROUND IMAGE OPTIONS AND RESOURCES</h2>
<dl>
<dt><code>-pixmap</code><i>file[;oplist]</i></dt>
<dd>  </dd>
<dt><code>backgroundPixmap:</code><i>file[;oplist]</i></dt>
<dd> <p> Compile <i>pixbuf</i>: Use the specified image file as the window&#8217;s background and also optionally specify a colon separated list of operations to modify it. Note that you may need to quote the <code>&quot;;&quot;</code> character when using the command line option, as <code>&quot;;&quot;</code> is usually a metacharacter in shells. Supported operations are: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>WxH+X+Y</code></dt>
<dd> <p> sets scale and position. <code>``W&#8217;&#8216; / ``H&#8217;&#8216;</code> specify the horizontal/vertical scale (percent), and <code>``X&#8217;&#8216; / ``Y&#8217;&#8216;</code> locate the image centre (percent). A scale of 0 disables scaling. </p>
 </dd>
<dt><code>op=tile</code></dt>
<dd> <p> enables tiling </p>
 </dd>
<dt><code>op=keep-aspect</code></dt>
<dd> <p> maintain the image aspect ratio when scaling </p>
 </dd>
<dt><code>op=root-align</code></dt>
<dd> <p> use the position of the terminal window relative to the root window as the image offset, simulating a root window background </p>
 </dd></dl>
</dl>
<dl>
<dd> <p> The default scale and position setting is <code>&quot;100x100+50+50&quot;</code>. Alternatively, a predefined set of templates can be used to achieve the most common setups: </p>
 </dd>
<dl>
<dt><code>style=tiled</code></dt>
<dd> <p> the image is tiled with no scaling. Equivalent to 0x0+0+0:op=tile </p>
 </dd>
<dt><code>style=aspect-stretched</code></dt>
<dd> <p> the image is scaled to fill the whole window maintaining the aspect ratio and centered. Equivalent to 100x100+50+50:op=keep-aspect </p>
 </dd>
<dt><code>style=stretched</code></dt>
<dd> <p> the image is scaled to fill the whole window. Equivalent to 100x100 </p>
 </dd>
<dt><code>style=centered</code></dt>
<dd> <p> the image is centered with no scaling. Equivalent to 0x0+50+50 </p>
 </dd>
<dt><code>style=root-tiled</code></dt>
<dd> <p> the image is tiled with no scaling and using &#8216;root&#8217; positioning. Equivalent to 0x0:op=tile:op=root-align </p>
 </dd></dl>
</dl>
<dl>
<dd> <p> If multiple templates are specified the last one wins. Note that a template overrides all the scale, position and operations settings. </p>
<p> If used in conjunction with pseudo-transparency, the specified pixmap will be blended over the transparent background using alpha-blending. </p>
 </dd></dl>
<dt><code>-tr</code>|<code>+tr</code></dt>
<dd>  </dd>
<dt><code>transparent:</code><i>boolean</i></dt>
<dd> <p> Turn on/off pseudo-transparency by using the root pixmap as background. </p>
<p> <code>-ip</code> (<code>inheritPixmap</code>) is still accepted as an obsolete alias but will be removed in future versions. </p>
 </dd>
<dt><code>-tint</code><i>colour</i></dt>
<dd>  </dd>
<dt><code>tintColor:</code><i>colour</i></dt>
<dd> <p> Tint the transparent background with the given colour. Note that a black tint yields a completely black image while a white tint yields the image unchanged. </p>
 </dd>
<dt><code>-sh</code><i>number</i></dt>
<dd>  </dd>
<dt><code>shading:</code><i>number</i></dt>
<dd> <p> Darken (0 .. 99) or lighten (101 .. 200) the transparent background. A value of 100 means no shading. </p>
 </dd>
<dt><code>-blr</code><i>HxV</i></dt>
<dd>  </dd>
<dt><code>blurRadius:</code><i>HxV</i></dt>
<dd> <p> Apply gaussian blur with the specified radius to the transparent background. If a single number is specified, the vertical and horizontal radii are considered to be the same. Setting one of the radii to 1 and the other to a large number creates interesting effects on some backgrounds. The maximum radius value is 128. An horizontal or vertical radius of 0 disables blurring. </p>
 </dd>
<dt><code>path:</code><i>path</i></dt>
<dd> <p> Specify the colon-delimited search path for finding background image files. </p>
 </dd></dl>
<h2>THE SCROLLBAR</h2>
<p> Lines of text that scroll off the top of the <code>urxvt256c-ml</code> window (resource: <code>saveLines</code>) and can be scrolled back using the scrollbar or by keystrokes. The normal <code>urxvt256c-ml</code> scrollbar has arrows and its behaviour is fairly intuitive. The <code>xterm-scrollbar</code> is without arrows and its behaviour mimics that of <i>xterm</i> </p>
<p> Scroll down with <code>Button1</code> (<code>xterm-scrollbar</code>) or <code>Shift-Next</code>. Scroll up with <code>Button3</code> (<code>xterm-scrollbar</code>) or <code>Shift-Prior</code>. Continuous scroll with <code>Button2</code>.  </p>
<h2>MOUSE REPORTING</h2>
<p> To temporarily override mouse reporting, for either the scrollbar or the normal text selection/insertion, hold either the Shift or the Meta (Alt) key while performing the desired mouse action. </p>
<p> If mouse reporting mode is active, the normal scrollbar actions are disabled --- on the assumption that we are using a fullscreen application. Instead, pressing Button1 and Button3 sends <font SIZE="-1"><code>ESC</code></font><code> [ 6 ~</code> (Next) and <font SIZE="-1"><code>ESC</code></font><code> [ 5 ~</code> (Prior), respectively. Similarly, clicking on the up and down arrows sends <font SIZE="-1"><code>ESC</code></font><code> [ A</code> (Up) and <font SIZE="-1"><code>ESC</code></font><code> [ B</code> (Down), respectively.  </p>
<h2>THE SELECTION: SELECTING AND PASTING TEXT</h2>
<p> The behaviour of text selection and insertion/pasting mechanism is similar to <i><a href="/docs/linux/man/1-xterm/">xterm</a></i>(1). </p>
<dl>
<dt><code>Selecting</code>:</dt>
<dd> <p> Left click at the beginning of the region, drag to the end of the region and release; Right click to extend the marked region; Left double-click to select a word; Left triple-click to select the entire logical line (which can span multiple screen lines), unless modified by resource <code>tripleclickwords</code>. </p>
<p> Starting a selection while pressing the <code>Meta</code> key (or <code>Meta+Ctrl</code> keys) (Compile: <i>frills</i>) will create a rectangular selection instead of a normal one. In this mode, every selected row becomes its own line in the selection, and trailing whitespace is visually underlined and removed from the selection. </p>
 </dd>
<dt><code>Pasting</code>:</dt>
<dd> <p> Pressing and releasing the Middle mouse button in an <code>urxvt256c-ml</code> window causes the value of the <font SIZE="-1">PRIMARY</font> selection (or <font SIZE="-1">CLIPBOARD</font> with the <code>Meta</code> modifier) to be inserted as if it had been typed on the keyboard. </p>
<p> Pressing <code>Shift-Insert</code> causes the value of the <font SIZE="-1">PRIMARY</font> selection to be inserted too. </p>
<p> rxvt-unicode also provides the bindings <code>Ctrl-Meta-c</code> and &lt;Ctrl-Meta-v&gt; to interact with the <font SIZE="-1">CLIPBOARD</font> selection. The first binding causes the value of the internal selection to be copied to the <font SIZE="-1">CLIPBOARD</font> selection, while the second binding causes the value of the <font SIZE="-1">CLIPBOARD</font> selection to be inserted. </p>
 </dd></dl>
<h2>CHANGING FONTS</h2>
<p> Changing fonts (or font sizes, respectively) via the keypad is not yet supported in rxvt-unicode. Bug me if you need this. </p>
<p> You can, however, switch fonts at runtime using escape sequences, e.g.: </p>
<pre><code>   printf '\e]710;%s\007' &quot;9x15bold,xft:Kochi Gothic&quot;
</code></pre>
<p> You can use keyboard shortcuts, too: </p>
<pre><code>   URxvt.keysym.M-C-1: command:\033]710;suxuseuro\007\033]711;suxuseuro\007
   URxvt.keysym.M-C-2: command:\033]710;9x15bold\007\033]711;9x15bold\007
</code></pre>
<p> rxvt-unicode will automatically re-apply these fonts to the output so far.  </p>
<h2>ISO 14755 SUPPORT</h2>
<p> <font SIZE="-1">ISO 14755</font> is a standard for entering and viewing unicode characters and character codes using the keyboard. It consists of 4 parts. The first part is available if rxvt-unicode has been compiled with <code>&quot;--enable-frills&quot;</code>, the rest is available when rxvt-unicode was compiled with <code>&quot;--enable-iso14755&quot;</code>. </p>
<dl>
<dt>&bull;</dt>
<dd> <p> 5.1: Basic method </p>
<p> This allows you to enter unicode characters using their hexcode. </p>
<p> Start by pressing and holding both <code>&quot;Control&quot;</code> and <code>&quot;Shift&quot;</code>, then enter hex-digits (between one and six). Releasing <code>&quot;Control&quot;</code> and <code>&quot;Shift&quot;</code> will commit the character as if it were typed directly. While holding down <code>&quot;Control&quot;</code> and <code>&quot;Shift&quot;</code> you can also enter multiple characters by pressing <code>&quot;Space&quot;</code>, which will commit the current character and lets you start a new one. </p>
<p> As an example of use, imagine a business card with a japanese e-mail address, which you cannot type. Fortunately, the card has the e-mail address printed as hexcodes, e.g. <code>&quot;671d 65e5&quot;</code>. You can enter this easily by pressing <code>&quot;Control&quot;</code> and <code>&quot;Shift&quot;</code>, followed by <code>&quot;6-7-1-D-SPACE-6-5-E-5&quot;</code>, followed by releasing the modifier keys. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> 5.2: Keyboard symbols entry method </p>
<p> This mode lets you input characters representing the keycap symbols of your keyboard, if representable in the current locale encoding. </p>
<p> Start by pressing <code>&quot;Control&quot;</code> and <code>&quot;Shift&quot;</code> together, then releasing them. The next special key (cursor keys, home etc.) you enter will not invoke its usual function but instead will insert the corresponding keycap symbol. The symbol will only be entered when the key has been released, otherwise pressing e.g. <code>&quot;Shift&quot;</code> would enter the symbol for <code>&quot;ISO Level 2 Switch&quot;</code>, although your intention might have been to enter a reverse tab (Shift-Tab). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> 5.3: Screen-selection entry method </p>
<p> While this is implemented already (it&#8217;s basically the selection mechanism), it could be extended by displaying a unicode character map. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> 5.4: Feedback method for identifying displayed characters for later input </p>
<p> This method lets you display the unicode character code associated with characters already displayed. </p>
<p> You enter this mode by holding down <code>&quot;Control&quot;</code> and <code>&quot;Shift&quot;</code> together, then pressing and holding the left mouse button and moving around. The unicode hex code(s) (it might be a combining character) of the character under the pointer is displayed until you release <code>&quot;Control&quot;</code> and <code>&quot;Shift&quot;</code>. </p>
<p> In addition to the hex codes it will display the font used to draw this character - due to implementation reasons, characters combined with combining characters, line drawing characters and unknown characters will always be drawn using the built-in support font. </p>
 </dd></dl>
<p> With respect to conformance, rxvt-unicode is supposed to be compliant to both scenario A and B of <font SIZE="-1">ISO 14755,</font> including part 5.2.  </p>
<h2>LOGIN STAMP</h2>
<p> <code>urxvt256c-ml</code> tries to write an entry into the <i><a href="/docs/linux/man/5-utmp/">utmp</a></i>(5) file so that it can be seen via the <i><a href="/docs/linux/man/1-who/">who</a>(1)</i> command, and can accept messages. To allow this feature, <code>urxvt256c-ml</code> may need to be installed setuid root on some systems or setgid to root or to some other group on others.  </p>
<h2>COLOURS AND GRAPHICS</h2>
<p> In addition to the default foreground and background colours, <code>urxvt256c-ml</code> can display up to 88/256 colours: 8 <font SIZE="-1">ANSI</font> colours plus high-intensity (potentially bold/blink) versions of the same, and 72 (or 240 in 256 colour mode) colours arranged in an 4x4x4 (or 6x6x6) colour <font SIZE="-1">RGB</font> cube plus a 8 (24) colour greyscale ramp. </p>
<p> Here is a list of the <font SIZE="-1">ANSI</font> colours with their names. </p>
<table>
<tr VALIGN=top>
<td>color0</td>
<td>(black)</td>
<td>= Black
</td>
</tr>
<tr VALIGN=top>
<td>color1</td>
<td>(red)</td>
<td>= Red3
</td>
</tr>
<tr VALIGN=top>
<td>color2</td>
<td>(green)</td>
<td>= Green3
</td>
</tr>
<tr VALIGN=top>
<td>color3</td>
<td>(yellow)</td>
<td>= Yellow3
</td>
</tr>
<tr VALIGN=top>
<td>color4</td>
<td>(blue)</td>
<td>= Blue3
</td>
</tr>
<tr VALIGN=top>
<td>color5</td>
<td>(magenta)</td>
<td>= Magenta3
</td>
</tr>
<tr VALIGN=top>
<td>color6</td>
<td>(cyan)</td>
<td>= Cyan3
</td>
</tr>
<tr VALIGN=top>
<td>color7</td>
<td>(white)</td>
<td>= AntiqueWhite
</td>
</tr>
<tr VALIGN=top>
<td>color8</td>
<td>(bright black)</td>
<td>= Grey25
</td>
</tr>
<tr VALIGN=top>
<td>color9</td>
<td>(bright red)</td>
<td>= Red
</td>
</tr>
<tr VALIGN=top>
<td>color10</td>
<td>(bright green)</td>
<td>= Green
</td>
</tr>
<tr VALIGN=top>
<td>color11</td>
<td>(bright yellow)</td>
<td>= Yellow
</td>
</tr>
<tr VALIGN=top>
<td>color12</td>
<td>(bright blue)</td>
<td>= Blue
</td>
</tr>
<tr VALIGN=top>
<td>color13</td>
<td>(bright magenta)</td>
<td>= Magenta
</td>
</tr>
<tr VALIGN=top>
<td>color14</td>
<td>(bright cyan)</td>
<td>= Cyan
</td>
</tr>
<tr VALIGN=top>
<td>color15</td>
<td>(bright white)</td>
<td>= White
</td>
</tr>
<tr VALIGN=top>
<td>foreground</td>
<td></td>
<td>= Black
</td>
</tr>
<tr VALIGN=top>
<td>background</td>
<td></td>
<td>= White
</td>
</tr>
</table>
<p> It is also possible to specify the colour values of <code>foreground</code>, <code>background</code>, <code>cursorColor</code>, <code>cursorColor2</code>, <code>colorBD</code>, <code>colorUL</code> as a number 0-15, as a convenient shorthand to reference the colour name of color0-color15. </p>
<p> The following text gives values for the standard 88 colour mode (and values for the 256 colour mode in parentheses). </p>
<p> The <font SIZE="-1">RGB</font> cube uses indices 16..79 (16..231) using the following formulas: </p>
<pre><code>   index_88 = (r * 4 + g) * 4 + b + 16 # r, g, b = 0..3
   index_256 = (r * 6 + g) * 6 + b + 16 # r, g, b = 0..5
</code></pre>
<p> The grayscale ramp uses indices 80..87 (232..239), from 10% to 90% in 10% steps (1/26 to 25/26 in 1/26 steps) - black and white are already part of the <font SIZE="-1">RGB</font> cube. </p>
<p> Together, all those colours implement the 88 (256) colour xterm colours. Only the first 16 can be changed using resources currently, the rest can only be changed via command sequences (``escape codes&#8217;&#8216;). </p>
<p> Applications are advised to use terminfo or command sequences to discover number and <font SIZE="-1">RGB</font> values of all colours (yes, you can query this...). </p>
<p> Note that <code>-rv</code> (<code>``reverseVideo: True&#8217;&#8216;</code>) simulates reverse video by always swapping the foreground/background colours. This is in contrast to <i><a href="/docs/linux/man/1-xterm/">xterm</a></i>(1) where the colours are only swapped if they have not otherwise been specified. For example, </p>
<pre><code>   urxvt256c-ml -fg Black -bg White -rv
</code></pre>
<p> would yield White on Black, while on <i><a href="/docs/linux/man/1-xterm/">xterm</a></i>(1) it would yield Black on White.  </p>
<font SIZE="-1"></font><h3>ALPHA CHANNEL SUPPORT</h3>
<p> If Xft support has been compiled in and as long as Xft/Xrender/X don&#8217;t get their act together, rxvt-unicode will do its own alpha channel management: </p>
<p> You can prefix any colour with an opaqueness percentage enclosed in brackets, i.e. <code>&quot;[percent]&quot;</code>, where <code>&quot;percent&quot;</code> is a decimal percentage (0-100) that specifies the opacity of the colour, where <code>0</code> is completely transparent and <code>100</code> is completely opaque. For example, <code>&quot;[50]red&quot;</code> is a half-transparent red, while <code>&quot;[95]#00ff00&quot;</code> is an almost opaque green. This is the recommended format to specify transparency values, and works with all ways to specify a colour. </p>
<p> For complete control, rxvt-unicode also supports <code>&quot;rgba:rrrr/gggg/bbbb/aaaa&quot;</code> (exactly four hex digits/component) colour specifications, where the additional <code>&quot;aaaa&quot;</code> component specifies opacity (alpha) values. The minimum value of <code>0000</code> is completely transparent, while <code>&quot;ffff&quot;</code> is completely opaque). The two example colours from earlier could also be specified as <code>&quot;rgba:ff00/0000/0000/8000&quot;</code> and <code>&quot;rgba:0000/ff00/0000/f332&quot;</code>. </p>
<p> You probably need to specify <code>``-depth 32&#8217;&#8216;</code>, too, to force a visual with alpha channels, and have the luck that your X-server uses <font SIZE="-1">ARGB</font> pixel layout, as X is far from just supporting <font SIZE="-1">ARGB</font> visuals out of the box, and rxvt-unicode just fudges around. </p>
<p> For example, the following selects an almost completely transparent black background, and an almost opaque pink foreground: </p>
<pre><code>   urxvt256c-ml -depth 32 -bg rgba:0000/0000/0000/4444 -fg &quot;[80]pink&quot;
</code></pre>
<p> When not using a background image, then the interpretation of the alpha channel is up to your compositing manager (most interpret it as transparency of course). </p>
<p> When using a background pixmap or pseudo-transparency, then the background colour will always behave as if it were completely transparent (so the background image shows instead), regardless of how it was specified, while other colours will either be transparent as specified (the background image will show through) on servers supporting the <font SIZE="-1">RENDER</font> extension, or fully opaque on servers not supporting the <font SIZE="-1">RENDER EXTENSION.</font> </p>
<p> Please note that due to bugs in Xft, specifying alpha values might result in garbage being displayed when the X-server does not support the <font SIZE="-1">RENDER</font> extension.  </p>
<h2>ENVIRONMENT</h2>
<p> <code>urxvt256c-ml</code> sets and/or uses the following environment variables: </p>
<dl>
<dt><font SIZE="-1"><code>TERM</code></font></dt>
<dd> <p> Normally set to <code>&quot;rxvt-unicode&quot;</code>, unless overwritten at configure time, via resources or on the command line. </p>
 </dd>
<dt><font SIZE="-1"><code>COLORTERM</code></font></dt>
<dd> <p> Either <code>&quot;rxvt&quot;</code>, <code>&quot;rxvt-xpm&quot;</code>, depending on whether urxvt256c-ml was compiled with background image support, and optionally with the added extension <code>&quot;-mono&quot;</code> to indicate that rxvt-unicode runs on a monochrome screen. </p>
 </dd>
<dt><font SIZE="-1"><code>COLORFGBG</code></font></dt>
<dd> <p> Set to a string of the form <code>&quot;fg;bg&quot;</code> or <code>&quot;fg;xpm;bg&quot;</code>, where <code>&quot;fg&quot;</code> is the colour code used as default foreground/text colour (or the string <code>&quot;default&quot;</code> to indicate that the default-colour escape sequence is to be used), <code>&quot;bg&quot;</code> is the colour code used as default background colour (or the string <code>&quot;default&quot;</code>), and <code>&quot;xpm&quot;</code> is the string <code>&quot;default&quot;</code> if urxvt256c-ml was compiled with background image support. Libraries like <code>&quot;ncurses&quot;</code> and <code>&quot;slang&quot;</code> can (and do) use this information to optimize screen output. </p>
 </dd>
<dt><font SIZE="-1"><code>WINDOWID</code></font></dt>
<dd> <p> Set to the (decimal) X Window <font SIZE="-1">ID</font> of the urxvt256c-ml window (the toplevel window, which usually has subwindows for the scrollbar, the terminal window and so on). </p>
 </dd>
<dt><font SIZE="-1"><code>TERMINFO</code></font></dt>
<dd> <p> Set to the terminfo directory iff urxvt256c-ml was configured with <code>&quot;--with-terminfo=PATH&quot;</code>. </p>
 </dd>
<dt><font SIZE="-1"><code>DISPLAY</code></font></dt>
<dd> <p> Used by urxvt256c-ml to connect to the display and set to the correct display in its child processes if <code>&quot;-display&quot;</code> isn&#8217;t used to override. It defaults to <code>&quot;:0&quot;</code> if it doesn&#8217;t exist. </p>
 </dd>
<dt><font SIZE="-1"><code>SHELL</code></font></dt>
<dd> <p> The shell to be used for command execution, defaults to <code>&quot;/bin/sh&quot;</code>. </p>
 </dd>
<dt><font SIZE="-1"><code>RXVT_SOCKET</code></font> [<i>sic</i>]</dt>
<dd> <p> The unix domain socket path used by <a href="/docs/linux/man/1-urxvt256c-mlc/">urxvt256c-mlc</a>(1) and <a href="/docs/linux/man/1-urxvt256c-mld/">urxvt256c-mld</a>(1). </p>
<p> Default <i></i>$HOME <i>/.urxvt/urxvtd-&lt;nodename&gt;</i>. </p>
 </dd>
<dt><font SIZE="-1"><code>URXVT_PERL_LIB</code></font></dt>
<dd> <p> Additional <i>:</i>-separated library search path for perl extensions. Will be searched after <code>-perl-lib</code> but before <i>~/.urxvt/ext</i> and the system library directory. </p>
 </dd>
<dt><font SIZE="-1"><code>URXVT_PERL_VERBOSITY</code></font></dt>
<dd> <p> See <a href="/docs/linux/man/3-urxvt256c-mlperl/">urxvt256c-mlperl</a>(3). </p>
 </dd>
<dt><font SIZE="-1"><code>HOME</code></font></dt>
<dd> <p> Used to locate the default directory for the unix domain socket for daemon communications and to locate various resource files (such as <code>&quot;.Xdefaults&quot;</code>) </p>
 </dd>
<dt><font SIZE="-1"><code>XAPPLRESDIR</code></font></dt>
<dd> <p> Directory where application-specific X resource files are located. </p>
 </dd>
<dt><font SIZE="-1"><code>XENVIRONMENT</code></font></dt>
<dd> <p> If set and accessible, gives the name of a X resource file to be loaded by urxvt256c-ml. </p>
 </dd></dl>
<h2>FILES</h2>
<dl>
<dt><code>/usr/lib/X11/rgb.txt</code></dt>
<dd> <p> Colour names. </p>
 </dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-urxvt256c-ml/">urxvt256c-ml</a>(7), <a href="/docs/linux/man/1-urxvt256c-mlc/">urxvt256c-mlc</a>(1), <a href="/docs/linux/man/1-urxvt256c-mld/">urxvt256c-mld</a>(1), urxvt256c-ml-<i>extensions</i>(1), urxvt256c-ml <i>perl</i>(3), <i><a href="/docs/linux/man/1-xterm/">xterm</a></i>(1), <i><a href="/docs/linux/man/1-sh/">sh</a></i>(1), <i><a href="/docs/linux/man/1-resize/">resize</a></i>(1), X(1), <i>pty</i>(4), <i><a href="/docs/linux/man/4-tty/">tty</a></i>(4), <i><a href="/docs/linux/man/5-utmp/">utmp</a></i>(5)  </p>
<h2>CURRENT PROJECT COORDINATOR</h2>
<dl>
<dt>Project Coordinator</dt>
<dd> <p> Marc A. Lehmann &lt;rxvt-unicode [at] schmorp.de&gt;. </p>
<p> &lt;<a rel="nofollow" href="http://software.schmorp.de/pkg/rxvt-unicode.html">http://software.schmorp.de/pkg/rxvt-unicode.html</a>&gt; </p>
 </dd></dl>
<h2>AUTHORS</h2>
<dl>
<dt>John Bovey</dt>
<dd> <p> University of Kent, 1992, wrote the original Xvt. </p>
 </dd>
<dt>Rob Nation &lt;nation [at] rocket.sanders.lockheed.com&gt;</dt>
<dd> <p> very heavily modified Xvt and came up with Rxvt </p>
 </dd>
<dt>Angelo Haritsis &lt;ah [at] doc.ic.ac.uk&gt;</dt>
<dd> <p> wrote the Greek Keyboard Input (no longer in code) </p>
 </dd>
<dt>mj olesen &lt;olesen [at] me.QueensU.CA&gt;</dt>
<dd> <p> Wrote the menu system. </p>
<p> Project Coordinator (changes.txt 2.11 to 2.21) </p>
 </dd>
<dt>Oezguer Kesim &lt;kesim [at] math.fu-berlin.de&gt;</dt>
<dd> <p> Project Coordinator (changes.txt 2.21a to 2.4.5) </p>
 </dd>
<dt>Geoff Wing &lt;gcw [at] pobox.com&gt;</dt>
<dd> <p> Rewrote screen display and text selection routines. </p>
<p> Project Coordinator (changes.txt 2.4.6 - rxvt-unicode) </p>
 </dd>
<dt>Marc Alexander Lehmann &lt;rxvt-unicode [at] schmorp.de&gt;</dt>
<dd> <p> Forked rxvt-unicode, unicode support, rewrote almost all the code, perl extension, random hacks, numerous bugfixes and extensions. </p>
<p> Project Coordinator (Changes 1.0 -) </p>
 </dd>
<dt>Emanuele Giaquinta &lt;emanuele.giaquinta [at] gmail.com&gt;</dt>
<dd> <p> pty/utmp code rewrite, image code improvements, many random hacks and bugfixes. </p>
 </dd></dl>
