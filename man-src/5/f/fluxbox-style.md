---
title: "fluxbox-style(5)"
name: "fluxbox-style"
section: "5"
letter: "f"
url: "/docs/linux/man/5-fluxbox-style/"
description: "fluxbox-style – A comprehensive look at styles/themes for"
---

<p>fluxbox-style &#8211; A comprehensive look at styles/themes for </p>
<p><a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1).</p>
<h2>Synopsis</h2>
<p>This document describes various options available for fluxbox styles.</p>
<h2>Description</h2>
<p>What is a Style? </p>
<p> Styles, sometimes referred to as Themes, are a graphical overlay for the <a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1) window manager. If you wanted to get to know fluxbox, the styles would be the <i>look</i> of the <i>look and feel</i>. </p>
<p> Styles are simple ASCII text files that tell <a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1) how to generate the appearance of different components of the window manager. The default installation of <a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1) is shipped with many classic examples that show a great deal of what one could do. To use one of the standard styles navigate to the <i>System Styles</i> menu under your main <a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1) menu. </p>
<p> <a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1) uses its own graphics class to render its images on the fly. By using styles you can determine, at a great level of configurability, what your desktop will look like. Since <a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1) was derived from blackbox many often wonder if old themes will work on the latest releases of <a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1). Well they basically do, but you will have to tune them since the <a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1) code has changed quite a bit since the initial grab.</p>
<h2>Structure</h2>
<p>A style is made up of a few major components which then have their own sub-directives. The major components are as follows: </p>
<p> The <i>window.*</i> directives control the appearance of the window frames, <i>window.tab.*</i> controls the appearance of the window tabs, <i>menu.*</i> controls the appearance of the popup menu that you see when you right click on the desktop. <i>toolbar.*</i> is the bar you will see at the top or bottom of your screen. Finally the <i>slit.*</i> has options you can use to customize the appearance of the slit. However if you don&#8217;t set the slit directives specifically, the slit&#8217;s appearance is controlled by the toolbar directives instead. </p>
<p> To understand how the style mechanism works, it is nice to know a little about how X11 resources work. X11 resources consist of a key and a value. The key is constructed of several smaller keys (sometimes referred to as children), delimited by a period (.). Keys may also contain an asterisk (*) to serve as a wildcard, which means that one line of text will match several keys. This is useful for styles that are based on one or two colors. </p>
<p> A more complete reference to this can be found in <a href="/docs/linux/man/7-x/">X</a>(7), section <i>RESOURCES</i>.</p>
<h2>Location</h2>
<p>There are many places to store your styles, the most common is in your <i>~/.fluxbox/styles</i> directory. The initial installation will place the default styles in <i>/usr/local/share/fluxbox/styles</i> providing a basic usable configuration. </p>
<p> When creating your own style, create a directory (normally the name of your style) in <i>~/.fluxbox/styles/</i> (If the <i>styles</i> directory doesn&#8217;t exist, create that also). While there isn&#8217;t an official structure, it is common to create a directory named after your style and place your pixmaps directory (if required) in there along with a file called theme.cfg (may also be named style.cfg). This file is where you will construct your style using the components covered later in this manual page. An example of steps taken when beginning a style project of your own may look like: </p>
<dl>
<dd>
<pre>$ cd
$ mkdir -p ~/.fluxbox/styles/YourStyle/pixmaps
$ cd ~/.fluxbox/styles/YourStyle
$ nano theme.cfg</pre>
</dl>
<p> Output of a packaged style should look like the following: </p>
<dl>
<dd>
<pre>$ cd
$ tar -tjvf YourStyle.tar.bz2
 .fluxbox/styles/YourStyle/theme.cfg
 .fluxbox/styles/YourStyle/pixmaps
 .fluxbox/styles/YourStyle/pixmaps/stick.xpm
 ...</pre>
</dl>
<p> Of course, all of these are just preferences, <a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1) allows for the customization of many things, including how you handle your styles. Just remember, however, that if you plan to distribute your style you may find some community bickering if you don&#8217;t follow practices. :)</p>
<h2>Creating Your Style</h2>
<p>As discussed above, <a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1) allows you to configure its four main components: the toolbar, menus, slit and window decorations. Remember that you can customize the slit with its own directives, otherwise the slit will take the appearance of the toolbar. </p>
<p> Here are some quick examples to illustrate basic syntax: </p>
<dl>
<dd>
<pre>toolbar.clock.color: green</pre>
</dl>
<p> This sets the color resource of the toolbar clock to <i>green</i>. Another example: </p>
<dl>
<dd>
<pre>menu*color: rgb:3/4/5</pre>
</dl>
<p> This sets the color resource of the menu and all of its <i>children</i> to &#8216;rgb:3/4/5&#8217;. (For a description of color names, see <a href="/docs/linux/man/1-x/">X</a>(1).) So this one also applies to <i>menu.title.color</i> and <i>menu.frame.color</i>. And with </p>
<dl>
<dd>
<pre>*font: -b&amp;h-lucida-medium-r-normal-*-*-140-*</pre>
</dl>
<p> you set the font resource for all keys to this font name all at once (For information about the fonts installed on your system, you can use a program like <a href="/docs/linux/man/1-xfontsel/">xfontsel</a>(1), gtkfontsel, or <a href="/docs/linux/man/1-xlsfonts/">xlsfonts</a>(1).) </p>
<p> In the last example you will notice the wildcard (*) before font. In a Fluxbox style you can set a value with a wildcard. The example means that every font in the style will be what is specified. You can do this with any component/value. For example if you wanted all of the text to be one color you would do: </p>
<dl>
<dd>
<pre>*textColor: rgb:3/4/5</pre>
</dl>
<p> This means that you can setup a very simple style with very few properties. See the EXAMPLES below for an example of this in practice. <a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1) also allows you to override wildcards in your style. Lets take our example above and add an override for the toolbar.clock.textColor component: </p>
<dl>
<dd>
<pre>*textColor: rgb:3/4/5
toolbar.clock.textColor: rgb:255/0/0</pre>
</dl>
<p> With that all of the text will be <i>rgb:3/4/5</i> except the toolbar clock text which will be <i>rgb:255/0/0</i>. </p>
<p> Now what makes <a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1) so spectacular is its ability to render textures on the fly. A texture is a fillpattern that you see on some styles. Texture descriptions are specified directly to the key that they should apply to, e.g.: </p>
<dl>
<dd>
<pre>toolbar.clock: Raised Gradient Diagonal Bevel1
toolbar.clock.color: rgb:8/6/4
toolbar.clock.colorTo: rgb:4/3/2</pre>
</dl>
<p> Don&#8217;t worry, we will explain what these mean. A texture description consists of up to five fields, which are as follows: </p>
<p> <code>Flat | Raised | Sunken</code>. gives the component either a flat, raised or sunken appearance. </p>
<p> <code>Gradient | Solid</code>. tells <a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1) to draw either a solid color or a gradient texture. </p>
<p> <code>Horizontal | Vertical | Diagonal | Crossdiagonal | Pipecross | Elliptic | Rectangle | Pyramid</code>. Select one of these texture types. They only work when <code>Gradient</code> is specified. </p>
<p> <code>Interlaced</code>. tells <a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1) to interlace the texture (darken every other line). This option is most commonly used with gradiented textures, but it also works in solid textures. </p>
<p> <code>Bevel1 | Bevel2</code>. tells <a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1) which type of bevel to use. Bevel1 is the default bevel. The shading is placed on the edge of the image. Bevel2 is an alternative. The shading is placed one pixel in from the edge of the image. </p>
<p> Instead of a texture description, also the option <code>ParentRelative</code> is available, which makes the component appear as a part of its parent, e.g. totally transparent. </p>
<p> Or for even more possibilities Pixmap. If pixmap texture is specified (it might not be necessary on every occasion) the pixmap file is specified in a separate pixmap resource. </p>
<dl>
<dd>
<pre>toolbar.clock: pixmap
toolbar.clock.pixmap: clock_background.xpm</pre>
</dl>
<p> This feature might need some investigation, reports say that sometimes the resources color and colorTo must be set and then they may not be set. </p>
<p> All gradiented textures are composed of two color values: the <i>color</i> and <i>colorTo</i> resources. When <code>Interlaced</code> is used in <code>Solid</code> mode, the <i>colorTo</i> resource is used to find the interlacing color.</p>
<h2>Font Effects</h2>
<p>In addition to specifying the font-family and the font-weight via the supported font-rendering-engine (eg, Xft), <a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1) supports some effects: <i>halo</i> and <i>shadow</i>. To set the shadow effect: </p>
<dl>
<dd>
<pre>menu.title.font: sans-8:bold
menu.title.effect: shadow
menu.title.shadow.color: green
menu.title.shadow.x: 3
menu.title.shadow.y: 3</pre>
</dl>
<p> To set the halo effect: </p>
<dl>
<dd>
<pre>menu.title.font: sans-8:bold
menu.title.effect: halo
menu.title.halo.color: green</pre>
</dl>
<h3>Font Problems</h3>
<p>If you have problems installing fonts or getting them to work, you should read the docs page at xfree.org. Here is a link to one of these: m[blue]<code><a rel="nofollow" href="http://xfree.org/4.3.0/fonts2.html#3">http://xfree.org/4.3.0/fonts2.html#3</a></code>m[]</p>
<h2>Full Component List</h2>
<p>Here is the exhaustive component list for <a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1) styles. Each one is listed with their type of value required. Comments in a style file are preceded with an exclamation point (!) which we also use here so that these can be pasted into a new theme.cfg to be customized appropriately. Please note that in order to keep styles consistent it is often the practice of stylists to provide all of the theme-items in their style file even if they are not used. This allows the user the ease of changing different components.</p>
<h2>Window Options</h2>
<p>Many, many things you can do with window design in <a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1), below are your options. Have fun. </p>
<dl>
<dd>
<pre>-----------------------------------------
window.bevelWidth: &lt;integer&gt;
window.borderColor: &lt;color&gt;
window.borderWidth: &lt;integer&gt;
window.button.focus: &lt;texture type&gt;
window.button.focus.color: &lt;color&gt;
window.button.focus.colorTo: &lt;color&gt;
window.button.focus.picColor: &lt;color&gt;
window.button.focus.pixmap: &lt;filename&gt;
window.button.pressed: &lt;texture type&gt;
window.button.pressed.color: &lt;color&gt;
window.button.pressed.colorTo: &lt;color&gt;
window.button.pressed.pixmap: &lt;filename&gt;
window.button.unfocus: &lt;texture type&gt;
window.button.unfocus.color: &lt;color&gt;
window.button.unfocus.colorTo: &lt;color&gt;
window.button.unfocus.picColor: &lt;color&gt;
window.button.unfocus.pixmap: &lt;filename&gt;
window.close.pixmap: &lt;filename&gt;
window.close.pressed.pixmap: &lt;filename&gt;
window.close.unfocus.pixmap: &lt;filename&gt;
window.font: &lt;font&gt;
window.frame.focusColor: &lt;color&gt;
window.frame.unfocusColor: &lt;color&gt;
window.grip.focus: &lt;texture type&gt;
window.grip.focus.color: &lt;color&gt;
window.grip.focus.colorTo: &lt;color&gt;
window.grip.focus.pixmap: &lt;filename&gt;
window.grip.unfocus: &lt;texture type&gt;
window.grip.unfocus.color: &lt;color&gt;
window.grip.unfocus.colorTo: &lt;color&gt;
window.grip.unfocus.pixmap: &lt;filename&gt;
window.handle.focus: &lt;texture type&gt;
window.handle.focus.color: &lt;color&gt;
window.handle.focus.colorTo: &lt;color&gt;
window.handle.focus.pixmap: &lt;filename&gt;
window.handle.unfocus: &lt;texture type&gt;
window.handle.unfocus.color: &lt;color&gt;
window.handle.unfocus.colorTo: &lt;color&gt;
window.handle.unfocus.pixmap: &lt;filename&gt;
window.handleWidth: &lt;integer&gt;
window.iconify.pixmap: &lt;filename&gt;
window.iconify.pressed.pixmap: &lt;filename&gt;
window.iconify.unfocus.pixmap: &lt;filename&gt;
window.justify: &lt;{Left|Right|Center}&gt;
window.label.active: &lt;texture type&gt;
window.label.active.textColor: &lt;color&gt;
window.label.focus: &lt;texture type&gt;
window.label.focus.color: &lt;color&gt;
window.label.focus.colorTo: &lt;color&gt;
window.label.focus.pixmap: &lt;filename&gt;
window.label.unfocus: &lt;texture type&gt;
window.label.unfocus.color: &lt;color&gt;
window.label.unfocus.colorTo: &lt;color&gt;
window.label.unfocus.pixmap: &lt;filename&gt;
window.label.focus.textColor: &lt;color&gt;
window.label.unfocus.textColor: &lt;color&gt;
window.maximize.pixmap: &lt;filename&gt;
window.maximize.pressed.pixmap: &lt;filename&gt;
window.maximize.unfocus.pixmap: &lt;filename&gt;
window.roundCorners: &lt;{Top|Bottom}{Left|Right}&gt;
window.shade.pixmap: &lt;filename&gt;
window.shade.pressed.pixmap: &lt;filename&gt;
window.shade.unfocus.pixmap: &lt;filename&gt;
window.stick.pixmap: &lt;filename&gt;
window.stick.pressed.pixmap: &lt;filename&gt;
window.stick.unfocus.pixmap: &lt;filename&gt;
window.stuck.pixmap: &lt;filename&gt;
window.stuck.unfocus.pixmap: &lt;filename&gt;
window.lhalf.pixmap: &lt;filename&gt;
window.lhalf.unfocus.pixmap: &lt;filename&gt;
window.rhalf.pixmap: &lt;filename&gt;
window.rhalf.unfocus.pixmap: &lt;filename&gt;
window.title.focus: &lt;texture type&gt;
window.title.focus.color: &lt;color&gt;
window.title.focus.colorTo: &lt;color&gt;
window.title.focus.pixmap: &lt;filename&gt;
window.title.height: &lt;integer&gt;
window.title.unfocus: &lt;texture type&gt;
window.title.unfocus.color: &lt;color&gt;
window.title.unfocus.colorTo: &lt;color&gt;
window.title.unfocus.pixmap: &lt;filename&gt;
-----------------------------------------</pre>
</dl>
<h2>Menu Options</h2>
<p>Everything you need to make your menu look pretty. </p>
<dl>
<dd>
<pre>-----------------------------------------
menu.bevelWidth: &lt;integer&gt;
menu.borderColor: &lt;color&gt;
menu.borderWidth: &lt;integer&gt;
menu.bullet: &lt;{empty|square|triangle|diamond}&gt;
menu.bullet.position: &lt;{left|right}&gt;
menu.frame: &lt;texture type&gt;
menu.frame.color: &lt;color&gt;
menu.frame.colorTo: &lt;color&gt;
menu.frame.disableColor: &lt;color&gt;
menu.frame.font: &lt;font&gt;
menu.frame.justify: &lt;{Left|Right|Center}&gt;
menu.frame.pixmap: &lt;filename&gt;
menu.frame.textColor: &lt;color&gt;
menu.hilite: &lt;texture type&gt;
menu.hilite.color: &lt;color&gt;
menu.hilite.colorTo: &lt;color&gt;
menu.hilite.font: &lt;font&gt;
menu.hilite.justify: &lt;{left|center|right}&gt;
menu.hilite.pixmap: &lt;filename&gt;
menu.hilite.textColor: &lt;color&gt;
menu.itemHeight: &lt;integer&gt;
menu.title: &lt;texture type&gt;
menu.title.color: &lt;color&gt;
menu.title.colorTo: &lt;color&gt;
menu.title.font: &lt;font&gt;
menu.title.pixmap: &lt;filename&gt;
menu.title.textColor: &lt;color&gt;
menu.title.justify: &lt;{Left|Right|Center}&gt;
menu.titleHeight: &lt;integer&gt;
menu.roundCorners: &lt;{Top|Bottom}{Left|Right}&gt;
menu.selected.pixmap: &lt;filename&gt;
menu.submenu.pixmap: &lt;filename&gt;
menu.unselected.pixmap: &lt;filename&gt;
-----------------------------------------</pre>
</dl>
<h2>Background</h2>
<p>Every style must specify the background option. If you don&#8217;t want your style to change the user&#8217;s background, then use &#8216;background: none&#8217;. The options &#8216;centered&#8217;, &#8216;aspect&#8217;, &#8217;tiled&#8217;, and &#8216;fullscreen&#8217; require the &#8216;background.pixmap&#8217; resource to contain a valid file name. The &#8216;random&#8217; option requires &#8216;background.pixmap&#8217; to contain a valid directory name. For these options, <code><a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1)</code> will call <code><a href="/docs/linux/man/1-fbsetbg/">fbsetbg</a>(1)</code> to set the background. The options &#8216;gradient&#8217;, &#8216;solid&#8217;, and &#8216;mod&#8217; all require &#8216;background.color&#8217; to be set. &#8216;gradient&#8217; and &#8216;mod&#8217; both require &#8216;background.colorTo&#8217;. &#8216;mod&#8217; requires &#8216;background.modX&#8217; and &#8216;background.modY&#8217; to be set as well. These options will be passed to <code><a href="/docs/linux/man/1-fbsetroot/">fbsetroot</a>(1)</code> to set the background. The special option &#8216;unset&#8217; is for use in user overlay files only. It specifies that fbsetbg should never be run (by default, even when &#8216;none&#8217; is set in the overlay, fluxbox will try to run &#8220;fbsetbg -z&#8221; to restore the last wallpaper). </p>
<dl>
<dd>
<pre>background: centered|aspect|tiled|fullscreen|random|solid|gradient &lt;texture&gt;|mod|none|unset
background.pixmap: &lt;file or directory&gt;
background.color: &lt;color&gt;
background.colorTo: &lt;color&gt;
background.modX: &lt;integer&gt;
background.modY: &lt;integer&gt;</pre>
</dl>
<h2>Slit</h2>
<p>Here are all of the options for the slit. </p>
<dl>
<dd>
<pre>-----------------------------------------
slit: &lt;texture type&gt;
slit.bevelWidth: &lt;integer&gt;
slit.borderColor: &lt;color&gt;
slit.borderWidth: &lt;integer&gt;
slit.color: &lt;color&gt;
slit.colorTo: &lt;color&gt;
slit.pixmap: &lt;filename&gt;
-----------------------------------------</pre>
</dl>
<h2>Toolbar Options</h2>
<p>Below you will find all of the configuration possibilities for the toolbar. The list is pretty extensive and offers you many options to make your toolbar look just the way you want it. </p>
<dl>
<dd>
<pre>-----------------------------------------
toolbar: &lt;texture type&gt;
toolbar.bevelWidth: &lt;integer (0-255)&gt;
toolbar.borderColor: &lt;color&gt;
toolbar.borderWidth: &lt;integer&gt;
toolbar.button.scale: &lt;integer&gt;
toolbar.color: &lt;color&gt;
toolbar.colorTo: &lt;color&gt;
toolbar.clock: &lt;texture type&gt;
toolbar.clock.borderColor: &lt;color&gt;
toolbar.clock.borderWidth: &lt;integer&gt;
toolbar.clock.font: &lt;font&gt;
toolbar.clock.justify: &lt;{Left|Right|Center}&gt;
toolbar.clock.pixmap: &lt;filename&gt;
toolbar.clock.color: &lt;color&gt;
toolbar.clock.colorTo: &lt;color&gt;
toolbar.clock.textColor: &lt;color&gt;
toolbar.height: &lt;integer&gt;
toolbar.iconbar.focused: &lt;texture type&gt;
toolbar.iconbar.focused.color: &lt;color&gt;
toolbar.iconbar.focused.colorTo:&lt;color&gt;
toolbar.iconbar.focused.pixmap: &lt;filename&gt;
toolbar.iconbar.unfocused: &lt;texture type&gt;
toolbar.iconbar.unfocused.color: &lt;color&gt;
toolbar.iconbar.unfocused.colorTo: &lt;color&gt;
toolbar.iconbar.unfocused.pixmap: &lt;filename&gt;
toolbar.iconbar.empty: &lt;texture type&gt;
toolbar.iconbar.empty.color: &lt;color&gt;
toolbar.iconbar.empty.colorTo: &lt;color&gt;
toolbar.iconbar.empty.pixmap: &lt;filename&gt;
toolbar.iconbar.focused.borderColor: &lt;color&gt;
toolbar.iconbar.focused.borderWidth: &lt;integer&gt;
toolbar.iconbar.unfocused.borderColor: &lt;color&gt;
toolbar.iconbar.unfocused.borderWidth: &lt;integer&gt;
toolbar.iconbar.borderColor: &lt;color&gt;
toolbar.iconbar.borderWidth: &lt;integer&gt;
toolbar.iconbar.focused.font: &lt;font&gt;
toolbar.iconbar.focused.justify: &lt;{Left|Right|Center}&gt;
toolbar.iconbar.focused.textColor: &lt;color&gt;
toolbar.iconbar.unfocused.font: &lt;font&gt;
toolbar.iconbar.unfocused.justify: &lt;{Left|Right|Center}&gt;
toolbar.iconbar.unfocused.textColor: &lt;color&gt;
toolbar.pixmap: &lt;filename&gt;
toolbar.shaped: &lt;boolean&gt;
toolbar.workspace.font: &lt;font&gt;
toolbar.workspace.justify: &lt;{Left|Right|Center}&gt;
toolbar.workspace.textColor: &lt;color&gt;
toolbar.workspace: &lt;texture type&gt;
toolbar.workspace.borderColor: &lt;color&gt;
toolbar.workspace.borderWidth: &lt;integer&gt;
toolbar.workspace.color: &lt;color&gt;
toolbar.workspace.colorTo: &lt;color&gt;
toolbar.workspace.pixmap: &lt;filename&gt;
-----------------------------------------</pre>
</dl>
<h2>Examples</h2>
<p>This list may seem intimidating, but remember, when you create your own style you can easily set a majority of these keys with a single component. For an example of this: </p>
<dl>
<dd>
<pre>-----------------------------------------
*color: slategrey
*colorTo: darkslategrey
*unfocus.color: darkslategrey
*unfocus.colorTo: black
*textColor: white
*unfocus.textColor: lightgrey
*font: lucidasans-10
-----------------------------------------</pre>
</dl>
<p> This sets nice defaults for many components.</p>
<h2>Color Formats</h2>
<p>These are the color formats for styles: </p>
<dl>
<dd>
<pre>#000000 (Hexadecimal)
rgb:&lt;0-255&gt;/&lt;0-255&gt;/&lt;0-255&gt;</pre>
</dl>
<p> See /usr/share/X11/rgb.txt for an explanation.</p>
<h2>Authors</h2>
<p>Blackbox was written and maintained by Brad Hughes &lt;blackbox at alug.org&gt; and Jeff Raven &lt;jraven at psu.edu&gt;. </p>
<p> <a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1) is written and maintained by Henrik Kinnunen &lt;fluxgen at fluxbox.org&gt; with contributions and patches merged from many individuals around the world. </p>
<p> The Official <a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1) website: m[blue]<code><a rel="nofollow" href="http://www.fluxbox.org">http://www.fluxbox.org</a></code>m[] You can find a lot of styles here: m[blue]<code><a href="http://tenr.de/">http://tenr.de/</a></code>m[] </p>
<p> This manpage was composed from various resources including the official documentation, <a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1) man page and numerous other resources by Curt &quot;Asenchi&quot; Micol. If you notice any errors or problems with this page, please contact him here: &lt;asenchi at asenchi.com&gt; and using the great contributions of &lt;grubert at users.sourceforge.net&gt;. Numerous other languages could be available if someone jumps in.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1) <a href="/docs/linux/man/1-fbsetbg/">fbsetbg</a>(1) <a href="/docs/linux/man/1-fbsetroot/">fbsetroot</a>(1)</p>
<h2>Author</h2>
<p><code>Henrik Kinnunen</code> &lt;fluxgen [at] fluxbox.org&gt;</p>
<dl>
<dd>Author.</dl>
