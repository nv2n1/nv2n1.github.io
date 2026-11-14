---
title: "ctangle(1)"
name: "ctangle"
section: "1"
letter: "c"
url: "/docs/linux/man/1-ctangle/"
---

<h2 class="name">NAME</h2>
 

 

 ctangle, cweave - translate CWEB to C/C++ and/or TeX 

<h2>SYNOPSIS</h2>

 

 ctangle [options] webfile[.w] [{changefile[.ch]|-} [outfile[.c]]] 

 cweave [options] webfile[.w] [{changefile[.ch]|-} [outfile[.tex]]]

<h2>DESCRIPTION</h2>

 

 The ctangle program converts a CWEB source document into a C/C++&nbsp;program that may be compiled in the usual way. The output file includes #line specifications so that debugging can be done in terms of the CWEB source file. 

 The cweave program converts the same CWEB file into a TeX file that may be formatted and printed in the usual way. It takes appropriate care of typographic details like page layout and the use of indentation, italics, boldface, etc., and it supplies extensive cross-index information that it gathers automatically. 

 CWEB allows you to prepare a single document containing all the information that is needed both to produce a compilable C/C++&nbsp;program and to produce a well-formatted document describing the program in as much detail as the writer may desire. The user of CWEB ought to be familiar with TeX as well as C/C++.

<h2>USAGE</h2>

 

 The command line should have one, two, or three names on it. The first is taken as the CWEB input file (and .w is added if there is no extension). If there is a second name, it is a change file (and .ch is added if there is no extension). The change file overrides parts of the CWEB file, as described in the documentation. If there is a third name, it overrides the default name of the output file, which is ordinarily the same as the name of the input file (but on the current directory) with the extension .tex. If you just want to change the output file name, but don't have a change file to apply, you can use `-' as the second argument.

<h2>DIFFERENCES TO ORIGINAL CWEB</h2>

 

 CWEBbin tries hard to be a drop-in replacement for CWEB, so in general you should not notice any differences in invoking the programs nor in the resulting output. There are, however, a few differences worth noting:
<dl>
<dt>&bull;
<dd> Options --help, --quiet, --verbose, --version, and flags -c, -i, -o, and +lX are new in CWEBbin and TeX Live.
<dt>&bull;
<dd> Option +lX is accompanied by several wrapper files for cwebmac.tex with translated captions for German (+ld), French (+lf), and Italian (+li).
<dt>&bull;
<dd> CWEB in TeX Live operates silently by default (as of 2019); use the --verbose option to get the original behavior.
<dt>&bull;
<dd> File lookup with the environment variable CWEBINPUTS is extended to permit several, colon-separated, paths; see ENVIRONMENT below.
<dt>&bull;
<dd> If properly configured, the main programs ctangle and cweave are localized with the "GNU gettext utilities".</dl>

<h2>OPTIONS</h2>

 

 Options on the command line may be either turned off with `-' (if they are on by default) or turned on with `+' (if they are off by default). In fact, the options are processed from left to right, so a sequence like --verbose -h will only show the banner line (+b) and the progress report (+p), but leave out the happy message (-h). 

 The first batch of options are common to both ctangle and cweave:
<dl>
<dt>&bull;
<dd> +b: print banner line on terminal
<dt>&bull;
<dd> +h: print success message on completion
<dt>&bull;
<dd> +p: print progress report messages
<dt>&bull;
<dd> +q/-q: shortcut for -bhp; also --quiet (default)
<dt>&bull;
<dd> +v/-v: shortcut for +bhp; also --verbose
<dt>&bull;
<dd> -c: ignore temporary output irrespective of changes
<dt>&bull;
<dd> +s: print usage statistics
<dt>&bull;
<dd> --help: display help message and exit
<dt>&bull;
<dd> --version: output version information and exit</dl>
 

 There is one other option applicable to ctangle only:
<dl>
<dt>&bull;
<dd> +k: keep separators in numeric literals in the output</dl>
 

 There are seven other options applicable to cweave only:
<dl>
<dt>&bull;
<dd> -e: do not enclose C/C++&nbsp;material in \PB{...}
<dt>&bull;
<dd> -f: do not force a newline after every C/C++&nbsp;statement in output
<dt>&bull;
<dd> -i: suppress indentation of parameter declarations
<dt>&bull;
<dd> -o: suppress separation of declarations and statements
<dt>&bull;
<dd> -x: omit indices, section names, table of contents
<dt>&bull;
<dd> +lX/-lX: use macros for language X as of Xcwebmac.tex
<dt>&bull;
<dd> +t: treat typename in a template like typedef</dl>

<h2>ENVIRONMENT</h2>

 

 The environment variable CWEBINPUTS is used to search for the input files, or the system default if CWEBINPUTS is not set. See <a HREF="/docs/linux/man/1-tex/">tex</a>(1) for the details of the searching. To avoid conflicts with other programs that also use the CWEBINPUTS environment, you can be more specific and use CWEBINPUTS_cweb for special requirements in CWEB. 

 If prepared for NLS support, ctangle and cweave use the environment variable TEXMFLOCALEDIR to configure the parent directory where the "GNU gettext utilities" search for translation catalogs. 

 These variables are preconfigured in TeX Live's texmf.cnf.

<h2>FILES</h2>

 

 The location of the files mentioned below varies from system to system. Use the kpsewhich utility to find their locations.
<dl>
<dt>&bull;
<dd> cwebmac.tex: The default TeX macros \input in the first line of the cweave output file.
<dt>&bull;
<dd> cwebman.tex: The CWEB user manual, available in PDF from CTAN (<a rel="nofollow" HREF="https://ctan.org/pkg/cweb">https://ctan.org/pkg/cweb</a>).</dl>

<h2>SEE ALSO</h2>

<dl>
<dt>&bull;
<dd> The CWEB System of Structured Documentation: by Donald E. Knuth and Silvio Levy (hardcopy version of cwebman.tex and the source code listings of common.w, ctangle.w, and cweave.w).
<dt>&bull;
<dd> Literate Programming: by D. E. Knuth.
<dt>&bull;
<dd> Weaving a Program: by Wayne Sewell.</dl>
 

 <a HREF="/docs/linux/man/1-cweb/">cweb</a>(1), <a HREF="/docs/linux/man/1-tex/">tex</a>(1), <a HREF="/docs/linux/man/1-cc/">cc</a>(1)

<h2>AUTHORS</h2>

 

 Don Knuth wrote WEB for TeX and Pascal. 

 Silvio Levy designed and developed CWEB by adapting the WEB conventions to C and by recoding everything in CWEB. Knuth began using CWEB and made further refinements. 

 Many other helpers are acknowledged in the CWEB manual. 

 Contemporary development on <a rel="nofollow" HREF="https://github.com/ascherer/cweb.">https://github.com/ascherer/cweb.</a> 

<h2>Index</h2>


