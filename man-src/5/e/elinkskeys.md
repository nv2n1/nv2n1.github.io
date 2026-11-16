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
</dd></dl>
<p> where: &lt;keymap&gt;</p>
<dl>
<dd>is <i>main</i>, <i>edit</i>, or <i>menu</i>. The main keymap is used for general browsing. The edit keymap is used for editing text fields. The menu keymap is used for navigating menus.</dd></dl>
<p> &lt;keystroke&gt;</p>
<dl>
<dd>is a case sensitive key, which you can prefix with <i>Ctrl-</i>, <i>Alt-</i>, or both. <i>Ctrl-</i> must be followed by an uppercase key. See below for a list of valid keys.</dd></dl>
<p> &lt;action&gt;</p>
<dl>
<dd>is what the key should do. The actions available are dependent on the keymap, and are listed separately below.</dd></dl>
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
</dd></dl>
<h2>Keys</h2>
<p>Valid keys are: alphanumeric characters, punctuation, <i>Enter</i>, <i>Backspace</i>, <i>Tab</i>, <i>Escape</i>, <i>Left</i>, <i>Right</i>, <i>Up</i>, <i>Down</i>, <i>Insert</i>, <i>Delete</i>, <i>Home</i>, <i>End</i>, <i>PageUp</i>, <i>PageDown</i>, <i>F1</i> to <i>F12</i>. </p>
<p> Some keys will need to be quoted or escaped. For example, space can be written as &quot; &quot; (quote space quote), and the quote itself as \&quot; (backslash quote). Backslash can be written as \ (double backslash).</p>
<h2>Keymap Actions</h2>
<h3>Main Actions</h3>
<p>abort-connection</p>
<dl>
<dd>Abort connection.</dd></dl>
<p> add-bookmark</p>
<dl>
<dd>Add a new bookmark.</dd></dl>
<p> add-bookmark-link</p>
<dl>
<dd>Add a new bookmark using current link.</dd></dl>
<p> add-bookmark-tabs</p>
<dl>
<dd>Bookmark all open tabs.</dd></dl>
<p> auth-manager</p>
<dl>
<dd>Open authentication manager.</dd></dl>
<p> backspace-prefix</p>
<dl>
<dd>Backspace the last entered digit of the current prefix.</dd></dl>
<p> bookmark-manager</p>
<dl>
<dd>Open bookmark manager.</dd></dl>
<p> cache-manager</p>
<dl>
<dd>Open cache manager.</dd></dl>
<p> cache-minimize</p>
<dl>
<dd>Free unused cache entries.</dd></dl>
<p> cookie-manager</p>
<dl>
<dd>Open cookie manager.</dd></dl>
<p> cookies-load</p>
<dl>
<dd>Reload cookies file.</dd></dl>
<p> copy-clipboard</p>
<dl>
<dd>Copy text to clipboard.</dd></dl>
<p> document-info</p>
<dl>
<dd>Show information about the current page.</dd></dl>
<p> download-manager</p>
<dl>
<dd>Open download manager.</dd></dl>
<p> exmode</p>
<dl>
<dd>Enter ex-mode (command line).</dd></dl>
<p> file-menu</p>
<dl>
<dd>Open the File menu.</dd></dl>
<p> find-next</p>
<dl>
<dd>Find the next occurrence of the current search text.</dd></dl>
<p> find-next-back</p>
<dl>
<dd>Find the previous occurrence of the current search text.</dd></dl>
<p> forget-credentials</p>
<dl>
<dd>Forget authentication credentials.</dd></dl>
<p> formhist-manager</p>
<dl>
<dd>Open form history manager.</dd></dl>
<p> frame-external-command</p>
<dl>
<dd>Pass URI of current frame to external command.</dd></dl>
<p> frame-maximize</p>
<dl>
<dd>Maximize the current frame.</dd></dl>
<p> frame-next</p>
<dl>
<dd>Move to the next frame.</dd></dl>
<p> frame-prev</p>
<dl>
<dd>Move to the previous frame.</dd></dl>
<p> goto-url</p>
<dl>
<dd>Open &quot;Go to URL&quot; dialog box.</dd></dl>
<p> goto-url-current</p>
<dl>
<dd>Open &quot;Go to URL&quot; dialog box containing the current URL.</dd></dl>
<p> goto-url-current-link</p>
<dl>
<dd>Open &quot;Go to URL&quot; dialog box containing the current link URL.</dd></dl>
<p> goto-url-home</p>
<dl>
<dd>Go to the homepage.</dd></dl>
<p> header-info</p>
<dl>
<dd>Show information about the current page protocol headers.</dd></dl>
<p> history-manager</p>
<dl>
<dd>Open history manager.</dd></dl>
<p> history-move-back</p>
<dl>
<dd>Return to the previous document in history.</dd></dl>
<p> history-move-forward</p>
<dl>
<dd>Go forward in history.</dd></dl>
<p> jump-to-link</p>
<dl>
<dd>Jump to link.</dd></dl>
<p> keybinding-manager</p>
<dl>
<dd>Open keybinding manager.</dd></dl>
<p> kill-backgrounded-connections</p>
<dl>
<dd>Kill all backgrounded connections.</dd></dl>
<p> link-download</p>
<dl>
<dd>Download the current link.</dd></dl>
<p> link-download-image</p>
<dl>
<dd>Download the current image.</dd></dl>
<p> link-download-resume</p>
<dl>
<dd>Attempt to resume download of the current link.</dd></dl>
<p> link-external-command</p>
<dl>
<dd>Pass URI of current link to external command.</dd></dl>
<p> link-follow</p>
<dl>
<dd>Follow the current link.</dd></dl>
<p> link-follow-reload</p>
<dl>
<dd>Follow the current link, forcing reload of the target.</dd></dl>
<p> link-info</p>
<dl>
<dd>Show information about current link.</dd></dl>
<p> link-menu</p>
<dl>
<dd>Open the link context menu.</dd></dl>
<p> link-form-menu</p>
<dl>
<dd>Open the form fields menu.</dd></dl>
<p> lua-console</p>
<dl>
<dd>Open a Lua console.</dd></dl>
<p> mark-goto</p>
<dl>
<dd>Go at a specified mark.</dd></dl>
<p> mark-set</p>
<dl>
<dd>Set a mark.</dd></dl>
<p> menu</p>
<dl>
<dd>Activate the menu.</dd></dl>
<p> move-current-top</p>
<dl>
<dd>Move downwards to put the current line at the top of the screen.</dd></dl>
<p> move-cursor-down</p>
<dl>
<dd>Move cursor down.</dd></dl>
<p> move-cursor-left</p>
<dl>
<dd>Move cursor left.</dd></dl>
<p> move-cursor-line-start</p>
<dl>
<dd>Move cursor to the start of the line.</dd></dl>
<p> move-cursor-right</p>
<dl>
<dd>Move cursor right.</dd></dl>
<p> move-cursor-up</p>
<dl>
<dd>Move cursor up.</dd></dl>
<p> move-document-end</p>
<dl>
<dd>Move to the end of the document.</dd></dl>
<p> move-document-start</p>
<dl>
<dd>Move to the start of the document.</dd></dl>
<p> move-half-page-down</p>
<dl>
<dd>Move downwards by half a page.</dd></dl>
<p> move-half-page-up</p>
<dl>
<dd>Move upwards by half a page.</dd></dl>
<p> move-link-down</p>
<dl>
<dd>Move one link down.</dd></dl>
<p> move-link-down-line</p>
<dl>
<dd>Move to the next line with a link.</dd></dl>
<p> move-link-left</p>
<dl>
<dd>Move one link left.</dd></dl>
<p> move-link-left-line</p>
<dl>
<dd>Move one link left or to the previous link.</dd></dl>
<p> move-link-next</p>
<dl>
<dd>Move to the next link.</dd></dl>
<p> move-link-prev</p>
<dl>
<dd>Move to the previous link.</dd></dl>
<p> move-link-right</p>
<dl>
<dd>Move one link right.</dd></dl>
<p> move-link-right-line</p>
<dl>
<dd>Move one link right or to the next link.</dd></dl>
<p> move-link-up</p>
<dl>
<dd>Move one link up.</dd></dl>
<p> move-link-up-line</p>
<dl>
<dd>Move to the previous line with a link.</dd></dl>
<p> move-page-down</p>
<dl>
<dd>Move downwards by a page.</dd></dl>
<p> move-page-up</p>
<dl>
<dd>Move upwards by a page.</dd></dl>
<p> open-link-in-new-tab</p>
<dl>
<dd>Open the current link in a new tab.</dd></dl>
<p> open-link-in-new-tab-in-background</p>
<dl>
<dd>Open the current link in a new tab in the background.</dd></dl>
<p> open-link-in-new-window</p>
<dl>
<dd>Open the current link in a new window.</dd></dl>
<p> open-new-tab</p>
<dl>
<dd>Open a new tab.</dd></dl>
<p> open-new-tab-in-background</p>
<dl>
<dd>Open a new tab in the background.</dd></dl>
<p> open-new-window</p>
<dl>
<dd>Open a new window.</dd></dl>
<p> open-os-shell</p>
<dl>
<dd>Open an OS shell.</dd></dl>
<p> options-manager</p>
<dl>
<dd>Open options manager.</dd></dl>
<p> quit</p>
<dl>
<dd>Open a quit confirmation dialog box.</dd></dl>
<p> really-quit</p>
<dl>
<dd>Quit without confirmation.</dd></dl>
<p> redraw</p>
<dl>
<dd>Redraw the terminal.</dd></dl>
<p> reload</p>
<dl>
<dd>Reload the current page.</dd></dl>
<p> rerender</p>
<dl>
<dd>Re-render the current page.</dd></dl>
<p> reset-form</p>
<dl>
<dd>Reset form items to their initial values.</dd></dl>
<p> resource-info</p>
<dl>
<dd>Show information about the currently used resources.</dd></dl>
<p> save-as</p>
<dl>
<dd>Save the current document in source form.</dd></dl>
<p> save-formatted</p>
<dl>
<dd>Save the current document in formatted form.</dd></dl>
<p> save-options</p>
<dl>
<dd>Save options.</dd></dl>
<p> save-url-as</p>
<dl>
<dd>Save URL as.</dd></dl>
<p> scroll-down</p>
<dl>
<dd>Scroll down.</dd></dl>
<p> scroll-left</p>
<dl>
<dd>Scroll left.</dd></dl>
<p> scroll-right</p>
<dl>
<dd>Scroll right.</dd></dl>
<p> scroll-up</p>
<dl>
<dd>Scroll up.</dd></dl>
<p> search</p>
<dl>
<dd>Search for a text pattern.</dd></dl>
<p> search-back</p>
<dl>
<dd>Search backwards for a text pattern.</dd></dl>
<p> search-typeahead</p>
<dl>
<dd>Search link text by typing ahead.</dd></dl>
<p> search-typeahead-link</p>
<dl>
<dd>Search link text by typing ahead.</dd></dl>
<p> search-typeahead-text</p>
<dl>
<dd>Search document text by typing ahead.</dd></dl>
<p> search-typeahead-text-back</p>
<dl>
<dd>Search document text backwards by typing ahead.</dd></dl>
<p> show-term-options</p>
<dl>
<dd>Show terminal options dialog.</dd></dl>
<p> submit-form</p>
<dl>
<dd>Submit form.</dd></dl>
<p> submit-form-reload</p>
<dl>
<dd>Submit form and reload.</dd></dl>
<p> tab-close</p>
<dl>
<dd>Close tab.</dd></dl>
<p> tab-close-all-but-current</p>
<dl>
<dd>Close all tabs but the current one.</dd></dl>
<p> tab-external-command</p>
<dl>
<dd>Pass URI of current tab to external command.</dd></dl>
<p> tab-menu</p>
<dl>
<dd>Open the tab menu.</dd></dl>
<p> tab-move-left</p>
<dl>
<dd>Move the current tab to the left.</dd></dl>
<p> tab-move-right</p>
<dl>
<dd>Move the current tab to the right.</dd></dl>
<p> tab-next</p>
<dl>
<dd>Next tab.</dd></dl>
<p> tab-prev</p>
<dl>
<dd>Previous tab.</dd></dl>
<p> terminal-resize</p>
<dl>
<dd>Open the terminal resize dialog.</dd></dl>
<p> toggle-css</p>
<dl>
<dd>Toggle rendering of page using CSS.</dd></dl>
<p> toggle-display-images</p>
<dl>
<dd>Toggle displaying of links to images.</dd></dl>
<p> toggle-display-tables</p>
<dl>
<dd>Toggle rendering of tables.</dd></dl>
<p> toggle-document-colors</p>
<dl>
<dd>Toggle usage of document specific colors.</dd></dl>
<p> toggle-html-plain</p>
<dl>
<dd>Toggle rendering page as HTML / plain text.</dd></dl>
<p> toggle-mouse</p>
<dl>
<dd>Toggle mouse handling.</dd></dl>
<p> toggle-numbered-links</p>
<dl>
<dd>Toggle displaying of links numbers.</dd></dl>
<p> toggle-plain-compress-empty-lines</p>
<dl>
<dd>Toggle plain renderer compression of empty lines.</dd></dl>
<p> toggle-wrap-text</p>
<dl>
<dd>Toggle wrapping of text.</dd></dl>
<p> view-image</p>
<dl>
<dd>View the current image.</dd></dl>
<h3>Edit Actions</h3>
<p>auto-complete</p>
<dl>
<dd>Attempt to auto-complete the input.</dd></dl>
<p> auto-complete-file</p>
<dl>
<dd>Attempt to auto-complete a local file.</dd></dl>
<p> auto-complete-unambiguous</p>
<dl>
<dd>Attempt to unambiguously auto-complete the input.</dd></dl>
<p> backspace</p>
<dl>
<dd>Delete character in front of the cursor.</dd></dl>
<p> beginning-of-buffer</p>
<dl>
<dd>Go to the first line of the buffer.</dd></dl>
<p> cancel</p>
<dl>
<dd>Cancel current state.</dd></dl>
<p> copy-clipboard</p>
<dl>
<dd>Copy text to clipboard.</dd></dl>
<p> cut-clipboard</p>
<dl>
<dd>Cut text to clipboard.</dd></dl>
<p> delete</p>
<dl>
<dd>Delete character under cursor.</dd></dl>
<p> down</p>
<dl>
<dd>Move cursor downwards.</dd></dl>
<p> end</p>
<dl>
<dd>Go to the end of the page/line.</dd></dl>
<p> end-of-buffer</p>
<dl>
<dd>Go to the last line of the buffer.</dd></dl>
<p> enter</p>
<dl>
<dd>Follow the current link.</dd></dl>
<p> home</p>
<dl>
<dd>Go to the start of the page/line.</dd></dl>
<p> kill-to-bol</p>
<dl>
<dd>Delete to beginning of line.</dd></dl>
<p> kill-to-eol</p>
<dl>
<dd>Delete to end of line.</dd></dl>
<p> kill-word-back</p>
<dl>
<dd>Delete backwards to start of word.</dd></dl>
<p> left</p>
<dl>
<dd>Move the cursor left.</dd></dl>
<p> move-backward-word</p>
<dl>
<dd>Move cursor before current word.</dd></dl>
<p> move-forward-word</p>
<dl>
<dd>Move cursor after current word.</dd></dl>
<p> next-item</p>
<dl>
<dd>Move to the next item.</dd></dl>
<p> open-external</p>
<dl>
<dd>Open in external editor.</dd></dl>
<p> paste-clipboard</p>
<dl>
<dd>Paste text from the clipboard.</dd></dl>
<p> previous-item</p>
<dl>
<dd>Move to the previous item.</dd></dl>
<p> redraw</p>
<dl>
<dd>Redraw the terminal.</dd></dl>
<p> right</p>
<dl>
<dd>Move the cursor right.</dd></dl>
<p> search-toggle-regex</p>
<dl>
<dd>Toggle regex matching (type-ahead searching).</dd></dl>
<p> up</p>
<dl>
<dd>Move cursor upwards.</dd></dl>
<h3>Menu Actions</h3>
<p>cancel</p>
<dl>
<dd>Cancel current state.</dd></dl>
<p> delete</p>
<dl>
<dd>Delete character under cursor.</dd></dl>
<p> down</p>
<dl>
<dd>Move cursor downwards.</dd></dl>
<p> end</p>
<dl>
<dd>Go to the end of the page/line.</dd></dl>
<p> enter</p>
<dl>
<dd>Follow the current link.</dd></dl>
<p> expand</p>
<dl>
<dd>Expand item.</dd></dl>
<p> home</p>
<dl>
<dd>Go to the start of the page/line.</dd></dl>
<p> left</p>
<dl>
<dd>Move the cursor left.</dd></dl>
<p> mark-item</p>
<dl>
<dd>Mark item.</dd></dl>
<p> next-item</p>
<dl>
<dd>Move to the next item.</dd></dl>
<p> page-down</p>
<dl>
<dd>Move downwards by a page.</dd></dl>
<p> page-up</p>
<dl>
<dd>Move upwards by a page.</dd></dl>
<p> previous-item</p>
<dl>
<dd>Move to the previous item.</dd></dl>
<p> redraw</p>
<dl>
<dd>Redraw the terminal.</dd></dl>
<p> right</p>
<dl>
<dd>Move the cursor right.</dd></dl>
<p> search</p>
<dl>
<dd>Search for a text pattern.</dd></dl>
<p> select</p>
<dl>
<dd>Select current highlighted item.</dd></dl>
<p> unexpand</p>
<dl>
<dd>Collapse item.</dd></dl>
<p> up</p>
<dl>
<dd>Move cursor upwards.</dd></dl>
<h2>Default Bindings</h2>
<p>The default bindings are shown below. Any bindings in ~/.elinks/elinks.conf will override these.</p>
<h3>Main Keys</h3>
<p><i>Space</i></p>
<dl>
<dd>Move downwards by a page (<i>move-page-down</i>)</dd></dl>
<p> <i>&quot;#&quot;</i></p>
<dl>
<dd>Search link text by typing ahead (<i>search-typeahead</i>)</dd></dl>
<p> <i>&quot;%&quot;</i></p>
<dl>
<dd>Toggle usage of document specific colors (<i>toggle-document-colors</i>)</dd></dl>
<p> <i>&quot;*&quot;</i></p>
<dl>
<dd>Toggle displaying of links to images (<i>toggle-display-images</i>)</dd></dl>
<p> <i>&quot;,&quot;</i></p>
<dl>
<dd>Open a Lua console (<i>lua-console</i>)</dd></dl>
<p> <i>&quot;.&quot;</i></p>
<dl>
<dd>Toggle displaying of links numbers (<i>toggle-numbered-links</i>)</dd></dl>
<p> <i>&quot;/&quot;</i></p>
<dl>
<dd>Search for a text pattern (<i>search</i>)</dd></dl>
<p> <i>&quot;:&quot;</i></p>
<dl>
<dd>Enter ex-mode (command line) (<i>exmode</i>)</dd></dl>
<p> <i>&quot;&lt;&quot;</i></p>
<dl>
<dd>Previous tab (<i>tab-prev</i>)</dd></dl>
<p> <i>Alt-&quot;&lt;&quot;</i></p>
<dl>
<dd>Move the current tab to the left (<i>tab-move-left</i>)</dd></dl>
<p> <i>&quot;=&quot;</i></p>
<dl>
<dd>Show information about the current page (<i>document-info</i>)</dd></dl>
<p> <i>&quot;&gt;&quot;</i></p>
<dl>
<dd>Next tab (<i>tab-next</i>)</dd></dl>
<p> <i>Alt-&quot;&gt;&quot;</i></p>
<dl>
<dd>Move the current tab to the right (<i>tab-move-right</i>)</dd></dl>
<p> <i>&quot;?&quot;</i></p>
<dl>
<dd>Search backwards for a text pattern (<i>search-back</i>)</dd></dl>
<p> <i>&quot;A&quot;</i></p>
<dl>
<dd>Add a new bookmark using current link (<i>add-bookmark-link</i>)</dd></dl>
<p> <i>Ctrl-&quot;A&quot;</i></p>
<dl>
<dd>Move to the start of the document (<i>move-document-start</i>)</dd></dl>
<p> <i>Ctrl-&quot;B&quot;</i></p>
<dl>
<dd>Move upwards by a page (<i>move-page-up</i>)</dd></dl>
<p> <i>&quot;C&quot;</i></p>
<dl>
<dd>Open cache manager (<i>cache-manager</i>)</dd></dl>
<p> <i>&quot;D&quot;</i></p>
<dl>
<dd>Open download manager (<i>download-manager</i>)</dd></dl>
<p> <i>&quot;E&quot;</i></p>
<dl>
<dd>Open &quot;Go to URL&quot; dialog box containing the current link URL (<i>goto-url-current-link</i>)</dd></dl>
<p> <i>Ctrl-&quot;E&quot;</i></p>
<dl>
<dd>Move to the end of the document (<i>move-document-end</i>)</dd></dl>
<p> <i>&quot;F&quot;</i></p>
<dl>
<dd>Open form history manager (<i>formhist-manager</i>)</dd></dl>
<p> <i>Ctrl-&quot;F&quot;</i></p>
<dl>
<dd>Move downwards by a page (<i>move-page-down</i>)</dd></dl>
<p> <i>&quot;G&quot;</i></p>
<dl>
<dd>Open &quot;Go to URL&quot; dialog box containing the current URL (<i>goto-url-current</i>)</dd></dl>
<p> <i>&quot;H&quot;</i></p>
<dl>
<dd>Go to the homepage (<i>goto-url-home</i>)</dd></dl>
<p> <i>&quot;K&quot;</i></p>
<dl>
<dd>Open cookie manager (<i>cookie-manager</i>)</dd></dl>
<p> <i>Ctrl-&quot;K&quot;</i></p>
<dl>
<dd>Reload cookies file (<i>cookies-load</i>)</dd></dl>
<p> <i>&quot;L&quot;</i></p>
<dl>
<dd>Open the link context menu (<i>link-menu</i>)</dd></dl>
<p> <i>Ctrl-&quot;L&quot;</i></p>
<dl>
<dd>Redraw the terminal (<i>redraw</i>)</dd></dl>
<p> <i>&quot;N&quot;</i></p>
<dl>
<dd>Find the previous occurrence of the current search text (<i>find-next-back</i>)</dd></dl>
<p> <i>Ctrl-&quot;N&quot;</i></p>
<dl>
<dd>Scroll down (<i>scroll-down</i>)</dd></dl>
<p> <i>Ctrl-&quot;P&quot;</i></p>
<dl>
<dd>Scroll up (<i>scroll-up</i>)</dd></dl>
<p> <i>&quot;Q&quot;</i></p>
<dl>
<dd>Quit without confirmation (<i>really-quit</i>)</dd></dl>
<p> <i>Ctrl-&quot;R&quot;</i></p>
<dl>
<dd>Reload the current page (<i>reload</i>)</dd></dl>
<p> <i>&quot;T&quot;</i></p>
<dl>
<dd>Open the current link in a new tab in the background (<i>open-link-in-new-tab-in-background</i>)</dd></dl>
<p> <i>&quot;W&quot;</i></p>
<dl>
<dd>Toggle wrapping of text (<i>toggle-wrap-text</i>)</dd></dl>
<p> <i>&quot;[&quot;</i></p>
<dl>
<dd>Scroll left (<i>scroll-left</i>)</dd></dl>
<p> <i>&quot;&#8217;&quot;</i></p>
<dl>
<dd>Go at a specified mark (<i>mark-goto</i>)</dd></dl>
<p> <i>&quot;\&quot;</i></p>
<dl>
<dd>Toggle rendering page as HTML / plain text (<i>toggle-html-plain</i>)</dd></dl>
<p> <i>&quot;]&quot;</i></p>
<dl>
<dd>Scroll right (<i>scroll-right</i>)</dd></dl>
<p> <i>&quot;a&quot;</i></p>
<dl>
<dd>Add a new bookmark (<i>add-bookmark</i>)</dd></dl>
<p> <i>&quot;b&quot;</i></p>
<dl>
<dd>Move upwards by a page (<i>move-page-up</i>)</dd></dl>
<p> <i>&quot;c&quot;</i></p>
<dl>
<dd>Close tab (<i>tab-close</i>)</dd></dl>
<p> <i>&quot;d&quot;</i></p>
<dl>
<dd>Download the current link (<i>link-download</i>)</dd></dl>
<p> <i>&quot;e&quot;</i></p>
<dl>
<dd>Open the tab menu (<i>tab-menu</i>)</dd></dl>
<p> <i>&quot;f&quot;</i></p>
<dl>
<dd>Maximize the current frame (<i>frame-maximize</i>)</dd></dl>
<p> <i>&quot;g&quot;</i></p>
<dl>
<dd>Open &quot;Go to URL&quot; dialog box (<i>goto-url</i>)</dd></dl>
<p> <i>&quot;h&quot;</i></p>
<dl>
<dd>Open history manager (<i>history-manager</i>)</dd></dl>
<p> <i>&quot;k&quot;</i></p>
<dl>
<dd>Open keybinding manager (<i>keybinding-manager</i>)</dd></dl>
<p> <i>&quot;l&quot;</i></p>
<dl>
<dd>Jump to link (<i>jump-to-link</i>)</dd></dl>
<p> <i>&quot;m&quot;</i></p>
<dl>
<dd>Set a mark (<i>mark-set</i>)</dd></dl>
<p> <i>&quot;n&quot;</i></p>
<dl>
<dd>Find the next occurrence of the current search text (<i>find-next</i>)</dd></dl>
<p> <i>&quot;o&quot;</i></p>
<dl>
<dd>Open options manager (<i>options-manager</i>)</dd></dl>
<p> <i>&quot;q&quot;</i></p>
<dl>
<dd>Open a quit confirmation dialog box (<i>quit</i>)</dd></dl>
<p> <i>&quot;r&quot;</i></p>
<dl>
<dd>Attempt to resume download of the current link (<i>link-download-resume</i>)</dd></dl>
<p> <i>&quot;s&quot;</i></p>
<dl>
<dd>Open bookmark manager (<i>bookmark-manager</i>)</dd></dl>
<p> <i>&quot;t&quot;</i></p>
<dl>
<dd>Open a new tab (<i>open-new-tab</i>)</dd></dl>
<p> <i>&quot;u&quot;</i></p>
<dl>
<dd>Go forward in history (<i>history-move-forward</i>)</dd></dl>
<p> <i>&quot;v&quot;</i></p>
<dl>
<dd>View the current image (<i>view-image</i>)</dd></dl>
<p> <i>&quot;x&quot;</i></p>
<dl>
<dd>Follow the current link, forcing reload of the target (<i>link-follow-reload</i>)</dd></dl>
<p> <i>&quot;z&quot;</i></p>
<dl>
<dd>Abort connection (<i>abort-connection</i>)</dd></dl>
<p> <i>&quot;{&quot;</i></p>
<dl>
<dd>Scroll left (<i>scroll-left</i>)</dd></dl>
<p> <i>&quot;|&quot;</i></p>
<dl>
<dd>Show information about the current page protocol headers (<i>header-info</i>)</dd></dl>
<p> <i>&quot;}&quot;</i></p>
<dl>
<dd>Scroll right (<i>scroll-right</i>)</dd></dl>
<p> <i>Backspace</i></p>
<dl>
<dd>Backspace the last entered digit of the current prefix (<i>backspace-prefix</i>)</dd></dl>
<p> <i>Delete</i></p>
<dl>
<dd>Scroll down (<i>scroll-down</i>)</dd></dl>
<p> <i>Down</i></p>
<dl>
<dd>Move to the next link (<i>move-link-next</i>)</dd></dl>
<p> <i>End</i></p>
<dl>
<dd>Move to the end of the document (<i>move-document-end</i>)</dd></dl>
<p> <i>Enter</i></p>
<dl>
<dd>Follow the current link (<i>link-follow</i>)</dd></dl>
<p> <i>Ctrl-Enter</i></p>
<dl>
<dd>Follow the current link, forcing reload of the target (<i>link-follow-reload</i>)</dd></dl>
<p> <i>Escape</i></p>
<dl>
<dd>Activate the menu (<i>menu</i>)</dd></dl>
<p> <i>F10</i></p>
<dl>
<dd>Open the File menu (<i>file-menu</i>)</dd></dl>
<p> <i>F9</i></p>
<dl>
<dd>Activate the menu (<i>menu</i>)</dd></dl>
<p> <i>Home</i></p>
<dl>
<dd>Move to the start of the document (<i>move-document-start</i>)</dd></dl>
<p> <i>Insert</i></p>
<dl>
<dd>Scroll up (<i>scroll-up</i>)</dd></dl>
<p> <i>Ctrl-Insert</i></p>
<dl>
<dd>Copy text to clipboard (<i>copy-clipboard</i>)</dd></dl>
<p> <i>Left</i></p>
<dl>
<dd>Return to the previous document in history (<i>history-move-back</i>)</dd></dl>
<p> <i>PageDown</i></p>
<dl>
<dd>Move downwards by a page (<i>move-page-down</i>)</dd></dl>
<p> <i>PageUp</i></p>
<dl>
<dd>Move upwards by a page (<i>move-page-up</i>)</dd></dl>
<p> <i>Right</i></p>
<dl>
<dd>Follow the current link (<i>link-follow</i>)</dd></dl>
<p> <i>Ctrl-Right</i></p>
<dl>
<dd>Follow the current link, forcing reload of the target (<i>link-follow-reload</i>)</dd></dl>
<p> <i>Tab</i></p>
<dl>
<dd>Move to the next frame (<i>frame-next</i>)</dd></dl>
<p> <i>Alt-Tab</i></p>
<dl>
<dd>Move to the previous frame (<i>frame-prev</i>)</dd></dl>
<p> <i>Shift-Tab</i></p>
<dl>
<dd>Move to the previous frame (<i>frame-prev</i>)</dd></dl>
<p> <i>Up</i></p>
<dl>
<dd>Move to the previous link (<i>move-link-prev</i>)</dd></dl>
<h3>Edit Keys</h3>
<p><i>Alt-&quot;&lt;&quot;</i></p>
<dl>
<dd>Go to the first line of the buffer (<i>beginning-of-buffer</i>)</dd></dl>
<p> <i>Alt-&quot;&gt;&quot;</i></p>
<dl>
<dd>Go to the last line of the buffer (<i>end-of-buffer</i>)</dd></dl>
<p> <i>Ctrl-&quot;A&quot;</i></p>
<dl>
<dd>Go to the start of the page/line (<i>home</i>)</dd></dl>
<p> <i>Alt-&quot;b&quot;</i></p>
<dl>
<dd>Move cursor before current word (<i>move-backward-word</i>)</dd></dl>
<p> <i>Ctrl-&quot;D&quot;</i></p>
<dl>
<dd>Delete character under cursor (<i>delete</i>)</dd></dl>
<p> <i>Ctrl-&quot;E&quot;</i></p>
<dl>
<dd>Go to the end of the page/line (<i>end</i>)</dd></dl>
<p> <i>Alt-&quot;f&quot;</i></p>
<dl>
<dd>Move cursor after current word (<i>move-forward-word</i>)</dd></dl>
<p> <i>Ctrl-&quot;H&quot;</i></p>
<dl>
<dd>Delete character in front of the cursor (<i>backspace</i>)</dd></dl>
<p> <i>Ctrl-&quot;K&quot;</i></p>
<dl>
<dd>Delete to end of line (<i>kill-to-eol</i>)</dd></dl>
<p> <i>Ctrl-&quot;L&quot;</i></p>
<dl>
<dd>Redraw the terminal (<i>redraw</i>)</dd></dl>
<p> <i>Alt-&quot;r&quot;</i></p>
<dl>
<dd>Toggle regex matching (type-ahead searching) (<i>search-toggle-regex</i>)</dd></dl>
<p> <i>Ctrl-&quot;F&quot;</i></p>
<dl>
<dd>Attempt to auto-complete a local file (<i>auto-complete-file</i>)</dd></dl>
<p> <i>Ctrl-&quot;R&quot;</i></p>
<dl>
<dd>Attempt to unambiguously auto-complete the input (<i>auto-complete-unambiguous</i>)</dd></dl>
<p> <i>Ctrl-&quot;T&quot;</i></p>
<dl>
<dd>Open in external editor (<i>open-external</i>)</dd></dl>
<p> <i>Ctrl-&quot;U&quot;</i></p>
<dl>
<dd>Delete to beginning of line (<i>kill-to-bol</i>)</dd></dl>
<p> <i>Ctrl-&quot;V&quot;</i></p>
<dl>
<dd>Paste text from the clipboard (<i>paste-clipboard</i>)</dd></dl>
<p> <i>Ctrl-&quot;W&quot;</i></p>
<dl>
<dd>Attempt to auto-complete the input (<i>auto-complete</i>)</dd></dl>
<p> <i>Ctrl-&quot;X&quot;</i></p>
<dl>
<dd>Cut text to clipboard (<i>cut-clipboard</i>)</dd></dl>
<p> <i>Alt-Backspace</i></p>
<dl>
<dd>Delete backwards to start of word (<i>kill-word-back</i>)</dd></dl>
<p> <i>Backspace</i></p>
<dl>
<dd>Delete character in front of the cursor (<i>backspace</i>)</dd></dl>
<p> <i>Delete</i></p>
<dl>
<dd>Delete character under cursor (<i>delete</i>)</dd></dl>
<p> <i>Down</i></p>
<dl>
<dd>Move cursor downwards (<i>down</i>)</dd></dl>
<p> <i>End</i></p>
<dl>
<dd>Go to the end of the page/line (<i>end</i>)</dd></dl>
<p> <i>Enter</i></p>
<dl>
<dd>Follow the current link (<i>enter</i>)</dd></dl>
<p> <i>Escape</i></p>
<dl>
<dd>Cancel current state (<i>cancel</i>)</dd></dl>
<p> <i>F4</i></p>
<dl>
<dd>Open in external editor (<i>open-external</i>)</dd></dl>
<p> <i>Home</i></p>
<dl>
<dd>Go to the start of the page/line (<i>home</i>)</dd></dl>
<p> <i>Ctrl-Insert</i></p>
<dl>
<dd>Copy text to clipboard (<i>copy-clipboard</i>)</dd></dl>
<p> <i>Left</i></p>
<dl>
<dd>Move the cursor left (<i>left</i>)</dd></dl>
<p> <i>Right</i></p>
<dl>
<dd>Move the cursor right (<i>right</i>)</dd></dl>
<p> <i>Tab</i></p>
<dl>
<dd>Move to the next item (<i>next-item</i>)</dd></dl>
<p> <i>Alt-Tab</i></p>
<dl>
<dd>Move to the previous item (<i>previous-item</i>)</dd></dl>
<p> <i>Shift-Tab</i></p>
<dl>
<dd>Move to the previous item (<i>previous-item</i>)</dd></dl>
<p> <i>Up</i></p>
<dl>
<dd>Move cursor upwards (<i>up</i>)</dd></dl>
<h3>Menu Keys</h3>
<p><i>Space</i></p>
<dl>
<dd>Select current highlighted item (<i>select</i>)</dd></dl>
<p> <i>&quot;*&quot;</i></p>
<dl>
<dd>Mark item (<i>mark-item</i>)</dd></dl>
<p> <i>&quot;+&quot;</i></p>
<dl>
<dd>Expand item (<i>expand</i>)</dd></dl>
<p> <i>&quot;-&quot;</i></p>
<dl>
<dd>Collapse item (<i>unexpand</i>)</dd></dl>
<p> <i>&quot;/&quot;</i></p>
<dl>
<dd>Search for a text pattern (<i>search</i>)</dd></dl>
<p> <i>&quot;=&quot;</i></p>
<dl>
<dd>Expand item (<i>expand</i>)</dd></dl>
<p> <i>Ctrl-&quot;A&quot;</i></p>
<dl>
<dd>Go to the start of the page/line (<i>home</i>)</dd></dl>
<p> <i>Ctrl-&quot;B&quot;</i></p>
<dl>
<dd>Move upwards by a page (<i>page-up</i>)</dd></dl>
<p> <i>Ctrl-&quot;E&quot;</i></p>
<dl>
<dd>Go to the end of the page/line (<i>end</i>)</dd></dl>
<p> <i>Ctrl-&quot;F&quot;</i></p>
<dl>
<dd>Move downwards by a page (<i>page-down</i>)</dd></dl>
<p> <i>Ctrl-&quot;L&quot;</i></p>
<dl>
<dd>Redraw the terminal (<i>redraw</i>)</dd></dl>
<p> <i>Ctrl-&quot;N&quot;</i></p>
<dl>
<dd>Move cursor downwards (<i>down</i>)</dd></dl>
<p> <i>Ctrl-&quot;P&quot;</i></p>
<dl>
<dd>Move cursor upwards (<i>up</i>)</dd></dl>
<p> <i>Alt-&quot;V&quot;</i></p>
<dl>
<dd>Move upwards by a page (<i>page-up</i>)</dd></dl>
<p> <i>Ctrl-&quot;V&quot;</i></p>
<dl>
<dd>Move downwards by a page (<i>page-down</i>)</dd></dl>
<p> <i>&quot;[&quot;</i></p>
<dl>
<dd>Expand item (<i>expand</i>)</dd></dl>
<p> <i>&quot;]&quot;</i></p>
<dl>
<dd>Collapse item (<i>unexpand</i>)</dd></dl>
<p> <i>&quot;_&quot;</i></p>
<dl>
<dd>Collapse item (<i>unexpand</i>)</dd></dl>
<p> <i>Delete</i></p>
<dl>
<dd>Delete character under cursor (<i>delete</i>)</dd></dl>
<p> <i>Down</i></p>
<dl>
<dd>Move cursor downwards (<i>down</i>)</dd></dl>
<p> <i>End</i></p>
<dl>
<dd>Go to the end of the page/line (<i>end</i>)</dd></dl>
<p> <i>Enter</i></p>
<dl>
<dd>Follow the current link (<i>enter</i>)</dd></dl>
<p> <i>Escape</i></p>
<dl>
<dd>Cancel current state (<i>cancel</i>)</dd></dl>
<p> <i>Home</i></p>
<dl>
<dd>Go to the start of the page/line (<i>home</i>)</dd></dl>
<p> <i>Insert</i></p>
<dl>
<dd>Mark item (<i>mark-item</i>)</dd></dl>
<p> <i>Left</i></p>
<dl>
<dd>Move the cursor left (<i>left</i>)</dd></dl>
<p> <i>PageDown</i></p>
<dl>
<dd>Move downwards by a page (<i>page-down</i>)</dd></dl>
<p> <i>PageUp</i></p>
<dl>
<dd>Move upwards by a page (<i>page-up</i>)</dd></dl>
<p> <i>Right</i></p>
<dl>
<dd>Move the cursor right (<i>right</i>)</dd></dl>
<p> <i>Tab</i></p>
<dl>
<dd>Move to the next item (<i>next-item</i>)</dd></dl>
<p> <i>Alt-Tab</i></p>
<dl>
<dd>Move to the previous item (<i>previous-item</i>)</dd></dl>
<p> <i>Shift-Tab</i></p>
<dl>
<dd>Move to the previous item (<i>previous-item</i>)</dd></dl>
<p> <i>Up</i></p>
<dl>
<dd>Move cursor upwards (<i>up</i>)</dd></dl>
<h2>Author</h2>
<p>This manual page was finally written by Peter Wang (one and a half years after writing the binding code), using excerpts by David Mediavilla. You can thank Petr Baudis for the subtle requests for documentation. Updated by Zas. Moved to asciidoc format and cleaned up by Jonas Fonseca.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-elinks/">elinks</a></code>(1), <code><a href="/docs/linux/man/5-elinks-conf/">elinks.conf</a></code>(5) </p>
