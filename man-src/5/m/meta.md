---
title: "meta(5)"
name: "meta"
section: "5"
letter: "m"
url: "/docs/linux/man/5-meta/"
---

META - [File that specifies metainformation of OCaml packages]

<h2>Grammar</h2>

<pre>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>metafile ::=&nbsp;<wbr>entry*
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>entry ::=&nbsp;<wbr>assignment | addition | subpackage
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>subpackage ::=&nbsp;<wbr>&quot;package&quot;&nbsp;<wbr>pkgname&nbsp;<wbr>'('&nbsp;<wbr>metafile&nbsp;<wbr>')'
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>assignment ::=&nbsp;<wbr>variable_name&nbsp;<wbr>[&nbsp;<wbr>formal_predicates&nbsp;<wbr>]&nbsp;<wbr>'='&nbsp;<wbr>&nbsp;<wbr>value
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>addition ::=&nbsp;<wbr>variable_name&nbsp;<wbr>[&nbsp;<wbr>formal_predicates&nbsp;<wbr>]&nbsp;<wbr>'+='&nbsp;<wbr>value
<br>
formal_predicates ::=&nbsp;<wbr>'('&nbsp;<wbr>formal_predicate&nbsp;<wbr>{&nbsp;<wbr>','&nbsp;<wbr>formal_predicate&nbsp;<wbr>}&nbsp;<wbr>')'
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>variable_name ::=&nbsp;<wbr>name
<br>
&nbsp;<wbr>formal_predicate ::=&nbsp;<wbr>name |&nbsp;<wbr>'-'&nbsp;<wbr>name
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>name ::=&nbsp;<wbr>[&nbsp;<wbr>'A'-'Z'&nbsp;<wbr>'a'-'z'&nbsp;<wbr>'0'-'9'&nbsp;<wbr>'_'&nbsp;<wbr>'.'&nbsp;<wbr>]+
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>pkgname ::=&nbsp;<wbr>'&quot;'&nbsp;<wbr>(character but not&nbsp;<wbr>'.')*&nbsp;<wbr>'&quot;'
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>value ::=&nbsp;<wbr>'&quot;'&nbsp;<wbr>character*&nbsp;<wbr>'&quot;'</pre>

<h2>Description</h2>

If a package directory contains a file with the fixed name &quot;META&quot; it is interpreted as described here. The file is a sequence of entries following the given grammar; every entry defines a variable under a certain condition given by the list of formal predicates, or it introduces a subpackage.

 There is a list of predefined variables and a list of standard predicates. These variables define: required packages, description, version information, directories, archive files, and linker options. The predicates denote circumstances of the application of the variables: whether the bytecode or the native compiler is used, if there is a toploop compiled in, details of multi-threading execution, details of profiling.

<h2>Details Of The File Format</h2>

The file consists of a sequence of entries which must be formed as the grammar prescribes. The lexical tokens are names, values, and interpunctuation like '(', ',' and so on. Note that linefeeds do not play a special role, i.e. an entry definition may be given in more than one line, or several definitions may occur on a single line. There may be comments which begin with '#' and run until the end of the line.

 Names are sequences of the characters A-Z, a-z, 0-9, or _. Names containing capital letters and names beginning with digits are allowed but not recommended.

 Values are enclosed between double quotes. Values may contain any character. The characters &quot; and \ must be preceded by backslashes. 

 Package names must not contain the '.' character because it is used as delimiter of compound names.

<h2>Main Packages And Subpackages</h2>

The outermost variable assignments and additions belong to the main package. The name of the main package is not defined within META; it is either the name of the directory containing META or the suffix of the META file (if the name of the META file is formed like
