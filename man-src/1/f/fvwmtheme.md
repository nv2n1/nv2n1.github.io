---
title: "fvwmtheme(1)"
name: "fvwmtheme"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fvwmtheme/"
description: "FvwmTheme – an fvwm module for managing the appearance of fvwm and its modules"
---

<p>FvwmTheme &#8211; an fvwm module for managing the appearance of fvwm and its modules</p>
<h2>Synopsis</h2>
<p>ModuleSynchronous Timeout 5 FvwmTheme </p>
<p> <code>FvwmTheme</code> can only be invoked by fvwm. Command line invocation of the FvwmTheme module will not work. </p>
<h2>Description</h2>
<p>FvwmTheme creates appearance resources that may be shared by fvwm and other modules. It reads an initial configuration and also reacts to configuration commands and messages sent from fvwm so that the resources can be dynamically changed. </p>
<h2>Invocation</h2>
<p>Starting with 2.5.1, FvwmTheme is obsolete, please read fvwm man page about the built-in colorsets solution. However, all options are still the same, so this man page defines the exact Colorset syntax. </p>
<p> FvwmTheme must be spawned as a module by fvwm. </p>
<p> It is highly suggested that FvwmTheme is invoked before any other modules that use the colorsets provided by FvwmTheme. Thus FvwmTheme has to be invoked with the &#8216;ModuleSynchronous&#8217; command by inserting the line &#8216;ModuleSynchronous Timeout 5 FvwmTheme&#8217; in the .fvwm2rc file right after the <i>ImagePath</i> has been defined. Invoking FvwmTheme from the <i>InitFunction</i>, <i>StartFunction</i> or <i>RestartFunction</i> or later can cause excessive redrawing of already running modules. It is highly suggested that the configuration lines for FvwmTheme appear in the configuration file before FvwmTheme is started. You can find a proper sample fvwm setup at the end of this document. It is pointless to run more than one FvwmTheme so there is no provision for using an alias name. </p>
<h2>Configuration Options</h2>
<p>FvwmTheme supports some configuration options. </p>
<dl>
<dt>*FvwmTheme: Colorset <i>n</i> <i>options</i></p>
<dd>Creates or modifies colorset <i>n</i>. Each colorset has four colors, an optional pixmap and an optional shape mask. The four colors are used by modules as the foreground, background, highlight and shadow colors. When a colorset is created it defaults to a foreground of black and background of gray. The background and foreground are marked as &quot;average&quot; and &quot;contrast&quot; (see later) so that just specifying a pixmap or gradient gives sensible results. </p>
<p> Warning: The highest colorset number used determines memory consumption. Thus if you define &#8216;Colorset 100000&#8217;, the memory for 100001 colorsets is used. Keep your colorset numbers as small as possible. </p>
<p> <i>options</i> is a comma separated list containing some of the keywords: fg, Fore, Foreground, bg, Back, Background, hi, Hilite, Hilight, sh, Shade, Shadow, fgsh, Pixmap, TiledPixmap, AspectPixmap, Transparent, RootTransparent, Shape, TiledShape, AspectShape, NoShape, ?Gradient, Tint, fgTint, bgTint, Alpha, fgAlpha, Dither, NoDither, IconTint, IconAlpha, NoShape and Plain. </p>
<p> <i>fg</i>, <i>Fore</i> and <i>Foreground</i> take a color name as an argument and set the foreground color. The special name <i>Contrast</i> may be used to select a color that contrasts well with the background color. To reset the foreground color to the default value you can simply omit the color name. </p>
<p> <i>bg</i>, <i>Back</i> and <i>Background</i> take a color name as an argument and set the background color. It also sets the highlight and shadow colors to values that give a 3d effect unless these have been explicitly set with the options below. The special name <i>Average</i> may be used to select a color that is the average color of the pixmap. If the pixmap is tinted with the <i>Tint</i> option, the tint is not taken in account in the computation of the average color. You should use the <i>bgTint</i> option to get the &quot;real&quot; average color. The background color is reset to the default value if the color name is omitted. </p>
<p> <i>hi</i>, <i>Hilite</i> and <i>Hilight</i> take a color name as an argument and set the highlight color. If the highlight color is not explicitly set, the default is to calculate it from the background color. To switch back to the default behavior the color name can be omitted. </p>
<p> <i>sh</i>, <i>Shade</i> and <i>Shadow</i> take a color name as an argument and set the shadow color. If the shadow color is not explicitly set, the default is to calculate it from the background color. To switch back to the default behavior the color name can be omitted. </p>
<p> <i>fgsh</i> takes a color name as an argument and sets the color used by the shadowing font effect. See the <code>FONT SHADOW EFFECTS</code> section of the fvwm man page. By default this color is computed from the foreground and background colors. To switch back to the default the color name can be omitted. </p>
<p> <i>Pixmap</i>, <i>TiledPixmap</i> and <i>AspectPixmap</i> take a file name as an argument, search the <i>ImagePath</i> and use it as the background pixmap. Any transparent parts are filled with the background color. Not specifying a file name removes any existing one from the colorset. <i>TiledPixmap</i> produces repeated copies of the image with no scaling, <i>Pixmap</i> causes the image to be stretched to fit whatever object the colorset is applied to and <i>AspectPixmap</i> stretches to fit but retains the image aspect ratio. </p>
<p> <i>Transparent</i> tries to create a transparent background pixmap. The pixmap may be used as a window background to achieve root transparency. For this you should use the <code>ParentalRelativity</code> fvwm style. The root background change may be detected or not, this depends on the program used to set the background. If you use fvwm-root, xsetbg (xli), FvwmBacker with a solid or a colorset colors or a recent version of Esetroot (&gt;= 9.2) a background change should be detected. If background changes are not detected (e.g., if you use xv or xsetroot) you can force detection by using the -d option of fvwm-root: </p>
<pre>xv -root -quit mybg.png; fvwm-root -d</pre>
<p>Due to the way X implements transparency no guarantees can be made that the desired effect can be achieved. The application may even crash. If you experience any problems with this option, do not use it. </p>
<p> Using outline move and resize (see the <code>OpaqueMoveSize</code> command and the <i>ResizeOpaque</i> style) as well as setting the <i>WindowShadeShrinks</i> style may help. The transparency achieved with <i>Transparent</i> depends on whether the colorset is applied to the foreground or the background of a window. In the second case the transparency is relative to the parent window of the window on which the colorset is defined. For example: </p>
<pre>Colorset 12 VGradient 200 grey30 grey60
Colorset 17 Transparent
*FvwmIconMan: Colorset 12
*FvwmIconMan: PlainColorset 17</pre>
<p>gives an IconMan with a vertical grey gradient background and the buttons use the background (by transparency). To obtain a (root) transparent IconMan: </p>
<pre>Colorset 12 Transparent
Colorset 17 Transparent
Colorset 18 Transparent
Colorset 19 Transparent
...
*FvwmIconMan: Colorset 12
*FvwmIconMan: PlainColorset 17
*FvwmIconMan: FocusColorset 18
*FvwmIconMan: IconColorset 19</pre>
<p>The Colorset IconMan option defines the IconMan window background, but the PlainColorset and the FocusColorset are drawn on the foreground. So, the transparency of the IconMan buttons is achieved by drawing nothing. Now if this IconMan is swallowed in an FvwmButtons as: </p>
<pre>FvwmButtons:(Colorset 10, Swallow &quot;FvwmIconMan&quot; 'FvwmIconMan')</pre>
<p>then, IconMan become a child of FvwmButtons and it is transparent relative to FvwmButtons. So, in this case IconMan uses Colorset 10 as background. If you want root transparency use the <i>RootTransparent</i> option. FvwmButtons, FvwmIconMan, FvwmIdent, FvwmScroll and FvwmTaskBar are relatively simple. There is one main colorset option which defines the background of the window and the other colorsets (if any) are drawn on the foreground. The case of FvwmWinList and FvwmProxy are simpler. With FvwmWinList all the colorsets are drawn on the foreground and with FvwmProxy the two colorsets refer to the window backgrounds. FvwmPager is more complicated as almost everything in the pager are windows with some parental relations (the mini windows are the child and the desktops are the parents and all this is complicated by the hilighted page). So, the colorsets apply to the background of these windows. You should experiment. For FvwmForm and FvwmScript the situation is similar. There is a main window (a child of the root window) which corresponds to the main colorset and most of the widgets are windows which are children of the main window. <i>Tint</i> may work or not with the <i>Transparent</i> option. When the colorset is drawn on the foreground <i>Tint</i> should work. In the other cases, tinting works in some exceptional cases (and may be very slow). Tinting may work with fvwm menu (without animation). In the other case tinting may work if your X server has backing store enabled (try xdpyinfo to see if this the case). But, there is a chance that the backing store support of your X server does not work well with the terrible hack used to Tint the ParentRelative Pixmap. So, to get tinted root transparency it is more safe to use the <i>RootTransparent</i> option. </p>
<p> <i>RootTransparent</i> [ <i>buffer</i> ] creates a root transparent background. To make this option work, you must use an Esetroot compatible program, fvwm-root with the &#8211;retain-pixmap option or FvwmBacker with the RetainPixmap option (and colorset or solid backgrounds). The <i>buffer</i> keyword is useful only when the <i>Tint</i> option is used too. This speeds up creation of windows which use the colorset (useful for fvwm menus) at the cost of memory usage. It also speeds up opaque move and resize which can be unacceptably slow without <i>buffer</i>. However, this option may add a lot of memory to your X server (depending on the size of the image used to set the background). In summary, using outline move and resize for modules which use such a colorset may be a good idea. </p>
<p> <i>Shape</i>, <i>TiledShape</i> and <i>AspectShape</i> take a file name as an argument, search the <i>ImagePath</i> and use it as the shape bitmap. <i>TiledShape</i> produces repeated copies of the bitmap with no scaling, <i>Shape</i> causes the bitmap to be stretched to fit whatever object the colorset is applied to and <i>AspectShape</i> stretches to fit but retains the bitmap aspect ratio. If the file is a pixmap in xpm format, the shape mask of the pixmap is used. </p>
<p> Warning: Due to the way X11 implements shapes and the implementation of the FvwmTheme module you cannot take back making windows shaped. You may have to restart fvwm or the shaped application. </p>
<p> <i>?Gradient &#8230;</i> creates a pixmap and stretches it to fit the window. <i>?Gradient</i> may be one of HGradient, VGradient, DGradient, BGradient, SGradient, CGradient, RGradient or YGradient. The gradient types are as follows: H is horizontal; V is vertical; D is diagonal from top left to bottom right; B is a backwards diagonal from bottom left to top right; S is concentric squares; C is concentric circles; R is a radar like pattern and Y is a Yin Yang style (but without the dots, we are not <i>that</i> mad). Please refer to the <i>COLOR GRADIENTS</i> section in the <i>fvwm</i> man page for the syntax of gradients. </p>
<p> <i>Tint</i> takes 2 arguments, a color and a percentage between 0 and 100. It causes the image defined using <i>?Pixmap</i> or <i>?Gradient</i> to be tinted with the specified color using the percentage. If the image is transparent <i>Tint</i> tints only the image part. Unfortunately, a colorset background specified using the <i>Transparent</i> option can give strange results. See the <i>Transparent</i> option for details. With no arguments this option removes the tint. </p>
<p> <i>fgTint</i> takes 2 arguments, a color and a percentage between 0 and 100. It causes the color defined using <i>fg</i> to be tinted with the specified color using the percentage. With no arguments this option removes the tint. </p>
<p> <i>bgTint</i> takes 2 arguments, a color and a percentage between 0 and 100. It causes the color defined using <i>bg</i> to be tinted with the specified color using the percentage. If the <i>sh</i> and <i>hi</i> colors are not specified, they are recomputed from the tinted bg color. With no arguments this option removes the tint. </p>
<p> <i>Alpha</i> takes a percentage between 0 and 100 as an argument. It causes fvwm to merge the image defined using <i>?Pixmap</i> or <i>?Gradient</i> with the <i>bg</i> color using the percentage. If the percentage is 0 the image is hidden and if it is 100 the image is displayed as usual (no merge). The default is 100 and it is restored if no argument is given. </p>
<p> <i>fgAlpha</i> takes a percentage between 0 and 100 as an argument. It causes fvwm to merge the text and the colorset background using the percentage. If the percentage is 0 the text is hidden and if it is 100 the text is displayed as usual (no merge). This option has an effect only with fonts loaded by Xft, see the <code>FONT NAMES AND FONT LOADING</code> section of fvwm man page. The default is 100 and it is restored if no argument is given. </p>
<p> <i>Dither</i> causes fvwm to dither the image defined using <i>?Pixmap</i> or <i>?Gradient.</i> This is useful only with displays with depth less than or equal to 16 (i.e., on displays which can only display less than 65537 colors at once). The dithering effect lets you simulate having more colors available that you actually have. <i>NoDither</i> causes fvwm to do not dither the images. <i>Dither</i> is the default if the depth is less than or equal to 8 (a screen with 256 colors or less). In depth 15 (32768 colors) and 16 (65536 colors), the default is <i>NoDither</i>, however this effect can be useful with images which contain a lot of close colors. For example a fine gradient will look more smooth. </p>
<p> <i>IconTint</i> takes 2 arguments, a color and a percentage between 0 and 100. It causes fvwm or a module to tint the &quot;icons&quot; which are rendered into the colorset background with the specified color using a percentage. Here &quot;icons&quot; means, fvwm Icons, fvwm menu icons, MiniIcons which represent applications in various modules, images loaded by modules (e.g., images specified by the <i>Icon</i> FvwmButtons button option) &#8230;etc. With no arguments this option removes the icon tint. </p>
<p> <i>IconAlpha</i> takes a percentage between 0 and 100 as an argument. It causes fvwm to merge the &quot;icons&quot; which are rendered into the colorset background using this percentage. The default is 100 and it is restored if no argument is given. </p>
<p> <i>Note</i>: It is equivalent to use &quot;Tint a_color rate&quot; and &quot;Alpha a&quot; if a = 100 and the bg color is a_color. This equivalence does not hold for IconAlpha and IconTint as the background can be an image or a gradient (and not a uniform color background). However, in some cases you can achieve (almost) the same effect by using IconTint in the place of IconAlpha. This is preferable as, in general, IconAlpha generates more redrawing than IconTint. </p>
<p> <i>NoShape</i> removes the shape mask from the colorset while <i>Plain</i> removes the background pixmap or gradient. </p>
</dl>
<h2>Commands</h2>
<p>The following fvwm command may be executed at any time to alter the colorsets. It may be bound to a menu item or typed into a module such as FvwmConsole. </p>
<dl>
<dt>SendToModule FvwmTheme Colorset <i>options</i></p>
<dd>The syntax is the same as the configuration option. </p>
</dl>
<h2>Examples</h2>
<pre>*FvwmTheme: Colorset 3 fg wheat, bg navy</pre>
<p>If necessary this creates colorsets 0, 1, 2 and 3 and then changes colorset 3 to have a foreground of wheat, a background of navy. </p>
<pre>*FvwmTheme: Colorset 3 bg &quot;navy blue&quot;</pre>
<p>changes the background color of colorset 3 to navy blue. The foreground and pixmap are unchanged. </p>
<pre>*FvwmTheme: Colorset 3 AspectPixmap large_murky_dungeon.xpm</pre>
<p>Causes depression. </p>
<pre>*FvwmTheme: Colorset 3 bg Average</pre>
<p>Sets the background color and the relief colors to match the background pixmap. This is the default setting but it must be used if a background color was specified and is now not required. </p>
<pre>*FvwmTheme: Colorset 3 YGradient 200 3 \
 blue 1000 navy 1 blue 1000 navy</pre>
