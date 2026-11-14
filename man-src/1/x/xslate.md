---
title: "xslate(1)"
name: "xslate"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xslate/"
---

<h2 class="name">NAME</h2>
 

 xslate - Process Xslate Templates 

<h2>USAGE</h2>

 <pre><code>
#process paths
$ xslate[options...] target - a-- cache Cache level - t-- type Output content type(html | xml | text) - E-- engine Template engine
    - D-- define Define template variables(e.g.foo = bar) - I-- path Include paths-- version Print version information-- oe-- output_encoding Output encoding(default
                                                                                                                                                              : UTF - 8) -
    M-- module Modules templates will use(e.g.name = sub1, sub2) - e-- eval One line of template code
    - s-- syntax Template syntax(e.g.TTerse) - d-- debug Debugging flags
    - x-- suffix Output suffix mapping(e.g.tx = html)-- ie-- input_encoding Input encoding(default
                                                                                           : UTF - 8) -
    i-- ignore Regular expression the process will ignore
    - c-- cache_dir Directory the cache files will be saved in
    - o-- dest Destination directry
    - w-- verbose Warning level(default : 2)
#one liners, with $ARGV and $ENV
          xslate
    - e 'Hello, &lt;: $ARGV[0] :&gt; world!' Xslate
#=&gt; Hello, Xslate world !
    xslate
    - MDigest::MD5 = md5_hex - e '&lt;: md5_hex($ARGV[0]) :&gt;' 'foo bar'
#=&gt; 327b6f07435811239bc47e1544353273
</code></pre>

<h2>DESCRIPTION</h2>

 The xslate script is used to process entire directory trees containing template files, or to process one liners.

<h2>ARGUMENTS</h2>

<h3>target</h3>

 Specifies the target to be processed by Xslate. 

 If the target is a file, the file is processed, and xslate will exit immediately. If the target is a directory, then the directory is traversed and each file found is processed via xslate.

<h2>AUTHOR</h2>

 Maki, Daisuke (lestrrat) 

 Fuji, Goro (gfx)

<h2>SEE ALSO</h2>

 Text::Xslate 

<h2>Index</h2>


