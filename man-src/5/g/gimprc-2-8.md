---
title: "gimprc-2-8(5)"
name: "gimprc-2-8"
section: "5"
letter: "g"
url: "/docs/linux/man/5-gimprc-2-8/"
description: "gimprc – gimp configuration file"
---

<p>gimprc &#8211; gimp configuration file</p>
<h2>Description</h2>
<p>The <code>gimprc</code> file is a configuration file read by GIMP when it starts up. There are two of these: one system-wide one stored in /etc/gimp/2.0/gimprc and a per-user <code>$HOME</code>/.gimp-2.8/gimprc which may override system settings. Comments are introduced by a hash sign (#), and continue until the end of the line. Blank lines are ignored. The <code>gimprc</code> file associates values with properties. These properties may be set by lisp-like assignments of the form:</p>
<dl>
<dd><code>(</code><i>property-name value</i><code>)</code></p>
<dt>where:</p>
<dd>
<dt><i>property-name</i></p>
<dd>is one of the property names described below.</p>
<dt><i>value</i></p>
<dd>is the value the property is to be set to.</dl>
<p> Either spaces or tabs may be used to separate the name from the value. </p>
<h2>Properties</h2>
<p>Valid properties and their default values are: </p>
<dl>
<dt>(temp-path &quot;${gimp_dir}/tmp&quot;)</p>
<dd>Sets the folder for temporary storage. Files will appear here during the course of running GIMP. Most files will disappear when GIMP exits, but some files are likely to remain, so it is best if this folder not be one that is shared by other users. This is a single folder. </p>
<dt>(swap-path &quot;${gimp_dir}&quot;)</p>
<dd>Sets the swap file location. GIMP uses a tile based memory allocation scheme. The swap file is used to quickly and easily swap tiles out to disk and back in. Be aware that the swap file can easily get very large if GIMP is used with large images. Also, things can get horribly slow if the swap file is created on a folder that is mounted over NFS. For these reasons, it may be desirable to put your swap file in &quot;/tmp&quot;. This is a single folder. </p>
<dt>(num-processors 1)</p>
<dd>Sets how many processors GIMP should try to use simultaneously. This is an integer value. </p>
<dt>(tile-cache-size 1421926k)</p>
<dd>When the amount of pixel data exceeds this limit, GIMP will start to swap tiles to disk. This is a lot slower but it makes it possible to work on images that wouldn&#8217;t fit into memory otherwise. If you have a lot of RAM, you may want to set this to a higher value. The integer size can contain a suffix of &#8216;B&#8217;, &#8216;K&#8217;, &#8216;M&#8217; or &#8216;G&#8217; which makes GIMP interpret the size as being specified in bytes, kilobytes, megabytes or gigabytes. If no suffix is specified the size defaults to being specified in kilobytes. </p>
<dd>Specifies the language to use for the user interface. This is a string value. </p>
<dt>(interpolation-type cubic)</p>
<dd>Sets the level of interpolation used for scaling and other transformations. Possible values are none, linear, cubic and lanczos. </p>
<dt>(default-threshold 15)</p>
<dd>Tools such as fuzzy-select and bucket fill find regions based on a seed-fill algorithm. The seed fill starts at the initially selected pixel and progresses in all directions until the difference of pixel intensity from the original is greater than a specified threshold. This value represents the default threshold. This is an integer value. </p>
<dt>(plug-in-path &quot;${gimp_dir}/plug-ins:${gimp_plug_in_dir}/plug-ins&quot;)</p>
<dd>Sets the plug-in search path. This is a colon-separated list of folders to search. </p>
<dt>(module-path &quot;${gimp_dir}/modules:${gimp_plug_in_dir}/modules&quot;)</p>
<dd>Sets the module search path. This is a colon-separated list of folders to search. </p>
<dt>(interpreter-path &quot;${gimp_dir}/interpreters:${gimp_plug_in_dir}/interpreters&quot;)</p>
<dd>Sets the interpreter search path. This is a colon-separated list of folders to search. </p>
<dt>(environ-path &quot;${gimp_dir}/environ:${gimp_plug_in_dir}/environ&quot;)</p>
<dd>Sets the environ search path. This is a colon-separated list of folders to search. </p>
<dt>(brush-path &quot;${gimp_dir}/brushes:${gimp_data_dir}/brushes&quot;)</p>
<dd>Sets the brush search path. This is a colon-separated list of folders to search. </p>
<dt>(brush-path-writable &quot;${gimp_dir}/brushes&quot;)</p>
<dd>This is a colon-separated list of folders to search. </p>
<dt>(dynamics-path &quot;${gimp_dir}/dynamics:${gimp_data_dir}/dynamics&quot;)</p>
<dd>Sets the dynamics search path. This is a colon-separated list of folders to search. </p>
<dt>(dynamics-path-writable &quot;${gimp_dir}/dynamics&quot;)</p>
<dd>This is a colon-separated list of folders to search. </p>
<dt>(pattern-path &quot;${gimp_dir}/patterns:${gimp_data_dir}/patterns&quot;)</p>
<dd>Sets the pattern search path. This is a colon-separated list of folders to search. </p>
<dt>(pattern-path-writable &quot;${gimp_dir}/patterns&quot;)</p>
<dd>This is a colon-separated list of folders to search. </p>
<dt>(palette-path &quot;${gimp_dir}/palettes:${gimp_data_dir}/palettes&quot;)</p>
<dd>Sets the palette search path. This is a colon-separated list of folders to search. </p>
<dt>(palette-path-writable &quot;${gimp_dir}/palettes&quot;)</p>
<dd>This is a colon-separated list of folders to search. </p>
<dt>(gradient-path &quot;${gimp_dir}/gradients:${gimp_data_dir}/gradients&quot;)</p>
<dd>Sets the gradient search path. This is a colon-separated list of folders to search. </p>
<dt>(gradient-path-writable &quot;${gimp_dir}/gradients&quot;)</p>
<dd>This is a colon-separated list of folders to search. </p>
<dt>(tool-preset-path &quot;${gimp_dir}/tool-presets:${gimp_data_dir}/tool-presets&quot;)</p>
<dd>Sets the dynamics search path. This is a colon-separated list of folders to search. </p>
<dt>(tool-preset-path-writable &quot;${gimp_dir}/tool-presets&quot;)</p>
<dd>This is a colon-separated list of folders to search. </p>
<dt>(font-path &quot;${gimp_dir}/fonts:${gimp_data_dir}/fonts&quot;)</p>
<dd>Where to look for fonts in addition to the system-wide installed fonts. This is a colon-separated list of folders to search. </p>
<dt>(default-brush &quot;Round Fuzzy&quot;)</p>
<dd>Specify a default brush. The brush is searched for in the specified brush path. This is a string value. </p>
<dt>(default-dynamics &quot;Dynamics Off&quot;)</p>
<dd>Specify a default dynamics. The dynamics is searched for in the specified dynamics path. This is a string value. </p>
<dt>(default-pattern &quot;Pine&quot;)</p>
<dd>Specify a default pattern. This is a string value. </p>
<dt>(default-palette &quot;Default&quot;)</p>
<dd>Specify a default palette. This is a string value. </p>
<dt>(default-gradient &quot;FG to BG (RGB)&quot;)</p>
<dd>Specify a default gradient. This is a string value. </p>
<dt>(default-tool-preset &quot;Current Options&quot;)</p>
<dd>Specify a default tool preset. The tool preset is searched for in the specified tool prests path. This is a string value. </p>
<dt>(default-font &quot;Sans&quot;)</p>
<dd>Specify a default font. This is a string value. </p>
<dt>(global-brush yes)</p>
<dd>When enabled, the selected brush will be used for all tools. Possible values are yes and no. </p>
<dt>(global-dynamics yes)</p>
<dd>When enabled, the selected dynamics will be used for all tools. Possible values are yes and no. </p>
<dt>(global-pattern yes)</p>
<dd>When enabled, the selected pattern will be used for all tools. Possible values are yes and no. </p>
<dt>(global-palette yes)</p>
<dd>When enabled, the selected palette will be used for all tools. Possible values are yes and no. </p>
<dt>(global-gradient yes)</p>
<dd>When enabled, the selected gradient will be used for all tools. Possible values are yes and no. </p>
<dt>(global-font yes)</p>
<dd>When enabled, the selected font will be used for all tools. Possible values are yes and no. </p>
<dt>(default-image</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(width 640)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(height 400)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(unit pixels)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(xresolution 72.000000)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(yresolution 72.000000)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(resolution-unit inches)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(image-type rgb)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(fill-type background-fill)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(comment&nbsp;&quot;Created with GIMP&quot;)) </p>
<p> Sets the default image in the &quot;File/New&quot; dialog. This is a parameter list. </p>
<dt>(default-grid</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(style solid)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(fgcolor&nbsp;(color-rgba 0.000000 0.000000 0.000000 1.000000))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(bgcolor&nbsp;(color-rgba 1.000000 1.000000 1.000000 1.000000))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(xspacing 10.000000)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(yspacing 10.000000)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(spacing-unit inches)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(xoffset 0.000000)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(yoffset 0.000000)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(offset-unit inches)) </p>
<p> Specify a default image grid. This is a parameter list. </p>
<dt>(undo-levels 5)</p>
<dd>Sets the minimal number of operations that can be undone. More undo levels are kept available until the undo-size limit is reached. This is an integer value. </p>
<dt>(undo-size 64M)</p>
<dd>Sets an upper limit to the memory that is used per image to keep operations on the undo stack. Regardless of this setting, at least as many undo-levels as configured can be undone. The integer size can contain a suffix of &#8216;B&#8217;, &#8216;K&#8217;, &#8216;M&#8217; or &#8216;G&#8217; which makes GIMP interpret the size as being specified in bytes, kilobytes, megabytes or gigabytes. If no suffix is specified the size defaults to being specified in kilobytes. </p>
<dt>(undo-preview-size large)</p>
<dd>Sets the size of the previews in the Undo History. Possible values are tiny, extra-small, small, medium, large, extra-large, huge, enormous and gigantic. </p>
<dt>(plug-in-history-size 10)</p>
<dd>How many recently used plug-ins to keep on the Filters menu. This is an integer value. </p>
<dt>(pluginrc-path &quot;${gimp_dir}/pluginrc&quot;)</p>
<dd>Sets the pluginrc search path. This is a single filename. </p>
<dt>(layer-previews yes)</p>
<dd>Sets whether GIMP should create previews of layers and channels. Previews in the layers and channels dialog are nice to have but they can slow things down when working with large images. Possible values are yes and no. </p>
<dt>(layer-preview-size medium)</p>
<dd>Sets the preview size used for layers and channel previews in newly created dialogs. Possible values are tiny, extra-small, small, medium, large, extra-large, huge, enormous and gigantic. </p>
<dt>(thumbnail-size normal)</p>
<dd>Sets the size of the thumbnail shown in the Open dialog. Possible values are none, normal and large. </p>
<dt>(thumbnail-filesize-limit 4M)</p>
<dd>The thumbnail in the Open dialog will be automatically updated if the file being previewed is smaller than the size set here. The integer size can contain a suffix of &#8216;B&#8217;, &#8216;K&#8217;, &#8216;M&#8217; or &#8216;G&#8217; which makes GIMP interpret the size as being specified in bytes, kilobytes, megabytes or gigabytes. If no suffix is specified the size defaults to being specified in kilobytes. </p>
<dt>(color-management</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(mode display)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(display-profile-from-gdk no)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(display-rendering-intent perceptual)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(simulation-rendering-intent perceptual)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(simulation-gamut-check no)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(out-of-gamut-color&nbsp;(color-rgb 0.501961 0.501961 0.501961))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(display-module&nbsp;&quot;CdisplayLcms&quot;)) </p>
<p> Defines the color management behavior. This is a parameter list. </p>
<dt>(color-profile-policy ask)</p>
<dd>How to handle embedded color profiles when opening a file. Possible values are ask, keep and convert. </p>
<dt>(save-document-history yes)</p>
<dd>Keep a permanent record of all opened and saved files in the Recent Documents list. Possible values are yes and no. </p>
<dt>(quick-mask-color (color-rgba 1.000000 0.000000 0.000000 0.500000))</p>
<dd>Sets the default quick mask color. The color is specified in the form (color-rgba red green blue alpha) with channel values as floats in the range of 0.0 to 1.0. </p>
<dt>(transparency-size medium-checks)</p>
<dd>Sets the size of the checkerboard used to display transparency. Possible values are small-checks, medium-checks and large-checks. </p>
<dt>(transparency-type gray-checks)</p>
<dd>Sets the manner in which transparency is displayed in images. Possible values are light-checks, gray-checks, dark-checks, white-only, gray-only and black-only. </p>
<dt>(snap-distance 8)</p>
<dd>This is the distance in pixels where Guide and Grid snapping activates. This is an integer value. </p>
<dt>(marching-ants-speed 200)</p>
<dd>Speed of marching ants in the selection outline. This value is in milliseconds (less time indicates faster marching). This is an integer value. </p>
<dt>(resize-windows-on-zoom no)</p>
<dd>When enabled, the image window will automatically resize itself when zooming into and out of images. Possible values are yes and no. </p>
<dt>(resize-windows-on-resize no)</p>
<dd>When enabled, the image window will automatically resize itself whenever the physical image size changes. Possible values are yes and no. </p>
<dt>(default-dot-for-dot yes)</p>
<dd>When enabled, this will ensure that each pixel of an image gets mapped to a pixel on the screen. Possible values are yes and no. </p>
<dt>(initial-zoom-to-fit yes)</p>
<dd>When enabled, this will ensure that the full image is visible after a file is opened, otherwise it will be displayed with a scale of 1:1. Possible values are yes and no. </p>
<dt>(perfect-mouse yes)</p>
<dd>When enabled, the X server is queried for the mouse&#8217;s current position on each motion event, rather than relying on the position hint. This means painting with large brushes should be more accurate, but it may be slower. Conversely, on some X servers enabling this option results in faster painting. Possible values are yes and no. </p>
<dt>(cursor-mode tool-icon)</p>
<dd>Sets the type of mouse pointers to use. Possible values are tool-icon, tool-crosshair and crosshair. </p>
<dt>(cursor-updating yes)</p>
<dd>Context-dependent mouse pointers are helpful. They are enabled by default. However, they require overhead that you may want to do without. Possible values are yes and no. </p>
<dt>(show-brush-outline yes)</p>
<dd>When enabled, all paint tools will show a preview of the current brush&#8217;s outline. Possible values are yes and no. </p>
<dt>(show-paint-tool-cursor yes)</p>
<dd>When enabled, the mouse pointer will be shown over the image while using a paint tool. Possible values are yes and no. </p>
<dt>(image-title-format &quot;%D*%f-%p.%i (%t, %L) %wx%h&quot;)</p>
<dd>Sets the text to appear in image window titles. This is a format string; certain % character sequences are recognised and expanded as follows: </p>
<p> %% literal percent sign<br />
 %f bare filename, or &quot;Untitled&quot;<br />
 %F full path to file, or &quot;Untitled&quot;<br />
 %p PDB image id<br />
 %i view instance number<br />
 %t image type (RGB, grayscale, indexed)<br />
 %z zoom factor as a percentage<br />
 %s source scale factor<br />
 %d destination scale factor<br />
 %Dx expands to x if the image is dirty, the empty string otherwise<br />
 %Cx expands to x if the image is clean, the empty string otherwise<br />
 %B expands to (modified) if the image is dirty, the empty string otherwise<br />
 %A expands to (clean) if the image is clean, the empty string otherwise<br />
 %l the number of layers<br />
 %L the number of layers (long form)<br />
 %m memory used by the image<br />
 %n the name of the active layer/channel<br />
 %P the PDB id of the active layer/channel<br />
 %w image width in pixels<br />
 %W image width in real-world units<br />
 %h image height in pixels<br />
 %H image height in real-world units<br />
 %M the image size expressed in megapixels<br />
 %u unit symbol<br />
 %U unit abbreviation </p>
<dt>(image-status-format &quot;%n (%m)&quot;)</p>
<dd>Sets the text to appear in image window status bars. This is a format string; certain % character sequences are recognised and expanded as follows: </p>
<p> %% literal percent sign<br />
 %f bare filename, or &quot;Untitled&quot;<br />
 %F full path to file, or &quot;Untitled&quot;<br />
 %p PDB image id<br />
 %i view instance number<br />
 %t image type (RGB, grayscale, indexed)<br />
 %z zoom factor as a percentage<br />
 %s source scale factor<br />
 %d destination scale factor<br />
 %Dx expands to x if the image is dirty, the empty string otherwise<br />
 %Cx expands to x if the image is clean, the empty string otherwise<br />
 %B expands to (modified) if the image is dirty, the empty string otherwise<br />
 %A expands to (clean) if the image is clean, the empty string otherwise<br />
 %l the number of layers<br />
 %L the number of layers (long form)<br />
 %m memory used by the image<br />
 %n the name of the active layer/channel<br />
 %P the PDB id of the active layer/channel<br />
 %w image width in pixels<br />
 %W image width in real-world units<br />
 %h image height in pixels<br />
 %H image height in real-world units<br />
 %M the image size expressed in megapixels<br />
 %u unit symbol<br />
 %U unit abbreviation </p>
<dt>(monitor-xresolution 96.000000)</p>
<dd>Sets the monitor&#8217;s horizontal resolution, in dots per inch. If set to 0, forces the X server to be queried for both horizontal and vertical resolution information. This is a float value. </p>
<dt>(monitor-yresolution 96.000000)</p>
<dd>Sets the monitor&#8217;s vertical resolution, in dots per inch. If set to 0, forces the X server to be queried for both horizontal and vertical resolution information. This is a float value. </p>
<dt>(monitor-resolution-from-windowing-system yes)</p>
<dd>When enabled, GIMP will use the monitor resolution from the windowing system. Possible values are yes and no. </p>
<dt>(navigation-preview-size medium)</p>
<dd>Sets the size of the navigation preview available in the lower right corner of the image window. Possible values are tiny, extra-small, small, medium, large, extra-large, huge, enormous and gigantic. </p>
<dt>(default-view</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(show-menubar yes)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(show-statusbar yes)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(show-rulers yes)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(show-scrollbars yes)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(show-selection yes)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(show-layer-boundary yes)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(show-guides yes)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(show-grid no)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(show-sample-points yes)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(padding-mode default)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(padding-color&nbsp;(color-rgb 1.000000 1.000000 1.000000))) </p>
<p> Sets the default settings for the image view. This is a parameter list. </p>
<dt>(default-fullscreen-view</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(show-menubar yes)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(show-statusbar yes)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(show-rulers yes)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(show-scrollbars yes)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(show-selection yes)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(show-layer-boundary yes)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(show-guides yes)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(show-grid no)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(show-sample-points yes)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(padding-mode default)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(padding-color&nbsp;(color-rgb 1.000000 1.000000 1.000000))) </p>
<p> Sets the default settings used when an image is viewed in fullscreen mode. This is a parameter list. </p>
<dt>(default-snap-to-guides yes)</p>
<dd>Snap to guides by default in new image windows. Possible values are yes and no. </p>
<dt>(default-snap-to-grid no)</p>
<dd>Snap to the grid by default in new image windows. Possible values are yes and no. </p>
<dt>(default-snap-to-canvas no)</p>
<dd>Snap to the canvas edge by default in new image windows. Possible values are yes and no. </p>
<dt>(default-snap-to-path no)</p>
<dd>Snap to the active path by default in new image windows. Possible values are yes and no. </p>
<dt>(activate-on-focus yes)</p>
<dd>When enabled, an image will become the active image when its image window receives the focus. This is useful for window managers using &quot;click to focus&quot;.<br />
&nbsp;Possible values are yes and no. </p>
<dt>(space-bar-action pan)</p>
<dd>What to do when the space bar is pressed in the image window. Possible values are none, pan and move. </p>
<dt>(zoom-quality high)</p>
<dd>There&#8217;s a tradeoff between speed and quality of the zoomed-out display. Possible values are low and high. </p>
<dt>(use-event-history no)</p>
<dd>Bugs in event history buffer are frequent so in case of cursor offset problems turning it off helps. Possible values are yes and no. </p>
<dt>(move-tool-changes-active no)</p>
<dd>If enabled, the move tool sets the edited layer or path as active. This used to be the default behaviour in older versions. Possible values are yes and no. </p>
<dt>(image-map-tool-max-recent 10)</p>
<dd>How many recent settings to keep around in color correction tools This is an integer value. </p>
<dt>(trust-dirty-flag no)</p>
<dd>When enabled, GIMP will not save an image if it has not been changed since it was opened. Possible values are yes and no. </p>
<dt>(save-device-status no)</p>
<dd>Remember the current tool, pattern, color, and brush across GIMP sessions. Possible values are yes and no. </p>
<dt>(save-session-info yes)</p>
<dd>Save the positions and sizes of the main dialogs when GIMP exits. Possible values are yes and no. </p>
<dt>(restore-session yes)</p>
<dd>Let GIMP try to restore your last saved session on each startup. Possible values are yes and no. </p>
<dt>(save-tool-options no)</p>
<dd>Save the tool options when GIMP exits. Possible values are yes and no. </p>
<dt>(show-tooltips yes)</p>
<dd>Show a tooltip when the pointer hovers over an item. Possible values are yes and no. </p>
<dt>(tearoff-menus yes)</p>
<dd>When enabled, menus can be torn off. Possible values are yes and no. </p>
<dt>(can-change-accels no)</p>
<dd>When enabled, you can change keyboard shortcuts for menu items by hitting a key combination while the menu item is highlighted. Possible values are yes and no. </p>
<dt>(save-accels yes)</p>
<dd>Save changed keyboard shortcuts when GIMP exits. Possible values are yes and no. </p>
<dt>(restore-accels yes)</p>
<dd>Restore saved keyboard shortcuts on each GIMP startup. Possible values are yes and no. </p>
<dt>(last-opened-size 10)</p>
<dd>How many recently opened image filenames to keep on the File menu. This is an integer value. </p>
<dt>(max-new-image-size 128M)</p>
<dd>GIMP will warn the user if an attempt is made to create an image that would take more memory than the size specified here. The integer size can contain a suffix of &#8216;B&#8217;, &#8216;K&#8217;, &#8216;M&#8217; or &#8216;G&#8217; which makes GIMP interpret the size as being specified in bytes, kilobytes, megabytes or gigabytes. If no suffix is specified the size defaults to being specified in kilobytes. </p>
<dt>(toolbox-color-area yes)</p>
<dd>Show the current foreground and background colors in the toolbox. Possible values are yes and no. </p>
<dt>(toolbox-foo-area no)</p>
<dd>Show the currently selected brush, pattern and gradient in the toolbox. Possible values are yes and no. </p>
<dt>(toolbox-image-area no)</p>
<dd>Show the currently active image in the toolbox. Possible values are yes and no. </p>
<dt>(toolbox-wilber yes)</p>
<dd>Show the GIMP mascot at the top of the toolbox. Possible values are yes and no. </p>
<dt>(theme-path &quot;${gimp_dir}/themes:${gimp_data_dir}/themes&quot;)</p>
<dd>Sets the theme search path. This is a colon-separated list of folders to search. </p>
<dt>(theme &quot;Default&quot;)</p>
<dd>The name of the theme to use. This is a string value. </p>
<dt>(use-help yes)</p>
<dd>When enabled, pressing F1 will open the help browser. Possible values are yes and no. </p>
<dt>(show-help-button yes)</p>
<dd>When enabled, dialogs will show a help button that gives access to the related help page. Without this button, the help page can still be reached by pressing F1. Possible values are yes and no. </p>
<dt>(help-locales &quot;&quot;)</p>
<dd>Specifies the language preferences used by the help system. This is a colon-separated list of language identifiers with decreasing priority. If empty, the language is taken from the user&#8217;s locale setting. This is a string value. </p>
<dt>(help-browser gimp)</p>
<dd>Sets the browser used by the help system. Possible values are gimp and web-browser. </p>
<dt>(user-manual-online no)</p>
<dd>When enabled, the online user manual will be used by the help system. Otherwise the locally installed copy is used. Possible values are yes and no. </p>
<dt>(user-manual-online-uri &quot;<a rel="nofollow" href="http://docs.gimp.org/2.8">http://docs.gimp.org/2.8</a>&quot;)</p>
<dd>The location of the online user manual. This is used if &#8216;user-manual-online&#8217; is enabled. This is a string value. </p>
<dt>(dock-window-hint utility)</p>
<dd>The window type hint that is set on dock windows and the toolbox window. This may affect the way your window manager decorates and handles these windows. Possible values are normal, utility and keep-above. </p>
<dt>(cursor-format pixbuf)</p>
<dd>Sets the pixel format to use for mouse pointers. Possible values are bitmap and pixbuf. </p>
<dt>(cursor-handedness right)</p>
<dd>Sets the handedness for cursor positioning. Possible values are left and right. </p>
<dt>(fractalexplorer-path &quot;${gimp_dir}/fractalexplorer:${gimp_data_dir}/fractalexplorer&quot;)</p>
<dd>Where to search for fractals used by the Fractal Explorer plug-in. This is a colon-separated list of folders to search. </p>
<dt>(gfig-path &quot;${gimp_dir}/gfig:${gimp_data_dir}/gfig&quot;)</p>
<dd>Where to search for Gfig figures used by the Gfig plug-in. This is a colon-separated list of folders to search. </p>
<dt>(gflare-path &quot;${gimp_dir}/gflare:${gimp_data_dir}/gflare&quot;)</p>
<dd>Where to search for gflares used by the GFlare plug-in. This is a colon-separated list of folders to search. </p>
<dt>(gimpressionist-path &quot;${gimp_dir}/gimpressionist:${gimp_data_dir}/gimpressionist&quot;)</p>
<dd>Where to search for data used by the Gimpressionist plug-in. This is a colon-separated list of folders to search. </p>
<dt>(script-fu-path &quot;${gimp_dir}/scripts:${gimp_data_dir}/scripts&quot;)</p>
<dd>This path will be searched for scripts when the Script-Fu plug-in is run. This is a colon-separated list of folders to search. </p>
</dl>
<h2>Path Expansion</h2>
<p>Strings of type PATH are expanded in a manner similar to <code><a href="/docs/linux/man/1-bash/">bash</a></code>(1). Specifically: tilde (~) is expanded to the user&#8217;s home directory. Note that the bash feature of being able to refer to other user&#8217;s home directories by writing ~userid/ is not valid in this file. </p>
<p> ${variable} is expanded to the current value of an environment variable. There are a few variables that are pre-defined:</p>
<dl>
<dt><i>gimp_dir</i></p>
<dd>The personal gimp directory which is set to the value of the environment variable GIMP2_DIRECTORY or to ~/.gimp-2.8.</p>
<dt><i>gimp_data_dir</i></p>
<dd>Base for paths to shareable data, which is set to the value of the environment variable GIMP2_DATADIR or to the compiled-in default value ${datarootdir}/gimp/2.0.</p>
<dt><i>gimp_plug_in_dir</i></p>
<dd>Base to paths for architecture-specific plugins and modules, which is set to the value of the environment variable GIMP2_PLUGINDIR or to the compiled-in default value /usr/lib/gimp/2.0.</p>
<dt><i>gimp_sysconf_dir</i></p>
<dd>Path to configuration files, which is set to the value of the environment variable GIMP2_SYSCONFDIR or to the compiled-in default value /etc/gimp/2.0. </p>
</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/gimp/2.0/gimprc</i></p>
<dd>System-wide configuration file</p>
<dt><i></i><code>$HOME</code>/.gimp-2.8/gimprc</p>
<dd>Per-user configuration file </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-gimp/">gimp</a></code>(1) </p>
