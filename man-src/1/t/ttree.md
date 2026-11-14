---
title: "ttree(1)"
name: "ttree"
section: "1"
letter: "t"
url: "/docs/linux/man/1-ttree/"
---

<h2 class="name">NAME</h2>
 

 Template::Tools::ttree - Process entire directory trees of templates 

<h2>SYNOPSIS</h2>

 <pre><code>
ttree[options][files]
</code></pre>

<h2>DESCRIPTION</h2>

 The <i>ttree</i> script is used to process entire directory trees containing template files. The resulting output from processing each file is then written to a corresponding file in a destination directory. The script compares the modification times of source and destination files (where they already exist) and processes only those files that have been modified. In other words, it is the equivalent of 'make' for the Template Toolkit. 

 It supports a number of options which can be used to configure behaviour, define locations and set Template Toolkit options. The script first reads the <i>.ttreerc</i> configuration file in the <font SIZE="-1">HOME</font> directory, or an alternative file specified in the <font SIZE="-1">TTREERC</font> environment variable. Then, it processes any command line arguments, including any additional configuration files specified via the <tt>&quot;-f&quot;</tt> (file) option.

<h3>The <i>.ttreerc</i> Configuration File</h3>

 When you run <i>ttree</i> for the first time it will ask you if you want it to create a <i>.ttreerc</i> file for you. This will be created in your home directory. 

 <pre>
    $ ttree
    Do you want me to create a sample '.ttreerc' file for you?
    (file: /home/abw/.ttreerc)   [y/n]: y
    /home/abw/.ttreerc created.  Please edit accordingly and re-run ttree
</pre> 

 The purpose of this file is to set any <i>global</i> configuration options that you want applied <i>every</i> time <i>ttree</i> is run. For example, you can use the <tt>&quot;ignore&quot;</tt> and <tt>&quot;copy&quot;</tt> option to provide regular expressions that specify which files should be ignored and which should be copied rather than being processed as templates. You may also want to set flags like <tt>&quot;verbose&quot;</tt> and <tt>&quot;recurse&quot;</tt> according to your preference. 

 A minimal <i>.ttreerc</i>: 

 <pre>
    # ignore these files
    ignore = \b(CVS|RCS)\b
    ignore = ^#
    ignore = ~$
    # copy these files
    copy   = \.(gif|png|jpg|pdf)$ 
    # recurse into directories
    recurse
    # provide info about what's going on
    verbose
</pre> 

 In most cases, you'll want to create a different <i>ttree</i> configuration file for each project you're working on. The <tt>&quot;cfg&quot;</tt> option allows you to specify a directory where <i>ttree</i> can find further configuration files. 

 <pre>
    cfg = /home/abw/.ttree
</pre> 

 The <tt>&quot;-f&quot;</tt> command line option can be used to specify which configuration file should be used. You can specify a filename using an absolute or relative path: 

 <pre>
    $ ttree -f /home/abw/web/example/etc/ttree.cfg
    $ ttree -f ./etc/ttree.cfg
    $ ttree -f ../etc/ttree.cfg
</pre> 

 If the configuration file does not begin with <tt>&quot;/&quot;</tt> or <tt>&quot;.&quot;</tt> or something that looks like a MS-DOS absolute path (e.g. <tt>&quot;C:\\etc\\ttree.cfg&quot;</tt>) then <i>ttree</i> will look for it in the directory specified by the <tt>&quot;cfg&quot;</tt> option. 

 <pre>
    $ ttree -f test1          # /home/abw/.ttree/test1
</pre> 

 The <tt>&quot;cfg&quot;</tt> option can only be used in the <i>.ttreerc</i> file. All the other options can be used in the <i>.ttreerc</i> or any other <i>ttree</i> configuration file. They can all also be specified as command line options. 

 Remember that <i>.ttreerc</i> is always processed <i>before</i> any configuration file specified with the <tt>&quot;-f&quot;</tt> option. Certain options like <tt>&quot;lib&quot;</tt> can be used any number of times and accumulate their values. 

 For example, consider the following configuration files: 

 <i>/home/abw/.ttreerc</i>: 

 <pre>
    cfg = /home/abw/.ttree
    lib = /usr/local/tt2/templates
</pre> 

 <i>/home/abw/.ttree/myconfig</i>: 

 <pre>
    lib = /home/abw/web/example/templates/lib
</pre> 

 When <i>ttree</i> is invoked as follows: 

 <pre>
    $ ttree -f myconfig
