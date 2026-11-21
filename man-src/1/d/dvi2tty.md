---

title: "dvi2tty(1)"
name: "dvi2tty"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dvi2tty/"
description: "dvi2tty – preview a TeX DVI file on an ordinary ASCII terminal"
---

<p> dvi2tty - preview a TeX DVI file on an ordinary ASCII terminal </p>
<h2>SYNOPSIS</h2>
<p> <code>dvi2tty</code> [ options ] dvifile  </p>
<h2>DESCRIPTION</h2>
<p> <i>dvi2tty</i> converts a TeX DVI file to a format that is appropriate for terminals and line printers. The program is intended to be used for preliminary proofreading of TeX-ed documents. By default the output is directed to the terminal, possibly through a pager (depending on how the program was installed), but it can be directed to a file or a pipe. </p>
<p> The output leaves much to be desired, but is still useful if you want to avoid walking to the laser printer (or whatever) for each iteration of your document. <br />
 Since <i>dvi2tty</i> produces output for terminals and line printers the representation of documents is naturally quite primitive. In principle font changes are totally ignored, but <i>dvi2tty</i> recognizes a few mathematical and special symbols that can be displayed on an ordinary ASCII terminal, such as the &#8216;+&#8216; and &#8216;-&#8216; symbol. </p>
<p> If the width of the output text requires more columns than fits in one line (cf. the -w option) it is broken into several lines by <i>dvi2tty</i> although they will be printed as one line on regular TeX output devices (e.g., laser printers). To show that a broken line is really just one logical line an asterisk (``*&#8216;&#8216;) in the last position means that the logical line is continued on the next physical line output by <i>dvi2tty.</i> Such a continuation line is started with a space and an asterisk in the first two columns. </p>
<p> Options may be specified in the environment variable DVI2TTY. Any option on the command line, conflicting with one in the environment, will override the one from the environment. </p>
<p> <code>Options:</code> </p>
<dl>
<dt><code>-o file</code></dt>
<dd> <p> Write output to file ``file&#8217;&#8216;. </p>
 </dd>
<dt><code>-p list</code></dt>
<dd> <p> Print the pages chosen by list. Numbers refer to TeX page numbers (known as \count0). An example of format for list is ``1,3:6,8&#8217;&#8216; to choose pages 1, 3 through 6 and 8. Negative numbers can be used exactly as in TeX, e.g., -1 comes before -4 as in ``-p-1:-4,17&#8217;&#8216;. </p>
 </dd>
<dt><code>-P list</code></dt>
<dd> <p> Like -p except that page numbers refer to the sequential ordering of the pages in the dvi-file. Negative numbers don&#8217;t make a lot of sense here... </p>
 </dd>
<dt><code>-w n</code></dt>
<dd> <p> Specify terminal width <i>n.</i> Valid range 16-132. Default is 80. If your terminal has the ability to display in 132 columns it might be a good idea to use -w132 and toggle the terminal into this mode as output will probably look somewhat better. </p>
 </dd>
<dt><code>-v</code></dt>
<dd> <p> Specify height of lines. Default value 450000. Allows one to adjust linespacing. </p>
 </dd>
<dt><code>-q</code></dt>
<dd> <p> Don&#8217;t pipe the output through a pager. This may be the default on some systems (depending on the whims of the person installing the program). </p>
 </dd>
<dt><code>-e n</code></dt>
<dd> <p> This option can be used to influence the spacing between words. With a negative value the number of spaces between words becomes less, with a positive value it becomes more. -e-11 seems to worked well. </p>
 </dd>
<dt><code>-f</code></dt>
<dd> <p> Pipe through a pager, $PAGER if defined, or whatever the installer of the program compiled in (often ``more&#8217;&#8216;). This may be the default, but it is still okay to redirect output with ``&gt;&#8216;&#8216;, the pager will not be used if output is not going to a terminal. </p>
 </dd>
<dt><code>-F</code></dt>
<dd> <p> Specify the pager program to be used. This overrides the $PAGER environment variable and the default pager. </p>
 </dd>
<dt><code>-Fprog</code></dt>
<dd> <p> Use ``prog&#8217;&#8216; as program to pipe output into. Can be used to choose an alternate pager (e.g., ``-Fless&#8217;&#8216;). </p>
 </dd>
<dt><code>-t</code></dt>
<dd> <p> \tt fonts were used (instead of cm) to produce the dvi file. </p>
 </dd>
<dt><code>-a</code></dt>
<dd> <p> Dvi2tty normally tries to output accented characters. With the -a option, accented characters are output without the accent sign. </p>
 </dd>
<dt><code>-l</code></dt>
<dd> <p> Mark page breaks with the two-character sequence ``^L&#8217;&#8216;. The default is to mark them with a form-feed character. </p>
 </dd>
<dt><code>-c</code></dt>
<dd> <p> Do not attempt to translate any characters (like the Scandinavian/latin1 mode) except when running in tt-font. </p>
 </dd>
<dt><code>-u</code></dt>
<dd> <p> Toggle option to process certain latin1 characters. Use this if your output devices supports latin1 characters. Note this may interfere with -s. Best not to use -u and -s together. </p>
 </dd>
<dt><code>-s</code></dt>
<dd> <p> Toggle option to process the special Scandinavian characters that on most (?) terminals in Scandinavia are mapped to ``{|}[\]&#8216;&#8216;. Note this may interfere with -u. Best not to use -u and -s together. </p>
 </dd>
<dt><code>-J</code></dt>
<dd> <p> Auto detect NTT JTeX, ASCII pTeX, and upTeX dvi format. </p>
 </dd>
<dt><code>-N</code></dt>
<dd> <p> Display NTT JTeX dvi. </p>
 </dd>
<dt><code>-A</code></dt>
<dd> <p> Display ASCII pTeX dvi. </p>
 </dd>
<dt><code>-U</code></dt>
<dd> <p> Display upTeX dvi. </p>
 </dd>
<dt><code>-Eenc</code></dt>
<dd> <p> Set output Japanese encoding. The enc argument &#8216;e&#8217;, &#8216;s&#8217;, &#8216;j&#8217;, and &#8216;u&#8217; denotes EUC-JP, Shift_JIS, ISO-2022-JP, and UTF-8, respectively. </p>
 </dd>
<dt><code>-bdelim</code></dt>
<dd> <p> Print the name of fonts when switching to it (and ending it). The delim argument is used to delimit the fontname. </p>
 </dd></dl>
<h2>FILES</h2>
<p> /bin/moreprobably the default pager.  </p>
<h2>ENVIRONMENT</h2>
<p> PAGERthe pager to use. <br />
 DVI2TTYcan be set to hold command-line options.  </p>
<h2>SEE ALSO</h2>
<p> TeX, dvi2ps  </p>
<h2>AUTHOR</h2>
<p> Original Pascal version: Svante Lindahl, Royal Institute of Technology, Stockholm <br />
 Improved C version: Marcel Mol, MESA Consulting <br />
 Now maintained at <a rel="nofollow" href="https://github.com/t-tk/dvi2tty/releases.">https://github.com/t-tk/dvi2tty/releases.</a>  </p>
<h2>BUGS</h2>
<p> Blanks between words get lost quite easily. This is less likely if you are using a wider output than the default 80. </p>
<p> Only one file may be specified on the command line. </p>
