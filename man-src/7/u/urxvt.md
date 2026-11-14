---
title: "urxvt(7)"
name: "urxvt"
section: "7"
letter: "u"
url: "/docs/linux/man/7-urxvt/"
description: "RXVT REFERENCE – FAQ, command sequences and other background information"
---

<p>RXVT REFERENCE &#8211; FAQ, command sequences and other background information</p>
<h2>Synopsis</h2>
<pre><code># set a new font set
printf '\33]50;%s' 9x15,xft:Kochi&quot; Mincho&quot;

# change the locale and tell rxvt-unicode about it
export LC_CTYPE=ja_JP.EUC-JP; printf &quot;\33]701;$LC_CTYPE&quot;

# set window title
printf '\33]2;%s' &quot;new window title&quot;</code></pre>
<h2>Description</h2>
<p>This document contains the <font SIZE="-1">FAQ,</font> the <font SIZE="-1">RXVT TECHNICAL REFERENCE</font> documenting all escape sequences, and other background information. </p>
<p> The newest version of this document is also available on the World Wide Web at &lt;<a rel="nofollow" href="http://pod.tst.eu/http://cvs.schmorp.de/rxvt-unicode/doc/rxvt.7.pod">http://pod.tst.eu/http://cvs.schmorp.de/rxvt-unicode/doc/rxvt.7.pod</a>&gt;. </p>
<p> The main manual page for urxvt itself is available at &lt;<a rel="nofollow" href="http://pod.tst.eu/http://cvs.schmorp.de/rxvt-unicode/doc/rxvt.1.pod">http://pod.tst.eu/http://cvs.schmorp.de/rxvt-unicode/doc/rxvt.1.pod</a>&gt;.</p>
<h2>Rxvt-Unicode/Urxvt Frequently Asked Questions</h2>
<h3>Meta, Features &amp; Commandline Issues</h3>
<p><i>My question isn&#8217;t answered here, can I ask a human?</i> </p>
<p> Before sending me mail, you could go to <font SIZE="-1">IRC: </font><tt>&quot;irc.freenode.net&quot;</tt>, channel <tt>&quot;#rxvt-unicode&quot;</tt> has some rxvt-unicode enthusiasts that might be interested in learning about new and exciting problems (but not FAQs :). </p>
<p> <i>I use Gentoo, and I have a problem&#8230;</i> </p>
<p> There are two big problems with Gentoo Linux: first, most if not all Gentoo systems are completely broken (missing or mismatched header files, broken compiler etc. are just the tip of the iceberg); secondly, it should be called Gentoo GNU/Linux. </p>
<p> For these reasons, it is impossible to support rxvt-unicode on Gentoo. Problems appearing on Gentoo systems will usually simply be ignored unless they can be reproduced on non-Gentoo systems. </p>
<p> <i>Does it support tabs, can I have a tabbed rxvt-unicode?</i> </p>
<p> Beginning with version 7.3, there is a perl extension that implements a simple tabbed terminal. It is installed by default, so any of these should give you tabs: </p>
<pre> urxvt -pe tabbed
 URxvt.perl-ext-common: default,tabbed</pre>
<p>It will also work fine with tabbing functionality of many window managers or similar tabbing programs, and its embedding-features allow it to be embedded into other programs, as witnessed by <i>doc/rxvt-tabbed</i> or the upcoming <tt>&quot;Gtk2::URxvt&quot;</tt> perl module, which features a tabbed urxvt (murxvt) terminal as an example embedding application. </p>
<p> <i>How do I know which rxvt-unicode version I&#8217;m using?</i> </p>
<p> The version number is displayed with the usage (-h). Also the escape sequence <tt>&quot;ESC [ 8 n&quot;</tt> sets the window title to the version number. When using the urxvtc client, the version displayed is that of the daemon. </p>
<p> <i>Rxvt-unicode uses gobs of memory, how can I reduce that?</i> </p>
<p> Rxvt-unicode tries to obey the rule of not charging you for something you don&#8217;t use. One thing you should try is to configure out all settings that you don&#8217;t need, for example, Xft support is a resource hog by design, when used. Compiling it out ensures that no Xft font will be loaded accidentally when rxvt-unicode tries to find a font for your characters. </p>
<p> Also, many people (me included) like large windows and even larger scrollback buffers: Without <tt>&quot;--enable-unicode3&quot;</tt>, rxvt-unicode will use 6 bytes per screen cell. For a 160x?? window this amounts to almost a kilobyte per line. A scrollback buffer of 10000 lines will then (if full) use 10 Megabytes of memory. With <tt>&quot;--enable-unicode3&quot;</tt> it gets worse, as rxvt-unicode then uses 8 bytes per screen cell. </p>
<p> <i>How can I start urxvtd in a race-free way?</i> </p>
<p> Try <tt>&quot;urxvtd -f -o&quot;</tt>, which tells urxvtd to open the display, create the listening socket and then fork. </p>
<p> <i>How can I start urxvtd automatically when I run urxvtc?</i> </p>
<p> If you want to start urxvtd automatically whenever you run urxvtc and the daemon isn&#8217;t running yet, use this script: </p>
<pre> #!/bin/sh
 urxvtc &quot;$@&quot;
 if [ $? -eq 2 ]; then
 urxvtd -q -o -f
 urxvtc &quot;$@&quot;
 fi</pre>
<p>This tries to create a new terminal, and if fails with exit status 2, meaning it couldn&#8217;t connect to the daemon, it will start the daemon and re-run the command. Subsequent invocations of the script will re-use the existing daemon. </p>
<p> <i>How do I distinguish whether I&#8217;m running rxvt-unicode or a regular xterm? I need this to decide about setting colours etc.</i> </p>
<p> The original rxvt and rxvt-unicode always export the variable &#8220;<font SIZE="-1">COLORTERM&#8221;,</font> so you can check and see if that is set. Note that several programs, <font SIZE="-1">JED,</font> slrn, Midnight Commander automatically check this variable to decide whether or not to use colour. </p>
<p> <i>How do I set the correct, full </i><font SIZE="-1"><i>IP</i></font><i> address for the </i><font SIZE="-1"><i>DISPLAY</i></font><i> variable?</i> </p>
<p> If you&#8217;ve compiled rxvt-unicode with <font SIZE="-1">DISPLAY_IS_IP</font> and have enabled insecure mode then it is possible to use the following shell script snippets to correctly set the display. If your version of rxvt-unicode wasn&#8217;t also compiled with <font SIZE="-1">ESCZ_ANSWER </font>(as assumed in these snippets) then the <font SIZE="-1">COLORTERM</font> variable can be used to distinguish rxvt-unicode from a regular xterm. </p>
<p> Courtesy of Chuck Blake &lt;cblake [at] BBN.COM&gt; with the following shell script snippets: </p>
<pre> # Bourne/Korn/POSIX family of shells:
 [ ${TERM:-foo} = foo ] &amp;&amp; TERM=xterm # assume an xterm if we don't know
 if [ ${TERM:-foo} = xterm ]; then
 stty -icanon -echo min 0 time 15 # see if enhanced rxvt or not
 printf &quot;Z&quot;
 read term_id
 stty icanon echo
 if [ &quot;&quot;${term_id} = '^[[?1;2C' -a ${DISPLAY:-foo} = foo ]; then
 printf '[7n' # query the rxvt we are in for the DISPLAY string
 read DISPLAY # set it in our local shell
 fi
 fi</pre>
<p><i>How do I compile the manual pages on my own?</i> </p>
<p> You need to have a recent version of perl installed as <i>/usr/bin/perl</i>, one that comes with <i>pod2man</i>, <i>pod2text</i> and <i>pod2xhtml</i> (from <i>Pod::Xhtml</i>). Then go to the doc subdirectory and enter <tt>&quot;make alldoc&quot;</tt>. </p>
<p> <i>Isn&#8217;t rxvt-unicode supposed to be small? Don&#8217;t all those features bloat?</i> </p>
<p> I often get asked about this, and I think, no, they didn&#8217;t cause extra bloat. If you compare a minimal rxvt and a minimal urxvt, you can see that the urxvt binary is larger (due to some encoding tables always being compiled in), but it actually uses less memory (<font SIZE="-1">RSS</font>) after startup. Even with <tt>&quot;--disable-everything&quot;</tt>, this comparison is a bit unfair, as many features unique to urxvt (locale, encoding conversion, iso14755 etc.) are already in use in this mode. </p>
<pre> text data bss drs rss filename
 98398 1664 24 15695 1824 rxvt --disable-everything
 188985 9048 66616 18222 1788 urxvt --disable-everything</pre>
<p>When you <tt>&quot;--enable-everything&quot;</tt> (which <i>is</i> unfair, as this involves xft and full locale/XIM support which are quite bloaty inside libX11 and my libc), the two diverge, but not unreasonably so. </p>
<pre> text data bss drs rss filename
 163431 2152 24 20123 2060 rxvt --enable-everything
 1035683 49680 66648 29096 3680 urxvt --enable-everything</pre>
<p>The very large size of the text section is explained by the east-asian encoding tables, which, if unused, take up disk space but nothing else and can be compiled out unless you rely on X11 core fonts that use those encodings. The <font SIZE="-1">BSS</font> size comes from the 64k emergency buffer that my c++ compiler allocates (but of course doesn&#8217;t use unless you are out of memory). Also, using an xft font instead of a core font immediately adds a few megabytes of <font SIZE="-1">RSS.</font> Xft indeed is responsible for a lot of <font SIZE="-1">RSS</font> even when not used. </p>
<p> Of course, due to every character using two or four bytes instead of one, a large scrollback buffer will ultimately make rxvt-unicode use more memory. </p>
<p> Compared to e.g. Eterm (5112k), aterm (3132k) and xterm (4680k), this still fares rather well. And compared to some monsters like gnome-terminal (21152k + extra 4204k in separate processes) or konsole (22200k + extra 43180k in daemons that stay around after exit, plus half a minute of startup time, including the hundreds of warnings it spits out), it fares extremely well *g*. </p>
<p> <i>Why C<font SIZE="-2">++</font>, isn&#8217;t that unportable/bloated/uncool?</i> </p>
<p> Is this a question? :) It comes up very often. The simple answer is: I had to write it, and C<font SIZE="-2">++</font> allowed me to write and maintain it in a fraction of the time and effort (which is a scarce resource for me). Put even shorter: It simply wouldn&#8217;t exist without C<font SIZE="-2">++</font>. </p>
<p> My personal stance on this is that C<font SIZE="-2">++</font> is less portable than C, but in the case of rxvt-unicode this hardly matters, as its portability limits are defined by things like X11, pseudo terminals, locale support and unix domain sockets, which are all less portable than C<font SIZE="-2">++</font> itself. </p>
<p> Regarding the bloat, see the above question: It&#8217;s easy to write programs in C that use gobs of memory, and certainly possible to write programs in C<font SIZE="-2">++</font> that don&#8217;t. C<font SIZE="-2">++</font> also often comes with large libraries, but this is not necessarily the case with <font SIZE="-1">GCC.</font> Here is what rxvt links against on my system with a minimal config: </p>
<pre> libX11.so.6 =&gt; /usr/X11R6/lib/libX11.so.6 (0x00002aaaaabc3000)
 libc.so.6 =&gt; /lib/libc.so.6 (0x00002aaaaadde000)
 libdl.so.2 =&gt; /lib/libdl.so.2 (0x00002aaaab01d000)
 /lib64/ld-linux-x86-64.so.2 (0x00002aaaaaaab000)</pre>
<p>And here is rxvt-unicode: </p>
<pre> libX11.so.6 =&gt; /usr/X11R6/lib/libX11.so.6 (0x00002aaaaabc3000)
 libgcc_s.so.1 =&gt; /lib/libgcc_s.so.1 (0x00002aaaaada2000)
 libc.so.6 =&gt; /lib/libc.so.6 (0x00002aaaaaeb0000)
 libdl.so.2 =&gt; /lib/libdl.so.2 (0x00002aaaab0ee000)
 /lib64/ld-linux-x86-64.so.2 (0x00002aaaaaaab000)</pre>
<p>No large bloated libraries (of course, none were linked in statically), except maybe libX11 :)</p>
<h3>Rendering, Font &amp; Look and Feel Issues</h3>
<p><i>I can&#8217;t get transparency working, what am I doing wrong?</i> </p>
<p> First of all, transparency isn&#8217;t officially supported in rxvt-unicode, so you are mostly on your own. Do not bug the author about it (but you may bug everybody else). Also, if you can&#8217;t get it working consider it a rite of passage: &#8230; and you failed. </p>
<p> Here are four ways to get transparency. <code>Do</code> read the manpage and option descriptions for the programs mentioned and rxvt-unicode. Really, do it! </p>
<p> 1. Use transparent mode: </p>
<pre> Esetroot wallpaper.jpg
 urxvt -tr -tint red -sh 40</pre>
<p>That works. If you think it doesn&#8217;t, you lack transparency and tinting support, or you are unable to read. This method requires that the background-setting program sets the _XROOTPMAP_ID or <font SIZE="-1">ESETROOT_PMAP_ID</font> property. Compatible programs are Esetroot, hsetroot and feh. </p>
<p> 2. Use a simple pixmap and emulate pseudo-transparency. This enables you to use effects other than tinting and shading: Just shade/tint/whatever your picture with gimp or any other tool: </p>
<pre> convert wallpaper.jpg -blur 20x20 -modulate 30 background.jpg
 urxvt -pixmap &quot;background.jpg;:root&quot;</pre>
<p>That works. If you think it doesn&#8217;t, you lack GDK-PixBuf support, or you are unable to read. </p>
<p> 3. Use an <font SIZE="-1">ARGB</font> visual: </p>
<pre> urxvt -depth 32 -fg grey90 -bg rgba:0000/0000/4444/cccc</pre>
<p>This requires <font SIZE="-1">XFT</font> support, and the support of your X-server. If that doesn&#8217;t work for you, blame Xorg and Keith Packard. <font SIZE="-1">ARGB</font> visuals aren&#8217;t there yet, no matter what they claim. Rxvt-Unicode contains the necessary bugfixes and workarounds for Xft and Xlib to make it work, but that doesn&#8217;t mean that your <font SIZE="-1">WM</font> has the required kludges in place. </p>
<p> 4. Use xcompmgr and let it do the job: </p>
<pre> xprop -frame -f _NET_WM_WINDOW_OPACITY 32c \
 -set _NET_WM_WINDOW_OPACITY 0xc0000000</pre>
<p>Then click on a window you want to make transparent. Replace <tt>0xc0000000</tt> by other values to change the degree of opacity. If it doesn&#8217;t work and your server crashes, you got to keep the pieces. </p>
<p> <i>Why does rxvt-unicode sometimes leave pixel droppings?</i> </p>
<p> Most fonts were not designed for terminal use, which means that character size varies a lot. A font that is otherwise fine for terminal use might contain some characters that are simply too wide. Rxvt-unicode will avoid these characters. For characters that are just &#8220;a bit&#8221; too wide a special &#8220;careful&#8221; rendering mode is used that redraws adjacent characters. </p>
<p> All of this requires that fonts do not lie about character sizes, however: Xft fonts often draw glyphs larger than their acclaimed bounding box, and rxvt-unicode has no way of detecting this (the correct way is to ask for the character bounding box, which unfortunately is wrong in these cases). </p>
<p> It&#8217;s not clear (to me at least), whether this is a bug in Xft, freetype, or the respective font. If you encounter this problem you might try using the <tt>&quot;-lsp&quot;</tt> option to give the font more height. If that doesn&#8217;t work, you might be forced to use a different font. </p>
<p> All of this is not a problem when using X11 core fonts, as their bounding box data is correct. </p>
<p> <i>How can I keep rxvt-unicode from using reverse video so much?</i> </p>
<p> First of all, make sure you are running with the right terminal settings (<tt>&quot;TERM=rxvt-unicode&quot;</tt>), which will get rid of most of these effects. Then make sure you have specified colours for italic and bold, as otherwise rxvt-unicode might use reverse video to simulate the effect: </p>
<pre> URxvt.colorBD: white
 URxvt.colorIT: green</pre>
