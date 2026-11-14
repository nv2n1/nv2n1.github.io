---
title: "cdargs(1)"
name: "cdargs"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cdargs/"
description: "cdargs – bookmarks and browser for cd shell built-in"
---

<h2>NAME</h2>
<p> cdargs &#8211; bookmarks and browser for cd shell built-in</p>
<h2>SYNOPSIS</h2>
<p> <code>cdargs</code> [<i>OPTIONS</i>] </p>
<p> <code>function cv () { </code><br />
 <code> cdargs $1 &amp;&amp; cd `cat $HOME/.cdargsresult` ;</code><br />
 <code>}</code><br />
 <code>cv </code> [<i>Needle</i>] </p>
<h2>DESCRIPTION</h2>
<p> With <i>cdargs</i> you can jump to various places throughout the file-system that are defined using a plain text, line oriented bookmarks file. </p>
<p> You can create bookmarks by editing your bookmarks file &quot;$HOME/.cdargs&quot; using your favorite editor, by using the &quot;&#8211;add&quot; option to <i>cdargs</i> or by using the built-in mechanism that will be described later. </p>
<p> While you are in <i>cdargs</i> you can use various commands to navigate through your list of bookmarks and through the file-system. These are described below in the section &quot;COMMANDS&quot;. The most commonly used and most obvious commands are the up/down keys for navigation, &quot;ENTER&quot; for selection of a path and &quot;q&quot; for quit. </p>
<p> To be able to actually use this program together with the shell built-in &quot;cd&quot; command you must use a little trick by defining a shell function. Of course the syntax for this is different between the <i>csh</i>-like shells (like <i>tcsh</i>) and the <i>sh</i>-like shells (like <i>bash</i>). </p>
<p> For <i>sh</i>-like shells:<br />
 function cv () { </p>
<p>&nbsp;<wbr>cdargs&nbsp;<wbr>&quot;$1&quot;&nbsp;<wbr>&amp;&amp;&nbsp;<wbr>cd&nbsp;<wbr>&quot;`cat&nbsp;<wbr>&quot;$HOME/.cdargsresult&quot;`&quot;&nbsp;<wbr>;<br />
 } </p>
<p> For <i>csh</i>-like shells:<br />
 alias cv &#8216;cdargs \!* &amp;&amp; cd `cat $HOME/.cdargsresult`&#8217; </p>
