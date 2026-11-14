---
title: "indexmaker(1)"
name: "indexmaker"
section: "1"
letter: "i"
url: "/docs/linux/man/1-indexmaker/"
description: "indexmaker – Creates index files for mrtg web sites (mrtg-2.17.4)"
---

<h2 class="name">NAME</h2>
<p> indexmaker &#8211; Creates index files for mrtg web sites (mrtg-2.17.4) </p>
<h2>SYNOPSIS</h2>
<p> indexmaker [options] mrtg.cfg [other.cfg &#8230;]</p>
<h2>OPTIONS</h2>
<pre><code>
 --output=filename   set output filename (default: stdout)
 --filter title=~regexp  select targets by matching regexp against titles
 --filter pagetop=~regexp  select targets by matching regexp against pagetop
 --filter name=~regexp  select targets by matchin regexp against name
 --addhead=text      insert this text between &lt;/TITLE&gt; and &lt;/HEAD&gt;
 --title=text        set title of generated index file
 --subtitle=text     add a subtitle to the generated index file
 --bodyopt=text      set body tag options
 --headlevel=number  use &lt;Hnumber&gt; at top of page (default: 1)
 --pagetop=text      insert this text between &lt;BODY&gt; and &lt;H1&gt;...&lt;/H1&gt;
 --pageend=text      insert this text after the main body
 --pagetopend=text   use this text for pagetop or pageend if undefined
 --nolegend          do not add the Mrtg legend at the end of the page
 --columns=number    show graphs in a table with x columns (default: 2)
 --perhost           show graphs of the same host on a row
 --compact           try to make a vertically more compact page
 --optlog            log the used command line in the page (default: log)
 --sort=title        sort graphs by title
 --sort=name         sort graphs by their name
 --sort=descr        sort graphs by their description
 --sort=original     leave as is (default)
 --enumerate         add a sequence number to the title of each graph
 --picfirst          place pictures before text (default: text first)
 --width=number      set width of graphs (default: not set)
 --height=number
 --sidebyside        place text / pictures side by side (default: above/below)
 --bold              use bold text (default: bold)
 --clicktext         make the text link to the inner page (like the image)
 --show=day          pick which graph to show in the index (default)
 --show=week
 --show=month
 --show=year
 --show=none
 --section=h1        h1 tag from pagetop as section heading (default)
 --section=title     title as section headings for graphs
 --section=name      graph name as section heading
 --section=descr     graph description as section heading
 --section=portname  port name entry in pagetop as section heading
 --sectionhost       Try to prepend the host to the section heading if missing
 --rrdviewer=path    path to rrdviewer (default: /cgi-bin/14all.cgi)
 --icondir=path      path to icondir
 --prefix=path       path from the location of the index.html to the graphs
 --headeradd=string  add string to the html page header
 --autoprefix        try to set prefix automatically
 
 --&lt;opt&gt;-file=file   read string argument for option &lt;opt&gt; from file
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>Indexmaker</code> can create web pages which display the status of an array of mrtg interface status pages.</p>
<dl>
<dt><code>&#8211;output</code> <i>filename</i></p>
<dd> set output filename (default: stdout)</p>
<dt><code>&#8211;filter</code> (<code>title</code>|<code>pagetop</code>|<code>name</code>)(<code>=~</code>|<code>!~</code>)<i>regexp</i></p>
<dd> Several filters may get set. Each filter can match agains the contents of a specific section of the mrtg config file. <code>Name</code> refers to the bit in square brackets (option[name]: bla). </p>
<p> Depending on the match operator chosen (<code>=~</code> or <code>!~</code>) the match will be positive or negative. </p>
<p> Note that some shells consider <code>!</code> a special character. It may be necessary to type <code>\!~</code> instead.</p>
<dt><code>&#8211;title</code> <i>text</i></p>
<dd> Set title of generated index file (default: regexp)</p>
<dt><code>&#8211;bodyopt</code> <i>text</i></p>
<dd> The value of this argument gets appended to the &lt;<font SIZE="-1">BODY</font>&gt; tag. This allows you to set document colors. By default this option is set to </p>
<pre>
 bgcolor=&quot;#ffffff&quot; text=&quot;#000000&quot; link=&quot;#000000&quot; vlink=&quot;#000000&quot; alink=&quot;#000000&quot;
</pre>
<dt><code>&#8211;columns</code> <i>number</i></p>
<dd> Display graphs in a table with <i>number</i> columns (default: 2)</p>
<dt><code>&#8211;sort</code> <code>title</code>|<code>name</code>|<code>descr</code>|<code>original</code></p>
<dd> Sort the graphs in the page either by <code>title</code>, by <code>name</code>, by interface <code>descr</code>iption, or leave them as is.</p>
<dt><code>&#8211;enumerate</code></p>
<dd> Add a sequence number to the title of each graph</p>
<dt><code>&#8211;width</code> <i>number</i></p>
<dd> Set width of graphs</p>
<dt><code>&#8211;height</code> <i>number</i></p>
<dd> Set the height of the graphs</p>
<dt><code>&#8211;show</code> <code>day</code>|<code>week</code>|<code>month</code>|<code>year</code>|<code>none</code></p>
<dd> Select which graph to show in the index page. You can supress images completely with <code>&#8211;show=none</code>.</p>
<dt><code>&#8211;section</code> <code>h1</code>|<code>title</code>|<code>name</code>|<code>description</code>|<code>portname</code></p>
<dd> Select what to use as the title for each graph in the page. <code>h1</code> is the H1 section from pagetop, <code>title</code> is the graph title, <code>name</code> is the bit in square brackets (option[name]: bla), and <code>descr</code> or <code>description</code> is the text from the Description field of the PageTop (the Cisco description text if it&#8217;s available, otherwise just the interface description). <code>portname</code> is the <tt>&quot;Port Name:&quot;</tt> from pagetop.</p>
<dt><code>&#8211;sectionhost</code></p>
<dd> Extract the hostname from the target line (this does not work if the target is a mathematial expression). Prepend the hostname (and a colon) to the section if not already present.</p>
<dt><code>&#8211;rrdviewer</code> <i>path</i></p>
<dd> If you have set the <code>LogFormat: rrdtool</code> property in the mrtg.cfg file, the index will take this into account. The only thing you must tell it is the path to your grapher cgi. (default: /cgi-bin/14all.cgi)</p>
<dt><code>&#8211;prefix</code> <i>path</i></p>
<dd> By default we assume that the file generated by indexmaker is stored in <i>WorkDir</i>. If you want to store it somewhere else, specify how to reach <i>WorkDir</i> from the place where the Index is stored. Note that you have to use &#8216;/&#8217; as path separator as this will be used in urls. Speaking of which, you can even enter a whole url.</p>
<dt><code>&#8211;autoprefix</code> <i>path</i></p>
<dd> Requires &#8211;output. Try to generate the prefix automatically by comparision of the path to the output file set with &#8211;output and the Htmldir set in the configuration files. Particulary useful when multiple configuration files are specified, with different Htmldir settings.</p>
<dt><code>&#8211;optlog</code></p>
<dd> Default is logging in the generated page the command line, suppress with &#8211;nooptlog . Useful if the commandline contains a complex &#8211;pagetop=string which could confuse simple browsers.</p>
<dt><code>&#8211;someoption-file</code> <i>filename</i></p>
<dd> For any someoption which takes a <i>string</i> as parameter you can read the string from a file by adding &lt;-file&gt; to the option keyword. The whole content of the file will be read and used as the <i>string</i>. The file must exist.</dl>
<h2>AUTHOR</h2>
<p> Tobias Oetiker &lt;tobi [at] oetiker.ch&gt;</p>
<h2>LICENSE</h2>
<p> <font SIZE="-1">GNU</font> General Public License</p>
<h2>COPYRIGHT</h2>
<p> 2000-2001 Tobias Oetiker &lt;tobi [at] oetiker.ch&gt; </p>
<h2>Index</h2>
