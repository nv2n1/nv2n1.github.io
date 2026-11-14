---
title: "tuxpaint(1)"
name: "tuxpaint"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tuxpaint/"
description: "tuxpaint — \"Tux Paint\", a drawing program for young children."
---

<h2>NAME</h2>
<p> tuxpaint &#8212; &quot;Tux Paint&quot;, a drawing program for young children. </p>
<h2>SYNOPSYS</h2>
<p> <code>tuxpaint</code> [&#8211;help &#8211;version &#8211;verbose-version &#8211;usage &#8211;copying] </p>
<dl>
<dt><code>tuxpaint</code></p>
<dd> [&#8211;fullscreen]<br />
 [&#8211;allowscreensaver]<br />
 [&#8211;WIDTHxHEIGHT]<br />
 [&#8211;native]<br />
 [&#8211;orient=portrait]<br />
 [&#8211;startblank]<br />
 [&#8211;nosound]<br />
 [&#8211;noquit]<br />
 [&#8211;noprint]<br />
 [&#8211;printdelay=<i>SECONDS</i>]<br />
 [&#8211;printcfg]<br />
 [&#8211;altprintalways | &#8211;altprintnever]<br />
 [&#8211;papersize <i>PAPERSIZE</i> | &#8211;papersize help]<br />
 [&#8211;simpleshapes]<br />
 [&#8211;uppercase]<br />
 [&#8211;grab]<br />
 [&#8211;noshortcuts]<br />
 [&#8211;nowheelmouse]<br />
 [&#8211;nobuttondistinction]<br />
 [&#8211;nofancycursors]<br />
 [&#8211;hidecursor]<br />
 [&#8211;nooutlines]<br />
 [&#8211;nostamps]<br />
 [&#8211;nostampcontrols]<br />
 [&#8211;nomagiccontrols]<br />
 [&#8211;nolabel]<br />
 [&#8211;mirrorstamps]<br />
 [&#8211;mouse-accessibility]<br />
 [&#8211;onscreen-keyboard]<br />
 [&#8211;joystick-dev=<i>DEVICE</i>]<br />
 [&#8211;joystick-dev=list]<br />
 [&#8211;joystick-slowness=<i>SPEED</i>]<br />
 [&#8211;joystick-threshold=<i>THRESHOLD</i>]<br />
 [&#8211;joystick-maxsteps=<i>STEPS</i>]<br />
 [&#8211;joystick-hat-timeout=<i>MILLISECONDS</i>]<br />
 [&#8211;joystick-hat-slowness=<i>SPEED</i>]<br />
 [&#8211;joystick-btn-escape=<i>BUTTON</i>]<br />
 [&#8211;joystick-btn-brush=<i>BUTTON</i>]<br />
 [&#8211;joystick-btn-stamp=<i>BUTTON</i>]<br />
 [&#8211;joystick-btn-lines=<i>BUTTON</i>]<br />
 [&#8211;joystick-btn-shapes=<i>BUTTON</i>]<br />
 [&#8211;joystick-btn-text=<i>BUTTON</i>]<br />
 [&#8211;joystick-btn-label=<i>BUTTON</i>]<br />
 [&#8211;joystick-btn-magic=<i>BUTTON</i>]<br />
 [&#8211;joystick-btn-undo=<i>BUTTON</i>]<br />
 [&#8211;joystick-btn-redo=<i>BUTTON</i>]<br />
 [&#8211;joystick-btn-eraser=<i>BUTTON</i>]<br />
 [&#8211;joystick-btn-new=<i>BUTTON</i>]<br />
 [&#8211;joystick-btn-open=<i>BUTTON</i>]<br />
 [&#8211;joystick-btn-save=<i>BUTTON</i>]<br />
 [&#8211;joystick-btn-pgsetup=<i>BUTTON</i>]<br />
 [&#8211;joystick-btn-print=<i>BUTTON</i>]<br />
 [&#8211;joystick-buttons-ignore=<i>BUTTON1,BUTTON2,&#8230;</i>]<br />
 [&#8211;stampsize=<i>SIZE</i>]<br />
 [&#8211;keyboard]<br />
 [&#8211;nosysfonts]<br />
 [&#8211;alllocalefonts]<br />
 [&#8211;savedir <i>DIR</i>]<br />
 [&#8211;datadir <i>DIR</i>]<br />
 [&#8211;saveover]<br />
 [&#8211;saveovernew]<br />
 [&#8211;nosave]<br />
 [&#8211;autosave]<br />
 [&#8211;colorfile <i>FILE</i>] </p>
<dt><code>tuxpaint (defaults)</code></p>
<dd> [&#8211;windowed]<br />
 [&#8211;disablescreensaver]<br />
 [&#8211;800&#215;600]<br />
 [&#8211;orient=landscape]<br />
 [&#8211;startlast]<br />
 [&#8211;sound]<br />
 [&#8211;quit]<br />
 [&#8211;print]<br />
 [&#8211;printdelay=0]<br />
 [&#8211;noprintcfg]<br />
 [&#8211;altprintmod]<br />
 [&#8211;complexshapes]<br />
 [&#8211;mixedcase]<br />
 [&#8211;dontgrab]<br />
 [&#8211;shortcuts]<br />
 [&#8211;wheelmouse]<br />
 [&#8211;buttondistinction]<br />
 [&#8211;fancycursors]<br />
 [&#8211;showcursor]<br />
 [&#8211;outlines]<br />
 [&#8211;stamps]<br />
 [&#8211;stampcontrols]<br />
 [&#8211;magiccontrols]<br />
 [&#8211;label]<br />
 [&#8211;dontmirrorstamps]<br />
 [&#8211;stampsize=default]<br />
 [&#8211;mouse]<br />
 [&#8211;sysfonts]<br />
 [&#8211;currentlocalefont]<br />
 [&#8211;saveoverask]<br />
 [&#8211;save]<br />
 [&#8211;noautosave] </p>
<dt><code>tuxpaint</code></p>
<dd> [&#8211;locale <i>LOCALE</i>] </p>
<dt><code>tuxpaint</code></p>
<dd> [&#8211;lang <i>LANGUAGE</i> | &#8211;lang help] </p>
<dt><code>tuxpaint</code></p>
<dd> [&#8211;nosysconfig]<br />
 [&#8211;nolockfile] </p>
</dl>
<h2>DESCRIPTION</h2>
<p> <i>Tux Paint</i> is a drawing program for young children. It is meant to be easy and fun to use. It provides a simple interface and fixed canvas size, and provides access to previous images using a thumbnail browser (i.e., no access to the underlying filesystem). </p>
<p> Unlike popular drawing programs like &quot;<i>The GIMP</i>,&quot; it has a very limited toolset. However, it provides a much simpler interface, and has entertaining, child-oriented additions such as sound effects. </p>
<h2>OPTIONS &#8211; INFORMATIONAL</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Display short, helpful information about Tux Paint.</p>
<dt><code>&#8211;version</code></p>
<dd> Output the version info.</p>
<dt><code>&#8211;verbose-version</code></p>
<dd> Output the version info and compile-time build options.</p>
<dt><code>&#8211;usage</code></p>
<dd> Display a list of all commandline options.</p>
<dt><code>&#8211;copying</code></p>
<dd> Show the license (GNU GPL) under which Tux Paint is released. </p>
</dl>
<h2>OPTIONS &#8211; INTERFACE</h2>
<p> <i>tuxpaint</i> accepts the following options to alter the interface. They can be used along with, instead of, or to override options set in configuration files. (See below.)</p>
<dl>
<dt><code>&#8211;fullscreen &#8211;windowed</code></p>
<dd> Run <i>Tux Paint</i> in full-screen mode, or in a window (default). </p>
<dt><code>&#8211;allowscreensaver &#8211;disablescreensaver</code></p>
<dd> Normally, <i>tuxpaint</i> disables your screensaver. Use &#8211;allowscreensaver to prevent this from happening. </p>
<dt><code>&#8211;native</code></p>
<dd> When in fullscreen mode, use the system&#8217;s default screen resolution. </p>
<dt><code>&#8211;WIDTHxHEIGHT</code></p>
<dd> Run <i>Tux Paint</i> in a particularly-sized window, or at a particular fullscreen resolution (if &#8211;native is not used). Default is 800&#215;600. Minimum width is 640. Minimum height is 480. Portrait and landscape orientations are both supported. (Also see &#8211;orient, below.) </p>
<dt><code>&#8211;orient=landscape &#8211;orient=portrait</code></p>
<dd> If &#8211;orient=portraitis set, asks <i>Tux Paint</i> to swap the WIDTH and HEIGHT values it uses for windowed or fullscreen mode, without having to actually change the WIDTH and HEIGHT values in the configuration file or on the command-line. (This is useful on devices where the screen can be rotated, e.g. tablet PCs.) </p>
<dt><code>&#8211;nosound &#8211;sound</code></p>
<dd> Disable or enable (default) sound. </p>
<dt><code>&#8211;noquit &#8211;quit</code></p>
<dd> Disable or enable (default) the on-screen <i>Quit</i> button and <i>Escape</i> key sequence for quitting <i>Tux Paint</i>. Instead, use the window close button in the titlebar, the <i>Alt+F4</i> key sequence, or the <i>Shift+Control+Escape</i> key sequence. </p>
<dt><code>&#8211;noprint &#8211;print</code></p>
<dd> Disable or enable (default) the <i>Print</i> command within <i>Tux Paint</i>. </p>
<dt><code>&#8211;printdelay=</code><i>SECONDS</i> &#8211;printdelay=0</p>
<dd> Only allow printing (via the <i>Print</i> command) once every <i>SECONDS</i> seconds. Default is 0 (no limitation). </p>
<dt><code>&#8211;printcfg &#8211;noprintcfg</code></p>
<dd> (Windows and Mac OS X only.) Enable or disable loading and saving of printer settings. By default, <i>Tux Paint</i> will print to the default printer with default settings. Pressing <i>[ALT]</i> while pushing the <i>Print</i> button will cause a printer dialog to appear (as long as you&#8217;re not in fullscreen mode; see also &#8211;altprintalways and &#8211;altprintnever, below.) Unless &#8211;noprintcfg is used, your previous settings will be loaded when <i>Tux Paint</i> starts up, and setting changes will be saved for next time. </p>
<dt><code>&#8211;altprintmod &#8211;altprintnever &#8211;altprintalways</code></p>
<dd> These options control whether an system printer dialog appears when the user clicks the <i>Print</i> button. By default (&#8211;altprintmod), pressing <i>[ALT]</i> while clicking <i>Print</i> will bring up a dialog (unless you&#8217;re in fullscreen mode). With &#8211;altprintalways, the dialog will always appear, even if <i>[ALT]</i> is not being held. With &#8211;altprintnever, the dialog will never appear, even if <i>[ALT]</i> is being held. </p>
<dt><code>&#8211;papersize </code><i>PAPERSIZE</i></p>
<dd> (Only when PostScript printing is used &#8211; not Windows, Mac OS X or BeOS.) Ask <i>Tux Paint</i> to generate PostScript of a particular paper size. Valid sizes are those supported by libpaper. See <a href="/docs/linux/man/5-papersize/">papersize</a>(5). </p>
<dt><code>&#8211;simpleshapes &#8211;complexshapes</code></p>
<dd> Disable or enable (default) the <i>rotation</i> step when using the <i>Shape</i> tool within <i>Tux Paint</i>. When disabled, shapes cannot be rotated; however, the interface is easier (click, drag, release), which can be useful for younger or disabled children. </p>
<dt><code>&#8211;uppercase &#8211;mixedcase</code></p>
<dd> In <i>uppercase</i> mode, all text prompts and the <i>Text</i> drawing tool will display only uppercase letters. This is useful for children who are not yet comfortable with the lowercase characterset. Default mode is <i>mixed case</i>. </p>
<dt><code>&#8211;grab &#8211;nograb</code></p>
<dd> Grab the mouse and keyboard input (if possible), so that the mouse is confined to the <i>Tux Paint</i> window. Default is to not grab. </p>
<dt><code>&#8211;noshortcuts &#8211;shortcuts</code></p>
<dd> If <i>noshortcuts</i> mode, keyboard shortcuts (e.g., Ctrl+S for Save) will be disabled. Default mode is <i>shortcuts enabled</i>. </p>
<dt><code>&#8211;nowheelmouse &#8211;wheelmouse</code></p>
<dd> By default, the wheel (jog dial) on a mouse will be used to scroll the <i>selector</i> on the right of the screen. This can be disabled, and the wheel completely ignored, with the <i>&#8211;nowheelmouse</i> option. This is useful for children who aren&#8217;t yet comfortable with the mouse. Default is to support the wheel. </p>
<dt><code>&#8211;nobuttondistinction &#8211;buttondistinction</code></p>
<dd> By default, only mouse button #1 (typically the leftmost mouse button on mice with more than one button) can be used for interacting with <i>Tux Paint</i>. With the <i>&#8211;nobuttondistinction</i> option, mouse buttons #2 (middle) and #3 (right) can be used, as well. This is useful for children who aren&#8217;t yet comfortable with the mouse. Default is to only recognize button #1. </p>
<dt><code>&#8211;nofancycursors &#8211;fancycursors</code></p>
<dd> Disable or enable (default) the &#8216;fancy&#8217; mouse pointer shapes in <i>Tux Paint</i>. While the shapes are larger, and context sensitive, some environments have trouble displaying the mouse pointer, and/or leave &#8216;trails&#8217; on the screen. </p>
<dt><code>&#8211;hidecursor &#8211;showcursor</code></p>
<dd> Completely hide, or enable (default) the mouse pointer in <i>Tux Paint</i>. This can be useful on touchscreen devices, such as tablet PCs. </p>
<dt><code>&#8211;nooutlines &#8211;outlines</code></p>
<dd> In <i>nooutlines</i> mode, much simpler outlines and &#8216;rubber-band&#8217; lines are displayed when using the <i>Lines</i>, <i>Shapes</i>, <i>Stamps</i> and <i>Eraser</i> tools. (This can help when <i>Tux Paint</i> is run on slower computers, or displayed on a remote X display.) </p>
<dt><code>&#8211;nostamps &#8211;stamps</code></p>
<dd> With <i>nostamps</i> set, Rubber Stamp images are not loaded, so the <i>Stamps</i> tool will not be available. This option can be used to reduce the time Tux Paint takes to load, and reduce the amount of RAM it requires. </p>
<dt><code>&#8211;nostampcontrols &#8211;stampcontrols</code></p>
<dd> Disable or enable (default) buttons to control stamps. Controls include mirror, flip, shrink and grow. (Note: Not all stamps will be controllable in all ways.) </p>
<dt><code>&#8211;nomagiccontrols &#8211;magiccontrols</code></p>
<dd> Disable or enable (default) buttons to control Magic tools. Controls include controlling whether a Magic tool is used like a paint brush, or if it affects the entire image at once. (Note: Not all Magic tools will be controllable.) </p>
<dt><code>&#8211;nolabel &#8211;label</code></p>
<dd> Disable or enable (default) the <i>Label</i> tool, which lets you create text which can be altered or moved later. </p>
<dt><code>&#8211;mirrorstamps &#8211;dontmirrorstamps</code></p>
<dd> With <i>mirrorstamps</i> set, stamps which can be mirrored will appear mirrored by default. This can be useful when used by people who prefer things right-to-left over left-to-right. </p>
<dt><code>&#8211;mouse-accessibility</code></p>
<dd> In this mode, instead of clicking, dragging and releasing (e.g., to draw), you click, move, and click again to end the motion. </p>
<dt><code>&#8211;onscreen-keyboard</code></p>
<dd> Presents a clickable on-screen keyboard when using the <i>Text</i> and <i>Label</i> tools. </p>
<dt><code>&#8211;stampsize=</code><i>size</i> &#8211;stampsize=default</p>
<dd> Sets the default size of all stamps, relative to their possible sizes (determined by <i>Tux Paint</i>, based on the dimensions of both the stamps themselves, and the drawing canvas). Valid values are from 0 (smallest) to 10 (largest). Use <i>default</i> to let <i>Tux Paint</i> choose (this is the default setting). </p>
<dt><code>&#8211;keyboard &#8211;mouse</code></p>
<dd> The <i>keyboard</i> option lets the mouse pointer in <i>Tux Paint</i> be controlled with the keyboard. The <i>arrow keys</i> move the pointer. <i>Spacebar</i> acts as the mouse button. </p>
<dt><code>&#8211;nosysfonts &#8211;sysfonts</code></p>
<dd> <i>Tux Paint</i> normally attempts to search for additional TrueType Fonts installed in common places on your system. If this causes trouble, or you&#8217;d prefer to only make fonts installed in <i>Tux Paint</i>&#8216;s directory available, use the <i>nosysfonts</i> option to disable this feature. </p>
<dt><code>&#8211;alllocalefonts &#8211;currentlocalefont</code></p>
<dd> Tux Paint avoids loading any fonts in its &#8216;locale&#8217; font subdirectory, except any that match the current locale <i>Tux Paint</i> is running under. Use the <i>alllocalefonts</i> option to load all such fonts, for use in the &quot;Text&quot; tool. (This is the old behavior, prior to version 0.9.21.) </p>
<dt><code>&#8211;savedir </code><i>DIR</i></p>
<dd> Specify where <i>Tux Paint</i> should save files. </p>
<dt><code>&#8211;datadir </code><i>DIR</i></p>
<dd> Specify where <i>Tux Paint</i> should look for personal data files (brushes, stamps, etc.). </p>
<dt><code>&#8211;saveover &#8211;saveovernew &#8211;saveoverask</code></p>
<dd> If, when saving a picture, an older version of the file will be overwritten, <i>Tux Paint</i> will, by default, ask for confirmation: either <i>save over</i> the old file, or <i>create</i> a new file. This prompt can be disabled with <i>&#8211;saveover</i> (which always saves over older versions of pictures) or <i>&#8211;saveovernew</i> (which always saves a new file). The default is to prompt (<i>&#8211;saveoverask</i>). </p>
<dt><code>&#8211;nosave &#8211;save</code></p>
<dd> The <i>nosave</i> option disables <i>Tux Paint&#8217;s</i> ability to save files. This can be used in situations where the program is only being used for fun, or in a test environment. </p>
<dt><code>&#8211;autosave &#8211;noautosave</code></p>
<dd> The <i>autosave</i> option prevents <i>Tux Paint</i> from asking whether you want to save the current picture when quitting, and assumes you do. </p>
<dt><code>&#8211;startblank &#8211;startlast</code></p>
<dd> When you start <i>Tux Paint</i>, it loads the last image that was being worked on. The <i>&#8211;startblank</i> option disables this, so it always starts with a blank canvas. The default behavior is <i>&#8211;startlast</i>. </p>
<dt><code>&#8211;colorfile </code><i>FILE</i></p>
<dd> This option allows you to override the default color palette in <i>Tux Paint</i> and replace it with your own. The file should be a plain ASCII text file containing one color description per line. Colors may be in decimal or 6- or 3-digit hexadecimal, and followed by a description. (For example, &quot;<i>#000 Black</i>&quot; and &quot;<i>255 192 64 Orange</i>&quot;.) </p>
</dl>
<h2>OPTIONS &#8211; LANGUAGE</h2>
<p> Various parts of <i>Tux Paint</i> have been translated into numerous languages. <i>Tux Paint</i> will try its best to honor your <i>locale</i> setting (i.e., the <i>LANG</i> environment variable), if possible. You can also specifically set the language using options on the command-line or in a configuration file. </p>
<dl>
<dt><code>&#8211;locale </code><i>LOCALE</i></p>
<dd> Specify the language to use, based on locale name (which is typically of the form <i>language</i>[_<i>territory</i>][.<i>codeset</i>][@<i>modifier</i>], where <i>language</i> is an ISO 639 language code, <i>territory</i> is an ISO 3166 country code, and <i>codeset</i> is a character set or encoding identifier like ISO-8859-1 or UTF-8.)</dl>
<dl>
<dt>
<dd> For example, <i>de_DE [at] euro</i> for German, or <i>pt_BR</i> for Brazilian Portuguese.</dl>
<dl>
<dt><code>&#8211;lang </code><i>LANGUAGE</i></p>
<dd> Specify the language to use, based on the language&#8217;s name (as recognized by <i>Tux Paint</i>). Choose one of the language names listed below:</dl>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;</p>
<dd> english | american-english</p>
<dt>&#8211;</p>
<dd> acholi | acoli</p>
<dt>&#8211;</p>
<dd> afrikaans</p>
<dt>&#8211;</p>
<dd> akan | twi-fante</p>
<dt>&#8211;</p>
<dd> albanian</p>
<dt>&#8211;</p>
<dd> amharic</p>
<dt>&#8211;</p>
<dd> arabic</p>
<dt>&#8211;</p>
<dd> aragones</p>
<dt>&#8211;</p>
<dd> armenian | hayeren</p>
<dt>&#8211;</p>
<dd> assamese</p>
<dt>&#8211;</p>
<dd> asturian</p>
<dt>&#8211;</p>
<dd> azerbaijani</p>
<dt>&#8211;</p>
<dd> australian-english</p>
<dt>&#8211;</p>
<dd> bambara</p>
<dt>&#8211;</p>
<dd> basque | euskara</p>
<dt>&#8211;</p>
<dd> belarusian | bielaruskaja</p>
<dt>&#8211;</p>
<dd> bokmal</p>
<dt>&#8211;</p>
<dd> bosnian</p>
<dt>&#8211;</p>
<dd> brazilian-portuguese | portugues-brazilian | brazilian</p>
<dt>&#8211;</p>
<dd> breton | brezhoneg</p>
<dt>&#8211;</p>
<dd> british | british-english</p>
<dt>&#8211;</p>
<dd> bulgarian</p>
<dt>&#8211;</p>
<dd> canadian-english</p>
<dt>&#8211;</p>
<dd> catalan | catala</p>
<dt>&#8211;</p>
<dd> chinese | simplified-chinese</p>
<dt>&#8211;</p>
<dd> croatian | hrvatski</p>
<dt>&#8211;</p>
<dd> czech | cesky</p>
<dt>&#8211;</p>
<dd> danish | dansk</p>
<dt>&#8211;</p>
<dd> dutch | nederlands</p>
<dt>&#8211;</p>
<dd> esperanto</p>
<dt>&#8211;</p>
<dd> estonian</p>
<dt>&#8211;</p>
<dd> faroese</p>
<dt>&#8211;</p>
<dd> finnish | suomi</p>
<dt>&#8211;</p>
<dd> french | francais</p>
<dt>&#8211;</p>
<dd> fula | fulah | pulaar-fulfulde</p>
<dt>&#8211;</p>
<dd> gaelic | irish-gaelic | gaidhlig</p>
<dt>&#8211;</p>
<dd> galician | galego</p>
<dt>&#8211;</p>
<dd> georgian</p>
<dt>&#8211;</p>
<dd> german | deutsch</p>
<dt>&#8211;</p>
<dd> greek</p>
<dt>&#8211;</p>
<dd> gronings | zudelk-veenkelonioals</p>
<dt>&#8211;</p>
<dd> gujarati</p>
<dt>&#8211;</p>
<dd> hebrew</p>
<dt>&#8211;</p>
<dd> hindi</p>
<dt>&#8211;</p>
<dd> hungarian | magyar</p>
<dt>&#8211;</p>
<dd> icelandic | islenska</p>
<dt>&#8211;</p>
<dd> indonesian | bahasa-indonesia</p>
<dt>&#8211;</p>
<dd> inuktitut</p>
<dt>&#8211;</p>
<dd> italian | italiano</p>
<dt>&#8211;</p>
<dd> japanese</p>
<dt>&#8211;</p>
<dd> kannada</p>
<dt>&#8211;</p>
<dd> kiga | chiga</p>
<dt>&#8211;</p>
<dd> kinyarwanda</p>
<dt>&#8211;</p>
<dd> khmer</p>
<dt>&#8211;</p>
<dd> klingon | tlhIngan</p>
<dt>&#8211;</p>
<dd> konkani-devaganari</p>
<dt>&#8211;</p>
<dd> konkani-roman</p>
<dt>&#8211;</p>
<dd> korean</p>
<dt>&#8211;</p>
<dd> kurdish</p>
<dt>&#8211;</p>
<dd> latvian</p>
<dt>&#8211;</p>
<dd> lithuanian | lietuviu</p>
<dt>&#8211;</p>
<dd> luganda</p>
<dt>&#8211;</p>
<dd> luxembourgish | letzebuergesch</p>
<dt>&#8211;</p>
<dd> macedonian</p>
<dt>&#8211;</p>
<dd> maithili</p>
<dt>&#8211;</p>
<dd> malay</p>
<dt>&#8211;</p>
<dd> malayalam</p>
<dt>&#8211;</p>
<dd> manipuri-bengali</p>
<dt>&#8211;</p>
<dd> manipuri-meitei-mayek</p>
<dt>&#8211;</p>
<dd> marathi</p>
<dt>&#8211;</p>
<dd> mexican-spanish | espanol-mejicano | mexican</p>
<dt>&#8211;</p>
<dd> mongolian</p>
<dt>&#8211;</p>
<dd> ndebele</p>
<dt>&#8211;</p>
<dd> nepali</p>
<dt>&#8211;</p>
<dd> northern-sotho | sesotho-sa-leboa</p>
<dt>&#8211;</p>
<dd> norwegian | nynorsk | norsk</p>
<dt>&#8211;</p>
<dd> occitan</p>
<dt>&#8211;</p>
<dd> odia | oriya</p>
<dt>&#8211;</p>
<dd> ojibway | ojibwe</p>
<dt>&#8211;</p>
<dd> persian</p>
<dt>&#8211;</p>
<dd> polish | polski</p>
<dt>&#8211;</p>
<dd> portuguese | portugues</p>
<dt>&#8211;</p>
<dd> punjabi | panjabi</p>
<dt>&#8211;</p>
<dd> romanian</p>
<dt>&#8211;</p>
<dd> russian | russkiy</p>
<dt>&#8211;</p>
<dd> sanskrit</p>
<dt>&#8211;</p>
<dd> santali-devaganari</p>
<dt>&#8211;</p>
<dd> santali-ol-chiki</p>
<dt>&#8211;</p>
<dd> scottish | scottish-gaelic | ghaidhlig</p>
<dt>&#8211;</p>
<dd> serbian</p>
<dt>&#8211;</p>
<dd> serbian-latin</p>
<dt>&#8211;</p>
<dd> shuswap | secwepemctin</p>
<dt>&#8211;</p>
<dd> slovak</p>
<dt>&#8211;</p>
<dd> slovenian | slovensko</p>
<dt>&#8211;</p>
<dd> songhay</p>
<dt>&#8211;</p>
<dd> southafrican-english</p>
<dt>&#8211;</p>
<dd> spanish | espanol</p>
<dt>&#8211;</p>
<dd> sundanese</p>
<dt>&#8211;</p>
<dd> swahili</p>
<dt>&#8211;</p>
<dd> swedish | svenska</p>
<dt>&#8211;</p>
<dd> tagalog</p>
<dt>&#8211;</p>
<dd> tamil</p>
<dt>&#8211;</p>
<dd> telugu</p>
<dt>&#8211;</p>
<dd> thai</p>
<dt>&#8211;</p>
<dd> tibetan</p>
<dt>&#8211;</p>
<dd> traditional-chinese</p>
<dt>&#8211;</p>
<dd> turkish</p>
<dt>&#8211;</p>
<dd> twi</p>
<dt>&#8211;</p>
<dd> ukrainian</p>
<dt>&#8211;</p>
<dd> valencian</p>
<dt>&#8211;</p>
<dd> venda</p>
<dt>&#8211;</p>
<dd> venetian | veneto</p>
<dt>&#8211;</p>
<dd> vietnamese</p>
<dt>&#8211;</p>
<dd> walloon | walon</p>
<dt>&#8211;</p>
<dd> welsh | cymraeg</p>
<dt>&#8211;</p>
<dd> wolof</p>
<dt>&#8211;</p>
<dd> xhosa</p>
<dt>&#8211;</p>
<dd> zapotec | miahuatlan-zapotec</p>
<dt>&#8211;</p>
<dd> zulu</dl>
</dl>
<dl>
<dt><code>&#8211;lang help</code></p>
<dd> Display a lists of all supported languages. </p>
</dl>
<h2>OPTIONS &#8211; MISCELLANEOUS</h2>
<dl>
<dt><code>&#8211;nosysconfig</code></p>
<dd> With this option, <i>Tux Paint</i> will not attempt to read the system-wide configuration file (typically <i>/etc/tuxpaint/tuxpaint.conf</i>). </p>
<dt><code>&#8211;nolockfile</code></p>
<dd> By default, <i>Tux Paint</i> uses a lockfile (stored in the user&#8217;s local Tux Paint directory) which prevents it from being launched more than once in 30 seconds. (Sometimes children get too eager, or user interfaces only require one click, but users think they need to double-click.) This option makes <i>Tux Paint</i> ignore the current lockfile. </p>
</dl>
<h2>ENVIRONMENT</h2>
<p> While <i>Tux Paint</i> may refer to a number of environment variables indirectly (e.g., via <i><a href="/docs/linux/man/3-sdl/">SDL</a>(3)</i>), it only directly accesses the following: </p>
<dl>
<dt><code>HOME</code></p>
<dd> to determine where picture files go when using the <i>Save</i> and <i>Open</i> commands within <i>Tux Paint</i>, to keep track of the current image, when quitting and restarting <i>Tux Paint</i>, and to get the user&#8217;s configuration file. </p>
<dt><code>LANG</code></p>
<dd> to determine language to use, if <i><a href="/docs/linux/man/3-setlocale/">setlocale</a>(3)</i> refers to &#8216;LC_MESSAGES&#8217;. </p>
</dl>
<h2>FILES</h2>
<dl>
<dt><code>/etc/tuxpaint/tuxpaint.conf</code></p>
<dd> System-wide configuration file. It is read first (unless the <i>&#8211;nosysconfig</i> option was given on the command-line).</p>
<dl>
<dt>
<dd>
<p> (Created during installation.)</dl>
<dt><code>$HOME/.tuxpaintrc</code></p>
<dd> User&#8217;s configuration file. It can be used to set default options (rather than setting them on the command-line every time), and/or to override any settings in the system-wide configuration file.</p>
<dl>
<dt>
<dd>
<p> (Not created or edited automatically; must be created manually. You can do this by hand, or use &#8216;<i>Tux Paint Config.</i>.&#8217;)</dl>
<dt><code>$HOME/.tuxpaint/saved/</code></p>
<dd> A directory of previously-saved images (and thumbnails). Only files in this directory will be made available using the <i>Open</i> command within <i>Tux Paint</i>. (See <i><a href="/docs/linux/man/1-tuxpaint-import/">tuxpaint-import</a>(1)</i>.)</p>
<dl>
<dt>
<dd>
<p> (Created when <i>Save</i> command is used.)</dl>
<dt><code>$HOME/.tuxpaint/current_id.txt</code></p>
<dd> A reference to the image which was being edited when <i>Tux Paint</i> was last quit. (This image is automatically loaded the next time <i>Tux Paint</i> is re-run.)</p>
<dl>
<dt>
<dd>
<p> (Created when <i>Tux Paint</i> is <i>Quit</i>.)</dl>
<dt><code>$HOME/.tuxpaint/lockfile.dat</code></p>
<dd> A lockfile that prevents <i>Tux Paint</i> from being launched more than once every 30 seconds. Disable checking the lockfile by using the &#8216;&#8211;nolockfile&#8217; command-line argument.</p>
<dl>
<dt>
<dd>
<p> (There&#8217;s no reason to delete the lockfile, as it contains a timestamp inside which causes it to expire after 30 seconds.)</dl>
</dl>
<h2>COPYRIGHT</h2>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<h2>OTHER INFO</h2>
<p> The canonical place to find <i>Tux Paint</i> information is at <a rel="nofollow" href="http://www.tuxpaint.org/.">http://www.tuxpaint.org/.</a> </p>
<h2>AUTHORS</h2>
<p> Bill Kendrick. &lt;bill [at] newbreedsoftware.com&gt; </p>
<p> With patches, fixes, extensions, translation, documentation and more from lots of people, including, but not limited to: </p>
<p> Aki, Ashish Arora, Khalid Al Holan, Daniel Andersson, Hodorog Andrei, Joana Portia Antwi-Danso, Adorilson Bezerra de Araujo, Xandru Armesto, Ben Armstrong, Ravishankar Ayyakkannu, Dwayne Bailey, Martin Benjamin, Denis Bodor, Ren� Brandenburger, Herman Bruyninckx, Lucie Burianova, Laurentiu Buzdugan, Albert Cahalan, Pere Pujal Carabantes, Ouychai Chaita, Zden�k Chalupsk�, Wei-Lun Chao, Jacques Chion, Ankit Choudary, Abdoul Cisse, Urska Colner, Adam &#8216;akanewbie&#8217; Corcoran, Helder Correia, Ricardo Cruz, Laurent Dhima, Chandrakant Dhutadmal, Yavor Doganov, Joe Dalton, Dawa Dolma, Kevin Donnelly, Ander Elortondo, Alberto Escudero-Pascual, Jamil Farzana, Doruk Fisek, Dovix, Korvigellou An Drouizig (Philippe), Fabian Franz, Derrick Frimpong, Martin Fuhrer, Fula Localization Project, Gabriel Gazzan, Alexander Geroimenko, Torsten Giebl, Solomon Gizaw, Robert Glowczynski, Chris Goerner, Mikel Gonz�lez, Volker Grabsch, The Greek Linux i18n Team, Edmund GRIMLEY EVANS, Frederico Goncalves Guimaraes, Joe Hanson, Sam &quot;Criswell&quot; Hart, Guy Hed, Farinaz Hedayat, Tedi Heriyanto, Pjetur G. Hjaltason, Knut Erik Hollund, Khaled Hosny, Henry House, Mohomodou Houssouba, Song Huang, Karl Ove Hufthammer, Roland Illig, Indigenas Sin Fronteras, Juan Irigoien, Students of Vocational Higher Secondary School Irimpanam, Ivana Rakic, Dmitriy Ivanov, Mogens Jaeger, Lis G�the � J�kupsstovu, Nedjeljko Jedvaj, Aleksandar Jelenak, Rasmus Erik Voel Jensen, Wang Jian, Amed �. Jiyan, Petri Jooste, Richard June, Andrej Kacian, Thomas Kalka, Jorma Karvonen, Kazuhiko, Gabor Kelemen, Mark Kim, Thomas Klausner, Koby, Marcin &#8216;Shard&#8217; Konicki, Ines Kovacevic, Mantas Kriauciunas, Freek de Kruijf, Andrzej M. Krzysztofowicz, Piotr Kwilinski, Serafeim Kyriaki, Matthew Lange, Fabio Lazarin, Niko Lewman, Arkadiusz Lipiec, Ricky Lontoc, Dag H. Loras, Burkhard Luck, Vincent Mahlangu, Ankit Malik, Neskie Manuel, Fred Ulisses Maranhao, Yannig MARCHEGAY (Kokoyaya), Jorge Mariano, Martin, Sergio Marques, Pheledi Mathibela, Scott McCreary, Marco Milanesi, Kartik Mistry, Mugunth, Steve Murphy, Samuel Murray (Groenkloof), Shumani Mercy Nehulaudzi, Mikkel Kirkgaard Nielsen, Alesis Novik, Daniel Nylander, Olli, James Olweny, Teresa Orive, Gareth Owen, Sorin Paliga, Yannis Papatzikos, Nikolay Parukhin, Alessandro Pasotti, Flavio Pastor, Patrick, George Patrick, Primoz Peterlin, Le Quang Phan, Henrik Pihl, Auk Piseth, Pablo Pita, Milan Plzik, Sergei Popov, John Popplewell, Rodrigo Perez Ramirez and Indigenas Sin Fronteras, Adam &#8216;foo-script&#8217; Rakowski, Rodrigo Perez Ramirez, Robert Readman, Leandro Regueiro, Simona Riva, Robin Rosenberg, Ilir Rugova, Jaroslav Rynik, Bert Saal, Ibraahiima SAAR, Saikumar, Samuel Sarpong, Kevin Patrick Scannell, Stephanie Schilling, Kiriaki SERAFEIM, Pavithran Shakamuri, Gia Shervashidze, Clytie Siddall, Kliment Simoncev, Sokratis Sofianopoulos, Khoem Sokhem, Geert Stams, Peter Sterba, Raivis Strogonovs, Tomasz &#8216;karave&#8217; Tarach, Michal Terbert, Ignacia Tike, Tilo, Tarmo Toikkanen, TOYAMA Shin-ichi, Niall Tracey, tropikhajma, Florence Tushabe, Matej Urban, Rita Verbauskaite, Daniel Jose Viana, Charles Vidal, Darrell Walisser, Frank Weng, Damian Yerrick, Muhammad Najmi Ahmad Zabidi, Eugene Zelenko, Martin Zhekov, and Huang Zuzhen. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tuxpaint-import/">tuxpaint-import</a></code>(1), <code><a href="/docs/linux/man/1-tuxpaint-config/">tuxpaint-config</a></code>(1), <code><a href="/docs/linux/man/1-tp-magic-config/">tp-magic-config</a></code>(1), <code><a href="/docs/linux/man/1-xpaint/">xpaint</a></code>(1), <code><a href="/docs/linux/man/1-gpaint/">gpaint</a></code>(1), <code><a href="/docs/linux/man/1-gimp/">gimp</a></code>(1), <code><a href="/docs/linux/man/1-kolourpaint/">kolourpaint</a></code>(1), <code><a href="/docs/linux/man/1-krita/">krita</a></code>(1), <code><a href="/docs/linux/man/1-gcompris/">gcompris</a></code>(1) </p>
<p> And documentation within /usr/[local/]share/doc/tuxpaint/. </p>
<h2>Index</h2>
