---
title: "ocamlfind(1)"
name: "ocamlfind"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ocamlfind/"
description: "ocamlfind – [Command-line interface of the Package manager]"
---

<h2>NAME</h2>
<p> ocamlfind &#8211; [Command-line interface of the Package manager]</p>
<h2>SYNOPSIS</h2>
<pre><code>
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
ocamlfind query &amp;nbsp;
[-help | other options] &amp; nbsp;
package_name &amp;nbsp;
...

    &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
or : ocamlfind ocamlc &amp;nbsp;
[-help | other options] &amp; nbsp;
file &amp;nbsp;
...

    &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
or : ocamlfind ocamlcp &amp;nbsp;
[-help | other options] &amp; nbsp;
file &amp;nbsp;
...

    &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
or : ocamlfind ocamlmktop &amp;nbsp;
[-help | other options] &amp; nbsp;
file &amp;nbsp;
...

    &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
or : ocamlfind ocamlopt &amp;nbsp;
[-help | other options] &amp; nbsp;
file &amp;nbsp;
...

    &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
or : ocamlfind ocamldoc &amp;nbsp;
[-help | other options] &amp; nbsp;
file &amp;nbsp;
...

    &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
or : ocamlfind ocamldep &amp;nbsp;
[-help | other options] &amp; nbsp;
file &amp;nbsp;
...

    &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
or : ocamlfind ocamlmklib &amp;nbsp;
[-help | other options] &amp; nbsp;
file &amp;nbsp;
...

    &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
or : ocamlfind ocamlbrowser &amp;nbsp;
[-help | other options]

    &amp; nbsp;
&amp;nbsp;
&amp;nbsp;
or : ocamlfind install &amp;nbsp;
[-help | other options] &amp; nbsp;
package_name &amp;nbsp;
file &amp;nbsp;
...

    &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
or : ocamlfind remove &amp;nbsp;
[-help | other options] &amp; nbsp;
package_name

    &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
or : ocamlfind list &amp;nbsp;
[-describe]

    &amp; nbsp;
&amp;nbsp;
&amp;nbsp;
or : ocamlfind printconf &amp;nbsp;
[&amp;nbsp; variable &amp; nbsp;]

    &amp; nbsp;
&amp;nbsp;
&amp;nbsp;
or : ocamlfind &amp;nbsp;
package / command &amp;nbsp;
arg &amp;nbsp;
...

    Optional toolchain selection by :

    &amp;nbsp;
&amp;nbsp;
ocamlfind - toolchain &amp;nbsp;
name &amp;nbsp;
...</code></pre>
<h2>THE &#8216;query&#8217; SUBCOMMAND</h2>
<h3>Synopsis</h3>
<pre> ocamlfind query&nbsp;<wbr>[&nbsp;<wbr>-predicates&nbsp;<wbr><i>p</i><code>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-format&nbsp;<wbr></code><i>f</i><code>&nbsp;<wbr>|<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-long-format | -l |<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-i-format |<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-l-format |&nbsp;<wbr><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-a-format |<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-o-format |&nbsp;<wbr><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-p-format |</p>
