---
title: "ctwill(1)"
name: "ctwill"
section: "1"
letter: "c"
url: "/docs/linux/man/1-ctwill/"
---

<h2 class="name">NAME</h2>
 

 

 ctwill, ctwill-refsort, ctwill-twinx - translate CWEB to TeX with mini-indexes 

<h2>SYNOPSIS</h2>

 

 ctwill [options] webfile[.w] [{changefile[.ch]|-} [outfile[.tex]]] 

 ctwill-refsort &lt; indexfile.ref &gt; indexfile.sref 

 ctwill-twinx outfile.tex [outfile.tex ...] &gt; index.tex

<h2>DESCRIPTION</h2>

 

 The ctwill program converts a CWEB source document into a TeX file that may be formatted and printed in the usual way. It takes appropriate care of typographic details like page layout and the use of indentation, italics, boldface, etc., and it supplies extensive cross-index information that it gathers automatically. 

 CWEB allows you to prepare a single document containing all the information that is needed both to produce a compilable C/C++&nbsp;program and to produce a well-formatted document describing the program in as much detail as the writer may desire. The user of CWEB ought to be familiar with TeX as well as C/C++.

<h2>USAGE</h2>

 

 The command line should have one, two, or three names on it. The first is taken as the CWEB input file (and .w is added if there is no extension). If there is a second name, it is a change file (and .ch is added if there is no extension). The change file overrides parts of the CWEB file, as described in the documentation. If there is a third name, it overrides the default name of the output file, which is ordinarily the same as the name of the input file (but on the current directory) with the extension .tex. If you just want to change the output file name, but don't have a change file to apply, you can use `-' as the second argument. 

 ctwill is exactly like cweave except that it produces much better documentation, for which you must work much harder. You should run ctwill twice, once to prime the pump and once to get decent answers. Moreover, you must run the output twice through TeX. 

 After tex foo you will have output that looks like final pages except that the entries of mini-indexes won't be alphabetized. The first run produces a weird file called foo.ref. Say ctwill-refsort &lt; foo.ref &gt; foo.sref and then another tex foo will produce alphabetized output. 

 The ctwill-twinx program compiles a master index for a set of related programs that have been processed by ctwill (not by cweave, mind you!). The individual programs should define their names with a line of the form \def\title{NAME}. For your convenience, ctwill-twinx grabs the first "word" in \title and turns it into uppercase form. You should adapt file twinx-startup.tex for the first page of the master index. 

 The mini-indexes list identifiers that are used but not defined on each two-page spread. At the end of each section, ctwill gives TeX a list of identifiers used in that section and information about where they are defined. 

 The current meaning of every identifier is initially \uninitialized. Then ctwill reads the .aux file for your job, if any. 

 Before reading the .aux file, ctwill actually looks for a file called system.bux, which will be read if present. And after foo.aux, a third possibility is foo.bux. The general convention is to put definitions of system procedures such as printf into system.bux, and to put definitions found in specifically foo-ish header files into foo.bux. Like the .aux files, .bux files should contain only @$ specifications. 

 The meaning specified by @$...@&gt; generally has four components: an identifier (followed by space), a program name (enclosed in braces), a section number (followed by space), and a TeX part. 

 A special proofmode is provided so that you can check ctwill's conclusions about cross-references. Run ctwill with the flag +P, and TeX will produce a specially formatted document (without mini-indexes) in which you can check that your specifications are correct. 

 More details how to use ctwill can be found in the first sections of its source code, respectively the change file cweav-twill.ch applicable to the cweave.w source. A complete example with all bells and whistles is described in Mini-Indexes for Literate Programs, pages 225-245 of Knuth's Digital Typography.

<h2>DIFFERENCES TO ORIGINAL CTWILL</h2>

 

 The present incarnation of ctwill and its utilities tries hard to be a drop-in replacement for the original package. There are, however, a few differences worth noting:
