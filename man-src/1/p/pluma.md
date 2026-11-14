---
title: "pluma(1)"
name: "pluma"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pluma/"
description: "Pluma – The MATE Text Editor"
---

<h2 class="name">NAME</h2>
<p> Pluma &#8211; The MATE Text Editor </p>
<h2>SYNOPSIS</h2>
<p> <code>pluma [OPTIONS&#8230;] [FILES&#8230;]</code></p>
<h2>DESCRIPTION</h2>
<p> Pluma is the official text editor of the MATE desktop environment. While aiming at simplicity and ease of use, Pluma is a powerful general purpose text editor. It can be used to create and edit all sorts of text files. </p>
<p> Pluma features a flexible plugin system which can be used to dynamically add new advanced features to Pluma itself. </p>
<p> This manual page briefly documents the <code>pluma</code> command. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>filename(s)&#8230;</code></p>
<dd> Specifies the file to open when <code>pluma</code> starts. If this is not specified, <code>pluma</code> will start a new, blank file with an &quot;Unsaved Document&quot; label. Multiple files can be loaded if they are separated by spaces. <code>pluma</code> also supports handling of remote files.</p>
<dt><code>&#8211;display=DISPLAY</code></p>
<dd> X display to use.</p>
<dt><code>&#8211;encoding</code></p>
<dd> Set the character encoding to be used for opening the files listed on the command line.</p>
<dt><code>&#8211;new-window</code></p>
<dd> Create a new toplevel window in an existing instance of <code>pluma</code>.</p>
<dt><code>&#8211;new-document</code></p>
<dd> Create a new document in an existing instance of <code>pluma</code>, on the last Pluma window that had focus.</p>
<dt><code>+[num]</code></p>
<dd> For the first file, go to the line specified by &quot;num&quot; (do not insert a space between the &quot;+&quot; sign and the number). If &quot;num&quot; is missing, go to the last line.</p>
<dt><code>&#8211;list-encodings</code></p>
<dd> Display list of possible values for the encoding option and exit</p>
<dt><code>&#8211;version</code></p>
<dd> Output version information and exit</p>
<dt><code>-?, -h, &#8211;help</code></p>
<dd> Print standard command line options.</p>
<dt><code>&#8211;help-all</code></p>
<dd> Print all command line options.</dl>
<p> This program also accepts the standard GTK options. </p>
<h2>EXAMPLES</h2>
<p> <code>pluma &#8211;encoding WINDOWS-1252 <a href="ftp://ftp.kernel.org/pub/linux/kernel/README">ftp://ftp.kernel.org/pub/linux/kernel/README</a></code></p>
<dl>
<dt>
<dd> Open the Linux Kernel README file from kernel.org&#8217;s FTP server using Windows-1252 character encoding.</dl>
<p> <code>pluma +156 <a rel="nofollow" href="http://mate-desktop.org/">http://mate-desktop.org/</a></code></p>
<dl>
<dt>
<dd> Open the main web page of mate-desktop.org and jump to line 156.</dl>
<p> <code>pluma &#8211;new-window ~/.bashrc ~/.bash_history</code></p>
<dl>
<dt>
<dd> Open the current users .bashrc and .bash_history files in a new Pluma window. </p>
</dl>
<h2>BUGS</h2>
<h3>Should you encounter any bugs, they may be reported at:</h3>
<p> <a rel="nofollow" href="http://github.com/mate-desktop/pluma/issues">http://github.com/mate-desktop/pluma/issues</a></p>
<h2>NOTES</h2>
<p> This version of the Pluma Manual Page was written with Pluma. =)</p>
<h2>AUTHORS</h2>
<h3>This Man Page has been updated/re-written for the MATE Desktop Environment by:</h3>
<p> Adam Erdman &lt;hekel [at] archlinux.info&gt; (2014)</p>
<h2>HISTORY</h2>
<h3>Some portions of this manual were originally written by Gedit&#8217;s previous developers, to accompany it in the GNOME Desktop Environment by:</h3>
<pre><code>
Paolo Maggi&lt;paolo[at] gnome.org&gt;
    Paolo Borelli&lt;pborelli[at] katamail.com&gt;
        James Willcox&lt;jwillcox[at] gnome.org&gt;
            Federico Mena Quintero&lt;federico[at] novell.com&gt;
                Chema Celorio(2000 - 2010)
</code></pre>
<h2>SEE ALSO</h2>
<h3>Pluma documentation can be found from the Help menu, or by pressing the F1 key.</h3>
<p> Further information may also be available at: <a rel="nofollow" href="http://wiki.mate-desktop.org/docs">http://wiki.mate-desktop.org/docs</a> </p>
<h2>Index</h2>