</pre> 

 the <tt>&quot;lib&quot;</tt> option will be set to the following directories: 

 <pre>
    /usr/local/tt2/templates
    /home/abw/web/example/templates/lib
</pre> 

 Any templates located under <i>/usr/local/tt2/templates</i> will be used in preference to those located under <i>/home/abw/web/example/templates/lib</i>. This may be what you want, but then again, it might not. For this reason, it is good practice to keep the <i>.ttreerc</i> as simple as possible and use different configuration files for each <i>ttree</i> project.

<h3>Directory Options</h3>

 The <tt>&quot;src&quot;</tt> option is used to define the directory containing the source templates to be processed. It can be provided as a command line option or in a configuration file as shown here: 

 <pre>
    src = /home/abw/web/example/templates/src
</pre> 

 Each template in this directory typically corresponds to a single web page or other document. 

 The <tt>&quot;dest&quot;</tt> option is used to specify the destination directory for the generated output. 

 <pre>
    dest = /home/abw/web/example/html
</pre> 

 The <tt>&quot;lib&quot;</tt> option is used to define one or more directories containing additional library templates. These templates are not documents in their own right and typically comprise of smaller, modular components like headers, footers and menus that are incorporated into pages templates. 

 <pre>
    lib = /home/abw/web/example/templates/lib
    lib = /usr/local/tt2/templates
</pre> 

 The <tt>&quot;lib&quot;</tt> option can be used repeatedly to add further directories to the search path. 

 A list of templates can be passed to <i>ttree</i> as command line arguments. 

 <pre>
    $ ttree foo.html bar.html
</pre> 

 It looks for these templates in the <tt>&quot;src&quot;</tt> directory and processes them through the Template Toolkit, using any additional template components from the <tt>&quot;lib&quot;</tt> directories. The generated output is then written to the corresponding file in the <tt>&quot;dest&quot;</tt> directory. 

 If <i>ttree</i> is invoked without explicitly specifying any templates to be processed then it will process every file in the <tt>&quot;src&quot;</tt> directory. If the <tt>&quot;-r&quot;</tt> (recurse) option is set then it will additionally iterate down through sub-directories and process and other template files it finds therein. 

 <pre>
    $ ttree -r
</pre> 

 If a template has been processed previously, <i>ttree</i> will compare the modification times of the source and destination files. If the source template (or one it is dependant on) has not been modified more recently than the generated output file then <i>ttree</i> will not process it. The <i>-a</i> (all) option can be used to force <i>ttree</i> to process all files regardless of modification time. 

 <pre>
    $ tree -a
</pre> 

 Any templates explicitly named as command line argument are always processed and the modification time checking is bypassed.

<h3>File Options</h3>

 The <tt>&quot;ignore&quot;</tt>, <tt>&quot;copy&quot;</tt> and <tt>&quot;accept&quot;</tt> options are used to specify Perl regexen to filter file names. Files that match any of the <tt>&quot;ignore&quot;</tt> options will not be processed. Remaining files that match any of the <tt>&quot;copy&quot;</tt> regexen will be copied to the destination directory. Remaining files that then match any of the <tt>&quot;accept&quot;</tt> criteria are then processed via the Template Toolkit. If no <tt>&quot;accept&quot;</tt> parameter is specified then all files will be accepted for processing if not already copied or ignored. 

 <pre>
    # ignore these files
    ignore = \b(CVS|RCS)\b
    ignore = ^#
    ignore = ~$
    # copy these files
    copy   = \.(gif|png|jpg|pdf)$ 
    # accept only .tt2 templates
    accept = \.tt2$
</pre> 

 The <tt>&quot;suffix&quot;</tt> option is used to define mappings between the file extensions for source templates and the generated output files. The following example specifies that source templates with a <tt>&quot;.tt2&quot;</tt> suffix should be output as <tt>&quot;.html&quot;</tt> files: 

 <pre>
    suffix tt2=html
</pre> 

 Or on the command line, 

 <pre>
    --suffix tt2=html
</pre> 

 You can provide any number of different suffix mappings by repeating this option. 

 The <tt>&quot;binmode&quot;</tt> option is used to set the encoding of the output file. For example use <tt>&quot;--binmode=:utf8&quot;</tt> to set the output format to unicode.

<h3>Template Dependencies</h3>

 The <tt>&quot;depend&quot;</tt> and <tt>&quot;depend_file&quot;</tt> options allow you to specify how any given template file depends on another file or group of files. The <tt>&quot;depend&quot;</tt> option is used to express a single dependency. 

 <pre>
  $ ttree --depend foo=bar,baz
