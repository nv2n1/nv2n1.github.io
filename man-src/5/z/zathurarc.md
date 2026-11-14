---
title: "zathurarc(5)"
name: "zathurarc"
section: "5"
letter: "z"
url: "/docs/linux/man/5-zathurarc/"
description: "zathurarc – zathura configuration file"
---

<p>zathurarc &#8211; zathura configuration file</p>
<h2>Synopsis</h2>
<p>/etc/zathurarc, $XDG_CONFIG_HOME/zathura/zathurarc</p>
<h2>Description</h2>
<p>The <i>zathurarc</i> file is a simple plain text file that can be populated with various commands to change the behaviour and the look of zathura which we are going to describe in the following subsections. Each line (besides empty lines and comments (which start with a prepended #) is evaluated on its own, so it is not possible to write multiple commands in one single line.</p>
<h2>Commands</h2>
<h3>set &#8211; Changing options</h3>
<p>In addition to the build-in <code>:set</code> command zathura offers more options to be changed and makes those changes permanent. To overwrite an option you just have to add a line structured like the following </p>
<pre>set &lt;option&gt; &lt;new value&gt;</pre>
<p>The <code>option</code> field has to be replaced with the name of the option that should be changed and the <code>new value</code> field has to be replaced with the new value the option should get. The type of the value can be one of the following:</p>
<dl>
<dt>&bull;</p>
<dd>INT &#8211; An integer number</p>
<dt>&bull;</p>
<dd>FLOAT &#8211; A floating point number</p>
<dt>&bull;</p>
<dd>STRING &#8211; A character string</p>
<dt>&bull;</p>
<dd>BOOL &#8211; A boolean value (&quot;true&quot; for true, &quot;false&quot; for false) </p>
<p> In addition we advice you to check the options to get a more detailed view of the options that can be changed and which values they should be set to. </p>
<p> The following example should give some deeper insight of how the <code>set</code> command can be used </p>
<pre>set option1 5
set option2 2.0
set option3 hello
set option4 hello\ world
set option5 &quot;hello world&quot;</pre>
<p>If you want to use <code>color codes</code> for some options, make sure to quote them accordingly or to escape the hash symbol. </p>
<pre>set default-fg &quot;#CCBBCC&quot;
set default-fg \#CCBBCC</pre>
</dl>
<h3>map &#8211; Mapping a shortcut</h3>
<p>It is possible to map or remap new key bindings to shortcut functions which allows a high level of customization. The <code>:map</code> command can also be used in the <i>zathurarc</i> file to make those changes permanent: </p>
<pre>map [mode] &lt;binding&gt; &lt;shortcut function&gt; &lt;argument&gt;</pre>
<h3>Mode</h3>
<p>The <code>map</code> command expects several arguments where only the <code>binding</code> as well as the <code>shortcut-function</code> argument is required. Since zathura uses several modes it is possible to map bindings only for a specific mode by passing the <code>mode</code> argument which can take one of the following values:</p>
<dl>
<dt>&bull;</p>
<dd>normal (default)</p>
<dt>&bull;</p>
<dd>fullscreen</p>
<dt>&bull;</p>
<dd>index </p>
<p> The brackets around the value are mandatory.</dl>
<h3>Single key binding</h3>
<p>The (possible) second argument defines the used key binding that should be mapped to the shortcut function and is structured like the following. On the one hand it is possible to just assign single letters, numbers or signs to it: </p>
<pre>map a shortcut_function
map b shortcut_function
map c shortcut_function
map 1 shortcut_function
map 2 shortcut_function
map 3 shortcut_function
map ! shortcut_function
map ? shortcut_function</pre>
<h3>Using modifiers</h3>
<p>It is also possible to use modifiers like the Control or Alt button on the keyboard. It is possible to use the following modifiers:</p>
<dl>
<dt>&bull;</p>
<dd>A &#8211; Alt</p>
<dt>&bull;</p>
<dd>C &#8211; Control</p>
<dt>&bull;</p>
<dd>S &#8211; Shift </p>
<p> Now it is required to define the <code>binding</code> with the following structure: </p>
<pre>map &lt;A-a&gt; shortcut_function
map &lt;C-a&gt; shortcut_function</pre>
</dl>
<h3>Special keys</h3>
<p>zathura allows it also to assign keys like the space bar or the tab button which also have to be written in between angle brackets. The following special keys are currently available: </p>
<pre>Identifier Description
BackSpace Back space
CapsLock Caps lock
Esc Escape
Down Arrow down
Up Arrow up
Left Arrow left
Right Arrow right
F1 F1
F2 F2
F3 F3
F4 F4
F5 F5
F6 F6
F7 F7
F8 F8
F9 F9
F10 F10
F11 F11
F12 F12
PageDown Page Down
PageUp Page Up
Return Return
Space Space
Super Windows key
Tab Tab</pre>
<p>Of course it is possible to combine those special keys with a modifier. The usage of those keys should be explained by the following examples: </p>
<pre>map &lt;Space&gt; shortcut_function
map &lt;C-Space&gt; shortcut_function</pre>
<h3>Mouse buttons</h3>
<p>It is also possible to map mouse buttons to shortcuts by using the following special keys: </p>
<pre>Identifier Description
Button1 Mouse button 1
Button2 Mouse button 2
Button3 Mouse button 3
Button4 Mouse button 4
Button5 Mouse button 5</pre>
<p>They can also be combined with modifiers: </p>
<pre>map &lt;Button1&gt; shortcut_function
map &lt;C-Button1&gt; shortcut_function</pre>
<h3>Buffer commands</h3>
<p>If a mapping does not match one of the previous definition but is still a valid mapping it will be mapped as a buffer command: </p>
<pre>map abc quit
map test quit</pre>
<h3>Shortcut functions</h3>
<p>The following shortcut functions can be mapped: </p>
<pre>Function Description
abort Switch back to normal mode
adjust_window Adjust page width
change_mode Change current mode
display_link Display link target
focus_inputbar Focus inputbar
follow Follow a link
goto Go to a certain page
jumplist Move forwards/backwards in the jumplist
navigate Navigate to the next/previous page
navigate_index Navigate through the index
print Show the print dialog
quit Quit zathura
recolor Recolor the pages
reload Reload the document
rotate Rotate the page
scroll Scroll
search Search next/previous item
set Set an option
toggle_fullscreen Toggle fullscreen
toggle_index Show or hide index
toggle_inputbar Show or hide inputbar
toggle_page_mode Toggle between one and multiple pages per row
toggle_statusbar Show or hide statusbar
zoom Zoom in or out</pre>
<h3>Pass arguments</h3>
<p>Some shortcut function require or have optional arguments which influence the behaviour of them. Those can be passed as the last argument: map &lt;C-i&gt; zoom in map &lt;C-o&gt; zoom out </p>
<p> Possible arguments are:</p>
<dl>
<dt>&bull;</p>
<dd>best-fit</p>
<dt>&bull;</p>
<dd>bottom</p>
<dt>&bull;</p>
<dd>collapse</p>
<dt>&bull;</p>
<dd>collapse-all</p>
<dt>&bull;</p>
<dd>default</p>
<dt>&bull;</p>
<dd>down</p>
<dt>&bull;</p>
<dd>expand</p>
<dt>&bull;</p>
<dd>expand-all</p>
<dt>&bull;</p>
<dd>full-down</p>
<dt>&bull;</p>
<dd>full-up</p>
<dt>&bull;</p>
<dd>half-down</p>
<dt>&bull;</p>
<dd>half-up</p>
<dt>&bull;</p>
<dd>in</p>
<dt>&bull;</p>
<dd>left</p>
<dt>&bull;</p>
<dd>next</p>
<dt>&bull;</p>
<dd>out</p>
<dt>&bull;</p>
<dd>page-bottom</p>
<dt>&bull;</p>
<dd>page-top</p>
<dt>&bull;</p>
<dd>previous</p>
<dt>&bull;</p>
<dd>right</p>
<dt>&bull;</p>
<dd>rotate-ccw</p>
<dt>&bull;</p>
<dd>rotate-cw</p>
<dt>&bull;</p>
<dd>select</p>
<dt>&bull;</p>
<dd>specific</p>
<dt>&bull;</p>
<dd>toggle</p>
<dt>&bull;</p>
<dd>top</p>
<dt>&bull;</p>
<dd>up</p>
<dt>&bull;</p>
<dd>width</dl>
<h3>unmap &#8211; Removing a shortcut</h3>
<p>In addition to mapping or remaping custom key bindings it is possible to remove existing ones by using the <code>:unmap</code> command. The command is used in the following way (the explanation of the parameters is described in the <code>map</code> section of this document </p>
<pre>unmap [mode] &lt;binding&gt;</pre>
<h2>Options</h2>
<h3>girara</h3>
<p>This section describes settings concerning the behaviour of libgirara and zathura. The settings described here can be changed with <code>set</code>.</p>
<h3>n-completion-items</h3>
<p>Defines the maximum number of displayed completion entries.</p>
<dl>
<dt>&bull;</p>
<dd>Value type: Integer</p>
<dt>&bull;</p>
<dd>Default value: 15</dl>
<h3>completion-bg</h3>
<p>Defines the background color that is used for command line completion entries</p>
<dl>
<dt>&bull;</p>
<dd>Value type: String</p>
<dt>&bull;</p>
<dd>Default value: #232323</dl>
<h3>completion-fg</h3>
<p>Defines the foreground color that is used for command line completion entries</p>
<dl>
<dt>&bull;</p>
<dd>Value type: String</p>
<dt>&bull;</p>
<dd>Default value: #DDDDDD</dl>
<h3>completion-group-bg</h3>
<p>Defines the background color that is used for command line completion group elements</p>
<dl>
<dt>&bull;</p>
<dd>Value type: String</p>
<dt>&bull;</p>
<dd>Default value: #000000</dl>
<h3>completion-group-fg</h3>
<p>Defines the foreground color that is used for command line completion group elements</p>
<dl>
<dt>&bull;</p>
<dd>Value type: String</p>
<dt>&bull;</p>
<dd>Default value: #DEDEDE</dl>
<h3>completion-highlight-bg</h3>
<p>Defines the background color that is used for the current command line completion element</p>
<dl>
<dt>&bull;</p>
<dd>Value type: String</p>
<dt>&bull;</p>
<dd>Default value: #9FBC00</dl>
<h3>completion-highlight-fg</h3>
<p>Defines the foreground color that is used for the current command line completion element</p>
<dl>
<dt>&bull;</p>
<dd>Value type: String</p>
<dt>&bull;</p>
<dd>Default value: #232323</dl>
<h3>default-fg</h3>
<p>Defines the default foreground color</p>
<dl>
<dt>&bull;</p>
<dd>Value type: String</p>
<dt>&bull;</p>
<dd>Default value: #DDDDDD</dl>
<h3>default-bg</h3>
<p>Defines the default background color</p>
<dl>
<dt>&bull;</p>
<dd>Value type: String</p>
<dt>&bull;</p>
<dd>Default value: #000000</dl>
<h3>exec-command</h3>
<p>Defines a command the should be prepanded to any command run with exec.</p>
<dl>
<dt>&bull;</p>
<dd>Value type: String</p>
<dt>&bull;</p>
<dd>Default value:</dl>
<h3>font</h3>
<p>Defines the font that will be used</p>
<dl>
<dt>&bull;</p>
<dd>Value type: String</p>
<dt>&bull;</p>
<dd>Default value: monospace normal 9</dl>
<h3>guioptions</h3>
<p>Shows or hides GUI elements. If it contains &#8216;c&#8217;, the command line is displayed. If it contains &#8216;s&#8217;, the statusbar is displayed. If it contains &#8216;h&#8217;, the vertical scrollbar is displayed. If it contains &#8216;v&#8217;, the horizontal scrollbar is displayed.</p>
<dl>
<dt>&bull;</p>
<dd>Value type: String</p>
<dt>&bull;</p>
<dd>Default value: s</dl>
<h3>inputbar-bg</h3>
<p>Defines the background color for the inputbar</p>
<dl>
<dt>&bull;</p>
<dd>Value type: String</p>
<dt>&bull;</p>
<dd>Default value: #131313</dl>
<h3>inputbar-fg</h3>
<p>Defines the foreground color for the inputbar</p>
<dl>
<dt>&bull;</p>
<dd>Value type: String</p>
<dt>&bull;</p>
<dd>Default value: #9FBC00</dl>
<h3>notification-bg</h3>
<p>Defines the background color for a notification</p>
<dl>
<dt>&bull;</p>
<dd>Value type: String</p>
<dt>&bull;</p>
<dd>Default value: #FFFFFF</dl>
<h3>notification-fg</h3>
<p>Defines the foreground color for a notification</p>
<dl>
<dt>&bull;</p>
<dd>Value type: String</p>
<dt>&bull;</p>
<dd>Default value: #000000</dl>
<h3>notification-error-bg</h3>
<p>Defines the background color for an error notification</p>
<dl>
<dt>&bull;</p>
<dd>Value type: String</p>
<dt>&bull;</p>
<dd>Default value: #FFFFFF</dl>
<h3>notification-error-fg</h3>
<p>Defines the foreground color for an error notification</p>
<dl>
<dt>&bull;</p>
<dd>Value type: String</p>
<dt>&bull;</p>
<dd>Default value: #FF1212</dl>
<h3>notification-warning-bg</h3>
<p>Defines the background color for a warning notification</p>
<dl>
<dt>&bull;</p>
<dd>Value type: String</p>
<dt>&bull;</p>
<dd>Default value: #FFFFFF</dl>
<h3>notification-warning-fg</h3>
<p>Defines the foreground color for a warning notification</p>
<dl>
<dt>&bull;</p>
<dd>Value type: String</p>
<dt>&bull;</p>
<dd>Default value: #FFF712</dl>
<h3>tabbar-fg</h3>
<p>Defines the foreground color for a tab</p>
<dl>
<dt>&bull;</p>
<dd>Value type: String</p>
<dt>&bull;</p>
<dd>Default value: #FFFFFF</dl>
<h3>tabbar-bg</h3>
<p>Defines the background color for a tab</p>
<dl>
<dt>&bull;</p>
<dd>Value type: String</p>
<dt>&bull;</p>
<dd>Default value: #000000</dl>
<h3>tabbar-focus-fg</h3>
<p>Defines the foreground color for the focused tab</p>
<dl>
<dt>&bull;</p>
<dd>Value type: String</p>
<dt>&bull;</p>
<dd>Default value: #9FBC00</dl>
<h3>tabbar-focus-bg</h3>
<p>Defines the background color for the focused tab</p>
<dl>
<dt>&bull;</p>
<dd>Value type: String</p>
<dt>&bull;</p>
<dd>Default value: #000000</dl>
<h3>show-scrollbars</h3>
<p>Defines if both the horizontal and vertical scrollbars should be shown or not. Deprecated, use &#8216;guioptions&#8217; instead.</p>
<dl>
<dt>&bull;</p>
<dd>Value type: Boolean</p>
<dt>&bull;</p>
<dd>Default value: false</dl>
<h3>show-h-scrollbar</h3>
<p>Defines whether to show/hide the horizontal scrollbar. Deprecated, use &#8216;guioptions&#8217; instead.</p>
<dl>
<dt>&bull;</p>
<dd>Value type: Boolean</p>
<dt>&bull;</p>
<dd>Default value: false</dl>
<h3>show-v-scrollbar</h3>
<p>Defines whether to show/hide the vertical scrollbar. Deprecated, use &#8216;guioptions&#8217; instead.</p>
<dl>
<dt>&bull;</p>
<dd>Value type: Boolean</p>
<dt>&bull;</p>
<dd>Default value: false</dl>
<h3>statusbar-bg</h3>
<p>Defines the background color of the statusbar</p>
<dl>
<dt>&bull;</p>
<dd>Value type: String</p>
<dt>&bull;</p>
<dd>Default value: #000000</dl>
<h3>statusbar-fg</h3>
<p>Defines the foreground color of the statusbar</p>
<dl>
<dt>&bull;</p>
<dd>Value type: String</p>
<dt>&bull;</p>
<dd>Default value: #FFFFFF</dl>
<h3>statusbar-h-padding</h3>
<p>Defines the horizontal padding of the statusbar and notificationbar</p>
<dl>
<dt>&bull;</p>
<dd>Value type: Integer</p>
<dt>&bull;</p>
<dd>Default value: 8</dl>
<h3>statusbar-v-padding</h3>
<p>Defines the vertical padding of the statusbar and notificationbar</p>
<dl>
<dt>&bull;</p>
<dd>Value type: Integer</p>
<dt>&bull;</p>
<dd>Default value: 2</dl>
<h3>window-height</h3>
<p>Defines the window height on startup</p>
<dl>
<dt>&bull;</p>
<dd>Value type: Integer</p>
<dt>&bull;</p>
<dd>Default value: 600</dl>
<h3>window-width</h3>
<p>Defines the window width on startup</p>
<dl>
<dt>&bull;</p>
<dd>Value type: Integer</p>
<dt>&bull;</p>
<dd>Default value: 800</dl>
<h3>zathura</h3>
<p>This section describes settings concerning the behaviour of zathura.</p>
<h3>abort-clear-search</h3>
<p>Defines if the search results should be cleared on abort.</p>
<dl>
<dt>&bull;</p>
<dd>Value type: Boolean</p>
<dt>&bull;</p>
<dd>Default value: true</dl>
<h3>adjust-open</h3>
<p>Defines which auto adjustment mode should be used if a document is loaded. Possible options are &quot;best-fit&quot; and &quot;width&quot;.</p>
<dl>
<dt>&bull;</p>
<dd>Value type: String</p>
<dt>&bull;</p>
<dd>Default value: best-fit</dl>
<h3>advance-pages-per-row</h3>
<p>Defines if the number of pages per row should be honored when advancing a page.</p>
<dl>
<dt>&bull;</p>
<dd>Value type: Boolean</p>
<dt>&bull;</p>
<dd>Default value: false</dl>
<h3>incremental-search</h3>
<p>En/Disables incremental search (search while typing).</p>
<dl>
<dt>&bull;</p>
<dd>Value type: Boolean</p>
<dt>&bull;</p>
<dd>Default value: true</dl>
<h3>highlight-color</h3>
<p>Defines the color that is used for highlighting parts of the document (e.g.: show search results)</p>
<dl>
<dt>&bull;</p>
<dd>Value type: String</p>
<dt>&bull;</p>
<dd>Default value: #9FBC00</dl>
<h3>highlight-active-color</h3>
<p>Defines the color that is used to show the current selected highlighted element (e.g: current search result)</p>
<dl>
<dt>&bull;</p>
<dd>Value type: String</p>
<dt>&bull;</p>
<dd>Default value: #00BC00</dl>
<h3>highlight-transparency</h3>
<p>Defines the opacity of a highlighted element</p>
<dl>
<dt>&bull;</p>
<dd>Value type: Float</p>
<dt>&bull;</p>
<dd>Default value: 0.5</dl>
<h3>page-padding</h3>
<p>The page padding defines the gap in pixels between each rendered page.</p>
<dl>
<dt>&bull;</p>
<dd>Value type: Integer</p>
<dt>&bull;</p>
<dd>Default value: 1</dl>
<h3>page-cache-size</h3>
<p>Defines the maximum number of pages that could be kept in the page cache. When the cache is full and a new page that isn&#8217;t cached becomes visible, the least recently viewed page in the cache will be evicted to make room for the new one. Large values for this variable are NOT recommended, because this will lead to consuming a significant portion of the system memory.</p>
<dl>
<dt>&bull;</p>
<dd>Value type: Integer</p>
<dt>&bull;</p>
<dd>Default value: 15</dl>
<h3>pages-per-row</h3>
<p>Defines the number of pages that are rendered next to each other in a row.</p>
<dl>
<dt>&bull;</p>
<dd>Value type: Integer</p>
<dt>&bull;</p>
<dd>Default value: 1</dl>
<h3>first-page-column</h3>
<p>Defines the column in which the first page will be displayed.</p>
<dl>
<dt>&bull;</p>
<dd>Value type: Integer</p>
<dt>&bull;</p>
<dd>Default value: 1</dl>
<h3>recolor</h3>
<p>En/Disables recoloring</p>
<dl>
<dt>&bull;</p>
<dd>Value type: Boolean</p>
<dt>&bull;</p>
<dd>Default value: false</dl>
<h3>recolor-keephue</h3>
<p>En/Disables keeping original hue when recoloring</p>
<dl>
<dt>&bull;</p>
<dd>Value type: Boolean</p>
<dt>&bull;</p>
<dd>Default value: false</dl>
<h3>recolor-darkcolor</h3>
<p>Defines the color value that is used to represent dark colors in recoloring mode</p>
<dl>
<dt>&bull;</p>
<dd>Value type: String</p>
<dt>&bull;</p>
<dd>Default value: #FFFFFF</dl>
<h3>recolor-lightcolor</h3>
<p>Defines the color value that is used to represent light colors in recoloring mode</p>
<dl>
<dt>&bull;</p>
<dd>Value type: String</p>
<dt>&bull;</p>
<dd>Default value: #000000</dl>
<h3>render-loading</h3>
<p>Defines if the &quot;Loading&#8230;&quot; text should be displayed if a page is rendered.</p>
<dl>
<dt>&bull;</p>
<dd>Value type: Boolean</p>
<dt>&bull;</p>
<dd>Default value: true</dl>
<h3>render-loading-bg</h3>
<p>Defines the background color that is used for the &quot;Loading&#8230;&quot; text.</p>
<dl>
<dt>&bull;</p>
<dd>Value type: String</p>
<dt>&bull;</p>
<dd>Default value: #FFFFFF</dl>
<h3>render-loading-fg</h3>
<p>Defines the foreground color that is used for the &quot;Loading&#8230;&quot; text.</p>
<dl>
<dt>&bull;</p>
<dd>Value type: String</p>
<dt>&bull;</p>
<dd>Default value: #000000</dl>
<h3>scroll-hstep</h3>
<p>Defines the horizontal step size of scrolling by calling the scroll command once</p>
<dl>
<dt>&bull;</p>
<dd>Value type: Float</p>
<dt>&bull;</p>
<dd>Default value: -1</dl>
<h3>scroll-step</h3>
<p>Defines the step size of scrolling by calling the scroll command once</p>
<dl>
<dt>&bull;</p>
<dd>Value type: Float</p>
<dt>&bull;</p>
<dd>Default value: 40</dl>
<h3>scroll-full-overlap</h3>
<p>Defines the proportion of the current viewing area that should be visible after scrolling a full page.</p>
<dl>
<dt>&bull;</p>
<dd>Value type: Float</p>
<dt>&bull;</p>
<dd>Default value: 0.1</dl>
<h3>scroll-wrap</h3>
<p>Defines if the last/first page should be wrapped</p>
<dl>
<dt>&bull;</p>
<dd>Value type: Boolean</p>
<dt>&bull;</p>
<dd>Default value: false</dl>
<h3>scroll-page-aware</h3>
<p>Defines if scrolling by half or full pages stops at page boundaries.</p>
<dl>
<dt>&bull;</p>
<dd>Value type: Boolean</p>
<dt>&bull;</p>
<dd>Default value: false</dl>
<h3>link-zoom</h3>
<p>En/Disables the ability of changing zoom when following links.</p>
<dl>
<dt>&bull;</p>
<dd>Value type: Boolean</p>
<dt>&bull;</p>
<dd>Default value: true</dl>
<h3>link-hadjust</h3>
<p>En/Disables aligning to the left internal link targets, for example from the index.</p>
<dl>
<dt>&bull;</p>
<dd>Value type: Boolean</p>
<dt>&bull;</p>
<dd>Default value: true</dl>
<h3>search-hadjust</h3>
<p>En/Disables horizontally centered search results.</p>
<dl>
<dt>&bull;</p>
<dd>Value type: Boolean</p>
<dt>&bull;</p>
<dd>Default value: true</dl>
<h3>window-title-basename</h3>
<p>Use basename of the file in the window title.</p>
<dl>
<dt>&bull;</p>
<dd>Value type: Boolean</p>
<dt>&bull;</p>
<dd>Default value: false</dl>
<h3>window-title-page</h3>
<p>Display the page number in the window title.</p>
<dl>
<dt>&bull;</p>
<dd>Value type: Boolean</p>
<dt>&bull;</p>
<dd>Default value: false</dl>
<h3>statusbar-basename</h3>
<p>Use basename of the file in the statusbar.</p>
<dl>
<dt>&bull;</p>
<dd>Value type: Boolean</p>
<dt>&bull;</p>
<dd>Default value: false</dl>
<h3>zoom-center</h3>
<p>En/Disables horizontally centered zooming.</p>
<dl>
<dt>&bull;</p>
<dd>Value type: Boolean</p>
<dt>&bull;</p>
<dd>Default value: False</dl>
<h3>zoom-max</h3>
<p>Defines the maximum percentage that the zoom level can be.</p>
<dl>
<dt>&bull;</p>
<dd>Value type: Integer</p>
<dt>&bull;</p>
<dd>Default value: 1000</dl>
<h3>zoom-min</h3>
<p>Defines the minimum percentage that the zoom level can be.</p>
<dl>
<dt>&bull;</p>
<dd>Value type: Integer</p>
<dt>&bull;</p>
<dd>Default value: 10</dl>
<h3>zoom-step</h3>
<p>Defines the amount of percent that is zoomed in or out on each command.</p>
<dl>
<dt>&bull;</p>
<dd>Value type: Integer</p>
<dt>&bull;</p>
<dd>Default value: 10</dl>
<h3>selection-clipboard</h3>
<p>Defines the X clipboard into which mouse-selected data will be written. When it is &quot;clipboard&quot;, selected data will be written to the CLIPBOARD clipboard, and can be pasted using the Ctrl+v key combination. When it is &quot;primary&quot;, selected data will be written to the PRIMARY clipboard, and can be pasted using the middle mouse button, or the Shift-Insert key combination.</p>
<dl>
<dt>&bull;</p>
<dd>Value type: String</p>
<dt>&bull;</p>
<dd>Default value: primary</dl>
<h3>syntex-dbus-service</h3>
<p>En/Disables the D-Bus service required for synctex forward synchronization.</p>
<dl>
<dt>&bull;</p>
<dd>Value type: Boolean</p>
<dt>&bull;</p>
<dd>Default value: true</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-zathura/">zathura</a>(1)</p>
<h2>Author</h2>
<p>pwmt.org</p>
