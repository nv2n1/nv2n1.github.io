---
title: "idt(1)"
name: "idt"
section: "1"
letter: "i"
url: "/docs/linux/man/1-idt/"
description: "idt – X window interactive image display tool"
---

<h2>NAME</h2>
<p> idt &#8211; X window interactive image display tool</p>
<h2>SYNOPSIS</h2>
<p> <code>idt </code> [ <code>-toolkitoption</code><i> &#8230;</i> ] [ <code>-background</code><i> color</i> ] [ <code>-f</code><i> font</i> ] [ <code>-foreground</code><i> color</i> ] [ <code>-history</code> ] [ <code>-lmin</code><i> min</i> ] [ <code>-lmax</code><i> max</i> ] [ <code>-lscale</code><i> scale</i> ] [ <code>-oldidt</code> ] [ <code>-pal</code><i> pal_fname</i> ] [ <code>-reverse</code> ] [ <code>-soft</code> ] [ <code>-Version</code> ] [ <code>metafile</code> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>idt</code> provides a graphical user interface to the NCAR View interactive metafile translator <code>ictrans</code>. <code>idt </code> supports a subset of the <code>ictrans</code> command interface. </p>
<p> <code>idt </code> provides two types of command panels for interacting with imagery. The first type is the control panel, which you see when you initially invoke <code>idt</code>. The control panel displays messages from the translators, provides a metafile selection utility and is responsible for instantiating the second type of command panel, the display panel. The display panel provides mechanisms for controlling translators. Each display panel manages a single metafile translator. There can be multiple display panels in existence at the same time but only one control panel.</p>
<h2>OPTIONS</h2>
<p> <code>idt</code> accepts all of the standard X Toolkit command line options (see <a href="/docs/linux/man/1-x/">X</a>(1)). <code>idt</code> also accepts the following options:</p>
<dl>
<dt><code>-f</code><i> fontcap</i></p>
<dd> Fontcap file to be used for stroking text. When interpreting CGM <code>TEXT</code> command elements use <i>fontcap</i> as the default font for textual translation. Note: CGMs may contain textual descriptions which are not embedded in CGM <code>TEXT</code> elements. Hence they are not influenced by <i>fontcap</i> specifications. Note also that a CGM may explicitly specify a named font which may override a font provided on the command line. The environment variable FONTCAP may also be used to specify a default fontcap.</p>
<dt>
<dd> If <i>fontcap</i> is preceded by a UNIX directory path then <code>ctrans</code> will look in that directory for the specified fontcap. Otherwise <code>idt</code> searches the directory $NCARG_ROOT/lib/ncarg/fontcaps for the fontcap.</p>
<dt>
<dd> See <code>fontcap(5NCARG)</code> for a description of the available fontcaps. See <code>fcap(1NCARG)</code> for a list of the fontcaps installed on your system.</p>
<dt>
<dd> This option overrides the <code>FONTCAP</code> environment variable.</p>
<dt><code>-history</code></p>
<dd> Write a record of all commands sent to the translator to the file <code>./.idthist</code>.</p>
<dt><code>-Version</code></p>
<dd> Print the version number and then exit.</dl>
<p> The following options are ignored by <code>idt</code> and are passed on to the metafile translator <code>ictrans</code>. See <code>ictrans(1NCARG)</code> for a description of their use.</p>
<dl>
<dt><code>-soft</code></p>
<dd>
<dt><code>-lmin</code><i> linewidth</i></p>
<dd>
<dt><code>-lmax</code><i> linewidth</i></p>
<dd>
<dt><code>-lscale</code><i> linewidth</i></p>
<dd>
<dt><code>-pal</code><i> pal_fname</i></p>
<dd>
<dt><code>-foreground</code><i> color</i></p>
<dd>
<dt><code>-background</code><i> color</i></p>
<dd>
<dt><code>-reverse</code></p>
<dd></dl>
<h2>CONTROL PANEL COMMANDS</h2>
<p> The control panel provides a text widget for displaying messages from the translators and a row of command buttons. Messages are preceded with the string &quot;Display[X]&quot;, where &quot;X&quot; is an integer id associated with the translator sending the message. The first translator spawned is &quot;Display[0]&quot;, the second is &quot;Display[1]&quot;, etc.</p>
<dl>
<dt>select file</p>
<dd> Selects a file for translation. This button brings up a popup menu containing a file selection box. The uppermost dialog box of the file selection box is used for specifying a filter for searching for files. For example, the filter &quot;/usr/local/lib/*.cgm&quot; finds all files in the directory /usr/local/lib whose names end with &quot;.cgm&quot;. The finder understands standard shell metacharacters.</p>
<dt>
<dd> The bottom dialog box displays the currently selected file. The user may enter a file name here or select one with the mouse from the list of files displayed in the middle text widget.</p>
<dt>display</p>
<dd> Popup a display panel. A display panel is popped up ready for translation of the file most recently selected with the file selector. This command will fail if a file has not been selected.</p>
<dt>quit</p>
<dd> Quits the application and terminates all translators.</dl>
<h2>DISPLAY PANEL COMMANDS</h2>
<p> The display panel provides a mechanism for manipulating the translator associated with a particular metafile. On most systems the name of the metafile appears in the title bar at the top of the panel. The first row in the panel contains a scroll bar for randomly selecting a frame to be translated. The label bar to the right displays the number of the frame scrolled to. The panel is intended to resemble a video tape editor. Thus, the second row contains play back, jog back, stop, jog and play buttons, respectively. The third and forth rows contain more complex display commands.</p>
<dl>
<dt>loop</p>
<dd> Toggle the looping mode on or off. When loop is on pressing the play (playback) button causes the translator to process all the frames in the segment sequentially (reverse sequentially) and then start over from the beginning (end). The process continues until the &quot;stop&quot; button is selected. By default loop mode is off.</p>
<dt>dup</p>
<dd> Sets duplication variable. If dup is set to <code>1 </code> each frame is displayed once, if dup is set to <code>2</code> each frame is displayed twice, etc. The default value of dup is <code>1</code>.</p>
<dt>goto</p>
<dd> Go to the specified frame and translate it. <code>goto </code> provides random access to the frames contained in the metafile.</p>
<dt>skip</p>
<dd> Set the skip variable. If skip is set to <code>1</code> every other frame is displayed during subsequent plays, if skip is set to <code>2</code> every third frame is displayed, etc. The default value for skip is <code>0.</code></p>
<dt>delay</p>
<dd> Set the between-frame animation delay-time. When <code>idt</code> is in animation mode you may request that <code>idt </code> pause for a period of time between the display of each image. The effect of setting a delay time is to govern the speed at which <code>idt</code> &quot;plays&quot; imagery.</p>
<dt>start segment</p>
<dd> Define the first frame in the segment. This button and the <code>stop segment</code> button define a segment which is a subset of the frames contained in the metafile. When in play (playback) mode only the frames contained within the defined segment are translated. The default value for <code>start segment</code> is <code>1</code>, the first frame in the file.</p>
<dt>stop segment</p>
<dd> Define the last frame in the segment. The default frame is the last frame in the file. Hence, by default the segment is the entire metafile.</p>
<dt>set window</p>
<dd> Specify the workstation window (in the GKS sense). Four coordinates are specified which define a rectangular window which is a subset of normalized VDC rectangle with corner points (0,0) and (1.0,1.0). The specified window is then mapped onto the entire viewport. For example, if the workstation window is defined by the corner points (0,0) and (0.5 0.5) then the lower left quarter of a plot would be blown up to fill the largest rectangle which fits in the drawing window while retaining the aspect ratio described by the normalized coordinates. Specification of such a window can be used for zooming and panning.</p>
<dt>done</p>
<dd> Terminate processing of current metafile.</p>
<dt>current frame</p>
<dd> Update the &quot;Scrolled to Frame -&gt;&quot; label box with the number of the current frame.</p>
<dt>print</p>
<dd> Send the current frame to the printer. The <code>print</code> command brings up a menu of all devices configured for accepting translator output. This list is created dynamically in response to changes in the spooler configuration file (see ncarv_spool(5NCARG)). Selecting an item from the menu causes the current frame to be sent to that device.</p>
<dt>save</p>
<dd> Save a frame to a file. This command allows you to write the metacode for the current frame to a file. The result is a complete NCAR Computer Graphics Metafile (CGM) containing a single frame.</p>
<dt>unzoom</p>
<dd> Reset windowing transformations previously set by the <code>zoom</code> command back to their default.</p>
<dt>zoom</p>
<dd> Zoom in on an area of a plot. The function of this command is identical to that of the <code>window </code> command. The <code>zoom</code> command, however, allows you to select the area of interest interactively with the mouse.</p>
<dt>animate</p>
<dd> Toggle animation mode on or off. When <code>idt</code> is put into animation mode the currently defined segment is rasterized with the translator and loaded into the X server memory. Subsequent <code>idt</code> commands operate on the memory-resident images. Not all <code>idt </code> commands are available in animation mode. By default animation is off.</dl>
<h2>RESOURCES</h2>
<p> As with all standard X applications, <code>idt</code> may be customized through entries in the resource manager. In the following list of application resources provided by <code>idt </code> the resource name is given followed by its class in parentheses. These resources supplement the resources provided by the widgets themselves.</p>
<dl>
<dt>history (Class History)</p>
<dd> Specify whether a history of commands sent to the metafile translators is recorded to the file &quot;./.idthist&quot; or not. The default for this resource is &quot;False&quot;.</p>
<dt>fileSelectAction (Class FileSelectAction)</p>
<dd> Set the default action to be executed after a file has been selected with the file selection box. Currently the only value this resource understands is &quot;display&quot;.</p>
<dt>messageHeight (Class MessageHeight)</p>
<dd> Set the height in lines of text of the message display panel.</p>
<dt>oldIdt (Class OldIdt)</p>
<dd> Specifies the &quot;-oldidt&quot; option.</p>
<dt>translatorDevice (Class TranslatorDevice)</p>
<dd> Specify the output device for metafile translation. The default for this resource is &quot;X11&quot;.</p>
<dt>translatorFont (Class TranslatorFont)</p>
<dd> Specify the name of the fontcap to use for stroking text during metafile translation. The default value for this resource is &quot;font1&quot;.</p>
<dt>translatorSoft (Class TranslatorSoft)</p>
<dd> Specifies the <code>ictrans</code> &quot;-soft&quot; option.</p>
<dt>translatorLmin (Class TranslatorLmin)</p>
<dd> Specifies the <code>ictrans</code> &quot;-lmin&quot; option.</p>
<dt>translatorLmax (Class TranslatorLmax)</p>
<dd> Specifies the <code>ictrans</code> &quot;-lmax&quot; option.</p>
<dt>translatorLscale (Class TranslatorLscale)</p>
<dd> Specifies the <code>ictrans</code> &quot;-lscale&quot; option.</p>
<dt>translatorForeground (Class TranslatorForeground)</p>
<dd> Specifies the <code>ictrans</code> &quot;-foreground&quot; option.</p>
<dt>translatorBackground (Class TranslatorBackground)</p>
<dd> Specifies the <code>ictrans</code> &quot;-background&quot; option.</p>
<dt>translatorReverse (Class TranslatorReverse)</p>
<dd> Specifies the <code>ictrans</code> &quot;-reverse&quot; option.</dl>
<h2>ACTIONS</h2>
<p> <code>idt </code> provides the following actions for use in event translation:</p>
<dl>
<dt>FinderTranslation()</p>
<dd> This action causes the file selector popup to search for files using the key supplied in the file finder text box.</p>
<dt>OkFinderTranslation()</p>
<dd> This action notifies the file selector that a selection has been made.</p>
<dt>SelectFileTranslation()</p>
<dd> This action updates the text box in the file selector which displays the currently selected file.</p>
<dt>OkSDTranslation()</p>
<dd> This action confirms a selection made in one of the display panel popup dialog boxes.</dl>
<h2>WIDGETS</h2>
<p> In order to specify resources, it is useful to know the hierarchy of the widgets which make up <code>idt</code>. In the notation below, indentation indicates hierarchal structure. The widget class name is given first, followed by the widget instance name. </p>
<pre>
Idt  idt
    Paned  paned
        Text  text
        Form  form
            Command  select file
            Command  display
                TopLevelShell  &lt;???&gt;
                    Paned  paned
                        Core  canvas    /* This is the drawing canvas
                        Form  form
                            Scrollbar  scrollbar
                            Label  Scrolled to Frame -&gt; 
                        Form  form
                            Command  playback
                            Command  jogback
                            Command  stop
                            Command  jog
                            Command  play
                        Form  form
                            Toggle  loop
                            Command  dup
                            Command  goto
                            Command  skip
                            Command  delay
                            Command  start segment
                            Command  stop segment
                            Command  set window
                        Form  form
                            Command  done
                            Command  current frame
                            MenuButton  print
                                SimpleMenu  menu
                                    SmeBSB  &lt;???&gt; 
                                    SmeBSB  &lt;???&gt; 
                                    SmeBSB  &lt;???&gt;
                                              |
                                              |
                                    dynamically configured
                                              |
                                              |
                                    SmeBSB  &lt;???&gt; 
                                    SmeBSB  &lt;???&gt;
                            Command  save
                            Command  zoom
                            Command  unzoom
                            Toggle  animate
                        Grip  grip
                        Grip  grip
                        Grip  grip
                        Grip  grip
                        Grip  grip
            Command  quit
        Grip  grip
        Grip  grip
</pre>
<p> Paned</p>
<h2>EXAMPLES</h2>
<p> The following resource specification can be used to set the default size of the graphics display window to 200 by 200 pixels: </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<pre>
        Idt*canvas.width:       200
        Idt*canvas.height:      200
</pre>
<p> If you want to place the control panel in the top right corner insert the following into your .Xdefaults file: </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> <tt>&nbsp;<wbr>&nbsp;<wbr></tt>idt.geometry: -0+0</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DISPLAY</code></p>
<dd> This is the standard X environment variable for specifying display name. If the translation output device is <code>X11</code> this variable MUST be set.</p>
<dt><code>FONTCAP</code></p>
<dd> Default fontcap specifier.</p>
<dt><code>NCARG_ROOT</code></p>
<dd> Path to root of NCAR Graphics installation.</p>
<dt><code>NCARG_LIB</code></p>
<dd> If set this variable contains the path to the installed NCAR Graphics libraries. <code>NCARG_LIB</code> overrides <code>NCARG_ROOT</code>.</p>
<dt><code>NCARG_TMP</code></p>
<dd> If set, this environment variable contains a directory path to be used for temporary files. On most systems the default is <code>/tmp</code>. On some systems the default is <code>/usr/tmp</code>.</p>
<dt><code>SHELL</code></p>
<dd> Specifies the UNIX shell that the file selector is to use for expanding metacharacters. /bin/sh is used by default.</p>
<dt><code>XENVIRONMENT</code></p>
<dd> Specifies the name of a resource file that overrides the global resources stored in the RESOURCE_MANAGER property.</dl>
<h2>FILES</h2>
<dl>
<dt>\.idthist</p>
<dd> &#8211; Translator command history file</p>
<dt>$NCARG_ROOT/lib/ncarg/xapp/Idt</p>
<dd> &#8211; Default resource file for <code>idt</code></p>
<dt>$HOME/.ncarv_spool</p>
<dd> &#8211; User spooler configuration file</p>
<dt>$NCARG_ROOT/lib/ncarg/ncarv_spool</p>
<dd> &#8211; System spooler configuration file</dl>
<h2>SEE ALSO</h2>
<p> <code>ctrans(1NCARG),</code> <code>fcaps(1NCARG),</code> <code>gcaps(1NCARG),</code> <code>ictrans(1NCARG),</code> <code>ncarv_spool(5NCARG),</code> <code><a href="/docs/linux/man/1-x/">X</a>(1),</code> <code><a href="/docs/linux/man/1-xrdb/">xrdb</a>(1)</code> </p>
<p> Hardcopy: NCAR Graphics Fundamentals, UNIX Version</p>
<h2>BUGS</h2>
<p> Zooming in on large cell arrays causes the translator to crash.</p>
<h2>CAVEATS</h2>
<p> The metafile file translation process is performed by spawning the <code>ictrans</code> translator. <code>ictrans </code> does not understand standard X Toolkit options. Hence, the DISPLAY environment variable must be set when translating a metafile to be displayed in a window. </p>
<p> You can not save &quot;zoomed&quot; plots to a file. More precisely, you may save a &quot;zoomed&quot; plot, however, the resultant plot will not be &quot;zoomed&quot;. </p>
<p> The &quot;Scrolled to Frame&quot; label is not continuously updated. </p>
<p> The range with which one may zoom in on a plot with either the <code>zoom</code> or <code>window </code> command is severely limited by Xlibs use of &#8216;short&#8217; integers for containing screen coordinate data. </p>
<p> IRIX 4.x users should not set use the shared memory connection to their X server. i.e don&#8217;t use the display shm:0. </p>
<p> Background color changes don&#8217;t work when <code>idt</code> is in animate mode. <code>idt</code> will use whatever color was most recently set in the animation segment for the entire segment.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research </p>
<p> The use of this Software is governed by a License Agreement. </p>
<h2>Index</h2>