<p><i>Some programs assume totally weird colours (red instead of blue), how can I fix that?</i> </p>
<p> For some unexplainable reason, some rare programs assume a very weird colour palette when confronted with a terminal with more than the standard 8 colours (rxvt-unicode supports 88). The right fix is, of course, to fix these programs not to assume non-ISO colours without very good reasons. </p>
<p> In the meantime, you can either edit your <tt>&quot;rxvt-unicode&quot;</tt> terminfo definition to only claim 8 colour support or use <tt>&quot;TERM=rxvt&quot;</tt>, which will fix colours but keep you from using other rxvt-unicode features. </p>
<p> <i>Can I switch the fonts at runtime?</i> </p>
<p> Yes, using an escape sequence. Try something like this, which has the same effect as using the <tt>&quot;-fn&quot;</tt> switch, and takes effect immediately: </p>
<pre> printf '\33]50;%s' &quot;9x15bold,xft:Kochi Gothic&quot;</pre>
<p>This is useful if you e.g. work primarily with japanese (and prefer a japanese font), but you have to switch to chinese temporarily, where japanese fonts would only be in your way. </p>
<p> You can think of this as a kind of manual <font SIZE="-1">ISO-2022</font> switching. </p>
<p> <i>Why do italic characters look as if clipped?</i> </p>
<p> Many fonts have difficulties with italic characters and hinting. For example, the otherwise very nicely hinted font <tt>&quot;xft:Bitstream Vera Sans Mono&quot;</tt> completely fails in its italic face. A workaround might be to enable freetype autohinting, i.e. like this: </p>
<pre> URxvt.italicFont: xft:Bitstream Vera Sans Mono:italic:autohint=true
 URxvt.boldItalicFont: xft:Bitstream Vera Sans Mono:bold:italic:autohint=true</pre>
<p><i>Can I speed up Xft rendering somehow?</i> </p>
<p> Yes, the most obvious way to speed it up is to avoid Xft entirely, as it is simply slow. If you still want Xft fonts you might try to disable antialiasing (by appending <tt>&quot;:antialias=false&quot;</tt>), which saves lots of memory and also speeds up rendering considerably. </p>
<p> <i>Rxvt-unicode doesn&#8217;t seem to anti-alias its fonts, what is wrong?</i> </p>
<p> Rxvt-unicode will use whatever you specify as a font. If it needs to fall back to its default font search list it will prefer X11 core fonts, because they are small and fast, and then use Xft fonts. It has antialiasing disabled for most of them, because the author thinks they look best that way. </p>
<p> If you want antialiasing, you have to specify the fonts manually. </p>
<p> <i>What&#8217;s with this bold/blink stuff?</i> </p>
<p> If no bold colour is set via <tt>&quot;colorBD:&quot;</tt>, bold will invert text using the standard foreground colour. </p>
<p> For the standard background colour, blinking will actually make the text blink when compiled with <tt>&quot;--enable-text-blink&quot;</tt>. Without <tt>&quot;--enable-text-blink&quot;</tt>, the blink attribute will be ignored. </p>
<p> On <font SIZE="-1">ANSI</font> colours, bold/blink attributes are used to set high-intensity foreground/background colours. </p>
<p> color0-7 are the low-intensity colours. </p>
<p> color8-15 are the corresponding high-intensity colours. </p>
<p> <i>I don&#8217;t like the screen colours. How do I change them?</i> </p>
<p> You can change the screen colours at run-time using <i>~/.Xdefaults</i> resources (or as long-options). </p>
<p> Here are values that are supposed to resemble a <font SIZE="-1">VGA</font> screen, including the murky brown that passes for low-intensity yellow: </p>
<pre> URxvt.color0: #000000
 URxvt.color1: #A80000
 URxvt.color2: #00A800
 URxvt.color3: #A8A800
 URxvt.color4: #0000A8
 URxvt.color5: #A800A8
 URxvt.color6: #00A8A8
 URxvt.color7: #A8A8A8
 URxvt.color8: #000054
 URxvt.color9: #FF0054
 URxvt.color10: #00FF54
 URxvt.color11: #FFFF54
 URxvt.color12: #0000FF
 URxvt.color13: #FF00FF
 URxvt.color14: #00FFFF
 URxvt.color15: #FFFFFF</pre>
<p>And here is a more complete set of non-standard colours. </p>
<pre> URxvt.cursorColor: #dc74d1
 URxvt.pointerColor: #dc74d1
 URxvt.background: #0e0e0e
 URxvt.foreground: #4ad5e1
 URxvt.color0: #000000
 URxvt.color8: #8b8f93
 URxvt.color1: #dc74d1
 URxvt.color9: #dc74d1
 URxvt.color2: #0eb8c7
 URxvt.color10: #0eb8c7
 URxvt.color3: #dfe37e
 URxvt.color11: #dfe37e
 URxvt.color5: #9e88f0
 URxvt.color13: #9e88f0
 URxvt.color6: #73f7ff
 URxvt.color14: #73f7ff
 URxvt.color7: #e1dddd
 URxvt.color15: #e1dddd</pre>
