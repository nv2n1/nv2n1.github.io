---
title: "elinkskeys(5)"
name: "elinkskeys"
section: "5"
letter: "e"
url: "/docs/linux/man/5-elinkskeys/"
description: "elinkskeys – keybindings for ELinks"
---

<p>elinkskeys &#8211; keybindings for ELinks</p>
<h2>Synopsis</h2>
<p>Information on how to configure keybinding and overview of the default keybindings. </p>
<h2>Description</h2>
<p>Key binding for elinks should be placed in the file ~/.elinks/elinks.conf. Note that any information regarding their format/structure may not be up-to-date. If you will discover that, please feed us with a patch. Key binding statements are of the form:</p>
<dl>
<dd>
<pre>bind &lt;keymap&gt; &lt;keystroke&gt; = &lt;action&gt;</pre>
</dl>
<p> where: &lt;keymap&gt;</p>
<dl>
<dd>is <i>main</i>, <i>edit</i>, or <i>menu</i>. The main keymap is used for general browsing. The edit keymap is used for editing text fields. The menu keymap is used for navigating menus.</dl>
<p> &lt;keystroke&gt;</p>
<dl>
<dd>is a case sensitive key, which you can prefix with <i>Ctrl-</i>, <i>Alt-</i>, or both. <i>Ctrl-</i> must be followed by an uppercase key. See below for a list of valid keys.</dl>
<p> &lt;action&gt;</p>
<dl>
<dd>is what the key should do. The actions available are dependent on the keymap, and are listed separately below.</dl>
<p> All words/strings may all be quoted &quot;like so&quot;. Backslashes are escape characters, even if not between quotes. Lines beginning with a hash character (#) are comments. Keys can be unbound just by binding them to the special <i>none</i> action. It may be of use if you accidentally type a key often. </p>
<h2>Example Bindings</h2>
<p>Some sample keybindings: </p>
<dl>
<dd>
<pre>bind &quot;main&quot; &quot;v&quot; = &quot;view-image&quot;
bind &quot;main&quot; &quot;l&quot; = &quot;jump-to-link&quot;
bind &quot;main&quot; &quot;L&quot; = &quot;link-menu&quot;
bind &quot;main&quot; &quot;F10&quot; = &quot;file-menu&quot;
bind &quot;main&quot; &quot;F9&quot; = &quot;menu&quot;
bind &quot;main&quot; &quot;Escape&quot; = &quot;menu&quot;
bind &quot;edit&quot; &quot;Ctrl-R&quot; = &quot;auto-complete-unambiguous&quot;
bind &quot;edit&quot; &quot;Ctrl-W&quot; = &quot;auto-complete&quot;
bind &quot;edit&quot; &quot;Ctrl-K&quot; = &quot;kill-to-eol&quot;
bind &quot;menu&quot; &quot;Ctrl-B&quot; = &quot;page-up&quot;
bind &quot;menu&quot; &quot;PageUp&quot; = &quot;page-up&quot;
bind &quot;menu&quot; &quot;Ctrl-F&quot; = &quot;page-down&quot;
bind &quot;menu&quot; &quot;PageDown&quot; = &quot;page-down&quot;
# ELinks with Lua support
bind &quot;main&quot; &quot;,&quot; = &quot;lua-console&quot;</pre>
</dl>
<h2>Keys</h2>
<p>Valid keys are: alphanumeric characters, punctuation, <i>Enter</i>, <i>Backspace</i>, <i>Tab</i>, <i>Escape</i>, <i>Left</i>, <i>Right</i>, <i>Up</i>, <i>Down</i>, <i>Insert</i>, <i>Delete</i>, <i>Home</i>, <i>End</i>, <i>PageUp</i>, <i>PageDown</i>, <i>F1</i> to <i>F12</i>. </p>
<p> Some keys will need to be quoted or escaped. For example, space can be written as &quot; &quot; (quote space quote), and the quote itself as \&quot; (backslash quote). Backslash can be written as \ (double backslash).</p>
<h2>Keymap Actions</h2>
<h3>Main Actions</h3>
<p>abort-connection</p>
<dl>
<dd>Abort connection.</dl>
<p> add-bookmark</p>
<dl>
<dd>Add a new bookmark.</dl>
<p> add-bookmark-link</p>
<dl>
<dd>Add a new bookmark using current link.</dl>
<p> add-bookmark-tabs</p>
<dl>
<dd>Bookmark all open tabs.</dl>
<p> auth-manager</p>
<dl>
<dd>Open authentication manager.</dl>
<p> backspace-prefix</p>
<dl>
<dd>Backspace the last entered digit of the current prefix.</dl>
<p> bookmark-manager</p>
<dl>
<dd>Open bookmark manager.</dl>
<p> cache-manager</p>
<dl>
<dd>Open cache manager.</dl>
<p> cache-minimize</p>
<dl>
<dd>Free unused cache entries.</dl>
<p> cookie-manager</p>
<dl>
<dd>Open cookie manager.</dl>
<p> cookies-load</p>
<dl>
<dd>Reload cookies file.</dl>
<p> copy-clipboard</p>
<dl>
<dd>Copy text to clipboard.</dl>
<p> document-info</p>
<dl>
<dd>Show information about the current page.</dl>
<p> download-manager</p>
<dl>
<dd>Open download manager.</dl>
<p> exmode</p>
<dl>
<dd>Enter ex-mode (command line).</dl>
<p> file-menu</p>
<dl>
<dd>Open the File menu.</dl>
<p> find-next</p>
<dl>
<dd>Find the next occurrence of the current search text.</dl>
<p> find-next-back</p>
<dl>
<dd>Find the previous occurrence of the current search text.</dl>
<p> forget-credentials</p>
<dl>
<dd>Forget authentication credentials.</dl>
<p> formhist-manager</p>
<dl>
<dd>Open form history manager.</dl>
<p> frame-external-command</p>
<dl>
<dd>Pass URI of current frame to external command.</dl>
<p> frame-maximize</p>
<dl>
<dd>Maximize the current frame.</dl>
<p> frame-next</p>
<dl>
<dd>Move to the next frame.</dl>
<p> frame-prev</p>
<dl>
<dd>Move to the previous frame.</dl>
<p> goto-url</p>
<dl>
<dd>Open &quot;Go to URL&quot; dialog box.</dl>
<p> goto-url-current</p>
<dl>
<dd>Open &quot;Go to URL&quot; dialog box containing the current URL.</dl>
<p> goto-url-current-link</p>
<dl>
<dd>Open &quot;Go to URL&quot; dialog box containing the current link URL.</dl>
<p> goto-url-home</p>
<dl>
<dd>Go to the homepage.</dl>
<p> header-info</p>
<dl>
<dd>Show information about the current page protocol headers.</dl>
<p> history-manager</p>
<dl>
<dd>Open history manager.</dl>
<p> history-move-back</p>
<dl>
<dd>Return to the previous document in history.</dl>
<p> history-move-forward</p>
<dl>
<dd>Go forward in history.</dl>
<p> jump-to-link</p>
<dl>
<dd>Jump to link.</dl>
<p> keybinding-manager</p>
<dl>
<dd>Open keybinding manager.</dl>
<p> kill-backgrounded-connections</p>
<dl>
<dd>Kill all backgrounded connections.</dl>
<p> link-download</p>
<dl>
<dd>Download the current link.</dl>
<p> link-download-image</p>
<dl>
<dd>Download the current image.</dl>
<p> link-download-resume</p>
<dl>
<dd>Attempt to resume download of the current link.</dl>
<p> link-external-command</p>
<dl>
<dd>Pass URI of current link to external command.</dl>
<p> link-follow</p>
<dl>
<dd>Follow the current link.</dl>
<p> link-follow-reload</p>
<dl>
<dd>Follow the current link, forcing reload of the target.</dl>
<p> link-info</p>
<dl>
<dd>Show information about current link.</dl>
<p> link-menu</p>
<dl>
<dd>Open the link context menu.</dl>
<p> link-form-menu</p>
<dl>
<dd>Open the form fields menu.</dl>
<p> lua-console</p>
<dl>
<dd>Open a Lua console.</dl>
<p> mark-goto</p>
<dl>
<dd>Go at a specified mark.</dl>
<p> mark-set</p>
<dl>
<dd>Set a mark.</dl>
<p> menu</p>
<dl>
<dd>Activate the menu.</dl>
<p> move-current-top</p>
<dl>
<dd>Move downwards to put the current line at the top of the screen.</dl>
<p> move-cursor-down</p>
<dl>
<dd>Move cursor down.</dl>
<p> move-cursor-left</p>
<dl>
<dd>Move cursor left.</dl>
<p> move-cursor-line-start</p>
<dl>
<dd>Move cursor to the start of the line.</dl>
<p> move-cursor-right</p>
<dl>
<dd>Move cursor right.</dl>
<p> move-cursor-up</p>
<dl>
<dd>Move cursor up.</dl>
<p> move-document-end</p>
<dl>
<dd>Move to the end of the document.</dl>
<p> move-document-start</p>
<dl>
<dd>Move to the start of the document.</dl>
<p> move-half-page-down</p>
<dl>
<dd>Move downwards by half a page.</dl>
<p> move-half-page-up</p>
<dl>
<dd>Move upwards by half a page.</dl>
<p> move-link-down</p>
<dl>
<dd>Move one link down.</dl>
<p> move-link-down-line</p>
<dl>
<dd>Move to the next line with a link.</dl>
<p> move-link-left</p>
<dl>
<dd>Move one link left.</dl>
<p> move-link-left-line</p>
<dl>
<dd>Move one link left or to the previous link.</dl>
<p> move-link-next</p>
<dl>
<dd>Move to the next link.</dl>
<p> move-link-prev</p>
<dl>
<dd>Move to the previous link.</dl>
<p> move-link-right</p>
<dl>
<dd>Move one link right.</dl>
<p> move-link-right-line</p>
<dl>
<dd>Move one link right or to the next link.</dl>
<p> move-link-up</p>
<dl>
<dd>Move one link up.</dl>
<p> move-link-up-line</p>
<dl>
<dd>Move to the previous line with a link.</dl>
<p> move-page-down</p>
<dl>
<dd>Move downwards by a page.</dl>
<p> move-page-up</p>
<dl>
<dd>Move upwards by a page.</dl>
<p> open-link-in-new-tab</p>
<dl>
<dd>Open the current link in a new tab.</dl>
<p> open-link-in-new-tab-in-background</p>
<dl>
<dd>Open the current link in a new tab in the background.</dl>
<p> open-link-in-new-window</p>
<dl>
<dd>Open the current link in a new window.</dl>
<p> open-new-tab</p>
<dl>
<dd>Open a new tab.</dl>
<p> open-new-tab-in-background</p>
<dl>
<dd>Open a new tab in the background.</dl>
<p> open-new-window</p>
<dl>
<dd>Open a new window.</dl>
<p> open-os-shell</p>
<dl>
<dd>Open an OS shell.</dl>
<p> options-manager</p>
<dl>
<dd>Open options manager.</dl>
<p> quit</p>
<dl>
<dd>Open a quit confirmation dialog box.</dl>
<p> really-quit</p>
<dl>
<dd>Quit without confirmation.</dl>
<p> redraw</p>
<dl>
<dd>Redraw the terminal.</dl>
<p> reload</p>
<dl>
<dd>Reload the current page.</dl>
<p> rerender</p>
<dl>
<dd>Re-render the current page.</dl>
<p> reset-form</p>
<dl>
<dd>Reset form items to their initial values.</dl>
<p> resource-info</p>
<dl>
<dd>Show information about the currently used resources.</dl>
<p> save-as</p>
<dl>
<dd>Save the current document in source form.</dl>
<p> save-formatted</p>
<dl>
<dd>Save the current document in formatted form.</dl>
<p> save-options</p>
<dl>
<dd>Save options.</dl>
<p> save-url-as</p>
<dl>
<dd>Save URL as.</dl>
<p> scroll-down</p>
<dl>
<dd>Scroll down.</dl>
<p> scroll-left</p>
<dl>
<dd>Scroll left.</dl>
<p> scroll-right</p>
<dl>
<dd>Scroll right.</dl>
<p> scroll-up</p>
<dl>
<dd>Scroll up.</dl>
<p> search</p>
<dl>
<dd>Search for a text pattern.</dl>
<p> search-back</p>
<dl>
<dd>Search backwards for a text pattern.</dl>
<p> search-typeahead</p>
<dl>
<dd>Search link text by typing ahead.</dl>
<p> search-typeahead-link</p>
<dl>
<dd>Search link text by typing ahead.</dl>
<p> search-typeahead-text</p>
<dl>
<dd>Search document text by typing ahead.</dl>
<p> search-typeahead-text-back</p>
<dl>
<dd>Search document text backwards by typing ahead.</dl>
<p> show-term-options</p>
<dl>
<dd>Show terminal options dialog.</dl>
<p> submit-form</p>
<dl>
<dd>Submit form.</dl>
<p> submit-form-reload</p>
<dl>
<dd>Submit form and reload.</dl>
<p> tab-close</p>
<dl>
<dd>Close tab.</dl>
<p> tab-close-all-but-current</p>
<dl>
<dd>Close all tabs but the current one.</dl>
<p> tab-external-command</p>
<dl>
<dd>Pass URI of current tab to external command.</dl>
<p> tab-menu</p>
<dl>
<dd>Open the tab menu.</dl>
<p> tab-move-left</p>
<dl>
<dd>Move the current tab to the left.</dl>
<p> tab-move-right</p>
<dl>
<dd>Move the current tab to the right.</dl>
<p> tab-next</p>
<dl>
<dd>Next tab.</dl>
<p> tab-prev</p>
<dl>
<dd>Previous tab.</dl>
<p> terminal-resize</p>
<dl>
<dd>Open the terminal resize dialog.</dl>
<p> toggle-css</p>
<dl>
<dd>Toggle rendering of page using CSS.</dl>
<p> toggle-display-images</p>
<dl>
<dd>Toggle displaying of links to images.</dl>
<p> toggle-display-tables</p>
<dl>
<dd>Toggle rendering of tables.</dl>
<p> toggle-document-colors</p>
<dl>
<dd>Toggle usage of document specific colors.</dl>
<p> toggle-html-plain</p>
<dl>
<dd>Toggle rendering page as HTML / plain text.</dl>
<p> toggle-mouse</p>
<dl>
<dd>Toggle mouse handling.</dl>
<p> toggle-numbered-links</p>
<dl>
<dd>Toggle displaying of links numbers.</dl>
<p> toggle-plain-compress-empty-lines</p>
<dl>
<dd>Toggle plain renderer compression of empty lines.</dl>
<p> toggle-wrap-text</p>
<dl>
<dd>Toggle wrapping of text.</dl>
<p> view-image</p>
<dl>
<dd>View the current image.</dl>
<h3>Edit Actions</h3>
<p>auto-complete</p>
<dl>
<dd>Attempt to auto-complete the input.</dl>
<p> auto-complete-file</p>
<dl>
<dd>Attempt to auto-complete a local file.</dl>
<p> auto-complete-unambiguous</p>
<dl>
<dd>Attempt to unambiguously auto-complete the input.</dl>
<p> backspace</p>
<dl>
<dd>Delete character in front of the cursor.</dl>
<p> beginning-of-buffer</p>
<dl>
<dd>Go to the first line of the buffer.</dl>
<p> cancel</p>
<dl>
<dd>Cancel current state.</dl>
<p> copy-clipboard</p>
<dl>
<dd>Copy text to clipboard.</dl>
<p> cut-clipboard</p>
<dl>
<dd>Cut text to clipboard.</dl>
<p> delete</p>
<dl>
<dd>Delete character under cursor.</dl>
<p> down</p>
<dl>
<dd>Move cursor downwards.</dl>
<p> end</p>
<dl>
<dd>Go to the end of the page/line.</dl>
<p> end-of-buffer</p>
<dl>
<dd>Go to the last line of the buffer.</dl>
<p> enter</p>
<dl>
<dd>Follow the current link.</dl>
<p> home</p>
<dl>
<dd>Go to the start of the page/line.</dl>
<p> kill-to-bol</p>
<dl>
<dd>Delete to beginning of line.</dl>
<p> kill-to-eol</p>
<dl>
<dd>Delete to end of line.</dl>
<p> kill-word-back</p>
<dl>
<dd>Delete backwards to start of word.</dl>
<p> left</p>
<dl>
<dd>Move the cursor left.</dl>
<p> move-backward-word</p>
<dl>
<dd>Move cursor before current word.</dl>
<p> move-forward-word</p>
<dl>
<dd>Move cursor after current word.</dl>
<p> next-item</p>
<dl>
<dd>Move to the next item.</dl>
<p> open-external</p>
<dl>
<dd>Open in external editor.</dl>
<p> paste-clipboard</p>
<dl>
<dd>Paste text from the clipboard.</dl>
<p> previous-item</p>
<dl>
<dd>Move to the previous item.</dl>
<p> redraw</p>
<dl>
<dd>Redraw the terminal.</dl>
<p> right</p>
<dl>
<dd>Move the cursor right.</dl>
<p> search-toggle-regex</p>
<dl>
<dd>Toggle regex matching (type-ahead searching).</dl>
<p> up</p>
<dl>
<dd>Move cursor upwards.</dl>
<h3>Menu Actions</h3>
<p>cancel</p>
<dl>
<dd>Cancel current state.</dl>
<p> delete</p>
<dl>
<dd>Delete character under cursor.</dl>
<p> down</p>
<dl>
<dd>Move cursor downwards.</dl>
<p> end</p>
<dl>
<dd>Go to the end of the page/line.</dl>
<p> enter</p>
<dl>
<dd>Follow the current link.</dl>
<p> expand</p>
<dl>
<dd>Expand item.</dl>
<p> home</p>
<dl>
<dd>Go to the start of the page/line.</dl>
<p> left</p>
<dl>
<dd>Move the cursor left.</dl>
<p> mark-item</p>
<dl>
<dd>Mark item.</dl>
<p> next-item</p>
<dl>
<dd>Move to the next item.</dl>
<p> page-down</p>
<dl>
<dd>Move downwards by a page.</dl>
<p> page-up</p>
<dl>
<dd>Move upwards by a page.</dl>
<p> previous-item</p>
<dl>
<dd>Move to the previous item.</dl>
<p> redraw</p>
<dl>
<dd>Redraw the terminal.</dl>
<p> right</p>
<dl>
<dd>Move the cursor right.</dl>
<p> search</p>
<dl>
<dd>Search for a text pattern.</dl>
<p> select</p>
<dl>
<dd>Select current highlighted item.</dl>
<p> unexpand</p>
<dl>
<dd>Collapse item.</dl>
<p> up</p>
<dl>
<dd>Move cursor upwards.</dl>
<h2>Default Bindings</h2>
<p>The default bindings are shown below. Any bindings in ~/.elinks/elinks.conf will override these.</p>
<h3>Main Keys</h3>
<p><i>Space</i></p>
<dl>
<dd>Move downwards by a page (<i>move-page-down</i>)</dl>
<p> <i>&quot;#&quot;</i></p>
<dl>
<dd>Search link text by typing ahead (<i>search-typeahead</i>)</dl>
<p> <i>&quot;%&quot;</i></p>
<dl>
<dd>Toggle usage of document specific colors (<i>toggle-document-colors</i>)</dl>
<p> <i>&quot;*&quot;</i></p>
<dl>
<dd>Toggle displaying of links to images (<i>toggle-display-images</i>)</dl>
<p> <i>&quot;,&quot;</i></p>
<dl>
<dd>Open a Lua console (<i>lua-console</i>)</dl>
<p> <i>&quot;.&quot;</i></p>
<dl>
<dd>Toggle displaying of links numbers (<i>toggle-numbered-links</i>)</dl>
<p> <i>&quot;/&quot;</i></p>
<dl>
<dd>Search for a text pattern (<i>search</i>)</dl>
<p> <i>&quot;:&quot;</i></p>
<dl>
<dd>Enter ex-mode (command line) (<i>exmode</i>)</dl>
<p> <i>&quot;&lt;&quot;</i></p>
<dl>
<dd>Previous tab (<i>tab-prev</i>)</dl>
<p> <i>Alt-&quot;&lt;&quot;</i></p>
<dl>
<dd>Move the current tab to the left (<i>tab-move-left</i>)</dl>
<p> <i>&quot;=&quot;</i></p>
<dl>
<dd>Show information about the current page (<i>document-info</i>)</dl>
<p> <i>&quot;&gt;&quot;</i></p>
<dl>
<dd>Next tab (<i>tab-next</i>)</dl>
<p> <i>Alt-&quot;&gt;&quot;</i></p>
<dl>
<dd>Move the current tab to the right (<i>tab-move-right</i>)</dl>
<p> <i>&quot;?&quot;</i></p>
<dl>
<dd>Search backwards for a text pattern (<i>search-back</i>)</dl>
<p> <i>&quot;A&quot;</i></p>
<dl>
<dd>Add a new bookmark using current link (<i>add-bookmark-link</i>)</dl>
<p> <i>Ctrl-&quot;A&quot;</i></p>
<dl>
<dd>Move to the start of the document (<i>move-document-start</i>)</dl>
<p> <i>Ctrl-&quot;B&quot;</i></p>
<dl>
<dd>Move upwards by a page (<i>move-page-up</i>)</dl>
<p> <i>&quot;C&quot;</i></p>
<dl>
<dd>Open cache manager (<i>cache-manager</i>)</dl>
<p> <i>&quot;D&quot;</i></p>
<dl>
<dd>Open download manager (<i>download-manager</i>)</dl>
<p> <i>&quot;E&quot;</i></p>
<dl>
<dd>Open &quot;Go to URL&quot; dialog box containing the current link URL (<i>goto-url-current-link</i>)</dl>
<p> <i>Ctrl-&quot;E&quot;</i></p>
<dl>
<dd>Move to the end of the document (<i>move-document-end</i>)</dl>
<p> <i>&quot;F&quot;</i></p>
<dl>
<dd>Open form history manager (<i>formhist-manager</i>)</dl>
<p> <i>Ctrl-&quot;F&quot;</i></p>
<dl>
<dd>Move downwards by a page (<i>move-page-down</i>)</dl>
<p> <i>&quot;G&quot;</i></p>
<dl>
<dd>Open &quot;Go to URL&quot; dialog box containing the current URL (<i>goto-url-current</i>)</dl>
<p> <i>&quot;H&quot;</i></p>
<dl>
<dd>Go to the homepage (<i>goto-url-home</i>)</dl>
<p> <i>&quot;K&quot;</i></p>
<dl>
<dd>Open cookie manager (<i>cookie-manager</i>)</dl>
<p> <i>Ctrl-&quot;K&quot;</i></p>
<dl>
<dd>Reload cookies file (<i>cookies-load</i>)</dl>
<p> <i>&quot;L&quot;</i></p>
<dl>
<dd>Open the link context menu (<i>link-menu</i>)</dl>
<p> <i>Ctrl-&quot;L&quot;</i></p>
<dl>
<dd>Redraw the terminal (<i>redraw</i>)</dl>
<p> <i>&quot;N&quot;</i></p>
<dl>
<dd>Find the previous occurrence of the current search text (<i>find-next-back</i>)</dl>
<p> <i>Ctrl-&quot;N&quot;</i></p>
<dl>
<dd>Scroll down (<i>scroll-down</i>)</dl>
<p> <i>Ctrl-&quot;P&quot;</i></p>
<dl>
<dd>Scroll up (<i>scroll-up</i>)</dl>
<p> <i>&quot;Q&quot;</i></p>
<dl>
<dd>Quit without confirmation (<i>really-quit</i>)</dl>
<p> <i>Ctrl-&quot;R&quot;</i></p>
<dl>
<dd>Reload the current page (<i>reload</i>)</dl>
<p> <i>&quot;T&quot;</i></p>
<dl>
<dd>Open the current link in a new tab in the background (<i>open-link-in-new-tab-in-background</i>)</dl>
<p> <i>&quot;W&quot;</i></p>
<dl>
<dd>Toggle wrapping of text (<i>toggle-wrap-text</i>)</dl>
<p> <i>&quot;[&quot;</i></p>
<dl>
<dd>Scroll left (<i>scroll-left</i>)</dl>
<p> <i>&quot;&#8217;&quot;</i></p>
<dl>
<dd>Go at a specified mark (<i>mark-goto</i>)</dl>
<p> <i>&quot;\&quot;</i></p>
<dl>
<dd>Toggle rendering page as HTML / plain text (<i>toggle-html-plain</i>)</dl>
<p> <i>&quot;]&quot;</i></p>
<dl>
<dd>Scroll right (<i>scroll-right</i>)</dl>
<p> <i>&quot;a&quot;</i></p>
<dl>
<dd>Add a new bookmark (<i>add-bookmark</i>)</dl>
<p> <i>&quot;b&quot;</i></p>
<dl>
<dd>Move upwards by a page (<i>move-page-up</i>)</dl>
<p> <i>&quot;c&quot;</i></p>
<dl>
<dd>Close tab (<i>tab-close</i>)</dl>
<p> <i>&quot;d&quot;</i></p>
<dl>
<dd>Download the current link (<i>link-download</i>)</dl>
<p> <i>&quot;e&quot;</i></p>
<dl>
<dd>Open the tab menu (<i>tab-menu</i>)</dl>
<p> <i>&quot;f&quot;</i></p>
<dl>
<dd>Maximize the current frame (<i>frame-maximize</i>)</dl>
<p> <i>&quot;g&quot;</i></p>
<dl>
<dd>Open &quot;Go to URL&quot; dialog box (<i>goto-url</i>)</dl>
<p> <i>&quot;h&quot;</i></p>
<dl>
<dd>Open history manager (<i>history-manager</i>)</dl>
<p> <i>&quot;k&quot;</i></p>
<dl>
<dd>Open keybinding manager (<i>keybinding-manager</i>)</dl>
<p> <i>&quot;l&quot;</i></p>
<dl>
<dd>Jump to link (<i>jump-to-link</i>)</dl>
<p> <i>&quot;m&quot;</i></p>
<dl>
<dd>Set a mark (<i>mark-set</i>)</dl>
<p> <i>&quot;n&quot;</i></p>
<dl>
<dd>Find the next occurrence of the current search text (<i>find-next</i>)</dl>
<p> <i>&quot;o&quot;</i></p>
<dl>
<dd>Open options manager (<i>options-manager</i>)</dl>
<p> <i>&quot;q&quot;</i></p>
<dl>
<dd>Open a quit confirmation dialog box (<i>quit</i>)</dl>
<p> <i>&quot;r&quot;</i></p>
<dl>
<dd>Attempt to resume download of the current link (<i>link-download-resume</i>)</dl>
<p> <i>&quot;s&quot;</i></p>
<dl>
<dd>Open bookmark manager (<i>bookmark-manager</i>)</dl>
<p> <i>&quot;t&quot;</i></p>
<dl>
<dd>Open a new tab (<i>open-new-tab</i>)</dl>
<p> <i>&quot;u&quot;</i></p>
<dl>
<dd>Go forward in history (<i>history-move-forward</i>)</dl>
<p> <i>&quot;v&quot;</i></p>
<dl>
<dd>View the current image (<i>view-image</i>)</dl>
<p> <i>&quot;x&quot;</i></p>
<dl>
<dd>Follow the current link, forcing reload of the target (<i>link-follow-reload</i>)</dl>
<p> <i>&quot;z&quot;</i></p>
<dl>
<dd>Abort connection (<i>abort-connection</i>)</dl>
<p> <i>&quot;{&quot;</i></p>
<dl>
<dd>Scroll left (<i>scroll-left</i>)</dl>
<p> <i>&quot;|&quot;</i></p>
<dl>
<dd>Show information about the current page protocol headers (<i>header-info</i>)</dl>
<p> <i>&quot;}&quot;</i></p>
<dl>
<dd>Scroll right (<i>scroll-right</i>)</dl>
<p> <i>Backspace</i></p>
<dl>
<dd>Backspace the last entered digit of the current prefix (<i>backspace-prefix</i>)</dl>
<p> <i>Delete</i></p>
<dl>
<dd>Scroll down (<i>scroll-down</i>)</dl>
<p> <i>Down</i></p>
<dl>
<dd>Move to the next link (<i>move-link-next</i>)</dl>
<p> <i>End</i></p>
<dl>
<dd>Move to the end of the document (<i>move-document-end</i>)</dl>
<p> <i>Enter</i></p>
<dl>
<dd>Follow the current link (<i>link-follow</i>)</dl>
<p> <i>Ctrl-Enter</i></p>
<dl>
<dd>Follow the current link, forcing reload of the target (<i>link-follow-reload</i>)</dl>
<p> <i>Escape</i></p>
<dl>
<dd>Activate the menu (<i>menu</i>)</dl>
<p> <i>F10</i></p>
<dl>
<dd>Open the File menu (<i>file-menu</i>)</dl>
<p> <i>F9</i></p>
<dl>
<dd>Activate the menu (<i>menu</i>)</dl>
<p> <i>Home</i></p>
<dl>
<dd>Move to the start of the document (<i>move-document-start</i>)</dl>
<p> <i>Insert</i></p>
<dl>
<dd>Scroll up (<i>scroll-up</i>)</dl>
<p> <i>Ctrl-Insert</i></p>
<dl>
<dd>Copy text to clipboard (<i>copy-clipboard</i>)</dl>
<p> <i>Left</i></p>
<dl>
<dd>Return to the previous document in history (<i>history-move-back</i>)</dl>
<p> <i>PageDown</i></p>
<dl>
<dd>Move downwards by a page (<i>move-page-down</i>)</dl>
<p> <i>PageUp</i></p>
<dl>
<dd>Move upwards by a page (<i>move-page-up</i>)</dl>
<p> <i>Right</i></p>
<dl>
<dd>Follow the current link (<i>link-follow</i>)</dl>
<p> <i>Ctrl-Right</i></p>
<dl>
<dd>Follow the current link, forcing reload of the target (<i>link-follow-reload</i>)</dl>
<p> <i>Tab</i></p>
<dl>
<dd>Move to the next frame (<i>frame-next</i>)</dl>
<p> <i>Alt-Tab</i></p>
<dl>
<dd>Move to the previous frame (<i>frame-prev</i>)</dl>
<p> <i>Shift-Tab</i></p>
<dl>
<dd>Move to the previous frame (<i>frame-prev</i>)</dl>
<p> <i>Up</i></p>
<dl>
<dd>Move to the previous link (<i>move-link-prev</i>)</dl>
<h3>Edit Keys</h3>
<p><i>Alt-&quot;&lt;&quot;</i></p>
<dl>
<dd>Go to the first line of the buffer (<i>beginning-of-buffer</i>)</dl>
<p> <i>Alt-&quot;&gt;&quot;</i></p>
<dl>
<dd>Go to the last line of the buffer (<i>end-of-buffer</i>)</dl>
<p> <i>Ctrl-&quot;A&quot;</i></p>
<dl>
<dd>Go to the start of the page/line (<i>home</i>)</dl>
<p> <i>Alt-&quot;b&quot;</i></p>
<dl>
<dd>Move cursor before current word (<i>move-backward-word</i>)</dl>
<p> <i>Ctrl-&quot;D&quot;</i></p>
<dl>
<dd>Delete character under cursor (<i>delete</i>)</dl>
<p> <i>Ctrl-&quot;E&quot;</i></p>
<dl>
<dd>Go to the end of the page/line (<i>end</i>)</dl>
<p> <i>Alt-&quot;f&quot;</i></p>
<dl>
<dd>Move cursor after current word (<i>move-forward-word</i>)</dl>
<p> <i>Ctrl-&quot;H&quot;</i></p>
<dl>
<dd>Delete character in front of the cursor (<i>backspace</i>)</dl>
<p> <i>Ctrl-&quot;K&quot;</i></p>
<dl>
<dd>Delete to end of line (<i>kill-to-eol</i>)</dl>
<p> <i>Ctrl-&quot;L&quot;</i></p>
<dl>
<dd>Redraw the terminal (<i>redraw</i>)</dl>
<p> <i>Alt-&quot;r&quot;</i></p>
<dl>
<dd>Toggle regex matching (type-ahead searching) (<i>search-toggle-regex</i>)</dl>
<p> <i>Ctrl-&quot;F&quot;</i></p>
<dl>
<dd>Attempt to auto-complete a local file (<i>auto-complete-file</i>)</dl>
<p> <i>Ctrl-&quot;R&quot;</i></p>
<dl>
<dd>Attempt to unambiguously auto-complete the input (<i>auto-complete-unambiguous</i>)</dl>
<p> <i>Ctrl-&quot;T&quot;</i></p>
<dl>
<dd>Open in external editor (<i>open-external</i>)</dl>
<p> <i>Ctrl-&quot;U&quot;</i></p>
<dl>
<dd>Delete to beginning of line (<i>kill-to-bol</i>)</dl>
<p> <i>Ctrl-&quot;V&quot;</i></p>
<dl>
<dd>Paste text from the clipboard (<i>paste-clipboard</i>)</dl>
<p> <i>Ctrl-&quot;W&quot;</i></p>
<dl>
<dd>Attempt to auto-complete the input (<i>auto-complete</i>)</dl>
<p> <i>Ctrl-&quot;X&quot;</i></p>
<dl>
<dd>Cut text to clipboard (<i>cut-clipboard</i>)</dl>
<p> <i>Alt-Backspace</i></p>
<dl>
<dd>Delete backwards to start of word (<i>kill-word-back</i>)</dl>
<p> <i>Backspace</i></p>
<dl>
<dd>Delete character in front of the cursor (<i>backspace</i>)</dl>
<p> <i>Delete</i></p>
<dl>
<dd>Delete character under cursor (<i>delete</i>)</dl>
<p> <i>Down</i></p>
<dl>
<dd>Move cursor downwards (<i>down</i>)</dl>
<p> <i>End</i></p>
<dl>
<dd>Go to the end of the page/line (<i>end</i>)</dl>
<p> <i>Enter</i></p>
<dl>
<dd>Follow the current link (<i>enter</i>)</dl>
<p> <i>Escape</i></p>
<dl>
<dd>Cancel current state (<i>cancel</i>)</dl>
<p> <i>F4</i></p>
<dl>
<dd>Open in external editor (<i>open-external</i>)</dl>
<p> <i>Home</i></p>
<dl>
<dd>Go to the start of the page/line (<i>home</i>)</dl>
<p> <i>Ctrl-Insert</i></p>
<dl>
<dd>Copy text to clipboard (<i>copy-clipboard</i>)</dl>
<p> <i>Left</i></p>
<dl>
<dd>Move the cursor left (<i>left</i>)</dl>
<p> <i>Right</i></p>
<dl>
<dd>Move the cursor right (<i>right</i>)</dl>
<p> <i>Tab</i></p>
<dl>
<dd>Move to the next item (<i>next-item</i>)</dl>
<p> <i>Alt-Tab</i></p>
<dl>
<dd>Move to the previous item (<i>previous-item</i>)</dl>
<p> <i>Shift-Tab</i></p>
<dl>
<dd>Move to the previous item (<i>previous-item</i>)</dl>
<p> <i>Up</i></p>
<dl>
<dd>Move cursor upwards (<i>up</i>)</dl>
<h3>Menu Keys</h3>
<p><i>Space</i></p>
<dl>
<dd>Select current highlighted item (<i>select</i>)</dl>
<p> <i>&quot;*&quot;</i></p>
<dl>
<dd>Mark item (<i>mark-item</i>)</dl>
<p> <i>&quot;+&quot;</i></p>
<dl>
<dd>Expand item (<i>expand</i>)</dl>
<p> <i>&quot;-&quot;</i></p>
<dl>
<dd>Collapse item (<i>unexpand</i>)</dl>
<p> <i>&quot;/&quot;</i></p>
<dl>
<dd>Search for a text pattern (<i>search</i>)</dl>
<p> <i>&quot;=&quot;</i></p>
<dl>
<dd>Expand item (<i>expand</i>)</dl>
<p> <i>Ctrl-&quot;A&quot;</i></p>
<dl>
<dd>Go to the start of the page/line (<i>home</i>)</dl>
<p> <i>Ctrl-&quot;B&quot;</i></p>
<dl>
<dd>Move upwards by a page (<i>page-up</i>)</dl>
<p> <i>Ctrl-&quot;E&quot;</i></p>
<dl>
<dd>Go to the end of the page/line (<i>end</i>)</dl>
<p> <i>Ctrl-&quot;F&quot;</i></p>
<dl>
<dd>Move downwards by a page (<i>page-down</i>)</dl>
<p> <i>Ctrl-&quot;L&quot;</i></p>
<dl>
<dd>Redraw the terminal (<i>redraw</i>)</dl>
<p> <i>Ctrl-&quot;N&quot;</i></p>
<dl>
<dd>Move cursor downwards (<i>down</i>)</dl>
<p> <i>Ctrl-&quot;P&quot;</i></p>
<dl>
<dd>Move cursor upwards (<i>up</i>)</dl>
<p> <i>Alt-&quot;V&quot;</i></p>
<dl>
<dd>Move upwards by a page (<i>page-up</i>)</dl>
<p> <i>Ctrl-&quot;V&quot;</i></p>
<dl>
<dd>Move downwards by a page (<i>page-down</i>)</dl>
<p> <i>&quot;[&quot;</i></p>
<dl>
<dd>Expand item (<i>expand</i>)</dl>
<p> <i>&quot;]&quot;</i></p>
<dl>
<dd>Collapse item (<i>unexpand</i>)</dl>
<p> <i>&quot;_&quot;</i></p>
<dl>
<dd>Collapse item (<i>unexpand</i>)</dl>
<p> <i>Delete</i></p>
<dl>
<dd>Delete character under cursor (<i>delete</i>)</dl>
<p> <i>Down</i></p>
<dl>
<dd>Move cursor downwards (<i>down</i>)</dl>
<p> <i>End</i></p>
<dl>
<dd>Go to the end of the page/line (<i>end</i>)</dl>
<p> <i>Enter</i></p>
<dl>
<dd>Follow the current link (<i>enter</i>)</dl>
<p> <i>Escape</i></p>
<dl>
<dd>Cancel current state (<i>cancel</i>)</dl>
<p> <i>Home</i></p>
<dl>
<dd>Go to the start of the page/line (<i>home</i>)</dl>
<p> <i>Insert</i></p>
<dl>
<dd>Mark item (<i>mark-item</i>)</dl>
<p> <i>Left</i></p>
<dl>
<dd>Move the cursor left (<i>left</i>)</dl>
<p> <i>PageDown</i></p>
<dl>
<dd>Move downwards by a page (<i>page-down</i>)</dl>
<p> <i>PageUp</i></p>
<dl>
<dd>Move upwards by a page (<i>page-up</i>)</dl>
<p> <i>Right</i></p>
<dl>
<dd>Move the cursor right (<i>right</i>)</dl>
<p> <i>Tab</i></p>
<dl>
<dd>Move to the next item (<i>next-item</i>)</dl>
<p> <i>Alt-Tab</i></p>
<dl>
<dd>Move to the previous item (<i>previous-item</i>)</dl>
<p> <i>Shift-Tab</i></p>
<dl>
<dd>Move to the previous item (<i>previous-item</i>)</dl>
<p> <i>Up</i></p>
<dl>
<dd>Move cursor upwards (<i>up</i>)</dl>
<h2>Author</h2>
<p>This manual page was finally written by Peter Wang (one and a half years after writing the binding code), using excerpts by David Mediavilla. You can thank Petr Baudis for the subtle requests for documentation. Updated by Zas. Moved to asciidoc format and cleaned up by Jonas Fonseca.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-elinks/">elinks</a></code>(1), <code><a href="/docs/linux/man/5-elinks-conf/">elinks.conf</a></code>(5) </p>