<dl>
<dt>&bull;
<dd> This version is based on the most recent version of CWEB (4.4).
<dt>&bull;
<dd> In TeX Live the utility programs are prefixed with ctwill- and the macro files with ct for technical reasons.
<dt>&bull;
<dd> Options --help, --quiet, --verbose, --version, and flags -c, -i, -o, and +lX are new in CWEBbin and TeX Live.
<dt>&bull;
<dd> Option +lX is accompanied by example wrapper files for ctwimac.tex and ctproofmac.tex with translated captions for German (+ld).
<dt>&bull;
<dd> Option +lX is also accompanied by an extended pdfctwimac.tex for production of PDF output with active hyperlinks (+lpdf).
<dt>&bull;
<dd> ctwill in TeX Live operates silently by default; use the --verbose option to get the original behavior.
<dt>&bull;
<dd> File lookup with the environment variable CWEBINPUTS is extended to permit several, colon-separated, paths; see ENVIRONMENT below.
<dt>&bull;
<dd> If properly configured, the main program ctwill is localized with the "GNU gettext utilities".</dl>

<h2>OPTIONS</h2>

 

 Options on the command line may be either turned off with `-' (if they are on by default) or turned on with `+' (if they are off by default). In fact, the options are processed from left to right, so a sequence like --verbose -h will only show the banner line (+b) and the progress report (+p), but leave out the happy message (-h).
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
<dd> +P: \input ctproofmac.tex instead of ctwimac.tex
<dt>&bull;
<dd> +lX/-lX: use macros for language X as of X{ctwimac|ctproofmac}.tex
<dt>&bull;
<dd> +s: print usage statistics
<dt>&bull;
<dd> +t: treat typename in a template like typedef
<dt>&bull;
<dd> --help: display help message and exit
<dt>&bull;
<dd> --version: output version information and exit</dl>

<h2>ENVIRONMENT</h2>

 

 The environment variable CWEBINPUTS is used to search for the input files, or the system default if CWEBINPUTS is not set. See <a HREF="/docs/linux/man/1-tex/">tex</a>(1) for the details of the searching. To avoid conflicts with other programs that also use the CWEBINPUTS environment, you can be more specific and use CWEBINPUTS_cweb for special requirements in CWEB. 

 If prepared for NLS support, ctwill like ctangle and cweave uses the environment variable TEXMFLOCALEDIR to configure the parent directory where the "GNU gettext utilities" search for translation catalogs. 

 These variables are preconfigured in TeX Live's texmf.cnf.

<h2>FILES</h2>

 

 The location of the files mentioned below varies from system to system. Use the kpsewhich utility to find their locations.
<dl>
<dt>&bull;
<dd> ctwimac.tex: The default TeX macros \input in the first line of the output file.
<dt>&bull;
<dd> ctproofmac.tex: If ctwill is invoked with the +P option, it will change the first line of the output file to \input ctproofmac.tex.</dl>
 

 In both cases you can request some prefix X with the +lX option, e.g., +ld will \input dctwimac.tex and +Pld will \input dctproofmac.tex. A special application is the use of option +lpdf that will \input pdfctwimac.tex for production of PDF output with active hyperlinks.
<dl>
<dt>&bull;
<dd> webfile.bux: Reference definitions to resolve from other modules.
<dt>&bull;
<dd> system.bux: Reference definitions to resolve from C/C++&nbsp;standard library header files like &lt;stdio.h&gt;.</dl>
 

 Other auxiliary files with references are created automatically by ctwill and the actual index files are created by TeX.
<dl>
<dt>&bull;
<dd> cwebman.tex: The CWEB user manual, available in PDF from CTAN (<a rel="nofollow" HREF="https://ctan.org/pkg/cweb">https://ctan.org/pkg/cweb</a>).</dl>

<h2>SEE ALSO</h2>

<dl>
<dt>&bull;
<dd> The CWEB System of Structured Documentation: by Donald E. Knuth and Silvio Levy (hardcopy version of cwebman.tex and the source code listings of common.w, ctangle.w, and cweave.w).
<dt>&bull;
<dd> Digital Typography: by D. E. Knuth.
<dt>&bull;
<dd> Literate Programming: by D. E. Knuth.
<dt>&bull;
<dd> Weaving a Program: by Wayne Sewell.</dl>
 

 <a HREF="/docs/linux/man/1-cweb/">cweb</a>(1), <a HREF="/docs/linux/man/1-tex/">tex</a>(1), <a HREF="/docs/linux/man/1-cc/">cc</a>(1)

<h2>AUTHORS</h2>

 

 Don Knuth wrote ctwill based on cweave by Silvio Levy and Knuth. 

 Contemporary development on <a rel="nofollow" HREF="https://github.com/ascherer/cwebbin.">https://github.com/ascherer/cwebbin.</a> 

<h2>Index</h2>