<p> Now you only have to put the <i>cdargs</i> binary somewhere into your path. </p>
<p> Of course you can create functions and/or aliases for different purposes. You might want to add a <i>pwd</i> call to echo your current directories or put &#8211;nowrap in your functions to enable a different scrolling behavior. See section SHELL FUNCTIONS below. </p>
<p> Since version 1.19 cdargs brings a collection of bash functions (and since 1.20 tcsh aliases, too) with it. You only have to source this in your ~/.profile or ~/.bashrc (or ~/.tcsh) and you get nice kinds of magic prepared (completion&#8230;). Please read the cdargs-bash.sh or cdargs-tcsh.csh respectively for the documentation of these functions. </p>
<h2>COMMAND-LINE OPTIONS</h2>
<p> You can call <i>cdargs</i> with a few options, but otherwise you probably won&#8217;t call it directly but via the function you defined.</p>
<dl>
<dt><code>-h</code> or <code>&#8211;help</code></p>
<dd> display usage information and exit.</p>
<dt><code>-v</code> or <code>&#8211;version</code></p>
<dd> output version information and exit.</p>
<dt><code>-a</code> or <code>&#8211;add=</code>[:<i>desc</i>:]<i>path</i></p>
<dd> add <i>path</i> to the bookmarks list using the optional <i>desc</i> as description string.</p>
<dt><code>-f</code> or <code>&#8211;file=</code><i>FILE</i></p>
<dd> uses the given FILE as bookmarks file</p>
<dt><code>-u</code> or <code>&#8211;user=</code><i>USER</i></p>
<dd> read the default bookmarks file of USER. Won&#8217;t modify that file.</p>
<dt><code>-o</code> or <code>&#8211;output=</code><i>FILE</i></p>
<dd> use FILE as the result-file (who knows what The World might make of this feature that I can&#8217;t imagine&#8230;)</p>
<dt><code>-b</code> or <code>&#8211;browse</code></p>
<dd> start <i>cdargs</i> in BROWSE mode in the current directory.</p>
<dt><code>-r</code> or <code>&#8211;noresolve</code></p>
<dd> Don&#8217;t exit with a result when the <i>Needle</i> matches a description exactly (which is some every-day-magic) but show a list (even if it contains just one entry).</p>
<dt><code>-c</code> or <code>&#8211;cwd</code></p>
<dd> Make the current working directory the current entry on startup if it appears on the list.</p>
<dt><code>&#8211;nowrap</code></p>
<dd> Don&#8217;t wrap the cursor around when hitting the end of the list.</p>
<dt><i>Needle</i></p>
<dd> The Needle performs some magic which I hope improves the usage of cdargs. </p>
<p> The Needle is examined in the following order and the first thing that fits is taken. </p>
<p> If <i>Needle</i> is a one-digit integer the appropriate entry is preselected. </p>
<p> Otherwise if <i>Needle</i> is a string each entry of the list is checked whether it contains <i>Needle</i>. </p>
<p> Then <i>Needle</i> has two functions:<br />
 If it just matches a substring of either path or description that option is placed in the list. </p>
<p> If it <code>exactly</code> matches a description string this is the result (that means cdargs closes the curses window, exits and the changing of directories takes place).<br />
&nbsp;<wbr> If it doesn&#8217;t match a line, that line won&#8217;t be displayed. </p>
<p> And to make things even more complicated you can affect this behavior by using the &quot;&#8211;noresolve&quot; option. This option is used when you think you give a <i>Needle</i> which matches descriptions exactly but you don&#8217;t want it to be resolved if it does. This option is internally turned on when you delete an entry (otherwise the deletion of entries until only one entry is left would lead to resolving) or when the bookmarks file contains only one entry. </p>
<p> Finally, if the filtered list (but not the bookmarks file) contains only one entry it is selected and the program exits successfully, unless you chose &#8211;noresolve. </p>
<p> I can only hope that you understand this nested if babble&#8230; </p>
<p> Please note, that the existence of a <i>Needle</i> disables the saving of the list at the end of the program.<br />
&nbsp;<wbr></dl>
<h2>COMMANDS</h2>
<p> When you are in <i>cdargs</i> you have two modes and several commands at your hands. </p>
<p> The two modes are LIST (when your bookmark list is displayed) and BROWSE (when you navigate through the file-system). </p>
<p> The navigation keys are mostly available in Emacs and vi style for all maniacs out there. </p>
<p> <code>Common Keys</code></p>
<dl>
<dt><code>&lt;UP&gt;/&lt;DOWN&gt;</code> or <code>k/j</code> or <code>C-n/C-p</code></p>
<dd> move selection up/down and scroll.</p>
<dt><code>&lt;ENTER&gt;</code></p>
<dd> select current entry.</p>
<dt><code>&lt;TAB&gt;</code></p>
<dd> toggle modes: LIST or BROWSE.</p>
<dt><code>&lt;HOME&gt;/&lt;END&gt;</code> or <code>C-a/C-e</code></p>
<dd> goto first/last entry in list.</p>
<dt><code>c</code></p>
<dd> add current directory to list.</p>
<dt><code>C</code></p>
<dd> add current directory to list but ask the user for a description</p>
<dt><code>&lt;PgUp&gt;/&lt;PgDown&gt;</code> or <code>C-v</code></p>
<dd> Scroll the list in 10-line-steps. This will never wraparound and does not honor the nowrap-option</p>
<dt><code>e, v</code></p>
<dd> edit the list in $EDITOR.</p>
<dt><code>H, ?</code></p>
<dd> show the help-screen.</p>
<dt><code>~, /</code></p>
<dd> browse home/root directory.</p>
<dt><code>q</code></p>
<dd> quit &#8211; saving the list.</p>
<dt><code>C-c, C-g, C-[ </code></p>
<dd> abort &#8211; don&#8217;t save the list.</dl>
<p> <code>Keys in BROWSE mode</code></p>
<dl>
<dt><code>&lt;LEFT&gt;, h, C-b</code></p>
<dd> descent into current directory.</p>
<dt><code>&lt;RIGHT&gt;, l, C-f</code></p>
<dd> up one directory.</p>
<dt><code>[num]</code></p>
<dd> make [num] the current highlighted entry</p>
<dt><code>a</code></p>
<dd> add current entry to list.</p>
<dt><code>A</code></p>
<dd> add current entry to list but ask the user for a description, just like with &#8216;c&#8217; and &#8216;C&#8217;.</p>
<dt><code>.</code></p>
<dd> toggle display of hidden files.</dl>
<p> <code>Keys in LIST mode</code></p>
<dl>
<dt><code>[num]</code></p>
<dd> select and resolve entry [num] if displayed.</p>
<dt><code>&lt;LEFT&gt;, h, C-b</code></p>
<dd> descent into the current entry.</p>
<dt><code>&lt;RIGHT&gt;, l, C-f</code></p>
<dd> up one directory from current dir.</p>
<dt><code>d</code> or <code>C-d</code></p>
<dd> delete current entry from list.</p>
<dt><code>s</code> or <code>t</code></p>
<dd> swap (transpose) two entries of the list.</p>
<dt><code>M</code> or <code>m</code></p>
<dd> move an entry up or down in the list and set the current position afterwards so that repeated keystrokes keep moving the same entry up and down. </p>
</dl>
<h2>SHELL FUNCTIONS</h2>
<p> In addition to the shell function mentioned above you might wish to add other commands to your function. One example is to echo the directory you changed to: </p>
<p> function cv () { </p>
<p>&nbsp;<wbr>cdargs&nbsp;<wbr>&quot;$1&quot;&nbsp;<wbr>&amp;&amp;&nbsp;<wbr>cd&nbsp;<wbr>&quot;`cat&nbsp;<wbr>&quot;$HOME/.cdargsresult&quot;`&quot;&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&amp;&amp;&nbsp;<wbr>pwd;<br />
 } </p>
<p> Or you can remove the file in which <i>cdargs</i> reports it&#8217;s result: </p>
<p> function cv () { </p>
<p>&nbsp;<wbr>cdargs&nbsp;<wbr>&quot;$1&quot;&nbsp;<wbr>&amp;&amp;&nbsp;<wbr>cd&nbsp;<wbr>&quot;`cat&nbsp;<wbr>&quot;$HOME/.cdargsresult&quot;`&quot;&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&amp;&amp;&nbsp;<wbr>rm -f&nbsp;<wbr>&quot;$HOME/.cdargsresult&quot;;<br />
 } </p>
<p> Since version 1.19 cdargs comes with a file of preset functions for bash: see cdargs-bash.sh in the distribution. From now on you only have to source that file if you are using a <i>sh</i>-like shell. Then you can use the shell completion to switch directories even faster by typing </p>
<p> cv [TAB] </p>
<p> Since version 1.20 cdargs comes with a file of rudimentary aliases (and completion) for the <i>tcsh</i>.<br />
 Any volunteers for porting all the bash functionality to <i>tcsh</i> are welcome. </p>
<h2>DISPLAY</h2>
<p> The <i>cdargs</i> window has one line at the bottom for the display of messages like when you added to your list or when you hit an unknown key. </p>
<p> The second line from the bottom is a status line which shows the current directory and a one letter code for the current operation mode:</p>
<dl>
<dt><code>B</code></p>
<dd> for BROWSE</p>
<dt><code>L</code></p>
<dd> for LIST</dl>
<p> The largest part of the display is used to show you either the list of your bookmarks or the contents of the current directory. On the left side you&#8217;ll probably find a number which you can use for a slightly quicker jumping compared to using the cursor movement. These numbers can be moved as described above. Next comes the short description of an entry in brackets. This is convient when you have quite long paths in your bookmarks and most of them start with the same base (e.g. /home/user). Finally there is the actual absolute path you&#8217;ll be warping to when finishing. Obviously the current entry is highlighted. </p>
<p> If the path is preced by a &quot;!&quot; it points to an invalid directory. A bookmark pointing to the current working directory is displayed in bold font (if the terminal emulation understands that attribute). </p>
<h2>FILES</h2>
<p> <i>$HOME/.cdargs</i> personal bookmarks file.</p>
<dl>
<dt><i>$HOME/.cdargsresult</i></p>
<dd> temporary file for passing results to shell.</p>
<dt><i>contrib/cdargs-bash.sh</i></p>
<dd> example collection of bash functions.</p>
<dt><i>contrib/cdargs-tcsh.csh</i></p>
<dd> example collection of tcsh functions.</p>
<dt><i>contrib/cdargs.el</i></p>
<dd> (X)Emacs front-end to personal bookmarks file </p>
</dl>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;mail [at] skamphausen.de&gt;.</p>
<h2>AUTHOR</h2>
<p> <i>cdargs</i> was written by Stefan Kamphausen with add-ons by Claus Brunzema. Many user-interface improvements came from Dan Allen.</p>
<h2>SEE ALSO</h2>
<p> The current version of <i>cdargs</i> is located at</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.skamphausen.de/software/cdargs">http://www.skamphausen.de/software/cdargs</a></dl>
<p> You might want to visit that site. Other than that pressing the &#8216;H&#8217; key in <i>cdargs</i> fires up a help screen.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001-2003 Stefan Kamphausen </p>
<p> <i>cdargs</i> is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA. </p>
<h2>Index</h2>