<p>Adds a Yin Yang gradient background pixmap to colorset 3. If the background is set to average it is recomputed along with the foreground if that is set to contrast. </p>
<pre> #!/bin/sh
 FvwmCommand &quot;SendToModule FvwmTheme Colorset 7 fg navy, bg gray&quot;
 while true
 do
 FvwmCommand &quot;SendToModule FvwmTheme Colorset 7 fg gray&quot;
 sleep 1
 FvwmCommand &quot;SendToModule FvwmTheme Colorset 7 fg navy&quot;
 sleep 1
 done</pre>
<p>Makes colorset 7 blink. </p>
<p> The color names used in colorsets can be substituted in any fvwm command. Please refer to the <i>COMMAND EXPANSION</i> section in the fvwm man page and the example below for a description. </p>
<h2>Sample Fvwm Configuration</h2>
<p>Below you can find a fvwm configuration file that demonstrates the use of the FvwmTheme module. The order in which FvwmTheme and the other modules are configured and started is important. </p>
<pre> # where your images are
 ImagePath &lt;put your image path here&gt;
 #
 # FvwmTheme
 #
 # The FvwmTheme setup must be first in the config file,
 # right after the paths are set.
 #
 # Instead of the *FvwmTheme: Colorset... lines below you
 # could read in a file with these commands. So to change
 # your color scheme you can simply copy a different file
 # over your palette file and restart fvwm:
 #
 # Read /home/my_user_name/.fvwm/.fvwm_palette
 #
 # 0 = Default colors
 # 1 = Inactive windows
 # 2 = Active windows
 # 3 = Inactive menu entry and menu background
 # 4 = Active menu entry
 # 5 = greyed out menu entry (only bg used)
 # 6 = module foreground and background
 # 7 = hilight colors
 *FvwmTheme: Colorset 0 fg black, bg rgb:b4/aa/94
 *FvwmTheme: Colorset 1 fg black, bg rgb:a1/b2/c8
 *FvwmTheme: Colorset 2 fg black, bg rgb:da/9a/68
 *FvwmTheme: Colorset 3 fg black, bg rgb:b4/aa/94, \
 VGradient 100 dtcolor5 rgb:b4/aa/94
 *FvwmTheme: Colorset 4 fg black, bg rgb:b4/aa/94
 *FvwmTheme: Colorset 5 fg rgb:d2/bf/a8, \
 bg rgb:b4/aa/94
 *FvwmTheme: Colorset 6 fg black, bg rgb:b4/aa/94, \
 VGradient 100 dtcolor5 rgb:b4/aa/94
 *FvwmTheme: Colorset 7 fg black, bg rgb:94/ab/bf
 # run FvwmTheme before anything else is done
 ModuleSynchronous Timeout 5 FvwmTheme
 #
 # general setup
 #
 Style * Colorset 1
 Style * HilightColorset 2
 MenuStyle * MenuColorset 3
 MenuStyle * ActiveColorset 4
 MenuStyle * GreyedColorset 5
 #
 # Applications
 #
 AddToFunc InitFunction
 + I Exec exec xterm -fg $[fg.cs0] -bg $[bg.cs0]
 #
 # module setup
 #
 # ... more FvwmPager config lines ...
 *FvwmPager: Colorset * 6
 *FvwmPager: BalloonColorset * 6
 *FvwmPager: HilightColorset * 7
 *FvwmPager: WindowColorsets 1 2
 # ... more FvwmIconMan config lines ...
 *FvwmIconMan: Colorset 6
 *FvwmIconMan: FocusColorset 2
 *FvwmIconMan: FocusAndSelectColorset 2
 *FvwmIconMan: PlainColorset 6
 *FvwmIconMan: SelectColorset 6
 *FvwmIconMan: TitleColorset 6
 # ... more FvwmButtons config lines ...
 *FvwmButtons: Colorset 6
 # sample button passing color to xterm
 *FvwmButtons: (Title xterm, \
 Action &quot;Exec exec xterm -fg $[fg.cs6] -bg[bg.cs6]&quot;)
 # ... more FvwmWharf config lines ...
 *FvwmWharf: Colorset 6
 # ... more FvwmIdent config lines ...
 *FvwmIdent: Colorset 6
 # ... more FvwmWinList config lines ...
 *FvwmWinList: Colorset 1
 *FvwmWinList: FocusColorset 2
 *FvwmWinList: IconColorset 1
 # ... more FvwmTaskBar config lines ...
 *FvwmTaskBar: Colorset 6
 *FvwmTaskBar: IconColorset 6
 *FvwmTaskBar: TipsColorset 0</pre>
<p>If you need to have more colors and don&#8217;t want to reinvent the wheel, you may use the convention used in fvwm-themes, it defines the meaning of the first 40 colorsets for nearly all purposes: </p>
<p>&nbsp;<wbr><code><a rel="nofollow" href="http://fvwm-themes.sourceforge.net/doc/colorsets">http://fvwm-themes.sourceforge.net/doc/colorsets</a></code> </p>
<h2>Bugs</h2>
<p>Initialization of fvwm, FvwmTheme and the other modules is tricky. Please pay close attention to the text in the <i>INVOCATION</i> section. The example above demonstrates the proper way to get a FvwmTheme setup running. </p>
<h2>Author</h2>
<p>Prefers to remain anonymous. With help from Brad Giaccio and Dominik Vogt. </p>
<h2>Copyright</h2>
<p>Copyright (C) 1999 Joey Shutup. No guarantees or warranties or anything are provided or implied in any way whatsoever. Use this program at your own risk. Permission to use this program for any purpose is given, as long as the copyright is kept intact.</p>