</pre> 

 This command line example shows the <tt>&quot;--depend&quot;</tt> option being used to specify that the <i>foo</i> file is dependant on the <i>bar</i> and <i>baz</i> templates. This option can be used many time on the command line: 

 <pre>
  $ ttree --depend foo=bar,baz --depend crash=bang,wallop
</pre> 

 or in a configuration file: 

 <pre>
  depend foo=bar,baz
  depend crash=bang,wallop
</pre> 

 The file appearing on the left of the <tt>&quot;=&quot;</tt> is specified relative to the <tt>&quot;src&quot;</tt> or <tt>&quot;lib&quot;</tt> directories. The file(s) appearing on the right can be specified relative to any of these directories or as absolute file paths. 

 For example: 

 <pre>
  $ ttree --depend foo=bar,/tmp/baz
</pre> 

 To define a dependency that applies to all files, use <tt>&quot;*&quot;</tt> on the left of the <tt>&quot;=&quot;</tt>. 

 <pre>
  $ ttree --depend *=header,footer
</pre> 

 or in a configuration file: 

 <pre>
  depend *=header,footer
</pre> 

 Any templates that are defined in the <tt>&quot;pre_process&quot;</tt>, <tt>&quot;post_process&quot;</tt>, <tt>&quot;process&quot;</tt> or <tt>&quot;wrapper&quot;</tt> options will automatically be added to the list of global dependencies that apply to all templates. 

 The <tt>&quot;depend_file&quot;</tt> option can be used to specify a file that contains dependency information. 

 <pre>
    $ ttree --depend_file=/home/abw/web/example/etc/ttree.dep
</pre> 

 Here is an example of a dependency file: 

 <pre>
   # This is a comment. It is ignored.
  
   index.html: header footer menubar 
  
   header: titlebar hotlinks
  
   menubar: menuitem
  
   # spanning multiple lines with the backslash
   another.html: header footer menubar \
   sidebar searchform
</pre> 

 Lines beginning with the <tt>&quot;#&quot;</tt> character are comments and are ignored. Blank lines are also ignored. All other lines should provide a filename followed by a colon and then a list of dependant files separated by whitespace, commas or both. Whitespace around the colon is also optional. Lines ending in the <tt>&quot;\&quot;</tt> character are continued onto the following line. 

 Files that contain spaces can be quoted. That is only necessary for files after the colon (':'). The file before the colon may be quoted if it contains a colon. 

 As with the command line options, the <tt>&quot;*&quot;</tt> character can be used as a wildcard to specify a dependency for all templates. 

 <pre>
    * : config,header
</pre>

<h3>Template Toolkit Options</h3>

 <i>ttree</i> also provides access to the usual range of Template Toolkit options. For example, the <tt>&quot;--pre_chomp&quot;</tt> and <tt>&quot;--post_chomp&quot;</tt> <i>ttree</i> options correspond to the <tt>&quot;PRE_CHOMP&quot;</tt> and <tt>&quot;POST_CHOMP&quot;</tt> options. 

 Run <tt>&quot;ttree -h&quot;</tt> for a summary of the options available.

<h2>AUTHORS</h2>

 Andy Wardley &lt;abw [at] andywardley.com&gt; 

 &lt;<a rel="nofollow" HREF="http://www.andywardley.com/">http://www.andywardley.com/</a>&gt; 

 With contributions from Dylan William Hardison (support for dependencies), Bryce Harrington (<tt>&quot;absolute&quot;</tt> and <tt>&quot;relative&quot;</tt> options), Mark Anderson (<tt>&quot;suffix&quot;</tt> and <tt>&quot;debug&quot;</tt> options), Harald Joerg and Leon Brocard who gets everywhere, it seems.

<h2>VERSION</h2>

 2.68, distributed as part of the Template Toolkit version 2.19, released on 27 April 2007.

<h2>COPYRIGHT</h2>

 <pre>
  Copyright (C) 1996-2007 Andy Wardley.  All Rights Reserved.
</pre> 

 This module is free software; you can redistribute it and/or modify it under the same terms as Perl itself.

<h2>SEE ALSO</h2>

 tpage 

<h2>Index</h2>



<dt><a HREF="#lbAJ">AUTHORS</a>
<dd>
<dt><a HREF="#lbAK">VERSION</a>
<dd>
<dt><a HREF="#lbAL">COPYRIGHT</a>
<dd>
<dt><a HREF="#lbAM">SEE ALSO</a>
<dd></dl>
