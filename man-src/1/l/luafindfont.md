---
title: "luafindfont(1)"
name: "luafindfont"
section: "1"
letter: "l"
url: "/docs/linux/man/1-luafindfont/"
---

<h2 class="name">NAME</h2>
 

 luafindfont - retrieve font informations of all installed system and TeX fonts. 

<h2>SYNOPSIS</h2>

 luafindfont [options] &lt;fontname&gt;

<h2>DESCRIPTION</h2>

 This command lists informations about installed otf|ttf|ttc fonts, installed by the system and by the TeX distribution

<h2>OPTIONS</h2>

<dl>
<dt>-h,--help
<dd> obvious ... :-)
<dt>-o,--otfinfo
<dd> Use the program otfinfo for the font with the given number. The number can be followed by an optional argument for otfinfo, e.g. -o 2f, list all features for font no 2. Without an additional character, otfinfo is called with -i
<dt>-i,--info
<dd> List the given fontstyles (regular, bold, italic, bolditalic) for the font with the given number
<dt>-v,--verbose
<dd> Give more informations, by now only -v works
<dt>-m,--max_string
<dd> The maximum of the stringlength of the full path of fonts
<dt>-n,--nosymbolicnames
<dd> The fontlist contains only fontfile and fontpath
<dt>&lt;fontname&gt;
<dd> Can be a substring, e.g. times, or a combination of two substrings which act like a boolean and, e.g. &quot;times &amp; bold&quot; (must be in quotes). All strings are not case sensitive. Upper and lowercase can be mixed.</dl>

<h2>EXAMPLES</h2>

 

 $ luafindfont libertinssans 

 

 Lists all fonts which have names or part of like libertinussans 

 <pre>
We are using Lua 5.3
Check for file /usr/local/texlive/texmf-var/luatex-cache/generic/names/luaotfload-names
 1.    LibertinusSans-Bold.otf libertinussans                          /Users/voss/Library/Fonts/libertinus-fonts/LibertinusSans-Bold.otf
 2.    LibertinusSans-Bold.otf libertinussans  /usr/local/texlive/texmf-d...onts/opentype/public/libertinus-fonts/LibertinusSans-Bold.otf
 3.  LibertinusSans-Italic.otf libertinussans                        /Users/voss/Library/Fonts/libertinus-fonts/LibertinusSans-Italic.otf
 4.  LibertinusSans-Italic.otf libertinussans  /usr/local/texlive/texmf-d...ts/opentype/public/libertinus-fonts/LibertinusSans-Italic.otf
 5. LibertinusSans-Regular.otf libertinussans                       /Users/voss/Library/Fonts/libertinus-fonts/LibertinusSans-Regular.otf
 6. LibertinusSans-Regular.otf libertinussans  /usr/local/texlive/texmf-d...s/opentype/public/libertinus-fonts/LibertinusSans-Regular.otf
</pre> 

 

 The --otfinfo: 

 $ luafindfont -o 3 libertinussans 

 

 This produces the following output: 

 <pre><code>
We are using Lua 5.3
Check for file /usr/local/texlive/texmf-var/luatex-cache/generic/names/luaotfload-names
 1.    LibertinusSans-Bold.otf libertinussans                          /Users/voss/Library/Fonts/libertinus-fonts/LibertinusSans-Bold.otf
 2.    LibertinusSans-Bold.otf libertinussans  /usr/local/texlive/texmf-d...onts/opentype/public/libertinus-fonts/LibertinusSans-Bold.otf
 3.  LibertinusSans-Italic.otf libertinussans                        /Users/voss/Library/Fonts/libertinus-fonts/LibertinusSans-Italic.otf
 4.  LibertinusSans-Italic.otf libertinussans  /usr/local/texlive/texmf-d...ts/opentype/public/libertinus-fonts/LibertinusSans-Italic.otf
 5. LibertinusSans-Regular.otf libertinussans                       /Users/voss/Library/Fonts/libertinus-fonts/LibertinusSans-Regular.otf
 6. LibertinusSans-Regular.otf libertinussans  /usr/local/texlive/texmf-d...s/opentype/public/libertinus-fonts/LibertinusSans-Regular.otf
Run otfinfo:3
Family:              Libertinus Sans
Subfamily:           Italic
Full name:           Libertinus Sans Italic
PostScript name:     LibertinusSans-Italic
Version:             Version 7.020;
RELEASE
Unique ID : 1.000;
QUE;
LibertinusSans - Italic
                     Designer : Philipp H.Poll,
    Khaled Hosny
        Manufacturer : Caleb Maclennan
                           Vendor URL : https :                       // github.com/alerque/libertinus
                                                License URL : https : // scripts.sil.org/OFL
                                                                      License Description : This Font Software is licensed under the SIL Open Font License,
                                                                                            Version 1.1 Vendor ID : QUE
</code></pre> 

 

 The --nosymbilcnames: 

 $ luafindfont -n 

 

 This produces the following output: 

 <pre>
bash-3.2$ luafindfont -n minion
We are using Lua 5.3
Check for file /usr/local/texlive/texmf-var/luatex-cache/generic/names/luaotfload-names
 Nr.                 Fontname                                   Path
   1.      MinionMath-Bold.otf  /Users/voss/Library/Fonts/MinionMath/
   2.   MinionMath-Regular.otf  /Users/voss/Library/Fonts/MinionMath/
   3.       MinionPro-Bold.otf   /Users/voss/Library/Fonts/MinionPro/
   4.     MinionPro-BoldCn.otf   /Users/voss/Library/Fonts/MinionPro/
   5.   MinionPro-BoldCnIt.otf   /Users/voss/Library/Fonts/MinionPro/
   6.     MinionPro-BoldIt.otf   /Users/voss/Library/Fonts/MinionPro/
   7.       MinionPro-Capt.otf   /Users/voss/Library/Fonts/MinionPro/
   8.       MinionPro-Disp.otf   /Users/voss/Library/Fonts/MinionPro/
   9.         MinionPro-It.otf   /Users/voss/Library/Fonts/MinionPro/
  10.     MinionPro-Medium.otf   /Users/voss/Library/Fonts/MinionPro/
  11.   MinionPro-MediumIt.otf   /Users/voss/Library/Fonts/MinionPro/
  12.    MinionPro-Regular.otf   /Users/voss/Library/Fonts/MinionPro/
  13.   MinionPro-Semibold.otf   /Users/voss/Library/Fonts/MinionPro/
  14. MinionPro-SemiboldIt.otf   /Users/voss/Library/Fonts/MinionPro/
  15.       MinionPro-Subh.otf   /Users/voss/Library/Fonts/MinionPro/
</pre> 

<h2>See also</h2>

 See luafindfont-doc.pdf for more details

<h2>BUGS</h2>

 No known bugs.

<h2>AUTHOR</h2>

 Herbert Voß (hvoss [at] tug.org)

<h2>LICENSE</h2>

 Permission is granted to copy, distribute and/or modify this software under the terms of the LaTeX Project Public License, version 1.3. 

 

<h2>Index</h2>