<p>They have been described (not by me) as &#8220;pretty girly&#8221;. </p>
<p> <i>Why do some characters look so much different than others?</i> </p>
<p> See next entry. </p>
<p> <i>How does rxvt-unicode choose fonts?</i> </p>
<p> Most fonts do not contain the full range of Unicode, which is fine. Chances are that the font you (or the admin/package maintainer of your system/os) have specified does not cover all the characters you want to display. </p>
<p> <code>rxvt-unicode</code> makes a best-effort try at finding a replacement font. Often the result is fine, but sometimes the chosen font looks bad/ugly/wrong. Some fonts have totally strange characters that don&#8217;t resemble the correct glyph at all, and rxvt-unicode lacks the artificial intelligence to detect that a specific glyph is wrong: it has to believe the font that the characters it claims to contain indeed look correct. </p>
<p> In that case, select a font of your taste and add it to the font list, e.g.: </p>
<pre> urxvt -fn basefont,font2,font3...</pre>
<p>When rxvt-unicode sees a character, it will first look at the base font. If the base font does not contain the character, it will go to the next font, and so on. Specifying your own fonts will also speed up this search and use less resources within rxvt-unicode and the X-server. </p>
<p> The only limitation is that none of the fonts may be larger than the base font, as the base font defines the terminal character cell size, which must be the same due to the way terminals work. </p>
<p> <i>Why do some chinese characters look so different than others?</i> </p>
<p> This is because there is a difference between script and language &#8212; rxvt-unicode does not know which language the text that is output is, as it only knows the unicode character codes. If rxvt-unicode first sees a japanese/chinese character, it might choose a japanese font for display. Subsequent japanese characters will use that font. Now, many chinese characters aren&#8217;t represented in japanese fonts, so when the first non-japanese character comes up, rxvt-unicode will look for a chinese font &#8212; unfortunately at this point, it will still use the japanese font for chinese characters that are also in the japanese font. </p>
<p> The workaround is easy: just tag a chinese font at the end of your font list (see the previous question). The key is to view the font list as a preference list: If you expect more japanese, list a japanese font first. If you expect more chinese, put a chinese font first. </p>
<p> In the future it might be possible to switch language preferences at runtime (the internal data structure has no problem with using different fonts for the same character at the same time, but no interface for this has been designed yet). </p>
<p> Until then, you might get away with switching fonts at runtime (see &#8220;Can I switch the fonts at runtime?&#8221; later in this document). </p>
<p> <i>How can I make mplayer display video correctly?</i> </p>
<p> We are working on it, in the meantime, as a workaround, use something like: </p>
<pre> urxvt -b 600 -geometry 20x1 -e sh -c 'mplayer -wid $WINDOWID file...'</pre>
<p><i>Why is the cursor now blinking in emacs/vi/&#8230;?</i> </p>
<p> This is likely caused by your editor/program&#8217;s use of the <tt>&quot;cvvis&quot;</tt> terminfo capability. Emacs uses it by default, as well as some versions of vi and possibly other programs. </p>
<p> In emacs, you can switch that off by adding this to your <tt>&quot;.emacs&quot;</tt> file: </p>
<pre> (setq visible-cursor nil)</pre>
<p>For other programs, if they do not have an option, your have to remove the <tt>&quot;cvvis&quot;</tt> capability from the terminfo description. </p>
<p> When urxvt first added the blinking cursor option, it didn&#8217;t add a <tt>&quot;cvvis&quot;</tt> capability, which served no purpose before. Version 9.21 introduced <tt>&quot;cvvis&quot;</tt> (and the ability to control blinking independent of cursor shape) for compatibility with other terminals, which traditionally use a blinking cursor for <tt>&quot;cvvis&quot;</tt>. This also reflects the intent of programs such as emacs, who expect <tt>&quot;cvvis&quot;</tt> to enable a blinking cursor.</p>
<h3>Keyboard, Mouse &amp; User Interaction</h3>
<p><i>The new selection selects pieces that are too big, how can I select single words?</i> </p>
<p> If you want to select e.g. alphanumeric words, you can use the following setting: </p>
<pre> URxvt.selection.pattern-0: ([[:word:]]+)</pre>
<p>If you click more than twice, the selection will be extended more and more. </p>
<p> To get a selection that is very similar to the old code, try this pattern: </p>
<pre> URxvt.selection.pattern-0: ([^&quot;&amp;'()*,;&lt;=&gt;?@[\\]^`{|})]+)</pre>
<p>Please also note that the <i>LeftClick Shift-LeftClick</i> combination also selects words like the old code. </p>
<p> <i>I don&#8217;t like the new selection/popups/hotkeys/perl, how do I change/disable it?</i> </p>
<p> You can disable the perl extension completely by setting the <code>perl-ext-common</code> resource to the empty string, which also keeps rxvt-unicode from initialising perl, saving memory. </p>
<p> If you only want to disable specific features, you first have to identify which perl extension is responsible. For this, read the section <font SIZE="-1"><code>PREPACKAGED EXTENSIONS</code></font> in the urxvt<i><a href="/docs/linux/man/3-perl/">perl</a></i>(3) manpage. For example, to disable the <code>selection-popup</code> and <code>option-popup</code>, specify this <code>perl-ext-common</code> resource: </p>
<pre> URxvt.perl-ext-common: default,-selection-popup,-option-popup</pre>
<p>This will keep the default extensions, but disable the two popup extensions. Some extensions can also be configured, for example, scrollback search mode is triggered by <code>M-s</code>. You can move it to any other combination either by setting the <code>searchable-scrollback</code> resource: </p>
<pre> URxvt.searchable-scrollback: CM-s</pre>
<p><i>The cursor moves when selecting text in the current input line, how do I switch this off?</i> </p>
<p> See next entry. </p>
<p> <i>During rlogin/ssh/telnet/etc. sessions, clicking near the cursor outputs strange escape sequences, how do I fix this?</i> </p>
<p> These are caused by the <tt>&quot;readline&quot;</tt> perl extension. Under normal circumstances, it will move your cursor around when you click into the line that contains it. It tries hard not to do this at the wrong moment, but when running a program that doesn&#8217;t parse cursor movements or in some cases during rlogin sessions, it fails to detect this properly. </p>
<p> You can permanently switch this feature off by disabling the <tt>&quot;readline&quot;</tt> extension: </p>
<pre> URxvt.perl-ext-common: default,-readline</pre>
<p><i>My numeric keypad acts weird and generates differing output?</i> </p>
<p> Some Debian GNU/Linux users seem to have this problem, although no specific details were reported so far. It is possible that this is caused by the wrong <tt>&quot;TERM&quot;</tt> setting, although the details of whether and how this can happen are unknown, as <tt>&quot;TERM=rxvt&quot;</tt> should offer a compatible keymap. See the answer to the previous question, and please report if that helped. </p>
<p> <i>My Compose (Multi_key) key is no longer working.</i> </p>
<p> The most common causes for this are that either your locale is not set correctly, or you specified a <code>preeditType</code> that is not supported by your input method. For example, if you specified <code>OverTheSpot</code> and your input method (e.g. the default input method handling Compose keys) does not support this (for instance because it is not visual), then rxvt-unicode will continue without an input method. </p>
<p> In this case either do not specify a <code>preeditType</code> or specify more than one pre-edit style, such as <code>OverTheSpot,Root,None</code>. </p>
<p> If it still doesn&#8217;t work, then maybe your input method doesn&#8217;t support compose sequences &#8211; to fall back to the built-in one, make sure you don&#8217;t specify an input method via <tt>&quot;-im&quot;</tt> or <tt>&quot;XMODIFIERS&quot;</tt>. </p>
<p> <i>I cannot type </i>&quot;Ctrl-Shift-2&quot;<i> to get an </i><font SIZE="-1"><i>ASCII NUL</i></font><i> character due to </i><font SIZE="-1"><i>ISO 14755</i></font><i></i> </p>
<p> Either try <tt>&quot;Ctrl-2&quot;</tt> alone (it often is mapped to <font SIZE="-1">ASCII NUL</font> even on international keyboards) or simply use <font SIZE="-1">ISO 14755</font> support to your advantage, typing &lt;Ctrl-Shift-0&gt; to get a <font SIZE="-1">ASCII NUL.</font> This works for other codes, too, such as <tt>&quot;Ctrl-Shift-1-d&quot;</tt> to type the default telnet escape character and so on. </p>
<p> <i>Mouse cut/paste suddenly no longer works.</i> </p>
<p> Make sure that mouse reporting is actually turned off since killing some editors prematurely may leave it active. I&#8217;ve heard that tcsh may use mouse reporting unless it is otherwise specified. A quick check is to see if cut/paste works when the Alt or Shift keys are pressed. </p>
<p> <i>What&#8217;s with the strange Backspace/Delete key behaviour?</i> </p>
<p> Assuming that the physical Backspace key corresponds to the Backspace keysym (not likely for Linux &#8230; see the following question) there are two standard values that can be used for Backspace: <tt>&quot;^H&quot;</tt> and <tt>&quot;^?&quot;</tt>. </p>
<p> Historically, either value is correct, but rxvt-unicode adopts the debian policy of using <tt>&quot;^?&quot;</tt> when unsure, because it&#8217;s the one and only correct choice :). </p>
<p> It is possible to toggle between <tt>&quot;^H&quot;</tt> and <tt>&quot;^?&quot;</tt> with the <font SIZE="-1">DECBKM</font> private mode: </p>
<pre> # use Backspace = ^H
 $ stty erase ^H
 $ printf &quot;[?67h&quot;
 # use Backspace = ^?
 $ stty erase ^?
 $ printf &quot;[?67l&quot;</pre>
<p>This helps satisfy some of the Backspace discrepancies that occur, but if you use Backspace = <tt>&quot;^H&quot;</tt>, make sure that the termcap/terminfo value properly reflects that. </p>
<p> The Delete key is a another casualty of the ill-defined Backspace problem. To avoid confusion between the Backspace and Delete keys, the Delete key has been assigned an escape sequence to match the vt100 for Execute (<tt>&quot;ESC [ 3 ~&quot;</tt>) and is in the supplied termcap/terminfo. </p>
<p> Some other Backspace problems: </p>
<p> some editors use termcap/terminfo, some editors (vim I&#8217;m told) expect Backspace = ^H, <font SIZE="-1">GNU</font> Emacs (and Emacs-like editors) use ^H for help. </p>
<p> Perhaps someday this will all be resolved in a consistent manner. </p>
<p> <i>I don&#8217;t like the key-bindings. How do I change them?</i> </p>
<p> There are some compile-time selections available via configure. Unless you have run &#8220;configure&#8221; with the <tt>&quot;--disable-resources&quot;</tt> option you can use the `keysym&#8217; resource to alter the keystrings associated with keysyms. </p>
<p> Here&#8217;s an example for a URxvt session started using <tt>&quot;urxvt -name URxvt&quot;</tt> </p>
<pre> URxvt.keysym.Prior: [5~
 URxvt.keysym.Next: [6~
 URxvt.keysym.Home: [7~
 URxvt.keysym.End: [8~
 URxvt.keysym.Up: [A
 URxvt.keysym.Down: [B
 URxvt.keysym.Right: [C
 URxvt.keysym.Left: [D</pre>
<p>See some more examples in the documentation for the <code>keysym</code> resource. </p>
<p> <i>I&#8217;m using keyboard model </i><font SIZE="-1"><i>XXX</i></font><i> that has extra Prior/Next/Insert keys. How do I make use of them? For example, the Sun Keyboard type 4 has the following map</i> </p>
<pre> KP_Insert == Insert
 F22 == Print
 F27 == Home
 F29 == Prior
 F33 == End
 F35 == Next</pre>
<p>Rather than have rxvt-unicode try to accommodate all the various possible keyboard mappings, it is better to use `xmodmap&#8217; to remap the keys as required for your particular machine.</p>
<h3>Terminal Configuration</h3>
<p><i>Can I see a typical configuration?</i> </p>
<p> The default configuration tries to be xterm-like, which I don&#8217;t like that much, but it&#8217;s least surprise to regular users. </p>
<p> As a rxvt or rxvt-unicode user, you are practically supposed to invest time into customising your terminal. To get you started, here is the author&#8217;s .Xdefaults entries, with comments on what they do. It&#8217;s certainly not <i>typical</i>, but what&#8217;s typical&#8230; </p>
<pre> URxvt.cutchars: &quot;()*,&lt;&gt;[]{}|'
 URxvt.print-pipe: cat &gt;/tmp/xxx</pre>
<p>These are just for testing stuff. </p>
<pre> URxvt.imLocale: ja_JP.UTF-8
 URxvt.preeditType: OnTheSpot,None</pre>
<p>This tells rxvt-unicode to use a special locale when communicating with the X Input Method, and also tells it to only use the OnTheSpot pre-edit type, which requires the <tt>&quot;xim-onthespot&quot;</tt> perl extension but rewards me with correct-looking fonts. </p>
<pre> URxvt.perl-lib: /root/lib/urxvt
 URxvt.perl-ext-common: default,selection-autotransform,selection-pastebin,xim-onthespot,remote-clipboard
 URxvt.selection.pattern-0: ( at .*? line \d+)
 URxvt.selection.pattern-1: ^(/[^:]+):\ 
 URxvt.selection-autotransform.0: s/^([^:[:space:]]+):(\d+):?$/:e \Q$1\E\x0d:$2\x0d/
 URxvt.selection-autotransform.1: s/^ at (.*?) line (\d+)$/:e \Q$1\E\x0d:$2\x0d/</pre>
<p>This is my perl configuration. The first two set the perl library directory and also tells urxvt to use a large number of extensions. I develop for myself mostly, so I actually use most of the extensions I write. </p>
<p> The selection stuff mainly makes the selection perl-error-message aware and tells it to convert perl error messages into vi-commands to load the relevant file and go to the error line number. </p>
<pre> URxvt.scrollstyle: plain
 URxvt.secondaryScroll: true</pre>
<p>As the documentation says: plain is the preferred scrollbar for the author. The <tt>&quot;secondaryScroll&quot;</tt> configures urxvt to scroll in full-screen apps, like screen, so lines scrolled out of screen end up in urxvt&#8217;s scrollback buffer. </p>
<pre> URxvt.background: #000000
 URxvt.foreground: gray90
 URxvt.color7: gray90
 URxvt.colorBD: #ffffff
 URxvt.cursorColor: #e0e080
 URxvt.throughColor: #8080f0
 URxvt.highlightColor: #f0f0f0</pre>
<p>Some colours. Not sure which ones are being used or even non-defaults, but these are in my .Xdefaults. Most notably, they set foreground/background to light gray/black, and also make sure that the colour 7 matches the default foreground colour. </p>
<pre> URxvt.underlineColor: yellow</pre>
<p>Another colour, makes underline lines look different. Sometimes hurts, but is mostly a nice effect. </p>
<pre> URxvt.geometry: 154x36
 URxvt.loginShell: false
 URxvt.meta: ignore
 URxvt.utmpInhibit: true</pre>
<p>Uh, well, should be mostly self-explanatory. By specifying some defaults manually, I can quickly switch them for testing. </p>
<pre> URxvt.saveLines: 8192</pre>
<p>A large scrollback buffer is essential. Really. </p>
<pre> URxvt.mapAlert: true</pre>
<p>The only case I use it is for my <font SIZE="-1">IRC</font> window, which I like to keep iconified till people msg me (which beeps). </p>
<pre> URxvt.visualBell: true</pre>
<p>The audible bell is often annoying, especially when in a crowd. </p>
<pre> URxvt.insecure: true</pre>
<p>Please don&#8217;t hack my mutt! Ooops&#8230; </p>
<pre> URxvt.pastableTabs: false</pre>
<p>I once thought this is a great idea. </p>
<pre> urxvt.font: 9x15bold,\
 -misc-fixed-bold-r-normal--15-140-75-75-c-90-iso10646-1,\
 -misc-fixed-medium-r-normal--15-140-75-75-c-90-iso10646-1, \
 [codeset=JISX0208]xft:Kochi Gothic, \
 xft:Bitstream Vera Sans Mono:autohint=true, \
 xft:Code2000:antialias=false
 urxvt.boldFont: -xos4-terminus-bold-r-normal--14-140-72-72-c-80-iso8859-15
 urxvt.italicFont: xft:Bitstream Vera Sans Mono:italic:autohint=true
 urxvt.boldItalicFont: xft:Bitstream Vera Sans Mono:bold:italic:autohint=true</pre>
<p>I wrote rxvt-unicode to be able to specify fonts exactly. So don&#8217;t be overwhelmed. A special note: the <tt>&quot;9x15bold&quot;</tt> mentioned above is actually the version from XFree-3.3, as XFree-4 replaced it by a totally different font (different glyphs for <tt>&quot;;&quot;</tt> and many other harmless characters), while the second font is actually the <tt>&quot;9x15bold&quot;</tt> from XFree4/XOrg. The bold version has less chars than the medium version, so I use it for rare characters, too. When editing sources with vim, I use italic for comments and other stuff, which looks quite good with Bitstream Vera anti-aliased. </p>
<p> Terminus is a quite bad font (many very wrong glyphs), but for most of my purposes, it works, and gives a different look, as my normal (Non-bold) font is already bold, and I want to see a difference between bold and normal fonts. </p>
<p> Please note that I used the <tt>&quot;urxvt&quot;</tt> instance name and not the <tt>&quot;URxvt&quot;</tt> class name. That is because I use different configs for different purposes, for example, my <font SIZE="-1">IRC</font> window is started with <tt>&quot;-name IRC&quot;</tt>, and uses these defaults: </p>
<pre> IRC*title: IRC
 IRC*geometry: 87x12+535+542
 IRC*saveLines: 0
 IRC*mapAlert: true
 IRC*font: suxuseuro
 IRC*boldFont: suxuseuro
 IRC*colorBD: white
 IRC*keysym.M-C-1: command:]710;suxuseuro]711;suxuseuro
 IRC*keysym.M-C-2: command:]710;9x15bold]711;9x15bold</pre>
<p><tt>&quot;Alt-Ctrl-1&quot;</tt> and <tt>&quot;Alt-Ctrl-2&quot;</tt> switch between two different font sizes. <tt>&quot;suxuseuro&quot;</tt> allows me to keep an eye (and actually read) stuff while keeping a very small window. If somebody pastes something complicated (e.g. japanese), I temporarily switch to a larger font. </p>
<p> The above is all in my <tt>&quot;.Xdefaults&quot;</tt> (I don&#8217;t use <tt>&quot;.Xresources&quot;</tt> nor <tt>&quot;xrdb&quot;</tt>). I also have some resources in a separate <tt>&quot;.Xdefaults-hostname&quot;</tt> file for different hosts, for example, on my main desktop, I use: </p>
<pre> URxvt.keysym.C-M-q: command:[3;5;5t
 URxvt.keysym.C-M-y: command:[3;5;606t
 URxvt.keysym.C-M-e: command:[3;1605;5t
 URxvt.keysym.C-M-c: command:[3;1605;606t
 URxvt.keysym.C-M-p: perl:test</pre>
<p>The first for keysym definitions allow me to quickly bring some windows in the layout I like most. Ion users might start laughing but will stop immediately when I tell them that I use my own Fvwm2 module for much the same effect as Ion provides, and I only very rarely use the above key combinations :-&gt; </p>
<p> <i>Why doesn&#8217;t rxvt-unicode read my resources?</i> </p>
<p> Well, why, indeed? It does, in a way very similar to other X applications. Most importantly, this means that if you or your <font SIZE="-1">OS</font> loads resources into the X display (the right way to do it), rxvt-unicode will ignore any resource files in your home directory. It will only read <i></i>$HOME<i>/.Xdefaults</i> when no resources are attached to the display. </p>
<p> If you have or use an <i></i>$HOME<i>/.Xresources</i> file, chances are that resources are loaded into your X-server. In this case, you have to re-login after every change (or run <i>xrdb -merge </i>$HOME<i>/.Xresources</i>). </p>
<p> Also consider the form resources have to use: </p>
<pre> URxvt.resource: value</pre>
<p>If you want to use another form (there are lots of different ways of specifying resources), make sure you understand whether and why it works. If unsure, use the form above. </p>
<p> <i>When I log-in to another system it tells me about missing terminfo data?</i> </p>
<p> The terminal description used by rxvt-unicode is not as widely available as that for xterm, or even rxvt (for which the same problem often arises). </p>
<p> The correct solution for this problem is to install the terminfo, this can be done by simply installing rxvt-unicode on the remote system as well (in case you have a nice package manager ready), or you can install the terminfo database manually like this (with ncurses infocmp. works as user and root): </p>
<pre> REMOTE=remotesystem.domain
 infocmp rxvt-unicode | ssh $REMOTE &quot;mkdir -p .terminfo &amp;&amp; cat &gt;/tmp/ti &amp;&amp; tic /tmp/ti&quot;</pre>
<p>One some systems you might need to set <tt>$TERMINFO</tt> to the full path of <i></i>$HOME<i>/.terminfo</i> for this to work. </p>
<p> If you cannot or do not want to do this, then you can simply set <tt>&quot;TERM=rxvt&quot;</tt> or even <tt>&quot;TERM=xterm&quot;</tt>, and live with the small number of problems arising, which includes wrong keymapping, less and different colours and some refresh errors in fullscreen applications. It&#8217;s a nice quick-and-dirty workaround for rare cases, though. </p>
<p> If you always want to do this (and are fine with the consequences) you can either recompile rxvt-unicode with the desired <font SIZE="-1">TERM</font> value or use a resource to set it: </p>
<pre> URxvt.termName: rxvt</pre>
<p>If you don&#8217;t plan to use <code>rxvt</code> (quite common&#8230;) you could also replace the rxvt terminfo file with the rxvt-unicode one and use <tt>&quot;TERM=rxvt&quot;</tt>. </p>
<p> <i>nano fails with &#8220;Error opening terminal: rxvt-unicode&#8221;</i> </p>
<p> This exceptionally confusing and useless error message is printed by nano when it can&#8217;t find the terminfo database. Nothing is wrong with your terminal, read the previous answer for a solution. </p>
<p> <i></i>&quot;tic&quot;<i> outputs some error when compiling the terminfo entry.</i> </p>
<p> Most likely it&#8217;s the empty definition for <tt>&quot;enacs=&quot;</tt>. Just replace it by <tt>&quot;enacs=\E[0@&quot;</tt> and try again. </p>
<p> <i></i>&quot;bash&quot;<i>&#8216;s readline does not work correctly under urxvt.</i> </p>
<p> See next entry. </p>
<p> <i>I need a termcap file entry.</i> </p>
<p> One reason you might want this is that some distributions or operating systems still compile some programs using the long-obsoleted termcap library (Fedora Core&#8217;s bash is one example) and rely on a termcap entry for <tt>&quot;rxvt-unicode&quot;</tt>. </p>
<p> You could use rxvt&#8217;s termcap entry with reasonable results in many cases. You can also create a termcap entry by using terminfo&#8217;s infocmp program like this: </p>
<pre> infocmp -C rxvt-unicode</pre>
<p>Or you could use the termcap entry in doc/etc/rxvt-unicode.termcap, generated by the command above. </p>
<p> <i>Why does </i>&quot;ls&quot;<i> no longer have coloured output?</i> </p>
<p> The <tt>&quot;ls&quot;</tt> in the <font SIZE="-1">GNU</font> coreutils unfortunately doesn&#8217;t use terminfo to decide whether a terminal has colour, but uses its own configuration file. Needless to say, <tt>&quot;rxvt-unicode&quot;</tt> is not in its default file (among with most other terminals supporting colour). Either add: </p>
<pre> TERM rxvt-unicode</pre>
<p>to <tt>&quot;/etc/DIR_COLORS&quot;</tt> or simply add: </p>
<pre> alias ls='ls --color=auto'</pre>
<p>to your <tt>&quot;.profile&quot;</tt> or <tt>&quot;.bashrc&quot;</tt>. </p>
<p> <i>Why doesn&#8217;t vim/emacs etc. use the 88 colour mode?</i> </p>
<p> See next entry. </p>
<p> <i>Why doesn&#8217;t vim/emacs etc. make use of italic?</i> </p>
<p> See next entry. </p>
<p> <i>Why are the secondary screen-related options not working properly?</i> </p>
<p> Make sure you are using <tt>&quot;TERM=rxvt-unicode&quot;</tt>. Some pre-packaged distributions break rxvt-unicode by setting <tt>&quot;TERM&quot;</tt> to <tt>&quot;rxvt&quot;</tt>, which doesn&#8217;t have these extra features. Unfortunately, some of these furthermore fail to even install the <tt>&quot;rxvt-unicode&quot;</tt> terminfo file, so you will need to install it on your own (See the question <code>When I log-in to another system it tells me about missing terminfo data?</code> on how to do this).</p>
<h3>Encoding / Locale / Input Method Issues</h3>
<p><i>Rxvt-unicode does not seem to understand the selected encoding?</i> </p>
<p> See next entry. </p>
<p> <i>Unicode does not seem to work?</i> </p>
<p> If you encounter strange problems like typing an accented character but getting two unrelated other characters or similar, or if program output is subtly garbled, then you should check your locale settings. </p>
<p> Rxvt-unicode must be started with the same <tt>&quot;LC_CTYPE&quot;</tt> setting as the programs running in it. Often rxvt-unicode is started in the <tt>&quot;C&quot;</tt> locale, while the login script running within the rxvt-unicode window changes the locale to something else, e.g. <tt>&quot;en_GB.UTF-8&quot;</tt>. Needless to say, this is not going to work, and is the most common cause for problems. </p>
<p> The best thing is to fix your startup environment, as you will likely run into other problems. If nothing works you can try this in your .profile. </p>
<pre> printf '\33]701;%s' &quot;$LC_CTYPE&quot; # $LANG or $LC_ALL are worth a try, too</pre>
<p>If this doesn&#8217;t work, then maybe you use a <tt>&quot;LC_CTYPE&quot;</tt> specification not supported on your systems. Some systems have a <tt>&quot;locale&quot;</tt> command which displays this (also, <tt>&quot;perl -e0&quot;</tt> can be used to check locale settings, as it will complain loudly if it cannot set the locale). If it displays something like: </p>
<pre> locale: Cannot set LC_CTYPE to default locale: ...</pre>
<p>Then the locale you specified is not supported on your system. </p>
<p> If nothing works and you are sure that everything is set correctly then you will need to remember a little known fact: Some programs just don&#8217;t support locales :( </p>
<p> <i>How does rxvt-unicode determine the encoding to use?</i> </p>
<p> See next entry. </p>
<p> <i>Is there an option to switch encodings?</i> </p>
<p> Unlike some other terminals, rxvt-unicode has no encoding switch, and no specific &#8220;utf-8&#8221; mode, such as xterm. In fact, it doesn&#8217;t even know about <font SIZE="-1">UTF-8</font> or any other encodings with respect to terminal I/O. </p>
<p> The reasons is that there exists a perfectly fine mechanism for selecting the encoding, doing I/O and (most important) communicating this to all applications so everybody agrees on character properties such as width and code number. This mechanism is the <i>locale</i>. Applications not using that info will have problems (for example, <tt>&quot;xterm&quot;</tt> gets the width of characters wrong as it uses its own, locale-independent table under all locales). </p>
<p> Rxvt-unicode uses the <tt>&quot;LC_CTYPE&quot;</tt> locale category to select encoding. All programs doing the same (that is, most) will automatically agree in the interpretation of characters. </p>
<p> Unfortunately, there is no system-independent way to select locales, nor is there a standard on how locale specifiers will look like. </p>
<p> On most systems, the content of the <tt>&quot;LC_CTYPE&quot;</tt> environment variable contains an arbitrary string which corresponds to an already-installed locale. Common names for locales are <tt>&quot;en_US.UTF-8&quot;</tt>, <tt>&quot;de_DE.ISO-8859-15&quot;</tt>, <tt>&quot;ja_JP.EUC-JP&quot;</tt>, i.e. <tt>&quot;language_country.encoding&quot;</tt>, but other forms (i.e. <tt>&quot;de&quot;</tt> or <tt>&quot;german&quot;</tt>) are also common. </p>
<p> Rxvt-unicode ignores all other locale categories, and except for the encoding, ignores country or language-specific settings, i.e. <tt>&quot;de_DE.UTF-8&quot;</tt> and <tt>&quot;ja_JP.UTF-8&quot;</tt> are the normally same to rxvt-unicode. </p>
<p> If you want to use a specific encoding you have to make sure you start rxvt-unicode with the correct <tt>&quot;LC_CTYPE&quot;</tt> category. </p>
<p> <i>Can I switch locales at runtime?</i> </p>
<p> Yes, using an escape sequence. Try something like this, which sets rxvt-unicode&#8217;s idea of <tt>&quot;LC_CTYPE&quot;</tt>. </p>
<pre> printf '\33]701;%s' ja_JP.SJIS</pre>
<p>See also the previous answer. </p>
<p> Sometimes this capability is rather handy when you want to work in one locale (e.g. <tt>&quot;de_DE.UTF-8&quot;</tt>) but some programs don&#8217;t support it (e.g. <font SIZE="-1">UTF-8</font>). For example, I use this script to start <tt>&quot;xjdic&quot;</tt>, which first switches to a locale supported by xjdic and back later: </p>
<pre> printf '\33]701;%s' ja_JP.SJIS
 xjdic -js
 printf '\33]701;%s' de_DE.UTF-8</pre>
<p>You can also use xterm&#8217;s <tt>&quot;luit&quot;</tt> program, which usually works fine, except for some locales where character width differs between program- and rxvt-unicode-locales. </p>
<p> <i>I have problems getting my input method working.</i> </p>
<p> Try a search engine, as this is slightly different for every input method server. </p>
<p> Here is a checklist:</p>
<dl>
<dt>&#8211; Make sure your locale <i>and</i> the imLocale are supported on your <font SIZE="-1">OS.</font></p>
<dd>Try <tt>&quot;locale -a&quot;</tt> or check the documentation for your <font SIZE="-1">OS.</font></p>
<dt>&#8211; Make sure your locale or imLocale matches a locale supported by your <font SIZE="-1">XIM.</font></p>
<dd>For example, <code>kinput2</code> does not support <font SIZE="-1">UTF-8</font> locales, you should use <tt>&quot;ja_JP.EUC-JP&quot;</tt> or equivalent.</p>
<dt>&#8211; Make sure your <font SIZE="-1">XIM</font> server is actually running.</p>
<dd>
<dt>&#8211; Make sure the &quot;XMODIFIERS&quot; environment variable is set correctly when <i>starting</i> rxvt-unicode.</p>
<dd>When you want to use e.g. <code>kinput2</code>, it must be set to <tt>&quot;@im=kinput2&quot;</tt>. For <code>scim</code>, use <tt>&quot;@im=SCIM&quot;</tt>. You can see what input method servers are running with this command: </p>
<pre> xprop -root XIM_SERVERS</pre>
</dl>
<p> <i>My input method wants &lt;some encoding&gt; but I want </i><font SIZE="-1"><i>UTF-8,</i></font><i> what can I do?</i> </p>
<p> You can specify separate locales for the input method and the rest of the terminal, using the resource <tt>&quot;imlocale&quot;</tt>: </p>
<pre> URxvt.imlocale: ja_JP.EUC-JP</pre>
<p>Now you can start your terminal with <tt>&quot;LC_CTYPE=ja_JP.UTF-8&quot;</tt> and still use your input method. Please note, however, that, depending on your Xlib version, you may not be able to input characters outside <tt>&quot;EUC-JP&quot;</tt> in a normal way then, as your input method limits you. </p>
<p> <i>Rxvt-unicode crashes when the X Input Method changes or exits.</i> </p>
<p> Unfortunately, this is unavoidable, as the <font SIZE="-1">XIM</font> protocol is racy by design. Applications can avoid some crashes at the expense of memory leaks, and Input Methods can avoid some crashes by careful ordering at exit time. <code>kinput2</code> (and derived input methods) generally succeeds, while <font SIZE="-1"><code>SCIM</code></font> (or similar input methods) fails. In the end, however, crashes cannot be completely avoided even if both sides cooperate. </p>
<p> So the only workaround is not to kill your Input Method Servers.</p>
<h3>Operating Systems / Package Maintaining</h3>
<p><i>I am maintaining rxvt-unicode for distribution/OS </i><font SIZE="-1"><i>XXX,</i></font><i> any recommendation?</i> </p>
<p> You should build one binary with the default options. <i>configure</i> now enables most useful options, and the trend goes to making them runtime-switchable, too, so there is usually no drawback to enabling them, except higher disk and possibly memory usage. The perl interpreter should be enabled, as important functionality (menus, selection, likely more in the future) depends on it. </p>
<p> You should not overwrite the <tt>&quot;perl-ext-common&quot;</tt> and <tt>&quot;perl-ext&quot;</tt> resources system-wide (except maybe with <tt>&quot;defaults&quot;</tt>). This will result in useful behaviour. If your distribution aims at low memory, add an empty <tt>&quot;perl-ext-common&quot;</tt> resource to the app-defaults file. This will keep the perl interpreter disabled until the user enables it. </p>
<p> If you can/want build more binaries, I recommend building a minimal one with <tt>&quot;--disable-everything&quot;</tt> (very useful) and a maximal one with <tt>&quot;--enable-everything&quot;</tt> (less useful, it will be very big due to a lot of encodings built-in that increase download times and are rarely used). </p>
<p> <i>I need to make it setuid/setgid to support utmp/ptys on my </i><font SIZE="-1"><i>OS,</i></font><i> is this safe?</i> </p>
<p> It should be, starting with release 7.1. You are encouraged to properly install urxvt with privileges necessary for your <font SIZE="-1">OS</font> now. </p>
<p> When rxvt-unicode detects that it runs setuid or setgid, it will fork into a helper process for privileged operations (pty handling on some systems, utmp/wtmp/lastlog handling on others) and drop privileges immediately. This is much safer than most other terminals that keep privileges while running (but is more relevant to urxvt, as it contains things as perl interpreters, which might be &#8220;helpful&#8221; to attackers). </p>
<p> This forking is done as the very first within <i>main()</i>, which is very early and reduces possible bugs to initialisation code run before <i>main()</i>, or things like the dynamic loader of your system, which should result in very little risk. </p>
<p> <i>I am on FreeBSD and rxvt-unicode does not seem to work at all.</i> </p>
<p> Rxvt-unicode requires the symbol <tt>&quot;__STDC_ISO_10646__&quot;</tt> to be defined in your compile environment, or an implementation that implements it, whether it defines the symbol or not. <tt>&quot;__STDC_ISO_10646__&quot;</tt> requires that <code>wchar_t</code> is represented as unicode. </p>
<p> As you might have guessed, FreeBSD does neither define this symbol nor does it support it. Instead, it uses its own internal representation of <code>wchar_t</code>. This is, of course, completely fine with respect to standards. </p>
<p> However, that means rxvt-unicode only works in <tt>&quot;POSIX&quot;</tt>, <tt>&quot;ISO-8859-1&quot;</tt> and <tt>&quot;UTF-8&quot;</tt> locales under FreeBSD (which all use Unicode as <code>wchar_t</code>). </p>
<p> <tt>&quot;__STDC_ISO_10646__&quot;</tt> is the only sane way to support multi-language apps in an <font SIZE="-1">OS,</font> as using a locale-dependent (and non-standardized) representation of <code>wchar_t</code> makes it impossible to convert between <code>wchar_t</code> (as used by X11 and your applications) and any other encoding without implementing OS-specific-wrappers for each and every locale. There simply are no APIs to convert <code>wchar_t</code> into anything except the current locale encoding. </p>
<p> Some applications (such as the formidable <code>mlterm</code>) work around this by carrying their own replacement functions for character set handling with them, and either implementing OS-dependent hacks or doing multiple conversions (which is slow and unreliable in case the <font SIZE="-1">OS</font> implements encodings slightly different than the terminal emulator). </p>
<p> The rxvt-unicode author insists that the right way to fix this is in the system libraries once and for all, instead of forcing every app to carry complete replacements for them :) </p>
<p> <i>How can I use rxvt-unicode under cygwin?</i> </p>
<p> rxvt-unicode should compile and run out of the box on cygwin, using the X11 libraries that come with cygwin. libW11 emulation is no longer supported (and makes no sense, either, as it only supported a single font). I recommend starting the X-server in <tt>&quot;-multiwindow&quot;</tt> or <tt>&quot;-rootless&quot;</tt> mode instead, which will result in similar look&amp;feel as the old libW11 emulation. </p>
<p> At the time of this writing, cygwin didn&#8217;t seem to support any multi-byte encodings (you might try <tt>&quot;LC_CTYPE=C-UTF-8&quot;</tt>), so you are likely limited to 8-bit encodings. </p>
<p> <i>Character widths are not correct.</i> </p>
<p> urxvt uses the system wcwidth function to know the information about the width of characters, so on systems with incorrect locale data you will likely get bad results. Two notorious examples are Solaris 9, where single-width characters like U+2514 are reported as double-width, and Darwin 8, where combining chars are reported having width 1. </p>
<p> The solution is to upgrade your system or switch to a better one. A possibly working workaround is to use a wcwidth implementation like </p>
<p> <a rel="nofollow" href="http://www.cl.cam.ac.uk/~mgk25/ucs/wcwidth.c">http://www.cl.cam.ac.uk/~mgk25/ucs/wcwidth.c</a></p>
<h2>Rxvt-Unicode Technical Reference</h2>
<p>The rest of this document describes various technical aspects of <code>rxvt-unicode</code>. First the description of supported command sequences, followed by pixmap support and last by a description of all features selectable at <tt>&quot;configure&quot;</tt> time.</p>
<h3>Definitions</h3>
<dl>
<dt><code>&quot;c&quot;</code></p>
<dd>The literal character c (potentially a multi-byte character).</p>
<dt><code>&quot;C&quot;</code></p>
<dd>A single (required) character.</p>
<dt><code>&quot;Ps&quot;</code></p>
<dd>A single (usually optional) numeric parameter, composed of one or more digits.</p>
<dt><code>&quot;Pm&quot;</code></p>
<dd>A multiple numeric parameter composed of any number of single numeric parameters, separated by <tt>&quot;;&quot;</tt> character(s).</p>
<dt><code>&quot;Pt&quot;</code></p>
<dd>A text parameter composed of printable characters.</dl>
<h3>Values</h3>
<dl>
<dt><code>&quot;ENQ&quot;</code></p>
<dd>Enquiry (Ctrl-E) = Send Device Attributes (<font SIZE="-1">DA</font>) request attributes from terminal. See &quot;ESC [ Ps c&quot;.</p>
<dt><code>&quot;BEL&quot;</code></p>
<dd>Bell (Ctrl-G)</p>
<dt><code>&quot;BS&quot;</code></p>
<dd>Backspace (Ctrl-H)</p>
<dt><code>&quot;TAB&quot;</code></p>
<dd>Horizontal Tab (<font SIZE="-1">HT</font>) (Ctrl-I)</p>
<dt><code>&quot;LF&quot;</code></p>
<dd>Line Feed or New Line (<font SIZE="-1">NL</font>) (Ctrl-J)</p>
<dt><code>&quot;VT&quot;</code></p>
<dd>Vertical Tab (Ctrl-K) same as &quot;LF&quot;</p>
<dt><code>&quot;FF&quot;</code></p>
<dd>Form Feed or New Page (<font SIZE="-1">NP</font>) (Ctrl-L) same as &quot;LF&quot;</p>
<dt><code>&quot;CR&quot;</code></p>
<dd>Carriage Return (Ctrl-M)</p>
<dt><code>&quot;SO&quot;</code></p>
<dd>Shift Out (Ctrl-N), invokes the G1 character set. Switch to Alternate Character Set</p>
<dt><code>&quot;SI&quot;</code></p>
<dd>Shift In (Ctrl-O), invokes the G0 character set (the default). Switch to Standard Character Set</p>
<dt><code>&quot;SP&quot;</code></p>
<dd>Space Character</dl>
<h3>Escape Sequences</h3>
<dl>
<dt><code>&quot;ESC # 8&quot;</code></p>
<dd><font SIZE="-1">DEC</font> Screen Alignment Test (<font SIZE="-1">DECALN</font>)</p>
<dt><code>&quot;ESC 7&quot;</code></p>
<dd>Save Cursor (<font SIZE="-1">SC</font>)</p>
<dt><code>&quot;ESC 8&quot;</code></p>
<dd>Restore Cursor</p>
<dt><code>&quot;ESC =&quot;</code></p>
<dd>Application Keypad (<font SIZE="-1">SMKX</font>). See also next sequence.</p>
<dt><code>&quot;ESC &gt;&quot;</code></p>
<dd>Normal Keypad (<font SIZE="-1">RMKX</font>) </p>
<p> <code>Note:</code> numbers or control functions are generated by the numeric keypad in normal or application mode, respectively (see Key Codes).</p>
<dt><code>&quot;ESC D&quot;</code></p>
<dd>Index (<font SIZE="-1">IND</font>)</p>
<dt><code>&quot;ESC E&quot;</code></p>
<dd>Next Line (<font SIZE="-1">NEL</font>)</p>
<dt><code>&quot;ESC H&quot;</code></p>
<dd>Tab Set (<font SIZE="-1">HTS</font>)</p>
<dt><code>&quot;ESC M&quot;</code></p>
<dd>Reverse Index (<font SIZE="-1">RI</font>)</p>
<dt><code>&quot;ESC N&quot;</code></p>
<dd>Single Shift Select of G2 Character Set (<font SIZE="-1">SS2</font>): affects next character only <i>unimplemented</i></p>
<dt><code>&quot;ESC O&quot;</code></p>
<dd>Single Shift Select of G3 Character Set (<font SIZE="-1">SS3</font>): affects next character only <i>unimplemented</i></p>
<dt><code>&quot;ESC Z&quot;</code></p>
<dd>Obsolete form of returns: &quot;ESC [ ? 1 ; 2 C&quot; <i>rxvt-unicode compile-time option</i></p>
<dt><code>&quot;ESC c&quot;</code></p>
<dd>Full reset (<font SIZE="-1">RIS</font>)</p>
<dt><code>&quot;ESC n&quot;</code></p>
<dd>Invoke the G2 Character Set (<font SIZE="-1">LS2</font>)</p>
<dt><code>&quot;ESC o&quot;</code></p>
<dd>Invoke the G3 Character Set (<font SIZE="-1">LS3</font>)</p>
<dt><code>&quot;ESC ( C&quot;</code></p>
<dd>Designate G0 Character Set (<font SIZE="-1">ISO 2022</font>), see below for values of <tt>&quot;C&quot;</tt>.</p>
<dt><code>&quot;ESC ) C&quot;</code></p>
<dd>Designate G1 Character Set (<font SIZE="-1">ISO 2022</font>), see below for values of <tt>&quot;C&quot;</tt>.</p>
<dt><code>&quot;ESC * C&quot;</code></p>
<dd>Designate G2 Character Set (<font SIZE="-1">ISO 2022</font>), see below for values of <tt>&quot;C&quot;</tt>.</p>
<dt><code>&quot;ESC + C&quot;</code></p>
<dd>Designate G3 Character Set (<font SIZE="-1">ISO 2022</font>), see below for values of <tt>&quot;C&quot;</tt>.</p>
<dt><code>&quot;ESC $ C&quot;</code></p>
<dd>Designate Kanji Character Set </p>
<p> Where &quot;C&quot; is one of: </p>
<table>
<tr VALIGN=top>
<td>C = 0</td>
<td>DEC Special Character and Line Drawing Set
</td>
</tr>
<tr VALIGN=top>
<td>C = A</td>
<td>United Kingdom (UK)
</td>
</tr>
<tr VALIGN=top>
<td>C = B</td>
<td>United States (USASCII)
</td>
</tr>
<tr VALIGN=top>
<td>C = &lt;</td>
<td>Multinational character set unimplemented
</td>
</tr>
<tr VALIGN=top>
<td>C = 5</td>
<td>Finnish character set unimplemented
</td>
</tr>
<tr VALIGN=top>
<td>C = C</td>
<td>Finnish character set unimplemented
</td>
</tr>
<tr VALIGN=top>
<td>C = K</td>
<td>German character set unimplemented
</td>
</tr>
</table>
</dl>
<h3><font SIZE="-1">CSI </font>(Command Sequence Introducer) Sequences</h3>
<dl>
<dt><code>&quot;ESC [ Ps @&quot;</code></p>
<dd>Insert &quot;Ps&quot; (Blank) Character(s) [default: 1] (<font SIZE="-1">ICH</font>)</p>
<dt><code>&quot;ESC [ Ps A&quot;</code></p>
<dd>Cursor Up &quot;Ps&quot; Times [default: 1] (<font SIZE="-1">CUU</font>)</p>
<dt><code>&quot;ESC [ Ps B&quot;</code></p>
<dd>Cursor Down &quot;Ps&quot; Times [default: 1] (<font SIZE="-1">CUD</font>)</p>
<dt><code>&quot;ESC [ Ps C&quot;</code></p>
<dd>Cursor Forward &quot;Ps&quot; Times [default: 1] (<font SIZE="-1">CUF</font>)</p>
<dt><code>&quot;ESC [ Ps D&quot;</code></p>
<dd>Cursor Backward &quot;Ps&quot; Times [default: 1] (<font SIZE="-1">CUB</font>)</p>
<dt><code>&quot;ESC [ Ps E&quot;</code></p>
<dd>Cursor Down &quot;Ps&quot; Times [default: 1] and to first column</p>
<dt><code>&quot;ESC [ Ps F&quot;</code></p>
<dd>Cursor Up &quot;Ps&quot; Times [default: 1] and to first column</p>
<dt><code>&quot;ESC [ Ps G&quot;</code></p>
<dd>Cursor to Column &quot;Ps&quot; (<font SIZE="-1">HPA</font>)</p>
<dt><code>&quot;ESC [ Ps;Ps H&quot;</code></p>
<dd>Cursor Position [row;column] [default: 1;1] (<font SIZE="-1">CUP</font>)</p>
<dt><code>&quot;ESC [ Ps I&quot;</code></p>
<dd>Move forward &quot;Ps&quot; tab stops [default: 1]</p>
<dt><code>&quot;ESC [ Ps J&quot;</code></p>
<dd>Erase in Display (<font SIZE="-1">ED</font>) </p>
<table>
<tr VALIGN=top>
<td>Ps = 0</td>
<td>Clear Right and Below (default)
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 1</td>
<td>Clear Left and Above
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 2</td>
<td>Clear All
</td>
</tr>
</table>
<dt><code>&quot;ESC [ Ps K&quot;</code></p>
<dd>Erase in Line (<font SIZE="-1">EL</font>) </p>
<table>
<tr VALIGN=top>
<td>Ps = 0</td>
<td>Clear to Right (default)</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 1</td>
<td>Clear to Left</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 2</td>
<td>Clear All</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 3</td>
<td>Like Ps = 0, but is ignored when wrapped</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td></td>
<td>(urxvt extension)
</td>
</tr>
</table>
<dt><code>&quot;ESC [ Ps L&quot;</code></p>
<dd>Insert &quot;Ps&quot; Line(s) [default: 1] (<font SIZE="-1">IL</font>)</p>
<dt><code>&quot;ESC [ Ps M&quot;</code></p>
<dd>Delete &quot;Ps&quot; Line(s) [default: 1] (<font SIZE="-1">DL</font>)</p>
<dt><code>&quot;ESC [ Ps P&quot;</code></p>
<dd>Delete &quot;Ps&quot; Character(s) [default: 1] (<font SIZE="-1">DCH</font>)</p>
<dt><code>&quot;ESC [ Ps;Ps;Ps;Ps;Ps T&quot;</code></p>
<dd>Initiate . <i>unimplemented</i> Parameters are [func;startx;starty;firstrow;lastrow].</p>
<dt><code>&quot;ESC [ Ps W&quot;</code></p>
<dd>Tabulator functions </p>
<table>
<tr VALIGN=top>
<td>Ps = 0</td>
<td>Tab Set (HTS)
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 2</td>
<td>Tab Clear (TBC), Clear Current Column (default)
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 5</td>
<td>Tab Clear (TBC), Clear All
</td>
</tr>
</table>
<dt><code>&quot;ESC [ Ps X&quot;</code></p>
<dd>Erase &quot;Ps&quot; Character(s) [default: 1] (<font SIZE="-1">ECH</font>)</p>
<dt><code>&quot;ESC [ Ps Z&quot;</code></p>
<dd>Move backward &quot;Ps&quot; [default: 1] tab stops</p>
<dt><code>&quot;ESC [ Ps &#8216;&quot;</code></p>
<dd>See &quot;ESC [ Ps G&quot;</p>
<dt><code>&quot;ESC [ Ps a&quot;</code></p>
<dd>See &quot;ESC [ Ps C&quot;</p>
<dt><code>&quot;ESC [ Ps c&quot;</code></p>
<dd>Send Device Attributes (<font SIZE="-1">DA</font>) &quot;Ps = 0&quot; (or omitted): request attributes from terminal returns: &quot;ESC [ ? 1 ; 2 c&quot; (&#8220;I am a <font SIZE="-1">VT100</font> with Advanced Video Option&#8221;)</p>
<dt><code>&quot;ESC [ Ps d&quot;</code></p>
<dd>Cursor to Line &quot;Ps&quot; (<font SIZE="-1">VPA</font>)</p>
<dt><code>&quot;ESC [ Ps e&quot;</code></p>
<dd>See &quot;ESC [ Ps A&quot;</p>
<dt><code>&quot;ESC [ Ps;Ps f&quot;</code></p>
<dd>Horizontal and Vertical Position [row;column] (<font SIZE="-1">HVP</font>) [default: 1;1]</p>
<dt><code>&quot;ESC [ Ps g&quot;</code></p>
<dd>Tab Clear (<font SIZE="-1">TBC</font>) </p>
<table>
<tr VALIGN=top>
<td>Ps = 0</td>
<td>Clear Current Column (default)
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 3</td>
<td>Clear All (TBC)
</td>
</tr>
</table>
<dt><code>&quot;ESC [ Pm h&quot;</code></p>
<dd>Set Mode (<font SIZE="-1">SM</font>). See &quot;ESC [ Pm l&quot; sequence for description of <tt>&quot;Pm&quot;</tt>.</p>
<dt><code>&quot;ESC [ Ps i&quot;</code></p>
<dd>Printing. See also the <tt>&quot;print-pipe&quot;</tt> resource. </p>
<table>
<tr VALIGN=top>
<td>Ps = 0</td>
<td>print screen (MC0)
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 4</td>
<td>disable transparent print mode (MC4)
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 5</td>
<td>enable transparent print mode (MC5)
</td>
</tr>
</table>
<dt><code>&quot;ESC [ Pm l&quot;</code></p>
<dd>Reset Mode (<font SIZE="-1">RM</font>)</p>
<dl>
<dd>
<dl>
<dt><code>&quot;Ps = 4&quot;</code></p>
<dd>
<table>
<tr VALIGN=top>
<td>h</td>
<td>Insert Mode (SMIR)
</td>
</tr>
<tr VALIGN=top>
<td>l</td>
<td>Replace Mode (RMIR)
</td>
</tr>
</table>
<dt><code>&quot;Ps = 20&quot;</code> (partially implemented)</p>
<dd>
<table>
<tr VALIGN=top>
<td>h</td>
<td>Automatic Newline (LNM)
</td>
</tr>
<tr VALIGN=top>
<td>l</td>
<td>Normal Linefeed (LNM)
</td>
</tr>
</table>
</dl>
</dl>
<dl>
<dd></dl>
<dt><code>&quot;ESC [ Pm m&quot;</code></p>
<dd>Character Attributes (<font SIZE="-1">SGR</font>) </p>
<table>
<tr VALIGN=top>
<td>Pm = 0</td>
<td>Normal (default)
</td>
</tr>
<tr VALIGN=top>
<td>Pm = 1 / 21</td>
<td>On / Off Bold (bright fg)
</td>
</tr>
<tr VALIGN=top>
<td>Pm = 3 / 23</td>
<td>On / Off Italic
</td>
</tr>
<tr VALIGN=top>
<td>Pm = 4 / 24</td>
<td>On / Off Underline
</td>
</tr>
<tr VALIGN=top>
<td>Pm = 5 / 25</td>
<td>On / Off Slow Blink (bright bg)
</td>
</tr>
<tr VALIGN=top>
<td>Pm = 6 / 26</td>
<td>On / Off Rapid Blink (bright bg)
</td>
</tr>
<tr VALIGN=top>
<td>Pm = 7 / 27</td>
<td>On / Off Inverse
</td>
</tr>
<tr VALIGN=top>
<td>Pm = 8 / 27</td>
<td>On / Off Invisible (NYI)
</td>
</tr>
<tr VALIGN=top>
<td>Pm = 30 / 40</td>
<td>fg/bg Black
</td>
</tr>
<tr VALIGN=top>
<td>Pm = 31 / 41</td>
<td>fg/bg Red
</td>
</tr>
<tr VALIGN=top>
<td>Pm = 32 / 42</td>
<td>fg/bg Green
</td>
</tr>
<tr VALIGN=top>
<td>Pm = 33 / 43</td>
<td>fg/bg Yellow
</td>
</tr>
<tr VALIGN=top>
<td>Pm = 34 / 44</td>
<td>fg/bg Blue
</td>
</tr>
<tr VALIGN=top>
<td>Pm = 35 / 45</td>
<td>fg/bg Magenta
</td>
</tr>
<tr VALIGN=top>
<td>Pm = 36 / 46</td>
<td>fg/bg Cyan
</td>
</tr>
<tr VALIGN=top>
<td>Pm = 37 / 47</td>
<td>fg/bg White
</td>
</tr>
<tr VALIGN=top>
<td>Pm = 38;5 / 48;5</td>
<td>set fg/bg to colour #m (ISO 8613-6)
</td>
</tr>
<tr VALIGN=top>
<td>Pm = 39 / 49</td>
<td>fg/bg Default
</td>
</tr>
<tr VALIGN=top>
<td>Pm = 90 / 100</td>
<td>fg/bg Bright Black
</td>
</tr>
<tr VALIGN=top>
<td>Pm = 91 / 101</td>
<td>fg/bg Bright Red
</td>
</tr>
<tr VALIGN=top>
<td>Pm = 92 / 102</td>
<td>fg/bg Bright Green
</td>
</tr>
<tr VALIGN=top>
<td>Pm = 93 / 103</td>
<td>fg/bg Bright Yellow
</td>
</tr>
<tr VALIGN=top>
<td>Pm = 94 / 104</td>
<td>fg/bg Bright Blue
</td>
</tr>
<tr VALIGN=top>
<td>Pm = 95 / 105</td>
<td>fg/bg Bright Magenta
</td>
</tr>
<tr VALIGN=top>
<td>Pm = 96 / 106</td>
<td>fg/bg Bright Cyan
</td>
</tr>
<tr VALIGN=top>
<td>Pm = 97 / 107</td>
<td>fg/bg Bright White
</td>
</tr>
<tr VALIGN=top>
<td>Pm = 99 / 109</td>
<td>fg/bg Bright Default
</td>
</tr>
</table>
<dt><code>&quot;ESC [ Ps n&quot;</code></p>
<dd>Device Status Report (<font SIZE="-1">DSR</font>) </p>
<table>
<tr VALIGN=top>
<td>Ps = 5</td>
<td>Status Report ESC [ 0 n (&#8220;OK&#8221;)
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 6</td>
<td>Report Cursor Position (CPR) [row;column] as ESC [ r ; c R
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 7</td>
<td>Request Display Name
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 8</td>
<td>Request Version Number (place in window title)
</td>
</tr>
</table>
<dt><code>&quot;ESC [ Ps SP q&quot;</code></p>
<dd>Set Cursor Style (<font SIZE="-1">DECSCUSR</font>) </p>
<table>
<tr VALIGN=top>
<td>Ps = 0</td>
<td>Blink Block
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 1</td>
<td>Blink Block
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 2</td>
<td>Steady Block
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 3</td>
<td>Blink Underline
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 4</td>
<td>Steady Underline
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 5</td>
<td>Blink Bar (XTerm)
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 6</td>
<td>Steady Bar (XTerm)
</td>
</tr>
</table>
<dt><code>&quot;ESC [ Ps;Ps r&quot;</code></p>
<dd>Set Scrolling Region [top;bottom] [default: full size of window] (<font SIZE="-1">CSR</font>)</p>
<dt><code>&quot;ESC [ s&quot;</code></p>
<dd>Save Cursor (<font SIZE="-1">SC</font>)</p>
<dt><code>&quot;ESC [ Ps;Pt t&quot;</code></p>
<dd>Window Operations </p>
<table>
<tr VALIGN=top>
<td>Ps = 1</td>
<td>Deiconify (map) window
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 2</td>
<td>Iconify window
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 3</td>
<td>ESC [ 3 ; X ; Y t Move window to (X|Y)
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 4</td>
<td>ESC [ 4 ; H ; W t Resize to WxH pixels
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 5</td>
<td>Raise window
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 6</td>
<td>Lower window
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 7</td>
<td>Refresh screen once
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 8</td>
<td>ESC [ 8 ; R ; C t Resize to R rows and C columns
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 11</td>
<td>Report window state (responds with Ps = 1 or Ps = 2)
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 13</td>
<td>Report window position (responds with Ps = 3)
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 14</td>
<td>Report window pixel size (responds with Ps = 4)
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 18</td>
<td>Report window text size (responds with Ps = 7)
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 19</td>
<td>Currently the same as Ps = 18, but responds with Ps = 9
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 20</td>
<td>Reports icon label (ESC ] L NAME 234)
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 21</td>
<td>Reports window title (ESC ] l NAME 234)
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 24..</td>
<td>Set window height to Ps rows
</td>
</tr>
</table>
<dt><code>&quot;ESC [ u&quot;</code></p>
<dd>Restore Cursor</p>
<dt><code>&quot;ESC [ Ps x&quot;</code></p>
<dd>Request Terminal Parameters (<font SIZE="-1">DECREQTPARM</font>)</dl>
<h3><font SIZE="-1">DEC</font> Private Modes</h3>
<dl>
<dt><code>&quot;ESC [ ? Pm h&quot;</code></p>
<dd><font SIZE="-1">DEC</font> Private Mode Set (<font SIZE="-1">DECSET</font>)</p>
<dt><code>&quot;ESC [ ? Pm l&quot;</code></p>
<dd><font SIZE="-1">DEC</font> Private Mode Reset (<font SIZE="-1">DECRST</font>)</p>
<dt><code>&quot;ESC [ ? Pm r&quot;</code></p>
<dd>Restore previously saved <font SIZE="-1">DEC</font> Private Mode Values.</p>
<dt><code>&quot;ESC [ ? Pm s&quot;</code></p>
<dd>Save <font SIZE="-1">DEC</font> Private Mode Values.</p>
<dt><code>&quot;ESC [ ? Pm t&quot;</code></p>
<dd>Toggle <font SIZE="-1">DEC</font> Private Mode Values (rxvt extension). <i>where</i></p>
<dl>
<dd>
<dl>
<dt><code>&quot;Pm = 1&quot;</code> (<font SIZE="-1">DECCKM</font>)</p>
<dd>
<table>
<tr VALIGN=top>
<td>h</td>
<td>Application Cursor Keys
</td>
</tr>
<tr VALIGN=top>
<td>l</td>
<td>Normal Cursor Keys
</td>
</tr>
</table>
<dt><code>&quot;Pm = 2&quot;</code> (<font SIZE="-1">DECANM</font>)</p>
<dd>
<table>
<tr VALIGN=top>
<td>h</td>
<td>Enter VT52 mode
</td>
</tr>
<tr VALIGN=top>
<td>l</td>
<td>Enter VT52 mode
</td>
</tr>
</table>
<dt><code>&quot;Pm = 3&quot;</code> (<font SIZE="-1">DECCOLM</font>)</p>
<dd>
<table>
<tr VALIGN=top>
<td>h</td>
<td>132 Column Mode
</td>
</tr>
<tr VALIGN=top>
<td>l</td>
<td>80 Column Mode
</td>
</tr>
</table>
<dt><code>&quot;Pm = 4&quot;</code> (<font SIZE="-1">DECSCLM</font>)</p>
<dd>
<table>
<tr VALIGN=top>
<td>h</td>
<td>Smooth (Slow) Scroll
</td>
</tr>
<tr VALIGN=top>
<td>l</td>
<td>Jump (Fast) Scroll
</td>
</tr>
</table>
<dt><code>&quot;Pm = 5&quot;</code> (<font SIZE="-1">DECSCNM</font>)</p>
<dd>
<table>
<tr VALIGN=top>
<td>h</td>
<td>Reverse Video
</td>
</tr>
<tr VALIGN=top>
<td>l</td>
<td>Normal Video
</td>
</tr>
</table>
<dt><code>&quot;Pm = 6&quot;</code> (<font SIZE="-1">DECOM</font>)</p>
<dd>
<table>
<tr VALIGN=top>
<td>h</td>
<td>Origin Mode
</td>
</tr>
<tr VALIGN=top>
<td>l</td>
<td>Normal Cursor Mode
</td>
</tr>
</table>
<dt><code>&quot;Pm = 7&quot;</code> (<font SIZE="-1">DECAWM</font>)</p>
<dd>
<table>
<tr VALIGN=top>
<td>h</td>
<td>Wraparound Mode
</td>
</tr>
<tr VALIGN=top>
<td>l</td>
<td>No Wraparound Mode
</td>
</tr>
</table>
<dt><code>&quot;Pm = 8&quot;</code> (<font SIZE="-1">DECARM</font>) <i>unimplemented</i></p>
<dd>
<table>
<tr VALIGN=top>
<td>h</td>
<td>Auto-repeat Keys
</td>
</tr>
<tr VALIGN=top>
<td>l</td>
<td>No Auto-repeat Keys
</td>
</tr>
</table>
<dt><code>&quot;Pm = 9&quot;</code> (X10 XTerm mouse protocol)</p>
<dd>
<table>
<tr VALIGN=top>
<td>h</td>
<td>Send Mouse X &amp; Y on button press.
</td>
</tr>
<tr VALIGN=top>
<td>l</td>
<td>No mouse reporting.
</td>
</tr>
</table>
<dt><code>&quot;Pm = 12&quot;</code> (<font SIZE="-1">AT&amp;T 610,</font> XTerm)</p>
<dd>
<table>
<tr VALIGN=top>
<td>h</td>
<td>Blinking cursor (cvvis)
</td>
</tr>
<tr VALIGN=top>
<td>l</td>
<td>Steady cursor (cnorm)
</td>
</tr>
</table>
<dt><code>&quot;Pm = 25&quot;</code> (<font SIZE="-1">DECTCEM</font>)</p>
<dd>
<table>
<tr VALIGN=top>
<td>h</td>
<td>Visible cursor {cnorm/cvvis}
</td>
</tr>
<tr VALIGN=top>
<td>l</td>
<td>Invisible cursor {civis}
</td>
</tr>
</table>
<dt><code>&quot;Pm = 30&quot;</code> (<code>rxvt</code>)</p>
<dd>
<table>
<tr VALIGN=top>
<td>h</td>
<td>scrollBar visible
</td>
</tr>
<tr VALIGN=top>
<td>l</td>
<td>scrollBar invisible
</td>
</tr>
</table>
<dt><code>&quot;Pm = 35&quot;</code> (<code>rxvt</code>)</p>
<dd>
<table>
<tr VALIGN=top>
<td>h</td>
<td>Allow XTerm Shift+key sequences
</td>
</tr>
<tr VALIGN=top>
<td>l</td>
<td>Disallow XTerm Shift+key sequences
</td>
</tr>
</table>
<dt><code>&quot;Pm = 38&quot;</code> <i>unimplemented</i></p>
<dd>Enter Tektronix Mode (<font SIZE="-1">DECTEK</font>)</p>
<dt><code>&quot;Pm = 40&quot;</code></p>
<dd>
<table>
<tr VALIGN=top>
<td>h</td>
<td>Allow 80/132 Mode
</td>
</tr>
<tr VALIGN=top>
<td>l</td>
<td>Disallow 80/132 Mode
</td>
</tr>
</table>
<dt><code>&quot;Pm = 44&quot;</code> <i>unimplemented</i></p>
<dd>
<table>
<tr VALIGN=top>
<td>h</td>
<td>Turn On Margin Bell
</td>
</tr>
<tr VALIGN=top>
<td>l</td>
<td>Turn Off Margin Bell
</td>
</tr>
</table>
<dt><code>&quot;Pm = 45&quot;</code> <i>unimplemented</i></p>
<dd>
<table>
<tr VALIGN=top>
<td>h</td>
<td>Reverse-wraparound Mode
</td>
</tr>
<tr VALIGN=top>
<td>l</td>
<td>No Reverse-wraparound Mode
</td>
</tr>
</table>
<dt><code>&quot;Pm = 46&quot;</code> <i>unimplemented</i></p>
<dd>
<dt><code>&quot;Pm = 47&quot;</code></p>
<dd>
<table>
<tr VALIGN=top>
<td>h</td>
<td>Use Alternate Screen Buffer
</td>
</tr>
<tr VALIGN=top>
<td>l</td>
<td>Use Normal Screen Buffer
</td>
</tr>
</table>
<dt><code>&quot;Pm = 66&quot;</code> (<font SIZE="-1">DECNKM</font>)</p>
<dd>
<table>
<tr VALIGN=top>
<td>h</td>
<td>Application Keypad (DECKPAM/DECPAM) == ESC =
</td>
</tr>
<tr VALIGN=top>
<td>l</td>
<td>Normal Keypad (DECKPNM/DECPNM) == ESC &gt;
</td>
</tr>
</table>
<dt><code>&quot;Pm = 67&quot;</code> (<font SIZE="-1">DECBKM</font>)</p>
<dd>
<table>
<tr VALIGN=top>
<td>h</td>
<td>Backspace key sends BS
</td>
</tr>
<tr VALIGN=top>
<td>l</td>
<td>Backspace key sends DEL
</td>
</tr>
</table>
<dt><code>&quot;Pm = 1000&quot;</code> (X11 XTerm mouse protocol)</p>
<dd>
<table>
<tr VALIGN=top>
<td>h</td>
<td>Send Mouse X &amp; Y on button press and release.
</td>
</tr>
<tr VALIGN=top>
<td>l</td>
<td>No mouse reporting.
</td>
</tr>
</table>
<dt><code>&quot;Pm = 1001&quot;</code> (X11 XTerm) <i>unimplemented</i></p>
<dd>
<table>
<tr VALIGN=top>
<td>h</td>
<td>Use Hilite Mouse Tracking.
</td>
</tr>
<tr VALIGN=top>
<td>l</td>
<td>No mouse reporting.
</td>
</tr>
</table>
<dt><code>&quot;Pm = 1002&quot;</code> (X11 XTerm cell motion mouse tracking)</p>
<dd>
<table>
<tr VALIGN=top>
<td>h</td>
<td>Send Mouse X &amp; Y on button press and release, and motion with a button pressed.
</td>
</tr>
<tr VALIGN=top>
<td>l</td>
<td>No mouse reporting.
</td>
</tr>
</table>
<dt><code>&quot;Pm = 1003&quot;</code> (X11 XTerm all motion mouse tracking)</p>
<dd>
<table>
<tr VALIGN=top>
<td>h</td>
<td>Send Mouse X &amp; Y on button press and release, and motion.
</td>
</tr>
<tr VALIGN=top>
<td>l</td>
<td>No mouse reporting.
</td>
</tr>
</table>
<dt><code>&quot;Pm = 1004&quot;</code> (X11 XTerm focus in/focus out events) <i>unimplemented</i></p>
<dd>
<table>
<tr VALIGN=top>
<td>h</td>
<td>Send Mouse focus in/focus out events.
</td>
</tr>
<tr VALIGN=top>
<td>l</td>
<td>Don&#8217;T send focus events.
</td>
</tr>
</table>
<dt><code>&quot;Pm = 1005&quot;</code> (X11 XTerm <font SIZE="-1">UTF-8</font> mouse mode) (Compile frills)</p>
<dd>Try to avoid this mode, it doesn&#8217;t work sensibly in non-UTF-8 locales. Use mode <tt>1015</tt> instead. </p>
<p> Unlike XTerm, coordinates larger than 2015) will work fine. </p>
<table>
<tr VALIGN=top>
<td>h</td>
<td>Enable mouse coordinates in locale-specific encoding.
</td>
</tr>
<tr VALIGN=top>
<td>l</td>
<td>Enable mouse coordinates as binary octets.
</td>
</tr>
</table>
<dt><code>&quot;Pm = 1010&quot;</code> (<code>rxvt</code>)</p>
<dd>
<table>
<tr VALIGN=top>
<td>h</td>
<td>Don&#8217;t scroll to bottom on TTY output
</td>
</tr>
<tr VALIGN=top>
<td>l</td>
<td>Scroll to bottom on TTY output
</td>
</tr>
</table>
<dt><code>&quot;Pm = 1011&quot;</code> (<code>rxvt</code>)</p>
<dd>
<table>
<tr VALIGN=top>
<td>h</td>
<td>Scroll to bottom when a key is pressed
</td>
</tr>
<tr VALIGN=top>
<td>l</td>
<td>Don&#8217;t scroll to bottom when a key is pressed
</td>
</tr>
</table>
<dt><code>&quot;Pm = 1015&quot;</code> (<code>rxvt-unicode</code>) (Compile frills)</p>
<dd>
<table>
<tr VALIGN=top>
<td>h</td>
<td>Enable urxvt mouse coordinate reporting.
</td>
</tr>
<tr VALIGN=top>
<td>l</td>
<td>Use old-style CSI M C C C encoding.
</td>
</tr>
</table>
<p> Changes all mouse reporting codes to use decimal parameters instead of octets or characters. </p>
<p> This mode should be enabled <i>before</i> actually enabling mouse reporting, for semi-obvious reasons. </p>
<p> The sequences received for various modes are as follows: </p>
<pre> ESC [ M o o o !1005, !1015 (three octets)
 ESC [ M c c c 1005, !1015 (three characters)
 ESC [ Pm M 1015 (three or more numeric parameters)</pre>
<p>The first three parameters are <tt>&quot;code&quot;</tt>, <tt>&quot;x&quot;</tt> and <tt>&quot;y&quot;</tt>. Code is the numeric code as for the other modes (but encoded as a decimal number, including the additional offset of 32, so you have to subtract 32 first), <tt>&quot;x&quot;</tt> and <tt>&quot;y&quot;</tt> are the coordinates (1|1 is the upper left corner, just as with cursor positioning). </p>
<p> Example: Shift-Button-1 press at top row, column 80. </p>
<pre> ESC [ 37 ; 80 ; 1 M</pre>
<p>One can use this feature by simply enabling it and then looking for parameters to the <tt>&quot;ESC [ M&quot;</tt> reply &#8211; if there are any, this mode is active, otherwise one of the old reporting styles is used. </p>
<p> Other (to be implemented) reply sequences will use a similar encoding. </p>
<p> In the future, more parameters might get added (pixel coordinates for example &#8211; anybody out there who needs this?).</p>
<dt><code>&quot;Pm = 1021&quot;</code> (<code>rxvt</code>)</p>
<dd>
<table>
<tr VALIGN=top>
<td>h</td>
<td>Bold/italic implies high intensity (see option -is)
</td>
</tr>
<tr VALIGN=top>
<td>l</td>
<td>Font styles have no effect on intensity (Compile styles)
</td>
</tr>
</table>
<dt><code>&quot;Pm = 1047&quot;</code> (X11 XTerm alternate screen buffer)</p>
<dd>
<table>
<tr VALIGN=top>
<td>h</td>
<td>Use Alternate Screen Buffer
</td>
</tr>
<tr VALIGN=top>
<td>l</td>
<td>Use Normal Screen Buffer &#8211; clear Alternate Screen Buffer if returning from it
</td>
</tr>
</table>
<dt><code>&quot;Pm = 1048&quot;</code> (X11 XTerm alternate <font SIZE="-1">DECSC</font>)</p>
<dd>
<table>
<tr VALIGN=top>
<td>h</td>
<td>Save cursor position
</td>
</tr>
<tr VALIGN=top>
<td>l</td>
<td>Restore cursor position
</td>
</tr>
</table>
<dt><code>&quot;Pm = 1049&quot;</code> (X11 XTerm 1047 + 1048)</p>
<dd>
<table>
<tr VALIGN=top>
<td>h</td>
<td>Use Alternate Screen Buffer &#8211; clear Alternate Screen Buffer if switching to it
</td>
</tr>
<tr VALIGN=top>
<td>l</td>
<td>Use Normal Screen Buffer
</td>
</tr>
</table>
<dt><code>&quot;Pm = 2004&quot;</code> (X11 XTerm bracketed paste mode)</p>
<dd>
<table>
<tr VALIGN=top>
<td>h</td>
<td>Enable bracketed paste mode &#8211; prepend / append to the pasted text the control sequences ESC [ 200 ~ / ESC [ 201 ~
</td>
</tr>
<tr VALIGN=top>
<td>l</td>
<td>Disable bracketed paste mode
</td>
</tr>
</table>
</dl>
</dl>
<dl>
<dd></dl>
</dl>
<h3>XTerm Operating System Commands</h3>
<dl>
<dt><code>&quot;ESC ] Ps;Pt ST&quot;</code></p>
<dd>Set XTerm Parameters. 8-bit <font SIZE="-1">ST:</font> 0x9c, 7-bit <font SIZE="-1">ST</font> sequence: <font SIZE="-1">ESC</font> \ (0x1b, 0x5c), backwards compatible terminator <font SIZE="-1">BEL </font>(0x07) is also accepted. any <code>octet</code> can be escaped by prefixing it with <font SIZE="-1">SYN </font>(0x16, ^V). </p>
<table>
<tr VALIGN=top>
<td>Ps = 0</td>
<td>Change Icon Name and Window Title to Pt
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 1</td>
<td>Change Icon Name to Pt
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 2</td>
<td>Change Window Title to Pt
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 3</td>
<td>If Pt starts with a ?, query the (STRING) property of the window and return it. If Pt contains a =, set the named property to the given value, else delete the specified property.
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 4</td>
<td>Pt is a semi-colon separated sequence of one or more semi-colon separated number/name pairs, where number is an index to a colour and name is the name of a colour. Each pair causes the numbered colour to be changed to name. Numbers 0-7 corresponds to low-intensity (normal) colours and 8-15 corresponds to high-intensity colours. 0=black, 1=red, 2=green, 3=yellow, 4=blue, 5=magenta, 6=cyan, 7=white
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 10</td>
<td>Change colour of text foreground to Pt
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 11</td>
<td>Change colour of text background to Pt
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 12</td>
<td>Change colour of text cursor foreground to Pt
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 13</td>
<td>Change colour of mouse foreground to Pt
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 17</td>
<td>Change background colour of highlight characters to Pt
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 19</td>
<td>Change foreground colour of highlight characters to Pt
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 20</td>
<td>Change background pixmap parameters (see section BACKGROUND IMAGE) (Compile pixbuf).
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 39</td>
<td>Change default foreground colour to Pt. [deprecated, use 10]
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 46</td>
<td>Change Log File to Pt unimplemented
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 49</td>
<td>Change default background colour to Pt. [deprecated, use 11]
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 50</td>
<td>Set fontset to Pt, with the following special values of Pt (rxvt) #+n change up n #-n change down n if n is missing of 0, a value of 1 is used empty change to font0 n change to font n
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 55</td>
<td>Log all scrollback buffer and all of screen to Pt [disabled]
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 701</td>
<td>Change current locale to Pt, or, if Pt is ?, return the current locale (Compile frills).
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 702</td>
<td>Request version if Pt is ?, returning rxvt-unicode, the resource name, the major and minor version numbers, e.g. ESC ] 702 ; rxvt-unicode ; urxvt ; 7 ; 4 ST.
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 704</td>
<td>Change colour of italic characters to Pt
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 705</td>
<td>Change background pixmap tint colour to Pt (Compile transparency).
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 706</td>
<td>Change colour of bold characters to Pt
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 707</td>
<td>Change colour of underlined characters to Pt
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 708</td>
<td>Change colour of the border to Pt
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 710</td>
<td>Set normal fontset to Pt. Same as Ps = 50.
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 711</td>
<td>Set bold fontset to Pt. Similar to Ps = 50 (Compile styles).
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 712</td>
<td>Set italic fontset to Pt. Similar to Ps = 50 (Compile styles).
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 713</td>
<td>Set bold-italic fontset to Pt. Similar to Ps = 50 (Compile styles).
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 720</td>
<td>Move viewing window up by Pt lines, or clear scrollback buffer if Pt = 0 (Compile frills).
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 721</td>
<td>Move viewing window down by Pt lines, or clear scrollback buffer if Pt = 0 (Compile frills).
</td>
</tr>
<tr VALIGN=top>
<td>Ps = 777</td>
<td>Call the perl extension with the given string, which should be of the form extension:parameters (Compile perl).
</td>
</tr>
</table>
</dl>
<h2>Background Image</h2>
<p>For the <font SIZE="-1">BACKGROUND IMAGE</font> XTerm escape sequence &quot;ESC ] 20 ; Pt ST&quot; the value of &quot;Pt&quot; can be one of the following commands:</p>
<dl>
<dt><code>&quot;?&quot;</code></p>
<dd>display scale and position in the title</p>
<dt><code>&quot;;WxH+X+Y&quot;</code></p>
<dd>change scale and/or position</p>
<dt><code>&quot;FILE;WxH+X+Y&quot;</code></p>
<dd>change background image</dl>
<h2>Mouse Reporting</h2>
<dl>
<dt><code>&quot;ESC [ M &lt;b&gt; &lt;x&gt; &lt;y&gt;&quot;</code></p>
<dd>report mouse position</dl>
<p> The lower 2 bits of &quot;&lt;b&gt;&quot; indicate the button:</p>
<dl>
<dt>Button = <code>&quot;(&lt;b&gt; &#8211; SPACE) &amp; 3&quot;</code></p>
<dd>
<table>
<tr VALIGN=top>
<td>0</td>
<td>Button1 pressed
</td>
</tr>
<tr VALIGN=top>
<td>1</td>
<td>Button2 pressed
</td>
</tr>
<tr VALIGN=top>
<td>2</td>
<td>Button3 pressed
</td>
</tr>
<tr VALIGN=top>
<td>3</td>
<td>button released (X11 mouse report)
</td>
</tr>
</table>
</dl>
<p> The upper bits of &quot;&lt;b&gt;&quot; indicate the modifiers when the button was pressed and are added together (X11 mouse report only):</p>
<dl>
<dt>State = <code>&quot;(&lt;b&gt; &#8211; SPACE) &amp; ~3&quot;</code></p>
<dd>
<table>
<tr VALIGN=top>
<td>4</td>
<td>Shift
</td>
</tr>
<tr VALIGN=top>
<td>8</td>
<td>Meta
</td>
</tr>
<tr VALIGN=top>
<td>16</td>
<td>Control
</td>
</tr>
<tr VALIGN=top>
<td>32</td>
<td>Motion Notify
</td>
</tr>
<tr VALIGN=top>
<td>32</td>
<td>Double Click (rxvt extension), disabled by default
</td>
</tr>
<tr VALIGN=top>
<td>64</td>
<td>Button1 is actually Button4, Button2 is actually Button5 etc.
</td>
</tr>
</table>
<p> Col = &quot;&lt;x&gt; &#8211; SPACE&quot; </p>
<p> Row = &quot;&lt;y&gt; &#8211; SPACE&quot;</dl>
<h2>Key Codes</h2>
<p>Note: <code>Shift</code> + <code>F1</code>&#8211;<code>F10</code> generates <code>F11</code>&#8211;<code>F20</code> </p>
<p> For the keypad, use <code>Shift</code> to temporarily toggle Application Keypad mode and use <code>Num_Lock</code> to override Application Keypad mode, i.e. if <code>Num_Lock</code> is on the keypad is in normal mode. Also note that the values of <code>BackSpace</code>, <code>Delete</code> may have been compiled differently on your system. </p>
<table>
<tr VALIGN=top>
<td></td>
<td>Normal</td>
<td>Shift</td>
<td>Control</td>
<td>Ctrl+Shift
</td>
</tr>
<tr VALIGN=top>
<td>Tab</td>
<td>^I</td>
<td>ESC [ Z</td>
<td>^I</td>
<td>ESC [ Z
</td>
</tr>
<tr VALIGN=top>
<td>BackSpace</td>
<td>^?</td>
<td>^?</td>
<td>^H</td>
<td>^H
</td>
</tr>
<tr VALIGN=top>
<td>Find</td>
<td>ESC [ 1 ~</td>
<td>ESC [ 1 $</td>
<td>ESC [ 1 ^</td>
<td>ESC [ 1 @
</td>
</tr>
<tr VALIGN=top>
<td>Insert</td>
<td>ESC [ 2 ~</td>
<td>paste</td>
<td>ESC [ 2 ^</td>
<td>ESC [ 2 @
</td>
</tr>
<tr VALIGN=top>
<td>Execute</td>
<td>ESC [ 3 ~</td>
<td>ESC [ 3 $</td>
<td>ESC [ 3 ^</td>
<td>ESC [ 3 @
</td>
</tr>
<tr VALIGN=top>
<td>Select</td>
<td>ESC [ 4 ~</td>
<td>ESC [ 4 $</td>
<td>ESC [ 4 ^</td>
<td>ESC [ 4 @
</td>
</tr>
<tr VALIGN=top>
<td>Prior</td>
<td>ESC [ 5 ~</td>
<td>scroll-up</td>
<td>ESC [ 5 ^</td>
<td>ESC [ 5 @
</td>
</tr>
<tr VALIGN=top>
<td>Next</td>
<td>ESC [ 6 ~</td>
<td>scroll-down</td>
<td>ESC [ 6 ^</td>
<td>ESC [ 6 @
</td>
</tr>
<tr VALIGN=top>
<td>Home</td>
<td>ESC [ 7 ~</td>
<td>ESC [ 7 $</td>
<td>ESC [ 7 ^</td>
<td>ESC [ 7 @
</td>
</tr>
<tr VALIGN=top>
<td>End</td>
<td>ESC [ 8 ~</td>
<td>ESC [ 8 $</td>
<td>ESC [ 8 ^</td>
<td>ESC [ 8 @
</td>
</tr>
<tr VALIGN=top>
<td>Delete</td>
<td>ESC [ 3 ~</td>
<td>ESC [ 3 $</td>
<td>ESC [ 3 ^</td>
<td>ESC [ 3 @
</td>
</tr>
<tr VALIGN=top>
<td>F1</td>
<td>ESC [ 11 ~</td>
<td>ESC [ 23 ~</td>
<td>ESC [ 11 ^</td>
<td>ESC [ 23 ^
</td>
</tr>
<tr VALIGN=top>
<td>F2</td>
<td>ESC [ 12 ~</td>
<td>ESC [ 24 ~</td>
<td>ESC [ 12 ^</td>
<td>ESC [ 24 ^
</td>
</tr>
<tr VALIGN=top>
<td>F3</td>
<td>ESC [ 13 ~</td>
<td>ESC [ 25 ~</td>
<td>ESC [ 13 ^</td>
<td>ESC [ 25 ^
</td>
</tr>
<tr VALIGN=top>
<td>F4</td>
<td>ESC [ 14 ~</td>
<td>ESC [ 26 ~</td>
<td>ESC [ 14 ^</td>
<td>ESC [ 26 ^
</td>
</tr>
<tr VALIGN=top>
<td>F5</td>
<td>ESC [ 15 ~</td>
<td>ESC [ 28 ~</td>
<td>ESC [ 15 ^</td>
<td>ESC [ 28 ^
</td>
</tr>
<tr VALIGN=top>
<td>F6</td>
<td>ESC [ 17 ~</td>
<td>ESC [ 29 ~</td>
<td>ESC [ 17 ^</td>
<td>ESC [ 29 ^
</td>
</tr>
<tr VALIGN=top>
<td>F7</td>
<td>ESC [ 18 ~</td>
<td>ESC [ 31 ~</td>
<td>ESC [ 18 ^</td>
<td>ESC [ 31 ^
</td>
</tr>
<tr VALIGN=top>
<td>F8</td>
<td>ESC [ 19 ~</td>
<td>ESC [ 32 ~</td>
<td>ESC [ 19 ^</td>
<td>ESC [ 32 ^
</td>
</tr>
<tr VALIGN=top>
<td>F9</td>
<td>ESC [ 20 ~</td>
<td>ESC [ 33 ~</td>
<td>ESC [ 20 ^</td>
<td>ESC [ 33 ^
</td>
</tr>
<tr VALIGN=top>
<td>F10</td>
<td>ESC [ 21 ~</td>
<td>ESC [ 34 ~</td>
<td>ESC [ 21 ^</td>
<td>ESC [ 34 ^
</td>
</tr>
<tr VALIGN=top>
<td>F11</td>
<td>ESC [ 23 ~</td>
<td>ESC [ 23 $</td>
<td>ESC [ 23 ^</td>
<td>ESC [ 23 @
</td>
</tr>
<tr VALIGN=top>
<td>F12</td>
<td>ESC [ 24 ~</td>
<td>ESC [ 24 $</td>
<td>ESC [ 24 ^</td>
<td>ESC [ 24 @
</td>
</tr>
<tr VALIGN=top>
<td>F13</td>
<td>ESC [ 25 ~</td>
<td>ESC [ 25 $</td>
<td>ESC [ 25 ^</td>
<td>ESC [ 25 @
</td>
</tr>
<tr VALIGN=top>
<td>F14</td>
<td>ESC [ 26 ~</td>
<td>ESC [ 26 $</td>
<td>ESC [ 26 ^</td>
<td>ESC [ 26 @
</td>
</tr>
<tr VALIGN=top>
<td>F15 (Help)</td>
<td>ESC [ 28 ~</td>
<td>ESC [ 28 $</td>
<td>ESC [ 28 ^</td>
<td>ESC [ 28 @
</td>
</tr>
<tr VALIGN=top>
<td>F16 (Menu)</td>
<td>ESC [ 29 ~</td>
<td>ESC [ 29 $</td>
<td>ESC [ 29 ^</td>
<td>ESC [ 29 @
</td>
</tr>
<tr VALIGN=top>
<td>F17</td>
<td>ESC [ 31 ~</td>
<td>ESC [ 31 $</td>
<td>ESC [ 31 ^</td>
<td>ESC [ 31 @
</td>
</tr>
<tr VALIGN=top>
<td>F18</td>
<td>ESC [ 32 ~</td>
<td>ESC [ 32 $</td>
<td>ESC [ 32 ^</td>
<td>ESC [ 32 @
</td>
</tr>
<tr VALIGN=top>
<td>F19</td>
<td>ESC [ 33 ~</td>
<td>ESC [ 33 $</td>
<td>ESC [ 33 ^</td>
<td>ESC [ 33 @
</td>
</tr>
<tr VALIGN=top>
<td>F20</td>
<td>ESC [ 34 ~</td>
<td>ESC [ 34 $</td>
<td>ESC [ 34 ^</td>
<td>ESC [ 34 @
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Application
</td>
</tr>
<tr VALIGN=top>
<td>Up</td>
<td>ESC [ A</td>
<td>ESC [ a</td>
<td>ESC O a</td>
<td>ESC O A
</td>
</tr>
<tr VALIGN=top>
<td>Down</td>
<td>ESC [ B</td>
<td>ESC [ b</td>
<td>ESC O b</td>
<td>ESC O B
</td>
</tr>
<tr VALIGN=top>
<td>Right</td>
<td>ESC [ C</td>
<td>ESC [ c</td>
<td>ESC O c</td>
<td>ESC O C
</td>
</tr>
<tr VALIGN=top>
<td>Left</td>
<td>ESC [ D</td>
<td>ESC [ d</td>
<td>ESC O d</td>
<td>ESC O D
</td>
</tr>
<tr VALIGN=top>
<td>KP_Enter</td>
<td>^M</td>
<td></td>
<td></td>
<td>ESC O M
</td>
</tr>
<tr VALIGN=top>
<td>KP_F1</td>
<td>ESC O P</td>
<td></td>
<td></td>
<td>ESC O P
</td>
</tr>
<tr VALIGN=top>
<td>KP_F2</td>
<td>ESC O Q</td>
<td></td>
<td></td>
<td>ESC O Q
</td>
</tr>
<tr VALIGN=top>
<td>KP_F3</td>
<td>ESC O R</td>
<td></td>
<td></td>
<td>ESC O R
</td>
</tr>
<tr VALIGN=top>
<td>KP_F4</td>
<td>ESC O S</td>
<td></td>
<td></td>
<td>ESC O S
</td>
</tr>
<tr VALIGN=top>
<td>KP_Multiply</td>
<td>*</td>
<td></td>
<td></td>
<td>ESC O j
</td>
</tr>
<tr VALIGN=top>
<td>KP_Add</td>
<td>+</td>
<td></td>
<td></td>
<td>ESC O k
</td>
</tr>
<tr VALIGN=top>
<td>KP_Separator</td>
<td>,</td>
<td></td>
<td></td>
<td>ESC O l
</td>
</tr>
<tr VALIGN=top>
<td>KP_Subtract</td>
<td>&#8211;</td>
<td></td>
<td></td>
<td>ESC O m
</td>
</tr>
<tr VALIGN=top>
<td>KP_Decimal</td>
<td>.</td>
<td></td>
<td></td>
<td>ESC O n
</td>
</tr>
<tr VALIGN=top>
<td>KP_Divide</td>
<td>/</td>
<td></td>
<td></td>
<td>ESC O o
</td>
</tr>
<tr VALIGN=top>
<td>KP_0</td>
<td>0</td>
<td></td>
<td></td>
<td>ESC O p
</td>
</tr>
<tr VALIGN=top>
<td>KP_1</td>
<td>1</td>
<td></td>
<td></td>
<td>ESC O q
</td>
</tr>
<tr VALIGN=top>
<td>KP_2</td>
<td>2</td>
<td></td>
<td></td>
<td>ESC O r
</td>
</tr>
<tr VALIGN=top>
<td>KP_3</td>
<td>3</td>
<td></td>
<td></td>
<td>ESC O s
</td>
</tr>
<tr VALIGN=top>
<td>KP_4</td>
<td>4</td>
<td></td>
<td></td>
<td>ESC O t
</td>
</tr>
<tr VALIGN=top>
<td>KP_5</td>
<td>5</td>
<td></td>
<td></td>
<td>ESC O u
</td>
</tr>
<tr VALIGN=top>
<td>KP_6</td>
<td>6</td>
<td></td>
<td></td>
<td>ESC O v
</td>
</tr>
<tr VALIGN=top>
<td>KP_7</td>
<td>7</td>
<td></td>
<td></td>
<td>ESC O w
</td>
</tr>
<tr VALIGN=top>
<td>KP_8</td>
<td>8</td>
<td></td>
<td></td>
<td>ESC O x
</td>
</tr>
<tr VALIGN=top>
<td>KP_9</td>
<td>9</td>
<td></td>
<td></td>
<td>ESC O y
</td>
</tr>
</table>
<h2>Configure Options</h2>
<p>General hint: if you get compile errors, then likely your configuration hasn&#8217;t been tested well. Either try with <tt>&quot;--enable-everything&quot;</tt> or use the default configuration (i.e. no <tt>&quot;--enable-xxx&quot;</tt> or <tt>&quot;--disable-xxx&quot;</tt> switches). Of course, you should always report when a combination doesn&#8217;t work, so it can be fixed. Marc Lehmann &lt;rxvt [at] schmorp.de&gt;. </p>
<p> All</p>
<dl>
<dt>&#8211;enable-everything</p>
<dd>Add (or remove) support for all non-multichoice options listed in <tt>&quot;./configure --help&quot;</tt>, except for <tt>&quot;--enable-assert&quot;</tt> and <tt>&quot;--enable-256-color&quot;</tt>. </p>
<p> You can specify this and then disable options you do not like by <i>following</i> this with the appropriate <tt>&quot;--disable-...&quot;</tt> arguments, or you can start with a minimal configuration by specifying <tt>&quot;--disable-everything&quot;</tt> and than adding just the <tt>&quot;--enable-...&quot;</tt> arguments you want.</p>
<dt>&#8211;enable-xft (default: on)</p>
<dd>Add support for Xft (anti-aliased, among others) fonts. Xft fonts are slower and require lots of memory, but as long as you don&#8217;t use them, you don&#8217;t pay for them.</p>
<dt>&#8211;enable-font-styles (default: on)</p>
<dd>Add support for <code>bold</code>, <i>italic</i> and bold italic font styles. The fonts can be set manually or automatically.</p>
<dt>&#8211;with-codesets=CS,&#8230; (default: all)</p>
<dd>Compile in support for additional codeset (encoding) groups (<tt>&quot;eu&quot;</tt>, <tt>&quot;vn&quot;</tt> are always compiled in, which includes most 8-bit character sets). These codeset tables are used for driving X11 core fonts, they are not required for Xft fonts, although having them compiled in lets rxvt-unicode choose replacement fonts more intelligently. Compiling them in will make your binary bigger (all of together cost about 700kB), but it doesn&#8217;t increase memory usage unless you use a font requiring one of these encodings. </p>
<table>
<tr VALIGN=top>
<td>all</td>
<td>all available codeset groups
</td>
</tr>
<tr VALIGN=top>
<td>zh</td>
<td>common chinese encodings
</td>
</tr>
<tr VALIGN=top>
<td>zh_ext</td>
<td>rarely used but very big chinese encodings
</td>
</tr>
<tr VALIGN=top>
<td>jp</td>
<td>common japanese encodings
</td>
</tr>
<tr VALIGN=top>
<td>jp_ext</td>
<td>rarely used but big japanese encodings
</td>
</tr>
<tr VALIGN=top>
<td>kr</td>
<td>korean encodings
</td>
</tr>
</table>
<dt>&#8211;enable-xim (default: on)</p>
<dd>Add support for <font SIZE="-1">XIM </font>(X Input Method) protocol. This allows using alternative input methods (e.g. kinput2) and will also correctly set up the input for people using dead keys or compose keys.</p>
<dt>&#8211;enable-unicode3 (default: off)</p>
<dd>Recommended to stay off unless you really need non-BMP characters. </p>
<p> Enable direct support for displaying unicode codepoints above 65535 (the basic multilingual page). This increases storage requirements per character from 2 to 4 bytes. X11 fonts do not yet support these extra characters, but Xft does. </p>
<p> Please note that rxvt-unicode can store unicode code points &gt;65535 even without this flag, but the number of such characters is limited to a few thousand (shared with combining characters, see next switch), and right now rxvt-unicode cannot display them (input/output and cut&amp;paste still work, though).</p>
<dt>&#8211;enable-combining (default: on)</p>
<dd>Enable automatic composition of combining characters into composite characters. This is required for proper viewing of text where accents are encoded as separate unicode characters. This is done by using precomposed characters when available or creating new pseudo-characters when no precomposed form exists. </p>
<p> Without &#8211;enable-unicode3, the number of additional precomposed characters is somewhat limited (the 6400 private use characters will be (ab-)used). With &#8211;enable-unicode3, no practical limit exists. </p>
<p> This option will also enable storage (but not display) of characters beyond plane 0 (&gt;65535) when &#8211;enable-unicode3 was not specified. </p>
<p> The combining table also contains entries for arabic presentation forms, but these are not currently used. Bug me if you want these to be used (and tell me how these are to be used&#8230;).</p>
<dt>&#8211;enable-fallback[=CLASS] (default: Rxvt)</p>
<dd>When reading resource settings, also read settings for class <font SIZE="-1">CLASS.</font> To disable resource fallback use &#8211;disable-fallback.</p>
<dt>&#8211;with-res-name=NAME (default: urxvt)</p>
<dd>Use the given name as default application name when reading resources. Specify &#8211;with-res-name=rxvt to replace rxvt.</p>
<dt>&#8211;with-res-class=CLASS (default: URxvt)</p>
<dd>Use the given class as default application class when reading resources. Specify &#8211;with-res-class=Rxvt to replace rxvt.</p>
<dt>&#8211;enable-utmp (default: on)</p>
<dd>Write user and tty to utmp file (used by programs like <i>w</i>) at start of rxvt execution and delete information when rxvt exits.</p>
<dt>&#8211;enable-wtmp (default: on)</p>
<dd>Write user and tty to wtmp file (used by programs like <i>last</i>) at start of rxvt execution and write logout when rxvt exits. This option requires &#8211;enable-utmp to also be specified.</p>
<dt>&#8211;enable-lastlog (default: on)</p>
<dd>Write user and tty to lastlog file (used by programs like <i>lastlogin</i>) at start of rxvt execution. This option requires &#8211;enable-utmp to also be specified.</p>
<dt>&#8211;enable-pixbuf (default: on)</p>
<dd>Add support for GDK-PixBuf to be used for background images. It adds support for many file formats including <font SIZE="-1">JPG, PNG, TIFF, GIF, XPM, BMP, ICO</font> and <font SIZE="-1">TGA.</font></p>
<dt>&#8211;enable-startup-notification (default: on)</p>
<dd>Add support for freedesktop startup notifications. This allows window managers to display some kind of progress indicator during startup.</p>
<dt>&#8211;enable-transparency (default: on)</p>
<dd>Add support for using the root pixmap as background to simulate transparency. Note that this feature depends on libXrender and on the availability of the <font SIZE="-1">RENDER</font> extension in the X server.</p>
<dt>&#8211;enable-fading (default: on)</p>
<dd>Add support for fading the text when focus is lost.</p>
<dt>&#8211;enable-rxvt-scroll (default: on)</p>
<dd>Add support for the original rxvt scrollbar.</p>
<dt>&#8211;enable-next-scroll (default: on)</p>
<dd>Add support for a NeXT-like scrollbar.</p>
<dt>&#8211;enable-xterm-scroll (default: on)</p>
<dd>Add support for an Xterm-like scrollbar.</p>
<dt>&#8211;disable-backspace-key</p>
<dd>Removes any handling of the backspace key by us &#8211; let the X server do it.</p>
<dt>&#8211;disable-delete-key</p>
<dd>Removes any handling of the delete key by us &#8211; let the X server do it.</p>
<dt>&#8211;disable-resources</p>
<dd>Removes any support for resource checking.</p>
<dt>&#8211;disable-swapscreen</p>
<dd>Remove support for secondary/swap screen.</p>
<dt>&#8211;enable-frills (default: on)</p>
<dd>Add support for many small features that are not essential but nice to have. Normally you want this, but for very small binaries you may want to disable this. </p>
<p> A non-exhaustive list of features enabled by <tt>&quot;--enable-frills&quot;</tt> (possibly in combination with other switches) is: </p>
<pre> MWM-hints
 EWMH-hints (pid, utf8 names) and protocols (ping)
 urgency hint
 separate underline colour (-underlineColor)
 settable border widths and borderless switch (-w, -b, -bl)
 visual depth selection (-depth)
 settable extra linespacing (-lsp)
 iso-14755 5.1 (basic) support
 tripleclickwords (-tcw)
 settable insecure mode (-insecure)
 keysym remapping support
 cursor blinking and underline cursor (-bc, -uc)
 XEmbed support (-embed)
 user-pty (-pty-fd)
 hold on exit (-hold)
 compile in built-in block graphics
 skip builtin block graphics (-sbg)
 separate highlight colour (-highlightColor, -highlightTextColor)
 extended mouse reporting modes (1005 and 1015).
 visual selection via -visual and -depth.</pre>
<p>It also enables some non-essential features otherwise disabled, such as: </p>
<pre> some round-trip time optimisations
 nearest colour allocation on pseudocolor screens
 UTF8_STRING support for selection
 sgr modes 90..97 and 100..107
 backindex and forwardindex escape sequences
 view change/zero scrollback escape sequences
 locale switching escape sequence
 window op and some xterm/OSC escape sequences
 rectangular selections
 trailing space removal for selections
 verbose X error handling</pre>
<dt>&#8211;enable-iso14755 (default: on)</p>
<dd>Enable extended <font SIZE="-1">ISO 14755</font> support (see <a href="/docs/linux/man/1-urxvt/">urxvt</a>(1)). Basic support (section 5.1) is enabled by <tt>&quot;--enable-frills&quot;</tt>, while support for 5.2, 5.3 and 5.4 is enabled with this switch.</p>
<dt>&#8211;enable-keepscrolling (default: on)</p>
<dd>Add support for continual scrolling of the display when you hold the mouse button down on a scrollbar arrow.</p>
<dt>&#8211;enable-selectionscrolling (default: on)</p>
<dd>Add support for scrolling when the selection moves to the top or bottom of the screen.</p>
<dt>&#8211;enable-mousewheel (default: on)</p>
<dd>Add support for scrolling via mouse wheel or buttons 4 &amp; 5.</p>
<dt>&#8211;enable-slipwheeling (default: on)</p>
<dd>Add support for continual scrolling (using the mouse wheel as an accelerator) while the control key is held down. This option requires &#8211;enable-mousewheel to also be specified.</p>
<dt>&#8211;enable-smart-resize (default: off)</p>
<dd>Add smart growth/shrink behaviour when resizing. This should keep the window corner which is closest to a corner of the screen in a fixed position.</p>
<dt>&#8211;enable-text-blink (default: on)</p>
<dd>Add support for blinking text.</p>
<dt>&#8211;enable-pointer-blank (default: on)</p>
<dd>Add support to have the pointer disappear when typing or inactive.</p>
<dt>&#8211;enable-perl (default: on)</p>
<dd>Enable an embedded perl interpreter. See the <code>urxvt</code><a href="/docs/linux/man/3-perl/">perl</a><code>(3)</code> manpage for more info on this feature, or the files in <i>src/perl/</i> for the extensions that are installed by default. The perl interpreter that is used can be specified via the <tt>&quot;PERL&quot;</tt> environment variable when running configure. Even when compiled in, perl will <i>not</i> be initialised when all extensions have been disabled <tt>&quot;-pe &quot;&quot; --perl-ext-common &quot;&quot;&quot;</tt>, so it should be safe to enable from a resource standpoint.</p>
<dt>&#8211;enable-assert (default: off)</p>
<dd>Enables the assertions in the code, normally disabled. This switch is only useful when developing rxvt-unicode.</p>
<dt>&#8211;enable-256-color (default: off)</p>
<dd>Force use of so-called 256 colour mode, to work around buggy applications that do not support termcap/terminfo, or simply improve support for applications hardcoding the xterm 256 colour table. </p>
<p> This switch breaks termcap/terminfo compatibility to <tt>&quot;TERM=rxvt-unicode&quot;</tt>, and consequently sets <tt>&quot;TERM&quot;</tt> to <tt>&quot;rxvt-unicode-256color&quot;</tt> by default (<i>doc/etc/</i> contains termcap/terminfo definitions for both). </p>
<p> It also results in higher memory usage and can slow down urxvt dramatically when more than six fonts are in use by a terminal instance.</p>
<dt>&#8211;with-name=NAME (default: urxvt)</p>
<dd>Set the basename for the installed binaries, resulting in <tt>&quot;urxvt&quot;</tt>, <tt>&quot;urxvtd&quot;</tt> etc.). Specify <tt>&quot;--with-name=rxvt&quot;</tt> to replace with <tt>&quot;rxvt&quot;</tt>.</p>
<dt>&#8211;with-term=NAME (default: rxvt-unicode)</p>
<dd>Change the environmental variable for the terminal to <font SIZE="-1">NAME.</font></p>
<dt>&#8211;with-terminfo=PATH</p>
<dd>Change the environmental variable for the path to the terminfo tree to <font SIZE="-1">PATH.</font></p>
<dt>&#8211;with-x</p>
<dd>Use the X Window System (pretty much default, eh?).</dl>
<h2>Authors</h2>
<p>Marc Lehmann &lt;rxvt [at] schmorp.de&gt; converted this document to pod and reworked it from the original Rxvt documentation, which was done by Geoff Wing &lt;gcw [at] pobox.com&gt;, who in turn used the XTerm documentation and other sources.</p>
