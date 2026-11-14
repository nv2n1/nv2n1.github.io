---
title: "xcscope(1)"
name: "xcscope"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xcscope/"
description: "xcscope.el – xemacs cscope lisp support package"
---

<h2>NAME</h2>
<p> xcscope.el &#8211; xemacs cscope lisp support package</p>
<h2>DESCRIPTION</h2>
<p> xcscope is a lisp package for use in integrating cscope functionality into xemacs</p>
<h2>INSTALLATION</h2>
<p>&nbsp;<wbr>Installation steps: </p>
<p>&nbsp;<wbr>0.&nbsp;<wbr>(It is, of course, assumed that cscope is already properly<br />
&nbsp;<wbr>installed on the current system.)<br />
&nbsp;<wbr>1. Ensure that the location of cscope-indexer is located in your path </p>
<p>&nbsp;<wbr>2. Ensure that the location of xcscope.el is in the xemacs module load path </p>
<p>&nbsp;<wbr>3. Edit your&nbsp;<wbr>~/.emacs file to add the line: <code>(require</code><i>&#8216;xcscope)</i> </p>
<p> 5. If you intend to use xcscope.el often you can optionally edit your ~/.emacs file to add keybindings that reduce the number of keystrokes required. For example, the following will add &quot;C-f#&quot; keybindings, which are easier to type than the usual &quot;C-c s&quot; prefixed keybindings. Note that specifying &quot;global-map&quot; instead of &quot;cscope:map&quot; makes the keybindings available in all buffers: </p>
<pre><code>
        (define-key global-map [(ctrl f3)]  'cscope-set-initial-directory)
        (define-key global-map [(ctrl f4)]  'cscope-unset-initial-directory)
        (define-key global-map [(ctrl f5)]  'cscope-find-this-symbol)
        (define-key global-map [(ctrl f6)]  'cscope-find-global-definition)
        (define-key global-map [(ctrl f7)]
                cscope-find-global-definition-no-prompting)
        (define-key global-map [(ctrl f8)]  'cscope-pop-mark)
        (define-key global-map [(ctrl f9)]  'cscope-next-symbol)
        (define-key global-map [(ctrl f10)] 'cscope-next-file)
        (define-key global-map [(ctrl f11)] 'cscope-prev-symbol)
        (define-key global-map [(ctrl f12)] 'cscope-prev-file)
        (define-key global-map [(meta f9)]  'cscope-display-buffer)
        (define-key global-map [(meta f10)] 'cscope-display-buffer-toggle)
</code></pre>
<p>&nbsp;<wbr>6. Restart&nbsp;<wbr>(X)Emacs.&nbsp;<wbr>&nbsp;<wbr>That&#8217;s it. </p>
<h2>USING THIS MODULE</h2>
<h3>* Basic usage:</h3>
<p>&nbsp;<wbr>If all of your C/C++/lex/yacc source files are in the same<br />
&nbsp;<wbr>directory, you can just start using this module.&nbsp;<wbr>&nbsp;<wbr>If your files are<br />
&nbsp;<wbr>spread out over multiple directories, see&nbsp;<wbr>&quot;Advanced usage&quot;, below. </p>
<p>&nbsp;<wbr>Just edit a source file, and use the pull-down or pop-up&nbsp;<wbr>(button 3)<br />
&nbsp;<wbr>menus to select one of: </p>
<pre>
        Find symbol
        Find global definition
        Find called functions
        Find functions calling a function
        Find text string
        Find egrep pattern
        Find a file
        Find files #including a file
</pre>
<p> The cscope database will be automatically created in the same directory as the source files (assuming that you&#8217;ve never used cscope before), and a buffer will pop-up displaying the results. You can then use button 2 (the middle button) on the mouse to edit the selected file, or you can move the text cursor over a selection and press [Enter]. </p>
<p> Hopefully, the interface should be fairly intuitive. </p>
<h3>* Locating the cscope databases:</h3>
<p> This module will first use the variable, `cscope-database-regexps&#8217;, to search for a suitable database directory. If a database location cannot be found using this variable then a search is begun at the variable, `cscope-initial-directory&#8217;, if set, or the current directory otherwise. If the directory is not a cscope database directory then the directory&#8217;s parent, parent&#8217;s parent, etc. is searched until a cscope database directory is found, or the root directory is reached. If the root directory is reached, the current directory will be used. </p>
<p> A cscope database directory is one in which EITHER a cscope database file (e.g., &quot;cscope.out&quot;) OR a cscope file list (e.g., &quot;cscope.files&quot;) exists. If only &quot;cscope.files&quot; exists, the corresponding &quot;cscope.out&quot; will be automatically created by cscope when a search is done. By default, the cscope database file is called &quot;cscope.out&quot;, but this can be changed (on a global basis) via the variable, `cscope-database-file&#8217;. There is limited support for cscope databases that are named differently than that given by `cscope-database-file&#8217;, using the variable, `cscope-database-regexps&#8217;. </p>
<p> Note that the variable, `cscope-database-regexps&#8217;, is generally not needed, as the normal hierarchical database search is sufficient for placing and/or locating the cscope databases. However, there may be cases where it makes sense to place the cscope databases away from where the source files are kept; in this case, this variable is used to determine the mapping. One use for this variable is when you want to share the database file with other users; in this case, the database may be located in a directory separate from the source files. </p>
<p> Setting the variable, `cscope-initial-directory&#8217;, is useful when a search is to be expanded by specifying a cscope database directory that is a parent of the directory that this module would otherwise use. For example, consider a project that contains the following cscope database directories: </p>
<pre>
        /users/jdoe/sources
        /users/jdoe/sources/proj1
        /users/jdoe/sources/proj2
</pre>
<p> If a search is initiated from a .c file in /users/jdoe/sources/proj1 then (assuming the variable, `cscope-database-regexps&#8217;, is not set) /users/jdoe/sources/proj1 will be used as the cscope data base directory. Only matches in files in /users/jdoe/sources/proj1 will be found. This can be remedied by typing &quot;C-c s a&quot; and then &quot;M-del&quot; to remove single path element in order to use a cscope database directory of /users/jdoe/sources. Normal searching can be restored by typing &quot;C-c s A&quot;. </p>
<h3>* Keybindings:</h3>
<p> All keybindings use the &quot;C-c s&quot; prefix, but are usable only while editing a source file, or in the cscope results buffer: </p>
<p> <code>C-c s s Find symbol.</code></p>
<dl>
<dt><code>C-c s d Find global definition.</code></p>
<dd>
<dt><code>C-c s g Find global definition (alternate binding).</code></p>
<dd>
<dt><code>C-c s G Find global definition without prompting.</code></p>
<dd>
<dt><code>C-c s c Find functions calling a function.</code></p>
<dd>
<dt><code>C-c s C Find called functions (list functions called</code></p>
<dd> <code> from a function).</code></p>
<dt><code>C-c s t Find text string.</code></p>
<dd>
<dt><code>C-c s e Find egrep pattern.</code></p>
<dd>
<dt><code>C-c s f Find a file.</code></p>
<dd>
<dt><code>C-c s i Find files #including a file.</code></p>
<dd>
<p> These pertain to navigation through the search results: </p>
<p> <code>C-c s b Display *cscope* buffer.</code></p>
<dt><code>C-c s B Auto display *cscope* buffer toggle.</code></p>
<dd>
<dt><code>C-c s n Next symbol.</code></p>
<dd>
<dt><code>C-c s N Next file.</code></p>
<dd>
<dt><code>C-c s p Previous symbol.</code></p>
<dd>
<dt><code>C-c s P Previous file.</code></p>
<dd>
<dt><code>C-c s u Pop mark.</code></p>
<dd>
<p> These pertain to setting and unsetting the variable, `cscope-initial-directory&#8217;, (location searched for the cscope database directory): </p>
<p> <code>C-c s a Set initial directory.</code></p>
<dt><code>C-c s A Unset initial directory.</code></p>
<dd>
<p> These pertain to cscope database maintenance: <code>C-c s L Create list of files to index.</code></p>
<dt><code>C-c s I Create list and index.</code></p>
<dd>
<dt><code>C-c s E Edit list of files to index.</code></p>
<dd>
<dt><code>C-c s W Locate this buffer&#8217;s cscope directory</code></p>
<dd> <code> (</code> &quot;W&quot; &#8211;&gt; &quot;where&quot; <code>).</code></p>
<dt><code>C-c s S Locate this buffer&#8217;s cscope directory.</code></p>
<dd> <code> (alternate binding: </code> &quot;S&quot; &#8211;&gt; &quot;show&quot; <code>).</code></p>
<dt><code>C-c s T Locate this buffer&#8217;s cscope directory.</code></p>
<dd> <code> (alternate binding: </code> &quot;T&quot; &#8211;&gt; &quot;tell&quot; <code>).</code></p>
<dt><code>C-c s D Dired this buffer&#8217;s directory.</code></p>
<dd>
</dl>
<h3>* Advanced usage:</h3>
<p> If the source files are spread out over multiple directories, you&#8217;ve got a few choices: </p>
<p> [ NOTE: you will need to have the script, &quot;cscope-indexer&quot;, properly installed in order for the following to work. ] </p>
<p> 1. If all of the directories exist below a common directory (without any extraneous, unrelated subdirectories), you can tell this module to place the cscope database into the top-level, common directory. This assumes that you do not have any cscope databases in any of the subdirectories. If you do, you should delete them; otherwise, they will take precedence over the top-level database. </p>
<p> If you do have cscope databases in any subdirectory, the following instructions may not work right. </p>
<p> It&#8217;s pretty easy to tell this module to use a top-level, common directory: </p>
<dl>
<dt>
<dd>a. Make sure that the menu pick, &quot;Cscope/Index recursively&quot;, is checked (the default value). </p>
<dt>
<dd>b. Select the menu pick, &quot;Cscope/Create list and index&quot;, and specify the top-level directory. This will run the script, &quot;cscope-indexer&quot;, in the background, so you can do other things if indexing takes a long time. A list of files to index will be created in &quot;cscope.files&quot;, and the cscope database will be created in &quot;cscope.out&quot;. </p>
<dt>
<dd>Once this has been done, you can then use the menu picks (described in &quot;Basic usage&quot;, above) to search for symbols. </p>
<dt>
<dd>Note, however, that, if you add or delete source files, you&#8217;ll have to either rebuild the database using the above procedure, or edit the file, &quot;cscope.files&quot; to add/delete the names of the source files. To edit this file, you can use the menu pick, &quot;Cscope/Edit list of files to index&quot;. </p>
<p> 2. If most of the files exist below a common directory, but a few are outside, you can use the menu pick, &quot;Cscope/Create list of files to index&quot;, and specify the top-level directory. Make sure that &quot;Cscope/Index recursively&quot;, is checked before you do so, though. You can then edit the list of files to index using the menu pick, &quot;Cscope/Edit list of files to index&quot;. Just edit the list to include any additional source files not already listed. </p>
<p> Once you&#8217;ve created, edited, and saved the list, you can then use the menu picks described under &quot;Basic usage&quot;, above, to search for symbols. The first time you search, you will have to wait a while for cscope to fully index the source files, though. If you have a lot of source files, you may want to manually run cscope to build the database: </p>
<pre>
        cd top-level-directory    # or wherever
        rm -f cscope.out          # not always necessary
        cscope -b
</pre>
<p>&nbsp;<wbr>3. If the source files are scattered in many different, unrelated<br />
&nbsp;<wbr>places, you&#8217;ll have to manually create cscope.files and put a<br />
&nbsp;<wbr>list of all pathnames into it.&nbsp;<wbr>&nbsp;<wbr>Then build the database using: </p>
<pre>
        cd some-directory         # wherever cscope.files exists
        rm -f cscope.out          # not always necessary
        cscope -b
</pre>
<p> Next, read the documentation for the variable, &quot;cscope-database-regexps&quot;, and set it appropriately, such that the above-created cscope database will be referenced when you edit a related source file. </p>
<p> Once this has been done, you can then use the menu picks described under &quot;Basic usage&quot;, above, to search for symbols. </p>
</dl>
<h3>* Interesting configuration variables:</h3>
<p> <code>cscope-truncate-lines</code> This is the value of `truncate-lines&#8217; to use in cscope buffers; the default is the current setting of `truncate-lines&#8217;. This variable exists because it can be easier to read cscope buffers with truncated lines, while other buffers do not have truncated lines. </p>
<p> <code>cscope-use-relative-paths</code> If non-nil, use relative paths when creating the list of files to index. The path is relative to the directory in which the cscope database will be created. If nil, absolute paths will be used. Absolute paths are good if you plan on moving the database to some other directory (if you do so, you&#8217;ll probably also have to modify `cscope-database-regexps&#8217;). Absolute paths may also be good if you share the database file with other users (you&#8217;ll probably want to specify some automounted network path for this). </p>
<p> <code>cscope-index-recursively</code> If non-nil, index files in the current directory and all subdirectories. If nil, only files in the current directory are indexed. This variable is only used when creating the list of files to index, or when creating the list of files and the corresponding cscope database. </p>
<p> <code>cscope-name-line-width</code> The width of the combined &quot;function name:line number&quot; field in the cscope results buffer. If negative, the field is left-justified. </p>
<p> <code>cscope-do-not-update-database</code> If non-nil, never check and/or update the cscope database when searching. Beware of setting this to non-nil, as this will disable automatic database creation, updating, and maintenance. </p>
<p> <code>cscope-display-cscope-buffer </code> If non-nil, display the *cscope* buffer after each search (default). This variable can be set in order to reduce the number of keystrokes required to navigate through the matches. </p>
<p> <code>cscope-database-regexps</code> List to force directory-to-cscope-database mappings. This is a list of `(REGEXP DBLIST [ DBLIST &#8230; ])&#8217;, where: </p>
<p> <code>REGEXP </code> is a regular expression matched against the current buffer&#8217;s current directory. The current buffer is typically some source file, and you&#8217;re probably searching for some symbol in or related to this file. Basically, this regexp is used to relate the current directory to a cscope database. You need to start REGEXP with &quot;^&quot; if you want to match from the beginning of the current directory. </p>
<p> <code>DBLIST </code> is a list that contains one or more of: </p>
<pre>
        ( DBDIR )
        ( DBDIR ( OPTIONS ) )
        ( t )
        t
</pre>
<p> Here, <code>DBDIR </code> is a directory (or a file) that contains a cscope database. If DBDIR is a directory, then it is expected that the cscope database, if present, has the filename given by the variable, `cscope-database-file&#8217;; if DBDIR is a file, then DBDIR is the path name to a cscope database file (which does not have to be the same as that given by `cscope-database-file&#8217;). If only DBDIR is specified, then that cscope database will be searched without any additional cscope command-line options. If OPTIONS is given, then OPTIONS is a list of strings, where each string is a separate cscope command-line option. </p>
<p>&nbsp;<wbr>In the case of&nbsp;<wbr>&quot;(&nbsp;<wbr>t&nbsp;<wbr>)&quot;, this specifies that the search is to use the<br />
&nbsp;<wbr>normal hierarchical database search.&nbsp;<wbr>&nbsp;<wbr>This option is used to<br />
&nbsp;<wbr>explicitly search using the hierarchical database search either before<br />
&nbsp;<wbr>or after other cscope database directories. </p>
<p>&nbsp;<wbr>If&nbsp;<wbr>&quot;t&quot;&nbsp;<wbr>is specified&nbsp;<wbr>(not inside a list), this tells the searching<br />
&nbsp;<wbr>mechanism to stop searching if a match has been found&nbsp;<wbr>(at the point<br />
&nbsp;<wbr>where&nbsp;<wbr>&quot;t&quot;&nbsp;<wbr>is encountered).&nbsp;<wbr>&nbsp;<wbr>This is useful for those projects that<br />
&nbsp;<wbr>consist of many subprojects.&nbsp;<wbr>&nbsp;<wbr>You can specify the most-used<br />
&nbsp;<wbr>subprojects first, followed by a&nbsp;<wbr>&quot;t&quot;, and then followed by a master<br />
&nbsp;<wbr>cscope database directory that covers all subprojects.&nbsp;<wbr>&nbsp;<wbr>This will<br />
&nbsp;<wbr>cause the most-used subprojects to be searched first&nbsp;<wbr>(hopefully<br />
&nbsp;<wbr>quickly), and the search will then stop if a match was found.&nbsp;<wbr>&nbsp;<wbr>If not,<br />
&nbsp;<wbr>the search will continue using the master cscope database directory. </p>
<p>&nbsp;<wbr>Here,&nbsp;<wbr>`cscope-database-regexps&#8217;&nbsp;<wbr>is generally not used, as the normal<br />
&nbsp;<wbr>hierarchical database search is sufficient for placing and/or locating<br />
&nbsp;<wbr>the cscope databases.&nbsp;<wbr>&nbsp;<wbr>However, there may be cases where it makes<br />
&nbsp;<wbr>sense to place the cscope databases away from where the source files<br />
&nbsp;<wbr>are kept;&nbsp;<wbr>in this case, this variable is used to determine the<br />
&nbsp;<wbr>mapping. </p>
<p>&nbsp;<wbr>This module searches for the cscope databases by first using this<br />
&nbsp;<wbr>variable;&nbsp;<wbr>if a database location cannot be found using this variable,<br />
&nbsp;<wbr>then the current directory is searched, then the parent, then the<br />
&nbsp;<wbr>parent&#8217;s parent, until a cscope database directory is found, or the<br />
&nbsp;<wbr>root directory is reached.&nbsp;<wbr>&nbsp;<wbr>If the root directory is reached, the<br />
&nbsp;<wbr>current directory will be used. </p>
<p> A cscope database directory is one in which EITHER a cscope database file (e.g., &quot;cscope.out&quot;) OR a cscope file list (e.g., &quot;cscope.files&quot;) exists. If only &quot;cscope.files&quot; exists, the corresponding &quot;cscope.out&quot; will be automatically created by cscope when a search is done. By default, the cscope database file is called &quot;cscope.out&quot;, but this can be changed (on a global basis) via the variable, `cscope-database-file&#8217;. There is limited support for cscope databases that are named differently than that given by `cscope-database-file&#8217;, using the variable, `cscope-database-regexps&#8217;. </p>
<p> Here is an example of `cscope-database-regexps&#8217;: </p>
<pre>
        (setq cscope-database-regexps
              '(
                ( &quot;^/users/jdoe/sources/proj1&quot;
                  ( t )
                  ( &quot;/users/jdoe/sources/proj2&quot;)
                  ( &quot;/users/jdoe/sources/proj3/mycscope.out&quot;)
                  ( &quot;/users/jdoe/sources/proj4&quot;)
                  t
                  ( &quot;/some/master/directory&quot; (&quot;-d&quot; &quot;-I/usr/local/include&quot;) )
                  )
                ( &quot;^/users/jdoe/sources/gnome/&quot;
                  ( &quot;/master/gnome/database&quot; (&quot;-d&quot;) )
                  )
                ))
</pre>
<p> If the current buffer&#8217;s directory matches the regexp, &quot;^/users/jdoe/sources/proj1&quot;, then the following search will be done: </p>
<dl>
<dt>1. First, the normal hierarchical database search will be used to</p>
<dd> locate a cscope database. </p>
<dt>2. Next, searches will be done using the cscope database</p>
<dd> directories, &quot;/users/jdoe/sources/proj2&quot;, &quot;/users/jdoe/sources/proj3/mycscope.out&quot;, and &quot;/users/jdoe/sources/proj4&quot;. Note that, instead of the file, &quot;cscope.out&quot;, the file, &quot;mycscope.out&quot;, will be used in the directory &quot;/users/jdoe/sources/proj3&quot;. </p>
<dt>3. If a match was found, searching will stop.</p>
<dd>
<dt>4. If a match was not found, searching will be done using</p>
<dd> &quot;/some/master/directory&quot;, and the command-line options &quot;-d&quot; and &quot;-I/usr/local/include&quot; will be passed to cscope. </p>
<dt>If the current buffer&#8217;s directory matches the regexp,</p>
<dd> &quot;^/users/jdoe/sources/gnome&quot;, then the following search will be done: </p>
<dt>The search will be done only using the directory,</p>
<dd> &quot;/master/gnome/database&quot;. The &quot;-d&quot; option will be passed to cscope. </p>
<dt>If the current buffer&#8217;s directory does not match any of the above</p>
<dd> regexps, then only the normal hierarchical database search will be done. </p>
</dl>
<h3>* Other notes:</h3>
<p> 1. The script, &quot;cscope-indexer&quot;, uses a sed command to determine what is and is not a C/C++/lex/yacc source file. It&#8217;s idea of a source file may not correspond to yours. </p>
<p> 2. This module is called, &quot;xcscope&quot;, because someone else has already written a &quot;cscope.el&quot; (although it&#8217;s quite old). </p>
<h2>KNOWN BUGS:</h2>
<p> 1. Cannot handle whitespace in directory or file names. </p>
<p> 2. By default, colored faces are used to display results. If you happen to use a black background, part of the results may be invisible (because the foreground color may be black, too). There are at least two solutions for this: </p>
<dl>
<dt><code>2a. Turn off colored faces, by setting `cscope-use-face&#8217; to `nil&#8217;, eg:</code></p>
<dd>
<dt><code>(setq cscope-use-face nil)</code></p>
<dd>
<dt><code> 2b. Explicitly set colors for the faces used by cscope. The faces are</code></p>
<dd>
<pre>
        cscope-file-face
        cscope-function-face
        cscope-line-number-face
        cscope-line-face
        cscope-mouse-face
</pre>
<dt>The face most likely to cause problems (e.g., black-on-black</p>
<dd> color) is `cscope-line-face&#8217;. </p>
<p> 3. The support for cscope databases different from that specified by `cscope-database-file&#8217; is quirky. If the file does not exist, it will not be auto-created (unlike files names by `cscope-database-file&#8217;). You can manually force the file to be created by using <a href="/docs/linux/man/1-touch/">touch</a>(1) to create a zero-length file; the database will be created the next time a search is done. </p>
</dl>
<h2>Index</h2>
